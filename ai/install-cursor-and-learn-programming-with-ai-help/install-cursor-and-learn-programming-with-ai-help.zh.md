我不太喜欢将 AI 作为一种捷径。另一方面，我完全可以接受将其作为一种学习工具。AI 非常擅长教授[编程语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/)。是的，你必须小心，确保自己没有被错误误导，但通过后续查询，我发现你几乎总是可以得到 AI 的帮助来纠正它的错误。

现在市场上有大量的 [AI 驱动的 IDE](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/)，甚至还有终端应用程序（如 Warp）也包含强大的 AI，可以做同样的事情。

其中一个 IDE 叫做 [Cursor](https://cursor.com/en)。你可以将 [Cursor 融入你的工作流程](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow)，并了解这个新的 IDE 如何[为 AI 驱动的编程工具设定标准](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance)。但是，在进入这些阶段之前，你需要安装和配置 Cursor，使其能够帮助你与 AI 交互，学习编程的艺术。

让我们开始吧。

## 你需要什么

因为 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 是我首选的操作系统（并且因为它越来越受欢迎），所以我将在 Pop!\_OS Linux 上演示这个过程。你也可以在 macOS 和 Windows 上安装这个 IDE，从下载页面下载安装文件，然后按照在你选择的平台上安装应用程序的标准步骤进行操作。

如果你使用的是 Linux，唯一的选择是 AppImage，这很好，因为这意味着 Cursor 将在任何 Linux 桌面发行版上运行。

## 在 Linux 上安装 Cursor

在你下载 Cursor AppImage 之前，我建议你安装一个名为 Gear Lever 的方便应用程序，它可以使 AppImage 的使用更加容易。Gear Lever 可以在你的桌面菜单中创建一个启动器，这样你就不必从命令行运行 AppImage。

Gear Lever 可以通过以下命令安装在任何支持 Flatpak 的 Linux 发行版上：

```
flatpak install flathub it.mijorus.gearlever
```

安装完成后，注销并重新登录，以确保 Gear Lever 启动器已添加到你的桌面菜单中。

接下来，从 Cursor [下载页面](https://cursor.com/downloads)下载 AppImage。

下载完成后，打开 Gear Lever 并单击左上角的“打开”按钮（图 1）。

[![图 1 显示了 Gear Lever 主窗口的屏幕截图，其中列出了已安装的应用程序。](https://cdn.thenewstack.io/media/2025/08/bef0f5f3-gearlever_ns.jpg)](https://cdn.thenewstack.io/media/2025/08/bef0f5f3-gearlever_ns.jpg)

图 1. Gear Lever 主窗口。

导航到包含 Cursor AppImage 的文件夹并选择该文件。然后，系统将提示你将 AppImage 移动到桌面菜单。执行此操作，你就可以启动该应用程序了。

## 使用 Cursor

首次启动 Cursor 时，你必须完成一个欢迎向导，在此期间你需要注册一个帐户。你可以使用电子邮件地址或使用 [Google](https://cloud.google.com/?utm_content=inline+mention) 等帐户注册。

完成后，就可以开始使用 Cursor 了。

让我引导你完成使用 Cursor 的 AI 功能的过程。

你必须做的第一件事是选择一个模型。你可能知道，某些模型需要一个帐户（甚至是付费的）和/或一个 API。对于你的第一步，我建议选择一个免费模型。为此，请在 Cursor 窗口右下角的查询字段中找到模型下拉列表。从该下拉列表中（图 2），选择一个像 deepseek-v3.1 这样的模型（可以免费使用）。选择要使用的模型后，运行你的查询。

[![图 2 是 Cursor 的屏幕截图，显示你可以选择任何你想要的模型，但如果你选择付费模型，你必须使用你的帐户和（可能）一个 API。](https://cdn.thenewstack.io/media/2025/08/7c5196d3-cursor_llm.jpg)](https://cdn.thenewstack.io/media/2025/08/7c5196d3-cursor_llm.jpg)

图 2. 你可以选择任何你想要的模型，但如果你选择付费模型，你必须使用你的帐户和（可能）一个 API。

例如，让 Cursor 编写一个 Python 程序，该程序接受用户输入姓名、地址、电子邮件和电话。该提示可能如下所示：

*编写一个 Python 程序，该程序接受用户输入姓名、地址、电子邮件和电话，然后将其写入名为 users.txt 的文件。*

在按 Enter 键之前，重要的是你要从 Agent 切换到 Ask，这可以通过模型选择器左侧的下拉列表完成。如果你尝试使用 Agent，系统将提示你注册 Pro 或 Business 计划。

然后，Cursor 将开始编写应用程序，并且速度非常快。

此时，我尝试使用“不调试运行”选项，但出现了一个错误。这不是 Python 错误，而是 Cursor 无法在我的主目录中找到 \_\_main\_\_ 模块。

为此，我复制了代码，将其粘贴到文件 *collect\_user\_info.py* 中，然后使用以下命令运行它：

```
python3 collect_user_info.py
```

你猜怎么着？代码运行完美。

然后我回去进行后续操作，并添加（通过查询）：

*向程序添加接受用户输入性别的功能。*

Cursor 开始工作并生成了新代码。我覆盖了原始文件，以查看新代码是否能按预期工作。成功了——运行完美。

在提供的代码的末尾，Cursor 甚至会为你提供运行新 Python 程序的步骤。

我并不是说你应该安装 Cursor 并开始使用它来构建你所有的应用程序，但对于那些试图学习如何编码的人来说，这是一个将梦想变为现实的好方法。

尝试一下 Cursor，看看它是否能帮助你理解你想要学习的任何编程语言。