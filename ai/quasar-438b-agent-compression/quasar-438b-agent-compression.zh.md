**一个拥有4380亿参数的推理模型**，在优先考虑速度时并非显而易见的选择。Multiverse Computing 正押注通过压缩技术使其成为可能。

周三，这家西班牙公司发布了 Quasar 438B，这是其首个大规模模型，也是专门为编码和企业智能体设计的系统。Quasar 在 Artificial Analysis 的智能指数（Intelligence Index）上获得了 43 分，在 Terminal-Bench v2.1 上获得了 69.3 分，而 Artificial Analysis 目前记录其输出速度约为每秒 183 个 token。Multiverse 将 Quasar 定位为智能指数得分最高的欧洲模型，表现优于 Mistral Medium 3.5（30 分）和 NVIDIA Nemotron 3 Ultra（38 分）。

> Multiverse 押注一个 4380 亿参数的模型可以足够快速且经济，足以支持需要反复推理、调用工具并检查结果的智能体。

这让 Quasar 处于一个有趣的中间地带。它在编码性能上无法与最强的模型相匹敌，但 Multiverse 押注 4380 亿参数的模型可以足够快速且经济，足以支持那些反复推理、调用工具并检查结果的智能体。

该模型具有 100 万个 token 的上下文窗口，提供英语和西班牙语版本，可通过 Multiverse CompactifAI API 进行访问。

## 压缩声明，细节缺失

Multiverse 构建了 CompactifAI 来缩小大型 AI 模型，使其在运行时需要更少的内存和计算资源。该公司表示，它可以在仅损失少量准确性的情况下将模型规模缩小 80% 到 95%，但尚未披露 Quasar 被压缩了多少，或者它是从哪个原始模型开始压缩的。

7 月，Multiverse 宣布获得 5.7 亿美元的 C 轮融资，用于扩展其压缩模型库并将该技术商业化。Quasar 是目前为止对该方法进行的规模最大的测试。

Multiverse 尚未说明运行 Quasar 需要什么硬件，或者压缩在多大程度上减少了其内存和计算需求。这对智能体来说很重要，因为智能体在完成任务之前可能会反复调用该模型和其他工具。

> Multiverse 尚未说明运行 Quasar 需要什么硬件，或者压缩在多大程度上减少了其内存和计算需求。

## 编码基准测试显示权衡

在 Multiverse 的比较中，Quasar 的 Terminal-Bench v2.1 得分为 69.3，使其领先于 Mistral Medium 3.5，但仍远远落后于最顶尖的系统，而 Claude Opus 5 在该基准测试中获得了 89.1 的最高分。

Multiverse 正在推广 Quasar 用于软件工程、技术副驾驶（copilots）、研究和工作流自动化。其 100 万 token 的上下文窗口为智能体处理大型代码库并在任务进展过程中保留信息提供了空间，尽管处理更多的上下文也需要更多的计算资源。这在编码中尤为重要，因为[即使是通过了每一项测试的代码，如果它丢失了之前的内容，仍然会绊倒下一个 AI 智能体](https://thenewstack.io/go-language-ai-agents/)。

## 吞吐量之外的智能体延迟

Artificial Analysis 发现，Quasar 开始响应的时间约为 1.1 秒，并能在约 15.3 秒内生成包括推理在内的 500 个 token 的响应。这些数字很快，但智能体在任务过程中还必须等待工具、处理不断增长的上下文并进行重复的模型调用。[智能体工具层本身](https://thenewstack.io/ard-agent-discovery-specification/)仍在赶上这些模型的需求。

> 这些数字很快，但智能体在任务过程中还必须等待工具、处理不断增长的上下文并进行重复的模型调用。

## 专有模型，悬而未决的问题

Quasar 是专有的，只能通过 Multiverse 的 API 使用，因此开发人员无法检查权重或在自己的硬件上运行它。目前，这也使得很难知道 Multiverse 报告的速度是否会延续到日常的智能体使用中。

Quasar 的出现正值[欧洲 AI 公司正在建立更多自己的模型和计算基础设施](https://thenewstack.io/mistral-third-party-open-models/)，而不是依赖美国超大规模云计算厂商之际。Multiverse 走了一条不同的路线，利用压缩技术使 4000 亿参数以上的模型运行成本更低、速度更快。下一步是观察它在基准测试中的表现如何。