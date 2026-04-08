<!--
title: 开源领袖质疑 Meta 的 Alexandr Wang 是否会真正开源其 AI 模型
cover: https://cdn.thenewstack.io/media/2026/04/0ec39ed2-ekaterina-bogdan-pmjoudfslt0-unsplash-scaled.jpg
summary: Meta 计划由 Alexandr Wang 领导发布新 AI 模型，旨在通过开源构建生态以抗衡竞争对手。但开源界领袖对此持怀疑态度，担心其延续以往带有商业限制的授权模式。
-->

Meta 计划由 Alexandr Wang 领导发布新 AI 模型，旨在通过开源构建生态以抗衡竞争对手。但开源界领袖对此持怀疑态度，担心其延续以往带有商业限制的授权模式。

> 译自：[Open-source leaders question whether Meta's Alexandr Wang will truly give away its AI models](https://thenewstack.io/meta-open-source-models/)
> 
> 作者：Adrian Bridgwater

[Meta](https://thenewstack.io/meta-metaverse-developers/) 将根据开源许可证发布其选定的一系列 AI 模型。这些模型归属于 Meta 首席 AI 官 [Alexandr Wang](https://www.meta.com/media-gallery/executives/alexandr-wang/?srsltid=AfmBOoo1MtTttp2VO-hKlc2TAKZaaKTHfmLaGdJXPtncHoSrTw03hpP4) 的管辖范围。

Alexandr Wang 曾作为 19 岁的麻省理工学院学生创立了数据标注公司 [Scale AI](https://scale.com/)，并于 2025 年 6 月加入 Meta，领导该机构的 Meta 超级智能实验室 (MSL)。

Alexandr Wang 热衷于推动美国构建的 AI 技术民主化，向软件工程师提供开放访问权限，他正在延续 Meta 在开源 AI 平台开发方面的深厚底蕴。

当然，该公司在开源 AI 领域已经因其过往的工作而闻名。这包括拥有开源 AI 框架的 [Llama 生态系统](https://ai.meta.com/blog/llama-2-updates-connect-2023/)，它最初只是一个相对简陋的单一大型语言模型 (LLM)；最初开发的 [PyTorch](https://pytorch.org/)，这是一个用于构建和训练神经网络的开源机器学习框架；它创建的 [React](https://ai.meta.com/blog/llama-2-updates-connect-2023/)，一个利用声明式编程风格构建用户界面的 JavaScript 库；以及早在 2011 年发起的更广泛的 [开放计算项目 (Open Compute Project)](https://www.opencompute.org/about)。

尽管尚未确定新开源版本的发布日期，但 Meta 的举动充分说明了其在 AI 领域的更广泛战略，那么为什么现在要这样做呢？

> 我们的 [开源代码库](https://thenewstack.io/ai-slop-open-source/) 以惊人的速度增长，仅在一年内总提交量就达到了 189,719 次 —— Meta 工程团队。

关于 Meta 迄今为止在 AI 开放性方面的成功程度，舆论一直摇摆不定。最初，这家 Facebook 的母公司以坚定地支持开源而闻名，传统上一直通过其前沿模型支持广泛的开放互动。

对于 2024 年（可获得的最新数据），[Meta 工程博客](https://engineering.fb.com/2025/04/02/open-source/meta-open-source-by-the-numbers/) 指出：“[该机构的] 开源代码库以惊人的速度增长，仅在一年内总提交量就达到了 189,719 次。社区贡献者占 71,018 次，而 Meta 员工贡献了剩余的 118,701 次。”

随着所谓的“类开源” AI 阴影逐渐笼罩公司（伴随着开放版本中延迟访问和功能阉割），Meta 的 Avocado 项目 [据报道](https://www.cnbc.com/2025/12/09/meta-avocado-ai-strategy-issues.html) 已转向更具专有性质的立场，避开了其开源生态系统的同类产品。

## 专有性的谨慎

在决定开源 [一系列新 AI 模型](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/) 之前，Alexandr Wang 无疑会考虑到所有这些因素。

上述拟议中的模型组可能会表现出 Meta 其他项目的一些“类开源”污点，而扎克伯格本人将希望确保他在各个层面降低用户安全风险，以避免吃官司。就在最近的 2026 年 3 月，[Meta 声称社交媒体成瘾并非真实存在](https://www.theguardian.com/technology/2026/mar/31/meta-youtube-social-media-court-cases)，结果陪审团并不认同。

毕竟，即使是作为首席执行官，骨子里是开发者的他也只有那么几套西装和洁白的衬衫。

从软件工程师的角度来看，MasTec 的高级 AI 系统工程师 [Sid Vangala](https://www.linkedin.com/in/sid-vangala-aab7393ba/) 告诉 The New Stack，Meta 开源其即将推出的 AI 模型的部分内容的决定从根本上来说是一种生态系统战略。

“通过降低准入门槛，Meta 可以加速开发者的采用，塑造标准，并推动基础设施对其工具链的依赖，” Sid Vangala 说。“与 OpenAI 或 Anthropic 等公司的完全封闭模型不同，这种方法用短期控制换取长期影响力。对企业而言，这意味着灵活性的增加，以及在模型安全、溯源和负责任部署方面的新治理责任。”

## 是真开源，还是老调重弹？

[OpenUK](https://openuk.uk/) 的首席执行官 [Amanda Brock](https://www.linkedin.com/in/amandabrocktech/) 教授对于全球流通的大量开源模型从不缺乏见解。Amanda Brock 告诉 *The New Stack*，在她看来，这里最值得注意的因素是 Meta “计划最终”将模型开源。

“我们需要了解 Meta 在这里的真实计划，以及该公司所说的将‘开源’这些技术是什么意思，” Amanda Brock 说。“如果它是带有商业限制的‘Llama 社区许可证’的老调重弹，那么按照任何理性人的理解，它都不是开源。事实上，这种有缺陷的方法可能是 Meta 此前传言中退出更广泛开源承诺的原因。”

Amanda Brock 提醒我们，开源不是一个魔法词；它是使某些开放事物获得成功的长期公认公式，这才是最重要的。她建议，也许 Alexandr Wang 已经说服了扎克伯格，真正开源其 AI 不仅仅是做正确的事，其核心实际上在于如何真正建立牵引力，就像 DeepSeek 等中国模型那样。

[Jason Corso](https://www.linkedin.com/in/jason-corso/)，Voxel51 的联合创始人兼首席科学家，以及密歇根大学的“丰田”人工智能教授，也同意 Meta 一直是开源和开放权重模型的领导者，其中许多模型激发了创新。

然而，Jason Corso 告诉 The New Stack，开放权重模型掩盖了其训练的某些方面，导致在使用时出现盲区。

“这给 Meta 和模型采用者都带来了风险，观察 Meta 将如何以不同的方式解决这个问题将会很有趣，” Jason Corso 说。

## Meta 的消费者播种策略

根据 [Ina Fried](https://www.linkedin.com/in/inafried/) 在 [Axios](https://www.axios.com/2026/04/06/meta-open-source-ai-models) 上的文章，“Alexandr Wang 认为 Anthropic 和 OpenAI 越来越专注于向政府和企业交付其模型。相比之下，据消息人士透露，Meta 的努力重点在于消费者。Meta 希望其模型在世界范围内尽可能广泛地传播。”

Alexandr Wang 还会考虑 OpenAI 和 [Anthropic](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) 何时发布新模型；他的总算法逻辑决策树可能比我们在此概述的还要复杂。

展望近期——即使 Alexandr Wang 即将推出的新“礼盒装”模型可供选择——理性的看法是，Meta 在模型访问方面已不如以往那样开放。现在可能是采用一种新型混合方法的时机，即倡导开发者访问，但在更精心定义且可治理的边界和阈值内进行。