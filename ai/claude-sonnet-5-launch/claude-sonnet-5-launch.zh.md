Anthropic 周二[发布了 Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)，这是其主流 Sonnet 系列中的最新模型。

该公司称 Sonnet 5 为其“迄今为止最具有代理能力的 Sonnet 模型”，在基准测试方面，其性能接近 [Opus 4.8](https://thenewstack.io/claude-opus-48-release/)，并较 [Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/) 有了显著提升。Anthropic 特别指出，它在涉及推理、工具使用、软件编码和知识工作的任务中表现更为出色。

与以往的一些 Sonnet 发布不同，虽然它在性能上并没有完全超越最新版本的大型 Opus 模型，但它已经足够接近，暂时成为了 Opus 4.8 的一个更具性价比的替代方案——因为 Opus 5 的发布应该也不远了（前提是它没有[像 Fable 5 那样受到限制](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)）。

Anthropic 强调，Opus 4.8 在更高推理水平上仍将提供更高的准确性，但也指出：“Sonnet 5 为开发者提供了价格更低、且质量远高于以往的选择。”

![](https://cdn.thenewstack.io/media/2026/06/679e5683-screenshot-2026-06-30-at-10.12.37-am-1024x481.png)

*Sonnet 5 基准测试。图片来源：Anthropic*

在最高“超高”（Extra High）推理级别下，Sonnet 5 在 OSWorld-Verified 和代理搜索 BrowseComp 基准测试中的表现与 Opus 4.8 的中到高设置大致相当。但由于在相同推理水平下，它的运行成本比 Opus 4.8 更高，因此对于某些任务，Opus 4.8 仍然是更好的选择。

![](https://cdn.thenewstack.io/media/2026/06/d5d68e3d-screenshot-2026-06-30-at-10.33.20-am-1024x570.png)

*图片来源：Anthropic*

至少从 Anthropic 目前提供的基准测试来看，Sonnet 5 的表现始终优于 [Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/)。

不过，基准测试只能反映一部分情况。模型的行为也会影响用户对模型的感知。Anthropic 表示，其测试人员注意到，该模型现在经常能完成复杂的任务，例如“此前 Sonnet 模型会中途停止”的任务。

## Sonnet 5 定价

为了让 Sonnet 5 对开发者更具吸引力（或许也能腾出一些运行 Opus 4.8 的资源），Anthropic 为 API 用户提供了介绍性价格：在 8 月 31 日之前，每百万输入 token 为 2 美元，每百万输出 token 为 10 美元。此后，价格将上涨至每百万输入/输出 token 3 美元/15 美元，这也是 Anthropic 之前对 Sonnet 模型收取的费用。

当被问及这是否是 Anthropic 首次提供介绍性定价时，一位发言人告诉 *The New Stack*：“我们希望客户在迁移窗口期内，以尽可能低的成本针对其实际工作负载测试 Sonnet 5。”

目前，Anthropic 还提高了 Chat、Cowork 和 Claude Code 用户的速率限制，正如公司所言，“以适应更高努力水平下更高的 token 使用量。”

## Sonnet 5 的安全性

在 AI 安全性方面（这显然是 Anthropic 的重点，特别是在 Fable 5 被撤下之后），Anthropic 指出，它并没有“刻意在网络安全任务上训练 Sonnet 5”，虽然它可以处理一些常规的网络安全任务，但其在这些测试上的表现远落后于 Opus 4.8，当然还有 Mythos。尽管如此，Anthropic 还是保留了该模型的网络安全防御措施，但由于风险较低，这些防御措施并不像 Fable 5 那类模型那样严格。

该公司明确指出，例如在尝试寻找 [Firefox 147](https://www.firefox.com/en-US/firefox/147.0/releasenotes/) 中的漏洞时，“Sonnet 5 从未能够开发出完整的有效漏洞利用，但它确实显示出比其前身 Sonnet 4.6 稍高的部分成功率。”

看来，美国政府将 Sonnet 5 撤出流通的风险相当低。

![](https://cdn.thenewstack.io/media/2026/06/7b24b9a5-screenshot-2026-06-30-at-10.42.15-am-1024x570.png)

*图片来源：Anthropic*