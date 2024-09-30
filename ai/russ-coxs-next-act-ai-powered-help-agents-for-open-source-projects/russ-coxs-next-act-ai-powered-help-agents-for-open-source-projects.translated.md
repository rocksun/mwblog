# Russ Cox's Next Stop: AI-Powered Help Agents for Open Source Projects

![Russ Cox's Next Stop: AI-Powered Help Agents for Open Source Projects](https://cdn.thenewstack.io/media/2024/09/8ffa6c69-github-profile-for-go-tech-lead-russ-cox-and-for-the-gaby-help-bot-he-created-1024x638.jpg)

Russ Cox's next stop looks like it might be his last, at least until he's replaced by a ChatBot.

When Cox [stepped down](https://thenewstack.io/russ-cox-steps-down-as-tech-lead-of-go-programming-language/) as [tech lead](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/) of the [Go language](https://thenewstack.io/how-golang-evolves-without-breaking-programs/), he emphasized in his August 1 [announcement](https://groups.google.com/g/golang-dev/c/0OqBkS2RzWw): "I'm not leaving the Go project..."

But beyond "occasionally" discussing design, answering questions, advocating for Go, and submitting issues, Cox will be focusing on an interesting new Go-related project that launched in June. Cox's larger goal is to help all open source maintainers with a tool architecture that can "automate the kinds of routine tasks that machines can reasonably do..."

"[Maintainer workload] is not unique to the Go project," the [homepage](https://pkg.go.dev/golang.org/x/oscar/internal/gaby) asserts, "so our goal is to build an architecture that any software project can reuse and extend, building their own agents to meet their project's needs."

## Can I Help You?

The [README file](https://github.com/golang/oscar/blob/master/README.md) on GitHub describes the code behind the project as an "open source contributor agent architecture" for "creating automated help or 'agents' for open source maintainers." They've named it OSCAR—an acronym for (O)pen (S)ource (C)ontributor (A)gent a(R)chitecture.

"Acting as a project search engine is still not the best use of a maintainer's time," Oscar's README file notes. But an automated agent can be on call, ready to instantly "present relevant project context" from past issue reports (as well as pull requests/changelists, documentation, and forum discussions).

The README file acknowledges that the project is "very much an experiment." But it notes that the first prototype contributor help agent has successfully executed "many" interactions for issues submitted to the Go programming language.

On June 7, Cox [announced the surprise release of a first prototype agent named Gaby](https://github.com/golang/go/discussions/67901#discussion-6793082), powered by Google's Gemini LLM. Its first task? Automatically adding hyperlinks when a specific changelist number is mentioned in an issue. (This led to Cox's first change to Gaby—telling it to ignore pull requests and focus only on editing *Issues*.)

The same day, Cox taught Gaby to rewrite any Google internal URLs that appeared in submitted issues, replacing them with their public counterparts. Within days, more feature requests began appearing in the discussion...

![Screenshot of reactions to Gaby bot launch announcement on June 7, 2024](https://cdn.thenewstack.io/media/2024/08/31a9193b-screenshot-of-reactions-to-gaby-bot-launch-announcement-on-june-7-2024.png)

Cox's announcement of Gaby's release generated a lot of buzz—including 133 thumbs-up.

But Gaby's biggest impact seems to be automatically posting what it identifies as "similar issues" when a new issue is submitted—"a list of up to ten highly relevant links to provide context for the report." (Cox noted in his June 7 announcement that Gaby only posts if it "finds enough similar links." Otherwise, it stays silent.) But he also noted that on Gaby's first day of operation, its "similar" links did correctly identify when duplicate issues were submitted.

Gaby's documentation notes that the agent's responses have been "very helpful." One grateful contributor even started their [reply](https://github.com/golang/go/issues/68196#issuecomment-2191837536) to Gaby with "Good bot :)"

In ten weeks, Gaby has already [commented on nearly 600 different Go issues](https://github.com/golang/go/issues?page=9&q=is%3Aissue+is%3Aopen+commenter%3Agabyhelp)—370 closed, and another 216 open.

Soon, Go's issues had a new label available: [gabywins](https://github.com/golang/go/issues?q=label%3Agabywins+is%3Aclosed).

## LLM... or Not

"Posting information about related issues is a limited form of analysis," Oscar's documentation acknowledges, "but we plan to add other types of semantic analysis, such as determining if an issue is primarily about performance and should have the 'performance' label added."
“我们还计划探索是否可以对报告进行充分的分析，以确定是否需要更多信息才能使报告有用。” 有一天，代理甚至可以在沙箱中重现错误，以查看它影响了哪些版本——“甚至使用 *git bisect* 来识别引入错误的提交。”

未来还会有哪些？可能的“扩展目标”包括自动标记问题或联系维护人员以获取关键的变更列表。（并且已经有一些关于 Gemini 的初步实验，以查看它在“从可用工具中选择并调用可用工具以满足维护人员提出的自然语言请求”方面的表现。）

“另一个扩展目标可能是识别何时问题需要更多信息并请求该信息。” 虽然 [Gaby 的文档](https://pkg.go.dev/rsc.io/gaby) 直言不讳地承认“不能保证今天的 [大型语言模型] 能够很好地工作，以构建该模型的有用版本。” 文档的最后几段甚至提出了 Gaby 有一天会进行“互动对话”的可能性。

“总的来说，我们相信有一些好主意，可以让基于 LLM 的机器人帮助项目维护人员的工作更轻松、更少单调，并且它们正在等待被发现。”

“也有很多不好的想法，必须过滤掉它们。理解差异需要大量的关注、思考和实验。我们还有工作要做。”

“这项工作的一些方面可能涉及 AI/LLM；有些则不会。”

该项目戏谑地指出，它还希望确定 LLM“不应该用于什么”。 但更重要的是，“指导原则是在创建对维护人员有帮助且维护人员喜欢的东西，这意味着在 LLM 有意义且有帮助时使用它们，但在没有意义且没有帮助时不要使用它们。” 因此，例如，它强调其对 LLM 的目标不是让它们取代程序员。“毕竟，编写代码是编写软件的乐趣所在。”

相反，它设想 LLM 成为交互的“一小部分（但至关重要！）”——“专注于不那么有趣的部分，例如处理传入问题、将问题与现有文档匹配等等……”

Oscar 的文档甚至展望了 Gaby 可以托管在其他平台（如 Google 的 Cloud Run）上的那一天，以便它可以与 GitHub 的基于事件的通知服务 Webhook 集成。 Gaby 使用 GitHub 的 REST API 下载问题跟踪器的状态以获取源材料（它还使用项目文档），Oscar 的 README 文件指出。“但架构使其易于添加其他来源。”

## 制定路线图
在 8 月 1 日的公告中，Cox 分享了他对担任 Go 技术主管 12 年后的角色的理解：“为你们所有人服务，并努力创造合适的条件，让你们所有人都能发挥出最佳水平。”

而且他似乎正在以其他方式继续这项工作——不仅仅是为了 Go 开发人员。 Cox 的公告中还表达了希望 Oscar 相关工作“将发现帮助开源维护人员的方法，这些方法将被其他项目采用，就像 Go 的一些最佳想法被其他项目采用一样。”

目前，Oscar 架构“正在 Go 项目的赞助下开发”，根据其 README 文件。“在未来的某个时刻，它可能会（也可能不会）被拆分成一个单独的项目……”

当 Cox 用一般性术语在他的公告中写道“我对 Oscar 的目标是构建一些有用的东西”，但也“学习一些新东西”——以及“为其他项目制定路线图”时，有一种令人心酸的感觉。 Cox 补充说，“这些是我一直以来对我们在 Go 上的工作所抱有的同样广泛的目标，因此从这个意义上说，Oscar 感觉就像是一种自然的延续。”

到 8 月 15 日，Cox 已经对 Oscar 进行了 13 次提交。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)