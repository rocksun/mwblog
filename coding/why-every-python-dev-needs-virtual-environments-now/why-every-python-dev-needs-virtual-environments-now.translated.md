# 为什么每个 Python 开发人员现在都需要虚拟环境

![为什么每个 Python 开发人员现在都需要虚拟环境的特色图片](https://cdn.thenewstack.io/media/2025/01/983492c7-unsplash-community-hdxlqjahsmu-unsplash-1024x693.jpg)

使用 [Python](https://thenewstack.io/python/) 进行开发时，您很可能需要安装各种库、依赖项和应用程序才能启动项目。好消息是（在大多数情况下）这些安装非常简单（感谢 [pip](https://thenewstack.io/how-to-use-python-pip-and-why-you-need-to/) 和其他工具）。

但是，如果您只是将所有这些项目需求安装到您的系统上，则可能会出现问题。这就像安装任何给定的应用程序一样，希望它不会与其他应用程序、您的操作系统或您的数据造成问题。在大多数情况下，它是安全的，但总是有一个实例，事情可能会很快出错。

您不希望这样。毕竟，您的系统是您工作的地方，而您的工作是您的生计。考虑到这一点，您为什么要冒哪怕是最轻微的风险，这可能会让您和您的项目倒退？尤其是在您时间紧迫，必须按时交付或冒着失去客户（或您的工作）的风险时更是如此。

为此，您该怎么办？

您使用虚拟环境。

## 什么是虚拟环境？

虚拟环境是一个隔离的沙箱，允许您安装项目所需的一切，而不会影响全局。在虚拟环境中，您可以安装所有需要的库和依赖项，而无需接触全局 Python 安装。

将 Python 虚拟环境想象成一台 [虚拟机](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/)。如果您曾经使用过 VirtualBox 等工具，您就会知道主机和客户机不会相互影响，并且您对客户机操作系统所做的任何操作都不会影响主机操作系统。您可以有效地安装 Linux 客户机操作系统，登录，运行 `sudo rm -rf /*` 命令（不要这样做），它会破坏客户机操作系统，但不会触及主机。

Python 虚拟环境的工作方式类似，并提供以下好处：

- 它们允许您同时处理具有不同依赖项的多个项目。
- 它们允许您创建可移植的项目。
- 没有版本冲突的风险。
- 它们避免了全局包安装的需要。
- 它们使测试更容易。
- 它们使清理更容易。
- 它们简化了协作。
- 它们更容易重现。
- 它们提供依赖项隔离。
- 它们创建了一个更干净、更有条理的工作区。

问问任何经验丰富的 [Python 开发人员](https://thenewstack.io/why-should-python-developers-care-about-testing/)，他们会告诉您，您创建的每个项目都应该在虚拟环境中完成。

好消息是 Python 包含创建和使用虚拟环境所需的一切。更好的是，创建虚拟环境非常容易。

让我向您展示如何创建、激活、停用和删除 Python 虚拟环境。

## 您需要什么

您唯一需要的就是在您选择的 OS 上安装 Python。我将在 [Pop!_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) 上使用 Python 3.10.12 版本演示这一点，但是无论操作系统如何，该过程都是相同的。请注意，只要您使用的是 Python 3.4 及更高版本，它就包含执行此操作所需的一切。如果您使用的是早于 3.4 的 Python 版本，建议您升级；否则，您需要使用 Pip 安装 virtualenv (`pip install virtualenv`)。

## 创建虚拟环境

首先，您需要创建一个新的虚拟环境。

登录到您的操作系统并打开一个终端窗口。一旦您可以访问 CLI，创建一个目录来存放您的 Python 项目，如下所示：

```bash
mkdir PYTHON
```

使用以下命令更改到该父目录：

```bash
cd PYTHON
```

假设您即将开始开发一个名为 ProjectX 的项目。使用以下命令为该项目创建一个新的虚拟环境：

```bash
python -m venv ProjectX
```

如果您收到错误消息，您可能需要为您的 Python 版本安装所需的 venv 命令，如下所示：

```bash
sudo apt-get install python3.10-venv
```

如果您使用的是早于 3.4 的 Python 版本，则命令为：

```bash
virtualenv ProjectX
```

您现在应该会找到一个名为 ProjectX 的新目录。在这个目录中，您会找到以下子目录：

- bin
- include
- lib
- lib64

您还应该找到一个名为 `pyvenv.cfg` 的文件。

使用以下命令更改到 ProjectX 目录：

```bash
cd ProjectX
```

接下来，您需要使用以下命令激活项目：

```bash
source bin/activate
```

您应该会看到您的提示符发生更改。它现在看起来像这样：

```bash
(ProjectX) hostname ->
```

如果您使用的是 Windows 环境，则激活将是以下之一：
- 对于 `cmd.exe`：`venv\Scripts\activate.bat`
- 对于 `PowerShell`：`venv\Scripts\Activate.ps1`

此时，您可以安装项目所需的所有必要的库和依赖项，而不会影响您的系统。安装完依赖项后，您可以开始处理您的项目。

## 停用项目

完成项目工作后，最好将其停用。这将保持虚拟环境不变，并防止其发生任何变化。

要停用虚拟环境，请在项目目录中键入以下命令：

```bash
deactivate
```

任何时候需要，您可以返回该目录并运行与之前相同的 activate 命令。

## 删除虚拟环境

如果需要删除虚拟环境，只需将其停用，然后使用以下命令删除目录：

```bash
rm -rf venv
```

如果您在 Windows 环境中工作，则需要将 `rm -rf venv` 更改为使用 Windows 等效命令，例如 `rmdir /s /q venv`。


我的朋友们，这就是使用 Python 虚拟环境的全部内容。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。