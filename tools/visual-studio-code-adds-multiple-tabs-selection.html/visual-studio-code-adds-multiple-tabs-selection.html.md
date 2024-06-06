
<!--
title: VSCode添加多选项卡选择功能
cover: https://images.idgesg.net/images/article/2023/01/shutterstock_561382627-100936182-large.jpg?auto=webp&quality=85,70
-->

从 VS Code 1.90 开始，用户可以选择多个选项卡，并一次对多个编辑器应用操作。

> 译自 [Visual Studio Code adds multiple tabs selection](https://www.infoworld.com/article/3715357/visual-studio-code-adds-multiple-tabs-selection.html)，作者 Paul Krill。

Visual Studio Code 1.90 中，也称为编辑器的 2024 年 5 月版本，Microsoft 引入了同时选择多个编辑器选项卡以及为新窗口配置首选配置文件的功能。

Visual Studio Code 1.90 于 [6 月 5 日](https://code.visualstudio.com/updates/v1_90) 发布。可以从 [Visual Studio Code 网站](https://code.visualstudio.com/Download) 下载适用于 Windows、Linux 和 MacOS 的版本。

借助编辑器选项卡多选功能，开发人员现在可以同时选择多个选项卡，从而能够对多个编辑器同时应用操作。此新功能使开发人员能够通过单个操作移动、固定或关闭多个选项卡。

开发人员现在可以通过配置 `window.netWindowProfile` 设置来指定打开新窗口时应使用哪个配置文件。以前，在打开新的 VS Code 窗口时，将使用活动窗口的 [配置文件](https://code.visualstudio.com/docs/editor/profiles)，或者如果没有活动窗口，则使用默认配置文件。

VS Code 1.90 还改进了源代码管理和编辑器操作。对于源代码管理，添加了用于创建键盘快捷键的工作台命令。其中包括专注于下一个或上一个源代码输入字段或专注于存储库中的下一个或上一个资源组的功能。对于编辑器操作，Microsoft 引入了 **始终显示编辑器操作（Always Show Editor Actions）** 设置。启用此设置后，将显示每个编辑器组的编辑器标题操作，无论编辑器是否处于活动状态。禁用此设置后，仅在编辑器处于活动状态时才显示编辑器操作。

VS Code 1.90 中的笔记本现在支持一种新的代码操作，该操作使用 `notebook.format` 代码操作类型前缀定义。可以通过显式格式化请求或保存时格式化请求自动触发这些代码操作。

VS Code 1.90 遵循上个月的 [VS Code 1.89 版本](https://www.infoworld.com/article/3715442/visual-studio-code-smooths-branch-switching.html)，该版本强调了增强分支切换和中键单击粘贴支持等功能。VS Code 1.90 中的其他新功能：

- 启用新的 **始终显示编辑器操作** 设置将显示每个编辑器组的编辑器标题操作，无论编辑器是否处于活动状态。
- 当设置 **消除位置更改的抖动** 启用时，开发人员可以使用 **信号选项延迟** 设置来自定义各种辅助功能信号的去抖时间。这是一项实验性功能。
- 当命令缺少键绑定分配时，开发人员现在可以从辅助功能帮助对话框中对其进行配置。
- 在 VS Code 1.89 中弃用的画布渲染器现在已完全删除。在不支持 WebGL2 的机器上，终端将使用基于 DOM 的渲染器。
- 设置 `terminal.integrated.rescaleOverlappingGlyphs` 在 [VS Code 1.88](https://www.infoworld.com/article/3714982/visual-studio-code-finalizes-test-coverage-api.html) 中作为预览功能引入，现在默认启用。
- VS Code 中的 [GitHub Copilot Enterprise](https://www.infoworld.com/article/3713186/github-ships-github-copilot-enterprise.html) 用户现在可以提出包含来自网络结果和企业知识库的上下文的问题。要试用此功能，开发人员必须安装最新版本的 Copilot Chat。
- 两个用于扩展创作的新 API，[聊天参与者 API](https://code.visualstudio.com/api/extension-guides/chat) 和 [语言模型 API](https://code.visualstudio.com/api/extension-guides/language-model)，使 VS Code 扩展能够参与聊天并访问语言模型。