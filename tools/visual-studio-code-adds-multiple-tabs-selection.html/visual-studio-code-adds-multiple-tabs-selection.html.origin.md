With Visual Studio Code 1.90, otherwise known as the May 2024 release of the editor, Microsoft has introduced the ability to select multiple editor tabs at once and the ability to configure a preferred profile for new windows.
Visual Studio Code 1.90 was published on
[June 5](https://code.visualstudio.com/updates/v1_90). It can be downloaded for Windows, Linux, and MacOS from the [Visual Studio Code website](https://code.visualstudio.com/Download).
With the editor tabs multi-select capability, developers now can select multiple tabs simultaneously, enabling the application of actions to multiple editors at once. This new capability lets developers move, pin, or close several tabs with a single action.
Developers now can specify which profile should be used when opening a new window by configuring the
window.netWindowProfile setting. Previously, when opening a new VS Code window, the
[profile](https://code.visualstudio.com/docs/editor/profiles) of the active window was used, or the default profile was used if there was no active window.
VS Code 1.90 also brings improvemens to source control and editor actions. For source control, workbench commands were added for creating keyboard shortcuts. These include capabilities to focus on the next or previous source control input field or to focus on the next or previous resource group within a repository. For editor actions, Microsoft is introducing an
Always Show Editor Actions setting. When this setting is enabled, editor title actions of each editor group are shown, regardless of whether the editor is active or not. When this setting is not enabled, editor actions are shown only when the editor is active.
Notebooks in VS Code 1.90 now support a new kind of Code Action, which is defined with the
notebook.format Code Action Kind prefix. These Code Actions can be triggered automatically via an explicit formatting request or a formatting on save request.
VS Code 1.90 follows last month’s
[VS Code 1.89 release](https://www.infoworld.com/article/3715442/visual-studio-code-smooths-branch-switching.html) which emphasized capabilities such as enhanced branch switching and middle-click paste support. Other new capabilities in VS Code 1.90:
- Enabling the new
Always Show Editor Actionssetting will show editor title actions of each editor group regardless of whether the editor is active or not.
- When the setting
Debounce position changesis enabled, developers can use the
Signal options delayssetting to customize the debouncing time for various accessibility signals. This is an experimental capability.
- When a command lacks a keybinding assignment, developers now can configure it from within the accessibility help dialog.
- The canvas renderer, deprecated in VS Code 1.89, is now removed completely. On machines that do not support WebGL2, the terminal will use the DOM-based renderer.
- The setting
terminal.integrated.rescaleOverlappingGlyphs, introduced as a preview feature in
[VS Code 1.88](https://www.infoworld.com/article/3714982/visual-studio-code-finalizes-test-coverage-api.html), is now enabled by default. [GitHub Copilot Enterprise](https://www.infoworld.com/article/3713186/github-ships-github-copilot-enterprise.html)users in VS Code now can ask questions enriched with context from web results and enterprise knowledge bases. To try out this capability, developers must install the latest release of Copilot Chat.
- Two new APIs for extension authoring, the
[Chat Participants API](https://code.visualstudio.com/api/extension-guides/chat)and the [Language Model API](https://code.visualstudio.com/api/extension-guides/language-model), enable VS Code extensions to participate in chat and to access language models.