**周二，谷歌推出了其全新的旗舰模型 Gemini 4 Argon**，通过 Google AI Studio 向 Gemini API 付费层的开发者开放，并已上线公司的多款开发者和消费级工具。

谷歌于 9 月 30 日[宣布](https://thenewstack.io/google-gemini-4-argon/)了该模型。最初的外部访问仅限于其 Fairwind 计划中的精选网络防御者和其他受信任的测试人员；谷歌员工也在内部使用它。

## Gemini 4 Argon 定价

谷歌为该模型制定了极具竞争力的价格。在 11 月 30 日之前，开发者通过 Google AI Studio 使用该模型的促销价为每百万输入 Token 2 美元、每百万输出 Token 10 美元，输入和输出共享一个总计 100 万 Token 的额度预算。这与 OpenAI 的 GPT-6.1 Sol 价格相同。

在此之后，谷歌的新模型价格将调整为每百万 Token 4 美元（输入）和 20 美元（输出），这与 Anthropic 的 [Claude Opus 5.5](https://platform.claude.com/docs/en/about-claude/pricing) 保持一致。在促销期间，缓存的输入 Token 可享 95% 的折扣。

在促销期间，Argon 的价格也是 Anthropic 的 [Claude Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/) 和 OpenAI 的 [GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/) 收费标准的五分之一，后两者的定价均为每百万 Token 10 美元（输入）和 50 美元（输出）。

开发者可以通过谷歌的 Interactions API 调用该模型（模型名称为 `gemini-4-argon`），并且 google-genai SDK 也提供了支持。Android 开发者还可以通过 Firebase AI Logic 将其构建到他们的应用程序中。

## 输入和输出共享配额

根据谷歌的说法，Argon 统一的 [100 万 Token 输入/输出限制](https://aistudio.google.com/docs/long-decode)涵盖了输入模型的内容以及模型输出的内容。这与谷歌在 9 月 30 日最初发布 Argon 公告时的描述有明显不同。当时，谷歌将该限制称为 100 万 Token 的输出上限，高于早期 Gemini 模型的 64,000 Token。

由于现在是共享预算，情况发生了一些变化，因为一个很长的提示词（Prompt）现在会占用模型写回内容的额度。例如，如果一个请求加载了 800,000 Token 的代码，那么留给回复的额度就只有 200,000 Token 了。

相比之下，Claude Opus 5.5 将标准的 100 万 Token [上下文窗口](https://platform.claude.com/docs/en/models/overview)与 128,000 Token 的独立输出上限结合在一起。

谷歌表示，额外的空间将使 Argon 能够继续处理漫长的、多步骤的编码、科学和智能体任务。

## Gemini 4 Argon 基准测试

谷歌表示，Argon 在 [Vals 指数](https://www.vals.ai/benchmarks/vals_index)上排名第一，该指数根据金融、编码、法律和税收工作对模型进行评分，并根据各行业占美国 GDP 的份额对每个行业进行加权。

在具身推理问答（ERQA，一项物理和空间推理测试）中，谷歌报告称 Argon 的得分为 87%。这使其领先于 Claude Opus 5.5 的 82.3%、GPT-6 Astra 的 81% 以及 Claude Fable 5.1 的 74%。

![](https://cdn.thenewstack.io/media/2026/10/aac23c15-gemini4-argon-erqa-1024x667.jpg)

Gemini 4 Argon ERQA 基准测试。图片来源：Google。

彭博社[报道](https://9to5google.com/?p=732252)称，9 月 30 日，一些能够访问该模型的谷歌员工表示，它在某些编码任务（尤其是前端设计）上表现吃力。谷歌告诉彭博社，说“Gemini 4 在编码等领域的表现不佳是不准确的”。

目前，我们还没有一套完整的全新基准测试来更好地将 Argon 与其他模型进行比较。与某些其他前沿实验室一样，谷歌的公告更多地关注“使用感”而非数据。基准测试永远无法说明全部情况，但一旦听到更多消息，我们将更新这篇文章。Artificial Analysis 于 9 月 30 日[发布了一项评估](https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs)：Argon 在其智能指数上得分为 53，在测试的推理设置下与 GPT-6 Astra 相当。但是，无法保证周二发布的模型与 9 月 30 日测试的模型完全相同。

## Antigravity 中的 Argon

Argon 在何处可用有点复杂。

对于编码，谷歌还将在 [Antigravity](https://antigravity.google) 中提供 Argon，这是一个用于在编辑器、终端和浏览器中运行编码智能体的平台。Argon 可以在适用于 macOS、Windows 和 Linux 的 Antigravity 桌面应用程序以及 Antigravity CLI 中使用，但仅限于 [Google AI Ultra](https://thenewstack.io/google-ai-ultra-pricing/) 订阅者和符合条件的 Gemini Enterprise 计划。

AI Pro 订阅者可以在 Gemini 应用程序中使用 Argon，但在 Antigravity 中不能。

谷歌还将 Antigravity 的编码界面引入了 macOS 版的 Gemini 应用程序，因此用户可以在不切换工具的情况下在聊天和编码之间移动。Anthropic 和 OpenAI 对其 Claude 和 [ChatGPT/Codex 桌面应用程序](https://thenewstack.io/openais-chatgpt-desktop-linux/)做了同样的事情，但还没有人找到一种优雅的方法将这些聊天和编码工具组合成一个单一的界面。

在 Android Studio Canary 中，开发者可以从智能体工具窗口登录 Antigravity，一个新的 Android CLI 插件使智能体能够访问本地 Android 构建工具。

该公司表示，超过 10 万名谷歌员工在内部构建的 Antigravity 中每月使用 Argon。在四周的时间里，智能体提交的代码增加了 35%，而提交后的回滚减少了 30%。

谷歌表示，其一半以上的云销售团队和近一半的财务团队现在都在使用 Antigravity。

## Gemini 应用中的 Argon

谷歌 AI Pro 和 Ultra 计划的订阅者现在还可以在 Gemini 应用程序和 Search 中的 AI 模式下访问 Argon。

除了新模型外，Gemini 应用程序还获得了一个新开关，允许用户将聊天变成任务，然后在用户离开电脑后，Gemini 可以继续处理该任务。

## 网络防御者与智能体安全

谷歌还在扩大 [Fairwind](https://thenewstack.io/google-ships-its-third-gemini-flash-model-in-six-weeks/) 计划，该计划于 9 月 2 日启动，旨在为经过审查的安全团队提供早期访问其网络模型的权限。

选定的 Fairwind 合作伙伴可以在没有网络护栏的情况下访问 Argon，谷歌表示它正在向该计划启动时的 650 多个合作伙伴添加数百个新合作伙伴。

对于现在向公众开放的模型，谷歌表示它已训练 Argon 在做任何无法撤消的事情之前先与人类进行核对，并在遇到瓶颈时进行报告，而不是强行绕过。

该公司表示，在编码评估中，Argon 尝试未经授权的捷径的比例为 2%，这是所有 Gemini 模型中最低的比率（尽管 2% 仍然不是零，并且当数千个智能体协同工作时，2% 仍然有相当多的智能体可能会失控）。

谷歌还运行了一个单独的监视器，在智能体工作时读取其推理和行动，并阻止意料之外的变通方法。该公司表示它在训练期间运行了该监视器，但没有因模型的想法而对其进行惩罚，因此其推理保持可读性。

根据谷歌的说法，Argon 在 Gray Swan 的间接提示词注入基准测试中也处于领先地位，在 15 次自适应尝试中，攻击成功率为 0.7%。

开发者有直到 11 月 30 日的时间以促销价测试 Argon。在此之后，Argon 和 Opus 5.5 的每个 Token 价格将相同。