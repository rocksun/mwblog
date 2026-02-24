<!--
title: Red Hat 企业版 Podman Desktop 正面迎战 Docker Desktop
cover: https://cdn.thenewstack.io/media/2026/02/0db0afdd-arturo-esparza-sbobozi-awy-unsplash-scaled.jpg
summary: Red Hat发布了企业版Podman Desktop，旨在提供受支持的容器开发环境。它紧密集成OpenShift与RHEL，挑战Docker Desktop，为企业提供替代方案。
-->

Red Hat发布了企业版Podman Desktop，旨在提供受支持的容器开发环境。它紧密集成OpenShift与RHEL，挑战Docker Desktop，为企业提供替代方案。

> 译自：[Red Hat takes on Docker Desktop with its enterprise Podman Desktop build](https://thenewstack.io/red-hat-enters-the-cloud-native-developer-desktop-market/)
> 
> 作者：Steven J. Vaughan-Nichols

[Red Hat](https://www.redhat.com/en) 可能是企业级Linux领域中最大的名字，但由于其Kubernetes发行版 [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)，它也是一个主要的云原生参与者。然而，它一直没有自己的开源、面向容器的桌面应用程序的支持企业版本……直到现在。最近发布的 [Red Hat build of Podman Desktop](https://developers.redhat.com/products/red-hat-build-podman-desktop) 是该公司的一个赌注，即与OpenShift和Red Hat Enterprise Linux (RHEL) 的紧密集成将使 [Podman Desktop](https://podman-desktop.io/) 的容器原生工作流对企业开发人员具有吸引力。

Podman Desktop 是一个流行的开源Docker兼容容器引擎。它具有一个图形前端，使开发人员能够通过单一UI管理容器、镜像、Pod和本地Kubernetes。

## 为什么？

Red Hat 于2025年1月将其贡献给Cloud Native Computing Foundation，目前它是一个沙盒项目。那么，如果Red Hat已经支持Podman，为什么还要推出这个新版本呢？Red Hat表示，这是客户的要求。

该公司在其 [公告](https://www.redhat.com/en/blog/introducing-red-hat-build-podman-desktop-enterprise-ready-local-container-development-environments) 中写道：“直到现在，许多团队不得不依赖缺乏工作所需的服务水平协议 (SLA) 的不受支持的开源工具或替代方案。”“Red Hat build of Podman Desktop 是一个由供应商支持的解决方案，提供官方Red Hat支持，包括安全修复、产品工程师和容器专家的访问。对于IT决策者和平台工程师来说，这意味着更可预测的生命周期管理、安全补丁以及从第一天起就能管理数千个工作站上的容器工具的能力。”

Red Hat build of Podman Desktop 带来的是一个由供应商支持的适用于Linux、macOS和Windows的桌面应用程序。它包括对Red Hat支持、安全修复和产品工程的访问。

视频

## 企业级桌面容器管理

它被定位为“企业级本地容器开发”，目前处于技术预览阶段，并通过Red Hat的开发者渠道向合格客户提供。Red Hat将此产品定位为降低使用容器门槛的一种方式，它允许开发人员构建、运行和调试容器和Pod，而无需深厚的命令行知识，同时仍与企业平台和策略保持一致。

从技术上讲，这个新版本带来了——惊喜！——与OpenShift和本地Kubernetes环境更紧密的耦合。这一举动反映了Red Hat更广泛的战略，即让笔记本电脑成为生产集群的可靠替代品。

通过Podman Desktop GUI，开发人员可以将容器分组到Pod中，生成Kubernetes YAML，并部署到诸如Kind或Minikube等本地集群，以及部署到远程OpenShift集群和诸如 [Red Hat OpenShift Local](https://developers.redhat.com/products/openshift-local) 和 [Developer Sandbox](https://developers.redhat.com/developer-sandbox) 等服务。Red Hat 版本还增加了精选扩展，用于构建和测试符合Open Container Initiative标准的、与RHEL“镜像模式”相关的可启动容器镜像。

Red Hat还将此桌面客户端用作组织的一个策略执行点，以解决开发人员敏捷性与受限网络之间的冲突。通过这种企业级的Podman，管理员可以跨机器集群定义和部署默认配置，包括注册表镜像、内部注册表、HTTP代理和自定义安全证书。管理员还可以锁定关键设置，以便用户无法覆盖企业安全规则。该应用程序还在启动时验证托管配置。这有助于确保在您的开发人员下次打开其本地环境时，新的代理端点、证书更新或注册表策略得以强制执行。

虽然Podman Desktop作为上游项目已经存在了一段时间，但Red Hat明确针对那些希望获得 [Docker](https://www.docker.com/)-风格工作流而不依赖完整Docker工具链的组织。该桌面工具通过Podman的Docker命令别名支持 [Dockerfiles](https://docs.docker.com/build/concepts/dockerfile/) 和 [Docker Compose](https://docs.docker.com/compose/)。这将使从现有基于Docker的项目和脚本迁移变得更容易。

在 [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) 上，Podman已随订阅提供。Podman Desktop可以直接从RHEL扩展仓库安装，它作为Red Hat签名的软件与其他精选开发工具一同交付。以这种方式安装时，Podman Desktop会自动检测RHEL上底层的Podman引擎并与之绑定，提供一个图形前端，镜像了生产中使用的相同容器堆栈。

这个受支持的桌面版本发布之际，Red Hat正在更广泛地努力推广Podman及其生态系统，使其成为企业环境中Docker的一流替代品。在此之前，Red Hat已经将Podman和相关工具，例如 [Buildah](https://github.com/containers/buildah)、[Skopeo](https://github.com/containers/skopeo)、[bootc](https://bootc-dev.github.io/) 和 [Composefs](https://github.com/composefs/composefs) 等 [Podman Container Tools](https://www.cncf.io/projects/podman-container-tools/) 捐赠给了 [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/)。这使得Podman堆栈成为专有容器工具的社区治理对应物，同时为客户保留了受支持的路径。

尽管如此，Red Hat进入商业支持的容器开发环境市场较晚。[Docker Desktop](https://www.docker.com/products/docker-desktop/)、[Rancher Desktop](https://rancherdesktop.io/) 和 [Portainer Business Edition](https://www.portainer.io/blog/portainer-community-edition-ce-vs-portainer-business-edition-be-whats-the-difference) 已上市多年。另一方面，将Podman转变为一个受管理、策略感知的工作站环境，并融入以OpenShift为中心的管道中，在我看来，对于构建在Red Hat软件堆栈上的企业来说，这是一个非常有吸引力的选择。