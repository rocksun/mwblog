# Kubernetes 是否环保？

![关于 Kubernetes 是否环保的特色图片](https://cdn.thenewstack.io/media/2024/10/48fc0054-is-kubernetes-green-2-1024x576-1.jpg)

[云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 将于周一启动其年度[可持续发展周](https://tag-env-sustainability.cncf.io/events/cloud-native-sustainability-week/)。周二，Kubernetes 的联合创始人[Brendan Burns](https://www.linkedin.com/in/brendan-burns-487aa590/) 将成为最引人注目的[演讲者](https://community.cncf.io/events/details/cncf-cloud-native-sustainability-presents-virtual-mini-conference-cloud-native-sustainability-week-2024/)。

问题是，他将要说什么？

也许 Burns 会要求 CNCF 工程师少吃肉，并在屋顶上安装太阳能板。我以前在科技主题演讲中听到过这种善意的个人行动呼吁。

也许他会告诉我们放弃现代技术，关闭我们所有的 AI 项目？我宁愿希望不是这样。我不确定倒退是许多人实际中会喜欢的选择。更重要的是，我认为这种论点不会非常有效。

既不是杞人忧天，也不是将一对光伏电池和一个香辣豆类汉堡英雄般地配对就能拯救世界。然而，Burns 的听众采取更多集体行动就可能做到。

好消息是他比任何人都清楚这一点。

## 科技人员应该做什么？

呼吁个人行动将是对 CNCF 工程师听众力量的悲惨浪费。他们可以产生更大的影响。

到目前为止，我们大多数人都知道[科技行业造成的](https://thenewstack.io/why-software-developers-should-be-thinking-about-the-climate/)[碳排放量](https://thenewstack.io/why-software-developers-should-be-thinking-about-the-climate/) 比航空业还要多。即使在 ChatGPT 出现并以其没有灵魂但欢快的姿态踩下油门之前，情况也是如此。我们行业的变化是优先事项，而不是我们自己。

好消息是，即使有 AI 的参与，科技行业的足迹最终也是可以避免的。最大限度地减少碳排放对系统成本和弹性都有好处，而且已经存在帮助我们做到这一点的工具，我们只需要使用它们。我们中太多人没有使用它们。或者没有很好地使用它们。这就是我们需要解决的问题。

为了解释为什么可持续性、成本和弹性如此一致，我们需要看看[Kubernetes 的起源故事](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)。

## 容器和编排：可持续的概念

为了解释为什么 Kubernetes 背后的概念是科技应对气候变化的关键，我们需要回到 20 多年前，回到一个更加年轻的[谷歌](https://cloud.google.com/?utm_content=inline+mention)。那时，一群勇敢的工程师决定构建一个有史以来最强大、最有远见的软件操作系统平台。

他们称之为[Borg](https://dl.acm.org/doi/10.1145/2741948.2741964)。

Borg 团队知道，谷歌需要比行业中任何人都实现的规模更大的数据中心机器利用率。这种极端的运营效率对于限制第一个超大规模软件系统的资源需求（以及由此产生的成本）是必要的。

此外，为了保持该系统正常运行，团队成员需要比以往任何时候都更好的弹性和恢复能力。他们还需要能够以机器速度而不是微不足道的速度对不断变化的环境（例如电力波动或硬件故障）做出反应。但是如何做到呢？

他们大胆的想法是尝试通过对软件运行方式的根本性转变来共同实现所有这些目标。谷歌团队规定，他们新平台上的所有作业都必须与它们的依赖项以及有关如何运行它们的的信息一起打包到一个名为[容器](https://thenewstack.io/containers/) 的新[Linux](https://thenewstack.io/linux/) 功能中。

结果是，这些作业可以使用调度算法而不是过度劳累和报酬过低（划掉 - 我们说的是谷歌）的人类系统管理员以闪电般的速度停止、启动或移动。

这种激进的方法被称为[编排](https://newstack.io/what-is-container-orchestration/)，它是现代软件开发和运营实践的基础。Borg 及其背后的概念启发了[Kubernetes](https://roadmap.sh/kubernetes)。

故事的转折是，事实证明，封装和编排也是可以让我们交付大规模绿色软件的概念。

## 绿色电力：一种可变电源

为了理解为什么像 Kubernetes 这样的编排平台与未来如此相关，我们需要将目光投向未来。
世界目前正在从化石燃料转向可再生能源，这是一个需要数十年才能完成的过渡。要使这种过渡成功，不仅仅是建造更多的太阳能农场或风力涡轮机，因为这还不够。

可再生能源发电，特别是来自太阳能和风能，与来自燃烧化石燃料的电力具有不同的特性。它更便宜，所以这是好事，但它也更不稳定。它的可用性取决于一些难以预测和管理的事情。这是一个问题。

我们无法控制阳光或风力。这些元素远不如将一艘装满液化天然气的油轮开到发电站并启动涡轮机那样可控。我们必须为之计划的近期未来，在（字面上的）开关一按之下，可用的电力要少得多。这是反乌托邦吗？这取决于我们如何看待它。

可再生能源发电或绿色电力意味着在某些时候电力更多、更便宜，而在其他时候电力更贵。何时何地只有部分可预测。如果你能在这样的世界中蓬勃发展，那它就是乌托邦。如果你不能，那它就是反乌托邦。

那么，有哪些工具可以帮助软件系统在这种环境中运行？系统需要能够快速反应和适应。我们希望它们在碳密集型电力时期使用更少的资源。我们还需要它们能够及时移动工作以匹配绿色能源的可用性。

二十年前，谷歌证明了一种创建此类系统的方法是将它们分解成小的可管理块（也称为分布式系统）并在编排平台上运行它们。从那时起，他们一直在这样做。

谷歌最初的愿望是创建能够适应不可预测、不断变化的环境的系统。这正是系统在直接运行在可再生能源上的时候将面临的情况。因此，谷歌的编排分布式系统设计非常适合处理未来的清洁能源。

这是一个幸运的巧合。让我们充分利用它。

## Kubernetes 的未来？
为了处理可再生能源的波动性，我们中的许多人将来需要运行更多编排的分布式系统。

Kubernetes 是一个经过验证的分布式系统编排器示例。这意味着我们最终都会使用它吗？不一定。它不是唯一的选择。

更广泛的技术界也从 Borg 中吸取了教训，现在有许多编排平台可用：无服务器平台，如 [Amazon Web Service’s](https://aws.amazon.com/?utm_content=inline+mention) Lambda，[服务器端 WebAssembly](https://thenewstack.io/webassembly-for-the-server-side-a-new-way-to-nginx/) 平台，托管服务，如谷歌的 [Cloud Run](https://thenewstack.io/how-google-cloud-run-combines-serverless-with-containers/)，所有超云上都可用的抢占式实例类型，以及托管的 Kubernetes 选项，如 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) [Azure’s AKS](https://thenewstack.io/introducing-aks-automatic-managed-kubernetes-for-developers/)。它们都采用封装的任务，并在空间和时间上以编程方式移动它们。有些使用容器进行封装，有些使用轻量级虚拟机。原理是一样的。

最终，我怀疑我们几乎所有人都会在编排平台上运行我们的软件。我们需要它来处理一个电力更像带宽的世界——一种可变资源，其可用性必须积极调整。

资源不可预测性不是一件坏事。这是互联网发展所处的环境，技术行业的部分人士已经对此了如指掌。

为不可预测的环境设计是构建绿色软件的基础，即可以直接在可再生能源上运行的软件和系统。正如谷歌和其他公司发现的那样，这样做有很多连带好处——降低托管成本和提高弹性是最重要的。

编排分布式系统设计对于技术适应气候变化至关重要。这可能是我们使数据中心成为负载均衡电网资产而不是耗电电网负债的最佳方式。

在我们关于该主题的 [O’Reilly 书籍](https://learning.oreilly.com/library/view/building-green-software/9781098150617/) 中，我和我的合著者描述了帮助构建这些绿色系统的工具和服务，称为绿色平台——Kubernetes 是其中之一，但无服务器、大多数托管服务和抢占式实例也是如此。

不幸的是，这些平台中的大多数——特别是 Kubernetes——仍然只是潜在的绿色平台。为了可持续发展，它们必须得到很好的使用，这很难。使用不当不会赢得任何绿色奖项。恰恰相反。你必须是这方面的专家，或者购买一些托管的东西。
减少碳排放也意味着利用我们作为消费者的力量，迫使这些平台不断改进。它们都有很大的空间可以做得更好，地球（或者让我们面对现实，人类）需要它们这样做。

大多数工程师仍然需要学习如何使他们的系统为能源转型做好准备——如何构建或运营绿色平台。希望伯恩斯将在他的主题演讲中为我们指明方向。

查看作者之前在 The New Stack Makers 的一集中谈论绿色软件的节目：

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。