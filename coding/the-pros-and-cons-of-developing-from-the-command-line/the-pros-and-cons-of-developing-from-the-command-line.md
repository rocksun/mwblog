
<!--
title: 从命令行开发的优缺点
cover: https://cdn.thenewstack.io/media/2025/05/66af3664-curated-lifestyle-dyno5ahumdg-unsplash-1.jpg
summary: 硬核！抛弃GUI，拥抱命令行开发！更低的硬件要求，更高效的工作流，还能灵活远程SSH。虽学习曲线陡峭，需更多前期工作，但能更好理解底层原理，玩转GCC、Make等工具，云原生DevOps效率倍增！
-->

硬核！抛弃GUI，拥抱命令行开发！更低的硬件要求，更高效的工作流，还能灵活远程SSH。虽学习曲线陡峭，需更多前期工作，但能更好理解底层原理，玩转GCC、Make等工具，云原生DevOps效率倍增！

> 译自：[The Pros and Cons of Developing From the Command Line](https://thenewstack.io/the-pros-and-cons-of-developing-from-the-command-line/)



早在 90 年代，我曾在当地一所大学学习 [C++](https://thenewstack.io/introduction-to-c-programming-language/)。班上除了我之外，每个人都有一台 [Windows](https://thenewstack.io/ebpf-is-coming-for-windows/) 机器。至于我自己，我已经是一个铁杆 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 用户，教授说什么也无法让我回到 Windows。

即使他当时建议使用 [Microsoft Visual Basic](https://thenewstack.io/visual-basic-lingers-on/)，但我确信我可以使用 [Linux 和命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 完成课程。

我确实做到了，但一开始花了一些功夫。最后，我以 A 的成绩完成了课程，然后迅速忘记了我所学的一切。

好吧，并非一切。

让我记忆犹新的一件事是，从命令行开发当然是一种选择，它既有优点也有缺点（就像使用 [GUI](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/) 时一样）。这些优点和缺点是什么？让我们深入了解一下。

## 优点

首先，我们将看看优点，这些优点足以让你考虑放弃 GUI。

### 更低的硬件要求

这对很多人来说都是一个重要的优势。[IDE](https://thenewstack.io/best-open-source-ides/) 对资源的要求相当高。而命令行……则不然。事实上，你可以在任何能够运行 Linux 的旧机器上使用命令行进行开发。从命令行工作时，编译时间甚至更快。因此，你无需花费大量资金购买顶级 PC 作为开发站。而且有这么多 Linux 发行版可用于旧硬件，即使是那台积满灰尘的旧机器也能发挥作用。

所以不要陷入必须拥有最新最好的硬件才能进行开发的想法中，因为命令行为你提供了更多更便宜的选择。

### 更好地理解事物的工作方式

我在 C++ 课程中学到的一件事是，事物如何协同工作以创建一个有凝聚力的整体。我没有让 GUI IDE 完成所有事情，而是必须将所有部分拼凑在一起，以创建一个能够使用该课程编程语言的工作站。最后，我对所有这些如何结合在一起（语言、编译器、调试器，所有东西）以使 [开发、编译和运行应用程序](https://thenewstack.io/3-recommended-low-code-tools-for-application-development/) 成为可能有了更好的理解。

### 更高效的工作流程

我在 C++ 期间发生的一件很酷的事情是，我开发了一个非常快速的工作流程。我没有在键盘和鼠标之间移动我的手，而是能够通过键盘完成所有事情，这使我创建了一个非常高效的工作流程。我经常与其他学生一起工作，并且发现我完成事情的速度比其他人都快得多，这归功于我工作方式的简单性。一旦你创建了一个有效的命令行工作流程，就很难用 GUI 来匹配它。而且考虑到你可以从命令行使用 [Git](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/)，实际上没有什么你不能以非常高的效率完成的事情。

### 更灵活的远程工作

我可以使用命令行做的一件非常棒的事情是 [SSH](https://thenewstack.io/linux-ssh-and-key-based-authentication/) 进入远程机器并完成我需要的一切，而无需离开我的办公桌。这意味着我可以在我的本地机器上进行开发，或者安全地 shell 进入远程机器并做同样的事情。我甚至可以打开多个终端窗口（或使用带有选项卡的终端应用程序）并远程连接到多台机器，并在同一会话期间在所有这些机器上进行开发。是的，有一些 GUI 允许你连接到远程桌面，但让它有效地工作可能是一个挑战。使用 [Linux 和 SSH](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/)，一切都在你的掌控之中，随时可以使用。

### 成本效益

从命令行开发很便宜。想想看：你无需购买任何软件，因为它都内置在操作系统中。虽然有很多免费或便宜的 IDE，但当你把所有东西加起来（包括更低的硬件要求）时，它最终成为一种非常经济高效的开发方法。

## 缺点

好吧，在命令行领域，并非一切都是美好的。以下是你在深入研究之前必须考虑的一些缺点。

### 更陡峭的学习曲线
刚开始上课的那几天，我感到很吃力，因为我不仅要学习如何从命令行执行操作，还必须弄清楚使它工作所需的所有组件。我需要 [GCC](https://gcc.gnu.org/), GCC+, [make](https://www.gnu.org/software/make/) 和一堆其他的命令行工具。最重要的是，我必须学习（并记住）编译和调试我构建的应用程序所需的命令行。这并不容易，但这是我在几天内克服的障碍。

### 需要更多的工作

这不仅仅是更陡峭的学习曲线，而且还涉及更多。 你必须键入命令而不是单击按钮。 你必须了解处理手头任务所需的一切，而不是安装可搜索的插件。 所有这些都意味着你将需要预先做更多的工作。 好消息是，一旦你完成了所有这些工作，一切都会很快变得顺利，你就可以开始了。

### 更少的集成

许多 IDE 包含大量的集成。 如果它们没有开箱即用，你可以通过插件添加它们。 命令行不是那样工作的。 如果你需要将某些东西集成到你的工作流程中，可能需要一些调整才能实现。 你可能必须找到正确的库并弄清楚如何安装它们。 最后，如果你的项目依赖于大量的 IDE 集成，你可能会发现自己很难从命令行完成工作。

## 结论

最后，我感到非常幸运，我能够仅使用命令行进行 C++ 开发来完成课程。 我觉得我更多地了解了这个过程，了解了语言的工作方式，并且能够以一种我可以匹配使用 GUI 的效率来完成工作。