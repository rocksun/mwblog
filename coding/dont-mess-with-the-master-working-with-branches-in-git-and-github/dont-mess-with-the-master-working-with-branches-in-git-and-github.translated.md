# 如何在 Git 和 GitHub 中使用分支
![Featued image for: How to Work With Branches in Git and GitHub](https://cdn.thenewstack.io/media/2018/05/e49988cf-tree-3369950_640.jpg)

在之前关于 git 版本控制软件的两篇教程中，我们学习了 [使用 git 的基本命令](https://thenewstack.io/tutorial-git-for-absolutely-everyone/)，以及 [如何使用 GitHub](https://thenewstack.io/git-with-the-program-getting-started-with-github/) 来建立仓库并将我们的项目代码推送到网站。

现在是时候开始真正使用 GitHub（和 git）了，它们的设计初衷是：在项目中安全地将更改放到一边，并在证明它们是正确的（或者至少不是灾难性的）之后再将它们合并回原始项目。

首先，快速回顾一下：什么是 git，它与 GitHub 有什么区别？

## 什么是 Git？
如今，绝大多数现代软件项目都依赖于 [git 版本控制系统](https://git-scm.com/downloads) 来管理其代码库中的更改。在 [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) 于 2005 年开发 git 作为开源版本控制工具之前，开发人员依赖于单线程系统（如 CVS 或 SVN）来跟踪其软件的完整历史记录。

然而，Git 的分布式架构为每个参与特定项目的开发人员提供了对代码工作副本的访问权限，该副本作为包含代码库所有更改的完整历史记录的仓库。

## Git 和 GitHub 之间的区别是什么？
Git 是一种工具——版本控制系统本身。作为开发人员，您会在本地机器上安装 git 并使用它。像 GitHub、[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 和 BitBucket 这样的平台通过在云端托管 git 仓库，使使用 git（尤其是在团队项目中）更加用户友好，开发人员可以在云端存储、共享和与他人协作编写代码。（在本教程中，我们使用 GitHub，但其他基于 git 的版本控制平台的工作方式相同）。

## 什么是 Git 分支？
现在您已经了解到，git 将项目的每个版本保存为代码的快照，该快照与您提交时的代码完全相同。您使用 git 创建项目不同版本的进度时间线，以便在出现问题时可以回滚到早期版本。

git 和 GitHub 管理此时间线的方式（尤其是在多人协作并进行更改时）是使用分支。分支本质上是一组具有唯一名称的独特代码更改。

每个仓库可以有一个或多个分支。主分支（所有更改最终都会合并回该分支）被称为 `main`，这很贴切。当您访问 `github.com/yourname/projectname` 上的项目仓库时，您会看到此版本。主分支是任何基于 git 的 GitHub 项目的官方工作版本，无论是开源项目还是商业项目。对于生产软件，`main` 通常是当前为用户部署的分支。

但是，所有项目都遵循相同的根本原则：**不要修改主分支。**

如果您在其他人也在修改主分支时修改了团队项目的 `main` 分支，您的即时更改将波及到所有人。您合并的代码现在是新的主版本……因此，任何其他人都在自己的本地分支上工作的人现在都在使用过时的版本，并且不知道有任何更改。也就是说，直到他们尝试将自己的更改分支合并回 `main`，才会遇到可怕的 [合并冲突](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts) 错误消息。

这会导致哭泣、撕裂衣服，以及人们头发着火地尖叫着四处乱跑——合并冲突可能非常严重。但即使它们不严重，它们仍然会浪费那些必须追踪 `main` 与他们自己的工作版本分叉的位置，然后协调所有差异的人的时间。

为什么 `main` 如此不可触碰？一个词：可部署。主分支是您的生产代码，准备发布到世界。`main` 应该保持稳定。开源软件的普遍社会契约是永远不要将任何未经测试或导致构建失败的内容推送到 `main`。

GitHub 对所有人（从个人开发者到拥有数百名开发人员的大型商业项目）都有效的全部原因是，从 `main` 工作始终是安全的。（这也是许多组织使用“不要合并自己的拉取请求”文化作为保障措施的原因，以确保没有人会无意中将更改推送到 `main`，从而导致所有人的所有内容都崩溃）。

## 如何在 Git 中使用分支

### EDITOR'S RESPONSE
与其直接在主分支上工作，每个人都会从主分支创建新的分支来进行实验、修复错误，以及进行一般性的编辑、添加和更改。准备就绪后，这个新的版本分支将被合并回主分支——但前提是代码已获批准且已知可以正常工作。然后，主分支将更新为包含所有新内容。

要开始在项目中进行任何新的工作，或更改现有内容，您需要从稳定的主分支创建分支。让我们继续使用为之前的教程创建的示例项目，也就是我们熟悉的 `studious_octo_carnival`。请现在打开您计算机上的版本，并进入目录。

### 第 1 步：盘点。
在创建新的分支之前，我们要检查是否存在其他现有分支。我们知道主分支，但谁知道我们的项目合作者在做什么，那些淘气的猴子？

因此，第一步是通过在终端中键入 `git branch -a` 来查看所有现有分支，这告诉 git 我们想要查看此项目中的 *所有* 分支，即使是那些不在我们本地工作区中的分支。

对于我们的项目，git branch 命令返回您在下面的代码示例中看到的输出。它的外观可能略有不同，具体取决于您的操作系统和终端应用程序，但信息最终是一样的。输出第一行中 `main` 旁边的星号表示我们当前位于该分支上。第二行告诉我们，在我们的远程仓库（名为 origin）上，有一个名为 `main` 的分支。（请记住，我们的远程仓库是此项目的 GitHub 仓库）。

### 第 2 步：创建新的分支
现在我们已经知道如何查看分支，让我们创建一个！请记住，我们有来自之前教程的原始项目作为 `main`。

我们现在将创建一个本地分支作为下载到我们自己计算机上的项目的新的副本版本。这样，我们就可以在本地（在我们自己的开发环境中）对项目进行修改和更改，而项目的原始版本 `main` 仍然安全地保存在 GitHub 上。我们给新分支一个描述性的名称，以提醒我们打算在其中进行什么操作。在本例中，它将是一个简单的“Hello World”东西，所以让我们将其命名为 `hello_octo`。

要创建此新分支，请键入 `git checkout -b branchNameHere`（因此，在本例中，为 `git checkout -b hello_octo`）。

假设还没有其他人创建名为 `hello_octo` 的分支，git 将返回“Switched to a new branch ‘hello_octo’”。（如果已经存在同名分支，git 将改为告诉我们“fatal: A branch named ‘hello_octo’ already exists.” 没什么大不了的，只需使用 `git checkout -b` 再次使用新的名称变体）。

我们还可以使用 `git checkout` 命令在两个分支之间来回切换。键入 `git checkout branchName` 切换到该分支。因此，`git checkout main` 将带您到主分支，而 `git checkout hello_octo` 将带您回到 `hello_octo` 分支。

如果您尝试切换到不存在的分支，例如 `git checkout hello_kitty`，git 会告诉您这是不行的：

git 如何知道您当前位于哪个分支？git 始终监控您的操作，并保留一个名为 HEAD 的特殊指针。就像指南针上的指针始终指向北方一样，HEAD 始终指示您当前所在的本地分支。

我们也可以使用 git 命令 `git branch branchNameHere` 创建分支，然后使用 git checkout 切换到该分支。但是，`git checkout -b branchNameHere` 中的 `-b` 这个小巧的快捷方式既创建了分支，又切换到了该分支。

我无法告诉您有多少刚接触 git 的程序员会生成错误消息和挫折感，因为他们只是忘记了在创建新分支后切换到该分支。因此，我们坚持使用 `git checkout -b`，好吗？

## 对工作分支进行更改
现在我们有了多个分支——我们的工作分支用于进行更改，我们的主分支保持安全不变——我们可以开始工作了。在我们的场景中，我们将使用 `hello_octo` 分支来进行和测试我们的更改，然后将这些更改推送到 GitHub 上的主分支。

请记住，使用 `git branch -a` 确保您位于工作分支上，而不是主分支上。

### 第 3 步。创建一个名为 `hello_octo_world` 的新空白文件：
（此空白文件仅用于演示目的，因此不用担心没有文件扩展名/类型。）

由于它是全新的，因此现在此文件仅位于您的分支上。使用 `ls` 命令查看它：

但是，请记住，我们位于工作分支 `hello_octo` 上，我们在这里创建了这个新东西。主分支不知道 `hello_octo`，因为它被安全地隔离在我们在这里对工作分支进行的任何随意更改之外。它仍然是我们开始时所拥有的那个平静不变的主分支：

### 第 4 步：将我们的新文件暂存并提交到工作分支。

```
git add hello_octo_world
git commit -m "Created hello_octo_world file"
```
现在是时候将我们的新文件添加到工作分支并提交了。（听起来熟悉吗？）这将把这个新实体附加到工作分支，为最终将其移到主分支做准备。此文件现在存在于 `hello_octo` 分支上；正如我们上面看到的，它目前不存在于主分支上。

此时，您只是对分支的更改进行了快照。在现实世界的项目中，可能还有更多更改和工作要做。现在是您进行这些操作的时候了，在逻辑点进行 [提交](https://thenewstack.io/another-way-to-git-bundle-commits-into-logical-groups/)。

**请记住，在 GitHub 上，提交代表您连续的保存。** 每个提交都有一个关联的提交消息，它 [描述了您在那里做了什么以及为什么](https://thenewstack.io/getting-legit-with-git-and-github-the-art-of-the-commit-message/)。提交消息记录了您的更改历史，以便未来的您以及其他项目贡献者可以了解您做了什么以及为什么。

## 在分支之间合并代码
一旦我们最终完成了所有更改和添加 - 并且一切正常* - 就可以合并了。有趣的部分是在我们切换回主分支后（用 `git checkout main` 说出来！）。`Hello_octo_world` 似乎不见了，但它并没有 - 目前，它存在于我们的工作分支上。目前，我们在主分支上。主分支还不知道这个新分支的存在，因为我们还没有合并新分支（即将其推送到 GitHub）。

我再次向您展示这一点，因为它是在理解 git 中分支的核心：

现在：在这个练习中，`hello_octo_world` 代表对任何文件的任何更改（或添加一个全新的文件），这些更改已通过我们开发分支上的所有测试，并已准备好投入生产。在分支之间移动代码（通常是从开发到生产）的过程称为合并。

非常重要：合并时，我们需要在要合并到的分支上。基本上，我们会告诉 git，“看到那个新东西了吗？现在可以把它带到这里了。”

### 第 5 步：合并来自工作分支的更改
在本例中，由于我们要从工作分支（`hello_octo_world` 文件存在的地方）合并到主分支，因此我们需要在主分支上。

在主分支上后，我们只需运行合并命令。最好的方法是键入 `git merge --no-ff`。额外的 `--no-ff` 告诉 git 我们希望保留合并之前的所有提交消息。这将使将来跟踪更改更容易：

## 返回 GitHub
现在我们需要做的最后一件事是让 GitHub 知道我们一直在本地开发环境中修改 `main`。

换句话说，是时候 `git push` 了。你做得到！

git 输出确认从您的开发分支到本地环境中的主分支的合并现在已复制到远程服务器：“master → master”。

就是这样！我们已经：（1）成功创建了一个与主分支分离的本地工作分支。（2）对其进行了更改。（3）暂存并提交了这些更改。然后（4）将它们合并回本地工作环境中的主分支。最后，我们（5）将所有内容推送到 GitHub，以便我们项目的所有版本在任何地方都保持一致！

## 不要忘记清理
现在需要进行一些清理：由于我们已成功合并了 `hello_octo` 分支，因此我们不再需要它。保留它也可能会混淆对新分支的未来更改，因此让我们摆脱它。

要删除已合并的分支，只需键入 `git branch -d branchName`：

不用担心：如果您不小心尝试删除尚未合并的分支，git 会抛出错误。

所以！到目前为止，我们一直在使用一个极其简化的示例项目，因为此时最重要的是理解和吸收 git 工作流程。在现实世界中，合并比这要复杂得多 - 例如，如果您的合并出现冲突，会发生什么？不用担心，新的 git 用户，我们会到达那里。

您的作业：在示例项目中创建（`touch`）一些新的文件，并练习进行更改、暂存、提交，最后将它们合并回来。注意您的 HEAD 指向哪里 - 也就是您当前的分支是什么。只将更改提交到您的工作分支。

因为，请记住：不要。弄乱。主分支。

*Git 入门系列的下一部分：克隆和分叉*
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)