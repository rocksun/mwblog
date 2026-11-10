![](https://cdn.thenewstack.io/media/2026/11/5d1eee3e-blog-header-visual-1024x576.png)

Meta 于周一推出了 [Muse Ember](https://research.meta.ai/blog/muse-ember)，这是其 Muse 模型家族中体积更小、效率更高多模态成员。

该公司显然采取了与其他前沿实验室相似的策略，即推出一个包含各种模型的家族，涵盖从专注的高容量任务（如 OpenAI 的 GPT-6 Luna 和 Anthropic 的 [Claude Haiku 5.5](https://thenewstack.io/anthropic-claude-haiku-5-5/)）到前沿智能（如 OpenAI 的 GPT-6 Astra、Anthropic 的 Claude Fable 5.1，以及最近推出的 Meta 的 [Muse Wonder Full](https://thenewstack.io/muse-wonder-claude-fable/)）。正如其竞争对手一样，Meta 将这款较小的模型定位为用于执行读取文件、运行测试和进行针对性修复等智能体子任务，而由像 Muse Wonder 这样更大的模型来进行规划。

Muse Ember 可在 Muse Code 以及通过模型 ID `muse-ember-1.0` 的 Meta Model API 中使用。鉴于 Meta 过去对其他 Muse 模型采取了相同的做法，它很可能很快也会在 OpenRouter 等服务以及新云服务商（neoclouds）上架。

与以往的 Muse 模型发布一样，Meta 对 Ember 的模型权重保持保密。

Ember 是 Meta 对小型、高性价比模型的诠释，至少在基准测试方面，它是一个强有力的竞争者。

![](https://cdn.thenewstack.io/media/2026/11/7ce96132-intelligence-vs.-cost-per-task-lm-1024x576.png)





图片来源：Meta。

在最大推理能力下，根据 [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) 的数据，Meta 将 Ember 的每个任务成本定在约 0.14 美元，相比之下 Haiku 为 0.41 美元，Luna 为 0.15 美元。Ember 以大约三分之一的成本追平了 Haiku 的四舍五入得分，并且以每个任务便宜约一美分的价格获得了高于 Luna 的分数。

在 xhigh（Meta 图表中显示的另一个 Ember 设置）下，该模型的得分约为 34，每个任务成本约为 0.12 美元。

## Muse Ember 定价

Ember 拥有 100 万 Token 的上下文窗口，并支持高达 512K 的输出 Token，其定价为每百万输入 Token 0.10 美元、每百万缓存输入 Token 0.004 美元以及每百万输出 Token 0.50 美元。这些输入和输出费率与 [GPT-6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/) 和 Claude Haiku 5.5 在其标准短上下文价格下的费率相匹配。这两者在此类费率下的缓存输入 Token 费用均为每百万 0.01 美元，对于更长的提示词则价格更高。Ember 可在 Muse Code 以及通过 Meta Model API 作为 `muse-ember-1.0` 使用，并支持 Responses API。

## 中国竞争对手对比

虽然 Meta 没有在图表中将新模型与诸如 [DeepSeek V4.1 Flash 1017](https://thenewstack.io/deepseek-flash-haiku-test/)、Z.ai 的 GLM-5.3 Flash 和 MiniMax M3.1 Flash 等中国竞争对手直接进行比较，但 Ember 的价格低于这三者所列出的未缓存输入费率。它也低于 DeepSeek 的直接非高峰期价格以及 MiniMax 所列出的输出价格，并与 GLM 持平。DeepSeek 的非高峰期缓存命中率略低，为每百万 Token 0.003 美元。

例如，在 Artificial Analysis 的智能指数上，Ember 在最大推理能力下得分为 36，而 DeepSeek V4.1 Flash 1017 为 33，MiniMax 为 29，GLM 为 28。与此同时，OpenAI 的 GPT-6 Luna 在同一基准测试中得分为 28，而 Haiku 达到 36，两者均处于最大推理能力状态。

## Muse Ember 对比 Muse Spark

Meta 自己的 [Muse Spark 1.3](https://thenewstack.io/muse-spark-1-3-gemini/) 在最大推理能力下得分为 37，在比较中使用的标准 API 费率下，每个任务成本为 2.39 美元。Meta 还提供了一个 Spark 贡献者层级（Spark Contributor tier），在该层级中它利用请求来改进其产品。该层级与 Ember 的未缓存输入价格相匹配，每百万输出 Token 收费 0.20 美元。

![](https://cdn.thenewstack.io/media/2026/11/8b1b16ed-muse-ember-and-muse-spark-1.3-comparison-lm-1024x409.png)





图片来源：Meta。

Meta 报告称，在其用于衡量个人和知识工作的“个人超智能指数”（Personal Superintelligence Index）上，该模型领先于 Haiku 和 Luna。Ember 表现不佳的一个基准测试是 FrontierCode 2.0，该测试评估仓库维护者是否会合并智能体的更改。Ember 的得分为 27.2%，而 Haiku 为 34.9%，DeepSeek 为 28.5%。Spark 1.3 的得分为 23.1%。

![](https://cdn.thenewstack.io/media/2026/11/77e246a3-muse-ember-evaluation-results-lm-921x1024.png)





Meta Muse Ember 基准测试。图片来源：Meta。

## OSWorld 上的计算机使用

Ember 可以接受文本、图像、音频和视频作为输入，Meta 表示它可以根据截图操作桌面应用程序。

在 [OSWorld 2.1](https://osworld-v2.xlang.ai/#leaderboard) 上，它获得了与 Haiku 几乎相同的部分得分（partial-credit score），分别为 69.5% 对 68.9%，但它彻底完成了更多的任务，为 33.8%，而 Haiku 为 27.8%，Luna 为 17%。在另一次 OSWorld 2.1 运行中，Spark 1.3 获得了与 Ember 几乎相同的部分得分，并完成了 39.25% 的任务。

Meta 表示，新模型是其使用更大的 Muse Wonder Full 模型训练的第一款模型。这类似于该公司之前使用 Muse Wonder 来训练专门模型的做法，这些模型已开始在其 [Muse 个人智能体和 Meta AI](https://thenewstack.io/meta-muse-specialized-models/) 中推出。

文章 [Meta launches Muse Ember to take on Claude Haiku and GPT-6 Luna](https://thenewstack.io/meta-muse-ember-launch/) 最初发布在 [The New Stack](https://thenewstack.io)。