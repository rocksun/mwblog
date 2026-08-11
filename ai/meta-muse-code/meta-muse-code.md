<!--
title: Meta的新款编程代理虽便宜，但代价是你的数据
cover: https://cdn.thenewstack.io/media/2026/08/137e169d-egor-komarov-dtop0f0ctmi-unsplash-scaled.jpg
summary: Meta发布了低价编程代理工具Muse Code，试图通过极低的价格挑战OpenAI和Anthropic。然而，其极具吸引力的优惠定价需以共享代码数据用于模型训练为条件，这引发了业界对核心知识产权外泄的严重担忧，导致企业普遍对其持谨慎态度。
-->

Meta发布了低价编程代理工具Muse Code，试图通过极低的价格挑战OpenAI和Anthropic。然而，其极具吸引力的优惠定价需以共享代码数据用于模型训练为条件，这引发了业界对核心知识产权外泄的严重担忧，导致企业普遍对其持谨慎态度。

> 译自：[Meta’s new coding agent is cheap (but it’ll cost you your data).](https://thenewstack.io/meta-muse-code/)
> 
> 作者：Meredith Shubel

**Meta 本周发布了 [Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)**，这是其首款旨在处理复杂软件工程任务的编程代理，例如规划变更、编写代码和验证结果。这款终端编程代理采用了 Muse Spark 1.2 技术，这是本周同步发布的 [Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/) 的更新版本。Meta 表示，该版本在代码生成、调试、代码库理解和端到端开发者工作流程方面均有改进。

或许最值得注意的是 Muse Code 的预期定价，Meta 将其定位为低于 Anthropic 的 Claude Code 或 OpenAI 的 Codex。尽管如此，软件领导者们并没有排队试用，他们表示这款编程代理可能更适合个人项目和开源工作。

根据 Meta 首席 AI 官 Alexandr Wang 的说法，这是因为要获得 Muse Code 的最低价格，需要选择加入 Meta 的模型改进计划。对于许多工程负责人来说，用代码数据换取更低价格是不可接受的。

正如 [Emburse](https://www.emburse.com/) 的 CTO 兼 [Snyk](https://snyk.io/platform) 顾问 [Ken Ringdahl](https://www.linkedin.com/in/kenringdahl/) 告诉 *The New Stack* 的那样：“安全性、数据隐私和数据安全至关重要，这不是我们可以为了低成本选项而牺牲的东西。”他说：“如果我的同行中有人愿意为了节省一点点成本而做出这种妥协，我会感到非常惊讶。”

Zuckerberg 的这家巨头正在全力以赴，试图缩小与 OpenAI 和 Anthropic 之间的差距。今年 7 月初，Meta 发布了图像生成模型 Muse Image。同月下旬，它还[首次推出了 Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api)，这是其首个付费 AI 模型，标志着该公司正从开源转向专有 AI 模型，并采取激进的定价策略来压低 OpenAI 和 Anthropic 的价格。

现在看来，Meta 正在将类似的定价策略应用于 Muse Code。其按需付费的定价与 Muse Spark 1.1 相似，为每百万输入 token 1.25 美元，每百万输出 token 4.25 美元，这表明该公司希望将 Muse Code 与 Anthropic 的 Claude Code 或 OpenAI 的 Codex 区分开来，成为更便宜的替代品。

最有趣的是该代理的贡献者层级（contributor tier），Wang 在接受 [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html) 采访时表示，该层级为用户提供了“显著更低的成本”，使其“比按需付费层级便宜 10 倍以上”。但这种降价背后有一个陷阱：你的数据。Wang 说，要通过贡献者层级使用 Muse Code，开发者必须“选择加入以帮助改进模型”。

> “没有比源代码本身更重要的知识产权了，”Ringdahl 说。“我不会拿我的知识产权去赌博。”

此举让人想起早些时候的报道，即 Meta 已经[将自身工程师的代码修复用作训练数据](https://thenewstack.io/meta-metacode-engineer-training/)，用于其内部 AI 编程代理 MetaCode，甚至使用颜色徽章系统来激励更多的代码修复提交。

因此出现了不感兴趣的情况。当被问及是否愿意为了更低的价格接受数据权衡时，似乎很少有人愿意。“没有比源代码本身更重要的知识产权了，”Ringdahl 说。“我不会拿我的知识产权去赌博。”

[TestSprite](https://testsprite.com/) 的联合创始人兼 CEO [Yunhao Jiao](https://www.linkedin.com/in/yunhaojiao/) 也表达了同样的观点。他告诉 *The New Stack*，他认为 Meta 的 Muse Code 选择加入机制可能会暴露的不仅仅是公司的代码：“实际上，Meta [获取的]不仅仅是你的代码，因为在每次编码会话中，不仅仅只有代码，”他解释道，并指出开发者提示词、代理响应和开发者的修改内容。

对 Jiao 而言，风险不在于 Meta 可能如何处理这些信息，而在于这些信息未来可能会落入竞争对手手中：“也许 Meta 的模型会记住所有这些细节，在未来，当其他公司——可能是我们的竞争对手，或者其他人在做类似功能时——模型会记住所有那些细节，并轻松地帮助他们复制我们的工作。”

虽然没有证据支持 Jiao 的担忧，但目前这足以让他远离 Muse Code。

## 那么谁应该使用 Muse Code 的贡献者层级？

据 [*TechCrunch*](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/) 报道，近几个月来，由于 token 成本上升速度超过预期，多家公司缩减了 AI 编码工具的使用或引入了新的控制措施。但当被问及他是否认为企业可能会因为 Meta 更便宜的代理而倾向于扩大编码代理的使用时，Jiao 表示他的团队并不认为编码代理是一项巨大的开支——肯定不足以让他们加入 Muse Code 贡献者层级的数据共享要求。

对于那些确实想寻找最便宜编程代理的人来说，按 token 价格比较可能并不是最好的衡量标准。正如 [Archdesk](https://archdesk.com/) 的 CTO [Michał Piszczek](https://www.linkedin.com/in/michalpiszczek/) 告诉 *The New Stack* 的那样：“有用的指标是审查和修复后，每次接受更改的成本。”

像 Ringdahl 和 Jiao 一样，Piszczek 同意选择加入 Meta 的模型改进计划使得 Muse Code 不适合用于生产环境的代码，但他表示它可以在开源工作、个人项目和“一次性原型”中占有一席之地。

展望未来，他设想了一种将编码代理使用分为两个层级的设置，低风险工作可以使用更便宜的数据共享选项，而专有代码则保留给那些零数据留存的选项：“一家初创公司可以在公共工作中使用贡献者定价，并要求其核心产品零数据留存。”

Wang 告诉 CNBC，Meta “也开始接受零数据留存的请求”，这意味着该公司不会保留开发者的数据来改进其模型，但 Meta 尚未确认零数据留存何时到来。

Muse Code 现已推出测试版。