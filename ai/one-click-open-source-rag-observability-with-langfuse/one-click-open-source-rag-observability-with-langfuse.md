
<!--
title: 一键式开源 RAG 可观测性，Langfuse — LlamaIndex，用于 LLM 应用程序的数据框架
cover: https://cdn.sanity.io/images/7m9jw85w/production/2e38fd76d589eed1dd66af785879e73b22eb7877-1999x1319.png
-->

LlamaIndex 是一款简单灵活的数据框架，用于将自定义数据源连接到大型语言模型 (LLM)。

> 译自 [One-click Open Source RAG Observability with Langfuse — LlamaIndex, Data Framework for LLM Applications](None)，作者 Langfuse。


[Image of Langfuse logo]

[Langfuse](/blog/author/langfuse) • March 18, 2024

# One-Click OSS Observability for RAG with Langfuse

*This is a guest post by the Langfuse team*

There are many different ways to make RAGs work for your use case. Which vector store to use? Which retrieval strategy to use? LlamaIndex makes it easy to try many of these approaches without having to deal with the complexities of integrations, prompting, and memory all at the same time.

Initially, we were working on complex RAG/agent applications at Langfuse and quickly realized the need for new observability and tooling to tweak and iterate on the details. Ultimately, these details are critical to going from a cool toy to a RAG application that is actually reliable and safe for users and customers. Imagine: if you have an interesting user session in your *production* RAG application, how can you quickly see if the context retrieved for that session is actually relevant, or if the LLM response is on point?

So we started working on [Langfuse.com](http://langfuse.com) ( [GitHub](https://github.com/langfuse/langfuse)) to build an open-source LLM engineering platform with tightly integrated features for tracing, prompt management, and evaluation. In the beginning, we were just solving our own and our friends' problems. Today, we have over 1000 projects relying on Langfuse and 2.3k stars on GitHub. You can [self-host](https://langfuse.com/docs/deployment/self-host) Langfuse or use our maintained [cloud instance](https://cloud.langfuse.com).

We are excited to announce our new integration with LlamaIndex today. This feature has been [highly anticipated by the community](https://github.com/orgs/langfuse/discussions/828) and fits into our project focus of native integrations with major application frameworks. Thanks to everyone who contributed and tested during the beta phase!

## The Challenge

We love LlamaIndex because its clean and standardized interface abstracts away a lot of complexity. Let's look at a simple example with a `VectorStoreIndex` and a `ChatEngine`.

```
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
chat_engine = index.as_chat_engine()
print(chat_engine.chat("What problems can I solve with RAGs?"))
print(chat_engine.chat("How can I optimize my RAG application?"))
```

In just 3 lines, we load local documents, add them to an index, and initialize a `ChatEngine` with an in-memory. We then have a stateful conversation with the `chat_engine`.

This is great for getting started, but we quickly run into questions like:

* "What context was actually retrieved from the index to answer the question?"
* "How is the chat memory managed?"
* "Which steps add the most latency to the overall execution? How can I optimize it?"

## One-Click OSS Observability to the Rescue

We integrated Langfuse to make it a one-click integration with LlamaIndex using a global callback handler.

**Setup**

- Install the community package (`pip install llama-index-callbacks-langfuse`)
- Copy/paste the environment variables from your Langfuse project settings into your Python project: `'LANGFUSE_SECRET_KEY'`, `'LANGFUSE_PUBLIC_KEY'`, and `'LANGFUSE_HOST'`

Now, all you need to do is set the global langfuse handler:

```
from llama_index.core import set_global_handler
set_global_handler("langfuse")
```

Voilà, with just two lines of code, you get detailed tracing of all aspects of your RAG application in Langfuse. They automatically include latency and usage/cost breakdowns.

[Image of Langfuse tracing screenshot]

## Grouping Multiple Chat Threads into a Session

Working with many teams building GenAI/LLM/RAG applications, we are constantly adding more features that help debug and improve these applications. One example is [session tracing](https://langfuse.com/docs/tracing/sessions) for conversational applications, so that you can see traces in the context of a complete message thread.

To activate it, simply add an ID that identifies the session as a trace parameter before calling `chat_engine`.

```
from llama_index.core import global_handler
global_handler.set_trace_params(
session_id="your-session-id"
)
chat_engine.chat("What did he do growing up?")
chat_engine.chat("What did he do at USC?")
chat_engine.chat("How old is he?")
```

This way, you can see all these chat calls grouped into a single session view in Langfuse Tracing:

[Image of Langfuse session tracing screenshot]
**跟踪更复杂的应用程序并使用其他 Langfuse 功能进行提示管理和评估**

此集成让您轻松开始跟踪。如果您的应用程序最终发展到使用自定义逻辑或其他框架/软件包，所有 Langfuse 集成都完全可以互操作。

我们还构建了其他功能来对提示进行版本控制和协作（Langfuse [提示管理](https://langfuse.com/docs/prompts/get-started)），跟踪 [实验](https://langfuse.com/docs/experimentation) 和 [评估](https://langfuse.com/docs/scores/overview) 生产跟踪。对于 RAG，我们专门与 RAGAS 团队合作，可以轻松在其使用 Langfuse 捕获的跟踪上运行其流行的评估套件（请参阅 [食谱](https://langfuse.com/docs/scores/model-based-evals/ragas)）。

**开始使用**

开始使用的最简单方法是按照 [食谱](https://docs.llamaindex.ai/en/stable/examples/callbacks/LangfuseCallbackHandler.html) 并查看 [文档](https://langfuse.com/docs/integrations/llama-index/get-started)。

**反馈？联系我们**

我们很乐意听到任何反馈。欢迎加入我们的 [社区 Discord](https://langfuse.com/discord) 或在此 [GitHub 线程](https://github.com/orgs/langfuse/discussions/828) 中添加您的想法。