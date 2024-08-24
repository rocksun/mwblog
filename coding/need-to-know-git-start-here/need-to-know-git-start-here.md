
<!--
title: 从这里开始了解Git
cover: https://cdn.thenewstack.io/media/2024/08/9dcdffe9-git.png
-->

Git 并不一定是最容易使用的工具，但一旦你理解了它的运作方式，它就会变得自然而然。从这里开始。

> 译自 [Need To Know Git? Start Here](https://thenewstack.io/need-to-know-git-start-here/)，作者 Jack Wallen。

如果您是开发者，您可能听说过 [Git](https://git-scm.com/)。如果您不是开发者，或者刚刚开始成为开发者的旅程，[Git](https://thenewstack.io/developers-want-pragmatic-gitops-and-better-cd-tools/) 可能不在您的雷达范围内，[但它将会](https://thenewstack.io/beyond-code-control-git-for-everything/)。

最终，每个开发者都会[接触](https://thenewstack.io/git-is-15-years-old-what-now/) Git。甚至一些非开发者类型也使用 Git。事实上，来自世界各地的众多个人和组织都依赖于 Git。

根据 [Kinsta](https://kinsta.com/blog/github-statistics/) 的数据，全球约有 1 亿开发者使用 [GitHub](https://thenewstack.io/github-models-review-of-microsofts-new-ai-engineer-platform/)（基于 Git 的 Web 服务），超过 90% 的财富 100 强公司使用该服务。超过 [3000 万开发者](https://ir.gitlab.com/) 使用竞争对手的服务，[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 也是如此。几乎不可能估计有多少人使用 Git 本身，因为许多人将其用于内部，这意味着任何统计数据都不准确。可以肯定地说，Git 无处不在，您甚至不知道它。

但是，我所说的这个 Git 东西是什么？

Git 由 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/)（Linux 的创建者）于 2005 年创建。据他所说，他构建 Git 的原因有很多，但主要是因为他无法继续使用 BitKeeper 版本控制系统。

等等……什么？

好的，让我们稍微退一步。

## 了解 Git

要了解 Git，您必须了解版本控制，因为这是问题的核心。版本控制（或版本控制）是一种管理文档、计算机程序和其他类型信息更改的系统。版本控制对于协作环境至关重要，尤其是那些以软件开发为中心的协作环境。

使用版本控制，您可以更好地管理代码（或其他文档）随时间的变化。这样的系统会跟踪对文件进行的即使是最小的更改或更新。

Git 就是这样一个版本控制系统。事实上，Git 是市场上最流行的版本控制系统。Git 与存储库一起使用，存储库充当与项目相关的所有内容的集中式中心。

Git 可以与本地存储库和远程存储库一起使用（取决于您的需求）。Git 可以管理提交、分支、合并和克隆。Git 也是一个分布式系统，每个开发者都可以拥有项目的本地副本，以便离线工作。Git 速度快，能够扩展，使项目协作成为可能，跟踪所有更改，并且免费使用。

关键是：Git 并不是最容易使用的工具。它实际上相当复杂，需要学习，但是一旦您了解了它的功能，它就会变得轻而易举。

在开始使用 Git 之前，您需要了解某些术语。让我们深入了解这些术语。

## Git 术语

以下是一些您需要了解的基本术语，以便理解 Git。

### 拉取（Pull）

拉取是一个 [两步过程](https://thenewstack.io/getting-legit-with-git-and-github-your-first-pull-request/)，首先从远程存储库中拉取更改，然后使用来自远程分支的任何新提交更新您当前的分支。

### 推送（Push）

推送是 [拉取的反面](https://thenewstack.io/push-vs-pull-in-gitops-is-there-really-a-difference/)，因为它使用本地提交更新远程分支。默认情况下，推送只会更新远程上的相应分支。换句话说，如果您已从主分支检出代码，您推送的任何更改只会影响该分支。

### 合并（Merge）

合并用于 [将来自一个或多个分支的更改](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) 合并到当前分支中，并整合这些分支的历史记录，以便包含所有更改并解决所有冲突。

### 提交（Commit）

提交就像特定时间本地存储库的快照。应该经常进行提交，因为它们充当存储库中文件更改的历史记录。

### 初始化（Init）

要使用存储库，必须先对其进行初始化。

### 克隆（Clone）

要将远程存储库下载到本地存储库，您需要 [克隆它](https://thenewstack.io/development-git-clone-a-project/)。

### 来源（Origin）

来源是您发布提交的远程存储库的名称。默认的远程存储库称为“来源”。

### 暂存区（Staging Area）

这就像一个草稿，您可以在其中添加文件的最新版本，以便在下次提交时保存。

### 分支（Branch）

分支是一个新版本的主仓库，它能让您在主分支中进行各种方面的项目工作，而不会造成任何更改。

## Git 工作流程

现在让我们谈谈 Git 的使用方法。以下是一个基本的 Git 工作流程：

1. 在本地机器上安装和配置 Git。
2. 创建一个新的仓库。
3. 将文件添加到仓库。
4. 提交更改。
5. 检查仓库的状态。
6. 查看提交历史。
7. 创建一个分支。
8. 合并分支。
9. 将更改推送到远程仓库。
10. 从远程仓库拉取更改。

## Git 适合所有人

我说过它不是最容易使用的工具。更复杂的是，大多数人从命令行使用 Git。是的，有一些 GUI 可以简化 Git 的使用，但大多数开发人员倾向于坚持使用命令行。

说到这里，Git 可用于 Linux、macOS 和 Windows。对于 Linux，Git 在所有标准仓库中都可以找到，因此安装非常简单。对于 macOS，安装 Git 的最佳方法是发出命令 `git`，这将提示您安装应用程序。在 Windows 上，[下载此安装程序](https://git-scm.com/download/win) 并像您通常安装任何安装程序一样运行它。

现在您已经对 Git 有了基本的了解，在接下来的几个教程中，我将带您完成一个实际的 Git 工作流程，向您展示如何设置本地仓库并开始使用文件。
