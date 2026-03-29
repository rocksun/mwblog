<!--
title: Solo.io 推出 AgentBench，解决代理式AI“最大未解难题”
cover: https://cdn.thenewstack.io/media/2026/03/8d0d3699-chloe-wecdf-iplqe-unsplash-scaled.jpg
summary: Solo.io推出开源项目AgentBench，旨在解决代理式AI评估难题。它提供框架测试AI代理在真实工作流中的可靠性与性能，通过与Gloo等平台集成，标准化评估AI系统。Solo.io还捐赠了agentregistry给CNCF，以推动AI代理的标准化管理。
-->

Solo.io推出开源项目AgentBench，旨在解决代理式AI评估难题。它提供框架测试AI代理在真实工作流中的可靠性与性能，通过与Gloo等平台集成，标准化评估AI系统。Solo.io还捐赠了agentregistry给CNCF，以推动AI代理的标准化管理。

> 译自：[Solo.io launches AgentBench to solve agentic AI's "biggest unsolved problem"](https://thenewstack.io/soloio-agentbench-evaluates-ai-agents/)
> 
> 作者：Steven J. Vaughan-Nichols

有如此多的代理，却如此少的时间来评估它们。 [Solo.io](http://solo.io) 的新项目可以提供帮助。

[Agentic AI（代理式人工智能）](https://thenewstack.io/agentic-ai-powerful-but-fragile-what-you-need-to-know/) 已经爆发式增长。这些工具变得炙手可热。但是，有一个小问题。你如何评估它们？Solo.io，以其云原生网络和API网关平台 Gloo 而闻名，推出了一项新的开源计划，名为 [AgentBench](https://github.com/THUDM/AgentBench)。它旨在帮助开发者评估和基准测试“代理式人工智能”系统。

Solo.io 在阿姆斯特丹举行的 [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上宣布了该项目。据 Solo.io 创始人兼首席执行官 Idit Levine 称，自主AI系统给云运营带来了新的挑战。

“企业正在试验AI副驾驶和基础设施代理，但他们缺乏对这些系统在给定开放式目标时行为方式的了解。AgentBench 帮助团队不仅了解模型能做什么，还能了解它们的推理在哪里出现问题，”Levine 告诉 The New Stack。

Levine 继续说道：“评估是当今代理式基础设施中最大的未解决问题。组织有构建代理的框架、连接代理的网关以及管理代理的注册表，但没有一致的方法来判断代理是否足够可靠，可以在生产环境中信任。”这就是症结所在。

AgentBench 提供了一个框架，用于测试AI代理在真实世界工作流中的有效性，例如基础设施自动化、API编排和服务管理。目标是为企业团队提供一种标准化方法，在将自主代理部署到生产环境之前，衡量其可靠性、延迟和成功率。

> “评估是当今代理式基础设施中最大的未解决问题。组织有构建代理的框架、连接代理的网关以及管理代理的注册表，但没有一致的方法来判断代理是否足够可靠，可以在生产环境中信任。”

该框架与 Solo.io 的 Gloo 平台和 Envoy Proxy 集成。这使您能够在受控条件下模拟多步任务，例如配置微服务、更新路由策略或故障排除 Kubernetes 集群。每次运行都会生成可重现的日志、指标和结果数据，可用于比较不同的AI后端或代理架构。

该公司声称“AgentBench 是第一个旨在评估 LLM-as-Agent 在不同环境中的基准测试。” 为此，该程序依赖于 OpenTelemetry。

> “无论您是使用商业API还是像 Llama 3 这样的开放式LLM，您都需要透明的指标来进行决策。……我们希望 AgentBench 成为AI运营社区的通用参考点。”

此外，Solo 表示该开源项目是使AI驱动运营可审计和可信赖的更广泛努力的一部分。Levine 说：“无论您是使用商业API还是像 Llama 3 这样的开放式LLM，您都需要透明的指标来进行决策。”“我们希望 AgentBench 成为AI运营社区的通用参考点。”

AgentBench 在 GitHub 上以 Apache 2.0 许可证提供。Solo.io 计划与其他云原生供应商和AI研究组合作，以扩展测试库并与常见的机器学习评估工具集成。

此外，Solo.io 将其 [agentregistry](https://aregistry.ai/)（一个用于AI代理、MCP工具和代理技能的AI原生开源注册表）捐赠给了 Cloud Native Computing Foundation (CNCF)。该程序使您能够标准化AI能力在整个企业中的目录、发现和管理方式。

随着每个人都迅速转向代理式计算，我预计这两个程序将获得许多拥趸。