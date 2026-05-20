<!--
title: Cursor押注低成本开发：Composer 2.5携手Kimi K2.5正式登场
cover: https://cdn.thenewstack.io/media/2026/05/25233ae1-adriandra-karuniawan-ndd8ngyai04-unsplash-scaled.jpg
summary: Cursor推出基于月之暗面Kimi K2.5的Composer 2.5，通过强化学习和大量合成数据提升了长任务处理能力。虽基准测试稍逊于顶级模型，但其极低的价格优势显著。
-->

Cursor推出基于月之暗面Kimi K2.5的Composer 2.5，通过强化学习和大量合成数据提升了长任务处理能力。虽基准测试稍逊于顶级模型，但其极低的价格优势显著。

> 译自：[Cursor bets on cheaper coding with Composer 2.5 and Kimi K2.5](https://thenewstack.io/cursor-composer-benchmarks/)
> 
> 作者：Meredith Shubel

Cursor 本周宣布 Composer 2.5 已在 Cursor 中上线，这距离 [Composer 2 发布](https://thenewstack.io/cursors-composer-2-beats-opus/) 仅过去两个月，此前 Composer 2 以极低的价格在编程基准测试中击败了 Opus 4.6。这是该公司模型发布热潮中的又一次爆发，标志着过去七个月里发布的第四款 Composer 模型。

Cursor 表示，最新版本在长时运行的编程任务、复杂指令遵循和训练效率方面带来了重大升级，同时在“沟通风格和努力程度校准”方面也进行了行为改进，但基准测试的提升能否转化为现实世界中的改进仍有待时间验证。

## 编程模型阵容中的廉价竞争者

与其前身一样，Composer 2.5 基于 [Moonshot Kimi K2.5](https://github.com/MoonshotAI/Kimi-K2.5) 构建，这是一个开源的原生多模态智能体模型，但现在其在智能和行为方面的表现应优于 Composer 2。

在[公告](https://cursor.com/blog/composer-2-5#targeted-rl-with-textual-feedback)中，Cursor 将这些改进归功于规模化训练、更复杂的强化学习（RL）以及新的学习方法。从基准测试来看，不难发现 Composer 2.5 相较于 Composer 2 的巨大跨越：在 [Terminal-Bench 2.0](https://www.tbench.ai/) 上的得分从 61.7% 提升至 69.3%，在其自有的 CursorBench v3.1 上则从 52.2% 提升至 63.2%。

虽然 Composer 2.5 尚未超越 Opus 4.7 和 GPT-5.5 的得分（除了在 [SWE-Bench Multilingual](https://www.swebench.com/multilingual.html) 上以 2% 的微弱优势超过 GPT-5.5），但它绝对让 Anthropic 和 OpenAI 感到了压力。

> 但基准测试终究只是基准测试。

![](https://cdn.thenewstack.io/media/2026/05/2e01da0c-cursor-benchmarks.webp)

图片来源：Cursor

虽然基准测试为行业主要竞争者提供了有趣的宏观对比，但它们并不能真实保证这些模型在现实世界中的表现。

正如一位 [Redditor 用户](https://www.reddit.com/r/vibecoding/comments/1tgyqoj/cursor_annonced_a_model_that_beats_opus_47_and/) 所评论的：“还没测试，但基准测试数据很疯狂。有趣的是，原始模型性能并不总能转化为实际的编程生产力。我见过很多‘更好’的模型生成的代码仍需要大量清理，或者无法正确适配项目上下文。”

> “任何在实际项目中使用过 Claude 或 GPT-4 的人都知道，基准测试中的智能程度并不等于实践中的实用性。”

相反，他们认为 Composer 2.5 的真正考验在于它处理多文件更改的能力，以及是否能保持与现有代码库的一致性：“任何在实际项目中使用过 Claude 或 GPT-4 的人都知道，基准测试中的智能程度并不等于实践中的实用性。”

## Cursor 旨在改进长时运行的智能体工作

Cursor 还表示，Composer 2.5 在长时运行的编程任务上有了显著提升。为此，公司通过定向文本反馈训练模型，以解决强化学习中棘手的信用分配（credit assignment）问题：“其核心思路是在模型轨迹中本可以表现得更好的节点上直接提供反馈。”

通过在本地上下文中构建并插入简短提示，Cursor 旨在针对特定错误进行纠正，同时保留宏观的强化学习目标。

发布仅一天，现在判断这种训练是否会产生实质性差异还为时过早，但初步的用户反馈显示，这个问题可能仍会困扰开发者。

正如一位 [Redditor 用户](https://www.reddit.com/r/cursor/comments/1tha71k/composer_25_suddenly_believes_its_in_ask_mode/?show=original) 所指出的：“Composer 2.5 开始以智能体模式工作，然后突然认为自己处于提问模式并停止工作。当我提示它继续时，它试图理解任务进度，结果只完成了正在处理的部分，却忘记了流水线中的其他所有任务。”

## 更多的合成数据训练，更多的意外奖励作弊

根据 Cursor 的说法，Composer 2.5 的合成任务训练量是 Composer 2 的 25 倍，并采用了多种方法来生成这些任务。但如此广泛的合成任务创建至少产生了一个负面副作用：意外的奖励作弊（reward hacking）。

正如 Cursor 自己承认的那样：“随着模型变得更加熟练，Composer 2.5 能够找到越来越复杂的变通方法来解决手头的任务，”例如对 Python 类型检查缓存进行逆向工程。

## 你得到的一定物有所值吗？

Composer 2.5 的成本为每百万输入 token 0.50 美元，每百万输出 token 2.50 美元。升级到“快速”档位将花费每百万输入 token 3.00 美元和每百万输出 token 15.00 美元——但智能程度是相同的。

无论更低的延迟是否值得这六倍的溢价，有一点是肯定的：Composer 2.5 比 [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) 和 [GPT-5.5](https://openai.com/api/pricing/) 便宜得多。Anthropic 模型的输出价格为每百万 token 25 美元，OpenAI 为 30 美元，且两家公司的输入价格均为每百万 token 5 美元。

较低的价格是否足以推动开发者转向该模型仍是一个疑问。“我们必须问自己 Opus 4.7 是否真的好上 10 倍，”一位 Redditor 评论道，另一位则回复：“对于某些任务——是的。我不太喜欢用 Composer 处理 UI。但对于小型的、针对性强的任务，它非常棒。此外，它在解释细节方面非常出色。”

无论如何，Cursor 表示改进工作已在进行中。上个月，Cursor 宣布与 SpaceX 在模型训练方面建立[合作伙伴关系](https://cursor.com/blog/spacex-model-training)。该公司现在透露，它正与 SpaceXAI 合作，“从零开始训练一个规模大得多的模型，使用 10 倍的总算力”，并预期这“将是模型能力的重大飞跃”。

考虑到本周关于 Composer 2.5 价格的新闻，开发者们不禁要猜测，这款新模型到时的价格会是多少。