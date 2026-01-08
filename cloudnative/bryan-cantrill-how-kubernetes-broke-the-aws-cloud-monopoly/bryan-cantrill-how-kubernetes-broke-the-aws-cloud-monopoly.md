<!--
title: 布莱恩·坎特里尔：Kubernetes如何粉碎AWS云垄断神话
cover: https://cdn.thenewstack.io/media/2025/12/cce06ebe-pragengineer-bryan_cantrill.jpg
summary: Bryan Cantrill认为，Kubernetes帮助GCP等新兴云提供商打破AWS垄断。它提供云选择，实现运营中立，促使多云兴起，对云市场民主化至关重要。
-->

Bryan Cantrill认为，Kubernetes帮助GCP等新兴云提供商打破AWS垄断。它提供云选择，实现运营中立，促使多云兴起，对云市场民主化至关重要。

> 译自：[Bryan Cantrill: How Kubernetes Broke the AWS Cloud Monopoly](https://thenewstack.io/bryan-cantrill-how-kubernetes-broke-the-aws-cloud-monopoly/)
> 
> 作者：Joab Jackson

Kubernetes 打破了[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)云的派对吗？

作为云原生硬件公司 [Oxide Computer Company](https://oxide.computer/) 的联合创始人兼首席技术官，Bryan Cantrill 从不回避表达自己的观点。在最近接受 [Pragmatic Engineer](https://www.youtube.com/@pragmaticengineer) 播客（由 Gergely Orosz 主持）的广泛采访中，他提出了一种观点，即在 AWS  relentlessly 统治市场时，Kubernetes 的发布对于推动 [谷歌云平台](https://cloud.google.com/?utm_content=inline+mention) 和其他新兴云提供商的增长至关重要。

“我认为，人们最初被 Kubernetes 吸引的部分原因是他们希望在云服务方面拥有一些选择性，并且觉得被 AWS 锁定了，”他说。

“有一段时间，我感觉要使用云服务，就必须实现每一个 AWS API。当时人们认为 Google 和 Azure 永远无法与 AWS 竞争，因为它们永远无法实现 API 兼容。”

Cantrill 擅长在正确的时间出现在正确的地点。1996 年从布朗大学毕业后，他进入了 [太阳微系统](https://thenewstack.io/sun-microsystems-a-look-back-at-a-tech-company-ahead-of-its-time/) 工作，当时公司都需要从那里购买服务器才能接入互联网。在那里，他帮助创建了 [DTrace](https://thenewstack.io/oxide-computings-bryan-cantrill-on-the-importance-of-toolmaking/)，这是一种强大的可观测性工具，最初是为 Sun 的 Solaris 操作系统（一个 [Unix 变体](https://thenewstack.io/unix-opensolaris-lives-on-in-this-openindiana-fork/)）开发的。

当甲骨文收购太阳微系统，[并于 2010 年完成收购](https://www.eweek.com/enterprise-apps/oracle-completes-sun-acquisition/)时，Cantrill 和许多 Sun 的技术人员一样，很快就离开了。他成为 [Joyent](https://thenewstack.io/joyent-makes-a-case-for-simplicity-not-openstack-complexity/) 的首席技术官，这是一家云服务公司，被宣传为对大型云服务商而言是工程师友好的替代方案。Cantrill 后来创立了 Oxide，销售用于运行内部云服务的服务器。

## AWS 巨头

Cantrill 回忆说，从 2010 年到 2014 年，在 Andy Jassy 的领导下，AWS 经历了一个“不懈执行”的时期。

2010 年，该公司仍被高德纳视为新兴的“远见者”。但到了 2014 年——亚马逊首次在其财报中公布 AWS 销售额——该公司带来了 [46 亿美元](https://www.sec.gov/Archives/edgar/data/1018724/000101872415000006/amzn-20141231x10k.htm) 的[收入](https://www.vox.com/2015/4/23/11561822/amazon-reveals-aws-is-a-nearly-5-billion-business-and-is-profitable)，并且拥有 [高德纳追踪的所有其他云提供商](https://virtualizationreview.com/blogs/the-schwartz-cloud-report/2014/06/gartner-iaas-report.aspx) 容量的五倍左右。

它似乎是不可战胜的。每年在 [AWS Re:Invent](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025/) 用户大会上，该公司都会宣布降价和数量惊人的新服务。展厅里的供应商会突然发现自己正在与 AWS 刚刚宣布的某个新服务竞争（据说，甚至有些供应商直接收拾展位，在中途就离开了）。

“如果你是 AWS 的竞争对手，你就会害怕 Re:Invent，因为又会有一次降价。如果你是 AWS 的合作伙伴，你也会害怕 Re:Invent，因为又会宣布一项与你正在开发的产品竞争的新服务，”Cantrill 回忆道。

金融记者会记得，在 2014 年之前的季度财报中，亚马逊没有专门公布 AWS 的收益。通常，公司会模糊这些数字以掩盖糟糕的业绩。Cantrill 认为，AWS 实际上恰恰相反。它隐藏其云收入是因为业绩太好，并且将其重新投资到零售业务中。

Joyent 当时正在与 AWS 竞争提供公共云服务，因此该公司看到了这项业务的丰厚利润。

“我们运营着一个公共云，我们知道公共云的经济效益。利润很好。”

事实上，Joyent 几个最主要的客户都是与亚马逊直接竞争的零售商，[例如沃尔玛](https://www.tritondatacenter.com/blog/nodejs-at-joyent)，并且大概不愿意使用竞争对手的云服务。

“零售商会说，‘如果你认为我会把我的钱花在 AWS 上，让亚马逊来和我开战，那就算了，’" Cantrill 推测。

## 内部运行云的力量

像财富 500 强公司这样，在内部构建自己的“私有”云的想法，对许多人来说似乎是一个有吸引力的替代方案，特别是当客户看到他们的 [AWS 账单增长](https://thenewstack.io/the-great-aws-outage-the-11-billion-argument-for-kubernetes/)时。

Joyent 拥有用于运行云的开源软件，即 [SmartOS](https://www.datacenterknowledge.com/open-source-software/joyent-open-sources-smartos-for-the-cloud)，一个 OpenSolaris 的变体，它允许企业使用通用硬件拼凑自己的云系统。Cantrill 说，三星在 2016 年 [收购](https://news.samsung.com/global/samsung-to-acquire-joyent-a-leading-public-and-private-cloud-provider) 了这家公司，纯粹是为了支持其自身的云运营。

这对于三星来说可能是一个明智的举动，尽管这次收购让其他企业在自主掌控云方面少了一个选择。

当时的其他选择包括 [Mesosphere](https://www.datacenterknowledge.com/cloud/mesosphere-kubernetes-to-meld-into-google-s-cloud) 和 [Docker Swarm](https://www.msn.com/en-us/news/technology/kubernetes-may-be-the-better-choice-but-docker-swarm-makes-more-sense-for-home-labs)。许多人认为，与 AWS 竞争的最佳方式是复制 AWS 自己的 API。这是在一个名为 [Eucalyptus](https://www.eucalyptus.cloud/) 的开源项目中完成的，该项目 [于 2014 年被惠普收购](https://www.datacenterknowledge.com/cloud/hp-buys-aws-compatible-cloud-builder-eucalyptus)。

## Kubernetes 登场

在与 Orosz 的讨论中，Cantrill 认为，正是 [Kubernetes 的推出](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/) 容器编排引擎在 2014 年实现了云市场的民主化，即使它一开始并未被广泛使用（现在它是继 Linux 之后第二大开源项目）。

当时，谷歌提供了云服务，但在内部，它们与特定的硬件紧密绑定。根据 [描述该技术的一份原始论文](https://people.eecs.berkeley.edu/~brewer/cs262b/TACC.pdf)，Kubernetes 作为一个项目应运而生，旨在实现“基于集群的可扩展网络服务”。[当时 Docker 的出现](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/)，得益于 [容器](https://thenewstack.io/containers/)，使得每个工作负载都能拥有自己的 IP 地址。

Kubernetes 的承诺在于它 [提供了配置基础架构的能力](https://thenewstack.io/docker-versus-kubernetes-start-here/)，但又不与特定的硬件平台绑定。你不再需要编写 AWS API。应用程序可以根据 Kubernetes API 构建，理论上可以在任何云提供商上运行，从而实现某种形式的运营云中立。

“我敢说，在 Kubernetes 之前，多云服务并不真正存在，”Cantrill 说。事实上，该项目许多早期贡献者都是受到 [这种云中立理想](https://thenewstack.io/why-open-platforms-are-the-future-of-kubernetes-deployments/) 的驱动。

## 为什么谷歌要开源 Kubernetes？

谷歌最初为何要开源 Kubernetes，这个从其内部 [Borg 平台](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/) 分离出来的项目，仍然有些神秘。

当然，[开源任何项目都有其好处](https://youtu.be/vBjonut1JMk?t=994)，例如代码库和安全性方面的更多贡献。

但发布一个开源项目以鼓励云中立也具有竞争意义，至少从谷歌的角度来看是这样。

“我认为，人们在内部争论的焦点是鼓励云中立，因为‘我们是那个有东西可以赢的人’，”Cantrill 说。

谷歌甚至向 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 提供了启动资金，于 2015 年创立了 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention)，以 [独立管理](https://www.cncf.io/announcements/2015/06/21/new-cloud-native-computing-foundation-to-drive-alignment-among-container-technologies) Kubernetes 及相关的开源技术。

尽管如此，谷歌云平台此后已在市场中站稳脚跟。目前，GCP 每年单独为 Alphabet 带来约 [600 亿美元](https://seekingalpha.com/article/4823341-alphabets-next-growth-cycle) 的收入。

AWS 仍然是最大的提供商，拥有约 [30% 的云市场份额](https://holori.com/cloud-market-share-2026-top-cloud-vendors-in-2026)，尽管市场本身已膨胀为 [如今万亿美元的市场](https://www.visualcapitalist.com/the-worlds-largest-cloud-providers-ranked-by-market-share/)，并有更多样化的参与者获得了市场份额。

“这完全要归功于 Kubernetes 吗？不，但我认为它肯定发挥了重要作用，”Cantrill 说。