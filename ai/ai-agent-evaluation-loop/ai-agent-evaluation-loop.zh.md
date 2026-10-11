**你的智能体已上线，服务运行正常。但它的回答真的在变好吗？** 通过将生产追踪、精选数据和评估体系结合起来，你的团队可以发现故障、选择改进方案，并在新版本到达用户手中之前证明其有效性。

首次部署依然是一个里程碑。随后，棘手的问题接踵而至：我们如何保持输出的准确性并让客户满意？成本会是多少？经过几次迭代后，团队花在维护工具和协调交接上的时间，往往超过了改进应用本身的时间。

## 找出团队之间的鸿沟

试想一下，当训练模型的AI工程师将其交接给应用或站点可靠性工程（SRE）团队时，会发生什么。工程师知道“优秀”的标准是什么；而生产团队则负责运行中的服务。从那时起，他们可能会关注不同的系统。

应用追踪数据会落入专门为正常运行时间构建的仪表盘中。值班工程师看到的是一个健康的服务，而研究团队却很难了解回答质量或用户情绪。随着用户行为的变化，评估套件也会发生漂移，但没有人负责对其进行更新。为了下一次发布，研究人员、AI工程师和业务负责人不得不回到各自独立的仪表盘前。

> 值班工程师看到的是一个健康的服务，而研究团队却很难了解回答质量或用户情绪。

首先要弄清楚：谁能将生产故障转化为评估案例，谁又负责保持该案例的实效性。如果这个过程需要在不同团队之间复制上下文信息，那么你们就在交接中迷失了方向。

## 串联改进的五个阶段

