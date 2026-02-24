<!--
title: 五角大楼的Anthropic难题，是所有企业的AI困境
cover: https://cdn.thenewstack.io/media/2026/02/18fd6a7f-getty-images-zqpqfatuzpa-unsplash-1.jpg
summary: 五角大楼与Anthropic因AI使用限制产生分歧，凸显单一AI模型依赖风险。专家建议企业应采用多样化、更小、更经济的模型，国防部更应自建AI，以避免供应商锁定和政策冲突。
-->

五角大楼与Anthropic因AI使用限制产生分歧，凸显单一AI模型依赖风险。专家建议企业应采用多样化、更小、更经济的模型，国防部更应自建AI，以避免供应商锁定和政策冲突。

> 译自：[The Pentagon's Anthropic problem is every enterprise's AI problem](https://thenewstack.io/pentagon-anthropic-model-orchestration/)
> 
> 作者：Darryl K. Taft

五角大楼与Anthropic的[僵局](https://www.reuters.com/technology/pentagon-threatens-cut-off-anthropic-ai-safeguards-dispute-axios-reports-2026-02-15/)向任何依赖单一前沿AI模型构建产品的CTO提出了一个问题：如果明天访问权限发生变化，迁移会有多困难，这又将实际涉及什么？

[*Axios*报道](https://www.axios.com/2026/02/23/hegseth-dario-pentagon-meeting-antrhopic-claude)称，国防部长Pete Hegseth已于周二上午召集Anthropic首席执行官Dario Amodei前往五角大楼，就美国国防部（DoD）使用Anthropic的Claude一事进行会谈。

## 国防部的沮丧

国防部对Anthropic对其Claude使用施加的限制感到沮丧。然而，Anthropic表示将放松一些限制，但不希望其技术用于对美国人的大规模监控或开发无人参与的武器，《Axios》报道。

文章指出：“卸载根深蒂固的Anthropic，并用一个目前能力较弱的AI实验室取而代之，将是一项艰巨的任务。”

## 真的很难迁移吗？

但如果迁移不必那么困难呢？

[NeuroMetric AI](https://www.neurometric.ai/)首席执行官Rob May表示，并非如此。

NeuroMetric通过分析AI流量，并在适当时将查询路由到更小、更便宜、更快的模型（包括开源选项或定制小型模型），帮助企业摆脱对Claude等单一前沿AI模型的依赖。

May告诉《The New Stack》：“所以，我们所做的是，公司将我们接入他们的AI流量，我们进行分析并说，‘嗯，你知道吗，比如这些查询你可以通过这个开源模型运行，这些你可能可以自己构建。’”

## 大材小用？

May认为，大型前沿模型对于许多任务来说是大材小用，对于多步骤代理工作流来说太慢，而且昂贵。NeuroMetric的工具处理模型评估、编排和自动化小型模型生成。

May表示：“大型前沿模型实验室公司有点像大型机时代……你需要这些大型模型公司来向你展示AI模型能做什么，但我们注意到，使用这些模型一段时间的人开始意识到，比如你一半的AI查询不需要发送到Anthropic或OpenAI。这是大材小用，而且你付的钱太多了。”

此外，May补充道：“大型模型[代表]你合作过的最聪明的人。你会带着所有非常简单的事情去找那个人吗？比如，‘嘿，你能回答这个简单的客户支持问题吗？’不，那是在浪费他们的时间。你的AI工作负载也将以类似的方式组织。”

## 企业需要两件事

May表示，企业需要两件事：一个能够路由到多个模型并具备故障转移功能的编排层，以及一个用于根据成本、速度和准确性测试新模型在实际工作负载上的评估框架。

May还指出，他认为国防部应该内部微调Meta的Llama等开源模型或人类反馈强化学习模型，而不是依赖商业供应商。

May说：“未来战争是AI驱动的，国防部将需要一些这类技术。现在，我的假设是国防部应该构建自己的模型。”

NeuroMetric宣传其服务可以帮助企业降低成本并实现更快的AI工作流。

May告诉《The New Stack》：“如果你有一个12步的代理工作流，并且每一步都必须调用Claude，那就会有800毫秒到2.5秒的延迟，你的工作流将长达25秒。所以，如果你能为其中一些步骤运行更小的模型，它会更便宜，更快。”

## 艰难的处境

无论是由于使用政策冲突、定价还是地缘政治压力，国防部的情况并非个例。Anthropic即使面对2亿美元的政府客户也愿意强制执行使用护栏，这表明前沿AI供应商会优先考虑自己的政策决策而非客户需求。

May问道：“他们[Anthropic]是否应该为了联邦政府而违反其服务条款？如果联邦政府想利用这些模型帮助计划摧毁加勒比海的毒品船——你不会容忍任何人这样做。所以，这让Anthropic陷入了困境。”

事实上，《Axios》报道称，上午的会议不会是友好的。“这是一次‘要么就干，要么就滚蛋’的会议，”一位高级国防官员告诉该出版物。