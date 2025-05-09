# Linux：如何从源代码安装应用程序

![Featued image for: Linux: How To Install Apps From the Source](https://cdn.thenewstack.io/media/2025/01/49ac0687-olivie-strauss-49fb-ltae40-unsplash-1024x683.jpg)

我刚开始使用[Linux](https://thenewstack.io/learning-linux-start-here/)时，安装应用程序只有一种方法……从原始源代码安装。那些日子早已过去，现在，安装软件有几种方法：

- 源代码
- 默认包管理器
- 通用包管理器
- AppImages

安装应用程序最可靠、最简单的方法是默认包管理器（例如 Debian 的 APT）和通用包管理器，例如 FlatPak。接下来是[AppImage](https://appimage.org/)，它允许你在任何平台上安装 Linux 应用程序。

剩下的就是从源代码安装。

为什么安装 Linux 应用程序的最古老方法排在列表的最后？这不仅仅是包管理器提供的简单性。事实上，你应该选择包管理器安装而不是源代码安装有一个非常好的理由。当你通过包管理器安装时，你的系统会知道该应用程序。

这是什么意思？

让我给你一个简单的解释。

假设你使用默认包管理器安装 AppX。当你这样做时，系统会知道该应用程序，这样，每当该应用程序有可用升级时，下次你使用包管理器运行升级时，它就会被应用。

现在，假设你通过源代码安装 AppX。下次你使用包管理器运行更新时，AppX 不会更新。为什么？因为包管理器不知道它，也没有升级通过源代码安装的应用程序的能力。

这是什么意思？好吧，让我们坚持我们的例子。你在 1 月份通过源代码安装了 AppX，并且你定期使用默认包管理器更新了你的系统。在 12 月份，你检查了 AppX，却发现它已经过时了。在 1 月份和 12 月份之间，AppX 开发人员发布了几个更新，其中包括安全补丁。

猜猜怎么了？你系统上的 AppX 现在很脆弱。如果你通过包管理器安装了 AppX，你就不会有这个问题。

另一个问题（一个可能被认为更重要的问题）是，通过包管理器安装并存储在发行版标准存储库中的应用程序已经过验证，理论上应该没有恶意代码（因为没有什么是有保证的）。

最后，从发行版的包管理器安装有助于解决所有依赖关系问题，因此你不会陷入通常所说的“依赖地狱”，在这种情况下，你必须安装一个依赖项来解决另一个依赖项，这又会解决另一个依赖项……你明白我的意思。我记得，过去，我花了几个小时试图解决基于源代码安装的依赖关系，这[可不是闹着玩的](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/)。

这并不是说应该不惜一切代价避免从源代码安装。你可能会遇到只能通过源代码安装的应用程序。发生这种情况时，你可能别无选择。如果出现这种情况，至关重要的是你必须自己检查软件，以确保源代码中不包含恶意代码。

好的，你决定通过源代码安装一个应用程序，并且你已经确保该应用程序是安全的。你如何安装它？

让我在这个过程中担任你的向导。

## 从依赖关系开始

还记得我提到的依赖地狱吗？这可能是从源代码安装中最能阻止大多数人继续前进的部分。从源代码安装的问题在于，你必须首先满足所有依赖关系，然后才能尝试编译和安装该应用程序。

通常，在应用程序的源代码文件夹中，会有一个 README 文件，其中应该包含有关依赖关系的所有信息。阅读该文件，然后开始查找、下载和安装依赖关系的过程。有时，这些依赖关系可以通过你的包管理器安装。其他时候，AppX 可能需要特定版本的依赖关系，这意味着你可能必须从源代码安装它。如果该依赖关系有其自身的依赖关系，则你首先应该尝试使用默认包管理器安装它们，然后再深入研究源代码安装的“兔子洞”。

但是你如何实际进行安装呢？

耐心点，我们快到了。

## 它是如何工作的？

好的，你已经下载了 AppX 的源代码（或者你已经从[Git 仓库](https://thenewstack.io/development-git-clone-a-project/)克隆了它）。你知道该应用程序是安全的，并且你准备尝试一下。

它是这样工作的。我将坚持使用我们虚构的 AppX 应用程序示例。
在继续之前，您可能需要安装一些必要的组件，否则您将无法构建应用程序所需的软件。如果您选择的系统基于[Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)，通常可以使用以下命令完成：

```bash
sudo apt-get install build-essential -y
```

`build-essential` 包安装了 libc、gcc、g++、make、dpkg-dev 等。

在基于 Fedora 的发行版上，该命令为：

```bash
sudo dnf install dh-autoreconf curl-devel expat-devel gettext-devel openssl-devel perl-devel zlib-devel gcc curl cmake -y
```

搞定这些后，您可以继续了。

下载软件包后，首先需要解压文件。大多数情况下，这些文件会使用 tar 等工具进行压缩和存档。最简单的方法是打开文件管理器，导航到文件，右键单击文件，然后选择“此处解压”。这将创建一个新目录，通常以应用程序名称命名。

此时，您将拥有一个名为 AppX 的目录。使用以下命令进入该目录：

```bash
cd AppX
```

一般来说，这个过程如下所示：

```bash
./configure
make
sudo make install
```

在运行`./configure`命令之前，您可能需要浏览一下源目录中的配置文件，其中可能包含在运行`configure`命令之前可以配置的选项。此外，README 中可能包含有关可用于配置的标志的详细信息，您绝对应该了解这些信息。

只有在`./configure`运行成功后，才能执行`make`命令，该命令编译应用程序。如果`./configure`命令失败，您可以查看输出以找出原因（大多数情况下是缺少依赖项）。如果`make`成功，则可以运行`sudo make install`命令，该命令将可执行二进制文件安装到`$PATH`中的目录中，以便可以按预期运行应用程序。

现在您已经从源代码安装了应用程序，您需要定期检查是否有新的更新可用。如果有，您将不得不再次执行相同的过程，这也是您应该坚持从默认包管理器安装应用程序的原因之一。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)