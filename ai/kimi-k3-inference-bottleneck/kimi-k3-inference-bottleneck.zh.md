**Moonshot AI 成为了最新一家发现**发布热门模型仅仅是成功一半的 AI 公司。在发布 [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/) 不到两天后，该公司因需求耗尽了其可用的 GPU 容量，停止接受新订阅者。现有用户将继续保留访问权限，同时 Moonshot 将扩展其基础设施并分批重新开放订阅。

## 推理需求超过供应

这一事件强调了需求是如何超过可用基础设施的。随着 AI 模型承担更长、更多的编程和代理工作负载，公司发现它们需要的推理容量超出了预期。

“Kimi K3 收到的喜爱远超我们的预期，” Moonshot 官方账号在 X 上写道。“在过去 48 小时内，需求已接近我们当前容量的极限。我们正在尽可能快地增加容量，并将分批重新开放新的订阅名额。”

> “我们正在尽可能快地增加容量，并将分批重新开放新的订阅名额。”

对于基础设施工程师和开发人员来说，由此产生的容量紧张是一个大胆的信号，表明了为什么从 OpenAI 到 Anthropic 再到 Moonshot 的公司都在 [配给访问权限](https://thenewstack.io/agentic-ai-token-costs/)，而不是出售无限的使用权。

## 开放权重，封闭容量

Kimi K3 拥有 2.8 万亿参数，是计划发布的最大开放权重模型之一——Moonshot 已将 [公开权重发布时间定为 7 月 27 日](https://aireiter.com/blog/kimi-k3-open-weights)。在 [Arena.ai 的前端代码竞技场 (Frontend Code Arena)](https://officechai.com/ai/kimi-k3-beats-fable-5-gpt-5-6-sol-on-frontend-code-arena/) 中，K3 在前端代码方面超过了 OpenAI 的 GPT-5.6 Sol 和 Anthropic 的 Claude Fable 5。在更广泛的 [人工智能分析指数 (Artificial Analysis Intelligence Index)](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/) 中，它落后于两者，得分为 57 分，而 Fable 5 为 60 分，Sol 为 59 分。但这并没有让它的运行变得更容易。

开放权重允许任何人部署模型，但无论谁托管它，都必须支付推理账单。编程活动往往比典型的聊天机器人交互占用更长时间的 GPU 资源，随着越来越多的开发人员涌入，保持低延迟变得更加困难。

“代理任务不是一次性的问答；它们在持续的任务中不断生成、读取和处理 Token，” 花旗集团半导体分析师 Peter Lee 在一份 [研究报告](https://www.binance.com/en/square/post/346652838928769) 中写道。

Lee 认为，随着开发人员构建更长的代理工作流程，较低的推理成本会迅速“转化为更高的总资源消耗”，从而将瓶颈从计算转移到服务器内存上。

Moonshot 的订阅暂停是一个迹象，表明一旦开发人员开始大规模使用，保持足够的推理容量在线可能与构建模型本身一样困难。

> “代理任务不是一次性的问答；它们在持续的任务中不断生成、读取和处理 Token。”

## 中国的芯片限制加剧了紧缩

对于像 Moonshot 这样的公司，这种普遍的行业瓶颈因区域性基础设施现实而加剧。与传统的软件公司不同，AI 开发人员通常从阿里云、腾讯云和华为云等云提供商处租用大部分计算能力，而不是自己拥有庞大的数据中心基础设施。

由于美国出口管制继续限制对领先芯片提供商 Nvidia 最先进 AI 芯片的访问，容量紧缩凸显了中国 AI 开发人员面临的日益严峻的挑战。因此，像 Moonshot 这样的公司依赖于旧芯片和国产替代品的组合。这些限制迫使中国开发人员非常专注于软件调优和更有效地利用计算资源，以缩小与美国竞争对手的性能差距。

## Token 经济学面临压力

对计算能力的争夺推动了中国数据中心建设的繁荣。阿里巴巴已承诺在三年内向 AI 和云计算基础设施投入超过 530 亿美元，据报道，字节跳动今年考虑在 AI 数据中心及相关基础设施上投入高达 700 亿美元。

AI 公司通常根据模型处理的 Token（即文本单元）数量向客户收费，这使得 Token 价格成为衡量运营成本的关键指标。

根据 [Bernstein Research](https://finance.yahoo.com/technology/ai/articles/chinas-latest-star-ai-model-081053486.html) 的数据，Moonshot 对 Kimi K3 的收费标准为每百万输入 Token 3 美元，每百万输出 Token 15 美元。这使其比 Anthropic 的 Opus 4.8 便宜约 40%，比 Claude Fable 5 便宜约 70%。

“一个只有 [两到三] 家拥有 90% 推理利润率的主导型前沿实验室的世界，对其他每一层来说都是净负面的，而对那 [两到三] 家实验室来说则是极好的，” Atreides Management 创始人 Gavin Baker 在 [X](https://x.com/GavinSBaker/status/2078110934740980193?utm_source) 上写道。Baker 认为，像 Kimi K3、Grok 4.5 和 Muse 1.1 这样的模型可能会将价值从模型层转移到芯片制造商、云提供商以及 [构建服务于 AI 模型的软件基础设施的公司](https://thenewstack.io/future-proof-ai-infrastructure/) 身上。

对于开发人员来说，Moonshot 的订阅冻结是一个 [架构警告](https://thenewstack.io/enterprise-ai-model-routing/)。假设拥有无限、廉价的 API 访问权限的时代正在结束。

> “一个只有 [两到三] 家拥有 90% 推理利润率的主导型前沿实验室的世界，对其他每一层来说都是净负面的，而对那 [两到三] 家实验室来说则是极好的。”