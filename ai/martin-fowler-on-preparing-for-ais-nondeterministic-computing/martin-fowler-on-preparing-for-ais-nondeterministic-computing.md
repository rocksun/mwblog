<!--
title: 马丁·福勒：如何驾驭AI非确定性计算
cover: https://cdn.thenewstack.io/media/2025/12/fbb39846-vintage-blue-robot-with-a-shadow-by-matthew-henry-from-burst-via-shopify-scaled-1.jpg
summary: Martin Fowler称AI为最大编程范式转变。LLM是非确定性计算，擅长理解遗留系统和快速原型，但高级编程需谨慎，并应理解其非确定性容差。
-->

Martin Fowler称AI为最大编程范式转变。LLM是非确定性计算，擅长理解遗留系统和快速原型，但高级编程需谨慎，并应理解其非确定性容差。

> 译自：[Martin Fowler on Preparing for AI's Nondeterministic Computing](https://thenewstack.io/martin-fowler-on-preparing-for-ais-nondeterministic-computing/)
> 
> 作者：Joab Jackson

[Martin Fowler](https://www.martinfowler.com/)，Thoughtworks 首席科学家，以及面向对象编程领域的资深专家，将人工智能（AI）视为他职业生涯中所见过的最大编程范式转变。

在 [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/) 主持的 [Pragmatic Engineer](https://www.youtube.com/@pragmaticengineer) 播客采访中，Fowler 承认关于人工智能，“我们仍在学习如何驾驭它。”

对于业界来说，最接近的类比可能是从汇编语言的转变。

汇编语言编写起来非常繁琐，大部分工作都涉及在寄存器之间移动内存值。这就是为什么转向更高级的编程语言（如 [COBOL](https://thenewstack.io/20-years-in-the-making-gnucobol-is-ready-for-industry/) 和 [Fortran](https://thenewstack.io/how-john-backus-fortran-beat-machine-codes-priesthood/)）对程序员来说是如此的幸事。

Fowler 说：“至少在像 Fortran 这样相对较弱的高级语言中，我可以编写条件语句和循环等东西。”

这些新语言比硬件本身具有更高层次的抽象。

他说，对于大型语言模型（LLM），这是一种“相似程度的思维转变”。

## 确定性计算与非确定性计算

但 LLM 并非是另一种抽象，而是完全不同类型的计算。

确切地说，LLM 是一种非确定性计算形式，它与我们今天认为是“计算”的一切（即确定性计算）具有不同的特征。

确定性计算是严格的二进制。一个计算要么正确，要么错误。如果它不正确，我们可以调试代码找出错误所在。

非确定性计算则模糊不清。LLM 可能在某个时刻给出一个答案，而在另一个时刻给出完全不同的答案。它生成的答案依赖于[统计推理](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/)，这是一组建立在二进制数学基础之上的概率，但并非万无一失。

他说，这完全改变了你思考计算的方式。

## AI 的应用领域

[Thoughtworks](https://www.thoughtworks.com/about-us) 是一家技术驱动的咨询公司，因此一直在关注 AI 的成功应用方式。

根据 Fowler 的说法，其中一个用例是快速制作原型，这部分得益于[氛围编程](https://thenewstack.io/why-there-might-be-something-to-vibe-coding-after-all/)的兴起。在这里，你可以比以前“更快地”探索一个想法。

但真正的杀手级应用是利用 AI 帮助[理解遗留系统](https://thenewstack.io/agent-infused-mongodb-tackles-application-modernization/)。在该公司最新一期关于新兴技术的[年度雷达报告](https://www.thoughtworks.com/en-us/radar)（第 33 期）中，使用生成式人工智能（GenAI）来现代化遗留系统是唯一获得该公司最高“采用”评级的 AI 技术。

对于试图现代化旧系统的客户，Thoughtworks 创建了一个例程，它基本上可以语义分析代码库，将结果放入[图数据库](https://thenewstack.io/common-uses-cases-for-graph-databases/)中，然后可以通过[检索增强生成（RAG）过程](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)进行查询，以理解应用程序的运行方式。

Fowler 说：“如果你正在对遗留系统进行任何工作，你应该以某种方式使用 LLM 来帮助你。”

## AI 较难处理的问题

然而，尽管 LLM 可以帮助我们理解遗留代码，但它们能否以安全的方式修改这些代码则是另一个问题。

LLM 在高级编程方面仍然很棘手。Fowler 说，在这种情况下，你必须将 AI 工作分解成非常“薄的切片”，并非常仔细地审查所有内容。

Fowler 说：“你必须将每个切片都视为来自一个相当靠不住的合作者的[拉取请求]，他在代码行数意义上的生产力很高，但你知道你不能信任他们所做的任何事情。”

尽管如此，以这种方式使用 AI 可以节省开发人员的时间，尽管可能不如[拥护者所声称的](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/)那么多。

他特别建议我们“想出一种更严谨的方式”来与 LLM 沟通，[以获得更好的结果](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning/)。[领域驱动设计](https://thenewstack.io/celebrating-20-years-of-domain-driven-design-ddd-and-eip/)（DDD）和[领域特定语言](https://thenewstack.io/rethinking-data-integrity-why-domain-driven-design-is-crucial/)可能提供前进方向。

## AI 与机械工程的相似之处

Fowler 指出，结构工程的实践也有助于更好地衡量在哪里使用 AI。

“我妻子是结构工程师。她总是从容差的角度思考：‘除了数学告诉我的之外，我还得多做多少额外的工作，因为我需要它来满足容差？’”Fowler 说。

正如我们知道一座混凝土桥能承受多少重量一样，LLM 也应该附带描述其支持精确度水平的指标。

他问道：“我们必须处理的非确定性容差是多少？”了解这一点，软件开发人员就会知道在哪里“不要过于冒险”。

Fowler 向软件开发人员推荐的一本有助于思考非确定性的书是 Daniel Kahneman 的[《思考，快与慢》](https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow)。

Fowler 说：“他在尝试让你对数字产生直觉，并发现我们在从概率和统计的角度思考时所犯的许多错误和谬误方面做得非常出色。”

一如既往，Fowler 是一位雄辩的演说家，在这次采访中，他对各种主题都有独到的见解，包括重构、敏捷流程、企业中的 LLM、企业应用模式，当然，还有每个面向对象程序员最喜欢的语言 [Smalltalk](https://thenewstack.io/the-big-impact-of-smalltalk-a-50th-anniversary-retrospective/)。

在此观看完整的访谈：[视频](https://youtu.be/CQmI4XKTa0U) 。