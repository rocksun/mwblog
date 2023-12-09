<!--
title: 2023人工智能工程五大新方向
cover: https://cdn.thenewstack.io/media/2023/10/4029c641-img_3988-1024x768.jpg
-->

除了LLM的大量增加，AI开发工具也有了扩展。我们来看一下今年AI开发中的五个关键趋势。

> 译自 [Top 5 AI Engineering Trends of 2023](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/)，作者 Richard MacManus 是The New Stack的高级编辑，专注于Web和应用程序开发趋势的报道。此前，他于2003年创办了ReadWriteWeb，并将其发展成为全球最有影响力的科技新闻站之一。从早期...

使用大语言模型(LLM)进行应用程序开发，是今年技术发展中的最大趋势之一。这始于公司通过 OpenAI 的专有模型使用其 API，但到 2023 年底，有大量不同的 LLM 可供选择，包括开发人员可以直接访问的开源 LLM，而不是依赖 API。

与 LLM 的激增一样，也有大量用于将 LLM 集成到应用中的开发工具。作为我们查看 AI 工程今年五大关键趋势的一部分，我们将讨论此问题及更多内容。

## 1. AI 工程师的出现

首先也是最重要的，开发人员现在有了一个新的职业选择:AI 工程师。

根据其主要宣传者 Shawn " @swyx" Wang 介绍，AI 工程师是“提示工程师”的下一步。今年早些时候，他创建了一个简洁的图表，展示了 AI 工程师在更广泛的 AI 和开发生态系统中的位置:

