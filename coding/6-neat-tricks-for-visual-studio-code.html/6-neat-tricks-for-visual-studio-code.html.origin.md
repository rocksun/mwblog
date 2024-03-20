Even without the oodles of extensions that make Visual Studio Code a power tool for every developer, Microsoft’s open source programming editor is loaded with nifty features by default. However, some of these useful features are not obvious, even to seasoned users. And with each new release of VS Code, more handy features get rolled in—often remaining below the waterline.
Here are 10 useful Visual Studio Code tips and shortcuts that you might not know about. Most will appeal to developers of all levels of VS Code expertise, from the newcomer to the seasoned veteran.
## 10 ways to boost your productivity in VS Code
- Find any VS Code command
- Use Ctrl-` to open and shut the VS Code terminal
- Use speech-to-text in VS Code
- Use multiple cursors in a VS Code document
- Detach tabs into floating windows
- Get word-based suggestions from multiple documents
- See VS Code’s internal process list
- Mark files as read-only
- Use Profiles to manage workflows
- Run VS Code as a portable application
### Find any VS Code command
Want to find a command, any command, in VS Code? Press
**Ctrl-Shift-P** and start typing. The command palette, as it’s called, gives you fast access to any registered command, including those provided by add-ons. Plus, if there’s a key binding associated with a given command, it’s displayed in the type-to-search drop-down list. This way, you can cut straight to the shortcut in the future. [IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-command-palette-100873300-orig.jpg?auto=webp&quality=85,70) ![visual studio code command palette]()
Type in the VS Code command palette to search for any command, including its key bindings.
### Use Ctrl-` to open and shut the VS Code terminal
The pop-open terminal window in VS Code is a massive convenience. No need to switch out to another application window to deal with it. It’s also readily accessible by pressing
**Ctrl-`** (Ctrl followed by the backtick key). Pressing these keys requires only one hand, so you can kick open the window or shut it without touching your mouse. Also, the focus for the cursor goes to the terminal window when you open it, so you can just open it and start typing. [IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-terminal-100873301-orig.jpg?auto=webp&quality=85,70) ![visual studio code terminal]()
Open and shut VS Code’s integrated terminal with a one-handed keystroke
### Use speech-to-text in VS Code
Want to talk to VS Code instead of typing? The
[VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech) extension lets you dictate text directly into the editor by pressing **Ctrl-Alt-V** (or another keybinding of your choice). The text-to-speech engine is entirely local, so it does not need a network connection to be useful. Microsoft Windows, macOS, and Linux are all supported. [IDG](https://images.idgesg.net/images/article/2024/03/voice-100962710-orig.jpg?auto=webp&quality=85,70) ![The VS Code Speech extension in action.]()
The VS Code Speech extension in action. The microphone near the cursor indicates the extension is listening for input.
### Use multiple cursors in a VS Code document
One fairly wizardly way to edit a document in VS Code is to define multiple cursors. That’s right—you can type in a document in more than one place at a time.
If you hold down the Alt key and click somewhere, you’ll put down a new cursor. Each cursor will accept the same key commands at the same time—a handy way to enter boilerplate text on multiple lines at once, for example.
Another way to add cursors is to hold
**Ctrl+Alt** and press the up or down arrow keys. Doing so will insert cursors in the lines above or below the current one—useful for working in columns of text.
Another slick move: You can insert a cursor at every instance of a selected piece of text by hitting
**Ctrl-Shift-L**. You can also control the selection size of multiple cursors by pressing **Shift-Alt** and the left or right arrow.
To go back to a single cursor, just hit the Escape key.
[IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-cursors-100873298-orig.jpg?auto=webp&quality=85,70) ![visual studio code cursors]()
VS Code lets you type in multiple places in a document at once using multiple cursors.
### Detach tabs into floating windows
Since VS Code's early days, users have asked for the ability to detach a tab from the main window and open it in a separate window. Microsoft made that capability available in November 2023. Right-click on a tab in the main window and select "Move into new window" to detach the tab. To reattach it, drag the tab back to the tab list on the original window.
[IDG](https://images.idgesg.net/images/article/2024/03/tabs-100962711-orig.jpg?auto=webp&quality=85,70) ![Detachable tabs can be moved around the desktop.]()
Tabs can be detached and converted into standalone windows and moved freely around the desktop. Note that the menus for the main window are not available in a detached window.
### Get word-based suggestions from multiple documents
VS Code can make word-based suggestions as you type in most common plain-text document types. By default, however, suggestions are only supplied from the current document or open documents of the same type.
A recently introduced feature lets you find suggestions from all currently open files. Set the
editor.wordBasedSuggestionsMode configuration option to
allDocuments to get suggestions from every file that’s open, not just what you’re currently editing or open files with the same extension. This is handy if you have files that hold type stubs for your application, but don’t share a file extension with the file you’re editing.
[IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-word-based-suggestions-100873302-orig.jpg?auto=webp&quality=85,70) ![visual studio code word based suggestions]()
Enable word suggestions in VS Code from all open documents. The suggestion “db_context” comes from an open code file.
### See VS Code’s internal process list
Operating systems have utilities, like Windows’ Task Manager, that let you see a list of the system’s currently running processes. Similarly, VS Code has its own internal Process Explorer that lets you see a list of all the subprocesses running inside the code editor—every window, extension, externally spawned process, and so on. For each process, Process Explorer displays the process ID and the CPU and memory usage.
To open Process Explorer, just select “Open Process Explorer” from the Help menu, or search for “Process Explorer” in the command palette. You can right-click on a process to copy its information or to kill it. Note that you can’t sort the view, but the process using the most memory or CPU will be highlighted.
[IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-process-explorer-100873299-orig.jpg?auto=webp&quality=85,70) ![visual studio code process explorer]()
VS Code’s Process Explorer lets you see all of the application’s running processes including extensions.
### Mark files as read-only
Sometimes you want to ensure you don't accidentally modify a file in your workspace. VS Code has the ability to mark the active editor read-only, or to toggle its read-only status. By default, no keybindings are assigned to these behaviors, but you can access them from the command palette (type "read-only" to search for them) and assign keys as desired.
[IDG](https://images.idgesg.net/images/article/2024/03/readonly-100962712-orig.jpg?auto=webp&quality=85,70) ![Mark a file in VS Code as read-only.]()
Marking a file as read-only for a session can prevent, for example, accidentally modifying crucial configuration data that isn't meant to change.
### Use Profiles to manage workflows
VS Code can work with any number of different languages and file types. But you may not want the same set of customizations for each one. A Python project demands a different set of customizations than a Java or C# project. To that end, VS Code lets you use
[Profiles](https://code.visualstudio.com/updates/v1_75#_profiles) to gang together various customizations and save them under a common name. You can modify and save settings, keyboard shortcuts, user snippets and tasks, and extensions by way of a profile, and you can share your profiles with teammates to keep workflows in sync. [IDG](https://images.idgesg.net/images/article/2024/03/profile-100962713-orig.jpg?auto=webp&quality=85,70) ![Use profiles to store and share customized settings.]()
Profiles can be used to store and share groups of settings customized for each workflow or language.
### Run VS Code as a portable application
As a rule, you’ll run Visual Studio Code as a formally installed application, just like you would full-blown Visual Studio or Microsoft Office. But there may be scenarios where it’s useful to run VS Code portably—i.e., from a removable drive, or from an odd directory on your system without formally installing it. To do this, VS Code provides
[Portable Mode](https://code.visualstudio.com/docs/editor/portable), which is supported on the
.zip/
.tar.gz archived version of the application.
Note that any upgrades to a portable copy of VS Code have to be made by hand, by copying the user data from the old install to the new one. Also note that you can migrate an existing VS Code installation to portable mode, but you can only do this by copying the data directory from a formally installed VS Code version to a new copy of the portable version. You can’t “in-place” convert an installed VS Code instance to a portable edition.