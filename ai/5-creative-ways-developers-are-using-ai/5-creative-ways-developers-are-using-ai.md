
<!--
title: 开发者使用 AI 的 5 种创意方式
cover: https://cdn.thenewstack.io/media/2024/07/4b855ebb-bruce-mars-fwvmhua_wby-unsplash.jpg
-->

我们与开发人员进行了交流，了解他们对 AI 的创造性使用方式，包括 PR 审查、创建学习路径和生成数据模型。

> 译自 [5 Creative Ways Developers Are Using AI](https://thenewstack.io/5-creative-ways-developers-are-using-ai/)，作者 Jeff James。

随着 AI 在科技领域的广泛应用，以及随之而来的人工智能驱动的编码平台、工具和服务的数量不断增加，开发者们正在努力寻找最佳方式利用 AI 来帮助他们完成编程任务和目标，利用 AI 来提高效率，同时处理一些更繁重和耗时的编程任务。

为此，我与几位开发者进行了交谈，了解他们使用 AI 的一些创意方式。虽然许多人使用 [GitHub Copilot](https://github.com/features/copilot)、[Claude 3 Opus](https://www.anthropic.com/news/claude-3-family)、[Pieces for Developers](https://pieces.app/) 和 [Codeium](https://codeium.com/) 等工具来帮助生成代码和自动化任务，但开发者们一直在探索 AI 可以帮助他们提高效率的其他方式。

## 1. 代码测试和 PR 审查

“我知道有人使用 AI 来编写他们编写的代码的单元测试，”资深软件工程师兼 [Audiofeed](https://audiofeed.ai/) 联合创始人 Shane Thomas 说。“这为他们节省了大量时间，不必一遍又一遍地编写相同类型的测试。他们仍然需要验证结果，但他们似乎从中获得了良好的结果。”

虽然使用 AI 进行单元测试有其优势，但其他专家（如 [Tia](https://asktia.com/) 的技术主管 [Swizec Teller](https://www.linkedin.com/in/swizec/)）[建议谨慎](https://swizec.com/blog/why-you-shouldnt-use-ai-to-write-your-tests/)依赖 AI 进行测试。在 [X 上发布的笔记](https://x.com/Swizec/status/1793006221630533813) 中，Teller 建议开发者在某些情况下使用 AI 进行测试，例如使用 AI 生成大量“多样化的生产级输入”。

开发者们还使用 AI 来模拟代码审查，这可以帮助开发者为与人类同事的审查做好准备。“我知道有人使用 AI 作为其团队成员拉取请求审查的第一步，”Thomas 说。“他告诉我，他收到了其他工程师关于他的 PR 审查的全面性的评论……但他的许多笔记最初是由 AI 标记的。”

## 2. 学习路径

教育和学习是开发者将 AI 用于好处的另一个领域。

“[Bekah Hawrot Weigel](https://www.linkedin.com/in/bekah-hawrot-weigel/)，[OpenSauced](https://opensauced.pizza/) 的技术 AI 倡导者说：“我一直使用 ChatGPT 为我创建学习路径，以便我能够更深入地了解提示。我给了它关于我们每天应该做什么的指示，并要求它想出一个我们可以讨论的活动。”

## 3. 自动化重复性任务

开发者使用 AI 的另一种创意方式是自动化一些最繁重和耗时的开发任务，例如通过分析复杂的代码来帮助进行代码维护和跟踪难以捉摸的错误。在 [最近发表在 The New Stack 上的一篇文章](https://thenewstack.io/5-software-development-skills-ai-will-render-obsolete/) 中，[Tabnine](https://www.tabnine.com/) 的首席技术官兼联合创始人 [Eran Yahav](https://www.linkedin.com/in/eranyahav/) 建议 AI 将有助于消除一些枯燥乏味的工作。

Yahav 写道：“AI 编码工具自动化了如此多的任务，开发者可能会发现他们获得的一些技能将不再需要。但这没关系，因为许多技能都涉及开发者乐于放弃的枯燥乏味的工作。”

## 4. 面向程序员的 AI 驱动的搜索

虽然所有开发者都依赖搜索和 AI 工具来帮助他们解决代码问题，但有些人一直在使用新的 AI 驱动的工具来帮助找到人类专业知识。

Weigel 说：“我在这里有偏见，因为我在 OpenSauced 工作，但我们创建了一个名为 [StarSearch](https://app.opensauced.pizza/star-search) 的工具，它允许你通过索引各种形式的开发者活动（包括 git 历史记录）来找到开源领域的‘明星’。例如，你可以要求它帮助你找到既了解 Rust 又了解 Tailwind 的开发者。这是一个很好的例子，说明 AI 如何能够超越代码补全，并提供对开源的更深入见解，从而增强开发者发现和协作。”

## 5. 生成文档和数据模型

“[Pieces for Developers](https://pieces.app/) 的首席技术官兼创始工程师 [Mark Widman](https://www.linkedin.com/in/mark-widman/) 说：“我经常使用的一些非常棒的 [例子] 是 [使用 AI 来] 编写单元测试、文档，以及帮助进行数据模型和名称生成。”

The New Stack 撰稿人 Jon Udell 也撰写了有关使用人工智能改善文档的文章，并且详细介绍了他使用 Unblocked 等由 LLM 支持的工具来增强代码文档的创建和维护的经验。

“从头开始编写文档和从头开始编写代码一样罕见。您通常会更新、扩展或重构现有文档。”Udell 写道。“我的期望是，一个包含代码和文档的 LLM 支持的工具可以提供有力的帮助，而 Unblocked 做到了。”

## 注意事项与顾虑

虽然 Widman 总的来说（特别是 OpenAI API）乐于见到 OpenAI 取得的全部进展——特别是后者如何更贴合开发者工作流——但他警告说要让迄今为止所做工作变得更好，还有很多工作要做。“我相信，他们在数据隐私、额外操作系统支持[和减少大型]延迟成本等方面仍然有很长的路要走。”

我已经稍微涉及了人工智能供应商尚未在数据隐私方面进行的工作——请参见我上一篇专注于 AI 驱动的开发工具的文章中的“缺点和警告”部分——但在考虑将 AI 用于创意用途时，开发者还应关注其他问题。一种危险是对 AI 过度依赖以完成过多任务，这可能导致代码质量降低，而开发人员在没有 AI 帮助的情况下无法执行开发任务。

2023 年，GitClear 发表了一项研究，表明 AI 辅助开发对“代码质量施加了‘向下压力’”，对“可维护性造成了‘令人不安的趋势’”，并强调了“... 创作者在撰写后的两周内被还原或更新的 [代码] 行数百分比预计与 2021 年人工智能前基线相比，2024 年将翻一番。”

## 人工智能辅助编程：最好的还在后头吗？

尽管存在一些警告和潜在缺点，但技术的不可阻挡的进步意味着未来还将有更多的人工智能驱动的发展，程序员可以期待并根据自己的定制需求进行创造性改编。Rainstorm Technologies 所有者、经验丰富的软件开发人员克里斯蒂安·兰斯特伦指出了 GitHub Copilot Workspace 等即将推出的工具如何将开发人员的生产力提升到新的高度。“

它尚未向公众开放，但我对 Copilot Workspace 非常感兴趣，”兰斯特伦说。“我已被列入候补名单，我很高兴看到它将如何加速我的工作。”

Ranstrom 表示：“它尚未向公众开放，但对于 Co-pilot Workspace 我非常期待。“我在等待名单上，并很高兴看到它将如何加快我的速度。”

Widman 鼓励开发人员检查人工智能在软件开发以外的其他方式中的使用方式以获得灵感，然后针对开发人员对这些示例进行调整和应用。他还认为，由于人工智能研究人员和开发人员的开创性工作，将会出现更多富有创意的用例。 

“我坚守的最重要的事情之一就是，我们建立在巨人的肩膀上，因此看看目前有哪些可用并且应用于你的领域来帮助改善流程、节省时间[和]金钱以及更多惊人的事情，并没有什么坏处！”
