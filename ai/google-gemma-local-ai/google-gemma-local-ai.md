<!--
title: 性能直逼26B！Google推出可在笔记本上本地运行的Gemma 4 12B
cover: https://cdn.thenewstack.io/media/2026/06/a51e3ff3-barsrsind-gtkgtdjwyxq-unsplash-scaled.jpg
summary: Google推出Gemma 4 12B，仅需16G内存即可在笔记本本地运行。其性能逼近26B模型，且首创免编码器原生音频输入，标志着高效低成本端侧AI新进展。
-->

Google推出Gemma 4 12B，仅需16G内存即可在笔记本本地运行。其性能逼近26B模型，且首创免编码器原生音频输入，标志着高效低成本端侧AI新进展。

> 译自：[Google Gemma 4 12B nearly matches 26B benchmarks — and runs on your laptop](https://thenewstack.io/google-gemma-local-ai/)
> 
> 作者：Meredith Shubel

Google[推出了](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) Gemma 4 12B，这是一款旨在为标准笔记本电脑带来高性能、多模态智能的新模型。该模型体量足够小，仅需 16GB 的显存（VRAM）或统一内存即可在本地运行。最新的 Gemma 模型在早期的社区讨论中引发了热烈反响，开发者们非常欢迎将高性能模型本地化的想法。

## **几乎与 Gemma 4 26B 一样好，但体积小得多**

体积至关重要。Google 周三发布的这款模型最杰出的品质在于，据该公司称，其性能几乎与 Gemma 4 26B 相当，但所需的总内存占用还不到后者的一半。看一下基准测试，12B 的表现确实与 26B 不分伯仲，甚至在 DocVQA（即文档视觉问答）上超越了这一较旧的模型。

![](https://cdn.thenewstack.io/media/2026/06/6289d467-google-gemma-4-benchmarks.webp)

来源：Google

让标准消费级笔记本电脑也能够拥有（或接近）Gemma 4 26B 的强大算力，意味着实际上任何人都可以随时随地离线运行高级的多步推理和智能体（agentic）工作流。而在以前，要做到这一点，必须求助于 Google 其他更强大（但更重）的 Gemma 变体。

如果你之前错过了，今年 4 月，Google [发布了](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)最新的四款 Gemma 模型——当时称其为“我们迄今为止最智能的开源模型”。该系列发布包括两款适用于个人电脑的模型（26B 和 31B）以及两款适用于移动和物联网设备的模型（E2B 和 E4B）。

现在，Gemma 4 12B 填补了中间地带，为开发者提供了比 E2B 和 E4B 更多的性能，同时比 26B 和 31B 更加轻量。

## **最吸睛的特点：原生音频输入**

体积虽然重要，但并不是全部。Gemma 4 12B 吸引开发者关注的另一个原因是，其统一架构支持原生音频输入。这是 Google 首款支持该功能的中型模型。

与传统的多模态模型（包括 Google 自身 Gemma 系列的其他成员）不同，Gemma 4 12B 没有使用独立的编码器来将图像和音频转化为用于 LLM 处理的表征。相反，正如 Google 在其发布博客中所述，新模型将这些输入“直接传递到 LLM 骨干网络中”，从而摒弃了通常与编码工作相伴的额外延迟和内存占用。

它是如何做到的？

对于图像，Gemma 4 12B 使用嵌入模块而非视觉编码器，允许 LLM 自身接管视觉处理。

这家科技巨头表示，音频处理甚至更简单；由于完全没有音频编码器，Gemma 4 12B 只需“将原始音频信号投影到与文本标记（tokens）相同的维度空间中”。

## **目前来看，反馈良好**

Gemma 4 12B 在 Reddit 开发者社区的盛大亮相，到目前为止受到了相当热烈的欢迎。

在 [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1tvw2ej/introducing_gemma_4_12b_a_unified_encoderfree/) 中，一位 Reddit 用户称其为“很长一段时间以来我听说过的最令人兴奋的模型之一”。尤其是统一架构引起了广泛关注，另一位 Reddit 用户表示：“在一个并非极小规模的模型上实现原生音频支持，对我来说显然是这之中最令人兴奋的一点。”

目前还没有太多时间来实际测试这个新模型，但热情已经高涨：“我有许多使用场景，如果这东西运行起来效果哪怕还算说得过去，都会带来极大的便利，”另一位 Reddit 用户补充道。

至于潜在的缺点，[Hacker News](https://news.ycombinator.com/item?id=48385906) 上的一个评论指出，他们猜测该模型的编程能力可能会受到限制——事实上，Google 的发布声明中确实没有提及这一点：“与 Qwen 3.6 35B A3B、Gemma 4 26B A4B、Nvidia Nemotron 3 Nano 30B-A3B、gpt-oss-20b 等其他小型模型相比，它在编程方面的总体表现可能不会太好。”

另一位评论者也表示赞同：“在我看来，Qwen 在编程方面要好得多，尤其是与 Pi 等工具结合进行智能体编程时，在很多使用场景中它的表现可能已经足够接近 Sonnet。而对于你使用本地大语言模型进行的大多数其他任务，Gemma 系列则是更好的选择。”

## **未来属于本地吗？**

但现在看来，在编程基准测试中拔得头筹可能并不是重点。值得注意的是 Gemma 4 12B 相当强劲的性能以及其并不臃肿的体量。

它可以在标准电脑上本地运行，这意味着开发者不必总是求助于云端来获取高性能智能，这可能会对未来的成本产生深远的影响。正如一位 [Reddit 用户](https://www.reddit.com/r/artificial/comments/1tw0cqv/google_just_dropped_gemma_4_12b_on_your_laptop/) 所言：“云端很方便，但你得永远按 token 付费，而且你的提示词（prompts）要经过别人的服务器。本地运行 = 一次性配置，保护隐私，无持续成本。”

也许 Google 确实认为未来属于本地。去年 9 月，这家科技巨头[推出](https://developers.googleblog.com/google-ai-edge-gallery-now-with-audio-and-on-google-play/?utm_source=chatgpt.com)了 Google AI Edge Gallery，并声明希望让这个开源应用成为“最具启发性和实用性的端侧 AI 展示平台”。

通过将接近 26B 的性能带到标准的消费级笔记本电脑上，Google 正在让端侧 AI 受到更多关注，而开发者们也正翘首以待。