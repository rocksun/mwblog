### 摘要

* Linux 7.1 开始逐步淘汰对 i486 CPU 的内置支持。
* Linus 表示，是时候放弃 i486 了，因为兼容性“胶水”会浪费开发时间并导致问题。
* 如果你仍在使用 i486，请继续使用 LTS 内核或旧版发行版；现代内核可能会放弃支持。

Linux 以支持旧硬件而闻名。如果你有一台老旧的 PC，并想在其上安装一个仍受其创建者支持的操作系统，那么你很有可能安装一个现代的 Linux 发行版，并且它会运行良好。然而，Linux 社区似乎对继续支持的硬件有一个限度。

Linux 7.1 版本有一项拟议的更改，如果合并，将开始逐步取消对英特尔 486 处理器的支持。如果你不确定那是什么，你可能会惊讶地发现这个处理器可能比你还老。

![一台笔记本电脑显示 KDE Plasma 桌面，打开了 Affinity 和 Vivaldi 等应用程序](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/linux-laptop-with-kde-plasma.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
相关阅读

我知道它不完美，但我爱它

## Linux 7.1 开始逐步淘汰对 37 年前处理器的支持

### i486 曾是传奇，但所有传奇终将谢幕

![在 Linux 终端上运行 Tmux 和几个应用程序](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/01/linux-tmux.jpg?q=49&fit=crop&w=825&dpr=2)

正如 [Phoronix](https://www.phoronix.com/news/Linux-7.1-Phasing-Out-i486) 所发现的，一项新更改已排队等待合并到 Linux 7.1 中。这项由 Ingo Molnar 撰写的更改，标题为“[x86/cpu: Remove M486/M486SX/ELAN support](https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/platform&id=8b793a92d862c89055daa97ffa61a6929cf732f9)”，开始逐步取消 Linux 对 i486 的内置支持，该处理器于 1989 年首次发布。正如更新日志所指出的，甚至 Linus 也渴望与该架构“断绝关系”：

> 在 x86 架构中，x86-32 存在各种复杂的硬件仿真设施，用于支持极少数人会与现代内核一起使用的古老 32 位 CPU。这种兼容性“胶水”有时甚至会导致问题，人们会花费时间去解决，而这些时间本可以用于其他事情。正如 Linus 最近评论道：
>
> “我真的觉得是时候放弃 i486 支持了。没有人有任何真正的理由在这种问题上浪费一秒钟的开发精力。”

为了实现这一点，拟议的更改通过删除 CONFIG_M486SX、CONFIG_M486 和 CONFIG_MELAN 来取消 M486/M486SX/ELAN 支持。这些更改尚未合并到 Linux 7.1 中，但考虑到 Linus 本人已表达了取消支持的兴趣，很有可能它们会被采纳。

如今，很可能没有人还在使用 i486，但如果有人 *真的* 在用，他们很有可能会使用 Linux 来完成工作。如果你是少数仍让这个几十年前的 CPU 保持活力的用户之一，那么你最好的选择是下载一个 LTS Linux 发行版，它会再保留旧版 Linux 几年。

![一只手上拿着一台 Steam Deck，背景色彩鲜艳。](https://static0.xdaimages.com/wordpress/wp-content/uploads/2024/09/reasons-to-pick-a-gaming-handheld-over-a-pc.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
相关阅读

Linux 与十年前相比已完全不同。