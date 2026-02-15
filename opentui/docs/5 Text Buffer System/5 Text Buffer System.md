The user is asking for the content of a specific section, "5 Text Buffer System", from a Markdown document. Based on the provided context, this section is part of the `High-Level Architecture` wiki page .

Here is the full Markdown content for section '5 Text Buffer System':

```markdown
---

## 5 Text Buffer System

The `TextBuffer` (Zig) and its TypeScript wrapper `TextBuffer` manage and manipulate text content efficiently.

### UnifiedTextBuffer (Zig)

The core text buffer logic resides in the `UnifiedTextBuffer` struct in Zig.  It uses a rope data structure (`UnifiedRope`) for efficient text manipulation, especially for large files and frequent edits. 

Key features:
- **Rope Data Structure**: `UnifiedRope` handles text storage and modifications. 
- **Memory Registry**: `MemRegistry` manages memory buffers, allowing text to be registered and retrieved by an ID. 
- **Styled Text**: Supports `StyledChunk`s for rich text with foreground/background colors and attributes. 
- **Syntax Highlighting**: Integrates with `SyntaxStyle` for dynamic highlighting. 
- **Line Information**: Tracks line breaks and line start positions for efficient line-based operations. 
- **Grapheme Pool**: Uses a `GraphemePool` for correct handling of Unicode grapheme clusters. 

### TextBuffer (TypeScript)

The `TextBuffer` class in TypeScript is a wrapper around the native Zig `UnifiedTextBuffer`.  It provides a high-level API for interacting with the text buffer via FFI. 

Key methods:
- `static create(widthMethod: WidthMethod)`: Creates a new `TextBuffer` instance. 
- `setText(text: string)`: Sets the entire content of the buffer. 
- `append(text: string)`: Appends text to the end of the buffer. 
- `loadFile(path: string)`: Loads content from a file into the buffer. 
- `setStyledText(text: StyledText)`: Sets text with styling information (colors, attributes, links). 

The TypeScript `TextBuffer` manages the lifecycle of the native Zig buffer, including memory registration and replacement for efficient updates.  It also handles encoding text to `Uint8Array` for FFI calls. 

### Interaction with Renderer

`TextBuffer` instances are used by `TextBufferRenderable` and `EditBufferRenderable` components to display and edit text. The `OptimizedBuffer` in Zig can draw content from a `TextBufferView` (a view into the `UnifiedTextBuffer`) to the screen. 

**Sources:** , , 
```

Wiki pages you might want to explore:
- [High-Level Architecture (anomalyco/opentui)](/wiki/anomalyco/opentui#1.2)

View this search on DeepWiki: https://deepwiki.com/search/provide-the-full-markdown-cont_707517d3-301a-4346-923e-db5813d97433
