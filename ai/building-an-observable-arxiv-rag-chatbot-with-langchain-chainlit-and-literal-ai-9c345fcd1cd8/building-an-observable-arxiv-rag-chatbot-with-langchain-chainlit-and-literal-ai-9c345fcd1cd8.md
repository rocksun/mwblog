
<!--
title: 使用LangChain、Chainlit和Literal AI构建一个可观测的arXiv RAG聊天机器人
cover: https://miro.medium.com/v2/resize:fit:1024/1*GUoz9w5z8FLzXHmQUarXyg.png
-->

使用 RAG、LangChain、Chainlit 协作应用程序和 Literal AI 可观测性构建语义论文引擎的教程。

> 译自 [Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI](https://towardsdatascience.com/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8)，作者 Tahreem Rasul。

在本指南中，我将演示如何使用检索增强生成 (RAG) 构建语义研究论文引擎。我将利用
[LangChain](https://www.langchain.com) 作为构建语义引擎的主要框架，以及 [OpenAI](https://openai.com) 的语言模型和 [Chroma DB](https://www.trychroma.com) 的向量数据库。对于构建协作嵌入式 Web 应用程序，我将使用 [Chainlit](https://docs.chainlit.io/get-started/overview) 的协作功能，并整合 [Literal AI](https://literalai.com) 的可观测性功能。此工具可以通过更轻松地查找相关论文来促进学术研究。用户还能够通过询问有关推荐论文的问题来直接与内容进行交互。最后，我们将在应用程序中集成可观测性功能，以跟踪和调试对 LLM 的调用。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*GUoz9w5z8FLzXHmQUarXyg.png)

*Copilot嵌入式语义研究论文应用程序的应用程序架构。作者提供的插图。*

以下是本教程中我们将涵盖的所有内容的概述：

- 使用 OpenAI、LangChain 和 Chroma DB 开发 RAG 管道，以处理和检索 arXiv API 中最相关的 PDF 文档。
- 开发一个带有协作功能的 Chainlit 应用程序，用于在线论文检索。
- 使用 Literal AI 增强应用程序的 LLM 可观测性功能。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*jtr_Sbj0Dt7nIBV2JAesuA.gif)

*Copilot嵌入式语义研究论文应用程序实战。作者提供。*

可以在[此 GitHub 仓库](https://github.com/tahreemrasul/semantic_research_engine) 中找到本教程的代码。

## 环境设置

创建一个新的 conda 环境：

```
conda create -n semantic_research_engine python=3.10
```

激活环境：

```
conda activate semantic_research_engine
```

通过运行以下命令在已激活的环境中安装所有必需的依赖项：

```
pip install -r requirements.txt
```

## RAG 管道创建

检索增强生成 (RAG) 是一种流行的技术，它允许您使用自己的数据构建自定义会话式 AI 应用程序。RAG 的原理非常简单：我们将文本数据转换为向量嵌入，并将这些嵌入插入到向量数据库中。然后将此数据库链接到大型语言模型 (LLM)。我们正在限制我们的 LLM 从我们自己的数据库中获取信息，而不是依赖于先验知识来回答用户查询。在接下来的几个步骤中，我将详细介绍如何为我们的语义研究论文引擎执行此操作。我们将创建一个名为 rag_test.py 的测试脚本，以了解和构建 RAG 管道的组件。在构建我们的协作集成 Chainlit 应用程序时，将重复使用这些组件。

### 步骤 1

通过注册一个帐户来保护 OpenAI API 密钥。完成后，在项目目录中创建一个 .env 文件，并按如下方式添加您的 OpenAI API 密钥：

```
OPENAI_API_KEY="your_openai_api_key"
```

此 .env 将容纳我们项目的所有 API 密钥。

### 步骤 2：导入

在此步骤中，我们将创建一个数据库来存储给定用户查询的研究论文。为此，我们首先需要从 arXiv API 中检索与查询相关的论文列表。我们将使用 LangChain 中的 ArxivLoader() 包，因为它抽象了 API 交互，并检索论文以供进一步处理。我们可以将这些论文分成更小的块，以确保以后进行高效处理和相关信息检索。为此，我们将使用 LangChain 中的 RecursiveTextSplitter()，因为它确保在拆分文档时保留信息的语义。接下来，我们将使用 [HuggingFace](https://python.langchain.com/docs/integrations/platforms/huggingface/#embedding-models) 中的 sentence-transformers 嵌入为这些块创建嵌入。最后，我们将把这些拆分文档嵌入导入 Chroma DB 数据库中以供进一步查询。

```python
# rag_test.py 
from langchain_community.document_loaders import ArxivLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

query = "lightweight transformer for language tasks"
arxiv_docs = ArxivLoader(query=query, load_max_docs=3).load()
pdf_data = []
for doc in arxiv_docs:
    text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=100)
    texts = text_splitter.create_documents([doc.page_content])
    pdf_data.append(texts)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-l6-v2")
db = Chroma.from_documents(pdf_data[0], embeddings)
```

## 步骤 3：检索和生成

在为特定主题创建数据库之后，我们可以使用此数据库作为检索器，根据提供的上下文来回答用户问题。LangChain 为检索提供了几个不同的链，最简单的就是我们将在本教程中使用的 RetrievalQA 链。我们将使用 from_chain_type() 方法对其进行设置，指定模型和检索器。对于将文档集成到 LLM 中，我们将使用 stuff 链类型，因为它会将所有文档填充到一个提示中。

```python
# rag_test.py
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, 
                                 chain_type="stuff", 
                                 retriever=db.as_retriever())

question = "how many and which benchmark datasets and tasks were 
            compared for light weight transformer?"
result = qa({"query": question})
```

Now that we have covered the online retrieval from the arXiv API and the ingestion and retrieval steps of the RAG pipeline, we are ready to develop a web application for the semantic search engine.

## Understanding Literal AI

[Literal AI](https://literalai.com) is an observability, evaluation, and analytics platform for building production-grade LLM applications. Some of the key features that Literal AI provides include:

- **Observability**: Ability to monitor LLM applications, including conversations, intermediate steps, prompts, etc.
- **Datasets**: Allows for the creation of datasets mixing production data and hand-written examples.
- **Online Evaluation**: Ability to evaluate threads and their performance in production using different evaluators.
- **Prompt Playground**: Allows for iteration, versioning, and prompt deployment.

We will use the observability and prompt iteration features to evaluate and debug the calls made using our semantic search paper application.

## Using Literal AI's Prompt Playground

When creating conversational AI applications, developers need to iterate over multiple versions of prompts to get the one that produces the best results. Prompt engineering plays a crucial role in most LLM tasks, as small modifications can significantly change the response of the language model. Literal AI's Prompt Playground can be used to simplify this process. After selecting the model provider, you can enter the initial prompt template, add any additional information, and iterate to optimize the prompt to find the most suitable one. In the next few steps, we will use this playground to find the best prompt for our application.

### Step 1

Create an API key by navigating to the [Literal AI Dashboard](https://cloud.getliteral.ai/). Sign up for an account, navigate to the **Projects** page, and create a new project. Each project has its unique API key. You will find your API key in the **Settings** tab, under the **API Keys** section. Add it to your `.env` file:

```
LITERAL_API_KEY="your_literal_api_key"
```

### Step 2

In the left sidebar, click on **Prompts**, then navigate to **New Prompt**. This should open a new prompt creation session.

Once in the playground, in the left sidebar, add a new **System** message in the **Template** section. Anything in curly braces will be added to the **Variables** and treated as input in the prompt:

```
You are a helpful assistant. Answer the user's {{question}} using the provided {{context}}. Do not use any prior knowledge.

Answer:
```

In the right sidebar, you can provide your OpenAI API key. Select parameters such as **Model**, **Temperature**, and **Max Completion Length** to use with the prompt.

For the prompt version you are satisfied with, click **Save**. You will be prompted to enter a name for the prompt and an optional description. We can add this version to our code. In a new script called `search_engine.py`, add the following code:

```python
#search_engine.py
from literalai import LiteralClient
from dotenv import load_dotenv
load_dotenv()
client = LiteralClient()
# This will fetch the champion version, you can also pass a specific version
prompt = client.api.get_prompt(name="test_prompt")
prompt = prompt.to_langchain_chat_prompt_template()
prompt.input_variables = ["context", "question"]
```

Literal AI allows you to save different runs of a prompt and has versioning capabilities. You can also see how each version differs from the previous one. By default, the champion version will be fetched. If you want to change a version to be the champion, you can select it in the playground and click **Promote**.

After adding the above code, we will be able to see the generations for a specific prompt in the Literal AI dashboard (more on this later).

## Understanding Chainlit's Co-pilot

[Chainlit](https://github.com/Chainlit/chainlit) is an open-source Python package designed to build production-oriented conversational AI applications. It provides decorators for multiple events (chat start, user message, session resume, session stop, etc.). You can check out my article below for a more comprehensive explanation:
## 使用 Chainlit 和 LangChain 构建聊天机器人应用程序

### 在本文中，我们将使用 Chainlit（一个框架）为我们的自定义聊天机器人 Scoopsie 开发一个应用程序界面…

[medium.com](https://medium.com/)

具体来说，在本教程中，我们将重点介绍使用 Chainlit 为我们的 RAG 应用程序构建一个 [软件副驾驶](https://docs.chainlit.io/deployment/copilot)。Chainlit 副驾驶在应用程序中提供上下文指导和自动用户操作。

## 构建副驾驶

在应用程序网站中嵌入副驾驶出于多种原因很有用。我们将为我们的语义研究论文引擎构建一个简单的 Web 界面，并在其中集成一个副驾驶。此副驾驶将具有几个不同的功能，但以下是其中最突出的功能：

- 它将嵌入到我们网站的 HTML 文件中。
- 副驾驶将能够代表用户执行操作。假设用户要求提供特定主题的在线研究论文。这些论文可以在模态中显示，我们可以配置我们的副驾驶自动执行此操作，而无需用户输入。

在接下来的几个步骤中，我将详细介绍如何使用 Chainlit 为我们的语义研究引擎创建软件副驾驶。

## 步骤 1

第一步涉及为我们的 chainlit 应用程序编写逻辑。我们将为我们的用例使用两个 chainlit 装饰器函数：@cl.on_chat_start 和 @cl.on_message。我们将从在线搜索和 RAG 管道向这些函数添加逻辑。需要记住以下几点：

- @cl.on_chat_start 包含在新用户会话开始时需要执行的所有代码。
- @cl.on_message 包含在用户发送新消息时需要执行的所有代码。

我们将从接收研究主题到创建数据库和在 @cl.on_chat_start 装饰器中导入文档的整个过程封装起来。在 search_engine.py 脚本中，导入所有必需的模块和库：

```python
# search_engine.py
import chainlit as cl
from langchain_community.document_loaders import ArxivLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
```

现在让我们添加 @cl.on_chat_start 装饰器的代码。我们将使此函数异步，以确保多个任务可以同时运行。

```python
# search_engine.py
# 续
@cl.on_chat_start
async def retrieve_docs():
    # 查询部分
    arxiv_query = None
    # 等待用户发送主题
    while arxiv_query is None:
        arxiv_query = await cl.AskUserMessage(
            content="请输入一个主题以开始！", timeout=15).send()
    query = arxiv_query['output']
    # ARXIV 文档部分
    arxiv_docs = ArxivLoader(query=arxiv_query, load_max_docs=3).load()
    # 准备 arXiv 结果以供显示
    arxiv_papers = [f"Published: {doc.metadata['Published']} \n "
                    f"Title: {doc.metadata['Title']} \n "
                    f"Authors: {doc.metadata['Authors']} \n "
                    f"Summary: {doc.metadata['Summary'][:50]}... \n---\n"
                    for doc in arxiv_docs]
    await cl.Message(content=f"{arxiv_papers}").send()
    await cl.Message(content=f"Downloading and chunking articles for {query} "
                    f"This operation can take a while!").send()
    # 数据库部分
    pdf_data = []
    for doc in arxiv_docs:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.create_documents([doc.page_content])
        pdf_data.append(texts)
    llm = ChatOpenAI(model='gpt-3.5-turbo',
                    temperature=0)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-l6-v2")
    db = Chroma.from_documents(pdf_data[0], embeddings)
    # 链部分
    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=db.as_retriever(),
                                        chain_type_kwargs={
                                            "verbose": True,
                                            "prompt": prompt
                                        }
                                        )
    # 让用户知道管道已准备就绪
    await cl.Message(content=f"Database creation for `{query}` complete. "
                    f"You can now ask questions!").send()
    cl.user_session.set("chain", chain)
    cl.user_session.set("db", db)
```

让我们浏览一下我们在此函数中包装的代码：

**提示用户查询：**我们首先让用户发送研究主题。此函数在用户提交主题之前不会继续执行。

**在线搜索：**我们使用 LangChain 的 arXiv 搜索包装器检索相关论文，并以可读格式显示每个条目中的相关字段。

**导入：**接下来，我们将文章分成块并创建嵌入以进行进一步处理。分块确保高效处理大型论文。之后，从处理过的文档块和嵌入中创建 Chroma 数据库。

**检索：**最后，我们设置一个 RetrievalQA 链，将 LLM 和新创建的数据库集成作为一个检索器。我们还提供了我们在 Literal AI 游乐场中创建的提示。

**存储变量：**我们使用 cl.user_session.set 功能存储 chain 和 db 中的变量，以便以后重复使用。
**用户消息：**我们在整个函数中使用 Chainlit 的 `cl.Message` 功能与用户交互。

现在让我们定义我们的 `@cl.on_message` 函数，并添加 RAG 管道的生成部分。用户应该能够从摄取的论文中提问，应用程序应该提供相关答案。

```python
@cl.on_message
async def retrieve_docs(message: cl.Message):
    question = message.content
    chain = cl.user_session.get("chain")
    db = cl.user_session.get("db")
    # 为每次调用创建一个新的回调处理程序实例
    cb = client.langchain_callback()
    variables = {"context": db.as_retriever(search_kwargs={"k": 1}),
                 "query": question}
    database_results = await chain.acall(variables,
                                        callbacks=[cb])
    results = [f"Question: {question} "
               f"\n Answer: {database_results['result']}"]
    await cl.Message(results).send()
```

以下是上述函数中代码的细分：

**链和数据库检索：**我们首先从用户会话中检索先前存储的链和数据库。

**LangChain 回调集成：**为了确保我们可以跟踪提示以及使用特定提示版本的所有生成，我们需要在调用链时从 Literal AI 添加 LangChain 回调处理程序。我们使用 `LiteralClient` 实例的 `langchain_callback()` 方法创建回调处理程序。此回调将自动将所有 LangChain 交互记录到 Literal AI。

**生成：**我们定义变量：数据库作为检索的上下文，用户的疑问作为查询，还指定检索最高结果（`k: 1`）。最后，我们使用提供的变量和回调调用链。

## 步骤 2

第二步涉及将副驾驶嵌入到我们的应用程序网站中。我们将创建一个简单的网站进行演示。创建一个 `index.html` 文件，并向其中添加以下代码：

```html
<!DOCTYPE html>
<html>
<head>
<title>语义搜索引擎</title>
</head>
<body>
<!-- ... -->
<script src="http://localhost:8000/copilot/index.js"></script>
<script>
window.mountChainlitWidget({
    chainlitServer: "http://localhost:8000",
});
</script>
</body>
</html>
```

在上面的代码中，我们通过指向托管我们应用程序的 Chainlit 服务器的位置，将副驾驶嵌入到我们的网站中。 `window.mountChainlitWidget` 在您网站的右下角添加了一个浮动按钮。单击它将打开副驾驶。

为了确保我们的副驾驶正常工作，我们需要首先运行我们的 Chainlit 应用程序。导航到您的项目目录并运行：

```
chainlit run search_engine.py -w
```

上面的代码在 `localhost:8000` 上运行应用程序。接下来，我们需要托管我们的应用程序网站。打开 `index.html` 文件，您会发现该脚本不起作用。相反，我们需要创建一个 HTTPS 测试服务器。您可以通过不同的方式来实现，但一种直接的方法是使用 `npx`。

`npx` 包含在 `npm（Node 包管理器）` 中，它随 Node.js 一起提供。要获取 `npx`，您只需 [在您的系统上安装 Node.js](https://nodejs.org/)。导航到您的目录并运行：

```
npx http-server
```

运行上面的命令将在 `https://localhost:8080` 上启动一个服务器。导航到该地址，您将能够看到一个带有嵌入式副驾驶的简单 Web 界面。

由于我们将使用 `@cl.on_chat_start` 包装函数来欢迎用户，因此我们可以将 `show_readme_as_default` 设置为 `false` 在我们的 Chainlit 配置中，以避免闪烁。您可以在项目目录中的 `.chainlit/config.toml` 中找到您的配置文件。

## 步骤 3

要仅在副驾驶中执行代码，我们可以添加以下内容：

```python
@cl.on_message
async def retrieve_docs(message: cl.Message):
    if cl.context.session.client_type == "copilot":
        # 仅在副驾驶中执行的代码
```

此代码块中的任何代码仅在您从副驾驶中与您的应用程序交互时执行。例如，如果您在托管在 `https://localhost:8000` 的 Chainlit 应用程序界面处运行查询，则上述 if 代码块中的代码将不会执行，因为它期望客户端类型为副驾驶。这是一个有用的功能，您可以使用它来区分直接在 Chainlit 应用程序中执行的操作和通过副驾驶界面启动的操作。通过这样做，您可以根据请求的上下文定制应用程序的行为，从而实现更动态、更响应的用户体验。

## 步骤 4

副驾驶可以在您的网站上调用函数。这对于代表用户执行操作（例如打开模态、创建新文档等）非常有用。我们将修改我们的 Chainlit 装饰器函数，以包括两个新的副驾驶函数。我们需要在
### Corrected Markdown

**index.html File**

In the `index.html` file, we need to handle how the frontend should respond when a Copilot function in the Chainlit backend application is invoked. The specific response will vary depending on the application. For our semantic research paper engine, we will generate a pop-up notification in the frontend whenever relevant papers or database answers need to be displayed based on the user's query.

We will create two Copilot functions in our application:

- `showArxivResults`: This function will be responsible for displaying online results fetched by the `arxivAPI` based on the user's query.
- `showDatabaseResults`: This function will be responsible for displaying results fetched from our ingested database based on the user's question.

First, let's set up the backend logic in the `search_engine.py` script and modify the `@cl.on_chat_start` function:

```python
@cl.on_chat_start
async def retrieve_docs():
    if cl.context.session.client_type == "copilot":
        # Same code as before
        # Trigger pop-up for arXiv results
        fn_arxiv = cl.CopilotFunction(name="showArxivResults",
                                      args={"results": "\n".join(arxiv_papers)})
        await fn_arxiv.acall()
        # Same code as before
```

In the above code, we define a Copilot function named `showArxivResults` and call it asynchronously. This function is intended to display a formatted list of arXiv papers directly in the Copilot interface. The function signature is straightforward: we specify the name of the function and the arguments it will send back. We will use this information in the `index.html` file to create the pop-up.

Next, we need to modify our `@cl.on_message` function with a second Copilot function that will be executed when the user asks a question based on the ingested papers:

```python
@cl.on_message
async def retrieve_docs(message: cl.Message):
    if cl.context.session.client_type == "copilot":
        # Same code as before
        # Trigger pop-up for database results
        fn_db = cl.CopilotFunction(name="showDatabaseResults",
                                   args={"results": "\n".join(results)})
        await fn_db.acall()
        # Same code as before
```

In the above code, we define a second Copilot function named `showDatabaseResults` to be called asynchronously. This function is responsible for displaying results retrieved from the database in the Copilot interface. The function signature specifies the name of the function and the arguments it will send back.

## Step 5

We will now edit the `index.html` file to include the following changes:

- Add the two Copilot functions.
- Specify what should happen on our website when either of the two Copilot functions is triggered. We will create a pop-up to display the query results from the application's backend.
- Add simple styling for the pop-up.

First, we need to add event listeners for the Copilot functions. In the `<script>` tag of the `index.html` file, add the following code:

```html
<script>
// Previous code
window.addEventListener("chainlit-call-fn", (e) => {
  const { name, args, callback } = e.detail;
  if (name === "showArxivResults") {
    document.getElementById("arxiv-result-text").innerHTML =
      args.results.replace(/\n/g, "<br>");
    document.getElementById("popup").style.display = "flex";
    if (callback) callback();
  } else if (name === "showDatabaseResults") {
    document.getElementById("database-results-text").innerHTML =
      args.results.replace(/\n/g, "<br>");
    document.getElementById("popup").style.display = "flex";
    if (callback) callback();
  }
});
</script>
```

Here's a breakdown of the above code:

- We include functions to show (showPopup()) and hide (hidePopup()) the pop-up modal.
- We register an event listener for the `chainlit-call-fn` event, which is triggered when a Copilot function (either `showArxivResults` or `showDatabaseResults`) is invoked.
- Upon detecting the event, the listener checks the name of the Copilot function that was invoked. Based on the function name, it updates the content in the relevant section of the pop-up using the results provided by the function. It replaces newlines (\n) with HTML line breaks (<br>) for proper formatting of text for HTML display.
- After updating the content, the pop-up modal is displayed (display: "flex"), allowing the user to view the results. The modal can be hidden using the close button, which calls the hidePopup() function.

Next, we need to define the pop-up modal that we specified above. We can do this by adding the following code to the `<body>` tag of the `index.html` script:

```html
<div id="popup" class="popup">
  <span class="close-btn" onclick="hidePopup()">×</span>
  <div class="arxiv-results-wrapper">
    <h1>Arxiv Results</h1>
    <p id="arxiv-result-text">Online results will be displayed here.</p>
  </div>
  <div class="database-results-wrapper">
    <h1>Database Results</h1>
    <p id="database-results-text">Database results will be displayed here.</p>
  </div>
</div>
```

We also add some styling for the pop-up. Edit the `<head>` tag of the `index.html` file:

```html
<style>
* {
  box-sizing: border-box;
}
body {
  font-family: sans-serif;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 24px;
  cursor: pointer;
}
.popup {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  max-width: 500px;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  z-index: 999;
}
.arxiv-results-wrapper,
.database-results-wrapper {
  margin-top: 20px;
}
</style>
```
### 启动应用程序

现在，我们已将 Copilot 逻辑添加到 Chainlit 应用程序中，我们可以同时运行应用程序和网站。为了让 Copilot 正常工作，我们的应用程序必须已经运行。在项目目录中打开一个终端，并运行以下命令以启动 Chainlit 服务器：

```
chainlit run search.py -h
```

在新的终端中，使用以下命令启动网站：

```
npx http-server
```

# 使用 Literal AI 实现 LLM 可观测性

将可观测性功能集成到生产级应用程序中（例如我们的 Copilot 运行的语义研究引擎）通常是必需的，以确保应用程序在生产环境中的可靠性。我们将使用 Literal AI 框架来实现此目的。

对于任何 Chainlit 应用程序，Literal AI 都会自动开始监视应用程序并将数据发送到 Literal AI 平台。我们在 `search_engine.py` 脚本中创建提示时已经启动了 Literal AI 客户端。现在，每次用户与我们的应用程序交互时，我们都会在 Literal AI 仪表板中看到日志。

# 仪表板

导航到 [Literal AI 仪表板](https://cloud.getliteral.ai/projects/)，从左侧面板中选择项目，然后单击 **可观测性**。您将看到以下功能的日志。

## 线程

线程表示助手和用户之间的会话。您应该能够看到用户在应用程序中进行的所有对话。

展开特定对话将提供关键详细信息，例如每个步骤花费的时间、用户消息的详细信息以及详细说明所有步骤的基于树的视图。您还可以将对话添加到数据集。

## 运行

运行是代理或链采取的一系列步骤。这提供了每次执行链或代理时采取的所有步骤的详细信息。使用此选项卡，我们可以获得每个用户查询的输入和输出。

您可以展开运行，这将提供更多详细信息。同样，您可以将此信息添加到数据集。

## 生成

生成包含发送到 LLM 的输入及其完成。这提供了关键详细信息，包括用于完成的模型、令牌计数以及请求完成的用户（如果您配置了多个用户会话）。

# 在 Literal AI 中评估提示

自我们添加 LangChain 集成以来，我们可以针对应用程序代码中创建和使用的每个提示跟踪生成和线程。因此，每次为用户查询调用链时，都会在 Literal AI 仪表板中针对它添加日志。这有助于了解哪些提示导致了特定生成，并比较不同版本的性能。

# 结论

在本教程中，我演示了如何使用 LangChain、OpenAI 和 ChromaDB 使用 RAG 功能创建语义研究论文引擎。此外，我还展示了如何为该引擎开发 Web 应用程序，并集成了 Literal AI 的 Copilot 和可观测性功能。在现实世界的语言模型应用程序中，通常需要纳入评估和可观测性以确保最佳性能。此外，Copilot 对于不同的软件应用程序来说可能是一个非常有用的功能，本教程可以作为一个很好的起点，了解如何为您的应用程序设置它。

您可以在我的 [GitHub](https://github.com/tahreemrasul/semantic_research_engine) 上找到本教程的代码。如果您觉得本教程有帮助，请考虑通过给予它五十次鼓掌来表示支持。您可以 [关注](/@tahreemrasul)，因为我分享了人工智能领域的实际演示、解释和很酷的副项目。来 [X](https://twitter.com/tahreemrasul1) 打个招呼！我在那里分享指南、代码片段和其他有用的内容。👋