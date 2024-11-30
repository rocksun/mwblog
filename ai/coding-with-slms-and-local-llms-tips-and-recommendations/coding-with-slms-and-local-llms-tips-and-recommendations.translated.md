# 使用 SLM 和本地 LLM 编码：技巧与建议

![使用 SLM 和本地 LLM 编码：技巧与建议的特色图片](https://cdn.thenewstack.io/media/2024/11/837bd360-gabriella-clare-marino-egxpsrg02su-unsplashb-1024x576.jpg)

虽然[GitHub Copilot 的影响](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/)以及其他主流 AI 解决方案在编码方面是不可否认的，但围绕这一整体趋势出现了许多问题。

首先，许多开发人员不太愿意将他们的代码（通常是专有的）与第三方共享。还有财务方面的问题，因为 API 成本可能会很快累积——尤其是在使用最先进的模型时。

于是出现了*本地*语言模型及其小型等效物，例如小型语言模型。开发者社区越来越关注它们的好处，所以让我们看看究竟是怎么回事。除了概念本身，我们还将介绍最佳模型、它们的好处以及这如何影响整体的 AI 辅助开发。

## 什么是本地托管的 LLM

本地托管的 LLM 是完全在本地环境中运行的先进机器学习模型。这些模型[通常拥有数十亿个参数](https://datasciencedojo.com/blog/tuning-optimizing-llm-parameters/)，提供复杂的代码生成、上下文理解和调试功能。本地部署 LLM 允许开发人员规避与云托管解决方案相关的延迟、隐私问题和订阅成本。

在本地运行 LLM 可以对模型优化和定制进行细粒度控制，这对于专门的开发环境特别有用。

此外，[在专有代码库上微调 LLM](https://huggingface.co/learn/cookbook/en/fine_tuning_code_llm_on_single_gpu) 可以实现更上下文感知的建议，这可以显著简化复杂的工作流程。能够在本地维护敏感数据还可以降低隐私风险，这使得该选项对需要遵守严格数据治理策略的企业开发人员具有吸引力。

但是，运行大型模型需要大量的硬件资源——通常是具有充足内存的多核 CPU 或 GPU——这使得它更适合那些拥有强大设置或特定性能需求的人。权衡的是一个强大且适应性强的工具，它可以在编码场景中提供深入的见解和支持。

### 什么是 SLM？

SLM，或小型语言模型，是其 LLM 对应物更轻量级的版本。它们的设计参数较少，[针对速度和效率进行了优化，而不会牺牲核心功能](https://www.salesforce.com/blog/small-language-models/)，例如代码完成和简单的上下文处理。它们不能做所有事情；但它们能做的事情，它们做得非常出色。

SLM 的小型架构也使其非常适合需要减少延迟和更小内存占用量的任务。SLM[适用于快速原型设计等场景](https://dl.acm.org/doi/10.1145/3643795.3648393)、嵌入式系统开发或在计算资源有限的机器上工作。

SLM 的主要限制是与 LLM 相比，其捕获复杂、广泛上下文的能力降低，这可能会影响其处理复杂项目或大型代码库时的性能。

尽管如此，它们仍然很有吸引力，因为专家认为手机将在几个月内能够高效地运行它们。我已经看到 SLM 使用计算机视觉[读取银行对账单](https://www.docuclipper.com/blog/how-to-read-a-bank-statement/)并将数据提交给 Freshbooks 的实验——类似的用例将会出现更多。

虽然 Google、Microsoft 和 Anthropic 关注的是作为服务分发的巨型模型，但 Apple 已成为开源 SLM 领域的领导者。他们的[OpenELM 系列旨在在移动设备上运行](https://venturebeat.com/ai/apple-releases-openelm-small-open-source-ai-models-designed-to-run-on-device/)，早期反馈表明它们能够高效地完成编码任务。

## 如何为编码选择最佳模型

选择[适合您开发的最佳本地 LLM 或 SLM](https://thenewstack.io/llm-chains-are-transforming-ai-development/) 需要结合社区见解、经验基准和个人测试。首先探索社区驱动的排行榜，这些排行榜根据速度、准确性和参数效率等各种性能指标对模型进行排名。

这些排名为理解哪些模型处于领先地位以及它们各自的社区在贡献增强和优化方面有多活跃提供了坚实的基础。然而，这仍然是一个相当稳健的观点。
下一步是看看[模型在更标准的排行榜上的表现](https://arxiv.org/abs/2403.19114)，例如：

**HumanEval**: 一个包含164个编程问题的基准测试，旨在评估LLM生成的代码的功能正确性。模型的评估基于其生成正确且可执行代码解决方案的能力。**MBPP (MultiPL-E)**: HumanEval基准测试的扩展，MBPP包含多种[编程语言](https://thenewstack.io/programming-languages/)的问题，能够评估多语言代码生成能力。它评估模型在各种编程语言中生成正确代码的能力。**BigCodeBench**: 一个综合性的基准测试，[评估LLM在43种编程语言上的代码理解和生成任务](https://arxiv.org/abs/2311.08588)和八个编码任务。它从长度、难度和效率三个维度衡量性能。**LiveCodeBench**: 一个动态的[基准测试，持续从LeetCode、AtCoder和CodeForces等平台收集新的编码问题](https://arxiv.org/abs/2403.07974)。它评估LLM的代码生成、自我修复、代码执行和测试输出预测能力，对编码能力进行全面评估。**EvoEval**: 一个基准测试套件，它通过改进现有的编码问题来创建新的挑战，评估LLM的程序综合能力。它突出了模型中潜在的过拟合问题，并提供了对其适应新编码任务能力的见解。

基准测试至关重要，但它们并非万能的。公共基准测试可以提供模型在标准化任务中性能的总体概述，但**最终测试始终是模型在您的特定开发环境中的表现**。

在您工作流程中常见任务上运行个人基准测试将有助于确定给定模型如何满足您的实际需求——无论是生成样板代码、调试遗留应用程序还是提供上下文感知的建议。考虑一下您对编码模型的要求，并提示不同的模型来完成它。定期重复此任务，并将其应用于新发布的模型。


## 最佳本地LLM编码模型
我知道“最佳”一词分量很重，但请记住，像这样的每个列表都是主观的。每个基准测试、每个测试和每个用例——它们都不同，因此对您有效的模型可能对其他人并不理想。

### DeepSeek V2.5
DeepSeek V2.5是一个开源模型，[集成了DeepSeek-V2-Chat和DeepSeek-Coder-V2-Instruct的功能](https://huggingface.co/deepseek-ai/DeepSeek-V2.5)，增强了一般的对话和编码能力。它支持长达128K个token的上下文长度，方便进行广泛的对话管理和复杂的数据处理。这使其成为大型项目的理想选择。

在评估中，DeepSeek V2.5在写作和指令遵循等任务中表现出显著的改进，在AlpacaEval 2.0和ArenaHard等基准测试中优于其前身。该模型可通过网络平台和API访问，提供简化、智能和高效的用户体验。

### Qwen2.5-Coder-32B-Instruct
Qwen2.5-Coder-32B-Instruct是一个最先进的开源代码模型，[由阿里云Qwen团队开发](https://www.alibabacloud.com/blog/alibaba-cloud-unveils-new-ai-models-and-revamped-infrastructure-for-ai-computing_601622)。它似乎与GPT-4o的编码能力相匹配，展现出强大而全面的编码能力以及良好的通用和数学技能。

该模型[支持128K个token的上下文长度，并且精通92种编程语言](https://arxiv.org/abs/2409.12186)。它在多个代码生成基准测试中取得了顶级性能，包括EvalPlus、LiveCodeBench和BigCodeBench，并且在代码修复任务中的表现与GPT-4o相当。

我也喜欢这个模型，因为它有多种量化版本，[提供0.5、1.5、3、7、14和320亿参数的版本](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)。因此，即使是使用较低规格设备的用户也可以运行它来辅助编码任务。

### Nxcode-CQ-7B-orpo
Nxcode-CQ-7B-orpo是一个针对编码任务优化的本地大型语言模型。它为简单的编码场景提供了均衡的性能，为寻求高效代码生成和理解能力的开发者提供了一个轻量级的解决方案。

有趣的是，它不是一个独立的模型——[它是Qwen/CodeQwen1.5-7B在与编码相关的高排名数据上的微调模型](https://huggingface.co/NTQAI/Nxcode-CQ-7B-orpo)，正如作者所述。
与Qwen-2.5和LLaMa 3相比，Nxcode-CQ-7B-orpo旨在有效处理基本的编码任务，使其适合不太复杂的项目。因此，它是代码相关任务和[JavaScript Web开发基础](https://thenewstack.io/top-10-javascript-seo-tricks-every-developer-should-know/)的最佳学习助手。例如，我发现它在处理更复杂的Three.js动画时表现平平。


### OpenCodeInterpreter-DS-33B
OpenCodeInterpreter-DS-33B是一个高参数模型，专注于高级代码解释和动态问题解决，[由中国科学家团队创建](https://arxiv.org/abs/2402.14658)。它擅长理解复杂的代码结构并生成复杂的代码解决方案。

与Qwen不同，该模型基于另一个模型，主要是Deepseek-coder-33b-base。它在发布后立即引起了社区的关注，[在HumanEval和MBPP上表现出色](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B)。

该模型的大参数量使其能够管理复杂的编码任务，使其成为从事需要深入代码分析和生成的复杂项目的开发人员的宝贵工具。


### Artigenz-Coder-DS-6.7B
由印度团队开发，[Artigenz-Coder-DS-6.7B专为快速代码原型设计而设计](https://huggingface.co/Artigenz/Artigenz-Coder-DS-6.7B)，提供高效的代码生成能力。虽然它可能无法与更大的模型的鲁棒性相匹配，但它为需要快速代码草稿和原型设计帮助的开发人员提供了一个实用的解决方案。

Artigenz-Coder-DS-6.7B适用于优先考虑速度和效率而不是处理高度复杂编码任务的项目。其13GB的内存占用量使其成为最易访问的编码模型之一，能够轻松地在中端硬件上运行。


## 本地LLM用于编码的缺点
最重要的是，本地模型受硬件限制。[英伟达顶级H100 GPU的价格高达40,000美元](https://sherwood.news/tech/companies-hoarding-nvidia-gpu-chips-meta-tesla/)，科技巨头囤积了价值数十亿美元的GPU，任何个人或组织都不可能与这种计算能力相匹敌。这甚至还没有提到[这些公司雇佣了最优秀的AI工程师](https://www.economist.com/business/2024/06/08/the-war-for-ai-talent-is-heating-up)并且领先于整个国家。

你仍然可以租用GPU时间来训练或微调LLM，但这仍然非常昂贵。目前，最好的希望是攒钱买一台家用服务器机架，安装几块3090显卡运行。

然后，事实是，即使数据在你的设备上也不安全。当连接到WiFi网络时，不要惊讶地看到人们[越来越警惕访问受限门户](https://www.cloudi-fi.com/blog/what-is-a-captive-portal)，因为黑客会试图窃取本地LLM数据。记住，这仍然是一个新兴领域，仍然存在我们甚至不知道的漏洞。

最后，不幸的是，Claude 3.5 Sonnet和o1-preview远远领先于任何开源的本地运行竞争对手。你无法战胜数十亿GB的VRAM[和数十亿美元的研发资金](https://www.reuters.com/technology/artificial-intelligence/openai-closes-66-billion-funding-haul-valuation-157-billion-with-investment-2024-10-02/)。然而，目标不是击败它——而是提供一个开源、免费且可定制的工具，开发人员可以可靠且一致地使用它，对吧？


## 结论
许多人认为本地LLM和SLM是未来编码助手的方向。Copilot、ChatGPT和Claude可能有数百亿美元的资金支持，但你将永远受制于他人的软件、限制、审查制度，当然还有数据中心问题。

另一方面，本地托管模型完全私密，不需要与第三方共享代码。此外，你不会受制于云或API预算的限制。

那么，问题是什么呢？好吧，这些LLM不仅在性能方面不如人意，而且它们也不如Copilot这样的现成的、无需代码的编码助手直观，也更难微调。然而，我们已经接近主流模型的性能，苹果和Meta等公司也正在将他们的努力集中在开源上。令人兴奋的时代即将到来。

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)