# Salesforce如何在4天内构建一个AI驱动型应用

![Featued image for: How Salesforce Built an AI-Driven App in Under 4 Days](https://cdn.thenewstack.io/media/2024/10/a9f262c8-salesforce-dogfoods-its-ai-agent-platform-2-1024x631.jpg)

Salesforce活动团队计划为Dreamforce大会应用构建一个定制AI的消息传出后，让在线CRM的AI团队感到惊讶，该团队已经创建并使用了一个名为Agentforce的新AI企业技术栈来为客户构建AI代理。

[Agentforce平台](https://www.salesforce.com/form/agentforce/demo/)于周二正式上市，但当时，AI团队正专注于利用它帮助外部客户为他们自己开发AI代理，Salesforce AI执行副总裁说。

“在Dreamforce召开前四天，我们接到一个电话，说：‘嘿，我们有一个活动团队正在构建的活动应用程序，他们完全自己动手——他们正在设置一个[向量数据库](https://thenewstack.io/ai-needs-more-than-a-vector-database/)，他们正在导入数据，’”告诉The New Stack。“试图将所有这些东西整合在一起需要大量的工作。我们当时想，‘嘿，等等，这正是这个技术栈所做的。你不需要自己动手做AI。’”

构建演示是一回事，但在全球最大的SaaS活动上只有四天的时间上线却让人担忧，尤其是在规模方面。但他表示，这实际上很简单，因为该技术栈是为支持扩展而构建的。

“你可以直接进来，插入你的数据，插入操作，让规划器发挥其魔力，并能够非常快速地获得代理的v1版本。”

– Salesforce AI高管
但这确实为Agentforce技术栈提供了一个很好的测试。

“是否可以将所有数据集中在一个地方用于上下文和基础？”他说。“是否可以通过几次点击就能构建一个[RAG系统](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/)，然后用于指导代理系统？是否可以通过简单的操作和描述来配置代理应该执行并能够代表你执行的所有任务？然后，是否可以配置一个完整的代理系统和推理引擎，只需一些指令和一些防护措施，这就是构建过程。”

但使用AgentForce构建整个[代理AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 只花了2-3天时间，Govindarajan表示这“让内部每个人都大吃一惊”。

该应用名为AskAstro，在大会上首次亮相，允许与会者查询AI以查找感兴趣的会议和其他信息。根据Salesforce的新闻稿，它在Dreamforce上部署了超过10,000个AI代理实例。

Govindarajan表示，Salesforce现在计划将其AskAstro用于所有活动。

## AskAstro背后的AI技术栈

尽管该应用只花了几天时间就开发完成，但Govindarajan表示，如果一个组织从头开始，支持它的技术栈将需要六到八个月的时间。

他补充说，任何代理系统的核心基本上包括三件大事：

- 一个规划和推理引擎；
- 提供数据屏蔽并确保保护隐私和知识产权的隐私引擎；以及
- 检索增强生成。
“检索增强生成是关于生成正确的上下文。把它想象成一个上下文引擎，”他说。

Govindarajan表示，数据也是Agentforce背后的一个关键要素。他补充说，如果没有正确的数据，大型语言模型就会产生幻觉，因此提供正确的上下文和正确的数据非常重要。

![An image showing two people and the Agentforce technology stack.](https://cdn.thenewstack.io/media/2024/10/f80d9131-salesforceagentforce-tech-stack.jpg)
Agentforce技术栈。图片由Salesforce提供。

他说，当[大型语言模型(LLM)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)和[生成式AI](https://thenewstack.io/whats-wrong-with-generative-ai-driven-development-right-now/)首次出现时，一切都与语言能力有关。但这很快就改变了。

“在过去八个月左右的时间里，我们意识到LLM不仅擅长语言，而且擅长协调任务，协调API调用，……一方面与客户交谈，然后将该任务分解成更小的子任务，然后将这些子任务映射到他们可以代表客户采取的具体行动，”他说。“这是一个彻底的改变游戏规则者。”
“Agentforce relies on a series of large language models (LLMs) for reasoning, planning, and system generation. Some of these are their own models used for privacy preservation, personally identifiable information (PII) redaction, and data masking.  This is a family of models we build and deliver, some of which are essentially blends of internal models we’ve developed and external models used for listening and language generation,” he said.

He likened it to the shift a decade ago when cloud SaaS models disrupted the traditional software development path of building and buying one’s own infrastructure.

“It’s kind of a déjà vu moment where you don’t need to set up your own vector database. You don’t need to set up your own data cloud. You don’t need to use a data engine. You don’t need to set up your own planner prompting mechanism,” he said. “You just come in, plug in your data, plug in the operation, let the planner do its magic, and you get a v1 version of the agent very quickly.”


## The Challenges of Testing AI

Testing AI agents can be a real challenge. Govindarajan outlined a series of considerations when testing agent AI:

- What testing tools can you use to test agent systems?
- Can you create synthetic data for simulated users?
- What happens if the correct answer doesn’t emerge?
- If you get an incorrect answer, are there tools to debug?
- Can you pinpoint the source of incorrect output?
“Basically, debugging is a problem when you hit the first problem, testing is a problem, but within four days, we were able to internally test all of these things very quickly,” he said. “It was a real test to see if our claims held water.  Could you build a production-ready agent within four days of introducing data, introducing context, introducing operations, and testing at scale? That’s what we did.”

AskAstro can also remember previous conversations with users. While it’s an agent, it’s built on a multi-tenant system, so if a user logs in, it can remember the conversation and provide a more personalized experience, he said.


## How Agent AI Will Change Front-End Development

Govindarajan added that agent AI will drive future applications, and it needs to change how front-end and web application developers approach their end products.

“We see a lot of two-dimensional applications presented as buttons and widgets on the screen that encode the work that needs to be done in the enterprise… This is going to transform into much more intelligent agents,” he said. “Everyone will have an agent. Everyone will have an assistant they can talk to and get work done.”

He added that in many ways, the interface is much simpler because you just talk to the system, and it understands enough context that you don’t need to over-prompt it.

“It understands enough context that you don’t need to prompt it in exactly the same way,” he said. “When people are trying to accomplish a task, they prompt the engine in various ways. They don’t always phrase the request in the same way. And the beauty of these agent systems is that they’re able to understand that range of expression and map it to the very specific thing you want to accomplish on behalf of the user.”

“Everyone will have an agent. Everyone will have an assistant they can talk to and get work done.”

– Govindarajan

He said that’s the key experience AI provides, simplifying everything else in the interface.

Another feature they added is that it can recommend questions attendees might ask. For example, if an attendee asks what happened at Dreamforce that day, the AI will provide some answers and then suggest other questions for the attendee based on any previous conversation or context. It might prompt the attendee if they want to know about evening events or want to figure out where to grab lunch nearby.

What does this mean for web application developers and front-end developers? It might be time to upskill while focusing on AI. Salesforce has trained nearly 8,000 web developers in its ecosystem how to build agents from scratch, and it’s largely about providing the right dataset for the user, he said.

“Once you build it, you test it, you’re ready to ship it,” he said. “Putting it into your mobile application is just a matter of an API call.”

[YOUTUBE.COM/THENEWSTACK Technology is moving fast. Don’t miss an episode. Subscribe to our YouTube channel to watch all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)