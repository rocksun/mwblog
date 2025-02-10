# Windsurf：与你一同思考和编码的 Agentic IDE

![Windsurf：与你一同思考和编码的 Agentic IDE 的特色图片](https://cdn.thenewstack.io/media/2025/01/1beac1f7-getty-images-b2lu5f9rohq-unsplash-1024x662.jpg)

多年来，我测试过几款 [IDE](https://thenewstack.io/best-open-source-ides/)，其中许多都提供了你在这种工具中期望的相同、经过验证的功能。这些 IDE 中的许多都功能强大，有助于使开发过程顺畅进行。

其中一些甚至在组合中添加了 AI。

然后是 [Windsurf](https://windsurfai.org/)，它声称是市场上第一个“agentic IDE”。这种描述让我措手不及，所以我必须弄清楚“agentic”是什么意思。根据 Merriam-Webster 的说法，agency 指的是有能力独立实现结果（“像代理一样运作”）或拥有这种能力、手段或力量（“拥有 agency”）的某人或某物。

如今，Agency 是一个强大的词，因为它描述了个人拥有权力和资源来实现其潜力的能力。没有 agency，我们能完成任何事情吗？可能不能，因此拥有一个能够增强 agency 的 IDE 可能会改变游戏规则。

Windsurf 的开发者们全力投入 AI，而这一切都始于 [Codeium](https://codeium.com/)。

Codeium 是一种 AI 驱动的 [代码自动完成工具](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/)，旨在通过为 70 多种 [编程语言](https://thenewstack.io/programming-languages/) 提供代码建议和完成来帮助开发人员。虽然 Codeium 与多个 IDE 集成，但 Windsurf 是第一个内置如此深入的 AI 功能的 IDE。将 Codeium AI 融入 Windsurf 的目标是使其能够与你协作，以帮助你完成复杂的任务。

Windsurf 具有工作区、Cascade（用于深入了解代码库和完全的上下文感知）、Flows（帮助你和 AI 始终在同一状态下运行）、多文件编辑、显式操作的自动推理等等。

根据 Codeium（Windsurf 背后的公司）的说法，“我们从 AI 使用的现有范例开始。Copilot 非常棒，因为它们与开发人员具有协作性——人始终参与其中。话虽如此，为了让人参与其中，Copilot 通常仅限于短范围的任务。另一方面，Agent 非常棒，因为 AI 可以独立迭代以完成更大的任务。缺点是你失去了协作方面，这就是为什么我们还没有看到 agentic IDE（尚未）。IDE 将是多余的。Copilot 和 Agent 都非常强大，并且有其用例，但通常被认为是互补的，因为它们的优势和劣势确实是互补的。”

听起来很棒，对吧？但它是如何工作的呢？

首先，让我们安装它。

## 如何安装 Windsurf

我将演示在 [Pop!_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) 上进行安装，该系统基于 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)。首先要做的是打开你的终端窗口，并使用以下命令添加所需的存储库：

```bash
curl -fsSL “https://windsurf-stable.codeiumdata.com/wVxQEIWkwPUEAGf3/windsurf.gpg” | sudo gpg –dearmor -o /usr/share/keyrings/windsurf-stable-archive-keyring.gpg echo “deb [signed-by=/usr/share/keyrings/windsurf-stable-archive-keyring.gpg arch=amd64] https://windsurf-stable.codeiumdata.com/wVxQEIWkwPUEAGf3/apt stable main” | sudo tee /etc/apt/sources.list.d/windsurf.list > /dev/null
```

添加存储库后，更新 apt：

```bash
sudo apt-get update
```

最后，使用以下命令安装 Windsurf：

```bash
sudo apt-get install windsurf -y
```

安装完成后，你将在桌面菜单中找到 Windsurf 启动器。启动该应用程序，你将看到一个登录屏幕，你可以在其中注册一个免费帐户。之后，你可以选择是否要从 [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) 导入你的设置，或者从头开始（**图 1**）。

**图 1**
![](https://cdn.thenewstack.io/media/2025/01/ddd04c61-windsurfer1.jpg)

如果你安装了 VS Code，我建议导入你的信息。

然后，你可以选择要使用的主题。然后，你将看到 Windsurf 的主窗口（**图 2**）。

**图 2**
![](https://cdn.thenewstack.io/media/2025/01/5fca8da5-windsurfermain.jpg)

Windsurf 的用户界面设计得非常好。

你应该做的第一件事是单击“打开文件夹”以打开先前创建的项目，或者单击下面的“使用 Cascade 生成项目”文本区域。单击“生成”时，会打开一个提示窗口，你可以在其中使用 AI 生成项目。
例如，您可能想要创建一个 Python 应用程序，该程序接受用户输入并将其写入文件。单击“Generate”，然后键入“Create Python app to accept user input and write it to a file.”。单击“Select Folder”：当您的文件管理器打开时，选择文件夹或创建一个新文件夹来存放项目。选择文件夹后，按键盘上的 Enter 键，Windsurf 就会开始工作。

在创建我的测试项目后，我决定深入研究一下，看看 AI 的工作效果如何。在窗口底部附近，有另一个 AI 查询字段，我在其中键入了“How do I specify the type of input to be entered?”。按下 Enter 键后，Windsurf 认真思考了一下，重写了应用程序，甚至解释了更改（**图 3**）。

**图 3**

![](https://cdn.thenewstack.io/media/2025/01/01b7ffaa-windsurferupdate.jpg)

Windsurf 根据我的查询进行了一些更改。

然后，我点击“Accept All”以接受 Windsurf 所做的更改，此时它会询问我是否希望向项目中添加任何特定类型的验证。

这太不可思议了。

出于好奇，我运行了该应用程序，看看它是否能正常工作。Windsurf 包含一个内置终端，因此在窗口底部，Python 应用程序运行并要求我输入（**图 4**）。瞧，脚本完美运行。

**图 4**

![](https://cdn.thenewstack.io/media/2025/01/968cce73-windsurferouput.jpg)

您可以运行您的新应用程序，看看它的表现如何。

我不是提倡在编程中使用 AI，但我要说的是：如果您只是在学习一门新语言，Windsurf 是一个很棒的 IDE，可以帮助您快速上手。通过正确的提示，您可以轻松构建一个应用程序，甚至可以在进行过程中了解事物的工作原理。

给我留下了深刻的印象。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.