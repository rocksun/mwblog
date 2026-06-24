<!--
title: Kiro迈向移动端：AWS将代理式编程监管引入iPhone
cover: https://cdn.thenewstack.io/media/2026/06/6be4a2e1-getty-images-6dhxbtwmmvk-unsplash.jpg
summary: AWS发布Kiro移动端应用，让开发者通过iPhone即可随时监控、审核并管理AI代理的编程任务，无需全程守在电脑前。该应用通过规范驱动开发模式，有效提升了AI代码生成的质量与可控性。
-->

AWS发布Kiro移动端应用，让开发者通过iPhone即可随时监控、审核并管理AI代理的编程任务，无需全程守在电脑前。该应用通过规范驱动开发模式，有效提升了AI代码生成的质量与可控性。

> 译自：[Kiro goes mobile: AWS brings agentic coding supervision to the iPhone](https://thenewstack.io/aws-kiro-mobile-ios-agentic-coding/)
> 
> 作者：Darryl K. Taft

Kiro迈向移动端：AWS将代理式编程监管引入iPhone

AWS发布了一款用于 [Kiro](https://thenewstack.io/kiro-requirements-analysis-automated-reasoning/) 的原生iOS应用程序，这是其 [人工智能驱动的开发环境](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/)。该应用让开发者无需电脑，即可在手机上监控、引导和批准代理式编程任务。

该应用在 [AWS纽约峰会](https://aws.amazon.com/events/summits/new-york/) 上宣布，允许开发者在离开工位时启动会话、查看差异（diffs）并批准变更。计算任务在AWS云端后台运行，这意味着从手机发起的会话即使在屏幕关闭后也会持续运行。

“开发者有一种‘焦虑感’，比如我想回到代理那里做些事情，”AWS Kiro首席开发者倡导者 [Darko Mesaros](https://www.linkedin.com/in/darko-mesaros/) 告诉 *The New Stack*，“开发者一直在要求一种与这些代理进行交互的方式。”

他指出，此次发布反映了AWS对代理式开发的看法发生了更广泛的转变。“随着 [自动代理](https://thenewstack.io/ai-agents-database-challenge/) 在多个存储库中承担长期运行的任务，瓶颈从编写代码转移到了管理编写代码的代理上。Kiro Mobile旨在让开发者保持在工作流程中，而无需被束缚在工作站前，”Mesaros说。

“Kiro现在让你能够授权、走开，然后回来查看PR，”Kiro首席产品经理 [Kyle Seaman](https://www.linkedin.com/in/kyleseaman/) 在一篇关于此次发布的博客文章中写道。“继续基于规范的工作流程，让Kiro从你上次中断的地方继续。或者从你的手机或网页发起一个自主会话，Kiro会在云沙箱中独立运行，检查文件并运行测试。当Kiro需要你的输入时，它会暂停。你可以在任何地方做出响应，选择方向，工作就会从中断处继续。”

## 三种模式，一个代理

该应用支持Kiro网页版提供的三种会话模式：用于快速查询的“聊天（Chat）”、用于需求驱动工作流的“规范（Spec）”以及用于完全委托任务的“自主（Autonomous）”。在网页上开始的会话会自动显示在移动应用程序中，并具有相同的身份、模型偏好和已连接的存储库。

差异（Diffs）以带有文件头的原生红绿卡片呈现，专为小屏幕上的可读性而设计。PR和代码审查状态显示在每个会话行上。AWS构建的是原生体验，而不是简单地将网页界面适配为移动端。Mesaros对此直言不讳。

“它不是一个相对笨重的网页界面，而是一个用于iPhone的原生应用程序，”他说。

## 规范驱动是基础

此次iOS发布的同时，AWS还将规范驱动开发引入了Kiro网页版，公司称这一工作流是工程师内部构建软件的核心。

与其提示代理实现某个功能并祈求最好的结果，规范驱动开发要求代理首先生成需求文档、设计文档和任务列表。在代理编写一行代码之前，开发者会审查并批准这些工件。

“规范驱动开发是AI编程混乱的解决方案，”Mesaros解释道。“它是代理和开发者之间的一份合同。它防止这些代理漫无目的地去修改它们不应该修改的东西。”

Mesaros表示，目前大约80%的AWS软件工程师使用Kiro，并将规范驱动的工作流融入了实践中。他指出，Kiro自动化了设计文档和需求规范的生成，减少了过去使规范驱动开发难以持续的手动开销。

## 可用性

Kiro Mobile目前在iOS 26及更高版本上提供预览版，适用于Kiro Pro、Pro+、Pro Max和Power订阅用户。支持通过Google、GitHub、IAM或AWS Builder ID登录。公司尚未设定正式发布日期。

目前没有Android支持计划。AWS表示，做出“iOS优先”的决定是基于开发者通过GitHub Issues和Discord提交的请求，并将根据未来的需求评估Android版本。