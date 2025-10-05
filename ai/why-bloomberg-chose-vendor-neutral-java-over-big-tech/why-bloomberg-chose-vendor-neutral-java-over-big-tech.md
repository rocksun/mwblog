<!--
title: 彭博为何弃用巨头技术，独选中立Java？
cover: https://cdn.thenewstack.io/media/2025/10/f118b2b8-bruno-aguirre-21vj-prosu4-unsplash.jpg
summary: 彭博社选择 Eclipse Temurin 标准化 Java 基础设施，原因在于其供应商中立、TCK 认证和长期支持，保障了可靠性。彭博社积极回馈社区，并建议其他组织根据自身需求选择，重视 LTS。
-->

彭博社选择 Eclipse Temurin 标准化 Java 基础设施，原因在于其供应商中立、TCK 认证和长期支持，保障了可靠性。彭博社积极回馈社区，并建议其他组织根据自身需求选择，重视 LTS。

> 译自：[Why Bloomberg Chose Vendor-Neutral Java Over Big Tech](https://thenewstack.io/why-bloomberg-chose-vendor-neutral-java-over-big-tech/)
> 
> 作者：Darryl K. Taft

2018 年，当彭博社决定将其 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 基础设施标准化时，该公司面临一个将影响 1,000 多名工程师以及全球最大规模的 [Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/)、[Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/) 和 [Solr](https://solr.apache.org/) 部署的决策。事关重大。作为全球投资和商业专业人士的金融基础设施提供商，可靠性不是可选项——而是强制性的。

该公司的选择——[Eclipse Temurin](https://adoptium.net/temurin)，来自 [Eclipse 基金会](https://www.eclipse.org/) [Adoptium 工作组](https://adoptium.net/)的 [OpenJDK](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) 发行版——为任何在日益复杂的开源采用环境中摸索的企业提供了宝贵的经验。

根据 Eclipse 的说法，Adoptium 工作组促进并支持在整个 Java 生态系统中使用的优质运行时和相关技术，通过 Eclipse Temurin 提供经过 Java 技术兼容性工具包 (TCK) 认证的 OpenJDK 构建版本。

## 供应商中立性的必要性

“我们正在寻找供应商中立的方案，”Bloomberg 首席技术官办公室的云计算、平台和安全架构负责人 Andrey Rybka 告诉 The New Stack。Rybka 自 1995 年以来一直从事 Java 相关工作，并领导 Bloomberg 的开源计划。

除了 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention)[的](https://openjdk.org/projects/jdk/25/)，还有“[IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention)、[Red Hat](https://developers.redhat.com/products/openjdk/overview)、[AWS](https://aws.amazon.com/?utm_content=inline+mention)[特有的发行版](https://www.theserverside.com/news/252452738/Amazon-Corretto-extends-OpenJDK-support)，[甚至微软](https://thenewstack.io/microsoft-openjdk-goes-ga-at-build/)现在也参与其中。选择多不胜数，”他说。

在单供应商开源项目主导的环境中，组织面临着实际的错位风险。“如果一个开源项目只是由一家公司主导的开源项目，你总会面临在某个时候与你想要做的事情，或者那家公司想要做的事情，可能出现错位的风险，”Rybka 说。

对于自称是“开源优先”公司的 Bloomberg 来说，由基金会治理提供的供应商中立性是不可谈判的。“如果它是一个供应商中立的实体，比如 Eclipse 基金会或我们参与的其他基金会，你就能更好地确保一致性和优先级，”他解释道。

Rybka 指出，虽然 Bloomberg 称自己为“开源优先”，但这不同于“仅限开源”。当有意义时，他们会使用商业软件，但当他们构建新事物时，他们会首先考虑开源选项。对于秉持这种理念的公司，中间有一个基金会——无论是 Eclipse、Apache、Linux 基金会还是其他——都能提供缓冲。“如果它是一个供应商中立的实体，你就能更好地确保一致性和优先级，”Rybka 说。

## 超越免费啤酒：真正的价值主张

该公司需要长期支持，以免被迫进行持续的风险更新；需要完整的 TCK 认证以确保兼容性；还需要与其特定硬件和操作系统要求相匹配的平台支持。TCK 是一个测试套件，它能证明你运行的是一个兼容的 Java 实现，而不是某人对规范的创造性解读。

Rybka 说，及时的安全补丁至关重要，获得 OSI 批准的、提供可预测条款的许可也同样重要。

除了这些技术要求，Bloomberg 还考虑了战略因素，包括供应商中立性和治理结构、[软件供应链安全](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/)能力、周边社区的活力以及在需要专业知识时获得商业支持的选择。

在一次声明中，Bloomberg 首席技术官办公室基础设施主管 Phil Vachon 强调了质量维度：“作为金融基础设施的供应商，我们寻求使用最高质量和稳定性的软件，因为我们的基础设施需要拥有我们提供给客户的同等可靠性和稳定性。”

Eclipse Temurin 满足了这些要求。该发行版的 TCK 认证、安全开发实践和透明的[软件物料清单 (SBOM)](https://thenwstack.io/sboms-are-great-for-supply-chain-security-but-buyers-beware/) 让 Bloomberg 有信心将该技术应用于内部系统和面向客户的产品。

此外，Eclipse 基金会的治理意味着没有一家公司可以独占该项目。

“组织正在寻求安全、高质量、开源和供应商中立的替代方案，而 Temurin 正是如此，”Eclipse 基金会执行董事 Mike Milinkovich 说。“通过最新版本，我们正在继续提供组织对商业产品所期望的质量和保障，同时也在引入新的方式，让社区能够支持并保持这一势头。”

## 安全维度

在金融服务领域，软件供应链安全至关重要。Bloomberg 维护着成熟的漏洞跟踪和补丁周期流程，并在其整个技术栈中生成和摄取 SBOM。

“软件供应链安全可能是最重要的事情，”Rybka 说。“[Log4Shell](https://thenewstack.io/log4shell-lives/) 是一个主要的警报，它揭示了这一点。但我们甚至在此之前就已经在做了。”

Daniel Scanteianu，Bloomberg 的一名软件工程师，担任公司 Java 和 [JVM（Java 虚拟机）](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/) 协会的联席主席，并为 Eclipse Adoptium 项目做出贡献，他指出了透明度因素。

他在一份声明中说：“提高软件组件和依赖项的透明度，使 Bloomberg 能够主动管理漏洞并减轻潜在风险。”

Eclipse 基金会的治理模式和 Temurin 对安全的关注与这些要求非常契合。“Temurin 在安全软件开发方面的工作以及其 JDK 通过 TCK 认证，让 Bloomberg 有信心信任 Temurin 的 OpenJDK 构建版本，”Scanteianu 说。

## 迁移的现实

Rybka 解释说，向 Temurin 的过渡并非易事。2018 年，Bloomberg 从其 [JDK 8](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/) 二进制文件切换，并将其 JVM 标准化为 Eclipse Temurin。鉴于 Java 在 Bloomberg 运营中的深度和广度整合，Rybka 称这种大部分手动进行的迁移是“一项巨大但值得的任务”。

然而，执行过程比预期更顺利。“从质量方面来看，它相当可靠，”Rybka 说。“我们没有看到太多的回归，即使我们报告了什么，也得到了及时处理。”

自动化和可观测性工具开箱即用。“[Eclipse Mission Control](https://projects.eclipse.org/projects/adoptium.mc)、用于堆分析的 [Memory Analyzer](https://projects.eclipse.org/projects/tools.mat)——如果你有任何问题，我们没有发现任何表明我们在这里遇到重大问题的情况，”他指出。

当你能准确地看到 Java 运行时中的内容，精确到依赖项级别时，你就能在漏洞造成危害之前采取措施。Temurin 的安全开发实践不仅仅是营销——它们与 Bloomberg 安全团队完成工作所需的一切相符。

然而，一个持续存在的挑战是：缺乏默认的商业支持。“默认情况下没有所谓的商业支持，”Rybka 说。“如果我与某个也支持特定开源产品的供应商有合作关系，那将是一种完美的结合。”Bloomberg 通过内部专业知识和选择性供应商关系相结合的方式来解决专业支持问题。

## 回馈社区：不仅仅是免费搭乘者

Bloomberg 的理念超越了单纯的消费。“我们不想仅仅是免费搭乘者。我们想回馈社区，”Rybka 强调。

该公司对 Adoptium 的贡献包括在 [VDR 生成器](https://github.com/adoptium/temurin-vdr-generator) 和 Temurin 构建工具方面的大量工作，Scanteianu 尤其参与了 Adoptium 工作组内的安全和供应链计划。一位 Bloomberg 工程师甚至在 [Python 指导委员会](https://github.com/python/steering-council)任职，同时团队还为 Chromium、[Kubernetes](https://thenewstack.io/kubernetes/)、Prometheus 和 Grafana 等众多其他项目做出贡献。

这种承诺源于理念和实用主义。“随着我们在这个特定项目或基金会中建立成熟的能力，将会遇到一些挑战，”Rybka 解释说。“当有贡献者能够帮助我们时，这会很有帮助。”

## 企业 Java 采用建议

根据 Bloomberg 的经验，Rybka 为评估 Java 发行版的组织提供了务实的指导。第一步是了解自身环境。

“我希望了解他们的生态系统和能力。我们有数千名工程师——对我们来说，这是正确的选择，”他说。“如果你全面采用 AWS，那么 AWS 发行版可能是更好的选择。这取决于你试图解决的具体问题。”

Rybka 建议创建一个决策矩阵，列出所有关键要求并相应地对每个供应商选项进行评分。[长期支持 (LTS)](https://thenewstack.io/java-25-oracle-makes-java-easier-to-learn-ready-for-ai-development/) 可能是一个必备项，平台兼容性是另一个重要因素，而云战略则是另一个考量。关键是根据你的具体需求匹配现有资源，而不是盲目追随行业趋势。

Rybka 还告诫不要寻找通用解决方案。

“我不认为应该只有一种发行版能够一统天下。我实际上很高兴这里有很多不错的选择，其中一些在特定领域非常合适，”他说。

不同的组织有不同的需求，选项的多样性反映了企业 Java 生态系统中用例的多样性。

Rybka 特别强调了长期支持的重要性。

“如果你的 JDK 没有 LTS，你就必须非常擅长更新，”他说。“每次更新都会带来一些风险，因为如果你在没有长期支持的情况下随意跳跃版本，可能会出现回归。”

## 展望未来：AI 与基金会的价值

Rybka 说，随着 Bloomberg 继续扩大其开源足迹——尤其是在 AI 领域，投资“增长极其强劲”——该公司坚持认为，即使在 AI 编码助手时代，基本的软件架构技能仍然至关重要。

“我认为这非常有前景，但我确实乐观地认为，优秀的软件工程是安全的，”Rybka 在谈到[氛围编程](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)和[AI 驱动的开发工具](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)时说。“良好的架构意识、良好的实践、软件开发生命周期实践——这些都不会消失。”

他表示，公司继续投资于中间件和数据库等“无聊堆栈”基础，同时探索包括[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 和[代理框架](https://thenewstack.io/ai-agents-unite-conference-reveals-next-gen-frameworks/)在内的前沿领域。 [Python](https://thenewstack.io/what-is-python/)、[JavaScript](https://thenewstack.io/introduction-to-javascript/)、Kubernetes 和[安全工具](https://thenewstack.io/the-security-tooling-faceoff-open-source-security-vs-commercial/)都在未来的计划中占据重要地位。

Bloomberg 的 Eclipse Temurin 决策是深思熟虑的企业开源采用的典范。

Vachon 说：“Temurin 对安全、及时构建的持续投入，让我们非常容易地将其作为我们首选的 JDK。”

确实，对 Rybka 而言，选择 Temurin 反映了 Bloomberg 更广泛的演进。“通过从消费到社区参与、项目贡献，再到如今成为开源领域的领导者这一整个过程，Bloomberg 可以确保 Temurin 继续作为免费、开源、企业级的 OpenJDK 平台，供我们内部使用以及更广泛的技术社区使用。”