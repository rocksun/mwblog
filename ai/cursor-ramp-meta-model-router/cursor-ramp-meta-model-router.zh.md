Cursor，这款最近被Elon Musk的SpaceX以[600亿美元全股票交易收购](https://thenewstack.io/spacex-cursor-ai-coding/)的AI编程工具，推出了一个模型路由器。其旨在将每项编程请求导向处理效果最好的模型，从而避免在无需前沿模型处理的工作上支付高昂费用。

在底层，新的[Cursor Router](https://cursor.com/docs/cursor-router)采用了类似于医院急诊室的分诊系统：它分析请求的实际需求——难度如何、用途是什么、周围代码环境如何——并选择最适合的模型。简单的修复任务被分派给廉价模型，而真正的难题则被升级处理，使用接近前沿水平的模型。

值得注意的是，开发者和管理员还可以使用三种不同的模式来调节这种平衡，根据需要优先考虑速度和成本，或者优先考虑能力。

![选择三种优化模式](https://cdn.thenewstack.io/media/2026/07/441a3375-gif3.gif)

*选择三种优化模式*

根据该公司现场CTO [David Pan](https://www.linkedin.com/in/davepan/)周三在社交媒体上发布的消息，Cursor Router更广泛的逻辑是，开发者不应该为了写代码而必须成为模型性能方面的专家。

> “我们一度变得疯狂，认为每个软件工程师都应该成为模型基准测试、思考水平和缓存命中率方面的专家。”

“我们一度变得疯狂，认为每个软件工程师都应该成为模型基准测试、思考水平和缓存命中率方面的专家，”Pan写道。

早期的社区反馈很大程度上呼应了Pan的观点：[PlanetScale](https://planetscale.com/)的软件工程师[Fatih Arslan](https://www.linkedin.com/in/arslanfatih/)在X上指出，工程师们已经在手动平衡成本和能力之间的选择——默认将廉价、快速的模型用于日常工作，并将缓慢、昂贵的模型留给“重大任务”。

“我们已经花了不少时间在[选择模型上](https://x.com/fatih/status/2080047596081414417)，”Arslan写道。“为什么不把那部分自动化呢？Cursor Router完成了自动化。”

> “我们已经花了不少时间在[选择模型上]。为什么不把那部分自动化呢？”

在周三发布的另一篇[博客文章](https://cursor.com/blog/router)中，Cursor声称，与通过Opus 4.8路由所有内容相比，早期访问客户在不降低输出质量的情况下节省了30-50%的成本。

## 工作模型：掌握技术栈的控制权

此次发布是在Cursor采取一系列举措以控制更多自身AI技术栈之后进行的。5月，该公司[发布了Composer 2.5](https://thenewstack.io/cursor-composer-benchmarks/)，这是对其内部编程模型的更新，旨在以比Anthropic和OpenAI的前沿选项更低的成本处理长期任务。Composer 2.5与[其前身](https://thenewstack.io/cursors-composer-2-beats-opus/)一样，建立在Moonshot AI的[Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5)之上，这是一款来自中国的开放权重模型。

现在，在世界上最有价值的公司之一的支持下（SpaceX自6月IPO以来市值已达到1.5万亿美元），Cursor正在推动其自身强大的前沿模型。

7月8日，[Cursor和SpaceXAI联合发布了](https://thenewstack.io/grok-45-opus-killer-launch/) Grok 4.5，这是一款基于名为V9的新基础构建的混合专家模型，Musk此前曾指出该模型约有1.5万亿参数。该模型是在数万亿token的真实Cursor使用数据上进行训练的，可在所有Cursor计划中使用，价格为每百万输入token 2美元，每百万输出token 6美元。

随着Composer处理廉价、快速的工作，以及现在用于处理更严谨任务的Grok品牌前沿产品线，Cursor除了通常的外部提供商列表外，还在混合中拥有了自己的模型。这就触及了Cursor构建Router的核心原因：大多数开发者选择一个模型并坚持使用它，而不考虑任务本身，这就导致为不需要的简单工作支付了前沿模型的高价。

将每个请求发送到自己的模型本来是保持内部利润的简单方法，但这也意味着在某些任务上输出质量较低——因此，Router将每个请求发送到真正适合它的模型，无论是否是Cursor自己的模型。

## 行业现状

模型路由本身并不是什么新鲜事。[OpenRouter](https://openrouter.ai/)自2023年以来就提供了一个版本：一个单一的API，位于来自60多家提供商（包括OpenAI、Anthropic和Google）的[400多个模型](https://openrouter.ai/models)之前。其自己的[自动路由](https://openrouter.ai/openrouter/auto)功能完成了Cursor Router所做的工作——对请求进行分类，然后将其发送到适合任务和个人在成本与质量之间偏好的模型。

最近，[OpenRouter推出了Fusion](https://openrouter.ai/blog/announcements/fusion-beats-frontier/)，它采取了略有不同的方法：它不是选择一个模型，而是同时将提示词发送给多个模型，并使用判别模型来综合出所有模型中最强大的答案。

上个月，该领域又迎来了一位新成员：日本的[Sakana AI于6月发布了Fugu](https://thenewstack.io/sakana-fugu-ai-sovereignty/)，它将单一任务分解为子任务，并将每个部分路由到不同的模型，Sakana将其宣传为规避依赖任何单一AI提供商的对冲手段。

> “[Cursor Router] 是技术创新如何直接转化为产品改进的一个很好的例子。”

然而，并不是所有人都看好其他一些尝试。周三，[Nethermind](https://www.nethermind.io/)的AI产品主管[Kirill Balakhonov](https://www.linkedin.com/in/kirill-balakhonov/)在[LinkedIn上](https://www.linkedin.com/posts/kirill-balakhonov_as-i-expected-sakana-fugu-is-already-forgotten-share-7485807826494320641-Jdqc/)辩称，Cursor的版本之所以成功，恰恰是因为它专注于编程，而不是试图成为任何任务的通用路由器。

“这是一个技术创新如何直接转化为产品改进的很好的例子……而不是像Sakana Fugu或OpenRouter Fusion那样抽象的概念，”Balakhonov[写道](https://www.linkedin.com/posts/kirill-balakhonov_as-i-expected-sakana-fugu-is-already-forgotten-share-7485807826494320641-Jdqc/)，并预测这两种更广泛的路由工作最终将逐渐被淘汰。

新的东西或许是在各种模型多样化努力背后涌现的一些名字。7月初，[微软成立了一个25亿美元的服务部门](https://thenewstack.io/enterprise-ai-model-routing/)，名为Microsoft Frontier Company，在客户现场派驻了数千名工程师，帮助他们通过多种AI模型的组合进行构建。

微软商业业务CEO Judson Althoff当时[告诉路透社](https://finance.yahoo.com/technology/ai/articles/microsoft-2-5-billion-unit-165003043.html)，这一推动力部分来自观察像DeepSeek和Google的Gemini等竞争对手缩小与OpenAI差距的结果。在提到最初的Copilot时，他承认：“我们犯了一个错误，将其绑定在仅有的OpenAI模型上。”

如果行业中拥有最深厚单一模型关系的公司[正在撤回这一做法](https://thenewstack.io/openai-microsoft-partnership-restructured/)，那么模型灵活性这一理念显然已经成为主流——如果本周的动向可以作为参考的话。

周二，支出管理巨头[Ramp](https://ramp.com/)（[估值440亿美元](https://techcrunch.com/2026/06/04/ramp-raises-750m-at-44b-valuation-as-investors-hunger-for-fintechs-with-an-ai-story/)）[开放了Ramp Router](https://ramp.com/router)，这是它为管理自身内部AI账单而构建的模型路由器的早期访问公共版本，它表示将LLM成本降低了约30%。它免费启动，无需Ramp账户，并可通过兼容OpenAI的端点在OpenAI、Gemini和包括Kimi在内的精选开源模型之间进行路由。

同一天，来自*The Information*的[Jyoti Mann](https://www.linkedin.com/posts/jyoti-mann-873a4317b_scoop-metas-internal-incubator-for-ai-powered-share-7485464037544194050-dt-b/)[报道称](https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs)，Meta也在开发模型路由器。根据报告中引用的内部文件，Meta内部一个名为AAI Labs的孵化器正在开发一个名为Switchboard的新产品，该产品将对每个请求的难度进行评分，并将较简单的请求发送给更小、更便宜的模型——最初旨在降低Meta自己的AI代理成本，尽管据报道它最终可能会作为公开发布。

Meta有特别的理由想要这样做。来自[Runpod的AI状态报告](https://thenewstack.io/runpod-ai-infrastructure-reality/)（发布于3月）的数据显示，Meta的开源Llama模型现在在生产环境中的存在感微乎其微：Llama 4在现实世界中的部署几乎为零，阿里巴巴的Qwen已超过它，成为部署最广泛的自托管LLM。

为了应对，Meta也在构建专有模型。其新成立的Meta Superintelligence Labs的首款模型Muse Spark于[4月发布](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/)。随后在7月[发布了Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/)，这是Meta首款具有公共付费API的模型，价格约为OpenAI和Anthropic同类模型价格的四分之一。

Meta正在积极针对现有的行业大佬，Switchboard也符合同样的模式：这是一种让用户更容易削减成本、自由切换模型，并在有意义的情况下，将请求导向Meta自身模型的方法。

但在关于模型路由的所有喧嚣中，或许存在一个更广泛的开放性问题。不是关于模型本身的开放性（这本身就是一个激烈的辩论），而是关于路由决策本身——决定哪个模型处理哪个请求的逻辑——是否应该完全驻留在供应商自己的封闭产品中。

> “有人在将其作为开源项目构建吗？”

前Meta AI技术产品营销经理、[DAIR.AI](https://www.dair.ai/)联合创始人[Elvis Saravia](https://www.linkedin.com/in/omarsar/)在X上表示，考虑到不同团队对成本与质量的权衡方式不同，路由决策不应该封闭。

“有人在将其作为开源项目构建吗？”Saravia[问道](https://x.com/omarsar0/status/2080034479020593525)。“感觉这是你不希望卸载到API上的东西。我们都在不同的权衡下工作，所以我们需要能够实现自定义路由的能力。”

至于Cursor自己的版本，Router目前仅向团队和企业客户提供，支持桌面端、Web端、iOS、CLI和Cursor SDK。目前还不清楚它最终是否会进入个人计划。