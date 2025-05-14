
<!--
title: 构建RAG驱动的聊天机器人的实用指南
cover: https://cdn.thenewstack.io/media/2025/05/6a69f156-chat-7767694_1280.jpg
summary: 手把手教你用云原生技术栈+LLM，快速打造基于 RAG 的 ChatGPT 聊天机器人！文章深入浅出讲解 RAG 基础，并提供基于 LangChain 和 OpenAI 的开源示例，教你玩转向量数据库，降低云服务"Egress Fee"，轻松应对 AI 落地挑战！
-->

手把手教你用云原生技术栈+LLM，快速打造基于 RAG 的 ChatGPT 聊天机器人！文章深入浅出讲解 RAG 基础，并提供基于 LangChain 和 OpenAI 的开源示例，教你玩转向量数据库，降低云服务"Egress Fee"，轻松应对 AI 落地挑战！

> 译自：[A Practical Guide To Building a RAG-Powered Chatbot](https://thenewstack.io/a-practical-guide-to-building-a-rag-powered-chatbot/)
> 
> 作者：Pat Patterson

“你能为我们构建一个聊天机器人吗？” 如果你的 IT 团队尚未收到此请求，请相信我，它已经在路上了。随着 LLM 的兴起，聊天机器人已成为新的必备功能——无论你是在发布 SaaS、管理内部工具，还是只是试图理解庞大的文档。问题是？用胶带将搜索索引连接到 LLM 是不够的。

如果你的聊天机器人需要从文档、日志或其他内部知识来源中找到答案，那么你不仅仅是在构建一个聊天机器人，而是在构建一个检索管道。如果你没有考虑你的数据存储在哪里、如何检索以及移动它的成本是多少，那么你就是在为自己构建一个臃肿、脆弱的系统。

今天，我将分解如何构建一个真正的对话式聊天机器人——它利用检索增强生成 (RAG)，最大限度地减少延迟，并避免悄无声息地扼杀你的利润的云出口费用陷阱。LLM 是容易的部分。基础设施才是真正的工作和成本所在。

我将展示一个简单的对话式 AI 聊天机器人 Web 应用程序，它具有 ChatGPT 风格的 UI，你可以轻松地将其配置为与 OpenAI、DeepSeek 或任何其他大型语言模型 (LLM) 一起使用。

## 首先：RAG 基础知识

检索增强生成（简称 RAG）是一种将 LLM 的生成功能应用于文档集合的技术，从而产生一个可以根据这些文档的内容有效回答问题的[聊天机器人](https://thenewstack.io/build-a-python-chatgpt-3-5-chatbot-in-10-minutes)。

典型的 RAG 实现将集合中的每个文档分成几个大小大致相等、重叠的块，并为每个块生成一个[嵌入](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/)。嵌入是具有数百或数千个维度的浮点数向量（列表）。两个向量之间的距离表示它们的相似度。小距离表示高相似度，大距离表示低相似度。

然后，RAG 应用程序将每个块及其嵌入加载到向量存储中。向量存储是一个专用数据库，可以执行相似性搜索——给定一段文本，向量存储可以通过比较嵌入来检索按与查询文本的相似性排序的块。

让我们把这些部分放在一起：

![](https://cdn.thenewstack.io/media/2025/04/6f3de614-image1.png)

给定用户提出的问题 (1)，RAG 应用程序可以查询向量存储，以查找与该问题相似的文本块 (2)。这些块构成了帮助 LLM 回答用户问题的上下文。以下是使用文档集合作为示例的样子：给定问题“告诉我关于对象锁的信息”，向量存储将四个文档块（每个块约 170 个单词）返回给应用程序 (3)。以下是每个块的文本链接和简短摘录：

*   [Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=before%20the%20set,on%20the%20file.): With Object Lock Legal Hold, files are prevented from being changed or deleted; however, immutability does not have a defined retention period.
*   [Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=From%20a%20functionality,than%20I%20wanted%3F): You can enable Object Lock on a bucket when you create a new bucket or on an existing bucket.
*   [Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=Backblaze%20B2%20SDKs,check%20the%20retention): Object Lock was designed with the Immutability feature in Veeam Backup & Replication in mind.
*   [Enable Object Lock with the S3-Compatible API](https://www.backblaze.com/docs/en/cloud-storage-enable-object-lock-with-the-s3-compatible-api#:~:text=Powered%20by-,Enable%20Object%20Lock%20with%20the%20S3%2DCompatible%20API,Backblaze%20API%20operations%20and%20their%20corresponding%20documentation%2C%20see%20API%20Documentation.,-Was%20this%20article): To enable Object Lock on an existing S3-compatible bucket, add the x-amz-bucket-object-lock-token header with a value of 1 to the S3 Put Object Lock Configuration API call.

不出所料，四个结果中有三个是从关于对象锁的主要文档文章中提取的。

为了提供对话体验，RAG 应用程序在消息存储中维护聊天历史记录。RAG 应用程序检索消息历史记录 (4)，以构成其将发送到 LLM 的查询的一部分。步骤 2 和 4（从向量和消息存储中检索数据）可以同时执行，因为它们互不依赖。

系统提示为 LLM 生成响应设置了指导方针。在 RAG 中，系统提示通常指定响应应基于检索到的文档数据，而不是模型记忆，并通过确保模型在未找到相关文档时不捏造信息来防止幻觉。以下是 RAG 应用程序中的系统提示：

> 1. 使用以下上下文片段和消息历史记录来回答最后的问题。如果您不知道答案，只需说您不知道；不要试图编造答案。

RAG 将系统提示、上下文、对话中的最后几条消息和用户的问题提交给 LLM (5)，LLM 生成一个（希望）有用的响应 (6)。以下是它对上述问题提供的答案：

对象锁定是一项允许用户对存储在云存储中的文件强制执行不变性的功能。以下是关于对象锁定的要点：

1. **不变性：** 一旦文件被锁定，在指定的保留期到期或解除法律保留之前，它不能被修改或删除。
2. **保留期：** 用户可以在锁定文件时设置保留期。在此期间，文件保持不变，这意味着它不能被更改或删除。
3. **法律保留：** 用户可以将文件置于法律保留之下，这将无限期地阻止修改或删除，直到解除保留。
4. **启用对象锁定：** 可以为新存储桶或现有存储桶启用对象锁定，但必须在上传文件之前在存储桶级别启用它。
5. **集成：** 某些应用程序（例如 Veeam Backup and Replication）提供对对象锁定的内置支持，从而简化了希望在备份期间确保文件不变性的用户的流程。
6. **无额外费用：** 使用对象锁定不收取额外费用；但是，标准存储费用仍然适用于锁定的文件。
7. **锁定中的错误：** 如果用户锁定的文件的时间超过了预期，他们可能需要联系支持人员来解决问题，这可能涉及在某些情况下关闭其存储帐户。

总的来说，对象锁定对于需要确保数据完整性并遵守有关数据保留的法规的组织来说是一项至关重要的功能。

RAG 应用程序将用户的问题和 LLM 的响应添加到消息存储 (7)，将答案返回给用户 (8)，并等待下一个问题。

## 示例应用程序快速浏览

示例应用程序已[发布在 GitHub 上](https://github.com/backblaze-b2-samples/ai-rag-examples)。该应用程序是开源的，采用 MIT 许可证，因此您可以将其用作实验的基础，没有任何限制。该应用程序使用与 S3 兼容的 API，因此它可以与任何与 S3 兼容的对象存储良好地配合使用。

请注意，与任何与一个或多个云服务提供商 (CSP) 集成的示例应用程序一样，您在运行示例应用程序时可能会产生费用，包括存储和从 CSP 下载数据的费用。下载费用通常被称为“出口费用”，并且可能很快超过存储数据的费用。AI 应用程序通常集成了来自多个专业提供商的功能，因此您应该仔细检查云存储提供商的定价，以避免在月底收到意外账单。货比三家——一些专业的云存储提供商免费提供慷慨的每月出口流量，高达您存储数据量的三倍，此外，在一种情况下，还可以无限制地免费出口到该存储提供商的合作伙伴。

README 文件详细介绍了配置和部署；在本博文中，我将提供一个高级概述。示例应用程序是用 Python 编写的，使用 [Django web framework](https://www.djangoproject.com/)。API 凭据和相关设置通过环境变量配置，而 LLM 和向量存储通过 Django 的 settings.py 文件配置：

```py
CHAT_MODEL: ModelSpec = {
    'name': 'OpenAI',
    'llm': {
        'cls': ChatOpenAI,
        'init_args': {
            'model': "gpt-4o-mini",
        }
    },
}
 
# Change source_data_location and vector_store_location to match your environment
# search_k is the number of results to return when searching the vector store
DOCUMENT_COLLECTION: CollectionSpec = {
    'name': 'Docs',
    'source_data_location': 's3://rag-app-bucket/pdfs',
    'vector_store_location': 's3://rag-app-bucket/vectordb/docs/openai',
    'search_k': 4,
    'embeddings': {
        'cls': OpenAIEmbeddings,
        'init_args': {
            'model': "text-embedding-3-large",
        },
    },
}
```
示例应用程序配置为使用 OpenAI GPT-4o mini。不过，README 解释了如何使用不同的在线 LLM，例如 DeepSeek V3 或 Google Gemini 2.0 Flash，甚至是通过 [Ollama](https://ollama.com/) 框架使用 Meta Llama 3.1 等本地 LLM。如果确实运行本地 LLM，请务必选择适合您硬件的模型。我尝试在配备 M1 Pro CPU 的 MacBook Pro 上运行 Meta 的 Llama 3.3，它有 700 亿个参数 (70B)。它花了将近 3 个小时才回答一个问题！Llama 3.1 8B 更适合，在不到 30 秒的时间内回答问题。

请注意，文档集合配置了向量存储的位置，其中包含技术文档库作为示例数据集。README 文件包含一个应用程序密钥，具有对 PDF 和向量存储的只读访问权限，因此您可以尝试该应用程序，而无需加载自己的文档集。

如果您想使用您的文档集合，可以使用一对自定义命令从云对象存储将其加载到向量存储中，然后查询向量存储以测试它是否全部工作。

首先，您需要加载您的数据：

```
% python manage.py load_vector_store
 
Deleting existing LanceDB vector store at s3://rag-app-bucket/vectordb/docs
Creating LanceDB vector store at s3://rag-app-bucket/vectordb/docs
Loading data from s3://rag-app-bucket/pdfs in pages of 1000 results
Successfully retrieved page 1 containing 618 result(s) from s3://rag-app-bucket/pdfs
Skipping pdfs/.bzEmpty
Skipping pdfs/cloud_storage/.bzEmpty
Loading pdfs/cloud_storage/cloud-storage-add-file-information-with-the-native-api.pdf
Loading pdfs/cloud_storage/cloud-storage-additional-resources.pdf
Loading pdfs/cloud_storage/cloud-storage-api-operations.pdf
...
Loading pdfs/v1_api/s3-put-object.pdf
Loading pdfs/v1_api/s3-upload-part-copy.pdf
Loading pdfs/v1_api/s3-upload-part.pdf
Loaded batch of 614 document(s) from page
Split batch into 2758 chunks
[2025-02-28T01:26:11Z WARN  lance_table::io::commit] Using unsafe commit handler. Concurrent writes may result in data loss. Consider providing a commit handler that prevents conflicting writes.
Added chunks to vector store
Added 614 document(s) containing 2758 chunks to vector store; skipped 4 result(s).
Created LanceDB vector store at s3://rag-app-bucket/vectordb/docs. "vectorstore" table contains 2758 rows
```

不要对“unsafe commit handler”警告感到惊慌——我们的示例向量存储永远不会收到并发写入，因此不会有冲突或数据丢失。
现在，您可以通过查询向量存储来验证数据是否已存储。请注意，来自向量存储的原始结果包括一个 S3 URI，用于标识源文档：

```
% python manage.py search_vector_store 'Which S3 API operation would I use to upload a file?'
 
2025-04-07 16:24:51,615 ai_rag_app.management.commands.search_vector_store INFO     Opening vector store at s3://blze-ev-ai-rag-app/vectordb/docs/openai
2025-04-07 16:24:51,615 ai_rag_app.utils.vectorstore DEBUG    Populating AWS environment variables from the b2-ev profile
Found 4 docs in 5.25 seconds
2025-04-07 16:24:57,386 ai_rag_app.management.commands.search_vector_store INFO     
page_content='b2_list_parts  b2_list_unfinished_large_files  b2_start_large_file  b2_update_file_legal_hold  b2_update_bucket  b2_upload_file  b2_update_file_retention  b2_upload_part  S3-Compatible API  To go directly to the detailed S3-Compatible API operations, click here.  To learn more about using the S3-Compatible API, click here.  API Operations  Object Operations  S3 Copy Object  S3 Delete Object  S3 Get Object  S3 Get Object ACL  S3 Get Object Legal Hold  S3 Get Object Retention  S3 Head Object  S3 Put Object  S3 Put Object ACL  S3 Put Object Legal Hold  S3 Put Object Retention  S3 Abort Multipart Upload  S3 Complete Multipart Upload  S3 Create Multipart Upload  S3 Upload Part  S3 Upload Part Copy  S3 List Multipart Uploads  Bucket Operations  S3 Create Bucket  S3 Delete Bucket  S3 Delete Bucket CORS  S3 Delete Bucket Encryption  S3 Delete Objects  S3 Get Bucket ACL  S3 Get Bucket CORS  S3 Get Bucket Encryption  S3 Get Bucket Location  S3 Get Bucket Versioning' metadata={'source': 's3://blze-ev-ai-rag-app/pdfs/cloud_storage/cloud-storage-api-operations.pdf'}
 
...
```

示例应用程序的核心是 RAG 类。有几种方法可以创建 RAG 的基本组件，但在这里我们将了解 _create_chain() 方法如何使用开源 [LangChain AI framework](https://python.langchain.com/v0.2/docs/introduction/) 将系统提示、向量存储、消息历史记录和 LLM 结合在一起。

首先，我们定义系统提示，其中包括上下文的占位符——RAG 将从向量存储中检索的那些文本块：

```
# These are the basic instructions for the LLM
system_prompt = (
    "Use the following pieces of context and the message history to "
    "Answer the question at the end. If you don't know the answer, "
    "just say that you don't know, don't try to make up an answer. "
    "\n\n"
    "Context: {context}"
)
```

然后我们创建一个提示模板，将系统提示、消息历史和用户的问题结合起来：

```py
# The prompt template brings together the system prompt, context, message history and the user's question
prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history", optional=True, n_messages=10),
        ("human", "{question}"),
    ]
)
```
现在我们使用 [LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/) (LCEL) 从各种组件形成一个链。LCEL 允许我们声明式地定义组件链；也就是说，我们提供所需链的高级表示，而不是指定组件应如何链接在一起：

```py
# Create the basic chain
# When loglevel is set to DEBUG, log_input will log the results from the vector store
chain = (
    {
        "context": (
            itemgetter("question")
            | retriever
            | log_data('Documents from vector store', pretty=True)
        ),
        "question": itemgetter("question"),
        "history": itemgetter("history"),
    }
    | prompt_template
    | model
    | log_data('Output from model', pretty=True)
)
```

请注意 `log_data()` 辅助方法——它只是记录其输入数据并将其传递给链中的下一个组件。

为链分配一个名称允许我们在调用它时添加检测。您将在本文后面看到我们如何添加一个回调处理程序，该处理程序使用执行链所花费的时间来注释链输出：

```markdown
# Give the chain a name so the handler can see it
named_chain: Runnable[Input, Output] = chain.with_config(run_name="my_chain")
```
现在，我们使用 LangChain 的 `RunnableWithMessageHistory` 类来管理从消息存储中添加和检索消息。Django 框架为每个用户分配一个会话 ID，我们使用它作为存储和检索消息历史记录的键：

```py
# Add message history management
return RunnableWithMessageHistory(
    named_chain,
    lambda session_id: RAG._get_session_history(store, session_id),
    input_messages_key="question",
    history_messages_key="history",
)
```

最后，`log_chain()` 函数将链的 ASCII 表示形式打印到调试日志。请注意，我们必须提供预期的配置，即使 `session_id` 不会被使用：

```py
log_chain(history_chain, logging.DEBUG, {"configurable": {'session_id': 'dummy'}})
```

这是输出——它提供了数据如何流经链的有用可视化：

![](https://cdn.thenewstack.io/media/2025/04/b9bd905e-image2-523x1024.png)

dumper 组件由 `log_data()` 辅助方法插入，以记录数据在链中传递时的数据。相比之下，Lambda 组件由 `itemgetter()` 方法插入，以从传入的 Python 字典中提取元素。

RAG 类的 `invoke()` 函数在响应用户的问题时被调用，非常简单。这是代码的关键部分：

```py
response = self._chain.invoke(
    {"question": question},
    config={
        "configurable": {
            "session_id": session_key
        },
        "callbacks": [
            ChainElapsedTime("my_chain")
        ]
    },
)
```
链的输入是一个包含问题的 Python 字典，而 `config` 参数使用 Django 会话密钥和一个回调来配置链，该回调使用其执行时间来注释链输出。由于链输出包含 [Markdown](https://www.markdownguide.org/getting-started/) 格式，因此处理来自前端的请求的 API 端点使用开源 [markdown-it library](https://github.com/markdown-it/markdown-it) 将输出呈现为 HTML 以进行显示。

代码的其余部分主要与呈现 Web UI 有关。一个有趣的方面是，负责在页面加载时呈现 UI 的 Django 视图使用 RAG 的消息存储来呈现对话，因此如果您重新加载页面，您不会丢失上下文。

## 运行此代码！

如上所述，[示例 AI RAG 应用程序](https://github.com/backblaze-b2-samples/ai-rag-examples) 是开源的，采用 MIT 许可证，我鼓励您将其用作您自己的 RAG 探索的基础。`README` 文件提出了一些您可以扩展它的方法，如果您正在考虑在生产环境中运行该应用程序，我还请您注意 `README` 的结论：

[…] 为了让您快速入门，我们以多种方式简化了应用程序。如果您希望在生产环境中运行此应用程序，则需要注意以下几个方面：

- 该应用程序不使用数据库来存储用户帐户或任何其他数据，因此它不需要身份验证。所有访问都是匿名的。如果您希望用户登录，则需要恢复 Django 的
将 [AuthenticationMiddleware](https://docs.djangoproject.com/en/5.1/ref/middleware/#module-django.contrib.auth.middleware) 类添加到 `MIDDLEWARE` 配置中，并 [配置数据库](https://docs.djangoproject.com/en/5.1/ref/databases/)。

*   会话存储在内存中。如上所述，[你可以使用 Gunicorn 将应用程序扩展到多个线程](https://github.com/backblaze-b2-samples/ai-rag-examples)，但你需要[配置 Django 会话后端](https://docs.djangoproject.com/en/5.1/topics/http/sessions/)才能在多个进程或多个主机上运行该应用程序。
*   同样，对话历史记录存储在内存中，因此你需要使用持久性消息历史记录实现，例如 [RedisChatMessageHistory](https://python.langchain.com/api_reference/redis/chat_message_history/langchain_redis.chat_message_history.RedisChatMessageHistory.html) 才能在多个进程或多个主机上运行该应用程序。

最重要的是，玩得开心！人工智能是一项快速发展的技术，供应商和开源项目每天都在发布新的功能。我希望你发现这个应用程序是开始使用的宝贵方式。