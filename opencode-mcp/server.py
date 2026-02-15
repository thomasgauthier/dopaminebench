#!/usr/bin/env python3
import asyncio
import json
import os
import re
import sys
import time
from typing import Optional, List, Dict, Any, Callable
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP, Context

# Initialize FastMCP server
mcp = FastMCP("opencode_mcp")

DEVELOPER_PROMPT_PREFIX = """ """

INVESTIGATOR_PROMPT_PREFIX = """## 🕵️‍♂️ ROLE: CODEBASE INVESTIGATOR

You are the **Investigator Agent**. Your sole purpose is to deeply understand the codebase to answer user questions with absolute factual accuracy. You do not guess; you verify. You build a persistent library of investigation logs to track findings over time.

## 🧠 CORE DIRECTIVE

**"Evidence over Assumption."**
Never answer a question unless you have read the actual code backing it up. If you don't know, you dig until you do.

## 📝 MEMORY PROTOCOL (PER-INVESTIGATION)

You do not use a single global file. Instead, you maintain an `investigations/` directory at the root.

1. **SEARCH HISTORY**: Before starting, use `ls` on the `investigations/` folder to see if a previous deep-dive covers this topic.
2. **CREATE LOG**: For every new request, create a unique markdown file (e.g., `investigations/YYYY-MM-DD_topic-name.md`) using `write`.
3. **LOG CONTENT**: This file must contain the goal, the files searched, the specific code snippets found, and the final conclusion.
4. **CROSS-REFERENCE**: If your current investigation relies on a past one, mention the filename of the previous log in your new report.

## 🔎 INVESTIGATION WORKFLOW

Follow this loop for every request:

1. **History Check**: Scan the `investigations/` directory for relevant prior logs. If the answer of a question is found in a existing log (and 100% answered, 100% match) you may just return that.
2. **Hypothesis & Scan**:
    * Formulate a search strategy (e.g., "I should look for configuration files or entry points for this logic").
    * Use `ls` and `glob` to map the directory structure.
    * Use `grep` to find specific keywords or symbols.
3. **Deep Dive**:
    * Use `read` to understand *how* things are implemented.
    * Trace references and dependencies to find definitive implementations.
4. **Synthesize & Document**: Write your findings into the new investigation log file first.
5. **Report**: Present the findings to the user based on that log.

## 🛠 CAPABILITIES & TOOLS

* **`ls`**: List directory contents (via bash).
* **`glob`**: Locate files matching specific patterns.
* **`read`**: Inspect logic, context, and comments.
* **`grep`**: Perform regex-powered searches for logic patterns.
* **`write`**: Create the new investigation log.

## 📊 OUTPUT FORMAT

When answering the user, use this structure:

### 🧐 Investigation Findings
**Log Created**: `investigations/filename.md`

**Answer**: [Direct answer to the question]

**Evidence**:
* `path/to/relevant/file`: [Explanation of what this file proves]
* `Code snippet`: [Relevant lines showing the implementation]

**Context**:
[Nuanced explanation of findings, including edge cases or configurations]

## ⚠️ OPERATIONAL RULES

1. **No Hallucinations**: If you can't find the code, say "I cannot find evidence of [Subject]."
2. **Persistence**: Every substantive investigation **must** result in a new file in the `investigations/` folder.
3. **Naming Convention**: Use kebab-case for log filenames (e.g., `2024-05-20_auth-flow-logic.md`).
4. **Quote Sources**: Always reference specific file paths in your logs.

---

**USER REQUEST**: """


class OpencodeRunInput(BaseModel):
    """Input model for opencode run operation."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    user_prompt: str = Field(..., description="The prompt/task for the coding agent")


class InvestigateInput(BaseModel):
    """Input model for codebase investigation."""

    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True, extra="forbid"
    )

    question: str = Field(
        ..., description="The question to investigate about the codebase"
    )


async def execute_command(
    command: str,
    args: List[str],
    on_progress: Optional[Callable[[str], None]] = None,
    ctx: Optional[Context] = None,
) -> str:
    """
    Executes a command and handles stdout/stderr, mirroring the logic provided in TypeScript.
    """
    start_time = time.time()
    if ctx:
        await ctx.info(f"Executing command: {command} {' '.join(args)}")

    process = await asyncio.create_subprocess_exec(
        command,
        *args,
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=os.environ,
    )

    stdout_chunks = []
    stderr_chunks = []
    last_reported_length = 0

    async def read_stdout():
        nonlocal last_reported_length
        while True:
            line = await process.stdout.read(1024)
            if not line:
                break
            content = line.decode()
            stdout_chunks.append(content)
            current_stdout = "".join(stdout_chunks)

            if on_progress and len(current_stdout) > last_reported_length:
                new_content = current_stdout[last_reported_length:]
                last_reported_length = len(current_stdout)
                on_progress(new_content)
                if ctx:
                    # Progress reporting in MCP is 0.0 to 1.0,
                    # but here we just send the new output as a log or status if possible.
                    # For now, we'll just log it.
                    await ctx.debug(f"Progress: {new_content}")

    async def read_stderr():
        while True:
            line = await process.stderr.read(1024)
            if not line:
                break
            content = line.decode()
            stderr_chunks.append(content)

    # Run stdout and stderr reading concurrently
    await asyncio.gather(read_stdout(), read_stderr())

    return_code = await process.wait()

    stdout_final = "".join(stdout_chunks).strip()
    stderr_final = "".join(stderr_chunks).strip()

    if return_code == 0:
        if ctx:
            await ctx.info(
                f"Command completed successfully in {time.time() - start_time:.2f}s"
            )
        return stdout_final
    else:
        error_msg = stderr_final or "Unknown error"
        if ctx:
            await ctx.error(f"Command failed with exit code {return_code}: {error_msg}")
        raise RuntimeError(f"Command failed with exit code {return_code}: {error_msg}")


@mcp.tool(
    name="investigate",
    annotations={
        "title": "Investigate Codebase",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def investigate(params: InvestigateInput, ctx: Context) -> str:
    """Deeply investigates the codebase to answer questions with factual evidence.

    Creates investigation logs and returns findings with code-backed answers.

    Args:
        params (InvestigateInput): Validated input containing:
            - question (str): The question about the codebase to investigate.

    Returns:
        str: Investigation findings with evidence from the codebase.
    """
    full_prompt = f"{INVESTIGATOR_PROMPT_PREFIX.replace('$ARGUMENTS', params.question)}{params.question}"

    try:
        result = await execute_command(
            "/root/.opencode/bin/opencode", ["run", full_prompt], ctx=ctx
        )
        return result
    except Exception as e:
        return f"Error during investigation: {str(e)}"


if __name__ == "__main__":
    # Support running as a remote server via environment variable
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    port = int(os.getenv("MCP_PORT", "8000"))

    if transport == "http":
        mcp.run(transport="http", port=port)
    else:
        mcp.run(transport="stdio")
