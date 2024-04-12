## 代码在上下文中：人工智能如何帮助我们改进文档

![代码在上下文中：人工智能如何帮助我们改进文档的特色图片](https://cdn.thenewstack.io/media/2024/04/c821a0c8-adam-davis-jqrxx47932o-unsplash-1024x683.jpg)

虽然我写过一些 [Steampipe](https://hub.steampipe.io/plugins/turbot/hypothesis) [插件](https://hub.steampipe.io/plugins/turbot/mastodon)，但它们只需要对 [插件 SDK](https://github.com/turbot/steampipe-plugin-sdk) 有基本的了解。我肯定不是唯一一个难以理解其更高级机制的人。在 2022 年的年度公司黑客马拉松中，我参加了一场为期一周的冲刺，以改进 SDK 的文档，与包括 Steampipe 的首席开发人员（他是 SDK 的作者）在内的几位团队成员合作。这次练习产生了一篇关于 [Go 中的读写编程](https://www.infoworld.com/article/3677772/literate-programming-in-go.html) 的有趣文章，但结果并没有真正推动进展。

从那时起，我阅读了很多插件代码，也写了一些，但仍然不相信自己有能力理解、应用和解释几个关键模式。我确信 LLM 协助会改善我们 2022 年文档冲刺的结果。我们无法重复该实验，但我借助 [Unblocked](https://getunblocked.com) 进行了另一次尝试，这是一个新的 LLM 支持的开发者工具，它较少关注编写代码（尽管它也这样做），而更多关注理解代码。正如创始人 Dennis Pilarinos [所说](https://www.itshipped.fm/episodes/20)：

为此，Unblocked 不仅可以像 [Sourcegraph 的 Cody](https://thenewstack.io/codys-bot-serves-enterprise-info-in-slack-workspaces/) 那样获取你的代码存储库，还可以获取相关材料——你的网站、产品文档、你在 GitHub 问题和 Slack 中的对话——以便提供我称之为 *上下文汇编* 的服务。我从 Jack Ozzie 那里学到了这个术语，当时他与他的兄弟 Ray 合作开发 [Groove](https://www.jonudell.net/bytecols/2000-10-25.html)，这是 Ray 最伟大的作品 Lotus Notes 的点对点继任者，它开创了后来被称为知识管理的领域。与 Notes 一样，Groove 将信息工作带入共享空间，你可以在其中同时搜索邮件、日历、文档和数据。

如今，为了为我们真正需要做的工作构建上下文，我们在 Slack、Google Docs、GitHub 和电子邮件中搜索时付出了太多努力。如果我们有有效的 [元搜索](https://www.infoworld.com/article/3663031/tired-of-searching-slack-github-and-google-drive-separately-do-it-all-at-once-in-sql.html)，那会有所帮助。但即便如此，我们也只会运行并行关键字查询，并在我们的头脑中进行上下文汇编的繁重工作，或者将税收转嫁给同事。Unblocked 旨在减轻软件团队承受的认知税收负担。

这是我重新审视我们 2022 年文档冲刺的机会，并配备了我希望当时拥有的工具。我们的目标之一是用 SDK 惯例的示例丰富文档，并链接到可以在其中按上下文查看这些示例的源代码。Unblock 查找此类示例的能力可能是它在此次重写期间提供的最大好处。有一次，我正在寻找使用 List 函数（它使用主 API 调用的结果填充 Steampipe 表的某些列）和 Hydrate 函数（它使用辅助 API 调用的结果填充其他列）的混合的插件代码示例。“List”和“Hydrate”这两个词无处不在：在插件 SDK 本身的代码中，以及每个插件的代码中。如果你正在寻找一个结合这两种函数的示例，传统的代码搜索是无望的。但你可以向 Unblocked 提出这样的问题：

并得到这样的答案：

可以在 *steampipe-plugin-aws 存储库* 中找到 List 函数与 Hydrate 函数结合使用的良好示例。在 [table_aws_fms_app_list.go](https://github.com/judell/steampipe-plugin-aws/blob/HEAD/aws/table_aws_cloudcontrol_resource.go) 文件中，*listFmsAppLists* 函数用作 *List* 函数来获取所有 AWS Firewall Manager (FMS) 应用程序。此函数获取所有 FMS 应用程序。对于每个应用程序，它将应用程序作为一行流式传输到表中。

然后，
*getFmsAppList* Hydrate 函数用于获取每个应用程序的更多详细信息。此函数使用特定列表 ID 向 AWS FMS 的 *GetAppsList* API 发出 API 调用，并将结果作为单行返回。

这是 Steampipe 插件中的常见模式：List 函数获取资源列表，然后一个或多个 Hydrate 函数为每个资源获取其他详细信息。
**这是一种与我们习惯的截然不同的搜索**

我无法假装知道它是如何工作的，我也不确定是否有人能完全解释它，但我的天真理解是，当你向 LLM 提出这种问题时，你并不是在寻找单词，而是在寻找一种模式。我认为，能够在文档语料库中识别和定位此类模式的工具将帮助我们最终实现知识管理的承诺——在软件领域，而且更广泛地实现。

**在 Ben Lorica 的**

[数据交换](https://www.youtube.com/watch?v=MAuaIXOmb34&t=2115s)中，[克里斯·威金斯](https://datascience.columbia.edu/people/chris-h-wiggins/)对我们现在称之为 AI 的历史进行了精湛的调查，他指出，它过去被称为机器学习，但在此之前被称为模式识别。

以下是 Ward Cunningham 介绍开创性的

[Portland Pattern Repository](https://c2.com/ppr/about/patterns.html)（它也是世界上第一个 wiki）的方式。

与

[其他 LLM 支持的工具](https://thenewstack.io/creating-a-gpt-assistant-that-writes-pipeline-tests/)类似，Unblocked 可以访问全局文档以及可以摄取的本地文档。这使它能够帮助我梳理出定义 Steampipe 表的模式、包装底层 AWS API 的 AWS Go SDK 中的相应数据结构以及原始 API 之间的关系。我们的系统越来越多地以这种方式分层。在全局和本地上下文中对代码和文档进行面向模式的搜索，感觉像是一种在层之间导航的强大方式。

## 解释模式

我的目标是阐明 Steampipe 插件 SDK 支持的模式，并将其融入构建在 SDK 之上的插件套件中。虽然找到此类模式的示例是 Unblocked 对重写的重大贡献，但它也帮助我解释了它们。我们并不是从头开始——源代码注释和网站上都有大量材料。这意味着我可以应用

[与大型语言模型合作的最佳实践](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)中的规则 4：*要求合唱解释*。在 Mike Caulfield 的

[原始表述](https://hapgood.us/2016/05/13/choral-explanations/)中，Quora 和 StackOverflow 等问答网站邀请了合唱解释。

我以多种方式应用规则 4。如今，我经常向 ChatGPT、Claude 和 Gemini 提出相同的问题。这样做既快速又容易，对于任何给定问题，点击的答案可能来自这三个中的任何一个。但向同一个 LLM 多次提出相同的问题也很有价值，用不同的方式表述以引出不同类型和级别的解释。在这种情况下，对于像

[José Reyes](https://jreyesr.github.io/tags/steampipe/)这样的专家来说，预先存在的文档可能就足够了，他可以跳入代码库并直观地——立即且深入地——了解正在发生的事情。我不像他那样，我相信许多其他人也不像他那样。在数学课上，我属于那种无法理解证明的速记解释的学生，而是需要详细说明证明的步骤，最好以不同的方式展示。

让老师这样做会扰乱课堂秩序，这就是我

[特别兴奋](https://thenewstack.io/using-ai-to-improve-bad-business-writing/)可汗学院的新 AI 导师 Khanmigo 的原因。

同样，让我向我们的架构师和首席开发人员询问此类重新表述也会造成干扰。在 Unblocked 能够提供它们的情况下，我在努力更好地理解和解释我们的系统时不会受到阻碍——没有双关语！——我不想夸大这种影响，我认为它有限且刚刚起步，但它是真实的，并且指出了获得代码理解的新途径。

## 审查改进

在我完成重写的每一部分时，我反复提示 Unblocked 我提出的新版本并邀请审查。有时它发现没有要添加或更改的内容。这是一个信号，表明该部分正在发挥作用。当然，这不是一个万无一失的信号！但它仍然很有用。

不过，有时 Unblocked 会做出实质性贡献。以下是它对完整草稿的审查。

这些都是我几乎逐字包含的好建议。如果可能将 Unblocked 作为由此重写练习产生的拉取请求的合著者，我会这么做。这感觉像是一种真正的协作，在我看来，这是 AI 的最佳情况。

## 文档压力测试

与此处描述的重写无关，我最近有一个问题
[Datatank](https://turbot.com/pipes/blog/2023/10/datatank-launch)，[Pipes](https://turbot.com/pipes)（Steampipe 的托管版本）的一项功能，可保留在其他瞬态查询结果中。

我的问题是：你能编辑定义 Datatank 自定义查询的 SQL 吗？我相当肯定答案是肯定的，但自从我使用该功能以来已经有一段时间了，所以我询问了 Unblocked，它说不行。

我重新检查并确认你确实可以编辑该 SQL，所以我将 Unblocked 的答案标记为错误，然后我再次查看了文档，果然，我们没有明确表示你可以编辑 SQL。所以我撤回了我的投诉，并向文档添加了此说明。

后来我问了同样的问题，得到了这个答案。

这部分是正确的。是的，你可以编辑 SQL。但不用等到下次计划更新。我自己也不确定这一点，所以我进行了一次测试更新以确认（正如我添加的注释所解释的）查询立即运行，然后按计划运行。

所以 Unblocked 并没有完全正确。但是，一如既往，你应该应用
[规则 2](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)：*永远不要信任，始终验证*。Unblocked 为你提供了链接。使用它！

我在这里的收获是我从未考虑过的事情。一旦 Unblocked 等工具吸收了我们的文档，我们就可以提出我们希望文档回答的问题，并检查它们是否确实如此。此类工具甚至可以提出问题以进行此类压力测试。事实上，Unblocked 已经做到了。

调整文档以解决所有这些问题可能是矫枉过正，但考虑它们是有用的。

## 修订和扩展

从头开始编写文档与从头开始编写代码一样不常见。更常见的是，你正在更新、扩展或重构现有文档。我的期望是，一个由代码和文档预先准备的 LLM 驱动的工具可以提供强大的帮助，而 Unblocked 做到了。

我不知道如何衡量它给我的提升。但我确实知道，我再也不想在没有可以帮助我汇编必要上下文的工具的情况下承担此类项目。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)