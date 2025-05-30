<!--
title: 平台工程：你产品化的 DevOps
cover: https://norbix.dev/platform-banner.jpg
summary: 告别重复造轮子！`Platform Engineering`整合 `DevOps`、`SRE` 和云工程，构建内部平台（`IDP`），用 `IaC`（`Terraform`等）、`CI/CD` 管道和可观测性工具赋能开发者。黄金路径是关键，告别 YAML 地狱，拥抱 `Kubernetes` 和 `OpenTelemetry`，提升开发者体验（DX），加速软件交付！
-->

告别重复造轮子！`Platform Engineering`整合 `DevOps`、`SRE` 和云工程，构建内部平台（`IDP`），用 `IaC`（`Terraform`等）、`CI/CD` 管道和可观测性工具赋能开发者。黄金路径是关键，告别 YAML 地狱，拥抱 `Kubernetes` 和 `OpenTelemetry`，提升开发者体验（DX），加速软件交付！

> 译自：[Platform Engineering: The DevOps You Productize](https://norbix.dev/posts/platform-engineering/)
> 
> 作者：norbix.dev



**“伟大的平台不会抽象权力，而是会赋予权力。”**

您可能听说过`Platform Engineering`这个术语。但它仅仅是重新命名的`DevOps`吗？是名字更酷的`SRE`吗？还是带有一些浮夸的`cloud automation`？

让我们把话说清楚——并展示为什么平台工程正在成为现代工程组织的支柱。

## 什么是平台工程？

`Platform Engineering`是设计、构建和维护内部平台，以简化和扩展软件交付的学科。它将DevOps、SRE和云工程的原则整合到一个有凝聚力的、对开发者友好的工具包中。

可以把它想象成构建“铺好的道路”，团队可以自信地在上面部署——而不需要每次都重新发明基础设施、管道或可观测性。

**最终目标？使开发团队能够更快、更安全地交付产品——而不需要成为Kubernetes、Terraform或AWS专家。**

## 平台包含哪些内容？

平台工程师经常构建和维护：

*   🏗️ 内部开发者平台 (IDP)：用于配置、部署和管理服务的自助服务接口和 API，例如[container8.io](https://container8.io)。
*   🔁 CI/CD 管道：用于测试和部署代码的标准化、可重用工作流。
*   ☁️ 基础设施即代码 (IaC)：Terraform、Pulumi、Crossplane 等。
*   🔍 可观测性工具：集中式日志记录、指标和追踪集成。
*   🔒 安全和合规控制：护栏，而不是障碍。

## 它与 DevOps、SRE 和云的关系

### DevOps ✅

DevOps 是一种协作和自动化的文化。

平台工程通过构建开发者可以实际使用的内部工具和工作流来实现 DevOps 的产品化。

### SRE ✅

SRE 侧重于可靠性、自动化和事件响应。

平台团队将 SRE 原则嵌入到平台中：错误预算、黄金信号、运行手册。

### 云工程 ✅

云工程提供基础设施基础。

平台工程师将这种复杂性抽象为可重用的模块和模板。

**平台工程 = DevOps + SRE + 云 + DX（开发者体验）**

## 为什么平台工程很重要

在复杂的环境中——多个团队、微服务、多语言堆栈——平台工程提供：

*   🔄 一致性：标准化的管道和基础设施减少认知负荷。
*   🧪 安全性：护栏防止意外事故并加速入职。
*   🛠️ 开发者赋能：工程师专注于功能，而不是 YAML。
*   ⚖️ 可扩展性：平台比英雄工程师更具可扩展性。

**优秀的平台团队就像产品团队一样：倾听用户、快速迭代并持续交付价值。**

## 黄金路径：秘诀

平台工程不仅仅是关于工具——它是关于有主见的默认设置。最好的平台提供“黄金路径”：

*   构建、测试和部署应用程序的推荐方法
*   服务、作业、基础设施的模板
*   标准化的可观测性和警报

**赋予开发者超能力——而不是空白画布。**

## 行业工具

平台团队使用的一些常用工具和模式：

`IaC`: Terraform, Pulumi, CDK
`CI/CD`: GitHub Actions, ArgoCD, Tekton, Spinnaker
`Containers & K8s`: Helm, Crossplane, Kubernetes Operators
`Developer Portals`: Backstage, Port, Humanitec
`Observability`: Prometheus, Grafana, OpenTelemetry

## 最后的想法

`Platform Engineering`不是一种时尚。它是对大规模现实世界复杂性的一种回应。随着组织的发展，他们需要铺好的道路，而不是铺好的工单。

软件交付的未来是内部平台，它结合了速度、可靠性和安全性——所有这些都以开发者至上的心态。