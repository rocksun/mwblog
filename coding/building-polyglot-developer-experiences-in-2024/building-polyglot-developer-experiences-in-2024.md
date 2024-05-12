
<!--
title: 构建2024年的多语言开发者体验
cover: https://cdn.thenewstack.io/media/2024/03/cda19fdc-letters-5570359_1280.jpg
-->

如何使用 Dapr、Knative Serving 和 Dagger 构建针对特定工作流优化的自定义（和多语言）开发者体验。

> 译自 [Building Polyglot Developer Experiences in 2024](https://thenewstack.io/building-polyglot-developer-experiences-in-2024/)，作者 Mauricio Salatino。

作为一名开发者，很容易被完成工作所需学习和使用的工具数量所淹没。虽然经验告诉我们，没有现成的万能解决方案可以满足所有需求，但有一些最佳实践、开放接口和标准可以极大地减轻开发者和团队的认知负担。

通过结合开源工具和标准，无论公司使用什么工具，都可以实现自定义开发工作流。

让我们看看如何基于开源项目（例如 [Dapr](https://thenewstack.io/microsofts-open-source-dapr-could-help-developers-build-agnostic-microservice-applications/)、[Knative Serving](https://thenewstack.io/knative-applies-to-join-kubernetes-community-at-cncf/) 和 [Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/)）构建针对专门工作流优化的自定义（和多语言）开发者体验。

## Dapr

[Dapr](https://dapr.io) 项目提供应用程序级 API、云原生模式和最佳实践，使开发者能够使用不同的语言构建复杂的分布式应用程序。这种 API 驱动的途径使应用程序在环境中具有可移植性，因为数据库、键值存储、消息代理和其他跨领域应用程序问题等应用程序基础设施被抽象在 API 之后。

无论是在本地运行应用程序，还是在云提供商管理的服务中使用 Kubernetes 运行应用程序，应用程序代码都不会更改。Dapr 与流行的框架和工具集成，例如：Java 开发者的 Spring Boot 和 Quarkus；C# 开发者的 ASP.NET Core 和 .NET Aspire；Python 开发者的 Flask，同时提供与 IntelliJ 和 VScode 等 IDE 的集成。

## Knative Serving

Knative Serving 是另一个 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 项目，专注于在 Kubernetes 之上提供无服务器体验，这不仅帮助团队扩展其生产工作负载，还帮助团队实施不同的发布策略（蓝/绿部署、金丝雀发布、A/B 测试）以优化其发布周期。

Knative Serving 也是一个 Kubernetes 扩展，通常不针对开发者，但它为开发者在日常活动中将使用的功能提供构建模块。

Knative Serving 以提供构建功能即服务 (FaaS) 平台的基础层而闻名，例如 [Red Hat OpenShift Serverless 平台](https://www.openshift.com/try?utm_content=inline+mention)，因为它极大地简化了工作负载部署的配置方式，与开箱即用的 Kubernetes 资源（例如入口、服务和部署）相比。

## Dagger

[Dagger](https://dagger.io) 使团队能够使用他们选择的语言对自定义开发和运营流程进行编码，这些流程可以在内部部署和云服务中运行。利用多种语言的开发团队可以结合这些不同的工具，以确保他们专注于开发任务，而不是学习如何组合多个工具。

通过使用大多数语言中可用的 Dagger SDK，团队可以对如何构建、打包和部署其应用程序进行编码。虽然 Dagger 主要与 Tekton、Jenkins 和 GitHub 操作等工具进行比较，但很明显，采用 Dagger 等工具的主要优势之一是在复杂工具之上创建定制体验。

Dagger 帮助我们为本地和远程开发编码不同但一致的体验。如果我们依赖 Dapr 提供的稳定且开放的 API 来构建复杂的分布式应用程序，则 [Dagger Dapr 模块](https://www.google.com/url?q=https://daggerverse.dev/mod/github.com/marcosnils/daggerverse/dapr@18ab6cf84f5a783a2c72629eea6ed9e9f728c71e&sa=D&source=docs&ust=1708464005151302&usg=AOvVaw3tZ2W3PFJh184p6L7MYM1c) 集成提供了一个本地和多语言的设置，用于在集群外部对应用程序进行编码。

使用 Dagger 构建的开发者体验可以简化对远程环境的部署，例如，隐藏 Kubernetes 资源的创建或专门为这些团队实施的发布策略。由于 Dagger 拥有一个集成生态系统，可以使用您最喜欢的编程语言进行组合，因此您的团队可以轻松地打包和分发基于现有和社区维护的集成的更复杂的体验。

## 摘要

本文介绍了三种开源工具，这些工具可帮助团队构建在不同环境中运行的应用程序，因为它们依赖于开放接口，例如 Dapr API。像 Knative Serving 这样的项目可以在减少团队配置其工作负载在 Kubernetes 集群中运行的方式的认知负荷方面发挥巨大作用，因为它提供了一个简化但强大的资源模型。

最后，Dagger 可用于抽象化使用 Kubernetes 的固有复杂性，以实现多语言和本地开发体验，提供 Kubernetes 集群外部应用程序所需的功能。当应用程序准备部署到远程环境时，可以使用您最喜欢的编程语言对自定义远程体验进行编码，并且可以向用户隐藏目标集群中使用了 Knative Serving 等工具。

这三种技术的结合提供了灵活性，并通过减少开发人员的认知负荷和在构建针对专门工作流优化的自定义（和多语言）开发者体验时需要学习的工具数量来提高生产力。而且这一切都基于免费提供的开源软件。
