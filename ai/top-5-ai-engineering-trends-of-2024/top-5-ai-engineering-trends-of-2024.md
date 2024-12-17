
<!--
title: 2024年人工智能工程五大趋势
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1.png
-->

2024年是AI软件（特别是AI编码工具）成熟、自动化（AI代理）发展、小型模型涌现等的一年。

> 译自 [Top 5 AI Engineering Trends of 2024](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/)，作者 Richard MacManus。

[去年这个时候](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/), 我写道2023年的AI工程是由大型语言模型（LLM）的激增和AI开发工具的扩展所定义的。2024年，这些趋势仍在继续——但LLM和AI开发工具的市场也成熟了很多。今年，AI被集成到开发人员的核心工具（IDE）中，而用于创建“AI智能体”的新技术则出现在LangChain和LlamaIndex等辅助工具中。可用的LLM类型也变得更加多样化，小型模型和本地开发能力尤其受到开发人员的关注。

让我们更深入地了解今年出现的五个关键AI工程趋势。

## 1. 智能体系统

如果说“提示工程”是去年AI开发领域的年度热词，那么“智能体”就是今年的热门词。AI智能体是一个自动化软件，它使用大型语言模型（LLM）执行各种任务，而今年[每个人都在构建智能体](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)和/或“智能体系统”。

在6月下旬于旧金山举行的AI工程师世界博览会上，两家领先的AI工程初创公司——LangChain和LlamaIndex——分别提出了自己对智能体系统的愿景。

LangChain在今年早些时候发布了LangGraph，其首席执行官Harrison Chase将其描述为“专为智能体而构建”并设计为“高度可控且低级别”的系统。

