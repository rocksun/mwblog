
<!--
title: Ceph：20年尖端的边缘存储技术
cover: https://cdn.thenewstack.io/media/2024/09/47f68405-ceph.png
-->

Ceph 最初是一个包含 40,000 行 C++ 代码的 Ceph 文件系统实现，现已发展成为全球组织使用的综合存储解决方案。

> 译自 [Ceph: 20 Years of Cutting-Edge Storage at the Edge](https://thenewstack.io/ceph-20-years-of-cutting-edge-storage-at-the-edge/)，作者 Steven J Vaughan-Nichols。

韩国水原 - CLYSO 首席技术官兼 Ceph 执行委员会成员 [Dan van der Ster](https://www.linkedin.com/in/dan-vanderster/) 在 OpenInfra Summit Asia 的主题演讲中表示，截至 2023 年，“82% 的开放基础设施用户报告称他们在使用 [Ceph](https://ceph.io/en/)”进行数据存储。然而，Ceph 最初只是加州大学圣克鲁兹分校（加州大学圣克鲁兹分校，加油香蕉蛞蝓！）的一个学生项目，由 [Sage Weil](https://www.linkedin.com/in/sageweil/) 作为其博士研究的一部分创立。

虽然 Ceph 最初只是 [Ceph 文件系统 (CephFS)](https://docs.ceph.com/en/reef/cephfs) 的一个 40,000 行 C++ 实现，但它已经发展成为一个全面的存储解决方案，被全世界的组织所使用。

然而，Ceph 从一开始就得到了主要机构的大力支持。从 2003 年到 2007 年，劳伦斯利弗莫尔国家实验室、桑迪亚国家实验室和洛斯阿拉莫斯国家实验室为 Weil 的初步工作提供了支持。当时的目标是为数据中心规模的高性能计算 (HPC) 工作负载创建一个水平可扩展的基于对象的 [文件系统](https://thenewstack.io/apptainer-a-container-system-for-high-performance-computing/)。

## 将智能推向边缘

为了做到这一点，Weil 采取了一种新颖的方法。其理念不是专注于管理大量“哑”磁盘，而是尽可能将智能推向边缘。此外，该设计还强调构建一致、可靠且没有单点故障的存储。

这些理念使得 Ceph 不同于当时的其它存储方法，例如 [Lustre](https://www.lustre.org/)、[Google 文件系统 (GFS)](https://research.google.com/archive/gfs-sosp2003.pdf) 和 [并行虚拟文件系统 (PFVS)](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/parallel-file-systems-for-hpc-storage-on-azure/ba-p/306223)。这包括以下特性：

1. **分布式对象存储**: Ceph 从一开始就被设计成一个分布式对象存储系统，即 [可靠的自主分布式对象存储 (RADOS)](https://www.oreilly.com/library/view/learning-ceph/9781787127913/68e88b41-adc3-411a-828d-6c96ab0c5d7a.xhtml)，而不是传统的文件系统。这使得它能够跨多个节点扩展到更大的容量。
2. **解耦数据和元数据**: Ceph 将文件元数据的管理与文件数据本身的存储分离开来。这通过允许元数据和数据操作独立处理来提高可扩展性。
3. **动态分布式元数据管理**: Ceph 使用一种称为 [动态子树分区 (DSP)](https://docs.ceph.com/en/reef/cephfs/dynamic-metadata-management/) 的新方法来自适应地在服务器之间分配元数据管理。这使得它能够随着系统的发展扩展元数据性能。
4. **CRUSH 算法**: Ceph 引入了 [可扩展哈希下的受控复制 (CRUSH)](https://ceph.com/assets/pdfs/weil-crush-sc06.pdf) 算法，以确定性地将数据放置在整个集群中。这消除了 [对集中式数据分配表的需要](https://thenewstack.io/3-reasons-we-need-data-protection-in-kubernetes/)。
5. **智能分布式对象存储**: Ceph 将数据迁移、复制、故障检测和恢复等任务委托给存储节点本身，从而使系统更加自主和可扩展。
6. **统一存储**: Ceph 的目标是从单一平台提供对象、块和文件存储接口，而不是为每个接口提供单独的系统。

然后，在 2007 年到 2011 年间，由 Weil 共同创立的网络托管公司 [DreamHost](https://www.dreamhost.com/) 成为了 Ceph 开发的关键支持者。在此期间，Ceph 的核心组件获得了稳定性，实现了新功能，并制定了未来路线图。Yehuda Sadeh-Weinraub、Gregory Farnum 和 Josh Durgin 等主要开发人员加入了该项目，为其快速发展做出了贡献。

正如 [红帽关于 Ceph 十年的历史](https://www.redhat.com/en/blog/ceph-turns-10-look-back) 所解释的那样，“随着 Sage 的研究接近尾声，他开始与许多传统存储供应商谈论 Ceph 以及他围绕该项目的工作。在目睹了许多同行被行业聘用，他们有趣且具有创新性的工作被抛弃或被大型专有系统吸收之后，他意识到这些行业巨头想要的是‘你’，而不是你的项目。”

![](https://cdn.thenewstack.io/media/2024/09/76778d58-ceph-arch.png)

## 存储领域的 Linux

作为开源的忠实信徒，Weil 希望 Ceph 成为“存储领域的 Linux”，并在 2012 年根据 [LGPL 2.1 版](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html) 授予 Ceph 许可。此外，他还不要求贡献者将其代码版权授予该项目。

与此同时，Weil 创立了 Inktank 来推广 Ceph 的广泛应用。此举为 Ceph 的实施带来了企业级的支持和专业知识。目标是提高 Ceph 的性能，使其能够投入生产，并为其提供支持。

当时，Ceph 在 Linux 上的速度并不快。它的客户端依赖于速度较慢的 [用户空间文件系统 (FUSE)](https://www.kernel.org/doc/html/latest/filesystems/fuse.html)，而不是 Linux 原生的文件系统。随着性能的提升，Linus Torvalds 在 2011 年将 Ceph 添加到 Linux 内核的主线 [2.6.34 内核](https://kernelnewbies.org/Linux_2_6_34) 中。

Inktank 成功地将 Ceph 从学术和研究机构推广到了企业。[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 意识到存储将变得越来越重要，看到了 Ceph 的发展，并决定在 [2014 年收购 Inktank](https://thenewstack.io/red-hat-seeks-to-bolster-openstack-position-with-inktank-acquisition/)。

在 Red Hat 的管理下，Ceph 成为面向企业的生产就绪软件，并提供专业支持和持续开发。在 Red Hat 收购 Inktank 的几个月内，它发布了一个重要的 Ceph 新版本。正如 Red Hat 首席执行官 Jim Whitehurst 当时在接受采访时告诉我的那样，“[Red Hat 希望为基础设施和平台即服务创建一个开源堆栈。](https://www.zdnet.com/article/red-hat-releases-inktank-ceph-enterprise-1-2/)”

多年来，Ceph 的技术一直在不断改进。[Ceph 12. Luminous 版本](https://docs.ceph.com/en/latest/releases/luminous) 是一个重要的里程碑。在此版本中，Ceph 引入了 [BlueStore](https://docs.ceph.com/en/latest/rados/configuration/storage-devices/)。这使您能够直接管理 SSD 和 HDD，而无需依赖传统的文件系统。这项创新极大地提高了 Ceph 的性能和效率。

由于 BlueStore 使用原始块设备和分区，因此它避免了可能限制性能或增加复杂性的中间 [抽象层](https://thenewstack.io/why-your-code-needs-abstraction-layers/)，例如本地文件系统。至于存储元数据，BlueStore 使用嵌入式 [RocksDB](http://rocksdb.org/) 键/值数据库。RockDB 包括对象名称到磁盘上块位置的所有重要映射。一个或多个校验和保护所有这些，以进一步 [保护数据](https://thenewstack.io/the-data-protection-challenges-of-kubernetes/) 和元数据。不会从磁盘读取任何数据或元数据并返回给用户，除非经过验证。

Ster 说，结果就是“神奇”，这始于 Ceph 的最初概念。“在存储的过去，您使用的是传统的体系结构，其中包含备用 IP 地址、虚拟 IP 和多路径。借助 CRUSH 和 DSP，您可以指定数据中心、机房和机架的位置，并制定有关数据放置位置的规则。该系统速度非常快，并且可以非常快速地计算对象的位置。这意味着您不需要大型数据库来记住所有对象的位置。您可以确定数据应该在哪里，并快速找到它。”

Ceph 还有自己的数据复制和可靠性方法。Ster 指出，有两种旧方法。一种是“复制磁盘，如果一个磁盘出现故障，您可以获得它的数据。另一种方法是复制对象。”这很有效，但他继续说道，“这两种方法都需要保留空的备用磁盘，这会浪费资源，也许更重要的是，恢复速度非常慢。”

“使用 Ceph，”Ster 说，“您可以将对象分组为小分组。在实践中，使用 Ceph，即使出现重大故障，我也从未在管理良好的集群上看到过数据丢失。因此，它不仅可以让您构建一个高度可用的系统，还可以确保如果集群中的任何组件出现故障，集群中的所有其他组件都能协同工作以复制数据。因此，在现实生活中，故障后的重建不需要几个小时。可能只需要一分钟，甚至 30 秒。”

## Ceph 基金会

有了这样的数字，也难怪现在有这么多公司在使用 Ceph。

不要认为 Ceph 的成功故事是由于 Red Hat 的支持。Ceph 社区对其成功起到了重要作用。2018 年，Linux 基金会推出了得到广泛支持的 [Ceph 基金会](https://ceph.io/en/foundation/)。许多公司和组织都在支持 Ceph。Weil 继续指导 Ceph 发展，这也是一件大事。

随着 Ceph 进入其第三个十年，它已成为各种环境（从企业部署到云基础设施）中的关键组成部分。展望未来，Ceph 正将自己定位为人工智能和机器学习的关键参与者。对于任何关心数据存储的人来说，Ceph 只会变得越来越重要。而且，现在 IT 领域的每个人都开始关注这一点。