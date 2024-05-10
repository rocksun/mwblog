
<!--
title: Red Hat重新思考容器时代的Linux发行版
cover: https://cdn.thenewstack.io/media/2024/05/0a999618-denver-bear.jpg
-->

Red Hat 希望将基于云原生的构建和部署实践引入 Linux 操作系统本身。

> 译自 [Red Hat Rethinks the Linux Distro for the Container Age](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/)，作者 Joab Jackson。

丹佛 — 正如您使用容器快速启动应用程序一样，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 希望让启动整个基于 Linux 的操作系统变得同样容易。

该公司已将其旗舰 Linux 发行版 [Red Hat Enterprise Linux](https://thenewstack.io/red-hat-enterprise-linux-8-1-released-with-live-kernel-patching/) (RHEL) 作为容器映像启动。换句话说，通常从容器中遗漏的所有操作系统代码（例如内核固件）都将包含在此映像中。

该公司在其年度用户大会 [Red Hat Summit](https://www.redhat.com/en/summit) 上宣布了这些举措，本周在丹佛举行。

“这是整个行业需要的，”Red Hat 高级首席软件工程师 Colin Walters 在峰会上的一次会议中解释道。“您使用云原生工具越多，而不是为基础设施构建一个独特的 bin，您就越能利用该开源维护和共享所有权。”

这种方法不同于该公司的典型包模式，其中新 RHEL 版本的最终副本作为独立包发布，以安装在服务器或虚拟机上，然后由管理员通过针对特定工作负载的自定义进行修改。

这种包模式 [长期以来一直是 Linux 发行版社区的传统](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)，与如今通过容器管理应用程序的方式越来越不同。

这个想法是“我们可以在容器方面学到的经验教训，我们可以带到操作系统世界，以便这两个世界不会完全分开管理，” [Ben Breard](https://www.redhat.com/en/authors/ben-breard)，Red Hat 高级首席营销经理在 Red Hat 新闻发布会上说！[](https://cdn.thenewstack.io/media/2024/05/983df5d9-red_hat-waters-02-1024x576.jpg)

![](https://cdn.thenewstack.io/media/2024/05/983df5d9-red_hat-waters-02-1024x576.jpg)

*基于容器的 Linux 操作系统的目标，来自 Colin Walters 的演示*

## 更广泛的工作负载

此举是为了使 RHEL 对更广泛的工作负载更具灵活性。RHEL 黄金映像仅适用于某些环境。许多环境，例如边缘或虚拟桌面环境，最终需要自定义不同的位。

容器化将极大地帮助简化对这些自定义环境的更新。Red Hats 声称，这使得测试和回滚变得更加容易。

管理员可以在构建时配置操作系统，而不是在操作系统安装后对其进行更改。[GitOps](https://thenewstack.io/gitops-git-push-all-the-things/) 或 [持续集成/持续部署](https://thenewstack.io/ci-cd/) 工作流对开发人员来说已经很熟悉，可以成为维护运行在不同环境中的 Linux 服务器集群的标准程序。

事实上，所有云原生工具都用于维护操作系统。

## 不仅仅适用于临时工作负载

这不是第一次尝试在容器中构建操作系统：[RancherOS](https://thenewstack.io/rancher-labs-releases-rancheros-general-availability/)、[Flatcar Linux](https://thenewstack.io/tutorial-install-flatcar-container-linux-on-remote-bare-metal-servers/)、[Talos](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/) 和 [CoreOS](https://thenewstack.io/coreos-open-cloud-services/)（[2018 年被 Red Hat 收购](https://thenewstack.io/red-hat-will-acquire-coreos-greater-kubernetes-presence/)) 等都采用了这种方法。

此版本的新增功能是一个名为 [boot.c](https://github.com/containers/bootc) 的新软件，它使用与 Docker 通过多层构建应用程序容器相同的 [开放容器计划](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) (OCI) 标准对可启动主机系统的组件进行分层。

Breard 说，该版本“包括内核固件和历史上你应该从容器中遗漏的所有东西”。因此，“我们现在可以使用几乎每个人内部都有的标准容器工具管理版本并部署完整操作系统。”

这项工作实际上源自 [合并到 OpenShift](https://thenewstack.io/coreos-says-red-hat-will-help-introduce-openshift-to-operators/) 中的 CoreOS 功能。2020 年，Red Hat [重命名](https://www.redhat.com/en/technologies/cloud-computing/openshift/what-was-coreos) CoreOS Container Linux 操作系统为（有点令人困惑）[Fedora CoreOS](https://fedoraproject.org/coreos/)，“容器优化操作系统”。
与早期的基于容器镜像的系统不同，Red Hat 的系统不会完全是短暂的。用户数据将保留在 `/etc` 目录中，同时根据需要更新其他组件。

Walters 解释说，这种方法对于必须保留某些系统和应用程序数据的大多数系统来说最有价值。

![](https://cdn.thenewstack.io/media/2024/05/983df5d9-red_hat-waters-02-1024x576.jpg)

*Colin Walters 在演讲中提出的基于容器的 Linux 操作系统的目标。*

**声明：Red Hat 支付了记者参加此次会议的差旅费。**
