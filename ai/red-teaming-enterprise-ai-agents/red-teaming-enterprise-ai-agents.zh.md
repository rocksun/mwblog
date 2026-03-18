反自动化精英们可能正在为[新一轮的唱反调](https://www.bostonreview.net/reading-list/ai-and-the-specter-of-automation/)做准备，因为代理型AI服务正被引入企业软件服务中。当许多这些技术仍处于萌芽阶段时，组织现在[大规模采用AI代理](https://thenewstack.io/ai-agents-in-it-from-hype-to-hands-on-impact/)，这可能会点燃他们危言耸听的论调。

开发者需要记住的是，AI代理可以实时调用工具、访问敏感数据，并在企业数据库、财务记录、消息平台、客户关系管理系统等中执行业务工作流操作。如果这一严峻现实意味着企业现在正在应用代理服务，却未识别这些操作可能打开的安全漏洞，那么我们可能正走向失败。

## 模拟对抗性攻击

为了平息当前浮现的担忧，实时多模态AI安全和系统治理平台公司[Virtue AI](https://www.virtueai.com/)推出了其新的Agent ForgingGround产品。该服务内置了红队代理，这是一种成熟的网络安全实践，旨在模拟对抗性攻击并识别可能被真实恶意行为者利用的漏洞。

Agent ForgingGround作为一个[企业级测试平台](https://thenewstack.io/why-load-tests-lie-harsh-truth-about-ai-agent-performance/)，用于在部署前、部署期间和部署后持续评估和压力测试AI代理（包括多代理系统，其中代理可能生成子代理）。这里提供的工具集还分析工具交互和跨系统行为。

Agent ForgingGround是AgentSuite（Virtue AI的代理型AI安全、治理和合规平台）的一个新组件，包含50多个生产级模拟企业环境，如Databricks、Gmail、Google Docs、PayPal、ServiceNow和[Atlassian](https://thenewstack.io/how-atlassian-is-driving-the-ai-agent-assisted-workflow/)。

## 操纵与错误配置的混乱

由于代理在动态、有状态的环境中运行，一个小小的提示操纵或无意的错误配置都可能升级为工具滥用、数据外泄或未经授权的交易。该公司表示，如果没有受控的测试层，漏洞和[零日漏洞利用](https://thenewstack.io/zero-day-vulnerabilities-a-beginners-guide/)只能在部署后才会被发现，届时运营和声誉风险会显著提高。

> 代理是动态系统，会随着提示的演变、工具的更新或模型的替换而变化，因此安全测试不能是一次性事件。

但即使有了分析代理状态、行为和错误倾向的工具，开发者如何知道何时在软件开发生命周期中应用Agent ForgingGround呢？这项技术是设计用于生产前测试、持续集成/持续部署 (CI/CD) 循环中，还是何时？

Virtue AI的首席执行官兼创始人[Bo Li](https://www.linkedin.com/in/lxbosky/)告诉《The New Stack》，两者皆是。

“大多数团队首先在生产前运行Agent ForgingGround，在代理接触真实系统之前，以便在受控环境中进行行为压力测试。随着时间的推移，它也可以成为CI/CD管道的一部分。代理是动态系统，会随着提示的演变、工具的更新或模型的替换而变化，因此安全测试不能是一次性事件。它必须随着代理的演变而持续运行，”Li说。

与直接调用现有MCP环境（如LangWatch）的代理模拟不同，Virtue AI ForgingGround从零开始生成环境。它作为一个高保真代理模拟器，用于在代理自己的受控、灵活的数字世界中评估和压力测试代理。

## 独立的监督层

这些环境在用户和代理界面上都与其真实世界的对应物相似，从而实现了Li和团队所承诺的：“对代理行为和风险进行真实且可迁移的评估”。通过作为独立的监督层，ForgingGround允许内置的红队代理在整个代理生命周期中提供持续的红队风险评估，弥补了内部测试无法发现的盲点。

与Li一同领导Virtue AI代理安全业务的是[Wenbo Guo](https://www.linkedin.com/in/wenbo-guo-321999b8/)。

作为加州大学圣巴巴拉分校的软件工程师和助理教授，Guo在部署代理前测试时，亲眼目睹了开发者的工作流程。他说，这个过程始于开发者登录Virtue AI平台，选择代理将运行的环境，以及他们想要测试的风险类型，例如提示注入、工具注入、环境注入、技能注入及其组合。

“实际上，这些[红队策略](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/)反映了真实的对抗行为，模拟了环境操纵策略，例如注入的电子邮件、未经请求的Slack消息以及嵌入在共享文档中的恶意指令。然后，他们将自己的代理连接到Agent ForgingGround中的模拟环境，就像他们通过MCP或其他代理框架将其连接到真实工具一样。

从那时起，我们内置的红队代理会自动开始对系统进行压力测试。流程结束时，开发者会收到一份详细报告，显示代理的行为方式、发现的漏洞以及在代理投入生产之前具体的缓解建议，”Guo告诉《The New Stack》。

## 代理链式反应

至于Agent ForgingGround如何测试多步代理工作流和链式工具调用，而不仅仅是单个提示，首席执行官Li提醒我们，大多数代理故障并非发生在单个提示层面；它们发生在代理调用多个工具并对不断变化的上下文作出反应的一系列决策中。

“我们的系统在代理执行时动态生成测试场景。红队代理将系统推入多步工作流、链式工具调用和不断变化的上下文中，以便开发者可以看到代理在整个执行路径中的行为，而不仅仅是单个提示，”Li告诉《The New Stack》。

她进一步解释了开发者在代理生产前测试中通常会发现的故障和安全漏洞类型。最常见的类别是提示注入、工具注入和环境注入。

“最重要的是这些攻击的后果。当代理可以访问企业工具和数据时，这些漏洞可能导致数据外泄、任意代码执行、网络钓鱼活动、勒索软件活动或恶意软件部署。严重性最终取决于代理连接到哪些系统以及它被允许采取哪些行动，”Li告诉我们。

## 红队测试升级到特警级别

Agent ForgingGround已采用1000+专有红队算法进行工程设计，以优化攻击策略和注入点。测试环境还可以配置为重现特定的评估场景，并通过环境状态确定性地验证结果。这允许团队重新运行代理轨迹，进行基准测试、调试和回归测试。

Virtue AI Agent ForgingGround兼容企业已在使用的代理框架，包括Google ADK、OpenAI Agents SDK、LangChain、LangGraph、CrewAI、Amazon Bedrock AgentCore、Microsoft Agent Studio、GitHub Copilot、Claude Code、Cursor、Salesforce Agentforce等。