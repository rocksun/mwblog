# Warp vs. Ghostty：哪个终端应用更符合你的开发需求？

![Featued image for: Warp vs. Ghostty: Which Terminal App Meets Your Dev Needs?](https://cdn.thenewstack.io/media/2025/01/b4c24844-zyanya-citlalli-dhv25adxf74-unsplashb-1024x576.jpg)

在The New Stack最近对[Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)的[评测](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)之后，我想从[Warp用户](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)的角度来看待它。它们都是终端应用程序（如果你喜欢的话，可以称之为GUI shell），尽管Warp在功能方面（包括AI）明显更强大。另一方面，Ghostty的设计目标是开箱即用。这篇文章是对这两个终端在其各自环境下的初步介绍。

## 为什么选择终端？

当我将Warp描述为“重量级”时，这仅仅从我的MacBook上应用程序的大小差异就可以看出（300MB vs 50MB）：

开发人员之间似乎存在着文化差异：一些开发人员几乎“生活”在他们的终端中——购买他们喜欢的字体，尽可能地运行命令和编写脚本，而无需使用任何GUI应用程序；而另一些开发人员则大部分时间都在应用程序中度过，如果他们不得不出于任何原因使用终端，就会感到紧张。我承认[Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)的目标用户非常接近前者，因此它拥有大量的配置选项。但是，开发人员有理由理解和使用这两种风格。

我现在使用的是MacBook，但优秀的终端的强大之处在于它可以在尽可能多的操作系统和发行版上运行——这就是人们仍然学习如何正确使用vim的原因。[Warp即将登陆Windows](https://www.warp.dev/windows-terminal)（有一个等待列表），Ghostty将在1.0版本之后登陆。两者都涵盖了主要的Linux发行版，但我预计Ghostty会更积极地支持。

不管我们是否喜欢，在任何平台上进行计算仍然是关于文件、文件夹和进程的。一个好的应用程序可以隐藏这些基础知识，但是如果你不能控制文件权限或理解长时间运行的任务，你的效率将会迅速下降。

例如，在我的MacBook上，我可以快速安装tree（或者我可以自己编写这个函数）……

```bash
brew install tree
```

……然后显示一个项目结构的仅目录视图。
即使我从未听说过[Avalonia](https://thenewstack.io/avalonia-an-open-source-option-for-cross-platform-ui-work/)，这个tree也能让我快速了解它是什么，比在我的Mac上使用Finder要快得多。

终端也成为一个非常强大的**记录场所**。使用支持多个标签的终端，我可以有效地显示不同会话的记录——并在需要时继续任何一个会话。

## 安装Ghostty

我不会过多地介绍Ghostty，因为我们[之前的文章](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)已经很好地介绍了它。我很乐意使用Homebrew来安装它，但你也可以使用[二进制文件](https://ghostty.org/download)。

```bash
brew install --cask ghostty
```

这是在Warp中安装它。
请注意，Warp为长时间运行的命令（进程）提供了通知。这是一个在终端上简洁高效地完成某些操作的很好的例子。如果你查看顶部，你会看到当Warp**块**完成（已完成的命令调用和响应）时，它会记录所花费的时间。

Ghostty开箱即用，无需配置。但是，应该理解的是，许多shell行为来自shell配置本身。我已经安装了[zsh shell](https://www.zsh.org/)和[oh-my-zsh](https://ohmyz.sh/)（一个[“有主见的提示系统”](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)），它也具有行为。我完全承认我不总是知道哪个负责什么。

为了快速检查Ghostty的启动方式，我们可以在启动Ghostty时流式传输日志：

```bash
log stream --level debug --predicate 'subsystem=="com.mitchellh.ghostty"'
```

这让我们了解它尝试的默认设置。我已经总结如下：

```
- known but unimplemented action action=29
- found Ghostty resources dir: /Applications/Ghostty.app/Contents/Resources/ghostty-
- shell integration automatically injected shell=termio.shell_integration.Shell.zsh
- known but unimplemented action action=16
- started subcommand path=/usr/bin/login pid=89591
- received and ignored icon=~
- unimplemented OSC command: change_window_icon
```

我正在寻找的是它自动集成了（注入）我的zsh shell，这很好。但同样重要的是，如果它遇到它不理解的设置，它不会出现问题。

如果我想设置配置，只需在应用程序中按**cmd-,**。在这个例子中，我复制了我在一个博客中看到的随机配置：
12345678 | theme=catppuccin-latte window-height=30 window-width=110 title="Oh, hello" window-title-font-family="MonoLisa Variable" font-family="MonoLisa Variable" font-size=14 font-feature=-ligafont-thicken=true |
我实际上并没有安装这些字体和主题，但是我们上面流式传输的日志确认Ghostty拒绝了这些设置并继续运行，而没有停止启动。即便如此，它确实“加粗”了我的字体并更改了窗口标题：

## 会话、窗口和标签
将终端用作记录场所最常见的方法是打开带有几个标签的终端窗口。每个标签实际上都是一个独立的shell，专注于单独的项目或进程。

在Warp中，我只需点击栏上的加号即可在新窗口中添加新标签。在Ghostty中，命令**⌘**T也能做到同样的事情：

Ghostty还会设置那些快速标签，**⌘1、⌘2**和**⌘3**——这是一个不错的想法。请注意，Ghostty明智地继承了我的git颜色设置。

在许多情况下，我们可以长时间保持终端开启，但永远不考虑恢复是不明智的。

在Warp中，在几个标签中工作后，我可以命名并保存配置，或启动已命名的配置：

如果我随后退出Warp，重新打开并启动，我将获得窗口和标签——此外，我还拥有可帮助我记住正在做什么的历史记录。

如果我想在Ghostty中获得类似的行为，可以将这些键值对添加到配置中：

1234 | ...window-save-state = always quit-after-last-window-closed=true |
如果我随后使用**cmd**–**z**退出Ghostty，重新启动会正确重置我的窗口。有趣的是，我拥有与Warp相同的会话历史记录。我认为*omz_history*管理着这种共享历史记录行为：

目前，你无法更改Ghostty中标签的颜色，这是一种区分正在进行的进程的好方法——我肯定在其他终端中使用过这种方法。在Warp中这很简单：

但我已经看到了对此的[功能请求](https://github.com/ghostty-org/ghostty/issues/2509)。

## 结论
Ghostty必须与许多优秀的终端应用程序（例如，[Kitty](https://sw.kovidgoyal.net/kitty/)）竞争，但目前它已经相当稳定。作为一名开发者，你应该重视任何可在任何平台上使用的终端应用程序，以便能够快速在新环境中启动新项目。

有时，你将受益于Warp中的细节（终端中的AI可以帮助你记住模糊的命令和标志），但在其他情况下，速度和个性化至关重要。随着像[Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/)这样的语言的出现，生产中可能会有更多快速的应用程序。因此，请同时保留Warp和Ghostty——根据需要使用每一个。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)