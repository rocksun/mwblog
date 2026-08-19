<!--
title: 一个可媲美Claude Managed Agents的开源替代方案正式发布
cover: https://cdn.thenewstack.io/media/2026/08/f085b1d4-stacey-knipe-scaled.jpg
summary: AI基础设施公司TrueFoundry推出了开源代理框架TrueForge，旨在替代Anthropic的Claude Managed Agents。该平台提供模型中立性，允许企业在自控基础设施上管理AI代理，通过优化模型调用和降低运维成本，减少对单一供应商的依赖。
-->

AI基础设施公司TrueFoundry推出了开源代理框架TrueForge，旨在替代Anthropic的Claude Managed Agents。该平台提供模型中立性，允许企业在自控基础设施上管理AI代理，通过优化模型调用和降低运维成本，减少对单一供应商的依赖。

> 译自：[An open source rival to Claude Managed Agents just launched](https://thenewstack.io/truefoundry-trueforge-claude-managed-agents/)
> 
> 作者：Adrian Bridgwater

AI基础设施平台公司 [TrueFoundry](https://90908956.streak-link.com/C_zjgFh2tnFZYzDI_gQtpMy5/https%3A%2F%2Fwww.truefoundry.com%2F) 发布了其开源代理框架 TrueForge。该技术直接被定位为 [Claude Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) 的替代方案，后者是 Anthropic 提供的托管基础设施服务，用于运行、沙箱化和编排自主的 Claude 代理。

TrueForge 承诺让软件工程师能够在任何模型（公司强调是“任何”模型）或 [MCP server](https://thenewstack.io/when-is-mcp-actually-worth-it/) 上构建、部署、[调试](https://thenewstack.io/5-steps-to-debug-development-and-operations-teams/) 和 [治理](https://thenewstack.io/five-pillars-ai-governance/) 生产级 AI 代理，同时将总代理运营成本预估降低 50%。

虽然来自中国前沿模型先行者 [Z.ai](https://z.ai) 的 [GLM-5.2](https://z.ai/blog/glm-5.2) 等开放模型正在以更低的成本 [挑战专有前沿模型](https://thenewstack.io/open-weight-models-frontier-costs/)，但大多数托管代理平台仍然将企业锁定在单一供应商的模型、基础设施和定价体系中。

## 挑战托管代理平台锁定这一普遍现象

曾任 Meta 机器学习技术负责人、现为 TrueFoundry 联合创始人兼首席执行官的 [Nikunj Bajaj](https://www.linkedin.com/in/nikunj-bajaj-10476824/) 告诉 *The New Stack*，这种普遍存在的托管代理平台锁定，正是他公司在模型供应商选择上采取中立态度的根本逻辑。

“一个以 50 美元向你兜售一百万 token 的供应商，完全没有动力告诉你同样的任务可以使用以每百万 token 50 美分收费的模型来完成，” Bajaj 说道。“传统上，一个供应商提供模型、构建代理并决定你的 token 用量、使用顺序、使用什么工具以及在托管代理供应商规定的治理下运行——而且他们把完全相同的配置卖给你的竞争对手。”

他坚持认为，从根本上说，这意味着“激励机制不匹配”，因此在托管代理部署场景中，由于总是存在权衡，“这个游戏中的玩家无法与裁判对话”。

“为什么构建强大的代理意味着要放弃对 AI 技术栈的控制权？我们为开发人员提供了托管代理体验，同时不强迫他们永久绑定在某一个供应商身上，” Bajaj 补充道。

> **“一个以 50 美元向你兜售一百万 token 的供应商，完全没有动力告诉你同样的任务可以使用以每百万 token 50 美分收费的模型来完成。激励机制不匹配，因此这个游戏中的玩家无法与裁判对话。”**

## 底层框架成为战略控制点

尽管 Claude Managed Agents 直到今年 4 月才 [作为 beta 版本发布](https://claude.com/blog/claude-managed-agents?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)，但 Bajaj 和他的团队认为他们可以追踪到这里正在形成的一条演进曲线。这条弧线预示着第一波 AI 代理存在于开发人员的笔记本电脑、编码工具和原型中。但下一波正转向以托管基础设施服务为代表的面向客户的产品，并具备使用共享工作流的能力。

至关重要的是，这种转变将这些产品底层的框架变成了一个战略控制点，在用户、模型及其交互的系统之间的操作循环中充当执行层。

“这确实是现实：框架是用户、LLM 和其他一切事物之间的关键层，” Bajaj 阐明道。“假设开发人员正在构建一个代理。他们使用自己的模型，但框架仍然决定何时调用 MCP server，何时使用他人已经构建好的代理，保留什么上下文，以及哪个模型处理计划的哪一部分。”

这意味着也存在安全隐患。Bajaj 指出，“某些操作”仍然需要在完全隔离的沙箱中运行，而且某些数据永远不应该发送到闭源模型中。

“所有的逻辑都驻留在框架中。如果软件工程师不使用一个（框架），那么开发团队就必须从零开始构建所有这些逻辑，”他补充道。

## 企业希望拥有核心代理层

在提供托管代理平台的开放式中立供应商方法中，组织必须管理每个代理的持久会话、工具凭据、执行沙箱、上下文、人工审批、调试、访问策略和支出。TrueFoundry 押注企业更希望拥有这一层，而不是从单一模型提供商那里继承它，同时还要以更低的成本构建企业治理功能。

TrueForge 通过 TrueFoundry 的 AI 网关路由每个模型调用和 MCP 交互，因此可以应用预算执行、速率限制和护栏，从而为企业提供受控且安全的托管代理体验。

## 当“foo”和“bar”掌舵时，就像无头苍蝇一样

Bajaj 表示，当组织没有掌控好方向盘时，他曾亲眼目睹过一些操作，其中 [“foo”和“bar”](https://en.wikipedia.org/wiki/Foobar)（计算机编程中用于尚未命名的已知元语法变量值的标准占位符名称，类似于 John Doe）最终成为了所有事情的执行者。

“系统中的每一个操作都来自一个通用的共享账户，而不是你可以真正识别的人。所以当某件事发生变化或被破坏时，你根本不知道该和谁谈。有一次，当我们从共享访问迁移到个人访问的过程中，一些密钥被轮换了。公司的一半人仍然在使用旧账户，系统就对公司的一半人瘫痪了，”他解释道。

团队可以在自己的基础设施上运行 TrueForge，使用自己的模型、MCP server 和 API 密钥，并将每个任务路由到符合该工作成本、延迟或质量需求的最优模型。但这是否意味着工作负载会因此变得过于碎片化？

“恰恰相反，工作负载变得更加统一，” Bajaj 热情地说。“大多数团队默认情况下已经在自带模型。所改变的是，组织可以定义模型、代理或 MCP 进入其注册表所需的条件。我称之为代理开发生命周期，即 ADLC。一旦你拥有了这一点，你就可以在所有事物上执行相同的操作原则。”

在实践中，TrueFoundry 团队确认，他们看到大多数以 AI 为中心的软件工程操作在典型任务上收敛于“大约十几个模型”，外加少数用于利基工作的专用模型。

## Anthropic 做错了吗？

TrueForge 随附支持 OpenAI、Anthropic 和其他 20 多个模型，以及 40 多个内置工具、沙箱执行、人工审批工作流、大上下文处理、生成式 UI 和由 Tavily 提供支持的网络搜索。但尽管提供了 Claude Managed Agents 的替代方案，Bajaj 还是费尽心思指出他并不把 Anthropic 看作某种被排斥的对象。

**“**这并不是关于 Anthropic 做错了什么，” Bajaj 确认道。“而是因为它并不拥有世界上所有的模型。Claude Managed Agents 只能从 Anthropic 提供的有限模型集中进行选择。在某些任务上，有些开源模型以极低的成本表现出色，或者对于该特定工作而言更有能力。一个开放的框架拥有更广泛的选择范围。”

## 当你拥有框架时，你可以剔除那些不适用的部分

他强调说，Anthropic 还必须为非常广泛的客户群构建一个框架；这一事实意味着其系统提示词必须考虑到各种指令、护栏和极端情况。

“其中许多元素可能与开发人员自己的用例无关，但它们仍然会进入每一次调用中，并增加成本和延迟。当你拥有框架时，你可以剔除那些不适用的部分，并使其极其专业化，”他补充道。

> “明确地说，我们将 Anthropic 支持为一流提供商，因为其模型非常棒。会有很多情况下我们的用户想要使用它们。重点是不应将这种选择局限于 Anthropic 一家。”

为了验证上述陈述，TrueFoundry 在 DevRev 公共 Enterprise-Bench 的总共 14 个一级和二级任务上测试了该声明。该公司表示，TrueForge “在相似准确度下成本降低了 50%”，因此节省的成本来自于使用了更少的 token，并且能够访问 Anthropic 集合之外更适合特定任务的模型。

“明确地说，我们将 Anthropic 支持为一流提供商，因为其模型非常棒。会有很多情况下我们的用户想要使用它们。重点是不应将这种选择局限于 Anthropic 一家，” Bajaj 总结道。

TrueFoundry 还为那些希望获得相同体验但无需自行管理基础设施的团队推出了托管的、按使用付费版本的 TrueForge。