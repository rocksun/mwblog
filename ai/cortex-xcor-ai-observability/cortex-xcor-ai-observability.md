<!--
title: Palo Alto Networks发布XCOR：可在几分钟内追踪故障，但目前仍会呼叫工程师
cover: https://cdn.thenewstack.io/media/2026/10/3e7b2848-masantocreative-varepj-lg38-unsplash-scaled.jpg
summary: Palo Alto Networks推出了基于AI的全新可观测性平台Cortex XCOR，旨在利用智能体自动排查故障并推荐修复方案，将故障定位时间缩短至3分钟以内，从而解放SRE并减少工程师的救火压力。
-->

Palo Alto Networks推出了基于AI的全新可观测性平台Cortex XCOR，旨在利用智能体自动排查故障并推荐修复方案，将故障定位时间缩短至3分钟以内，从而解放SRE并减少工程师的救火压力。

> 译自：[XCOR launches to trace outages in minutes. It still pages engineers.](https://thenewstack.io/cortex-xcor-ai-observability/)
> 
> 作者：Adrian Bridgwater

**Palo Alto Networks 上周推出了一种AI驱动可观测性的新方法**，标志着行业从仪表盘和人工事件响应转向由AI智能体自主调查问题并推荐修复方案。

Cortex XCOR 是一个AI驱动的平台，旨在实现可观测性的圣杯：自动查找问题根源并推荐修复方案，而不仅仅是向技术人员展示仪表盘。

该公司表示，云原生架构在基础规模和成本方面的挑战阻碍了这一目标的实现，并且AI爆发前的自动化反应迟钝。Palo Alto Networks 在1月[收购](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-to-acquire-chronosphere--next-gen-observability-leader--for-the-ai-era)了云原生可观测性平台和遥测管道公司 Chronosphere，以便在此方向上开发实时的智能体修复技术。

Cortex XCOR 由 Palo Alto Networks 内部的 Chronosphere 团队构建，旨在将可观测性从静态仪表盘和手动修复转变为AI优先的体验，从而自动化常规和复杂的调查。

Palo Alto Networks 可观测性高级副总裁兼总经理 [Martin Mao](https://www.linkedin.com/in/martinmao/) 告诉 *The New Stack*，当警报触发时，Cortex XCOR 会自动启动一个专门的智能体，由其自主推理底层问题并推荐行动和缓解措施。

“我们不想再在半夜把工程师叫醒来帮他们看懂仪表盘；说实话……我们根本不想叫醒他们，”Mao说道。“虽然 XCOR 默认采用人在回路（human-in-the-loop）的模型，但工程领导者可以随着时间推移扩大其自主权限，最终睡个好觉。”

> “我们不想再在半夜把工程师叫醒来帮他们看懂仪表盘；说实话……我们根本不想叫醒他们。”

## 告别仪表盘杂务与烦琐的故障排除

如果像 XCOR 这样的技术蓬勃发展并普及，我们完全可以预期站点可靠性工程师（SRE）的角色将超越仪表盘杂务。随着 [AI SRE](https://thenewstack.io/ai-sre-root-cause-analysis/) “角色”开始出现，自动化将针对常规的根本原因分析和故障排除。

“现在我们正处于这样一个时刻：SRE将像飞机驾驶员一样运作；他们在平稳飞行时可以依赖自动驾驶，但当出问题时，驾驶舱里仍然需要经验丰富的飞行员。通过自动化故障排除，SRE可以腾出时间专注于更具战略意义的架构工作，而不是疲于救火，”Mao强调道。

BairesDev 的[开发者晴雨表](https://www.bairesdev.com/blog/dev-barometer-q3-2026-devs-answering-for-code/)分析表明，42%的开发者现在表示AI编写了他们至少一半的代码，高于去年的12%。显然，这种节奏带来的代码创建速度需要与以安全为中心的监督相匹配。

> “SRE将像飞机驾驶员一样运作；他们在平稳飞行时可以依赖自动驾驶，但当出问题时，驾驶舱里仍然需要经验丰富的飞行员。”

Palo Alto Networks 的最新产品包括 XCOR Operator，这是一个据称可以帮助“运营团队以与上下文相关的能力匹配AI编码速度”的AI助手。Mao和他的团队表示，XCOR Operator强大的原因在于它“理解用户意图”，并作为在幕后执行的专业智能体的对话接口。

## 从预定义规范到赋予推理模型访问权限和能力

“XCOR Operator解决超出我最初预期的高难度问题的能力让我震惊，”Mao回忆道。“它不仅改变了我与平台和可观测性工作流互动的方式，还让我从根本上重新思考了我们如何设计产品。我们现在正从强大的、针对功能和工作流的预定义规范，转向赋予推理模型正确的访问权限和能力，让它们自己去发现通往答案的各种路径。”

> “它让我从根本上重新思考了我们如何设计产品。”

Mao解释说，如今，可观测平台的用户根据整体部署环境的不同，通常必须扮演多种角色。他们将忙于调查事件、调整警报和仪表盘、优化数据量等。有了 Cortex XCOR，这些角色中的每一个都由专门的AI智能体所镜像，这些智能体经过优化，可以端到端地完成这些特定于任务的工作流。

根据 [Mao关于此次更新的博客](https://www.paloaltonetworks.com/blog/2026/10/observabilitys-ai-moment-introducing-cortex-xcor-ai-driven-observability-for-autonomous-response-with-ai-sre/)，当警报触发时，AI SRE智能体会自动启动，并在平均不到三分钟的时间内自主推理底层问题并推荐行动和缓解措施，在复杂的生产环境中，其根本原因分析的成功率达到75%，另有19%的事件分析被认为是有用的。

## 人工响应仅定位问题就需要20分钟

相比之下，人工响应仅用于定位相关问题、收集初始上下文以及找到正确的待命工程师，就可能需要20分钟。

“随着我们的客户熟悉这种新体验，我们对当前低于三分钟的平均响应时间感到满意。目前，我们在事件发生时首先呼叫工程师，他们通常需要几分钟才能登录平台。在那段时间里，XCOR 已经完成了调查，因此三分钟满足了我们目前的需求，”Mao确认道。

随着用户对分析建立信任并越来越多地自动化修复，Palo Alto Networks 将专注于缩短响应时间。Mao认为团队“已经很好地掌握了”实现这一目标所需的技术，并指出“成本是一个重要因素”，同时Token价格也在稳步下降。

Mao进一步解释说，如果没有完全的端到端可见性和上下文，该平台的任何自动推理都是不可能实现的。Palo Alto Networks 在7月宣布计划收购高保真真实用户监控（RUM）公司 Embrace，并计划将前端 RUM（XCOR RUM）与其自家的 XCOR Synthetics 以及后端和基础设施可观测性结合起来，交付一个全栈平台。

## 救火掩盖了面向未来的能力与远见

如果软件工程团队错过这种可观测性优势，情况会有多糟？Mao暗示最坏的情况是工程师将100%的时间花在救火上，而不是创新或为业务交付价值。由于故障排除已经是工程师工作中压力最大的部分，他认为这可能导致“严重的职业倦怠”，而AI生成代码的日益普及只会加剧这种风险。

“不受控制的可观测性就像一只多动的小狗。它充满希望，但如果不加控制就会摧毁你的预算。随着云原生和AI工作负载导致遥测数据量飙升，组织需要内在的纪律。Chronosphere 将这些成本控制在合理范围内，确保团队获得完全的可见性而不会产生失控的账单。这就是为什么数据优化和成本效益仍然是 XCOR 使命的核心，”Mao说道。

支撑全栈可见性工作的是 XCOR Fabric，这是一项为AI智能体提供实时应用、基础设施和机构上下文的技术。

XCOR Fabric 的生命源泉来自组织的知识库（被描述为结合了基础设施、应用程序和业务逻辑的实时模型）、运营记忆（从过去事件调查中捕获的历史缓存）、用户行为（此处的用户是指运行特定查询和访问特定仪表盘的高级工程师），以及从运行手册、文档和运营文件中获得的人类知识。