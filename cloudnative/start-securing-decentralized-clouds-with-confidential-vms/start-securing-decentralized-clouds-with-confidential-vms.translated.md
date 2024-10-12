# 使用机密虚拟机开始保护去中心化云

![使用机密虚拟机开始保护去中心化云的特色图片](https://cdn.thenewstack.io/media/2024/10/f0c8c787-fabrizio-conti-athvihiobko-unsplash-1024x683.jpg)

[Fabrizio Conti](https://unsplash.com/@conti_photos?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/white-clouds-AtHvihIObKo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上。

尽管加密和网络安全不断改进，但数据泄露事件却[逐年增多](https://www.statista.com/statistics/273550/data-breaches-recorded-in-the-united-states-by-number-of-breaches-and-records-exposed/)。但这不仅仅是黑客和白帽黑客之间无休止的拉锯战。在处理数据方面存在更基本、更根本的缺陷。

您的敏感信息，如银行对账单、医疗记录和商业 IP，通常在存储和传输时会被加密。然而，最脆弱的阶段是在处理数据时。云数据涉及[82% 的泄露事件](https://secureframe.com/blog/data-breach-statistics/)，其中 74% 涉及人为因素。这表明，当数据被积极使用和处理时，风险很大，尤其是在人们进行交互的云环境中。传统上，数据在计算过程中未加密，增加了风险。

机密计算允许数据在此阶段被加密。然而，去中心化的机密计算更进一步，确保*没有人*（甚至您的云提供商）可以在数据处理过程中访问您的数据。

**技术**

机密虚拟机 (VM) 计算的一个例子是[AMD 安全加密虚拟化 (SEV)](https://www.amd.com/en/developer/sev.html)。AMD SEV 是一种基于硬件的内存加密功能，集成到 AMD 的 EPYC 处理器中。它对单个 VM 的内存进行加密，即使是管理程序也无法访问明文数据。这是通过为每个 VM 分配一个唯一的加密密钥来实现的，该密钥由 AMD 安全处理器管理，AMD 安全处理器是 CPU 中一个专用的安全子系统。

加密过程对 VM 来说是透明的。内存读写操作由内存控制器使用 VM 特定的密钥自动加密和解密。这确保了数据在 CPU 边界之外保持加密状态，使任何未经授权的访问尝试都变得徒劳。虽然管理程序仍然负责资源分配和调度，但它无法拦截或操纵 VM 的内存内容。

另一个重要组成部分是可信执行环境 (TEE)。TEE 在主处理器中提供一个安全区域，将代码和数据与系统其余部分隔离开来。TEE 确保敏感计算在受保护的环境中进行，不受恶意软件和硬件攻击的影响。在 AMD SEV 的背景下，TEE 通过硬件强制的隔离机制来实现，这些机制隔离了 VM 内存空间。

AMD 安全处理器在建立 TEE 中发挥着至关重要的作用，它负责处理加密操作和密钥管理。它确保加密密钥安全生成，并且对未经授权的实体（包括管理程序和系统管理员）不可访问。这种硬件信任根基是 SEV 提供的完整性和机密性保证的基础。

**去中心化的机密虚拟机**

在过渡到*去中心化的*机密虚拟机之前，值得考虑一下为什么我们需要它们。毕竟，机密虚拟机已经存在，您可能不会看到与 Google、Amazon 或 Microsoft 共享个人数据的风险。高达[90%](https://storecloud.org/store-cloud/node-centralization) 的去中心化网络仍然使用 AWS 等集中式基础设施来运行关键操作。然而，这种方法存在一些问题。

其中一个问题是集中式模型存在单点故障。通过去中心化基础设施，您可以消除单点故障，并减少集中式系统固有的信任依赖关系。Aleph.im 和 TwentySix Cloud 已经实现了这一点，他们使用 AMD SEV 在分布式网络上部署了完全[去中心化的机密虚拟机](https://console.twentysix.cloud/)。研究人员和开发人员可以注册他们的去中心化云，符合条件的人员可以获得免费访问权限。

网络中的每个节点都运行着由 SEV 强制执行内存加密的 VM，确保即使在多租户环境中，数据也保持机密性。
这种方法得益于区块链原理，其中去中心化增强了[安全性和弹性](https://thenewstack.io/build-resilient-secure-microservices-with-microsegmentation/)。TEE 和去中心化共识机制的结合使网络能够在存在对抗节点的情况下保持完整性。[VM 内的数据和代码受到保护](https://thenewstack.io/the-data-protection-challenges-of-kubernetes/)，防止外部干扰，并且网络的去中心化性质减轻了与集中控制相关的风险。

**Azure 的机密 VM 与去中心化机密 VM**
Microsoft Azure 还使用 Intel SGX（软件保护扩展）和 AMD SEV 技术提供机密 VM。Azure 的[平台在其云基础设施内提供隔离的执行环境](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide/)，保护数据免受其他租户的侵害。但是，基础设施仍然处于 Microsoft 的控制之下，引入了关于提供商的安全态势和治理的信任假设。

相比之下，去中心化机密 VM 在独立控制的节点网络中运行。信任模型从依赖单个提供商转变为多个参与者之间的共识。这种去中心化降低了系统性漏洞和外部实体胁迫的风险。此外，它与 Web3 用户主权和数据所有权理念相一致。

从技术上讲，Azure 和去中心化机密 VM 利用 AMD SEV 进行内存加密和隔离。但是，部署模型存在很大差异。Azure 的解决方案仅限于其数据中心，而去中心化 VM 跨越异构环境。后者引入了密钥管理、证明和协调复杂性，但提供了增强的弹性和信任去中心化。

**实际应用和影响**
让我们看看去中心化机密 VM 的一些实际应用。在围绕隐私问题的所有报道中，您可能已经猜到了第一个应用：AI。

[训练机器学习模型](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/) 通常涉及包含个人或专有信息的敏感数据集。在去中心化[机密 VM 中部署训练过程允许组织利用分布式计算](https://thenewstack.io/brendan-burns-everything-you-need-to-know-about-confidential-computing-and-containers/)资源，而无需公开原始数据。这些模型得益于联邦学习，在不损害个人数据隐私的情况下聚合见解。例如，[LibertAI](https://libertai.io/) 正在探索如何利用 Aleph.im 的机密 VM 来运行安全的、大规模的 AI 部署，而无需公开敏感的个人数据。
更广泛地说，对数据的任何类型的分析都可能存在风险。借助去中心化机密 VM，我们可以获得这些分析得出的见解，而无需与未加密和/或集中计算相关的隐私风险。企业可以在去中心化节点上对加密数据集执行分析。同态加密和安全多方计算技术可以在机密 VM 中使用，从而在不解密数据的情况下实现见解。这主要有利于受严格监管合规性约束的行业，例如医疗保健和金融。

另一个用例是安全的去中心化金融 (DeFi) 协议和交易算法。DeFi 平台可以在机密 VM 中执行复杂的金融合约和交易策略。私钥和交易数据在加密的内存空间中处理，防止敏感信息的泄露。这增强了[自动交易机器人和处理大量金融资产的智能合约的安全性](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/)。

游戏和 NFT 也从这项技术中受益。可验证随机函数 (VRF) 可以安全地实现在机密 VM 中，确保为游戏头像特征、彩票等公平透明地生成随机数。

最终，随着世界向更大的透明度、安全性和隐私转变，去中心化机密 VM 代表的不仅仅是增量改进——它们在安全计算方面提供了范式转变。它们使企业和个人能够前所未有地保护其信息，确保没有集中实体可以访问其数据。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)