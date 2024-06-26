<!--
title: 提高检索增强的相关性
cover: https://cdn.thenewstack.io/media/2023/11/8fdb1433-fetching-1024x696.jpg
-->

次优的嵌入模型、低效的分块以及缺乏元数据过滤可能会影响LLM响应的相关性。以下是应对方法。

> 译自 [Fixing Relevancy in Retrieval Augmentation](https://thenewstack.io/fixing-relevancy-in-retrieval-augmentation/)。作者Chris Latimer是DataStax的产品管理副总裁，领导公司在事件流和云消息传递方面的产品策略。 在加入DataStax之前，克里斯在谷歌、NetJets和Apigee等公司担任软件工程师、架构师和产品经理，在技术领域工作了20多年。

构建采用[检索增强生成](https://www.datastax.com/guides/what-is-retrieval-augmented-generation?utm_source=thenewstack&utm_medium=byline&utm_campaign=RAG&utm_term=all-plays&utm_content=fixing-relevance)(RAG)的生成式AI应用程序可能面临各种挑战。让我们来看看依靠向量数据库检索相关上下文，然后将其融入提示送入[大语言模型(LLM)](https://roadmap.sh/guides/introduction-to-llms)，以提供更相关结果的RAG实现的故障排除。

我们将这个过程分成两个主要部分。第一个是嵌入流水线，它用嵌入填充[向量数据库](https://www.datastax.com/guides/what-is-a-vector-database?utm_source=thenewstack&utm_medium=byline&utm_campaign=RAG&utm_term=all-plays&utm_content=fixing-relevance):

![](https://cdn.thenewstack.io/media/2023/11/a413da9c-image1a.png)

在这里，我们将考察三个可能导致糟糕结果的主要领域：次优的嵌入模型、低效的分块策略以及缺乏元数据过滤。

第二个领域是与LLM的实际交互，这里用简化的形式表示:

![](https://cdn.thenewstack.io/media/2023/11/4343d5ac-image2a.png)

我们将检查一些常见的问题，这些问题可能导致糟糕的结果，包括不精确的提示和不充分的生成方法。

## 选择合适的嵌入模型

您选择的嵌入模型将对RAG应用程序的整体相关性和可用性产生重大影响。因此，这需要对每个模型的功能以及这些功能与应用程序要求的匹配进行细致的理解。

如果您对RAG和嵌入整体比较陌生，您应该知道的最好资源之一是[MTEB(大规模文本嵌入基准)嵌入排行榜](https://huggingface.co/spaces/mteb/leaderboard)。本文重点关注检索用例，但嵌入当然可以用于许多其他应用，包括分类、聚类和总结。该排行榜可以帮助您确定对特定用例表现最佳的模型。

RAG性能差的一个最常见原因是开发人员刚接触这个领域，进行谷歌搜索以找到嵌入生成的示例。他们经常发现使用Word2Vec、sBERT和RoBERTa等嵌入模型的样本代码，而这些模型对于检索用例来说是糟糕的选择。如果您由于相关性结果差而找到这篇文章，并且您使用了类似sBERT的模型生成嵌入，那么我们可能已经找到了相关性问题的原因。

如果是这样，您下一个自然的问题可能是哪些嵌入模型可以用来改进[相似性搜索结果](https://thenewstack.io/datastax-adds-vector-search-to-astra-db-on-google-cloud/)。在不知道您的具体用例的情况下，我们推荐的三个是:

### text-embedding-ada-002 (Ada v2)

[来自OpenAI的Ada v2](https://openai.com/blog/new-and-improved-embedding-model)可能是大多数RAG应用程序的最常见起点，简单是因为许多开发人员一开始就使用OpenAI的API。Ada v2在检索用例中表现突出，它是为处理不同类型的内容(包括文本和代码)而构建的。它支持长达8192个标记的最大输入序列长度，也允许您为比替代模型更长的文本创建嵌入。这既是优势也是劣势。拥有大序列长度简化了为更多文本内容创建嵌入的过程，它允许嵌入模型在更大的文本体中识别单词和句子之间的关系。

然而，这也会导致在比较两个长文档的相似性时结果变得模糊，而您正在寻找的是相关上下文以促进生成过程。

Ada v2有两个主要缺点。第一个是它不能在本地运行。您必须使用OpenAI的API来创建嵌入。这不仅可能在您希望为许多内容创建嵌入的情况下引入瓶颈，而且还增加了每1000个标记0.0001美元的成本。第二个是OpenAI模型创建的嵌入每个都是1536维的。如果您使用云向量数据库，这可以大大增加向量存储成本。

**何时选择**：您需要一个只需要API调用的简单解决方案，您可能需要为大型文档建立向量，成本不是问题。

### jina嵌入式v2(Jina v2)

Jina v2是一个新的开源嵌入模型，它为您提供与Ada v2相同的8000输入序列支持，实际上在检索用例中得分略高。

Jina v2提供了对Ada v2问题的解决方案。它是Apache许可证2.0下的[开源](https://huggingface.co/jinaai/jina-embeddings-v2-base-en?ref=jina-ai-gmbh.ghost.io)，可以在本地运行，当然，如果您不想运行自己的代码来做到这一点，这也是一个劣势。它还产生一个具有Ada v2一半维数的嵌入向量。因此，不仅在基准用例的检索性能方面略胜一筹，而且还以较低的存储和计算需求从向量数据库角度获得了这些改进的结果。

**何时选择**：您希望使用开源解决方案，可能需要为大型文档建立向量，并且适应在本地运行嵌入管道。您想要降低矢量数据库成本，使用较低维度的嵌入。

### bge-large-en-v1.5

[bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)在MIT许可下开源，目前在检索用例的MTEB排行榜上排名第一的嵌入模型。带有更小的输入序列，它将需要您更多地考虑分块策略，但最终为检索用例提供了最佳的全面性能。

**何时选择**：您希望使用开源解决方案，并愿意花更多时间研究分块策略，以适应输入大小限制。您适应在本地运行嵌入管道。您想要检索用例中表现最佳的嵌入模型。

虽然超出本文的范围，但您可能需要更深入地研究MTEB排行榜中的15个基准，以确定最接近您特定情况的基准。虽然各种嵌入模型在不同基准中的表现确实存在模式，但通常每个基准中都有特定的模型脱颖而出。如果您需要进一步优化嵌入选择，这是一个可能的进一步调查区域。

## 优化分块策略

输入文本的分割或“分块”是关键因素，它会显著影响生成输出的相关性和准确性。各种分块策略提供了独特的优势，适用于特定类型的任务。在这里，我们深入研究这些方法，并提供应用建议，结合一些关键注意事项：

- **固定长度分块**:
  - **何时使用**: 除非您的内容本身高度结构化且长度固定，否则通常需要依靠更有用的分块策略，如下所述的策略。
  - **技术考量**: 虽然实现非常简单，但这种分块策略通常会导致RAG应用程序的性能差。
  - **额外见解**: 如果您在RAG应用程序中使用固定长度策略并且相关性出现问题，则应考虑切换到不同的分块方法。


- **句子级分块**:
  - **何时使用**: 当输入文本中的每句话都充满意义和上下文时，此策略很有效。它允许模型专注于每句话的细微之处，从而生成更连贯和相关的响应。您很少会在RAG用例中使用句子级分块。
  - **技术考量**: 句子级分块通常涉及基于句子边界的标记化，这可以使用自然语言处理(NLP)库来实现。
  - **额外见解**: 当您在寻找特定语句时，例如在会议记录中寻找与给定文本语义上相似的语句时，句子级分块尤其有用。


- **段落级分块**:
  - **何时使用**: 当输入文本组织成独立的段落，每个段落封装一个单独的想法或主题时使用此策略。这使得模型能够专注于每个段落中的相关信息。
  - **技术考量**: 识别段落边界通常涉及检测表示段落结束的换行符或其他分隔符。
  - **额外见解**: 当您拥有涵盖同一主题的许多不同方面的文档时，段落级分块很有用。例如，产品文档页面可能会介绍产品功能，解释何时使用它，讨论如何配置它并给出不同配置的示例。使用段落级分块可以帮助您确定为LLM提供上下文的文档中最相关的部分。


- **内容感知分块**:
  - **何时使用**: 当文本中特定部分的相关性至关重要时，选择此策略。例如，在法律文件中，根据条款或章节对文本进行分割可以产生更具针对性的响应。
  - **技术考量**: 这种方法可能需要先进的NLP技术来理解文本中的语义边界。
  - **额外见解**: 在处理结构化或半结构化数据时，内容感知分块特别有用，因为可以将特定块与元数据过滤相结合，以实现更精确的检索。例如，在法律文档中，您可能希望提取所有保修或赔偿条款，并在将文本块嵌入存储在向量数据库中时，可以使用元数据使其更容易根据构建RAG用例时需要的内容类型进行搜索。

- **递归分块**:
  - **何时使用**: 递归分块使用分层方法将数据分成越来越小的碎片。例如，在对文本文档进行分块时，您可以先将文本分成段落，然后分成句子，最后分成词。一旦将数据分割成第一组块，然后可以递归地将分块过程应用于每个较小的块，重复直到达到您感兴趣的最小块大小。
  - **技术考量**: 实现递归分块可能涉及多级解析策略，其中块被进一步划分为子块，具体取决于其他条件。如果使用LangChain，其递归实现比这里描述的要简单得多。
  - **额外见解**: 这种方法使模型能够在多个层面上理解上下文，从高级主题到详细的细微差别，这对于复杂的文档(如学术论文、技术手册或法律合同)特别有用。这样既带来了灵活性的优势，因为相似性搜索可以识别较广泛和较短查询的相似文本；又存在源文档中的相似块在相似性搜索中被过度表示的可能性，特别是如果在文本拆分器配置中选择较长的块重叠。

作为一种通用方法，在尝试将大型语料库分块并向量化之前，您应该考虑对数据进行一些特殊实验。手动检查在给定查询下您希望检索的文档，确定表示您希望为LLM提供的理想上下文的块，然后尝试不同的分块策略，看哪种策略为LLM提供您认为最相关的块。

### 上下文窗口的考量

LLM的可用上下文窗口是选择分块策略的一个重要因素。如果上下文窗口很小，您需要在馈送模型的数据块中进行更选择性的选择，以确保包含最相关的信息。相反，更大的上下文窗口允许更大的灵活性，即使并非所有内容都严格必要，也可以包含可能增强模型输出的额外上下文。

通过实验这些分块策略并考虑这些因素，您可以评估它们对生成输出相关性的影响。关键是将所选策略与RAG应用程序的具体要求相匹配，保持输入的语义完整性，并对上下文进行全面理解。这将使您能够找到最佳性能的正确分块流程。

## 元数据过滤

随着搜索索引中的嵌入数量的增长，近似最近邻居(ANN)在查找相关上下文以包含在提示中的用处变得不大。假设您在知识库中为200篇文章建立了索引嵌入。如果您可以以1%的准确率识别最近的邻居，那么找到非常相关的结果的可能性很高，因为1%代表200篇文章中的前两篇文章，您将获得这两篇文章之一。

现在考虑一个包含维基百科上每一篇文章的搜索索引。这大约是670万篇文章。如果您的最近邻居位于最相似文章的前1%，这意味着您将获得约67，000篇最相似文章之一。对于像维基百科这样的语料库，这意味着您最终仍可能偏离目标。

元数据过滤提供了一种方法，可以先过滤文档，然后再应用最近邻算法来缩小内容块的范围。在处理大量可能匹配的情况下，这种初始预过滤可以帮助您在检索最近的邻居之前缩小可能的选项。

## 完善提示

即使是最好的嵌入和分块策略也无法取代高质量的[提示工程](https://www.datastax.com/guides/what-is-prompt-engineering?utm_source=thenewstack&utm_medium=byline&utm_campaign=RAG&utm_term=all-plays&utm_content=fixing-relevance)的需要。这涉及使[提示更明确、更具体和更符合预期](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)输出。应该测试各种提示格式、长度和词汇选择以微调RAG过程。

具体来说，在为RAG应用程序构建提示时，您应该考虑几件事。这些包括:

**告诉LLM其角色**: 与ChatGPT等LLM代理交互时，它们默认会充当有帮助的聊天机器人。但是，您可以通过指示LLM以特定方式行事来改变将生成的响应的性质。示例可以是“你是一个律师，正在评估任何一方是否违反了协议”或“你是互联网服务提供商的客户服务代理；您的工作是帮助人们解决互联网问题”或任何与您的特定情况相关的内容。

**明确告诉LLM使用提供的上下文**: 明确告诉LLM您正在提供上下文，并且您希望生成的响应反映该上下文。您可以通过说“您的响应应考虑以下上下文”然后添加上下文来实现这一点。

**使用示例**: 在上述要求LLM充当评估合同的律师的场景中，您可能希望在提示中包含几个示例。例如，您可以提供一个合同示例，说明在合同签署后30天内应付款，但买方在合同签署后40天才发送付款，因此违反了协议。您可以提供有关补救权利和可能的合同违约解决方法的额外示例。

**指定输出格式**: 如果您的用例需要特定输出，您可以指定生成输出应遵循的格式。您可以将这种技术与上述提示相结合，以提供示例，使LLM明确知道您希望它如何响应以及您希望生成的响应中需要包含的关键信息点。

**使用思路链**: 对于需要推理才能确定适当响应的用例，您可以考虑使用一种称为[思路链](https://digitaliq.com/2023/10/14/what-is-chain-of-thought/)的技术来帮助解释您希望LLM遵循的步骤以得出生成的响应。例如，在法律合同的例子中，您可能希望引导LLM遵循人员确定合同条款是否已违反的逻辑步骤。例如，在处理法律合同时，您可能会告诉LLM首先查找指定付款条款的条款，然后确定买方提交付款的时间，然后计算收到付款与签订合同日期之间的天数。然后，如果付款时间超过了约定的时间范围，买方就违反了协议。

利用这些技术改进提示工程可以显著提高您能够在RAG应用程序中生成的结果质量。但是，有时您需要使用涉及与LLM多次交互的技术才能获得可接受的响应。

## 高级模式

### FLARE

前向主动检索(Forward-looking active retrieval，FLARE)是一种多查询RAG技术的例子，它涉及在提示中以定制指示迭代调用LLM，要求LLM提供有关关键短语的额外问题，这些关键短语将有助于它生成更好的答案。一旦LLM具有无间隙的上下文，它就会以最终响应结束。该过程在LLM和AI代理(图中的AI聊天机器人)之间添加了一个循环，以促进这些迭代:

![](https://cdn.thenewstack.io/media/2023/11/5caaf8aa-image3a.png)

您可以在[LangChain Cookbook的FLARE示例](https://github.com/langchain-ai/langchain/blob/master/cookbook/forward_looking_retrieval_augmented_generation.ipynb)中看到FLARE的工作方式。

### RAG Fusion

通过生成类似用户查询的查询并为原始查询和生成的类似查询检索相关上下文，我们能够增加选择最有用上下文来生成准确结果的可能性。该过程称为“RAG融合”，如下所示:

![](https://cdn.thenewstack.io/media/2023/11/773dcc40-image4.png)

这里的关键步骤是[利用排名函数](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)进一步优化ANN结果，以确定要使用的生成响应的最相关上下文。

## 总结

RAG是一个简单上手但常让开发者对莫名其妙的糟糕结果感到沮丧的方法。RAG支持的生成AI应用程序中的输出相关性可能受几个因素的影响。通过精心选择嵌入模型、制定分块策略和设计提示，您可以显著提高ChatGPT等LLM驱动的系统中生成响应的质量和精确度。希望这些技巧能帮助您创建更有用的RAG应用程序，提供您期望的体验和价值。

试试[DataStax Astra DB](https://www.datastax.com/products/vector-search?utm_source=thenewstack&utm_medium=byline&utm_campaign=RAG&utm_term=all-plays&utm_content=fixing-relevance)，这是市场上唯一一个用于构建实时数据AI应用的向量数据库。