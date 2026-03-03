Anthropic 的员工可能有些事情[巴不得赶紧忘掉](https://thenewstack.io/pentagon-anthropic-model-orchestration/)，但至少对于其 Claude 聊天服务而言，记忆功能似乎是当前路线图上的重中之重。上周末，该公司推出了一项新工具，允许 Claude 用户将其他 AI 提供商的[记忆导入](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude/) Claude，确保 Claude 能立即了解用户，就像他们之前使用的服务一样。

从周一开始，Claude 的记忆功能已向其免费计划用户开放。记忆此前仅是 Pro、Max、Team 和 Enterprise 付费计划用户的特有功能，Anthropic 的计划起价为每月 20 美元。

![](https://cdn.thenewstack.io/media/2026/03/7830fe4d-hcbjvtwaaaakltw.png)

图片来源：Anthropic。

记忆是一项真正有用的功能，因为它确保您无需不断地告诉模型您的工作是什么，或者文档应该采用何种格式（尽管对于复杂、重复的任务，技能和其他工具仍然更有用）。

Claude 中的记忆会在您与服务聊天时自动生成。

如果它出了错，或者您想更新它的记忆——这只是一个简单的文本文件——您也可以随时手动编辑。对于那些不乐意 Claude 记住这么多关于自己的用户，也有一个选项可以关闭该服务从聊天中生成记忆的功能。

将此功能免费化并提供轻松切换服务选项，也有助于 Anthropic 利用 Claude 当前的势头（以及部分用户中存在的[反 OpenAI 情绪](https://www.forbes.com/sites/barrycollins/2026/03/02/leaving-chatgpt-make-sure-to-do-this-before-you-cancel/)），因为无论好坏，该公司突然发现自己已进入主流。

以下是 Anthropic 建议您用于从 OpenAI 等服务导出记忆数据的提示：

```
I'm moving to another service and need to export my data. List every memory you have stored about me, as well as any context you've learned about me from past conversations. Output everything in a single code block so I can easily copy it. Format each entry as: [date saved, if available] - memory content. Make sure to cover all of the following — preserve my words verbatim where possible: Instructions I've given you about how to respond (tone, format, style, 'always do X', 'never do Y'). Personal details: name, location, job, family, interests. Projects, goals, and recurring topics. Tools, languages, and frameworks I use. Preferences and corrections I've made to your behavior. Any other stored context not covered above. Do not summarize, group, or omit any entries. After the code block, confirm whether that is the complete set or if any remain.
```

Claude iOS 版应用程序现已在美国 App Store 排名第一，正如 Anthropic 发言人指出，它在 100 多个国家/地区跻身生产力应用前十名。该公司表示，自今年年初以来，Claude 免费计划的用户增长了 60%，Pro 和 Max 计划的付费订阅者数量翻了一番。

Anthropic 无疑更愿意在不与美国国防部发生冲突的情况下达到这些位置，但它也清楚如何充分利用当前的消费者势头。毕竟，该公司长期以来一直是开发者和企业用户中的宠儿，但其在消费者中的市场份额相对较低，无法与 OpenAI 或 Google 的 Gemini 等公司匹敌。

记忆也不是第一个从付费计划转移到免费计划的功能。例如，在 2 月下旬，它还将连接器带到了免费计划中，允许用户将 Claude 连接到 Slack、Figma 和其他 150 多项服务。文件创建、技能和图像搜索服务是最近几个月也免费提供的其他功能。