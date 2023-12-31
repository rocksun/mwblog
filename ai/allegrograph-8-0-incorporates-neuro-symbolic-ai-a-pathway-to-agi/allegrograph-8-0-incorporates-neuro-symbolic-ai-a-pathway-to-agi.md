<!--
title: AllegroGraph 8.0融合神经符号AI
cover: https://cdn.thenewstack.io/media/2023/12/b668ff9f-bridge-19513_1280-1024x682.jpg
-->

凭借自然语言查询功能，三元组数据库让组织能够充分发挥这些AI技术的优势，并规避其劣势。

> 译自 [AllegroGraph 8.0 Incorporates Neuro-Symbolic AI， a Pathway to AGI](https://thenewstack.io/allegrograph-8-0-incorporates-neuro-symbolic-ai-a-pathway-to-agi/)，作者 Jelani Harper。


Franz更新了其旗舰[三元组存储图数据库AllegroGraph](https://allegrograph.com/)，加入了向量生成和向量存储功能。这种融合允许组织利用所有形式的AI：统计机器学习、非统计推理和在整个互联网上训练的[大型语言模型](https://thenewstack.io/large-language-models-in-2023-tools-and-assistants-for-devs/)(LLM)。

在知识图谱框架内提供所有这些方法，组织可以轻松实现[检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)(RAG)，以提高语言模型结果的准确性。更重要的是，它们可以利用这三种AI分支相互制衡，以使一种方法的优势抵消另一种方法的缺点。

其结果是一个自然语言查询系统，AI的宏伟远景在统计和非统计上终于实现了。

根据[Franz](https://franz.com/) CEO [Jans Aasman](https://www.linkedin.com/in/jans-aasman)的说法，“神经符号系统的要点是当你组合这些系统时，你可以做出惊人的事情，并获得比仅用这些系统中任一种都好的结果。”

因此，组织可以将逻辑和规则技术的可解释性与[LLM学习的海量信息相结合](https://thenewstack.io/demystifying-machine-learning-how-ml-discovers-new-information/)，同时添加高级机器学习的概率模式识别，以确保任何域或用例的准确AI。

## 检查和制衡

这三种AI表达的合成在企业方面最显着的体现是预测。

在医疗保健领域，它们可能涉及患者对某种治疗形式或一系列疾病的结果。在金融领域，它可能包括在动荡市场中的交易或贷款机会的结果。或者，它可能只是对具有特定历史和人口统计资料的客户的理想保险费率。

对于这些应用程序和其他应用程序，AllegroGraph的语义[知识图谱](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/)基础支持一个简单的基于事件的模式，这对于从当前事件确定未来事件是最佳的。组织可以依靠图数据库对基于患者[特定数据的深度学习预测](https://thenewstack.io/machine-learning-data-gets-type-checking-validation-with-flyte-pandera/)，或者使用自然语言查询向量数据库ChatGPT可能发生的事情，“其基于3600万篇Pubmed文章”，Aasman指出。

当这些AI分支同时使用时，会产生最佳结果。

“假设你从[机器学习得出一个结论](https://thenewstack.io/machine-learning-is-as-easy-as-an-api-says-hugging-face/)，说某事将要发生”，Aasman假设。“你可以A，[使用ChatGPT询问](https://thenewstack.io/with-chatgpt-honeycomb-users-simply-say-what-theyre-looking-for/)‘这是否与医学文献一致，或者是新发现？’ 或者B，‘向我解释为什么会这样’。”

每种AI技术的结果都可以输入知识图谱中(8.0版本包括即服务知识图谱产品)，增加组织对其领域的具体知识。

这种机制支持100%可解释的基于规则的推理技术。“机器学习可以通过LLM进行解释，或者LLM的[计算可以通过机器学习支持](https://thenewstack.io/machine-learnings-next-frontier-quantum-computing/)或被机器学习驳斥”，Aasman说。

## 向量生成，向量检索

AllegroGraph 8.0的向量存储有几个有趣的地方。组织不仅可以用自己或第三方(如[Amazon Bedrock](https://aws.amazon.com/bedrock/)、[LangChain](https://www.langchain.com/)等)的外部模型嵌入内容，还可以在AllegroGraph内嵌入内容。

根据Aasman的说法，该数据库支持使用LLaMA或ChatGPT进行嵌入，后者为使用SPARQL的用户提供了自然语言查询功能。“你只需要告诉AllegroGraph文件在哪里，文本片段应该有多大，要使用的机器是什么，它就会为你完成所有工作”，Aasman说。

除了创建嵌入之外，AllegroGraph还使用FLAT索引和近似最近邻哎呀(ANNOY)索引内容。值得注意的是，索引和向量不必保留在内存中。当这些信息保留在内存中时，专用向量存储的成本会显著增加。

“我们可以把这些向量放在磁盘上”，Aasman补充道。“但如果你有快速的SSD和使用一种叫内存映射的技术，它会尽量多地放入内存。” 在AllegroGraph的嵌入和索引过程中也[生成了关于向量](https://thenewstack.io/vector-primer-understand-the-lingua-franca-of-generative-ai/)的元数据，这对于过滤搜索结果很有用。它支持的知识图谱环境在这方面非常有效。

对于专用[向量数据库解决方案](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)，“对于每个文本片段，你可以有一个有限的元数据元素列表，当然，你可以在向量搜索之前或之后进行过滤”，Aasman指出。“但对我们来说，我们可以字面上使用整个图进行预过滤。”

## 检索增强生成

8.0版本使用户能够利用LLM来填充知识图谱，并为特定域构建本体和分类法。还有一个API [SerpApi](https://serpapi.com/)，通过它SPARQL可以直接访问谷歌搜索引擎，这对于验证LLM结果很有帮助。谷歌的结果以文本片段的形式回来，所以对于通过SerpAPI从谷歌收集某人口统计资料中最昂贵汽车价格的用例，“我让LLM询问，让它读取谷歌的每个信息片段，钓出价格并将其放入数据库”，Aasman解释道。组织可以检查两个来源之间的任何差异，并让人们进行必要的调查。虽然AllegroGraph使用SerpAPI与谷歌配合，但该API支持几种[搜索源](https://thenewstack.io/ibm-releases-open-source-counterparts-for-deep-search/)，包括Bing、DuckDuckGo、雅虎和沃尔玛。

在AllegroGraph 8.0中实现RAG的主要方法当然是让语言模型针对知识图谱本身发出自然语言SPARQL查询，知识图谱可以用语言模型、谷歌和内部文档及本体进行填充，并经过人工验证。

因此，对于生命科学用例，“你可以获取知识图中的非结构化文本，比如临床试验，并从文本中提取医学实体和术语之间的关系”，Aasman说。 “因为我们内置了一个向量存储，你实际上可以询问你知识图中任何临床试验，并根据知识图中自己的私有文档获得答案。”

## 总体意义

AllegroGraph 8.0还具有一个新的名为AGWebView的网页界面，增强了分片功能，并更新了其可视化构造，现在可以可视化语义图中标记属性的RDF*注释。

然而，此数据库版本的真正意义在于其将非统计AI、机器学习和从LLM学习的信息合并在增强的向量数据库知识图环境中的倾向。 AI的这些分支可以增强其他分支的优势，同时纠正其缺点，这一直是真正AI的宏伟远景，而不仅仅是基于其统计优势的AI。
