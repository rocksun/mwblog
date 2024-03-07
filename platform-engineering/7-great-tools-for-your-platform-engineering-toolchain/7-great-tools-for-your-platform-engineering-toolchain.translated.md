# 平台工程工具链的 7 款优秀工具

![平台工程工具链的 7 款优秀工具的特色图片](https://cdn.thenewstack.io/media/2024/03/294350e8-platform-engineering-tools-1024x576.jpg)

平台工程，即为软件开发构建和管理内部开发者平台的做法，正在迅速流行起来。它的承诺是什么？无缝集成并优化传统的开发和 DevOps 方法，解决其关键差距。

然而，[平台工程](https://thenewstack.io/platform-engineering/) 的兴起导致了一系列工具集的爆炸式增长，每个工具集都声称可以解决你组织的所有问题。遗憾的是，只有少数工具能够兑现这一炒作。仔细了解一下这七款确实有用的平台工程工具。

## 平台工程师的七款工具

以下是一些促进平台工程无缝采用的工具。

### 1. OPA 和 Rönd

[开放策略代理](https://www.openpolicyagent.org/) (OPA) 是一款开源通用策略引擎，旨在简化和统一跨不同软件和系统的安全策略管理。OPA 让你能够以代码的形式声明性和强制执行策略，利用高级语言 [Rego](https://thenewstack.io/5-things-you-didnt-know-about-open-policy-agent/) 的表达能力。

此策略引擎为以下解决方案提供支持，例如 [Rönd](https://rond-authz.io/docs/)，这是一个轻量级开源 Kubernetes 容器，[开发](https://mia-platform.eu/blog/rond-open-source-api-enforcement/) 用于通过简单的安全策略保护你的 API。

通过利用 OPA 作为验证授权规则的安全引擎，以及利用 Rego 编写安全策略，Rönd 超越了其作为授权机制的角色。它让你能够构建强大且灵活的 [基于角色的访问控制](https://mia-platform.eu/blog/role-based-access-control-rbac/) (RBAC) 或 [基于属性的访问控制](https://thenewstack.io/5-application-authorization-best-practices-for-better-cybersecurity/) (ABAC) 解决方案，方法是提供其基本构建模块：角色、权限和用户组。

通过弥合策略定义和执行之间的差距，OPA 和 Rönd 简化了安全管理，并增强了应用程序的整体安全态势。

然而，保护应用程序不仅仅是定义谁可以访问什么；它还涉及保护解锁该访问权限的密钥和凭据。输入 Hashicorp Vault。

### 2. HashiCorp Vault

在过去几十年中，不同规模的网络攻击给大型企业造成了数百万美元的损失。持续不断的违规行为证明了对强大数据安全性的不可否认的需求。

组织传统上使用密码、加密密钥和证书来控制对敏感信息的访问。然而，这些“凭据”通常没有一个中心位置，而是分散在各个系统中。这使得跟踪谁可以访问什么变得具有挑战性，通常会使敏感数据容易受到攻击。

这就是 [HashiCorp Vault](https://thenewstack.io/how-hcp-vault-secrets-radar-fight-sprawl-of-corporate-secrets/) 的用武之地。它是一个基于身份的秘密和加密管理系统，旨在简化安全地存储、生成、加密和传输秘密。Vault 使用身份验证和授权，帮助确保只有经过授权的个人才能访问他们有权访问的信息。

Vault 在一个集中式平台中安全地存储和管理各种秘密，包括密码、API 密钥、SSH 密钥、RSA 令牌和一次性密码 (OTP)。Vault 的另一个关键功能是动态秘密——短寿命、自动续订的凭据，可最大程度地减少暴露。

Vault 还支持各种身份验证方法，如令牌、轻量级目录访问协议 (LDAP) 和多因素身份验证 (MFA)，提供灵活且适应性强的安全框架。它的加密功能不仅限于存储，还促进了数据在传输和静止状态下的加密。

访问控制和秘密管理固然重要，但还不够。为了真正安心，持续监控至关重要。这意味着实时深入了解你的安全基础设施的运行状况和性能，让你能够在潜在问题成为问题之前识别并解决它们。这将我们带到了经典的监控和可视化二人组 Prometheus 和 Grafana。

### 3. Prometheus 和 Grafana

[Prometheus](https://prometheus.io/) 擅长从各种目标（例如应用程序、服务器和云服务）收集实时数据。这些目标通过专用的 /metrics 路径公开关键指标，允许 Prometheus 评估系统运行状况和性能。

但收集数据只是第一步。
**Grafana** ([https://grafana.com/](https://grafana.com/))，可视化专家，将 Prometheus 存储的复杂指标转化为可操作的见解。Grafana 赋能团队构建交互式仪表盘，将原始数字转化为易于理解的可视化内容，揭示趋势和潜在问题。

共同，
**Grafana 和 Prometheus** ([https://thenewstack.io/grafana-wants-to-help-you-avoid-getting-dinged-by-kubernetes-costs/](https://thenewstack.io/grafana-wants-to-help-you-avoid-getting-dinged-by-kubernetes-costs/)) 组成一个强大的团队。Prometheus 收集并存储实时指标，而 Grafana 以清晰且有见解的方式呈现这些指标。这种协作使团队能够快速识别性能问题、跟踪趋势并保持最佳系统运行状况和资源利用效率。这带来了下一个节省成本且环保的工具：kube-green。

### 4. kube-green

**kube-green** ([https://kube-green.dev/](https://kube-green.dev/)) 是一个开源运营商，旨在减少 Kubernetes 集群的 [环境影响](https://thenewstack.io/sos-sustainable-open-source/) 和成本。此 Kubernetes 附加组件会自动关闭未使用的资源，最大程度地减少能耗和碳排放。这种“绿色”方法与科技行业日益增长的可持续发展工作相一致。kube-green 由 Mia-Platform 的 Davide Bianchi 开发，是 [CNCF](https://cncf.io/?utm_content=inline-mention) [Landscape](https://landscape.cncf.io/?selected=kube-green&item=orchestration-management--scheduling-orchestration--kube-green) 的一部分。

除了其环境效益之外，kube-green 还可以帮助您省钱。许多云提供商使用即用即付的付款模式，因此通过智能关闭未使用的资源，kube-green 可以显著降低您的云账单。

[采用者报告节省了 30% 至 40%](https://kube-green.dev/docs/adopters/)，巩固了 kube-green 作为资源使用、能耗和财务资源的强大优化器的声誉。

kube-green 专为与 [Kubernetes](https://thenewstack.io/kubernetes/) 无缝协作而构建，Kubernetes 是 [最流行的](https://cloud.google.com/discover/what-is-container-orchestration) 容器编排平台之一。这使得与流行的工作流和 CI/CD 管道平滑集成成为可能，从而无需中断当前设置即可轻松获得其好处。

### 5. Git 提供商

如果您曾经接触过软件开发，那么您几乎肯定会遇到 **git** ([https://thenewstack.io/tutorial-git-for-absolutely-everyone/](https://thenewstack.io/tutorial-git-for-absolutely-everyone/))，流行的分布式版本控制系统，及其众多提供商。从本质上讲，这些平台托管您的 git 存储库，使团队能够有效地协作和管理软件项目。

但 git 提供商提供的不仅仅是协作和版本控制。它们已成为现代软件工程中不可或缺的工具，拥有简化开发和提高质量的功能。

例如，
**GitHub** ([https://github.com/](https://github.com/)) 利用其内置的 CI/CD 解决方案 GitHub Actions，来自动化代码构建、测试和部署，从而在加快开发过程的同时确保质量。同样，**GitLab** ([https://about.gitlab.com/?utm_content=inline-mention](https://about.gitlab.com/?utm_content=inline-mention)) 也提供 CI/CD 管道以及问题跟踪、项目管理和访问控制，从而在平台内实现全面的项目管理。

除了这些巨头之外，其他提供商还带来了独特的优势。与 Jira 紧密集成，
**Bitbucket** ([https://bitbucket.org/product](https://bitbucket.org/product)) 便于无缝的项目管理和问题跟踪，特别是对于 Atlassian 生态系统中的团队。**GitKraken** ([https://www.gitkraken.com/](https://www.gitkraken.com/)) 和 **SourceTree** ([https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/)) 专注于用户友好的图形界面，使不太熟悉命令行的开发人员更容易进行版本控制。

Git 提供商简化了整个开发和交付过程。它们通过高效的协作工作流，使团队能够采用敏捷实践，加速交付并通过高效的协作工作流维护高质量代码。但是，当您将代码更改手动部署到越来越多的 Kubernetes 集群时，会出现一个新的挑战：在它们之间保持一致性。这就是 Argo CD 介入以在您的集群之间维持无缝和谐的地方。

### 6. Argo CD

**Argo CD** ([https://argo-cd.readthedocs.io/](https://argo-cd.readthedocs.io/)) 是 Kubernetes 的开源声明式 GitOps 持续交付工具。它通过使用 git 作为应用程序配置的单一真实来源，简化了在 Kubernetes 集群中部署、扩展和更新应用程序的自动化。应用程序的所需状态在 git 存储库中指定。

Argo CD 使用此存储库将应用程序的实际状态与存储库中声明的所需状态进行协调。通过 Argo CD 确保一致且及时的 Kubernetes 部署，链中的下一个工具使开发人员能够在内部开发人员平台提供的稳定性和自动化之上进行构建。

### 7. Mia-Platform
## Mia 平台

Mia 平台使组织能够构建和管理其内部开发者平台 (IDP)。IDP 是通过抽象底层基础设施的上下文和复杂性来加速开发过程的工具、服务和流程。这种抽象减少了负责交付产品的开发人员的[认知负荷](https://mia-platform.eu/blog/platform-engineering-reduces-cognitive-load/)，最终改善了[开发者体验](https://mia-platform.eu/blog/advancing-developer-experience/)。

Mia 平台还通过提供一个包含即用型组件的软件目录来支持可组合开发，例如 [支付集成中心](https://mia-fintech.io/blog/payment-integration-hub-unlock-digital-payments/) 和 [Mia 平台快速数据](https://mia-platform.eu/platform/fast-data/)。该目录使开发人员能够快速组装功能齐全的应用程序，而无需“重复造轮子”。

## 平台工程工具链的注意事项

虽然这些工具对于任何希望采用平台工程的组织来说都是一个很好的起点，但没有一刀切的工具链或解决方案。为了做出明智的决策并选择符合您的要求和目标的工具，请考虑一些关键因素，以确保无缝集成和最大影响：

**安全性：**安全性在平台工程工具中是必不可少的，尤其是在处理敏感数据时。一些第三方解决方案就像“黑匣子”——您看不到其内部安全功能，因此您不知道它们如何工作。为了安全起见，请研究并选择优先考虑强大安全性的工具来保护您的数据。寻找具有强大加密、漏洞扫描和安全访问控制等功能的工具链。

**兼容性：**选择与您现有的系统和基础设施无缝集成的工具，以避免麻烦。不兼容的工具可能会创建孤立的信息孤岛并中断工作流，从而导致开发和部署延迟。为了增强兼容性，请选择在不同环境中拥有良好记录的广泛使用的工具。

**供应商锁定：**尽可能采用开源工具，以避免供应商锁定。这减少了对特定供应商的依赖，并允许您在业务逻辑和需求发生变化时自定义和调整您的平台。如果您必须选择闭源工具，请避免将您困在专有生态系统中的工具；为冗余和风险管理维护多个供应商选项。

**可扩展性：**选择专为可扩展性而设计的工具，以有效管理您当前和未来的需求，因为您的用户群和数据量会不断扩大。此外，确保工具的定价模型允许资源优化，以便增加使用量不会造成意外的财务负担。

**可扩展性：**支持高效可扩展性的另一个特性是可扩展性。选择允许您根据团队需求无缝集成新工具和服务的工具。

## 平台工程的未来

平台工程改变了组织构建和交付软件的方式。它不仅仅关乎速度和安全性；它还关乎让开发人员用更少的资源做更多的事情。

曾经的战略投资已成为软件开发的根本性转变，为敏捷和创新的未来铺平了道路。

平台工程的格局远非一成不变。虽然这些工具为革命性的变革铺平了道路，但未来还有更大的可能性。您可以期待通过人工智能加深自动化和智能化，使平台能够独立学习和适应。此外，使用 [无代码工具](https://thenewstack.io/low-code-vs-no-code/) 构建平台的民主化即将到来，使所有技能水平的开发人员都能为平台的演进做出贡献。这一未来为软件开发带来了更高的效率、敏捷性和创新。

尽管平台工程的未来充满潜力，但务实地对待它很重要。仔细评估您团队的具体需求，并选择直接满足这些需求的工具。通过采用灵活且面向解决方案的思维方式，您可以自信地利用平台工程。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、采访、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)