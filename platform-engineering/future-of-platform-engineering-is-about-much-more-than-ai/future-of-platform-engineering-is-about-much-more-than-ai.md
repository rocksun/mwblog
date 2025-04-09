<!--
title: 平台工程的未来远不止于人工智能
cover: https://cdn.thenewstack.io/media/2025/04/4a26ecbf-viktor-farcic-mauricio-salatino-kubecon-2025.jpg
summary: 平台工程未来不止于AI！文章回顾了IDP演进，强调API、Docker、Kubernetes等关键技术。现有BACK Stack、CNOE、KusionStack三大蓝图加速落地。未来平台需关注AI集成，如Dapr AI Agent Framework，实现LLM的安全性、可观测性与弹性，拥抱“平台即产品”思维。
-->

平台工程未来不止于AI！文章回顾了IDP演进，强调API、Docker、Kubernetes等关键技术。现有BACK Stack、CNOE、KusionStack三大蓝图加速落地。未来平台需关注AI集成，如Dapr AI Agent Framework，实现LLM的安全性、可观测性与弹性，拥抱“平台即产品”思维。

> 译自：[Future of Platform Engineering Is About Much More Than AI](https://thenewstack.io/future-of-platform-engineering-is-about-much-more-than-ai/)
> 
> 作者：Jennifer Riggins

伦敦 — “[Viktor Farcic](https://www.linkedin.com/in/viktorfarcic/)”在平台工程日的演讲开场时说：“我所要做的，我所知道的，就是编写代码，然后所有其他需要做的事情，总是由其他人来完成。”他是[Upbound](https://www.upbound.io/?utm_campaign=2022_Q3_EVER_GBL_The-NewStack-GENERAL&utm_medium=The-New-Stack&utm_source=referral&utm_content=inline-mention)的开发者倡导者。

“实际上，在早期，我大部分时间都在等待事情发生，等待别人做一些事情，以便让我能够继续编写代码。”

在周二[KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/)之前的平台工程日上，[Mauricio Salatino](https://www.linkedin.com/in/salaboy/)加入了Farcic的演讲，他是“[Kubernetes平台工程](https://www.manning.com/books/platform-engineering-on-kubernetes?utm_source=salaboy&utm_medium=affiliate&utm_campaign=book_salatino2_continuous_9_18_21&a_aid=salaboy&a_bid=b7ac598c&chan=mm_conference1)”一书的作者，也是Diagrid的开源软件工程师。两人开始分享他们对[平台工程](https://thenewstack.io/platform-engineering/)的历史和未来的看法，回顾了他们软件开发职业生涯的开端。

同样，Salatino说，当他开始担任[Java](https://thenewstack.io/introduction-to-java-programming-language/)应用程序开发人员时，他“总是从非常强的开发角度出发。我真正关心的是我们正在构建的应用程序，而不是它们在生产环境中的运行方式。”

为了节省时间，他们都开始自动化一些重复性的工作，比如[测试](https://thenewstack.io/introduction-to-software-testing/)，并拥抱[测试驱动开发](https://thenewstack.io/a-next-step-beyond-test-driven-development/)和行为驱动开发——所有这些都是手动完成的。

“最终，这导致其他人开始使用我正在做的事情，”Varcic说。“然后问题来了，如果你创建了一堆工具，无论你使用哪种技术，而这些工具恰好被组织内部的其他人或许多人使用，你是否认为这是一个平台？”

Salatino创建了Java应用程序服务器功能，这样他就不必编写其他函数，并构建了库来跨应用程序重用功能，最终他也与同事分享了这些功能。那么，这个应用程序服务器是一个平台吗？

第一个[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)是否自然而然地作为协作团队合作的结果而出现？或者平台工程是有意为之的？平台何时转变为IDP？了解了这些答案，面对[人工智能](https://thenewstack.io/ai/)，平台工程的未来是什么？请继续阅读，加入我们的旅程。

## 第一个“黄金路径”

大约15年前，[API](https://thenewstack.io/api-management/)作为一种标准方式出现，用于与任何事物进行交互、在其基础上构建或扩展任何事物。因此，为未来内部开发者平台的[黄金路径](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/)奠定了第一块基石。

API仍然是互联网的支柱，并且仍然是在您的平台上实现可扩展性的标准方式。

接下来是[Docker](https://www.docker.com/?utm_content=inline+mention)，Farcic说它与构建平台无关，而是关于如何以某种标准方式打包应用程序，然后在任何地方（除了生产环境）运行它们。

“Docker真正特别之处在于，这是我第一次看到来自不同领域的工程师都对同一件事感兴趣，”Farcic说。“这是大家第一次说，‘哦，这很酷。我们都想用这个。’”

各种不同的工程师确实可以使用Docker在打包和运行时方面做很酷的事情，但是，他说，它在生产环境中实际上不可用。

真正改变一切的是[Kubernetes在2014年的发布](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)。

“我们都同意，这就是我们要放置东西的地方，无论我们的东西是什么——数据库、应用程序、基础设施，任何东西，”Farcic说。“我们最终达成了行业共识，即我们将在哪里构建东西。”

公司只需要弄清楚如何到达那里。而且，[特别是对于开发人员来说](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)，这并非易事。
不过，一路走来，平台始终存在。

Varcic 说：“公司构建平台和未能构建平台已经有 30 或 40 年的历史了。就我们想要完成的目标而言，我们并没有做什么新的事情。技术和一些模式是新的。这是最近发生的变化。”

那就是——以及行业围绕“平台工程”这个术语凝聚起来。

## 平台工程的模式

平台的常见模式也不是什么新鲜事。它始终是 [Kubernetes](https://thenewstack.io/kubernetes/) 和 API，中间有控制器。

例如，Farcic 认为，[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 一直是一个公共平台。“他们拥有它，他们开发它，他们代表服务消费者管理它——这些都是以某种方式消费它并用它做一些事情的该服务的用户。”

一直都有服务所有者和服务消费者，但最近，业界更加关注将内部开发人员视为一流的消费者，遵循 [平台即产品 的思维模式](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)，API 仍然是交付所需体验的首选方式。除此之外，Kubernetes 已成为平台所基于的实际基础——并抽象出其复杂性。

然后，组织是[构建还是购买](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/)控制器变得不太明确。根据 Farcic 和 Salatino 的经验，组织通常从第三方控制器开始——最常见的是在 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) [landscape](https://landscape.cncf.io/) 中找到的开源工具。

然后，Salatino 说，你需要一堆功能添加到你的平台上，比如用于请求驱动计算的 [Knative](https://github.com/knative/serving) 和用于声明式持续部署的 [ArgoCD](https://argoproj.github.io/argo-cd/)。他说，无论你构建什么样的自定义 IDP，你都需要尽早构建某些东西，比如安全性和可观测性。

Farcic 说：“六年前，我们当时的大多数人都在选择我们将要使用或贡献的第三方。”

然后，Salatino 继续说道，这是关于弄清楚下一步：你如何让你的平台为你自己的领域需求服务？他的角色从在基础设施工作转变为帮助其他工程师编写他工作的机制。

[平台工程师角色](https://thenewstack.io/how-to-hire-a-platform-engineer/) 从那里有机地发展起来，甚至在它有这个名字之前。

当前平台工程时代的最终模式或最佳实践是努力通过仪表板、[GitOps](https://thenewstack.io/streamlining-kubernetes-implementation-with-gitops-best-practices/) 等使你的 IDP 更加用户友好。

对于 Salatino 来说，这是通过隐藏平台背后的 Kubernetes 复杂性、通过 API 扩展它并向用户提供服务来实现的。

## 平台工程：为速度而构建

既然平台工程成功的基本模式已经确定，那么一切都必须针对速度进行优化。

在过去的三年或四年里，面对 CNCF landscape 的复杂性，并为了响应组织分享他们的经验，平台工程蓝图已经出现，它们以一定的节奏混合和匹配不同的第三方工具集。

目前最常见的三个平台工程蓝图是：

*   [BACK Stack](https://github.com/back-stack): [Backstage](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/), ArgoCD, [Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) 和 [Kyverno](https://thenewstack.io/using-the-kyverno-cli-to-write-policy-test-cases/).
*   [CNOE](https://thenewstack.io/building-an-idp-with-help-from-the-open-source-cnoe-framework/): Kubernetes, ArgoCD, Backstage, Crossplane 和 [Keycloak](https://github.com/keycloak/keycloak).
*   [KusionStack](https://github.com/KusionStack): Kusion, Karpor 和 Kuperator.

Salatino 说：“我认为这是一个巨大的进步，表明社区正在向前发展。我们有这些蓝图，我们肯定会尝试减少组织开始所需的时间。”

他补充说，每一个都是“不同的蓝图，你可以更换组件的不同工具组合，具体取决于你想使用什么——但同样，展示了如何在不弄清楚你可以使用的所有可能的工具组合的情况下到达那里。”
为了让新兴的平台工程师尽快上手，CNCF 正在启动一个[平台工程认证项目](https://training.linuxfoundation.org/platform-engineering-programs/)。为了确保所有这些平台工程的势头不会忽略最终用户或消费者（即内部开发人员），KubeCon Europe 2025 甚至有史以来第一次包括了一个应用程序开发轨道。

Salatino 说，此举不仅旨在分享平台工程的经验和进展，而且旨在获得应用程序开发人员关于如何构建更好平台的反馈，包括 Kubernetes 到底需要抽象多少。

## AI 在平台工程中的作用是什么？

最后，不出所料，[AI](https://thenewstack.io/ai/) 在改进平台工程策略的下一步中发挥着作用。

“我们如何在平台内部引入 AI 功能，而不仅仅是从我们的应用程序中调用 [一个 [大型语言模型](https://thenewstack.io/llm/)]？” Salatino 说。“因为，如果我们这样做，那么我们只是在浪费所有的平台资源，以及我们正在进行的所有的对话。”

今年 3 月，CNCF 宣布扩展其毕业的 [Dapr](https://thenewstack.io/dapr-graduates-cncf-and-connects-to-webassembly/) 项目，发布了 [Dapr AI Agent Framework](https://github.com/dapr/dapr-agents)，该框架旨在构建自主、弹性且可观测的 AI 代理，具有内置的工作流程编排、安全性、状态性和遥测功能。

“如果你想访问 LLM，你需要确保，作为平台工程，你的安全性与你公司拥有的所有其他安全策略集成在一起，你可以以一致的方式管理这种访问，你具有弹性和可观测性，”Salatino 说。“我们希望确保无论你使用什么样的数据，无论你使用什么语言，你始终需要提供与治理的工作流程集成。”

Dapr 的一个重要强调是，无论 LLM 开发人员使用什么，甚至他们选择使用什么代理 AI 框架，这些横切关注点都会贯穿始终：

- 安全性：访问控制、安全凭证和个人身份信息混淆。
- 弹性：自动重试、请求超时和断路器。
- 可观测性：请求跟踪、网络指标和错误日志。

像所有开源事物一样，即使是 AI，也归结为社区如何共同构建。

正如 Salatino 提醒他的听众，“云原生平台不是孤立构建的。如果你正在公司内部构建平台，请确保与其他公司交谈，确保分享你的知识。”

你准备好开始你的平台工程之旅了吗？获取我们的电子书的免费副本：“[平台工程：你现在需要知道什么](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)。”