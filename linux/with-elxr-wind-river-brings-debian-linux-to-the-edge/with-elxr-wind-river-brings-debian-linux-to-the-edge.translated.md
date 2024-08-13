# eLxr 助力 Wind River 将 Debian Linux 带到边缘

![eLxr 助力 Wind River 将 Debian Linux 带到边缘的特色图片](https://cdn.thenewstack.io/media/2024/08/ce349d59-elxr-1024x683.png)

长期嵌入式系统提供商 [Wind River Software](https://www.windriver.com/) 推出了面向新一代边缘部署的企业级 [Linux](https://roadmap.sh/linux) 发行版。

Wind River 工程师并没有升级公司的 [Wind River Linux](https://www.windriver.com/products/linux) 发行版（过去 20 年来一直针对传统嵌入式系统，尤其是电信领域），而是构建了一个新的发行版，以匹配新兴的云原生环境，这些环境使用异构的、计算能力有限的边缘计算设备，运行在远程部署的设备中。

这个名为 [eLxr](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/10/8f56c2943b0cc46647a279257325aa02b409f6516a42a5cecce8a2c7d370b665) 的发行版将基于 Debian，但也将包含高级功能，如空中升级 (OTA)、[软件物料清单 (SBOM)](https://thenewstack.io/a-good-sbom-is-hard-to-find/)、边缘处理、预测性维护和数据聚合。该发行版在 [MIT 开源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 下发布。

Wind River 的计划不是直接管理该项目，而是让 eLxr 由社区驱动。

Wind River 首席技术专家 [Mark Asselstine](https://www.linkedin.com/in/mark-asselstine-88b3367/?originalSubdomain=ca) 在接受 The New Stack (TNS) 采访时表示，该项目的目标是实现“边缘到云”。

该发行版旨在减少边缘计算市场的碎片化，大型组织已经收集了无数的软件和硬件变体，所有这些变体都必须独立管理，因此效率不高。一个统一的堆栈，用于边缘设备和支持它们的云服务器，可以大大简化管理。

Asselstine 说，eLxr 背后的理念是“我们如何以不同的方式来处理它，以便您可以拥有一个供应商和一个操作系统，可以涵盖从边缘到服务器的所有情况”。

Asselstine 上周在韩国釜山举行的 [DebConf](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/11/ac7384b252db4c31af258a49acb502950007a7f08859ded708692c4ca52688b3) 上介绍了该发行版，并在 [技术演示](https://gemmei.ftp.acc.umu.se/pub/debian-meetings/2024/DebConf24/debconf24-337-a-unified-approach-for-intelligent-deployments-at-the-edge.av1.webm) 中进行了展示。

## eLxr 的起源

eLxr 源于另一个 Wind River Linux 项目 [StarlingX](https://www.starlingx.io/)，这是一个基于云原生的 Linux 发行版。[OpenInfra Foundation 项目](https://www.openstack.org/) StarlingX 已经成为许多大型电信提供商的首选，他们使用它来管理其 5G 网络上的数千个节点。

StarlingX 最初基于 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 CentOS。但 Red Hat [更改了该发行版](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/)，采用 [流式模型](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/)，即更新一经发布就会立即安装。

考虑到快速更新的不稳定性，StarlingX 无法迁移到流式模型，因此决定将基础迁移到 Debian。

开发团队发现 [Debian](https://thenewstack.io/build-a-debian-deb-file-from-your-projects-source/) 将是运行边缘设备的合适基础。[Debian](https://www.debian.org/) 已经发布了 30 年的稳定版本，并且不受任何拥有自身议程的企业实体控制。

在将 StarlingX 迁移到 Debian 之后，Wind River 的开发团队想要一个用于“边缘到云”操作的 Linux 发行版。

对于 Wind River 来说，边缘设备不仅仅是交换机、路由器、复用器和其他网络设备，而是整个工业和零售嵌入式设备领域。这将包括从销售点机器到医疗设备的所有设备：任何具有互联网连接且比基本可编程逻辑电路 (PLC) 具有更多计算能力的设备。

这些边缘系统比云服务器有更多限制。它们可能在低功耗环境中运行，或者在 CPU 能力或内存方面受到限制。连接性和带宽可能有限，这可能会缩短应用安全更新的时间窗口。

Asselstine 在他的演讲中说：“大多数二进制 Linux 发行版并不一定能解决边缘设备的问题。”

eLxr 的另一个区别在于它将高度依赖现代构建和运行时工具，例如 [Docker](https://www.docker.com/?utm_content=inline+mention) 和 [GitLab](https://about.gitlab.com/?utm_content=inline+mention)。
Asselstine hopes that this cloud-native tool will also attract a younger generation of contributors. As TNS freelance writer [Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/) has pointed out elsewhere, open source has an [aging problem](https://www.theregister.com/2024/07/15/opinion_open_source_attract_devs/), with fewer and fewer maintainers.

“We want to get young people involved in operating systems again,” Asselstine told TNS.

## How eLxr Works

For standard distributions like Debian, an image is installed on the device, and then a specific environment is configured by removing and [adding necessary packages](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/).

This approach doesn’t work for edge devices because the package manager software must be installed locally.

“When you deploy to edge devices, you don’t always have access to a package manager. You also don’t want to use a package manager to do updates,” Asselstine told TNS.

So, eLxr takes the opposite approach: developers create a manifest to build a pre-configured image, which can then be downloaded and installed.

eLxr uses [OSTree](https://ostreedev.github.io/ostree/introduction/) to update packages as atomic commits. So, in your build system, you can commit a single package, such as [systemd](https://thenewstack.io/unix-greatest-inspiration-behind-systemd/) or libc, to update. “The manifest will allow you to only include the parts you need,” Asselstine said.

In the future, eLxr will provide some level of support for SBOMs, although the team is still figuring out what that will entail. They are reviewing the work that Debian has done. Their goal is to provide an SBOM when the user creates the final image.

## Building eLxr from Source

Wind River engineers are able to use the [Yocto Project](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/8/b7800902d2d7cdb166fb16abd424cc1950c8c5d7d00a8aadd005ff1147f282dc) and [Buildroot](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/9/3616e3de5686889026350160d6c05e8d79ffc15d2c8bba9a9fbda0df7add778f) to assemble distributions and generate software development kits (SDKs) for cross-platform toolchains.

The Yocto Project, started by Wind River and Intel in 2011, can be thought of as a distribution builder, providing users with a way to build custom images from source. It can even generate an SDK for the distro it produces.

Yocto is great for building operating systems for custom environments. The downside is that building a distribution requires a lot of work. eLxr can significantly simplify this process.

eLxr will adopt an “upstream first” release strategy. It follows the [Debian release cycle](https://wiki.debian.org/DebianReleases), with releases expected to come out a few months after Debian releases.

Currently, eLxr is built on the [latest](https://wiki.debian.org/DebianReleases) Debian “Bookworm” release, and when Debian releases its next version, “Trixie,” eLxr will release its own version within three to four months.

Core engineers will be working on Debian’s testing release, enabling them to contribute their features and fixes back to the Debian community.

## eLxr in the Community

Discussions are still ongoing about how to establish long-term and commercial support for eLxr.

Wind River is still working to make rLxr a truly community-driven project, working out details like governance and contributor models.

But overall, the idea is that “Wind River doesn’t have to control the project, and we can benefit from it,” Asselstine said.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don’t miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)