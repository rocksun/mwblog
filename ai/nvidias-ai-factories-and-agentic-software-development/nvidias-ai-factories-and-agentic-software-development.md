<!--
title: 英伟达AI工厂：重塑智能体软件开发
cover: https://cdn.thenewstack.io/media/2025/10/70294566-nvidia3.png
summary: 英伟达收购Solver，推进AI垂直整合。其AI工厂模式利用强大芯片优化AI效率和功耗。未来代理CLI可能依赖英伟达平台，预示AI软件开发新生态。
-->

英伟达收购Solver，推进AI垂直整合。其AI工厂模式利用强大芯片优化AI效率和功耗。未来代理CLI可能依赖英伟达平台，预示AI软件开发新生态。

> 译自：[NVIDIA’s AI Factories and Agentic Software Development](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/)
> 
> 作者：David Eastman

我通常会关注可以立即测试的大语言模型（LLM）软件工具，但这篇文章的起因却是因为我无法测试的软件。我一直在关注 Solver（一款[所谓的“自动驾驶”AI编程工具](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/)）自我们一年前发表文章以来的表现。我注意到它已经——[卖给了 NVIDIA](https://techstartups.com/2025/09/03/nvidia-acquires-ai-coding-startup-solver-amid-growing-ai-investment-spree/)。Solver 去年就已经采用了基于代理的方法，因此它走在了前沿。但 NVIDIA 想要它做什么呢？

“NVIDIA 是一家硬件公司”通常足以打消我进一步探究的念头。但当然，NVIDIA 的芯片是AI革命的核心，因此它成为世界上第一家市值达到4万亿美元的公司。所以，即使你的兴趣在于软件开发领域，NVIDIA 的动向也值得关注。

NVIDIA 最近进行了大量收购，包括[对其自身生态系统的投资](https://thenewstack.io/how-solid-is-ed-zitrons-case-against-generative-ai/)，这些投资导致股价飙升，而没有真正的收入支撑。更令人困惑的是，NVIDIA 还宣布将向 OpenAI 投入1000亿美元。但它究竟在押注一个怎样的不同世界呢？线索就在那个尘封已久的术语“垂直整合”中。

## 了解AI中的垂直整合

让我们看看我定期评测的典型代理CLI设置。我从一个终端（通常是 [Warp](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/)）开始，然后在其上安装目标代理CLI应用程序（例如，[Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)）。运行时，它可能会查询 Claude Sonnet LLM，通过 Anthropic 进行通信，Anthropic 则在 AWS 云上运行其模型。这把一切都视为链中的组件。你希望有机会使用同类最佳的，或者至少是最经济实惠的。通常的论点是，一旦模型经过训练，就可以在更便宜的芯片和商品化云上运行，从而形成一个横向或模块化的市场。

相比之下，垂直整合是苹果公司所做的事情。它制造自己的硬件、自己的芯片、自己的操作系统，并且不情愿地允许人们为自己的生态系统编写软件应用程序。至少，这提高了可靠性和安全性。

AI的横向市场有什么问题？在代理时代，我们不再向聊天机器人提出一次性问题。多个代理并行工作，这使得与大语言模型（或大语言模型群）的关系变得复杂。正如 NVIDIA 创始人兼 CEO [黄仁勋](https://www.linkedin.com/in/jenhsunhuang/)所说，真正的资源限制不再是每个芯片的成本；而是每千瓦可以生成多少令牌，因为限制因素现在是功耗。无论你如何获取电力，持续地通过一个大型地点泵送电力都是一个挑战。很快，限制因素很可能将是水。

## NVIDIA的优势：AI工厂模式

这就是 NVIDIA 的优势所在：拥有各种最强大的芯片，每千瓦可生成最多的令牌。为了处理各种不同类型的请求（短或深），NVIDIA 拥有一个软件层，可以优化 AI 模型在可能数百或数千个 GPU 上运行的方式，根据其 AI 工厂或数据服务器中的工作负载需求动态分配资源。

但我们并不需要深入细节，因为 Apple MacBook 的集成示例已经足够说明问题。MacBook 只是效率更高，因为操作系统不必对硬件进行有根据的猜测。它可以立即停止并重新启动，而没有神秘的“睡眠”或“休眠”机制带来的不稳定问题。问任何PC游戏玩家，他们都不知道自己的最新游戏在他们的机器上运行得如何，直到他们真正运行它。

NVIDIA 的 AI 工厂旨在进行工业部署。其理念是它们可以为特定行业进行训练，然后处理推理请求。但让我们想象一下，一个合适的工厂最终将可供下游开发者使用。

## 代理初创公司的未来与NVIDIA的角色

那么，未来的代理CLI如何在AI工厂中工作呢？

你可能会在本地的“AI工厂”拥有一个账户，或者通过 NVIDIA 达成更全面的协议。而且应该只有一张账单，其金额可以实时准确地跟踪（或预测）。

如果你的代码存储在一个对 NVIDIA 可见的仓库中，那将允许进行项目扫描和[用于并行运行的独立分支](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/)。拥有 GitHub 的优势仍然牢牢掌握在微软（以及通过它，OpenAI）手中。无论哪种方式，项目都将在本地扫描并发送到“AI工厂”或通过共享仓库读取。垂直整合的一个优势是你的查询经过的手续更少。你显然必须信任 NVIDIA，但可能无需信任其他人。NVIDIA 必须决定这对它的客户有多重要。

NVIDIA 可以根据你的账户可用的芯片范围提供不同的服务产品。提供的范围越大，就越容易将浅层代理卸载到更便宜的大语言模型，这可能允许用户从节省中分一杯羹。

现在，我预计 API 将会可用，但设计（或采购）一个 Claude Code 风格的代理CLI的诱惑将是巨大的。当然，这就是我们开始讨论 Solver 的起点。

## 结论

幕后发生的事情对软件开发者来说不应太重要，但代理时代的优势与令牌生成速度和并行运行紧密耦合。

在某个时刻，代理初创公司的繁荣期必将走向寒冬。届时，NVIDIA 肯定会是收拾残局的领先公司之一。当然，除了专业的 [CUDA 平台](https://developer.nvidia.com/cuda-toolkit)之外，它与开发社区并没有太多关系。因此，如果它要朝着这个方向发展，我预计在代理时代仍在享受它的夏天时，就会有测试版工具发布。