![](https://cdn.thenewstack.io/media/2024/07/70abc3c8-langchain_agents.jpg)

*根据 LangChain 的 Harrison Chase 的说法，代理人的历史*

早期AI智能体（例如[2023年的AutoGPT](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)）的批评之一是，它们试图在没有人工干预的情况下做太多事情。2024年，Chase热衷于强调，在其对AI智能体的愿景中，人类仍然非常“参与其中”。他说，LangGraph“自带内置持久层”，“这使得许多非常酷的‘人工参与循环’交互模式成为可能”。

与此同时，在世界博览会的另一场演示中，LlamaIndex的创建者Jerry Liu将智能体定位为RAG（检索增强生成）的自然继承者，RAG是将预训练LLM与外部数据源集成的最常见方法。LlamaIndex将其AI智能体称为“知识助手”，这可能是为了使其更易于企业接受。

LlamaIndex今年的一个新功能是Llama Agents，Liu将其定位为“一个生产级的知识助手——尤其是在世界随着时间的推移变得越来越智能化的背景下”。

![](https://cdn.thenewstack.io/media/2024/07/32ec741d-llamaindex_agents1.jpg)

*LlamaIndex的Jerry Liu讨论了从简单到高级的代理。*

同样值得注意的是，10月份[Meta发布了“Llama Stack”](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/)，以帮助开发人员使用其Llama模型构建“智能体应用程序”。Meta的首席产品官Chris Cox表示：“Llama Stack是一套针对现代已部署LLM系统的每个组件的参考API。它也是一堆带有PyTorch和其他开发环境的库，可以帮助你立即上手。”


## 2. AI编码工具

如果说AI智能体在其发展中还处于早期阶段，那么AI辅助编码现在已成为开发人员的常见做法。根据最新的[Stack Overflow调查](https://survey.stackoverflow.co/2024/ai#sentiment-and-usage-ai-select)，76%的开发人员正在使用或打算使用AI。在[最新的JetBrains开发者调查](https://blog.jetbrains.com/team/2024/12/11/the-state-of-developer-ecosystem-2024-unveiling-current-developer-trends-the-unstoppable-rise-of-ai-adoption-leading-languages-and-impact-on-developer-experience/)中，用户压倒性地表示，节省时间和提高效率是使用AI工具进行开发的首要好处。另一方面，只有23%的人表示使用AI工具进行编码实际上提高了所创建代码和解决方案的质量。因此，关于AI生成的代码质量仍然存在疑问。

然而，毫无疑问，开发人员正在为这些AI工具找到许多用途。The New Stack的一位开发者兼撰稿人Jon Udell在今年发表了一系列文章，解释了他如何使用各种LLM作为“[助手团队](https://thenewstack.io/lets-talk-conversational-software-development/)”来帮助他完成和/或解释编码任务。他还发现了一些具有变革意义的AI用例，例如[创建软件图表](https://thenewstack.io/how-to-create-software-diagrams-with-chatgpt-and-claude/)。

另一个趋势是，开发人员不再需要特殊的工具来使用AI——它通常直接集成到他们的IDE中，使AI成为其开发流程的正常组成部分。今年早些时候，我们的驻站工程师兼撰稿人David Eastman测试了JetBrains系列IDE中的AI功能。[他的结论是](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)：
在某种程度上，“嘿！看！我们有AI！”对于IDE来说是当前的业务需求，因为环境在不断扩展，而商定的预期仍在形成中。到明年，很多这样的功能将成为IDE体验的一部分，就像今天的剪切和粘贴一样。

Eastman还对另外两种流行的AI编码工具进行了评估，[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)和[Zed AI](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/)。他对两者都印象深刻，并评论道：“很可能，不到一年，并且随着更具演示性的添加/删除/替换机制，Cursor和Zed都将成为使用AI的代码流的典范。”

10月份，我查看了另一个[新的AI编码工具Solver](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/)。它声称是AI辅助编码的范式转变，因为它允许开发人员将任务交给AI自主构建。该公司表示，这比GitHub Copilot、Cursor和Devin等简单的“AI自动完成工具”有了明显的进步。

![](https://cdn.thenewstack.io/media/2024/10/4399737c-solver-finished.png)

*Solver，市场上众多人工智能编码产品之一。*

最后，除了直接的编码工具外，选择和部署LLM的选项也越来越多。例如，GitHub在8月份[发布了GitHub Models](https://thenewstack.io/github-models-review-of-microsofts-new-ai-engineer-platform/)——使开发人员能够轻松使用最新的生成式AI模型。

## 3. AI工程师作为一种职业

去年，“AI工程师”这个职位刚刚兴起。但今年，随着越来越多的组织实施某种形式的AI软件，AI工程师变得不可或缺。

正如Fatih Nar和Roy Chua最近在[The New Stack上发表的一篇文章](https://thenewstack.io/ai-engineering-level-up-your-it-career/)中所写，“随着AI越来越深入地嵌入到业务运营中，AI工程师在确保AI解决方案在企业软件生态系统中的成功设计、实施和扩展方面发挥着关键作用。”

Nar和Chua观察到，AI工程师“必须精通数据管道的管理、确保数据质量以及为模型训练部署数据。”

如果您有兴趣在2025年从事这一职业，我们的姊妹网站Roadmap提供了一个循序渐进的[成为AI工程师的指南](https://roadmap.sh/ai-engineer)。还可以查看我们关于[AI工程的五大领先JavaScript工具](https://thenewstack.io/top-5-javascript-tools-for-ai-engineering/)的文章。

![](https://cdn.thenewstack.io/media/2024/12/fd471207-roadmap_aiengineer.png)

*成为人工智能工程师的路线图指南*

## 4. 小型模型和本地托管的LLM

2024年的两个LLM趋势对开发人员特别有吸引力。

第一个是小型语言模型（SLM）的兴起。正如Kimberley Mok在[2月份的概述](https://thenewstack.io/the-rise-of-small-language-models/)中所说，“这些模型是其大型同类模型的精简版本，对于预算紧张的小型企业来说，SLM正成为一个更具吸引力的选择，因为它们通常更容易训练、微调和部署，而且运行成本也更低。”

2月份，[谷歌发布了两个较小的开放模型](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)，并具有宽松的商业许可证：Gemma 2B和Gemma 7B。谷歌声称这两个模型在该尺寸范围内优于Llama 2和Mistral。

那么，使用Gemini和类似的SLM可以构建哪些类型的应用程序呢？根据谷歌DeepMind总监Tris Warkentin的说法，“这些模型有各种各样的应用。”

Warkentin说：“事实上，如果你看看整个生态系统的使用情况，这是开发人员最想使用的尺寸——7B尺寸用于文本生成和理解应用程序，从开放模型的角度来看。”

因为小型语言模型基本上是LLM的更精简版本，所以它们通常更容易在你的计算机上实现。这让我们想到了开发人员的第二个与LLM相关的趋势：本地托管的AI模型。

今年早些时候，The New Stack的David Eastman研究了[如何本地运行开源LLM](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，使用Ollama和Llama 2。他发现这使他能够在私有数据上运行查询，而没有任何安全问题。最近，我们的前端教程作者Alexander T. Williams提供了更多[关于SLM和本地开发的技巧和建议](https://thenewstack.io/coding-with-slms-and-local-llms-tips-and-recommendations/)。还可以查看Janakiram MSV关于如何使用Nvidia NIM和Milvus构建基于RAG的LLM应用程序的教程[在GPU加速的机器上本地运行](https://thenewstack.io/build-a-rag-app-with-nvidia-nim-and-milvus-running-locally/)。

![](https://cdn.thenewstack.io/media/2024/02/0deb09f2-untitled-1024x499.png)


*来自@patrickdubois的GenAI测试演示*

## 5. 开源AI

今年关于AI的开源内容有很多深入的讨论。
尤其是一些人声称Meta的LLaMA模型并非真正意义上的开源，因为训练数据访问受限以及其他问题——例如许可条款鼓励在Meta的生态系统内进行开发（而不是像典型的开源软件那样允许不受限制的使用和修改）。Meta还对LLaMA模型的使用施加了商业限制。

正如开放基础设施基金会首席运营官Mark Collier在[四月的一篇文章](https://thenewstack.io/open-source-has-a-definition-lets-get-serious-about-defending-it/)中所说，“Meta的自定义许可证通过限制使用和创建衍生作品的能力，违反了当前开源定义以及OSI社区针对AI的任何最终成果的多个原则。”

为了澄清情况，开放源代码倡议组织(OSI)在十月发布了[其期待已久的开源AI定义](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/)的候选版本1。正如TNS编辑Heather Joslyn所指出的那样，OSI文件建议将术语“开源”用于其AI系统的组织“共享数据（如果可共享），以及用于训练和运行系统的源代码和模型参数”。

## 结论

2024年，我们观察到AI软件（特别是面向开发人员的AI编码工具）日趋成熟，自动化（AI代理）的推动，小型模型和本地托管LLM的出现，以及对什么是或不是开源的一些澄清（尽管这场辩论将持续到新年）。

今年也证明成为一名AI工程师是一个可行的职业选择——特别是如果你想比GitHub Copilot或Cursor等工具允许的更深入地研究AI。
