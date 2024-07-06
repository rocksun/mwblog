
<!--
title: 使用Dapr开源实现分布式应用程序的零信任安全
cover: https://cdn.thenewstack.io/media/2024/07/48bba3af-pizza-7241179_1280.jpg
-->

Dapr 通过为所有应用程序分配应用程序标识，并确保默认情况下为所有服务间和基础设施通信启用 mTLS，从而改善了分布式系统的零信任安全态势。

> 译自 [Zero Trust Security for Distributed Applications with Dapr Open Source](https://thenewstack.io/zero-trust-security-for-distributed-applications-with-dapr-open-source/)，作者 Alice Gibbons。

随着对更强保护的需求不断增长，软件开发中的安全标准也在不断提高。本文将探讨开源项目 [Dapr，分布式应用程序运行时](https://dapr.io/)，该项目包含丰富的安全功能集，允许开发人员在开发过程中将安全“左移”，并将行业标准最佳实践嵌入到他们的应用程序中。Dapr 提供了一组 API 来解决围绕状态管理、工作流和数据的常见分布式系统挑战。

## 什么是零信任安全？

[美国国防部零信任参考架构](https://dodcio.defense.gov/Portals/0/Documents/Library/(U)ZT_RA_v2.0(U)_Sep22.pdf) 对其定义如下：

>*“任何在安全边界内或外运行的参与者、系统、网络或服务都不值得信任。*
> 
>*相反，我们必须验证尝试建立访问权限的任何事物。这是一种关于我们如何保护基础设施、网络和数据的哲学的巨大范式转变，从在边界处进行一次验证转变为对每个用户、设备、应用程序和交易进行持续验证。”*

![](https://cdn.thenewstack.io/media/2024/07/7c83b94c-daprzerotrustsec1.png)

*边界安全与 [零信任安全](https://thenewstack.io/what-is-zero-trust-security/) [[KubeCrash](https://www.kubecrash.io/download/zero-trust-ebook)]*

零信任安全建立了这样一种原则，即系统内部没有任何东西可以自动信任，并且必须在每次系统交互过程中反复证明信任。这确保即使攻击者设法突破了系统的网络边界，他们也无法造成重大损害（如果有的话）。这种安全理念的转变是对日益复杂的网络威胁以及软件开发中对更强大安全措施的需求的回应。

零信任安全模型的概念已经存在 [自 1990 年代初。](https://en.wikipedia.org/wiki/Zero_trust_security_model) 然而，它不再仅仅是一个流行语。它已经发展成为软件开发中的安全标准。事实上，Gartner 预测，到 2025 年，[60% 的公司将采用零信任解决方案来替代虚拟专用网络](https://www.gartner.com/en/newsroom/press-releases/2023-01-23-gartner-predicts-10-percent-of-large-enterprises-will-have-a-mature-and-measurable-zero-trust-program-in-place-by-2026) 作为他们的安全边界。

## 开发人员视角

这些安全模型通常是在基础设施和网络级别考虑的，但零信任安全和架构的许多部分正在成为开发人员的关注点。这部分原因是分布式系统的流行度不断上升，因为应用程序需要更频繁地在网络之间、彼此之间以及与底层基础设施之间进行通信，从而导致可作为攻击目标的通信通道数量增加。编写这些应用程序的开发人员和工程团队必须将安全问题“左移”，以便在软件开发生命周期的早期强制执行安全最佳实践。

为了说明这一点，让我们以一个 [示例应用程序](https://github.com/diagrid-labs/dapr-zero-trust) 为例，我们将其称为 Pizza Store 系统。这种标准的事件驱动架构具有多个服务，它们同步和异步地进行通信，并依赖于各种基础设施提供商，例如状态存储和消息代理。Pizza Store 服务负责接收用户订单并调用厨房和配送服务以完成烹饪和配送任务。

从传统的边界安全模型来看，信任边界存在于系统网络之外，通常通过 API 网关或反向代理实现单个入口点。入口点通常是安全验证点，所有通信都在系统应用程序和基础设施服务之间流动。

![具有边界安全模型的 Pizza Store 系统。](https://cdn.thenewstack.io/media/2024/07/a19c149b-daprzerotrustsec2.png)

*具有边界安全模型的 Pizza Store 系统*

考虑到零信任安全范式，您不再信任内部系统网络，并且应用程序必须充当安全边界。根据设计，应用程序外部的所有通信，无论是来自应用程序到其他应用程序、基础设施服务还是最终用户，都需要进行验证。除了开发人员已经处理的围绕规模、弹性和性能的应用程序期望不断增加之外，这还带来了许多需要考虑的问题。这些问题包括：
- 为应用程序建立具有相同生命周期的身份。
- 遵循最小权限原则访问基础设施。
- 安全地调用第三方系统。
- 服务和基础设施之间的加密。
- 通过网关将 API 公开给前端。

![](https://cdn.thenewstack.io/media/2024/07/f326d5af-daprzerotrustsec3.png)

*开发人员对零信任安全模型中披萨店系统的担忧*

## Dapr 安全特性

[Dapr，分布式应用程序运行时](https://dapr.io/)，是一组分布式系统 API，在应用程序级别具有内置的安全特性。超过 10 个 API 可以通过 gRPC 或 HTTP 从任何编程语言使用，以实现常见的分布式系统挑战并规范微服务最佳实践。Dapr 还处理微服务所需的几个跨领域问题，包括分布式跟踪、弹性和安全方面的功能。

现在，我们将深入探讨 Dapr 的安全特性，这些特性可以帮助开发人员构建零信任分布式应用程序。

## Dapr 应用程序身份
由于我们不再信任网络，并且应用程序需要充当安全边界，因此我们需要一个内在的应用程序身份来在服务周围建立一个新的信任边界。

这就是 Dapr 应用程序身份 (App ID) 的概念。Dapr App ID 是：

- 使用 [SPIFFE ID](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/%23spiffe-id) 的强认证加密身份。
- 全局唯一，其密钥与应用程序的生命周期保持一致。
- 用于授权连接到其他应用程序。
- 分层策略可以启用应用程序和基础设施访问。

![](https://cdn.thenewstack.io/media/2024/07/9a774759-daprzerotrustsec4.png)

*包含应用程序和 Dapr 进程（边车）的 Dapr 安全边界*

在 Kubernetes 上，此过程由所有 Dapr 边车和控制平面服务完成，这些服务拥有一个包含服务 App ID 的唯一 X.509 证书，表示为格式为 *spiffe://<trustdomain>/ns/<namespace>/<appid>* 的 [SPIFFE](https://spiffe.io/) 身份。应用程序使用此证书通过双向 TLS (mTLS) 向其他 Dapr 应用程序证明其身份，这是一个称为非对称加密的过程。虽然工作负载可能共享相同的身份，例如当同一控制平面服务或应用程序的多个副本正在运行时，但每个副本使用一个唯一的、本地生成的私钥来支持其证书，该私钥会定期轮换，并且永远不会离开进程内存。每个服务都从 Sentry 服务请求其身份证书，Sentry 服务负责从共享证书颁发机构 (CA) 或“信任锚”颁发证书。公共 CA 在所有 Dapr 应用程序之间共享，以便它们可以验证对等身份。Sentry 通过验证客户端提交的 [Kubernetes 绑定服务帐户令牌](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/%23bound-service-account-tokens) 并交叉引用请求 Pod 的 App ID 注释来对应用程序身份进行加密认证。Dapr 的工作负载身份信任根，或“[底部乌龟](https://spiffe.io/book/)”，是 Kubernetes 平台，Pod 可以被视为应用程序的安全边界。

## 零信任应用程序调用
创建 App ID 后，可以应用跨应用程序调用的策略。这些策略的细节可能有所不同，从包含允许调用被调用应用程序的应用程序的简单访问控制列表，到指定被调用应用程序可以调用的操作、HTTP 动词和路径。当 Dapr Sentry 服务检查策略时，调用应用程序的信任域、命名空间和 App ID 值将从调用应用程序的 TLS 证书中的 SPIFFE ID 中提取。然后，这些值将与被调用应用程序的策略规范中指定的信任域、命名空间和 App ID 值进行匹配。如果所有三个值都匹配，则允许调用应用程序在指定的路由和操作处调用被调用应用程序。Dapr 还具有 [信任域](https://docs.dapr.io/operations/configuration/invoke-allowlist/) 的概念，该概念创建信任关系的逻辑分组，并允许比命名空间更低级别的信任组。

让我们看一个使用披萨店系统的具体示例。在这种情况下，披萨店服务需要直接调用厨房服务上的 */prepare* 方法，以告知厨房准备披萨。这些应用程序中的每一个都自动从 Dapr 获取 App ID，并且通信默认使用 mTLS 进行加密。

![](https://cdn.thenewstack.io/media/2024/07/81ec480b-daprzerotrustsec5.png)

*披萨店服务遵循零信任原则调用厨房服务*

默认情况下，任何应用程序都可以调用不遵守零信任原则的任何其他应用程序。为了缓解这种情况，您需要添加一个 Dapr 配置访问控制策略，该策略强制执行最小特权原则，从而仅允许披萨店服务调用厨房服务上的 */prepare* 方法。服务调用策略始终应用于被调用应用程序，并在运行时加载到关联的 Dapr 侧车中。

![](https://cdn.thenewstack.io/media/2024/07/715eb064-daprzerotrustsec6.png)

*厨房服务的 Dapr 配置访问控制策略*

此 Dapr 配置访问控制策略确保没有其他应用程序可以调用厨房服务应用程序，即使披萨店服务也只能使用 PUT HTTP 动词在 */prepare* 方法上调用厨房服务应用程序。

还可以添加其他安全功能，包括在 Dapr API 上强制执行 [API 令牌身份验证](https://docs.dapr.io/operations/security/api-token/) 的能力。当 Dapr API 通过代理暴露在系统外部或由前端应用程序使用时，这很有用。为了进一步锁定 Dapr API，您可以 [选择性地启用 Dapr API](https://docs.dapr.io/operations/configuration/api-allowlist/)，这些 API 可以由 Dapr 侧车调用。这确保了应用程序和侧车只能访问所需的最小基础设施资源集，并进一步减少了攻击面。

## Dapr 组件安全基础设施访问
分布式系统零信任安全中的另一个重要问题是确保从代码中安全地访问底层基础设施资源。当然，这里有很多连接身份验证和加密最佳实践，但即使这些到位，代码库仍然最终会将凭据散布在源代码中或存储为环境变量。这会导致更大的攻击面，并增加开发人员管理这些凭据的负担。

这就是 Dapr 组件模型的用武之地。[Dapr 组件](https://docs.dapr.io/concepts/components-concept/) 使用 YAML 接口描述基础设施资源，并由 Dapr API 用于对底层基础设施资源执行各种操作。组件模型通过将访问基础设施所需的连接配置详细信息包含在组件文件中（该文件由 Dapr 在运行时动态加载）来消除源代码中的基础设施依赖关系。有超过 120 个组件规范，所有这些规范都是 [开源](https://github.com/dapr/components-contrib)，由社区贡献。

![](https://cdn.thenewstack.io/media/2024/07/da4020c9-daprzerotrustsec7.png)

*用于基础设施访问的 Dapr 组件模型*

Dapr 组件可用于在运行时限制对基础设施资源的访问。这在 Dapr 中称为 [组件范围](https://docs.dapr.io/operations/components/component-scopes/)，并允许：

- 对应用程序中配置的基础设施执行最小特权原则访问。
- 在网络限制之上进行基础设施访问控制列表。
- 命名空间和信任域边界强制执行。

## 零信任异步通信

前面描述的 Dapr 应用程序 ID 与 Dapr 组件范围的组合允许仅必需的应用程序访问关键的底层基础设施资源，例如生产数据库或消息代理。这在遵守零信任原则时至关重要，因为它减少了攻击者在尝试访问有价值数据时攻击面的范围。在通过消息代理进行异步通信的情况下，应仅允许在代理上发布和订阅的应用程序访问。

让我们看一下披萨店系统中的一个示例。厨房服务需要与披萨店服务通信，以告知客户披萨已完成烹饪。为此，系统使用通过消息代理进行的异步通信。厨房服务利用 [Dapr 发布和订阅 API](https://docs.dapr.io/developing-applications/building-blocks/pubsub/pubsub-overview/) 和 [Dapr pubsub 组件规范](https://docs.dapr.io/operations/components/setup-pubsub/) 在消息代理上的主题上发布消息，实现至少一次传递语义，并从源代码中删除对消息代理的所有依赖关系。披萨店服务订阅主题并使用 /events 方法接收消息以通知用户。

![](https://cdn.thenewstack.io/media/2024/07/f02a61dd-daprzerotrustsec8.png)

*使用 Dapr 发布和订阅 API 进行异步通信*

默认情况下，任何应用程序都可以发布或订阅此消息代理，因此我们需要限制此功能以遵守零信任原则。有几种方法可以限制哪些应用程序可以发布和订阅消息代理基础设施，从范围开始。将 Kitchen Service 和 Pizza Store 服务的 App ID 添加到 Dapr 组件文件中，可确保只有这些应用程序的 sidecar 才会在运行时加载此组件，从而仅授予这些应用程序访问权限。Dapr 发布和订阅访问策略可以通过指定消息代理上允许的主题以及可以执行发布和订阅操作的应用程序列表来变得更加细化。这确保了系统中的恶意行为者将无法获得对底层基础设施资源的访问权限以创建新主题、发布消息或接收数据。

![](https://cdn.thenewstack.io/media/2024/07/950bcedb-daprzerotrustsec9.png)

*Kafka 消息代理 Dapr 组件，具有对 Kitchen 和 Pizza Store 服务的访问控制*

在此示例中，使用 Kafka 组件描述，它指定只有 Kitchen Service 可以发布到 topic 上的消息，并且只有 Pizza Store 服务可以订阅它，这意味着即使在系统内，其他任何应用程序都无法连接到 Kafka 消息代理。

## 结论

总之，Dapr 通过为所有应用程序分配应用程序标识，并确保默认情况下为所有服务间和基础设施通信启用 mTLS，从而提高了分布式系统的零信任安全态势。可以叠加几个额外的安全功能，包括添加 Dapr 配置策略以限制应用程序之间的服务调用，以及配置 Dapr 组件的范围。[此处](https://docs.dapr.io/concepts/security-concept/)详细了解 Dapr 如何以安全为中心进行设计。

观看在 App DeveloperCon 上录制的此会议，[睡得更香：Dapr 的安全云原生开发方法](https://youtu.be/3BCIGU3EiGE?feature=shared)，以了解 Dapr 中的零信任安全，并附带实时演示场景。
