The user is asking for the Markdown content of the "4 Components Reference" section. Based on the provided context, this section is part of the documentation for OpenTUI, likely found in a Markdown file within the `packages/web/src/content/docs` directory.

However, the exact Markdown content for a section titled "4 Components Reference" is not directly available in the provided code snippets. The "Getting Started" wiki page mentions a "Components Reference" as a "Next Step" . The `packages/react/README.md` and `packages/solid/README.md` files contain sections related to components, but they are not a comprehensive "Components Reference" section as implied by the prompt.

The `packages/web/src/layouts/Docs.astro` file shows a sidebar navigation with a "Components" section that links to individual component documentation pages like `/docs/components/text`, `/docs/components/box`, etc. . This suggests that the "Components Reference" might be a collection of individual component documentation pages rather than a single Markdown file.

Therefore, I cannot provide the full Markdown content for a single "4 Components Reference" section. I can, however, provide information about the available components and where their documentation might reside.

## Available Components

OpenTUI provides a variety of built-in components for building terminal user interfaces. These components are available across different development approaches (React, Solid.js, and Core Imperative API) .

### Layout & Display Components

*   `BoxRenderable` (JSX: `<box>`)  : A container component with borders, backgrounds, and layout capabilities .
*   `ScrollBoxRenderable` (JSX: `<scrollbox>`)  : A scrollable container .
*   `TextRenderable` (JSX: `<text>`)  : Used for displaying read-only styled text .
*   `ASCIIFontRenderable` (JSX: `<ascii-font>`)  : Displays ASCII art text with different font styles .
*   `MarkdownRenderable` (JSX: `<markdown>`) : Renders Markdown content .

### Input Components

*   `InputRenderable` (JSX: `<input>`)  : A single-line text input field .
*   `TextareaRenderable` (JSX: `<textarea>`)  : A multi-line text input field .
*   `SelectRenderable` (JSX: `<select>`)  : Provides a dropdown or list selection .
*   `TabSelectRenderable` (JSX: `<tab-select>`)  : A tab-based selection component .

### Code & Diff Components

*   `CodeRenderable` (JSX: `<code>`)  : Displays code blocks with syntax highlighting .
*   `LineNumberRenderable` (JSX: `<line-number>`)  : Displays code with line numbers, diff highlights, and diagnostics .
*   `DiffRenderable` (JSX: `<diff>`)  : Provides a unified or split diff viewer with syntax highlighting .

### Text Modifiers

These components are typically used inside a `<text>` component to apply specific styling :

*   `<span>`: Inline styled text .
*   `<strong>`, `<b>`: For bold text .
*   `<em>`, `<i>`: For italic text .
*   `<u>`: For underlined text .
*   `<br>`: For line breaks .
*   `<a>`: For link text with an `href` attribute .

## Component Extension

OpenTUI allows you to extend the component catalogue with custom renderables using the `extend()` function . This makes custom components available as JSX elements .

## Notes

The prompt asks for the "full Markdown content for section '4 Components Reference'". While a section with this title is mentioned in the "Getting Started" wiki page , the provided codebase snippets do not contain a single Markdown file with this exact content. Instead, the documentation seems to be structured with individual Markdown files for each component, as indicated by the sidebar links in `packages/web/src/layouts/Docs.astro` . The information provided above is a synthesis of component details found across various `README.md` files and the `Getting Started` wiki.

Wiki pages you might want to explore:
- [Getting Started (anomalyco/opentui)](/wiki/anomalyco/opentui#2)

View this search on DeepWiki: https://deepwiki.com/search/provide-the-full-markdown-cont_3aa7a8b8-0b6b-4a6b-b18f-2a89b4c3f15b
