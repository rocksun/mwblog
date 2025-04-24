
<!--
title: Heroku如何“重新平台化”其平台
cover: https://cdn.thenewstack.io/media/2025/04/56e4407a-kccnc-eu-25_betty-junod_featured.png
summary: Heroku “重新平台化”拥抱云原生！新平台 Fir 基于 Kubernetes OCI，采用 Heroku Cloud Native Buildpacks，无需 Dockerfile。开源 Twelve-Factor App 方法论，拥抱 CNCF，引入 OpenTelemetry，集成 AI，构建可靠高性能云应用！
-->

Heroku “重新平台化”拥抱云原生！新平台 Fir 基于 Kubernetes OCI，采用 Heroku Cloud Native Buildpacks，无需 Dockerfile。开源 Twelve-Factor App 方法论，拥抱 CNCF，引入 OpenTelemetry，集成 AI，构建可靠高性能云应用！

> 译自：[How Heroku Is ‘Re-Platforming’ Its Platform](https://thenewstack.io/how-heroku-is-re-platforming-its-platform/)
> 
> 作者：Heather Joslyn

构建一个内部平台，或者将遗留的单体应用迁移到微服务和云端，可能是一项巨大的工程。但是，与 Heroku 在过去一年半里所做的事情相比，这些项目可能就相形见绌了。

根据 Betty Junod 的说法，在这段时间里，这家平台即服务公司一直在“重新平台化平台”。Betty Junod 是 Salesforce 旗下 Heroku 的首席营销官兼高级副总裁。（自 2011 年以来，Salesforce 一直拥有 Heroku。）

Junod 在伦敦举行的 [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) 上录制的 The New Stack Makers 的 On the Road 节目中告诉我：“对于最终用户组织来说，这是一个足够重大的决定。”

“但是对于像我们这样，在我们的平台上托管成千上万最终用户的公司来说，这是一个相当重大的决定。”

下一代 Heroku，[代号为 Fir](https://blog.heroku.com/heroku-fir-generally-available-new-platform-capabilities)，将于本月全面上市。

作为其重新平台化的一部分，Heroku 重申了其开源的诚意。它转向了 [Kubernetes OCI](https://thenewstack.io/kubernetes-1-31-arrives-with-new-support-for-ai-ml-networking/) ([Open Container Initiative](https://opencontainers.org/))，这是管理容器格式和运行时的开放标准。

新的、改进的平台还包括 [Heroku Cloud Native Buildpacks](https://github.com/heroku/buildpacks)，它允许开发人员为他们的应用程序创建一个生产就绪的容器镜像，而无需使用 Dockerfile。

Junod 说，Heroku 始于 2007 年，是 [Buildpacks](https://buildpacks.io/) 的早期开发者。“那是在 [Docker](https://www.docker.com/?utm_content=inline+mention) 之前，在容器之前。那是 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 的早期。因此，我们的服务构建在 AWS 之上，但是，我们的工程师必须使用 LXC 和我们自己的编排来定制我们自己的容器化。”

Junod 指出，该项目最初是在 Ruby on Rails 上启动的。今天，它支持八种语言，包括 [Go](https://thenewstack.io/introduction-to-go-programming-language/)、[Java](https://thenewstack.io/introduction-to-java-programming-language/)、[PHP](https://thenewstack.io/php-creator-rasmus-lerdorf-shares-lessons-learned-from-the-last-25-years/) 和 [Python](https://thenewstack.io/python/)。

## 重新思考“十二要素应用”方法论

Junod 告诉 Makers 观众，Heroku 已经成为 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) 的白金会员，这标志着对开源社区的承诺增加。

作为其为期三年的白金会员资格的一部分，“我们在理事会中占有一席之地，因此我们正在积极参与其中，”她说。“当我们研究可以将哪些技术引入平台时，这使我们能够与这些贡献者和项目进行互动。”

例如，“OpenTelemetry 是我们一直在……花费更多时间的另一个项目，因为我们正在将其引入平台。因此，这确实是与整个云原生生态系统进行更富有成果的旅程的开始。”

去年 11 月，Heroku 开源了其 [十二要素应用](https://github.com/twelve-factor/twelve-factor) 方法论（您可以从 [Makers 之前的剧集](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/) 中了解更多信息）。Junod 说，十二要素应用标准是“一种宣言式方法论……关于如何为云构建可靠、高性能的应用程序”。“因为这仍然是新的。人们不知道；我们应该如何做某些事情？”

她说，展望未来，社区将参与更新该方法论，解决诸如 secrets 和 workload identity 之类的问题，这些问题多年来变得越来越重要。

她说，项目贡献者将提出的关于十二要素的问题是，“它们在当今世界中如何仍然适用？因为现在我们有很多公司已经运行了大量的 infrastructure 和大量的 web 规模的应用程序。

“因此，我们如何才能汲取这些经验教训，将其编纂到更新这些要素中，也许现在我们需要以不同的方式看待和应用某些要素，因为我们了解了更多。然后与社区分享。”

查看完整剧集，了解有关下一代 Heroku 的更多信息，包括它如何将 AI 以及数据科学家和开发人员的需求集成到其平台中。