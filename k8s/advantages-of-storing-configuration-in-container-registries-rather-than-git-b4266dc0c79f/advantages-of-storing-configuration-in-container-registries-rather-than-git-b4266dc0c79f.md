
<!--
title: 将配置存储在容器registry而非Git中的优势
cover: ./cover.png
-->

除了Git，甚至可以替代Git，为什么您应该考虑将配置文件存储在容器注册表中？

> 译自 [Advantages of storing configuration in container registries rather than git](https://itnext.io/advantages-of-storing-configuration-in-container-registries-rather-than-git-b4266dc0c79f)，作者 Brian Grant。

将配置文件和包存储在 Git 中非常常见。有时它们与源代码一起提交，有时与其他配置包一起存储，有时则位于它们自己的存储库中。

将部署配置与源代码一起存储最初看起来很方便，但在部署时会导致许多挑战，例如源代码和配置的[权限耦合和 Git 触发器](https://codefresh.io/blog/argo-cd-best-practices/)、跨环境的冲突分支和推广策略、多组件部署的协调等等。当将配置单独存储时，在 Git 中执行配置编辑的繁琐工作变得更加明显：克隆、分支、编辑、添加、提交、推送、创建变更请求、审查、合并、标记。

无论哪种方式，为了部署一组配置文件（例如使用 Helm），有时会将其复制到对象存储、工件注册表或容器注册表，通常来自 CI 过程，但在某些情况下也可能[自动构建](https://docs.docker.com/docker-hub/builds/)或[镜像](https://cloud.google.com/artifact-registry/docs/repositories/remote-overview#user-defined-upstreams)。此类存储库满足生产部署系统的可扩展性、性能、可靠性、网络访问、安全性和数据驻留要求，并且对于某些场景（例如[边缘部署](https://medium.com/@briankgrant/is-gitops-actually-useful-a1c851ba99d8)）特别有用。图像也可以缓存、复制和对等分布。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dNirX8ROJ66-9XUztOYjfA.png)

*通过容器注册表部署配置*


如果我们要将配置推送到此类存储库，为什么不一开始就将其存储在那里呢？镜像可以模拟[草稿（更改）和修订](https://github.com/kptdev/kpt/blob/main/docs/design-docs/07-package-orchestration.md)，并且可以像 Git 提交一样进行版本控制和引用，既有不可变的内容摘要，也有用户定义的标签。

使用容器注册表进行通用[工件存储](https://github.com/oras-project/oras)存在一种[更广泛的趋势](https://blog.andyserver.com/2024/03/kubecon-eu-2024-a-model-conference/)。毕竟，容器镜像本质上是一组文件的捆绑包。（能够[将镜像作为卷挂载到 Kubernetes 中运行的容器中](https://github.com/kubernetes/kubernetes/issues/831)本来是很好的，但这又是另一个问题。）许多工具都已支持[OCI](https://opencontainers.org/)注册表，包括[Helm](https://helm.sh/docs/topics/registries/)、[Config Sync](https://cloud.google.com/blog/products/containers-kubernetes/gitops-with-oci-artifacts-and-config-sync)、[Flux](https://fluxcd.io/flux/cheatsheets/oci-artifacts/)、[timoni](https://timoni.sh/#oci-artifacts)、[Crossplane](https://docs.crossplane.io/latest/concepts/packages/)和[Tekton](https://github.com/tektoncd/community/blob/main/teps/0005-tekton-oci-bundles.md)。

原因之一是它们的普遍性。部署到容器运行时的团队已经需要访问存储库。此外，注册表 API 和身份验证方法比对象存储或 Git 提供商[更标准化](https://github.com/opencontainers/distribution-spec)。这使得它们更容易集成。因为镜像比包含配置包的[典型 Git 存储库](https://medium.com/@briankgrant/monorepos-vs-many-repos-is-there-a-good-answer-9bac102971da)更细粒度、更集中的文件捆绑包，并且它们可以使用有关其内容的信息进行[注释](https://github.com/opencontainers/image-spec/blob/main/annotations.md)，所以容器注册表中的配置包比位于 Git 存储库子目录中的配置包更容易发现、列出和过滤。

容器注册表还支持许多管理和治理功能，这些功能对可部署资产（如配置包）非常有益。例如：

- 丰富的元数据：一些注册表支持[各种元数据](https://cloud.google.com/artifact-analysis/docs/metadata-management-overview)，包括来源、[SBOM](https://www.cisa.gov/sbom)、证明、部署事件等等。
- 签名：可以[签名](https://www.sigstore.dev/)镜像以确保真实性。
- 策略执行：可以验证和要求各种镜像属性。

此外，将来，一旦我们自动化了大多数配置生成和更改，配置就会成为生成的工件。在这种情况下，Git 会失去大部分价值，因为用户不会直接与它交互。这也适用于[渲染清单模式](https://akuity.io/blog/the-rendered-manifests-pattern/)。

鉴于容器镜像有很多优势，希望将来会有更多用户将其作为配置文件和软件包的权威来源，并有更多工具支持它。

也就是说，一旦我们自动化了大部分配置更改，我们就应该从根本上重新思考配置工具链，以及我们是否真的想把自己逼到这个角落里。例如，将配置推送到更高可用性的存储系统根本不会改进变更控制流程。

您是否将配置模块、模板或软件包视为其他可部署构建工件，还是直接从其真实来源应用它们？您在[GitOps 控制器](/is-gitops-actually-useful-a1c851ba99d8)中是否遇到直接从您的 git 提供商拉取配置的挑战？您是否发现难以[跟踪所有包含可部署配置的 git 仓库](/the-insidious-problem-of-configuration-sprawl-66360fce6ca3)？您是否发现难以[保持这些仓库的最新状态](/making-mass-changes-to-infrastructure-as-code-b1edea2f7c48)？您尝试过将配置存储在容器镜像中吗？它比其他方法更好吗？这看起来仍然显得不必要地麻烦吗？

欢迎在此回复，或通过[LinkedIn](https://www.linkedin.com/in/bgrant0607/)或[X/Twitter](https://x.com/bgrant0607)给我发消息，我计划将此内容交叉发布。

如果您觉得这篇文章有趣，您可能还会对我的[基础设施即代码和声明式配置系列](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836)中的其他文章感兴趣。