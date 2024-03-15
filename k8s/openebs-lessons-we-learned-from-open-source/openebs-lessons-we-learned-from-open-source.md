<!--
title: OpenEBS：我们从开源汲取的经验教训
cover: https://cdn.thenewstack.io/media/2024/03/06b38d46-trees-1024x576.jpg
-->

历经四载，我们的开源项目最终被CNCF归档，这一过程给我们留下了宝贵的教训，值得任何准备踏上开源之路的公司借鉴。

> 译自 [OpenEBS: Lessons We Learned from Open Source](https://thenewstack.io/openebs-lessons-we-learned-from-open-source/)，作者 Ed Robinson 是一位经验丰富的企业家、首席执行官和公司董事，在开源和专有企业软件方面拥有丰富经验。他目前正在就 OpenEBS 产品和项目策略的各个领域为 DataCore Software 提供建议。

[OpenEBS](https://thenewstack.io/how-openebs-brings-container-attached-storage-to-kubernetes/) 是一个针对 Kubernetes 的数据存储框架，使得 Kubernetes 容器可以访问位于集群中任何位置的存储，并自动提供诸如自我修复存储、复制卷、克隆和快照等弹性服务。

如果没有 OpenEBS，容器只能访问本地节点存储或位于集群外部的存储。由于其有用性，每天有 500,000 到 1,000,000 人[使用 OpenEBS 来管理](https://thenewstack.io/tutorial-install-and-configure-openebs-on-amazon-elastic-kubernetes-service/)他们 Kubernetes 集群中的存储。

DataCore Software 在 2021 年收购了 OpenEBS 背后的公司。我们对 OpenEBS 的经验，从最初作为云原生计算基金会 (CNCF) 沙箱项目开始，到四年后被 CNCF 归档，为任何着手开源的公司提供了宝贵的经验教训。

## 教训 1:了解开源背后的目的

除非你是一家拥有无限资源的大公司，否则大多数中型企业都根据投资回报率 (ROI) 来衡量他们的投资——那些可以带来有形回报的计划。这与开源形成了自然的张力:你是急于将其货币化？还是承认你正在投资于一个具有长期效益但较难衡量 ROI 的社区？对我们来说，我们当时并不知情。这是我们第一次尝试。

OpenEBS 曾经是一个 CNCF 项目，有大约 350 位贡献者，但 90% 的代码都是由 DataCore 开发人员编写的——存储框架基于对磁盘上的物理块进行数据存储编排。这是一门低级火箭科学，每个组件的开发都需要数年时间。要保持发展势头，你需要一个专门的团队来构建这些低级组件。从社区中获取专业知识和时间承诺并不容易。

DataCore 有 20 名全职工程师致力于 OpenEBS 项目，贡献了 90% 的代码。我们应该怎么做？我们是否应该急于将其货币化？投资于 Kubernetes 社区就足够了吗？我们如何衡量收益？对我们来说，我们当时并不知情。

## 教训 2:保持真实

有人认为所有软件都应该是免费的。有人认为所有软件都应该收费。或许答案介于两者之间——开源和专有软件在未来的公司中都应该有一席之地。个人和公司都应该有选择的权利。对我们来说，我们的真理，我们的目的是成为 OpenEBS 的驱动力，确保这个广受欢迎的 Kubernetes 数据存储项目拥有闪电般的速度、功能齐全、企业级质量和永久免费。同时，我们也为需要支持和企业集成的公司提供商业选择。

这听起来很简单，但我们花了数年时间来理解这一目的。开源的一个挑战是"商业化"是一个肮脏的词。专有软件的一个挑战是"开源"是一个肮脏的短语。作为一个社区，我们需要克服这一点。

## 教训 3:归档后的生活

OpenEBS 项目已被 CNCF 归档([你可以在这里阅读相关信息](https://github.com/cncf/toc/issues/1051))。对于许多人来说，归档后会发生什么并不清楚。对我们来说，我们仍有 20 人在致力于该项目;我们仍在 Slack 频道和 GitHub 上回答问题;人们仍在使用 OpenEBS 并贡献代码。最大的区别在于，CNCF 的项目生命周期为项目提供了未来，保证项目将继续下去。当使用开源项目的人们投入数年时间，并基于开源项目构建自己的软件时，他们就依赖于该项目，需要知道它会继续存在。作为 CNCF 的沙箱、孵化或毕业项目可以提供这种确定性。但归档项目则无法提供。

## 做出改变并重新尝试

作为一个项目，我们对每一个为 OpenEBS 贡献过代码的人、每一个基于 OpenEBS 构建自己软件的人、每一个相信我们的人都负有责任。作为一个项目，我们承认我们写出了出色的代码，但并没有运营一个良好的符合 CNCF 要求的项目。两者都是必不可少的。

[开源给予](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/)人们自由创新、尝试新事物并接纳来自世界各地任何人的新想法。我们的项目被归档了。怀着社区的精神，为服务于数十万使用 OpenEBS 的人，我们将重新尝试。

要了解有关 Kubernetes 和云原生生态系统的更多信息，请于 3 月 19 日至 22 日在巴黎与我们相聚，参加 KubeCon + CloudNativeCon Europe 大会。
