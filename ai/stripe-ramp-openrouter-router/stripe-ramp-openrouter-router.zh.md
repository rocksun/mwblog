*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 发展动态，并解释它们对于致力于应用这项技术的个人和组织意味着什么。核心论点很简单：学会使用 AI 的从业者将定义他们行业的下一个时代，而这份时事通讯旨在帮助你成为其中一员。*

---

模型分类（Model triage）正在成为 AI 原生开发者最重要的技能之一。整个夏天我一直在强调，那些能从前沿模型中获得最大收益的人，都是那些足够自律、不会默认运行最强大模型的人。周三，Stripe 和 Ramp 间隔 70 分钟验证了这一理念：[Stripe 收购了 OpenRouter](https://thenewstack.io/stripe-acquires-openrouter-tokens/)，而 [Ramp 发布了其内部路由](https://x.com/vral/status/2090144932711575631)。

据 [*Bloomberg*](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) 报道，OpenRouter 的收购价格超过 70 亿美元，而 [*Axios*](https://www.axios.com/2026/08/17/stripe-openrouter-paypal) 则称其交易金额（现金加股票）超过 80 亿美元。Stripe 尚未公布条款，因此细节仍不明确。

尽管此次收购占据了头条，但架构才是真正的焦点。过去几年里，选择模型通常是写入应用程序代码或配置文件中的字符串，切换模型需要耗费一定的工作量。而路由改变了这一工作流。Stripe 买下了这一层，而 Ramp 构建了它。两者都在押注现有的客户关系将为他们提供独特的切入点，从而在新的 AI 技术栈中占据这一关键层。

## 选择模型正成为运行时的决策

OpenRouter 是一个端点，为 80 多家提供商的 400 多个模型提供服务，[每天处理超过 10 万亿个 Token](https://x.com/OpenRouter/status/2090127246430216403)。Andrej Karpathy 将其称为 [AI 的转换开关](https://x.com/deedydas/status/2090129029777224033)。Ramp 的路由器在较小的模型库上完成了同样的工作，并[声称对于相同的输出成本降低了约 40%](https://x.com/vral/status/2090144932711575631)。

两者都认为代码库中硬编码模型名称是一种负担。他们基本是对的。早在六月，[我就指出 Mitchell Hashimoto](https://thenewstack.io/claude-fable-cost-model-triage/) 发现了一个标准的编码任务：在 GPT-5.5 上成本约为 1.50 美元，而在 Claude Fable 上则约为 9 美元，但两者产生的结果同样可接受。路由器可以自动处理这种分类，在每次请求时做出决策，而不是仅在开发者明确配置的情况下才进行。

这正在成为一个巨大的问题，也是一个巨大的机遇。我们团队的 Amanda Caswell [本周报道称](https://thenewstack.io/claude-code-token-reduction/)，Anthropic 的 `/claude-api` 技能在回答单个问题前会消耗约 20 万个 Token，而按需加载参考文档而不是预先加载，可以将这一数字削减至约 2.5 万。[Hafiz Hassan 上周为我们撰文](https://thenewstack.io/ai-pipeline-token-optimization/) 解释了为什么 AI 管道的成本比演示时高出 10 倍，而他列出的每个罪魁祸首都是工程决策：每轮重新发送的系统提示词、附加的整个对话历史、过大的 RAG 分块、以及直接转储到上下文中的原始 JSON。这是一份非常实用的指南，Hassan 指出的所有项目都不是采购问题。

Token 账单是由你的代码生成的，这就是为什么控制它的工具也随之出现的原因。

## Stripe 和 Ramp 想要同一个层，原因却截然不同

Stripe 正通过开发者从下往上攻击这个问题。该公司周三由 Eric Newcomer [泄露的投资者信](https://x.com/EricNewcomer/status/2090133049291788434) 直接论证了这一点：“到目前为止，每个开发者都需要一种简单可靠的方法来管理他们的收入管道，满足这一需求催生了 Stripe。然而，展望未来，每个开发者也将需要一种简单可靠的方法来管理他们的智能管道。”

> Stripe 希望通过广大的开发者群体来控制 AI 支出。Ramp 则希望通过其与财务部门的现有关系来控制支出。

Stripe 以前就构建过类似产品。其支付业务将数十种本地支付方式隐藏在一个 API 之后，将每笔交易路由到最有可能转化的支付方式。AI 版本只是将同样的理念应用于模型，而不是支付网络。

Ramp 正通过财务部门从上往下进行攻坚。该公司购买了 router.com 域名，并称其客户每月已经通过 Ramp 购买了千万亿级的 Token。创始人 Veeral Patel 在发布文章中[推介](https://x.com/vral/status/2090144932711575631)该服务时表述得很简洁：“监控并控制你在每个提供商处的 AI 账单。” [Adam Wazzan](https://x.com/theCTO) 比我更好地总结了 Ramp 的战略：“当首席财务官为首席技术官发布产品时。”

Stripe 希望通过广大的开发者群体来控制 AI 支出。Ramp 则希望通过其与财务部门的现有关系来控制支出。两者都在追逐企业技术预算中迅速成为最大支出项目之一的内容：Token。

在 X 上，Kabir Goel [反驳了](https://x.com/KabirGoel/status/2090200868016767465) Stripe 的表述。路由 Token 是一种少花钱的方式，而 Stripe 的其他产品旨在帮助企业赚更多钱。

“团队并不是去 Stripe 了解他们花了多少钱，”他写道。“那绝对是 Ramp 的地盘。”

关于团队目前在哪里寻求解决方案，他的观点有一定道理。但这在三年后是否依然成立，正是 Stripe 刚刚花费数十亿美元下注以推翻的预判。

## 最值得选择的路由器是不卖模型的那一个

无论你指向哪个路由器，它都决定了哪个模型来编写你的代码，而并非每个路由器都是中立的。我们团队的 Paul Sawers 在 7 月报道 Cursor、Ramp 和 Meta 的第一波路由器时就[指出了这个问题](https://thenewstack.io/cursor-ramp-meta-model-router/)。Cursor 支持 Grok 和 Composer。Meta 正在构建 Muse Spark。两者都有理由将工作发送到自己的模型中，Paul 引用了开发者 Elvis Saravia 的提问：路由逻辑是否应该开源，而不是由供应商私下决定。

Stripe 和 Ramp 都不销售模型。OpenRouter 首席执行官 Alex Atallah 在 Stripe 的公告中也表达了这一点：开发者“需要一个中立的层来编排和管理所有这些模型。” 投资者 Gavin Baker 对这一机会的判断如出一辙，他认为 Stripe 可以成为 AI 的中立基础设施层，就像它成为支付的中立基础设施层一样。

不过，中立并非免费。Stripe 从 Token 支出中抽取比例，而 Ramp 想要你的消费关系，所以“2026 年底前免费”只是一个带有截止日期的客户获取策略。

显而易见的异议是，供应商的动机不应成为担忧的重点，路由质量才是真正重要的。这很公平，《Towards Data Science》发表了一个我读过的最好的实际案例。Pratik Rupareliya [描述了一个路由层](https://towardsdatascience.com/we-built-a-routing-layer-to-cut-our-ai-costs-it-broke-the-product/)，它将一名支持代理的推理账单降低了 40%，但也导致产品崩溃。分类器将“简单”查询发送到更便宜的模型，但其中一些“简单”查询实际上是欺诈调查。

更便宜的模型充满信心地给出了错误的回答。客户停止使用该代理，第四个月流失率上升超过基准线，留存成本是节省费用的四到五倍。花了三个月时间才浮出水面，又花了一个月才查明原因。他的修复方法是分层质量监控，结合不确定性路由级联，最终在不牺牲质量的情况下实现了 35% 的成本节省。在深入研究模型路由之前，[这是一篇非常值得阅读的文章](https://x.com/vral/status/2090144932711575631)。

所以，请对路由进行仪表化。记录路由器在每次请求时的选择，并按服务于它们的模型细分你的质量指标。据报道，Ramp Router 会记录每次调用的模型、提供商、层级、Token、延迟、成本和回退尝试。Stripe OpenRouter 的排名多年来一直是这种遥测数据的公开版本。通过这两种方法，你都可以获得类似的可观测性。

目前，模型正在成为一种实现细节。竞争正在转向决定哪个模型来完成工作的层。Stripe 和 Ramp 押注开发者并不关心端点后面是什么，只要账单更低且结果足够好就行。