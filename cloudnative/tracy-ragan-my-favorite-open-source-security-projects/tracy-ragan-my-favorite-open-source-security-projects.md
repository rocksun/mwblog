# Tracy Ragan：我最喜欢的开源安全项目

翻译自 [Tracy Ragan: My Favorite Open Source Security Projects](https://thenewstack.io/tracy-ragan-my-favorite-open-source-security-projects/) 。

一位长期的开源软件名人敦促开源峰会与会者将他们的超能力应用于安全工作组。

![](https://cdn.thenewstack.io/media/2023/05/51e7ceb6-shutterstock_1-1024x724.jpg)

不列颠哥伦比亚省温哥华 - 长期的开源软件爱好者 [Tracy Ragan](https://twitter.com/tracyragan?lang=en) 敦促那些参加 Linux 基金会[北美开源峰会](https://events.linuxfoundation.org/open-source-summit-north-america/)的人参与社区。

“我们每个人都有超能力。去把你的超能力应用到其中一个群体中，因为我们真的，真的需要你，“ Ragan 说，他在一次主题演讲中赞扬了[开源安全基金会（OpenSSF）](https://openssf.org/)的工作以及背后的辛勤工作的推动者和变革者。

她指出，安全性已成为开源世界的一个主导主题，尽管“我们都在非常非常努力地生产安全且高质量的软件......现在我们意识到我们必须做得更好。

应该指出的是，DeployHub 的首席执行官兼联合创始人 Ragan 本人参与其中。她曾在 OpenSSF 管理委员会任职，并且是 [CD 基金会（CDF）](https://cd.foundation/)和 [Eclipse 基金会](https://www.eclipse.org/)的创始董事会成员。

“许多新工具正在开源世界中推向市场，”她说。“我们有来自 OpenSSF 的工具。我们有来自持续交付基金会的工具，我们有来自[云原生计算基金会]项目的工具，我在这里只列出了我最喜欢的几个。

## SLSA (Supply-Chain Levels for Software Artifacts)

OpenSSF 在四月份发布了 SLSA 的 [1.0 版本](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/)，发音为 “salsa” 。 [SLSA 提供了一个通用词汇](https://thenewstack.io/securing-the-software-supply-chain-with-slsa/)来讨论软件供应链安全性、评估上游依赖关系、提供清单以提高软件安全性并根据即将推出的安全软件开发框架 （SSDF） 标准衡量合规性工作。版本 1.0 将其需求划分为[多个轨道](https://slsa.dev/spec/v1.0/levels#build-l1)，重点关注软件供应链的特定领域，例如构建、源代码和依赖项。第一个轨道侧重于构建。

“ SLSA 级别对于真正了解如何将安全性引入构建过程非常重要，”她说。

## Pyrsia 

[Pyrsia](https://pyrsia.io/) 是 CDF 下的一个开源软件社区计划，最初是在 JFrog 创建的。它使用区块链技术作为分散、安全的构建网络和软件包存储库的一部分，为开发人员提供他们正在使用的软件包的来源。

开发人员会收到其代码的数字签名、不可变的证据链，这是软件[物料清单 （SBOM）](https://thenewstack.io/sbom-everywhere-the-openssf-plan-for-sboms/) 的基本构建块。 JFrog 与包括 Docker、DeployHub、Futurewei 和 Oracle 在内的其他公司于 2022 年 5 月推出了 Pyrsia。在 Rust 中构建，你可以在 GitHub 上找到 Pyrsia，它描述该项目处于早期 alpha 阶段，致力于构建最小可行产品。

“如果你想做 SLSA ，你可以实施 Pyrsia ，” Ragan 说。“ Pyrsia 确实检查了很多 SLSA 盒子。这就是所谓的去中心化包网络。这意味着你基本上可以考虑通过跨去中心化包或去中心化网络构建来将各种库排除在你的构建之外，你在多个位置进行构建，它们相互检查以确保它们都有相同的确切结果。

Ragan 说:“我长期从事构建工作，知道有些人会说‘我们几乎无法让一个构建正常工作’。相信我，你可以做到这一点。”

## Scorecard

Scorecard 是 OpenSSF 的一个工具，用于自动分析和信任开源项目的安全性决策。它查看了许多与软件安全相关的启发式方法或“检查”，并为每个启发式方法或“检查”分配从 0 到 10 的分数。可以使用这些分数来了解需要注意的安全状况的特定区域。它还允许您评估依赖关系引入的风险，就接受这些风险做出明智的决策，评估替代解决方案或与维护者合作进行改进。

“每个人都应该能够完成这项工作，” Ragan 说。“这一切都内置在 GitHub 的 Actions 中。这是唾手可得的果实，您可以很快开始。所以看看 Scorecard 。

## Alpha-Omega

Alpha-Omega 于 2022 年 2 月推出，涉及与项目维护人员合作，识别开源代码中尚未发现的漏洞并修复它们。 “Alpha” 部分寻找开源生态系统中资金可能产生重大影响的领域。它与 “Omega” 方面的维护者合作，在 10，000 个最关键的开源项目中寻找漏洞的纠正。在那里，它为用户提供自动安全分析、评分和补救指导。

去年秋天在欧洲开源峰会上， [OpenSSF 宣布](https://thenewstack.io/alpha-omega-dishes-out-cash-to-secure-open-source-projects/)微软已经为 [Omega 分析工具链](https://github.com/ossf/alpha-omega)开发并捐赠了技术，该工具链编排了超过 27 种不同的安全分析器，以识别开源包中的关键安全漏洞。它还宣布向 Rust 基金会提供 460，000 美元的赠款，向 Node.js 提供 300，000 美元的赠款，向 Eclipse 基金会提供 400，000 美元的赠款，所有这些都是为了提高安全性。

Ragan 称 Alpha Omega 是她从一开始就最喜欢的项目之一。

## Ortelius

[Ortelius](https://ortelius.io/) 是 CDF 的一个项目，旨在将供应链和微服务管理集中到一个工具中。它最初由 DeployHub 和 OpenMake Software 开发，是 CDF 的一个孵化项目。

Ortelius 跟踪软件供应链中每个组件的开发和安全细节并进行版本控制。可以使用 Ortelelius 跟踪群集之间的微服务版本偏移、聚合 SBOM 的信息，并跨团队和环境管理各种重用组件的使用。Ragan 是该项目的执行董事。

“老实说，未来在 DevOps 方面，我们希望开始以更智能的方式做事，”她说。“我们希望实现事物自动化;我们希望以一种神奇的方式让事情发生。嗯，这就是人工智能。

“人工智能和 DevOps 的问题在于我们没有数据。如果我们考虑一下 GitHub 和像 Copilot 这样的工具，这些工具是如何成为现实的，是他们有数据。他们可以查看所有开源 git 存储库，找到代码片段并做出决定。...我们在 DevOps 中没有，所以 Ortelius 就是这个梦想。它是安全和 DevOps 信息的集中式证据存储，从 SBOM 一直到解耦环境中的逻辑应用程序，并将所有这些信息汇集在一起。因此，你有一个地方可以获取这些信息，在未来，你可以有地方来定义政策和构建人工智能系统。

## CDEvents

同样来自 CDF ， CDEvents 提供了一个供应商中立的规范，用于定义事件数据的格式，以提供跨服务，平台和系统的互操作性。 Ragan 称其为“当今 DevOps 中最重要的项目之一”。

缺乏标准化意味着开发人员不得不不断重新学习如何使用事件，从而限制了整个生态系统中事件数据的使用。

“如果我们考虑如何实现我们的管道，我们就关闭了，”她告诉开源峰会的观众。“从字面上看，在这个房间里，我们有数百万个工作流程。现在，如果要将 SBOM 的生成添加到工作流中，则必须访问大量工作流。CDEvents 解决了互操作性问题...并有可能自动化您的工作流程模板化。

“你们每个人都可以成为英雄。你们每个人都可以提供一些东西来解决这个问题。...出现是成功的一半，“她说，敦促与会者查看各个工作组。