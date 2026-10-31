**Kubernetes集群可能运行正常，但其上运行的AI服务却让用户感到失望。** 模型可能会迅速返回第一个Token，但完成整个回答却花费了太长时间。它也可能迅速响应，却依然给出错误的答案。而繁忙的GPU对于这两种结果都提供不了多少洞察。运营上面临的挑战是将AI服务的行为与其背后的Kubernetes、GPU、计算、存储和网络条件联系起来，而不是孤立地看待每一层。

这就是为什么你应该在生产环境部署之前测量推理服务，然后将实际运行表现与基准进行对比。在HPE赞助的这篇关于AI和Kubernetes系列文章的第四篇中，《The New Stack》采访了HPE Morpheus Software的高级首席产品经理Marius Bogoevici；[HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html)产品管理副总裁[Mahesh Ramachandran](https://www.linkedin.com/in/ramachandranm/)；以及[HPE Morpheus Software](https://www.linkedin.com/in/morpheus-software.html)的首席产品经理[Karthik Subramanian](https://www.linkedin.com/in/karthik-subramanian-lnkd/)。

推理带来了进一步的问题：整个服务能否以业务能够支持的成本和速度提供有用的结果？

*本系列前期文章：*

## **从用户体验入手，然后建立基准**

对于对话式服务，Bogoevici建议测量首字延迟（time to first token）、每个输出Token的时间、可靠性、容量、资源效率、成本和回答质量。合适的组合取决于团队打算提供的体验。快速的第一个Token可能会掩盖后续生成缓慢的问题；快速的完整响应仍然可能是不准确或无帮助的。

> “快速的第一个Token可能会掩盖后续生成缓慢的问题；快速的完整响应仍然可能是不准确或无帮助的。”

首字延迟和完整响应时间回答了不同的问题。Token间延迟和每个输出Token的时间有助于解释首字到达之后的生成速度。团队应该记录他们在哪里测量每个时间间隔，并在持续负载和需求激增的情况下比较结果。为特定的工作负载和用户体验设定目标。

Ramachandran敦促团队在客户依赖AI服务之前对其进行性能剖析（profile）。测试具有代表性的提示词（prompt）和上下文长度、输出体量以及流量水平。记录这些条件下的Token吞吐量、延迟和服务级别指标。由此产生的基准为运维人员提供了一个参考，用于衡量生产环境中的行为变化。

将这些工作负载指标与基础设施性能和容量相关联，可以帮助团队区分不断上升的推理需求与资源争用，从而更有效地规划容量。正如Ramachandran告诉《The New Stack》的那样，团队应该“在发布之前对其进行性能剖析。”

质量需要单独评估。Bogoevici表示，团队应该询问服务是给出了正确的答案还是产生了幻觉。平台遥测数据可以显示请求得到了服务，但数据科学和领域专家需要针对答案进行具有代表性的测试和验收标准。

新出版的电子书[《2027年的Kubernetes：构建面向AI、自主性和规模的平台》](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)建议，在评估服务性能的同时评估输出质量，并且在模型、提示词、检索或服务发生更改后重新审视这两者。

## **当GPU很忙但服务很慢时**

GPU利用率是一个有用的信号，但它[并不能识别瓶颈所在](https://www.hpe.com/us/en/newsroom/blog-post/2026/02/the-next-bottleneck-in-enterprise-ai-isnt-compute-its-context.html)。Bogoevici勾勒了一个具有误导性的庆祝场景：“我们的GPU利用率达到了100%。所以我们做得很好。”这并没有告诉团队该服务实际表现如何。Ramachandran建议检查推理Pod是否根据适合工作负载的指标进行扩缩容、请求是否到达了预期的模型、以及相关组件是否能在需要时进行调度。不同的模型可能有不同的延迟和容量需求，因此请求组合的变化可能会改变用户体验，即使GPU活动看起来很正常。

> Bogoevici勾勒了一个具有误导性的庆祝场景：“我们的GPU利用率达到了100%。所以我们做得很好。”

Subramanian增加了围绕模型的依赖项：网络配置以及数据库或向量数据库的响应时间。他提出了另一个问题：“GPU分区是否太小而无法服务该模型？”这些是排查路径，而不是适用于每个部署的诊断结果。团队应该在选择修复方案之前，将它们与受影响的请求和时间窗口进行关联。

Kubernetes的[水平Pod自动扩缩器（HPA）](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)可以使用配置的自定义或外部指标，因此团队不必仅仅因为CPU利用率是推理的不良触发器而替换它。他们确实需要为其服务栈提供和测试指标管道、扩缩容边界以及可用的加速器容量。扩缩容策略无法让额外的GPU容量瞬间出现。

## **HPE Morpheus和OpsRamp的贡献**

HPE将[HPE](https://www.hpe.com/us/en/products/software/morpheus-software.html) [Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html)描述为一个用于跨混合环境进行受控配置和自动化的平台。其Advanced和Enterprise版本包括[HPE Kubernetes Service (HKS)](https://developer.hpe.com/blog/hpe-morpheus-enterprise-software-enhances-its-kubernetes-service-with-new-features/)；Enterprise将运营模型扩展到了混合云和公共云环境。平台团队可以使用目录项、蓝图、访问控制和审批来定义他们如何请求和管理受支持的环境。这为平台团队提供了一种一致的方法来交付受控的自助服务并共同管理虚拟机和Kubernetes集群，从而减少了单独的工具和手动交接。仅凭这些功能并不能对模型进行基准测试，也不能决定其答案是否优秀。

[HPE OpsRamp Software](https://www.hpe.com/us/en/products/software/opsramp-software.html)提供了跨多厂商混合基础设施和应用程序的全栈可观测性和监控，具有服务拓扑图、AI驱动的事件关联和运维自动化，帮助团队了解依赖关系并从检测走向解决。Ramachandran将HPE Morpheus描述为HPE更广泛云运维方法中的配置引擎，将OpsRamp描述为可观测性引擎。

Ramachandran表示，HPE的组合解决方案包括Morpheus、OpsRamp和运行时。他说，它可以在模型服务环境中测量Token服务速率，并在智能体（agentic）工作负载中测量Token请求速率。HPE正在扩展OpsRamp的AI工作负载可观测性，将模型和智能体活动、Token体量、Token服务速率、推理延迟以及首字延迟与支持的基础设施遥测数据连接起来。

运营价值在于相关性：团队可以调查缓慢的响应是源于应用程序、模型服务层还是基础设施，同时利用工作负载需求来为容量规划和成本问责提供信息。对于特定的部署，团队应确认哪个组件发出每个指标、它是如何收集的，以及需要哪些额外的应用程序插桩（instrumentation）。

对于智能体应用程序，HPE计划的可观测性增强功能将该上下文扩展到AI跟踪、工具调用、错误和质量信号，以及Kubernetes、CPU、GPU、内存、存储和网络遥测。还计划采用基于轻量级eBPF和OpenTelemetry的插桩，以深化可见性，同时最大限度地减少收集开销。这些信号支持调查；它们不能取代特定领域的答案评估或安全控制。

正如本系列[前一篇文章](https://thenewstack.io/kubernetes-hidden-latency-telemetry/)所解释的那样，跨技术栈收集遥测数据取决于部署的agent、集成、权限和应用程序插桩。对于推理服务，将面向用户的测量与模型服务器指标和跟踪、Kubernetes事件以及相关的网络、数据库和加速器信号连接起来。检查可见性在哪里停止，尤其是在外部模型或服务边界处。

## **为AI特定的路由和调度做计划**

展望2027年，Ramachandran敦促团队将自动扩缩容、模型路由和调度视为AI工作负载的刻意设计选择。他讨论了内容感知请求路由、协同调度相关组件以及分类服务（disaggregated serving）。这些是针对特定架构进行评估的领域，而不是每个Kubernetes安装或HPE产品自动提供的功能。

一个[实验性的Gateway API提案](https://gateway-api.sigs.k8s.io/geps/gep-5224/)描述了预路由过滤器，并引用了推理扩展的基于主体的路由器（Body-Based Router）作为示例。该路由器可以从请求体中提取模型名称用于路由，但团队需要兼容的实现和配置。他们应该用自己的模型、流量和硬件来衡量来自路由和调度选择的任何延迟或效率优势。

## **保护遥测数据并共享发布决策**

推理可观测性还有一个数据处理问题。Bogoevici警告说，提示词、响应和检索到的文档可能会出现在日志和跟踪中。他问道：“实际捕获了什么信息，它去哪儿了？”团队应该决定收集什么、在哪里存储、保留多长时间以及谁可以看到它。他强调了一个简单的观点：提示词就是数据。即使团队为了故障排查而收集敏感内容，它也需要保护。

Ramachandran看到随着AI智能体引入新的事件和访问记录，运维和安全可观测性正变得越来越紧密。他说，OpsRamp正准备从安全角度解释现有的遥测数据，而特定于智能体的活动可能需要额外的插桩。团队仍然需要设计和测试他们的安全控制和事件响应。

在发布之前，Ramachandran建议业务和IT利益相关者就服务应交付的价值达成一致，包括[与业务成果挂钩的合理的推理体量](https://developer.hpe.com/blog/tokenomics-understanding-the-economics-of-enterprise-ai/)。“必须有可衡量的商业价值，”他说。

> “目标不仅仅是繁忙的GPU，而是性能和资源使用与业务需求相一致的可靠AI服务。”

Subramanian直截了当地表达了签字认可的观点：“这不能由单个人决定。”平台管理员、机器学习和数据科学团队以及安全团队需要合作并为故障或攻击做好计划。添加相关的业务负责人，测试具有代表性的负载和故障案例，并记录决策背后的容量、质量、成本和恢复证据。

发布决策应基于以下证据：服务能够满足商定的用户和业务目标，并且负责团队知道在无法满足时该测量什么以及如何响应。发布后，继续将AI工作负载行为与基础设施条件进行比较，以便团队能够检测性能退化、跨层排查故障并随着需求变化调整容量。目标不仅仅是繁忙的GPU，而是性能和资源使用与业务需求相一致的可靠AI服务。