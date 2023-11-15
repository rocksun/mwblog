<!-- 
# Freeplay：面向Java开发者（还有其他）的新型LLM开发工具
https://cdn.thenewstack.io/media/2023/11/fe83e08e-freeplay_feature-1024x524.jpg

-->

两位前Twitter开发者平台高管成立了一家名为Freeplay的AI开发平台。他们表示，它不仅仅是可观测性。

译自 [Freeplay: New LLM Dev Tool for Java Developers (and Others)](https://thenewstack.io/freeplay-new-llm-dev-tool-for-java-developers-and-others/) 。

Freeplay是一款全新的LLM开发平台(今年我已经[多次](https://thenewstack.io/llm-app-ecosystem-whats-new-and-how-cloud-native-is-adapting/)重复这个句子了)。一位投资者称它为“Figma的”，把它称为“LLM开发的Figma”。所以到目前为止，我们是两个[开发工具](https://thenewstack.io/ai-for-dev-tools-create-software-requirements-with-userdoc/)炒作指数中的其中一个。

但是让我们先退一步：[Freeplay](https://freeplay.ai/)到底是什么？为了弄清楚，我采访了联合创始人兼CEO [Ian Cairns](https://www.linkedin.com/in/iancairns/)，他以前在[Twitter的开发者平台](https://thenewstack.io/developers-twitter-wants-your-bots-and-other-read-write-apps/)工作，直到该公司被埃隆·马斯克收购。

Cairns告诉我，他和联合创始人Eric Ryan(也来自Twitter)创立Freeplay是为了“帮助产品开发团队在其产品中利用LLM”。目前，Freeplay可以帮助测试、试验、监测和提示管理。

“这些功能组合起来可以帮助人们完成软件开发生命周期，”Cairns说。“从原型阶段，到测试阶段以确保它准备好投产，最后 - 当它已经上线时 - 帮助您了解系统中的大规模运行情况，然后找到方法进行改进。”

与我最近介绍的LLM开发平台[Gradient](https://thenewstack.io/new-ai-dev-platform-allows-you-to-customize-open-source-llms/)一样，Freeplay面向企业软件开发者。

“我们的大多数客户都是一些已有业务的软件公司，”Cairns说。“也就是说，它们不是以AI为先的创业公司。它们都是一些试图采用LLM的公司，已经有了成熟的业务和客户群。它们有很出色的软件开发者，但可能以前没有使用过LLM，甚至没有使用过机器学习。”

## 将Java引入AI世界

Freeplay为Python、Node和Java提供了开发者SDK。Cairns声称，Java SDK在当前的AI工程空间中是独一无二的。

“AI创业社区中的许多人要么使用Python，因为传统上有大量的机器学习和AI工具在Python世界，要么使用Node或JavaScript - 因为他们正在构建React应用程序，您可以使用JavaScript进行服务器端和前端工作。我们与众不同的地方在于：我没有看到目前这个领域有人为JVM构建过SDK。”

他说，许多成熟的软件公司使用的是Kotlin等语言，Kotlin与JVM兼容。他补充说，当他在Twitter工作时，他们使用的是Scala(Scala是另一种兼容JVM的语言)。

“仅为了调用语言模型就采用一种全新的编程语言，这可能不是很合理，”他说。“我们发现，很多老牌公司只是与他们这多年来一直在使用的软件进行集成 - 他们不会去使用某些新的AI框架。”

## 数据飞轮：不仅仅是可观测性

我提到，乍一看，Freeplay让我想起了[Humanloop](https://thenewstack.io/a-playground-for-llm-apps-how-ai-engineers-use-humanloop/)，后者将自己描述为一个“协作游乐场”，开发人员可以在其中测试和部署提示。我问Cairns，这是否是一个公平的比较？

他回答说，这是一个“合理的类比”，但是Freeplay更常被客户在“已经上线生产”后使用 - 暗示它可能不像Humanloop那么像一个“游乐场”。

![](https://cdn.thenewstack.io/media/2023/11/3d489cd8-freeplay2.jpg)

*Freeplay演示图片*

我注意到Freeplay和Humanloop都包含了测试和监测功能，所以它们两者都类似于传统的DevOps[可观测性](https://thenewstack.io/observability/)平台。Cairns在某种程度上赞同这点，但他指出LLM应用程序的需求与传统应用程序不同。

“在传统的可观测性中，大部分目标就是 - 嘿，发生了什么，”他解释说。“但是对于机器学习系统，我认为这对LLM也适用，可观测性的需求 - 发生了什么 - 仍然存在，但它实际上也是这个数据飞轮的一部分，以一种不同的方式帮助您逐步优化产品，当您进行机器学习时。”

关键在于，LLM应用程序的质量依赖于基础数据(或数据的查询方式)，任何来自软件开发周期有助于优化应用程序的内容，都会反馈到LLM(或提示/查询)中。正如Cairns所说，Freeplay“不仅是一个可观测性平台 - 可观测性是一个帮助更大优化循环的功能”。

## Figma的类比

与低代码平台类似，Freeplay旨在被开发人员和产品/业务人员共同使用。这就是Figma类比的来源。它是一个使专业开发人员能够通过Web前端与业务利益相关者进行协作的工具。我问Cairns通常是开发人员还是产品经理在推动这个过程。

“进行初始设置的人一直是技术领导者，”他回答说。“无论是CTO还是工程主管，也就是说，他们是那些说，嘿，我们想给团队提供更好工具的人。”

开发人员的作用是项目的实施。

“开发人员肯定会首先使用Freeplay进行集成并持续使用它，”Cairns说。“但是它的工作方式是您将我们的SDK嵌入到您正在构建的应用程序中。我们开始管理提示，就像管理服务器端实验一样。”

他将其比作类似Amplitude或LaunchDarkly等工具，可以进行A/B测试 - “这样产品经理就可以启用实验”。因此一旦开发人员设置了系统，产品经理就可以进行这种实验或测试。

## 将OpenAI的开发者平台与Twitter的进行比较

最后，我问Cairns他和他的联合创始人Eric Ryan是否从在Twitter开发者平台工作中获得了一些经验教训。两人都在2014年加入Twitter，因为Twitter在那年收购了Gnip，一家社交媒体API聚合公司。

你们中一些人可能还记得，Twitter曾有可能成为一个大规模的应用开发平台，但他们在2010年代初不明智地[打压](https://thenewstack.io/twitter-turmoil-we-need-an-open-protocol-for-public-discourse/)第三方开发者。Cairns谨慎地没有过多谈论这一点，但他确实得出了一个有趣的类比，即OpenAI现在的处境。

“我认为OpenAI确实做得很好，这是Twitter在2010年我们不在的时候错过的机会。昨天它们做出了重大改变 - 似乎与那些构建独立聊天机器人或代理的人存在竞争，但它们也通过应用商店和在其平台上获利的机会吸引了这些人。我认为它们在这方面做得不错。”
