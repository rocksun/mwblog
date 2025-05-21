
<!--
title: 数据共享空间可以拯救开放人工智能
cover: https://cdn.thenewstack.io/media/2025/05/8ea39356-erik-mclean-rtysoc1bks0-unsplash-scaled.jpg
summary: 开源AI崛起，数据成瓶颈！FineWeb、Dolma等数据集涌现，但专有AI利用未公开数据引争议。需从剥削转向协作，构建数据公共资源，如BlueSky用户意图框架。Current AI等机构应支持数据共享，推动数据集创新，保障AI的开放性、透明性和公正性。
-->

开源AI崛起，数据成瓶颈！FineWeb、Dolma等数据集涌现，但专有AI利用未公开数据引争议。需从剥削转向协作，构建数据公共资源，如BlueSky用户意图框架。Current AI等机构应支持数据共享，推动数据集创新，保障AI的开放性、透明性和公正性。

> 译自：[Data Commons Can Save Open AI](https://thenewstack.io/data-commons-can-save-open-ai/)
> 
> 作者：Alek Tarkowski

今年将被铭记为开源AI系统取得突破的一年。人们的情绪已经从过去两年主导公共辩论的对开源AI相关风险的恐惧，转变为其他。DeepSeek的开放权重模型的发布再次证明了[“没有护城河”](https://semianalysis.com/2023/05/04/google-we-have-no-moat-and-neither/)，并且开放解决方案既可以与封闭的基础模型竞争，又可以支持开放开发生态系统中的创新。

近几个月来，新的模型、版本和衍生物的稳定开发流已经成为常态。毫不夸张地说，开源AI模型正在蓬勃发展。

不幸的是，在这种背景下，我们看到了一个突出的问题：数据格局停滞不前。即使每个人都同意数据是构建更好AI系统所需的关键资源，但在公共或开放训练数据集方面进展甚微。

## 开放数据在哪里？拥抱爬取

2024年更重要的数据集发布之一是[HuggingFace的FineWeb](https://github.com/huggingface/fineweb-2)，被称为“网络所能提供的最好的15万亿个token”。它是Common Crawl转储的清理和优化版本，Common Crawl转储几乎是所有LLM的库存训练数据来源。另一个主要版本，AI2的[Dolma数据集](https://allenai.org/dolma)，也改进了Common Crawl数据，并将其与选定的开放数据源相结合。

开放数据集的最新进展显示了在没有法律约束的情况下构建完全开放的AI模型的希望。法国初创公司Pleias创建了[Common Corpus](https://huggingface.co/blog/Pclanglais/common-corpus)，这是一个仅基于允许许可来源的LLM训练数据集。Spawning创建了[PD12M](https://huggingface.co/datasets/Spawning/PD12M)，这是一个包含超过1200万个图像-文本对的公共领域数据集。

虽然这些进步有利于AI开发并支持开源AI的创建，但它们主要侧重于通过聚合和改进从现有资源中提取最大价值。

## 专有AI数据的未言明的成本

开源AI开发仍然处于持续的劣势。发布封闭[模型但不披露数据](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)来源的私有AI实验室正在利用各种类型的专有数据或他们没有合法依据重复使用的数据。来自开放源代码促进会（OSI）的Stefano Maffulli[将此描述为](https://opensource.org/blog/open-data-and-open-source-ai-charting-a-course-to-get-more-of-both)剥削人们生成的数据，并将其输入到以一定价格授予访问权限的专有系统中。

数据共享的风险很高，并且超出了与AI训练相关的问题。[Stefan Verhuulst认为](https://sverhulst.medium.com/are-we-entering-a-data-winter-f654eb8e8663)，我们可能正在进入“长期的数据寒冬”。虽然企业AI实验室继续依赖各种专有数据来源，但我们看到数据共享正在减少的信号：[Web域正在限制](https://www.dataprovenance.org/consent-in-crisis-paper)与AI相关的Web爬网的访问，并且社交网络正在删除甚至存在的有限形式的数据访问。数据寒冬对于缺乏购买专有数据所需预算的开源AI开发人员来说尤其困难，对于他们来说，数据透明度和访问原则甚至进一步限制了他们可以使用的数据源。

## 从剥削到协作

什么样的集体行动可以帮助防止数据寒冬，同时加强将数据共享与负责任的治理相结合的方法，确保数据质量并保护数据权利？

去年夏天，[开放源代码促进会](https://thenewstack.io/open-source/)和Open Future召集了一组专家来探讨这一挑战并提出前进的道路。最近发布的一份会议报告“[开源AI中的数据治理](https://opensource.org/wp-content/uploads/2025/02/2025-OSI-DataGovernanceOSAI-final-v5.pdf)”认为，需要采取集体行动来发布更多数据并改善数据治理，以平衡开放共享与负责任的发布。
我们需要两种范式转变。首先，人工智能开发者不能再像过去那样，孤立地构建数据集，将大量的知识、文化和信息视为可以转化为 tokens 的原始资源。数据集必须被视为解决人工智能开发挑战和满足其他利益相关者需求的工具。这首先需要与档案馆、研究机构、文化组织和公民项目所拥有的各种开放和公共收藏的管理人员和所有者进行合作。

其次，我们需要在 [开放数据的基础](https://thenewstack.io/linux-foundation-overture-maps-the-globe-with-open-data/) 上继续发展，但越来越多地将数据视为一种公共资源。开放数据方法 [对于人工智能开发具有巨大的价值](https://www.genai.opendatapolicylab.org/)，尤其适用于公共资源。然而，许多类型的数据可能很有用，但开放共享 [未能充分防止数据](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/) 被利用。我们需要各种数据共享和治理模型来平衡开放性和控制。在 2024 年初，一个有前景的数据信托试点不是由人工智能实验室发起的，而是一家美术馆：Serpentine Labs 创建了一个数据信托来管理 [the Choral AI dataset](https://arxiv.org/html/2412.01433v1)，这是一个合唱团录音的集合。

## 下一场革命不会是数据抓取

我们需要超越数据抓取范式，以及这两种转变的需求，可以通过 BlueSky 的例子来说明。[该平台通过一个特别适合机器使用的开放 API 公开分享数据](https://thenewstack.io/google-cloud-adds-genai-core-enhancements-across-data-platform/)。2024 年底，[一位 HuggingFace 数据档案管理员下载了 100 万条帖子](https://www.404media.co/bluesky-posts-machine-learning-ai-datasets-hugging-face/)，并将它们打包成一个公开可用的训练数据集。几天后，由于 BlueSky 用户反对他们的数据被使用，该数据集被撤下。因此，BlueSky 开始开发一个用于细粒度表达 [“用户数据重用意图”](https://github.com/bluesky-social/proposals/tree/main/0008-user-intents) 的框架，目前正在与用户社区进行协商。

希望一种改进的使用 BlueSky 数据进行人工智能训练的方法将成为开源人工智能开发者所需的主要数据集创新，并展示参与式治理和公共资源的价值。

## 建立集体力量，保持人工智能的开放性、透明性和公正性

虽然许多技术挑战仍然与数据质量和偏差、数据透明度或环境可持续性等问题有关，但多个团队正在开放的开发生态系统中解决这些问题。

它们需要机构支持，以确保数据公共资源工作的可持续性。在巴黎的人工智能峰会上，[the Current AI initiative](https://www.currentai.org) 启动，初始预算为 4 亿美元，重点是数据共享而不是人工智能开发。这创造了一个建立新的数据公共资源生态系统的机会，使其像开源人工智能生态系统一样成功。

在很大程度上，我们将在开源人工智能领域看到的真正创新不在于模型，而在于数据集。我们必须尽一切努力确保未来的数据集建立在具有管理和控制的数据公共资源之上。