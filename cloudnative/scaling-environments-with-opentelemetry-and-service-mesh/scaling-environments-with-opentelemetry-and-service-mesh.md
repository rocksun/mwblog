<!--
# 使用 OpenTelemetry 和服务网格扩展环境
https://cdn.thenewstack.io/media/2023/10/14731552-clilmbing-1024x487.jpg
Featued image for: Scaling Environments with OpenTelemetry and Service Mesh
Feature image from Pakorn Khantiyaporn on Shutterstock.
 -->

OpenTelemetry 的 Baggage 功能以及 Istio 和 Linkerd 等服务网格可以协同使用，以实现高度可扩展的开发、预览和测试环境。

译自 [Scaling Environments with OpenTelemetry and Service Mesh](https://thenewstack.io/scaling-environments-with-opentelemetry-and-service-mesh/) 。

使用微服务架构，每个团队一次只处理应用程序的一小部分，将开发和运维的复杂度进行了模块化。另一方面，这也产生了对各组件能够协同工作的验证和测试的需求。近年来，许多新类别的解决方案应运而生，例如短暂环境、按需环境、预览环境等，目的都是帮助确保功能尽早在开发生命周期的整体工作。

所有这些微服务环境类传统上都是整套微服务的完全独立副本。这些堆栈实际可能共享基础设施，比如在同一个 Kubernetes 集群的不同命名空间中运行，或在单节点集群上运行，甚至在本地或远程节点上的 [Docker 容器](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/)中运行(小规模)。然而，这种从彼此隔离地运行每个微服务及其所有依赖的做法存在一些缺点：

1. **成本扩展**: 随着[微服务数量](https://thenewstack.io/microservices/)的增加，成本会呈指数增长，通常需要各种变通方法来控制成本，无论是维护工作量还是基础设施支出。成本影响可能使开发人员不得不排队使用某些共享环境进行测试。
2. **依赖关系陈旧，与生产环境存在偏差**: 每个环境都包含每个依赖项的独立副本，使其保持同步非常困难，更别说每个微服务的不断变更和持续推送了。此外，另一种偏差是第三方依赖和与云服务的集成在这些环境中的行为可能与暂存或生产环境不同，更容易出现“测试通过而生产失败”的问题。
3. **运维开销增加**: 即使只负责堆栈中的单个微服务，运维成本也会增加。
4. **开发者体验欠佳**: 平台团队很难支持每个这样的环境，常导致糟糕的开发者体验和利用率不高。设置环境的时间也会影响开发效率。微服务越多，这些环境启动越慢。

业界已经尝试了许多变通手段来应对这些问题，但我想介绍一种不同的思考环境的方式，与以前的方法相比，它有几个优势。

## 重新思考微服务环境

当我们开发微服务时，每个开发人员或团队只需关注整体架构的一小部分。尽管新版本频繁上线生产环境，但每个微服务通常都有[自己独立的持续集成/持续交付(CI/CD)流程](https://thenewstack.io/ci-cd/)，可将更新推送到类似暂存环境这样的更高级环境。给定这种设置以及希望能尽早在开发周期中进行测试，我们可以将每个微服务的开发/预览/测试环境视为正在改动的部分与其他所有服务的“最新”版本相结合。

![](https://cdn.thenewstack.io/media/2023/10/37da1fed-image1a.png)

如上图所示，我们将整个技术栈中所有微服务的最新版本定义为基准环境。基准环境为任何设置的环境提供了每个微服务依赖项的默认版本，并通过每个微服务的 CI/CD 流程持续更新。它通常是一个像暂存(甚至生产)这样的 Kubernetes 集群。对于每个新的开发/测试/预览环境，我们只部署“已改动的部分”(上图中的沙盒)，这通常只涉及少量相对整体来说很少的几个微服务，其余未变更的依赖项与基准环境共享。

这种方法与在生产环境采用金丝雀发布类似，但这里更强调隔离微服务，以便在开发过程中创建可重用的沙盒环境。下面部分我们看看如何在实践中构建这样的沙盒环境系统。

## 请求租户

前面部分我们了解了沙盒的逻辑构造，它将测试内容与来自基准环境的共同依赖组合。在实践中，这样一个系统依赖两个关键点：请求租户和路由。

![](https://cdn.thenewstack.io/media/2023/10/1172c8e7-image2ab.jpg)

如上图所示，我们假设请求可以通过特殊标识符进行标记，表示发送请求的租户。只要此租户信息随调用在系统内部的服务链路之间传递下去，我们就可以根据该特定租户进行路由决策，即使用来自基准环境中svcA服务的“沙盒化”版本满足特定请求，而不是使用最新版本。因此，我们需要两点来实现这种流程：

1. 一种通过特殊标识符为通过微服务网络的请求标记租户的方法。
2. 一种根据上述标识符的存在进行本地化路由决策的方法。

幸运的是，在现代微服务中传递请求上下文已变得很简单，得益于 [OpenTelemetry](https://opentelemetry.io/)。有了微服务中的 [OpenTelemetry instrumentation](https://thenewstack.io/opentelemetry-in-go-its-all-about-context/)，此功能已经可用。一个特殊的 [baggage](https://opentelemetry.io/docs/concepts/signals/baggage/) header 可以自动转发到后续的微服务。因此，只要我们使用 OpenTelemetry 来实现微服务检测，就可以自动标记请求，无需额外工作。

至于实际进行路由决策，最自然的解决方案是服务网格，如 Istio、Linkerd 等。这些服务网格支持创建规则进行此类本地化路由决策。因此，我们最终可以具备这样的设置：

![](https://cdn.thenewstack.io/media/2023/10/9ba2dd1f-image3a.png)

使用这种系统的一个很大优势是测试多个微服务变得非常简单。由于功能通常跨越多个微服务，在它们全部推送到某个共享环境之前进行联合测试往往非常困难。这里可以通过控制用于标记请求的标识符，轻松创建组合多个其他租户的新租户，这有助于微服务开发过程中实现更融洽的协作。

![](https://cdn.thenewstack.io/media/2023/10/8d8125be-image4.png)

## 数据隔离

上面我们使用一个简单的无状态微服务为例，其中我们使用 HTTP 或 gRPC 等 L7 协议，这使请求标记和路由非常简单。但在实际情况下，存在数据库、消息队列、云依赖等，请求租户可能不足以实现隔离。

例如，测试微服务使用的数据库模式更改可能需要设置临时数据库实例或逻辑数据库来实现必要的隔离。在请求租户不足以实现隔离的这些情况下，可以使用更高级别的隔离。通常有两种更高级别的隔离：逻辑隔离和基础设施隔离。

逻辑隔离是指使用相同基础设施(如PostgreSQL数据库集群)，但在下面设置某种租户单元，如新数据库或模式。基础设施隔离则为特定租户提供专用基础设施，例如设置独立的PostgreSQL数据库集群。无论使用哪种，都可以通过环境变量或Kubernetes中的配置映射，将临时的逻辑或物理资源连接到沙盒的其余部分。

![](https://cdn.thenewstack.io/media/2023/10/fe9805c9-image5.png)

选择什么隔离级别取决于用例，但这里存在明确的权衡：更高级别增加了设置和管理基础设施的运维工作量，同时减少了系统其他部分的干扰。在实际中，大多数情况下，逻辑隔离就足够了，除非数据存储本身不支持此功能，或在某些性能/负载测试场景下。

## 消息队列

对于消息队列，最简单的方法是将租户信息集成到消息本身中(OpenTelemetry支持此功能)，并在消费微服务中根据该信息判断特定消息是否与自身相关。关键是让消费者可以选择性地消费消息，以避免处理不属于自己的租户的消息。

![](https://cdn.thenewstack.io/media/2023/10/14f80399-image6b.png)

在[Apache Kafka](https://thenewstack.io/apache-kafka-primer/)等系统中，方法是为每个租户设置独立的消费者组，然后对应用层中的消费者库进行修改，实现根据该信息选择性地消费消息。

## 异步作业和第三方依赖

某些情况下，微服务可能不参与请求流，而是以完全异步的方式运行，如定期执行某些操作的计划任务，或自己发起请求。在这种情况下，仍可以为其新版本创建“沙盒”，但租户将指定给该微服务的特定沙盒实例本身。从本质上说，在这种场景下，我们的“租户”成为整个微服务，而不仅仅是单个请求。

这同样适用于由于无法使用请求租户而需要依赖配置进行隔离的第三方服务或自定义协议情况。关键是在无法使用请求租户时，仍能回退到使用配置实现隔离。

## 总结

使用请求租户和可调整隔离来创建环境的方法，解决了Kubernetes中传统预览、测试和开发环境设置存在的一些问题。具体来说，由于我们根据每个环境的需要只部署所需的最少量的微服务，即使在大规模情况下，与传统做法相比这也非常节省成本，正如[Uber的SLATE](https://www.uber.com/blog/simplifying-developer-testing-through-slate/)、[Lyft的Staging Overrides](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f)和[Doordash](https://doordash.engineering/2022/06/23/fast-feedback-loop-for-kubernetes-product-development-in-a-production-environment/)等公司内部运行数百个此类系统已经证明的那样。

它还可以针对最新依赖进行高保真测试，并且设置迅速，在开发人员体验和效率方面具有优势。借助这种方法，可以以全新的方式实现无缝协作，跨开发人员和团队一起开发不同的微服务。

我们在Signadot正在构建一个Kubernetes原生解决方案，可以轻松创建这类环境并在Kubernetes中用作预览、开发和测试环境。我们很高兴能够提供这种能力并减少其中的复杂性。您可以在我们的[文档](https://www.signadot.com/docs/overview)中了解有关Signadot方法的更多信息，或者加入我们的[社区Slack](https://join.slack.com/t/signadotcommunity/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ)频道与我们交流!