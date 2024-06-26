<!--
title: 像开发者一样思考，助力开发团队更快交付项目
cover: https://cdn.thenewstack.io/media/2023/11/a9ba2e28-think-like-developer-1024x683.jpg
-->

为了加速开发流程，构建内部开发者平台的团队需要深入了解开发过程的内部运作。

> 译自 [Think Like a Developer to Help Dev Teams Ship Faster](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/)，作者 Thor Sigurdsson 是 Garden 的工程副总裁兼联合创始人，该公司提供开源 Kubernetes 开发和测试平台。他本质上是一位程序员和架构师，拥有超过 10 年的全栈经验。与他的联合创始人们一起，他致力于...

我于2011年开始专业编程。可以说，在那个时候，大多数公司并未感到有必要构建内部开发工具。

大多数应用程序都是单体应用，你选择的编程语言通常带有一个充满活力的生态系统，其中包括框架、库和工具，为你提供了实时重载、测试自动化、调试器以及编写和发布软件所需的一切。

而现在，你的生产系统包括部署到 [Kubernetes](https://thenewstack.io/kubernetes/) 的30个服务，并使用多个托管云服务。使用社区标准工具编写、调试和测试这些系统不再那么直截了当。

创建开发环境，实时重载它们，运行API测试，流式传输日志 —— 所有这些自动化必须通过[CI流水线](https://garden.io/blog/ci-is-just-a-script-runner)和各种供应商构建的工具拼凑在一起。这导致了很多复杂性、挫折和缓慢的反馈周期。最终结果是，开发人员在开发现代应用程序时很难保持高效。

正因为如此，并为了在整个组织中保持合规性和一致性，越来越多的公司意识到需要一个[内部开发平台（IDP）](https://garden.io/blog/ci-is-just-a-script-runner)。

虽然如果你的IDP帮助你在开发过程中集中管理合规性和安全性方面的问题，那是很好的。但不要止步于此。你的主要目标应该是开发人员的生产力和幸福感。这是你的公司能够更快地交付高质量软件的方式。

简而言之，将你的内部开发平台（IDP）的重点放在提供开发工作流上，使开发人员能够更快、更顺畅、更轻松地进行迭代、测试和部署。理想情况下，它为开发服务系统提供了与使用语言特定工具开发单一服务时相同水平的凝聚力和质量（尽管这很难实现，但却是一个值得追求的目标）。

## 了解生产不等同于了解开发

了解系统在生产环境中的部署和运行，并不等同于了解它是如何开发的。

正确完成所有这些工作的难点在于，负责构建内部开发平台（IDP）的工程师通常是站点可靠性工程师（SREs）和其他专业工程师，他们的专业知识主要涉及系统在生产环境中的部署，而不是系统的开发过程。

与开发过程相关的工具、工作流、摩擦点以及其他设计约束（例如，代码库的哪些部分难以或容易进行工作）最终会强烈影响系统在实践中的开发、调试和测试方式。而这些实际约束会随着系统的增长和变化而不断地变化和重新对齐。

很多时候，这些知识被嵌入在个别开发团队和开发人员的部落传说以及个体人类大脑的思维模式中。

为了加速开发过程，平台团队需要从内部了解它。从最基本的层面来说，这可以归结为两个原则。

### 1. 了解你的开发人员

定位公司开发工作流中的瓶颈应该从与开发人员密切合作开始。从他们的视角了解开发和测试过程，而不仅仅是从生产操作和CI/CD系统的视角，是确保他们能够从你的内部开发平台（IDP）中受益并热爱使用它的最佳途径。

这个过程应该始于绘制不同类型开发人员首选工具和工作流的地图。

例如，[前端Web开发人员](https://roadmap.sh/frontend)可能更喜欢针对类似生产的开发环境的API进行本地（非容器化）开发。相反，后端开发人员在处理多个服务时可能希望使用[Docker](https://www.docker.com/?utm_content=inline-mention) Compose，但在处理单个服务时切换到非容器化的本地工作流。这也可能因团队、以及用于各种服务的编程语言或工具而有很大的差异。

随着与来自不同团队的更多开发人员的交流，你将看到主要的开发人员类型和工具偏好的主要集群逐渐浮现。你选择包含在IDP中的工具和产品应该源自与开发人员互动时发现的工作流程和过程。术语“开发者体验”将其中许多工具标记为“Nice to have”，尽管它们对团队快速交付高质量[软件的能力有着显著的影响](https://garden.io/resource-download)。

每个开发人员都梦想着以思维的速度工作。你越接近这个理想，他们就会越快乐 — 同样，管理层也会如此！

这不仅仅是关于推出功能和达到季度目标 — 开发人员还希望编程感觉神奇而令人振奋。

### 2. 识别最严重的瓶颈，修复，重复。

任何过程的吞吐量都受到其瓶颈的限制。这对化学反应、工厂装配线以及软件交付同样成立。提高吞吐量的最佳途径是解决整个软件交付生命周期中最严重的瓶颈。

如果最严重的瓶颈发生在开发和测试期间，那么不支持实时重载或调试的自助暂存环境在解决为何API测试在你的分支上失败的问题时并没有太大帮助。

由于开发和生产环境之间的差异或缺乏工具，软件系统的某些区域往往很难调试。当一个功能涉及到这些区域时，缓慢和挫折就会产生。

识别（并修复）架构和自动化中的[触发点](https://garden.io/resource-improve-developer-productivity)，这些触发点迫使开发人员从快速迭代降级为反复触发缓慢流水线或与不熟悉的操作细节搏斗以重现他们正在编写（或调试）的行为，是创建出色内部开发平台（IDP）过程的关键部分。

深入挖掘指标：你的开发人员在哪里花费了时间？常见的开发和测试工作流中某些关键步骤需要多长时间？它们随时间的推移趋势如何？

一旦你对公司的开发和测试工作流有了足够清晰的了解，你就可以通过数据和仪表板来追踪开发自动化的健康状况。

无论你选择什么工具和方法，都要紧密关注[解决开发过程中最严重瓶颈](https://thenewstack.io/how-to-find-and-solve-engineering-bottlenecks/)的焦点，重新评估并重复，这将帮助开发人员更快、更轻松地交付。

## 综合一切

与开发人员的交流将为你提供洞见：

- 当一切顺利时，他们喜欢使用什么样的工具和工作流，例如：
  - 前端开发人员使用本地Web开发工具，结合共享API。
  - 后端开发人员使用Docker Compose。
  - 本地运行单元测试、调试器和其他高效的开发工具。
- 触发开发人员使用更慢、更令人沮丧的工作流的触发点，例如：
  - 不能轻松地同时部署他们正在处理的所有服务，而不让Docker Compose资源耗尽。
  - 不能轻松地创建具有实时重载的开发环境，以重现刚刚在CI中出现的错误。
  - 不能验证他们对破碎的集成或API测试的修复是否有效，而不是反复运行CI流水线。

在可能的情况下，你的IDP应该尽量通过[自动化和功能](https://garden.io/blog/devops-automation)增强开发人员已经喜欢使用的工具，使他们能够保持在快车道上。

创建一个在所有这些方面都做得很好的IDP可能看起来像是一项艰巨的任务。但是与开发人员合作，找到你当前设置中的触发点，将会缩小你的选择范围并提供一个清晰的前进路径。

在 Garden，我们构建了一个工具，它是使用 Kubernetes 和其他云原生技术[构建内部开发平台（IDP）的理想基础](https://garden.io/developer-platform)。Garden 架起了你的基础设施和开发工具之间的桥梁，在加速、可移植的流水线中编排你的 Dockerfiles、Helm charts 和 Terraform 配置，实现在任何地方运行。[快来试试吧](https://app.garden.io/)！

