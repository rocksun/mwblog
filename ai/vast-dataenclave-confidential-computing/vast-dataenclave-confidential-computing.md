<!--
title: AI与数据之争正迎来第三种选择
cover: https://cdn.thenewstack.io/media/2026/09/2292a6b7-screenshot-2026-09-23-at-15.29.24.png
summary: 随着AI在企业中普及，数据安全与模型知识产权的冲突日益激化。VAST Data推出的DataEnclave技术利用机密计算，在保护企业数据不外泄的同时确保AI实验室的模型权重安全，为行业提供了兼顾双方利益的第三种选择。
-->

随着AI在企业中普及，数据安全与模型知识产权的冲突日益激化。VAST Data推出的DataEnclave技术利用机密计算，在保护企业数据不外泄的同时确保AI实验室的模型权重安全，为行业提供了兼顾双方利益的第三种选择。

> 译自：[A third option is emerging in the fight over AI and your data](https://thenewstack.io/vast-dataenclave-confidential-computing/)
> 
> 作者：Alex Wilhelm

关于人工智能与你的数据的争夺战，正在涌现第三种选择

不是你的密钥，就不是你的代币。不是你的模型，就不是你的数据？

今年夏天，科技行业[陷入了一场辩论](https://www.cnbc.com/2026/08/03/palantir-karp-open-ai-anthropic-open-weight.html)，关于人工智能在企业中的应用以及保护知识产权的必要性。如果企业使用专有模型，数据泄露是否是一件不可避免的坏事？

视频

企业似乎有两个选择：他们可以使用最先进的专有模型，但面临失去数据控制权的风险；或者他们可以使用开源权重模型，却永远无法触及最前沿的技术。

谢庆，第三种选择正在浮现。

考虑一下这样的担忧：A公司希望使用来自人工智能实验室C的大语言模型B，并且他们希望避免训练人工智能实验室C如何通过将其实际能力内置到大语言模型B中来抢夺A公司的生意。解决这种紧张关系的一个好方法是让A公司在自己的基础设施上运行大语言模型B，这样就不会有其信息凭空外泄的风险。

> AI 代理正在“在数据层创造一套完全不同的需求。”
> ——Vast Data 联合创始人 Jeff Denworth

但这引发了*另一个*问题：人工智能实验室C不想允许A公司在自己的GPU上运行大语言模型B，因为它不想交出自己的模型权重。这与该公司遇到的知识产权问题如出一辙，只是反过来了。你必须双向解决信任问题！

[VAST Data](https://www.vastdata.com/)联合创始人[Jeff Denworth](https://linkedin.com/in/jeffreydenworth)闪亮登场，带来了一款名为[DataEnclave](https://www.vastdata.com/press-releases/vast-data-introduces-dataenclave-to-bring-leading-ai-models-and-enterprise-data-together-on-trusted-infrastructure)的新产品，旨在让AI实验室和企业级公司在安全的计算环境中部署专有模型，而不会在任何一个方向上面临数据传输的风险。（DataEnclave使用Nvidia的机密计算技术来使系统运转；Vast Data的核心产品是AI操作系统，这是一种适合公司AI应用程序之下的基础设施。）

*The New Stack*邀请Denworth参加了播客节目，聊了聊机密计算市场。我对时机很好奇。*为什么Vast现在才构建DataEnclave？*毕竟，Nvidia在2024年就开始[大力](https://developer.nvidia.com/blog/?p=81376)推行机密计算。Denworth认为，市场确实需要核心技术，但也需要需求。

而且直到2025年底，与今天的Token总量相比，人工智能的需求还是温和的。一旦氛围编程工具起飞，企业对人工智能产品的需求就会飙升。这就导致了我们在2026年初看到的定价危机，以及我们在夏天忍受的安全人工智能使用辩论。

性能推动了需求，需求推动了使用，而使用又挖掘出了需要解决的新问题。现在市场面临的问题是，DataEnclave是否已经解决了*专有AI与专有数据*方程式两端足够的担忧。随着它从早期访问走向全面上市，市场将对此进行梳理。

我们的对话深入探讨了人工智能的发展轨迹、企业目前在人工智能旅程中的所处位置，以及企业内部仍有多少数据等待被释放。如果你想感受到这种加速，这会是一个很有趣的节目！