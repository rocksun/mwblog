# Bitnami开源应用目录迎来18周年！

![Featued image for: The Bitnami Open Source Application Catalog Turns 18!](https://cdn.thenewstack.io/media/2025/04/acd4ccff-bitnami-18-1024x576.jpg)

[Bitnami](https://bitnami.com/)开源应用目录在18年前推出时，从根本上改变了开发者访问和部署[开源软件](https://thenewstack.io/open-source/)的方式。如今，它为全球许多最大的软件市场提供支持，包括最大的云提供商提供的市场，并且每月下载量超过5亿次。既然它已经接近二十年了，也许现在是你了解Bitnami的时候了！

## Bitnami的起源故事

Bitnami由[Daniel López](https://www.linkedin.com/in/ridruejo/)和[Erica Brescia](https://www.linkedin.com/in/ebrescia/)于2007年创立，其使命很简单：让开发者更容易在任何平台上部署开源软件。在Bitnami之前，开发者经常面临为流行的开源应用程序配置复杂环境的艰巨任务。无论是像WordPress这样的内容管理系统（CMS），还是像[LAMP](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/)这样的开发堆栈，启动并运行应用程序的过程绝非易事。

![Old Bitnami image](https://cdn.thenewstack.io/media/2025/04/e7ef43f7-bitnami.png)

来源：Bitnami

Bitnami着手通过提供可以轻松安装、配置和保持更新的预打包应用程序堆栈来解决这个问题。这些堆栈包括所有必要的组件——比如正确版本的数据库、运行时和库——因此开发者可以专注于构建出色的软件，而不是管理复杂的环境。

## 从安装程序到云和Kubernetes

随着技术格局的演变，Bitnami也在不断发展。虽然它最初是使用安装程序和虚拟机，但云计算的兴起为扩展提供了新的机会。在[AWS](https://aws.amazon.com/marketplace/search/results?searchTerms=bitnami)、[Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=bitnami&page=1)和[Google Cloud](https://console.cloud.google.com/marketplace/browse?q=bitnami)等云平台上轻松部署应用程序的能力，对开发者来说是一个游戏规则改变者，Bitnami通过创建[云原生](https://thenewstack.io/cloud-native/)应用程序并通过云市场提供轻松部署来快速适应。

在过去的十年中，容器的兴起塑造了Bitnami的轨迹。认识到向容器化应用程序的转变，Bitnami引入了对Docker容器和Helm charts的支持。Bitnami扩展了[支持的Helm charts](https://github.com/bitnami/charts)的数量，贡献了代码，并使开发者能够在Kubernetes环境中无缝部署和管理他们的应用程序。

## 构建企业级目录

如今，Bitnami是现代开发者工具包中的一个关键工具。凭借即用型应用程序堆栈、开发环境和基础设施工具，Bitnami帮助开发者自动化部署，并专注于真正重要的事情：构建自己的产品。

Bitnami团队继续使用新版本和应用程序扩展目录。在过去的几个月中，Bitnami发布了[Clickhouse 25](https://github.com/bitnami/charts/pull/31786/)、[Cypress 14](https://github.com/bitnami/containers/pull/76447/)、[Envoy 1.33](https://github.com/bitnami/containers/pull/76495/)、[Golang 1.24](https://github.com/bitnami/containers/pull/77394/)、[Laravel 12](https://github.com/bitnami/containers/pull/78652/)、[MariaDB 11.7](https://github.com/bitnami/containers/tree/main/bitnami/mariadb/11.7)、[Node.js 23](https://github.com/bitnami/containers/tree/main/bitnami/node/23)、[WildFly 35](https://github.com/bitnami/charts/pull/31290)等的新主要版本。添加了新的Kubernetes和容器解决方案，包括[Apache Superset](https://github.com/bitnami/charts/tree/main/bitnami/superset)、[ArangoDB Kubernetes Operator](https://github.com/bitnami/charts/tree/main/bitnami/kube-arangodb)、[CloudNativePG (PostgreSQL Operator)](https://github.com/bitnami/charts/tree/main/bitnami/cloudnative-pg)和[VictoriaMetrics](https://github.com/bitnami/charts/tree/main/bitnami/victoriametrics)。

在过去的18年中，Bitnami记录了：

- 在[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)和[Azure](https://news.microsoft.com/?utm_content=inline+mention)市场上，用户可以使用超过300,000个云镜像。
- 发布了超过200万个[容器](https://thenewstack.io/introduction-to-containers/)镜像版本。
- 发布了超过120,000个Helm charts。
Bitnami 的应用仍然非常强劲，如今每月启动超过 4200 万个云实例，并拉取超过 5 亿个容器镜像。

为了不辜负其座右铭 [“深受开发者喜爱。深受运维信任。”](https://bitnami.com/)，Bitnami 扩展了其对企业级安全和合规性的关注。

Bitnami 可完全自动化应用程序生命周期管理流程，从安装和配置到部署和完整堆栈更新。这允许在出现严重安全问题时实现更快的响应时间和 [MTTR（平均恢复时间）](https://thenewstack.io/to-improve-mttr-start-at-the-beginning/)。最近的一个例子是在官方发布后仅两个小时内，Bitnami 应用程序目录中的用户即可获得针对最新的 [Ingress-nginx 严重 CVE（2025-1974，或 IngressNightmare）](https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/03/25/ingress-nginx-cve-2025-1974) 的修复程序。

为了帮助保护软件供应链，Bitnami 实施安全最佳实践，并支持领先和最新的安全框架和法规，包括 SLSA（软件工件供应链级别）3 级合规性、签名、in-toto 证明、SBOM（供应链物料清单）以及防病毒和实时 CVE 扫描。最近，Bitnami 的商业产品 Bitnami Premium 和 Tanzu Application Catalog 发布了基于 distroless 镜像的 [运行时最小容器](https://blogs.vmware.com/tanzu/introducing-minimal-application-runtimes-in-tanzu-application-catalog-and-bitnami-premium/)，从而减少了攻击面并接近零 CVE。

## 社区的力量

如果没有其杰出社区的贡献，Bitnami 就不可能实现这一里程碑。无论您是开发人员、系统管理员还是云工程师，您的反馈、贡献和热情对于将 Bitnami 塑造成今天的样子都至关重要。

感谢多年来使用 Bitnami 解决方案的每个人（从小型初创公司到企业公司）对我们的信任。您的奉献和支持不断激励我们突破可能的界限。

## 展望未来：Bitnami 的未来

在我们庆祝成立 18 周年之际，我们已经展望未来。云计算、容器和 [DevOps](https://roadmap.sh/devops) 的世界正在迅速发展，Bitnami 团队致力于站在这些创新的前沿。与往常一样，我们将帮助开发人员和企业轻松地部署和管理他们的应用程序，无论是在云、容器还是 Kubernetes 中。让我们共同迎接未来 18 年的创新、协作和赋能全球开发人员！

[技术发展迅速，不要错过任何一集。 订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)