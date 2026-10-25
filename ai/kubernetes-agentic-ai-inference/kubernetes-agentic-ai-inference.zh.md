**欢迎阅读新一期的 [*通往 KubeCon 之路*](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)**！随着我们倒计时迎接将于 11 月 9 日至 12 日在盐湖城举行的 [KubeCon + CloudNativeCon North America 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/) 大会，我们将持续追踪 Kubernetes 和云原生生态系统的最新动态。

本周专栏的一半内容聚焦于在融入智能体 AI 需求时理顺 Kubernetes 的复杂性：自动化 pod 重启故障排查、同步调度器与自动扩缩容器之间的通信，以及成熟化我们在云原生堆栈中分发推理的方式。

另一半内容则更深入地探讨了我们需要在 Kubernetes 环境中密切关注的问题：缺少了什么上下文、哪些指标被漏掉了，以及你已经在使用的 AI 智能体是否真的具备 SRE 的实力。

让我们切入正题。

# HPE 谈 AI 开发中的 pod 重启自动化

随着越来越多的企业转向 Kubernetes 来运行大规模 AI 和机器学习任务，他们正遭遇一个共同的障碍：pod 重启。当客户利用 [HPE](https://www.hpe.com/) 的 [HPE Private Cloud AI](https://www.hpe.com/us/en/products/private-cloud/pcai.html) (PCAI) 在诸如 Kubernetes 这种本质上短暂的基于容器的基础设施上托管长期运行的 [AI/ML 工作负载](https://thenewstack.io/kagent-kubernetes-ai-agents/)时，HPE 注意到了这一现象。

*Hewlett Packard Enterprise (HPE) 是通往 KubeCon 之路的首席赞助商。* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *帮助 IT 组织在混合、多供应商环境中现代化基础设施、简化运营并加速 AI 倡议。*

据 HPE 系统软件工程师 [Guoping Jia](https://www.linkedin.com/in/guoping-jia-934a6820?originalSubdomain=fr) 介绍，Kubernetes 虽开箱即提供了一些故障排查命令，但仍需要大量的纯手动调查。“这种运维工作流在 PCAI 的大型集群环境中无法有效扩展，”[Jia 在 HPE 博客中写道](https://developer.hpe.com/blog/automating-kubernetes-pod-troubleshooting-in-hpe-private-cloud-ai/)。

他的解决方案涉及针对故障排查的更智能的自动化，即利用开源的 Kubernetes 故障排查工具 [k8s-pod-restart-info-collector](https://github.com/airwallex/k8s-pod-restart-info-collector)，自动收集详细信息并将诊断信息直接发送到 Slack 频道。这是改善 Kubernetes 操作人员可用性的一个有用策略。

## 调度器与自动扩缩容器会走向联合吗？

最近有很多关于 Kubernetes 如何演进以满足 AI 新需求的讨论。本周，[AWS](https://aws.amazon.com/) 高级软件开发经理 [Sajjan Gundapuneedi](https://www.linkedin.com/in/sgundapu/) 和 [Neelendra Bhandari](https://www.linkedin.com/in/neelendrabhandari/) 在[这篇博客文章](https://www.cncf.io/blog/2026/10/19/how-ai-workloads-are-reshaping-kubernetes-autoscaling/)中就 AI 如何重塑 Kubernetes 自动扩缩容发表了看法。

他们强调的核心问题是，在 Kubernetes 上管理 GPU 加速器时，将 pod 放置在现有节点上的调度器与添加新节点的自动扩缩容器之间存在摩擦。通常这两方并不在同一频道上，导致 pod 处于挂起状态，而昂贵的 GPU 却处于闲置状态。容量预留、设备拓扑以及 GPU 共享使情况变得更加复杂。

> “稀缺的加速器的价值，取决于调度它的循环与配置它的循环之间达成的一致。”

“稀缺的加速器的价值，取决于调度它的循环与配置它的循环之间达成的一致，”作者写道。“推理使其变得紧迫而不是流于学术，因为突发性的服务和智能体工作负载对冷节点毫无耐心。”

对他们来说，解决方案已经在成型中：[动态资源分配](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/)（DRA）感知的自动扩缩容器、[工作负载感知调度](https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/)，以及一个配套机制——[配置请求](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/proposals/provisioning-request.md)，用来连接这两方。尽管如此，他们预计自动扩缩容器将成长为“一个更具调度感知能力的合作伙伴”。

更深层次的整合也在进行中。[SIG-Autoscaling 小组](https://groups.google.com/g/kubernetes-sig-autoscaling/c/CzuCD--BETM)中的一项公开提案勾勒出了一些 API，这些 API 将允许两个循环直接对话，从而使调度器能够看到可被配置的容量、表达跨容量的放置偏好并明确请求它。

## 随着 llm-d v1.0 的发布，分布式 AI 推理走向成熟

周二，在[北美 PyTorch 会议](https://events.linuxfoundation.org/pytorch-conference-2026/)上，CNCF 沙箱项目 llm-d [达到了 v1.0 版本](https://llm-d.ai/blog/llm-d-v1.0-state-of-the-art-inference-ready-for-day-2)。该项目现在架起了 [PyTorch 生态系统](https://pytorch.org/)中的 AI 应用开发者与生产级云原生堆栈之间的桥梁。

llm-d 的联合创始人兼首席维护者、IBM AI 混合云平台杰出工程师 [Carlos Costa](https://www.linkedin.com/in/carlos-costa-9b9b1a1/) 表示，v1.0 版本的发布标志着成熟。

“这是开源 AI 服务从实验项目跨越到你可以构建其上的可靠基础设施的时刻，”Costa 告诉 *The New Stack*。他补充说，早期版本侧重于证明先进的性能，而 v1.0 则是为了在生产中维持这种性能。

llm-d 已经在 [Tesla](https://llm-d.ai/blog/production-grade-llm-inference-at-scale-kserve-llm-d-vllm)、AWS、[Oracle](https://blogs.oracle.com/ai-and-datascience/llm-inference-at-scale-with-llm-d-on-oci)、Google 等公司得到了广泛应用。Costa 补充说，[最近的一项 IBM Research 演示](https://www.ibm.com/downloads/documents/us-en/17f55bd44d44b0e3)发现，探索量子纠错硬件的智能体工厂在使用 llm-d 运行开源模型时，其推理成本比全专有配置低 11.5 倍。

“这个演示展示了 llm-d 真正大放异彩的地方：智能体工作负载，”他说，并补充说它吸收了突发的智能体流量，并且在 IBM 的测试中，将缓存重用率推高至 98% 左右。

## 从构建模型到大规模运维前沿智能

为了领略 KubeCon NA 上预期会出现的讨论类型，让我们简要访问东方。CNCF 首席技术官 [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) 上个月在上海举行的 KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026 上，与张潇一起发表了题为[《大规模运维前沿智能》](https://www.youtube.com/watch?v=EyY90x3Z1GE)的演讲，为大会奠定了很好的基调。

正如他所说，这不再仅仅关于模型。而是关于将它们全部投入工作。“AI 的本质正在从纯粹关于构建最伟大的模型，[转向]我们如何真正让它大规模运行、将其全部缝合在一起并在不同类型的环境中运行，”Aniszczyk 说。

Cloudflare 首席执行官 Matthew Prince [最近宣布](https://www.computing.co.uk/news/2026/ai/bot-traffic-overtakes-humans-online)，由 AI 智能体驱动的机器人流量在线上首次超过了人类流量。Aniszczyk 表示，这种转变给系统带来了巨大的压力，他提到了[最近的 GitHub 故障](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/)。随着推理成为主要的负载，一切都在发生转变。

> “这可能是我职业生涯中见过最疯狂的技术变革。”

他指出，这种转变引发了各种附带问题，从构建新基础设施、构建更多数据中心到确保有足够的可获取电力。“这可能是我职业生涯中见过最疯狂的技术变革，”Aniszczyk 说。

尽管如此，他依然是个乐观主义者，将其视为一个有趣的问题和云原生社区共同攻克的挑战。

大量 AI 站点可靠性工程师（SRE）平台正在涌现。但据 [Radar](https://github.com/skyhook-io/radar)（[Skyhook.io](http://skyhook.io)）首席产品官 [Roy Libman](https://www.linkedin.com/in/roylibman/) 称，你的下一个 SRE 雇员可能就在你的指尖下：你已经在使用的 AI 编程智能体。诀窍是赋予它正确的上下文。

“你的工程师们使用的编程智能体——无论是 Claude Code、Codex 还是 Cursor——已经可以调查 Kubernetes 集群了，”Libman [在 CNCF 博客上写道](https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context/)。“它通常缺少的是上下文：现在是什么在失败，以及在它崩溃之前发生了什么改变。”

在他的实时集群 50 个注入故障的基准测试中，通过 MCP 工具获得只读上下文的 Claude Code，其诊断准确率略高于通过 shell 和 kubectl 访问。更大的差异在于速度：在拥有上下文的情况下，它在 86% 的故障中能在两分钟内得出正确诊断，而使用 shell 的比例为 60%。

这是一个有趣的信号，表明上下文对于诊断复杂错误至关重要，并且你可能不需要为了分诊问题而花钱（双关语）购买另一个 AI 订阅。

# 行业视角：Kubernetes 中未被检测到的是什么

[先前的一篇通往 KubeCon 之路](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/)曾询问 OTel 和 Prometheus 还缺少什么。嗯，其中一个差距是不是时间序列的状态，比如慢日志条目、客户端列表以及访问控制列表（ACL）的更改，[Redis](https://redis.io/) 前工程经理、[Valkey](https://valkey.io/) 现状贡献者兼 [BetterDB](https://www.betterdb.com/) 创始 CTO [Kristiyan Ivanov](https://www.linkedin.com/in/kristiyan-i-8b3b5671/) 分享道。“这些在抓取（scrapes）之间丢失了，”他告诉 *The New Stack*。

> “指标很重要，但它们无法解释原因。”

“指标很重要，但它们无法解释原因。”Ivanov 表示，Kubernetes 中有很多东西未被检测到，因为 [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 和 Redis 将证据保存在内存缓冲区中，而 Prometheus 将其精简为长度和计数器。“Kubernetes 在几个方面使情况变得更糟，”他说，并指出 pod 重启、故障转移和短暂的 pod IP 会恶化追踪。

“生态系统中的几乎所有东西都是一个 INFO 抓取器，”他说。“普遍缺失的是：跨重启和故障转移的持久历史、对服务或 ACL 用户的归属、ACL 和配置更改的审计跟踪，以及跨分片的聚合。”

新兴的方法正在帮助云运营商发现这些盲区。他指出了 Valkey 检测能力的改进以及 OpenTelemetry eBPF 仪表的进步，从而实现了精细追踪。但他表示，eBPF 无法看到驱逐、ACL 拒绝或配置更改。这些需要引擎级别的收集。

*随着 Kubernetes 的演进，对其运行团队的要求也在演进。首席赞助商* [*HPE*](https://www.hpe.com/us/en/products/software.html) *通过涵盖虚拟化、云管理、可观测性和自动化的软件，帮助团队应对这种复杂性。*

## 一半人无法有效衡量 AI 智能体

根据 10 月 20 日发布的 [Splunk 2026 年可观测性状态报告](https://www.splunk.com/en_us/pdfs/gated/ebooks/state-of-observability-2026.pdf)（该报告调查了 2,050 名 ITOps 和工程专业人员），87% 的受访者表示监控 AI 是当务之急，但超过一半的人承认他们无法有效衡量 AI 质量（如 LLM 响应质量）或控制 AI 成本。

该报告还发现，83% 的人对 AI 智能体的意料之外的后果感到担忧。这与智能体 AI 倾向于采取意外行动并产生突发流量模式的趋势相吻合，这两者都在推动重大基础设施变革。

思科总裁兼首席产品官 Jeetu Patel 在[新闻稿](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m10/splunk-state-of-observability-2026-avoiding-the-hidden-costs-of-ai-agents.html)中表示：“大多数公司很快将拥有远超人类数量的在职智能体。”根据 81% 的受访者的说法，监控 AI 也在推动可观测性团队与安全团队之间进行更多的协作。

## 来自云原生宇宙的更多更新

围绕云原生的兴奋永不眠。以下是过去一周左右的一些社区、项目和供应商更新。

## 通往 KubeCon 之路的又一站

*通往 KubeCon 之路是由 HPE 呈献的八部分系列文章。在您前往之前，探索* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *如何帮助 IT 团队以更少的心力做更多的事情。*

这个系列即将结束——只剩最后一期了。

我们下周将在这里通过一篇特殊的通往 KubeCon 之路告别信来做个总结。在此期间，您可以在[通往 KubeCon 之路存档](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)中回顾以前的版本。

本系列的作者 Bill Doerrfeld 欢迎社区投稿。欢迎分享有趣的观点、新版本，或者关于盐湖城最佳潜水酒吧的建议。

他接受 [LinkedIn](https://www.linkedin.com/in/doerrfeldbill/) 上的直接消息，或者您可以通过他的[个人联系页面](https://www.doerrfeld.io/contact)与他联系。