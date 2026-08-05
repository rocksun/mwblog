**阿里巴巴发布了 Qwen3.8-Max**，这是一个拥有 2.4 万亿参数的多模态模型，专为可能需要数天才能完成的复杂任务而设计。目前该模型已通过 QwenCloud 和阿里云模型服务（Model Studio）提供，定价为每百万输入 token 2 美元，每百万输出 token 6 美元。

[Qwen3.8-Max](https://qwen.ai/blog?id=qwen3.8&utm_content=list_content_0_alibaba_says_its_latest_qwen_ai_model_beats_moonshots_kimi_k3&j=157227&sfmc_sub=30697404&l=1227_HTML&u=11189807&mid=546014653&jb=72&utm_source=sfmc&utm_medium=email&utm_campaign=NL_fortune-tech_2026-8-3_157227&utm_term=fortune-tech&sfmc_id=30697404) 基于 Qwen3.5 架构，采用了带有混合注意力机制的稀疏混合专家（MoE）设计。尽管该模型总参数量为 2.4 万亿，但每个 token 仅激活约 950 亿个参数。

混合专家架构会根据每个任务的需要调用模型的相应部分，而不是每次都运行全部 2.4 万亿参数。据该公司称，模型权重将于下周在 Hugging Face 和 ModelScope 上发布，使其成为首个发布可下载权重的 Qwen-Max 模型。

> 该模型的混合专家架构会根据每个任务的需求调用相应部分，但这仍然给开发者留下了巨大的模型部署需求。

## 架构如何运作

即使每次仅激活 950 亿参数，完整的权重仍必须存储并分布在多个高内存 GPU 节点上。在实践中，这使得大多数开发者无法进行私有化部署，也让 Qwen3.8-Max 更适合拥有相应基础设施的大型组织和推理提供商。

> Qwen3.8-Max 是大型组织和拥有基础设施的推理提供商的可行选择。

这使得阿里巴巴在参数规模上接近 Moonshot AI 拥有 [2.8 万亿参数](https://thenewstack.io/kimi-k3-open-weight-coding/) 的新产品 Kimi K3。由于阿里巴巴持有 [Moonshot AI 36% 的股份](https://www.euronews.com/next/2026/08/03/alibabas-new-qwen-ai-claims-to-match-unsupervised-working-skills-touted-by-claude)，因此它们并非完全独立的竞争对手。Kimi K3 在发布数小时内就登顶了 Arena 的前端编码排行榜，但市场需求迅速压垮了 Moonshot 的 GPU 容量，导致公司不得不暂停新订阅。Kimi K3 的开源权重发布也遇到了同样的问题：需求在 48 小时内突破了 GPU 容量上限，其 2.8 万亿参数使私有化部署对绝大多数小型团队来说不切实际。Qwen3.8-Max 现在也进入了同样的竞争赛道。

## 其他长时间运行的演示

根据阿里巴巴的测试，Qwen3.8-Max [花费 16 天构建了一个命令行应用](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/)，[用 5 天时间复现了一篇研究论文的结果](https://the-decoder.com/alibabas-open-weight-qwen3-8-max-takes-on-long-horizon-ai-tasks-with-2-4-trillion-parameters/)，并[在大约 500 次迭代后改进了芯片设计](https://technofuzn.com/blog/qwen-3.8-max)。阿里巴巴尚未发布足够的信息供外部研究人员验证这些结果。

阿里巴巴最雄心勃勃的软件演示是让 Qwen3.8-Max 独立花费 16 天构建 [“oh-my-cli”](https://github.com/qwen-code-dev-bot/oh-my-cli)。在此期间，它进行了 [265 次提交并提交了 127 个合并请求（pull requests）](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/)，解决了 [151 个 GitHub 问题](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/)。该代码仓库及其审计追踪在 [qwen-code-dev-bot/oh-my-cli](https://github.com/qwen-code-dev-bot/oh-my-cli) 下公开，因此开发者不必仅仅依赖阿里巴巴的描述。

> 模型及其运行框架之间的区别对于长时间运行的任务至关重要。

模型及其运行框架之间的区别对于长时间运行的任务至关重要。模型决定下一步做什么，而其周围的系统则处理其他所有事务。这些部分决定了智能体（agent）是能运行 16 天，还是在 16 分钟后失败。

这种基础设施层正是 [Anthropic 收购 CI/CD 初创公司 Mendral 所要构建的东西](https://thenewstack.io/anthropic-mendral-cicd-acquihire/)，这也是 [GoDaddy 在向 AI 智能体开放注册商时学到的经验](https://thenewstack.io/godaddy-developer-platform-domains/)；护栏（guardrails）必须先行。

阿里巴巴表示，他们使用智能体可能遇到的复杂项目对 Qwen3.8-Max 进行了训练。该模型在配合 QwenWork、Claude Code、Codex、OpenClaw 和 Hermes 进行测试时表现相似。

该公司已经[发布了指南](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/)，向开发者展示如何将其连接到这些工具。开发者应该很快就能测试这一说法。Model Studio 支持 OpenAI 和 Anthropic 的 API 格式，因此团队可以将 Qwen3.8-Max 引入他们现有的编码工具中，而无需从头重构设置。

## 上下文窗口限制

在一次实验中，该模型在没有任何代码的情况下收到了“用于大模型推理的统一数据选择”（Unified Data Selection for LLM Reasoning）这篇论文。阿里巴巴称，该智能体编写了约 7,600 行代码，启动了 33 个 GPU 训练任务，并复现了论文的六个主要结果。它还测试了另外 18 个想法，并将报告的 AIME24 结果提高了 2.7 分。

在另一次测试中，Qwen3.8-Max 在约 500 次迭代中优化了一个加密电路。阿里巴巴称，该模型将设计从 [8,298 个逻辑门减少到了 678 个](https://technofuzn.com/blog/qwen-3.8-max)。在使用开源芯片设计工具 OpenROAD 运行后，物理面积减少了 81%。

这并不是一次性的编码测试。智能体必须检查每个结果，并利用它来决定下一步尝试什么。但即使是百万 token 的上下文窗口，对智能体的帮助也是有限的。开发者将希望看到 Qwen3.8-Max 是否能在项目增长时记住早期的决策和指令。

在每一步都发送近一百万个 token 会导致其他问题——而且正如[智能体 AI 的经济学所表明的那样](https://thenewstack.io/agentic-ai-token-costs/)，当自主智能体以远超人类监督会话的速率消耗 token 时，更便宜的单 token 定价并不一定会转化为更便宜的项目成本。

> 但即使是百万 token 的上下文窗口，对智能体的帮助也是有限的。开发者将希望看到 Qwen3.8-Max 是否能在项目增长时记住早期的决策和指令。

## 基准测试需要外部验证

阿里巴巴的内部基准测试显示，Qwen3.8-Max 的表现接近 Anthropic 和 OpenAI 的模型。据阿里巴巴称，它在 Terminal-Bench 2.1 上得分 86.6，而 OpenAI 的 GPT-5.6 Sol (max) 得分为 88.8。对同一基准测试进行的独立运行会为这两个模型产生略有不同的分数，因此一旦外部实验室重复这些测试，这些数据可能会发生变化。它还在 [Text Arena 中排名第五，在 Vision Arena 中排名第二](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/)。在 [阿里巴巴涵盖 31 项测试的对照表中](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/)，该模型在六项测试中领先；其余大部分测试中 Claude Fable 5 或 GPT-5.6 Sol 领先。

这些结果使 Qwen3.8-Max 成为一个强有力的竞争者，但它们还不能证明该模型可以独自维持生产级软件数周。一旦阿里巴巴发布权重，开发者就能发现 Qwen3.8-Max 在公司自身环境之外的表现如何。如果它在迁移到不同基础设施或连接到其他编码工具时性能下降，那么这比它在排行榜上的位置更能说明问题。