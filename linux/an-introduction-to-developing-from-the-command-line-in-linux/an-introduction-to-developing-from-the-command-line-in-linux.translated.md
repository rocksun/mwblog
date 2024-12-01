# Linux 命令行开发入门

![Linux 命令行开发入门特色图片](https://cdn.thenewstack.io/media/2024/11/112ef20c-gabriel-heinzer-xbevm6oj1fs-unsplash-1024x768.jpg)

想到软件开发，你可能会认为需要各种应用程序和服务才能完成工作。你需要一个强大的[IDE](https://thenewstack.io/do-ides-make-you-stupid/)，一个用于版本控制的[GUI](https://thenewstack.io/tauri-mixing-javascript-with-rust-for-gui-desktop-apps/)，以及许多其他工具。

如果我说事实并非如此呢？

在我短暂学习[C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)时，教授告诉我们必须购买[Microsoft](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/)的IDE。虽然软件的学生价并不算贵，但我无法使用Windows电脑。我做的一切都在[Linux](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)系统中进行，我也不会改变这一点。

我该怎么办？

像任何优秀的Linux用户一样，我找到了解决方法。

令我惊讶的是，这并没有那么大的挑战。我必须安装一些软件（例如GNU C/C++编译器），但一旦完成，我就准备好了。我开始做我的第一个作业，一切都很顺利。

事实上，与我的同学们相比，我的过程效率要高得多。一些人抱怨他们的电脑不够强大，无法运行IDE，而另一些人则必须克服使用这种强大工具所涉及的学习曲线。

对我来说，我使用nano文本编辑器编写代码，用gcc编译它，然后运行应用程序。这非常容易。

这是一个使用C语言[Hello, World](https://thenewstack.io/beyond-hello-world-startup-gamifies-development-skills/)的示例。

代码如下：

将文件保存为`demo.c`。

使用以下命令编译应用程序：

```bash
cc demo.c -o demo
```

使用以下命令运行应用程序：

```bash
./demo
```

输出将是：

```
Hello, New Stack!
```

真的没有比这更容易的了。

但让我们退一步，讨论一下需要什么。

## 在Linux上开发所需内容

显然，你需要一个正在运行的Linux实例。这可以是任何发行版，因为无论你使用哪种Linux版本，工具都可以在标准存储库中找到。但是，也有例外。例如，大多数标准存储库中找到的Java版本已经过时，这意味着你需要添加一个包含最新版本的存储库。

其他语言呢？让我们来看看。

[Python](https://thenewstack.io/what-is-python/) – 大多数Linux发行版中预装。

C/C++ – 可以从标准存储库安装。在基于Fedora的发行版上，可以使用以下命令添加：`sudo dnf groupinstall ‘Development Tools’`，在基于Ubuntu的工具上，该命令是`sudo apt-get install build-essential -y`。

Go – Go二进制文件可以从[https://go.dev](https://go.dev)下载。下载后，使用以下命令解压存档：`sudo tar -C /usr/local/ -xzf goXXX.linux-amd64.tar.gz`（其中XXX是发行版号）。然后，你必须通过将以下行添加到`~/.profile`文件的底部来设置Go的路径：`export PATH=$PATH:/usr/local/go/bin`。

Java – 如何安装Java取决于你需要的版本，但你可以使用以下命令之一从标准存储库安装默认包：Ubuntu – `sudo apt-get install default-jdk -y` 或 Fedora – `sudo dnf install <openjdk-package-name>`。你可以使用`dnf search openjdk`找到要安装的包。

Node.js – 在Ubuntu上，使用以下命令安装Node.js：`sudo apt-get install nodejs -y`，在Fedora上，命令是：`sudo dnf install nodejs -y`

如你所见，在Linux上安装实际的[编程语言](https://thenewstack.io/programming-languages/)非常容易。

你可能还想为选择的语言安装调试器。例如，你可以对C、C++、Ada和Fortran使用`gdb`调试器。如果你需要命令行调试器，请快速搜索一下，你很快就会发现你选择的语言是否有命令行调试器以及如何安装它。

接下来是什么？

## 选择你的编辑器

我只想说：Nano一直是我的首选编辑器。我知道它不是流行的选择，但我发现它从来不会妨碍我完成需要做的事情。

也就是说，大多数使用Linux的资深开发者倾向于更喜欢老式的（并且极其强大的）`vi`或`emacs`。这两个编辑器的问题是它们都有学习曲线。让我解释一下`vi`的工作流程。

- 打开一个终端窗口。
- 使用命令`vi`启动`vi`。
- 按键盘上的i键，从命令模式切换到插入模式。
- 键入您的代码。
- 首先按键盘上的 Escape 键，然后键入 `:wq` (写入/退出) 来保存并退出。
这只是最基本的用法，每次使用 *vi* 都必须经历这个过程。

以下是使用 nano 的相同过程：

- 打开终端窗口。
- 使用命令 `nano` 启动 nano。
- 键入您的代码。
- 使用 Ctrl-X 组合键保存并退出。
使用 nano，步骤较少，也更容易记住。另一方面，它的功能要少得多。因此，我总是建议新用户从 nano 开始，一旦他们觉得需要更多功能，就可以迁移到 *vi*。

## 完成它

在某些时候，您将需要一个版本控制系统，尤其是在与团队合作时。幸运的是，您可以通过命令行与 Git 交互，因此无需 GUI。

Git 可以从标准存储库安装，例如使用以下命令：

```bash
sudo apt-get install git -y
```

安装 Git 后，基本的命令行工作流程如下所示：

- 创建一个新仓库 – `mkdir ~/new-project`
- 初始化仓库 – `git init`
- 将文件添加到仓库 – 您可以复制它们或从头创建它们。
- 使用以下命令将本地仓库与 GitHub 仓库连接：`git remote add origin URL`（其中 URL 是 GitHub 仓库的地址）
- 使用以下命令拉取远程仓库的内容：`git pull origin master`
- 创建一个 README 文件，然后使用以下命令添加它：`git add README`
- 使用以下命令进行第一次提交：`git commit -m "Added new information to README file"`
- 使用以下命令推送更改到远程仓库：`git push`

请注意，您必须在 GitHub 个人资料中创建一个访问令牌。您还需要使用以下命令配置全局选项：

```bash
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR EMAIL"
```

其中 NAME 是您的真实姓名，EMAIL 是与您的 GitHub 帐户关联的电子邮件地址。

从 Linux 命令行进行开发并不像您想象的那么具有挑战性。您能否大规模地以这种方式工作？也许可以。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。