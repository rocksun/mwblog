<!--
title: Kore发布Artemis：为可治理AI智能体打造的“登月计划”
cover: https://cdn.thenewstack.io/media/2025/05/0fd38168-rocket.jpg
summary: Kore发布Artemis平台，通过声明式语言ABL和“双脑”架构，将AI开发从零散的提示词链转向可治理的系统，支持智能体自动构建与优化，确保企业级AI的合规与可靠。
-->

Kore发布Artemis平台，通过声明式语言ABL和“双脑”架构，将AI开发从零散的提示词链转向可治理的系统，支持智能体自动构建与优化，确保企业级AI的合规与可靠。

> 译自：[Kore counts down to Artemis, its moonshot for governable AI agents](https://thenewstack.io/kore-artemis-agent-platform/)
> 
> 作者：Adrian Bridgwater

**Kore 希望将企业级智能体开发带离“提示词链”的荒原。** 这家智能体软件公司周四发布了 Artemis，即 Kore 智能体平台（Kore Agent Platform）的最新版本。这是一个集成了可视化与代码的环境，用于构建、治理和优化多智能体 AI 系统，其核心围绕声明式蓝图语言、双脑运行环境以及一个能根据纯语言目标编写智能体的机器架构师。

Artemis 被略显奇特地定义为[多引擎 NLP](https://www.kore.ai/whitepaper/multi-engine-nlp-guide)，它是一个多管齐下的 NLP 引擎，采用所谓的“基本意义”（将句子分解为语法、同义词和概念）、机器学习和知识图谱技术，形成一个大于各部分总和的服务。

Kore 将其描述为无代码/专业代码（no-code/pro-code，而非 [无代码/低代码](https://thenewstack.io/low-code-vs-no-code/)），使用该术语是为了表明其平台既允许开发人员使用传统编程语言，又提供了将 API 集成到最终多智能体 AI 系统中的关键网关连接。

## 什么是 Kore 的 AI 原生特性？

在这个每个软件供应商都不得不宣称拥有内在 AI 能力的时代（Kore 也没能免俗，使用了 .ai 公司域名后缀），该公司声称通过其注册商标“智能体蓝图语言”（Agent Blueprint Language，简称 ABL）证明了其在该领域的地位。

Kore 解释称，ABL 是一种编译型[声明式语言](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again/)，它规范了 AI 智能体、系统和工作流的定义、验证和治理方式。内置了六种编排模式（监督、委派、移交、扇出、升级和智能体间联邦），以便开发人员构建生产级多智能体系统。

Kore 产品负责人兼首席技术官 [Prasanna Arikala](https://www.linkedin.com/in/arikala/) 告诉 *The New Stack*，ABL 从一开始就是为了可移植性和治理而构建的。

“像 LangChain、LlamaIndex、Semantic Kernel 这样的提示词链框架，以及大多数团队最终采用的手写编排脚本都是指令式的：开发人员在代码中连接链条，往往只有在生产环境中 LLM 调用失败时，才会发现架构漂移、工具引用缺失或移交中断——ABL 反转了这种模式，”Prasanna Arikala 说道。

他解释说，开发人员（或设计师通过可视化编辑器）使用类型化的 DSL 编写包含智能体、工具、记忆、护栏、监督者和拓扑结构的声明式蓝图。

“我们的解析器和编译器会静态验证整个智能体图谱，在生成单个 token *之前* 就能发现契约不匹配、未解析的工具、未绑定的记忆插槽和不可达状态。这样做的好处是可移植性和治理，”他表示。

Kore 提供的另一项商标技术是 Arch，即组织的智能体架构师。它不是人（尽管其设计初衷是表现得像人类系统架构师），而是一个机器实体，致力于将业务目标翻译成生产就绪的 ABL。

它支持完整的智能体生命周期（即设计、构建、训练、扩展、监控，有时还包括停用），并奠定了底层的智能体拓扑结构，这意味着它能够利用真实的生产追踪数据不断优化智能体行为。

## 拥有“双脑”的智能体

除了 ABL 语言和 Arch 智能体架构师之外，Kore 还提供了其 AI 原生工具“三剑客”中的第三个组件：双脑架构。这是一种由两个认知引擎（结合了智能体推理和确定性流程）组成的架构，并行运行。这两个大脑通过共享记忆工作，由统一语言编写，并由单一运行环境治理。

首席技术官 Prasanna Arikala 进一步解释了其中的原理，他表示双脑架构在共享的类型化记忆层上耦合了两个执行引擎：一个是负责规划和即兴发挥的 LLM 驱动的“推理脑”，另一个是强制执行业务规则、事务、SLA 和合规步骤的脚本流智能体组成的“确定性脑”。

“这两个大脑永远不会在未经调解的情况下相互改写状态，”Prasanna Arikala 澄清道。“ABL 蓝图中的每个记忆插槽都声明了所有者、可见性和写入策略。推理智能体提出状态更改建议；确定性引擎通过事务存储提交更改；监督者根据蓝图中固有的优先级规则仲裁冲突——这意味着在硬约束上确定性逻辑获胜，在建议性插槽上推理获胜，而平局则转交给人工参与步骤，由蓝图请求人工干预。”

从更高的维度来看，Kore 平台独立于所使用的 AI 模型。这种“政教分离”的设计旨在保持 AI 系统的可预测性、可审计性和可扩展性，涵盖从实验性原型阶段到生产级运营的全过程。

> “这种架构的严谨性脱颖而出，”Keyur Parikh 说道。“编译型蓝图、独立确定性层中的治理，以及适用于每个智能体的统一语言，正是企业级 AI 一直缺失的设计选择。” —— Vanguard 的 Keyur Parikh。

## 智能体的架构严谨性

[Keyur Parikh](https://www.linkedin.com/in/keyur-parikh/) 是总部位于宾夕法尼亚州的金融服务公司 Vanguard 的工作场所技术战略与服务负责人。作为 Kore 的客户，Keyur Parikh 已经提前了解了 Kore Agent Platform。

“这种架构的严谨性脱颖而出，”Keyur Parikh 说道。“编译型蓝图、独立确定性层中的治理，以及适用于每个智能体的统一语言，正是企业级 AI 一直缺失的设计选择。”

Kore 首席执行官兼创始人 [Raj Koneru](https://www.linkedin.com/in/rajkonerufl/) 表示，他认为企业级 AI 正在进入第三波浪潮，治理、可观测性和信任将决定成败。

“Kore Agent Platform 映射了这一转变，向市场推出了 AI 原生架构，使企业能够自信地构建、管理和优化多智能体系统，”Raj Koneru 说道。“这种深度源于十年来在复杂、受监管的环境中交付 AI 体验的经验，在这些环境中，规模、合规性和可靠性是不可逾越的底线。”

## 这是 AI 在构建、治理和优化 AI

Raj Koneru 及其团队将这项技术定位为“AI 构建 AI”。这一断言源于 Arch 能够从纯语言目标生成生产就绪的智能体，用 ABL 编写它们，并在部署前进行验证。

这也是“AI 治理 AI”，即每个决策、路径和结果都由 AI 实时记录、追踪和分析。确定性约束和流程控制由平台本身强制执行，而不是留给智能体决定。

第三，它被称为“AI 优化 AI”。平台从生产信号中学习，并将具体的改进方案推荐为可审查的优化建议，且内置了人工监督机制。

## CIO、CISO 和 CFO 应该如何看待

Kore 再次运用“三位一体”的力量，针对 Artemis 的发布向 CIO、CISO 和 CFO 传达了信息。

对于 CIO 来说，这是一个可管理性的信息——该平台将零散的第三方和自研智能体整合到一个统一的基础上。对于 CISO 来说，AI 行为变得可预测——治理在平台层强制执行，不受模型控制。

智能体的每一个动作和策略决策都会被记录并打上时间戳，且可追溯到特定的监管控制项。

第三，对于 CFO，该公司建议 AI 投资具有复利效应——Arch、ABL 和运行环境是所有智能体共享的基础设施，因此第 N 个智能体的边际成本将趋近于编写其蓝图的成本。

## Microsoft Azure 兼容性

Artemis 版本的 Kore 平台最初在 Microsoft Azure 上推出，并承诺随后将实现“更广泛的云可用性”。对于采用微软技术栈标准的企业，Kore 平台可与 Microsoft Foundry、Microsoft Agent 365、Entra ID 和 Microsoft Graph API 集成。它还通过 Azure Bot Framework 支持原生的 Microsoft Teams 频道。

客户可以部署在公有云、主权地区、私有云或本地，并支持按地区进行数据留存。