<!--
title: 给套壳应用开发者的严厉警告
cover: https://cdn.thenewstack.io/media/2026/11/2d5f82cf-pablo-dr-yvf7hmzw3hu-unsplash-1024x683.jpg
summary: 文章探讨了Anthropic拓展企业级软件业务引发的担忧。开发者和创始人担心，作为底层模型提供商的Anthropic可能会利用平台数据，将合作伙伴挤压为竞争对手，重演亚马逊自有品牌的竞争逻辑。
-->

文章探讨了Anthropic拓展企业级软件业务引发的担忧。开发者和创始人担心，作为底层模型提供商的Anthropic可能会利用平台数据，将合作伙伴挤压为竞争对手，重演亚马逊自有品牌的竞争逻辑。

> 译自：[A nervous warning to wrappers](https://thenewstack.io/anthropic-enterprise-developer-competition/)
> 
> 作者：Amanda Caswell

**Anthropic希望开发者在Claude上构建业务**，但其向企业软件领域的扩张正在引发创始人们的担忧：提供底层模型的公司，最终可能会变成他们最大的竞争对手。

## 给套壳应用开发者的严厉警告

GlacierGrid 的总裁兼首席运营官 [Gerald Zingraf](https://www.linkedin.com/in/gerald-zingraf/) 在 Anthropic 周二扩大 Claude 企业级产品线后，[在 LinkedIn 上表达了这种担忧](https://www.linkedin.com/in/gerald-zingraf/)，他将 Anthropic 的战略比作亚马逊的自有品牌业务。

Zingraf 写道：“这让我对套壳应用和纯 SaaS 公司感到紧张，”他结合了自己过去通过亚马逊销售自己设计的产品，随后眼睁睁看着这家零售商推出竞争产品的经历。

> “这让我对套壳应用和纯 SaaS 公司感到紧张，”

他的担忧在于，Anthropic 可以看到客户最频繁地使用哪些第三方集成，并在决定自己构建哪些功能时潜在地利用这些信息。

他认为：“Anthropic 拥有相同的视角，”尽管他没有提供证据证明该公司曾使用集成数据来识别竞争对手或指导其产品路线图。对一些开发者而言，这种风险已不再是假设。

## 当合作伙伴变成竞争对手

法律AI初创公司 Spellbook 的 CEO [Scott Stevenson](https://www.linkedin.com/in/scottas/) 在 11 月 2 日接受*[福布斯](https://www.forbes.com/sites/rashishrivastava/2026/11/02/inside-silicon-valleys-love-hate-relationship-with-anthropic/)*采访时，描述了 Anthropic 进军他公司所在市场时发生的事情。

Spellbook 的业务广泛使用 Claude 模型，从审查合同、建议修改到自动化法律工作流。Stevenson 回忆说，Anthropic 的员工曾向他保证，公司没有计划直接进军法律软件领域，但随后 Anthropic 就推出了 Claude for Legal，其中包括与 Spellbook 业务重叠的合同审查功能。

> “Anthropic 一直是一个伟大的合作伙伴，但这让我们意识到他们是一家庞大的公司，组织内的不同部门可能会有冲突的指令，”

Stevenson 在采访中说：“Anthropic 一直是一个伟大的合作伙伴，但这让我们意识到他们是一家庞大的公司，组织内的不同部门可能会有冲突的指令。归根结底，这是不可避免的。”

Spellbook 并没有放弃 Claude。Anthropic 仍然[将这家初创公司作为客户进行展示](https://claude.com/customers/spellbook)，据报道，其由 Claude 驱动的智能体每月执行约 530,000 次合同审查，同时 Stevenson 也出现在 Anthropic 10 月 28 日关于法律制品的公告中。

这种关系凸显了产品依赖前沿模型的开发者所处的艰难境地。尽管 Anthropic 开发了针对部分相同客户的应用程序，Spellbook 依然受益于 Anthropic 的技术。Stevenson 的叙述中没有任何证据表明 Anthropic 使用了 Spellbook 的专有信息来开发其法律产品。

## 当平台直接发布你的产品

技术创始人和 Dalton Mills CEO [Todd Saunders](https://www.linkedin.com/in/tosaunders/) 在 3 月 10 日的 [X 平台发文](https://x.com/toddsaunders/status/2031116948411429149)中也表达了类似的观点，此前 Anthropic 推出了 [Claude Code Review](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/)。

> “Anthropic 是新时代的亚马逊，”

Saunders 写道：“Anthropic 是新时代的亚马逊，”并警告在 Claude 的 SDK 上构建应用的开发者，该公司可能会观察应用的使用情况，并最终将竞争功能融入 Claude 中。

该公司在 [11 月 10 日的公告](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors)中推出了 Claude Sheets、Claude Whiteboards 和 Claude Data，同时预览了 Claude Meetings。扩展的交互式连接器还允许合作伙伴直接在 Claude 内部嵌入应用程序，包括来自 Adobe 和 Atlassian 的软件。

## 政策中未明说的事

Anthropic 可以访问有关客户如何与第三方应用程序和服务进行交互的信息，该公司在其 2026 年 9 月 10 日生效的[隐私政策](https://www.anthropic.com/legal/privacy)中承认了这一点。目前尚不清楚的是，Anthropic 在决定下一步构建什么时，是否会查看哪些集成最受欢迎。

企业客户的规则则有所不同。根据 Anthropic 的[商业条款](https://www.anthropic.com/legal/commercial-terms)，客户保留其输入内容的权利并拥有输出内容，而 Anthropic 同意不使用其内容来训练模型。其[商业隐私文档](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)还指出，除非用户将其直接粘贴到对话中，否则反馈数据不包括通过连接器（包括本地和远程 [MCP servers](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)）拉取的内容。

这两份文件都没有明确 Anthropic 如何使用聚合的集成数据。

## 开发者接受的权衡

该公司仍在鼓励开发者在 Claude 上构建业务。只是，获得其不断增长的企业客户群体需要付出一定的代价，因为 Anthropic [控制着界面](https://thenewstack.io/claude-enterprise-apps-connectors)，并且可以在不征求依赖它的开发者意见的情况下引入竞争功能。

目前，Anthropic 正要求开发者将其视为技术提供商和商业合作伙伴，尽管它正进军这些开发者正努力建立业务的市场。这种关系能否保持可持续，可能与其说取决于 Anthropic 今天承诺了什么，不如说取决于它接下来决定推出什么。

*The New Stack* 已联系 Anthropic 请求置评，但尚未收到回复。