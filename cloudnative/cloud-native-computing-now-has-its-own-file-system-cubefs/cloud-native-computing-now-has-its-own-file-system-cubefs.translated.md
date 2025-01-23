# 云原生计算现在有了自己的文件系统：CubeFS

![云原生计算现在有了自己的文件系统：CubeFS的特色图片](https://cdn.thenewstack.io/media/2025/01/44ceb1c1-cubefs-1024x683.jpg)

基于Kubernetes的分布式系统如果没有一个合适的、能够清晰地将计算层和存储层分离的文件系统会怎样？

现在，[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)为其Kubernetes堆栈提供了一个高度可扩展的开源云原生分布式文件和对象存储系统，[CubeFS](https://cubefs.io/)（中文名“储宝”）。

中国电子商务和服务巨头[京东](https://corporate.jd.com/ourBusiness)于2017年启动了CubeFS项目，最初名为[ChubaoFS](https://thenewstack.io/chubaofs-the-cloud-native-computing-foundations-speedy-new-distributed-file-system/)，旨在[支持需要计算和存储分离的有状态应用程序](https://cubefs.io/blog/bestPractices/elasticsearch.html)。此后，它已在200多个生产环境中得到应用，其中许多是大型中国电子商务运营商。

中国消费巨头[OPPO](https://www.oppo.com/en/about/)使用CubeFS进行AI、大数据和存储计算分离。“CubeFS为各种场景和接口提供了丰富的功能，展现了良好的稳定性和持续迭代能力，带来了极佳的用户体验，”CubeFS工程师王红岩在一份声明中写道。

中国游戏公司网易也依赖这项技术。“该项目的稳定性以及清晰的范围和路线图赢得了网易的信任，使其成为其云原生基础设施需求的可靠组件，”网易的张锐在一份声明中写道。

总的来说，该文件系统[总共存储](https://github.com/kevin-wangzefeng/toc/blob/cubefs-graduation/proposals/graduation/cubefs-graduation-dd.md#adoption)了超过350PB的数据，涵盖了广泛的商业应用、云存储和在线媒体流。

## CubeFS毕业典礼

周二，CubeFS顺利毕业于CNCF评估流程，在这个流程中，开源技术必须证明其在多个云原生环境中的稳定性、成熟度和采用率。

CubeFS于2019年加入CNCF项目，迅速通过了沙箱和孵化阶段。为了毕业，该项目完成了一次安全审计，包括创建威胁模型以评估风险和入口点。还对代码中可能的漏洞进行了审查，并检查了供应链。

CNCF极大地帮助了该项目。自加入以来，CubeFS获得了许多新的贡献者，从5家公司的27个人增加到42家公司的379个贡献者。

## 云原生时代的存储系统

CubeFS是一个用于非结构化数据存储的多用途工具，尤其注重大数据、AI/LLM、容器平台以及其他将[计算层与存储层分离](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/)的架构。

它可以通过多种协议访问，例如亚马逊网络服务的[S3对象存储接口](https://thenewstack.io/why-you-might-bring-your-own-s3-bucket-byob-to-the-observability-party/)、大数据青睐的[HDFS](https://thenewstack.io/optimizing-compute-in-the-post-hadoop-era/)以及当今所有服务器都使用的[POSIX语义](https://thenewstack.io/google-cloud-offers-posix-compliant-file-storage-red-hat-gluster/)。它提供强一致性、完全隔离和多租户支持，以及CNCF所说的高度可扩展的元数据服务。

展望未来，该项目计划增加对分层存储和分布式缓存加速的支持。对于问题跟踪，该项目计划实现调用链跟踪。


[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)