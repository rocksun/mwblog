<!--
title: Amazon S3 Files：为全球最大的对象存储赋予文件系统能力
cover: https://cdn.thenewstack.io/media/2026/04/85f256ca-img_3509-scaled.jpg
summary: AWS 推出 S3 Files 功能，允许通过 NFS v4.1 协议将 S3 存储桶作为原生文件系统访问。该方案基于 EFS 技术而非 API 模拟，支持毫秒级延迟及多端并发协作。
-->

AWS 推出 S3 Files 功能，允许通过 NFS v4.1 协议将 S3 存储桶作为原生文件系统访问。该方案基于 EFS 技术而非 API 模拟，支持毫秒级延迟及多端并发协作。

> 译自：[Amazon S3 Files gives the world's biggest object store a file system](https://thenewstack.io/aws-s3-files-filesystem/)
> 
> 作者：Frederic Lardinois

Amazon S3 现在可以作为一个文件系统了。周一，AWS 发布了一项名为 S3 Files 的新 S3 功能，使 S3 存储桶可以作为原生文件系统访问，支持 NFS v4.1+ 操作，如创建、读取、更新和删除文件。在今天的公告中，AWS 的 Sébastien Stormacq 称其为“首个且唯一一个为您的数据提供全功能、高性能文件系统访问的云对象存储”。

S3 Files 将任何 AWS 计算资源（包括 EC2 实例、ECS 和 EKS 容器、Fargate 任务和 Lambda 函数）直接与已存储在 S3 中的数据连接。数据保留在 S3 中，也可以通过 S3 的常用 API 访问。

值得注意的是，这并不会将 S3 变成一个你可以从桌面或其他云提供商本地挂载的文件系统。例如，它不会让你把 S3 存储桶挂载为 Finder 文件夹。

Stormacq 写道，在 S3 之上的文件系统“非常适合多个计算资源——无论是生产应用程序、使用 Python 库和 CLI 工具的代理式 AI 代理，还是机器学习 (ML) 训练流水线——需要协同读取、写入和更改数据的工作负载。”

## S3 从未弥补的鸿沟

AWS 拥有足够的文件存储服务，足以让“云架构师在架构评审会议中乐在其中”，Stormacq 坦言。他指出，S3 Files 专门用于对已经存在于 S3 中的数据进行交互式、共享式访问。

根据 AWS 的说法，S3 目前在数百个艾字节 (exabytes) 中存储了超过 500 万亿个对象。从一开始，该服务就被构建为一个对象存储平台，但开发人员很快意识到，利用其近乎无限的扩展性作为应用程序文件系统基础的潜力。

像 s3fs-fuse 和 Goofys 这样的开源项目使用 FUSE 将标准文件操作转换为 S3 API 调用。然而，这些工具往往较慢，且由于 S3 的限制，无法支持文件锁定，并将重命名视为复制加删除操作。其他选项如 [ObjectiveFS](https://objectivefs.com/) 和 [JuiceFS](https://juicefs.com/en/) 提供完整的 POSIX 语义，但需要单独的元数据基础设施。

AWS 也看到了这里的潜力。作为 Storage Gateway 家族的一部分，S3 File Gateway 多年来一直提供对 S3 的 NFS 和 SMB 访问——但它是一个混合云工具，专为连接到 S3 的本地环境设计。

2023 年，该公司还推出了开源的 Mountpoint for S3，这是一个高性能的 FUSE 客户端，针对云原生、读密集型工作负载进行了优化。它比 s3fs 更快，但仍然无法进行就地编辑、目录重命名或文件锁定。

## 基于 EFS 构建，而非 S3 API

通过 S3 Files，AWS 采取了不同的方法。S3 Files 并非在 S3 API 之上构建文件系统仿真，而是使用 Amazon Elastic File System (EFS)，这是该公司的托管 NFS 服务，长期以来一直是 AWS 针对需要在多个计算实例之间共享文件访问的工作负载的解决方案。

AWS 并没有试图让 S3 API 的行为像文件系统，而是直接在 S3 存储上分层了一个生产级文件系统。EFS 已经提供对 NFS v4.1 的支持，具有亚毫秒级的读取延迟，并支持数千个客户端的并发访问。根据 AWS 的说法，S3 Files 为活跃使用的数据提供了类似的约 1ms 延迟。

S3 Files 的一个有趣方面——开发人员可能并不喜欢——是缓存架构分为两层。受益于低延迟访问的文件会自动放置在文件系统的高性能存储中。对于低延迟访问不是首要任务的文件（例如大型顺序读取），S3 Files 直接从 S3 提供服务以最大化吞吐量。

该系统还支持智能预取，用户可以控制是加载完整文件数据还是仅加载元数据，从而针对特定的访问模式进行优化。
S3 Files 将适用于任何现有的通用 S3 存储桶。无需进行任何迁移。