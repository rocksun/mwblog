
<!--
title: OpenAI Codex与Claude Code的代码能力测评
cover: https://cdn.thenewstack.io/media/2025/06/568ececc-ruhan-shete-4lkn72w4czg-unsplashb.jpg
summary: 文章介绍了 OpenAI Codex，一个基于云的软件工程代理，并将其与 Claude Code 和 Google Jules 进行了比较。文章展示了如何使用 Codex 更新 JSON 文件，并赞扬了 Codex 在合并文件、提供注释和处理模糊请求方面的能力。文章还提到了 Codex 与其他智能代理的不同之处，以及对 OpenAI 未来发展的猜测。
-->

文章介绍了 OpenAI Codex，一个基于云的软件工程代理，并将其与 Claude Code 和 Google Jules 进行了比较。文章展示了如何使用 Codex 更新 JSON 文件，并赞扬了 Codex 在合并文件、提供注释和处理模糊请求方面的能力。文章还提到了 Codex 与其他智能代理的不同之处，以及对 OpenAI 未来发展的猜测。

> 译自：[Testing OpenAI Codex and Comparing It to Claude Code](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/)
> 
> 作者：David Eastman

这个月对“智能代理”产品来说真是意义非凡。 我在使用 [Claude Code 的一篇文章](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 中获得了良好的体验，然后将其与 [Google Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/) 进行了比较。 同时，您可以在其他地方阅读有关新的 [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) 的信息，我稍后将介绍 Warp 的“智能代理开发环境”。

但在这篇文章中，我将介绍 [OpenAI Codex](https://openai.com/codex/)，它于上个月发布，OpenAI 将其描述为“基于云的软件工程代理”。 与我提到的其他产品一样，Codex 在命令行中工作，而不是在编辑器中。

Codex 没有“氛围编码器”可能需要的各种花哨功能； 事实上，它很可能纯粹被认为是经验丰富的开发人员的工具。

## 从 OpenAI Codex CLI 开始

让我们启动这个“实验性”项目 —— [目前仍然只是一个 GitHub 页面](https://github.com/openai/codex/blob/main/README.md) —— 使用一个非常简单的 npm 包。

在某些方面，Codex 更加“朴实”，因为它要求您将 API 密钥直接绑定到环境变量中：

```shell
export OPENAI\_API\_KEY="your-api-key-here"
```

您可以在[此处](https://platform.openai.com/settings/organization/api-keys)找到您的 OpenAI 密钥。 它会很长。 您还可以使用设置文件。

要启动交互式会话，只需使用命令 `codex`:

[![](https://cdn.thenewstack.io/media/2025/06/a70d1f83-image-1024x308.png)](https://cdn.thenewstack.io/media/2025/06/a70d1f83-image-1024x308.png)

实际上，它比 Claude Code 等智能代理竞争对手拥有更好的起始摘要，因为它立即声明它会提出建议并在执行任何[破坏性](https://help.openai.com/en/articles/11096431-openai-codex-cli-getting-started)操作之前寻求批准。 我们还可以看到模型和工作目录 —— 它似乎不需要或不需要上下文文件。 键入“Exit”将让您离开。

## 更新 JSON 内容

我的任务只是更新一个 JSON 文件与另一个 JSON 文件的内容。 这是基于我最近与一位同事遇到的问题，因为我们没有在 git 上共享 JSON 文件，所以我们突然有点不同步。

JSON 文件只是一组键/值对。 有些人将键称为名称字段。 在下面的示例中，该文件仅保存城市信息（一些文本和图像），并且有一个“id”键允许直接比较。 将这些条目视为网站的数据。

有趣的细微差别是，“image”键可能指向一个真实的资源，因此我没有直接使用新的图像引用（可能还不存在）更新它，而是要求我的同事创建一个“imageintended”键来保存图像更新。

当然，理解模糊的人类描述是 LLM 面临的挑战之一。 如果 LLM 总是需要精确的输入，那么开发民主的梦想将会破灭，因为始终需要有一位经验丰富的开发人员在场。 JSON 数据并非专门设计用于以这种方式进行比较，因此必须小心谨慎。

好的，现在设置 JSON 文件。 我在工作目录中创建了第一个写得很差的 *original\_cities.json* 文件：

```json
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

请注意巴黎条目中的尾随逗号，以及“EifelTower”的拼写错误 —— 即使它只是一个图像名称。 另请注意柏林图像名称的拼写和不良格式。

这是 *updated\_cities.json* 文件：

```json
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

请注意，图像名称已更正，但这表示它无法再引用原始图像。

现在这是我对 Codex 的粗略请求：

*“请使用 updated\_cities.json 文件的内容更新 JSON 文件 original\_cities.json，但如果“image”字段不同，请更新或写入一个新的“imageintended”字段，并使用新值代替”*

换句话说，更新后的内容很好，但保留图像名称，因为更新此图像可能会导致问题。

在思考这个问题时，我收到了大量的权限请求，主要是针对 `sed` 命令：

[![](https://cdn.thenewstack.io/media/2025/06/50ec83c7-image-1-1024x185.png)](https://cdn.thenewstack.io/media/2025/06/50ec83c7-image-1-1024x185.png)

当然，这假设我知道 `sed` 命令会做什么！ 最后，它生成了一个补丁：

[![](https://cdn.thenewstack.io/media/2025/06/4f2992ae-image-2-790x1024.png)](https://cdn.thenewstack.io/media/2025/06/4f2992ae-image-2-790x1024.png)

然后它完成了：

[![](https://cdn.thenewstack.io/media/2025/06/3498833d-image-3-1024x578.png)](https://cdn.thenewstack.io/media/2025/06/3498833d-image-3-1024x578.png)

它确实正确地修改了 original\_cities.json 文件：

```json
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
      "image": "Brandonburg Gate",
      "imageintended": "BrandenburgGate"
    },
    {
      "id": "Paris",
      "text": "Held the Olympics of 2024",
      "image": "EifelTower",
      "imageintended": "NotreDame"
    },
    {
      "id": "Rome",
      "text": "The Eternal City",
      "image": "TheColleseum"
    }
  ]
}
```

## 结论

Claude Code 实际上搞砸了这件事，但 Codex 不仅很好地完成了合并，而且还提供了一组非常好的注释，说明了它为什么这样做。

它修复了细微的格式错误，但没有被英语拼写错误弄糊涂，并且理解了保留图像引用的需要。 然而，它清楚地理解了它正在进行的更改 —— 这些注释巧妙地提到了目的。

在思考过程中，它多次要求获得许可，正如我们知道的那样。

与 Claude Code 不同，它并没有完全创建一个透明的计划来遵循。 它只是输出了一堆 `sed` 命令，但这些命令在执行时显然足够好。 这使得从氛围编码的角度来看，它更难控制，因为不熟悉代码的人需要知道会发生什么。

我想知道这是否是一个更大产品的原型，或者 OpenAI 是否会暂时让位于 Anthropic、Google 和 Warp —— 在推出自己对完美智能代理体验的看法之前，先磨练它的实验。