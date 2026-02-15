
╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮
│ D ││ O ││ P ││ A ││ M ││ I ││ N ││ E │╰───╯
╰─┬─╯╰─┬─╯╰─┬─╯╰─┬─╯╰─┬─╯╰─┬─╯╰─┬─╯╰─┬─╯
  ⚡    ⚡    ⚡    ⚡    ⚡    ⚡    ⚡    ⚡
╭─┴─╮╭─┴─╮╭─┴─╮╭─┴─╮╭─┴─╮
│ B ││ E ││ N ││ C ││ H │
╰───╯╰───╯╰───╯╰───╯╰───╯

A benchmark for evaluating AI agents on terminal UI construction.

> **Status: Pretty much WIP**
> 
> This is a weekend project that works but is not finished. There's no actual evaluation logic yet, just the opencode based TUI generation harness.

## What

DopamineBench tests how well AI coding agents can build feature-rich, visually appealing TUIs using the OpenTUI framework. Agents are given a task and must produce a working terminal application with:

- Visual polish (colors, animations, layout)
- Interactive features (keyboard input, state management)
- Overall "juice" (satisfying feedback, delightful details)

## How

Uses a two-agent architecture:

1. **Builder Agent**: Receives the task prompt, writes the TUI code
2. **Investigator Agent**: Has full access to OpenTUI functionning via MCP, answers technical questions and debugs issues

The investigator agent is necessary because OpenTUI is too recent for most LLM knowledge cutoffs.


## Roadmap

- [ ] Implement "Ralph Wiggum loop" with screenshot-based validation
- [ ] Arena like voting ELO
- [ ] Maybe some tests?

## Structure

```
bench/          # Template project agents work from
opentui/        # On-the-fly OpenTUI documentation (MCP-accessible)
opencode-mcp/   # MCP server for investigator agent
docker-compose.yml  # Containerized environment
```

## Run

```bash
docker-compose up
```

## License

MIT
