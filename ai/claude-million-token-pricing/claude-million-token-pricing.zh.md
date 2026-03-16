Anthropic [周五宣布](https://claude.com/blog/1m-context-ga)，[Claude Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 和 [Claude Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/) 的100万个token上下文窗口现已全面上市，标准定价取代了之前当提示符超过一定大小阈值时生效的高级长上下文费率。

该公司于二月在数周内相继推出了这两款模型。Claude Opus 4.6 是 Anthropic 的旗舰模型，适用于需要在大型内部数据集上进行持续推理和复杂编码任务的企业工作负载。与此同时，Claude Sonnet 4.6 是该公司更高效的通用模型，专为高吞吐量的开发者使用和需要强大推理性能但成本低于 Opus 的生产应用而设计。

这两款模型都配备了100万个token的上下文窗口——这个限制允许开发者将大量信息放入单个提示符中。这可以包括整个代码库、冗长的研究论文、法律文件，或者需要AI系统一起分析的大量内部文档。

然而，有一个重要的注意事项：尽管这些模型在技术上支持接近100万个token限制的提示符，但超过大约20万个token的请求将按照更高的“长上下文”定价层级计费，从而将整个请求移入高级费率区间。

Anthropic 现已取消了这种定价区分。

在新安排下，无论提示符大小如何，请求都将按相同的每token费率计费。现在，包含数十万个token的提示符与小得多的请求采用相同的每token费率定价。

## 迈向100万个token之路

在过去两年中，Anthropic 迈向百万token上下文窗口的举措分阶段展开。

早期的 Claude 模型以20万个token的限制推出，这在当时已经是最大的公开可用上下文窗口之一。当 Anthropic 在 [2024年初推出 Claude 3 系列](https://www.anthropic.com/news/claude-3-family) 时，该公司指出这些模型在技术上能够处理超过100万个token的输入，尽管对这些更大上下文的访问最初仅限于“特定用例”，并且需要申请。

100万个token窗口的首次公开发布[于2025年8月到来](https://thenewstack.io/anthropics-claude-sonnet-4-model-gets-a-1m-token-context-window/)，当时 Anthropic 在 Claude Sonnet 4 中引入了这一功能。这一飞跃比早期的 Sonnet 模型增加了五倍，尽管其定价结构与提示符大小挂钩。

值得注意的是，Anthropic 在某些方面正在迎头赶上：[Google](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) 和 [OpenAI](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) 都已经推出了能够处理接近100万个token的提示符的模型。

尽管如此，百万token里程碑已成为AI模型提供商之间越来越引人注目的基准。更大的上下文窗口允许模型处理更长的文档或更广泛的数据集，而无需将任务分解为多个步骤。

在当前定价下，Claude Opus 4.6 的输入 token 约为每百万 $5，输出 token 约为每百万 $25；而 Claude Sonnet 4.6 的输入 token 约为每百万 $3，输出 token 约为每百万 $15。此前，一旦提示符超过长上下文阈值，Sonnet 的输入定价从约 $3 上升到约 $6 每百万 token，而 Opus 的输入定价从约 $5 上升到约 $10 每百万 token。输出 token 定价在高级层级下也有所上涨。

Anthropic 表示，100万个token的上下文窗口可在 Claude Platform 本机使用，并通过 Amazon Bedrock、Google Cloud 的 Vertex AI 和 Microsoft Foundry 提供。运行 Opus 4.6 的 Claude Code Max、Team 和 Enterprise 用户也将默认获得完整的100万个token上下文窗口。

## 更便宜的长提示符给开发者带来了什么改变

对于开发者而言，取消长上下文附加费可能会影响应用程序的设计方式。

一种流行的降低成本的机制是尽量减少一次性发送给模型的信息量。检索系统——它只提取最相关的数据片段——成为一种常见的架构模式，部分原因是发送非常大的提示符可能很快变得昂贵。

随着高级层的消失，这种限制也不复存在。开发者仍然可以依赖检索系统来管理 token 使用，但当更广泛的上下文有用时，他们也可以选择直接向模型发送更大的信息主体。

这可以使某些工作流程变得更简单。开发者有时可以将更大一部分数据放入单个提示符中，并要求模型对其进行推理，而不是将文档分块成更小的片段或协调多次模型调用。

对于AI原生编码工具而言，这种方法尤其有吸引力。一个拥有大型上下文窗口的模型可以一次性检查更多的代码库——包括多个文件、文档和以前的对话——这可以改进诸如调试、代码重构或生成拉取请求等任务。

Techstars 联合创始人兼风险投资家 Brad Feld 表示，更大的上下文窗口可以消除开发者之前为管理有限上下文大小而需要的某些工程变通方法。

“Claude Code 的1M token上下文窗口完全改变了工程计算，”Feld 在一篇 LinkedIn 帖子中[写道](https://www.linkedin.com/posts/bfeld_the-1m-token-context-window-for-claude-code-activity-7438444810929336320-ExTT/)。“我构建了四个 markdown 状态机，总计4700行，用于管理我的开发工作流程——从工单到部署。大部分复杂性是由于200K上下文限制造成的。”

他写道，有了更大的窗口，许多这些机制变得不必要。

“有了1M token，可靠性很大程度上通过足够的空间得到了解决。限制转移到物理时钟速度——而速度来自于并行性。”

翻译过来就是，模型现在有足够的内存来跟踪长任务，主要瓶颈变成了它处理所有信息的 F速度。

值得强调的是，取消附加费并不意味着大型提示符是免费的。token 使用量仍然会随着输入大小的增加而增加，开发者必须权衡此成本与其他架构方法。

但通过消除定价阈值，Anthropic 使长上下文工作负载更容易进行实验，并可能更容易部署到生产系统中。