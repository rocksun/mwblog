
<!--
title: VSCode的10个巧妙技巧
cover: ./cover.png
-->

即使没有让 Visual Studio Code 成为每个开发人员的强大工具的大量扩展，Microsoft 的开源编程编辑器默认情况下也加载了许多巧妙的功能。但是，其中一些有用的功能并不明显，即使对于经验丰富的用户也是如此。而且，随着 VS Code 的每次新版本发布，更多便捷的功能被推出——通常会保持在水线以下。

> 译自 [10 neat tricks for Visual Studio Code](https://www.infoworld.com/article/3602661/6-neat-tricks-for-visual-studio-code.html)，作者 Serdar Yegulalp。

以下是 10 个你可能不知道的有用的 Visual Studio Code 提示和快捷方式。从初学者到经验丰富的资深用户，对各个等级的 VS Code 开发者都具有吸引力。

## 查找任何 VS Code 命令

想要在 VS Code 中查找任何命令吗？按 **Ctrl-Shift-P** 并开始输入。命令面板（按其名称）可让你快速访问任何已注册的命令，包括加载项提供的命令。此外，如果给定命令关联了键绑定，它将显示在键入搜索的下拉列表中。通过这种方式，你可以直接使用快捷方式。

![IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-command-palette-100873300-orig.jpg?auto=webp&quality=85,70)

*在 VS Code 命令面板中键入以搜索任何命令，包括其键绑定。*

## 使用 Ctrl-` 打开和关闭 VS Code 终端

VS Code 中的弹出式终端窗口非常方便。无需切换到另一个应用程序窗口来处理它。按 **Ctrl-`**（Ctrl 后跟反引号键）也可以轻松访问它。按这些键只需要一只手，因此你可以打开或关闭窗口，而无需触摸鼠标。此外，当你打开光标时，光标的焦点会转到终端窗口，因此你可以直接打开它并开始键入。

![IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-terminal-100873301-orig.jpg?auto=webp&quality=85,70)

*使用单手快捷键开启和关闭 VS Code 的集成终端*

## 在 VS Code 中使用语音转文本

想与 VS Code 交谈而不是键入吗？ [VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech) 扩展允许你通过按 **Ctrl-Alt-V**（或你选择的其他键绑定）直接在编辑器中听写文本。文本转语音引擎完全是本地的，因此它不需要网络连接即可使用。Microsoft Windows、macOS 和 Linux 都受支持。

![IDG](https://images.idgesg.net/images/article/2024/03/voice-100962710-orig.jpg?auto=webp&quality=85,70)

*VS Code 语音扩展在操作中。光标附近的麦克风图标表示扩展程序正在监听输入。*

## 在 VS Code 文档中使用多个光标

在 VS Code 中编辑文档的一种相当神奇的方法是定义多个光标。没错——你可以一次在文档中的多个位置键入。

如果你按住 Alt 键并单击某个位置，你将放下一个新光标。每个光标都将同时接受相同的键命令——例如，这是一种一次在多行上输入样板文本的便捷方法。

添加光标的另一种方法是按住 **Ctrl+Alt** 并按向上或向下箭头键。这样做会在当前光标上方或下方的行中插入光标——这对于在文本列中工作很有用。

另一个巧妙的技巧：你可以通过按 **Ctrl-Shift-L** 在所选文本的每个实例中插入光标。你还可以通过按 **Shift-Alt** 和左右箭头来控制多个光标的选择大小。

要返回到单个光标，只需按 Escape 键。

![IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-cursors-100873298-orig.jpg?auto=webp&quality=85,70)

*VS Code 允许您使用多个光标同时在一个文档中的多个位置处键入。*

## 将选项卡分离到浮动窗口中

自 VS Code 早期以来，用户就要求能够从主窗口分离选项卡并在单独的窗口中打开它。Microsoft 于 2023 年 11 月提供了此功能。右键单击主窗口中的选项卡，然后选择“移至新窗口”以分离选项卡。要重新附加它，请将选项卡拖回到原始窗口上的选项卡列表中。

![IDG](https://images.idgesg.net/images/article/2024/03/tabs-100962711-orig.jpg?auto=webp&quality=85,70)

*可将标签分离并转换为独立窗口，并在桌面上自由移动。请注意，分离的窗口中不提供主窗口的菜单。*

## 从多个文档中获取基于单词的建议

VS Code 可以在您键入大多数常见纯文本文档类型时提供基于单词的建议。但是，默认情况下，建议仅从当前文档或相同类型的打开文档中提供。

最近引入的一项功能允许您从所有当前打开的文件中查找建议。将 `editor.wordBasedSuggestionsMode` 配置选项设置为 `allDocuments` 以从每个已打开的文件中获取建议，而不仅仅是您当前正在编辑的文件或具有相同扩展名的打开文件。如果您有包含应用程序类型存根的文件，但与您正在编辑的文件不共享文件扩展名，这将非常方便。

![IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-word-based-suggestions-100873302-orig.jpg?auto=webp&quality=85,70) 

*从所有打开的文档中启用 VS Code 中的单词建议。建议“db_context”来自一个打开的代码文件*。

## 查看 VS Code 的内部进程列表

操作系统具有实用程序，如 Windows 的任务管理器，可让您查看系统当前正在运行的进程列表。类似地，VS Code 有自己的内部进程资源管理器，可让您查看在代码编辑器中运行的所有子进程的列表——每个窗口、扩展、外部生成的进程等。对于每个进程，进程资源管理器会显示进程 ID 以及 CPU 和内存使用情况。

要打开进程资源管理器，只需从帮助菜单中选择“打开进程资源管理器”，或在命令面板中搜索“进程资源管理器”。您可以右键单击进程以复制其信息或将其终止。请注意，您无法对视图进行排序，但使用最多内存或 CPU 的进程将被突出显示。

![IDG](https://images.idgesg.net/images/article/2021/01/visual-studio-code-process-explorer-100873299-orig.jpg?auto=webp&quality=85,70) 

*VS Code 的进程资源管理器可让您查看应用程序的所有正在运行的进程，包括扩展。*

## 将文件标记为只读

有时您希望确保不会意外修改工作区中的文件。VS Code 能够将活动编辑器标记为只读，或切换其只读状态。默认情况下，没有为这些行为分配任何键绑定，但您可以从命令面板中访问它们（键入“只读”以搜索它们）并根据需要分配键。

![IDG](https://images.idgesg.net/images/article/2024/03/readonly-100962712-orig.jpg?auto=webp&quality=85,70) 

*将文件标记为只读以进行会话可以防止意外修改不应更改的关键配置数据。*

## 使用配置文件管理工作流

VS Code 可以处理任意数量的不同语言和文件类型。但您可能不希望为每个语言和文件类型使用相同的自定义设置。Python 项目需要与 Java 或 C# 项目不同的自定义设置。为此，VS Code 允许您使用 [配置文件(Profile)](https://code.visualstudio.com/updates/v1_75#_profiles) 将各种自定义设置组合在一起，并将其保存在一个通用名称下。您可以通过配置文件修改和保存设置、键盘快捷键、用户代码段和任务以及扩展，并且可以与队友共享您的配置文件以保持工作流同步。

![IDG](https://images.idgesg.net/images/article/2024/03/profile-100962713-orig.jpg?auto=webp&quality=85,70) 

*配置文件可用于存储和共享针对每个工作流或语言自定义的设置组。*

## 将 VS Code 作为便携式应用程序运行

通常，您会像运行成熟的 Visual Studio 或 Microsoft Office 一样，将 Visual Studio Code 作为正式安装的应用程序运行。但在某些情况下，便携式运行 VS Code 会很有用——即从可移动驱动器或系统上的奇特目录运行，而无需正式安装它。为此，VS Code 提供了 [便携模式](https://code.visualstudio.com/docs/editor/portable)，该模式受应用程序的 `.zip/` `.tar.gz` 存档版本支持。

请注意，必须手动对 VS Code 的便携副本进行任何升级，方法是从旧安装将用户数据复制到新安装。另请注意，您可以将现有的 VS Code 安装迁移到便携模式，但只能通过将数据目录从正式安装的 VS Code 版本复制到便携版本的新副本来执行此操作。您无法“就地”将已安装的 VS Code 实例转换为便携版。