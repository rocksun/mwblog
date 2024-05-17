# 平台工程大行其道：八大关键主题

![平台工程大行其道：八大关键主题的特色图片](https://cdn.thenewstack.io/media/2024/05/e9a49996-jonny-gios-ja2gxsfwyei-unsplash-1-1024x683.jpg)

[平台工程](https://thenewstack.io/platform-engineering/) 绝对已经起飞。事实上，平台工程是几个月前在巴黎举行的 KubeCon + CloudNativeCon Europe 2024 的热门话题。

有 60 场与平台工程相关的会议，几乎是关于 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 会议的两倍。毫不奇怪，我们发现“开发者”始终位列活动中最重要的 20 个主题之首，紧随其后的是数据和安全性。这很有道理，因为几乎任何关于平台工程的会议都会探讨如何让开发者安全地创建越来越智能的 [数据驱动型应用](https://thenewstack.io/the-rise-of-data-driven-apps-where-we-are-and-whats-next/)。

接下来是运维、集成和计算，这些主题在 [平台工程](https://thenewstack.io/platform-engineering/architecture-and-design-considerations-for-platform-engineering-teams/) 的背景下也至关重要，反映了支持整个 [软件开发生命周期](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) 所需的综合方法。这些主题强调了运营效率、工具和服务无缝集成以及计算资源有效管理的重要性。

这些主题共同突出了平台工程的多方面性质，旨在简化开发流程、增强安全措施并有效利用数据，同时确保运营顺利进行。对开发者、数据、安全性、运营、集成和计算的关注展示了平台工程在提高开发者生产力和以安全高效的方式促进复杂数据驱动型应用程序创建方面所采取的整体观点。

## KubeCon 上的平台工程：60 场会议、20 个主题和 8 个关键主题

KubeCon Europe 上的 60 场平台工程会议遵循八个关键主题，所有这些主题都专注于优化软件开发生命周期的不同方面。

## 通过内部开发者平台 (IDP) 提升开发者体验

平台工程中的一个关键主题是通过实施和优化 [内部开发者平台 (IDP)](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms/) 来改善开发者体验。构建多租户、与云无关的平台，重点在于平衡开发速度和系统可靠性，这一点至关重要。KubeCon 上的主题涵盖了广泛的真实客户案例，从嵌入安全和 [可观测性](https://thenewstack.io/observability/) 工具到展示在 [Kubernetes](https://thenewstack.io/kubernetes/) 生态系统中进行调试的实用方法。在公司合并中集成此类平台，强调了在统一的 IDP 中协调不同工程团队的文化和技术挑战。

这些讨论集中在培育内部平台的主题上，旨在抽象基础设施复杂性、强制执行最佳实践并允许开发者专注于高效交付高质量软件。此外，生成式 AI 有可能通过创建可定制的抽象来彻底改变平台工程，从而进一步减轻开发者的负担。

### 有趣的产品

#### GitPod 开源或云托管

我很高兴看到 [GitPod](https://thenewstack.io/the-goldilocks-cde-gitpod-fits-between-saas-and-self-hosted/) 作为 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 平台工程日的赞助商，因为我自底特律的 KubeCon 2022 以来就关注这个特定产品，并且非常喜欢他们的云开发环境如何提供类似桌面的开发者体验，而不会占用实际的开发者机器。我在 GitPod 上运行了几个基于 [Python](https://thenewstack.io/how-python-is-evolving/) 的 Streamlit 数据应用，发现不需要任何网络配置。我只需运行我的应用，GitPod 就会将 URL 交还给我。

我可以使用我喜欢的 IDE，
## Kubernetes 中的数据管理和有状态应用程序

随着平台工程的成熟，一个显着主题是在 Kubernetes 中配置和管理以数据为中心的负载。KubeCon Europe 上的演示和研讨会重点关注处理有状态应用程序的独特挑战和创新，重点介绍有意义的计算和存储分离、利用各种存储技术以及构建弹性平台的策略。强调了 Kubernetes 不断增长的能力，解决了以下主题：

- [NVMe](https://thenewstack.io/why-nvme-is-a-better-choice-for-your-data-center/) SSD 限制
- 自动卷调整
- 大规模处理各种分析数据库

该主题深入探讨了利用 Kubernetes 原生存储功能来构建可靠且可扩展的数据平台的实用性，使组织能够在云原生环境中充分利用其数据的潜力。

### 有趣的产品

#### Vitess 和 PlanetScale

[PlanetScale](https://thenewstack.io/planetscale-serves-up-vitess-powered-serverless-mysql/) 以分布式云原生数据库平台而著称，建立在 [Vitess](https://thenewstack.io/planetscale-serves-up-vitess-powered-serverless-mysql/) 和 [MySQL](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/) 的强大基础之上。该平台特别引人注目，因为它专注于以开发者为先的方法，促进了为全球分布式 [SQL 数据库](https://thenewstack.io/the-new-stack-context-sql-databases-in-a-cloud-native-world/) 创建应用程序，具有无缝的零停机迁移能力。这与简单且适应性强的 API 相结合，让人联想到 [NoSQL](https://thenewstack.io/why-choose-a-nosql-database-there-are-many-great-reasons/) 平台（如 [MongoDB](https://thenewstack.io/how-mongodbs-atlas-helped-amadeus-reengineer-a-crucial-app/））提供的便利性。Vitess 为 PlanetScale 提供了执行数据库部署或迁移（包括回滚选项）的能力，而不会造成停机或数据丢失，从而确保持续运行和数据完整性。

## Kubernetes 中的机器学习和生成式 AI

机器学习和生成式 AI 工作负载的快速增长带来了独特的可扩展性和运营挑战，尤其是在部署具有广泛计算需求的大型模型时。此主题揭示了 Kubernetes 如何与 [Ray](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/) 等框架一起，通过与硬件加速器的无缝集成来促进这些 AI 模型的有效服务。提供了对在 Kubernetes 环境中部署生成式 AI 模型的增强功能和成本效益策略的见解，为从业者提供了一条途径，可以向其平台注入更智能和更自动化的功能。

### 有趣的产品

#### Anyscale 的 Ray
## Ray：分布式计算框架

Ray 是一款分布式计算框架，旨在高效地跨集群扩展机器学习 (ML) 和人工智能 (AI) 工作负载，为从深度学习到强化学习、超参数调优和模型服务的广泛应用提供统一的解决方案。其核心价值主张在于能够毫不费力地以最小的工作量扩展复杂的工作负载，这要归功于其简单、灵活的 API，该 API 可与流行的 ML 库（如 PyTorch 和 TensorFlow）无缝集成。Ray 通过允许开发人员在细粒度级别（例如作业中各个任务或 actor 的 CPU 和 GPU 分配）指定计算资源需求来实现这一点，从而促进最佳资源利用和性能。Ray 获得了领先的 AI 团队和组织的信赖，解决了部署大规模、计算密集型 AI 模型的可扩展性、灵活性和效率挑战，使其成为现代 AI 驱动型应用程序的基石技术。

## Anyscale：Ray 的商业版本

Anyscale 提供了 Ray 的商业版本。Anyscale 为 Ray 提供托管云服务，该服务专为那些更喜欢托管服务的便利性和速度而不是自行管理集群和基础设施的组织而设计。此商业产品包括超出 Ray 开源版本提供的附加功能、支持和服务，以满足企业对 AI 和 Python 工作负载的生产化和扩展需求。Anyscale 作为 Ray 的主要商业支持者，旨在简化创建、运行和管理 Ray 工作负载的过程，让公司更容易在 AI 方面取得成功并从其 AI 计划中获得价值。

## 平台抽象和 AI 驱动的开发的进步

在迅速扩展的云原生技术领域，平台工程正逐渐集中于创建熟练的抽象和实施 AI 驱动的开发方法。KubeCon Europe 会议上关于不同级别的平台抽象的会议概述了平衡教育、功能开发和快速实施的重要性。这些抽象的演变证明了行业正在持续努力改进开发人员体验。

同时，使用生成式 AI 来提升平台工程——通过自动化创建更高级别的抽象和 API——进一步强化了简化构建和使用这些技术的复杂性的趋势。利用 LLM 生成代码并制作更直观、以人为中心的 API，使平台工程走上了有望大幅降低进入门槛、提高效率并定制适合组织需求的解决方案的轨道。

### 有趣的产品

#### GitHub Copilot 和 GPT-Engineer

GitHub Copilot 非常有效地提高了开发人员的生产力，因为它允许 OpenAI 的 GPT LLM “查看”所有项目代码的项目上下文。Copilot 与 Visual Studio Code 和我个人偏好的 IDE Pycharm 集成得很好。用户会注意到，AI 在 IDE 项目工作区中使用得越多，它就会持续改进，并且它可以更多地观察用户如何采用其代码建议。

除了 Copilot 之外，您还应该看看 GPT-Engineer。GPT-Engineer 基于 GPT-4，但它能够基于用户在项目目录中维护的简单提示文件创建完整、结构良好的应用程序。

#### Syntasso 的 Kratix

Kratix 本质上是内部开发人员平台的构建套件。它是一个开源框架，使平台工程师能够提供平台即服务 (PaaS) 解决方案。Kratix 专注于使平台工程师能够利用 Kubernetes 和其他云原生技术的力量来构建更好的平台。它允许创建“承诺”，这些承诺是在 Kubernetes 集群中为特定请求（例如环境创建）提供服务的配置。这些承诺可以自动化和简化各种非开发活动，使开发人员更容易请求和接收他们需要的资源，而无需平台团队直接干预。这种方法不仅通过减少手动服务各个请求的需要为平台工程师节省了时间，而且还通过提供更有效率的自助工作流来增强开发人员体验。Syntasso 提供了 Kratix 的企业版本，其中包括企业支持和咨询服务。

## 使用 eBPF 和 Cilium 的云原生网络和安全

云原生网络和安全的发展是一个中心主题，深入探讨
## eBPF 和 Cilium：Kubernetes 的网络、可观测性和安全解决方案

[eBPF（扩展伯克利数据包过滤器）](https://thenewstack.io/what-is-ebpf/) 和 [Cilium](https://thenewstack.io/cisco-gets-cilium-what-it-means-for-developers/) 是 Kubernetes 的网络、可观测性和安全解决方案。众多 KubeCon Europe 会议探讨了 eBPF 和 Cilium 如何改变容器和微服务通信和安全的方式，重点介绍了它们的扩展性、性能和灵活性。生产部署、技术深度剖析以及对 API 网关安全和加密等高级功能的讨论展示了 eBPF 和 Cilium 提供的全面功能。还重点介绍了向专家用户和维护人员学习的机会，强调了社区在该领域内知识共享和创新中的作用。

### 有趣的产品

#### Isovalent 的 Cilium Enterprise（已被 [思科](http://cisco.com/?utm_content=inline+mention) 收购）

虽然 Cilium 本身是一个开源项目，但 Isovalent 提供了 Cilium 的企业版，其中包括附加功能、支持和服务，供组织在生产环境中部署 Cilium。Cilium Enterprise 在 Cilium 开源版本中发现的核心 eBPF 驱动的网络、可观测性和安全功能中增加了以企业为重点的功能。

#### Falco

Falco 由 Sysdig 开发，现已成为 CNCF 的一部分，是一个云原生运行时安全项目。它使用 eBPF（和可选的内核模块）来监视 Linux 内核中的系统调用，以检测异常活动并在运行时发出威胁警报。Falco 可用于保护 Kubernetes 集群以及容器和云原生应用程序。

## Kubernetes 上的多租户和数据平台可扩展性

在 Kubernetes 上运行多个租户和广泛的数据应用程序时，确保可扩展性和资源效率是此主题的核心。会议深入探讨了管理多租户平台、底层存储注意事项和数据库操作的实际经验和创新方法。它们揭示了 Kubernetes 功能（如命名空间、存储编排和策略执行）在支持广泛的应用程序（包括 AI 密集型工作负载）中的重要性。通过案例研究和技术解释，与会者了解了多租户架构和利用 Kubernetes 应对数据密集型环境的策略。

### 有趣的产品：

#### Loft 的虚拟集群 (vClusters)

[VClusters](https://thenewstack.io/vcluster-to-the-rescue/) 提供了一种在单个物理集群内创建轻量级虚拟 Kubernetes 集群的方法。每个虚拟集群都有自己的 API 服务器、资源隔离、RBAC 和网络策略。这允许在租户之间进行强隔离。

Loft 现在提供 vCluster pro，提供企业级功能和支持，包括管理 UI、SSO、审计日志记录、跨集群 DNS 的 CoreDNS 集成以及在自己的专用 Kubernetes 集群中运行 vCluster 控制平面。

## 可观测性和性能工程

应用程序的仪器化和性能优化是此主题的核心方面。演讲者讨论了在 [OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) 中使用火焰图和分析来收集跨不同编程环境的性能见解。在开发生态系统中集成分析工具的经验展示了可观测性如何导致增强的应用程序调整和优化。了解不同堆栈的性能瓶颈以及从这些经验中获得的共同见解，强调了在云原生上下文中持续追求应用程序效率和可靠性。

### 有趣的产品

#### Grafana Cloud

[Grafana Cloud](https://thenewstack.io/grafana-extends-free-access-for-cloud-managed-observability/) 和 OpenTelemetry 无缝协作，提供完整的可观测性解决方案。

以下是它们集成的过程：

- **仪器化：**使用 OpenTelemetry 仪器化库从应用程序和基础设施生成指标、日志和跟踪。
- **数据收集：**使用 OpenTelemetry 收集器接收、处理和将遥测数据导出到 Grafana Cloud。或者，可以使用 Grafana Agent，它是一个针对 Grafana Cloud 优化的轻量级收集器。
- **数据存储和可视化：**Grafana Cloud 摄取并存储来自 OpenTelemetry 的遥测数据，提供了一个统一的平台，用于使用强大的 Grafana 仪表板可视化和分析指标、日志和跟踪。
- **应用程序可观测性：**Grafana Cloud 提供了一个专门的“应用程序可观测性”功能，该功能提供预构建的仪表板和工具，用于监视使用 OpenTelemetry 进行仪器化的应用程序，遵循 Prometheus 数据模型和语义约定。
## 通过 Grafana Cloud 和 OpenTelemetry 实现端到端的可观测性

通过将 Grafana Cloud 的托管可观测性平台与 OpenTelemetry 的供应商中立仪表和数据收集功能相结合，您可以在不管理和扩展底层组件的开销的情况下，为您的应用程序和基础设施实现端到端的可观测性。

## 电信中的云原生转型

随着电信公司应对 5G 技术不断增长的需求，采用云原生原则变得越来越关键。本主题涵盖了电信公司的云原生之旅，强调了服务提供商、供应商和更广泛的云原生社区之间的协作精神。演讲和小组讨论分享了沿途遇到的经验和挑战，提供了针对电信应用程序和基础设施的数字化转型的经验教训。整个生态系统中见解的分享成为动态电信领域内创新和适应的催化剂。

## 结语

KubeCon Europe 2024 标志着平台工程的一个重要里程碑，展示了它作为云原生生态系统内技术演进的最前沿。在 60 场会议中，平台工程因其在提升开发者体验中的核心作用而受到赞扬，重点是 IDP 的实施和优化。该活动突出了开发速度和系统可靠性之间的微妙平衡，支撑着平台工程的本质——创建工具链和工作流，最大化开发人员生产力，同时确保数据驱动应用程序的安全性和效率。

从使用 IDP 提升开发者体验，到在 Kubernetes 中管理以数据为中心的工作负载，再到利用 AI 进行平台抽象并使用 eBPF 和 Cilium 改善云原生网络，主题的多样性反映了支持软件开发生命周期所需的综合方法。这些讨论不仅提供了对平台工程当前状态的宝贵见解，还指出了未来的趋势，包括使用 [生成式 AI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 来减轻开发人员负担，以及平台抽象的持续演进，以满足日益复杂的云原生环境的需求。

当我们回顾 KubeCon Europe 2024 的主题时，很明显，平台工程不仅仅关乎工具和技术；它还关乎培养重视效率、安全性和创新的文化。该活动强调了平台工程在提高开发人员生产力和以安全有效的方式促进复杂的数据驱动应用程序创建方面所采取的整体观点。在平台工程的领导下， [云原生开发](https://thenewstack.io/cloud-native/) 的未来将迎来前所未有的增长和转型，使组织能够充分利用其技术投资的潜力。KubeCon Europe 2024 确实重申，在不断发展的云原生技术领域，平台工程至高无上。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。