![](https://cdn.thenewstack.io/media/2023/08/e71540ee-aiengineer_diagram_swyx.png)

*通过 swyx。*

AI 工程师的角色仍然非常新。截至 2023 年底，它意味着使用 LLM 和相关工具的开发人员，例如 LangChain 框架和向量数据库。

在 10 月我对 Shawn Wang 在旧金山联合主持的 [AI 工程师峰会](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)上的采访中，他将 AI 工程师的角色比作是移动专家。

“所以，把AI看作一个平台，就像移动工程一样，对吧？就像，你只专注于移动堆栈。我不想碰它，因为移动很复杂。你参加所有移动会议，了解所有移动技术，还知道争论。但当我需要处理任何移动问题时，我就来找你，你知道如何解决。”

他补充说，所有开发人员都应该至少了解一下什么是AI工程，就像十到十五年前移动工程变得流行时他们至少了解了移动工程的范围一样。

## 2. LLM堆栈的演进

今年AI工程中的一个相关趋势是这一新角色的技术堆栈的出现。关于堆栈包含什么，有不同的意见，但我喜欢VC公司安德森·霍洛维茨（a16z）的以下[图表](https://a16z.com/2023/06/20/emerging-architectures-for-llm-applications/)：

![](https://cdn.thenewstack.io/media/2023/07/6b75311f-a16z_emerging_llm_stack.jpg)

对于AI工程师来说，编排层可能是最重要的，因为这是他们的应用程序将连接到LLMs的地方。这就是“提示工程”的地方，基本上是一种查询LLMs的方法，以使这些系统为应用程序提供有用的信息。在2023年，[类似LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)和[LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/)的工具出现，以帮助开发人员进行提示工程和其他LLM集成。

值得注意的是LangChain名称中的“Chain”一词，它表明它可以与其他工具进行互操作 - 不仅仅是各种LLMs，还有其他开发框架。例如，今年五月，Cloudflare宣布LangChain支持其Workers框架。

## 3. 开源LLMs

今年在AI工程领域最具影响力的发展，可以说是开源LLMs的兴起。在OpenAI在11月份几乎因一场董事会政变而[濒临崩溃](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/)后，拥有选择的另类、非专有LLMs变得尤为重要。

我与大多数AI工程师的交流中得知，他们认为OpenAI的LLMs仍然优于其他LLMs。然而，[开源模型](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)正在迅速赶超。Meta于7月宣布的LLama 2目前在[斯坦福的HELM](https://crfm.stanford.edu/helm/latest/#/leaderboard)（语言模型的整体评估）基准排行榜上居首。

![](https://cdn.thenewstack.io/media/2023/12/12319841-llama2_dimensions.png)

*LLama 2规格；来自Meta*

当Meta在2月份首次宣布LLama时，它以非商业许可向研究界发布了模型权重。而其他强大的LLMs，如GPT，通常只能通过有限的API访问。

“所以你必须通过OpenAI并访问API，但你实际上不能，比如说，下载模型或在你的电脑上运行它，” Lightning AI 的[Sebastian Raschka](https://sebastianraschka.com/)在五月向我解释道。“基本上你不能进行任何自定义。”

换句话说，LLama对于开发人员来说更加灵活。随着我们进入2024年，这对于当前LLMs的领导者，如OpenAI和Google，可能具有潜在的颠覆性。

## 4. 向量数据库

今年在LLM开发的数据方面最大的影响力无疑是[向量数据库](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/)的使用。

微软将[向量数据库定义](https://learn.microsoft.com/en-us/semantic-kernel/concepts-ai/vectordb)为“一种将数据存储为高维向量的数据库类型，这些向量是特征或属性的数学表示。” 数据以一种称为“嵌入”的技术存储为向量。

在今年早些时候的《The New Stack》上的[一篇投稿](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/)中，[Mark Hinkle](https://www.linkedin.com/in/markrhinkle/)使用仓库的类比来解释向量数据库的用例。“想象一下，将向量数据库视为一个巨大的仓库，而AI则是熟练的仓库管理员，” Hinkle写道。“在这个仓库中，每个物品（数据）都存储在一个箱子（向量）中，整齐地组织在多维空间的货架上。” 然后，AI可以根据它们的相似性检索或比较物品。据Hinkle称，向量数据库“非常适用于推荐系统、异常检测和自然语言处理等应用。”

像Pinecone这样的新型数据库解决方案或Chroma等开源项目在今年在向量数据库领域开辟了有利可图的市场。但市场上现在有许多[向量数据库的选择](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)，包括一些现有的数据库公司为其产品添加这一功能。例如，Redis在其Redis Enterprise产品中提供了向量数据库功能。

## 5. AI代理

也许在AI工程领域最具争议的趋势之一就是AI代理软件，比如AutoGPT，该软件于三月底发布。AI代理是使用LLMs执行各种任务的自动化软件片段。

十月份的AI工程师峰会上，我感觉到一些演讲者对这些自动化代理的能力过于自信。也许甚至有些傲慢，因为代理的一般理念似乎是将人类排除在外。但如果你曾经与银行或电话公司等机构的自动聊天机器人打过交道，有可能你希望在聊天的另一端是一个人类。

Voxel51的机器学习工程师Jacob Marks在[LinkedIn的一篇文章](https://www.linkedin.com/posts/jacob-marks_aiengineer-aiengineersummit-aiesummit-activity-7117624778105970688-_mcr?utm_source=share&utm_medium=member_desktop)中这样表达：“AI代理远未达到其充分潜力。部分原因是很难为这些代理创建健壮的评估。AutoGPT正经历重大波动。”

也许2024年是Auto-GPT和其他AI代理软件崭露头角的时候。但目前，正如OpenAI联合创始人Andrej Karpathy在四月警告的那样，风险在于AI代理可能“失控”。

## 结论

在AI工程领域，这一年是创新的繁忙之年。尽管存在明显的问题，无论是技术上的（见AI代理）还是商业上的（见OpenAI董事会），我们可以期待来年生成式AI方面取得更大的进展。OpenAI正受到Meta和Google等公司的积极挑战，所有迹象都表明底层技术将继续飞速改进。就在这周，[Google发布了Gemini](https://www.theguardian.com/technology/2023/dec/06/google-new-ai-model-gemini-bard-upgrade)，声称在大多数测试中胜过了ChatGPT。对于LLM霸权的争夺将持续到2024年。

此外，LLM应用生态系统可能会成熟，像LangChain和Pinecone这样的年轻公司不断扩张。明年我们可能还会看到政府介入进行监管，因此一切可能并不会一帆风顺。

无论2024年会带来什么，202年对于AI工程领域来说都是一个狂野的一年 — 也许会被记为互联网历史上的一个关键时刻。

