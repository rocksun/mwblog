<!--
title: “代码应当被重构，而非维护”：Codeplain 倡导规格驱动的开发理念
cover: https://cdn.thenewstack.io/media/2026/06/b5af3842-summertime-flag-sfrnzzjylck-unsplash-scaled.jpg
summary: 本文探讨了 Codeplain 提出的“规格驱动开发”理念，主张在 AI 时代，代码应作为可丢弃的产物，通过维护规格而非直接维护代码来构建软件。这一范式不仅减轻了认知负担，还通过 plain-forge 工具实现了自动化开发，旨在解决 AI 带来的“溯源债务”问题，重塑软件工程的效率与逻辑。
-->

本文探讨了 Codeplain 提出的“规格驱动开发”理念，主张在 AI 时代，代码应作为可丢弃的产物，通过维护规格而非直接维护代码来构建软件。这一范式不仅减轻了认知负担，还通过 plain-forge 工具实现了自动化开发，旨在解决 AI 带来的“溯源债务”问题，重塑软件工程的效率与逻辑。

> 译自：["Code should be regenerated, not maintained": Codeplain makes the case for spec-driven development](https://thenewstack.io/codeplain-spec-driven-regenerative-code/)
> 
> 作者：Paul Sawers

AI 生成代码的速度远超团队的审查能力。越来越多的开发者认为，答案并非追求更快的代码审查，而是完全用别的方式取代代码审查。

[Dušan Omerčević](https://www.linkedin.com/in/dusanomercevic/) 是 [Codeplain](https://www.codeplain.ai/) 的首席执行官兼联合创始人，该公司全力推崇[规格驱动开发](https://thenewstack.io/vibe-coding-spec-driven/)，将其作为构建和维护 AI 时代软件的基础。Codeplain 于 2025 年初在斯洛文尼亚卢布尔雅那成立，并于同年[九月低调发布](https://blog.codeplain.ai/p/beyond-vibe-coding)，主打“规格驱动、生产就绪的代码生成”。

其基础是 [Plain](https://plainlang.org/)，这是一种开源规格语言，使用结构化、人类可读的文档作为软件如何构建和运行的单一事实来源。其核心思想是：如果代码损坏或需要变更，你只需编辑规格，而非代码本身，Codeplain 会从头开始重新生成实现。

![一个用于 Trello 客户端应用的 Plain 规格（左）以及 Codeplain 由此生成的 Python 代码（右）。](https://cdn.thenewstack.io/media/2026/06/ef967213-codegif.gif)

*一个用于 Trello 客户端应用的 Plain 规格（左）以及 Codeplain 由此生成的 Python 代码（右）。*

如今，Omerčević 正在进一步推广这一理念。在接受 *The New Stack* 采访时，他认为随着 AI 生成的代码量剧增，瓶颈已从编写软件转向审查和维护软件——而审查那些编码意图而非实现细节的规格，所需的认知负荷远小于审查代码。

> “我们的论点是，代码不应被维护，而应被重新生成。应该审查的是规格，而你要维护的也是规格。”

为了推进这一使命，该公司正在推出一个名为 [plain-forge](https://github.com/Codeplain-ai/plain-forge) 的开源代理技能框架。它允许 Claude Code、Codex 和 OpenCode 等编码代理通过对话起草和维护 Plain 规格，从而有效地自动化了规格驱动开发中原本最耗费人力的一部分。

发布的同时，Codeplain 还宣布已获得 300 万美元融资，投资方包括 [GapMinder VC](https://gapminder.vc/) 和 [Silicon Gardens](https://www.silicongardens.com/)。

## **规格的乐趣：一种新的开发范式**

Codeplain 绝非唯一拥抱规格驱动开发的公司。早在 2025 年 7 月，[Amazon 就推出了 Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/)，这是一个使用从自然语言提示生成的结构化规格来引导开发的代理式 IDE。与此同时，GitHub 也[紧随其后发布了 Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)，这是一个旨在将规格转化为 AI 代理可直接操作的可执行制品的开源工具包。

然而，这一底层概念比上述两者出现得更早。[SpecLang](https://githubnext.com/projects/speclang/) 是 GitHub Next 的一个研究项目，始于 2023 年，旨在探索纯英文是否可以作为一种真正的编程媒介——由 AI 处理从人类意图到可运行代码的转换。

这种传承也直接关联到 Codeplain。[Johan Rosenkilde](https://www.linkedin.com/in/johan-rosenkilde/)（SpecLang 的创始人之一及 GitHub Copilot 团队的创始成员）[目前担任 Codeplain 的董事会成员](https://www.linkedin.com/posts/codeplain_codeplain-welcomes-dr-johan-sebastian-activity-7334949185768599552-bsKS/)，也是其最早的投资者之一。

尽管规格驱动开发势头强劲，但开发者似乎并不太愿意编写规格。通过用户测试，Omerčević 和他的团队发现，虽然开发者抵触编写规格，但他们通常很乐意阅读规格。事实证明，结构良好的规格比它最终生成的代码更容易审查和推理。

Plain-forge 是 Codeplain 对这种张力的回应。它不再要求开发者从零开始编写规格，而是让编码代理进行工作——研究问题、增量起草规格，并在人类看到之前针对 Codeplain 的渲染器进行验证。至关重要的是，它不会通过预先生成庞大的规格来增加流程负荷——这是 Omerčević 公开批评的一种方法。

“我们不会扔给开发者 200 行规格，我们是迭代完成的，”他说。

每一个小的规格都能生成可运行的软件，开发者可以立即检查并反馈，从而在不面对成品文档的情况下，逐个特性地建立对规格的熟悉感。

“通过增量添加规格，开发者正在与规格建立关系。”

“以这种方式，通过增量添加规格，开发者正在与规格建立关系，”Omerčević 说。“规格是事实来源，也是 AI 理解了开发者的反馈。”

## **浴火重生**

这一切的基础是一种根本信念：代码应被视为一次性的输出而非耐用的资产，而规格——而非生成的代码——才是团队应当保存和维护的东西。Omerčević 表示，他通过构建 Codeplain 的亲身经历得出了这一结论，但发现很难向那些职业身份完全建立在代码之上的开发者表达清楚。

这就是 [Chad Fowler](https://www.linkedin.com/in/fowlerchad/) 的 [*Phoenix Architecture*（凤凰架构）](https://aicoding.leaflet.pub/) 发挥作用的地方。Fowler 是一位资深工程师和 BlueYard Capital 的合伙人，他在过去六个月里为这种方法开发了一个更广泛的哲学框架。

他在去年 12 月该系列的第一篇文章[*《再生软件》*](https://aicoding.leaflet.pub/3majnyfydzs2y)中指出，AI 使得代码变得丰富且廉价，颠覆了过去几十年来关于软件系统中什么值得保存的假设，那些死守现有实现方式的团队正在比他们意识到的更快地制造技术债。

Omerčević 表示，这个框架为他提供了他一直在寻找但难以表达的词汇。

> “向普通开发者传达规格驱动开发真的很困难。”

“向普通开发者传达规格驱动开发真的很困难，”Omerčević 说。“Chad 真正做得好的是将故事落地于代码，他说唯一的区别在于这些代码不再是永久的——它是短暂的，并且总是可以从其他制品中重新生成。”

[凤凰](https://en.wikipedia.org/wiki/Phoenix_(mythology))（Phoenix）对初学者而言，是希腊神话中的一种生物——一种循环焚烧自己并从灰烬中重生的鸟。Fowler 的观点是，软件系统也应该设计成这样。

在 3 月的文章[*《对话即提交》*](https://aicoding.leaflet.pub/3mhxvpam4z22z)中，Fowler 认为，当开发者手动编辑 AI 生成的代码时，他们割断了某种重要的东西：代码为何存在以及哪些决策塑造了它的记录。输出变了，但变更背后的推理却丢失了。

随着时间的推移，这种失去上下文的积累就是 Fowler 所说的“*溯源债务*”（provenance debt）——他的观点是，大多数开发者整个职业生涯都在堆积这种债务，却一直没有给它命名。

> “如果我们不朝着最终捕获这些丰富且重要的信息迈进，我们在面对软件构建方式的这场创新浪潮时是不负责任的。”

“只是在技术上，如果不通过极端的官僚主义，就不可能捕捉到溯源信息，所以作为行业，我们在大多数情况下都决定这不值得尝试，”Fowler 向 *The New Stack* 解释道。“现在，工具在没有繁重流程的情况下开启了这种可能性。我的观点是，如果我们不朝着最终捕获这些丰富且重要的信息迈进，我们在面对软件构建方式的这场创新浪潮时是不负责任的。”

换句话说，规格及其背后的推理现在是值得保存的东西，而不是它们所生成的代码。

很难夸大这将带来的文化转变有多么显著——毕竟，开发者一直以代码为中心构建自己的身份。那么，你如何说服工程师，删除和重新生成代表着进步？

对于 Fowler 来说，有两种方式，每一种都反映了不同类型的说服：

“第一种是等待，因为他们会看到，随着时间的推移，旧的做事方式已经过时，他们需要进化或灭亡，”他说。“第二种，也是更积极的方式，是向他们展示，删除和重生成定义了一种新的严谨性，并且只有这种新工具才使之成为可能，并为其提供支持。”

在 Fowler 看来，Codeplain 代表了一种将这种严谨性融入实际产品的可靠尝试——尽管他小心翼翼地指出，这仅仅是仍在拼凑的巨大难题中的一小部分。

“我希望许多公司和开源开发者[参与构建]，”他说。“因为我认为这个缺失的层面可以有多种不同的形式。这里有大量的想象和创新空间。我不想局限于任何个人或团队对于它应该如何工作的假设。我认为越怪异越好。我们必须发明一套新的习语和工具。”

## **规格之上**

![Codeplain 创始人 Dusan Omercevic (CEO) 和 Predrag Radenkovic (CTO)](https://cdn.thenewstack.io/media/2026/06/217cfb17-codeplain-dusan-predrag-photo-1024x681.jpg)

*Codeplain 创始人 Predrag Radenkovic (CTO)* 和 *Dusan Omercevic (CEO)*

Omerčević 对构建和交付企业级软件并不陌生——他之前[创立了 Cleanshelf](https://techcrunch.com/2017/01/24/cleanshelf-teams-up-with-squrb-to-clean-your-saas-clock/)，这是一个 SaaS 管理平台，[他在 2021 年将其出售给 LeanIX](https://www.leanix.net/en/company/press/leanix-acquire-saas-management-provider-cleanshelf)，而 LeanIX 随后[被 SAP 收购](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/)。因此，Codeplain 是他的下一步行动——而且已经有客户将其投入使用。

[Incode](https://www.incode.com/) 是一家身份验证服务提供商，使用 Codeplain 来构建和维护与外部数据提供商的集成——这类工作涉及持续的 API 研究、快速变化的外部系统以及对意外中断的高度容忍。

正是最后一个问题——即“中断”——让 Omerčević 最为激动。因为规格编码的是意图而非实现细节，当外部 API 发生变更导致集成损坏时，Codeplain 往往可以通过从完全相同且未更改的规格中重新生成代码来修复它。规格没有坏，只有代码坏了。

“你甚至不需要调整规格，”Omerčević 说。“你只是从完全相同的规格中重新生成代码，因为通常情况下，某些小的变动会导致损坏，但规格不会。”

这种方法背后也有严谨的经济论点。Omerčević 表示，生成规格的编码代理所消耗的 token 比直接生成代码要少五到十倍——而且由于规格对代理的认知需求较低，它可以在相同的上下文窗口内处理更大、更复杂的问题。对于代码生成步骤本身，Codeplain 使用 Gemini Flash 等更快、更便宜的模型，而不是前沿模型，从而降低了成本。

Omerčević 给出的类比是 TypeScript 编译器：Claude 本可以直接从 TypeScript 生成 JavaScript，但当有专门的工具能更快、更便宜地完成这项工作时，为什么还要这样做呢？

“让专业工具去做它们真正擅长的事情，”他说。“让 Claude 去做它真正擅长的事情——那就是研究。”