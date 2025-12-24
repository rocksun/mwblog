<!--
title: AI智能体：为何必须拥有“自我”，而非复制你？
cover: https://cdn.thenewstack.io/media/2025/12/f00a5558-agents-identity-2.jpg
summary: AI代理不应绑定人类身份，自动化验证局限。AuthZed提供授权，但代理管理与安全仍需沙盒隔离及人工监督，以防恶意行为。
-->

AI代理不应绑定人类身份，自动化验证局限。AuthZed提供授权，但代理管理与安全仍需沙盒隔离及人工监督，以防恶意行为。

> 译自：[Why AI Agents Need Their Own Identity, Not Yours](https://thenewstack.io/why-ai-agents-need-their-own-identity-not-yours/)
> 
> 作者：Alex Williams

AI原生初创公司无疑是为非人类群体服务的。

AuthZed 首席执行官 [Jake Moshenko](https://www.linkedin.com/in/jake-moshenko/) 表示，AI 代理无法真正拥有人类身份。在考虑 AuthZed 如何与 OpenAI 合作以及 OpenAI 部署的生产级 [检索增强生成 (RAG)](https://thenewstack.io/how-rag-architecture-overcomes-llm-limitations/) 授权模型时，这一前提就显现出来了。

“人们普遍误解你想要将一个代理部署为‘我’，”Moshenko 说。“人们希望从代理中获取的许多价值都是作为公司一部分运行的自主流程。”

## 将AI代理与人类身份绑定所带来的问题

还记得过去，当服务共享已离职人员的身份时所造成的混乱吗？

“如果用户离开公司或改变角色，你不会希望这会自动限制他们部署过的每一个代理，”Moshenko 说。“这就像做出招聘决定一样——如果我更换了经理，这并不意味着我希望所有为该经理工作的员工都离开。”

但是，假设代理确实绑定到了一个人。

Moshenko 说：“我部署一个代理来帮助进行一些代码审查，并不意味着我希望该代理能够从[人力资源]或筹资的角度做像 Jake 那样的事情。”

AuthZed 的权限模型将代理视为主体类型。它允许组织像管理人类一样，为代理联邦化访问权限。但仍然存在差距。

“仅仅因为你可以看到它正在读取敏感财务数据并可能回写一些数字，这本身并不能作为验证模型来说明代理正在做正确的事情，”他说。“如果我聘请一位会计师，我会向他们开放账簿——他们必须这样做才能完成工作。但这并不意味着他们不会对账簿做一些不正确或恶意的事情。”

Moshenko 表示，云原生工具提供了授权，通过权限边界控制代理可以访问的内容。云原生工具也提供了可观测性，跟踪代理采取了哪些行动。但验证呢？你无法自动确定它是否做出了正确的决策。

## 自动化AI代理验证的局限性

但即使使用确定性工具也未必能使其变得容易。总会有人为和非人为因素。使用安全扫描、代码检查和其他工具进行的自动化代理测试可能会失效。

Moshenko 说：“足够聪明的黑客可以把完全无害的东西伪装成非常恶毒的样子。”“足够恶毒的人和/或人工智能肯定可以通过你所有的代码检查测试、单元测试和集成测试，但仍然在做它们不该做的事情。”

他引用了图灵奖获得者 [Ken Thompson](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/) 的“[信任的信任](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf)”一文。该论文详细阐述了如果编译器本身已被攻破，你便无法信任它。编译器可能会注入漏洞，这些漏洞在编译编译器自身时会重新注入，从而通过传统测试几乎无法检测到。

“真的，这就像雇佣一个人：一切都变成了‘信任但需验证’，”Moshenko 说。“我们会在循环中进行人工代码审查，因为当恶意活动必须经过两个人而非一个人时，这会降低我们面临恶意活动的风险。”

## 规模化生产：OpenAI 与 AuthZed 的案例研究

AuthZed 指出，它有能力[为 OpenAI 提供](https://authzed.com/customers/openai)领先的大型语言模型 (LLM) 提供商正在使用的 RAG 授权能力。AuthZed 与 OpenAI 合作开发了其 ChatGPT Enterprise Connector，该连接器展示了其授权技术的用例，该技术基于 Google [关于其全球授权系统 Zanzibar 的论文](https://authzed.com/zanzibar)。

“他们确保任何询问第四季度收益的人确实有权访问 Google Drive 上存在的源文档，”Moshenko 说。“他们不会注入任何用户无法自行挖掘出来的上下文。”

AuthZed 允许 OpenAI 摄取企业数据。接下来发生的事情是关键。授权数据与文档相关联。届时，在将文档片段输入 LLM 的上下文窗口之前，他们会用 AuthZed 验证权限。更好的是，无需检查上游来源。而且数字也很可观。截至今年秋季，AuthZed 已处理了 370 亿份文档。

与云原生工具的差异是显著的。传统系统授权 API。AuthZed 根据用户权限对哪些文档进入 LLM 上下文进行后过滤。

AuthZed 提供了身份验证，但如果没有更深入的验证方法，代理行为的验证仍然无法完全解决。

[Jentic](https://jentic.com/) 的前提是，AI 工作负载的基础设施有点像 1996 年的情景。他们连接不同的系统，与企业架构师合作，这些架构师正在解开并填补他们的技术债务中的空白。

Jentic 首席技术官兼联合创始人 [Michael Cordner](https://www.linkedin.com/in/michaelcordner/) 在 [AWS re:Invent](https://reinvent.awsevents.com/on-demand) 接受 The New Stack 采访时说：“我认为，即使所有 LLM 开发明天停止，我们可能也需要再花五年或十年才能弄清楚到底该做什么，最佳实践是什么，以及与之相关的各种流程、方法和工作方式。”

Jentic 的联合创始人兼首席运营官 [Dorothy Creavan](https://www.linkedin.com/in/dorothycreaven/) 在接受 The New Stack 采访时也表示，这有点像新技术开始被采用的旧时代，但现在还没有将 API 世界与 AI 工作连接起来的蓝图。你必须拥有机器可读的 API 文档才能使其有用。然后你才能创建这些可以真正依赖的确定性工作流。

Cordner 说：“我们平台的一部分将所有身份验证集中在一个地方……集中式身份验证并能够观察代理正在做什么。” 在很多情况下，代理“正在开发，有点像影子 IT 组织。”

## Intuit 的 GenOS 平台如何加速 AI 采用

在亚特兰大举行的 [KubeCon + CloudNativeCon 北美大会](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/)上，[Intuit 的服务网格团队展示了其专有的 GenOS](https://medium.com/intuit-engineering/intuits-custom-llm-leaderboard-optimizing-model-selection-for-financial-use-cases-ac08d467f8f3)，以加速 AI 在其产品中的采用。这是一个内部平台，内置了代理和工具注册表、追踪、内存管理和评估功能。

Intuit 展示了值班调试代理如何访问日志、指标、变更日志和 Envoy 响应标志，然后使用 RAG 与内部文档、根本原因分析和架构审查进行匹配。

Intuit 拥有超过 350 个 Kubernetes 集群，2,000 次发布和部署，每天 1600 万次交易，以及每秒 292,000 次峰值交易。在如此大的规模下进行调试，至少可以说，极具挑战性。

Intuit 的资深软件工程师 [Kartikeya Pharasi](https://www.linkedin.com/in/kartikeyapharasi/) 说：“在这样的规模下工作意味着你通过所有相互连接的服务（如日志、指标和追踪）生成了大量的数据。”“在发生事故的情况下，你可能会花大量时间提出复杂的查询，或者在高压情况下即时查阅文档。”

Pharasi 表示，正确的工具选择变得至关重要。它几乎比工具本身更重要，“因为比无法进行这种调试更危险的是，如果你选择了错误的工具，并且执行了错误的步骤。”

## 为什么AI代理需要机器专用接口

显而易见？机器需要与人类不同的接口。在 AWS re:Invent 上，我采访了参与 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 生成式 AI 创业计划的公司，一次又一次地看到了这一点。

Cordner 表示，Jentic 认为代理是运行在 API 上的软件的未来。问题在于：AI 工作负载、不适用的基础设施和未针对机器优化的 API 之间存在不匹配。

“想象一下这样一个世界：你的所有 API 层都文档完善，人工智能能够轻松地将你的业务流程转化为确定性工作流，”Creavan 说，“这就是未来。”

当你考虑到确定性系统中的语言障碍以及它是如何被打破，并且在某些方面，使得描述能够更好地定义它们在组织中的目的时，你就会看到格局正在发生变化。

Intuit 的软件工程师 [Ryan Tay](https://www.linkedin.com/in/ryan-tay-8578991a9/) 说：“如果你考虑编写一个撤销支付交易的函数，你可能会将该函数命名为 `reverse_transaction` 或 `revert_record`。”“但是用户，以及类似地，LLM 不会认为那是撤销交易，对吗？他们会称之为退款之类的东西。”

这更多地与机器所需的可读性有关。例如，另一个创业公司 [LlamaIndex](https://www.llamaindex.ai/)，和 Jentic 一样，都参与了 AWS 生成式 AI 项目，它表示将文档转换为使用 RAG 的 token，从而加深了代理的上下文。

Liu 说：“总体的推理能力一直在提高，但核心只是更专业的上下文。如果代理能够非常准确地理解所有这些内容，那么它们就能突然做出决策。”

Intuit 还在研究 [模型上下文协议 (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/)，以便在团队之间共享。

Tay 说：“我们目前正在关注其他团队，他们试图构建一个完整的事件响应代理，该代理可以调用我们的工具以及其他特定于平台的工具。”“模型上下文协议……允许代理与你定义的工具以及其他团队甚至其他组织定义的工具进行通信。”

缺失的部分：代理特定的授权——AuthZed 正在解决，但 Intuit 尚未实施。

## AI代理管理与安全的未来

2025 年，随着企业争相采用 AI，AI 工作负载基础设施的困惑更加凸显。技术债务以以人为中心的 API 的形式依然存在。这种情况将在明年发生变化，届时团队将着手构建评估框架、代理身份模型以及开发沙盒环境等举措。

代理管理将采取不同的形式。Weights & Biases 的产品设计负责人 [Adam Draper](https://www.linkedin.com/in/adamwdraper/) 谈到通过将代理分解成更小的代理来管理它们，而他的同事，W&B 的机器学习工程师 [Ayush Thakur](http://Ayush%20Thakur) 则表示，一些公司可能会采取不同的方法。

Thakur 说：“一些大型实验室希望拥有一个具备代码执行、文件系统工具等基本工具的代理……LLM 在编写代码方面非常强大。一个代理的方法允许代理访问所有数据库和系统，并编写在沙盒中执行的代码片段。”

清晰度很重要。Draper 说：“你让这些提示越清晰简洁，你创建的代理就越能按你希望的方式运作。”

沙盒隔离变得至关重要。Thakur 表示，他从未见过代理被授予根访问权限。他说，一些公司将所有沙盒容器化，这样代理就可以在该沙盒中执行操作，然后在不再需要时将其终止。

然而，Moshenko 表示，无论采用何种方法，验证都存在根本性限制。

他说：“足够聪明的黑客可以把完全无害的东西伪装成非常恶毒的样子。足够恶毒的人和/或人工智能肯定可以通过你所有的代码检查测试、单元测试和集成测试，但仍然在做它们不该做的事情。”

这再次说明，人类的监督是必不可少的。

Moshenko 说：“真的，这就像雇佣一个人：一切都变成了‘信任但需验证’。”“我们会在循环中进行人工代码审查，因为当恶意活动必须经过两个人而非一个人时，这会降低我们面临恶意活动的风险。”