# Combined Documentation for editorjs
<!-- Source .knowledge file: editorjs/.knowledge -->
<!-- GitHub API Roots: https://api.github.com/repos/editor-js/image/contents/, https://api.github.com/repos/codex-team/editor.js/contents/docs/ -->



---

<!-- Source: README.md -->

---

![](https://badgen.net/badge/Editor.js/v2.0/blue)

# Image Tool

Image Block for the [Editor.js](https://editorjs.io).

![](https://capella.pics/63a03d04-3816-45b2-87b2-d85e556f0066.jpg)

## Features

- Uploading file from the device
- Pasting copied content from the web
- Pasting images by drag-n-drop
- Pasting files and screenshots from Clipboard
- Allows adding a border, a background and a caption
- Allows stretching an image to the container's full-width

**Notes**

This Tool requires server-side implementation for the file uploading. See [backend response format](#server-format) for more details.

This Tool is also capable of uploading & displaying video files using the `<video>` element. To enable this, specify video mime-types via the 'types' config param.


## Installation

Get the package

```shell
yarn add @editorjs/image
```

Include module at your application

```javascript
import ImageTool from '@editorjs/image';
```

Optionally, you can load this tool from [JsDelivr CDN](https://cdn.jsdelivr.net/npm/@editorjs/image@latest)

## Usage

Add a new Tool to the `tools` property of the Editor.js initial config.

```javascript
import ImageTool from '@editorjs/image';

// or if you inject ImageTool via standalone script
const ImageTool = window.ImageTool;

var editor = EditorJS({
  ...

  tools: {
    ...
    image: {
      class: ImageTool,
      config: {
        endpoints: {
          byFile: 'http://localhost:8008/uploadFile', // Your backend file uploader endpoint
          byUrl: 'http://localhost:8008/fetchUrl', // Your endpoint that provides uploading by Url
        }
      }
    }
  }

  ...
});
```

## Config Params

Image Tool supports these configuration parameters:

| Field | Type     | Description        |
| ----- | -------- | ------------------ |
| endpoints | `{byFile: string, byUrl: string}` | Endpoints for file uploading. <br> Contains 2 fields: <br> __byFile__ - for file uploading <br> __byUrl__ - for uploading by URL |
| field | `string` | (default: `image`) Name of uploaded image field in POST request |
| types | `string` | (default: `image/*`) Mime-types of files that can be [accepted with file selection](https://github.com/codex-team/ajax#accept-string).|
| additionalRequestData | `object` | Object with any data you want to send with uploading requests |
| additionalRequestHeaders | `object` | Object with any custom headers which will be added to request. [See example](https://github.com/codex-team/ajax/blob/e5bc2a2391a18574c88b7ecd6508c29974c3e27f/README.md#headers-object) |
| captionPlaceholder | `string` | (default: `Caption`) Placeholder for Caption input |
| buttonContent | `string` | Allows to override HTML content of «Select file» button |
| uploader | `{{uploadByFile: function, uploadByUrl: function}}` | Optional custom uploading methods. See details below. |
| actions | `array` | Array with custom actions to show in the tool's settings menu. See details below. |
| features | `object` | Allows you to enable/disable additional features such as border, background tunes and caption. See details below. |

Note that if you don't implement your custom uploader methods, the `endpoints` param is required.

## Tool's settings

![](https://capella.pics/c74cdeec-3405-48ac-a960-f784188cf9b4.jpg)

1. Add border

2. Stretch to full-width

3. Add background

4. Add caption

Add extra setting-buttons by adding them to the `actions`-array in the configuration:
```js
actions: [
    {
        name: 'new_button',
        icon: '<svg>...</svg>',
        title: 'New Button',
        toggle: true,
        action: (name) => {
            alert(`${name} button clicked`);
        }
    }
]
```

**_NOTE:_**  return value of `action` callback for settings whether action button should be toggled or not is *deprecated*. Consider using `toggle` option instead.

You can disable features such as border, background tunes and caption by defining `features` in the configuration:
```js
features: {
  border: false,
  caption: 'optional',
  stretch: false
}
```

**_NOTE:_** set caption to `optional` in order to configure caption as a tune.

## Output data

This Tool returns `data` with following format

| Field          | Type      | Description                     |
| -------------- | --------- | ------------------------------- |
| file           | `object`  | Uploaded file data. Any data got from backend uploader. Always contain the `url` property |
| caption        | `string`  | image's caption                 |
| withBorder     | `boolean` | add border to image             |
| withBackground | `boolean` | need to add background          |
| stretched      | `boolean` | stretch image to screen's width |


```json
{
    "type" : "image",
    "data" : {
        "file": {
            "url" : "https://www.tesla.com/tesla_theme/assets/img/_vehicle_redesign/roadster_and_semi/roadster/hero.jpg"
        },
        "caption" : "Roadster // tesla.com",
        "withBorder" : false,
        "withBackground" : false,
        "stretched" : true,
    }
}
```

## Backend response format <a name="server-format"></a>

This Tool works by one of the following schemes:

1. Uploading files from the device
2. Uploading by URL (handle image-like URL's pasting)
3. Uploading by drag-n-drop file
4. Uploading by pasting from Clipboard

### Uploading files from device <a name="from-device"></a>

Scenario:

1. User select file from the device
2. Tool sends it to **your** backend (on `config.endpoints.byFile` route)
3. Your backend should save file and return file data with JSON at specified format.
4. Image tool shows saved image and stores server answer

So, you can implement backend for file saving by your own way. It is a specific and trivial task depending on your
environment and stack.

The tool executes the request as [`multipart/form-data`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST), with the key as the value of `field`  in configuration.

The response of your uploader **should**  cover the following format:

```json5
{
    "success" : 1,
    "file": {
        "url" : "https://www.tesla.com/tesla_theme/assets/img/_vehicle_redesign/roadster_and_semi/roadster/hero.jpg",
        // ... and any additional fields you want to store, such as width, height, color, extension, etc
    }
}
```

**success** - uploading status. 1 for successful, 0 for failed

**file** - uploaded file data. **Must** contain an `url` field with full public path to the uploaded image.
Also, can contain any additional fields you want to store. For example, width, height, id etc.
All additional fields will be saved at the `file` object of output data.

### Uploading by pasted URL

Scenario:

1. User pastes an URL of the image file to the Editor
2. Editor pass pasted string to the Image Tool
3. Tool sends it to **your** backend (on `config.endpoints.byUrl` route) via 'url' in request body
4. Your backend should accept URL, **download and save the original file by passed URL** and return file data with JSON at specified format.
5. Image tool shows saved image and stores server answer

The tool executes the request as `application/json` with the following request body:

```json5
{
  "url": "<pasted URL from the user>"
  "additionalRequestData": "<additional request data from configuration>"
}
```

Response of your uploader should be at the same format as described at «[Uploading files from device](#from-device)» section


### Uploading by drag-n-drop or from Clipboard

Your backend will accept file as FormData object in field name, specified by `config.field` (by default, «`image`»).
You should save it and return the same response format as described above.

## Providing custom uploading methods

As mentioned at the Config Params section, you have an ability to provide own custom uploading methods.
It is a quite simple: implement `uploadByFile` and `uploadByUrl` methods and pass them via `uploader` config param.
Both methods must return a Promise that resolves with response in a format that described at the [backend response format](#server-format) section.


| Method         | Arguments | Return value | Description |
| -------------- | --------- | -------------| ------------|
| uploadByFile   | `File`    | `{Promise.<{success, file: {url}}>}` | Upload file to the server and return an uploaded image data |
| uploadByUrl    | `string`  | `{Promise.<{success, file: {url}}>}` | Send URL-string to the server, that should load image by this URL and return an uploaded image data |

Example:

```js
import ImageTool from '@editorjs/image';

var editor = EditorJS({
  ...

  tools: {
    ...
    image: {
      class: ImageTool,
      config: {
        /**
         * Custom uploader
         */
        uploader: {
          /**
           * Upload file to the server and return an uploaded image data
           * @param {File} file - file selected from the device or pasted by drag-n-drop
           * @return {Promise.<{success, file: {url}}>}
           */
          uploadByFile(file){
            // your own uploading logic here
            return MyAjax.upload(file).then(() => {
              return {
                success: 1,
                file: {
                  url: 'https://codex.so/upload/redactor_images/o_80beea670e49f04931ce9e3b2122ac70.jpg',
                  // any other image data you want to store, such as width, height, color, extension, etc
                }
              };
            });
          },

          /**
           * Send URL-string to the server. Backend should load image by this URL and return an uploaded image data
           * @param {string} url - pasted image URL
           * @return {Promise.<{success, file: {url}}>}
           */
          uploadByUrl(url){
            // your ajax request for uploading
            return MyAjax.upload(file).then(() => {
              return {
                success: 1,
                file: {
                  url: 'https://codex.so/upload/redactor_images/o_e48549d1855c7fc1807308dd14990126.jpg',,
                  // any other image data you want to store, such as width, height, color, extension, etc
                }
              }
            })
          }
        }
      }
    }
  }

  ...
});
```


---

<!-- Source: docs/CHANGELOG.md -->

---

# Changelog

### 2.31.0

- `New` - Inline tools (those with `isReadOnlySupported` specified) can now be used in read-only mode
- `New` - Inline tools (those with `isReadOnlySupported` specified) shortcuts now work in read-only mode
- `Improvement` - Block manager passes target tool config to the `conversionConfig.import` method on conversion
- `Fix` - Fix selection of first block in read-only initialization with "autofocus=true"
- `Fix` - Incorrect caret position after blocks merging in Safari
- `Fix` - Several toolbox items exported by the one tool have the same shortcut displayed in toolbox
- `Improvement` - The current block reference will be updated in read-only mode when blocks are clicked
- `Fix` - codex-notifier and codex-tooltip moved from devDependencies to dependencies in package.json to solve type errors
- `Fix` - Handle whitespace input in empty placeholder elements to prevent caret from moving unexpectedly to the end of the placeholder
- `Fix` - Fix the memory leak issue in `Shortcuts` class
- `Fix` - Fix when / overides selected text outside of the editor
- `DX` - Tools submodules removed from the repository
- `Improvement` - Shift + Down/Up will allow to select next/previous line instead of Inline Toolbar flipping
- `Improvement` - The API `caret.setToBlock()` offset now works across the entire block content, not just the first or last node.

### 2.30.7

- `Fix` - Link insertion in Safari fixed

### 2.30.6

- `Fix` – Fix the display of ‘Convert To’ near blocks that do not have the ‘conversionConfig.export’ rule specified
- `Fix` – The Plus button does not appear when the editor is loaded in an iframe in Chrome
- `Fix` - Prevent inline toolbar from closing in nested instance of editor

### 2.30.5

– `Fix` – Fix exported types

### 2.30.4

- `Fix` - Tool's exporting types added

### 2.30.3

- `Fix` – I18n in nested popover

### 2.30.2

- `Fix` – The onChange callback won't be fired when editor is initialized in the Read-Only mode
- `Fix` – Convert To supports i18n again
- `Fix` – Prevent form submit on inline tool click

### 2.30.1

- `Fix` – Remove fake selection after multiple "convert to" inline tool toggles

### 2.30.0

- `New` – Block Tunes now supports nesting items
- `New` – Block Tunes now supports separator items
- `New` – *Menu Config* – New item type – HTML
- `New` – *Menu Config* – Default and HTML items now support hints
- `New` – Inline Toolbar has new look 💅
- `New` – Inline Tool's `render()` now supports [Menu Config](https://editorjs.io/menu-config/) format
- `New` – *ToolsAPI* – All installed block tools now accessible via ToolsAPI `getBlockTools()` method
- `New` – *SelectionAPI* – Exposed methods `save()` and `restore()` that allow to save selection to be able to temporally move focus away, methods `setFakeBackground()` and `removeFakeBackground()` that allow to immitate selection while focus moved away
- `New` – *BlocksAPI* – Exposed `getBlockByElement()` method that helps find block by any child html element
- `New` – "Convert to" control is now also available in Block Tunes
- `New` — Editor.js now supports contenteditable placeholders out of the box. Just add `data-placeholder` or `data-placeholder-active` attribute to make it work. The first one will work like native placeholder while the second one will show placeholder only when block is current.
- `Improvement` — Now Paragraph placeholder will be shown for the current paragraph, not only the first one.
- `Improvement` - The API `blocks.update` now accepts `tunes` data as optional third argument and makes `data` - block data as optional.
- `Improvement` — The ability to merge blocks of different types (if both tools provide the conversionConfig)
- `Improvement` - The API `blocks.convert()` now returns the new block API
- `Improvement` - The API `caret.setToBlock()` now can accept either BlockAPI or block index or block id
- `Improvement` – *MenuConfig* – `TunesMenuConfig` type is deprecated, use the `MenuConfig` instead
– `Improvement` — *Types* — `BlockToolConstructorOptions` type improved, `block` and `config` are not optional anymore
- `Improvement` - The Plus button and Block Tunes toggler are now better aligned with large line-height blocks, such as Headings
- `Improvement` — Creating links on Android devices: now the mobile keyboard will have an "Enter" key for accepting the inserted link.
- `Improvement` — Placeholders will stay visible on inputs focus.
– `Refactoring` – Switched to Vite as Cypress bundler
- `Fix` — `onChange` will be called when removing the entire text within a descendant element of a block.
- `Fix` - Unexpected new line on Enter press with selected block without caret
- `Fix` - Search input autofocus loosing after Block Tunes opening
- `Fix` - Block removing while Enter press on Block Tunes
- `Fix` – Unwanted scroll on first typing on iOS devices
- `Fix` - Unwanted soft line break on Enter press after period and space (". |") on iOS devices
- `Fix` - Caret lost after block conversion on mobile devices.
- `Fix` - Caret lost after Backspace at the start of block when previoius block is not convertable
– `Fix` — Deleting whitespaces at the start/end of the block
- `Fix` — The problem caused by missed "import type" in block mutation event types resolved

### 2.29.1

- `Fix` — Toolbox wont be shown when Slash pressed with along with Shift or Alt
- `Fix` — Toolbox will be opened when Slash pressed in non-US keyboard layout where there is no physical '/' key.

### 2.29.0

- `New` — Editor Config now has the `style.nonce` attribute that could be used to allowlist editor style tag for Content Security Policy "style-src"
- `New` — Toolbox now will be opened by '/' in empty Block instead of Tab
- `New` — Block Tunes now will be opened by 'CMD+/' instead of Tab in non-empty block
- `New` — Tab now will navigate through Blocks. In last block Tab will navigate to the next input on page.
- `Fix` — Passing an empty array via initial data or `blocks.render()` won't break the editor
- `Fix` — Layout did not shrink when a large document cleared in Chrome
- `Fix` — Multiple Tooltip elements creation fixed
- `Fix` — When the focusing Block is out of the viewport, the page will be scrolled.
- `Fix` - Compiler error "This import is never used as a value and must use 'import type'..." fixed
- `Fix` — `blocks.render()` won't lead the `onChange` call in Safari
- `Fix` — Editor wrapper element growing on the Inline Toolbar close
- `Fix` — Fix errors thrown by clicks on a document when the editor is being initialized
- `Fix` — Caret losing on Mobile Devices when adding a block via Toolbox or via Backspace at the beginning of a Block
- `Improvement` — Now you can set focus via arrows/Tab to "contentless" (decorative) blocks like Delimiter which have no inputs.
- `Improvement` — Inline Toolbar sometimes opened in an incorrect position. Now it will be aligned by the left side of the selected text. And won't overflow the right side of the text column.
- `Improvement` - Now the `data-mutation-free` supports deep nesting, so you can mark some element with it to prevent the onChange call caused by child element mutating
- `Improvement` - Now the `data-mutation-free` also allows to skip "characterData" mutations (eg. text content change)
- `Refactoring` — `ce-block--focused` class toggling removed as unused.

### 2.28.2

- `Fix` — Get rid of redundant logs from the build

### 2.28.1

- `Fix` — Some Block were be skipped on saving after pasting them as HTML

### 2.28.0

- `New` - Block ids now displayed in DOM via a data-id attribute. Could be useful for plugins that want to access a Block's element by id.
- `New` - The `blocks.convert(blockId, newType)` API method was added. It allows to convert existing Block to a Block of another type.
- `New` - The `blocks.insertMany()` API method added. It allows to insert several Blocks to the specified index.
- `Improvement` - The Delete keydown at the end of the Block will now work opposite a Backspace at the start. Next Block will be removed (if empty) or merged with the current one.
- `Improvement` - The Delete keydown will work like a Backspace when several Blocks are selected.
- `Improvement` - If we have two empty Blocks, and press Backspace at the start of the second one, the previous will be removed instead of the current.
- `Improvement` - Tools shortcuts could be used to convert one Block to another.
- `Improvement` - Tools shortcuts displayed in the Conversion Toolbar
- `Improvement` - Initialization Loader has been removed.
- `Improvement` - Selection style won't override your custom style for `::selection` outside the editor.
- `Improvement` - Performance optimizations: initialization speed increased, `blocks.render()` API method optimized. Big documents will be displayed faster.
- `Improvement` - "Editor saving" log removed
- `Improvement` - "I'm ready" log removed
- `Improvement` - The stub-block style is simplified.
- `Improvement` - If some Block's tool throws an error during construction, we will show Stub block instead of skipping it during render
- `Improvement` - Call of `blocks.clear()` now will trigger onChange with "block-removed" event for all removed blocks.
- `Improvement` - The `blocks.clear()` now can be awaited.
- `Improvement` - `BlockMutationType` and `BlockMutationEvent` types exported
- `Improvement` - `blocks.update(id, data)` now can accept partial data object — it will update only passed properties, others will remain the same.
- `Improvement` - `blocks.update(id, data)` now will trigger onChange with only `block-change` event.
- `Improvement` - `blocks.update(id, data)` will return a promise with BlockAPI object of the changed block.


### 2.27.2

- `Fix` - `onChange` won't be called when element with data-mutation-free changes some attribute

### 2.27.1

- `Fix` - `onChange` will be called on removing the whole text in a block

### 2.27.0

- `New` — *Toolbar API* — Added a new method for toggling the toolbox.
- `New` — Added types for block mutation events
- `New` — Batching added to the `onChange` callback. Now the second argument can contain an array of CustomEvents as well as a single one. Multiple changes made in a short period of time will be batched under a single `onChange` call.
- `Improvement` — *Toolbox* — Number of `close()` method calls optimized.
- `Improvement` — The `onChange` callback can be muted if all mutations contain nodes with the `data-mutation-free` attribute.
- `Improvement` — Pressing "Enter" at the end of a Block won't lead to redundant `block-changed` event triggering. Only `block-added` event will be dispatched.
- `Improvement` — The block mutation handler is now called on every block change (including background changes), instead of only when a block is focused
- `Improvement` — Number of caret saving method calls optimized for Block Tunes opening/closing.
- `Improvement` — Package size reduced by removing redundant files.
- `Refactoring` — Switched from Webpack to Vite as the build system.
- `Refactoring` — *Dependencies* — Upgraded Cypress to v12 and related libraries to the latest versions.
- `Refactoring` — *Dependencies* — Upgraded TypeScript to v5.
- `Refactoring` — `EventDispatcher` types improved. Now we can pass `EventsMap` via generic to specify a map of event names and their payloads that can be used in a particular EventDispatcher instance.
- `Refactoring` — All events in common editor Event Bus now have own type declarations.
- `Refactoring` — Removed the block mutation observer from blocks and attached a single observer to the editor's blocks wrapper element.
- `Refactoring` — Removed the debounce from the block mutation handler and used batching instead.
- `Refactoring` — Refactored the popover class for better performance and maintenance.
- `Fix` — The `onChange` callback won't trigger when block tunes are opened or closed.
- `Fix` — Resolved a compiler error caused by importing the `BlockToolData` type.
- `Fix` — Resolved a problem where the document would scroll to the beginning after moving a block above the viewport.
- `Fix`- Fixed several bugs caused by browser extensions — Removed the search for a block's container in the DOM on saving and kept it in memory instead, updating it when the tool changes a container element.
- `Fix` — *ToolsAPI* — `pasteConfig` getter with `false` value could be used to disable paste handling by Editor.js core. Could be useful if your tool has its own paste handler.
- `CI` — Ubuntu container is now used for Edge tests runner.
- `CI` — Node 16 is used for GitHib Actions.

### 2.26.5

- `Fix` — *Types* — Remove unnecessary import that creates a dependency on the `cypress`.

### 2.26.4

- `Improvement` — *Menu Config* — Property `label` renamed to `title`.

### 2.26.3

- `Fix` — *Paste Module* — fix for a problem with specifying of `pasteConfig().tags` in upper case  [#2208](https://github.com/codex-team/editor.js/issues/2208).

### 2.26.2

- `Fix` — *Menu Config* — Installed tunes are rendered above default tunes again.

### 2.26.1

- `Improvement` — *Menu Config* — Now it becomes possible to create toggle groups.

### 2.26.0

- `New` — *UI* — Block Tunes became vertical just like the Toolbox 🤩
- `New` — *Block Tunes API* — Now `render()` method of a Block Tune can return config with just icon, label and callback instead of custom HTML. This improvement is a key to the new straightforward way of configuring tune's appearance in Block Tunes menu.
- `New` — *Tools API* — As well as `render()` in `Tunes API`, Tool's `renderSettings()` now also supports new configuration format.
- `New` — *UI* — Meet the new icons from [CodeX Icons](https://github.com/codex-team/icons) pack 🛍 💝
- `New` — *BlocksAPI* — the `blocks.insert()` method now also have the optional `id` param. If passed, this id will be used instead of the generated one.
- `Deprecated` — *Styles API* — CSS classes `.cdx-settings-button` and `.cdx-settings-button--active` are not recommended to use. Consider configuring your block settings with new JSON API instead.
- `Fix` — Wrong element not highlighted anymore when popover opened.
- `Fix` — When Tunes Menu open keydown events can not be handled inside plugins.
- `Fix` — If a Tool specifies some tags to substitute on paste, all attributes of that tags will be removed before passing them to the tool. Possible XSS vulnerability fixed.
- `Fix` — Pasting from Microsoft Word to Chrome (Mac OS) fixed. Now if there are no image-tools connected, regular text content will be pasted.
- `Fix` — Workaround for the HTMLJanitor bug with Tables (https://github.com/guardian/html-janitor/issues/3) added
- `Fix` — Toolbox shortcuts appearance and execution fixed [#2112](https://github.com/codex-team/editor.js/issues/2112)
- `Fix` — Inline Tools click handling on mobile devices improved
- `Improvement` — *Tools API* — `pasteConfig().tags` now support sanitizing configuration. It allows you to leave some explicitly specified attributes for pasted content.
- `Improvement` — *CodeStyle* — [CodeX ESLint Config](https://github.com/codex-team/eslint-config) has bee updated. All ESLint/Spelling issues resolved
- `Improvement` — *ToolsAPI* — The `icon` property of the `toolbox` getter became optional.


### 2.25.0

- `New` — *Tools API* — Introducing new feature — toolbox now can have multiple entries for one tool! <br>
Due to that API changes: tool's `toolbox` getter now can return either a single config item or an array of config items
- `New` — *Blocks API* — `composeBlockData()` method was added.

### 2.24.4

- `Fix` — Keyboard selection by word [#2045](https://github.com/codex-team/editor.js/issues/2045)

### 2.24.3

- `Fix` — Issue with toolbox preventing text selection fixed

### 2.24.2

- `Fix` — Scrolling issue when opening toolbox on mobile fixed
- `Fix` — Typo in toolbox empty placeholder fixed
- `Fix` — The issue with scroll jumping on block hovering have fixed [2036](https://github.com/codex-team/editor.js/issues/2036)
- `Improvement` — *Dev Example Page* - Add popup example page
- `Improvement` — *UI* - The Toolbox will restore the internal scroll on every opening

### 2.24.1

— `Fix` — The I18n of Tools` titles at the Toolbox now works correctly [#2030](https://github.com/codex-team/editor.js/issues/2030)

### 2.24.0

- `New` — *UI* — The Toolbox became vertical 🥳
- `Improvement` — *UI* — the Plus button will always be shown (previously, it appears only for empty blocks)
- `Improvement` — *Dev Example Page* - Server added to allow opening example page on other devices in network.
- `Fix` — `UI` — the Toolbar won't move on hover at mobile viewports. Resolves [#1972](https://github.com/codex-team/editor.js/issues/1972)
- `Fix` — `OnChange` event invocation after block insertion. [#1997](https://github.com/codex-team/editor.js/issues/1997)
- `Fix` — `ReadOnly` — the `readonly.isEnabled` API getter now works correctly after `readonly.toggle()` calling. Resolves [#1822](https://github.com/codex-team/editor.js/issues/1822)
- `Fix` — `Paste` — the inline HTML tags now will be preserved on pasting. [#1686](https://github.com/codex-team/editor.js/pull/1686)

### 2.23.2

— `Fix` — Crash on initialization in the read-only mode [#1968](https://github.com/codex-team/editor.js/issues/1968)

### 2.23.1

— `Fix` — Incorrect release tag fixed

### 2.23.0

- `Improvement` — *EditorConfig* — The `onChange` callback now accepts two arguments: EditorJS API and the CustomEvent with `type` and `detail` allowing to determine what happened with a Block
- `New` — *Block API* — The new `dispatchChange()` method allows to manually trigger the 'onChange' callback. Useful when Tool made a state mutation that is invisible for editor core.
- `Improvement` — *UI* — Block Tunes toggler moved to the left
- `Improvement` — *UI* — Block Actions (BT toggler + Plus Button) will appear on block hovering instead of click
- `Improvement` — *UI* — Block Tunes toggler icon and Plus button icon updated
- `Improvement` — *Dev Example Page* — The menu with helpful buttons added to the bottom of the screen
- `Improvement` — *Dev Example Page* — The 'dark' theme added. Now we can code at night more comfortably.
- `Improvement` — *Rectangle Selection* — paint optimized
- `Fix` — *Rectangle Selection* — the first click after RS was not clear selection state. Now does.
- `Improvement` — *Blocks API* — toolbar moving logic removed from `blocks.move()` and `blocks.swap()` methods. Instead, you should use Toolbar API (it was used by MoveUp and MoveDown tunes, they were updated).
- `New` — *Blocks API* — The `getBlockIndex()` method added
- `New` — *Blocks API* — the `insert()` method now has the `replace: boolean` parameter
- `New` — *Blocks API* —  the `insert()` method now returns the inserted `Block API`
- `New` — *Listeners API* — the `on()` method now returns the listener id.
- `New` — *Listeners API* — the new `offById()` method added
- `New` — `API` — The new `UiApi` section was added. It allows accessing some editor UI nodes and methods.
- `Refactoring` — Toolbox became a standalone class instead of a Module. It can be accessed only through the Toolbar module.
- `Refactoring` — CI flow optimized.
- `Fix` - Recognize async `onPaste` handlers in tools [#1803](https://github.com/codex-team/editor.js/issues/1803).
- `Fix` — Fire onChange event for native inputs [#1750](https://github.com/codex-team/editor.js/issues/1750)

### 2.22.3

- `Fix` — Tool config is passed to `prepare` method [editor-js/embed#68](https://github.com/editor-js/embed/issues/68)

### 2.22.2

- `Improvement` — Inline Toolbar might be used for any contenteditable element inside Editor.js zone
- `Improvement` *Tunes API* - Tunes now can provide sanitize configuration
- `Fix` *Tunes API* - Tune config now passed to constructor under `config` property
- `Fix` *Types* - Add common type for internal and external Tools configuration
- `Fix` — Block's destroy method is called on block deletion
- `Fix` - Fix jump to the button of editor zone on CBS

### 2.22.1

- `Fix` — I18n for internal Block Tunes [#1661](https://github.com/codex-team/editor.js/issues/1661)

### 2.22.0

- `New` - `onChange` callback now receive Block API object of affected block
- `New` - API method `blocks.update(id, data)` added.

### 2.21.0

- `New` - Blocks now have unique ids [#873](https://github.com/codex-team/editor.js/issues/873)

### 2.20.2

- `Fix` — Append default Tunes if user tunes are provided for Block Tool [#1640](https://github.com/codex-team/editor.js/issues/1640)
- `Fix` - Prevent the leak of codex-tooltip when Editor.js is destroyed [#1475](https://github.com/codex-team/editor.js/issues/1475).
- `Refactoring` - Notifier module now is a util.

### 2.20.1

- `Fix` - Create a new block when clicked at the bottom [#1588](https://github.com/codex-team/editor.js/issues/1588).
- `Fix` — Fix sanitization problem with Inline Tools [#1631](https://github.com/codex-team/editor.js/issues/1631)
- `Fix` — Fix copy in FireFox [1625](https://github.com/codex-team/editor.js/issues/1625)
- `Refactoring` - The Sanitizer module is util now.
- `Refactoring` - Tooltip module is util now.
- `Refactoring` — Refactoring based on LGTM [#1577](https://github.com/codex-team/editor.js/issues/1577).
- `Refactoring` — Refactoring based on ESLint [#1636](https://github.com/codex-team/editor.js/issues/1636).

### 2.20.0

- `New` — [Block Tunes API](block-tunes.md) added

### 2.19.3

- `Fix` — Ignore error raised by Shortcut module

### 2.19.2

- `New` - `toolbar.toggleBlockSettings()` API method added [#1442](https://github.com/codex-team/editor.js/issues/1421).
- `Improvements` - A generic type for Tool config added [#1516](https://github.com/codex-team/editor.js/issues/1516)
- `Improvements` - Remove unused `force` option in `Caret.navigateNext()` and `Caret.navigatePrevious()` [#857](https://github.com/codex-team/editor.js/issues/857#issuecomment-770363438).
- `Improvements` - Remove bundles from the repo [#1541](https://github.com/codex-team/editor.js/pull/1541).
- `Improvements` - Document will be scrolled when blocks are selected with `SHIFT+UP` or `SHIFT+DOWN` [#1447](https://github.com/codex-team/editor.js/issues/1447)
- `Improvements` - The caret will be set on editor copy/paste [#1470](https://github.com/codex-team/editor.js/pull/1470)
- `Improvements` - Added generic types to OutputBlockData [#1551](https://github.com/codex-team/editor.js/issues/1551).
- `Fix` - Fix BlockManager.setCurrentBlockByChildNode() with multiple Editor.js instances [#1503](https://github.com/codex-team/editor.js/issues/1503).
- `Fix` - Fix an unstable block cut process [#1489](https://github.com/codex-team/editor.js/issues/1489).
- `Fix` - Type definition of the Sanitizer config: the sanitize function now contains param definition [#1491](https://github.com/codex-team/editor.js/pull/1491).
- `Fix` - Fix unexpected behavior on an empty link pasting [#1348](https://github.com/codex-team/editor.js/issues/1348).
- `Fix` - Fix SanitizerConfig type definition [#1513](https://github.com/codex-team/editor.js/issues/1513)
- `Refactoring` - The Listeners module now is a util.
- `Refactoring` - The Events module now is a util.
- `Fix` - Editor Config now immutable [#1552](https://github.com/codex-team/editor.js/issues/1552).
- `Refactoring` - Shortcuts module is util now.
- `Fix` - Fix bubbling on BlockManagers' listener [#1433](https://github.com/codex-team/editor.js/issues/1433).


### 2.19.1

- `Improvements` - The [Cypress](https://www.cypress.io) was integrated as the end-to-end testing framework
- `Improvements` - Native `typeof`replaced with custom utils methods
- `Improvements` - Bind shortcuts listeners on the editor wrapper instead of document [#1391](https://github.com/codex-team/editor.js/issues/1391)
- `Fix` - The problem with destroy() method [#1380](https://github.com/codex-team/editor.js/issues/1380).
- `Fix` - add getter keyword to `block.mergeable` method [#1415](https://github.com/codex-team/editor.js/issues/1415).
- `Fix` — Fix problem with entering to Editor.js by Tab key [#1393](https://github.com/codex-team/editor.js/issues/1393)
- `Fix` - Sanitize pasted block data [#1396](https://github.com/codex-team/editor.js/issues/1396).
- `Fix` - Unnecessary block creation after arrow navigation at last non-default block[#1414](https://github.com/codex-team/editor.js/issues/1414)

### 2.19

- `New` - Read-only mode 🥳 [#837](https://github.com/codex-team/editor.js/issues/837)
- `New` - RTL mode added [#670](https://github.com/codex-team/editor.js/issues/670)
- `New` - Allows users to provide common `inlineToolbar` property which will be used for all tools whose `inlineToolbar` property is set to `true`. It can be overridden by the tool's own `inlineToolbar` property. Also, inline tools will be ordered according to the order of the inline tools in array provided in the `inlineToolbar` property. [#1056](https://github.com/codex-team/editor.js/issues/1056)
- `New` - Tool's `reset` static method added to the API to clean up any data added by Tool on initialization
- `Improvements` - The `initialBlock` property of Editor config is deprecated. Use the `defaultBlock` instead. [#993](https://github.com/codex-team/editor.js/issues/993)
- `Improvements` - BlockAPI `call()` method now returns the result of calling method, thus allowing it to expose arbitrary data as needed [#1205](https://github.com/codex-team/editor.js/pull/1205)
- `Improvements` - Useless log about missed i18n section has been removed  [#1269](https://github.com/codex-team/editor.js/issues/1269)
- `Improvements` - Allowed to set `false` as `toolbox` config in order to hide Toolbox button [#1221](https://github.com/codex-team/editor.js/issues/1221)
- `Fix` — Fix problem with types usage [#1183](https://github.com/codex-team/editor.js/issues/1183)
- `Fix` - Fixed issue with Spam clicking the "Click to tune" button duplicates the icons on FireFox. [#1273](https://github.com/codex-team/editor.js/issues/1273)
- `Fix` - Fixed issue with `editor.blocks.delete(index)` method which throws an error when Editor.js is not focused, even after providing a valid index. [#1182](https://github.com/codex-team/editor.js/issues/1182)
- `Fix` - Fixed the issue of toolbar not disappearing on entering input in Chinese, Hindi and some other languages. [#1196](https://github.com/codex-team/editor.js/issues/1196)
- `Fix` - Do not stop events propagation if not needed (essential for React synthetic events) [#1051](https://github.com/codex-team/editor.js/issues/1051) [#946](https://github.com/codex-team/editor.js/issues/946)
- `Fix` - Tool's `destroy` method is not invoked when `editor.destroy()` is called. [#1047](https://github.com/codex-team/editor.js/issues/1047)
- `Fix` - Fixed issue with enter key in inputs and textareas [#920](https://github.com/codex-team/editor.js/issues/920)
- `Fix` - blocks.getBlockByIndex() API method now returns void for indexes out of range [#1270](https://github.com/codex-team/editor.js/issues/1270)
- `Fix` - Fixed the `Tab` key behavior when the caret is not set inside contenteditable element, but the block is selected [#1302](https://github.com/codex-team/editor.js/issues/1302).
- `Fix` - Fixed the `onChange` callback issue. This method didn't be called for native inputs before some contenteditable element changed [#843](https://github.com/codex-team/editor.js/issues/843)
- `Fix` - Fixed the `onChange` callback issue. This method didn't be called after the callback throws an exception [#1339](https://github.com/codex-team/editor.js/issues/1339)
- `Fix` - The internal `shortcut` getter of Tools classes will work now.
- `Deprecated` — The Inline Tool `clear()` method is deprecated because the new instance of Inline Tools will be created on every showing of the Inline Toolbar

### 2.18

- `New` *I18n API* — Ability to provide internalization for Editor.js core and tools. [#751](https://github.com/codex-team/editor.js/issues/751)
- `New` — Block API that allows you to access certain Block properties and methods
- `Improvements` - TSLint (deprecated) replaced with ESLint, old config changed to [CodeX ESLint Config](https://github.com/codex-team/eslint-config).
- `Improvements` - Fix many code-style issues, add missed annotations.
- `Improvements` - Adjusted GitHub action for ESLint.
- `Improvements` - Blocks API: if `blocks.delete` method is called, but no Block is selected, show warning instead of throwing an error [#1102](https://github.com/codex-team/editor.js/issues/1102)
- `Improvements` - Blocks API: allow deletion of blocks by specifying block index via `blocks.delete(index)`.
- `Improvements` - UX: Navigate next Block from the last non-initial one creates new initial Block now [#1103](https://github.com/codex-team/editor.js/issues/1103)
- `Improvements` - Improve performance of DOM traversing at the `isEmpty()` method [#1095](https://github.com/codex-team/editor.js/issues/1095)
- `Improvements` - CODE OF CONDUCT added
- `Improvements` - Disabled useCapture flag for a block keydown handling. That will allow plugins to override keydown and stop event propagation, for example, to make own Tab behavior.
- `Improvements` - All modules now might have `destroy` method called on Editor.js destroy
- `Improvements` - Block settings can contain text inputs, focus will be restored after settings closed [#1090](https://github.com/codex-team/editor.js/issues/1090)
- `Fix` - Editor's styles won't be appended to the `<head>` when another instance have already do that [#1079](https://github.com/codex-team/editor.js/issues/1079)
- `Fix` - Fixed wrong toolbar icon centering in Firefox [#1120](https://github.com/codex-team/editor.js/pull/1120)
- `Fix` - Toolbox: Tool's order in Toolbox now saved in accordance with `tools` object keys order [#1073](https://github.com/codex-team/editor.js/issues/1073)
- `Fix` - Setting `autofocus` config property to `true` cause adding `.ce-block--focused` for the autofocused block  [#1073](https://github.com/codex-team/editor.js/issues/1124)
- `Fix` - Public getter `shortcut` now works for Inline Tools [#1132](https://github.com/codex-team/editor.js/issues/1132)
- `Fix` - `CMD+A` handler removed after Editor.js destroy [#1133](https://github.com/codex-team/editor.js/issues/1133)

>  *Breaking changes* `blocks.getBlockByIndex` method now returns BlockAPI object. To access old value, use BlockAPI.holder property

### 2.17

- `Improvements` - Editor's [onchange callback](https://editorjs.io/configuration#editor-modifications-callback) now accepts an API as a parameter
- `Fix` - Some mistakes are fixed in [installation.md](installation.md)
- `Fix` - Fixed multiple paste callback triggering in a case when several editors are instantiated [#1011](https://github.com/codex-team/editor.js/issues/1011)
- `Fix` - Fixed inline toolbar flipper activation on closing conversion toolbar [#995](https://github.com/codex-team/editor.js/issues/995)
- `Improvements` - New window tab is opened by clicking on anchor with ctrl [#1057](https://github.com/codex-team/editor.js/issues/1057)
- `Fix` - Fix block-tune buttons alignment in some CSS-resetors that forces `box-sizing: border-box` rule [#1003](https://github.com/codex-team/editor.js/issues/1003)
- `Improvements` - New style of a Block Settings button. Focused block background removed.
- `New` — Add in-house copy-paste support through `application/x-editor-js` mime-type
- `New` Block [lifecycle hook](tools.md#block-lifecycle-hooks) `moved`
- `Deprecated` — [`blocks.swap(fromIndex, toIndex)`](api.md) method is deprecated. Use `blocks.move(toIndex, fromIndex)` instead.
- `Fix` — Improve plain text paste [#1012](https://github.com/codex-team/editor.js/issues/1012)
- `Fix` — Fix multiline paste [#1015](https://github.com/codex-team/editor.js/issues/1015)


### 2.16.1

- `Fix` — Fix Firefox bug with incorrect height and cursor position of empty content editable elements [#947](https://github.com/codex-team/editor.js/issues/947) [#876](https://github.com/codex-team/editor.js/issues/876) [#608](https://github.com/codex-team/editor.js/issues/608) [#876](https://github.com/codex-team/editor.js/issues/876)
- `Fix` — Set initial hidden Inline Toolbar position [#979](https://github.com/codex-team/editor.js/issues/979)
- `Fix` — Fix issue with CodeX.Tooltips TypeScript definitions [#978](https://github.com/codex-team/editor.js/issues/978)
- `Fix` — Fix some issues with Inline and Tunes toolbars.
- `Fix` - Fix `minHeight` option with zero-value issue [#724](https://github.com/codex-team/editor.js/issues/724)
- `Improvements` — Disable Conversion Toolbar if there are no Tools to convert [#984](https://github.com/codex-team/editor.js/issues/984)

### 2.16

- `Improvements` — Inline Toolbar design improved
- `Improvements` — Conversion Toolbar now included in the Inline Toolbar [#853](https://github.com/codex-team/editor.js/issues/853)
- `Improvements` — All buttons now have beautiful Tooltips provided by [CodeX Tooltips](https://github.com/codex-team/codex.tooltips)
- `New` — new Tooltips API for displaying tooltips near your custom elements
- `New` *API* — Block [lifecycle hooks](tools.md#block-lifecycle-hooks)
- `New` *Inline Tools API* — Ability to specify Tool's title via `title` static getter.
- `Fix` — On selection from end to start backspace is working as expected now [#869](https://github.com/codex-team/editor.js/issues/869)
- `Fix` — Fix flipper with empty dom iterator [#926](https://github.com/codex-team/editor.js/issues/926)
- `Fix` — Normalize node before walking through children at `isEmpty` method [#943](https://github.com/codex-team/editor.js/issues/943)
- `Fix` — Fixed Grammarly conflict [#779](https://github.com/codex-team/editor.js/issues/779)
- `Improvements` — Module Listeners now correctly removes events with options [#904](https://github.com/codex-team/editor.js/pull/904)
- `Improvements` — Styles API: `.cdx-block` default vertical margins decreased from 0.7 to 0.4 ems.
- `Fix` — Fixed `getRangeCount` call if range count is 0 [#938](https://github.com/codex-team/editor.js/issues/938)
- `New` — Log levels now available to suppress Editor.js console messages [#962](https://github.com/codex-team/editor.js/issues/962)
- `Fix` — Fixed wrong navigation on block deletion

### 2.15.1

- `Refactoring` — Constants of tools settings separated by internal and external to correspond API
- `Refactoring` — Created universal Flipper class that responses for navigation by keyboard inside of any Toolbars
- `Fix` — First CMD+A on block with now uses default behaviour. Fixed problem with second CMD+A after selection clearing [#827](https://github.com/codex-team/editor.js/issues/827)
- `Improvements` — Style of inline selection and selected blocks improved
- `Fix` - Fixed problem when property 'observer' in modificationObserver is not defined

### 2.15

- `New` — New [`blocks.insert()`](api.md) API method [#715](https://github.com/codex-team/editor.js/issues/715).
- `New` *Conversion Toolbar* — Ability to convert one block to another [#704](https://github.com/codex-team/editor.js/issues/704)
- `New` *Cross-block selection* — Ability to select multiple blocks by mouse and with SHIFT+ARROWS [#703](https://github.com/codex-team/editor.js/issues/703)
- `Deprecated` — [`blocks.insertNewBlock()`](api.md) method is deprecated. Use `blocks.insert()` instead.
- `Improvements` — Inline Toolbar now works on mobile devices [#706](https://github.com/codex-team/editor.js/issues/706)
- `Improvements` — Toolbar looks better on mobile devices [#706](https://github.com/codex-team/editor.js/issues/706)
- `Improvements` — Now `pasteConfig` can return `false` to disable paste handling on your Tool [#801](https://github.com/codex-team/editor.js/issues/801)
- `Fix` — EditorConfig's `onChange` callback now fires when native inputs\` content has been changed [#794](https://github.com/codex-team/editor.js/issues/794)
- `Fix` — Resolve bug with deleting leading new lines [#726](https://github.com/codex-team/editor.js/issues/726)
- `Fix` — Fix inline link Tool to support different link types like `mailto` and `tel` [#809](https://github.com/codex-team/editor.js/issues/809)
- `Fix` — Added `typeof` util method to check exact object type [#805](https://github.com/codex-team/editor.js/issues/805)
- `Fix` — Remove internal `enableLineBreaks` option from external Tool settings type description [#825](https://github.com/codex-team/editor.js/pull/825)

### 2.14

- `Fix` *Config* — User config now has higher priority than internal settings [#771](https://github.com/codex-team/editor.js/issues/771)
- `New` — Ability to work with Block Actions and Inline Toolbar from the keyboard by Tab. [#705](https://github.com/codex-team/editor.js/issues/705)
- `Fix` — Fix error thrown by click on the empty editor after `blocks.clear()` method calling [#761](https://github.com/codex-team/editor.js/issues/761)
- `Fix` — Fix placeholder property appearance. Now you can assign it via `placeholder` property of EditorConfig. [#714](https://github.com/codex-team/editor.js/issues/714)
- `Fix` — Add API shorthands to TS types [#788](https://github.com/codex-team/editor.js/issues/788)

### 2.13

- `Improvements` *BlockSelection* — Block Selection allows to select single editable element via CMD+A
- `New` *API* — Added [API methods](api.md) to open and close inline toolbar [#665](https://github.com/codex-team/editor.js/issues/665)
- `New` *Config* - Added new property in EditorConfig `holder`, use this property for append Editor instead `holderId`. `holder` property now support reference on dom element. [#696](https://github.com/codex-team/editor.js/issues/696)
- `Deprecated` *Config* - `holderId` property now is deprecated and will removed in next major release. Use `holder` instead.
- `Fix` *Types* — Fixed error with `codex-notifier` package [#713](https://github.com/codex-team/editor.js/issues/713)
- `Improvements` — Close inline toolbar after creating a new link.
- `New` *Config* — Option `minHeight` for customizing Editor's bottom zone height added.

### 2.12.4

- `Improvements` — CodeX.Shortcuts version updated to the v1.1 [#684](https://github.com/codex-team/editor.js/issues/684)
- `Fix` — Do not start multi-block selection on Toolbox and Inline Toolbar [#646](https://github.com/codex-team/editor.js/issues/646)
- `Fix` — Minor fixes of caret behaviour [#663](https://github.com/codex-team/editor.js/issues/663)
- `Fix` — Fix inline-link icon position in Firefox [#674](https://github.com/codex-team/editor.js/issues/674)

### 2.12.3

- `Fix` — Make Toolbox tooltip position font-size independent

### 2.12.2

- New *Inline Tools* — pass tool settings from configuration to Tool constructor

### 2.12.1

- `Fix` — Fix processing `color-mod` function in styles

### 2.12.0

- `New` *API* - new `blocks` API method `renderFromHTML`

### 2.11.11

- `New` — Add ability to pass configuration for internal Tools

### 2.11.10

- `Fix` - Fix editor view on mobile devices

### 2.11.9

- `Fix` - Fix inline toolbar buttons margin. Update dependencies list. Update tools for example page.

### 2.11.8

- `Fix` — Block tunes margins now better works with more than 3 buttons

### 2.11.7

- `Fix` *Paste* — Fix pasting into non-initial Blocks

### 2.11.6

- `Fix` *Paste* — Polyfill for Microsoft Edge

### 2.11.5

- `Fix` *RectangleSelection* — Redesign of the scrolling zones

### 2.11.4

- `Fix` - Clear focus when click is outside the Editor instance

### 2.11.3

- `Fix` — Fix CMD+A Selection on multiple Editor instances

### 2.11.2

- `Improvements` — Docs updated and common enhancements

### 2.11.1

- `Fix` *RectangleSelection* — Selection is available only for the main mouse button

### 2.11.0

- `New` — Add API methods shorthands

### 2.10.0

- `New` — Rename from CodeX Editor to Editor.js

### 2.9.5

- `New` — Toolbox now have beautiful helpers with Tool names and shortcuts

### 2.9.4

- `Improvements` — Prevent navigating back on Firefox when Block is removing by backspace

### 2.9.3

- `Fix` — Handle paste only on initial Block

### 2.9.2

- `New` — Blocks selected with Rectangle Selection can be also removed, copied or cut

### 2.9.1

- `Improvements` — Migrate from `postcss-cssnext` to `postcss-preset-env` and disable `postcss-custom-properties` which conflicts with `postcss-preset-env`

### 2.9.0

- `New` *RectangleSelection* — Ability to select Block or several Blocks with mouse

### 2.8.1

- `Fix` *Caret* — Fix "History back" call on backspace in Firefox

### 2.8.0

- `Improvements` *API* — Added [API methods](api.md#caretapi) to manage caret position

### 2.7.32

- `Improvements` *Types* — TypeScript types sre updated

### 2.7.31

- `Fix` — Caret now goes through <input> elements without `type` attribute

### 2.7.30

- `Fix` — Fixed selection behavior when text has modifiers form Inline Toolbar

### 2.7.29

- `Fix` — cmd+x works only for custom selection now

### 2.7.28

- `New` [Tools Validation](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#validate-optional) is added.

### 2.2.27

- `New` *Mobile view* — Editor now adopted for mobile devices
- `New` *Narrow mode* — Editor now adopted for narrow containers

### 2.2.26

- `Improvements` *Caret* — Improvements of the caret behaviour: arrows, backspace and enter keys better handling.

### 2.2.25

- `New` *Autofocus* — Now you can set focus at Editor after page has been loaded

### 2.2.24

- `Improvements` *Paste* handling — minor paste handling improvements

### 2.2.23

- `New` *Shortcuts* — copy and cut Blocks selected by CMD+A

### 2.2—2.7

- `New` *Sanitize API* — [Sanitize Config](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#automatic-sanitize) of `Block Tools` now automatically extends by tags of `Inline Tools` that is enabled by current Tool by `inlineToolbar` option. You don't need more to specify `a, b, mark, code` manually. This feature will be added to fields that supports inline markup.
- `New` *Block Selection* — Ability to select Block by `CMD+A`, and the whole Editor by double `CMD+A`. After that, you can copy (`CMD+C`), remove (`Backspace`) or clear (`Enter`) selected Blocks.
- `New` *[Styles API](https://github.com/codex-team/editor.js/blob/master/types/api/styles.d.ts)* — Added `button` class for stylization of any buttons provided by Tools with one unified style.
- `New` *[Notifier API](https://github.com/codex-team/editor.js/blob/master/docs/api.md#notifierapi)* — methods for showing user notifications: on success, errors, warnings, etc.
- `New` *Block Tool* — [Table](http://github.com/editor-js/table) constructor 💪
- `New` If one of the Tools is unavailable on Editor initialization, its Blocks will be rendered with *Dummy Block*, describing that user can not edit content of this Block. Dummy Blocks can be moved, removed and saved as normal Blocks. So saved data won't be lost if one of the Tools is failed
- `New` [Public TS-types](https://github.com/codex-team/editor.js/tree/master/types) are presented.
- `Changes` *Tools API*  — options `irreplaceable` and `contentless` was removed.
- `Changes` *Tools API* — [Paste API](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#paste-handling): tags, patterns and mime-types now should be specified by Tool's `pasteConfig` static property. Custom Paste Event should be handled by `onPaste(event)` that should not be static from now.
- `Changes` *Tools API* — options `displayInToolbox ` and `toolboxIcon` was removed. Use [`toolbox`](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#internal-tool-settings) instead, that should return object with `icon` and `title` field, or `false` if Tool should not be placed at the Toolbox. Also, there are a way to override `toolbox {icon, title}` settings provided by Tool with you own settings at the Initial Config.
- `Improvements` — All Projects code now on TypeScript
- `Improvements` — NPM package size decreased from 1300kb to 422kb
- `Improvements` — Bundle size decreased from 438kb to 252kb
- `Improvements` — `Inline Toolbar`: when you add a Link to the selected fragment, Editor will highlight this fragment even when Caret is placed into the URL-input.
- `Improvements` — Block Settings won't be shown near empty Blocks of `initialType` by default. You should click on them instead.
- `Improvements` — `onChange`-callback now will be fired even with children attributes changing.
- `Improvements` — HTMLJanitor package was updated due to found vulnerability
- `Improvements` — Logging improved: now all Editor's logs will be preceded by beautiful label with current Editor version.
- `Improvements` — Internal `isEmpty` checking was improved for Blocks with many children nodes (200 and more)
- `Improvements` — Paste improvements: tags that can be substituted by Tool now will matched even on deep-level of pasted DOM three.
- `Improvements` — There is no more «unavailable» sound on copying Block by `CMD+C` on macOS
- `Improvements` — Dozens of bugfixes and small improvements

See a whole [Changelog](/docs/)

### 2.1-beta changelog

- `New` *Tools API* — support pasted content via drag-n-drop or from the Buffer. See [documentation](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#paste-handling) and [example](https://github.com/editor-js/simple-image/blob/master/src/index.js#L177) at the Simple Image Tool.
- `New` *Tools API* — new `sanitize` getter for Tools for automatic HTML sanitizing of returned data. See [documentation](https://github.com/codex-team/editor.js/blob/master/docs/tools.md#sanitize) and [example](https://github.com/editor-js/paragraph/blob/master/src/index.js#L121) at the Paragraph Tool
- `New` Added `onChange`-callback, fired after any modifications at the Editor. See [documentation](https://github.com/codex-team/editor.js/blob/master/docs/installation.md#features).
- `New` New Inline Tool example — [Marker](https://github.com/editor-js/marker)
- `New` New Inline Tool example — [Code](https://github.com/editor-js/code)
- `New` New [Editor.js PHP](http://github.com/codex-team/codex.editor.backend) — example of server-side implementation with HTML purifying and data validation.
- `Improvements` - Improvements of Toolbar's position calculation.
- `Improvements` — Improved zero-configuration initialization.
- and many little improvements.


---

<!-- Source: docs/api.md -->

---

# Editor.js API

---
Most actual API described by [this interface](../types/api/index.d.ts).

---
📃 See official API documentation [https://editorjs.io/api](https://editorjs.io/api)

---

Tools have access to the public methods provided by Editor.js API Module. Plugin and Tune Developers
can use Editor\`s API as they want.

## Block API

API for certain Block methods and properties. You can access it through `editor.api.block.getBlockByIndex` method or get it form `block` property of [Tool constructor](../types/tools/block-tool.d.ts) argument.

`name: string` — Block's Tool name (key, specified in `tools` property of initial configuration)

`config: ToolConfig` — Tool config passed on Editor initialization

`holder: HTMLElement` — HTML Element that wraps Tool's HTML content

`isEmpty: boolean` — `true` if Block has any editable content

`selected: boolean` - `true` if Block is selected with Cross-Block Selection

`set stretched(state: boolean)` — set Block's stretch state

`stretched: boolean` — `true` if Block is stretched

`call(methodName: string, param?: object): void` — method to call any Tool's instance methods with checks and error handlers under-the-hood. For example, [Block lifecycle hooks](./tools.md#block-lifecycle-hooks)

`save(): Promise<void|SavedData>` — returns data saved from current Block's state, including Tool name and saving exec time

`validate(data: BlockToolData): Promise<boolean>` — calls Tool's validate method if exists

`dispatchChange(): void` - Allows to say Editor that Block was changed. Used to manually trigger Editor's 'onChange' callback. Can be useful for block changes invisible for editor core.

## Api object description

Common API interface.

```js
export interface API {
   blocks: IBlocksAPI;
   caret: ICaretAPI;
   sanitizer: ISanitizerAPI;
   toolbar: IToolbarAPI;
   // ...
 }
 ```

#### BlocksAPI

Methods that working with Blocks

`render(data)` - render passed JSON data

`renderFromHTML(data)` - parse and render passed HTML string (*not for production use*)

`swap(fromIndex, toIndex)` - swaps two Blocks by their positions (deprecated:
use 'move' instead)

`move(toIndex, fromIndex)` - moves block from one index to another position.
`fromIndex` will be the current block's index by default.

`delete(blockIndex?: Number)` - deletes Block with passed index

`getCurrentBlockIndex()` - current Block index

`getBlockByIndex(index: Number)` - returns Block API object by passed index

`getBlocksCount()` - returns Blocks count

`stretchBlock(index: number, status: boolean)` - _Deprecated. Use Block API interface instead._ make Block stretched.

`insertNewBlock()` - __Deprecated__ insert new Block after working place

`insert(type?: string, data?: BlockToolData, config?: ToolConfig, index?: number, needToFocus?: boolean)` - insert new Block with passed parameters

`update(id: string, data?: BlockToolData, tunes?: {[name: string]: BlockTuneData})` - updates block data and block tunes for the block with passed id

#### SanitizerAPI

`clean(taintString, config)` - method uses HTMLJanitor to clean taint string.

Editor.js provides basic config without attributes, but you can inherit by passing your own config.

If Tool enables inline-tools, we get it's sanitizing rules and merge with your passed custom rules.

Usage:

```js
let taintString = '<div><p style="font-size: 5em;"><b></b>BlockWithText<a onclick="void(0)"></div>'
let customConfig = {
  b: true,
  p: {
    style: true,
  },
}
this.api.sanitizer.clean(taintString, customConfig);
```

### ToolbarAPI

Methods that working with Toolbar

`open()` - opens toolbar

`close()` - closes toolbar, toolbox and blockSettings if they are opened

### InlineToolbarAPI

Methods that works with inline toolbar

`open()` - opens inline toolbar, (opens for the current selection)

`close()` - closes inline toolbar

### ListenerAPI

Methods that allows to work with DOM listener. Useful when you forgot to remove listener. Module collects all listeners and destroys automatically

`on(element: HTMLElement, eventType: string, handler: Function, useCapture?: boolean)` - add event listener to HTML element

`off(element: HTMLElement, eventType: string, handler: Function)` - remove event handler from HTML element


### CaretAPI

Methods to manage caret position.

Each method accept `position` and `offset` parameters. `Offset` should be used to shift caret by passed amount of characters.

`Position` can be one of the following values:

| Value     | Description
| --------- | -----------
| `start`   | Caret will be set at the Block's beginning
| `end`     | Caret will be set at the Block end
| `default` | More or less emulates browser behaviour, in most cases behaves as `start`

Each method returns `boolean` value: true if caret is set successfully or false otherwise (e.g. when there is no Block at index);

`setToFirstBlock(position?: 'end'|'start'|'default', offset?: number): boolean;` — set caret to the first Block

`setToLastBlock(position?: 'end'|'start'|'default', offset?: number): boolean;` — set caret to the last Block

`setToNextBlock(position?: 'end'|'start'|'default', offset?: number): boolean;` — set caret to the next Block

`setToPreviousBlock(position?: 'end'|'start'|'default', offset?: number): boolean;` — set caret to the previous Block

`setToBlock(index: number, position?: 'end'|'start'|'default', offset?: number): boolean;` — set caret to the Block by passed `index`

`focus(atEnd?: boolean): boolean;` — set caret to the Editor. If `atEnd` is true, set it at the end.

### NotifierAPI

If you need to show any messages for success or failure events you can use notifications module.

Call on target Editor:

```javascript
let editor = new EditorJS({
  onReady: () => {
    editor.notifier.show({
      message: 'Editor is ready!'
    });
  },
});
```

In Tool's class:

```javascript
this.api.notifier.show({
  message: 'Cannot upload image. Wrong mime-type.',
  style: 'error',
});
```

![](assets/14fcdbe4-d6eb-41d4-b66e-e0e86ccf1a4b.jpg)


Check out [`codex-notifier` package page](https://github.com/codex-team/js-notifier) on GitHub to find docs, params and examples.

### Destroy API

If there are necessity to remove Editor.js instance from the page you can use `destroy()` method.

It makes following steps:

1. Clear the holder element by setting it\`s innerHTML to empty string

2. Remove all event listeners related to Editor.js

3. Delete all properties from instance object and set it\`s prototype to `null`

After executing the `destroy` method, editor inctance becomes an empty object. This way you will free occupied JS Heap on your page.

### Tooltip API

Methods for showing Tooltip helper near your elements. Parameters are the same as in [CodeX Tooltips](http://github.com/codex-team/codex.tooltips) lib.

#### Show

Method shows tooltip with custom content on passed element

```js
this.api.tooltip.show(element, content, options);
```

| parameter | type | description |
| -- | -- | -- |
| `element` | _HTMLElement_ | Tooltip will be showed near this element |
| `content` | _String_ or _Node_ | Content that will be appended to the Tooltip |
| `options` | _Object_ | Some displaying options, see below |

Available showing options

| name | type | action |
| -- | -- | -- |
| placement | `top`, `bottom`, `left`, `right` | Where to place the tooltip. Default value is `bottom' |
| marginTop | _Number_ | Offset above the tooltip with `top` placement |
| marginBottom | _Number_ | Offset below the tooltip with `bottom` placement |
| marginLeft | _Number_ | Offset at left from the tooltip with `left` placement |
| marginRight | _Number_ | Offset at right from the tooltip with `right` placement |
| delay | _Number_ | Delay before showing, in ms. Default is `70` |
| hidingDelay | _Number_ | Delay before hiding, in ms. Default is `0` |

#### Hide

Method hides the Tooltip.

```js
this.api.tooltip.hide();
```

#### onHover

Decorator for showing tooltip near some element by "mouseenter" and hide by "mouseleave".

```js
this.api.tooltip.onHover(element, content, options);
```

### API Shorthands

Editor`s API provides some shorthands for API methods.

| Alias    | Method          |
| ------   | --------------- |
| `clear`  | `blocks.clear`  |
| `render` | `blocks.render` |
| `focus`  | `caret.focus`   |
| `save`   | `saver.save`    |

> Example

```javascript
const editor = EditorJS();

editor.focus();
editor.save();
```



---

<!-- Source: docs/block-tunes.md -->

---

# Block Tunes

Similar with [Tools](tools.md) represented Blocks, you can create Block Tunes and connect it to particular Tool or for all Tools.

Block Tunes allows you to set any additional options to Blocks. For example, with corresponded Block Tunes you can mark Block as «spoiler», give it an anchor, set a background, and so on.

## Base structure

Tune's class should have the `isTune` property (static getter) set to `true`.

Block Tune must implement the `render()` method which returns an HTML Element that will be appended to the Block Settings panel.

- `render()` — create a button

Also, you can provide optional methods

- `wrap()` — wraps Block content with own HTML elements
- `save()` — save Tunes state on Editor's save

At the constructor of Tune's class exemplar you will receive an object with following parameters:

| Parameter | Description |
| --------- | ----------- |
| api  | Editor's [API](api.md) obejct |
| config | Configuration of Block Tool Tune is connected to (might be useful in some cases) |
| block | [Block API](api.md#block-api) methods for block Tune is connected to |
| data | Saved Tune data |

---

### render(): HTMLElement

Method that returns button to append to the block settings area

#### Parameters

Method does not accept any parameters

#### Return value

type | description |
-- | -- |
`HTMLElement` | element that will be added to the block settings area |

---

### wrap(blockContent: HTMLElement): HTMLElement

Method that accepts Block's content and wrap it with your own layout.
Might be useful if you want to modify Block appearance.

```javascript
class Tune {
    wrap(blockContent) {
        const myWrapper = document.createElement('div');

        myWrapper.append(blockContent);

        return myWrapper;
    }
}
```

#### Parameters

name | type | description |
-- |-- | -- |
blockContent | HTMLElement | Block's content (might be wrapped by other Tunes) |

#### Return value

| type | description |
| -- | -- |
| HTMLElement | Your element that wraps block content |

---

### save()

Method should return Tune's state you want to save to Editor's output

#### Parameters

No parameters

#### Return value

type | description |
-- | -- |
`any` | any data you want to save |

---

### static prepare()

If you need to prepare some data for Tune (eg. load external script, create HTML nodes in the document, etc) you can use the static `prepare()` method.

It accepts tunes config passed on Editor's initialization as an argument:


```javascript
class Tune {
  static prepare(config) {
    loadScript();
    insertNodes();
    ...
  }
}
```

#### Parameters

type | description |
-- | -- |
`object` | your Tune configuration |


#### Return value

No return value

---

### static reset()

On Editor destroy you can use an opposite method `reset` to clean up all prepared data:

```javascript
class Tune {
  static reset() {
    cleanUpScripts();
    deleteNodes();
  ...
  }
}
```

#### Parameters

No parameters

#### Return value

No return value

---

### static get sanitize()

If your Tune inserts any HTML markup into Block's content you need to provide sanitize configuration, so your HTML is not trimmed on save.

Please see more information at [sanitizer page](sanitizer.md).


```javascript
class Tune {
  static get sanitize() {
    return {
      sup: true
    }
  }
}
```

## Format

Tunes data is saved to `tunes` property of output object:

```
{
  blocks: [
    {
      type: 'paragraph',
      data: {
        text: 'This is paragraph with Tune'
      },
      tunes: {
        'my-tune-name': {},
        favorite: true,
        anchor: 'might be string'
      }
    }
  ]
}
```


---

<!-- Source: docs/caret.md -->

---

# Editor.js Caret Module

The `Caret` module contains methods working with caret. Uses [Range](https://developer.mozilla.org/en-US/docs/Web/API/Range) methods to navigate caret
between blocks. 

Caret class implements basic Module class that holds User configuration
and default Editor.js instances

## Properties

## Methods

### setToBlock

```javascript
Caret.setToBlock(block, position, offset)
```

> Method gets Block instance and puts caret to the text node with offset

#### params

| Param        | Type | Description|
| -------------|------ |:-------------:|
| block        | Object | Block instance that BlockManager created|
| position     | String | Can be 'start', 'end' or 'default'. Other values will be treated as 'default'. Shows position of the caret regarding to the Block.|
| offset       | Number | caret offset regarding to the text node (Default: 0)|


### setToTheLastBlock

```javascript
Caret.setToTheLastBlock()
```

> sets Caret at the end of last Block
If last block is not empty, inserts another empty Block which is passed as initial


---

<!-- Source: docs/installation.md -->

---

# Installation Guide

There are few steps to run Editor.js on your site.

1. [Load Editor's core](#load-editors-core)
2. [Load Tools](#load-tools)
3. [Initialize Editor's instance](#create-editor-instance)

## Load Editor's core

Firstly you need to get Editor.js itself. It is a [minified script](../dist/editor.js) with minimal available

Choose the most usable method of getting an Editor for you.

- Node package
- Source from CDN
- Local file from a project

### Node.js

Install the package via NPM or Yarn

```shell
npm i @editorjs/editorjs
```

Include module at your application

```javascript
import EditorJS from '@editorjs/editorjs';
```

### Use from CDN

You can load specific version of package from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/@editorjs/editorjs).

`https://cdn.jsdelivr.net/npm/@editorjs/editorjs@2.10.0`

Then require this script.

```html
<script src="..."></script>
```

### Save sources to project

Copy [editor.js](../dist/editor.js) file to your project and load it.

```html
<script src="editor.js"></script>
```

## Load Tools

Each Block at the Editor.js represented by [Tools](tools.md). There are simple external scripts with their own logic. You'll probably want to use several Block Tools that should be connected.

For example, check out our [Header](https://github.com/editor-js/header) Tool that represents heading blocks.

You can install the Header Tool via the same ways as an Editor (Node.js, CDN, local file).

Check [Editor.js's community](https://github.com/editor-js/) to see Tools examples.

**Example:** use Header from CDN

```html
<script src="https://cdn.jsdelivr.net/npm/codex.editor.header@2.1.0/dist/bundle.js"></script>
```

## Create Editor instance

Create an instance of Editor.js and pass [Configuration Object](../src/types-internal/editor-config.ts).
At least the `holder` option is required.

```html
<div id="editorjs"></div>
```

You can create a simple Editor only with a default Paragraph Tool by passing a string with element's Id (wrapper for Editor) as a configuration param or use default `editorjs`.

```javascript
var editor = new EditorJS(); /** Zero-configuration */

// equals

var editor = new EditorJS('editorjs');
````

Or pass a whole settings object.

```javascript
var editor = new EditorJS({
    /**
     * Create a holder for the Editor and pass its ID
     */
    holder : 'editorjs',

    /**
     * Available Tools list.
     * Pass Tool's class or Settings object for each Tool you want to use
     */
    tools: {
        header: {
          class: Header,
          inlineToolbar : true
        },
        // ...
    },

    /**
     * Previously saved data that should be rendered
     */
    data: {}
});
```

## Ready callback

Editor.js needs a bit of time to initialize. It is an asynchronous action so it won't block execution of your main script.

If you need to know when the editor instance is ready you can use one of the following ways:

##### Pass `onReady` property to the configuration object.

It must be a function:

```javascript
var editor = new EditorJS({
   // Other configuration properties

   /**
    * onReady callback
    */
   onReady: () => {console.log('Editor.js is ready to work!')}
});
```

#### Use `isReady` promise.

After you create a new `EditorJS` object it will contain `isReady` property.
It is a Promise object that resolves when the editor will be ready to work and rejected otherwise.
If there is an error during initialization `isReady` promise will be rejected with an error message.

```javascript
var editor = new EditorJS();

editor.isReady
  .then(() => {
    /** Do anything you need after editor initialization */
  })
  .catch((reason) => {
    console.log(`Editor.js initialization failed because of ${reason}`)
  });
```

You can use `async/await` to keep your code looking synchronous:

```javascript
var editor = new EditorJS();

try {
  await editor.isReady;
  /** Do anything you need after editor initialization */
} catch (reason) {
  console.log(`Editor.js initialization failed because of ${reason}`)
}
```


## Saving Data

Call `editor.saver.save()` and handle returned Promise with saved data.

```javascript
editor.saver.save()
  .then((savedData) => {
    console.log(savedData);
  });
```

## Features

Also, Editor.js provides useful methods to work with Editor's state.

```javascript
var editor = new EditorJS({
   // Other configuration properties

   /**
    * onReady callback
    */
   onReady: () => {console.log('Editor.js is ready to work!')},

   /**
    * onChange callback
    * Accepts CustomEvent describing what happened
    */
   onChange: (editorAPI, event) => {console.log('Now I know that Editor\'s content changed!')}
});
```

## Example

Take a look at the [example.html](../example/example.html) to view more detailed examples.


---

<!-- Source: docs/releases.md -->

---

# Branches, versions and releases — complete guideline

## Branches

The project has two main branches: `master` and `next`.

Branch `master` contains the latest stable version of the editor.
The latest version published to NPM available by default or by the tag `latest`.

Branch `next` used for development the next (release candidate) version of the editor.
It may contain bug fixes, improvements or features. This version is available in NPM by `next` tag.

## Versions

We use [semantic versioning](https://semver.org) as a main guide for naming updates.

`<major>.<minor>.<patch>`

You need to bump the part of version according the changes:

- `patch` — for bug fixes, docs updates, code style fixes and other changes which do not affect the result project bundle
- `minor` — for new features with no backward compatibility problems.
- `major` — for breaking changes without backward compatibility with the api of the previous version of the project.

Pre-release versions may contain additional `-rc.*` suffix.

## Release publishing

Drafts for new releases are created automatically via [create-a-release-draft.yml](.github/workflows/create-a-release-draft.yml)
workflow when pull request to `next` branch was merged with an updated version in the package.json file.

There is a [workflow](.github/workflows/publish-package-to-npm.yml) that fired on a new release publishing on GitHub.

Use target version changelog as a description.

![](assets/57267bab-f2f0-411b-a9d1-69abee6abab5.jpg)

Then you can publish the release and wait for package publishing via action.

This package version will be published to NPM with default `latest` tag.

### Release candidate publishing

If you want to publish release candidate version, use suffix `-rc.*` for package
version in package.json file and in tag on releases page. Workflow will detect it and mark a release as "pre-release".

![](assets/796de9eb-bbe0-485c-bc8f-9a4cb76641b7.jpg)

This package version will be published to NPM with `next` tag.

Stable version: `2.19.0`
Release candidate: `2.19.1-rc.0`, `2.19.1-rc.1`, ...
Next version: `2.19.1`

## Auto-bump version

After each PR merge to the `next` branch [bump-version-on-merge-next.yml](.github/workflows/bump-version-on-merge-next.yml)
workflow will check if a package version was updated. If there is no update then it will open a new PR with a next
prerelease version.

### How it works

The command for bumping a version will be running in a workflow.

`yarn version --prerelease --preid rc --no-git-tag-version`

Prerelease version will be bumped or a new prerelease patch will be created:

- `2.19.1` -> `2.19.2-rc.0`
- `2.19.2-rc.0` -> `2.19.2-rc.1`

### Change version

You can edit version (and PR name of course) if you need to publish not a pre-release version or any other.

If the next update is planned to raise the minor version (`2.19.1` -> `2.20.0`), then change it before version update merge.

- `2.19.1` will be bumped to `2.19.2-rc.0` be default, change `2.19.2-rc.0` to `2.20.0-rc.0`

### Ignore update

If you do not need to upgrade and publish the update with the merged pull request (docs update or any other non-important changes),
you can close the pull request generated by the workflow.

## Example pipeline

Let's imagine that package version is `2.19.0` and you want to add some bug fixes and publish an update as `2.19.1`.

1. Merge a single update or a few pulls with fixes to the default branch `next`.
2. Workflow [bump-version-on-merge-next.yml](.github/workflows/bump-version-on-merge-next.yml) will bump the version up
to `2.19.1-rc.0` in the package.json and open a new pull request.
3. After bump version PR merge, the workflow [create-a-release-draft.yml](.github/workflows/create-a-release-draft.yml)
will automatically create a draft release on GitHub.
4. Check this new draft release on the releases page. Check tag `v2.19.1-rc.0` and notice "This is pre-release" checkbox
if it should be for a release candidate versions. Then publish that release.
5. [Workflow](.github/workflows/publish-package-to-npm.yml) will automatically push the package to NPM with tag `next`.
6. When you ready to publish a release, remove suffix from version name in package.json (`2.19.1-rc.0` -> `v2.19.1`)
in pull request from workflow [bump-version-on-merge-next.yml](.github/workflows/bump-version-on-merge-next.yml).
Follow steps 3-5 with workflows and publish a new version as `latest` update.
7. Merge branch `next` to `master` and save sources for history.


---

<!-- Source: docs/sanitizer.md -->

---

# Editor.js Sanitizer Module

The `Sanitizer` module represents a set of methods that clears taint strings.
Uses lightweight npm package with simple API [html-janitor](https://www.npmjs.com/package/html-janitor)

## Methods 

### clean

```javascript
clean(taintString, customConfig)
```

> Cleans up the passed taint string
 
#### params

| Param        | Type | Description|
| -------------|------ |:-------------:|
| taintString  | String | string that needs to be cleaned|
| customConfig | Object | Can be passed new config per usage (Default: uses default configuration)|



---

<!-- Source: docs/toolbar-settings.md -->

---

# Editor.js Toolbar Block Settings Module

Toolbar Module has space for Block settings. Settings divided into:
 - space for plugin's settings, that is described by «Plugin»'s Developer
 - space for default settings. This option is also can be implemented and expanded

They difference between zones is that the first option is specified by plugin
and each Block can have different options, when second option is for every Block
regardless to the plugin's option.

### Let's look the examples:

«Plugin»'s Developers need to expand «renderSettings» method that returns HTML.
Every user action will be handled by itself. So, you can easily write
callbacks that switches your content or makes better. For more information
read [Tools](tools.md).

---

«Tune»'s Developers need to implement core-provided interface to develop
tunes that will be appeared in Toolbar default settings zone.

Tunes must expand two important methods:
 - `render()` - returns HTML and it is appended to the default settings zone
 - `save()` - extracts important information to be saved

No restrictions. Handle user action by yourself

Create Class that implements block-tune.ts

Your Tune's constructor gets argument as object and it includes:
 - {Object} api - object contains public methods from modules. @see [API](api.md)
 - {Object} settings - settings contains block default state.
This object could have information about cover, anchor and so on.

Example on TypeScript:

```js

import IBlockTune from './block-tune';

export default class YourCustomTune implements IBlockTune {

  public constructor({api, settings}) {
    this.api = api;
    this.settings = settings;
  }

  render() {
    let someHTML = '...';
    return someHTML;
  }

  save() {
    // Return the important data that needs to be saved
    return object
  }

  someMethod() {
    // moves current block down
    this.api.blocks.moveDown();
  }
}
```

Example on ES6

```js
export default class YourCustomTune {

  constructor({api, settings}) {
    this.api = api;
    this.settings = settings;
  }

  render() {
    let someHTML = '...';
    return someHTML;
  }

  save() {
    // Return the important data that needs to be saved
    return object
  }

  someMethod() {
    // moves current block down
    this.api.blocks.moveDown();
  }
}
```


---

<!-- Source: docs/tools-inline.md -->

---

# Tools for the Inline Toolbar

Similar with [Tools](tools.md) represented Blocks, you can create Tools for the Inline Toolbar. It will work with 
selected fragment of text. The simplest example is `bold` or `italic` Tools.

## Base structure

First of all, Tool's class should have a `isInline` property (static getter) set as `true`. 

After that Inline Tool should implement next methods.

- `render()` — create a button
- `surround()` — works with selected range
- `checkState()` — get Tool's activated state by selected range

Also, you can provide optional methods

- `renderActions()` — create additional element below the buttons
- `clear()` — clear Tool's stuff on opening/closing of Inline Toolbar
- `sanitize()` — sanitizer configuration

At the constructor of Tool's class exemplar you will accept an object with the [API](api.md) as a parameter.

---

### render()

Method that returns button to append at the Inline Toolbar

#### Parameters

Method does not accept any parameters

#### Return value

type | description | 
-- | -- |
`HTMLElement` | element that will be added to the Inline Toolbar |

---

### surround(range: Range)

Method that accepts selected range and wrap it somehow

#### Parameters

name | type | description | 
-- |-- | -- |
range | Range | first range of current Selection |

#### Return value

There is no return value

---

### checkState(selection: Selection)

Get Selection and detect if Tool was applied. For example, after that Tool can highlight button or show some details.

#### Parameters

name | type | description | 
-- |-- | -- |
selection | Selection | current Selection |

#### Return value

type | description | 
-- | -- |
`Boolean` | `true` if Tool is active, otherwise `false` |

---

### renderActions()

Optional method that returns additional Element with actions. 
For example, input for the 'link' tool or textarea for the 'comment' tool. 
It will be places below the buttons list at Inline Toolbar.

#### Parameters

Method does not accept any parameters

#### Return value

type | description | 
-- | -- |
`HTMLElement` | element that will be added to the Inline Toolbar |

---

### clear()

Optional method that will be called on opening/closing of Inline Toolbar. 
Can contain logic for clearing Tool's stuff, such as inputs, states and other.

#### Parameters

Method does not accept any parameters

#### Return value

Method should not return a value. 

### static get sanitize()

We recommend to specify the Sanitizer config that corresponds with inline tags that is used by your Tool. 
In that case, your config will be merged with sanitizer configuration of Block Tool 
that is using the Inline Toolbar with your Tool.

Example:

If your Tool wrapps selected text with `<b>` tag, the sanitizer config should looks like this:

```js
static get sanitize() {
  return {
    b: {} // {} means clean all attributes. true — leave all attributes
  }
}
``` 

Read more about Sanitizer configuration at the [Tools#sanitize](tools.md#sanitize)

### Specifying a title

You can pass your Tool's title via `title` static getter. It can be used, for example, in the Tooltip with 
icon description that appears by hover. 

```ts
export default class BoldInlineTool implements InlineTool {
  /**
   * Specifies Tool as Inline Toolbar Tool
   *
   * @return {boolean}
   */
  public static isInline = true;

  /**
   * Title for hover-tooltip
   */
  public static title: string = 'Bold';

  // ... other methods
}
```


---

<!-- Source: docs/tools.md -->

---

# Editor.js Tools

Editor.js is a block-oriented editor. It means that entry composed with the list of `Blocks` of different types: `Texts`, `Headers`, `Images`, `Quotes` etc.

`Tool` — is a class that provide custom `Block` type. All Tools represented by `Plugins`.

Each Tool should have an installation guide.

## Tool class structure

### constructor()

Each Tool's instance called with an params object.

| Param  | Type                                                   | Description                                     |
| ------ | ------------------------------------------------------ | ----------------------------------------------- |
| api    | [`IAPI`](../types/index.d.ts)                          | Editor.js's API methods                         |
| config | [`ToolConfig`](../types/tools/tool-config.d.ts)        | Special configuration params passed in «config» |
| data   | [`BlockToolData`](../types/tools/block-tool-data.d.ts) | Data to be rendered in this Tool                |
| block  | [`BlockAPI`](../types/api/block.d.ts)                  | Block's API methods                             |

[iapi-link]: ../src/types-internal/api.ts

#### Example

```javascript
constructor({data, config, api}) {
  this.data = data;
  this.api = api;
  this.config = config;
  // ...
}
```

### render()

Method that returns Tool's element {HTMLElement} that will be placed into Editor.

### save()

Process Tool's element created by `render()` function in DOM and return Block's data.

### validate(data: BlockToolData): boolean|Promise\<boolean\> _optional_

Allows to check correctness of Tool's data. If data didn't pass the validation it won't be saved. Receives Tool's `data` as input param and returns `boolean` result of validation.

### merge() _optional_

Method that specifies how to merge two `Blocks` of the same type, for example on `Backspace` keypress.
Method does accept data object in same format as the `Render` and it should provide logic how to combine new
data with the currently stored value.

## Internal Tool Settings

Options that Tool can specify. All settings should be passed as static properties of Tool's class.

| Name | Type | Default Value | Description |
| -- | -- | -- | -- |
| `toolbox` | _Object_ | `undefined` | Pass the `icon` and the `title` there to display this `Tool` in the Editor's `Toolbox` <br /> `icon` - HTML string with icon for the Toolbox <br /> `title` - title to be displayed at the Toolbox. <br /><br />May contain an array of `{icon, title, data}` to display the several variants of the tool, for example "Ordered list", "Unordered list". See details at [the documentation](https://editorjs.io/tools-api#toolbox) |
| `enableLineBreaks` | _Boolean_ | `false` | With this option, Editor.js won't handle Enter keydowns. Can be helpful for Tools like `<code>` where line breaks should be handled by default behaviour. |
| `isInline` | _Boolean_ | `false` | Describes Tool as a [Tool for the Inline Toolbar](tools-inline.md) |
| `isTune` | _Boolean_ | `false` | Describes Tool as a [Block Tune](block-tunes.md) |
| `sanitize` | _Object_ | `undefined` | Config for automatic sanitizing of saved data. See [Sanitize](#sanitize) section. |
| `conversionConfig` | _Object_ | `undefined` | Config allows Tool to specify how it can be converted into/from another Tool. See [Conversion config](#conversion-config) section. |

## User configuration

All Tools can be configured by users. You can set up some of available settings along with Tool's class
to the `tools` property of Editor Config.

```javascript
var editor = new EditorJS({
  holder : 'editorjs',
  tools: {
    text: {
      class: Text,
      inlineToolbar : true,
      // other settings..
    },
    header: Header
  },
  defaultBlock : 'text',
});
```

There are few options available by Editor.js.

| Name | Type | Default Value | Description |
| -- | -- | -- | -- |
| `inlineToolbar` | _Boolean/Array_ | `false` | Pass `true` to enable the Inline Toolbar with all Tools, or pass an array with specified Tools list |
| `config` | _Object_ | `null` | User's configuration for Plugin.

## Tool prepare and reset

If you need to prepare some data for Tool (eg. load external script, create HTML nodes in the document, etc) you can use static prepare method.

It accepts tools config passed on Editor's initialization as an argument:

```javascript
class Tool {
  static prepare(config) {
    loadScript();
    insertNodes();
    ...
  }
}
```

On Editor destroy you can use an opposite method `reset` to clean up all prepared data:

```javascript
class Tool {
  static reset() {
    cleanUpScripts();
    deleteNodes();
    ...
  }
}
```

Both methods might be async.

## Paste handling

Editor.js handles paste on Blocks and provides API for Tools to process the pasted data.

When user pastes content into Editor, pasted content will be splitted into blocks.

1. If plain text will be pasted, it will be splitted by new line characters
2. If HTML string will be pasted, it will be splitted by block tags

Also Editor API allows you to define your own pasting scenario. You can either:

1. Specify **HTML tags**, that can be represented by your Tool. For example, Image Tool can handle `<img>` tags.
If tags you specified will be found on content pasting, your Tool will be rendered.
2. Specify **RegExp** for pasted strings. If pattern has been matched, your Tool will be rendered.
3. Specify **MIME type** or **extensions** of files that can be handled by your Tool on pasting by drag-n-drop or from clipboard.

For each scenario, you should do 2 next things:

1. Define static getter `pasteConfig` in Tool class. Specify handled patterns there.
2. Define public method `onPaste` that will handle PasteEvent to process pasted data.

### HTML tags handling

To handle pasted HTML elements object returned from `pasteConfig` getter should contain following field:

| Name | Type | Description |
| -- | -- | -- |
| `tags` | `String[]` | _Optional_. Should contain all tag names you want to be extracted from pasted data and processed by your `onPaste` method |

For correct work you MUST provide `onPaste` handler at least for `defaultBlock` Tool.

#### Example

Header Tool can handle `H1`-`H6` tags using paste handling API

```javascript
static get pasteConfig() {
  return {
    tags: ['H1', 'H2', 'H3', 'H4', 'H5', 'H6'],
  }
}
```

**Note. Same tag can be handled by one (first specified) Tool only.**

**Note. All attributes of pasted tag will be removed. To leave some attribute, you should explicitly specify them. Se below**

Let's suppose you want to leave the 'src' attribute when handle pasting of the `img` tags. Your config should look like this:

```javascript
static get pasteConfig() {
  return {
    tags: [
      {
        img: {
          src: true
        }
      }
    ],
  }
}
```

[Read more](https://editorjs.io/sanitizer) about the sanitizing configuration.

### RegExp patterns handling

Your Tool can analyze text by RegExp patterns to substitute pasted string with data you want. Object returned from `pasteConfig` getter should contain following field to use patterns:

| Name | Type | Description |
| -- | -- | -- |
| `patterns` | `Object` | _Optional_. `patterns` object contains RegExp patterns with their names as object's keys |

**Note** Editor will check pattern's full match, so don't forget to handle all available chars in there.

Pattern will be processed only if paste was on `defaultBlock` Tool and pasted string length is less than 450 characters.

> Example

You can handle YouTube links and insert embeded video instead:

```javascript
static get pasteConfig() {
  return {
    patterns: {
      youtube: /http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?[\w\?‌​=]*)?/
    },
  }
}
```

### Files pasting

Your Tool can handle files pasted or dropped into the Editor.

To handle file you should provide `files`  property in your `pasteConfig` configuration object.

`files` property is an object with the following fields:

| Name | Type | Description |
| ---- | ---- | ----------- |
| `extensions` | `string[]` | _Optional_ Array of extensions your Tool can handle |
| `mimeTypes` | `sring[]` | _Optional_ Array of MIME types your Tool can handle |

Example

```javascript
static get pasteConfig() {
  return {
    files: {
      mimeTypes: ['image/png'],
      extensions: ['json']
    }
  }
}
```

### Pasted data handling

If you registered some paste substitutions in `pasteConfig` property, you **should** provide `onPaste` callback in your Tool class.
`onPaste` should be public non-static method. It accepts custom _PasteEvent_ object as argument.

PasteEvent is an alias for three types of events - `tag`, `pattern` and `file`. You can get the type from _PasteEvent_ object's `type` property.
Each of these events provide `detail` property with info about pasted content.

| Type  | Detail |
| ----- | ------ |
| `tag` | `data` - pasted HTML element |
| `pattern` | `key` - matched pattern key you specified in `pasteConfig` object <br /> `data` - pasted string |
| `file` | `file` - pasted file |

Example

```javascript
onPaste (event) {
  switch (event.type) {
    case 'tag':
      const element = event.detail.data;

      this.handleHTMLPaste(element);
      break;

    case 'pattern':
      const text = event.detail.data;
      const key = event.detail.key;

      this.handlePatternPaste(key, text);
      break;

    case 'file':
      const file = event.detail.file;

      this.handleFilePaste(file);
      break;
  }
}
```

### Disable paste handling

If you need to disable paste handling on your Tool for some reason, you can provide `false` as `pasteConfig` value.
That way paste event won't be processed if fired on your Tool:

```javascript
static get pasteConfig {
  return false;
}
```

## Sanitize <a name="sanitize"></a>

Editor.js provides [API](sanitizer.md) to clean taint strings.
Use it manually at the `save()` method or or pass `sanitizer` config to do it automatically.

### Sanitizer Configuration

The example of sanitizer configuration

```javascript
let sanitizerConfig = {
  b: true, // leave <b>
  p: true, // leave <p>
}
```

Keys of config object is tags and the values is a rules.

#### Rule

Rule can be boolean, object or function. Object is a dictionary of rules for tag's attributes.

You can set `true`, to allow tag with all attributes or `false|{}` to remove all attributes,
but leave tag.

Also you can pass special attributes that you want to leave.

```javascript
a: {
  href: true
}
```

If you want to use a custom handler, use should specify a function
that returns a rule.

```javascript
b: function(el) {
  return !el.textContent.includes('bad text');
}
```

or

```javascript
a: function(el) {
  let anchorHref = el.getAttribute('href');
  if (anchorHref && anchorHref.substring(0, 4) === 'http') {
    return {
      href: true,
      target: '_blank'
    }
  } else {
    return {
      href: true
    }
  }
}
```

### Manual sanitize

Call API method `sanitizer.clean()` at the save method for each field in returned data.

```javascript
save() {
  return {
    text: this.api.sanitizer.clean(taintString, sanitizerConfig)
  }
}
```

### Automatic sanitize

If you pass the sanitizer config as static getter, Editor.js will automatically sanitize your saved data.

Note that if your Tool is allowed to use the Inline Toolbar, we will get sanitizing rules for each Inline Tool
and merge with your passed config.

You can define rules for each field

```javascript
static get sanitize() {
  return {
    text: {},
    items: {
      b: true, // leave <b>
      a: false, // remove <a>
    }
  }
}
```

Don't forget to set the rule for each embedded subitems otherwise they will
not be sanitized.

if you want to sanitize everything and get data without any tags, use `{}` or just
ignore field in case if you want to get pure HTML

```javascript
static get sanitize() {
  return {
    text: {},
    items: {}, // this rules will be used for all properties of this object
    // or
    items: {
      // other objects here won't be sanitized
      subitems: {
        // leave <a> and <b> in subitems
        a: true,
        b: true,
      }
    }
  }
}
```

## Conversion config <a name="conversion-config"></a>

Editor.js has a Conversion Toolbar that allows user to convert one Block to another.

![](assets/6c1f708b-a30c-4ffd-a427-5b59a1a472e0.jpg)

1. You can add ability to your Tool to be converted. Specify «export» property of `conversionConfig`.
2. You can add ability to convert other Tools to your Tool. Specify «import» property of `conversionConfig`.

Conversion Toolbar will be shown only near Blocks that specified an «export» rule, when user selected almost all block's content.
This Toolbar will contain only Tools that specified an «import» rule.

Example:

```js
class Header {
  constructor(){
    this.data = {
       text: '',
       level: 2
    }
  }

  /**
   * Rules specified how our Tool can be converted to/from other Tool.
   */
  static get conversionConfig() {
    return {
      export: 'text', // this property of tool data will be used as string to pass to other tool
      import: 'text' // to this property imported string will be passed
    };
  }
}
```

### Your Tool -> other Tool

The «export» field specifies how to represent your Tool's data as a string to pass it to other tool.

It can be a `String` or a `Function`.

`String` means a key of your Tool data object that should be used as string to export.

`Function` is a method that accepts your Tool data and compose a string to export from it. See example below:

```js
class ListTool {
  constructor(){
    this.data = {
      items: [
        'Fisrt item',
        'Second item',
        'Third item'
      ],
      type: 'ordered'
    }
  }

  static get conversionConfig() {
    return {
      export: (data) => {
        return data.items.join('.'); // in this example, all list items will be concatenated to an export string
      },
      // ... import rule
    };
  }
}
```

### Other Tool -> your Tool

The «import» rule specifies how to create your Tool's data object from the string created by original block.

It can be a `String` or a `Function`.

`String` means the key in tool data that will be filled by an exported string.
For example, `import: 'text'` means that `constructor` of your block will accept a `data` object with `text` property filled with string composed by original block.

`Function` allows you to specify own logic, how a string should be converted to your tool data. For example:

```js
class ListTool {
  constructor(data){
    this.data = data || {
      items: [],
      type: 'unordered'
    }
  }

  static get conversionConfig() {
    return {
      // ... export rule

      /**
       * In this example, List Tool creates items by splitting original text by a dot symbol.
       */
      import: (string) => {
        const items = string.split('.');

        return {
          items: items.filter( (text) => text.trim() !== ''),
          type: 'unordered'
        };
      }
    };
  }
}
```

## Block Lifecycle hooks

### `rendered()`

Called after Block contents is added to the page

### `updated()`

Called each time Block contents is updated

### `removed()`

Called after Block contents is removed from the page but before Block instance deleted

### `moved(MoveEvent)`

Called after Block was moved. `MoveEvent` contains `fromIndex` and `toIndex`
respectively.


---

<!-- Source: docs/usage.md -->

---

# So how to use Editor.js

## Basics

Editor.js is a Block-Styled editor. Blocks is a structural units, of which the Entry is composed. 
For example, `Paragraph`, `Heading`, `Image`, `Video`, `List` are Blocks. Each Block is represented by a Plugin. 
We have [many](http://github.com/editor-js/) ready-to-use Plugins and the [simple API](tools.md) for creation new ones.

So how to use the Editor after [Installation](installation.md).

- Create new Blocks by Enter or with the Plus Button
- Press `TAB` or click on the Plus Button to view the Toolbox
- Press `TAB` again to leaf Toolbox and select a Block you need. Then press Enter.


 ![](https://github.com/editor-js/list/raw/master/assets/example.gif)
 
- Select text fragment and apply a style or insert a link from the Inline Toolbar

![](assets/7ccbcfcd-1c49-4674-bea7-71021468a1bd.jpg)

- Use «three-dots» button on the right to open Block Settings. From here, you can move and delete a Block 
or apply Tool's settings, if it provided. For example, set a Heading level or List style.

![](assets/01a55381-46cd-47c7-b92e-34765434f2ca.jpg)   

## Shortcuts

We really appreciate shortcuts. So there are few presets. 

Action | Shortcut | Restrictions
-- | -- | --
`TAB` | Show/leaf a Toolbox. | On empty block
`SHIFT+TAB` | Leaf back a Toolbox. | While Toolbox is opened
`ENTER` | Create a Block | While Toolbox is opened and some Tool is selected
`CMD+B` | Bold style | On selection
`CMD+I` | Italic style | On selection
`CMD+K` | Insert a link | On selection
 
Also we support shortcuts on the all type of Tools. Specify a shortcut with the Tools configuration. For example:

```js
var editor = new EditorJS({
  //...
  tools: {
    header: {
      class: Header,
      shortcut: 'CMD+SHIFT+H'
    },
    list: {
      class: List,
      shortcut: 'CMD+SHIFT+L'
    }
  }
  //...
 });

```

## Autofocus

If you want to focus Editor after page has been loaded, you can enable autofocus by passing `autofocus` to the initial config


```js
var editor = new EditorJS({
  //...
  autofocus: true
  //...
 });

```

## Holder
The `holder` property supports an id or a reference to dom element.

```js
var editor = new EditorJS({
  holder: document.querySelector('.editor'),
})

var editor2 = new EditorJS({
  holder: 'codex-editor' // like document.getElementById('codex-editor')
})
```



## Placeholder

By default Editor\`s placeholder is empty.

You can pass your own placeholder via `placeholder` field:


```js
var editor = new EditorJS({
  //...
  placeholder: 'My awesome placeholder'
  //...
 });

```

If you are using your custom `Initial Block`, `placeholder` property is passed in `config` to your Tool constructor.

## Log level

You can specify log level for Editor.js console messages via `logLevel` property of configuration:

```js
var editor = new EditorJS({
  //...
  logLevel: 'WARN'
  //..
})
```

Possible values:

| Value     | Description                  |
| -----     | ---------------------------- |
| `VERBOSE` | Show all messages            |
| `INFO`    | Show info and debug messages |
| `WARN`    | Show errors and warns only   |
| `ERROR`   | Show errors only             |
  
