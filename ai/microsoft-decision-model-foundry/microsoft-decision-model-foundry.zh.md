**微软于周五**在 Foundry 中推出了 Microsoft-Decision-1，此前三天 OpenAI [向所有开发者开放了其 Decisions API](https://thenewstack.io/openai-decision-models-deployment/) 的公开测试版。微软选择在阿里巴巴的 Qwen3.5-9B 模型上对该决策模型进行了后训练，而没有采用其合作伙伴 OpenAI 构建的任何模型，不过该公司计划很快将其迁移到自家的 MAI 模型以及 OpenAI 的模型上。

[Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) 的定价为每百万输入 Token 0.042 美元，输出免费，这与 TypeSafe 对 [Jev](https://thenewstack.io/typesafe-jev-system-one/) 的收费完全一致。它的发布恰逢 TypeSafe 宣布获得由 a16z 领投的 8.7 亿美元 A 轮融资，估值达到 75 亿美元的同一天。

微软比开创这一品类的这家初创公司落后了大约三周半，而在那段时间里，OpenAI、Upstage、Perplexity、Cloudflare 和 AWS 都[推出了各自的决策模型](https://thenewstack.io/decision-models-system-one/)。

TypeSafe 表示，近 30% 的财富 500 强企业已经试用了 Jev，尽管它并未透露具体名单。TypeSafe 首席执行官 [Diogo Almeida](https://www.linkedin.com/in/diogomda) 在 X 上发文称，在发布后的三周内，“29.4% 的财富 500 强企业都出现了”。

这些正是微软向其销售 Azure 的同一批公司，这使得 TypeSafe 取得的早期进展让微软难以忽视。

## 微软的第一个客户是自己

微软董事长兼首席执行官 Satya Nadella 于周五在 X 上宣布了该模型，他写道：“我们已经开始在整个微软内部对其进行测试，”四个内部团队也对此提供了支持。

Xbox Research 利用它对 10,000 多条玩家反馈进行了分类，Copilot 团队用它来评估聊天和智能体响应，值班工程师在突发事件期间用它来提取上下文，微软 Discovery 则在智能体重新规划之前用它来对实验进行评分。

微软的数据显示，对于 Xbox 而言，它的速度是 GPT-6 Sol 的 14 倍以上，成本只是其一小部分，而在 Discovery 中，其一致性高出 46 倍。

但该模型可能承担着更重大的任务。周三，该公司表示 GitHub Copilot 很快将[决定何时在本地设备上运行任务，以及何时将其发送到云端规模的模型](https://thenewstack.io/https-thenewstack-io-copilot-local-inference-routing/)，不过该公司尚未透露 Copilot 会将什么内容发送到云端。

模型路由是微软列出的 Decision-1 的用例之一，但该公司尚未透露该模型是否会为 Copilot 做出这些调用。由于要在 Copilot、GitHub 和 Xbox 之间做出路由决策，微软有动力在内部处理这些决策。

> 由于要在 Copilot、GitHub 和 Xbox 之间做出路由决策，微软有动力在内部处理这些决策。

## 决策模型变得廉价

Cognition 工程副总裁 [Jared Palmer](https://www.linkedin.com/in/jaredlpalmer/) [花费了约 95 美元的 Modal H100 计算时间](https://runtimewire.com/article/jared-palmer-kev-qwen35-decision-models)，将他的开源 Kev 模型移植到 Qwen3.5 上，Cloudflare 则在微软挑选的同一 Qwen3.5-9B 基础模型上[构建了 Clef-flash](https://blog.cloudflare.com/clef-decision-models/)。

Jev 的价格正在成为市场标准：Palmer 在 OpenRouter 上将 Kev-4B 定价为每百万输入 Token 0.042 美元，Perplexity 收费 0.02 美元，而 OpenAI 的收费则是 Jev 的两倍多。在这些价格下，来自单个决策调用的收入微乎其微，而微软更大的机会在于让智能体流量（包括围绕每个决策的生成式调用）继续通过 Foundry 运行。此外，OpenRouter 上的上架可能会将不使用 Azure 的开发者吸引到该生态系统中。

微软 CTO 办公室软件工程副总裁 [Achint Srivastava](https://www.linkedin.com/in/achint/) [介绍了 Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)，将其作为一种在“安全、受信任的环境中”将决策能力添加到现有应用程序、智能体和工作流中的方法。

## 纯文本，无权重

这表明了 Decision-1 逊色于其竞争对手的地方。其 Foundry 列表显示它接受长达 32,768 Token 的文本并返回 JSON，但它不支持图像，这与 OpenAI 的 Decisions API 以及使用视觉编码器的 Cloudflare Clef 不同。

虽然 Cloudflare [在 Apache 2.0 许可证下发布了 Clef](https://blog.cloudflare.com/clef-decision-models/)，但微软尚未宣布开源权重。AWS、Upstage 和 Ollama 也[采用了 TypeSafe 的 System One API](https://thenewstack.io/decision-models-system-one/)（现在是该品类的通用接口），但微软尚未说明 Decision-1 是否完全兼容，尽管其 Foundry 示例代码调用了 /systemone 端点。

## 对抗压力下的校准

该公司表示，Decision-1 的概率是经过校准的，这意味着在典型案例中，90% 的预测在 10 次中有 9 次应该是正确的，但对 Jev 的研究表明，当输入被编写得具有误导性时，自信的评分会偏离多远。微软自己的 Foundry 文档建议客户在自己的数据上验证校准。

> 该公司表示，Decision-1 的概率是经过校准的，这意味着在典型案例中，90% 的预测在 10 次中有 9 次应该是正确的。

在 [JevOut 预印本](https://arxiv.org/abs/2609.30243)中，南加州大学计算机科学研究员 Zixiang Xu 及其合著者发现，对上下文进行简短、听起来很自然的添加，就会使 Jev 最初正确的 508 个决策中的 312 个发生翻转。在 229 个案例中，Jev 给错误答案分配了至少 70% 的概率。在相同的测试方法下，其他三个评分系统的翻转率在 64.9% 到 73.2% 之间。

微软用八种类型的扰动测试了 Decision-1，包括重新排序的选项和释义描述，这平均改变了其 1.3% 的答案。JevOut 没有测试 Decision-1，因此目前尚不清楚该模型在面对类似攻击时的表现如何。微软也未确认 Decision-1 是否完全支持竞争对手采用的 System One API，这留下了关于互操作性以及对其置信度分数该信任多少的问题。