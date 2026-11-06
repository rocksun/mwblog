<!--
title: Anthropic找到证明哪个AI模型回答你的方法——但代价高昂
cover: https://cdn.thenewstack.io/media/2026/11/caa0e2d8-chloe-f5wzv43ls-0-unsplash-scaled.jpg
summary: Anthropic开源了加密系统FlashProve，利用zkSNARKs技术来验证AI模型的真实身份而不泄露权重。虽然它比以往方案快得多，但由于巨大的GPU计算开销，目前尚无法用于常规API生产环境。
-->

Anthropic开源了加密系统FlashProve，利用zkSNARKs技术来验证AI模型的真实身份而不泄露权重。虽然它比以往方案快得多，但由于巨大的GPU计算开销，目前尚无法用于常规API生产环境。

> 译自：[Anthropic found a way to prove which AI model answered you — but there's a costly catch](https://thenewstack.io/anthropic-flashprove-model-verification/)
> 
> 作者：Amanda Caswell

使用 AI API 的开发者几乎无法知道回答他们请求的模型是否真的是他们付费使用的模型。提供商可能会将请求路由到更便宜的模型，或者攻击者可能会干预响应，而客户没有明显的方法来检测这种切换。

现在，Anthropic 想要改变这一现状。该公司的前沿红队（Frontier Red Team）发布了 [FlashProve](https://www.anthropic.com/research/provable-inference)，这是一个开源的密码学系统，旨在验证哪个 AI 模型生成了响应，同时不暴露其底层权重。

这项于[周二宣布](https://x.com/AnthropicAI/status/2117710942826123294)的研究最终可以帮助开发者验证第三方 AI 服务并检测受损的推理系统。但 FlashProve 仍然是一个研究原型，生成证明的成本使得它对于常规 API 流量来说不切实际。

> 但 FlashProve 仍然是一个研究原型，生成证明的成本使得它对于常规 API 流量来说不切实际。

## FlashProve 如何证明模型

FlashProve 使用 [zkSNARKs](https://www.anthropic.com/research/provable-inference) 来验证响应来自一组特定的模型权重，而不会透露这些权重。承诺仍然必须来自受信任的来源，否则证明意义不大。

Anthropic 已在 [GitHub 上发布了 FlashProve](https://github.com/anthropics/FlashProve)，开发者可以在那里下载代码并自行测试该系统。然而，它仍然是一个研究原型，并未作为 Claude API 的一项功能提供。

## 每个证明的成本

Anthropic 在 Meta 的 Llama 4 Maverick（一个拥有 4,000 亿参数的混合专家模型）上测试了 FlashProve，而不是 Claude。

根据 Anthropic 的[基准测试](https://www.anthropic.com/research/provable-inference)，FlashProve 在单个 Nvidia H100 GPU 上生成证明的同时，每秒处理大约 110 个 prompt Token。每个证明约为 18.78 MB，在单 CPU 线程上验证大约需要 21 秒。生成证明的成本远高于检查证明。

与使用 vLLM 的标准推理相比，FlashProve 生成证明所需的 GPU 时间多出 70 到 95 倍。它还在请求完成后以批处理方式生成证明，而不是在 Token 交付时进行验证。

> FlashProve 将证明大小缩减至约 19 MB，验证时间缩短至几秒钟

FlashProve 将证明大小缩减至约 19 MB，并将验证时间缩短至几秒钟，尽管生成这些证明的成本仍然很高，对于需要立即验证每个响应的应用程序来说不太实用。

对于那些已经[在推理支出上精打细算的开发者](https://thenewstack.io/minimax-flash-agent-costs/)来说，增加如此多的 GPU 开销对于常规 API 流量来说很难证明其合理性。

尽管如此，Anthropic 表示 FlashProve 比以往的开源系统快得多。一个名为 [VerInf](https://github.com/JamesPetrie/VerInf) 的早期系统需要 14.3 小时来生成涵盖 1,000 个 Token 的证明。生成的证明大小为 93.6 GB，验证花费了几乎一整天。

## Claude 构建，人类验证

Anthropic 将 FlashProve 的大部分开发归功于 Claude，包括使其密码学证明速度大幅加快的优化。但研究人员仍必须验证这些改进没有损害协议的安全保证。

该团队使用 [Lean](https://www.anthropic.com/research/provable-inference) 来形式化验证协议的数学属性，包括它接受有效证明、以极高概率拒绝伪造证明，并且不会泄露超出响应所透露范围的模型权重。

FlashProve 包含两个验证器：更快的 C++ 实现和由形式化证明支持的 Lean 版本。C++ 验证器通过了 Anthropic 的对比测试，但它尚未经过形式化验证。GPU 验证器也没有。

Anthropic 表示，C++ 验证器和 GPU 验证器已经过针对形式化定义协议的测试，但两者都不具备与 Lean 实现相同的数学保证。

## 为什么 FlashProve 尚未准备好投入生产

FlashProve 的上下文仍限制在 1,024 个 Token 以内。它还使用基于整数的推理和贪婪解码，而生产模型通常依赖于浮点计算和采样。

> 目前没有迹象表明 FlashProve 何时或是否会进入 Claude API。

目前没有迹象表明 FlashProve 何时或是否会进入 Claude API。Anthropic 将 [GitHub 发布](https://github.com/anthropics/FlashProve)描述为一个研究成果，该成果目前不受维护且不接受贡献。