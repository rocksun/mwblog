<!--
title: 云、代码与控制：新的开源权力斗争
cover: https://cdn.thenewstack.io/media/2025/05/f5b7e689-lance-reis-vvqkfatfnyk-unsplash-scaled.jpg
summary: 开源权力斗争：云厂商利用项目盈利引争议，小型公司被迫 relicense。Fork 机制成关键，AGPL V3 许可证被重新采用。关注 CLA、中立基金会和项目治理，保障贡献者权益和项目可持续性，共建云原生生态。
-->

开源权力斗争：云厂商利用项目盈利引争议，小型公司被迫 *relicense*。*Fork* 机制成关键，*AGPL V3* 许可证被重新采用。关注 *CLA*、中立基金会和项目治理，保障贡献者权益和项目可持续性，共建云原生生态。

> 译自：[Clouds, Code, and Control: The New Open Source Power Struggle](https://thenewstack.io/clouds-code-and-control-the-new-open-source-power-struggle/)
> 
> 作者：Dawn Foster

自古以来，当权者常常利用他们的权力来剥削或支配那些影响力较小的人。这种动态不仅限于历史例子；在现代背景下，例如技术和软件开发，尤其是在开源项目中，也可以清楚地看到。

封建主义就是一个典型的例子，强大的统治阶级控制着土地，导致对辛勤耕作和保护土地的人民的压迫和剥削。在封建主义制度下，权力主要集中在少数人手中，国王和教会拥有最大的权力。大部分权力被委托给贵族和领主，他们管理土地，并通过军事服务提供保护。但他们仍然在国王的统治下，国王可以剥夺他们的权力。这些领主和贵族然后控制着耕种土地的农民，他们几乎没有权力或自主权，尽管他们做了大部分实际工作。因此，大部分权力掌握在国王和教会手中，贵族和领主拥有一些权力，而农民和农奴在做大部分工作的同时，几乎没有权力。

大型云提供商掌握着最大的权力，小型公司掌握着一些权力，而个人贡献者和用户掌握的权力很小。界限比较模糊，后果也不那么极端，但随着大型云提供商的日益普及，开源的权力动态可能感觉类似。在开源的情况下，我们有办法扭转这些权力动态。

随着我们的许多应用程序迁移到云端，使用这些云提供商提供的许多服务变得很容易。他们可以为开源项目提供这些服务，无论他们是否回馈这些项目。当他们对这些开源项目的贡献不足时，就会与一些小型公司产生摩擦，而这些小型公司通常是开源项目的驱动力。在某些情况下（但不是全部），这些小型公司可能有权重新许可开源项目，这可以扭转小型公司和云提供商之间的权力平衡。然而，小型公司的这种权力游戏使维护者、贡献者和用户处于更弱势的地位。它会在刚刚重新许可的项目周围产生摩擦。在开源项目中，那些权力最小的人可以[fork the project](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)再次翻转权力动态，但这需要大量的工作，并且可能成功也可能不成功。

## 云提供商与开源权力之战

这些权力动态并不像我说的那么简单。这些公司中的许多都属于多个类别。例如，云提供商也是各种开源软件项目的用户、贡献者和维护者。公司还需要对风险投资公司、董事会以及对公司拥有权力的其他利益相关者负责，无论是一家小公司还是一个非常大的云提供商。

最近，一些公司在风险投资公司、股东或其他投资者的压力下，[relicense their open source projects to generate more license revenue](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-%20impact-on-financial-outcomes/)，主要是当供应商的收入来源完全或主要依赖于开源项目时。如果其他公司（通常是大型云提供商）竞争相同的客户并从供应商投入大量资源开发的开源项目中获利，这种情况可能会更加复杂。对盈利能力的这些担忧导致投资者施加压力，要求将开源项目置于新的许可之下，该许可的限制比开源许可下的限制更多。这些限制通常使云提供商或其他公司更难以从新获得许可的开源项目中获利。

这颠覆了力量的动态，增加了与较小公司相关的力量，同时降低了云提供商的力量。然而，这并不是力量动态翻转的结束。这就是 fork 发挥作用的地方，它是一种集体行动的形式，再次翻转了力量动态，并允许那些权力较小的人掌控我们的命运，就像一个 fork，我们控制着这个新成立项目的治理。然而，事情并没有那么简单。Fork 是一项艰苦的工作，所以虽然你[经常听到人们说任何人都可以 fork 一个项目](https://thenewstack.io/from-poc-to-production-why-genai-projects-often-stall/)并运行它，但这需要大量的人员和资源才能成功。我提到过，一家较小的公司可以重新许可一个开源项目，以翻转力量动态，并从云提供商那里重新获得权力。但是，这些云提供商可以通过 fork 一个项目并从这些较小的公司那里重新获得权力来再次翻转力量动态，而且这种方法效果很好，因为这些大型云提供商通常可以投入大量的人员和其他资源来使 fork 成功。

在之前的[TNS 博客文章](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)中，我分享了关于三个项目案例研究的数据，在这些项目中，重新许可导致了 fork（Elasticsearch / OpenSearch、Terraform / OpenTofu 和 Redis/Valkey）。值得注意的是，在这三个案例中，由这些重新许可事件产生的 fork 往往比原始项目具有更多的组织差异，特别是当 fork 是在像 Linux 基金会这样的中立基金会下创建的，而不是由单个公司 fork 的时候。由于这些 fork，[Redis 和 Elasticsearch 已经添加了 AGPL V3 许可证](https://thenewstack.io/redis-is-open-source-again/)，再次成为开源项目，但鉴于这些 fork 获得的关注，可能为时已晚，无法产生太大的影响。

## 保护贡献者并维持项目可持续性

这些力量动态的转变可能会为那些使用和贡献这些项目的人带来重大问题。作为开源的维护者、贡献者，甚至用户，我们将我们最宝贵的资源投入到这些项目中：时间。我们需要我们花费时间的项目能够长期保持可持续性，以避免浪费这种宝贵的资源。没有办法预测哪些项目会随着时间的推移而保持可持续性，哪些项目可能会经历重新许可或其他 rug pull，但有一些警告信号，以及在决定在一个特定项目上花费太多时间之前我们可以考虑的事情。

*   贡献者许可协议 (CLA)：这些协议在开源社区中造成了力量失衡。权力倾向于拥有项目并控制 CLA 的公司，这使得公司比其他贡献者拥有更多的权力。它可能允许公司重新许可一个项目。
*   中立基金会：如果项目是在中立、良好运行的基金会（而不是单个公司）下进行的，则不太可能发生 rug pull，因为这些基金会鼓励治理结构，从而创建一个公平的竞争环境，来自不同公司的人可以像平等的伙伴一样一起工作，创造出对每个人都有利的东西。
*   治理：Rug pull 可能会并且确实仍然会发生在基金会项目中，通常是当所有或大部分开发都来自单个公司的员工时。具有中立治理的项目，其中领导职位和维护者来自不同的组织，并且具有公平和透明的流程来选择这些领导者，则不太可能经历这些类型的中断。
*   贡献者可持续性：项目是否有足够的[贡献者来长期维持它](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/)，并在现有维护者转移到其他项目时替换他们？对于我们依赖的开源项目，是否有足够的贡献者，如果其中一位明天在海滩上退休，没有发出任何通知，项目是否可以继续进行，并且中断程度最小？

这直接关系到公司如何帮助对他们重要的开源项目。我已经谈了很多关于权力动态的问题。尽管如此，公司也有能力和资源做出真正的改进，并且公司的参与可以积极地影响我们开源项目的可持续性，包括分支（forks）。公司可以分配员工时间来为项目做贡献，或提供资金和其他资源来帮助维持开源项目。让你的员工[在一个项目中工作](https://thenewstack.io/internal-projects-working-inside-the-panopticon/)，也能让你了解可能存在的权力动态，更好地了解该项目的优势和劣势，同时也能从内部影响该项目。

随着大型云提供商的日益普及，开源权力动态看起来有点类似于我在本博文开头谈到的封建主义例子，但在开源案例中，不同之处在于我们有办法转变或颠覆权力动态。一家较小的公司决定将一个项目从开源许可证中移除，可以颠覆权力动态，并从那些大型云提供商那里夺回权力。但是，当他们决定重新许可该项目时，他们也同时将权力平衡进一步从贡献者和用户手中转移开。这鼓励那些权力较小的人采取集体行动来派生（fork）一个项目，从而使权力动态向贡献者和用户倾斜，通常包括云提供商作为用户。在开源世界中，我们比农民和农奴要好，因为我们拥有某些自由，允许我们采取集体行动，通过派生项目来重新获得权力，以对抗其他人滥用权力。