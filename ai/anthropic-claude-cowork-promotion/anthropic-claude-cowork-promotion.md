<!--
title: Anthropic为何突然免费翻倍Claude Cowork使用额度？
cover: https://cdn.thenewstack.io/media/2026/06/45cbee79-papermax-studio-zepajz3hiom-unsplash-scaled.jpg
summary: Anthropic宣布为Pro、Max及Team等付费用户免费提供Claude Cowork限时使用额度翻倍优惠。专家指出，此举旨在培养用户工作流依赖，通过环境锁定而非模型本身来提高迁移成本，同时这也引发了业界关于AI数据处理能力与安全风险的讨论。
-->

Anthropic宣布为Pro、Max及Team等付费用户免费提供Claude Cowork限时使用额度翻倍优惠。专家指出，此举旨在培养用户工作流依赖，通过环境锁定而非模型本身来提高迁移成本，同时这也引发了业界关于AI数据处理能力与安全风险的讨论。

> 译自：[Why Anthropic just doubled Claude Cowork limits at no charge](https://thenewstack.io/anthropic-claude-cowork-promotion/)
> 
> 作者：Adrian Bridgwater

Anthropic宣布了一项限时促销活动，将其Claude Cowork中用户的五小时使用限制翻了一番。

这项活动于周一宣布，在当前[代币经济低迷](https://thenewstack.io/tokenomics-foundation/)的时期，通过承诺提供[双倍的](https://i.ebayimg.com/images/g/OxcAAOSw6l9lAooD/s-l1200.jpg)免费配额，无疑会赢得一些用户的青睐。[Claude Cowork](https://www.anthropic.com/product/claude-cowork)是该公司开发的协作开发环境，专为[非技术知识工作者](https://thenewstack.sc/productivity-paradox-productivity-in-the-age-of-knowledge-work/)打造。它能够整合来自多个来源的信息来完成任务，而无需用户协调每个步骤。

## 免费翻倍——是指我吗？

该工具也被软件开发人员用于承担与文档、数据和文件相关的任务。此优惠适用于Pro、Max和Team计划的用户。它也扩展到企业计划中的传统席位用户。

免费计划和基于消费的企业席位不包括在此促销活动中。

Anthropic陈述的具体条款告知我们：“从2026年6月5日至2026年7月5日，您在Cowork中的5小时使用限制翻倍。每周使用限制保持不变。无需采取任何行动即可参与。如果您使用的是符合条件的计划，翻倍的使用量将自动应用。”

## 这是Claude Cowork，不是Claude

2倍的使用量增加仅适用于Claude Cowork。其他Claude产品的使用限制——例如[网页、桌面和移动端上的Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)——保持不变。

Claude Cowork于今年1月12日作为研究预览版推出，允许用户将工具指向特定的文件夹、一组本地文件或应用程序，以返回完成的交付成果。用户可以通过标准的聊天界面修改软件随后的操作。

> “这类促销活动是典型的漏斗顶部策略：在开发者和广大用户还没来得及仔细考虑替代方案之前，就让他们沉迷于工作流……真正的锁定不在于模型，而在于你的环境。” ——Eric Paulsen, Coder。

尽管这一切表面上看起来很有吸引力，但这种“促销”行为（咳咳，对于一家前沿模型公司来说，用这个词是不是有点不太合适？）真的会推动用户和开发者更深入地进入Anthropic的漏斗吗？

[Eric Paulsen](https://www.linkedin.com/in/ericpaulsen17/)是安全、自托管、代理式AI开发环境公司[Coder](https://coder.com/)在EMEA地区的外勤CTO。他告诉*The New Stack*，他以前见过这种钳形攻势。

“这类促销活动是典型的漏斗顶部策略：在开发者和广大用户还没来得及仔细考虑替代方案之前，就让他们沉迷于工作流，” Paulsen说。

而且，他认为这很有效。

“为什么？因为一旦你深入到某个提供商的工具链和生态系统中，切换的成本就太高了；迁移和转换你的工作流本身就是一个工程，” Paulsen说。 “所以真正的锁定不在于模型，而在于你的环境。”

## 为什么AI的可移植性如此痛苦？

Paulsen提到了切换成本，我们知道在不同模型之间迁移上下文是痛苦的，甚至几乎是不可能的。但为什么会这样呢？

这可能是由于分词（tokenization）不兼容造成的，因为每个大语言模型都使用自己独特的分词器、[分块逻辑](https://www.mongodb.com/resources/basics/chunking-explained)（将信息分解为更小的部分）和词汇量大小。此外，还有一个事实是，不存在通用的AI内存层；例如，正如DevOps工程师Daniel Ginês所解释的那样，AI内存可移植性问题意味着用户上下文被困住了。

“当你切换时，你不会丢失数据——你丢失的是理解，” Ginês说。

> “前沿模型如今正在基准测试中追逐任务的复杂性，以证明自己的地位。但实际上，在企业内部，真正的复杂性在于数据，而这正是这些模型容易严重失足的地方，” Dheeraj Pandey, DevRev。

## 前沿模型的圈地运动仍在继续

Anthropic的这一促销举措，部分原因可能在于现在关于前沿模型公司如何运作和宣传的[主流电视新闻](https://www.bbc.co.uk/news/articles/cx2124z7g45o)报道数量巨大。也许他们的想法是……当非技术门外汉处于这种宣传的炮火中时，那就以门外汉为目标。这就是你获得锁定的方式，对吧？

企业AI和客户服务平台公司[DevRev](https://devrev.ai/)的创始人兼CEO [Dheeraj Pandey](https://www.linkedin.com/in/dpandey/)告诉*The New Stack*，只有当提供的软件工具变得“精确、高效且安全”以供长期使用时，锁定（对于Claude Cowork，或者实际上对于Claude本身）才有效。

“前沿模型如今正在基准测试中追逐任务的复杂性，以证明自己的地位。但实际上，在企业内部，真正的复杂性在于数据，而这正是这些模型容易严重失足的地方，” Pandey说。“生成代码是前沿模型的一个很好的通用目标，但它也是最简单的目标。要使协作真正发挥作用，前沿模型需要在数据检索方面变得更加准确，仅靠GPU无法实现这一点。”

Pandey进一步解释说，他认为在高度复杂的数据上运行的简单任务继续“产生糟糕的答案”，他认为这种“对MCP的过度依赖并没有帮助”我们整个行业。

## 使用量翻倍，风险也翻倍吗？

在一篇现在已被覆盖的博客文章中，Anthropic曾预告了Claude Cowork的最初发布，并警告了当输入模糊、模棱两可或相互矛盾的指示时，该工具存在的风险。意外删除文件和提示词注入的可能性被列为可能的风险。

“这些风险在Cowork中并不新鲜，” Anthropic当时表示。“但这可能是你第一次使用超越简单对话的更高级工具。”

六个月过去了，Anthropic在向用户保证此类脆弱性方面并没有过于慷慨，但确实表示Claude Cowork是“在设计时考虑了人工监督”，并且随着它完成任务，“后续的决策权仍然掌握在用户手中”。

“Anthropic对代理安全（agent safety）的处理方法，包括我们如何考虑信任、访问和控制，已在我们的研究中记录在案，” 该公司表示。

2026年7月5日之后，Cowork中的5小时使用限制将恢复到标准水平。用户计划或账单没有变化。

Claude Cowork可通过[Claude桌面应用程序](https://claude.com/product/cowork)在所有付费计划中使用。