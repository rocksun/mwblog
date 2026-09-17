<!--
title: Shopify深耕React Native多年后，竟在12周内完成了全原生重构
cover: https://cdn.thenewstack.io/media/2026/09/92d0ae32-betsy-nwankwo-bdfqey9icfi-unsplash-scaled.jpg
summary: Shopify决定从React Native转向全原生开发，并利用AI代理（Agents）大幅提升重构效率。尽管放弃跨平台，但AI改变了开发经济学，使其能快速、低成本地进行底层迁移。Shopify通过内部系统Helix分步拆解任务，确保重构质量，并重新设计代码架构以适配AI协作模式。
-->

Shopify决定从React Native转向全原生开发，并利用AI代理（Agents）大幅提升重构效率。尽管放弃跨平台，但AI改变了开发经济学，使其能快速、低成本地进行底层迁移。Shopify通过内部系统Helix分步拆解任务，确保重构质量，并重新设计代码架构以适配AI协作模式。

> 译自：[Shopify spent years on React Native — then rebuilt everything in 12 weeks](https://thenewstack.io/shopify-native-ai-agents/)
> 
> 作者：Amanda Caswell

2020年，Shopify通过在React Native中编写一次移动端代码，而不是在Swift和Kotlin中复制每个功能，打下了一个在开发者世界引起共鸣的赌注。

周四，该公司[表示将回归原生](https://shopify.engineering/back-to-native)。

您没有看错；该公司正在抛弃跨平台移动应用，转向全原生开发，并且严重依赖AI代理来承担繁重的工作。其消费者应用Shop从概念验证到完全原生生产版本发布仅用了12周时间。接下来是更艰巨的商家应用，这是一个拥有300多个屏幕的庞然大物，严重依赖深度的iOS平台集成。

有趣的是，Shopify并不认为它在React Native上的投入是一个错误，因为该框架确实在多年内完成了公司需要它完成的任务。更不用说，也没有明显的迹象表明Shopify准备放弃这一切；就在[2025年1月](https://shopify.engineering/five-years-of-react-native-at-shopify)，该公司还在公开谈论其与React Native的未来。

## 代理取代了跨平台的权衡

但是，编码代理能力变得更强了，到2025年底，Shopify发现代理可以观察一个功能如何在iOS上运行并构建Android版本，或者反向操作。工程师们也可以在他们不太熟悉的平台上工作，因为代理可以处理更多特定于平台的任务。

“LLM改变了我们2020年决策背后的核心假设之一，”Shopify工程总监Mustafa Ali写道。

> “LLM改变了我们2020年决策背后的核心假设之一，”

## 重写的经济性不断变化

Shopify并不是唯一一家将代理投入此类问题的公司。Bun的创建者、现任Anthropic技术团队成员[Jarred Sumner](https://www.linkedin.com/in/jarred-sunner-a8772425/)使用了64个并行运行的Claude Fable 5实例，将[JavaScript运行时从Zig移植到Rust](https://bun.sh/blog/rewriting-bun-in-rust)——在大约11天内重写了约一百万行代码，预估API成本为165,000美元。Sumner报告称，在合并之前，现有的测试套件已在所有六个支持的平台上通过。

一年前，这需要一个小团队花费多个季度才能完成，但今天这是一个由一个人监督的11天冲刺。

> 一年前，这需要一个小团队花费多个季度才能完成，但今天这是一个由一个人监督的11天冲刺。

请记住，这些生产力收益并不是均匀分布的。正如*The New Stack*[最近报道的](https://thenewstack.io/openai-agent-research-bottleneck/)，AI代理在使某些开发任务变得更快捷的同时，也可能在工程组织的其他地方创造更多的工作量。但它们也改变了那些曾经难以撤回且成本高昂的决策所涉及的工作量。

5月，开发者[Simon Willison](https://www.linkedin.com/in/simonwillison/)[写道](https://simonwillison.net/2026/May/14/not-so-locked-in/)，他遇到了一位工程师，该公司的团队利用编码代理将其旧的iPhone和Android应用合并为一个单一的React Native应用。Willison问他们为什么要合并，因为代理使维护独立的代码库变得更容易，但该工程师并不担心被锁定。React Native完成了公司需要的工作，如果以后情况有变，他们总是可以搬回原生。Shopify现在正在做同样的事情，只是应用规模更大，投入也更多。

## Zero-shot提示词产生了垃圾代码

Shopify首先尝试给LLM现有的React Native代码，并要求其将其原生重写。结果并不好。Ali将输出描述为垃圾（slop），但增加更多的步骤并没有解决问题。

即使在团队让模型在接触代码之前编写规格说明书和任务文件时，它仍然产生了太多工程师不想维护的代码。

## Helix将迁移分解成小块

Helix应运而生，这是Shopify用于管理进行重写的代理的内部系统。它将迁移按屏幕进行，将每个屏幕分解成更小的块，而不是试图一次性重新创建所有内容。Shopify在进行过程中将结果与现有应用程序进行比较，而独立的代理在人类签字批准之前检查代码中的问题。该系统还保留了审查反馈，以便更早发现的问题可以为后续工作提供参考。

很难不将这种方法与[Shopify首席执行官公开威胁要封禁Claude Code](https://thenewstack.io/shopify-claude-code-agentsmd/)时发生的事情联系起来，原因是有工程师在没有充分审查的情况下发布了代理生成的代码。Helix采取了类似的谨慎方法，假设代理的输出在任何人依赖它之前需要证明自己。

## 为代理构建的代码库

迁移揭示了另一个问题。代理可以在几秒钟内更改代码，但在移动模拟器中测试它可能需要两倍的时间。

Shopify通过将业务逻辑与UI分离，并让代理通过在桌面上运行的CLI与应用程序交互来解决这个问题。一些曾经需要几分钟的检查现在可以在几毫秒内完成，同时相同的接口可以在需要时控制模拟器。

[大多数代码库在构建时并未考虑AI代理](https://thenewstack.io/go-language-ai-agents/)。Shopify正开始围绕它们进行构建，并表示将部分通过代理最终能独立处理多少工作量来评估原生应用。

> 一些曾经需要几分钟的检查现在可以在几毫秒内完成，同时相同的接口可以在需要时控制模拟器。