<!--
title: Agentic 编码工具的未来：Gemini CLI 试用
cover: https://cdn.thenewstack.io/media/2025/07/593eb3ab-steve-johnson-3crphyk6eju-unsplashb.jpg
summary: 文章介绍了 Google 的开源 AI 终端应用 Gemini CLI。它强调了 Agentic 应用的易用性、权限控制和会话摘要等重要特性。通过一个 JSON 文件合并的示例，展示了 Gemini CLI 在实际应用中的高效和准确性，并肯定了其作为开发工具的价值。
-->

文章介绍了 Google 的开源 AI 终端应用 Gemini CLI。它强调了 Agentic 应用的易用性、权限控制和会话摘要等重要特性。通过一个 JSON 文件合并的示例，展示了 Gemini CLI 在实际应用中的高效和准确性，并肯定了其作为开发工具的价值。

> 译自：[Expectations for Agentic Coding Tools: Testing Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)
> 
> 作者：David Eastman

在启动 Google 的开源 AI 终端应用 [Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/) 之前，让我们先看看对 Agentic 应用的 “生活质量” 期望是什么。现在我们已经有了几个这样的工具 —— [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)、[Warp](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) 和 [OpenAI Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 是其他例子 —— 我们对开发者需要它们提供什么有了更好的认识。

首先，需要在终端的命令行中轻松上手。开发者仍然是 Agentic 应用的主要目标受众，因此环境变量或选项标志是可以接受的。但直接上手至关重要。

例如，将你的 API 密钥连接到你的帐户可以通过环境变量或在网页控制台中完成。了解你何时耗尽 tokens（无论是免费赠送的还是付费购买的）现在是一个重要的衡量标准。

当我们点击开始按钮时，我们需要一个简单的会话介绍摘要，以便我们至少知道以下几点：

* 使用中的模型；
* 项目目录；
* 任何其他相关的权限或帐户信息，或者是否正在监视工作文件。

项目目录中的工作文件，其中写入了基于项目的假设并且可以被跟踪（例如 Claude.md 文件），这是一项重要的创新，可以将生命周期从会话级别转移到项目级别。

必须尊重权限边界；总的来说，我们还处于允许大型语言模型 (LLM) 更改文件以及更改位置的早期阶段。我曾说过，强迫 Vibe 程序员使用 Git 有点恶意 —— 但话说回来，如果你不计划，那么你显然是在计划失败。

向我们展示 LLM 将遵循的执行计划来满足你的请求感觉很好，但尚未被证明是必不可少的。但是，除非这样做，否则 LLM 将使用的确切策略是不透明的。一个简单的复选框列表就足够了。

显示时间、请求和使用的 tokens 的退出会话摘要非常棒。完整的帐户只能在用户页面上跟踪。

还有很多其他功能会逐渐添加到上面的列表中，但我们需要注意倒退以及真正有用的创新。

## 启动 Gemini

与所有基于云的 LLM 一样，我们必须在获得珍贵的 tokens 之前表达我们的忠诚。转到 [Google Studio](https://aistudio.google.com/apikey) 以生成密钥。目前，你每天可以获得 100 个请求（在此处查看其他层级限制 [here](https://ai.google.dev/gemini-api/docs/rate-limits#free-tier)）。

我们可以通过终端上的 npm [安装](https://github.com/google-gemini/gemini-cli) Gemini：

```shell
npm install -g @google/gemini-cli
```

接下来，将你的 API 密钥设置为环境变量 —— 我在这里在我的 MacBook 上的命令行中执行此操作：[![](https://cdn.thenewstack.io/media/2025/07/7271928f-image.png)](https://cdn.thenewstack.io/media/2025/07/7271928f-image.png)

然后输入命令 `gemini`，我们就开始了：

[![](https://cdn.thenewstack.io/media/2025/07/d059b290-image-1.png)](https://cdn.thenewstack.io/media/2025/07/d059b290-image-1.png)

正如我在上面的生活质量部分中提到的，这确实完成了指向活动模型（在本例中为 Gemini-2.5 Pro）以及反映项目目录的重要工作。

主题选择屏幕在你按下回车键后立即消失，但我假设你可以将其恢复。它在介绍屏幕上占据了相当大的空间。

与 Claude Code 类似，有一个 markdown 文件 —— 在这种情况下为 GEMINI.md —— 用于请求自定义。我不会在此帖子中使用它。

“没有沙盒” 是什么意思？坏消息是，Gemini 一开始就没有任何限制你的 AI 可能漫游的位置。恐怕这不是很明智，但 Gemini 为你提供了相当简单的选项。好消息是我们可以使用 [macOS Seatbelt](https://github.com/google-gemini/gemini-cli/blob/main/docs/sandbox.md)，它一开始就有一个明智的策略，即限制对项目目录内的访问。

因此，我将退出此会话（键入 `/quit`），我们可以使用此基本安全性重新启动。

退出屏幕提供了一些我之前提到的统计信息：

[![](https://cdn.thenewstack.io/media/2025/07/1fc29cc5-image-2-1024x471.png)](https://cdn.thenewstack.io/media/2025/07/1fc29cc5-image-2-1024x471.png)

我们可以通过在此会话中仅设置一个环境变量，然后添加一个标志来使用 Seatbelt：

[![](https://cdn.thenewstack.io/media/2025/07/85c1263f-image-3-1024x462.png)](https://cdn.thenewstack.io/media/2025/07/85c1263f-image-3-1024x462.png)

现在我们一切顺利，因为我们系好了安全带。

正如我在最近的一篇文章中对 [Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 所做的那样，让我们尝试合并两个 JSON 文件。和以前一样，我正在寻找该结构如何支持我，以及结果。如果你不想阅读之前的文章，请想象我有一个使用 JSON 数据的城市网站。我有一个名为 *original\_cities.json* 的 JSON 文件：

```json
// original_cities.json
{
  "cities": [
    {
      "id": "London",
      "text": "London is the capital of the UK",
      "image": "BigBen"
    },
    {
      "id": "Berlin",
      "text": "Great night club scene",
      "image": "Brandonburg Gate",
      "imageintended": "Reichstag"
    },
    {
      "id": "Paris",
      "text": "Held the Olympics of 2024",
      "image": "EifelTower",
    }
  ]
}
```

拼写错误和格式错误（多余的逗号）是故意的；我们想看看是否可以引诱 LLM。

我还有另一个文件，名为 *updated\_cities.json*：

```json
// updated_cities.json
{
  "cities": [
    {
      "id": "London",
      "text": "London is the capital and largest city in Great Britain",
      "image": "BigBen"
    },
    {
      "id": "Berlin",
      "text": "Great night club scene but a small population",
      "image": "BrandenburgGate",
      "imageintended": "Reichstag"
    },
    {
      "id": "Paris",
      "text": "Held the Olympics of 2024",
      "image": "NotreDame"
    },
    {
      "id": "Rome",
      "text": "The Eternal City",
      "image": "TheColleseum"
    }
  ]
}
```

我想用第二个文件的内容更新第一个文件。这模拟了稍微不同步的工作。我有一个条件：我希望将任何更新的图像引用（我可能还没有）复制到一个名为“imageintended”的键中，这样我就不会使用该数据并导致崩溃。

从本质上讲，所有合并都应该做的是将 Rome 条目添加到第一个文件，并引入新的图像引用，而不会覆盖现有的 image 键。

所以我的项目文件夹看起来像这样。请注意，我还没有创建 GEMINI.md 文件：

[![](https://cdn.thenewstack.io/media/2025/07/f804495a-image-4-1024x230.png)](https://cdn.thenewstack.io/media/2025/07/f804495a-image-4-1024x230.png)

我将使用我给 Codex 的相同请求：

*“请使用文件 updated\_cities.json 的内容更新 JSON 文件 original\_cities.json，但如果 ‘image’ 字段不同，请更新或写入一个新的 ‘imageintended’ 字段，其中包含新值”*

让我们看看它会做什么。这项任务看起来可能很具体，但实际上有点模糊，这反映了普通人的请求。

在对其项目文件感到困惑之后，它给了我一个非常好的答案：

[![](https://cdn.thenewstack.io/media/2025/07/4fd8ba33-image-5-1024x578.png)](https://cdn.thenewstack.io/media/2025/07/4fd8ba33-image-5-1024x578.png)

更新文本，添加新条目并且不覆盖 “image” 键中的任何值 —— 全部完成。它没有尝试修复无关紧要的拼写，也没有被尾随逗号弄糊涂。它也比 Codex 快得多。

我检查了文件，确实进行了更改。在它回答之前，它并没有完全制定计划，而是给了我一个相当基本的解释，说明它将做什么：

[![](https://cdn.thenewstack.io/media/2025/07/cd590cdf-image-6-1024x193.png)](https://cdn.thenewstack.io/media/2025/07/cd590cdf-image-6-1024x193.png)

由于结果完全正确，因此过程实际上并不重要。但只有通过检查意图，你才能在 LLM 采取错误的路径时真正纠正 LLM 的 “思考”。

我将退出以显示最终支出摘要：

[![](https://cdn.thenewstack.io/media/2025/07/56b65551-image-7-1024x607.png)](https://cdn.thenewstack.io/media/2025/07/56b65551-image-7-1024x607.png)

## 结论

正如我所说，这不是一个直接的 LLM 比较，但 Gemini 给了我一个高效的 Agentic 体验。我确信 Google 可以插入我提到的任何缺失的生活质量问题（特别是关于 tokens 使用的一些正在运行的统计信息），但它现在绝对可以立即投入使用。现在有越来越多的 Agentic 终端应用程序供开发人员尝试，Gemini CLI 是该列表的一个可靠补充。