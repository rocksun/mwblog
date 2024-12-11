# 阻止AI谎言：利用可信来源获得更智能的答案

![主题图片：阻止AI谎言：利用可信来源获得更智能的答案](https://cdn.thenewstack.io/media/2024/12/578a4f98-fake-1024x576.jpg)

当您使用GPT-4或搜索互联网时，其回复通常包含引用，将信息链接到其来源。这种透明度允许您作为用户验证内容并信任您收到的答案。引用来源对于确保[AI生成的回复](https://thenewstack.io/ai/)中的问责制和可靠性至关重要，尤其是在准确性至关重要的应用中。

[带有引用的检索增强生成 (RAG)](https://zilliz.com/learn/Retrieval-Augmented-Generation?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns) 应用了这一原则，它从外部数据源检索相关信息，并将生成的回复链接回其来源。通过将输出与准确检索到的数据关联并引用来源，基于RAG的系统增强了信任度和透明度。这种方法在研究、医疗保健和法律服务等领域特别有价值，在这些领域，验证信息至关重要。

让我们探讨一下引用在RAG系统中的重要性。我还将演示它们在确保可靠AI输出中的作用，并提供一个逐步指南，指导您在应用程序中实现带有引用的RAG。

## 什么是检索增强生成？

检索增强生成，或[RAG](https://zilliz.com/learn/Retrieval-Augmented-Generation)，是一个框架，它通过将信息检索与[大型语言模型 (LLM)](https://zilliz.com/glossary/large-language-models-(llms)?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)的生成能力相结合来提高AI回复的准确性和相关性。虽然[像GPT-3和GPT-4这样的LLM](https://thenewstack.io/llm/)是在大量数据集上训练的，但它们的知识仅限于在其训练期间可用的静态数据。这种限制使得它们在回答有关近期事件或特定领域信息的问题时效率较低。

RAG通过从外部知识库检索相关且最新的文档来解决这一挑战。然后，这些检索到的文档被用作LLM生成更精确回复的上下文。这种检索和生成相结合的方式创建了既准确又灵活的系统，使它们能够处理更广泛的查询。

例如，想象一下向一个RAG驱动的系统询问：“休斯顿的当前人口是多少？”检索器可能会找到包含2024年人口普查数据的文档，并将其作为输入提供给语言模型。然后，系统根据最新的2024年人口普查报告回应说，休斯顿的人口约为240万。这确保了响应的准确性并以可靠的数据为基础。

## 为什么引用很重要？

引用在RAG系统中至关重要，因为它们提供了一条清晰的路径，可以追溯到回复中使用信息的来源。这在信任和可靠性至关重要的场景中尤其重要。如果没有引用，用户必须完全依赖系统的权威性，这可能会导致不确定性或不信任，尤其是在高风险领域。

### 确保透明度

引用通过显示信息的来源，使RAG系统的内部运作透明化。例如，如果法律助理从合同中检索一个条款，它可以包含一个指向特定部分的引用。这允许用户验证回复并理解其基础，从而降低误解或错误的风险。

### 建立信任

引用其来源的系统能够培养信任，因为用户可以独立验证其提供的答案。这在医疗或学术环境中非常有价值。例如，引用医学期刊或治疗指南的医疗保健聊天机器人确保用户对其建议充满信心，因为他们知道这些建议是有可靠证据支持的。

### 添加上下文

引用通过向AI生成的回复添加上下文来增强用户的理解。引用提供了诸如来源日期或作者等详细信息，帮助用户评估信息的可靠性和相关性。例如，关于科学突破的回复可能会链接到最近的一项研究，允许用户进一步探索该主题。

### 提高可解释性

引用有助于[通过揭示如何生成回复来提高RAG系统的可解释性](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/)。用户和开发人员都可以追溯推理过程，这在法律研究或合同分析等复杂应用中非常有用。
引用不仅验证了响应，还提高了系统的鲁棒性。它们确保了问责制，使RAG系统适用于需要准确性的关键任务。

现在我们已经确定了引用的重要性，让我们探讨如何构建一个包含引用的系统。

## 构建带有引用的RAG系统

构建引用系统需要用于数据收集、处理和检索的工具。让我们逐步创建一个从维基百科收集信息、使用[Milvus Lite](https://milvus.io/docs/milvus_lite.md?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)处理信息并生成带有引用的响应的RAG系统。Milvus Lite是[Milvus向量数据库](https://milvus.io/?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)的轻量级版本，旨在高效存储和检索[向量嵌入](https://zilliz.com/learn/everything-you-should-know-about-vector-embeddings?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)，它们是数据的数值表示。它们捕获数据点之间的[语义关系](https://zilliz.com/glossary/semantic-similarity?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)。

### 安装所需的库

首先，安装构建应用程序时所需的这些[Python包](https://thenewstack.io/the-top-5-python-packages-and-what-they-do)：

```bash
pip install llama-index llama-index-vector-stores-milvus python-dotenv requests
```

`llama-index`包为[RAG操作和向量处理](https://thenewstack.io/vector-embeddings-explained-a-beginners-guide-to-powerful-ai/)提供了基础。[Milvus集成包连接到我们的向量存储](https://thenewstack.io/what-is-milvus-vector-database/)。`python-dotenv`用于安全地保存API密钥，而`requests`则用于从维基百科获取数据。

### 设置您的环境

安装完成后，下一步是将它们导入您的代码中。此外，将OpenAI API密钥加载到您的环境中。如果您没有API密钥，[请从此处获取](https://openai.com/api/)。

您的环境现在已准备好开始编写应用程序的逻辑代码。

### 创建您的知识库

系统首先需要知识库。我们将使用关于北美城市的维基百科文章来形成我们的知识库。这些数据将使我们能够在跟踪信息来源的同时回答问题。让我们从定义我们的数据源开始。

定义好数据源后，您需要一种方法来收集和组织这些信息。

上述函数为可靠的引用创建了基础。当它获取文章时，它还会记录重要的元数据：标题、来源、URL和访问日期。这些元数据在系统需要引用其来源时变得至关重要。通过在本地存储内容和元数据，它创建了一个持久性知识库，可以重复使用而无需重复访问维基百科。

该函数将每篇文章及其元数据包装在一个LlamaIndex Document对象中。这些Document对象是RAG系统的构建块；它们包含生成准确引用所需的所有上下文信息。

### 管理文档存储

为了使知识库在多个会话中可访问，我们需要一种方法来重新加载保存的信息：

上面的代码从保存的文件中重建Document对象，保持内容与其来源之间的连接。默认的元数据值确保即使元数据文件丢失，系统也能保持健壮性。

### 设置向量存储

现在是RAG系统的一个关键部分：将文本转换为计算机可以高效搜索的格式。这是通过一个称为嵌入生成的流程实现的。当文本被输入到[LlamaIndex](https://zilliz.com/learn/getting-started-with-llamaindex?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)时，它使用OpenAI的[text-embedding-ada-002](https://zilliz.com/ai-models/text-embedding-ada-002?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)模型将文本转换为1536个数字（向量）的列表。这些向量捕获了文本的语义含义。即使使用不同的词语，相似的概念也具有相似的向量。为了高效地存储和搜索这些向量，我们将使用Milvus Lite。

当`VectorStoreIndex`
创建知识库时，后台会发生一系列操作。文档会被[分割成块](https://zilliz.com/learn/guide-to-chunking-strategies-for-rag?utm_source=vendor&utm_medium=referral&utm_campaign=2024-12-05_blog_rag-with-citations_tns)；每个块都被转换成嵌入向量，这些向量存储在Milvus Lite中。块之间的重叠确保重要的信息不会在块边界丢失。

### 创建查询引擎

知识库嵌入并存储后，我们需要一种方法来查询它并生成带引用的回复：

当你提出问题时，会发生以下几件事：

- 你的问题会被转换成一个嵌入向量。在本例中，查询是：“西雅图还是休斯顿的机场更大？”
- Milvus Lite 找到知识库中三个最相似的块。
- 这些块及其元数据被发送到 GPT-3.5 Turbo。
- GPT-3.5 Turbo 根据这些块生成回复。
- `CitationQueryEngine`添加引用以显示信息来源。

为了使这些引用更有用，让我们添加一种显示它们的方法：

### 格式化来源引用

来源引用帮助我们验证信息并将事实追溯到它们的来源。让我们创建一个函数来显示引用元数据：

上面的代码为每个来源显示多个引用元素。标题显示哪个文章提供了信息。来源和URL允许用户找到原始文档。访问日期有助于跟踪信息的时效性。文本摘录显示了告知答案的具体段落，允许直接验证所使用信息。

### 整合所有部分

最后，你需要一个主函数来协调所有这些组件：

上面的代码协调整个过程。首先，它通过`scrape_wikipedia()`触发维基百科数据收集。此函数收集文章及其元数据，并将它们存储在本地。接下来，`setup_rag_with_citations()`初始化RAG系统，创建向量嵌入，设置Milvus Lite并准备查询引擎。错误处理包装这些操作以捕获并报告任何问题，确保系统可靠运行。这种顺序执行确保所有组件在系统处理问题之前都已准备好。

让我们看看RAG系统如何处理关于机场大小的查询。以下是预期的输出：

![带引用的RAG系统比较机场大小的结果](https://cdn.thenewstack.io/media/2024/12/4009ee1d-image1a-1024x569.jpg)
带引用的RAG系统比较机场大小的结果。

输出显示我们的系统能够正确回答问题，并引用维基百科中的相关来源来支持其答案。

## 结论

带引用的检索增强生成改变了AI系统传递信息的方式，在AI能力和用户信任之间架起了一座桥梁。与仅限于其训练数据的传统AI模型不同，RAG系统主动检索并引用相关信息，使用户能够验证来源并检查参考段落。这种透明度将抽象的回复转化为可验证的事实，使这些系统在研究、医疗保健和法律服务等需要准确性和问责制的领域中变得非常有价值。通过将每条信息与其来源关联起来，RAG系统增强了对AI生成回复的信心，同时为信息验证至关重要的应用打开了新的可能性。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)