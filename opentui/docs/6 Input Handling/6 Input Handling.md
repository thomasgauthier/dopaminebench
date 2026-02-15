The user is asking for the content of a section titled "6 Input Handling". Based on the provided context, this section is likely part of a documentation or wiki page related to the `anomalyco/opentui` repository. However, the provided codebase context does not contain a section explicitly named "6 Input Handling" with full Markdown content. The closest relevant information is found in the wiki page "Input Components"  which details how input is handled by various components.

Therefore, I will provide a summary of input handling based on the "Input Components" wiki page.

## Input Handling in OpenTUI

OpenTUI provides several interactive input components for capturing user data entry, managing keyboard input, cursor, text editing, and selection . These components include `InputRenderable`, `TextareaRenderable`, `SelectRenderable`, and `TabSelectRenderable` . All input components extend from the core `Renderable` class and integrate with OpenTUI's focus management system, ensuring that only the focused component receives keyboard input .

### InputRenderable: Single-Line Text Input

The `InputRenderable` component is designed for single-line text input . It extends `TextareaRenderable` and enforces single-line constraints such as a height of 1, no newlines, and stripping newlines from pasted text .

#### Key Features
*   **Constraints**: Enforces single-line input, disallowing newlines .
*   **Events**: Emits `INPUT` on every keystroke, `CHANGE` on blur or enter (if value changed), and `ENTER` on Enter key press .
*   **Validation**: Supports `maxLength` and sanitization .
*   **Methods**: Overrides `newLine()` to prevent newlines, `handlePaste()` to strip newlines, and `insertText()` to enforce `maxLength` .

### TextareaRenderable: Multi-Line Text Editor

The `TextareaRenderable` component provides a multi-line text editor with customizable key bindings, undo/redo, cursor management, and text selection . It serves as the base for `InputRenderable` .

#### Key Binding System
`TextareaRenderable` uses a key binding system that supports default keybindings (Emacs-style and standard), custom keybindings, key aliases, and modifier keys . Actions like `move-left`, `insert`, `undo`, and `redo` are available . Key events are processed by looking up actions in a `keyBindingsMap` and executing corresponding action handlers .

#### Text Editing Operations
Core methods include `insertChar()`, `insertText()`, `deleteChar()`, `deleteCharBackward()`, `newLine()`, `deleteLine()`, `deleteToLineEnd()`, and `deleteToLineStart()` .

#### Cursor Movement
Navigation methods like `moveCursorLeft()`, `moveCursorRight()`, `moveCursorUp()`, `moveCursorDown()`, `gotoLineHome()`, `gotoLineEnd()`, `gotoVisualLineHome()`, `gotoVisualLineEnd()`, `gotoBufferHome()`, `gotoBufferEnd()`, and `gotoLine()` are available, all supporting an optional `select` parameter to extend selection .

#### Undo/Redo System
Undo/redo functionality is provided by the underlying native Zig `EditBuffer` .

#### Selection Management
Text selection is integrated with OpenTUI's global selection system, allowing for `updateSelectionForMovement()`, `hasSelection()`, `getSelection()`, `getSelectedText()`, `deleteSelectedText()`, and `selectAll()` .

### SelectRenderable: List Selection

`SelectRenderable` provides a scrollable list of options with keyboard navigation .

#### Key Bindings
Default key bindings include Up/K for `move-up`, Down/J for `move-down`, Shift+Up/Down for fast scrolling, and Return/Linefeed for `select-current` .

#### Events
It emits `SELECTION_CHANGED` when the selected index changes and `ITEM_SELECTED` when the user confirms a selection (e.g., by pressing Enter) .

### TabSelectRenderable: Horizontal Tab Selection

`TabSelectRenderable` offers a horizontal tab-based selection interface .

#### Key Bindings
Default key bindings include Left/[ for `move-left`, Right/] for `move-right`, and Return/Linefeed for `select-current` .

#### Events
Similar to `SelectRenderable`, it emits `SELECTION_CHANGED` and `ITEM_SELECTED` events .

### Common Patterns and Integration

All input components share common patterns for focus management, custom key bindings, event handling, programmatic control, and color theming .

*   **Focus Management**: Components can be focused and blurred using `component.focus()` and `component.blur()`, and their focus state can be checked with `component.focused` .
*   **Custom Key Bindings**: Custom key bindings can be provided via options, which are merged with default bindings, with custom ones taking precedence .
*   **Event Handling**: Components emit events like `INPUT`, `CHANGE`, and `ENTER` which can be listened to using `component.on()` .
*   **Programmatic Control**: Components allow programmatic manipulation of their state, such as setting `input.value`, `textarea.cursorOffset`, or `select.setSelectedIndex()` .
*   **Color Theming**: Components support separate colors for focused and unfocused states, including `backgroundColor`, `textColor`, `focusedBackgroundColor`, `focusedTextColor`, and `placeholderColor` .

## Notes

The user's prompt specifically asked for "section '6 Input Handling'". While the provided context does not contain a document with this exact section title, the "Input Components" wiki page  is highly relevant as it describes how input is handled across various components in OpenTUI. The answer summarizes the key aspects of input handling as described in this wiki page.

Wiki pages you might want to explore:
- [Input Components (anomalyco/opentui)](/wiki/anomalyco/opentui#4.3)

View this search on DeepWiki: https://deepwiki.com/search/provide-the-full-markdown-cont_dbed5112-b823-48a0-88ff-b2cae623a5e5
