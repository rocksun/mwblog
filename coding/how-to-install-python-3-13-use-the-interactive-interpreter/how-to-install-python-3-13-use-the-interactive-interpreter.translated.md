# 如何安装 Python 3.13？使用交互式解释器

![Featued image for: 如何安装 Python 3.13？使用交互式解释器](https://cdn.thenewstack.io/media/2024/10/08963947-line-1644072_1280-1024x526.jpg)

随着 [Python (版本 3.13)](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) 的最新发布，出现了许多令人兴奋的功能，包括新的 [交互式解释器](https://docs.python.org/3/tutorial/interpreter.html)。该解释器具有多行编辑功能，并保留历史记录；支持 read–eval–print loop (REPL) 特定的命令（例如 help、exit 和 quit），无需将其作为函数调用；提示和回溯（启用颜色）；带有单独命令历史记录的交互式帮助浏览；历史记录浏览；以及粘贴模式。

这些功能的结合，使解释器在最近没有出现太多新功能的情况下，取得了长足的进步。对于任何使用 [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 交互式解释器的人来说，这应该是一个早期的圣诞礼物。

该交互式解释器基于 [PyPy](https://pypy.org/) 项目的代码，可以通过设置 PYTHONG_BASIC_REPL 环境变量来禁用。新的交互式 shell 可用于 [UNIX](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) 类系统（例如 [Linux](https://thenewstack.io/learning-linux-start-here/)），并支持 curses 和 Windows。默认情况下，解释器使用颜色来显示提示和回溯等内容。可以通过将 TERM 变量设置为 *dumb* 来禁用颜色选项。

让我们看看新的解释器是如何工作的。

## 更简单的退出

如果您使用过 Python 解释器，那么您知道退出它需要使用 Ctrl+D 键盘快捷键。

或者至少以前是这样。

现在，解释器退出变得有意义，因为您只需键入“exit”即可。作为几十年来一直使用 Linux 终端的人，这是一个受欢迎的改变。当我完成使用解释器时，我总是会键入 exit，但总是会收到错误提示。

在 Python 3.13 之前，它完全是 [让-保罗·萨特和没有](https://en.wikipedia.org/wiki/No_Exit) 退出。

同样，您现在也可以使用 *clear* 命令清除解释器屏幕，当您需要重新开始并想要一个干净的空间来使用时，这非常有用。

## 改进的错误消息

坦白地说：当我刚开始学习 Python 时，我不知道在使用文件名时需要小心。例如，我将创建一个使用随机库模块的应用程序，并将文件命名为 random.py。然后，我尝试运行代码，但只收到一条非常神秘的消息，没有告诉我哪里错了。

我当时并不知道问题出在文件名上。最终我发现了问题，更改了文件名并重新运行了应用程序，没有问题。显然，错误不在代码本身。

使用新的解释器，这些错误消息不再那么神秘。例如，您可能会在错误消息中看到类似以下内容：

```
1 |
(考虑重命名 '/home/jack/PYTHON/random.py'，因为它与名为 'random' 的标准库模块同名，并且导入系统优先使用它) |
```

这在我刚开始学习 Python 时肯定很有用。我将节省大量时间来解决诸如文件名冲突之类的愚蠢问题。

说到错误消息……

## 无处不在的颜色

好的，新的 Python 解释器不会将颜色洒在所有东西上。您会发现颜色（默认情况下）已启用，用于提示和回溯。这意味着什么？这意味着您将能够更容易地从解释器输出中发现问题。

让我们来体验一下我们改进的错误消息功能。我们将继续使用我们的 numpy.py 示例。如果我尝试运行该应用程序，我知道我会因为文件名而收到错误消息。但是，使用 Python 3.13，这些错误将以颜色显示，便于阅读。

**图 1**
![](https://cdn.thenewstack.io/media/2024/10/78d64b40-python313.jpg)
错误消息不仅更智能，而且在 Python 3.13 中更容易阅读。

## 可执行脚本

另一个很酷的功能是能够在 Linux 上使 Python 脚本可执行，而无需使用 python3 运行它。为此，您必须在代码顶部添加以下行：

```
1 |
#!/usr/bin/env python3 |
```

保存并关闭文件。接下来，使用以下命令授予文件可执行权限：

```
1 |
chmod u+x name.py |
```

其中 name 是您的脚本的名称。

现在，要运行您的 Python 脚本，您只需发出以下命令：

```
1 |
./name.py |
```

其中 name 是您的脚本的名称。

## 在 Ubuntu 上获取 Python 3.13


### TRANSLATOR'S RESPONSE

### EDITOR'S RESPONSE
如果您尝试从标准存储库安装 Python 3.13，您将不会成功。但是，有一个存储库您可以使用（如果您无法等待您选择的发行版将最新版本添加到标准存储库中）。让我向您展示如何解决这个问题。

首先，打开一个终端窗口并使用以下命令安装唯一依赖项：

```
sudo apt-get install software-properties-common -y
```

完成此操作后，使用以下命令添加所需的存储库：

```
sudo add-apt-repository ppa:deadsnakes/ppa
```

出现提示时，按键盘上的“Enter”键。

添加存储库后，您可以使用以下命令安装 Python 3.13：

```
sudo apt-get install python3.13 -y
```

您还没有脱离困境。目前，您的系统可能仍然默认使用 Python 3.10，因此您必须将其配置为使用 3.13。为此，我们将 3.10 和 3.13 都添加为备选方案。首先使用以下命令添加 3.10：

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
```

接下来，使用以下命令添加 3.13：

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 2
```

最后，使用以下命令配置默认值：

```
sudo update-alternatives --config python
```

出现提示时，选择 2，Python 3.13 就设置好了。如果您发出命令 *python -v*，您应该会看到 3.13 现在是默认值。

要详细了解 Python 3.13 中添加的内容，请务必查看 [官方发布公告](https://docs.python.org/3.13/whatsnew/3.13.html)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。