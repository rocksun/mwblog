<!--
title: 资源有限？低参数RAG可以提供帮助
cover: https://cdn.thenewstack.io/media/2024/02/2b63152e-game-1024x576.jpg
-->

使用大众硬件、检索增强生成和向量存储搭建战锤聊天机器人。

> 译自 [Limited Compute Resources? Low-Parameter RAG Can Help](https://thenewstack.io/limited-compute-resources-low-parameter-rag-can-help/)，作者 Mario Charnell-Delgado。

在构建一个需要多次调用大型语言模型(LLM)来完成任务的生成式AI应用程序时，一个常见的问题是，对LLM的重复查询既昂贵又难以预测。像GPT-3.5/4这样的大型模型训练和运行推理所需的计算资源非常大，这反映在API收费以及服务偶尔中断上。ChatGPT最初被释出仅用于研究预览，并非用于生产应用。然而，其在广泛的应用中的有用性是不容置疑的，因此对[LLM的兴趣](https://roadmap.sh/guides/introduction-to-llms)爆炸式增长。

自ChatGPT面世以来，用户一直在寻找规避使用GPT时缺乏隐私以及无法控制正常运行时间或推理设置的方法。这导致了对免费公共模型(如Meta的[Llama 2](https://ai.meta.com/llama/))的普及，后来又出现了Llama的量化和较低参数版本，可以在消费者硬件上运行。这些公共模型能够以远少得多的计算能力提供与GPT类似的大部分功能，尽管以较少的参数和更简洁的输出为代价。

如果您的应用程序不一定依赖于处理过度大的上下文或产生详细的输出，那么在您控制的实例上自行托管推理可能是一个更具成本效益的选择。而当谈及[检索增强生成](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_source=thenewstack&utm_medium=byline&utm_campaign=raG&utm_term=all-plays&utm_content=warhammer)(RAG)的实际应用时，成本差异可能会更加显著。

我将演示一个简单的方法，通过组合向量存储、词汇搜索和提示工程来在大众硬件上进行准确的RAG。使用这种方法，您可以降低大量信息的复杂性，并使生成式AI应用在规模上更准确、高效和具成本效益。通过在特定信息库上使用RAG，您可以获得消除幻觉并从任何源材料创建有效和知识渊博的代理的能力，而无需支付第三方API的费用。

开始使用，您需要一个DataStax Enterprise 7实例或[DataStax Astra DB](https://www.datastax.com/products/datastax-astra?utm_source=thenewstack&utm_medium=byline&utm_campaign=RAG&utm_term=all-plays&utm_content=warhammer)来存储向量和文本数据，以及一个LLM和一个句子转换器模型来生成响应并为数据编码向量。根据数据或用户提示的复杂性，您还可以考虑与DataStax Enterprise 6.8数据库相结合，该数据库可以执行Solr搜索以匹配更广泛的数据范围，这也是我在此示例中使用的。DataStax不断努力改进，以使所有这些操作都可以通过单个数据库完成，但就目前而言，我使用了两个数据库。

## 解决幻觉问题

无论您选择哪种LLM，它们都仍然存在[幻觉](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)问题。目前，这一局限性需要通过向LLM的提示上下文中输入真实信息来解决，也称为RAG。您定位信息并将其转换为提示的方法完全取决于您的数据模型，但是通过使用向量数据库，您可以以更高效的方式找到更相关的信息。

假设您有一系列关于您想探索的主题的电子书，例如如何玩[战锤40,000](https://warhammer40000.com/)。在正常情况下，您需要花费多年的时间阅读支持文献，并积累足够的游戏经验才能达到专家级别。

这样一个有针对性的问题，"你能告诉我关于Adepta Sororitas的Morvenn Vahl的什么?" 最好由一位资深玩家或任何一位战锤商店的员工回答。尽管ChatGPT可以回答关于这个游戏的许多问题，但不幸的是，它没有覆盖这个特定角色的训练数据:

![缩放](https://cdn.thenewstack.io/media/2024/02/f7cf6487-image1a.png)

与此相比，在配备Nvidia RTX A4000图形卡的消费者工作站上托管的13B参数的Llama 2 LLM。类似地，该模型可以演示对战锤宇宙的基本知识，但由于调优的原因，模型不在意该角色未被发现，而是提供了最佳的幻觉回复:

![缩放](https://cdn.thenewstack.io/media/2024/02/45de8075-image2a.png)

如果您想搭建一个能帮助新手和老手玩战锤40，000的聊天机器人，那么这些输出是不可接受的。要成为一个有效的游戏指导，聊天机器人需要知道游戏的规则、每个单位的规则、一些关于背景故事的知识，以及一些策略和评论。幸运的是，所有关于第10版规则的这些信息都可以免费从Games Workshop和粉丝网站获得，您所需要做的就是使您的聊天机器人应用能搜索到这些信息。

与让含有RAG的相同的13B Llama模型相比，其被要求比较关于Morvenn Vahl的一些来源，并根据用户提示派生出相关的答案。这次，聊天机器人可以访问[一个搜索数据库和一个向量数据库](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/)，其中包含有关如何玩战锤40，000第10版的所有公开信息:

![缩放](https://cdn.thenewstack.io/media/2024/02/c7e3e4da-image3a.png)

有了巨大的不同!它不仅找到了关于这个小众角色的相关信息，还使其输出保持与如何用第10版规则玩游戏的上下文一致。

在所有这些中，最困难的部分是执行有效的搜索以找到相关页面并馈送到LLM。这就是向量数据库特别有用的地方。

## 应用向量

在这个例子中，我们将使用运行在Docker实例中的DSE 7和DSE 6.8来满足聊天机器人应用的数据库需求，它需要能够比较向量并执行词汇搜索。DSE 7和Astra DB已经引入了存储向量、执行向量搜索以及通过文本匹配进行过滤的功能。对于这个例子，我们只需要搜索几十本书，所以在Docker中运行DSE实例对大多数消费者硬件来说就足够了。

在数据库中使用向量将有助于找到与给定查询相似的文档，或者它们可以用于比较从另一个搜索中检索到的结果。这可以帮助您克服词汇搜索的局限性，并提高数据模型的有效性。

例如，像电子书PDF这样的内容可以从使用[miniLM](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)等句子转换器进行编码中受益，并且向量可以用于在查询和给定源之间运行相似性比较。在这种情况下，句子转换器模型用于创建电子书页面文本的嵌入，这可以使您与用户的提示进行比较，以确定结果是否与查询相关。相关页面应该包含与用户查询相似的一个或多个术语的实例，并从模型的角度产生更好的相似性分数。

也就是说，向量的最佳用法是作为对现有词汇搜索模型的补充。如果仅根据向量进行搜索，则可能最终检索到不相关的文档，并将其作为上下文提供，而这些上下文并不适用。

在这个例子中，查询“你能告诉我关于Adepta Sororitas的Morvenn Vahl什么?”可以由一个LLM转换为一组简单的搜索词:

Morvenn,Vahl,Adepta,Sororitas

找到相关文档的第一步将是搜索包含这些基本术语的文档。这可以通过先在数据库中进行文本匹配过滤来找到与这样一个查询匹配的页面文本中的关键词来完成。使用LLM生成关键词的原因是提供更广泛的可能关键词来搜索，因为它通常会尝试添加更多相关但不在原提示文本中的关键词。但是要当心这一点，因为LLM也可以生成特殊字符和奇怪的序列，您需要对其进行清理。

一旦您至少有一个结果，就可以将用户的查询向量化，并将其与词汇搜索的向量进行比较，创建每个结果的相关性分数。这使您可以检查搜索结果对查询的准确性，并在最终向LLM呈现结果时设置拒绝不相关结果的阈值。

在这种情况下，第一步应该匹配具体显示Morvenn Vahl索引卡或游戏机制的页面，因为这些页面描述了该角色在游戏中的单位播放方式。如果页面与用户查询的相关性达到应用程序确定的某个阈值，则将其总结并放入结果列表中。

最后，搜索结果可以被编译成一个列表并馈送回LLM，在那里它被要求使用最相关的上下文来回答原始查询。以下是流程的可视化:

![缩放](https://cdn.thenewstack.io/media/2024/02/48c5d7de-image1.png)

如您所见，这个流程中LLM被频繁调用。LLM负责将用户提示转换为关键词，总结适用的结果，并选择哪个上下文最能回答查询。要检查的每个源都增加了另一个LLM调用，这对于查询GPT而言可能相当昂贵。但是，如果您已经拥有所需的信息，只想要总结或转换它，那么您可能不需要使用如此大的模型。事实上，切换到较小的模型可以提供许多好处。

通过使用较小的LLM，您可以降低每个查询的计算成本，从长期来看这可以节省大量资源。这也可以为用户带来更快的响应时间，从而提升其整体体验。在这个例子中，在同一个GPU实例上使用小型LLM和小型数据库执行RAG，需要大约30秒的时间来检索15个源，分析其相关性并提供最终答案。且提示(源)越短，输出可以返回得越快。

此外，这种方法允许增加安全性和可扩展性。通过提示工程和对LLM的调用流水线，您可以[完全控制数据](https://thenewstack.io/the-path-to-getting-the-full-data-stack-on-kubernetes/)的访问方式以及用户在响应中获得的内容。在资源使用方面，13B参数的示例模型仅消耗略高于8GB的VRAM，但仍能提供相关的答案。根据需求，这表明即使在用户工作站和移动设备等无数其他平台上运行RAG也具有潜力。

## 控制输出

提示工程对于使RAG完全按照您的意愿行事至关重要。您可以控制聊天机器人如何解释数据以及应考虑的上下文。在这个例子中，我们要确保聊天机器人知道我们特别在寻求有关战锤的信息，所以我们可以先要求它帮助为用户的查询提供支持上下文:

```
Query: “<user query>”

Answer:

Warhammer 40,000 is full of terms and names that might appear in other, unrelated popular culture, so it is important to set the context of the RAG in the very first query. This context should be something available to select or modify if your application covers multiple contexts, such as if you need to cover multiple editions of the Warhammer game rules or combine with the official lore books.
```

请注意，在这个试验中，用户的查询始终用引号封装。这有助于LLM区分它正在尝试直接回答的查询和单独的提示工程指令，后者不应直接回答。提示的问题/答案部分可以调整以适应特定的上下文，但您主要需要能够做的是告知LLM它应该和不应该直接回复什么，以及如何回复。

在这种情况下，可以安全地假设LLM确实对游戏宇宙有一般的知识，因为该系列是相当流行的，一般信息可以免费获得。第一个查询的输出有助于在词汇搜索中生成一些关键词，而无需在我们的应用程序中构建作弊表。

然后可以在后台执行词汇和向量比较，并编译结果列表以供LLM审阅。因为用户的原始提示在第一步永远不会用推理直接回答，所以LLM只转换在搜索中找到的内容，并且可以轻松停止回答其警戒线或知识库之外的查询。

```
Query: “<user query>”

Review these search results and use them to answer the query.

Result 1

Result 2

etc.

Answer:

If there are no relevant results from the search:

Query: “<user query>”
Politely tell me you searched but could not find an answer for the query. Answer to the best of your knowledge instead.

Answer:

For added security, you can completely reject or redirect the request when it cannot be served.

Query: “<user query>”

Politely tell me you searched but could not find an answer for the query. Instruct me to reach out to the Customer Support team for assistance instead.

Answer:

You can even make the outputs lengthier by asking for more details. As long as you can fit your source material within the context window, the LLM can transform it for you.

Query: “<user query>”

Review these search results and use them to answer the query. Be as detailed as possible and cite the sources.

Result 1

Result 2

etc.

Answer:
```

## 局限性

LLM具有有限的上下文窗口，将无法处理异常大的文本页面。考虑对行大小进行限制，以使[数据更易于管理](https://thenewstack.io/what-is-data-management-in-the-kubernetes-age/)，LLM也更容易处理。例如，将页面切分成约1，000字符的块似乎效果很好，并尽量避免将超过四五个详细答案喂入提示中。

LLM没有对话的记忆，除了您可以装进上下文窗口的内容。可以构建对话数据的永久存储，但LLM不可能在提示中适应过分大的对话或详细的上下文;它可以转换的内容有上限。这意味着无论如何，在某个时候您会注意到，即使在提供上下文的情况下，LLM似乎也会“忘记”某些细节;这仅仅是该工具的一种固有局限性。最好只依赖它进行短对话，并专注于每次转换小量文本，以尽量减少幻觉。

LLM的随机性可能是一个问题。需要测试和调优以确定哪些提示对您的数据集效果最佳，以及哪种模型最适合您的使用案例。在我用13B参数模型进行的测试中，随着提示长度的增加，第一个提示生成的搜索关键词存在很多不可预测性。为了获得最佳结果，请坚持使用较短的提示。

## 结论

总之，利用RAG通过组合向量和词汇搜索模型可以更有效地找到和排序相关结果，并生成远少出现幻觉的代理输出。可搜索的上下文越小，响应就越精确和准确。构建自己的自定义LLM调用流水线可以在调整响应方面提供更大的灵活性，以达到所需的准确性和警戒线。

尽管它无法在有限的上下文窗口内处理过量的数据，但它确实提供了在有限知识库上创建有效助理的能力，以及在与以前相同或更少的硬件上运行更多并发代理的能力。这可能为桌面游戏等应用的虚拟助手打开更多可能性，甚至可以覆盖政府、法律和会计事务所、科学研究、能源等更复杂的主题。

如果您准备开始构建，可以免费试用Astra DB。今天就创建您的数据库并开始加载RAG源，无需任何云或数据库运维经验。
