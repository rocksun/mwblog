
<!--
title: 谷歌云平台集成 Lustre 并行文件系统
cover: https://cdn.thenewstack.io/media/2025/07/43779f13-lustre-architecture.png
summary: Google Cloud推出托管Lustre并行文件系统服务，提供高性能数据吞吐，适用于大规模AI和HPC工作负载。该服务与NVIDIA合作，并与其他Google Cloud服务集成，提供不同吞吐量级别的计费选项，并构成Google HPC堆栈的一部分。
-->

Google Cloud推出托管Lustre并行文件系统服务，提供高性能数据吞吐，适用于大规模AI和HPC工作负载。该服务与NVIDIA合作，并与其他Google Cloud服务集成，提供不同吞吐量级别的计费选项，并构成Google HPC堆栈的一部分。

> 译自：[Google Brings the Lustre Parallel File System to Its Cloud](https://thenewstack.io/google-brings-the-lustre-parallel-file-system-to-its-cloud/)
> 
> 作者：Joab Jackson

[Google Cloud](https://thenewstack.io/need-a-trillion-parameter-llm-google-cloud-is-for-you/) 现在提供完全托管的 [Lustre 并行文件系统](https://wiki.lustre.org/images/6/64/LustreArchitecture-v4.pdf)版本。[Google Cloud Managed Lustre 服务](https://www.ddn.com/press-releases/google-cloud-launches-general-availability-of-managed-lustre-powered-by-ddns-exascaler-technology/)于 7 月 8 日在全球范围内上线（“全面可用”）。

[Lustre](https://www.lustre.org/) 是一款开源、高性能的文件系统，长期以来一直用于高性能计算（或[超级计算](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/)）系统，用于天气建模等大规模工作。

Google 将其 Lustre 产品定位为一种降低运行[这些超级计算作业](https://cloud.google.com/products/managed-lustre?hl=en#high-performance-computing-hpc) 负担的方式。Lustre 每秒传输速度高达 TB 级的数据能力也使其对[大规模 AI 作业](https://cloud.google.com/products/managed-lustre?hl=en#artificial-intelligence-ai-or-machine-learning-ml-workloads)具有吸引力。那些饥渴的 GPU 需要喂养；没有大量数据，就无法实现通用人工智能。

此服务提供每个命名空间 1TB/s 的读取吞吐量，延迟小于 1 毫秒。

部署可以从 18TiB 开始——一个 tebibyte 是 2 的 40 次方字节（或[非常接近 1TB](https://simple.wikipedia.org/wiki/Tebibyte)）——并且可以扩展到 8PiB 或更多。

通过此次发布，Google Cloud 在提供基于云的 Lustre 方面赶上了其他云提供商。它与 [Azure Managed Lustre](https://azure.microsoft.com/en-us/pricing/details/managed-lustre/)、[AWS](https://aws.amazon.com/?utm_content=inline+mention) 的 [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) 和 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 的 [OCI File Storage with Lustre](https://www.oracle.com/cloud/storage/file-storage-with-lustre/) 竞争。

但这项服务带有一些特殊的优势：它严重依赖 [EXAScaler](https://www.ddn.com/products/lustre-file-system-exascaler/)，这是一种针对吞吐量和可扩展性优化的 Lustre 部署，这要归功于与 [DDN](https://www.ddn.com/about-us/) 的合作。

“[NVIDIA](https://thenewstack.io/nvidia-gtc-2025-wrap-up-18-new-products-to-watch/) 加速计算产品总监 [Dave Salvator](https://www.linkedin.com/in/davesalvator/) 在一份声明中表示：“通过整合 DDN 的企业级数据平台和 Google 的全球云能力，组织可以轻松访问海量数据，并充分释放 AI 的潜力。”

换句话说，Lustre 可以帮助保持那些 NVIDIA GPU 的繁忙。

## Lustre 的方式

Lustre 由卡内基梅隆大学研究员 [Peter J. Braam](https://www.braam.io/) 于 1999 年专门为 HPC 系统创建，旨在解决超级计算对极高吞吐量的需求。当时，传统的网络文件系统（如 [NFS](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/)）难以扩展到 HPC 所需的级别。

Lustre 是一种并行文件系统：文件本身被分片到多个服务器上以实现更快的访问，并且每个服务器可以同时传输其比特。

每个文件的元数据（文件位置、权限、目录层次结构等）单独保存在元数据服务器上，该服务器还控制文件系统操作，如创建和删除文件，并消除服务器级别的 I/O 瓶颈。

## 它的成本是多少？

Google 的 Lustre 服务在全球范围内提供四种不同的吞吐量级别：对于每 TB 数据，分别为 125 MB/s、250 MB/s、500 MB/s 和 1000 MB/s。每个命名空间可以大到 1PB。

托管的 Lustre 实例按 1 秒的增量计费，具体取决于实例的配置容量。例如，在 125MB/s 层级上存储一个 gibibyte 每月将花费 0.145 美元。

有一个[专门的页面](https://cloud.google.com/products/managed-lustre/pricing?hl=en) 介绍定价：

[![screenshot of prices](https://cdn.thenewstack.io/media/2025/07/51a50693-lustre-pricing-1024x270.jpg)](https://cdn.thenewstack.io/media/2025/07/51a50693-lustre-pricing-1024x270.jpg)

托管的 Lustre 定价示例列表 (Google)。

托管的 Lustre 与其他 Google Cloud 服务（如 Google Cloud Compute Engine、Google Kubernetes Engine (GKE)、IAM、VPC Service Controls 和 Google Cloud 的 Vertex AI 平台）原生集成。

## Google HPC 堆栈

在 Google Next 25 大会上，Google HPC 和 AI 基础设施解决方案经理 [Wyatt Gorman](https://www.linkedin.com/in/wyattgorman/) 进一步讨论了托管的 Lustre 产品。

他说，Google 设置该服务是为了使“暂存空间尽可能靠近计算资源”。

托管的 Lustre 产品提供持久的暂存空间，但在会议上，Gorman 还谈到了 [Parallelstore](https://cloud.google.com/parallelstore?hl=en)，这是一项建立在开源 [DAOS 项目](https://daos.io/) 之上的补充服务，它将提供超快的*非持久性*暂存空间。

![](https://cdn.thenewstack.io/media/2025/07/1768c07c-google-managed-lustre-1024x569.png)

理想的 Google HPC 堆栈还应包括 [H4D CPU VM](https://cloud.google.com/blog/products/compute/new-h4d-vms-optimized-for-hpc)（目前处于预览阶段），它们基于 AMD 的 EPYC 处理器和支持 RDMA，以及基于 Terraform 的 [Cluster Toolkit](https://cloud.google.com/cluster-toolkit/docs/overview)，用于可重复的部署。

有关 Google HPC 堆栈的更多信息，请查看[完整的 Google Next HPC 演示文稿](https://cloud.withgoogle.com/next/25/session-library?session=BRK2-019)。