[AI循环](https://www.coreweave.com/blog/the-ai-loop-launch-day-is-day-one?utm_source=coreweave.com&utm_medium=site)遵循一个熟悉的周期：运行模型或智能体、观察其行为、将信号整理为数据、改进系统、评估结果，然后重复这一过程。每个阶段都需要承载足够的上下文，以便下一个团队采取行动。

**运行**。为工作负载选择合适的模型和智能体控制框架（即模型周围的代码和工具）。捕获部署后调查行为所需的信号。

**观察**。不要只看可用性。捕获追踪信息、指标、工具使用情况以及行为反馈，以便检查智能体的决策并找出运行出错的地方。

**精选**。将生产环境中的示例转化为有用的数据集和焕然一新的评估套件。在流程中保留人工审核，并保留说明示例来源的血统关系。

> 一次发布应该展示改进了什么，而不是依赖于几个有前途的答案。

**改进**。将变更与故障进行匹配。你可以调整控制框架、切换模型，或者通过[强化学习](https://www.coreweave.com/solutions/reinforcement-learning?utm_source=coreweave.com&utm_medium=site)（RL）、[监督微调](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site)或模型蒸馏来精炼行为。明确你期望达到的质量、延迟或成本结果。

**评估**。在部署前、部署期间和部署后，将候选方案与可重复的标准进行对比。一次发布应该展示改进了什么，而不是依赖于几个有前途的答案。

## 让记录与工作同行

这些交接经验塑造了我们的[CoreWeave Forge](https://www.coreweave.com/products/coreweave-forge?utm_source=coreweave.com&utm_medium=site)方法，这是我们在上周的[Fully Connected 2026大会](https://www.coreweave.com/fully-connected-2026)上发布的。我们将其设计为在一个开发环境中将运行、观察、精选、改进和评估连接起来。[MasterClass](https://www.coreweave.com/news/coreweave-ai-cloud-platform-powers-masterclasss-ai-teaching-agents?utm_source=coreweave.com&utm_medium=site)和Canva已经开始使用Forge来完成他们的AI循环。

检验互联环境是否好用的一个标准是：你是否能将一次部署追溯到它的模型版本、评估、数据集以及生产示例。[CoreWeave Registry](https://coreweave.com/products/coreweave-forge/registry)负责管理模型、智能体和数据集；[Weights & Biases Models](https://www.coreweave.com/products/coreweave-forge/weights-and-biases-models?utm_source=coreweave.com&utm_medium=site)则追踪实验、超参数扫描、分析和自动化工作流。这些记录共同帮助团队了解发生了什么变化以及它是否改善了结果。

在可观测性方面，[CoreWeave Agent Lens](https://www.coreweave.com/products/coreweave-forge/agent-lens?utm_source=coreweave.com&utm_medium=site)能够追踪步骤、决策和工具调用，并提供对话视图和技术细节。监控系统在人工监督和精选下对实时流量进行评分。我们的[发布博客](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement)指出，Agent Lens将故障检测率提高了20%，并以一半的成本修复了问题；团队应当根据自身的工作负载来评估这些结果。

[CoreWeave Notebooks](https://www.coreweave.com/products/coreweave-forge/notebooks?utm_source=coreweave.com&utm_medium=site)为共享评估和自定义分析提供了托管的Python笔记本。[CoreWeave ARIA](https://www.coreweave.com/products/coreweave-forge/aria?utm_source=coreweave.com&utm_medium=site)负责分析运行情况、提出实验建议并推荐存储在GitHub中的代码变更。它与Weights & Biases Models的集成支持基于检测到信号的自动研究。将评估证据与任何提出的变更放在一起，以便团队能够判断结果。

[CoreWeave Sandboxes](https://www.coreweave.com/products/coreweave-forge/sandboxes?utm_source=coreweave.com&utm_medium=site)为智能体、工具调用、强化学习和评估提供隔离的中央处理器（CPU）或图形处理器（GPU）环境。CoreWeave ARIA和CoreWeave Sandboxes已全面上市；Agent Lens、Notebooks和模型蒸馏（作为CoreWeave Training的一部分）则是CoreWeave Forge中的新功能。

## 选择你的工作负载所需的改进

后训练利用生产信号来改善模型质量、延迟和成本，而无需训练集群。[Serverless SFT（监督微调）](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site)和[Serverless RL（强化学习）](https://www.coreweave.com/products/coreweave-forge/serverless-rl?utm_source=coreweave.com&utm_medium=site)让团队能够使用自己的训练方案进行实验。

对于已经在生产中得到验证的任务，[模型蒸馏](https://www.coreweave.com/products/coreweave-forge/model-distillation?utm_source=coreweave.com&utm_medium=site)会在较大模型的输出上训练一个更小、权重开源的模型。然后，它将候选模型与现有模型进行面对面的评分对比。这种对比为你决定是否转移流量提供了证据。更小的模型只有在满足任务需求时才有用。

## 将推理视作循环的一部分

每个阶段都依赖于推理，但工作负载需要不同级别的控制。[CoreWeave Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site)提供[Serverless Inference](https://www.coreweave.com/products/serverless-inference?utm_source=coreweave.com&utm_medium=site)以访问开源权重模型，并提供[Dedicated Inference](https://www.coreweave.com/products/dedicated-inference?utm_source=coreweave.com&utm_medium=site)以满足隔离基础设施上的工作负载需求。

借助[Serverless Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site)，CoreWeave负责管理基础设施。借助[Dedicated Inference](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site)，团队可以控制模型权重、部署设置和GPU资源。根据工作负载的需求进行选择；随着这些需求的发展，团队可以在这两种方法之间进行切换。

[Cline](https://cline.bot/?utm_source=coreweave.com&utm_medium=site)在其开源、开放选择的编码智能体中使用了Serverless Inference中的开源模型，我们的[发布博客](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement)描述它受到了超过1100万开发者的信任。[Grammarly](https://www.grammarly.com/?utm_source=coreweave.com&utm_medium=site)则使用具有显式GPU选择和完全托管操作的Dedicated Inference。

强化学习带来了另一个需求。策略会生成推出（rollouts）——即其行为的示例——训练会产生更新后的权重，然后这些权重会返回给服务用于下一轮。缓慢的检查点加载会拖慢整个周期。

我们在Dedicated Inference中推出的全新[RL rollouts](https://docs.coreweave.com//products/inference/rl-rollouts?utm_source=coreweave.com&utm_medium=site)功能利用NVIDIA Dynamo基础架构，以最小的停机时间热加载更新后的检查点。我们与NVIDIA及you.com的工程团队合作，在NeMo gym中使用you.com的网络搜索应用程序编程接口（API），通过RL Rollouts对NVIDIA Nemotron 3.5 Lightning进行了后训练。我们的[发布博客](https://coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement)报道称，相比基准线，模型重新加载延迟降低了15倍。

## 保持循环对你的技术栈开放

改进循环延伸到了你已经在使用的可观测性平台、数据仓库和安全技术栈。[CoreWeave Partner Network](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site)包括基础设施、数据服务、独立软件供应商（ISV）以及模型和推理，其解决方案均已在CoreWeave的生产条件下进行了测试。

这其中也包括智能体调用的工具。[Exa](https://exa.ai/?utm_source=coreweave.com&utm_medium=site)、[Parallel Web Systems](https://parallel.ai/?utm_source=coreweave.com&utm_medium=site)和[You.com](http://you.com/?utm_source=coreweave.com&utm_medium=site)通过一次集成提供了一个实时网页搜索层。搜索使智能体能够访问其训练数据之外的信息；你仍然需要观察和评估其工具调用及由此产生的回答。

我们构建[CoreWeave Forge](http://forge.coreweave.com/?utm_source=coreweave.com&utm_medium=site)是为了服务那些在CoreWeave Cloud、其他云以及私有数据中心拥有工作负载的团队。改进数据保持可移植性，各阶段之间具有开放接口，因此无论你在哪里运行，精选的数据集和评估套件都能保持实用性。

## 从一个生产故障开始

挑选一个你们团队能够理解的故障。从追踪信息开始，一路追踪到精选示例、提出的修复方案、评估和部署。记录下上下文信息消失的地方以及权责不清的地方。这为你连接整个循环提供了一个具体的切入点。

为了测试这一工作流，CoreWeave Forge提供了[30天Pro免费试用](https://id.coreweave.com/signup?utm_source=coreweave.com&utm_medium=site)，并在各个产品线提供额度。对于那些有兴趣通过直接接触CoreWeave专家和基础设施来验证生产工作负载的人，可以尝试[CoreWeave ARENA](https://www.coreweave.com/coreweave-arena?utm_source=coreweave.com&utm_medium=site)。我们的目标是让每一次部署都为你的下一步构建提供养分，并有证据证明新版本比上一个版本更好。