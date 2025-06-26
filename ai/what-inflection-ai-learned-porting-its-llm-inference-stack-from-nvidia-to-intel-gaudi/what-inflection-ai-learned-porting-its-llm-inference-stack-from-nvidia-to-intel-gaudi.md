<!--
title: Inflection AI：LLM推理栈从NVIDIA到Intel Gaudi的迁移经验
cover: https://cdn.thenewstack.io/media/2025/06/1243a7c1-boitumelo-pjxdfzxtmf8-unsplash-scaled.jpg
summary: Inflection AI 将 LLM 推理堆栈从 NVIDIA GPU 迁移到 Intel Gaudi，以解决 GPU 供应短缺和价格上涨问题。通过重写不支持的 ops、优化 Eager 和 Lazy 模式执行以及使用 Profiler 进行完善，最终实现了接近性能对等的水平。
-->

Inflection AI 将 LLM 推理堆栈从 NVIDIA GPU 迁移到 Intel Gaudi，以解决 GPU 供应短缺和价格上涨问题。通过重写不支持的 ops、优化 Eager 和 Lazy 模式执行以及使用 Profiler 进行完善，最终实现了接近性能对等的水平。

> 译自：[What Inflection AI Learned Porting Its LLM Inference Stack from NVIDIA to Intel Gaudi](https://thenewstack.io/what-inflection-ai-learned-porting-its-llm-inference-stack-from-nvidia-to-intel-gaudi/)
> 
> 作者：Raghav Garg

在 Inflection AI，我们最近对我们的基础设施进行了一次重大转变：我们将 LLM 推理堆栈从 NVIDIA GPU 移植到了 Intel 的 Gaudi 加速器。 推动这一转变的原因几乎是每个企业目前都面临的问题：GPU 供应短缺、价格上涨以及不灵活的长期租赁意味着构建在 NVIDIA 硬件之上可能会限制我们以及我们客户的扩展能力。

很明显，我们需要一个更灵活的堆栈。在评估各种选项时，Intel 跃居榜首，因为它已经在全球范围内拥有最大的企业硬件足迹。这意味着，如果我们能够在 Intel 硬件上实现性能对等，企业就可以利用他们现有的数据中心投资来进行 AI 部署，而不是争夺 NVIDIA GPU 的访问权限。

这个过程并非易事，花费了数周时间和多次内核重写，但最终，我们[设法调整和优化了我们的定制](https://thenewstack.io/how-to-optimize-customer-identity-and-access-management/)推理运行时，以实现接近性能对等的水平。在解决这些问题的过程中，我们学到了一些经验，我们相信这些经验广泛适用于任何构建更灵活、更高效的推理系统的人。

## **解决不支持的 Ops**

将 AI 架构映射到底层加速器硬件是实现高效且可扩展的 AI 工作负载的关键。在迁移到 Gaudi 时，我们发现 SynapseAI（为 Intel 加速器堆栈提供支持的后端）并未完全支持 PyTorch 的全部操作（如今已超过 2,000 个操作）。 特别是，像 Pythonic（类似 numpy）张量切片和更晦涩的操作（例如 torch.triu\_indices）都不受支持。

在某些情况下，不支持的 ops 会导致段错误。在其他情况下，PyTorch 会回退到 CPU 执行，这会因 CPU 和 HPU 之间的数据传输而导致[巨大的性能损失](https://thenewstack.io/processing-large-data-sets-in-fine-grained-parallel-streams-with-sql/)。

为了解决这些挑战，我们重写了不支持或有问题的 ops，仅此一项就带来了近 15 倍的性能提升，并消除了段错误。

## **Eager 模式与 Lazy 模式执行**

Lazy 加载与 Eager 加载的二分法存在于计算的许多领域，并且许多 AI [软件和硬件堆栈都试图支持](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/)这两种模式。为了简单起见，我们首先尝试在 PyTorch 的默认 Eager 模式下运行我们的模型。虽然输出是准确的，但由于“逐个”操作执行，延迟远高于 NVIDIA。

但是，切换到 Gaudi 的默认 Lazy 模式会导致更差的性能，执行速度慢两倍。 动态操作，[例如数据相关的分支和可变](https://thenewstack.io/transparency-from-behind-the-generative-ai-curtain/)输入形状，正在破坏图，从而引入来自重新累积操作和生成新图的主机开销。

值得庆幸的是，我们看到了解决在 Lazy 模式下遇到的问题的前进道路。[解决此问题包括识别并删除导致正向传递中图形中断的每个动态操作](https://thenewstack.io/5-steps-to-identify-and-address-incident-response-gaps/)，然后集成 HPU 图。 HPU 图类似于 CUDA 图，因为它们支持直接在 HPU 上记录和重放计算图，而无需涉及主机。由于这些抽象操作作用于固定形状的输入张量，因此我们使用分桶策略和填充来处理可变输入张量形状，以匹配我们缓存的 HPU 图的形状。

通过这些优化，我们[实现了 4 倍的加速，可以与我们的模型在 NVIDIA 硬件上的性能相媲美](https://thenewstack.io/5-tips-to-achieve-performance-engineering-at-scale/)。

## **使用 Profiler 进行完善**

虽然这些模型优化提供了显着的改进，但我们希望实现更多目标。为了充分优化性能，我们利用 Habana 基于 torch 的 profiler 堆栈来了解 Gaudi 硬件在其两个主要计算引擎上的利用率：用于 GEMM 操作的 MME 和用于逐元素操作的 TPC。为了充分利用硬件，两者都需要保持繁忙状态。

最初，我们的注意力机制作为单个内核运行，因此我们与 Intel Habana 团队合作拆分了注意力块。当 MME 处理一层的矩阵乘法时，TPC 可以同时开始处理下一层。由于增加内存开销的复杂性，这是一个微妙的过程，但释放数据并行性使我们能够接近加速器的理论最大吞吐量。结合模型优化，我们的方法现在可以扩展到从 1B 到超过 100B+ 参数的模型大小。

## **面向未来的灵活架构**

进行此移植的艰苦工作的影响远远超出了仅仅使用 Gaudi。 硬件设计模式往往会在不同的加速器中重复出现，这意味着获得的见解将使我们在未来为任何新架构构建时都具有优势。

随着 AI 硬件格局的快速发展，公司不应认为 NVIDIA 是唯一可行的选择。 对我们来说，Gaudi 是对该假设的第一次真正检验，并且证明了通过对架构的正确理解，性能和灵活性不必相互对立。