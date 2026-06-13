
<!--
title: 编程智能体也有困惑，于是 Stack Overflow 为它们建了个家
cover: https://cdn.thenewstack.io/media/2026/06/c98b1292-graficon-stuff-g-dn3lt8e84-unsplash-scaled.jpg
summary: 面对 AI 导致的活跃度下降，Stack Overflow 推出专为 AI 编程智能体设计的协作平台。通过建立知识库和声誉机制，解决智能体重复劳动及知识无法沉淀的“短暂智能差”问题，促进 AI 间的经验共享。
-->

面对 AI 导致的活跃度下降，Stack Overflow 推出专为 AI 编程智能体设计的协作平台。通过建立知识库和声誉机制，解决智能体重复劳动及知识无法沉淀的“短暂智能差”问题，促进 AI 间的经验共享。

> 译自：[Coding agents have questions, too — so Stack Overflow built them a home](https://thenewstack.io/stack-overflow-for-agents/)
> 
> 作者：Paul Sawers

[Stack Overflow](https://stackoverflow.com/) 作为互联网软件开发者的首选故障排除地已经超过 15 年了——每当凌晨 4 点遇到生产环境危机时，这里总是能找到一群经验丰富的开发者来解决问题。然而，它所服务的受众群体正在发生变化，该平台也面临着必须跟上节奏的压力。

事实上，这种压力早已显现。*[The Pragmatic Engineer](https://www.pragmaticengineer.com/)* 通讯作者 [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/) 在 2025 年 1 月曾[思考](https://newsletter.pragmaticengineer.com/p/the-pulse-119)大语言模型（LLM）是否已让 Stack Overflow 变得不再重要，到了 5 月，他[得出结论](https://newsletter.pragmaticengineer.com/p/the-pulse-134)称该平台已近乎消亡。

Stack Overflow 自身[公开数据浏览器](https://data.stackexchange.com/stackoverflow/query/1882532/questions-per-month)的数据也印证了这一点：每月问题数量在 2014 年初达到约 28.9 万的峰值，多年来基本保持稳定，但在 2022 年底 ChatGPT 发布后出现断崖式下跌。到 2025 年底，这一数字已降至几千个——这是该平台自诞生之初以来从未见过的低点。

Orosz 指出了两种汇聚的力量：自 2014 年以来一直让开发者感到疏远的审核文化，以及在完成任务时效率更高、摩擦更少的 LLM。

“ChatGPT 更快，而且它是在 Stack Overflow 数据上训练的，所以答案质量相近，” Orosz 当时写道，“此外，与 Stack Overflow 的版主不同，ChatGPT 礼貌且乐于回答所有问题。”

关于下一步该怎么办的问题已经讨论了很久。今年 3 月，著名计算机科学家和企业家 [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng) 在他的通讯 *The Batch* 中[提出了一个想法](https://www.deeplearning.ai/the-batch/issue-344)：智能体是否可以像以前开发者在 Stack Overflow 上分享知识那样，彼此分享学习心得？事实上，他已经开始着手解决这个问题，[发布了](https://www.deeplearning.ai/the-batch/crowdsourced-context-for-coding-agents)一个名为 [Context Hub](https://github.com/andrewyng/context-hub) 的开源 CLI 工具，旨在让编程智能体获取最新的 API 文档。

大约在同一时间，[Mozilla 启动](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)了一个名为 [cq](https://github.com/mozilla-ai/cq)（即 colloquy 的缩写）的开源项目，其构想正是如此：一个共享的知识公地，智能体可以在其中查询过去的经验并贡献新的知识，而不是孤立地重复解决相同的问题。

现在，Stack Overflow 本身也进入了这个领域。公司在[周三](https://stackoverflow.blog/2026/06/10/announcing-stack-overflow-for-agents/)推出了 [Stack Overflow for Agents](https://agents.stackoverflow.com/)，这是一个优先考虑 API 的平台，将其知识共享模型扩展到了 AI 编程智能体。

## “短暂智能差”

如果任由智能体自行其是，它们没有任何机制来分享自己的发现。一个智能体可能会花费大量时间和算力来弄清楚为什么 API 会返回意外错误，却完全不知道这个修复方案早已有人知晓。当会话结束时，它所学到的一切也都随之消失。

在[本周的一篇 LinkedIn 文章](https://www.linkedin.com/feed/update/urn:li:activity:7470497718881280001/)中，Stack Overflow 首席执行官 [Prashanth Chandrasekar](https://www.linkedin.com/in/pchandrasekar/) 将此描述为“短暂智能差”（ephemeral intelligence gap）——本质上是一个重复重塑的循环，智能体在其中消耗算力来重新发现别人已经找到的解决方案。

> “这种‘短暂智能差’拖慢了进度，浪费了资源，并使人类始终处于监控模式。”

“它拖慢了进度，浪费了资源，并使人类始终处于监控模式，” Chandrasekar 写道。

## 工作原理

该平台目前处于测试阶段，围绕三种帖子类型组织，每种类型记录一种独特的知识。问题（Questions）记录未解决的问题及已尝试的方法。TIL（“Today I Learned”，今日学到）帖子记录调试追踪过程和在实际工作中发现的未公开行为；Stack Overflow 认为这是最有价值的贡献，因为它们准确捕获了模型训练数据中缺失的内容。蓝图（Blueprints）是可重用的设计模式，旨在适用于多种类似构建，并以此确立最高质量标准。

![Stack Overflow for Agents](https://cdn.thenewstack.io/media/2026/06/975701de-stack-overflow-for-agents-1024x513.png)

Stack Overflow for Agents

预期的工作流程是“搜索优先”：在尝试任务之前，智能体先查询语料库。如果答案存在，则直接使用；如果没有，且智能体解决了问题，它会在发布到 Stack Overflow 之前草拟一份帖子供人类审核。后续尝试相同问题的智能体可以反馈哪些方案有效及其适用条件，随着时间推移积累投票和验证反馈。

问责制通过 Stack Overflow 现有的声誉体系来处理。开发者使用其 Stack Overflow 凭证通过单点登录（SSO）注册其智能体，将智能体的贡献直接与其人类所有者在平台上的声誉挂钩。

人类角色本质上是一个检查点：智能体自主查询和草拟，但在没有人类协调员签署之前，没有任何内容会进入共享语料库。发布后，更广泛的社区可以像在原始平台上一样投票和验证贡献。

在宣布此次发布的一篇博客文章中，Stack Overflow 的数据科学家 [David Gibson](https://www.linkedin.com/in/davidgibsonp/) 和产品经理 [Janice Manningham](https://www.linkedin.com/in/janicemanningham/) 明确表示，这种信任架构是整个系统的核心。

> “你智能体的表现、贡献和准确性直接与你既定的人类声誉挂钩。”

“你智能体的表现、贡献和准确性直接与你既定的人类声誉挂钩，”作者写道，“通过利用这一社区信任锚点，我们确保问责制始终是生态系统的核心，防止产生糟糕的数据循环并保持纯净的内容质量。”

## 正在形成的类别

Stack Overflow 的加入为这个新兴且很大程度上仍处于实验性的领域增加了机构权重。Ng 的 Context Hub 目前在 GitHub 上拥有超过 13,000 个星标和 1,000 多个分支，采取了更窄的方法——专门专注于让智能体获取最新的 API 文档，而不是更广泛的知识交流。

Mozilla 的 cq 项目目前已有可安装的验证原型，正从开源起点朝着类似的目标构建。这两种方法并非互斥——cq 被设计为与智能体无关且可本地部署，而 Stack Overflow for Agents 则押注于基于现有社区信任的、以声誉为锚点的中心化模型。

智能体是否能产生那种让 Stack Overflow 对人类开发者不可或缺的持久且经过同行评审的知识，还有待观察。但根本问题——数百万智能体独立解决相同问题却没有任何产出——确实存在，以至于现在有多个严肃的努力都指向了这一点。