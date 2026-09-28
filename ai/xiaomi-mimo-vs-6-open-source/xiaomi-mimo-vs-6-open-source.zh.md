新模型层出不穷，几乎以每周一次的节奏迭代，从美国各大AI实验室推出的强大专有系统，到中国几家最大科技公司发布的更开放的替代方案。

仅在周二，[Anthropic 推出了 Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-lifecycle/)，而 [OpenAI 推出了 GPT-6 Sol 和 Luna](https://thenewstack.io/gpt-sol-alignment-gaps/)，每个模型发布时都伴随着关于它们如何击败竞争对手的常规宣称。然而，在所有关于前沿模型的狂热喧嚣中，[小米也推出了 MiMo-V2.6](https://mimo.xiaomi.com/mimo-v2-6)，这是中国日益壮大的AI开发阵营中的又一个强大开源模型。

所有最初的头条数据看起来也非常有前景。旗舰级 [MiMo-V2.6-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) 是一个万亿参数模型，每次激活 420 亿参数，拥有 100 万个 Token 的上下文窗口，并支持文本、图像、音频和视频。从广义上讲，这使其与 OpenAI 和 Anthropic 的最新模型处于相同的前沿领域：GPT-6 Sol 拥有 105 万个 Token 的上下文窗口，而 Claude Opus 5.5 拥有 100 万个 Token 的窗口，尽管两家公司都没有披露可比的参数数量。

就小米而言，它广泛宣称在编程、智能体任务、网络安全、多模态工作和研究方面达到了前沿水平。独立分析为其说法提供了一些分量——Artificial Analysis [给 MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) 打出了 46 分的智能指数评分，在其追踪的 114 个大型开源权重模型中排名第一。

![Artificial Analysis 智能指数](https://cdn.thenewstack.io/media/2026/09/b019f9a5-screenshot-2026-09-23-at-15-27-41-mimo-v2.6-pro-intelligence-performance-price-analysis-artificial-analysis.png)

*Artificial Analysis 智能指数*

目前一切顺利。但可以说，小米产品中更大的新闻在于它训练模型的方式、它向公众展示该过程的程度，以及它随后发布的内容。

## 公共记录

小米通过公共仪表盘[直播了其强化学习（RL）训练](https://mimo.xiaomi.com/rl/)，从9月15日开始的五天时间里，实时暴露了生产强化学习运行的指标。到运行结束时，仪表盘显示较小的 [MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) 模型成本为 854,044 美元，Pro 模型成本为 2,620,670 美元——总计约 350 万美元。

![小米在5天时间内直播了其强化学习运行过程。](https://cdn.thenewstack.io/media/2026/09/6fbce13b-livestreamdata-1024x401.png)

*小米在5天时间内直播了其强化学习运行过程。*

值得注意的是，这个数字仅涵盖强化学习阶段；小米尚未透露模型的预训练成本。即便如此，公开的强化学习账单也很罕见。最接近的先例发生在去年，当时 MiniMax 表示其 4560 亿参数的 [MiniMax-M1 的强化学习阶段](https://www.minimax.io/news/minimaxm1)在 GPU 租赁上花费了 534,700 美元，而 DeepSeek 将其 6710 亿参数的 R1 模型的强化学习训练[定为 294,000 美元](https://www.theregister.com/software/2025/09/19/deepseek-didnt-really-train-its-flagship-model-for-294000/1025726)。两者在发布时都是领先的开源推理模型，尽管这种比较有其局限性：MiMo-V2.6-Pro 规模更大，其强化学习运行针对的是更长的智能体任务。

直播开始不久后，曾在 DeepSeek 工作、现领导小米 MiMo 团队的[罗福莉 (Fuli Luo)](https://x.com/_LuoFuli)[在 X 上发文](https://x.com/_LuoFuli/status/2100296686719610932)解释了该项目背后的思考。她说，团队花了近六个月的时间探索强化学习的极限，增加了训练量、环境和智能体设置的多样性，以及用于评估模型尝试的资源。

“我们在接下来的几周里会逐步开源细节，”她补充道。

Hugging Face 联合创始人兼首席科学官[托马斯·沃尔夫 (Thomas Wolf)](https://www.linkedin.com/in/thom-wolf)在 X 上回应称，[此举](https://x.com/Thom_Wolf/status/2100581195255775636)是“在如此大规模的运行中表现出令人惊叹的开放度”。

然而，小米在成品模型旁发布的内容同样引人注目。该公司在宽松的 MIT 许可证下发布了模型权重，同时发布的还有其[技术报告](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf)以及一个[基于 Qwen 的 90 亿参数模型](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)，旨在作为进一步进行智能体强化学习研究的起点。

> “在如此大规模的运行中表现出令人惊叹的开放度。”

小米表示，它还“完全开源”了一套更广泛的强化学习资源：跨越软件工程、漏洞复现、知识工作和网络开发的 7,000 多个任务环境；一个涵盖从环境交互到奖励评估和策略优化的端到端训练框架；以及用于试验不同工具、提示词和上下文设置的轻量级智能体工具包。然而，在撰写本文时，小米在 [Hugging Face 上的开源集合链接](https://huggingface.co/collections/XiaomiMiMo/mimo-v26)仅包含三个模型版本，那 7,000 多个环境和其他配套资源并未在其中显现。罗此前曾表示，小米将在“未来几周内”开源各个元素。

随着[本周结果的陆续公布](https://x.com/ArtificialAnlys/status/2102128560962187701)，研究界注意力迅速从基准测试分数转移到小米承诺总体发布的内容上。曾在 Hugging Face 从事研究、现为 Prime Intellect 研究工程师的 [Elie Bakouch](https://www.linkedin.com/in/eliebak/) 特别提到了承诺的强化学习资源。

“最疯狂的部分是，他们将发布约 7k 强化学习训练数据以及导致 AA 上这个前 6 名模型的框架，”Bakouch [在 X 上写道](https://x.com/eliebakouch/status/2102136275708879078)。“他们在开始最终强化学习运行不到 1 周的时间里，就发布了模型加技术报告。”

沃尔夫进一步指出，随着更多模型开发转向具有可验证奖励的强化学习（[RLVR](https://www.promptfoo.dev/blog/rlvr-explained/)），访问模型学习的环境现在可能变得特别有价值。因为 RLVR 依赖于其结果可以自动检查的任务（例如代码是否通过测试），所以环境本身成为训练的关键要素。

> “发布大量高质量的开源强化学习环境是目前任何人所能做出的推动开源前沿的最具影响力的事情。”

“发布大量高质量的开源强化学习环境是目前任何人所能做出的推动开源前沿的最具影响力的事情，”沃尔夫[写道](https://x.com/Thom_Wolf/status/2102137611011674173)。“这相当于分享高质量的预训练数据，但却是在新的 RLVR 范式中。”

## 开源权重 vs 开源

因此，虽然小米最新模型周围的基准测试本身就很引人注目，但该公司的做法才是迄今为止引发大量欢呼的原因。

事实上，MiMo-V2.6 很好地说明了在 [AI 领域经常被混淆](https://techcrunch.com/2024/06/22/what-does-open-source-ai-mean-anyway/)的一个区别：“开源权重”和“开源”经常被当作同义词使用，但它们并非如此。许多“open”模型很大程度上只是可下载的权重——本质上是模型在训练过程中学到的庞大数值集合，可用于运行或微调它——而用于产生它们的许多内容仍然是闭源的。

一些公司在混淆这些术语方面走得更远。例如，Meta 经常将其次世代 Llama 模型称为开源，[尽管存在重大限制](https://www.forkable.io/p/metas-new-llama-4-ai-models-arent)，这[导致开源倡导者](https://opensource.org/blog/metas-llama-license-is-still-not-open-source)强烈反对这种描述。

因此，MiMo-V2.6 比大多数开源发布走得更远。它的 MIT 许可证不包含诸如[月之暗面 Kimi K3](https://pub.towardsai.net/is-kimi-k3-free-to-use-commercially-the-license-decoded-204896e1ecd5?gi=3e26d880934b)和[阿里巴巴 Qwen3.8-Max](https://www.scmp.com/tech/tech-trends/article/3363927/alibaba-adds-commercial-restrictions-open-weight-qwen38-max-ai-model)等针对大型商业用户附加的任何条件。如果这些环境如承诺的那样发布，外部研究人员将拥有更多后训练过程来进行检查和构建。