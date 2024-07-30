
<!--
title: 如何使用RAG构建准确率更高的AI代理
cover: https://cdn.thenewstack.io/media/2024/07/e25239a7-rick-rothenberg-x3mylqmg9u8-unsplash.jpg
-->

本教程展示了如何使用检索器从非结构化数据中提取上下文，同时调用 API 获取更多数据来构建代理。

> 译自 [How To Build an AI Agent That Uses RAG To Increase Accuracy](https://thenewstack.io/how-to-build-an-ai-agent-that-uses-rag-to-increase-accuracy/)，作者 Janakiram MSV。

[检索增强生成](https://thenewstack.io/retrieval-augmented-generation-for-llms/) (RAG) 和 [函数调用](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/) 的结合可以极大地提高基于 LLM 的应用程序的功能。[基于函数调用的 RAG 代理](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/) 结合了两种方法的优势，依赖于外部知识库进行准确的数据检索，并执行特定函数以高效地完成任务。

RAG 框架中的函数调用使检索过程更加结构化。例如，可以预定义一个函数，根据用户查询从综合知识库中提取特定信息，RAG 系统将从该知识库中检索信息。这种方法确保响应既相关又精确地满足应用程序的要求。

![](https://cdn.thenewstack.io/media/2024/05/5026cffa-rag_function_call-1024x835.jpeg)

在本教程中，我们将构建一个代理，旨在帮助电子商务公司的产品经理分析销售和产品组合。它使用检索器从存储在 PDF 中的非结构化数据中提取上下文，同时调用 API 获取销售信息。

该代理可以访问一组工具和向量数据库。初始提示和注册的工具将发送到 LLM。如果 LLM 响应包含工具的子集，代理将执行它们并收集上下文。如果 LLM 不建议执行任何工具，代理将在向量数据库中执行语义搜索并检索上下文。无论从哪里收集上下文，它都将添加到原始提示中并发送到 LLM。

为了简化配置，我创建了一个 Docker Compose 文件来运行 MySQL 数据库和 Flask API 层。PDF 被单独索引并导入 ChromaDB。假设您有权访问 OpenAI 环境。

首先克隆 [Git 仓库](https://github.com/janakiramm/rag-agent) 并按照以下步骤在您的机器上配置代理。

```
git clone https://github.com/janakiramm/rag-agent.git
```

## 第 1 步：启动数据库和 API 服务器

切换到 `api` 目录并运行 Docker Compose 文件以启动数据库和相应的 API 服务器。

```
docker compose up -d --build
```

API 服务器公开了四个 API 端点：

*   `get_top_selling_products`
*   `get_top_categories`
*   `get_sales_trends`
*   `get_revenue_by_category`

您可以从 curl 调用这些端点。

```
curl "http://localhost:5000/api/sales/top-products?start_date=2023-04-01&end_date=2023-06-30"

curl "http://localhost:5000/api/sales/top-categories?start_date=2023-04-01&end_date=2023-06-30"

curl "http://localhost:5000/api/sales/trends?start_date=2023-04-01&end_date=2023-06-30"

curl "http://localhost:5000/api/sales/revenue-by-category?start_date=2023-04-01&end_date=2023-06-30"
```

![](https://cdn.thenewstack.io/media/2024/07/29eef344-rag-agent-1-1024x399.png)

## 第 2 步：索引 PDF 并将向量存储在 Chroma DB 中

在 `data` 目录下，您会找到一个 PDF，其中包含电子产品类别中一些产品的描述。我们的任务是索引它并将嵌入向量存储在 Chroma 中。

![](https://cdn.thenewstack.io/media/2024/07/b89aa059-rag-agent-2-801x1024.jpeg)

为此，启动 `Index-Datasheet` Jupyter Notebook 并运行所有单元格。

![](https://cdn.thenewstack.io/media/2024/07/9610f06e-rag-agent-3-1024x257.jpeg)

这将加载 PDF，执行分块，生成嵌入，最后将向量存储在 ChromaDB 中。

此 Notebook 的最后一个单元格执行简单的语义搜索以验证索引过程。

![](https://cdn.thenewstack.io/media/2024/07/533f8826-rag-agent-4-1024x347.jpeg)

现在，我们有两个可以帮助我们获取上下文的实体：1) API 和 2) 向量数据库。

## 第 3 步：运行 RAG 代理

代理代码在 `RAG-Agent` Jupyter Notebook 中可用。启动它并运行所有单元格以查看它的运行情况。

此 Notebook 包含决定执行工具还是执行语义搜索的逻辑。

我将 REST API 调用包装在 `tools.py` 中，该文件位于仓库的根目录中，我们将其导入代理。

```python
from tools import (
    get_top_selling_products,
    get_top_categories,
    get_sales_trends,
    get_revenue_by_category
)
```

由于我们决定从上一步执行的索引过程中持久化 Chroma 集合，我们将简单地加载它。

```python
chroma_client = chromadb.PersistentClient(path="./data")
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = chroma_client.get_or_create_collection(name="products", embedding_function=embedding_function)
```

根据可用的工具，我们将它们与提示一起传递给 LLM 以进行映射。然后，LLM 会推荐要调用的正确函数。以下是 `map_tools` 函数中的部分代码片段。

```python
….
messages = [{"role": "user", "content": prompt}]
    response = llm.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    # Ensure response has valid tool_calls
    response_message = response.choices[0].message
    tool_calls = getattr(response_message, 'tool_calls', None)
 
    functions = []
    if tool_calls:
        for tool in tool_calls:
            function_name = tool.function.name
            arguments = json.loads(tool.function.arguments)
            functions.append({
                "function_name": function_name,
                "arguments": arguments
            })
 
    return functions
```
类似地，我们有一个检索器负责从向量数据库中提取上下文。

```python
def retriever(query):
    vector = embedding_function([query])
    results = collection.query(    
        query_embeddings=vector,
        n_results=5,
        include=["documents"]
    )
    res = " \n".join(str(item) for item in results['documents'][0])
    return res
```

我们有一个简单的辅助函数，用于将收集到的上下文和原始提示发送到 LLM。

```python
def generate_response(prompt,context):
    input_text = (
        "Based on the below context, respond with an accurate answer. If you don't find the answer within the context, say I do not know. Don't repeat the question\n\n"
        f"{context}\n\n"
        f"{prompt}"
    )
    response = llm.chat.completions.create(
        model= model,
        messages=[
            {"role": "user", "content": input_text},
        ],
        max_tokens=150,
        temperature=0
    )
 
    return response.choices[0].message.content.strip()
```

代理的工作是首先检查 LLM 是否推荐任何工具，然后执行这些工具以生成上下文。如果没有，它将依靠向量数据库来生成上下文。

```python
def agent(prompt):
    tools = map_tools(prompt)
    
    if tools:    
        tool_output = execute_tools(tools)
        context = json.dumps(tool_output)       
    else:
        context = retriever(prompt)
        
    response = generate_response(prompt, context)
    return response
```

在下面的屏幕截图中，第一个响应来自工具/API，第二个来自向量数据库。

![](https://cdn.thenewstack.io/media/2024/07/ba23bae1-rag-agent-5-1024x289.jpeg)

## 扩展 RAG 代理以使用联邦语言模型

在这种情况下，我们依赖 OpenAI 的 GPT-4o 来映射函数调用并根据上下文生成最终响应。通过依赖联邦模型的概念，我们可以完全避免将上下文发送到基于云的 LLM，并使用部署在边缘的本地 LLM 来响应查询。

在我的下一篇文章（本系列的最后一部分）中，我们将看到如何将 RAG 代理的概念与联邦语言模型结合起来。敬请关注。