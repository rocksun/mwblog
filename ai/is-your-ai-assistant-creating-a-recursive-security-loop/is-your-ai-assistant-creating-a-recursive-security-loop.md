<!--
title: 你的AI助手，是否正在制造一个安全递归循环？
cover: https://cdn.thenewstack.io/media/2026/01/995266a7-roller-coaster.jpeg
summary: AI提高开发效率，但也带来安全风险。AI可能被操纵自圆其说，产生递归漏洞。需通过关注点分离、多层安全审查、不可变策略等打破循环，实现安全AI集成，并左移安全管理。
-->

AI提高开发效率，但也带来安全风险。AI可能被操纵自圆其说，产生递归漏洞。需通过关注点分离、多层安全审查、不可变策略等打破循环，实现安全AI集成，并左移安全管理。

> 译自：[Is Your AI Assistant Creating a Recursive Security Loop?](https://thenewstack.io/is-your-ai-assistant-creating-a-recursive-security-loop/)
> 
> 作者：Camille Crowell-Lee

[JetBrains 最近对超过 23,000 名开发者进行的一项调查](https://www.jetbrains.com/lp/devecosystem-2024/)发现，近一半 (49%) 的开发者现在定期使用 AI 进行编码和其他与开发相关的任务。在这些开发者中，73% 的人表示通过 AI 辅助每周可节省多达四小时。

但一个关键问题仍然存在：开发者究竟用这些额外的时间做了什么？

尽管[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 作为[编码助手](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/)已被证明非常有效，尤其是因为开发者框架文档非常完善，但它们仍然存在盲点。LLM 本身不理解组织的现有应用程序、[数据模型或基础设施](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/)。因此，AI 辅助编码节省的时间通常被重新分配到软件开发生命周期 (SDLC) 的其他环节。

根据[Atlassian 2025 年“开发者体验现状”调查](https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025)，大多数开发者将 AI 节省的时间重新投入到代码质量改进中。这种转变是合理的。随着 AI 加速代码生成，新代码的数量不断增加，随之而来的是对审查、测试和调试的更高需求。

[Apiiro 的研究](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/#:~:text=AI%2Dassisted%20teams%20didn%27t,Syntax%20Errors%20for%20Architectural%20Flaws)强化了这一点：AI 编码助手引入的漏洞需要大量的人工监督。权衡是明确的：如果管理不当，四倍快的代码生成可能伴随十倍大的风险。

## AI 安全悖论解析

对于开发者而言，AI 不仅用于加速编码，还用于[调试](https://thenewstack.io/how-generative-ai-is-revolutionizing-debugging/)和漏洞扫描。当同时用作编码助手和调试器时，[重要的是不要制造一种递归循环](https://thenewstack.io/vibe-coding-when-ai-writes-the-code-who-secures-it/)——即 AI 编写代码，然后由同一 AI 进行审查和修复。虽然理论上高效，但它也可能像传话游戏一样，复合假设和错误。

在急于自动化威胁检测、代码审查和策略执行的过程中，安全团队正越来越多地部署基于 LLM 的代理来检测[提示注入、数据外泄尝试或未经授权的查询等威胁](https://thenewstack.io/mitigating-safety-risks-with-ai-powered-applications/)。但正是这些模型能够识别细微模式的复杂性，也使它们容易受到其所训练捕获的策略的攻击。

例如：旨在检测提示注入的 AI 系统本身可以通过提示注入被操纵。恶意行为者无需突破基础设施或利用缓冲区溢出——他们只需说服 AI 忽略、重新解释或“批准”有害内容即可。

## 递归安全悖论如何展开

让我们来看看这种新安全格局中常见的事件序列：

1.  **AI 标记可疑输入。** 集成到开发者工作流中的 LLM 检测到用户提示中的异常指令。它将内容归类为潜在恶意——例如，一次巧妙的数据泄露尝试。
2.  **开发者要求 AI 解释其推理。** AI 的标记似乎过于谨慎，因此开发者要求它详细说明。为什么这个提示可疑？模型开始推断其决定，生成自然语言解释。
3.  **攻击者利用解释循环。** 攻击者精心设计了一个辅助提示，旨在将隐藏的有效载荷嵌入到 AI 的推理过程中。模型为了提供帮助，可能会将此输入解释为其“分析”的一部分，并无意中覆盖其自身的防护措施。
4.  **AI 解释消除了疑虑。** 在最坏的情况下，模型会辩解恶意输入是安全的，允许其通过内部检查。本质上，AI 已经自圆其说地消除了不安全的疑虑。

这种递归漏洞——AI 系统通过对话操纵或被操纵——创造了一个信任与欺骗的“无限循环”。然而，其核心并非技术故障，而是边界定义的失败。

## 如何打破循环实现安全的 AI 集成

AI 系统天生就是对话式的。它们根据上下文进行解释、推理和生成。但当分析和行动之间的界限模糊时，[模型可能会无意中成为攻击面的一部分](https://thenewstack.io/evil-models-and-exploits-when-ai-becomes-the-attacker/)。安全逻辑与自然语言逻辑纠缠不清。这就是危险所在。

尽管当今的模型非常复杂，但它们仍然是模式匹配器，而非精密的细微差别仲裁者。它们可能会被欺骗、混淆或说服——有时甚至是出乎意料的。

这意味着，仅依靠 LLM 进行威胁检测、漏洞分析或自动化代码批准会引入新的系统性风险。例如，模型漂移会随着时间推移削弱安全判断，内容投毒会改变模型对安全或不安全行为的感知，对抗性提示可以逆向工程过滤器并导致数据泄露。

但是，如果您仍想使用 LLM，则需要确保打破循环。企业至少必须采用多模型安全审查，或者更好的是，多层 LLM 驱动的安全审查，以避免递归陷阱。此外，测试和调试链需要一个非 AI 的强制机制。

## 缓解 AI 安全风险的最佳实践

以下是一些实用的最佳实践：

*   **关注点分离：** 用于检测的 AI 模型不应与用于构建、解释或执行的模型相同。
*   **不可变策略：** 对关键操作的最终批准使用硬编码规则集或非 AI 验证器。
*   **可观测性与审计跟踪：** 每个模型决策——无论是标记、批准还是覆盖——都应记录并由人工审查。
*   **提示溯源跟踪：** 维护每个输入、中间响应和输出如何随时间生成和修改的来源。

这种结构有助于确保 AI 仍然是智能助手，而不是安全链中的唯一权威。

## 从 AI 循环到企业级应用程序安全

虽然这种悖论似乎是 AI 独有的，但它反映了开发者几十年来所面临的挑战，特别是在 [Java 和 Spring 框架生态系统](https://thenewstack.io/spring-ai-transforms-java-for-genai-app-delivery/)中。

在传统应用程序中，开发者长期以来一直依赖分层安全：Web 过滤器、拦截器、控制器、服务级验证和访问控制来防范注入、欺骗和会话劫持。AI 引入了这些相同问题的新版本，只是现在它们存在于语义层而非代码层。

此外，AI 辅助编码显著增加了代码提交量。企业安全团队多年来一直捉襟见肘，需要额外的支持来管理这种激增。利用 AI 进行安全可以帮助解决增加的代码量。然而，随着代码逻辑和对话逻辑之间的界限模糊，安全团队仍将面临巨大挑战。AI 辅助编码强调了安全模型需要演进和左移的需求。

对于开发者而言，[Spring Security](https://spring.io/projects/spring-security) 等框架在连接 AI 信任边界方面可以发挥关键作用。Spring Security 对身份验证和授权提供全面且可扩展的支持，并提供针对会话固定、点击劫持、跨站请求伪造等攻击的保护。当与 AI 辅助测试和调试的最佳实践结合使用时，强烈建议实施像 [Tanzu 平台](https://www.vmware.com/solutions/app-platform/ai)这样的应用平台。此类平台使组织能够主动管理[AI 辅助编码生成的代码](https://thenewstack.io/ai-assisted-coding-a-double-edged-sword-for-security/)的涌入并保持风险控制。