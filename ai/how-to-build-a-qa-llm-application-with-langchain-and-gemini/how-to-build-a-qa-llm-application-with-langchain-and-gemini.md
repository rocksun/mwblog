<!--
title:  LangChain和Gemini打造问答应用
cover: https://cdn.thenewstack.io/media/2024/03/9d8797e0-emily-morter-8xaa0f9yqne-unsplash-1024x683.jpg
-->

本文将指导您集成 LangChain 和 Google 的 Gemini LLM 模型,构建一个基于 PDF 文件的问答应用。

> 译自 [How to Build a Q&A LLM Application with LangChain and Gemini](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/)，作者 Janakiram MSV。

在本教程中，我们将探索 LangChain 编程框架（用于在应用程序中使用大型语言模型（LLM））与 Google 的 Gemini LLM 的集成，以构建基于 PDF 文件的问答应用程序。

在继续本教程之前，请确保您已从 [Google AI Studio](https://aistudio.google.com/app/) 获得 API 密钥。

## 第一步：初始化环境

创建 Python 虚拟环境并从 requirements.txt 文件中安装所需的模块。

```
python -m venv venv
source venv/bin/activate
```

使用以下内容创建 requirements.txt 文件：

```
pypdf2
chromadb
google.generativeai
langchain-google-genai
langchain
langchain_community
jupyter
```

```bash
pip install -r requirements.txt
```

设置环境变量，以便代码可以隐式访问 API 密钥。

```bash
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

启动 Jupyter Notebook，开始编写代码。

## 第二步：导入模块

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import Chroma
import os
```

## 第三步：初始化模型

此步骤加载 LLM 与负责将文本转换为低维向量的 Embeddings 模型。

```python
1  llm = ChatGoogleGenerativeAI(model="gemini-pro")
2  embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
```

## 第四步：加载并拆分 PDF 文件

您可以使用任何您选择的 PDF 文件。但在本教程中，我们将加载一家虚构公司的员工手册。

下面的代码加载 PDF 文件，并将其拆分为长度为 250 个字符的块，每个块之间重叠 50 个字符。

```python
1  loader = PyPDFLoader("handbook.pdf")
2   
3  text_splitter = CharacterTextSplitter(
4      separator=".",
5      chunk_size=250,
6      chunk_overlap=50,
7      length_function=len,
8      is_separator_regex=False,
9  )
10  
11  pages = loader.load_and_split(text_splitter)
```

## 第五步：初始化向量并配置检索器

在下一步中，我们将把每个文本块转换为嵌入向量，并将它们存储在 Chroma 向量数据库中，以便进行检索。参数 search_kwargs={"k": 5} 定义了从搜索中检索的前 5 个匹配项。

```python
1  vectordb=Chroma.from_documents(pages,embeddings)
2  retriever = vectordb.as_retriever(search_kwargs={"k": 5})
```

## 第六步：定义检索链

在 LangChain 中，每个组件都被组装在一起形成一个逻辑链。在这种情况下，我们有 prompt、LLM 和 retriever 作为关键组件。让我们从它们创建一个链。

```python
1  template = """
2  You are a helpful AI assistant.
3  Answer based on the context provided. 
4  context: {context}
5  input: {input}
6  answer:
7  """
8  prompt = PromptTemplate.from_template(template)
9  combine_docs_chain = create_stuff_documents_chain(llm, prompt)
10 retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
```

## 第七步：调用链

现在是时候测试一下这个拼图的各个部分是否连接正确了。我们将调用链并检查响应。

```python
1  response=retrieval_chain.invoke({"input":"How do I apply for personal leave?"})
2  print(response)
```

![](https://cdn.thenewstack.io/media/2024/03/268219af-langchain-gemini-1-1024x454.jpeg)

如我们所见，答案键中有来自链的预期响应。让我们将其打印出来。

```python
1  response["answer"]
```

![](https://cdn.thenewstack.io/media/2024/03/90e46175-langchain-gemini-2-1024x119.jpeg)

以下是完整的代码：

```python
### Install required modules and set the envvar for Gemini API Key
#pip install pypdf2
#pip install chromadb
#pip install google.generativeai
#pip install langchain-google-genai
#pip install langchain
#pip install langchain_community
#pip install jupyter

#export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"

#Import Python modules
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import Chroma

#Load the models
llm = ChatGoogleGenerativeAI(model="gemini-pro")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

#Load the PDF and create chunks
loader = PyPDFLoader("handbook.pdf")
text_splitter = CharacterTextSplitter(
    separator=".",
    chunk_size=250,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)
pages = loader.load_and_split(text_splitter)

#Turn the chunks into embeddings and store them in Chroma
vectordb=Chroma.from_documents(pages,embeddings)

#Configure Chroma as a retriever with top_k=5
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

#Create the retrieval chain
template = """
You are a helpful AI assistant.
Answer based on the context provided. 
context: {context}
input: {input}
answer:
"""
prompt = PromptTemplate.from_template(template)
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

#Invoke the retrieval chain
response=retrieval_chain.invoke({"input":"How do I apply for personal leave?"})

#Print the answer to the question
print(response["answer"])
```