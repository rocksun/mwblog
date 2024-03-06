
<!--
title: Unix Shell 能否得到改进？当然可以！（FOSDEM 24）
cover: https://cdn.thenewstack.io/media/2024/03/a270fc6f-liquid_prompt.png
-->

一窥另类命令行环境或“固执己见的提示系统”的世界，例如 Liquid Prompt 和 Oh-My-Posh。

> 译自 [Can the Unix Shell Be Improved? Hell Yes! (FOSDEM 24)](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)，作者 Joab Jackson。

*2 月 3 日 [FOSDEM 2024](https://fosdem.org/2024/) 演讲的笔记“Liquid Prompt：是的，我们可以彻底重新考虑 shell 提示符的设计”。（FOSDEM 索引中的 aw1.126）

[Nojhan](https://github.com/nojhan)（全名）是一位 [视觉设计师](http://nojhan.net/)，也是 [LiquidPrompt](https://github.com/liquidprompt/liquidprompt) 备选 shell 的创建者，它是一种“Bash 和 Zsh 的自适应提示符”[承诺](https://liquidprompt.readthedocs.io/en/stable/)“在需要时提供一个显示精美的提示符，其中包含有用的信息”。

尽管[GUI 取得了数十年的进步](https://thenewstack.io/cloud-ides-have-a-wow-factor-but-for-developers-its-just-different/)，但大多数管理员和许多开发人员仍然通过某种 shell 使用点阵式命令行界面。当你了解这些命令时，[它会更快](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/)，并且更容易使用 shell [集成不同的任务](https://thenewstack.io/pipe-how-the-system-call-that-ties-unix-together-came-about/)。

Nojhan 在他的 FOSDEM 演示中指出，当今的命令解释器 shell（自始至终使用最广泛的是 [Bash](https://www.gnu.org/software/bash/)）存在可用性问题。

它们不是很用户友好：没有人体工程学，没有风水，只有无穷无尽的小型 ASCII 文本行。这些 shell 并未设计为突出显示用户感兴趣的重要部分，而且正如 Nojhan 指出的那样，它们也没有“遵循工作的状态”。

为什么在这些 shell 中，在一个未经区分的文本屏幕上，找到提示符如此困难？

碰巧的是，有大量的[备选 shell](https://thenewstack.io/posh-a-data-aware-shell-for-faster-distributed-text-processing/) 或“固执己见的提示符系统”，所有这些都具有创新的设计来克服这些限制。

Nojhan 不仅指出了他自己的 LiquidPrompt，还指出了其他一些，每个名称都比上一个更出色：
[Starship](https://starship.rs/), [Oh-My-Posh](https://ohmyposh.dev/), [Powerline](https://github.com/b-ryan/powerline-shell), [Powerlevel10k](https://github.com/romkatv/powerlevel10k) 和 [Pure](https://github.com/sindresorhus/pure)。

Nojhan 在一篇详尽的[博客文章](https://github.com/liquidprompt/liquidprompt/wiki/why) 中对上述所有内容进行了比较。通过这项相当可观的分析，Nojhan 得出结论，LiquidPrompt 是所有提示符系统中最棒的（尽管他承认每个系统都有其优点，并且所有系统都应该针对特定的用户需求进行考虑，这是理所当然的）。

![](https://cdn.thenewstack.io/media/2024/03/604de989-liquid-prompt-compare.jpg)

但是，无论这些发明多么创新，是否有任何发明足以吸引管理员和编码人员从他们信赖的（尽管单调乏味的）单行 shell 中转移出来？

## 更好的 Shell 的设计提示

![](https://cdn.thenewstack.io/media/2024/02/01c5064c-oh-my-popsh-300x195.png)

*ohmyposh.dev*

Nojhan 说：“一个好的提示符应该是集中的。”它应该突出显示对用户有用的状态。你需要知道你的工具的版本号吗？也许不需要。有些状态的变化比其他状态多，因此不需要重复。这一切都取决于你需要且应该可定义的范围。

一些覆盖层（例如 Oh-My-Posh）使用颜色来区分数据的不同部分。Nojhan 嘲笑这是“迷幻彩虹”，并指出它们对色盲者毫无用处。

但与此同时，你希望避免“文本过载”或屏幕上出现太多文本。

基于 Bash 的 LiquidPrompt 使用三行方法。它只使用四种颜色：黑色、白色和两种可供选择的对比色，对于色盲者来说，这两种颜色是可辨别的。

> “重要的信息应该是可见的”——Nojhan。

以下是默认命令行：

![](https://cdn.thenewstack.io/media/2024/03/ae7281cd-liquid-prompt-default-med.png)

以下是“Powerline”主题：

![](https://cdn.thenewstack.io/media/2024/03/70881974-liquid-prompt-powertheme-med.png)

三行命令行当然很有趣，但真正吸引人的是你可以将什么放入每一行。你可以嵌入各种简洁的小部件，
[包括](https://liquidprompt.readthedocs.io/en/latest/overview.html)：

- **当前路径**：显示你的位置，并“智能缩短路径”。
- **上次命令执行时间**
- **电池电量**
- **用户名**
- **主机名**
- **退出代码**：如果上次命令是错误，则显示其退出代码。
- **作业**：后台、休眠和分离作业的计数器。
- **时间**
- **可用内存/磁盘空间**
- **远程 shell**
- **Wifi** 信号强度。

它可以嵌入[git](https://thenewstack.io/tutorial-git-for-absolutely-everyone/) 和其他存储库的版本控制信息，显示当前分支/标签、当前状态以及当前提交/编辑的统计信息。

在演示中，Nojham 显示了一行，显示了待处理 git 命令的状态，*git st*。该命令本身像往常一样位于该行的最右侧。

![](https://cdn.thenewstack.io/media/2024/02/029b6708-liquidprompt-01.png)

但提示之前，该行还显示了主分支待更改的数量——68 个添加和 189 个删除。它还可以通过巧妙地使用行阴影和指针警告用户有其他可能冲突的待处理提交。

LiquidPrompt 可针对特定环境进行配置，包括[AWS](https://aws.amazon.com/?utm_content=inline-mention)、[Kubernetes](https://thenewstack.io/kubernetes-1-29-mandala-tests-mutable-pod-resources/) 和 [Terraform](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)。它甚至为以下语言提供定制的虚拟环境：

- [Python](https://thenewstack.io/what-is-python/)
- [Ruby](https://thenewstack.io/why-were-sticking-with-ruby-on-rails-at-gitlab/)
- [Perl](https://thenewstack.io/getting-started-at-long-last-on-perl-6/)
- [Docker](https://www.docker.com/?utm_content=inline-mention)

这么多功能需要记住！因此，只有时间才能证明现代编码人员的大脑是否已为 Tres Hombre 命令行做好准备。

