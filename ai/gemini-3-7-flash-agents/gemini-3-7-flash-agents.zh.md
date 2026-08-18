谷歌发布了新的 Gemini 模型，但不是 Gemini 3.5 Pro。Gemini 3.7 Flash 于周四发布，作为公司针对编码智能体和自动化业务工作流的新型主力模型，距离 Gemini 3.6 Flash 上线仅过去三周。

快速的更新频率可能会导致一些版本疲劳，但谷歌表示，新模型在编写代码和处理保持智能体正常运行的更长工作流方面表现更佳。谷歌不仅提升了性能，还为其提供了初始 API 价格，仅为 Gemini 3.6 Flash 原价的一半，但有一个警告：该价格将于 2027 年 1 月 1 日上涨。

> 谷歌表示，Gemini 3.7 Flash 在出现问题时不太容易卡住，并且能更好地判断何时需要在继续之前获取更多信息。

## 编码基准测试大幅跃升

谷歌表示，Gemini 3.7 Flash 在出现问题时不太容易卡住，并且能更好地判断何时需要在继续之前获取更多信息。该模型在 FrontierCode 1.1 Main 上得分为 43.6%，高于 Gemini 3.6 Flash 的 34.4%。其 DeepSWE v1.1 的得分从 49% 上升至 65.3%。这一模式呼应了之前 [DeepSeek 的小型模型超越其旗舰模型](https://thenewstack.io/deepseek-v4-flash-open-weights/) 的情况——更轻量的模型持续展现出超越其重量级的实力。WebDev Arena 的得分则有小幅增长，从 1,538 升至 1,588。

但基准测试无法展示在企业自身环境中这些模型的可靠程度。谷歌似乎专注于帮助智能体在代码库中工作而不卡住。如果 Gemini 3.7 Flash 能从一次失败的尝试中恢复并更快地达到正确结果，即使从纸面上看另一个模型更便宜，它也能节省时间和 Token。

## 思维等级控制成本

Gemini 3.7 Flash 提供了三个 thinking_level 设置：低、中、高，其中默认使用中等。

低等级适用于延迟敏感的工作，如事件响应流水线和实时聊天。中等级在速度与编码及智能体工作流所需的推理能力之间取得平衡。高等级允许模型在遇到困难的编码、数学或规划问题时，花费更多时间进行推理和使用工具。

路由智能体在低等级下可能工作得很好，而试图理清竞争条件的智能体可能需要高等级。其代价是成本：Gemini 花费在思考和调用工具上的时间越长，消耗的 Token 就越多——可以说更重要的是 [整个智能体循环中的总 Token 消耗](https://thenewstack.io/agentic-ai-token-costs/)。

Gemini 3.7 Flash 目前的定价为每百万输入 Token 0.75 美元，每百万输出 Token 3.75 美元。谷歌也将此费率应用于 Gemini 3.6 Flash 直至 12 月 31 日。2027 年 1 月 1 日，这两个费率都将翻倍，达到每百万输入 Token 1.50 美元，每百万输出 Token 7.50 美元。谷歌并非唯一一家通过积极定价来赢得开发者采用的公司——[OpenAI 最近在全球竞争加剧的情况下削减了自己的 API 成本](https://thenewstack.io/gpt-5-6-api-price-cuts/)。

折扣让团队有几个月的时间大规模测试 Gemini 3.7 Flash，但一旦价格上涨，携带大量上下文或花费更多时间推理的智能体运行成本可能会翻倍。[“空头支票”式 AI 编程时代已经结束](https://thenewstack.io/microsoft-copilot-token-budgets/)，因此围绕当前价格进行构建的团队需要为年初的价格上涨做好计划。

> “空头支票”式 AI 编程时代已经结束，因此围绕当前价格进行构建的团队需要为年初的价格上涨做好计划。

## 迁移需要实质性工作

从 Gemini 3.5 Flash、Gemini 3 Flash Preview 或 Gemini 3.1 Pro 迁移的团队还有更多工作要做。[谷歌的迁移指南](https://ai.google.dev/gemini-api/docs/latest-model)指出，他们需要移除 temperature、top_p 和 top_k，将数字型的 thinking_budget 替换为 thinking_level 设置，并舍弃 candidate_count。

开发人员还必须删除预填充的模型轮次（prefilled model turns）。谷歌建议围绕服务器端的 previous_interaction_id 标准化多轮交互。使用 generateContent API 的应用程序应确保每个 FunctionResponse 都包含相应的调用 ID 和函数名称。

这些更改是可控的，但工程师在将模型投入生产环境信任其工作之前，仍应进行测试。[可以通过所有测试的代码在触碰它的下一个 AI 智能体时仍可能崩溃](https://thenewstack.io/go-language-ai-agents/)——这提醒我们测试覆盖率和智能体可靠性并不是一回事。

## 自动化的收益仍处于早期阶段

改进不仅限于编码。Gemini 3.7 Flash 在 GDP.pdf 上的得分为 34%，高于之前的 22%，其 AutomationBench 得分从 17% 上升至 30.4%。两者都有显著的进步，尽管这并不意味着模型可以被放任不管而无需监督。

那些刚刚转向 Gemini 3.6 Flash 的团队不需要从头开始。谷歌尚未宣布任何关闭该模型的计划，这让开发人员有时间决定是否值得进行另一次迁移。

与此同时，Gemini 3.5 Pro 依然缺席。谷歌曾承诺在 6 月发布，后来表示“很快”到来，此后已开始训练 Gemini 4。这是一个 [跨越前沿实验室的常见问题](https://thenewstack.io/opus-5-agentic-coding-cost/)：开发人员正在等待的模型并不总是会在他们需要的时候出现。

> 开发人员正在等待的模型并不总是会在他们需要的时候出现。