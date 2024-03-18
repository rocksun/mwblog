## Web3 应用的可观测性有何不同

![Web3 应用的可观测性有何不同：特色图片](https://cdn.thenewstack.io/media/2024/03/64761b08-looking-1024x570.jpg)

Web3 代表了构建 Web 应用程序的下一个进化步骤。Web3 结合了区块链技术、去中心化协议和点对点交互，通过去中心化应用程序 (dApp) 催生了透明度和安全性的新标准。dApp 依赖于去中心化服务器，而不是基于集中式服务器的传统 (Web2) 应用程序。

然而，这种新范式给 [应用程序性能监控](https://scoutapm.com/php-monitoring?utm_source=tns&utm_medium=affiliate&utm_campaign=03_24&utm_content=observability_web3_django_apps) 和可观测性带来了挑战。让我们探讨如何使用 Scout APM 在基于 Django 的 Web3 应用程序中实现可观测性的主要支柱——[日志记录](https://scoutapm.com/docs/python/logging)、[指标](https://scoutapm.com/docs/features#app-performance-overview) 和 [跟踪](https://scoutapm.com/docs/features#transaction-traces)。

### 去中心化应用程序中的可观测性有何不同？

[Web3 dApp 中的可观测性提出了几个需要解决的独特挑战](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/)。

**不可变交易**

Web3 dApp 严重依赖区块链技术。一般来说，一旦区块链交易得到确认，即使出现错误，也无法更改。这使得密切监控和可观测性变得极其重要，以便在数据 [写入区块链](https://thenewstack.io/web3-architecture-and-how-it-compares-to-traditional-web-apps/) 之前检测和防止问题。

**分布式数据**

传统 Web 应用程序依赖于集中式服务器，而 [Web3 dApp](https://thenewstack.io/web3-architecture-and-how-it-compares-to-traditional-web-apps/) 依赖于全球分布且去中心化的节点网络。因此，需要一个强大的可观测性解决方案来汇总和分析这个复杂网络中的数据。

**可变网络条件**

Web3 网络的分布式特性导致了固有的不确定性。交易有时会延迟或完全失败。这导致交易时间差异很大。

**交易成本**

许多区块链网络对通过网络中继并成功写入区块链的每笔交易收取费用。例如，在以太坊网络中，此费用称为 [gas](https://ethereum.org/en/developers/docs/gas/)。因此，至关重要的是，您不仅要监控 Web3 dApp 的功能，还要密切关注其经济效率。不必要的大交易或过多交易会增加运行 Web3 dApp 的成本。

**智能合约**

去中心化应用程序严重依赖智能合约。智能合约是指部署在区块链上并由运行网络的节点执行的自执行程序。

Web3 dApp 依赖于智能合约来进行操作。它们充当 dApp 的“后端逻辑”，在“服务器”（区块链网络）上运行。智能合约执行的操作通常会产生交易费用。这些费用用于补偿运行区块链的节点 [为运行智能合约代码提供的计算能力](https://thenewstack.io/how-kubernetes-provides-networking-and-storage-to-applications/)。

此外，智能合约通常处理敏感操作，例如以加密货币的形式释放或接收资金。因此，密切监控智能合约以确保资金得到妥善处理至关重要，以避免造成灾难性损失。

**第三方依赖项**

大多数非平凡的去中心化应用程序 (dApp) 通常与多个第三方 dApp 或合约交互。这引入了复杂的事务流，可能难以追踪和监控。更复杂的 Web3 应用程序涉及 [跨链操作](https://chain.link/education-hub/cross-chain-smart-contracts)，其中一个区块链上的智能合约与另一个区块链上的智能合约交互。这增加了复杂性，使得交易流更难追踪和监控。

### 强大的 Web3 可观测性解决方案的基本功能

鉴于 Web3 环境带来的独特挑战，显然传统的可观测性解决方案可能不够用。需要一种更高级的解决方案来解决这些痛点。以下是为 Web3 dApp 的可观测性解决方案寻找的基本功能。

**实时监控**

鉴于区块链的不可逆转性以及与交易和智能合约操作相关的费用，实时监控是不可协商的。您采用的任何解决方案都应提供即时警报和见解。
**分布式数据聚合**

理想的可观测性解决方案必须让你能够从分散的一组来源提取数据，确保整个网络的完全可见性。如果你的 dApp 执行跨链操作，也必须考虑这一点。具有此功能的可观测性解决方案将为你提供跨层可见性。

**网络分析**

网络分析至关重要，即使对于传统的 Web 应用程序也是如此。在 Web3 dApp 这样的分布式环境中，它们甚至更为重要。网络分析提供对网络拥塞、交易队列时间甚至可能是 gas 价格的见解。这些关键信息让你能够做出明智的决策，预见问题并先发制人地解决问题。

**自定义可观测性解决方案**

Web3 仍处于起步阶段，并且正在迅速发展。鉴于这种日新月异的变化速度，你需要一个允许自定义的可观测性解决方案。扩展基本功能的能力将使你能够填补解决方案提供商提供的功能与你的 dApp 需求之间的任何空白。此外，随着 web3 格局的演变，你可以在无需等待解决方案提供商推出新功能的情况下快速响应。

**用于 Web3 可观测性的 Scout APM 与 Django**

[Scout APM](https://scoutapm.com/) 是你可以用于你的 web3 dApp 的可观测性解决方案。它开箱即用，具有性能见解、内存膨胀检测、SQL 查询监控等功能。然而，它最有价值的功能是 [自定义检测](https://scoutapm.com/docs/python/advanced-features#custom-instrumentation)，它允许你扩展 Scout 以添加你自己的监控和性能测量代码，确保见解针对你的 Web3 dApp 的独特需求量身定制。

这允许进行更细粒度的监控，让你能够专注于可能感兴趣的特定操作或功能。你可以选择跟踪什么、如何跟踪以及在哪里报告数据。

![](https://cdn.thenewstack.io/media/2024/03/197f4a4e-image1.gif)

[Scout APM](https://scoutapm.com/) 与许多流行的编程语言和框架兼容，包括 Python（Django 和其他框架）、Ruby、PHP、Node.js 等。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)