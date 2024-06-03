
<!--
title: Cluster.dev：扩展SaaS部署选项
cover: https://cdn.thenewstack.io/media/2024/05/a4836188-chincherinchee-seeds-7674154_1280.jpg
-->

数据安全和合规性方面的担忧迫使某些客户探索 SaaS 实施的替代方式。

> 译自 [Cluster.dev: Expanding the Options for SaaS Deployment](https://thenewstack.io/cluster-dev-expanding-the-options-for-saas-deployment/)，作者 Volodymyr Tsap。


随着企业 [软件即服务](https://thenewstack.io/how-saas-based-global-server-load-balancing-eases-it-burden/) ( [SaaS](https://thenewstack.io/private-saas-is-coming-are-you-ready/)) 客户数量的增长，B2B 供应商面临着将他们的软件与高企业标准相匹配的挑战。然而，对于某些行业而言，基于云的 SaaS 的多租户性质使其由于安全、合规性和性能原因而成为不可行的选择。在本文中，我们将探讨实施 SaaS 架构的各种场景，重点关注部署到客户管理的环境作为企业级客户的替代方案。

## 澄清 SaaS 租户的概念

在开始之前，让我们简要回顾一下 SaaS 或软件即服务一词的含义：它是一种软件分发模式，授予 [用户基于订阅访问基于云的产品](https://thenewstack.io/adding-too-many-features-will-break-your-product-users-and-team/)、工具或服务。

下面，我们将探讨 [在云](https://thenewstack.io/3-key-factors-for-future-proofing-saas-cloud-platforms/) 环境中实施 SaaS 的不同场景。

## 多租户 SaaS

多租户是一个经常与 SaaS 相关的概念，因为传统的 SaaS 模型意味着多个客户端将利用特定的基础设施资源。但是，资源共享的程度可能会根据 SaaS 架构而有所不同：它们可能在给定的实现中共享或不共享，如下面的示例所示。

案例 1 说明了 SaaS 服务消耗的经典模型。

![](https://cdn.thenewstack.io/media/2024/05/88cb39c2-saas1.png)

*场景 1：所有资源共享的 SaaS 架构*

在此场景中，所有客户端都部署在提供商的云帐户中，他们在其中共享所有资源：SaaS 应用程序、计算能力和数据库。

场景二描绘了一个具有部分资源共享的实现模型。

![](https://cdn.thenewstack.io/media/2024/05/cf23a927-saas2.png)

*场景 2：具有部分资源共享的 SaaS 架构*

如图所示，客户共享 SaaS 应用程序/计算资源，但为每个用户部署了专用数据库。虽然从客户的角度来看，此环境可以被视为多租户，但从技术上讲，它的一部分是多租户，而另一部分不是。

这两个示例都可以归类为多租户，因为它们包含资源共享，尽管有一些差异。

**多租户 SaaS 的优点**

- 高效的资源使用和分配。使用负载均衡器可确保将可用的基础设施资源分配给处理更重工作负载。
- 更快的扩展，因为客户端使用相同的软件和硬件。
- 价格实惠，因为环境的成本在多个客户之间共享。
- 自动化维护作为 SaaS 订阅的一部分。
- 完善的入职流程保证新客户轻松上手。

**多租户 SaaS 的缺点**

- 受限的定制选项，因为所有客户共享相同的操作条件和通用流程。
- 数据安全问题，因为损害一个客户的安全可能会给其他客户带来风险。
- 可能的性能问题，因为一个客户的停机时间或峰值负载会影响邻居服务的可用性。
- 由于定期软件升级和数据库维护而导致的停机时间。

## 单租户 SaaS

单租户 SaaS 意味着 SaaS 客户端是租户的架构。在单租户环境中，客户端部署有一组专用资源，他们对此拥有独占权。由于单租户模型中的产品无法共享，因此租户可以根据自己的需要自由定制 SaaS 软件。

下图描绘了一个具有每个租户专用堆栈的单租户 SaaS 环境。

![](https://cdn.thenewstack.io/media/2024/05/719019e8-saas3.png)

*场景 3：每个租户堆栈的 SaaS 环境*

**单租户 SaaS 的优点**

- 增强安全性，因为每个客户的数据都是隔离的并存储在专用服务器上。
- 灵活的定制选项允许配置 [围绕具体业务需求的基础设施](https://thenewstack.io/how-iac-meets-the-differing-infrastructure-needs-of-dev-and-ops/)。
- 在对客户方便的时间窗口中进行单独的软件升级。
- 由于独占资源使用而实现可靠的操作。

**单租户 SaaS 的缺点**

- 价格昂贵，因为每个客户都需要单独的实例。此外，额外的修改需要更多的时间和资源，从而导致更高的成本。
- 可扩展性有限，因为扩展资源需要手动配置。
- 由于需要维护具有自定义配置的多个实例而导致维护复杂。
- 入职速度较慢，因为 SaaS 提供商需要时间来根据每个客户的需求配置基础设施。

## 在客户端运行 SaaS

在之前的示例中，多租户和单租户[基础设施均部署在提供商云](https://thenewstack.io/3-tips-to-secure-your-cloud-infrastructure-and-workloads/)帐户中，这使得某些流程对所有客户端都是通用的。场景 3 图表显示，尽管部署在隔离的基础设施中，但租户仍然被集体管理和操作，共享部署、监控和入职流程。此外，如果发布了新的 SaaS 软件版本，提供商会同时为所有租户进行升级。

这些示例表明，无论其架构如何，所有 SaaS 环境在某种程度上都包含某种形式的多租户。因此，客户出于数据安全和隐私方面的考虑，仍然更喜欢在自己的环境中安装软件，这不足为奇。

在这种情况下，内部部署安装似乎是最佳选择，它授予客户对资源、服务和数据的完全控制权。然而，内部系统存在一些挑战，例如采购和维护硬件和软件、聘用具有传统 IT 技能的员工进行管理以及可扩展性选项有限，这可能会使其对于动态且快速增长的企业非常低效。此外，许多

[安全工具和架构都是为云环境量身定制的](https://thenewstack.io/the-role-of-context-in-securing-cloud-environments/)，这可能会影响其内部性能。

解决方案是将软件安装到客户管理的环境中，并在公司的云帐户中运行 SaaS 的副本实例。

[Replicated 进行的研究](https://www.replicated.com/state-of-the-industry-for-software-distribution-download-the-report) 证明了此选项在客户中非常受欢迎：79% 的受访者由于需求旺盛而增加了其“客户管理环境”软件业务，而 56% 的受访者报告称每月有超过 10 个新的客户安装。

这种方法的一个主要优点是它提供了更高的安全性和控制力。

让我们仔细看看此实施模型。

## 全面控制

在具有专用资源的 SaaS 模型中，客户支付许可证费用，但无权访问包含代码的容器。事实上，客户无法控制 SaaS 应用程序运行的环境。

相反，将 SaaS 副本部署到[云帐户使客户能够完全控制](https://thenewstack.io/cloud-control-planes-for-all-implement-internal-platforms-with-crossplane/)系统。这授予对 SaaS 代码和底层运行时环境的访问权限。通过完全访问服务器基础设施，客户可以分配资源、选择实例类型、自定义扩展，甚至可以将 SaaS 应用程序迁移到另一个数据中心——这些选项在传统 SaaS 模型中是不可能的。

## 安全

在[专用基础设施中运行 SaaS 提供高级安全](https://thenewstack.io/top-6-saas-security-threats-for-2023/)功能，例如专用服务器和实施专有安全工具的自由。但将 SaaS 部署到[云帐户更进一步，授予客户](https://thenewstack.io/what-tools-a-swedish-it-provider-relies-on-for-its-customers-cloud-native-journey/)访问 SaaS 文件系统的权限。这使得能够跨越所有安全态势层（包括容器映像）进行漏洞扫描，以确保安全部署，而不会出现错误配置。

此外，由于您的 IT 人员对资源、服务和数据拥有完全控制权，因此您可以决定谁可以在什么条件下访问它们。

## 安装到客户云帐户

此方案的一个缺点是安装过程复杂，并且需要在初始步骤和未来升级中为客户提供支持。根据 Replicated 调查，复杂安装是 SaaS 软件在客户环境中设置和配置可能需要长达 14 天的主要原因之一。为客户简化此流程的承诺促使 SaaS 供应商为其软件开发自定义云安装程序，而 [Cluster.dev](https://docs.cluster.dev/) 可以提供帮助。

Cluster.dev 开源框架旨在解决 SaaS 公司为客户管理的环境构建软件的挑战。它能够将软件代码与预配置的基础设施捆绑到一个安装包中，从而可以为 SaaS 软件创建一键式云安装程序。这种安装允许客户在没有专门技能或知识的情况下无缝启动产品。该脚本通过采用模板化和将最佳实践编入部署和第 2 天操作中，促进了在任何云平台或内部部署上的安装。

![](https://cdn.thenewstack.io/media/2024/05/33681391-saas4.png)

*Cluster.dev 安装程序图*

## 供应商核心价值

- 启用客户自助服务
- 减少向客户交付软件时的故障
- 简化用户采用和操作产品的流程
- 与为云安装建立的最佳实践保持一致
- 使分发和版本升级变得容易
- 可以与云托管服务集成

## 结论

对数据安全性和合规性的担忧迫使某些客户探索 SaaS 实施的替代方式。虽然对于企业客户而言，直接将 SaaS 部署到云帐户的选项从安全性和控制性的角度来看似乎很有吸引力，但复杂的安装和通过升级为客户提供支持的必要性可能会阻碍 SaaS 供应商的这一进程。

[Cluster.dev](https://cluster.dev/) 通过为其 SaaS 启用单命令云安装程序，为公司提供更好的软件部署选项，确保新客户轻松上手。*SHALB 的技术撰稿人 Anastasiya Kulyk 是本文的合著者。*
