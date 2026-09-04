**据报道，Nvidia已同意以129亿美元收购 Hugging Face**，这将使这家 AI 硬件领域的巨头掌管一个开发者赖以寻找和运行开源模型的平台。

[*The Information*](https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion) 周三首次报道了这笔交易，并援引了一位知情人士的消息。截至本文发布时，Nvidia 和 Hugging Face 尚未公开确认此消息。

Hugging Face 不会强迫开发者使用特定的芯片制造商，这也是此次收购引人注目的原因。其 Optimum 库不仅适用于 Nvidia 的 TensorRT-LLM，还支持来自 AMD、Intel 和 AWS 的硬件。例如 Optimum AMD 和 Optimum Intel 等项目，让开发者能够在非 Nvidia 硬件上运行 Transformers 和 Diffusers 模型。

该公司在开发者选择模型后的环节中也发挥着重要作用，包括他们能多方便地在想要使用的硬件上运行这些模型。Nvidia 面临的问题可能是：它正在购买一个价值取决于开放性和硬件中立性的平台，如果这笔收购意味着 Nvidia 硬件将获得优待，那么该平台的价值可能会降低。

> 该公司在开发者选择模型后的环节中也发挥着重要作用，包括他们能多方便地在想要使用的硬件上运行这些模型。

## Hugging Face 已经处于模型和芯片之间

Hugging Face 的业务早已超越了文件托管。借助推理端点（Inference Endpoints），开发者可以从 Hub 部署模型，而由 Hugging Face 处理底层基础设施。

这些托管部署可以运行在 AWS、Microsoft Azure 或 Google Cloud 上，但 Hugging Face 列出的大多数 GPU 选项都是 Nvidia 芯片，包括 T4、L4 和 A100。通过 Hugging Face 的开源库，开发者获得的硬件选择空间要比通过其托管服务选择的更多。

如果交易达成，Nvidia 将同时拥有这种体验的双方。

## 部署默认设置偏向 Nvidia

NIM（Nvidia 推理微服务）已经可以与托管在 Hugging Face 上的模型配合使用。开发者可以将 NIM 指向 hf:// 仓库路径，直接从 Hub 拉取模型。

拥有 Hugging Face 将使 Nvidia 有更多空间将 NIM 和 CUDA 优化容器直接引入部署体验中。Nvidia 尚未宣布将 NIM 设为默认的计划，对 AMD 和 Intel 的支持也可能维持原样。

> 拥有 Hugging Face 将使 Nvidia 有更多空间将 NIM 和 CUDA 优化容器直接引入部署体验中。

更大的问题在于长远发展。Nvidia 可能会为其自身硬件上的新模型提供更早的支持，或者使部署变得更容易。与此同时，AMD、Intel 和 AWS 可能不得不重新考虑他们愿意为竞争对手拥有的平台内维护的集成投入多少工程工作。其中一些工作最终可能会转移到其他地方。

对于开发者来说，区别可能取决于哪条路径需要的工作量更少。如果部署 Nvidia 模型所需的步骤更少，即便竞争对手的芯片没有从 Hugging Face 上消失，其吸引力也会下降。我们已经在 AI 模型与使用它们的开发者之间的层级上看到了类似的竞争，比如 [Cloudflare 正在自主构建更多的此类基础设施](https://thenewstack.io/cloudflare-ai-web-economics/)。

## 开源模型对抗定制芯片

这种张力也有助于解释为什么 Hugging Face 对 Nvidia 的价值可能远高于其收入所显示出的水平。

Nvidia 一直在扩展其自有的 Nemotron 开源模型系列，同时在整个 AI 生态系统中进行大量投资。与此同时，其一些最大的客户正在努力减少对 Nvidia 硬件的依赖。

Google 有自己的 TPU，AWS 有 Trainium，Microsoft 有 Maia。OpenAI 和 Anthropic 也在开发自己的 AI 服务器芯片。这种推动力不仅限于超大规模云厂商。本月早些时候，[五家欧洲公司承诺购买围绕尚未制造的非 Nvidia 硬件构建的 AI 计算资源](https://thenewstack.io/mistral-third-party-open-models/)——这表明市场对替代加速器的需求强劲到足以吸引远期合同。

OpenAI 本周公布了其新款 Jalapeño 加速器的结果，该芯片在大型开源权重模型上显示出 [每瓦工作效率提高了 1.5 到 1.9 倍，同时将端到端延迟降低了高达 3.6 倍](https://thenewstack.io/openai-jalapeno-inference-chip/)——尽管该芯片尚未在接近 Nvidia 规模的任何场景中部署。强大的开源模型生态系统为 Nvidia 提供了对抗这一趋势的筹码。

开源模型通常需要在非常不同的环境中运行，而 Hugging Face 帮助开发者实现了这一点。在 Hub 上找到的模型最终可能会在 Nvidia 硬件、AMD GPU 或云加速器上运行。

这种灵活性正是 Nvidia 将要购买的部分资产。如果过分将 Hugging Face 推向自己的硬件，可能会使该平台对于那些依赖它在不同系统间工作的开发者来说变得没那么好用。

人们对这些模型的兴趣也在增长。来自 DeepSeek、Moonshot AI 和 Z.ai 等公司的模型已经缩小了与专有系统之间的差距。与此同时，Hugging Face 首席执行官 Clément Delangue 在 6 月份告诉 *The Information*，该公司在 2026 年的前六个月里，付费订阅用户数量翻了一番。Delangue 后来表示，该公司“已接近盈利”。

*The Information* 预计 Hugging Face 的年化收入约为 1.5 亿美元。相对于 129 亿美元的收购价格，这意味着其估值约为营收的 86 倍。

因此，Nvidia 支付的费用将远远超过 Hugging Face 目前的业务价值。它买下的是一个开发者在想要使用开源模型时已经会去的地方，包括那些不必运行在 Nvidia 硬件上的模型。

> 它买下的是一个开发者在想要使用开源模型时已经会去的地方，包括那些不必运行在 Nvidia 硬件上的模型。

收购 Hugging Face 不会赋予 Nvidia 对开发者在上面发现的一切内容的控制权。transformers 和 diffusers 等库是开源的，Hub 上的模型仍然受其各自许可证的约束。开源许可的模型仍然可以托管在其他地方，而底层库也可以被分叉。

更难复制的是 Hugging Face 围绕它们建立的社区。开发者已经知道在哪里寻找模型，并围绕 Hub 及其集成构建了工作流。