人工智能模型领域正在酝酿一场悄无声息的革命。[私有闭源顶尖模型](https://thenewstack.io/proprietary-ai-models-are-dead-long-live-proprietary-ai-models/)的统治地位因全球公众的迷恋而得以巩固，这种迷恋已渗透到从[美国](https://thenewstack.io/openai-defense-department-debate/)、[欧洲](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)到[中国](https://uk.practicallaw.thomsonreuters.com/8-618-2325?transitionType=Default&contextData=(sc.Default)&firstPage=true)的各国政府及监管机构中。

尽管存在这种垄断，但开源社区很少回避竞争（还记得 Windows 吗？现在是 Linux 和 Android？），开源倡导者[指出，闭源模型只不过是围绕着具备记忆、可观测性控制、路由智能和连接器功能的模型所打造的企业级包装](https://www.linkedin.com/posts/borisrenski_open-source-models-are-now-only-about-4-months-share-7481767295229317120-AihK/)。

如果开源模型的每个 token 成本大约便宜 10 倍，那么这种包装纸就显得相当昂贵了。

## 大公司的恐惧营销因素

AI 代理集成初创公司 [Apelogic](https://apelogic.ai/) 的创始人兼首席执行官 [Boris Renski](https://www.linkedin.com/in/borisrenski/) 告诉 *The New Stack*，顶尖实验室正“忙于散布恐惧”，宣扬模型具有独特的智慧、危险性以及即将到来的通用人工智能 (AGI)。

“这种恐惧因素旨在转移人们对基准测试的注意力，这些基准显示开源模型仅落后四个月，且成本只是其一小部分，” Renski 说。“这意味着大多数时候，企业支付给 OpenAI 或 Anthropic 的钱并不是为了获取智能，而是为了获取模型周围的‘商品化企业功能’，如 [IDP 集成](https://thenewstack.io/how-idps-and-ai-are-democratizing-platform-engineering-roles/)、[MCP 连接器](https://thenewstack.io/build-mcp-server-tutorial/) 和可观测性。”

![](https://cdn.thenewstack.io/media/2026/07/ae37be15-1783792326753-1024x776.jpeg)

*图片来源: Epoch AI*

> “大多数时候，企业支付给 OpenAI 或 Anthropic 的钱并不是为了获取智能，而是为了获取模型周围的‘商品化企业功能’，如 IDP 集成、MCP 连接器和可观测性。”

Renski 的担忧很大程度上源于他构建开源基础设施公司的二十年经历，他说他曾见证“开源总是迎头赶上，并经常在能力和采用率上超越”垂直集成的专有堆栈。这是一个反复出现的模式，他在 Windows 与 Linux、Oracle 与 MySQL、Docker Enterprise 与 Kubernetes 等对比中都发现了这一点。

## 这会是 Oracle 所有权重演吗？

“几年后，企业看待他们与顶尖实验室签署的多年期 LLM 合同时，会像今天看待他们的 Oracle 许可证一样，但那时为时已晚。这是因为他们业务的根基将与这些专有 LLM 供应商紧密交织，导致迁移变得不可能，” Renski 建议道。

[云原生计算基金会](https://www.cncf.io/) (CNCF) 执行董事 [Jonathan Bryce](https://www.linkedin.com/in/jbryce/) 同意这一说法，并告诉 *The New Stack*，为四个月的能力领先支付十倍以上的价格，在今天“绝非企业 AI 战略”。

“这显然不是一种审慎的方法或战略，” Bryce 说。“实际上，这是一种非常昂贵的锁定形式。前沿技术在不断进步，因此开发人员应该构建在开源基础设施上，使其能够在每次排行榜发生变化时无需重建应用程序即可更换模型和硬件。”

Renski 对此事的坦率观点（以及 Bryce 的赞同）恰逢无服务器推理平台公司 Featherless 做出了一些大胆的断言。该组织声称，通过对 [Z.ai GLM 5.2](https://z.ai) 开源权重中国 AI 模型进行原生优化，可以“大幅削减前沿 AI 成本”。

## 等一下，每月 1000 亿个 token 是多少钱？

该公司周一发布的一份声明称，其在 AMD 私有云基础设施上对 GLM 5.2 模型进行的本地优化，使前沿级 AI 推理费用预计降低了 94%。据 Featherless 称，对于一个以最大利用率运行且每月使用约 1000 亿个 token 的开发团队，GPT-5.5 的年度成本为 1,557,600 美元；使用 Claude Opus 4.8，相同的月工作负载年度成本为 1,506,000 美元。

如果 1000 亿个 token 听起来很多，今年引用德勤（Deloitte）研究的报告显示，一家医疗保健企业在六个月内消耗了 1 万亿个 token。

相比之下，Featherless 私有云选项将这些变量因素整合为每年 90,000 美元的固定费率，对于一个满负荷运转的开发团队来说，每年可节省超过 146 万美元。

## 推理上没有区别

我们是否真的会达到这样一个地步：大型前沿品牌感受到开源和开放权重模型的压力，以至于最终开发人员（和用户）根本不会去考虑他们的推理运行在什么硬件上？

Featherless 的开发者关系主管 [Isaac Gemal](https://www.linkedin.com/in/isaac-gemal/) 告诉 *The New Stack*，开放权重模型通常被认为性能较差或无法进行实际工作，但现在，“GLM 5.2 彻底颠覆了这种说法”。那么，让 GLM 5.2 在 AMD 而非 Nvidia 硬件上原生运行有多容易？开发人员应该注意哪些陷阱？

> “大型实验室经常说类似……‘我们不会记录您的请求，除了 XYZ 情况’，任何他们自己的系统认为‘不安全’的内容无论如何都会被保留，有时会保留数年，完全由他们自己决定。他们的区分往往含糊且非常广泛。我们认为这种方法是倒退的。”

“这并不容易；对 GLM 5.2 的需求甚至超过了我们的预测，这让我们感到惊讶，因此在开始时有效分配 GPU 资源是一个挑战，” Gemal 说。“我们拥有一支非常有才华的工程团队，他们直接与 Tensorwave 合作，确保这些大型模型部署运行良好。”

确实存在需要注意的操作限制和隐患。Gemal 建议开发人员关注隐藏在日志隐私政策中的条款。

“大型实验室经常说类似……‘我们不会记录您的请求，除了 XYZ 情况’，任何他们自己的系统认为‘不安全’的内容无论如何都会被保留，有时会保留数年，完全由他们自己决定。他们的区分往往含糊且非常广泛。我们认为这种方法是倒退的——我们非常重视隐私，” Gemal 说。

## 现实世界的开发人员怎么看？

这里的试金石显然归结为现实世界的开发人员和数据科学从业者如何看待这些开源替代方案。

波兰 Screen Studio 的软件工程师 [Kacper Michalik](https://www.linkedin.com/in/kacpermichalik/) 告诉 *The New Stack*，他一直在实际工作中测试开放权重模型（实际上是 GLM 5.2）与 Opus 4.8 等闭源模型的对比，例如为数据工程、算法问题和组件生成研究技术栈。

“对于技术研究任务，GLM 5.2 给出的结果与 Claude Opus 4.8 相似或更好，” Michalik 说。“它的范围很广，主动扩展相关主题，甚至能生成有用的可视化图表。在编码面试问题上，我比较了 GPT、Claude 和 GLM。GPT 很好地解释了思考步骤，但没有提供代码；Claude 简洁明了，但在复杂性解释上过于简略；GLM 处于中间位置，即要点清晰，有扎实的文字逐步解释，并且提供了可运行的 Python 解决方案。”

Michalik 指出，考虑到一个清晰的提示词，他觉得结果非常好。GLM 还构建了一个带有 Zod 和 TypeScript 的 React 表单组件，该组件工作正常，类型明确，能够正确处理字段，并显示清晰的验证错误。他解释说，它默认使用 Tailwind 进行样式设置，这在现在是标准做法。

“它并不完美，” Michalik 澄清道。“当我要求它在一个文件中用 React 和 TypeGPU 构建 3D 场景时，它无法正确渲染结果——我原本期待它能像 v0 或 Lovable 那样进行完整的项目生成。我在下午晚些时候还遇到了使用限制警告。”

## 开源 AI 模型安全与终点竞赛

随着其中许多开源 AI 模型来自中国，安全问题必须提上日程。

开源 CMS 公司 [Umbraco](https://umbraco.com/flexible-cms/?gad_source=1&gad_campaignid=23799046955&gbraid=0AAAAADL94wTNyiM1ghOBggOiOIh0LCvMK&gclid=CjwKCAjwvNfSBhBiEiwAyaGMCfVq-ptCKy21PlVj215GDafnmSclji4wNnDYekrqDN2EOftBgXFWRRoCPkcQAvD_BwE) 的主任工程师 [Phil Whittaker](https://www.linkedin.com/in/phil-whittaker-82481716/) 告诉 *The New Stack*，他同意开放权重（而非开源）AI 模型比前沿模型落后四到五个月，但这并非全部事实。

“我不确定我是否同意这些模型便宜 10 倍，因为这完全取决于规模和目标，” Whittaker 说。“但确实，大多数开放权重模型都是中国的。直接连接到提供商的 AI 端点具有安全和隐私隐患。使用像 Ollama 这样的第三方提供商更好，但成本是基于 token 的，模型之间分词器的差异可能意味着成本仅降低了 50%。”

最后，Whittaker 表示，自托管是一个选择，但这需要前期资本支出（服务器）和持续维护。他指出，基准测试和经验表明，GLM 5.2 正在“接近” Anthropic Opus 4.8 的智能水平。这里需要注意的警告是，虽然它不够快，但它更适合长时间运行和独立的任务，而不是推理速度至关重要的代理式编码工具。

“结果也来自驱动模型的引导程序的质量，” Whittaker 补充道。“随着模型变得越来越商品化，普通用户的需求可以通过低质量模型来满足，引导程序及其配置方式将变得更加重要。”

这里有大量的变数，当我们进入可能是中程赛道时，谈论 AI “竞赛”听起来已经陈腐且老套了。我们也许需要分析的是赛道上有多少匹马，它们被喂养什么，以及谁在勒着缰绳。