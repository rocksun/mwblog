阿里巴巴发布了其最新、最强大的大型语言模型（LLM）Qwen 3.8，并称其为当今最强大的模型之一。

更具体地说，该公司在周日的公告中声称，该模型“仅次于Fable 5”，即Anthropic的[备受炒作的旗舰模型](https://thenewstack.io/fable-5-honeycomb-opus/)。然而，除了这一说法外，该公司没有提供任何模型卡片、基准测试或其他有意义的数据点。

值得注意的是，该公告发布仅几天前，中国竞争对手Moonshot刚刚发布了Kimi K3，因[登顶Arena编程排行榜](https://thenewstack.io/kimi-k3-open-weight-coding/)并能在内部基准测试中与Anthropic和OpenAI的系统媲美而广受赞誉，同时在[BBC](https://www.bbc.co.uk/news/articles/cy9w4q8pgp0o)、[Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/moonshot-s-kimi-k3-may-be-more-about-memory-than-compute)等主流媒体上占据了引人注目的头条。

虽然Moonshot尚未发布K3的权重，但它[已经](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart)发布了一份[相当详尽的技术分析](https://www.kimi.com/blog/kimi-k3)，其中包括与其他领先系统的完整基准测试对比表、架构细节和公开定价，并确定了7月27日作为开源权重发布的日期。

相比之下，阿里巴巴主要依靠X平台（原Twitter）上的一条帖子来做出大胆断言。最重要的是，该消息还包含了一些语法错误，其中一个似乎将“compatible”（兼容）与“comparable”（可比）混淆了。

虽然这本身并不重要，但对于一个旨在将模型定位为真正的领先竞争者的发布会来说，这种细节可能无法建立多少信任。

## 开源权重因素

今年，市场对开源权重AI的胃口迅速增长。分析师和基础设施供应商认为，开源模型目前落后于闭源领先模型[仅四个月左右](https://thenewstack.io/open-weight-models-frontier-costs/)，且成本仅为后者的一小部分。

这种价格差距正在改变企业的AI采购方式。6月，《The New Stack》报道称，AI代理初创公司[Lindy正在将其](https://thenewstack.io/lindy-deepseek-anthropic-switch/)所有生产流量从Anthropic的模型迁移到DeepSeek v4，其CEO表示此举将为公司节省数百万美元。供应商锁定也是一个日益严重的问题，业内许多人[警告称不要过度依赖单一的专有模型](https://thenewstack.io/karp-mensch-ai-lockin/)栈。

Qwen是这种转变的主要受益者。基础设施提供商[Runpod的平台数据](https://thenewstack.io/runpod-ai-infrastructure-reality/)显示，Qwen已经超越Meta的Llama，成为其用户中部署最广泛的开源权重LLM。

然而，尽管Qwen凭借作为高产的开源权重发布者建立了声誉，但其最近两个旗舰模型却打破了这一模式。4月推出的[Qwen3.6-Max-Preview](https://qwen.ai/blog?id=qwen3.6-max-preview)是Qwen历史上第一个仅通过API发布的旗舰模型，没有发布权重。5月推出的[Qwen3.7-Max](https://qwen.ai/blog?id=qwen3.7)同样是闭源的，没有本地可运行版本，也没有确定的发布日期。

随着Qwen3.8的发布，阿里巴巴显然正在回归本源，确认它将作为开源权重模型发布。然而，这次最大的问题是时间——以及公告本身的时机是否更多是与某位竞争对手有关，而非出于开放性。

## “验证差距”

[Julien Simon](https://www.linkedin.com/in/juliensimon/)，私募股权公司[Fortino Capital](https://www.fortino.capital/)的AI运营合伙人，同时也是Hugging Face和AWS的前AI布道者，认为真正的核心在于他所说的“验证差距”（checkpoint gap）——即从做出领先声明到发布任何能让任何人真正验证它的实物之间的窗口期。

> “在[Kimi K3]发布中的每一项主张都可以对照日历进行评估。”

他在周日的《The AI Realist》时事通讯中[指出](https://www.airealist.ai/p/qwen-38-soon-is-not-a-date)，Kimi K3的[版本差距](https://www.airealist.ai/p/kimi-k3-and-the-checkpoint-gap)是“激进但纪律严明的”：提供了基准测试表、公开价格，并给出了7月27日发布权重的明确日期。

“在那次发布中的每一项主张都可以对照日历进行评估，”Simon写道。

Simon认为，Qwen3.8造成了同样的差距，但没有任何纪律：没有基准测试表、没有价格、没有日期——只有“开源权重即将到来”。这种没有日期的空白本质上是供应商可以在自己的时间表上行使的期权，同时还可以“在此期间抢占开源叙事”。

这两种模型在不同层面上背后其实是同一家公司。截至2024年，阿里巴巴是Moonshot最大的股东，投入了约8亿美元获得了[当时36%的股份](https://www.scmp.com/tech/big-tech/article/3264017/alibaba-emerges-major-backer-high-flying-chinese-start-moonshot-ai-36-stake)——考虑到Moonshot的融资和估值[持续飙升](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/)，这一持股比例可能已被稀释。

仅Kimi K3的发布据称就在几天内导致全球半导体市值[蒸发了超过3万亿美元](https://www.techtimes.com/articles/321066/20260720/kimi-k3-wipes-33t-chip-stocks-moonshot-moves-toward-hong-kong-ipo.htm)。而现在，仅仅几天后，阿里巴巴就宣布了一个参数略小的模型（2.4T参数对2.8T），声称排名略好，并附带了同样的开源权重说法——只是缺少了关键细节。

> “文字和数字之间的差距越大，公告就越像是一个纯粹的产品。”

现在显而易见的问题是，一家公司为何要看似与自己的投资项目竞争。Simon的回答归结为真实的基准测试表会迫使阿里巴巴透露什么。他认为，如果数据强大到足以击败Kimi K3，那会让它自己的Moonshot持股看起来比内部模型更差，而此时Moonshot正[计划进入公开市场](https://finance.yahoo.com/technology/ai/articles/china-moonshot-plans-ipo-six-053131621.html)。

如果数据不够好，则等于直接拱手让出“*仅次于Fable 5*”的桂冠。什么都不说，就避开了这两种结果——Qwen能够在头条新闻和企业对话中占据一席之地，而不会被放在K3旁边进行可验证的对比。

“文字和数字之间的差距越大，公告就越像是一个纯粹的产品，”Simon写道。

简而言之，这次公告本身可能从未真正关乎模型。它关乎的是将自己插入围绕一个备受炒作的竞争对手的讨论中。

> “缺失的架构细节对于一个2.4T的模型来说很重要。”

目前已经有一些对Qwen3.8进行独立基准测试的初步尝试。一份[周日发布](https://trilogyai.substack.com/p/qwen-38-max-benchmark-how-it-compares)的测试，由[Trilogy](https://trilogy.com/)人工智能卓越中心副总裁[Leonardo Gonzalez](https://www.linkedin.com/in/leonardo-gonzalez-technology/)完成，在匹配任务中运行了托管预览版与Kimi K3的对比。但这只是一个单一的测试，由一位评审员打分，且针对的是阿里巴巴自己声称在正式发布前还会不断更改的预览版。这远不能替代阿里巴巴尚未公布的基准测试表。

“缺失的架构细节对于一个2.4T的模型来说很重要，”Gonzalez承认。

目前，Qwen3.8仍处于它开始时的状态：一个针对强大的Anthropic提出的整洁的头条声明，除此之外，别无其他。