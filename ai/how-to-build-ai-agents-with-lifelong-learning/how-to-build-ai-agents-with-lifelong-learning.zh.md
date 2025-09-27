AI 正在超越“设置即忘”的时代。尽管我们日常使用的强大语言模型，如 GPT-4，令人印象深刻，但在达到一定程度后，你会遇到瓶颈。这些模型尽管拥有诸多优点，一旦部署就无法从新经验中学习，这意味着你只能使用它们在训练期间拥有的信息。

但如果你的 AI 助手能记住每一次对话呢？如果它在处理完每个支持工单后能更好地帮助客户，或者从处理的每份文档中了解你的行业，那会怎样？这正是持续学习代理所做的，随着企业要求 AI 能够适应而非停滞不前，它们正变得至关重要。

传统 AI 就像雇用了一个才华横溢但无法形成新记忆的人。他们可以根据已知信息给出很好的答案，但他们从不从经验中改进或学习。持续学习代理则不同。它们就像拥有一位每天都在工作中不断进步的同事。

你的销售 AI 在处理了数百个客户问题后应该更了解你的产品。你的研究助手应该及时了解你领域内的最新论文。你的客户服务机器人应该识别重复出现的问题并随着时间的推移发展出更好的响应。

[构建这些自适应代理](https://thenewstack.io/self-aware-ai-building-adaptive-llm-decision-agents/) 的技术如今已经存在。通过将语言模型与智能记忆系统和反馈循环相结合，你可以创建出与你的业务一同进化的 AI。无论你是否有足够的技术能力自行构建，还是需要了解这对你的组织意味着什么，本指南都将向你展示它是如何工作的以及它对 AI 应用进化的重要性。

## **带有代码的教程步骤**

这份 [构建持续学习 AI 代理](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/) 的分步指南将向你展示如何安装依赖项、设置一个带有记忆的对话代理、创建一个基于向量的知识存储、实现一个用于新知识更新的管道、构建一个反射循环以随着时间的推移改进答案，并最终演示如何使用学习到的知识和大型语言模型 (LLM) 来检索和回答问题。请按照每个代码片段和解释来构建你自己的自适应代理。

### **安装依赖项**

我们首先安装所需的 Python 包：`langchain` 用于 [LLM](https://thenewstack.io/build-scalable-llm-apps-with-kubernetes-a-step-by-step-guide/) 编排，`llama-index` 用于向量存储和检索，`openai` 用于连接 GPT-4，`pandas` 用于数据处理，以及 `faiss-cpu` 用于支持向量存储索引。

`pip install langchain llama-index openai pandas faiss-cpu`

这些工具协同工作，创建一个交互式、可检索且持久的 AI 管道。

### **设置基础代理**

```
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

llm = ChatOpenAI(model="gpt-4")
memory = ConversationBufferMemory()
agent = initialize_agent([], llm, agent="chat-conversational-react-description", memory=memory)
```

在这里，我们使用 LangChain 和 GPT-4 初始化一个对话代理。`ConversationBufferMemory` 跟踪对话上下文，使 AI 能够引用之前的消息并保持连贯性。

### **为知识库创建向量存储**

```
from llama_index import VectorStoreIndex, SimpleDirectoryReader

reader = SimpleDirectoryReader("./knowledge")
docs = reader.load_data()
index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()
```

这段代码从名为 `./knowledge` 的文件夹加载文档，并使用 LlamaIndex 创建一个基于向量的索引。该索引将每个文档转换为嵌入并存储起来，以便之后进行快速和相关的上下文检索。

### **定义持续学习更新**

```
def update_knowledge(new_text):
    from llama_index.schema import Document
    doc = Document(text=new_text)
    index.insert(doc)
    index.save_to_disk("./kb_index.json")
```

这个函数允许 AI 存储新知识——也许是对话中产生的洞察——通过将它们封装为文档并保存到知识库索引中。这模拟了代理的长期记忆。

### **反射和自训练循环**

```
def continual_loop():
    while True:
        query = input("Ask something: ")
        response = agent.run(query)
        print(response)
        feedback = input("Do you want to save this knowledge? (y/n)")
        if feedback.lower() == 'y':
            update_knowledge(response)
```

在这里，我们实现了一个连续循环，供 AI 与用户进行交互。回答后，AI 会征求反馈。如果获得批准，它将新的响应保存到其知识存储中。这个循环是代理实时学习的方式。

### **从更新的知识中检索**

```
def ask_with_context(question):
    context = query_engine.query(question).response
    prompt = f"Using this context: {context}, answer: {question}"
    return llm.predict(prompt)
```

在回答问题时，我们从向量索引中检索上下文，以丰富 LLM 的响应。这弥补了静态 LLM 功能与动态学习信息之间的差距。

## **真实世界部署的专业提示**

*   **用上下文标记一切：** 为你的文档添加来源信息和时间戳，以便你可以追溯知识的来源和学习时间。
*   **定期清理：** 设置定期审查，在重复或冲突信息混淆代理记忆之前发现它们。
*   **标记不确定内容：** 当你的代理对某个答案不确定时，将其标记以供人工审查，而不是让它随意回答。
*   **使其在会话之间保持：** 将你的代理所学内容存储在 [Pinecone](https://www.pinecone.io) 或 [Qdrant](https://qdrant.tech) 等共享数据库中，以便它在不同的对话和用户之间记住。
*   **控制谁学习什么：** 在团队环境中，你将需要不同的访问级别，以防止敏感知识泄露给错误的用户或上下文。

## **重要性与未来展望**

如今让我们印象深刻的聊天机器人，一旦我们拥有能够从每次交互中变得更智能的代理，最终将显得过时。你是愿意拥有一个永远给出相同预设回复的助手，还是一个能学习你的偏好并随着时间推移更好地帮助你的助手？

这种演变正在发生，因为公司意识到静态 AI 很快就会遇到瓶颈，而那些能够适应和进化的代理则成为真正有用的工具，与用户一同成长。

从基本聊天机器人到真正能记住、学习和改进的 AI，这仅仅是个开始，无论你是构建一个适应学生需求的导师、一个学习市场模式的财务顾问，还是一个越来越擅长解决问题的支持代理。

很快，我们将看到这些 [学习代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) 连接到实时网络搜索、日历系统，甚至是实体机器人。你现在用持续学习打下的基础，将是区分真正智能系统与其余系统的关键。

借助 [Andela 的指南](https://www.andela.com/blog-posts/develop-a-master-ai-agent-with-langgraph-in-python/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=ai-agents-python&utm_term=writers-room)，了解如何使用 LangGraph 在 Python 中构建 AI 代理。