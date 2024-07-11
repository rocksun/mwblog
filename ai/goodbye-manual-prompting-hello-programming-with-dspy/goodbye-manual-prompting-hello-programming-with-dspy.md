
<!--
title: 告别人工提示，用DSPy编程
cover: https://cdn.thenewstack.io/media/2024/07/582bf2b8-prompt.jpg
-->

DSPy 框架旨在通过优先考虑声明式、系统化编程而不是手动编写提示来解决一致性和可靠性问题。

> 译自 [Goodbye Manual Prompting, Hello Programming With DSPy](https://thenewstack.io/goodbye-manual-prompting-hello-programming-with-dspy/)，作者 Usama Jamil。

使用 [大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 开发可扩展且优化的 AI 应用程序仍处于发展阶段。由于涉及大量手动工作，例如编写提示，因此基于 LLM 构建应用程序既复杂又耗时。

提示编写是任何 LLM 应用程序中最重要的部分，因为它可以帮助我们从模型中提取最佳结果。但是，[精心设计优化的提示](https://roadmap.sh/prompt-engineering) 需要开发人员严重依赖试错法，浪费大量时间才能获得预期结果。

传统的手动编写提示方法既耗时又容易出错。开发人员经常花费大量时间调整提示以获得所需的输出，并面临以下问题：

- **脆弱性**: 提示可能会因细微变化而失效或表现不一致。
- **手动调整**: 需要大量手动工作来完善提示。
- **处理不一致**: 针对类似任务的不同提示会导致结果不一致。

## 什么是 DSPy

[DSPy](https://github.com/stanfordnlp/dspy) (声明式自改进语言程序) 是由 [Omer Khattab](https://omarkhattab.com/) 及其团队在 [斯坦福 NLP 小组](https://nlp.stanford.edu/) 开发的框架。它旨在通过优先考虑编程而不是手动提示编写来解决提示编写的一致性和可靠性问题。它提供了一种更具声明性、系统性和编程性的方法来构建数据流水线，使开发人员能够创建高级工作流，而无需关注低级细节。

它允许您定义要实现的目标，而不是如何实现。因此，为了实现这一点，DSPy 取得了以下进展：

- **对提示的抽象**: DSPy 引入了签名的概念。签名旨在用类似模板的结构替换手动提示措辞。在此结构中，我们只需要定义任何给定任务的输入和输出。这将使我们的流水线更具弹性和更灵活地适应模型或数据的变化。
- **模块化构建块**: DSPy 提供了封装常见提示技术的模块（例如 [思维链](https://www.promptingguide.ai/techniques/cot.en#chain-of-thought-cot-prompting) 或 [ReAct](https://www.promptingguide.ai/techniques/react)）。这消除了为这些技术手动构建复杂提示的需要。
- **自动优化**: DSPy 支持内置优化器，也称为“提示器”，它会自动为您的特定任务和模型选择最佳提示。此功能消除了手动提示调整的需要，使流程更简单、更高效。
- **编译器驱动的适应**: DSPy 编译器会优化整个流水线，根据您的数据和验证逻辑调整提示或微调模型，确保即使组件发生变化，流水线也能保持有效。

## DSPy 程序的构建块

让我们探索构成 DSPy 程序基础的必要组件，并了解它们如何交互以创建强大且高效的自然语言处理 (NLP) 流水线。

### 签名

签名充当定义您希望 LLM 做什么的蓝图。您无需编写确切的提示，而是根据其输入和输出描述任务。

例如，用于总结文本的签名可能如下所示：`text -> summary`。这告诉 DSPy 您希望输入一些文本并接收简洁的摘要作为输出。更复杂的任务可能涉及多个输入，例如问答签名：`context, question -> answer`。签名很灵活，可以根据输入和输出字段的描述进行自定义。

```py
class GenerateAnswer(dspy.Signature):
   """Answer questions with short factoid answers."""

   context = dspy.InputField(desc="may contain relevant facts")
   question = dspy.InputField()
   answer = dspy.OutputField(desc="often between 1 and 5 words")
```

### 模块：LLM 行为的构建块

模块是预构建的组件，封装了特定的 LLM 行为或技术。它们是您用来组装 LLM 应用程序的构建块。例如，`ChainOfThought`模块鼓励 LLM 逐步思考，使其更擅长处理复杂的推理任务。`ReAct`模块允许您的 LLM 与外部工具（如计算器或数据库）交互。您可以将多个模块链接在一起以创建复杂的流水线。

```py
# Method 1: Pass the Class to the ChainOfThought module
chain_of_thought = ChainOfThought(TranslateText)
```

每个模块都接受一个签名，并使用 `defined`方法（如 `ChainOfThought`）根据定义的输入和输出构建必要的提示。此方法确保系统地生成提示，保持一致性并减少手动提示编写的需要。

这样，模块就会获取签名，应用其特定的行为或技术，并生成与任务要求一致的提示。签名和模块的这种集成允许构建复杂且灵活的 LLM 应用程序，而无需人工干预。

### 提示器（优化器）：提示的耳语者

提示器就像你 LLM 的教练。它们使用先进的技术来找到最适合你的特定任务和模型的提示。它们通过自动尝试不同的提示变体并根据你定义的指标评估其性能来做到这一点。例如，提示器可能会使用准确性之类的指标来进行问答任务，或者使用 [ROUGE 分数](https://aclanthology.org/W04-1013.pdf) 来进行文本摘要。

```py
from dspy.teleprompt import BootstrapFewShot

# Simple teleprompter example
teleprompter = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
```

### DSPy 编译器：主编排器

DSPy 编译器是操作背后的核心。它获取你的整个程序——包括你的签名、模块、训练数据和验证逻辑——并对其进行优化以实现峰值性能。编译器能够自动处理应用程序中的更改，使 DSPy 变得非常健壮且适应性强。

```py
from dspy.teleprompt import BootstrapFewShot
# Small training set with question and answer pairs
trainset = [dspy.Example(question="What is Albert Einstein best known for developing?",
                        answer="The theory of relativity").with_inputs('question'),
           dspy.Example(question="What famous equation did Albert Einstein's theory of relativity produce?",
                        answer="E = mc²").with_inputs('question'),
           dspy.Example(question="Which prestigious award did Albert Einstein receive in 1921?",
                        answer="The Nobel Prize in Physics").with_inputs('question'),
           dspy.Example(question="In which year did Albert Einstein move to the United States?",
                        answer="1933").with_inputs('question'),
           dspy.Example(question="What significant scientific work did Einstein publish in 1905, sometimes referred to as his annus mirabilis (miracle year)?",
                        answer="Four groundbreaking papers including theories on the photoelectric effect, Brownian motion, special theory of relativity, and mass-energy equivalence").with_inputs('question'),]

# Set up a basic teleprompter, which will compile our RAG program.
teleprompter = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
compiled_rag = teleprompter.compile(RAG(), trainset=trainset)
```

DSPy 编译器获取基本提示、训练示例和 DSPy 程序以生成经过优化且性能最佳的提示。此过程涉及在输入上模拟程序的各种版本，并引导每个模块的示例跟踪以优化你的任务的流水线。

这种自动优化过程消除了手动提示调整的需要，使 DSPy 能够适应变化，最终提供高效且高效的 NLP 流水线。

## 实用示例：使用 DSPy 和 MyScaleDB 构建 RAG 模型

现在我们已经介绍了 DSPy 的基础知识，让我们创建一个实际的应用程序。我们将构建一个问答 RAG 流水线，并使用 MyScaleDB 作为向量数据库。

### 从维基百科加载文档

我们首先从维基百科加载与“阿尔伯特·爱因斯坦”相关的文档。这是使用 `WikipediaLoader`
从 `langchain_community.document_loaders`
模块完成的。

```py
from langchain_community.document_loaders.wikipedia import WikipediaLoader
loader = WikipediaLoader(query="Albert Einstein")

# Load the documents
docs = loader.load()
```

### 将文档转换为纯文本

接下来，我们使用 `Html2TextTransformer`
将加载的文档转换为纯文本。

```py
from langchain_community.document_transformers import Html2TextTransformer
html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(docs)

# Get the cleaned text
cleaned_text = docs_transformed[0].page_content
text = ' '.join([page.page_content.replace('\\t', ' ') for page in docs_transformed])
```


### 将文本拆分为块

文本使用 `CharacterTextSplitter` 拆分为可管理的块。这有助于处理大型文档，并确保模型能够高效地处理它们。

```py
import os
from langchain_text_splitters import CharacterTextSplitter
# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
# Split the text into chunks
text = ' '.join([page.page_content.replace('\\\\t', ' ') for page in docs])
text_splitter = CharacterTextSplitter(
   separator="\\n",
   chunk_size=300,
   chunk_overlap=50,
   length_function=len,
   is_separator_regex=False,
)
texts = text_splitter.create_documents([text])
splits = [item.page_content for item in texts]
```


### 定义嵌入模型

我们使用 `transformers` 库来定义嵌入模型。我们将使用 `all-MiniLM-L6-v2` 模型将 [文本转换为向量嵌入](https://thenewstack.io/an-sql-vector-database-to-enhance-text-search-how-we-did-it/)。

```py
import torch
from transformers import AutoTokenizer, AutoModel
# Initialize the tokenizer and model for embeddings
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
def get_embeddings(texts: list) -> list:
       inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
       with torch.no_grad():
           outputs = model(**inputs)
       embeddings = outputs.last_hidden_state.mean(dim=1)
       return embeddings.numpy().tolist()
```

### 获取嵌入

我们使用上面的嵌入模型为文本块生成嵌入。

```ot
import pandas as pd
all_embeddings = []
for i in range(0, len(splits), 25):
   batch = splits[i:i+25]
   embeddings_batch = get_embeddings(batch)
   all_embeddings.extend(embeddings_batch)

# Create a DataFrame with the text chunks and their embeddings
df = pd.DataFrame({
   'page_content': splits,
   'embeddings': all_embeddings
})
```

### 连接到向量数据库
我们将使用 [MyScaleDB](https://myscale.com/) 作为向量数据库来开发此示例应用程序。你可以通过访问 MyScale [注册页面](https://console.myscale.com/passport/login?screenHint=signup) 在 MyScaleDB 上创建一个免费帐户。之后，你可以按照 [快速入门教程](https://myscale.com/docs/en/quickstart/) 启动一个新的集群并获取连接详细信息。

```py
import clickhouse_connect

client = clickhouse_connect.get_client(
   host='your-cloud-host',
   port=443,
   username='your-user-name',
   password='your-password'
)
```

将连接详细信息复制粘贴到你的 Python 笔记本中并运行代码块。它将连接到云上的 MyScaleDB 集群。

### 创建表并推送数据

让我们分解在 MyScaleDB 集群上创建表的流程。首先，我们将创建一个名为 RAG 的表。此表将具有三列：`id`、`page_content` 和 `embeddings`。id 列将保存每行的唯一 `id`，`page_content` 列将存储文本内容，`embeddings`
列将保存相应页面内容的嵌入。

```py
# Create the table
client.command("""
CREATE TABLE IF NOT EXISTS default.RAG (
   id Int64,
   page_content String,
   embeddings Array(Float32),
   CONSTRAINT check_data_length CHECK length(embeddings) = 384
) ENGINE = MergeTree()
   ORDER BY id
""")

# Insert data into the table
batch_size = 100
num_batches = (len(df) + batch_size - 1) // batch_size

for i in range(num_batches):
   batch_data = df[i * batch_size: (i + 1) * batch_size]
   client.insert('default.RAG', batch_data.values.tolist(), column_names=batch_data.columns.tolist())
   print(f"Batch {i+1}/{num_batches} inserted.")
```

创建表后，我们将数据以批处理的形式保存到新创建的 RAG 表中。

### 使用 MyScaleDB 配置 DSPy

我们连接 DSPy 和 MyScaleDB，并配置 DSPy 默认使用我们的语言和检索模型。

```py
import dspy
import openai
from dspy.retrieve.MyScaleRM import MyScaleRM

# Set OpenAI API key
openai.api_key = "your_openai_api_key"

# Configure LLM
lm = dspy.OpenAI(model="gpt-3.5-turbo")

# Configure retrieval model
rm = MyScaleRM(client=client,
              table="RAG",
              local_embed_model="sentence-transformers/all-MiniLM-L6-v2",
              vector_column="embeddings",
              metadata_columns=["page_content"],
              k=6)

# Configure DSPy to use the following language model and retrieval model by default
dspy.settings.configure(lm=lm, rm=rm)
```


注意：我们在此处使用的嵌入模型应与上面定义的模型相同。

### 定义签名

我们定义 `GenerateAnswer`
签名以指定问答任务的输入和输出。

```py
class GenerateAnswer(dspy.Signature):
   """Answer questions with short factoid answers."""

   context = dspy.InputField(desc="may contain relevant facts")
   question = dspy.InputField()
   answer = dspy.OutputField(desc="often between 1 and 5 words")
```

### 定义 RAG 模块

`RAG` 模块集成了检索和生成步骤。它检索相关段落并根据上下文生成答案。

```py
class RAG(dspy.Module):
   def __init__(self, num_passages=3):
       super().__init__()

       self.retrieve = dspy.Retrieve(k=num_passages)
       self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
  
   def forward(self, question):
       context = self.retrieve(question).passages
       prediction = self.generate_answer(context=context, question=question)
       return dspy.Prediction(context=context, answer=prediction.answer)
```

`forward` 方法接受问题作为输入，并使用检索器从集成数据库中查找相关块。然后将这些检索到的块传递给 `ChainOfThought`
模块以生成基础提示。

### 设置提示器(Teleprompters)

接下来，我们将使用 `BootstrapFewShot` 提示器/优化器来编译和优化我们的基本提示。

```py
from dspy.teleprompt import BootstrapFewShot

# Small training set with question and answer pairs
trainset = [dspy.Example(question="What is Albert Einstein best known for developing?",
                        answer="The theory of relativity").with_inputs('question'),
           dspy.Example(question="What famous equation did Albert Einstein's theory of relativity produce?",
                        answer="E = mc²").with_inputs('question'),
           dspy.Example(question="Which prestigious award did Albert Einstein receive in 1921?",
                        answer="The Nobel Prize in Physics").with_inputs('question'),
           dspy.Example(question="In which year did Albert Einstein move to the United States?",
                        answer="1933").with_inputs('question'),
           dspy.Example(question="What significant scientific work did Einstein publish in 1905, sometimes referred to as his annus mirabilis (miracle year)?",
                        answer="Four groundbreaking papers including theories on the photoelectric effect, Brownian motion, special theory of relativity, and mass-energy equivalence").with_inputs('question'),]

# Set up a basic teleprompter, which will compile our RAG program.
teleprompter = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)

# Compile the RAG pipeline with the teleprompter
compiled_rag = teleprompter.compile(RAG(), trainset=trainset)
```

此代码负责上面定义的 `RAG` 类，并使用示例以及优化器为我们的 LLM 生成最佳提示。

### 运行流水线

最后，我们运行编译后的 RAG 流水线，根据存储在 MyScaleDB 中的上下文来回答问题。

```py
# Retrieve relevant documents
retrieve_relevant_docs = dspy.Retrieve(k=5)
context = retrieve_relevant_docs("Who is Albert Einstein?").passages

# Make the query
pred = compiled_rag(question="Who was Albert Einstein?")

This will generate an output like this:
['Albert Einstein (1879-1955) was a renowned theoretical physicist of the 20th century,
best known for his theories of special relativity ........
.......
originality have made the word "Einstein" synonymous with "genius".']
```

## 结论

DSPy 框架通过用可编程接口替换硬编码提示，彻底改变了我们与 LLM 的交互方式，极大地简化了开发流程。这种从手动编写提示到更结构化、面向编程的方法的转变 [提高了 AI 应用程序的效率](https://thenewstack.io/enhance-your-rag-application-with-advanced-sql-vector-queries/)、一致性和可扩展性。通过抽象提示工程的复杂性，DSPy 允许开发人员专注于定义高级逻辑和工作流程，从而加速复杂 AI 驱动解决方案的部署。

MyScaleDB 是一款专门为 AI 应用程序开发的向量数据库，在提高此类系统的性能方面发挥着至关重要的作用。其先进的专有算法提高了 AI 应用程序的速度和准确性。此外，MyScaleDB 具有成本效益，为新用户提供高达 500 万个向量的免费存储空间。这使其成为希望使用强大的数据库解决方案而无需初始投资的初创公司和研究人员的理想选择。
