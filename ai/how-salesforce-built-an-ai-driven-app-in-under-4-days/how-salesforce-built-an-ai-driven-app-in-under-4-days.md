
<!--
title: Salesforce如何在4天内构建一个AI驱动型应用
cover: https://cdn.thenewstack.io/media/2024/10/a9f262c8-salesforce-dogfoods-its-ai-agent-platform-2.jpg
-->

Salesforce仅用四天时间，就利用其新的AI技术栈构建了一个交互式Dreamforce应用程序。一位Salesforce高管解释了其方法。

> 译自 [How Salesforce Built an AI-Driven App in Under 4 Days](https://thenewstack.io/how-salesforce-built-an-ai-driven-app-in-under-4-days/)，作者 Loraine Lawson。

Salesforce活动团队计划为Dreamforce大会应用构建一个定制AI的消息传出后，让在线CRM的AI团队感到惊讶，该团队已经创建并使用了一个名为Agentforce的新AI企业技术栈来为客户构建AI代理。

[Agentforce平台](https://www.salesforce.com/form/agentforce/demo/)于周二正式上市，但当时，AI团队正专注于利用它帮助外部客户为他们自己开发AI代理，Salesforce AI执行副总裁说。

“在Dreamforce召开前四天，我们接到一个电话，说：‘嘿，我们有一个活动团队正在构建的活动应用程序，他们完全自己动手——他们正在设置一个[向量数据库](https://thenewstack.io/ai-needs-more-than-a-vector-database/)，他们正在导入数据，’”告诉The New Stack。“试图将所有这些东西整合在一起需要大量的工作。我们当时想，‘嘿，等等，这正是这个技术栈所做的。你不需要自己动手做AI。’”

构建演示是一回事，但在全球最大的SaaS活动上只有四天的时间上线却让人担忧，尤其是在规模方面。但他表示，这实际上很简单，因为该技术栈是为支持扩展而构建的。

> “你可以直接进来，插入你的数据，插入操作，让规划器发挥其魔力，并能够非常快速地获得代理的v1版本。”
>
> – Salesforce AI高管

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

*Agentforce技术栈。图片由Salesforce提供。*

他说，当[大型语言模型(LLM)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)和[生成式AI](https://thenewstack.io/whats-wrong-with-generative-ai-driven-development-right-now/)首次出现时，一切都与语言能力有关。但这很快就改变了。

“在过去八个月左右的时间里，我们意识到LLM不仅擅长语言，而且擅长协调任务，协调API调用，……一方面与客户交谈，然后将该任务分解成更小的子任务，然后将这些子任务映射到他们可以代表客户采取的具体行动，”他说。“这是一个彻底的改变游戏规则者。”

他将其比作十年前云基础的SaaS模型颠覆了传统的软件开发路径，即构建和购买自己的基础设施。

他说：“这有点像是似曾相识的时刻，你不需要建立自己的向量存储。你不需要建立自己的数据云。你不需要去数据引擎。你不需要去设置规划提示机制。” “你可以直接进来，插入你的数据，插入动作，让规划器发挥它的魔力，并且能够非常、非常快地得到一个代理的v1版本。”

## 人工智能测试中的头痛问题

人工智能代理测试可能是一个真正的挑战。Govindarajan列举了在测试代理型AI时需要考虑的问题：

- 你能用哪些测试工具来测试代理系统？
- 你能创建模拟用户的合成数据吗？
- 如果正确答案没有出现怎么办？
- 如果它给出了错误答案，你有工具进行调试吗？
- 你能确定错误输出来自哪里吗？

“基本上，当你遇到第一个问题时，调试是个问题，测试是个问题，但在四天内，我们能够快速地自我测试所有这些事情，”他说。“这确实是对我们的故事是否真实的真正考验。你能否在四天内通过引入数据、引入上下文、引入行动，并在大规模测试后立即启动，构建一个生产级别的代理？这就是我们所做的。”

AskAstro还能记住与用户的先前对话。虽然它是一个代理，但它建立在多租户系统上，所以如果用户登录了，它可以记住对话并提供更个性化的体验，他说。

## Agentic AI将如何改变前端开发

Agentic AI将推动未来的应用程序发展，这将需要前端和Web应用开发者改变他们对最终产品的开发方式，Govindarajan补充说。

“我们目前看到的许多在屏幕上布局的二维应用程序，它们通过按钮和小部件编码了企业中工作需要完成的方式……这将变得更加具有代理性，”他说。“每个人都将拥有一个代理。每个人都将拥有一个可以与他们链接并帮助完成工作的助手。”

他补充说，在很多方面，界面变得更加简单，因为你只需要与系统对话，它就能理解足够的上下文，你不必过度提示它。

“它理解了足够的上下文，所以你不必以完全相同的方式提示它，”他说。“人类在尝试完成任务时，会以多种方式提示引擎。他们并不总是以相同的方式表达请求。而这些代理系统很酷的一点是，它们能够理解那种表达范围，并且能够将其映射到用户希望完成的非常具体的事情上。”

> “每个人都将拥有一个代理。每个人都将拥有一个可以与他们链接并帮助他们完成工作的助手。” 
> 
> – Govindarajan

他说，这就是人工智能提供的关键体验，它简化了界面中的其他一切。

他们增加的一个额外功能是，它能够推荐会议用户可以提出的问题。例如，如果与会者询问今天Dreamforce上发生了什么，人工智能会提供一些答案，然后会根据之前的任何对话或上下文，为与会者提供额外的问题建议。它可能会提示与会者是否想知道晚上的活动，或者与会者是否想知道在附近哪里吃午饭。

那么，这给Web应用开发者和前端开发者留下了什么？可能是时候以人工智能为方向，发展你的技能集了。Salesforce已经从其生态系统中培训了近8000名Web开发者，如何从头开始构建代理，这再次主要是关于将正确的数据集带给用户，他说。

“一旦你构建了它，测试了它，你准备启动它，”他说。“将其放入你的移动应用只是一个API调用的问题。”