# 一家公司重新思考 Diff 以缩短代码审查时间

![Featued image for: One Company Rethinks Diff to Cut Code Review Times](https://cdn.thenewstack.io/media/2024/09/32e5470e-gitclear.png)

一篇 [Stack Overflow 博客文章](https://stackoverflow.blog/2024/08/05/this-developer-tool-is-40-years-old-can-it-be-improved/) 将其称为“当代开发人员最广泛使用的最古老工具”。文件比较程序 [diff](https://man7.org/linux/man-pages/man1/diff.1.html) 已经存在了整整半个世纪。

时至今日，其底层的“Myers *diff* 算法”仍然出现在我们的工作流程中——包括我们在 [GitHub](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) 上查看更改的方式（使用红色突出显示更改的代码，绿色突出显示新代码）。

是时候换个角度思考了吗？即使是 *diff* 的官方 *info* 文件也指出，GNU 项目“已经确定了一些改进，作为志愿者的潜在编程项目”。

但 Stack Overflow 博客文章提供了一个引人入胜的案例研究，一家开发工具公司决定尝试构建一个更好的 diff...

## 全面了解 Alloy

Alloy.dev 的 [网站](https://alloy.dev/) 表示，该公司从事“优质软件产品”的业务，副标题承诺他们的工具“每天都被热爱构建软件的人使用”。并且它特别推出了两款产品，这两款产品“帮助有抱负的创作者从每个工作时间中获得最大价值”——其中之一是 Amplenote，一款笔记/待办事项列表应用程序。

然后是“[GitClear](https://www.gitclear.com/)”——该公司在经过三年的迭代后于 2018 年发布了这款产品。“对于 GitClear，我们渴望让拉取请求审查占开发团队一周时间的 1-5%，而不是 20%，”Alloy 的 [网页](https://alloy.dev/) 上写道。

*Harding 和他的团队添加了新的方法来显示代码何时只是被移动、收到少量更新或经历了来自查找和替换命令的名称更改。*

该公司在进行了一些研究后发现，只有 5% 的 [代码更改](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) 是真正“实质性”的更改，Alloy 创始人/首席执行官 Bill Harding 在他的 [2022 年演示](https://www.youtube.com/watch?v=11WQeDdGlgI) 中说，其余的都被他们认为是“更改噪音”。

大约 30% 的拉取请求中所有更改的行只是代码块，这些代码块只是被移动到一个新的位置。“为什么开发人员仍然阅读拉取请求，其中这 30% 的未更改代码与应该引起注意的实质性更改一样突出？”Harding 问道。

正如 Harding 在 [6 月份的演示](https://www.youtube.com/watch?v=ZulFo7DijWU) 中所说，“我们希望帮助开发人员尽可能少地审查代码。”

## 构建一个更好的 Diff？

在 Stack Overflow 上的一篇客座文章中，Harding 描述了 Alloy 如何首先对一组新的 diff 运算符进行实验。他的目标是看看“更深层的词汇表”是否可以压缩提交的表示方式。“更改是否可以比近 40 年前更简洁地显示？”因此，除了添加和删除之外，Harding 和他的团队还添加了新的方法来显示代码何时只是被移动、收到少量更新或经历了来自查找和替换命令的名称更改。

Harding 在 [另一个视频](https://www.youtube.com/watch?v=zj8TIGpbaGs) 中说，减少行数会让事情变得更好。“这最终可以让你有更多时间来编写代码，而不是审查代码。”

Alloy 提供了几个示例和 [视频](https://www.youtube.com/@gitclear5499) 来证实他们的说法，即他们的工具可以使拉取请求中需要审查的代码减少 30%。

## 工作原理

显然，它的有用性取决于它试图总结的内容。但是，当代码块被移动到一个单独的函数中时，GitClear 不会突出显示所有移动但仍然相同的代码——只突出显示新添加的方法定义。

Harding 的博客文章还重点介绍了一个案例，他们对一个常量值进行了微小的更改——在前面添加了一个 0。该工具不是将其显示为删除一行然后添加另一行不同的行，而是简单地显示更改的行及其更改的字符（并内联显示）。

最终结果？需要审查的“更改行”减少了大约 28%——Harding 认为这是一个明显的胜利。“这意味着更新 git diff 处理工具可以将需要审查的行数减少近三分之一。”

Harding 甚至表示，他们从 CodeMentor 招募了 48 名测试对象来审查拉取请求——其中一半来自 GitClear。结果发现对代码的“理解程度相同”。但是，由于需要审查的行数更少，因此审查所花费的时间更少——平均减少了 23%，中位数减少了 36%。

## 其他功能
当我向该公司提交了一个指向“[替代拉取请求审查工具](https://www.gitclear.com/best_github_alternative_pull_request_review_tool)”的 URL 时，GitClear 向我发送了一封电子邮件，重点介绍了使用该工具我可以节省多少行代码审查工作……

但他们的工具还包括其他功能。

访问拉取请求会调出一个概述页面，提供 Harding 所谓的“拉取请求当前状态的高级详细信息……以及它与之前提交的拉取请求的比较”。一个图表显示了拉取请求已打开的天数——甚至允许你将它与存储库中的其他文件进行比较——或者与所有存储库的拉取请求进行比较，甚至“与你所在行业的其他公司进行比较”。（另一个图表对拉取请求中的测试覆盖率进行了相同的比较。）

然后是“差异增量”的图表，该公司的网站将其吹捧为 GitClear 的专有但“[经验证的评估](https://www.gitclear.com/diff_delta_factors)”，用于评估每次提交发生的持久性更改量”，将提交的整个历史记录编织在一起，以跟踪“每个作者代码行的长期命运——通过移动、重命名和其他更新”。

他们添加了其他方法来尝试改进代码审查体验。在[视频演示](https://www.youtube.com/watch?v=ZulFo7DijWU)中，Harding 指出他们的工具还提供了一个视图，仅显示“自上次审查以来的未审查提交”

“对于我们团队的工作方式来说，这可能是节省时间最多的单一功能……因为如果你的团队对拉取请求进行了多轮审查，你肯定感受过试图查看之前已经看过的文件并挑选出‘哪些更改是对我的反馈的回应？哪些更改已经存在，我之前已经看过了？’的痛苦。”

还可以[回溯时间](https://youtu.be/ZulFo7DijWU?si=P2eSN4QwB6bf4XvL&t=317)。将鼠标悬停在某行上会显示其提交消息的完整历史记录，“这通常可以阐明为什么特定行演变成其最终形式，”Harding 在他的博客文章中解释道。这意味着，即使一行代码被移动——并且可能被查找和替换命令更改——该行的原始位置仍然可用。[他们的文章认为，看到代码出现在应用程序的过去版本中很有用。]

## 代码审查时间更少
Harding 的文章最后为他们的工具进行了辩护。审查那些额外的 28% 代码行要花费多少时间？Harding 估计，一个 10 人的团队每周要花费数千美元。Harding 还建议开发人员可能更喜欢在代码审查上花费更少的时间。

“考虑到代码审查通常是开发人员职责中最[令人不快、需要高度意志力的工作](https://stackoverflow.blog/2024/07/05/what-can-devs-do-about-code-review-anxiety/)之一，减少代码审查时间带来的士气提升可能与‘节省时间’带来的收益相当。”

它并不是唯一的替代方案。在 Harding 故事的评论中，一位名为[Difftastic](https://github.com/Wilfred/difftastic) 的其他替代方案的粉丝。

在[2022 年 GitKon 的一次演讲](https://www.youtube.com/watch?v=11WQeDdGlgI)中，Harding 承认现在至少有 10 家公司提供 Git 分析/开发人员分析工具（通常与问题跟踪相结合）。

但 Harding 的帖子在网络上引发了一些关于代码审查工具现状的热烈讨论。Stack Overflow 的一些长期读者在他们的博客文章中留下了他们的评论：

- “能够识别带有注释块和通常尾随空行的完整函数作为一个单元，因此是一个更改，这将非常棒”
- “如果差异能够识别重命名的文件……那就太好了”
- “审查过程中的许多改进可以来自有意地将提交分离，以方便审查。
无论未来会发生什么，人们显然都渴望获得最好的代码审查工具。也许这并不难理解。

在[2022 年的另一场演讲](https://www.youtube.com/watch?v=11WQeDdGlgI)中，Harding 笑着说，“开发人员天生对编写代码比对审查代码更有热情。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)