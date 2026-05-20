Google 在其年度 I/O 开发者大会上宣布了许多用于构建 Android 应用的新 AI 工具。其中包括在 AI Studio 原型设计环境中构建原生应用的能力，而 Google 专门用于构建这些应用的 IDE——Android Studio，也迎来了一系列更新。此外，Android CLI 现已发布 1.0 版本，并可在 Google 的 Antigravity 应用中使用。

> “这种灵活性让开发者能够更好地控制性能、隐私和成本，”Google 在其公告中表示。

## 选择你自己的模型

最能体现 Google 当前对开发者构建应用方式之看法的，或许是开发者现在可以在 Android Studio 内部选择使用 Gemini、OpenAI 的 GPT 或 Anthropic 的 Claude。对于那些希望使用本地模型的开发者，Gemma 4 现已可用，并且在 Android Studio 的最新 Canary 版本中，开发者可以直接从 IDE 下载，无需借助外部服务器运行。

“这种灵活性让开发者能够更好地控制性能、隐私和成本，”Google 在其公告中表示。

今年早些时候，该公司推出了 [Android 测试基准](https://developer.android.com/bench)，这是其用于测试特定模型处理 Android 开发任务表现的基准和排行榜。目前，GPT 5.5 在该排行榜中处于领先地位，GPT 5.4 和 Google 自家的 Gemini 3.1 Pro 预览版并列第二（Opus 4.7 位列第四）。目前表现最好的模型可以解决基准测试中近 75% 的测试用例。

当然，Google 更希望你使用自家的 Gemini 模型，为了增加吸引力，Google 表示 Google AI Pro 和 Ultra 订阅者将获得“Android Studio 中 Gemini 的专属容量和更高频率限制”。

## Android CLI

[Android CLI](https://developer.android.com/tools/agents/android-cli) 已经推出数周，在 I/O 大会上，Google 宣布其现已发布 1.0 稳定版。与近期许多其他 CLI 工具一样，这里的重点与其说是为了让开发者从命令行访问 Android 开发功能，不如说是为了让 AI 智能体（agents）能够访问它们。这关乎智能体优先的工作流，赋予智能体使用 Google 官方工具、技能和 Android 开发知识库的能力。

任何智能体都可以使用该 CLI，这也是 Google 在这个“[开发者零忠诚度](https://thenewstack.io/google-doesnt-care/)”时代对近期众多公告的定位之一。这意味着 Claude Code、Codex 或 Google 自家的 Antigravity 都可以使用该 CLI。

在最新版本的 CLI 工具中，Google 引入了 *`android studio`* 命令，让“你选择的智能体能够利用 Android Studio 的深层上下文能力，更好地理解并在打开的 Android 项目上执行操作，”Google 解释道。

正如 Google 还指出的那样，让智能体与 Android Studio 并行运行将使其能够更好地处理代码库，而当从智能体控制台转移到 Android Studio 时，过渡也会变得更加容易。

“通过利用新的 `android studio` 命令，开发者现在可以授予他们首选的智能体执行语义符号解析、分析文件警告、甚至渲染 Jetpack Compose 预览的能力，”Google 表示。

顺便提一下，Android Studio 现在也提供智能体技能（Agent Skills），以帮助模型针对特定项目建立专业知识。Android Studio 现已内置了用于 Android 开发和使用 Google Firebase 平台的技能。