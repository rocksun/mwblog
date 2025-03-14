# Warp Terminal 如何帮助我纠正脚本和代码

![Featued image for: How Warp Terminal Helps Me Correct My Scripts and Coding](https://cdn.thenewstack.io/media/2025/03/b1b62fca-chris-briggs-u4t-e-ktgmg-unsplash-1-1024x683.jpg)

每隔一段时间，科技真的会给我留下深刻而神奇的印象，这在如今并非易事。毕竟，我们几乎已经看到了科技行业所能提供的一切。

或者我们是这么认为的。

正如你所知，技术正以惊人的速度发展，所以每天我醒来都会想：“今天我会发现什么宝贝？”

前段时间，我在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 和 [macOS](https://thenewstack.io/the-best-macos-terminal-emulation-programs-for-developers/) 上安装了 [Warp terminal](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/)（它也适用于 Windows，但我不用微软的操作系统），发现它是一款令人印象深刻的软件，以至于它已经取代了我在这两个操作系统上的默认终端应用程序。

Warp 令人印象深刻。非常令人印象深刻。

然而……（这是一个很好的“然而”）前几天，我偶然发现了 Warp 中的一个功能，它让我大吃一惊。

让我来描述一下当时的情景。

我正在编写一个 bash 脚本，用于生成随机密码。目标是使用 *pwgen* 命令（因为我正在写一篇关于该命令的文章），我想展示如何从 [CLI](https://thenewstack.io/mongodb-atlas-finally-gets-a-command-line-interface/) 和脚本中使用它。

我编写了如下脚本：

```bash
#!/bin/bash
# Generate a random password using pwgen
password=$(pwgen -s 12 1)
echo "Your random password is: $password"
```

我使用以下命令授予脚本可执行权限：

*chmod u+x pw.sh*

当我在 Warp 中运行脚本时，收到了以下错误：

```text
./pw.sh: line 3: pwgen: command not found
```

你可能认为这很容易修复……只需按照错误提示修复问题即可。但无论我做什么，都无法让脚本运行。我没有继续抓狂，而是决定尝试一下 Warp 的 AI，看看它是否能解决这个问题。

运行脚本后，我注意到 Warp 不仅发现了错误，还主动提出修复语法问题（**图 1**）。

**图 1**

![](https://cdn.thenewstack.io/media/2025/03/b2082cf4-warpai1.jpg)

Warp 比我想象的更聪明。

我接受挑战。

我按下 Ctrl+Shift+Enter，等待应用程序执行操作。

Warp 开始工作并解释了问题。在弄清楚问题后（不到一分钟），它显示了修复后的脚本，并让我选择取消、优化、编辑或应用更改。我按 Enter 键，允许 Warp 将更改应用到我的脚本。修复运行后，它描述了它所做的事情，并将我的提示符返回给我。

重大的考验来临了。我运行了编辑后的脚本，看看会发生什么，你猜怎么着，它发现了更多的错误。再次按下 Ctrl+Shift+Enter。

我让 Warp 再次尝试修复它注入到我的脚本中的新问题，希望这次一切都能正常工作。

在它完成整个过程后，我按 Enter 键应用更改并再次运行脚本。

成了！

脚本的输出完全符合预期：

*
*毋庸置疑，我印象深刻。

我决定尝试一些不同的东西。这次我编写了一个 [Python app](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/)，它接受用户输入的年龄、身高、体重、性别表达和年龄，并将其附加到一个文件中。原始脚本是：

```python
#!/usr/bin/env python3
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")
gender_expression = input("Enter your gender expression: ")

with open("user_data.txt", "a") as file:
    file.write(f"Name: {name}, Age: {age}, Height: {height}, Weight: {weight}, Gender Expression: {gender_expression}\n")
```

运行脚本后，我遇到了一堆错误，所以我按下 Ctrl+Shift+Enter，让 Warp 修复问题。

毫不奇怪，Warp 的 AI 成功了。这一次，在 Warp 的“大思考”结束时，它主动提出为我运行该程序。我按 Enter 键，脚本运行了。你猜怎么着？Warp 成功了。最重要的是，Warp 注意到我的 [PYTHON](https://thenewstack.io/python/) 目录中有一个名为 random.py 的文件，这可能会在需要 random 模块的脚本中引起问题。我重命名了该脚本，一切都很好。

至少可以说，令人印象深刻。

如果你正在学习一门新语言，并且你的调试技能和我一样好，我强烈建议你尝试一下 Warp terminal，看看它是否可以解决问题并帮助你一路学习。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)