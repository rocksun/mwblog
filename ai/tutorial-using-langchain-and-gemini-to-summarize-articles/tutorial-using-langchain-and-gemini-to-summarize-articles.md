
<!--
title: 使用LangChain和Gemini总结文章
cover: https://cdn.thenewstack.io/media/2024/03/878e4b6d-maarten-van-den-heuvel-8eznkvlqosk-unsplash.jpg
-->

我们演示如何结合 LangChain 和 Google 的 Gemini LLM 来总结互联网上的博客文章和文章。

> 译自 [Tutorial: Using LangChain and Gemini to Summarize Articles](https://thenewstack.io/tutorial-using-langchain-and-gemini-to-summarize-articles/)，作者 Janakiram MSV。

在本教程中，我们将了解如何结合使用 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)（一个用于在应用程序中使用大型语言模型 (LLM) 的编程框架）和 Google 的 [Gemini LLM](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/) 来总结互联网上的博客文章或文章。

在继续本教程之前，请确保你已从 Google AI Studio 获取了 API 密钥。

此应用程序旨在总结基于网络的文章，提供其内容的简洁概述。这对于快速了解长篇文章的要点非常有用，而无需阅读全文。

## 步骤 1：初始化环境

创建一个 Python 虚拟环境，并从 requirements.txt 文件中安装所需的模块。

```bash
python -m venv venv
source venv/bin/activate
```

使用以下内容创建 requirements.txt 文件：

```
google.generativeai
langchain-google-genai
langchain
langchain_community
jupyter
```

```bash
pip install -r requirements.txt
```

设置一个环境变量，以便从代码中隐式访问 API 密钥。

```
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

启动 Jupyter Notebook 并开始编写代码。

## 步骤 2：导入模块

首先导入必要的 Python 模块。这些导入包括来自 LangChain 和 Google Generative AI 的类和函数，它们对于构建我们的应用程序至关重要。在继续之前，请确保在 Python 环境中安装了这些库。

```
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
```

## 步骤 3：加载博客

从基于网络的文章中加载内容。下面代码段中提供的 URL 只是一个示例；你可以随意将其替换为要总结的任何文章 URL。获取内容并将其存储起来以供进一步处理。

```
loader = WebBaseLoader("https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/")
docs = loader.load()
```

## 步骤 4：定义总结链

在此关键步骤中，我们将定义摘要模板并配置 LangChain 模型以生成摘要。该模板指导模型如何构建其输出，重点是创建输入文本的简洁摘要。

```python
template = "Write a concise summary of the following:\n\"{text}\"\nCONCISE SUMMARY:"
prompt = PromptTemplate.from_template(template)
llm_chain = LLMChain(llm=llm, prompt=prompt)
stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text"
```

## 步骤 5：调用链

最后一步是调用链，它触发对已加载文档的摘要处理。输出是模型尝试总结文章，为你提供其内容的浓缩版本。

```python
response=stuff_chain.invoke(docs)
print(response["output_text"])
```

## 更多关于 LangChain 和 LLM 的信息

[问题解答 (Q&A) 用例](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/)（如前一个教程中所示）和摘要用例（如上所述）利用了 LangChain 和 Gemini 的强大功能，但服务于不同的目的并采用不同的方法。

问答应用程序专注于从给定文本（例如 PDF 文档）中提取特定答案，要求系统理解上下文并检索准确的信息以回答查询。此过程涉及加载和将文档拆分为可管理的块，将这些块转换为嵌入，并使用检索机制查找最相关的文本部分来回答提出的问题。

另一方面，摘要用例旨在将基于网络的长篇文章浓缩成简洁的摘要。此应用程序强调理解文章的总体主题和要点，需要一个摘要链来指导模型生成内容的简要概述。与问答用例不同，摘要涉及直接加载网络内容、应用摘要模板并生成文章的浓缩版本——突出其核心信息，而无需深入了解具体内容。

这两个应用程序展示了 LangChain 在处理自然语言处理任务方面的多功能性，但它们各自满足不同的需求。一个专注于在文档中精确定位特定信息，而另一个旨在提供冗长文章的快速、易于消化的摘要。

您可以在下面找到摘要的完整代码：


```python
### Install required modules and set the envvar for Gemini API Key
#pip install google.generativeai
#pip install langchain-google-genai
#pip install langchain
#pip install langchain_community
#pip install jupyter

#export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"

#Import Modules
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

#Initialize Model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

#Load the blog
loader = WebBaseLoader("https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/")
docs = loader.load()

#Define the Summarize Chain
template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""

prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(llm=llm, prompt=prompt)
stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

#Invoke Chain
response=stuff_chain.invoke(docs)
print(response["output_text"])
```