<!--
# 知识图谱如何改进生成式AI
https://images.idgesg.net/images/article/2021/12/artificial-intelligence-concept-picture-id1160995648-100855293-large-100912931-large.jpg?auto=webp&quality=85，70
-->

大语言模型有巨大的潜力，但也存在明显的缺陷。知识图谱可以使大语言模型变得更准确、透明，并且结果易于解释。

译自 [How knowledge graphs improve generative AI](https://www.infoworld.com/article/3707814/how-knowledge-graphs-improve-generative-ai.html) 。

[ChatGPT](https://www.infoworld.com/article/3689172/chatgpt-and-software-development.html)的初期热潮正在减退。问题是，这对企业意味着什么？这只是一种可以安全忽略的短暂趋势，还是一种需要积极拥抱的强大工具？如果是后者，采用它最安全的方式是什么?

ChatGPT只是大语言模型(LLM)的一个实例。LLM是一项必不可少的技术，但并不能直接应用到业务流程中。想从中获得好处需要您付出某些努力。

尽管LLM潜力巨大，它们也存在一系列挑战。这些挑战包括产生臆想、训练和扩展带来的高成本、解决和更新的复杂性、内在的不一致性、进行审计和提供解释的困难，以及英语内容的主导地位等。

另外，LLM在推理方面表现不佳，需要仔细提示才能给出正确答案。所有这些问题可以通过利用知识图谱来支持新的内部语料库LLM而得到缓解。

## 知识图谱的力量

知识图谱是一种信息丰富的结构，它描绘实体及其相互关系。例如，Rishi Sunak担任英国首相一职。Rishi Sunak和英国是两个实体，担任首相描述了它们之间的关系。我们可以用一组可断言的事实以及我们已知的关系网来表达这些身份和关系。

建立知识图谱后，您不仅可以查询图谱模式，例如“Rishi Sunak内阁成员是谁”，还可以用图算法和图数据科学在图谱上进行计算。有了这些额外工具，您可以问关于全图上数十亿元素的本质问题，而不仅仅是子图。现在您可以问这样的问题:“不在Sunak内阁的政府成员中，谁最具影响力？”

用图的形式表达这些关系可以发现之前被掩盖的事实，获得 valuable insights。您甚至可以从图谱(包括其数据和结构)生成嵌入，在[机器学习流水线](https://www.infoworld.com/article/3651453/orchestrating-data-for-machine-learning-pipelines.html)中使用，或作为与LLM集成的连接点。

## 知识图谱与大语言模型的结合

但是，知识图谱只能发挥一半作用。LLM是另一半，我们需要了解如何使它们协同工作。目前出现了四种模式:

1. 使用LLM创建知识图谱。
2. 使用知识图谱训练LLM。
3. 在LLM交互路径中使用知识图谱丰富查询和响应。
4. 使用知识图谱创建更好的模型。

第一种模式中，我们利用LLM的[自然语言处理](https://www.infoworld.com/article/3398696/what-is-natural-language-processing-ai-for-speech-and-text.html)功能处理大规模文本数据(例如网上或期刊的内容)。然后，我们要求不透明的LLM生成透明的知识图谱。知识图谱可以检查、质量保证并仔细挑选。重要的是，对于制药等受监管行业，知识图谱明确并确定其答案，而LLM做不到这一点。

第二种模式相反，我们不在大规模通用语料库上训练LLM，而是专门在现有知识图谱上训练。这样我们可以构建精通我们产品和服务的聊天机器人，它可以不臆造地回答问题。

第三种模式中，我们拦截到LLM的消息，用知识图谱的数据对其进行丰富。例如，LLM无法独立回答“展示最近五部有我喜欢演员出演的电影”，但是结合电影知识图谱的流行电影及其演员信息可以丰富该提示。同样，从LLM返回时，我们可以解析嵌入到知识图谱中，为用户提供更多见解。

第四种模式是使用知识图谱创建更好的AI。[华盛顿大学Yejin Choi](https://homes.cs.washington.edu/~yejin/)的研究展示了最佳方式。他们的工作中，一个LLM由名为“critic”的小型AI增强。该AI寻找LLM响应中的推理错误，同时为后续消费创建知识图谱，以训练一个更准确的“student”模型。该student模型规模更小、在许多基准测试上更准确，因为它从未学习过不准确的事实或对问题的不一致回答。

## 使用知识图谱了解地球生物多样性

我们应该提醒自己，采用ChatGPT等工具的目的。使用生成AI可以帮助知识工作者执行他们的自然语言查询，而无需了解查询语言或构建复杂API。这可以提高工作效率，让员工将时间和精力集中在更重要的任务上。

以英国生物技术公司Basecamp Research为例，它正在绘制地球生物多样性图，并试图以道德方式支持将新的自然解决方案引入市场。为此，它构建了拥有超过40亿关系的地球最大规模的自然生物多样性知识图谱BaseGraph。

该数据集为许多其他创新项目提供支持。一个是蛋白质设计，该团队利用ChatGPT风格的酶序列生成模型ZymCtrl实现了一个大语言模型，该模型专门用于生成AI。正如我前面描述的，Basecamp正在知识图谱周围集成越来越多的LLM。它正在升级BaseGraph，使其成为一个完全基于LLM增强的知识图谱。

## 使复杂内容更易检索、访问和解释

尽管Basecamp Research的工作开创性，但它在探索LLM与知识图谱的组合上并非唯一。一家全球知名能源公司正使用知识图谱与ChatGPT相结合构建企业知识中心，下一步将为法律、工程等部门的数千名员工提供基于生成AI的认知服务。

再举一个例子，一家全球出版商正在开发一个在知识图谱上训练的生成AI工具，该工具将使大量复杂的学术内容更易于研究客户使用自然语言进行检索、访问和解释。

值得注意的是，后者与我们前面讨论的完全一致：将极其复杂的思想转化为可访问、直观、实用的语言，支持交互和协作。它使我们能够以人们信任的方式精确解决重大挑战。

越来越明显，通过在知识图谱的策划、高质量、结构化数据上训练LLM，可以解决ChatGPT相关的各种挑战，更轻松地实现生成AI的价值。Gartner的报告《[AI Design Patterns for Knowledge Graphs and Generative AI](https://www.gartner.com/document/4436199?ref=solrResearch&refval=375662872&)》强调知识图谱是LLM的理想伴侣，可以提供高水平的准确性。

在我看来，这是知识图谱与LLM完美的结合。你觉得呢?

[Jim Webber](https://www.linkedin.com/in/jim-webber-a3b5033/)是[Neo4j](https://neo4j.com/company/)的首席科学家，也是《Graph Databases》 (1st and 2nd editions, O’Reilly)、《Graph Databases for Dummies》(Wiley)和《Building Knowledge Graphs》(O’Reilly)的合著者。
