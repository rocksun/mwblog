<!--
title: 生成式 AI 时代，为什么 JSON Schema 比以往任何时候都更重要
cover: https://cdn.thenewstack.io/media/2026/04/162228ed-stacey-knipe-lfhqhc_wq9e-unsplash-scaled.jpg
summary: 本文探讨了 JSON Schema 在生成式 AI 时代的关键作用。它通过为大模型的随机输出提供结构化验证，弥合了确定性系统与非确定性 AI 之间的鸿沟，已成为可靠 AI 集成的核心基础设施。
-->

本文探讨了 JSON Schema 在生成式 AI 时代的关键作用。它通过为大模型的随机输出提供结构化验证，弥合了确定性系统与非确定性 AI 之间的鸿沟，已成为可靠 AI 集成的核心基础设施。

> 译自：[Why JSON Schema matters more than ever in the age of generative AI](https://thenewstack.io/json-schema-ai-reliability/)
> 
> 作者：Charles Humble

#### 当企业在应对大型语言模型的不可预测性时，悄然普及的 JSON Schema 标准正脱颖而出，成为强化结构、对齐团队并将概率性输出转化为可靠、受契约约束系统的关键工具。

你很有可能已经在通过某些方式使用 [JSON Schema](https://json-schema.org)，只是你可能还没意识到。

它默默地支撑着 API 网关中的验证逻辑，存在于团队发布微服务的流水线中，也潜伏在开发人员不假思索安装的 IDE 插件里。大多数人遇到它时，都将其视为在进入“真正”工作前必须搞定的一个技术细节。但是，尽管你可能将其视为基础设施的管道工程，它的核心目标其实是验证结构化数据。

## 漫长而曲折的道路

这一标准有着悠久的历史。自 2007 年 Chris Zyp 首次提议将其作为一种声明式语言，用于注释和验证 JSON 文档的结构、约束及数据类型以来，该规范已经历了多个维护者和版本的更迭，在此过程中积累了各种观点和变通方法。它也变得相当复杂——其词汇表和组合器（如 *oneOf*、*anyOf* 和 *allOf*）代表了一个深不可测的“兔子洞”，常在错误的时机让工程师们感到意外。

开源 API 基金会 [**Naftiko**](https://naftiko.io) 的联合创始人兼首席社区官 (CCO) Kin Lane 告诉 *The New Stack*：“坦率地说，它有点乱。”

但尽管存在这种混乱，它已悄然成为 API 生态系统中几乎所有主要规范的基石。依赖 JSON Schema 来定义和验证自身结构的规范包括 [OpenAPI](https://spec.openapis.org) 和 [AsyncAPI](https://www.asyncapi.com/docs/concepts/asyncapi-document/define-payload)，以及 Anthropic 的 [模型上下文协议 (Model Context Protocol)](https://modelcontextprotocol.io/specification/2025-11-25/basic#json-schema-usage) 等新规范。同样，Google 新兴的 [A2A 规范](https://a2a-protocol.org/latest/specification/) 虽然依赖 Protobuf 而非 JSON Schema 作为权威来源，但也体现了类似的结构化需求。

更重要的是，随着 JSON Schema 所解决的问题——围绕结构化数据建立共享意义——始终存在，其采用率仍在持续增长。“它是目前最重要的规范，但也是最让人沮丧的规范，”Kin Lane 说道。

## 验证的实际作用

要理解为什么 JSON Schema 在当下比以往任何时候都重要，准确理解“验证”在实践中的含义会有所帮助。在[本系列的前一篇文章](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/)中，我们讨论了“统一语言”的重要性。

当你为（例如）邮政地址定义 JSON Schema 时，你是在发表一个机器和人类都能读懂的声明：这就是我们所说的“地址”。它是美国的地址还是其他地方的？它是否需要特定格式的邮政编码？它可以有第二行吗？一个构建良好的 Schema 回答了所有这些问题甚至更多，它将团队甚至整个组织的集体理解编码成网关、流水线或 IDE 可以自动执行的东西。

“它不仅仅是为了系统，”Kin Lane 解释道，“验证主要是为了人。如果你没有让人就这些标准达成一致——什么是地址、PII（个人身份信息）意味着什么、发票是什么样的——并且没有在注册表中将这些商定为 JSON Schema，它就无法发挥应有的影响力。”

> “如果你没有让人就这些标准达成一致……并且没有在注册表中将这些商定为 JSON Schema，它就无法发挥应有的影响力。”

Schema 文件本身就是共享词汇表。验证是执行机制。但目标是“对齐”（alignment），正如任何企业架构师所知，这是在大规模环境下最难实现、也最有价值的事情。

## 非确定性世界中的确定性

Kin Lane 认为，[生成式 AI](https://thenewstack.io/how-generative-ai-informs-platform-engineering-strategy/) 的非确定性使得 JSON Schema 比以往任何时候都更具相关性。

向 LLM 问两次同一个问题，你可能会得到两个截然不同的答案。这种概率行为使 AI 能够处理歧义、跨领域综合信息，并生成任何基于规则的系统都无法产生的创造性输出。

然而，企业通常更倾向于可预测性。因此，将 AI 集成到企业运营中的挑战在于架起确定性与非确定性之间的桥梁。JSON Schema 是划定这条界限的最佳工具之一。

“确定性与非确定性（即传统的 API 与 AI 函数）之间的平衡，将是未来世界分割的方式，”Kin Lane 说，“所以，如果你还没有对数据进行任何清理、结构化和类型定义工作，你就会处于劣势。”

> “确定性与非确定性（即传统的 API 与 AI 函数）之间的平衡，将是未来世界分割的方式……”

在我们的交谈中，Kin Lane 提到了“已知的已知”（可用事实）、“已知的未知”（我们意识到的信息差距）和“未知的未知”（不可预见的风险因素），这个词在 2002 年 Donald Rumsfeld 提及后进入了公众视野。

在 [AI 集成](https://thenewstack.io/the-data-engineers-guide-to-genai-and-ai-integration/)中，“已知的已知”是可验证、有类型且结构化的数据和输出。目标是尽可能多地将内容推向“已知的已知”类别，同时尽量减少代表真正不可预测性和风险的“未知的未知”。

Kin Lane 建议，JSON Schema 允许你将一段数据变成“已知的已知”。有了 Schema，数据就可以被验证、测试和模拟。如果它可以被模拟，它就构成了一个[契约](https://thenewstack.io/risk-mitigation-agentic-ai/)的基础，无论 AI 是如何生成结果的，你的 AI 驱动系统都可以为此负责。

“只要你能说，‘这是一个地址/医疗记录/发票’——并且它符合特定标准——你就真正为那 90% 的 AI 质量门槛完成了关键工作，”Kin Lane 说，“但这需要付出努力。你必须[清理数据](https://thenewstack.io/clean-data-trusted-model-ensure-good-data-hygiene-for-your-llms/)，拥有自己的数据管道和 Schema。”

## 注册表作为组织基础设施

在这个方向上取得最大进展的企业往往具有一个共同的结构特征。“拥有注册表，并配备倡导者、系统、网关、IDE 和使用它的流水线的组织，往往更成熟，在 AI 集成方面做得更好，”Kin Lane 观察到。

你可以把它想象成意义的“包管理器”。正如 NPM 为开发人员提供了一个共享的、版本化的代码依赖池，Schema 注册表为团队提供了一个共享的、版本化的数据定义池。这个类比可以进一步延伸：正如没有[依赖管理](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/)的代码往往容易脆弱和漂移，没有 Schema 治理的数据往往会导致不一致和隐藏的定义，从而悄悄破坏构建在其之上的系统。

Schema 应用最直接的地方，如 IDE、流水线和 API 网关，也是现代软件交付中杠杆率最高的地方。在开发过程中、在到达流水线或生产网关之前捕获 Schema 违规，其成本远低于在 AI 驱动的工作流处理了损坏的输入并产生了一个“一本正经胡说八道”的输出之后再去捕获它。

## JSON Structure：领域新秀

JSON Schema 并非没有竞争对手。一个名为 [JSON Structure](https://json-structure.org) 的新规范已经出现，旨在成为一个更简单的替代方案，没有 JSON Schema 积累的那些复杂性和毛刺。

该规范发布于 2025 年 7 月，由 Microsoft 的 Clemens Vasters 编写。它采取了截然不同的哲学：强调严格类型和确定性，而非 JSON Schema 那种更灵活、注释驱动的方法。

JSON Structure 目前仍是草案，没有正式的 IETF 地位，但 Kin Lane 对此持谨慎乐观态度。

“我希望它能取代 JSON Schema，后者有很多包袱和反对者，”他说，“但 JSON Structure 要挑战 15 年的普及沉淀，这绝非易事。”

因此，目前 JSON Schema 仍然是务实的选择。它无处不在，受所有主要工具链支持，并嵌入在每一个重要的规范中。

“不要试图使用它的全部，因为它非常复杂，”Kin Lane 说，“但它在稳定系统方面非常有用，因此它可以落地你的 AI 努力，帮助你和你的团队达成共识，朝着实现目标的正确方向前进。”

在当前的 AI 热潮中，人们很容易将注意力完全集中在新事物上：模型、智能体、编排框架、界面。JSON Schema 不属于这些。它是一个大多数人都不愿多想的 17 岁“高龄”规范。

但 Kin Lane 相信，未来几年能够最成功集成 AI 的企业，将是那些拥有最强大基础的企业，包括有类型的结构、共享的词汇表以及系统之间经过验证的契约。近二十年来，JSON Schema 一直在企业中默默地构建这些基础。