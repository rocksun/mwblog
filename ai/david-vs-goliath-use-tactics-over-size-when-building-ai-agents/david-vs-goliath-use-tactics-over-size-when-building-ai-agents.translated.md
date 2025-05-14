# 大卫对歌利亚：构建 AI Agent 时，战术比规模更重要

![Featued image for: David vs. Goliath: Use Tactics Over Size When Building AI Agents](https://cdn.thenewstack.io/media/2025/05/d79559f1-artem-sapegin-b18trxc8upq-unsplash-2-1024x683.jpg)

[Artem Sapegin](https://unsplash.com/@sapegin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/turned-on-macbook-air-displaying-coding-application-b18TRXc8UPQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上发布。

近几个月来，由大型语言模型（LLM）驱动的通用浏览器 Agent 取得了显著进展。OpenAI 和 Anthropic 等行业领导者分别发布了这些 Agent，Operator 和 Computer Use，供公众使用。这些浏览器工具展示了令人印象深刻的功能，从预订餐厅到回答各种复杂问题。

通用浏览器 Agent 尽管具有灵活性，但无法执行结构化、可重复的业务任务。精确的分析、自动化的工作流程和可靠的[数据](https://thenewstack.io/automating-context-in-structured-data-for-llms/)丰富严重依赖于一致的结构化数据。如果没有可预测的结构，提取的数据会迅速变得不可靠，严重限制了其对业务和技术应用程序至关重要的下游流程的实际价值。

## 为什么通用 Agent 难以扩展

当应用于大规模数据提取任务时，一些[关键问题限制了通用 AI Agent 的有效性](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/)，例如 OpenAI 的 Operator 和 Claude 的 Computer Use：

**缺乏结构：** Agent 通常产生不一致结构化的输出。由于大多数 Agent 的构建都以问答为主要重点，因此它们的输出往往是段落格式或组织松散。
**网站覆盖范围有限：** 用于评估这些 Agent 的现有基准通常仅包括一小部分网站，通常是模拟或严格控制的环境。因此，通用 Agent 难以适应真实世界网站的复杂性、可变性和混乱性。
**模型惰性：** Open AI Operator 或 Claude Computer Use 经常在仅提取部分数据（例如，单个列表页面）后过早停止执行。例如，对于具有多个数据页面的特定任务，这些模型会将部分信息保存在第一页上并终止执行。

## 关键见解：所有问题都有结构

在 [Bardeen](https://www.bardeen.ai/)，我们构建 Web Agent 的方法从根本上不同。我们没有通过构建越来越大、计算成本越来越高的模型来与大型模型提供商正面竞争，而是选择利用真实世界 Web 任务的内在结构。通过为团队和企业客户构建数百万个自动化，我们了解到，许多关键业务任务（例如提取职位发布、监控公司博客更新或分析客户评价）在很大程度上依赖于结构化数据。

此外，我们观察到，呈现此数据的网站始终如一地使用重复的 HTML 结构。

通过识别和利用这种底层结构（无论是在业务问题本身还是在呈现数据的网站中），我们意识到，我们可以构建一个效率更高、更准确、更可扩展的 AI Agent，而无需诉诸蛮力计算。

## BardeenAgent：构建浏览器 Agent 的新方法

我们的解决方案 BardeenAgent 通过两步执行过程来实现这种结构化方法：

**捕获提取结构（一次）**

首先，BardeenAgent 导航到网页上所需的数据，并使用 LLM 识别和记录如何提取单个数据项。此步骤生成强大的 CSS 选择器和一个结构化的提取脚本，本质上是创建了一个可重用的“配方”来捕获类似的数据。

**精确重放（多次）**

BardeenAgent 不是为每个后续数据项重复调用昂贵的 AI 推理，而是在[多个页面或数据](https://thenewstack.io/stream-data-across-multiple-regions-and-clouds-with-kafka/)点上重放此记录的提取脚本。这种方法大大降低了计算开销并提高了可靠性。

**为什么有效：通过可重用性提高效率**

这种结构化方法之所以强大，是因为它可以确保以下几点：
**一致性**：结构化脚本可靠地提取数据，确保一致的输出格式。

**可扩展性**：一旦捕获了结构，提取就可以[快速有效地扩展到成百上千个数据](https://thenewstack.io/five-strategies-for-securing-and-scaling-streaming-data-in-the-ai-era/)点。

**成本和时间效率**：减少 AI 调用意味着大幅降低成本并加快数据提取速度。

## 实际应用和结果：WebLists 介绍

为了评估 BardeenAgent 在提取结构化数据方面的有效性，我们评估了 [LLM 浏览器代理在我们新的基准](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/) WebLists 上的表现，该基准由真实企业客户提出的用例组成。 这包括以下场景：

- 跟踪
  **招聘信息**，以识别竞争对手的增长或招聘趋势
- 监控
  **公司博客**和产品更新，以准备知情的销售推广。
- 提取
  **客户评价**，以进行强大的竞争分析。

在 WebLists 基准上评估 BardeenAgent 与其他方法时，结果很明显：我们的评估表明，BardeenAgent 的结构化方法明显优于现有的最先进的代理，包括 [Wilbur](https://www.bardeen.ai/posts/wilbur-adaptive-in-context-learning-for-robust-and-accurate-web-agents)（Bardeen 之前发布的代理）、[Agent-E](https://www.emergence.ai/blog/agent-e-sota) 和 [Perplexity](https://www.perplexity.ai/)。 BardeenAgent 实现了 66.2% 的召回率，**是最佳方法性能的两倍多**。 最重要的是，结构化方法也直接转化为成本效率：与竞争解决方案相比，BardeenAgent **每次提取行的成本大约降低了 3 倍**。

## 一种不同的方法

通用 AI 令人印象深刻，但是当结果的结构和准确性对您的业务至关重要时，您需要一种不同的方法。 BardeenAgent 通过利用 Web 数据的固有结构来弥补这一差距，使企业和研究人员能够高效、可靠地大规模提取有价值的见解。

如果您想超越通用 AI 的局限性并利用结构化 Web 智能，请阅读我们的完整技术论文和[此处的博客文章](https://www.bardeen.ai/blog)。

如果您有兴趣测试您自己的代理的比较情况或进一步探索这种方法，请通过 ml@bardeen.ai 与我们联系。 我们很高兴与更广泛的 AI 社区合作并为其提供支持。

*TNS 的所有者 Insight Partners 也投资了 Bardeen。 因此，Bardeen 作为贡献者享有优先权。*

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)