![在黑色背景上掠过的抽象发光数字光线与数据粒子，象征着 AI 训练循环。](https://cdn.thenewstack.io/media/2026/11/7a22998e-paris-bilal-gld2k8ozalu-unsplash-1024x768.jpg)

生产环境流量会暴露出基准测试或部署前评估无法完全揭示的失效问题。它能告诉你哪些边缘情况至关重要，以及用户真正需要什么。将这一信号转化为下一个模型版本，需要提前做出判断：究竟是需要修改模型本身，还是问题出在检索、上下文、提示词、工具或推理服务上？

修改模型权重并不能解决系统其他环节的故障。当模型确实是正确的干预位置时，[生产环境数据能够同时提升](https://thenewstack.io/ai-agent-evaluation-loop/)模型质量与经济效益。更小的模型或许能复现更昂贵模型的行为；更优质的示例或许能提高输出一致性；基于结果的奖励机制或许更契合特定任务。[对现有高性能模型进行微调优化](https://thenewstack.io/is-fine-tuning-or-prompt-engineering-the-right-approach-for-ai/)还能避免再次迁移到新一代模型。

## 依据失效模式选择技术

当更强的模型已经能够产生理想行为，而你希望用一个更小、更经济的模型来复现它时，适合采用模型蒸馏。当高质量示例能够教会模型更一致的行为时，适合采用[监督微调（SFT）](https://www.coreweave.com/products/coreweave-forge/serverless-sft?utm_source=coreweave.com&utm_medium=site)。当你可以可靠地评估输出结果，却难以事先明确指定理想回复时，则适合采用[强化学习（RL）](https://www.coreweave.com/products/coreweave-forge/serverless-rl?utm_source=coreweave.com&utm_medium=site)。

> “修改模型权重并不能解决系统其他环节的故障。当模型确实是正确的干预位置时，生产环境数据能够同时提升模型质量与经济效益。”

在模型的整个生命周期中，你可能会用到全部这三种方法。请根据工作负载中的实际证据来选择技术方案，即便这意味着要采用配置更复杂的技术。

生产环境轨迹必须转化为训练数据。[后训练](https://docs.coreweave.com/products/post-training?utm_source=coreweave.com&utm_medium=site)需要[算力与编排调度](https://www.coreweave.com/solutions/ai-model-training?utm_source=coreweave.com&utm_medium=site)，而生成的模型必须经过评估并重新投入[推理服务](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site)。这就是完成[AI 闭环](https://www.coreweave.com/blog/the-ai-loop-launch-day-is-day-one?utm_source=coreweave.com&utm_medium=site)的工作。在强化学习中，推理阶段会在训练期间生成采样轨迹（rollouts），且新权重必须在整个运行过程中持续返回到服务中。

在 [Fully Connected 2026](https://www.coreweave.com/fully-connected-2026?utm_source=coreweave.com&utm_medium=site) 大会上，我们推出了 [CoreWeave Model Distillation](https://www.coreweave.com/products/coreweave-forge/model-distillation?utm_source=coreweave.com&utm_medium=site)、基于 CoreWeave Inference 的 [CoreWeave RL Rollouts](https://docs.coreweave.com/products/inference/rl-rollouts?utm_source=coreweave.com&utm_medium=site)，以及可编程训练 API。这些工作流均集成在 [CoreWeave Forge](https://www.coreweave.com/products/coreweave-forge?utm_source=coreweave.com&utm_medium=site) 中。可编程 API 目前处于有限预览阶段，计划于 2026 年晚些时候正式发布。

## 基础模型不变时，保持数据新鲜度

CoreWeave Model Distillation 提供了一套托管工作流。[CoreWeave Agent Lens](https://www.coreweave.com/products/coreweave-forge/agent-lens?utm_source=coreweave.com&utm_medium=site) 会在应用运行期间捕获推理流量。该工作流将其转化为训练数据、重新标注薄弱输出、测试基础模型与超参数、将候选模型部署至 [Serverless Inference](https://www.coreweave.com/products/coreweave-forge/serverless-inference?utm_source=coreweave.com&utm_medium=site)，并与生产模型进行对比。

如果模型已经具备任务所需的能力，新鲜的生产数据可以在不改变你所熟悉的服务配置的前提下提升其任务契合度。在切换流量之前，请先将新版本与正在运行的模型进行对比。

[Method](https://methodfi.com/?utm_source=coreweave.com&utm_medium=site) 利用这一工作流重新优化了其已部署的模型。2024 年，该公司使用 OpenPipe 并借助 GPT-4o 的输出，训练 Llama 3.1 8B 来处理银行交互式语音应答（IVR）系统。2026 年 8 月，Method 引入了新鲜的生产数据，使用 GPT-5.6 Sol 重新标注，并训练了另一个版本。在与已部署版本的正面对比评估中，该候选模型赢得了 57.5% 的胜率。

基础模型并未改变。新鲜的生产数据加上 Forge 中的 Model Distillation，使新一轮迭代得以更快实现。57.5% 这一结果即代表新版本在正面对比评估中获胜的比例。

## 在 Python 中掌控训练配方

对于希望自主设计学习流程的团队，面向 Serverless Training 的可编程训练 API 将训练逻辑与基础设施运维分离开来。你只需编写一个 Python 循环，CoreWeave 便会管理算力及底层训练基础设施。

下面展示了如何将 RL 更新与针对已验证演示数据的周期性监督更新相结合。该示例创建了一个学习器（learner）和服务适配器（serving adapter），使用学习率为 1e-5 的 Adam 优化器，并在每一步之后将更新后的权重发布至采样器（sampler）。

```

Python
learner = await training.create_learner(model=model, lora=lora)
sampler = await serving.create_adapter(name="sampler")
optimizer = AdamConfig(learning_rate=1e-5)

for step in range(num_steps):
    trajectories = await run_agent(sampler, tasks)
    update = learner.batch()
    update.forward_backward(
        build_rl_batch(trajectories), loss="importance_sampling"
    )
    update.optim_step(optimizer=optimizer)

    if (step + 1) % sft_interval == 0:
        update.forward_backward(next_demo_batch(), loss="cross_entropy")
        update.optim_step(optimizer=optimizer)

    update.publish_weights(to=sampler)
    await update.result()

await (await learner.save_state("final")).result()
await learner.close()

```

其中的 rollout 和 batch 辅助函数仅作示意。你的智能体逻辑、奖励计算和数据准备都应放在这些辅助函数中。该循环对 RL 使用重要性采样损失，对演示数据使用交叉熵损失，然后等待更新结果。最后保存学习器状态并关闭学习器。

你可以自行决定演示数据进入循环的频率、奖励的计算方式以及训练配方的演进方式。SFT、RL 和蒸馏共享相同的训练原语，而平台则在底层运行分布式系统。

[Willow](https://willowvoice.com/?utm_source=coreweave.com&utm_medium=site) 从监督学习起步，随后加入了 RL 评分器，用于减少填充词、提高可读性并消除自我纠正的短语。这些评分器被组合成一个奖励函数。Willow 首席技术官兼联合创始人 Lawrence Liu 表示，相比已部署的模型，新模型在文本格式排版、表情符号处理以及对指令的响应速度方面均有显著提升。

## 消除强化学习中的检查点重载延迟

[RL 推理服务](https://www.coreweave.com/solutions/reinforcement-learning?utm_source=coreweave.com&utm_medium=site)需要充足的 rollout 生成能力、与正在训练的策略保持对齐，以及及时的权重更新。训练器、奖励逻辑和环境都可以保持在原位，而由 CoreWeave Inference 来处理循环中的这一部分。

[CoreWeave RL Rollouts](https://docs.coreweave.com/products/inference/rl-rollouts?_gl=1*130xxj6*_gcl_au*MTMzMTYxMjc2My4xNzg5NDkwMDE3Li0uLS4xNzkyMTU5MDIyLjMxMzA2MzQxMS4xNzkyMTU5MDIzLjE3OTIxNTkwMjI.*_ga*MTc4NDk5MDM5NC4xNzkwODc1MzU0*_ga_XKNHS53VYL*czE3OTI3MDQxOTAkbzM0JGcxJHQxNzkyNzA1NjE1JGozNyRsMCRoMjIzMzMxMQ..) 基于支持 vLLM 的 [Nvidia](https://www.nvidia.com/en-us/?utm_source=coreweave.com&utm_medium=site) Dynamo 构建。当训练器写入检查点时，该服务会将其热加载到实时部署中，同时保留正在处理的请求和端点可用性。它还会返回训练元数据：Token 对数概率（logprobs）、Token ID 以及混合专家（MoE）模型的专家路由信息。

> “当训练器写入检查点时，该服务会将其热加载到实时部署中，同时保留正在处理的请求和端点可用性。推理服务直接使用训练器当前的策略权重，从而消除了权重陈旧以及原本会阻塞下一批 rollouts 的重新部署延迟。”

检查点可以是完整快照，也可以是增量差异（delta），从而减少首次上传之后的同步开销。推理服务直接使用训练器当前的策略权重，从而消除了权重陈旧以及原本会阻塞[下一批 rollouts](https://thenewstack.io/nebius-agentic-rl-training-bottlenecks/) 的重新部署延迟。

## 分别衡量模型质量与基础设施效率

我们与 Nvidia 及 you.com 合作，通过对 Nvidia Nemotron 3.5 Lightning 进行网页搜索后训练，验证了该工作流。本次训练将 SFT 和 RL 与训练循环内的 [you.com 搜索工具](https://you.com/?utm_source=coreweave.com&utm_medium=site)结合在一起。

BrowseComp 准确率从 36.97% 的基线提升至 45.45%，相对提升幅度达 22.94%。平均工具调用次数下降了 30.24%。与此同时，将检查点热加载到实时部署中的速度比传统重新部署周期快了约 15 倍。

更优秀的搜索工具、后训练优化以及测试框架的改进共同发挥作用，提升了准确率并减少了工具调用次数。热加载则缩短了等待检查点同步所耗费的时间。如果你正试图让一个更小或更高效的模型媲美体量大一个数量级的模型，这些节省下来的训练时间同样至关重要。

## 让模型与其实验过程保持关联

[CoreWeave Forge 重新打通了生产推理](https://forge.coreweave.com/?utm_source=coreweave.com&utm_medium=site)、训练与服务部署。Model Distillation 提供了托管路径；可编程 API 让研究人员无需管理基础设施即可掌控训练循环；而 RL Rollouts 则支持团队在保留自有训练器的同时，使用 CoreWeave 进行 rollout 推理。

无服务器训练生成的模型会作为带标签的产物返回，无需单独的注册表交接即可直接进入 Serverless Inference。实验记录也会保留在旁，使训练运行、模型与最终部署始终保持关联。

> “选择一个你可以复现的失效场景，用它来指导训练方法的选择，并将候选模型与当前服务用户的生产模型进行对比。”

选择一个你可以复现的失效场景，用它来指导训练方法的选择，并将候选模型与当前服务用户的生产模型进行对比。将生产示例、评估结果和最终产物保留在一起，以便团队能够持续复用。

[CoreWeave Forge 博客](https://www.coreweave.com/blog/coreweave-forge-turn-ai-iteration-into-compounding-improvement?utm_source=coreweave.com&utm_medium=site)和[发布新闻稿](https://www.coreweave.com/news/coreweave-forge-launches-turning-the-ai-loop-production-run-into-a-better-model-and-agent?utm_source=coreweave.com&utm_medium=site)介绍了在 Fully Connected 2026 大会上推出的各项能力背景。CoreWeave 还计划进一步发布关于 Model Distillation、可编程训练 API 和 RL Rollouts 的工程技术解析。

本文[《CoreWeave 将自定义训练循环连接至模型服务》](https://thenewstack.io/coreweave-forge-training-loops/)首发于 [The New Stack](https://thenewstack.io)。