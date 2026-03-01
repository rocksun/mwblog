<!--
title: 掌控全局：Google Conductor AI 如何确保代码可控
cover: https://cdn.thenewstack.io/media/2026/02/5d8143fa-sara-oliveira-h-f6qrzenq0-unsplash-scaled.jpg
summary: Google Conductor AI引入自动化代码审查，强调以人类为中心，通过上下文理解和指令遵循确保AI生成代码的质量与安全，应对幽灵依赖等风险。
-->

Google Conductor AI引入自动化代码审查，强调以人类为中心，通过上下文理解和指令遵循确保AI生成代码的质量与安全，应对幽灵依赖等风险。

> 译自：[In the driver’s seat: How Google Conductor AI actually stays under control](https://thenewstack.io/google-conductor-automated-reviews/)
> 
> 作者：Adrian Bridgwater

Google 希望为开发者提供一个全面、实用的AI软件开发工具包。因此，本月该公司为其 [Google Conductor AI](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) 扩展程序添加了一项新的自动化审查功能。

Conductor 是一个上下文驱动的开发扩展，目前作为 Gemini CLI 的预览版提供。它以持久化、版本控制的 Markdown 文件的形式，在开发者的代码旁创建正式规范。Markdown 是一种轻量、便携的文本格式，深受程序员喜爱。

[Google 表示](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/)，Conductor 允许开发者在构建前进行规划，在编写代码前审查计划，并将人类开发者牢牢地置于主导地位。

Conductor 的新自动化审查扩展旨在理解和解释代码库的规范和指南，并随后生成实施后的 [代码质量和合规性](https://thenewstack.io/checks-by-google-ai-powered-compliance-for-apps-and-code/) 报告。

> “Conductor 背后的理念很简单：控制你的代码。”

Google 为何这样做？因为在一个非技术业务人员也开始意识到AI驱动代码及其在没有人为监督下自动化决策潜力的世界里，Google 需要强调其核心信息，正如 [这篇关于更新的博客文章](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/#:~:text=The%20philosophy%20behind%20Conductor%20is%20simple%3A%20control%20your%20code.) 中明确指出的那样：“Conductor 背后的理念很简单：控制你的代码。”

## 更智能，但更安全

Anthropic 也为 Cloud Code 实施了自动化审查功能，以监督安全性、逻辑和集成。那么，编程社区如何看待这些新的、所谓更智能但也更安全的工具在实际应用中的实用性呢？

Cloudsmith 的开发者关系主管 Nigel Douglas 用一个关于电锯的生动比喻来解释。

“没有自动化审查的AI编码CLI就像一把没有‘关闭’按钮的电锯，但遗憾的是，这些改变只关注已生成的代码，即完全跳过了它所引入的上游组件。如果一个AI编码助手建议一个不存在或已被恶意软件感染的包，那么 [开发者最终会比任何人都能更快地发布漏洞](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/)，” Douglas 告诉 *The New Stack*。

> “没有自动化审查的AI编码CLI就像一把没有‘关闭’按钮的电锯……”

Douglas 提醒我们，当大型语言模型（LLM）能够在几分钟内生成数千行功能代码时，同行评审无法再像以往那样运作。这是一个远远超出人类阅读能力的计算过程。他坚持认为，当前AI开发工具的状态意味着自动化审查只是一个步骤；因此，他呼吁在拉取请求阶段加入人工干预，将贡献从“可信输出”重新定位为“需要专家验证的提议草稿”。

## 一个（仅仅）有意义的里程碑

“Google 持续投资于提高AI生成代码的质量和可靠性，是该行业的重要一步。讨论的焦点正从AI是否能 [生成代码转向它是否值得信赖](https://thenewstack.io/ai-code-generation-trust-and-verify-always/) 来评估和改进代码……因此，自动化审查是这一进展中一个有意义的里程碑，” Tabnine 的首席营销官 Chris du Toit 说。

Chris du Toit 表示，他的团队在企业中看到的是，信任最终来源于上下文，理解代码如何适应真实系统、真实依赖项和真实操作限制。

“随着AI从协助开发者转向执行真正的工程工作，组织将越来越需要一个组织智能层，为AI提供对其环境的结构化理解，从而使自动化审查能够安全、一致地大规模运行，”Chris du Toit 针对新功能提出。

## 遗留项目的脏活累活

虽然 Tabnine 分析整个代码库的上下文（而不仅仅是单行代码）并且可以建议从单个变量名到整个函数和测试用例相关的所有操作，但 Google Conductor 在这方面并非没有能力。Conductor 的上下文驱动开发方法旨在确保AI服务理解项目的架构、规则和历史。

Google 还明确表示，Conductor 可以通过其工作区范围的扫描功能应用于已经启动的棕地项目。这家云计算巨头证实，Conductor 的扫描使其能够识别编程语言、文件夹结构和现有模式，从而为 Markdown 文件提供初始内容。该公司表示，这样即使在大型代码库中，应用后也能“尊重你的特定编码风格”。

Sysdig 的常驻首席信息安全官 Conor Sherman 对代码助手同样乐观且谨慎。他说，智能体编码系统空间的一个具体 [风险](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/) 是幽灵依赖（phantom dependencies）的出现，有些人也称之为“slopsquatting”。

## Slopsquatting 的粗糙性

“这是指编码智能体编造一个听起来可信但不存在的包或组件名称。然后，威胁行为者可以在那个完全虚构的名称下发布恶意包。如果智能体——或者信任该智能体的开发者——安装了它，你就会将攻击者代码引入你的构建管道。从那里，它就可以进入生产环境，”Sherman 解释道。

Sysdig 建议将AI智能体视为拥有高度权限的内部人员。这意味着要为每个智能体赋予严格限定范围的身份、最小权限，并对其可以安装、获取或执行的内容设置严格的边界。然后使审计跟踪不可协商：如果你无法回答智能体做了什么、何时做的以及在谁的授权下做的，你就无法控制该系统。

另外，Sherman 指出 Anthropic 去年11月的安全报告显示，更强大的模型在某些评估设置中可能被推向有害的、高自主性的行为。这很重要，因为同样能够加速良性工作的通用能力，也可以大规模压缩攻击时间线。

## 指令遵循作为衡量标准

Salesforce 的首席开发者布道师 Mohith Shrivastava 认为，衡量像 Google Conductor 这样的智能体服务是否有效运作的问题，将从评估其输出转向对“指令遵循”进行更明确和可衡量的分析……而这将成为行业新的AI治理关键可靠性指标。

“企业将要求提供概率性的遵循分数——分为高、低或不确定——以使开发者能够相应地完善他们的指令，并让首席信息官对他们的智能体的可靠性和可信度有信心。这种对合规性进行量化衡量的关注，对于扩大企业智能体的规模并避免代价高昂的错误至关重要，为安全可靠的AI设定了新的基准，”Shrivastava 说。

Google 在这一领域目前的最后宣言是，相信上下文驱动的开发，并将开发者文档视为事实的来源，以此作为复杂项目实现更高质量成果的途径。在全行业范围内，对于下一步要做什么存在共识：这并非单纯地优化代码生成；而是在符合架构、资源高效和安全的方式下进行。