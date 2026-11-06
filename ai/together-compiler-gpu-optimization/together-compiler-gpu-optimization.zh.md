**Together AI 正在让 AI 编码智能体致力于 GPU 代码的开发**，该代码负责运行其推理基础设施，从而实现性能调优的自动化，而这过去需要工程师进行数天或数周的手动工作。

该公司于周三推出了 [Together Compiler](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference)（Together 编译器），这是一个无需工程师指导每个实验就能生成、测试和改进 GPU 内核的系统，Together AI 表示它可以在一夜之间带来性能提升。该过程在运行过程中无需人工干预每个步骤，但它不会自行发布任何内容。

当被问及人类在多大程度上参与其中时，Together AI 告诉 *The New Stack*：“优化循环是自主进行的，”并补充说，“最后的评估和部署过程是自动化的，但必须由人类启动，他们在部署到生产环境之前会对更改进行审查。”

> “优化循环是自主进行的。最后的评估和部署过程……必须由人类启动，他们在部署到生产环境之前会对更改进行审查。”

## 为什么 GPU 内核会落后

新 AI 模型的发布速度如此之快，以至于保持推理基础设施的优化已成为一项挑战。每个模型都有不同的要求，为某个工作负载调优的 GPU 代码在另一个工作负载上可能表现不佳。

Together AI 表示，OpenRouter 80% 的流量现在来自过去三个月内发布的模型。这使得工程师不得不不断调整代码以跟上步伐；现在，Together Compiler 将大部分此类工作实现了自动化。

多个编码智能体同时运行实验，编写和测试 GPU 内核，同时共享结果以指导下一轮改进。

## 更快的测试，更多的实验

该公司还找到了一种加快测试速度的方法。Together Compiler 没有在智能体每次更改代码时重新启动推理引擎，而是保持引擎运行并加载新代码。据 Together AI 称，这将其初始化时间从大约 467 秒缩短至仅仅 9 秒。

> Together Compiler 没有在智能体每次更改代码时重新启动推理引擎，而是保持引擎运行并加载新代码。

## 解读 252 倍的说法

Together AI 表示，其编译器运行的优化实验数量是现有基于智能体系统的 252 倍。该公司告诉 *The New Stack*，它使用苹果的 RSI Inference Bench 测试工具作为基准，在相同的推理工作负载和硬件上比较了这两个系统，且仅改变了优化方法。

252 倍这个数字指的是 Together Compiler 可以运行的实验数量，与苹果的系统相比，而不是 AI 模型本身的运行速度提高了多少。

该公司另外报告称，与公布的基准配置相比，推理吞吐量提升高达 2.6 倍。这些收益取决于模型和硬件，且结果尚未得到独立验证。

更多的实验让 Together Compiler 有更多机会发现改进。由于每次测试耗时更少，智能体可以在一夜之间完成原本可能需要工程师数周手动调优的工作。

## 更好的性能，相同的成本

更快的推理并不一定意味着更低的价格。当被问及性能提升是否会转化为客户节省的成本或主要用于提高其自身的基础设施效率时，Together AI 告诉 *The New Stack*：“Together Compiler 提高了 Together AI 的基础设施效率。在相同的美元成本下，客户将获得更好的性能。”

> “在相同的美元成本下，客户将获得更好的性能。”

开发者可能会从相同的 GPU 中获得更多的工作成果，但这并不总是意味着更低的 [Token 价格](https://thenewstack.io/google-frozen-gemini-chip/)。该公司告诉 *The New Stack*，客户将以相同的成本获得更好的性能，而不是降价。

Together AI 表示，其编译器每天已经在处理数万亿个 Token。这是 [编码智能体](https://thenewstack.io/gpt-5-6-codex-user-surge/) 正在超越编写应用代码、迈入 GPU 性能优化领域的又一个迹象，工程师们则负责审查智能体现在能够在一夜之间完成的工作。

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & 可观测性](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=together-compiler-gpu-optimization)