**欢迎阅读最后一期** [**通往 KubeCon 之路**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)。随着我们迎向 11 月 9 日至 12 日在犹他州盐湖城举办的 KubeCon + CloudNativeCon NA，我们将在 *The New Stack* 上每周追踪 Kubernetes 和云原生生态系统。

本周，我们将探讨 Kubernetes 如何获得运行 AI 工作负载的新指导，包括 TNS 的一本新书、一个专门的 Kubernetes 工作组，以及关于在多个 GPU 上运行大语言模型的建议。

在这个万圣节前夕发布的专栏中，我们还邀请了讲新语言的 OTel 运营商、来自最新 AGNTCon + MCPCon 的安全恐怖故事，以及理清 Kubernetes Pod 故障排查误入歧途的黑暗网络。

## **在 KubeCon 上与 HPE 一起加入对话**

HPE 今年将在 KubeCon NA 上有[强大的阵容](https://www.hpe.com/us/en/events/kubecon.html)。作为黄金赞助商，他们将设在 151 号和 145 号展位，全天进行现场演讲，主题涵盖 vSphere、HPE Kubernetes 服务 (HKS)、分布式推理、为 Kubernetes 设置云存储等。

*Hewlett Packard Enterprise (HPE) 是“通往 KubeCon 之路”的呈现赞助商。* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *帮助 IT 组织跨混合、多供应商环境现代化基础设施、简化运营并加速 AI 倡议。*

今年，重点是跨虚拟机、基础设施和云的 Kubernetes 环境中获得可见性和控制力。如果您想安排与 HPE 代表的会面，请联系 jennifer.osuna@hpe.com。

## **TNS 发布 2027 年 Kubernetes 指南**

与 HPE 合作，The New Stack [出版了一本实用书籍](https://thenewstack.io/kubernetes-agentic-ai-platforms/)，其中包含在 Kubernetes 上运行 AI 工作负载的团队的十项检查。该书名为《[*2027 年的 Kubernetes：为 AI、自主性和规模构建平台*](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)》，现已开放下载。

该指南由特约作家 [Chris J. Preimesberger](https://www.linkedin.com/in/editingwhiz/) 撰写，涵盖了整个生命周期，包括如何在发布前对基础设施进行压力测试、如何满足智能体 AI 的细微需求、需要注意什么以及如何为智能体开发更强大的权限模型。

由于智能体 AI 容易出现突发且不可预测的行为，在 Kubernetes 上为您的基础设施配备正确的方法是实现生产稳定性和规模化 AI 成功的重要第一步。

## **Kubernetes 成立工作负载一致性工作组**

工作负载类型多年来一直在扩展。毫无疑问，AI 增加了更多的多样性。在此背景下，10 月 27 日星期二，Kubernetes 社区宣布成立专门的[工作负载一致性工作组](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/)。

Broadcom 的 [Nabarun Pal](https://www.linkedin.com/in/palnabarun/) 在 [Kubernetes 博客](https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/)上代表 WG Workload Conformance 撰文称：“该工作组正在为工作负载在 Kubernetes 上的运行时行为编写共享标准。” Pal 补充说，为此，他们需要社区的意见。

[Kubernetes AI 一致性](https://github.com/cncf/k8s-ai-conformance)测试已经确定集群是否可以运行 AI 或机器学习 (ML) 工作负载。然而目前尚不存在针对工作负载的一致性测试，这需要变通方法、手动探索或监控诸如节点排空或权限问题等迹象。因此，新的工作组旨在为工作负载创建类似的标准。

随着 Kubernetes 社区应对包括 AI 在内的日益增长的工作负载多样性，这是向前迈出的重要一步。感兴趣的人士可以阅读[工作组提案](https://github.com/kubernetes/community/pull/9139)了解更多信息，加入 [Slack 频道](https://kubernetes.slack.com/messages/wg-workload-conformance)，或参加[双周会议](https://docs.google.com/document/d/16GPnmukPqbTkauWb3CtXzA3aEDUXoVKY34gA41YQmPk/edit)以参与其中。

## **OpenTelemetry 转换语言达到 v1 版本**

本周早些时候，OpenTelemetry (OTel) 项目达到了一个里程碑：[OpenTelemetry 转换语言 (OTTL) 已达到 v1 版本](https://opentelemetry.io/blog/2026/ottl-v1/)。它对于追踪、指标和日志是稳定的，并包含在 Collector Contrib v0.164.0 及更高版本中。

正如 Grafana Labs 的 [Tyler Helmuth](https://www.linkedin.com/in/tyler-helmuth-53150899/) [在 OTel 博客上](https://opentelemetry.io/blog/2026/ottl-v1/)回忆的那样，OTTL 创立于 2022 年，作为转换处理器的配置语言。这种特定领域语言允许您直接在收集器级别修改、过滤和丰富遥感数据。

长远思考者会喜欢这一点：他们还对 OTTL 做出了重大的向后兼容承诺。Helmuth 说：“如果您编写 OTTL 语句，语法和标准函数将保持向后兼容。”

*随着 Kubernetes 的演进，对其运行团队的要求也在变化。呈现赞助商* [*HPE*](https://www.hpe.com/us/en/products/software.html) *通过涵盖虚拟化、云管理、可观测性和自动化的软件，帮助团队应对这种复杂性。*

## **在共享 GPU 上解决大语言模型问题**

将所有 AI 工作负载放在单个 GPU 上既昂贵又低效。但是，我们如何在共享 GPU 上安全地打包多个大语言模型，而不需要大量的猜测或手动苦差事呢？

AWS 高级解决方案架构师 [Ratnopam Chakrabarti](https://www.linkedin.com/in/ratnopam/) 在 X 上分享了他即将进行的 Nvidia-AWS 联合会议的早期预览，这似乎将为 KubeCon 与会者解答这个问题。

他说他的 KubeCon 会议将“实时演示一个智能体流水线，该流水线可配置文件工作负载并处理 GPU 上的模型共置”。这是今年 KubeCon 上众多解决 Kubernetes 上 AI 优化的会议之一。

## **使用 VPC 流日志排查 GKE 工作负载故障**

本周在 [Google Cloud 博客](https://cloud.google.com/blog/products/containers-kubernetes/using-vpc-flow-logs-to-troubleshoot-gke-workloads/)上，Google Cloud 产品经理 Nishant Kumar 和 Whitney Jenkins 描述了云运营商面临的一个常见问题：Kubernetes Pod 是短暂的，这使得它们很难进行故障排查。

正如他们所描述的，“在标准的云网络中，流日志通过记录 IP 地址、端口和协议之间的连接来提供这种视图。” 然而，在 Kubernetes 中，Pod 是临时的；它们不断添加，当你追踪到它们时，它们通常已经消失了——几乎没有留下任何证据或记录来指导故障排查。

变通方法（至少对于使用 Google Kubernetes Engine (GKE) 的人来说）是其内置的 [VPC 流日志](https://docs.cloud.google.com/vpc/docs/using-flow-logs)。此功能使用 Google 的虚拟化网络记录每个采样的流，并附带 Pod、工作负载、命名空间和服务等元数据。

这是云原生平台如何继续推进 Kubernetes 周围的基础设施以提高其可见性和可用性的一个例子。

## **AGNTCon + MCPCon 优先考虑智能体安全**

你的智能体是否在不知情的情况下安装了恶意软件？这完全有可能。

本月在加利福尼亚州圣何塞举行的最新 [AGNTCon + MCPCon](https://events.linuxfoundation.org/agntcon-mcpcon-north-america/) 活动有很多有趣的演讲，可能会引起云原生社区的共鸣，他们正带着担忧的目光看着智能体趋势。

例如，Snyk 的 [Liran Tal](https://lirantal.com/speaking/talks/your-ai-agent-installed-malware-because-a-skill-md-told-it-to) 发表了一场名为《[*你的 AI 智能体安装了恶意软件，因为一个 SKILL.md 文件这样告诉它*](https://lirantal.com/speaking/events/2026-10-23-agntcon-mcpcon-north-america-2026)》的演讲。Tal 探讨了智能体是如何经常被诱骗运行恶意软件的，并提供了一些如何防止这种情况的指导。

Vstorm 的 Antoni Kozelski 和 Bartosz Adam Gonczarek [还展示了](https://vstorm.co/events/agntcon-mcpcon-north-america-2026/)他们如何构建电子商务 MCP 服务器，并让智能体跨四个不同的主机对购买进行实验。它在每种情况下的行为都截然不同。

这次会议引发了一场关于允许或禁止智能体采取不可逆步骤的授权规则应该存在于何处的对话。对于 Vstorm 来说，这意味着将它们放在服务器上，而不是本地。他们还将很快跟进关于此主题的[网络研讨会](https://vstorm.co/events/agntcon-mcpcon-follow-up-webinar-2026/)。

这些故事只是我们看到的众多案例中的两个：赋予 AI 智能体最高权限的[意料之外的后果](https://curity.io/blog/5-agentic-ai-security-incidents-and-vulnerabilities/)。云原生运营商在构建支持智能体的基础基础设施时，应该关注这样的故事。

## **KubeCon 见**

*“通往 KubeCon 之路”是由 HPE 呈现的八部分系列节目。在您出发之前，探索* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *如何帮助 IT 团队以更少的复杂性做更多的事情。*

今年的“通往 KubeCon 之路”系列节目到此结束！在过去的两个月里，能够剖析云原生世界的顶级运动是一种特权和冒险。

在这个每周专栏中，我们在八个版本中涵盖了许多领域，跨越了 Kubernetes 本身的更新（例如 [Kubernetes 1.37 更新](https://thenewstack.io/kubecon-kubernetes-updates-security/)和转向 [cgroup v2](https://thenewstack.io/kubernetes-node-swap-ai/)）。

大部分讨论都集中在云原生技术如何为 AI 演进上。我们研究了关于[大规模 Kubernetes 推理](https://thenewstack.io/kubernetes-ai-inference-costs/)的案例研究，以及[智能体工具包](https://thenewstack.io/kubecon-agent-harness-koordinator/)是如何演进的。

另一个反复出现的主题是提高运营商的可见性。我们看到了 [OpenTelemetry 和 Prometheus 如何融合](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/)，以及如何[发现空闲的 GPU](https://thenewstack.io/kubernetes-agentic-ai-inference/) 并进行优化。

可以说，最大的收获是 Kubernetes 生态系统正面临重大转变，以应对[大规模运行 AI 工作负载](https://thenewstack.io/kagent-kubernetes-ai-agents/)的挑战。它能胜任这项任务吗？

KubeCon NA 预计将正面解决这个问题，从同期活动的讨论到主旨演讲、分会场和展示大厅。

查看[“通往 KubeCon 之路”归档](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)以获取本系列的所有版本，以及 TNS 和 [HPE](https://www.hpe.com/us/en/products/software.html) 团队的其他见解。非常感谢该专栏的赞助商 HPE 使本专栏得以实现，也感谢分享其见解的社区成员。

现在，我们很高兴能在 KubeCon NA 上继续面对面交流！

在那里见。