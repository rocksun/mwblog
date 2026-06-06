**如果说本周 AI 编程领域有什么重大启示**，那就是固定费率、“无限量畅写”的定价时代即将结束——而且账单到来的速度比一些人预期的还要快。

最明显的例证来自 GitHub，它取消了 Copilot 的固定订阅模式，转而[采用基于 token 的计费方式](https://thenewstack.io/github-copilot-token-billing/)，将成本直接与消耗挂钩。自 [4 月份宣布这一消息](https://thenewstack.io/github-copilot-usage-billing/)以来，积怨已久的反对声浪排山倒海。一些订阅者表示，预计的月度账单一夜之间暴涨了十倍，还有人将这一变化定性为“诱导转向”。

随后在周三，Linux 基金会[宣布计划](https://thenewstack.io/tokenomics-foundation/)成立 [Tokenomics Foundation](https://www.tokeneconomics.com/)，这是一个由谷歌、微软、Salesforce、摩根大通等巨头支持的新行业机构，旨在围绕 AI token 的生产、消耗和货币化构建开放标准与框架——这也默认了当前企业缺乏一致、中立的方式来衡量或控制他们所需支付的费用。

## 为企业带来可观测性与控制力

至于 [Cursor](https://cursor.com/home)，它显然一直在关注这一动向。周一，这家 AI 编程智能体公司[重组了其团队版（Teams）的定价](https://cursor.com/blog/teams-pricing-june-2026)，将年度席位费下调了 20% 至每用户每月 32 美元，同时推出了每月 120 美元的全新 Premium 档，承诺以 3 倍的价格提供 5 倍于标准席位的用量——此举明确针对那些消耗量难以预测的重度用户。

与此同时，Cursor 升级了其[自研 Composer 模型](https://cursor.com/blog/composer)的专用使用额度池，使其独立于 Anthropic 和 OpenAI 等第三方模型的额度。

此次更新还包括重新设计的支出预警功能，允许管理员根据金额阈值（按成员或团队范围）配置警报，并在意外扣费发生之前，通过 Slack 或电子邮件发送通知。

![支出预警](https://cdn.thenewstack.io/media/2026/06/08794395-spendalertgif.gif)

*支出预警*

到了周三，[Cursor 推出](https://cursor.com/blog/organizations)了一个企业治理层，直击 IT 和财务团队的痛点，他们目前正负责控制 AI 支出。

新的“[组织 (organizations)](https://cursor.com/docs/enterprise/organizations)”结构使大型企业能够从单个仪表盘管理多个 Cursor 部署，并可在部门级别配置预算、模型访问权限和智能体权限。

> 核心逻辑在于，不同的职能部门具有不同的风险属性和不同的成本容忍度。

核心逻辑在于，不同的职能部门具有不同的风险属性和不同的成本容忍度——产品或工程团队可能需要完整的模型列表和宽裕的支出空间，而营销或财务团队可能会被限制使用更便宜的模型、设定更低的上限，并要求智能体在执行任何命令前必须获得人工确认。

组织级的仪表盘汇总了每个团队的支出和 token 消耗，支持按用户、团队或云端智能体进行筛选，为财务团队提供了按业务单元进行内部转账核算的可观测性。

![按团队划分的用量分析](https://cdn.thenewstack.io/media/2026/06/05061613-usageanalyticsgifyeah.gif)

*按团队划分的用量分析*

总的来说，这些功能旨在为企业环境带来可观测性与控制力，在当前，难以掌控的 AI 定价已成为各行各业 CFO 最关注的问题。

要理解其中的原因，有助于探究 Cursor 等工具背后的经济学原理。

> 这些功能旨在为企业环境带来可观测性与控制力，在当前，难以掌控的 AI 定价已成为各行各业 CFO 最关注的问题。

## “套壳”模式的生存挤压

像 Anthropic 或 OpenAI 这样的公司直接基于每个 token 收取推理费，而 Cursor 与之不同，它是一个“套壳（wrapper）”——它以 API 价格从前沿模型提供商处购买推理额度，然后向开发者转售访问权，历史上一直采用固定的月度服务费模式。当使用量较小时，这种模式行得通，但随着智能体化（agentic）编程会话变得更长、更重且消耗更多的 token，这种模式就难以为继了。

设立隔离的 Composer 额度池是 Cursor 对这一生存挤压最直接的回应。[Composer 2.5](https://thenewstack.io/cursor-composer-benchmarks/) 作为 Cursor 自研的编程模型，其[成本](https://cursor.com/docs/models-and-pricing)为每百万输入 token 收费 0.50 美元，每百万输出 token 收费 2.50 美元。相比之下，Claude Opus 4.7 和 4.8 的输入成本为 5.00 美元，输出成本为 25.00 美元——在最核心的 token 消耗上，两者存在十倍的差距。

通过为 Composer 提供独立的专属额度，并在用户耗尽第三方 API 额度时自动降级切换到该模型，Cursor 在结构上正引导用户使用其自身控制的更便宜的推理服务，从而在此过程中维护其利润率。

> Cursor 在结构上正引导用户使用其自身控制的更便宜的推理服务，从而在此过程中维护其利润率。

这一动态正在整个行业内上演。周一，[JetBrains 开源了 Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)，这是一个具有 120 亿参数的编程模型，专为智能体系统的基础设施层构建（如路由、检索管道和子智能体任务），并支持在 Cursor 和 Claude Code 等托管工具无法运行的环境中进行本地部署。尽管其前身 Mellum 仅能处理代码补全，但 Mellum2 是为更广泛的协同工作而设计的，而这正是当今工程团队部署 AI 的核心所在。

两者的方法虽有不同——Mellum2 支持自托管，将推理成本完全交由运行它的团队掌控——但底层的动机是一致的：减少对高昂第三方 API 调用的依赖。

## 价格调整带来的伤疤

鉴于本周 GitHub 因 Copilot 的重大改版而面临愤怒用户的声讨，值得注意的是，Cursor 以前也曾在棘手的定价泥潭中摸爬滚打过。

在 2025 年 6 月，该公司[推出了](https://cursor.com/blog/new-tier)每月 200 美元的 Ultra 计划——这得益于其与 Anthropic、OpenAI、Google 和 xAI 签署的多年期批量协议。但与此同时，它将其 Pro 计划从基于请求的计费方式转变为基于算力的计费方式，这一变化让许多用户猝不及防，并导致了意料之外的扣费。

那次调整的执行过程非常糟糕，以至于 Cursor 不得不[公开道歉](https://cursor.com/blog/june-2025-pricing)并向受影响的用户退款。

本周的举措是对同样底层压力的另一种回应。2025 年的变化侧重于重组 Cursor 的收费标准及其应用方式，而本周的更新则赋予了组织机构可观测性和控制力，以管理他们已经产生的支出。

这一举措能否成功，部分取决于透明度。Cursor 仍未公布其包含的使用额度池的具体大小，仅将其描述为“慷慨”——这种模糊性可以说是 Tokenomics Foundation 成立旨在解决的问题。

正如 FinOps 基金会执行董事 [J.R. Storment](https://www.linkedin.com/in/jrstorment/) 告诉 *The New Stack* 的那样，组织机构目前没有一致的方法来跨提供商比较成本，也无法在 AI 部署方面做出明智的决策。

“每个超大规模云厂商、每个模型提供商和每个硬件提供商都会有自己的方法、数据和价值指标，”Storment 说道。“我们的目标是在他们之间协调出一致的模型，正如我们以前所做的那样。”

在现状改变之前，各个平台上的用户在很大程度上都在黑暗中探索这种全新的代币经济（token economy）——这也是为什么 Cursor 的支出预警、使用仪表盘和模型访问控制功能，尽管还算不上完美，但也确实朝着正确的方向迈出了一步。