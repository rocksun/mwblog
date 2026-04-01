<!--
title: 如何在VS Code中集成Ollama以实现本地AI辅助
cover: https://cdn.thenewstack.io/media/2026/03/6cdf31d4-fachri-ersan-mca_mux0jdo-unsplash-1.jpg
summary: 本文指导将本地AI工具Ollama与VS Code集成，提供编程AI辅助。内容涵盖Ollama和VS Code的跨平台安装，以及VS Code内Continue扩展的配置。强调AI是学习助手。
-->

本文指导将本地AI工具Ollama与VS Code集成，提供编程AI辅助。内容涵盖Ollama和VS Code的跨平台安装，以及VS Code内Continue扩展的配置。强调AI是学习助手。

> 译自：[How to integrate VS Code with Ollama for local AI assistance](https://thenewstack.io/how-to-integrate-vs-code-with-ollama-for-local-ai-assistance/)
> 
> 作者：Jack Wallen

如果你正踏上程序员之旅，并希望加速这一进程，你可能会对利用AI来简化入门过程感兴趣。毕竟，编程行业竞争激烈，你应该考虑利用一切可以获得的优势。

在我继续之前，我要声明一点：利用AI来帮助你学习感兴趣的语言，而不是将其作为实际学习语言的替代品。将其视为一名*助手*，而非技能的替代者。

当我需要求助于AI时，我总是选择本地安装的选项，原因有二。首先，使用[本地安装的AI](https://thenewstack.io/how-to-deploy-a-local-ai-via-docker/)不会对电网造成压力。其次，我不必担心第三方会窥探我的查询，因此隐私得以实现。

为此，我依赖[Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)作为我选择的本地安装AI工具。Ollama易于使用、灵活且可靠。

如果你选择的IDE是[Visual Studio Code](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/)，那么你很幸运，因为你可以将其与本地安装的Ollama实例集成。

我将向你展示如何完成。

## 你需要什么

要使其正常工作，你需要一台运行[Linux](https://thenewstack.io/introduction-to-linux-operating-system/)、macOS或Windows的桌面操作系统。我将在一款基于Ubuntu的Linux发行版（Pop!_OS）上演示该过程。如果你使用macOS或Windows，唯一需要更改的是Ollama和VS Code的安装。幸运的是，在这两种情况下，都只需下载每个工具的二进制安装程序，双击下载的文件，然后按照设置过程操作即可。

在Linux上，情况有些不同。

让我来向你展示。

## 安装Ollama

我们要做的第一件事是安装Ollama。如果你使用的是macOS或Windows，请下载[适用于Mac的.dmg文件](https://ollama.com/download/Ollama.dmg)或[适用于Windows的.exe文件](https://ollama.com/download/OllamaSetup.exe)，双击文件，即可开始。

在Linux上，打开一个终端窗口并执行命令：

*`curl -fsSL https://ollama.com/install.sh | sh`*

安装开始前，系统将提示你输入sudo密码。

安装完成后，你需要为Ollama拉取一个特定的LLM。在macOS和Windows上，打开Ollama GUI，进入查询字段，点击向下箭头，输入*codellama*，然后点击该条目来安装模型。

在Linux上，打开终端应用程序并使用以下命令拉取所需的LLM：

*`ollama pull codellama`*

## 安装VS Code

接下来，你需要安装VS Code。

同样，对于macOS或Windows，[下载适用于你所选操作系统的VS Code可执行二进制文件](https://code.visualstudio.com/download)，双击下载的文件，并按照安装向导完成安装。

在Linux上，你还需要下载适用于你所选发行版的安装程序（适用于基于Debian的发行版的.deb文件，适用于基于Fedora的发行版的.rpm文件，或Snap软件包）。

要在Linux上安装VS Code，请切换到你下载的安装文件所在的目录。使用以下命令之一安装应用程序：

* 对于基于Ubuntu的发行版：*sudo dpkg -i code\*.deb*
* 对于基于Fedora的发行版：*sudo rpm -i code\*.rpm*
* 对于Snap软件包：*sudo snap install code –classic*

你现在已经拥有了开始所需的两个主要组件。

## 设置VS Code

下一步是设置VS Code以与Ollama协同工作。为此，你需要安装一个名为“Continue”的扩展。

为此，请按Ctrl+P（在macOS上是Cmd+P）。

在出现的字段中，输入：

*`ext install continue.continue`*

在出现的页面（**图1**）中，点击“安装”。

![](https://cdn.thenewstack.io/media/2026/03/c591870f-ollamacode2.jpg)

**图1：** 在VS Code上安装所需扩展很简单。

扩展安装完成后，点击左侧边栏中的Continue图标。在出现的窗口中，点击“选择模型”下拉菜单，然后点击“添加聊天模型”（**图2**）。

![](https://cdn.thenewstack.io/media/2026/03/8e952efb-ollamacode3-1024x641.jpg)

**图2：** 在继续之前，你必须添加一个模型。

在出现的窗口中，从提供商下拉菜单中选择Ollama（**图3**）。

![](https://cdn.thenewstack.io/media/2026/03/1c817b9d-ollamacode5.jpg)

**图3：** 你可以选择任何一个可用模型，但我们选择Ollama。

接下来，请确保从标签页中选择“本地”，然后点击每个命令右侧的终端图标。这将打开内置终端，你需要在键盘上按回车键来执行命令（**图4**）。

![](https://cdn.thenewstack.io/media/2026/03/c66b5613-ollamacode6-1024x643.jpg)

**图4：** 这是配置的核心所在。

当第一个命令（聊天模型命令）完成后，对第二个命令（自动补全模型）和第三个命令（嵌入模型）执行相同的操作。这需要一些时间，请耐心等待。每一步完成后，你都会看到一个绿色的√。

完成后，点击“连接”。

如果你点击Continue扩展，现在应该会看到一个连接到你本地安装的Ollama实例的新聊天窗口（**图5**）。

![](https://cdn.thenewstack.io/media/2026/03/17092a75-ollamacode7-1024x643.jpg)

你已全部设置完毕，准备就绪。