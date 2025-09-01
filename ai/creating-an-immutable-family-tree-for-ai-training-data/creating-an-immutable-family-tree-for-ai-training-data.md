
<!--
title: 构建AI训练数据的不可变“族谱”
cover: https://cdn.thenewstack.io/media/2025/08/cabe56ba-chain123-3.jpeg
summary: 文章讨论了人工智能训练数据溯源的重要性以及面临的挑战，并介绍了 Hedera 等公司利用区块链技术提供可信数据来源记录的方案，强调了区块链在透明度、不可变性和去中心化等方面的优势，以确保人工智能的可信度。
-->

文章讨论了人工智能训练数据溯源的重要性以及面临的挑战，并介绍了 Hedera 等公司利用区块链技术提供可信数据来源记录的方案，强调了区块链在透明度、不可变性和去中心化等方面的优势，以确保人工智能的可信度。

> 译自：[Creating an Immutable 'Family Tree' for AI Training Data](https://thenewstack.io/creating-an-immutable-family-tree-for-ai-training-data/)
> 
> 作者：Susan Hall

每个公司都在竞相拥抱人工智能，这导致他们在训练中使用无数且常常文档不一致的数据集，从而引发了关于数据实际来源的法律和伦理问题。

[麻省理工学院的数据溯源倡议](https://www.media.mit.edu/projects/data-provenance-for-ai/overview/)对超过 1,800 个数据集的审计发现，公司无法可靠地追踪其人工智能训练数据的来源。事实上，研究人员已经得出结论，人工智能领域的[真实性、许可实践和溯源都已崩溃](https://mit-genai.pubpub.org/pub/uk7op8zs/release/2)，导致公司缺乏必要的[训练数据透明度](https://thenewstack.io/ethical-and-explainable-ai-are-startup-imperatives-in-2025/)，无法了解其人工智能模型的局限性。

[《纽约时报》对 OpenAI 的诉讼](https://www.reuters.com/legal/litigation/judge-explains-order-new-york-times-openai-copyright-case-2025-04-04/)以及[不断演变](https://thenewstack.io/regulating-ai-presents-confounding-issues/)的法规（如欧盟《人工智能法案》）正在增加公司在使用人工智能时正确实现数据透明度的压力。但证明训练数据的溯源并不一定明确，因为庞大而多样的数据集以以前无法想象的方式组合在一起。

总部位于德克萨斯州的区块链提供商 [Hedera](https://hedera.com/) 正在与人工智能治理初创公司 [EQTY Lab](https://www.eqtylab.io/) 以及芯片制造商 NVIDIA 和 Intel 合作，以提供可信的数据来源记录。

Hedera 联合创始人 [Leemon Baird](https://www.linkedin.com/in/leemon-baird/) 在一次采访中表示：“看到所有这些（与人工智能相关的）事情发生令人兴奋，但它发生得太快了，世界正在努力追赶。” “我认为这里蕴藏着巨大的潜力，但也存在一些出错的可能性，因此采取一些措施来确保人工智能的安全性非常重要。”

不仅数据可能被用于不良目的，而且还可能违反版权或许可规定。当数据集组合在一起时，就会形成“人工智能的整个族谱，以及所有影响它的不同[数据集]”，他说。

“如果你突然发现其中一个数据集有问题，你必须弄清楚，‘我必须将人工智能恢复到多早的版本才能找到没有问题的一个？’”他说。“如果有人查看过其中一些数据集并签署了，你需要知道是谁查看的，以及你是否可以证明他们签署了？”

它解决该问题的方案始于片上溯源跟踪架构。[NVIDIA](https://developer.nvidia.com/blog/confidential-computing-on-h100-gpus-for-secure-and-trustworthy-ai/#:~:text=NVIDIA%20Confidential%20Computing%20using%20hardware,is%20established%20through%20the%20following:) 和 [Intel](https://docs.scrt.network/secret-network-documentation/introduction/secret-network-techstack/privacy-technology/intel-sgx) 都使用[可信执行环境 (TEE)](https://thenewstack.io/confidential-computing-is-transforming-data-encryption-in-healthcare-finance/) 安全地存储密钥。当人工智能模型接受训练时，TEE 使用其私钥生成数字签名，以证明该模型的来源。此签名以加密方式证明该模型是由特定芯片上的特定数据集创建的。

接下来是 EQTY Lab 与 Intel 和 NVIDIA 合作创建的名为 [Verifiable Compute](https://www.eqtylab.io/blog/verifiable-compute-and-hedera) 的数字公证和证书系统，用于隔离敏感的人工智能操作，并为人工智能训练和推理中使用的每个数据对象和代码创建防篡改记录。源自 TEE 的一系列证明可用于描述整个人工智能管道。

该技术创建了一个详细的计算证明，以加密方式链接每个特定会话的输入、计算和输出，从而创建一个可审计的记录，准确记录每次所做的事情。这些证书可以涵盖不同的流程、计算环境以及不同组织所做的事情，从而创建数据的端到端沿袭记录。Verifiable Compute 还可以对数据强制执行业务策略和法规遵从性要求。

数据的数字签名以及有关训练数据和过程的元数据随后被记录在分布式账本上，例如开源 Hedera。这提供了对数据执行的每个操作的不可变、带时间戳且可公开验证的记录。该系统还可以通过链接溯源记录来跟踪模型的“族谱”，包括模型组合或进一步训练的情况。

Baird 认为区块链是证明数据溯源的理想方式。

“你可以将 Hedera 视为一个大型广告牌，世界上任何人都可以上来写东西，一旦你写了，我们保证它永远不会被删除，直到人类历史的尽头。我们会在旁边放一个小时间戳，说明它是什么时候写在那里的。没有人能够上来更改它，并且写在旁边的小时间戳永远不会被更改。这就是 Hedera。它是一个全世界都可以读取且永远无法更改的账本，你可以信任其中的时间。”

区块链提供：

* **透明度：** 公共账本允许任何人验证数据集或人工智能模型的来源。
* **不可变性：** 一旦写入，就无法更改或删除。该记录是永久性的且防篡改的。
* **去中心化：** 由多个独立组织使用，没有一个组织可以更改记录，这降低了恶意行为的风险。
* **时间戳：** 每个条目都带有可信的记录，记录其发生的时间。
* **无单点故障：** 只要大多数参与者是诚实的，数据仍然安全且准确。
* **支持复杂的溯源链：** 它可以跟踪复杂的历史，例如模型何时组合、重新训练或何时授予和撤销权限。

“你肯定知道全世界都在看到同样的东西，并且你确切地知道这件事发生在什么日期。没有人可以撒谎并假装过去发生过某件事，而实际上并没有发生。他们无法将日期倒填并说，‘哦，是的，这件事是早些时候完成的’，或者‘这件事是晚些时候完成的’，并假装它是早些时候完成的，”Baird 说。

“你可以确定你的人工智能是值得信赖的。它被写在拉什莫尔山上，全世界都可以看到你正在使用的人工智能模型是值得信赖的。如果你正在使用别人的 AI 并且想知道你是否可以信任它，你就可以这样做。老实说，我认为地球上的每个人都应该这样做。”