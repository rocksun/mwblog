<!--
title: JetBrains命名AI代理“影子技术债务”
cover: https://cdn.thenewstack.io/media/2026/03/2e36e3d1-gustopo-galang-0aujxtqes9i-unsplash-1.jpg
summary: JetBrains提出AI代理导致“影子技术债务”。为解决此问题，公司推出Junie CLI和JetBrains Air，旨在通过代码库智能和中立平台提升大规模代理编程的代码质量与协调。
-->

JetBrains提出AI代理导致“影子技术债务”。为解决此问题，公司推出Junie CLI和JetBrains Air，旨在通过代码库智能和中立平台提升大规模代理编程的代码质量与协调。

> 译自：[JetBrains names the debt AI agents leave behind](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)
> 
> 作者：Darryl K. Taft

开发者们多年来一直在与[技术债务](https://thenewstack.io/technical-debt-vs-architecture-debt-dont-confuse-them/)作斗争。现在，一种新的变体正在代码库中积累，许多团队甚至还没有意识到这种堆积。

[JetBrains](https://www.jetbrains.com/)将其称为影子技术债务——由AI代理生成的低质量、缺乏架构意识的代码，这些代理在修改项目时缺乏对项目结构的理解。随着周一[Junie CLI](https://blog.jetbrains.com/junie/2026/03/junie-cli-the-llm-agnostic-coding-agent-is-now-in-beta/)的发布，该公司认为这将是企业软件开发中的下一个大问题。

诊断始于碎片化。

JetBrains的产品负责人Nik Tkachev本周在[一篇博文](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/)中宣布JetBrains Air时写道：“当前使用编程代理的状况是碎片化的：每个代理都在单独的工具中运行，具有不同的设置、不同的上下文，并且对您的代码没有结构性理解。” JetBrains认为，这种代码孤立地工作，但随着时间的推移，会悄悄地破坏更广泛代码库的连贯性。

在过去18个月里，[代理编程工具](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/)激增，工程团队为了提高生产力而接受了它们——但很大程度上推迟了大规模代码质量问题的思考。代理不会阅读架构决策记录。它们不知道为什么三年前选择了特定的模式。它们不理解遗留模块中固有的部落知识。它们完成手头的任务，然后继续前进。

对于一次性脚本来说，这是一个合理的权衡。但当自主代理在[CI/CD流水线](https://thenewstack.io/introduction-to-ci-cd/)中运行、发起拉取请求并直接提交到共享仓库时，这就成了一个更严重的问题。

“说实话：复杂的代码库还没有为纯粹的代理编程做好准备，”Tkachev写道。“Air专注于代理编排，而不是取代现有的开发工作流程。”

## Junie CLI登场

Junie CLI（目前处于测试阶段）是JetBrains针对代码质量问题的更直接解决方案。该工具被设计为一个完全独立的编程代理——可在终端、任何IDE、GitHub、GitLab和CI/CD流水线中使用——其核心是该公司所称的“代码库智能”。

JetBrains营销卓越负责人Anastasia Krivosheeva在[另一篇博文](https://blog.jetbrains.com/junie/2026/03/junie-cli-the-llm-agnostic-coding-agent-is-now-in-beta/)中宣布Junie CLI时写道：“Junie不仅仅是‘终端中的AI’。” “它是一个功能齐全的独立代理，其功能旨在超越简单的提示。”

Junie CLI没有将每个任务视为无状态提示，而是整合了结构化的项目上下文和工作流程感知，因此它生成的代码是基于代码库的实际形态。

该产品还包括下一任务预测——代理根据项目上下文预测开发人员可能需要什么——以及从竞争工具（包括Claude Code和Codex）的一键迁移。它支持来自OpenAI、Anthropic、Google和Grok的模型，并采用BYOK（自带密钥）方法，除了模型成本外，不收取额外平台费用。

## 大规模代理编程

“我们对代理软件开发抱有原则性的乐观态度——以及务实的态度，”Tkachev写道。“新概念出现的速度比任何人验证它们的速度都快，所以我们宁愿发布有效的产品，也不愿炒作可能有效的产品。”

JetBrains告诉开发者，大规模代理编程需要专业级的技术设施，同时又不疏远那些已经满意使用Claude Code或Cursor的开发者。“影子技术债务”的框架完成了这项工作——它不攻击代理本身，而是攻击它们运行的条件。

JetBrains表示，代理时代需要一个中立的技术设施层，而不是又一个代理。

“我们正在从IDE原生AI扩展到生态系统级AI——使用一个代理连接多个平台，”Krivosheeva写道。

Junie CLI与JetBrains Air一同发布，后者是一个基于开放Agent Client Protocol的新代理开发环境，允许Claude Agent、Gemini CLI、Codex和Junie在同一个工作区中并排运行。这两个产品共同将JetBrains定位为所有代理之下的平台层，而不是任何单个代理的竞争对手。

“Junie在您所在之处与您相遇。通过使Junie在JetBrains IDE之外可用，我们正在从IDE原生AI扩展到生态系统级AI——使用一个代理连接平台，”Krivosheeva写道。“这对我们来说是一个重要的里程碑，也是朝着即使在IDE之外也能实现专业级开发迈出的重要一步。”