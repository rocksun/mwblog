<!--
title: Nscale 收购 Anyscale：对多云中立性意味着什么？
cover: https://cdn.thenewstack.io/media/2026/07/49f41857-eva-corbisier-pi4bgnllrrg-unsplash-scaled.jpg
summary: Nscale 以约 16.5 亿美元收购 AI 工作负载扩展专家 Anyscale，旨在打造全栈 AI 云平台。此举引发了关于云中立性的争议，分析认为虽然 Anyscale 仍支持多云，但“在某处运行效果最佳”的性能差异可能导致事实上的供应商锁定。
-->

Nscale 以约 16.5 亿美元收购 AI 工作负载扩展专家 Anyscale，旨在打造全栈 AI 云平台。此举引发了关于云中立性的争议，分析认为虽然 Anyscale 仍支持多云，但“在某处运行效果最佳”的性能差异可能导致事实上的供应商锁定。

> 译自：[Nscale just bought Anyscale. Here's why it matters for multi-cloud neutrality.](https://thenewstack.io/nscale-anyscale-acquisition-neocloud-lockin/)
> 
> 作者：Adrian Bridgwater

云平台公司 [Nscale](https://www.nscale.com/) 本周宣布，已达成收购 AI 工作负载扩展专家 [Anyscale](https://www.anyscale.com/) 的最终协议。此举引发了一项新的考验：云中立的 AI 软件在与 GPU 新云（neocloud）结合后，是否还能保持中立。

此次收购将 Nscale 的基础设施能力（涵盖 GPU、数据中心、功耗控制系统以及执行 AI 服务的应用层）与 [Anyscale 用于跨数据处理、训练、推理和强化学习的 AI 工作负载扩展软件层](https://thenewstack.io/anyscale-new-optimized-runtime-for-ray-kubernetes-operator/) 进行了整合。

Nscale 认为这是“两家高度互补的公司”的结合。Nscale 收购 Anyscale 可能会从根本上改变由此产生的商业模式。

## 这是 GPU 新云锁定的开始吗？

需要记住的是，[Nscale 是一家 GPU 新云厂商](https://www.reuters.com/business/ai-cloud-provider-nscale-buy-software-startup-anyscale-2026-07-30/)（一种运行裸金属 GPU 并针对 AI 和机器学习工作负载优化基础设施的专业云服务提供商），这意味着它运行着自己的 GPU 密集型数据中心和软件栈。与此同时，Anyscale 是一个独立、云中立的软件编排多云控制平面，适用于任何云超大规模厂商……但现在它归属于一家单一的新云厂商。

这听起来不太像[云中立](https://thenewstack.io/the-next-stages-of-ai-conformance-in-the-cloud-native-open-source-world/)和不可知论；这听起来更像是一个垂直整合的 AI 云服务提供商的命题。

Nscale 首席产品官 [Dan Bathurst](https://www.linkedin.com/in/danielbathurst/) 告诉 *The New Stack*，Anyscale 平台“将继续作为一个独立的品牌和产品存在”，包括继续支持在 AWS、GCP、Azure 和其他云厂商上进行“自带云”（BYOC）部署。

> “我们希望在性能上胜出，而不是靠任何形式的供应商锁定或强迫任何人选择 Nscale 作为基础设施提供商。”

“但真正改变的是——或者说正在改变的是——客户现在也有了这个第一方选择，他们可以让 Anyscale 在 Nscale 集群上运行，作为一个全栈、高度优化的解决方案。我们希望在性能上胜出，而不是靠任何形式的供应商锁定或强迫任何人选择 Nscale 作为基础设施提供商，”Bathurst 说道。

他坚称，确保软件工程团队能够利用他们想要运行的工作负载轻松实现目标，符合 Nscale 的利益。

“对我们来说，现有的承诺将会延续，所以 Anyscale 的价值确实在于它能满足计算已经存在的场景，”他说。“我们希望在性能上胜出，而不是靠任何形式的供应商锁定或强迫任何人选择 Anyscale 作为基础设施提供商。”

## 平台层中立，基础设施层差异化

Bathurst 请用户将其视为“平台层中立，基础设施层差异化”，因为这两个组织的结合是一个全栈方案。

“差异化来自于 Nscale 与 Anyscale 完全垂直整合的事实。因此，如果用户想要那个第一方选项，他们可以选择 Anyscale 并获得最优化的解决方案，因为显然，我们正在设计、优化和共同设计从电力到数据中心再到应用层的每一层堆栈。这是一个非常独特的命题，但我们不会强迫任何客户接受它，”Bathurst 确认道。

并非所有人都相信该公司承诺保持一个不可知且中立的开放平台。分析师机构 SanjMo 的首席分析师、前 Gartner 数据与分析研究副总裁 [Sanjeev Mohan](https://www.linkedin.com/in/sanjmo/) 告诉 *The New Stack*，Anyscale 在其最佳功能和最优定价首先落地于 Nscale 的那一刻起，“就不再是一个中立的参与者了”。

> “软件仍然可以在任何地方运行，但‘随处运行’和‘在某处运行效果最好’是两回事，买家会感受到性能和成本上的差距。到那时，中立性就仅仅是一个标签而已。”

## 随处运行，但……在某处运行效果最好

“软件仍然可以在任何地方运行，但‘随处运行’和‘在某处运行效果最好’是两回事，买家会感受到性能和成本上的差距。到那时，中立性就仅仅是一个标签而已，”Mohan 说。

他认同整合软件和计算将产生可衡量的成本、性能和可靠性收益。Mohan 解释说，这是“交易中最强大的部分”，因为 Nscale 同时控制着硅片和 Anyscale 的控制平面，它可以以计算中立的 Anyscale 永远无法做到的方式，同时调整调度、内存和网络。

## Anyscale 对 Ray 的商业支持

Anyscale 由 [Ray](https://www.anyscale.com/product/open-source/ray?utm_source=the%20new%20stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns%20platform) 的创建者创立，Ray 是一个开源项目，提供分布式计算框架，旨在将 Python 工作负载扩展到任何基础设施上的实时生产应用程序任务和服务中。

[Ray 于 2025 年捐赠给了 PyTorch 基金会](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/)。Anyscale 继续为其提供商业支持服务，其中包括一条通往 100% 托管云基础设施和无服务器自动扩缩容的“零运维”途径，使在生产环境中创建、部署和监控机器学习工作流变得更加简单。

Anyscale 支持跨公共和私有云环境的数据处理、模型训练、批处理推理和 LLM。尽管这一切看起来很开源，但我们是否仍在滑向更狭窄的专有渠道，或者是开发者最终将不得不面对更深层应用和服务依赖的潜在威胁？

“我不这么认为，主要是因为该平台的工作方式旨在跨各种不同的云和不同的基础设施进行编排。它就像一个异构的分布式计算平台。所以该平台将永远保持多云特性，”Nscale 的 Bathurst 确认道。

## 定价变数与超大规模厂商的传闻

当被问及任何即将到来的定价变化或主要云超大规模厂商对 Nscale 现在成为一个可信替代者的可能反应时，Bathurst 和他的团队表现得非常谨慎（考虑到这是收购协议宣布的第二天，这或许是可以理解的）。

一向友好的分析师 Mohan 则更为健谈，他说：“所有只在 Nscale 硬件上出现的优化都是一种依赖。因此，两种观点都有理由。独立的编排软件和独立的工具供应商正在被任何拥有 GPU 的人所吸收，因为只有当你同时控制两者时，经济学才成立。预计这种情况会更多，”Mohan 强调道。

他解释说，Nscale “现在成为了一个真正的专业云服务提供商替代者”，即它不是像 AWS、Azure 和 Google Cloud 那样拥有从数据库、数据仓库到容器编排再到 AI/ML 流水线技术等大量托管服务的通用型提供商。然而，他确实看到了 Nscale 在大规模原始训练和推理领域成为强力玩家的空间。

## 从加密货币到云端竞争者

总部位于英国伦敦的 Nscale 成立于 2024 年，其前身是一家加密货币挖矿企业。

正如所暗示的，Anyscale 将作为 Nscale 大家庭的一部分保留其品牌名称，该公司重申其立场，即客户今天“可以自由选择运行其 AI 工作负载的云基础设施”。

该公司的初步新闻稿表示，“随着时间的推移”，用户将获得在 Nscale 全栈 AI 平台上运行 Anyscale 软件层的额外选项。

## 第一个全栈 AI 超大规模云厂商？

“企业正在超越仅仅使用 AI 的阶段，转而开始构建自己的 AI。做好这一点需要软件及其运行的基础设施协同设计，”Anyscale 首席执行官 [Keerti Melkote](https://www.linkedin.com/in/keertimelkote/) 在宣布收购的新闻稿中表示。

Melkote 将基于 Ray 构建的 Anyscale 平台与 Nscale 的数据中心、计算和 AI 云服务结合，定义为“第一个全栈 AI 超大规模云厂商”，即一个能以更大规模运行任何 AI 工作负载的厂商，以便更多的软件工程团队可以构建和拥有自己的 AI 应用程序和服务。

通过此次收购以及 Nscale 与 Anyscale 软件层的融合，该组织旨在扩大其客户群。该公司目前的工作涵盖了从医疗保健、电子商务到机器人等各个垂直领域。它表示，其全栈产品将帮助企业加快图像和文档处理速度，基于其私有数据微调 LLM，并在内部使用开源模型部署 AI 智能体。

该交易尚需满足成交条件并获得监管部门批准，预计于 2026 年下半年完成。交易的财务条款未披露，尽管据[路透社报道](https://www.bloomberg.com/news/articles/2026-07-30/nscale-to-buy-ai-software-startup-anyscale-for-1-65-billion?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc4NTQxMDIyNywiZXhwIjoxNzg2MDE1MDI3LCJhcnRpY2xlSWQiOiJUSVhaU0hLSkg2VkUwMCIsImJjb25uZWN0SWQiOiJEQ0FGMjNFM0YyMkE0Qzk5OTM0RUMyRDEwNkM0ODc0NyJ9.1hChskM6Twv1RarQXZnJwXh8vZCjp_93Gr18w86cZ1I&leadSource=article-gifting)，一位知情人士表示交易价格“约为 16.5 亿美元”。

AWS、Google Cloud 和 Microsoft Azure 的代表均已收到联系并被邀请就此事发表评论。