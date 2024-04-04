# 如何使用 ChromaDB 和 Python 构建 RAG 驱动的 LLM 聊天应用程序

![如何使用 ChromaDB 和 Python 构建 RAG 驱动的 LLM 聊天应用程序的特色图片](https://cdn.thenewstack.io/media/2024/03/dfa91eb2-rag-llm-chat-app-python-1024x576.jpg)

生成式 AI 正以其创建上下文相关内容的能力彻底改变技术，开创了 AI 可能性的新时代。其核心是 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/)，它将信息检索与 [大型语言模型 (LLM)](https://www.cloudflare.com/en-gb/learning/ai/what-is-large-language-model/) 相结合，从外部文档中生成智能、明智的响应。

本教程解释了如何使用 [ChromaDB](https://www.trychroma.com/) 构建 RAG 驱动的 LLM 应用程序，ChromaDB 是一款以 AI 为本、开源的嵌入式数据库，以其高效处理大型数据集而闻名。我将指导你完成每一步，展示 RAG 在创建高级 LLM 应用程序中的实际适用性。

## 你需要什么

要开始构建你的 LLM 应用程序，你需要 [Python](https://thenewstack.io/python/)（可从 [Python 官方网站](https://www.python.org/downloads/) 下载）、OpenAI API 密钥（可在 [OpenAI 平台](https://platform.openai.com/signup) 上获得）以及对 Python 和 Web API 的基本了解。这些技术将帮助确保在遵循本教程和开发生成式 AI 驱动的聊天应用程序时获得顺畅的体验。

## 设置项目

下载完所需的应用程序和技术后，开始设置你的项目环境。

**1. 创建并导航到项目目录：**在你的终端中，创建一个新目录：

```
mkdir rag_lmm_application
```

将你的工作目录更改为项目文件夹：

```
cd rag_lmm_application
```

**2. 创建你的虚拟环境：**这是依赖项管理的关键步骤。你可以使用以下命令创建一个虚拟环境：

```
python -m venv venv
```

并激活它。

对于 Mac 或 Linux：

```
source venv/bin/activate
```

对于 Windows：

```
Venv\Scripts\activate
```

**3. 安装必需的包：**使用以下命令为你的项目安装必要的库：

```
pip install -r requirements.txt
```

确保所有必需的依赖项都在 requirements.txt 文件中。

完成这些步骤后，你的环境已准备就绪，你可以开始使用 ChromaDB 构建最先进的 RAG 聊天应用程序。

## 加载和处理文档

此 LLM 应用程序使用 [LangChain](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/) 加载器熟练地处理各种文档格式，包括 PDF、DOCX 和 TXT。这对于启用外部数据可访问性、确保高效的数据处理和维护后续阶段的统一数据准备至关重要。以下代码片段说明了该过程：

```python
from langchain import LangChain

# 创建 LangChain 加载器
loader = LangChain()

# 加载文档
documents = loader.load_documents("path/to/documents")
```

数据分块——将不同信息分组到更易于管理或更有意义的块中——简化了处理和嵌入，并实现了高效的上下文保留和信息检索。以下代码片段演示了这一重要过程：

```python
# 分块文档
chunks = loader.chunk_documents(documents)
```

## 使用 OpenAI 和 ChromaDB 创建嵌入

在此应用程序中，RAG 使用 [OpenAI](https://thenewstack.io/why-microsoft-has-to-save-openai/) 语言模型创建嵌入——文本的基本向量表示，以便高效地理解数据。这些嵌入对于 RAG 的检索至关重要，允许访问相关外部数据。它们有效地存储在 ChromaDB 中，可以快速检索信息，如下面的代码片段所示。此过程极大地增强了应用程序的 AI 能力。

```python
from chromadb import ChromaDB

# 创建 ChromaDB 客户端
client = ChromaDB()

# 创建嵌入
embeddings = client.create_embeddings(chunks)
```

## 使用 Streamlit 构建聊天界面

[Streamlit](https://streamlit.io/) 是一款应用程序，它可以在几分钟内将数据脚本转换为可共享的 Web 应用程序。此 RAG LLM 应用程序将用户输入链接到后端处理。通过 Streamlit 的初始化和布局设计，用户可以上传文档和管理数据。后端处理这些输入，并直接在 Streamlit 界面中返回响应，显示前端和后端操作的无缝集成。

以下代码显示了如何在 Streamlit 中创建文本输入字段和处理用户输入。

```python
import streamlit as st

# 创建文本输入字段
text_input = st.text_input("输入你的问题：")

# 处理用户输入
if text_input:
    # 调用后端处理函数
    response = process_input(text_input)

    # 在 Streamlit 界面中显示响应
    st.write(response)
```

完成此设置后，用户可以与 AI 应用程序无缝直观地交互。

## 检索答案并增强用户交互

此 RAG 聊天应用程序利用 [LangChain 的 RetrievalQA](https://python.langchain.com/docs/modules/data_connection/) 和 ChromaDB，从 ChromaDB 的嵌入数据中提取相关、准确的信息，高效地响应用户查询，展示了高级生成式 AI 能力。

以下代码片段演示了在 Streamlit 应用程序中实际实现此过程：

```python
from langchain.retrievalqa import RetrievalQA

# 创建 RetrievalQA 对象
retrieval_qa = RetrievalQA(client)

# 检索答案
answer = retrieval_qa.retrieve_answer(text_input)

# 在 Streamlit 界面中显示答案
st.write(answer)
```
**此代码集成了 Streamlit 中的用户输入和响应生成。它使用 ChromaDB 的矢量数据获取准确的答案，增强了聊天应用程序的交互性，并提供了信息丰富的 AI 对话。**

## 结论

本教程探讨了使用 OpenAI、ChromaDB 和 Streamlit 构建 LLM 应用程序的复杂性。它解释了如何设置环境、处理文档、创建和存储嵌入，以及构建用户友好的聊天界面，突出了 RAG 和 ChromaDB 在生成式 AI 中的强大组合。

此 [GitHub 存储库](https://github.com/sowole-aims/chat-with-documents-app) 涵盖了该过程。要运行该应用程序，请在终端中执行以下命令：

```
streamlit run ./chat_with_documents.py
```

您现在可以通过导航到 http://localhost:8501 来测试该应用程序。

我鼓励您尝试此应用程序，使其成为您自己的应用程序，并与他人分享您的经验！

*确定适合您业务的正确 GenAI 策略：解锁各种用例、必要的资源和战略考虑因素，以成功实施。下载 CIO 的生成式 AI 指南，帮助您的组织走向创新和积极的投资回报率。* [YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。