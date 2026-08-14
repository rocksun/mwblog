<!--
title: Nvidia发布更小、更快的Nemotron模型及配套工作路由器
cover: https://cdn.thenewstack.io/media/2026/08/9d824325-img_3505-scaled.jpg
summary: Nvidia发布了轻量级Nemotron 3.5 Lightning模型及NeMo Switchyard路由库。该方案旨在通过模型组合（System of Models）策略，利用小模型的定制化能力与路由器的智能调度，在降低企业运行成本的同时，保持接近前沿模型的任务处理精度。
-->

Nvidia发布了轻量级Nemotron 3.5 Lightning模型及NeMo Switchyard路由库。该方案旨在通过模型组合（System of Models）策略，利用小模型的定制化能力与路由器的智能调度，在降低企业运行成本的同时，保持接近前沿模型的任务处理精度。

> 译自：[Nvidia launches a smaller, faster Nemotron model and a router to put it to work](https://thenewstack.io/nvidia-nemotron-lightning-switchyard/)
> 
> 作者：Frederic Lardinois

Nvidia于周二发布了Nemotron 3.5 Lightning，这是其Nemotron 3系列开源模型的最新成员。此外，该公司还推出了NeMo Switchyard，这是一个能够支持模型路由器的全新开源库。

Nemotron 3.5 Lightning是一个拥有300亿参数的专家混合（mixture-of-experts）模型，由Nemotron联盟共同开发，其推理能力已接近规模更大的Nemotron 3 Super模型。然而，在Artificial Analysis的智能指数（Intelligence Index）中，这两款Nvidia模型均落后于来自Google、规模相近的Gemma 4 31B模型。

![](https://cdn.thenewstack.io/media/2026/08/78b8abe3-artificial-analysis-intelligence-index-chart-1-nvidia-nemotron-3.5-lightning-1024x576.png)

图片来源：Nvidia。

## 为速度而生

Nvidia表示，此处的重点与其说是基准测试，不如说是速度以及轻松定制模型的能力。与类似的轻量化模型一样，其核心用例是让前沿模型负责规划和编排工作，而由较小（且可能经过微调）的模型来执行任务。

正如Nvidia高级总监Joey Conway最近向*The New Stack*透露的那样，该公司认为，毕竟这些[模型系统](https://www.youtube.com/watch?v=F96DvTrijdI)才是人工智能的未来。

在速度方面，Nvidia称3.5 Lightning的输出速度最高可提升4倍。但正如Nvidia的Kari Briski在发布会前的媒体吹风会上所指出的，Nvidia希望凭借针对特定工作流修改和优化模型的能力，使自身在竞争中脱颖而出。

![](https://cdn.thenewstack.io/media/2026/08/914bf7c9-announcing-nvidia-nemotron-3.5-lightning-1024x576.png)

图片来源：Nvidia。

## 针对专门任务的后训练

“通用智能体基准测试只是起点，但在生产环境中，重要的是任务的准确性——而这正是后训练发挥最大作用的地方，”她说。“我们让客户提前使用Lightning，以便针对专门的工作流进行定制。后训练显著提高了准确性。Lightning的表现超越了合作伙伴目前使用的开源或专有模型。”

通过与CrowdStrike、CodeRabbit等合作伙伴合作，Nvidia发现，像3.5 Lightning这样经过微调的开源模型，在执行其经过后训练的专门任务时，表现可以达到（有时甚至超过）更大的专有模型。

由于企业正变得极其关注运行前沿模型的成本，开源模型的优势便得以显现，尽管对它们进行后训练的工作并非总是简单的。

![](https://cdn.thenewstack.io/media/2026/08/259da000-customization-chart-nvidia-nemotron-3.5-lightning-1024x576.png)

图片来源：Nvidia。

然而，Nvidia认为其NeMo生态系统提供了简化这一过程所需的所有工具。在今天的另一次发布中，该公司还提供了[用于训练编码智能体的智能体强化学习完整数据集](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Terminal-Pivot-v1-nano35-release)。

任何模型系统的核心都是一个路由器，用于决定针对特定任务使用哪个模型。路由本身其实非常简单，但决策过程却很复杂。借助NeMo Switchyard，Nvidia现在提供了一个全新的开源路由库，现有的路由器和AI网关（如Kong、OpenRouter和LiteLLM）已经将其集成到各自的产品中。

“我们与生态系统合作，”Briski说。“我们是生态系统的拥护者，我们希望确保我们是集成的。我们的库已经集成到了开发者现有的工具中。”

Switchyard本身是用Rust编写的，但由于开发者通过API与其交互，它旨在无需太多额外工作即可接入现有的技术栈。开发者定义自己的模型池，然后设置路由标准和策略——并利用他们可以针对质量、延迟和成本进行调整的算法，具体取决于给定工作流的需求。

在Nvidia的内部基准测试中，一个混合了少量开源模型与Anthropic的Opus 4.8的Switchyard路由系统，在保持前沿级准确性的同时，将任务完成成本降低到了单独运行Opus的大约三分之一。

早期合作伙伴的数据也显示了类似的结果。LangChain在145个多轮Deep Agents任务中，通过仅将7%的调用路由到前沿模型，成本降低了74%（尽管准确率有6%的折损）；Ramp则表示，在内部的SWE-Bench测试中，它不仅匹配了前沿模型的性能，还降低了58%的成本，缩短了33%的运行时间。

Nemotron 3.5 Lightning现已在Hugging Face、ModelScope、OpenRouter以及作为Nvidia NIM微服务的build.nvidia.com上提供。NeMo Switchyard可在GitHub上获取，更多合作伙伴集成即将推出。

如果Nvidia的观点正确，即智能体确实将成为多个模型的集合体，那么路由器将成为实际做出成本和质量决策的层级——而Nvidia显然希望其开源、易于定制的模型能够成为那些路由器在大规模工作负载中所选择的对象。