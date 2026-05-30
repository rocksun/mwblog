<!--
title: AI 云账单飙升怎么治？解决方法就在眼前，我们为何不敢信任？
cover: https://cdn.thenewstack.io/media/2026/05/b2d95265-rizki-ardia-ajtrcuhubru-unsplash-scaled.jpg
summary: 随着AI工作负载导致云账单飙升，自动资源适配成为优化成本的关键。然而，出于对生产事故的担忧，大多数工程师依然难以完全信任机器自动化。
-->

随着AI工作负载导致云账单飙升，自动资源适配成为优化成本的关键。然而，出于对生产事故的担忧，大多数工程师依然难以完全信任机器自动化。

> 译自：[The fix for soaring AI cloud bills exists — so why won't we trust it?](https://thenewstack.io/kubernetes-rightsizing-trust-gap/)
> 
> 作者：Jennifer Riggins

听 [CloudBolt](https://www.cloudbolt.io/demo) 的首席运营官 [Yasmin Rajabi](https://www.linkedin.com/in/yasminrajabi/) 道来，我们在看待自动化时存在一种不平衡。我们乐于将那些能提高生产力和流程的决策自动化——但当需要向左转动旋钮（即收缩资源）时呢？出于某种原因，人们对此犹豫不决。

“在传统自动化方面，人们的信任度极高，但在资源适配（right-sizing）方面，人们仍然非常谨慎，” Rajabi 告诉 *The New Stack*。“那些每天通过 CI/CD 进行多次部署的工程师不再质疑[自动化]，但当要把资源适配的工作委托给机器时，赢得信任的门槛要高得多。”

数据揭示了这种不平衡为何存在：当面临保持服务“时刻在线”的压力时，过度配置导致的更高云账单似乎是值得付出的代价。但现在，随着消耗大量 GPU 的 AI 工作负载导致云账单飙升，根据 [2026年3月的 CloudBolt 研究报告](https://www.cloudbolt.io/industry-research/cii-kubernetes-automation-trust-gap/)，自动化的资源适配流程已成为 89% 组织的首要任务。

然而，71% 的 Kubernetes 工程师表示，他们仍然需要人工审查来进行资源优化，只有 27% 允许自动应用 CPU 和内存的更改。因此，尽管数据表明这是首要任务，但这种动力并未体现在实际的工作流中。

> “当要把资源适配的工作委托给机器时，赢得信任的门槛要高得多。”

*The New Stack* 将在**太平洋时间 6 月 24 日星期三**上午 9 点（英国夏令时下午 5 点）与 Rajabi 以及 StormForge 的产品负责人 [Reid Vandewiele](https://www.linkedin.com/in/reidmv/) 进行座谈，共同探讨弥补这种资源适配差距的紧迫性——特别是针对 AI 的 Kubernetes 工作负载。

欢迎加入我们的直播，不仅可以学习如何衡量组织自动化的成熟度，还能随着时间的推移逐步建立这种信任，包括使用策略性 CPU 限流、内存不足（OOM）行为，以及回退模式。

## **注册加入这场对话**

Rajabi 解释说，资源适配是一个多维度的难题，跨越了在日益复杂的环境中日益复杂的工作负载，因此一旦出现问题，感觉几乎不可能逆转。要让这种自动化发挥作用，这种信任不仅必须在团队内部建立，还必须在整个组织中进行扩展。

“建立对自动化解决方案的信任需要很长时间，而消除或严重削弱这种信任却非常快，” Rajabi 警告说。“一次生产事故就能让一个应用团队从愿意尝试自动资源调配变成绝对不接受——‘不要在我的应用上用，我们很特殊’。”

[加入我们 6 月 24 日的活动](https://thenewstack.io/webinar/the-kubernetes-rightsizing-trust-gap-why-the-stakes-just-got-higher/)，了解如何洞察 AI 工作负载的实际成本，并采取能消除资源配置中盲目推测的计划。