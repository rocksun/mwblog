
<!--
title: 更好的 LLM 代理质量：通过代码生成和 RAG
cover: https://cdn.thenewstack.io/media/2024/11/246af3fb-robot.png
-->

我们分享在构建大型语言模型 (LLM) 代理过程中的见解和经验。

> 译自 [Better LLM Agent Quality Through Code Generation and RAG](https://thenewstack.io/better-llm-agent-quality-through-code-generation-and-rag/)，作者 Junhwi Kim; Jack Snowdon。

[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms) 的兴起正在改变公司实现对其平台自然对话访问的方式。通过将 LLM 与各种工具（例如计算器、搜索引擎或 [数据库](https://thenewstack.io/data/)）集成，我们可以自动化各种任务。这些代理可以选择最适合给定问题的服务或 API，并使用正确的设置和参数来使用它。

我们构建了自己的 LLM 驱动的代理系统 [PromptAI](https://thenewstack.io/improving-llm-output-by-combining-rag-and-fine-tuning/)，将用户直接连接到我们的运营数据，使数据洞察更容易获得。它允许用户通过聊天界面交互式地探索大量的时间序列数据，并根据 Conviva 广泛的知识库提供可操作的见解建议。

![](https://cdn.thenewstack.io/media/2024/11/d0246072-image3a-867x1024.png)

我们很高兴分享我们在构建 LLM 代理过程中的见解和经验，希望它们可以使其他构建 LLM 代理的人受益。

**关键要点如下：**

* **代码作为 API 和 LLM 之间的接口，而不是 JSON：** 尽管大多数 API 需要 JSON 或其他序列化格式作为接口，但我们发现提示 LLM 编写 [Python](https://thenewstack.io/what-is-python/) 代码可以提高准确性。这是因为 LLM 在编写代码方面比 JSON 更流畅，并且代码更适合表达复杂参数值的复杂推理。
* **使用检索增强生成 (RAG) 提高 API 调用的准确性：** 当 API 参数具有高基数时，[使用 RAG](https://thenewstack.io/5-bottlenecks-impacting-rag-pipeline-efficiency-in-production/) 进行参数选择可以减少 LLM 必须考虑的值的空间。这种方法减少了输入上下文长度，从而提高了准确性和效率。


## LLM 编写代码以使用工具

通常，大多数 API 要求输入采用机器可读格式，例如 JSON。例如，要回答“过去三天有多少用户活跃？”之类的问题，LLM 应生成如表 1 所示的 JSON 有效负载。根据给定的问题，LLM 遵循每个 API 接口的规范来确定每个参数的正确值。然而，直接生成这种序列化格式会带来独特的挑战。

*表 1：JSON 有效负载示例*

第一个挑战是 LLM 在生成结构化输出（例如 JSON）方面的准确性较低。如果有效负载的模式很复杂，LLM 经常会虚构键、使用不正确的类型值或添加不必要的尾随逗号，从而导致语法错误。

另一个挑战是找到参数的正确值需要多个推理步骤。例如，要计算“from”和“to”参数的正确值，LLM 必须知道当前日期时间值，然后从当前日期减去三天才能获得“from”的正确值。这就像试图在没有日历的情况下确定三天前的日期。它涉及跟踪日期、月份，甚至要考虑不同月份的长度。然而，在生成最终 JSON 输出时，LLM 必须一步完成此计算，这具有挑战性且准确性较低。

这些挑战提出了一个重要的问题：LLM 和 API 之间最合适的表示或接口是什么？

在 PromptAI 中，我们使用代码作为 LLM 和 API 之间的接口，利用 LLM 对编写代码的熟悉程度。与 JSON 等序列化数据格式不同，代码使 LLM 能够表达更复杂的推理并执行复杂的任务。

![图 1：使用 Python 代码作为接口的输入提示和输出示例](https://cdn.thenewstack.io/media/2024/11/0775fd9f-image2x-1024x460.png)

图 1：使用 Python 代码作为接口的输入提示和输出示例
使用代码作为接口的另一个好处是，大型语言模型 (LLM) 更熟悉编写代码，而不是直接以 JSON 等格式输出结构化数据，因为在 JSON 中很容易出现语法错误，例如尾随逗号。生成所需的 JSON 结构有时需要额外的微调。然而，LLM 已经在大规模代码库上进行了训练，可以有效地编写代码。这使得代码成为 API 集成的低开销、高精度的选择，尤其是在使用像 CodeLlama 这样的专用编码 LLM 时。

## 使用 RAG 定义有效参数值

代码充当 LLM 和数据检索工具之间强大的接口，这种交互的一个关键要素是确保 LLM 为特定任务选择有效的输入值。在 Python 中，Enum 模块对于定义变量可以取的有限有效值集特别有用。这有助于我们约束由指标和维度组成的有效输入空间。

在 Conviva，Python 的 Enum 用于将 LLM 的输入选择限制为有效的指标和维度。然而，这种 Enum 设置可能会变得笨拙，因为大量的潜在值可能会超过 token 限制并引入不相关的选项，从而导致效率低下。许多可能的值与给定查询无关，这些无关的值会消耗不必要的 token。为了优化这一点，我们可以智能地减少提供给 LLM 的值，只关注与上下文相关的值，从而在涵盖所有有效可能性的同时节省 token。

检索增强生成 (RAG) 提供了一种通过从外部来源获取相关信息来扩展 LLM 功能的有效方法。在 Conviva 的案例中，我们使用 RAG 动态填充 Enum 的值，进一步优化 LLM 和我们庞大数据之间的交互。例如，如果用户要求特定设备类型的活跃用户，RAG 可以仅从向量数据库中检索相关的设备选项，确保 LLM 使用准确的、特定于上下文的数据，而不会被无关的值淹没。

为了启用 RAG，我们使用向量数据库，它存储 Enum 值及其任何相关元数据的嵌入，例如值的描述。向量数据库允许我们根据向量相似性和传统的语义搜索进行高度可定制的向量搜索。通过从向量数据库中检索候选值，我们确保 LLM 使用经过精炼的相关可能值子集，而不是被选项淹没。

在认知处理方面，我们可以将其视为类似于类型 1 和类型 2 思维范式。RAG 充当快速、类型 1 的思考者，检索快速但相关的结果，而 LLM 充当较慢、更彻底的类型 2 思考者，分析候选者以选择正确的值。这种两步法提高了准确性。事实上，我们观察到 LLM 单独猜测错误的实例，但是通过 RAG 增强的系统缩小了选择范围，从而识别出了正确的值。

## 多个代理的协作

构建代理的另一个挑战是 LLM 必须能够解释这些工具的结果并向用户提供有意义的解释。这需要 LLM 额外的上下文和知识。我们将 API 集成和 RAG 用于知识库，以提高响应的质量。如前所述，我们使用专门用于编码的 CodeLlama 来提高 API 集成的准确性。然而，为了生成全面的最终响应，像 Llama 这样的更通用的 LLM 由于其更广泛的理解而提供了更好的描述。通过结合不同模型的优势，我们可以最大限度地提高 API 调用的准确性和响应的质量。

## 结论

LLM 代理通过利用现有的 API 或服务，在自动化各种人类任务方面具有巨大的潜力。将 LLM 与 API 集成时，用众所周知的编程语言来构建问题通常比使用 JSON 或其他数据格式更有效。RAG 的集成通过动态提供相关上下文进一步增强了系统，从而可以精确选择 API 的参数。通过结合这些技术，我们提高了 LLM 代理 PromptAI 的准确性，使其能够以对话方式与数据进行交互。我们希望我们的经验和见解可以为其他致力于构建 LLM 代理的人员提供宝贵的指导。

*Haijie Wu 也对本文做出了贡献。*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.](https://youtube.com/thenewstack?sub_confirmation=1)