![清理中](https://cdn.thenewstack.io/media/2026/11/ca5aed9f-handrush-supply-i8sfnhlttdo-unsplash-1024x724.jpg)

DeepSeek 的开源编码智能体在一个主要基准测试中失分，原因是一个通常被开发者视为良好习惯的行为：清理自己留下的痕迹。

这个问题浮出水面是因为 Hugging Face 的 harness 优化研究员 [Joël Niklaus](https://www.linkedin.com/in/joelniklaus/) 将 [DeepSeek Harness](https://huggingface.co/spaces/joelniklaus/harness-leaderboard) 加入了他的编码智能体排行榜，该排行榜对比了运行相同底层模型的十个 harness。

DeepSeek Harness 在该排行榜的五个评分评估中在统计上并列第一，然而仅在 Terminal-Bench 上它就跌至第六位，因为其一个内置行为导致它未能完成竞争智能体成功完成的任务。

> DeepSeek Harness 在该排行榜的五个评分评估中在统计上并列第一，然而仅在 Terminal-Bench 上它就跌至第六位……

“一个习惯解释了大部分差距，”[Niklaus 在 X 上写道](https://x.com/joelniklaus/status/2120540528886603949)，指的是该智能体较弱的 Terminal-Bench 表现。

## 一个爱干净的习惯适得其反

DeepSeek Harness 在任务结束时会关闭后台进程，这对于需要这些进程持续运行的三个 Terminal-Bench 任务来说是个问题。

Niklaus 发现，使用 DeepSeek-V4.1-Flash 和 GLM-5.3-Flash 时，DeepSeek Harness 在 36 次尝试中仅通过了 2 次，而 OpenCode、Pi 以及 Nous Research 的 Hermes Agent 在这些相同的任务中全部通过了 36 次。

> DeepSeek Harness 在 36 次尝试中仅通过了 2 次……而 OpenCode、Pi 和 Nous Research 的 Hermes Agent 在这些相同的任务中全部通过了 36 次。

该行为使 DeepSeek Harness 的分数降低了 1.5 到 1.7 个百分点。在使用 DeepSeek-V4.1-Flash 进行高推理投入时，这足以抵消甚至超过 DeepSeek Harness 与领先者之间 1.3 个百分点的全部差距。

该[排行榜的更新日志](https://huggingface.co/spaces/joelniklaus/harness-leaderboard/blob/main/CHANGELOG.md)证实，关闭行为属于 DeepSeek Harness 本身，且结果保持不变。

DeepSeek 的[工程文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/jobs/jobs-local/README.md)将其次本地作业注册表描述为一个故意生命周期短暂的组件。“当作业应该在 harness 进程中生存并随之消亡时，请选择它，”文档指出。需要从重启中存活或跨进程运行的作业需要不同的后端。

## 相同的模型，不同的结果

Niklaus 于 11 月 5 日推出了他的[Harness 排行榜](https://huggingface.co/spaces/joelniklaus/harness-leaderboard)，此前他使用三个开源模型（DeepSeek-V4.1-Flash、GLM-5.3-Flash 和 Flint）在其最初的九个 harness 中运行了 28,849 次试验。

他在更换 harness 的同时保持了模型、提供商和推理投入的不变，而差异是巨大的。Mini-swe-agent 是一个相对简单的基于 bash 的智能体，完成了 51.4% 的任务，而 OpenClaw 的这一比例为 27.3%，尽管其他几个 harness 与领先者统计上并列。

成本的差异同样巨大。Pi 以每个解决任务 0.29 美元的成本实现了 49.4% 的解决率，而在初次评估中，OpenCode 每个解决任务的成本为 3.35 美元。Hugging Face 的联合创始人 [Thomas Wolf](https://www.linkedin.com/in/thom-wolf/) [在 X 上](https://x.com/Thom_Wolf/status/2118863053001531676)将这些发现总结为“相同的开源模型，不同的 harness => 非常不同的结果。”

*The New Stack* 已联系 DeepSeek 就这些发现寻求评论，但在截稿前未收到回复。

## 编排并不能保证成功

Y Combinator 总裁兼首席执行官 [Garry Tan](https://www.linkedin.com/in/garrytan/) 一直在使用 Claude Opus 5.5 和 GPT-6.1 Sol 进行[单独的评估](https://github.com/garrytan/g-harness-evals)。

“[Harness 在成本上的差异大于它们解决任务频率上的差异](https://github.com/garrytan/g-harness-evals?tab=readme-ov-file#what-we-found)，”研究人员写道。在多用户任务上，运行 Opus 5.5 的 OpenClaw 每个解决任务的成本大约是其他 Opus harness 的两倍，主要是因为它在每个请求中重复发送上下文。

该项目还测试了 Tan 的 gstack 工作流技能。在 46 次会话中，Opus 5.5 阅读了说明但从未遵循规定的步骤，并且尝试的成本大约高出一倍。

研究人员指出，这些任务相对简单，因此尚不清楚遵循说明是否会改善结果。这些结果证明了像测试模型一样仔细测试 harness 的必要性。

> 这些结果证明了像测试模型一样仔细测试 harness 的必要性。

这篇文章最初发布在 [The New Stack](https://thenewstack.io)，标题为 [DeepSeek 的编码智能体太爱干净，反而在基准测试中吃了亏](https://thenewstack.io/deepseek-harness-cleanup-benchmark/)。