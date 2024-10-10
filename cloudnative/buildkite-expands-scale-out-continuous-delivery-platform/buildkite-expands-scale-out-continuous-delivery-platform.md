
<!--
title: Buildkite扩展了其规模化持续交付平台
cover: https://cdn.thenewstack.io/media/2024/10/e6c1ea3d-buildkite.png
-->

Buildkite，深受高流量、横向扩展的企业对消费者巨头的青睐，已将其同名 CI/CD 服务扩展为一个完整的平台。

> 译自 [Buildkite Expands Scale-Out Continuous Delivery Platform](https://thenewstack.io/buildkite-expands-scale-out-continuous-delivery-platform/)，作者 Joab Jackson。

[Buildkite Pty Ltd](https://buildkite.com/) 扩展了其同名注重并发性的 [持续集成和交付软件](https://thenewstack.io/ci-cd/)，使其成为一个完整的平台，增加了测试引擎、包注册服务和移动交付云。

该软件于十年前由 Buildkite 首席执行官 [Keith Pitt](https://x.com/keithpitt) 推出，旨在并发运行，允许用户运行比传统构建流水线多一百倍的代理。

因此，该软件在许多规模化公司中得到应用，包括 Airbnb、Canva、Lyft、PagerDuty、Pinterest、PlanetScale、Shopify、Slack、Tinder、Twilio、Uber 和 Wayfair 等。

在 TNS 上，我们记录了 [Equinix 如何使用 Buildkite](https://thenewstack.io/how-our-bare-metal-cloud-keeps-up-with-all-the-new-os-releases/) 来更新其裸机云上支持的众多操作系统。

Pitt 在担任开发人员时创建了该软件，当时他与 [Heroku](https://thenewstack.io/how-heroku-is-positioned-to-help-ops-engineers-in-the-genai-era/) 和 [git 代码库](https://thenewstack.io/need-to-know-git-start-here/) 合作。

“Heroku 是一个神奇的平台。Heroku 做了一些其他平台没有做的事情，而且他们关心开发人员体验，”Kitt 说。他工作的公司强制使用 [Jenkins](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/)，当时它很难使用，尤其是在远程访问资产时。

“我需要一种不同的方法来完成我的工作，”他说。

据该公司称，总体而言，使用该软件构建的软件每天被超过十亿人使用。

Uber 工程经理 Shesh Patel 在一份声明中表示，这家网约车巨头通过切换到 Buildkite 将其构建时间缩短了一半。“采用交付优先的思维方式对于我们发展至关重要，”他断言。

![](https://cdn.thenewstack.io/media/2024/10/88b1c80f-buildkite-4-1024x529.png)

## Buildkite 与其他 CI/CD 系统的区别

Kitt 声称，Buildkite 在两个主要方面不同于其他 CI/CD 软件和服务提供商。一个是它被构建为并发运行，支持同时运行多个作业。另一个是它不按构建分钟数或并发作业数收费，这是 CI/CD 领域中两种广泛使用的计费方法。

相反，Buildkite 提供 [按席位计费的无限使用定价模式](https://buildkite.com/pricing)。

IDC 软件开发 DevOps 和 DevSecOps 项目副总裁 Jim Mercer 在一份声明中指出，在许多情况下，组织都与“传统 DevOps 工具”绑定在一起，这些工具将它们束缚在缓慢的构建周期中。

为了说明为什么加速持续集成对于规模化公司如此重要，Kitt 提供了一个例子：像 Uber 这样的公司可能拥有 5000 名开发人员。在工作日开始时，大多数开发人员或多或少会同时开始进行代码提交。由于 Uber 复杂的代码库拥有 5000 万行代码或更多，每次更改可能会触发多达 50000 次单独测试。将此乘以 5000 次更改，构建系统可能同时管理数亿个事件。

“你不能一个接一个地运行测试。否则，它将需要数周、数月、数年，甚至在某些情况下，需要数年才能按顺序运行测试，”Kitt 补充道。“所以你必须瘫痪，你必须并发运行它们。”

该软件 [以开源形式提供](https://github.com/buildkite/)，可以轻松复制以运行所需的构建工作流。

开发人员定义了一组代码在投入生产之前应该经历的步骤，或 [流水线](https://buildkite.com/docs)，这可能包括单元测试和集成测试，以及其他检查。每个步骤都由构建运行器代理处理，这些代理是用 Go 编程语言编写的，因此可以在不同的平台上运行。每个代理通过 HTTPS 轮询 Buildkite 的代理 API。输出 [存储并重复使用](https://buildkite.com/docs/pipelines/artifacts) 作为工件。

![](https://cdn.thenewstack.io/media/2024/10/67f5bc42-buildkite-hybrid-architecture-44856ac4-1024x610.png)

Kitt 指出，该领域中另一个阻碍持续集成扩展能力的问题是客户的计费方式。

“这个领域中的许多其他参与者都没有动力让你更快，因为他们的主要收入来源是计算，”Kitt 说。“他们转售电力，所以他们没有动力让你更快。”

作为替代方案，Buildkite 按活跃用户收费，这使该公司能够通过并发性将工作流时间尽可能地缩短到接近零。

Buildkite 采用混合架构，这意味着它使用客户的计算能力，而公司则在其自己的云控制平面（Kitt 将这种方法称为 [自带云 [BYOC]](https://www.confluent.io/learn/bring-your-own-cloud/)）上运行操作。Buildkite 本身无法访问代码（这对许多组织来说是一个真正的安全优势）。

## Buildkite 如何扩展

对于新版本，Buildkite 扩展了其 BYOC 格式以包含包注册表，提供具有快速索引和增强安全功能的高性能资产管理服务。客户提供存储，Buildkite 提供管理。

该公司还加强了自己的云环境，以代表客户运行移动应用程序，该环境（与其他 Buildkite 产品不同）基于按使用付费。Kitt 表示，对于不想管理移动应用程序交付复杂物流的组织来说，这是理想的选择。
