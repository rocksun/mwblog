
<!--
title: Jujutsu：像武术一样处理版本控制
cover: https://cdn.thenewstack.io/media/2025/02/db5c82a9-natalia-blauth-znrnassj8f0-unsplashb.jpg
-->

> 译自：[Jujutsu: Dealing With Version Control as a Martial Art](https://thenewstack.io/jujutsu-dealing-with-version-control-as-a-martial-art/)
> 
> 作者：David Eastman

Jujutsu 是 Google 使用的版本控制系统，它为许多开发人员使用的 git 系统提供了一种替代方案。我们来看看。

和多年来的大多数开发人员一样，我习惯了每天需要用到的一些 git 命令，并尽量避免陷入大型合并冲突。即使我经常推动 git 的使用，我还是会告诉开发人员，如果他们不记得如何操作，就去 Google 搜索，而不是试图记住各种场景。我记得当从 [Apache Subversion](https://en.wikipedia.org/wiki/Apache_Subversion) 迁移时，不得不解释说，基本上你需要三个命令，而以前只需要两个，这引起了一些抵触。

从好的方面来说，我还记得一个初级开发人员删除了我们的中央存储库。然后我冷静地向这个人解释说，我们可能可以在几分钟内恢复它，因为 git 中的“中央存储库”更像是一种共同协议，而不是唯一的真理来源。

那么，为什么 Google 要使用不同的东西呢？我今天仍然在一些项目中使用 git，但主要使用 [Plastic SCM](https://www.plasticscm.com/)（现在由 Unity 控制），因为它完全适合大型文件。但是，什么可以打破 git 对大多数开发人员的束缚呢？

[Jujutsu](https://github.com/jj-vcs/jj) 登场了。在 Steve Klabnik 的 [教程](https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html) 中，他指出 Jujutsu（或 jj）是“一个 DVCS，它吸取了 git 的优点、Mercurial 的优点，并将它们合成为一种新的、但又出奇地熟悉的东西。”而且由于 Google 使用它，它不会突然消失。我知道 jujutsu 听起来像是像武术一样处理版本控制——这不一定是个好兆头，但可能是一个潜在的事实。

在这篇文章中，我将逐步介绍这些差异，所以我假设读者至少熟悉工作中的 git。

因此，使用 git，我们知道我们有**一个索引**、**一个暂存区**和**未跟踪的文件**。这就是你在完成一些工作后使用 `git status` 时，git 告诉你的内容：

![](https://cdn.thenewstack.io/media/2025/02/debb90ab-image-1024x619.png)

因此，git 识别已经跟踪的已更改文件和出现的未跟踪文件。

## 工作副本

如果你曾经使用过 `git stash` 或者被告知“你对以下文件的本地更改将被合并覆盖”，那么你基本上了解 git 将你跟踪和未跟踪的更改视为可能与上游中央存储库中的内容不同的实体。

Jujutsu 通过将工作副本表示为一个新的提交来消除暂存区或索引。因此，检出一个提交会导致在目标提交之上创建一个新的工作副本提交。如果你经常使用 `git add .` ——它暂存所有新文件和修改——你已经认为你正在处理的所有内容都是你下一个提交的一部分。因此，Jujutsu 的大简化可能对许多用户和用例都有意义。

好的，现在我已经解释了一些有趣的事情——而且我们已经知道 jj 与 git 兼容——让我们安装它并试用一下。

## 开始使用

由于 jujutsu 是用 Rust 编写的，所以有很多方法可以 [安装它](https://jj-vcs.github.io/jj/v0.23.0/install-and-setup/)。使用我的 MacBook，我只需使用：

```
brew install jj
```

现在，当我说“jj 与 git 兼容”时，我的意思是 jujutsu 使用兼容的模型，而不是 jj 可以直接与现有的 git 仓库一起工作。如果我尝试在 git 中使用一个简单的指令 `jj status`，我会得到：

![](https://cdn.thenewstack.io/media/2025/02/0df758b6-image-1-1024x172.png)

所以我们要做的就是在 jj 命令中继续使用 git，以表示我们想要 git 兼容性。我将从克隆一个熟悉的旧小演示开始：

```
> jj git clone https://github.com/octocat/Hello-World
```

![](https://cdn.thenewstack.io/media/2025/02/6c2a0bd2-image-2-1024x248.png)

就像使用 git 一样，我们被警告说我们还没有设置用户名和电子邮件。我们已经获得了关于这个仓库的线索，但让我们直接询问 `jj st` 的状态：

![](https://cdn.thenewstack.io/media/2025/02/52f7a09a-image-4-1024x166.png)

所以它把我们放在一个小的只读编辑器风格的程序中（称为“pager”，用“q”退出），但让我们详细看看这个响应。

现在，jj 显然使用了两组标识符：它使用了**变更 ID** 和**提交 ID** 的概念。工作副本上以“y”开头的第一个数字是变更 ID，以“3”开头的第二个数字是提交 ID，父提交有它自己的一对。我们还可以看到父提交上看起来像 master 的分支名称。我们的工作副本没有设置描述，而父提交是一个 pull request。

如果我们开始我们自己的本地仓库并查看相同的信息，我们会在逻辑上学到更多。我们可以使用 `jj git init`，使用相同的逻辑，即 jj 使用 git 格式：

![](https://cdn.thenewstack.io/media/2025/02/c4d6d8a0-image-5.png)

这是来自我们的新仓库的 pager 中的内容：

![](https://cdn.thenewstack.io/media/2025/02/32dc5ab6-image-6.png)

现在我们可以看到父提交有一个非常具体的标识对，其中更改 ID 为“zzzzzzzz”，提交 ID 为“00000000”。不出所料，这被称为**根提交**。这次新添加的文件被标记为这样。请记住，没有索引。正如预期的那样，没有设置历史记录或分支名称。

我按照之前克隆时的建议设置了我的 `[user.name](http://user.name)` 和 `[user.email](http://user.email)`，所以我可以继续前进。现在，或者实际上，在任何时候，我都可以描述我的工作提交：

![](https://cdn.thenewstack.io/media/2025/02/fb7728d2-image-7-1024x181.png)

所以更改 ID 没有改变，但提交 ID 改变了。这告诉我们提交 ID 正在逐步跟踪更改，而到目前为止，所有内容都在同一个更改 ID 中。请注意，我们正在远离 git 术语。

所以让我们闭环并“签入”。我们通过说 `jj new` 来做到这一点。这是一个稍微不同的重点——我们标记的是开始而不是结束：

![](https://cdn.thenewstack.io/media/2025/02/08d1495d-image-8-1024x426.png)

所以你可以看到我们的工作副本变成了父副本，我们得到了一个新的工作副本。

这一切都很棒，但我们将在另一篇文章中进行更重量级的使用——但让我们以整体查看我们的 repo 来结束。

我几乎不使用 `git log`，但 `jj log` 是一种不同的动物。首先，让我们回到 Hello-World 目录，看看克隆的 repo 是什么样子的：

![](https://cdn.thenewstack.io/media/2025/02/2e598680-image-9-1024x222.png)

我们可以看到各种标记（一个 at 符号、一个菱形和一个波浪号）以及我们开始的提交的非常早的日期，以及我未使用的工作提交。请注意，我们自然的兴趣在于稳定的更改 ID。顺便说一句，更改 ID 中的品红色字符（和提交 ID 中的蓝色字符）表示一个字符足以唯一标识它。如果您使用过 git，您可能已经利用了这个概念来节省各种命令中的击键次数——jujutsu 明确地说明了这一点，这很好。

好的，让我们用我们新的 repo 做同样的事情：

![](https://cdn.thenewstack.io/media/2025/02/6378a170-image-10.png)

我们看到了根、我的第一次提交和新的工作提交。您现在可以看到 at 符号是工作副本提交，菱形在这种情况下代表根。我猜克隆中的波浪号表示“我们没有的历史记录”，留下圆圈表示“其他提交”。

## 结论

我们只看到了基本用法，但与 git 已经有很多不同之处——其中大多数是可以接受的，有些甚至很好。我需要在即将发布的文章中更认真地对 jujutsu 进行路测，看看使用它的感觉如何。
