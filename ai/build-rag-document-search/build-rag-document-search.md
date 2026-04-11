<!--
title: 如何使用 RAG、ChromaDB 和 Memory 构建 AI 驱动的私有文档搜索应用
cover: https://cdn.thenewstack.io/media/2026/04/89248da0-willian-reis-fdotghsmhxa-unsplash-scaled.jpg
summary: 本文详细介绍了如何结合 LangChain、ChromaDB 和 RAG 技术，构建具备对话记忆功能的私有文档搜索应用。通过文档分块、向量存储及上下文检索，实现精准的知识提取与交互。
-->

本文详细介绍了如何结合 LangChain、ChromaDB 和 RAG 技术，构建具备对话记忆功能的私有文档搜索应用。通过文档分块、向量存储及上下文检索，实现精准的知识提取与交互。

> 译自：[How to build an AI-powered private document search app with RAG, ChromaDB, and memory](https://thenewstack.io/build-rag-document-search/)
> 
> 作者：Teri Eyenike

随着 AI 的进步，越来越多的工具被引入到生态系统中，使工程师和开发者能够实验并构建定制化的 AI 应用。但这并非易事。

事实上，AI 的每一个优势都伴随着一个劣势。例如，对于像 Chroma 这样的向量数据库，主要的挑战是高效的数据处理。而许多最新的 AI 应用都依赖向量嵌入作为 [LLM 的核心](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)。

向量数据库旨在存储和查询非结构化数据——即缺乏固定模式的输入，如文本、图像和音频。这与传统的 SQL 数据库有明显的不同，后者通常查询值符合特定标准的行，例如使用 “SELECT” 语句。

> “向量数据库旨在存储和查询非结构化数据——即缺乏固定模式的输入，如文本、图像和音频。”

本教程旨在帮助你将 LangChain 连接的 LLM 与你自己的数据源（在本例中为 PDF 文档）结合起来，同时使用 ChromaDB 作为向量数据库来充当记忆。这就是 RAG 进入视野的地方，它引入了在对话过程中存储和检索数据的能力，并添加了聊天记录，使你能够构建具有记忆功能的复杂应用。

以下是整个产品的流水线示意图：

![连接 PDF 文档到 LangChain LLM 并使用 ChromaDB 作为向量数据库的工作流图](https://cdn.thenewstack.io/media/2026/04/77eac6f8-3.png)

## 项目工作流步骤

现在，你已经对我们要构建的应用类型有了基本了解。本节将介绍实现步骤，包括：将数据加载到 LangChain 文档中；将其切分为块（chunks）；根据与问题嵌入的相似度对向量进行排序；最后，输入问题，将最相关的块插入到发送给 GPT 模型的消中，并返回 GPT 的回答。

让我们深入了解。

### 第 1 步：安装依赖

在你的 Notebook 中，运行这些 [Python 包](https://thenewstack.io/the-top-5-python-packages-and-what-they-do "Python packages")：

```python
pip install pypdf docx2txt openai langchain chromadb langchain-community langchain-openai "langchain-chroma>=0.1.2"
```

* `pypdf:` 负责拆分和转换 PDF 文件
* `docx2txt:` 从 docx 文件中提取文本
* `openai:` 提供对模型的访问
* `langchain:` 作为 LLM 的封装器
* `chromadb:` 用于存储和查询嵌入的开源向量数据库
* `langchain-community:` 将数据加载为标准的 LangChain 文档格式
* `langchain-openai:` 连接 OpenAI 和 LangChain 的包
* `"langchain-chroma>=0.1.2":` 用于访问 Chroma 向量存储

这些工具协同工作，共同创建一个由 LLM 驱动的问答应用。

### 第 2 步：加载你的密钥

```python
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
```

与每个 Python 项目一致，你应该将环境变量加载到 .env 文件中，当你决定在 GitHub 上共享项目时，不要将其提交到源码控制中。

### 第 3 步：加载文档

在这里，我们将使用 LangChain 文档并通过 `load_document` 函数加载 PDF 文件。这将使用 `pypdf` 库将文件转换为文档数组，其中每个文档包含页面内容以及使用 `loader.load()` 函数关联的页码元数据。

```python
def load_document(file): 
    import os
    name, extension = os.path.splitext(file)

    if extension == '.pdf':
        from langchain_community.document_loaders import PyPDFLoader
        print(f'Loading {file}')
        loader = PyPDFLoader(file)
    elif extension == '.docx':
        from langchain_community.document_loaders import Docx2txtLoader
        print(f'Loading {file}')
        loader = Docx2txtLoader(file)
    elif extension == '.txt':
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(file)
    else:
        print('Document format is not supported!')
        return None

    data = loader.load()
    return data
```

### 第 4 步：数据分块

```python
def chunk_data(data, chunk_size=256):

    from langchain.text_splitter import RecursiveCharacterTextSplitter
    
    overlap = int(chunk_size * 0.15)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)

    chunks = text_splitter.split_documents(data)

    return chunks
```

`chunk_data` 函数将使用 LangChain 的 `RecursiveCharacterTextSplitter` 处理将文档拆分为指定大小的文本块。通过这种方法，你可以通过索引访问页面内容的指定文本。

### 第 5 步：查询与响应

```python
def ask_and_get_answer(vector_store, q, k=3):
    from langchain_openai import ChatOpenAI
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)

    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': k})

    # 定义提示词模板以获得更好的控制
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({"input": q})
    return response
```

由于我们需要自然语言形式的答案，LLM 就派上用场了。这个特定的函数使用 GPT-3.5-turbo 模型生成答案，并从向量存储中查询文档。

### 第 6 步：使用 Chroma 作为向量数据库

```python
def create_embeddings_chroma(chunks, persist_directory='./chroma_db'):
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=1536)  

    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory) 

    return vector_store
```

这段代码实例化了一个来自 OpenAI 的嵌入模型。在此过程中，它使用提供的文本块和嵌入模型创建了一个向量存储，并将其配置为将数据保存到指定的目录 `chroma_db` 中。

```python
def load_embeddings_chroma(persist_directory='./chroma_db'):
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=1536) 
    
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings) 

    return vector_store
```

在这里，我们定义了一个函数，将持久化目录作为参数传递，从而将现有的嵌入从磁盘加载到向量存储对象中。接着，实例化创建时使用的同一个嵌入模型。返回的加载向量存储将使用提供的嵌入函数从指定目录加载 Chroma 向量存储。

### 第 7 步：运行代码

在编写了大量代码之后，是时候测试并运行代码了。

首先，将 PDF 文档加载到 LangChain 中，文件路径代表文件所在的目录：

```python
data = load_document('files/rag_powered_by_google_search.pdf') # 使用你拥有的任何文件

chunks = chunk_data(data, chunk_size=256)

vector_store = create_embeddings_chroma(chunks)
```

接下来，你应该观察到运行此代码会显示消息：“Loading files/rag_powered_by_google_search.pdf”——表示加载成功。

```python
db = load_embeddings_chroma() 

q = 'How many pairs of questions and answers had the StackOverflow dataset?'

answer = ask_and_get_answer(vector_store, q)
print(answer)
```

在这里，我们[从向量库中检索答案](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/)对象。

![从向量存储中检索到的输出图像](https://cdn.thenewstack.io/media/2026/04/e6a4303a-4-1024x614.png)

如果你问一个后续问题，很明显你不会从向量存储中获得准确的答案。这是因为缺乏聊天记录（记忆）。

```python
q = 'Multiply that number by 2.'
answer = ask_and_get_answer(vector_store, q)

print(answer['answer'])
```

此响应的结果应该是类似：“由于上下文中没有提供具体数字，因此无法将其乘以 2。”

### 第 8 步：为你的 RAG 应用添加聊天记录记忆

```python
from langchain_openai import ChatOpenAI
from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

retriever = vector_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k': 5}
)

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", qa_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(
    llm, qa_prompt
)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
```

对于 RAG 应用，一个基本要求是支持后续问题——包括那些引用过去聊天记录的问题。

这里的代码展示了一种构建对话式 AI 链的方法，该链作为存储对话记忆的实现，并在交互过程中使用 `ConversationBufferMemory` 类跟踪对话。

### 第 9 步：创建提问函数

```python
from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

query = "How many pairs of questions and answers had the StackOverflow dataset?"

def ask_question(query, chain):
    response = rag_chain.invoke({
        "input": query,
        "chat_history": chat_history
    })
    return response

result = ask_question(query, rag_chain)
print(result['answer'])

# 手动更新记忆
chat_history.append(HumanMessage(content=query))
chat_history.append(AIMessage(content=result["answer"]))
```

该函数接受第 8 步中的 “query” 和 “rag_chain” 变量作为参数来显示结果。

![第 8 步查询结果的图像](https://cdn.thenewstack.io/media/2026/04/e6800f28-5-1024x69.png)

现在，对于后续问题，在另一个单元格块中运行以下代码：

```python
query = 'Multiply the answer by 4.'

result = ask_question(query, rag_chain)

print(result['answer'])
```

响应应该给你一个 “32 million” 的数字，你可以继续传递不同的提示词来从结果中获得答案。

### 第 10 步：RAG 应用中的交互式问题循环

为了实现动态和交互式的工作流，运行这段代码：

```python
while True:
    query = input('Your question: ')
    if query.lower() in ['exit', 'quit', 'bye']:
        print('Bye bye!')
        break
    result = ask_question(query, rag_chain)
    print(result['answer'])
    print('-' * 100)
```

![第 10 步代码中一些示例问题的结果](https://cdn.thenewstack.io/media/2026/04/ac3e3d61-6-1024x238.png)

## 欢迎来到 AI 的 RAG 时代

[检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/)对于 AI 工程师来说不仅仅是一个华丽的词汇。它的深层实用性源于它是一种利用并将 LLM 与信息检索方法相结合的技术。

> “检索增强生成不仅仅是一个华丽的词汇…… 它的深层实用性源于它是一种利用并将 LLM 与信息检索方法相结合的技术。”

通过遵循上述步骤，开发者和工程师可以确保采用该系统将帮助人们从文档中检索重要信息。这还将使答案更加真实，因为它在不损害数据完整性的情况下读取并学习数据，避免了常见的偏见想法和推理问题。

在我们继续利用 AI 进行构建时，让我们拥抱 RAG。查看[此仓库](https://github.com/Terieyenike/langchain-rag)获取完整工作流。