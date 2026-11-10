从周五开始，所有使用 Meta 的 Muse 智能体和 Meta AI 的用户都将获得由该公司使用其前沿模型 Muse Wonder 训练的新模型。订阅用户仍然可以获得 Wonder 本身以处理更困难的任务。

Meta 尚未为这些新模型命名，不过我们可以假设[它们的代号不涉及水果](https://www.businessinsider.com/meta-will-stop-naming-its-ai-models-after-fruit-2026-11)。该公司称它们是现有模型的“专用”版本，这些模型是“使用 Muse Wonder 训练的”。它们还附带了该公司首次随 Wonder 推出的两项功能：Active Memory（主动记忆）和 Active Focus（主动专注）。

Meta 最初于 10 月 12 日[推出了 Wonder](https://thenewstack.io/muse-wonder-claude-fable/) 以及功能更强大的 Wonder Full。Wonder 目前可以通过 [Meta Model API](https://thenewstack.io/meta-muse-spark-api/) 以及该公司的编程智能体 Muse Code 使用，而 Wonder Full 仅限于 Muse Code 的两个最贵订阅计划。

## 面向所有人的 Wonder 训练模型

[Muse 是 Meta 的个人智能体应用](https://thenewstack.io/amazon-meta-muse-block/)，于 9 月在较小的 [Muse Spark](https://thenewstack.io/meta-abandons-llama-spark/) 模型上推出，对 Meta 来说取得了一定的爆发式成功，并将个人智能体的概念引入了消费端。

与许多个人智能体不同，Muse 设有免费层级，这使其进入门槛远低于 OpenAI 的 Dots 或 Anthropic 的 Duet，后者仅向这些供应商最高定价层级的订阅者开放。

从技术的角度来看，这里也许最有趣的是，Meta 并没有简单地开发一个更小的、通用版本的 Wonder。

![](https://cdn.thenewstack.io/media/2026/11/6b69cf0c-personal-superintelligence-index_light-1024x553.png)

图片来源：Meta。

相反，该公司强调，他们是根据消费级应用（如 Muse）中重要的行为来训练新模型的。这意味着智能体必须决定何时自己工作，何时与用户核对（例如），并且能够在任务进行到一半时接受修正而不会迷失方向。

使用大模型来训练小模型，显然是 AI 实验室将前沿行为以消费级规模推向产品的一种常见方式，但 Meta 遗憾地尚未详细说明其方法。

同样值得注意的是，Meta 正在针对非常具体的用例对这些模型进行微调。

个人智能体需要能够预订餐桌并管理用户的收件箱，但为该智能体提供动力的模型不需要了解前沿模型所知道的一切。但它确实需要记住用户一周前说过的话，并且知道当网站在预订中途崩溃时如何继续运行。

这就是 Active Memory 和 Active Focus 等功能发挥作用的地方。

## “Active Memory”

Active Memory 帮助模型记住细节，并将它们从先前的对话带入新的对话中。

正如 Meta 在其公告中所写：“我们已经训练我们的模型来识别哪种类型的信息是临时的还是永久的，跨时间进行推理，并区分仍然相关的内容和已经过时的内容。”

在 Meta 的内部评估中，Muse 中的新模型在 90% 的任务中正确使用了关键上下文，高于上一模型的 76%。

![](https://cdn.thenewstack.io/media/2026/11/8daaa87a-active-memory-eval_light-1024x553.png)

图片来源：Meta。

## “Active Focus”

Active Focus 专注于当事情出问题时让模型继续处理任务。

Meta 写道：“我们在反映现实世界的各种瓶颈上训练了我们的模型，以便它们能够代表你更加努力地尝试、恢复或寻找替代方案。”在 Muse 中，该公司报告称，当这些新模型遇到意外问题时，完成常规任务的能力提高了 67%，但它没有分享基线数据。

Meta 表示，这些模型还更擅长决定何时自己工作以及何时与用户核对，并且它们可以处理任务中途的修正。

## 两个层级的模型

在 API 上，Wonder 的成本为每百万输入 Token 4 美元，每百万输出 Token 20 美元，而 Muse 也拥有免费层级，并且 Meta AI 在 WhatsApp、Instagram、Facebook 和 Messenger 内部运行。

用 Wonder 训练轻量级模型，可能是一种比为所有用户提供 Wonder 本身更便宜的触达如此多用户的方式。

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
Evaluation & 可观测性](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=meta-muse-specialized-models)