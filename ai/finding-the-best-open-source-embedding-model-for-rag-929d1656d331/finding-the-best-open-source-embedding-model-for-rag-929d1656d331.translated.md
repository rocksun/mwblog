# 寻找最佳的开源嵌入模型用于 RAG

像[OpenAI](https://platform.openai.com/docs/models?ref=timescale.ghost.io#embeddings)的 text-embedding-large-3 和 text-embedding-small 这样的专有嵌入模型在检索增强生成 (RAG) 应用中很流行，但它们会增加成本、第三方 API 依赖性以及潜在的**数据隐私**问题。

另一方面，开源嵌入模型提供了一种经济高效且可定制的替代方案。通过在本地运行这些模型，您可以[停止支付 OpenAI 税](https://www.timescale.com/blog/the-emerging-open-source-ai-stack?ref=timescale.ghost.io)，并完全控制嵌入创建过程，增强数据隐私，并根据您的需求定制模型。

然而，评估开源嵌入模型可能很复杂、耗时且资源密集，导致许多工程师默认使用专有解决方案。

这篇博文将引导您完成一个**易于复制的工作流程，用于比较开源嵌入模型**，该工作流程使用[Ollama](https://ollama.com/?ref=timescale.ghost.io)，这是一个用于在本地运行大型语言模型 (LLM) 的开源平台，以及[pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io)，这是一个基于 PostgreSQL 的工具，用于通过单个 SQL 命令自动化嵌入生成和管理。我们将使用[Paul Graham 的文章](https://paulgraham.com/articles.html?ref=timescale.ghost.io)作为我们的评估数据集来演示此工作流程。

# 选择最佳开源嵌入模型：评估工作流程

比较开源嵌入模型的评估工作流程通常包括以下步骤：

- 准备用于嵌入生成的评估数据集
- 在本地机器上下载和设置嵌入模型
- 设置向量数据库以存储嵌入
- 为每个模型生成和存储嵌入
- 设计评估管道以评估模型
- 通过评估管道运行嵌入
- 比较结果以确定最佳模型

虽然此工作流程听起来很简单，但由于以下几个挑战，它的实现可能会很快变得复杂且资源密集：

**开源模型的访问和管理**: 为每个嵌入模型安装依赖项并确保系统兼容性可能很繁琐。存储管理是另一个问题，因为大型模型可能会消耗本地机器上的大量空间。**嵌入生成的自动化**: 建立一个可靠的工作流程来跨多个模型生成和摄取嵌入是复杂的。您需要处理资源限制、监控错误并确保效率，这可能需要大量工作。**创建公平且强大的评估管道**: 选择合适的评估数据集并定义清晰且相关的标准（例如检索质量或搜索准确性）对于确保所有模型的一致、无偏见和有意义的评估至关重要。

不用担心——我们可以让这个过程更容易！

虽然强大的评估管道的细节可能因您的 RAG 应用程序而异，但您只需使用两个工具即可显著降低复杂性：**Ollama** 用于访问和管理嵌入模型，以及 **pgai Vectorizer** 用于跨多个模型自动化嵌入生成和管理（我们在之前的文章中分享了如何[自动化嵌入生成](https://www.timescale.com/blog/how-to-automatically-create-update-embeddings-in-postgresql?ref=timescale.ghost.io)）。

**想一起参与吗？** 查看此[GitHub 存储库](https://github.com/timescale/pgai/tree/main/examples/finding_best_open_source_embedding_model?ref=timescale.ghost.io)，了解本文中使用的所有代码。

# Ollama：简化对开源嵌入模型的访问

Ollama 通过消除依赖项和兼容性方面的难题，使运行开源模型变得轻而易举。只需下载并运行模型即可——无需复杂的设置。它可在 macOS、Linux、Windows 和 Docker 环境中无缝运行。在此评估中，我们在 Docker 容器内运行 Ollama。

Ollama 通过捆绑模型的配置、数据和权重来简化模型管理。此捆绑包使清理和实验变得简单明了，同时确保完全拥有数据——您可以完全控制如何处理数据以及数据流向何处。

## 开源嵌入模型比较

Ollama 提供对最先进的大型语言模型的访问。在此评估中，我们比较了[Ollama](https://ollama.com/search?c=embedding&ref=timescale.ghost.io)上提供的三个最流行的嵌入模型：
[nomic-embed-text](https://www.nomic.ai/blog/posts/nomic-embed-text-v1?ref=timescale.ghost.io): 在短文本和长文本嵌入任务上均优于**text-embedding-ada-002**和**text-embedding-3-small**。 [mxbai-embed-large](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1?ref=timescale.ghost.io): 优于**text-embedding-3-large**，同时尺寸显著小于后者。

# Pgai Vectorizer：PostgreSQL中的自动嵌入管理

[Pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io)无需构建复杂的自动化基础设施来生成和管理多个模型的嵌入。它是一个开源的强大工具，旨在直接在PostgreSQL中自动化嵌入的创建和管理，PostgreSQL是一个广泛采用且强大的数据库，通过[pgvector](https://github.com/pgvector/pgvector?ref=timescale.ghost.io)和[pgai](https://github.com/timescale/pgai?ref=timescale.ghost.io)等扩展具有向量功能。

在本评估中，我们使用PostgreSQL作为数据库来存储评估数据集及其对应的嵌入。

对于此用例，pgai Vectorizer 的独特之处在于其**与Ollama的集成**，允许您使用Ollama支持的任何开源模型生成嵌入。

要为每个嵌入模型配置向量化器，只需使用一条包含所有嵌入配置的SQL命令，如下面的`create_vectorizer`函数所示。您可以在[pgai Vectorizer 的API参考](https://github.com/timescale/pgai/blob/main/docs/vectorizer-api-reference.md?ref=timescale.ghost.io)中找到有关这些配置的更多信息。

```python
def create_vectorizer(embedding_model, embeddings_dimensions):
    embeddings_view_name = f"{'essays'}{'_'}{embedding_model.replace('-','_')}{'_'}{'embeddings'}"
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
SELECT ai.create_vectorizer(
'essays'::regclass,
destination => %s,
embedding => ai.embedding_ollama(%s, %s),
chunking => ai.chunking_recursive_character_text_splitter('text', 512, 50),
formatting => ai.formatting_python_template('title: $title $chunk')
);
""", (embeddings_view_name, embedding_model, embeddings_dimensions, )
            )
```

在此之后，pgai Vectorizer 将处理所有繁重的工作：

- 自动生成和更新嵌入，以适应数据集的变化
- 将数据分割成块并进行格式化
- 创建一个表来存储具有指定名称的嵌入
- 生成一个视图，将您的数据与其嵌入结合起来，以便于访问和查询
- 管理嵌入生成队列

使用此[Docker compose 文件](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io#setup-a-local-development-environment)，您可以快速在Docker环境中配置PostgreSQL、pgai Vectorizer工作程序和Ollama服务。

要开始使用，请查看此[快速入门指南](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io)，了解有关pgai Vectorizer与Ollama集成的更多信息。

## 配置多个向量化器

运行PostgreSQL服务后，安装[pgai](https://github.com/timescale/pgai?tab=readme-ov-file&ref=timescale.ghost.io#quick-start)扩展。然后，您可以使用pgai函数插入评估数据集，[Paul Graham 的文章](https://huggingface.co/datasets/sgoel9/paul_graham_essays?ref=timescale.ghost.io)，该函数可直接将Hugging Face中的数据集加载到您的数据库中！[load_datasets](https://github.com/timescale/pgai/blob/main/docs/load_dataset_from_huggingface.md?ref=timescale.ghost.io)

```python
with connect_db() as conn:
    with conn.cursor() as cur:
        # 将 Paul Graham 的文章数据集加载到 'essays' 表中
        cur.execute("""
SELECT ai.load_dataset(
'sgoel9/paul_graham_essays',
table_name => 'essays',
if_table_exists => 'append');
""")
```

让我们使用`create_vectorizer`函数为每个嵌入模型配置一个向量化器！

```python
EMBEDDING_MODELS = [
    {'name':'mxbai-embed-large', 'dimensions': 1024},
    {'name':'nomic-embed-text','dimensions': 768},
    {'name':'bge-m3','dimensions': 1024},
]
for model in EMBEDDING_MODELS:
    create_vectorizer(model['name'], model['dimensions'])
```

向量化器的创建顺序与嵌入生成队列中的顺序相同。您可以使用以下函数查看队列：[vectorizer_status](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io#monitor-a-vectorizer)

```python
with connect_db() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM ai.vectorizer_status;")
        for row in cur.fetchall():
            print(f"Vectorizer ID: {row[0]}, Embedding Table: {row[2]}, Pending Items: {row[4]}")
```

# 评估流程
**丰富的嵌入**——捕获文本潜在含义、关系和上下文的高密度向量表示——对于RAG应用程序提供准确和相关的结果至关重要。我们的评估过程侧重于嵌入的两个关键方面：**语义理解**: 能够捕捉超越精确词语匹配的含义，包括同义词、释义和细微的措辞。**上下文检索**: 能够理解文本中更广泛的关系、意图和上下文，确保模型检索与查询含义一致的结果，即使措辞不同。

评估流程包括两个主要阶段：**测试数据生成**和**模型评估**。

## 测试数据生成

我们通过利用向量化器在嵌入过程中创建的文本片段来创建测试数据集。以下是我们方法的逐步分解：

**随机片段选择**: 我们通过查询其中一个嵌入表，随机选择了**20个文本片段**。由于向量化器使用相同的配置进行分块和格式化，这确保了数据的一致性。**问题生成**: 对于每个检索到的文本片段，我们使用Ollama提供的强大且开源的生成式LLM生成了**20个问题**。**Llama 3.2**

这些问题在以下五个类别中平均分配，以模拟人类提问的方式。这些问题使我们能够模拟RAG应用程序可能收到的潜在查询：

此函数为每个文本片段生成特定类型的疑问：

```python
def generate_questions_by_question_type(chunk, question_type, num_questions):
    prompts = {
        'short': "Generate {count} short, simple questions about this text. Questions should be direct, under 10 words",
        'long': "Generate {count} detailed, comprehensive questions about this text. Include specific details:",
        'direct': "Generate {count} questions that directly ask about explicit information in this text",
        'implied': "Generate {count} questions that require understanding context and implications of the text:",
        'unclear': "Generate {count} vague, ambiguous questions about the general topic of this text:"
    }
    prompt = prompts[question_type].format(count=num_questions) + f"\n\nText: {chunk}"
    system_instructions = """
Generate different types of questions about the given text following the prompt provided.
Each question must be on a new line. Do not include empty lines or blank questions.
"""
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
SELECT ai.ollama_generate(
'llama3.2',
%s,
system_prompt=>%s,
host=>%s
)->>'response';
""",(prompt, system_instructions, OLLAMA_HOST))
            generated_questions = [q.strip() for q in cur.fetchone()[0].split("\n") if q.strip()]
            print(f"Number of questions generated for {question_type}: {len(generated_questions)}")
    return generated_questions
```

以下是一些关键见解：

**提示设计很重要**: 测试数据集的质量很大程度上取决于提示和系统指令的直接性和描述性。关于所需输出的具体说明会导致生成问题LLM产生更准确的结果。**与PostgreSQL和pgai集成**: 此函数突出显示了通过利用pgai函数[ollama_generate](https://github.com/timescale/pgai/blob/main/docs/ollama.md?ref=timescale.ghost.io#generate)在PostgreSQL环境中使用Ollama模型的简易性。

这是一个例子：

从Paul Graham的**[如何创办一家创业公司？](https://paulgraham.com/start.html?ref=timescale.ghost.io)** (2005年3月)中选择的文本片段：

> *我担心我们规模多么小，多么默默无闻。但事实上，我们正在做完全正确的事情。一旦你做大了（用户或员工方面），就很难改变你的产品了。那一年实际上是改进我们软件的实验室。到年底，我们远远领先于竞争对手，他们根本没有机会赶上。而且由于所有黑客都花了许多时间与用户交谈，我们比任何人都更了解在线商务。*

从文本片段生成并用于测试的问题：

- 到年底他们领先于竞争对手了吗？
**(简短问题)**
- 作者在那一年（被称为“实验室”）的产品开发方法是如何使他们能够在软件创新方面获得比竞争对手显著的领先优势的？
**(长问题)**
- 创业公司的实验室阶段在什么时候结束，到那时他们领先竞争对手多远？
**(直接问题)**
- 是什么促使作者最初担心他们创业公司规模小且默默无闻？
**(隐含问题)**
- 创业公司的发展如何迫使他们适应和创新？
**(含糊不清的问题)**

## 模型评估
我们使用向量相似性搜索来评估每个嵌入模型检索正确父文本块的能力。目标是检查原始文本块是否出现在测试数据集每个问题的`top_K`最近匹配（检索窗口）中。以下是涉及的步骤：

**执行向量相似性搜索：**我们对每个模型和问题使用余弦相似度来检索`top_K`最近的嵌入。**评分：**如果原始文本块出现在`top_K`结果中，则记录分数1。否则，记录分数0。**统计结果：**我们汇总分数以计算整体准确率和按问题类型划分的准确率。按问题类型细分结果可以更深入地了解每个模型的优势所在，因为异常值有时会歪曲整体准确率。
选择检索窗口的大小通常是在精度和召回率之间取得平衡。较小的窗口可能会错过排名稍低的正确结果，而较大的窗口可能会歪曲整体准确率。我们选择10作为我们的`top_K`，因为它达到了平衡：它足够大，可以解释文本数据中的语义重叠，其中许多块可能具有相似的嵌入，但又足够小，可以保持有意义的评估结果。

# 结果
我们的评估数据集，[Paul Graham 的文章](https://huggingface.co/datasets/sgoel9/paul_graham_essays/viewer/default/train?ref=timescale.ghost.io)，提供了各种各样的简短、直接和上下文丰富的文本。数据被分成**6,257 个文本块，每个文本块 512 个字符，重叠 50 个字符**。我们仅使用开源 LLM（嵌入和生成模型）完成了此工作流程，并且是**免费的**——从生成到评估！

`bge-m3`实现了最高的整体检索准确率，达到**72%**，明显优于其他模型。`mxbai-embed-large`其次是**59.25%**，而`nomic-embed-text`排名最后，为**57.25%**。
虽然具有更高维度（**1,024**）的嵌入模型整体表现最好，但**`bge-m3`与其他模型在所有问题类型上的差距是显著的**。这种优越的性能可能是由于`bge-m3`的[多功能性](https://huggingface.co/BAAI/bge-m3?ref=timescale.ghost.io)，使其能够有效地处理各种嵌入类型，例如**密集型、多因素和稀疏检索**。这种多功能性能够更好地理解上下文，尤其是在处理冗长和隐含的问题时。

`bge-m3`在长问题上表现尤其出色，其**最高的检索准确率为 92.5%**，展示了其强大的上下文理解能力。同样，`mxbai-embed-large`在此类别中也表现良好，准确率为**82.5%**，进一步支持了**更高嵌入维度与改进的上下文能力之间的相关性**。有趣的是，`nomic-embed-text`也在长问题上取得了最佳性能，这表明嵌入模型与人类一样，更有效地处理详细和上下文丰富的查询。
另一方面，尽管`mxbai-embed-large`和`nomic-embed-text`的嵌入维度不同，但它们在所有问题类型上的性能相当。`nomic-embed-text`在简短和直接的问题上优于`mxbai-embed-large`，分别实现了**57.5%**和**63.75%**的检索准确率，**展示了其在处理较小的语义查询方面的优势**。

虽然`mxbai-embed-large`在上下文较重的问题（例如冗长和隐含的问题）上表现更好，但**准确率差距并不显著**。这表明，虽然嵌入维度有助于提高性能，但**在为您的 RAG 应用程序选择最佳嵌入模型时，它们并不是唯一决定因素**。

最后，所有三个模型在不清楚和含糊不清的问题上的表现都很差，最低准确率从`bge-m3`的 51.25% 到`nomic-embed-text`的 37.5%。

# 选择最佳开源嵌入模型
现在我们已经探讨了评估结果，那么如何为您的 RAG 应用程序选择最佳的开源嵌入模型呢？

幸运的是，**成本**在这里不是问题，因为所有这些模型都是**免费使用的**。相反，您的选择应该取决于以下关键考虑因素：

**您的 RAG 应用程序最常处理哪种类型的问题？**
您的查询是**简短直接的**，还是涉及**上下文丰富和详细的问题**？

这种区别有助于确定您需要的**嵌入维度**。例如，像`bge-m3`这样的模型由于其更高的嵌入维度而在处理上下文丰富查询方面表现出色，而像`nomic-embed-text`这样的模型更适合处理简短的语义查询。

**您愿意分配哪些资源？**
虽然**嵌入维度**对于性能至关重要，但您还必须考虑**模型大小**以及它是否适合您的可用资源（例如，存储、计算）。
例如，如果您存储空间受限但仍需要强大的性能，`mxbai-embed-large` 是一个不错的选择。它在大小和复杂度之间取得了平衡，由于其更高的维度，其性能优于`nomic-embed-text` 等较小的模型。

**您需要多快的嵌入生成速度？**
另一个需要考虑的因素是**模型生成嵌入的速度**。虽然嵌入生成通常是**异步**进行的，给用户留下即时处理的印象，但使用**本地**模型可能会带来挑战。本地机器上的计算能力有限可能会影响提供**快速且无缝的用户体验**。

例如：

**较大的模型**，例如`bge-m3` 和`mxbai-embed-large`，由于其更高的维度和复杂性，生成嵌入的时间更长。但是，它们会生成更丰富、更注重上下文的嵌入。**较小的模型**，例如`nomic-embed-text`，生成嵌入的速度要快得多，但代价是**降低了丰富性和深度**。
选择开源嵌入模型时，评估嵌入生成速度对于您的用例是否至关重要，并将其与所需的嵌入质量进行平衡至关重要。

# 结论

这篇博文探讨了一个评估工作流程，该流程表明，为您的 RAG 应用程序选择最佳的开源嵌入模型需要在性能、资源和查询类型之间取得平衡。

感谢**Ollama** 和**pgai Vectorizer**，实施此工作流程简单高效。Ollama 简化了模型访问和管理，而 pgai Vectorizer 自动化了 PostgreSQL 中的嵌入生成和存储，无需复杂的架构。

这些工具使评估和比较开源模型比以往任何时候都更加简单，使您能够找到最适合您需求的开源解决方案——**免费且完全控制您的数据**。

要使用您自己的数据和模型尝试此工作流程，请查看[pgai Vectorizer 的文档](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io)、[Ollama 的快速入门指南](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io) 和[pgai 的 GitHub 存储库](https://github.com/timescale/pgai?ref=timescale.ghost.io)！

## 推荐阅读

要了解更多信息，请查看以下关于开源 LLM 和使用 PostgreSQL 的 RAG 应用程序的博文：

*本文由 Hervé Ishimwe 撰写，并于 2024 年 12 月 19 日在此处发布在 Timescale 官方博客上。*