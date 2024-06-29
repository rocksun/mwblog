# Canonical 为 K8s 提供 LTS “无发行版” 容器化应用程序

![Canonical 为 K8s 提供 LTS “无发行版” 容器化应用程序的特色图片](https://cdn.thenewstack.io/media/2024/06/6123a22b-clay-banks-pho_ila8dgg-unsplash-1024x784.jpg)

Canonical 正在将长期支持 (LTS) 扩展到其旗舰 [Ubuntu Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) 发行版之外，承诺 [提供](https://canonical.com/blog/canonical-offers-12-year-lts-for-any-open-source-docker-image) 12 年的任何 [Docker](https://www.docker.com/?utm_content=inline+mention) 打包的开源软件的安全支持。

这些“无发行版”容器非常适合 Kubernetes 环境，它们可以在一个 Pod 中打包在一起，以实现最大的计算效率。

Canonical 将认证 LTS 容器在其自己的 [MicroK8s](https://thenewstack.io/microk8s-and-portainer-is-the-easiest-way-to-deploy-an-application-on-kubernetes/) 和 [Charmed Kubernetes](https://ubuntu.com/kubernetes/charmed-k8s) 平台上运行，这是自然而然的。

但 LTS 包也将由 Canonical 认证，可在其他主要的生产级 Kubernetes 环境中运行，例如 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) OpenShift（通过 [Red Hat Enterprise Linux](https://thenewstack.io/red-hats-new-linux-distro-brings-centos-closer-to-rhel/)），以及 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 的 K8s 平台：[Tanzu Kubernetes Grid](https://tanzu.vmware.com/kubernetes-grid) 和 [vSphere with Kubernetes](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/vsphere/vmw-vsphere7-solution-brochure.pdf)。

在公有云上，Canonical 将正式认证容器在 [Azure](https://news.microsoft.com/?utm_content=inline+mention)、[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)、[IBM](https://www.ibm.com?utm_content=inline+mention) 和 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 上运行。

这些镜像将基于标准化的 [Open Container Initiative](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/) (OCI) 格式构建，因此 LTS 容器应该可以在任何符合 OCI 的运行时环境中运行。

## Canonical 容器化 Deb 包

迄今为止，Canonical 使用 [deb 包格式](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html) 将应用程序放到其自己的 Linux 发行版 [Ubuntu](https://thenewstack.io/enable-automatic-updates-for-ubuntu-server/) 上。到目前为止，Ubuntu 和社区已经制作了超过 36,700 个 deb 包。“Deb” 来自 [Debian](https://thenewstack.io/build-a-debian-deb-file-from-your-projects-source/), 它是 Canonical 用于构建其自己的 Ubuntu 发行版的库存发行版。

许多这些打包在 deb 中的应用程序也已经使用 [Docker 和类似工具](https://thenewstack.io/docker-rolls-out-3-tools-to-speed-and-ease-development/) 容器化。

在这个新计划中，Canonical 将为任何以 OCI 格式（如 Docker）容器化的开源应用程序维护 12 年的安全维护。

许多开源应用程序已经可以在 [Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) 等网站上获得。对于这项服务，Canonical 甚至会接受将您最喜欢的开源应用程序“LTS”化的请求。它将分析您的应用程序依赖关系树，并将那些尚未被 Ubuntu Pro 覆盖的包纳入 LTS 维护。

为了支持专有应用程序，客户可以请求一个包含所有必要 [开源依赖项](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/) 的 LTS 基础镜像。

拥有 Ubuntu Pro 订阅的用户（前五个实例 [免费](https://ubuntu.com/pricing/pro)）可以使用支持的镜像，这些镜像将在需要时更新安全修复程序。相同的定价结构也将用于在其他认证平台（VMware、RHEL 和公有云主机）上运行“Everything LTS”容器。

此举还将为该公司自己的 Ubuntu Pro 发行版提供数千个新的开源上游组件，包括许多为运行生成式 AI 应用程序而新出现的应用程序，其中许多尚未打包在 deb 中。

## “无发行版”容器

常规容器，例如那些打包在 Docker 中的容器，通常可以在支持 Docker 的任何 Linux 发行版上运行。这些传统的容器仍然包含一些操作系统 (OS) 实用程序以供支持，例如 [Secure Shell](https://thenewstack.io/port-knocking-ubuntu-servers-or-containers-for-more-secure-ssh/) (SSH)，它允许用户登录到容器。
然而，无发行版容器仅包含运行应用程序所需的特定文件或二进制文件，从而减小了容器的大小，并减少了攻击者可用于利用软件的攻击面。不必要的软件包和元数据将被删除。

使用无发行版容器，容器没有 SSH。没有人可以使用“root”访问权限登录。容器化应用程序没有包管理器；它们无法更新。用行业术语来说，它们是真正的“不可变的”。当需要更新时，它们会被新副本替换。

此外，安装脚本、文档、头文件、有关其他依赖项的信息也消失了。相反，此类外部信息保存在称为切片的 YAML 文件中，与容器本身一起。

从头开始构建容器可能很棘手。Canonical 使用 [Debian Chisel](https://github.com/canonical/chisel) 工具为各种平台构建无发行版容器。


## 转向“无发行版”的好处
LTS 的主要优势是用户无需担心使用最新的安全修复程序来更新其应用程序。

该公司将修补发现 [CVE 注册漏洞](https://thenewstack.io/five-myths-about-cves/) 的任何应用程序。CVE 修补对于许多政府和行业安全授权是必需的，包括 FIPS、FedRAMP、欧盟网络弹性法案 (CRA)、FCC 美国网络信任标志和 DISA-STIG。

除了安全性之外，无发行版容器还有许多次要好处。它们可以更快地下载，并且启动速度更快。您可以在一台服务器中打包更多这样的容器。

总的来说，Canonical 估计无发行版容器可以提供 20% 到 25% 的整体性能提升。您仍然可以使用现有的容器构建系统来更新您的应用程序。

Canonical 与微软一起，已经创建了一组 [针对 .NET 用户的无发行版容器](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/)。

通过这种方法，.Net 容器被压缩了大约 100MB，压缩后大小为 6MB，两家公司估计。

## 来自 Red Hat 的可启动容器
Canonical 不是唯一一家重新思考如何为 [云原生计算](https://thenewstack.io/cloud-native/) 做 Linux 发行版的公司。今年早些时候，Red Hat 将其旗舰 Linux 发行版 RHEL 作为容器镜像启动。所有通常从容器中排除的操作代码（例如内核固件）都将包含在此镜像中。

在 5 月的 Red Hat 峰会上，Red Hat 技术人员演示了如何从 [Podman 容器管理控制台](https://thenewstack.io/deploy-a-pod-on-centos-with-podman/) 启动 RHEL 或在 OpenShift 下启动，甚至如何从镜像中刻录 ISO，以便它们可以在任何机器上启动。

尽管 Red Hat 的方法与 Canonical 的方法不同，但两者都在努力实现同一个想法：如何清除遗留操作系统杂乱，以在云环境中获得更好的性能。

Red Hat 希望在“容器方面使用最好的技术，我们可以将其带到操作系统世界，这样这两个世界就不会完全独立地管理，”Red Hat 高级首席营销经理 [Ben Breard](https://www.redhat.com/en/authors/ben-breard) 在 [Red Hat 峰会上的新闻发布会上](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/) 表示。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)