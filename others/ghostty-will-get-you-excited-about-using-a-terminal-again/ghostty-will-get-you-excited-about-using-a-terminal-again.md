
<!--
title: Ghostty让你再次爱上终端
cover: https://cdn.thenewstack.io/media/2025/01/03abe217-ghostty.jpg
-->

尽管Mitchell Hashimoto的Ghostty仍处于早期开发阶段，它已经是一款非常棒的终端应用程序，前景光明。

> 译自 [Ghostty Will Get You Excited About Using a Terminal Again](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)，作者 Jack Wallen。

这些年来我用过很多终端应用程序，多到我已经记不清它们是什么、曾经是什么或将是什么了。到目前为止，我最喜欢的终端应用程序是[Warp](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/)，但还有一个隐藏在暗处，随时准备跳出来吓唬我，让我改用它。

这个新的[终端应用程序](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)叫做[Ghostty](https://ghostty.org)，它是由[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention)的[联合创始人](https://thenewstack.io/mitchell-hashimotos-move-from-cto-garners-r-e-s-p-e-c-t/)创建的。这个新的终端轻量级、快速、功能丰富且跨平台。

Ghostty 的做法有点不同。一些终端应用程序使用 GUI 功能进行配置，而这个应用程序使用启动时加载的纯文本文件（或者在您进行更改时手动重新加载）。仅凭这一点，Ghostty 就不是刚开始使用命令行的用户的理想终端。相反，Ghostty 是针对那些经验丰富的用户。

这并不是说你不能使用默认的最小配置来使用 Ghostty；你当然可以，但你会错过很多功能。

说到功能，是什么让 Ghostty 如此特别？我们从哪里开始呢？

- 平台原生 GUI。
- 使用 Zig 编写，并在[Linux](https://thenewstack.io/introduction-to-linux-operating-system)上使用 GTK4/libawaita，在 macOS 上使用 Swift 编写，这意味着 Ghostty 完全原生于您的操作系统。
- 支持多个窗口、标签页和分割窗格。
- GPU 加速渲染。
- 100 个内置主题，并支持自定义主题。
- 常规键盘快捷键。
- Shell 集成（适用于 bash、zsh、fish 和 elvish）。
- 调整大小后重新绘制提示符。
- 工作目录报告。
- 活动进程检测。
- 程序化斜体。
- 支持连字和可变字体。
- 字素群集

目前，Ghostty 可在 Arch Linux（及其衍生版本）、macOS 和从源代码安装。我在 macOS 和 Arch Linux 上都安装了 Ghostty，发现安装过程非常简单。在 macOS 上，只需下载 .dmg 包，双击它，然后将 Ghostty 图标拖到应用程序文件夹即可。

在 Arch Linux 上，可以使用 pacman 从标准存储库安装 Ghostty，如下所示：

```bash
sudo pacman -S ghostty
```

安装完成后，从桌面菜单打开 Ghostty，您可以立即开始将其用作终端模拟器。

## 配置 Ghostty

对于那些从未通过文本文件进行过任何配置的人来说，这就是事情变得棘手的地方。让我向您展示如何自定义 Ghostty。

自定义方式与您在 Linux 上配置任何内容的方式相同。首先，配置文件位于以下位置之一：

- Linux – `$HOME/.config/ghostty/config`
- macOS – `$HOME/Library/Application\ Support/com.mitchellh.ghostty/config`

在 Linux 上，您必须通过配置文件和您最喜欢的文本编辑器来配置 Ghostty。在 macOS 上，您可以单击*文件 > 设置*以打开 GUI 文本编辑器并进行所需的更改。请注意，默认情况下，配置文件为空，因此您是从零开始。

例如，假设您想更改 Ghostty 的背景和前景（文本）颜色。假设您想要玫瑰粉色的背景和黑色的前景。这些配置将是：

```
background = #ff66cc
foreground = #000000
```

保存这些选项，然后单击 Ghostty 的*菜单按钮 > 重新加载配置*。Ghostty 终端应用程序现在应该反映您的更改（图 1）。

![图 1：配置 Ghostty 比您想象的要容易得多。](https://cdn.thenewstack.io/media/2025/01/8ea650cf-ghostty1.jpg)

*图1：配置Ghostty比你想象的要容易得多。*

假设您想创建一个键盘快捷键将当前 Ghostty 窗口分成两个窗格；为此，您可以将操作绑定到 Ctrl+d 快捷键，如下所示：

```
keybind = ctrl+d=new_split:right
```

您还可以配置 Ghostty 中使用的字体系列。为此，您首先需要使用以下命令列出可用的字体：

```bash
ghostty +list-fonts
```

您不会获得任何关于每种字体外观的视觉提示，因此您要么只能猜测，要么搜索您认为可能有效的字体名称。例如，您可能想要使用 Hack Bold 字体，其配置如下：

或者，您可以应用 100 个可用主题中的一个，如下所示：

首先，使用命令 `ghostty +list-themes` 列出所有主题，这实际上会为您提供每个主题外观的预览（图 2）。

![图 2：Ghostty 的可用主题。](https://cdn.thenewstack.io/media/2025/01/5fe09c63-ghostty2.jpg)

*图2：Ghostty可用的主题。*

找到你想要的主题后，你可以在配置文件中这样配置它：

```
`theme = Unikitty`
```

另一个很酷的技巧是，你可以将Ghostty窗口标题栏配置为与背景使用相同的主题颜色（图3）：

```
window-theme = ghostty
```

![](https://cdn.thenewstack.io/media/2025/01/5455a19b-ghostty3.jpg)

*图3：为Ghostty添加主题非常有趣。*

关于主题，我要说的是：由于某种原因，主题在Arch Linux安装上不起作用，但在macOS上却可以。

你可以在这里查看Ghostty配置选项的完整列表：[here](https://ghostty.org/docs/config/reference)。我建议你浏览这些选项，看看是否有任何东西能引起你的注意。

关于配置，我建议你：打开一个单独的终端窗口应用程序来编辑配置文件。这样，如果出现问题，你可以轻松地更改它，然后从Ghostty菜单重新加载配置文件。

虽然Ghostty仍处于开发早期阶段，但它已经是一款非常棒的终端应用程序，展现出巨大的潜力。
