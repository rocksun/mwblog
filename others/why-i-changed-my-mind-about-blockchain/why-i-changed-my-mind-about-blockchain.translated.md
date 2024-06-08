# 我为何改变了对区块链的看法

![区块链特写图片](https://cdn.thenewstack.io/media/2024/06/d494bd17-blockchain-1024x576.jpg)

我大学时学习密码学，而比特币作为一个新颖且非常规的概念出现。在我的一门课程中，我们分析了与比特币非常类似的加密货币的密码学构建模块。尽管我钦佩算法和协议的精妙，但我对 [区块链技术](https://thenewstack.io/the-use-cases-for-blockchain-real-and-hypothetical/) 并不特别感兴趣。我的主要保留意见是，尽管其设计创新，但它并没有解决我个人认为重要的任何问题。

我对区块链的怀疑一直持续到几个月前，当时我与 Aerospike 的一位新客户合作， [BSV 协会](https://association.bsvblockchain.org/)。它使用区块链优雅地解决了据我所知尚未在其他地方得到有效解决的工程难题，尤其是无缝地解决了创建无界限且线性可扩展的核心银行系统。

我选择使用“核心银行系统”而不是“加密货币”是为了避免与后一个术语相关的各种含义。对于此讨论，我们可以简单地将加密货币视为一个使客户能够创建帐户、存款、取款和转账的系统——这些功能与传统核心银行系统的功能类似。

在我看来，核心银行系统代表了复杂、任务关键、安全和精确应用程序的典型示例，尽管付出了相当大的努力，但始终抵制现代化。

## 无法现代化的

许多 [核心银行系统要么无法扩展](https://thenewstack.io/banks-must-innovate-or-die-could-gitops-be-the-lifeline/)，要么扩展效率低下，导致金融服务公司为仅增加最小的工作负载容量而投入大量资源和精力。通常，这些可扩展性限制源于对关系数据库管理系统 (RDBMS) 的依赖，例如大型机或 Oracle，它们本身缺乏必要的可扩展性。

将核心银行系统的心脏和灵魂从 RDBMS 升级到可扩展、更快速、更具成本效益和高效的 NoSQL 数据库已被证明极具挑战性。这在很大程度上是由于 RDBMS 的固有特性，它非常适合构建复杂系统。然而，最初使用关系方法开发的各种应用程序已成功过渡到 NoSQL。

在从 RDBMS 过渡到 NoSQL 的过程中，数据存储层不可避免地会丢失某些关键特性，同时获得其他特性。这些丢失的特性对于应用程序的功能至关重要，不容忽视。因此，必须在应用程序层中解决这些特性的缺失，这正是将高度复杂的任务关键系统从 RDBMS 迁移开如此困难的原因。

此外，RDBMS 操作由数学证明支持，即使在存在应用程序层错误的情况下，也能提供牢不可破的数据完整性保证。相比之下，在 NoSQL 领域，最高权威是 [一个人](https://aphyr.com/about)，他以测试数据库为生（恕我直言）。他最多只能断言在某个技术测试版本中没有发现错误。显然，这种保证级别对于核心银行系统等关键环境来说是不够的。因此，如果我们打算从关系模型提供的数学保证中过渡，我们必须在应用程序层中实施类似的保证。

实现这些保证的一种方法是通过 [形式化方法](https://en.wikipedia.org/wiki/Formal_methods)。然而，鉴于核心银行系统的复杂性，仅使用这种方法构建一个系统极具挑战性。

## 区块链的潜力

抛开流行语，区块链从根本上来说是一种经过数学证明的 [零信任](https://thenewstack.io/zero-trust-security-and-the-software-development-lifecycle/) 算法。因此，它可以部署在应用程序层中，以抵消底层存储模型中缺乏数学保证的情况。此外，比特币的成功表明，区块链技术确实可以有效地用于构建核心银行系统。

然而，比特币和许多其他基于区块链的加密货币 [受到交易吞吐量的显着限制](https://en.wikipedia.org/wiki/Bitcoin_scalability_problem)，这远低于传统不可扩展金融交易系统。因此，在这一特定方面，现有的加密货币并没有比传统金融系统提供实质性的改进。

## BSV 对区块链吞吐量挑战的解决方案
### 更正后的 Markdown 格式

**区块链吞吐量限制**

无需深入探讨细节，基于区块链的加密货币的有限吞吐量主要源于 [区块链块的大小](https://www.bitstamp.net/learn/crypto-101/what-is-block-size/)。例如，[比特币白皮书](https://bitcoinwhitepaper.co/) 最著名的实现 [比特币](https://en.wikipedia.org/wiki/Bitcoin) 的块大小上限为 1 MB，限制其每秒只能处理七笔交易，这是一个令人尴尬的低数字。相比之下，[比特币现金](https://en.wikipedia.org/wiki/Bitcoin_Cash) 的实现通过将块大小增加到 32 MB，将吞吐量提升至每秒超过 100 笔交易，尽管这个数字仍然令人失望地低。[比特币中本聪愿景](https://wiki.bitcoinsv.io/index.php/Bitcoin_Satoshi_Vision)，简称 BSV，是比特币白皮书的另一种实现。BSV 的主要设计目标是通过消除块大小上限来克服吞吐量限制，理论上可以实现无限吞吐量。然而，此修改提出了一个重大的工程挑战。

基于比特币白皮书构建的加密货币使用 [未花费交易输出](https://en.wikipedia.org/wiki/Unspent_transaction_output) (UTXO) 模型，这与核心银行系统中使用的传统会计模型不同。UTXO 信息在 UTXO 存储中检索和更新，以验证比特币交易是否可以花费。处理 UTXO 的任何延迟都会极大地降低比特币节点的性能，从而导致矿工收入损失。

为了加快此过程，必须尽可能快地访问 UTXO。将 UTXO 存储在内存中将提供高效操作所需的速率。然而，这种方法会带来重大的成本影响：每秒数百万笔交易会导致数万亿个 UTXO，需要数十 TB 的 RAM。如此高的资源需求可能会使解决方案变得极其昂贵，从而对广泛采用和可扩展性构成重大障碍。

## Aerospike：BSV 可扩展未来的关键

与 Aerospike 一样，使用商品固态驱动器代替 RAM 进行数据存储可以显著降低 BSV 维护快速数据存储中的 UTXO 的成本，确保效率和可负担性，进而促进更广泛的网络采用。

值得注意的是，UTXO 存储的一致性和完整性对于节点的正常运行至关重要。如果 UTXO 存储损坏，节点将无法成功参与数个周期的创收活动，从而造成有限但不需要的损害。因此，BSV 节点依赖于 Aerospike 的强一致性模式来降低此风险。

然而，协议的整体正确性，包括余额和转账的准确性（如果损坏可能会造成无限的损害），依赖于 [区块链在应用程序层提供的强有力的数学保证](https://blockchain.ieee.org/images/files/pdf/techbriefs-2022-q3/the-mathematics-behind-blockchain.pdf)。

## 打破障碍：前所未有的交易容量

在测试阶段，BSV 网络展示了 [每秒维持 100 万笔交易](https://teranode.bsvblockchain.org/) 的能力，持续时间很长（数周）。相比之下，Visa 支付系统每秒最多可以处理 [65,000 笔交易](https://www.visa.co.uk/dam/VCOM/download/corporate/media/visanet-technology/aboutvisafactsheet.pdf)。

为了每秒管理 100 万笔交易，每个 BSV 节点（称为 [Teranode](https://www.bsvblockchain.org/teranode)）在其 Aerospike 集群上每秒生成大约 300 万个请求，这是一个很大的数字，但与其他一些客户端相比却很小。

例如，[Criteo](https://aerospike.com/news/press-release/aerospike-future-proofs-criteo-ai-ad-platform/?utm_source=The%20New%20Stack&utm_medium=3pp&utm_campaign=The%20New%20Stack)，一家著名的法国 AdTech 公司，使用 Aerospike 每秒处理 2.8 亿个请求，这表明 Aerospike 和块大小都不会成为扩展 BSV 网络的限制因素。

## 在平行宇宙中

在过去十年中，我帮助多家金融机构扩展其系统以适应新的用例，例如移动银行和 [开放银行](https://thenewstack.io/authentication-specification-enhances-open-banking-experience/) 等监管合规举措。这些项目中反复出现的主题是实施解决方案以提高底层系统的吞吐量限制。在 [前一篇文章](https://thenewstack.io/is-a-database-caching-layer-still-necessary/) 中，我详细阐述了为什么这种方法非常低效。
### MARKDOWN TEXT CORRECTED

通常，这些解决方案采用可扩展数据库，通过复杂的数据提取、转换、加载 (ETL) 流程从不可扩展的 RDBMS 中检索数据。虽然这些系统确实增加了工作负载容量，但它们需要大量投资于新基础设施，需要数百万小时的工程工作，并导致创建难以维护的复杂系统。这就是我所说的低效扩展。

我可以想象一个平行宇宙，其中核心系统是无限且线性可扩展的。在这样的世界中，适应一个增加对核心系统需求的新用例可以通过扩展现有基础设施来简单地管理。无需构建其唯一目的是保护最薄弱环节的系统。没有不断升级的复杂性。没有耗时数年、耗资数十亿美元的项目来启动一个应用程序。

正是这种愿景改变了我对区块链的看法。

*了解有关 Aerospike 的大规模可扩展性、毫秒级延迟、* *实时数据库* *的更多信息。* * [YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。