人工智能的影响力已导致人们的关注点从搜索引擎优化 ([SEO](https://thenewstack.io/does-jamstack-or-wordpress-handle-seo-requirements-better/)) 转向答案引擎优化 (AEO)，即内容被优化以作为代理式答案呈现。此外，还出现了[生成式引擎优化](https://www.searchable.com/blog/geo-vs-seo-vs-aeo?utm_source=ads-google&utm_medium=cpc&utm_campaign=23642330155&utm_content=196203551253&utm_term=ai%20seo&utm_source=ads-google&utm_medium=cpc&utm_campaign=23642330155&utm_content=196203551253&utm_term=ai%20seo&gc_id=23642330155&h_ga_id=196203551253&h_ad_id=808018123338&h_keyword_id=kwd-307611916965&h_keyword=ai%20seo&h_placement=&gad_source=1&gad_campaignid=23642330155&gbraid=0AAAABDC7kber9zE3ZXZHBhrumDB40Ck1n&gclid=CjwKCAjwnvTUBhBoEiwAZNDxZ1DoBNzomZ30ZOVzeSIJ5yOGuZpcvzEsa-_zqmXq6Bm8HtxgEnmiThoCarsQAvD_BwE) (GEO)，品牌试图借此影响大语言模型 (LLM)。

软件工具本身是否即将重新调整，使得诸如 [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/)、[Codex](https://thenewstack.io/openai-codex-claude-code/) 和 [Cursor](https://thenewstack.io/cursor-3-demotes-ide/) 等代码助手表现出更强烈的偏好，从而选择特定的调试套件、渗透测试、迁移工具、包管理器、数据库（或者你选择的任何软件栈核心功能工具集）？

开发者工具增长服务公司 [Armature](https://armature.tech/) 认为答案是肯定的。

## （巨大的）利益攸关

Armature 在这一领域显然投入巨大，其在上周发布的一项[详细研究](https://armature.tech/blog/which-tools-coding-agents-install)中，作为其“如何影响编码代理选择”及促进产品被选中这一“更广泛工作”的一部分。该公司进行了一项实验分析，旨在了解编码代理如何看待工具、如何发现和挑选工具，以及在每个类别中最终胜出的是哪一个。

Armature 联合创始人 [Theodore Otzenberger](https://www.linkedin.com/in/theodore-otzenberger-895345131/) 告诉 *The New Stack*，软件开发者采用 AI 的速度和深度超过了任何其他职业，而且（随着模型变得更聪明，[框架/钩子](https://thenewstack.io/agent-harness-distributed-feedback-problem/)设计得更好），整个任务正被端到端地委托给代理。

“在分析中观察了 17,000 次工具选择会话后，我们看到工具供应商花费 20 年时间建立的品牌效应在瞬间冻结了，”Otzenberger 说。“当容器化需求出现时，代理会立刻联想到 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，但随后却忽略了其[现在提供的沙箱功能](https://www.docker.com/blog/docker-sandboxes-run-claude-code-and-other-coding-agents-unsupervised-but-safely/)，导致它最终并没有选择该工具。你的声誉会跟随你进入模型的参数权重中，附着在你赖以成名的产品上……但这种权重在今天以一种不同的重力规则运行。”

> “在分析中观察了 17,000 次工具选择会话后，我们看到工具供应商花费 20 年时间建立的品牌效应在瞬间冻结了。”

Otzenberger 提醒我们，现在是代理在决定将哪个工具接入代码库，这对当前的开发者工具供应商来说具有“生死攸关的影响”。这些供应商现在需要确保他们的工具被提及、被选中并提升到必备状态，以便被编码代理视为极具可用性。他确信，如果不这样做，它们明天就会“直接从技术栈中消失”。

## 决策者正在改变……

“我们公开了整个研究过程，包括发布了每一个跟踪记录和每一个提示词，所以任何人都可以验证我们没有偏袒任何一方，并了解它们当下的处境。这种格局会随着每一个新代理和新模型的出现而改变，所以我们很快将对 Astra 和 Fable 5.1 进行完整研究的重测。决策者正在改变，理解他们现在是一个工程问题，”Otzenberger 补充道。

Otzenberger 与联合创始人 [Louis Scremin](https://www.linkedin.com/in/louis-scremin/) 描述了他们如何观察不同类型人类开发者角色（涵盖氛围编程者、初创公司的初级工程师、企业的高级开发人员）在 1,163 种提示词变化下的数千次工具搜索会话。我们应该澄清，该公司展示的标题数字来自其 5,292 次会话的验证子集，而非完整的 17,000 次。

## 实验分析是如何进行的

搜索过程涵盖了 75 个存储库（即彼此独立的独特代码库），并研究了三个编码代理（Claude Code、Codex、Cursor），以检查代理将如何实际实施工具，而不仅仅是提供建议。

分析是在 GitHub 的公共存储库上运行的，团队提取了与编程语言和框架、第三方服务、部署平台、团队规模和代码库时长相关的统计数据。由于使用的开源存储库比企业软件巨头的软件更有可能是由初创公司构建的，因此团队根据公开数据对统计数据进行了去偏，以实现理想的面板分布。

随后，他们要求三个编码代理执行创建真实世界存储库的任务，以匹配代码库的确切要求。最后，他们生成了删除了代码库部分内容的变体。为了防止进一步的代理偏见，他们使用了虚构的公司名称，并配合人工生成的 Git 历史记录和虚构的 API 密钥。使用编排器创建了一个模拟的“人类参与循环”（Human in the loop），在本例中由 Gemini 3.7 Flash 扮演。

“模拟人类总是会选择顶级解决方案，或者要求编码代理选择最好的一个并实现它。但我们注意到，如果在开始时直接要求实现而不返回任何问题，会促使代理倾向于在内部构建所有内容，因为它无法请求授权去挑选特定的第三方解决方案。加入这个‘人类’环节后，减少了最初观察到的领导者[工具]和原生云平台解决方案的支配地位，转向了一个更现实的图景，”Armature 澄清道。

Armature 指出存储库背景是关键，这或许并不令人惊讶。当代理被派去询问获胜的电子邮件/通信服务提供商时，用四种不同语言编写的四个不同代码库返回了四个不同的获胜工具。

Armature 还发现，不同的编码代理使用不同的来源，最终它们会产生分歧。

* Cursor 在 2/3 的会话中将其决策建立在网络搜索基础上。
* Codex 几乎总是使用网络搜索（94% 的会话），但在 10 次查询中有 9 次会使用类似 site: 的运算符。
* Claude Code 主要依赖其先验知识，仅在约 30% 的情况下搜索网络。但当它搜索时，其浏览的页面数量是 Codex 的 3 倍。

所有三个代理在只有 42% 的情况下选择了同一个工具，且 Claude Code 自建工具的频率几乎是 Codex 和 Cursor 的两倍（19% 对 10%）。

![](https://cdn.thenewstack.io/media/2026/09/5a938d68-armature-image-1024x674.png)

## 这是通过后门进行的采购

Glokal AI OÜ 的创始人兼首席技术官 [Jeet Pattanaik](http://linkedin.com/in/jeet-pattanaik) 告诉 *The New Stack*，Armature 提供开发者工具增长服务的工作属于一种“因为激励机制存在而存在”的类别，这实际上是“通过后门进行的采购”。

“我最关注的发现是，被提及并不等同于获胜，”Pattanaik 说。“PayPal 被引用了 139 次，但从未被选中。LangChain 是提及次数最多的框架，有 194 次，但它只被选中了四次。这种差距就是整个商业模式的核心，因为它意味着杠杆不再是品牌知名度，而是代理在决定时刻恰好读到的任何内容。”

Pattanaik 强调，促成代理决策的因素往往小得惊人。

“因此，供应商接下来将要优化的东西（除了研究中承认的存储库上下文之外）是工具的支持文档和定价页面——这些将呈现给一个不进行略读、不被 Logo 吸引、并将保留脚注完全按字面理解的非人类读者。这是一种奇怪的新型 SEO，它会像旧的一样被游戏化，”Pattanaik 补充道。

> “供应商接下来将要优化的东西是工具的支持文档和定价页面——这些将呈现给一个不进行略读、不被 Logo 吸引、并将保留脚注完全按字面理解的非人类读者。”

这种分析对现实世界开发者的影响可能在未来几个月内成为茶余饭后的谈资。

## 这种对齐是一个日益增长的趋势

[MailChannels](https://www.mailchannels.com/) 的创始人 [Ken Simpson](https://www.linkedin.com/in/ksimpson/) ([ttul](https://news.ycombinator.com/user?id=ttul)) 在 [Hacker News](https://news.ycombinator.com/item?id=49557206) 上写道，他为自己的公司构建了这种分析。

“Armature 确实掌握了一些东西。你从分析代理在各种用例中会做出的选择开始，然后收集你可以做些什么（如果有的话）来开始让代理向你的产品倾斜，并远离竞争对手，”Simpson 写道。

值得指出的是，Armature 是一家非常年轻的公司（成立于 2026 年），所以这在该组织对此类分析的展示中尚属早期阶段。无论如何，在一个代理利用从公共代码库、开放数据存储库和整个网络中提取的分析来做出决策的世界里，我们可能真的需要把营销手册扔出窗外，重新开始。