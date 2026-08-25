**每个人都想知道是谁构建了 Ox Alpha**。但那些使用匿名编码模型处理私有代码的开发者们，将会面临一个更为紧迫的问题：*当他们按下发送键后，代码会发生什么？*

让我们从该模型的异常出现开始说起。一位匿名提供商于 8 月 20 日在 OpenRouter 上架了 Ox Alpha，至今没有任何公司认领。开源终端代理 [OpenCode](https://opencode.ai/) 同日发布了该模型，并[宣布](https://x.com/opencode/status/2090544355824038300)其每天拥有 100 万亿 token 的处理容量。

OpenRouter 将其描述为一个专为长视距软件工程构建的推理模型。该列表将上下文窗口设置为 1,048,576 个 token，且在预览期间输入和输出价格均为 0。

> 对于此次发布而言，哪个检查点（checkpoint）位于端点之后并不重要。重要的是哪个法律实体接收了请求，以及是在何种条款下运行的，这一点几乎没有引起任何审查。

外界的反应变成了一场侦探故事，充斥着分词器探测、基准测试截图，以及一份不断轮换的嫌疑人名单。

## 身份追寻比基准测试更严苛

一位名为 unclecode 的开发者（Crawl4AI 爬虫的作者）构建了 [modelprint](https://github.com/unclecode/modelprint) 来对匿名 API 端点进行指纹识别。发布版本发送了九次基础设施探测，并将响应与已知模型进行匹配。Ox Alpha 在九次探测中有六次与 GLM-5.3 吻合。

他对自己所证明的内容非常谨慎。他在项目文档中写道，匹配指纹只能确定共享的基础设施，而非模型身份。同一个实验室可以使用相同的技术栈服务于两个不同的检查点。

围绕 Z.ai 的间接证据非常充分。据报道，该公司曾在 OpenRouter 上以 [Pony Alpha](https://x.com/OpenRouterAI/status/2021639702789730631) 的名义预览过 GLM-5，并在 Ox Alpha 出现前六天宣布了 GLM-5.3。小米的 [MiMo](https://x.com/haider1/status/2090725700739477692) 团队也常被作为替代方案提及，对分词器行为的一种解读则指向 [cl100k\_base](https://wccftech.com/a-mysterious-ai-lab-is-offering-100-trillion-free-tokens-day-for-its-ox-alpha-model-as-evidence-points-to-zhipus-unreleased-glm/)——这是一种在中文模型上显得格格不入的 OpenAI 编码方式。

基准测试的情况则更糟糕。X 平台上的 [Ben Davis](https://x.com/davis7/status/2090655207831298095) 报告了 10 个 DeepSWE 任务中 80% 的得分，但他自己也指出了样本量过小的问题。后来 GitHub 上发布的一份 [113 项任务测试](https://github.com/MatchaOnMuffins/oxalpha)显示，经过 20 小时的智能体工作，模型解决了其中的 66 项（58.4%）。

那次测试是可复现的，而那个病毒式传播的截图却无法复现。它仍然是一个社区基准，官方的 DeepSWE 排行榜根本没有列出 Ox Alpha。

## 一个模型，不同的路径，不同的隐私预期

Ox Alpha 的模型页面显示，提供商保留提示词和补全内容，且不将其用于训练。OpenRouter 更广泛的 [Stealth Program 条款](https://openrouter.ai/terms/stealth)（管辖所有其他使用情况）则授予了一项在该文档中描述为不可撤销且永久的许可。OpenCode 表示其 Zen 提供商遵循零保留和不训练政策。其发布的例外列表中并不包括 Ox Alpha。

OpenRouter 目前发布的披露信息相互冲突：Ox Alpha 的页面称保留的数据不会用于训练，而纳入其中的 Stealth EULA 许可声明则称，提交的内容会被用于训练和改进。根据团队通过何种方式接入该模型，他们会产生实质上不同的隐私预期。开发者无法从模型名称中推断出任何信息。

规模使得这种差距变得具有操作性而非理论性，因为自周四以来，编码智能体已经通过 Ox Alpha 推送了数十亿个 token。这些流量可能包含代码仓库内容、测试日志、环境输出以及来自私有生产代码库的截图。

如果 Z.ai 的归属属实，则会出现第二个尽职调查问题。美国商务部于 2025 年 1 月将 Zhipu AI（该公司之前使用的名称）列入了[实体清单](https://www.federalregister.gov/documents/2025/01/16/2025-00704/addition-of-entities-to-and-revision-of-entry-on-the-entity-list)。该规则称，所列实体通过开发和整合先进 AI 研究，推动了中国的军事现代化。出口管制管辖的是受《出口管理条例》（EAR）约束的物品，而非普通的 API 流量，因此这里没有任何内容使该调用非法。但这确实将该供应商归入大多数企业采购团队会进行筛选的类别。

## 最终确定的揭秘来自第一方渠道

OpenRouter 在其博客上[点名](https://openrouter.ai/announcements/quasar-alpha-and-optimus-alpha-reveal) Quasar Alpha 和 Optimus Alpha 为早期的 GPT-4.1 测试。小米[亲自确认](https://www.technology.org/2026/03/19/whos-that-ai-the-mystery-model-everyone-blamed-on-deepseek-turned-out-to-be-xiaomi/) Hunter Alpha 为其早期的 MiMo 构建版本。社区指纹识别曾多次指向正确的实验室，但这从未足以解决疑问。

一个合理的反驳是，匿名预览可以在发布前收集公正的评估，这是运行匿名预览的正当理由。

> 名字会在几周内出现在某人的博客上，但那时，每一个通过免费预览发送私有代码仓库的团队，早已在不了解真实情况的前提下做出了决定。

Ox Alpha 的数据条款也比 OpenRouter 的通用 Stealth Program 条款更为严格，后者考虑将提交的用户内容用于训练。

名字会在几周内出现在某人的博客上，但那时，每一个通过免费预览发送私有代码仓库的团队，早已在不了解真实情况的前提下做出了决定。