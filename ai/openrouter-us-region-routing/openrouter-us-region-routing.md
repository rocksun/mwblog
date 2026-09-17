<!--
title: 中国AI模型主导OpenRouter美国流量，现可确保流量完全留美处理
cover: https://cdn.thenewstack.io/media/2026/09/fe0dcd4b-allison-saeng-5jy9qxixrky-unsplash-scaled.jpg
summary: 中国开源AI模型在OpenRouter流量中占据主导地位，引发美企对数据安全的担忧。为此，OpenRouter推出美国区域路由功能，允许企业确保AI请求完全在美境内处理，以兼顾成本优势与合规要求。
-->

中国开源AI模型在OpenRouter流量中占据主导地位，引发美企对数据安全的担忧。为此，OpenRouter推出美国区域路由功能，允许企业确保AI请求完全在美境内处理，以兼顾成本优势与合规要求。

> 译自：[Chinese AI models dominate OpenRouter's US token consumption. It can now guarantee that traffic stays entirely in the US.](https://thenewstack.io/openrouter-us-region-routing/)
> 
> 作者：Paul Sawers

大家都已经了解了开源权重模型的商业主张：企业可以下载权重、进行定制、在自己选择的基础设施上运行，并且能比使用专有模型更好地控制数据处理位置——通常成本也低得多。

此外，目前的开源权重模型被认为仅比顶尖的前沿模型落后[约四到五个月](https://thenewstack.io/open-weight-models-frontier-costs/)。全球市值最高的公司 Nvidia 正在大力押注这一未来。9 月初，[Nvidia 同意以 129 亿美元收购 Hugging Face](https://thenewstack.io/nvidia-acquires-hugging-face/)——这个庞大的“AI 界的 GitHub”托管了超过 300 万个模型——同时承诺保持该平台对不同模型、云和计算提供商的开放性。周四，Nvidia 详细介绍了[Nvidia 如何利用其自有的开源权重 Nemotron 模型](https://thenewstack.io/ai-factories-are-among-the-most-complex-systems-ever-built-nvidia-and-palantir-turn-nvidias-supply-chain-into-a-proving-ground-for-sovereign-ai/)，与 Palantir 合作管理其庞大的全球供应链。

这种能力也带来了严峻的安全问题。OpenAI 总裁 Greg Brockman 最近警告称，随着具有先进网络能力的模型可以自由下载和修改，日益强大的开源权重模型——[他特别指出了中国的 GLM-5.3](https://thenewstack.io/openai-open-weight-glm-5-3/)——可能会“显著加剧威胁态势”。

但对于通过第三方服务访问这些模型的企业来说，还有一个更切身的担忧：当他们使用这些模型时，特别是模型源自中国时，他们自己的数据去了哪里。

## 中国与开源权重因素

Hugging Face 2 月份的数据显示，来自中国开发者的模型在过去 12 个月中[占下载量的 41%](https://thenewstack.io/china-leads-open-ai-models/)，超过了美国的 36.5%。与此同时，在 [OpenRouter](https://openrouter.ai/) 上，开源权重模型目前约占美国发起的请求所消耗的 Token 的 60%，该公司指出，中国模型构成了其中的大部分。

![OpenRouter: Share of monthly tokens (Sept. '25 - Aug. '26)](https://cdn.thenewstack.io/media/2026/09/f0933dd1-openroutergraph-1024x576.png)

*OpenRouter：月度 Token 份额（2025 年 9 月至 2026 年 8 月）* *— 美国和欧盟*

这就是为什么 OpenRouter 现在为企业提供了一种为其流量设置地理围栏的方法。这个 AI 模型市场已正式向企业级客户全面开放[美国区域内路由](https://openrouter.ai/docs/guides/features/in-region-routing)，承诺通过其美国终端发送的请求将在美国境内进行解密、处理和服务——如果无法做到，则会拒绝。

该功能本身在此之前已以某种形式悄然提供，OpenRouter 在[8 月初](https://github.com/OpenRouterTeam/docs/commit/40ca0ef2ec9d1f51af3d3f54841b8f548f5d1780)更新了文档，称企业客户可按需使用美国区域内路由。值得注意的是，这不仅适用于美国，欧洲区域内路由自 2025 年 10 月起就已经提供。

OpenRouter 由前 OpenSea 首席技术官 [Alex Atallah](https://www.linkedin.com/in/alexatallah/) 于 2023 年初创立，作为拥挤的 AI 模型市场的接口，开发人员可以通过单个 API 在来自众多提供商的数百个模型之间进行切换。支付巨头 Stripe 最近[宣布计划以约 80 亿美元的价格收购](https://thenewstack.io/stripe-acquires-openrouter-tokens/)该公司，而包括 Cursor、Ramp 和 Meta 在内的许多其他公司[也在构建自己的模型路由器](https://thenewstack.io/cursor-ramp-meta-model-router/)。

模型路由器之所以现在如此热门，很大程度上是因为经济原因。开发人员过去习惯将应用程序硬编码，将所有内容发送到同一个模型，而模型路由器则可以[逐个请求做出选择](https://thenewstack.io/stripe-ramp-openrouter-router/)，将简单的任务发送给更便宜的模型，同时为确实需要它们的工作保留昂贵的前沿系统。

这种中介角色也是 OpenRouter 新的驻留控制功能成为可能的原因：它已经决定了由哪个提供商处理每个请求，现在它可以将该选择限制为在美国运营的提供商终端。

## 将中国模型保留在美国境内

在周三宣布这一新功能的[博客文章](https://openrouter.ai/blog/announcements/us-in-region-routing/)中，负责 OpenRouter 产品团队的 [Cailee Moberg](https://www.linkedin.com/in/cailee-moberg/) 指出，尽管来自 Nvidia 和 [Thinking Machines](https://thinkingmachines.ai/news/introducing-inkling/) 的美国开发模型正在推动更广泛的开源权重模型热潮，但中国模型在用量上占据主导地位，并为担心数据的企业提出了棘手的问题。

> “来自中国实验室的模型仍然占据了（开源权重模型）流量的大部分，而对这些模型的采购审批可能会很困难。”

Moberg 写道：“来自中国实验室的模型仍然占据了[开源权重模型]流量的大部分，而对这些模型的采购审批可能会很困难。”

在 2026 年的《[企业 AI 状况](https://www.deloitte.com/uk/en/issues/generative-ai/state-of-ai-in-enterprise.html)》报告中，德勤 [得出结论](https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html)称主权 AI 正在兴起，指出 77% 的企业“现在将原产国作为供应商选择的考虑因素”，而近 60% 的企业“主要使用本地供应商”构建其 AI 技术栈。

这至少部分解释了为什么 OpenRouter 现在为美国客户提供区域内路由。Moberg 列举了 [DeepSeek V4 Pro](https://thenewstack.io/deepseek-flash-pro-benchmark/)、[Kimi K3](https://thenewstack.io/kimi-k3-open-weights/) 和 [GLM 5.2](https://z.ai/blog/glm-5.2) 作为具体示例。这三个模型都可以通过美国区域内路由获得，因为 Baseten、Fireworks 和 Azure 都在美国数据中心提供服务。企业本来就可以通过自行托管或直接使用美国提供商将这些模型保留在美国境内；OpenRouter 的新路由功能使其客户无需自行管理这些部署即可获得这种驻留保证。

OpenRouter [维护着一份实时列表](https://openrouter.ai/models?region=us)，列出了符合美国区域内路由条件的模型，范围从 OpenAI 和 Anthropic 的专有前沿模型，到中国主要实验室的开源权重模型。

Moberg 继续说道：“区域内路由允许有数据驻留要求的团队从中国的开源权重模型中获得价格和性能优势。当美国或欧盟的提供商托管模型时，请求会发送给该提供商，而实验室本身并不参与。”

> “区域内路由允许有数据驻留要求的团队从中国的开源权重模型中获得价格和性能优势。”

技术变更发生在路由层。使用 OpenRouter 的标准全球终端时，请求可以由在任何区域运营的合格提供商提供服务，因此即使使用美国公司的模型，也无法保证请求本身是在美国处理的。使用 *us.openrouter.ai* 时，请求会在美国境内的 OpenRouter 基础设施上解密，并且提供商池被过滤为 OpenRouter 批准在那里运营的终端。

如果没有符合条件的美国提供商可以服务请求的模型，OpenRouter 将返回 *404 错误*。企业还可以在工作区、团队或 API 密钥级别通过 OpenRouter 的防护栏执行区域限制，而会将提示数据发送到美国境外的工具在区域终端上会被禁用。

因此，虽然这一切最终并不会改变 DeepSeek、Kimi 或 GLM 模型是在哪里开发的，但区域内路由改变了其美国客户可以被路由到的模型副本，以及在此过程中处理其提示信息的位置。