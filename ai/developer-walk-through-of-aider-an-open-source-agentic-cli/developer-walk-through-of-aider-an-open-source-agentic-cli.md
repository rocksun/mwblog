<!--
title: Aider开发者步入式教程：开源Agentic CLI
cover: https://cdn.thenewstack.io/media/2025/07/56a9cfbe-lorenzo-herrera-yp89apz2taa-unsplashb.jpg
summary: Aider是一个社区主导的开源代理CLI，通过与LLM结对编程来启动或构建项目。安装涉及Python和API密钥配置。它使用git进行代码更改，但终端控制不佳，用户体验不如最近的代理模型。总体而言，作者不推荐Aider，认为有更好的选择。
-->

Aider是一个社区主导的开源代理CLI，通过与LLM结对编程来启动或构建项目。安装涉及Python和API密钥配置。它使用git进行代码更改，但终端控制不佳，用户体验不如最近的代理模型。总体而言，作者不推荐Aider，认为有更好的选择。

> 译自：[Developer Walk-Through of Aider, an Open Source Agentic CLI](https://thenewstack.io/developer-walk-through-of-aider-an-open-source-agentic-cli/)
> 
> 作者：David Eastman

在我探索代理命令行界面 (CLI) 的旅程中，我终于找到了一个由社区主导的开源项目 [Aider](https://aider.chat/)。具有讽刺意味的是，这是最初的代理 CLI 之一，正如你将看到的，它在某种程度上显示了它的年代感。我将根据我为[代理 AI 提供的生活质量功能](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)以及我的简短测试来评估它。

电梯演讲 *“*Aider 让你与 LLM 进行结对编程，以启动一个新项目或在你现有的代码库上进行构建*”* 与我关于 [代理 CLI 在何处擅长](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) 的论点相吻合。微妙但明确地指出，大型语言模型 (LLM) 最好被视为在你的整个项目中工作的工程工具——而不是在编写代码时提供编辑帮助。

## 安装

Aider [作为 Python 项目安装](https://aider.chat/docs/install.html)。建议使用 3.8-3.13 之间的 Python：

[![](https://cdn.thenewstack.io/media/2025/07/6a4a832c-image.png)](https://cdn.thenewstack.io/media/2025/07/6a4a832c-image.png)

没有立即提到 Homebrew，所以我将启动一个虚拟环境，正如鼓励的那样。我向下移动一个目录来设置 venv：

[![](https://cdn.thenewstack.io/media/2025/07/4580d386-image-1.png)](https://cdn.thenewstack.io/media/2025/07/4580d386-image-1.png)

请注意 venv 在提示符中给你的标志性项目名称。

要完成安装，我输入以下内容：

```
> aider-install
```

然后，文档提供了来自 DeepSeek、OpenAI 和 Anthropic 的模型之间的选择。我有一个 Anthropic 的密钥，所以我将使用它。我登录并使用[控制台](https://console.anthropic.com/settings/keys)创建一个密钥。要启动 Aider，我输入：

```
> aider --model sonnet --api-key anthropic=sk..
```

话虽如此，我可以看到[使用许多其他 LLM 启动 Aider](https://aider.chat/docs/llms.html) 的方法，包括 [Ollama 自托管 LLM](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)。

我们得到了一个简单的启动会话：

[![](https://cdn.thenewstack.io/media/2025/07/cbfda785-image-2-1024x283.png)](https://cdn.thenewstack.io/media/2025/07/cbfda785-image-2-1024x283.png)

所以 Aider 运行它自己的 CLI，在本例中是在 [我的 Warp 控制台](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 中。（如果我调整终端的大小，那条绿线就不再适合宽度了。在终端中，整行并不是一个非常明智的设计。稍后 Aider 的伪终端还有其他小问题，例如重复的提示符。）

你会注意到 git 目录位于工作目录之下，这导致了一个问题，因为我没有检入这些内容。但这不是一个常见的问题。只是一个可能造成混淆的警告。

那么主模型和弱模型之间有什么区别呢？幸运的是，我能够询问 Aider。它建议较弱的模型用于简短、快速（并且希望更便宜）的交互：

* 简单的代码补全
* 基本的重构任务
* 当主模型不可用时
* 对成本敏感的操作
* 完美代码不重要的快速迭代

简而言之，主模型用于代理任务。

看看最后一个响应的结尾，我注意到它给出了成本的运行总计。这是我在我的代理生活质量功能中寻找的东西：

[![](https://cdn.thenewstack.io/media/2025/07/b28004c2-image-3-1024x118.png)](https://cdn.thenewstack.io/media/2025/07/b28004c2-image-3-1024x118.png)

列出正在使用的模型也是必要的。我没有看到任何关于权限或限制的线索。

## 标准 JSON 合并测试

与之前的 [代理 CLI 评论](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 中一样，我将使用一个简单的警告将两个 JSON 文件合并在一起。

请注意，这不代表任何形式的标准化测试（请访问 [terminal-bench](https://www.tbench.ai/) 了解类似的内容）。我只是想要一个简单但可能含糊不清的测试，我知道 LLM 可以管理，这样我们就可以看到界面是如何工作的。

Aider 有一个关注文件的概念，你可以像它说的那样“添加到聊天中”。尽管我看到它在扫描我的仓库时感到困惑，但它理解应该关注的一组文件，以便它可以将自己暂存到 git 中。

我将要做的是将我熟悉的两个城市 JSON 文件添加到当前目录，然后将它们 /add 到 Aider。我将在一个单独的标签中执行此操作：

[![](https://cdn.thenewstack.io/media/2025/07/171f4898-image-4-1024x317.png)](https://cdn.thenewstack.io/media/2025/07/171f4898-image-4-1024x317.png)

这些目录是由 Aider 添加的，我们很快就会看到原因。

和以前一样，我将使用以下请求来请求 JSON 合并：

*“请使用 updated\_cities.json 文件的内容更新 JSON 文件 original\_cities.json，但如果“image”字段不同，请更新或写入一个新的“imageintended”字段，其中包含新值。”*

## 但首先，限制

我不得不说，我无法找到关于 Aider 可能漫游到哪里的简单参考。它可以查看仓库，并且它只会认为它拥有使用 `/add` 添加的文件——这可能是因为它是在较新模型提供的强大功能（和风险）之前开发的。我添加此注释是因为，通常，在使用任何代理工具之前，你必须了解它认为允许对文件系统进行哪些更改。

现在，当我继续进行请求时，我们得到了一个明确的指示，说明了我之前提到的内容：它希望文件“添加”到“聊天”中。这应该有助于消除安全问题：

[![](https://cdn.thenewstack.io/media/2025/07/62a68641-image-5-1024x190.png)](https://cdn.thenewstack.io/media/2025/07/62a68641-image-5-1024x190.png)

然后我遇到了两个问题。首先，我没有阅读警告，即所有文件都是相对于 git 目录的，而不是当前目录。其次，我注意到它被它自己的 `.gitignore` 文件搞糊涂了。

然后我想到了发生了什么：它显然认为我的 `aider` 目录也是它的 aider 目录！一个简单的目录名称冲突。所以我重新启动了一个新目录。这也给了我使用 `--subtree-only` 标志来阻止它扫描整个仓库的机会：

[![](https://cdn.thenewstack.io/media/2025/07/4c07075c-image-6-1024x115.png)](https://cdn.thenewstack.io/media/2025/07/4c07075c-image-6-1024x115.png)

我将文件复制到新目录并将它们添加到 Aider：

[![](https://cdn.thenewstack.io/media/2025/07/202c83ae-image-7-1024x161.png)](https://cdn.thenewstack.io/media/2025/07/202c83ae-image-7-1024x161.png)

我给出了之前的请求，最后我们开始了：

[![](https://cdn.thenewstack.io/media/2025/07/48d4603f-image-8-1024x145.png)](https://cdn.thenewstack.io/media/2025/07/48d4603f-image-8-1024x145.png)

这是对它需要做什么的一个很好的总结。然后它显示了为 original\_cities.json 建议的更改的 git diff 样式。

```
<<<<<<< SEARCH
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
=======
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
>>>>>>> REPLACE
```

因为它使用了 git，所以它实际上不需要请求权限，因为它只是本地提交：

[![](https://cdn.thenewstack.io/media/2025/07/bfaf9460-image-9-1024x341.png)](https://cdn.thenewstack.io/media/2025/07/bfaf9460-image-9-1024x341.png)

当然，我没有进行任何提交，但 Aider 正确地将自己添加为合作者。

## 结论

毫无疑问，与最近的代理示例（如 Claude Code、Gemini CLI 和 Warp）相比，Aider 对终端的控制不佳。我发现 Aider 不是一个特别好的体验；或者更准确地说，它与最近的代理模型的距离是显而易见的。

然而，使用 git 使体验更有效率，即使 git 本身非常“反氛围”。当然，这是完全故意的——这个产品不是为氛围编码员设计的。我认为一些令人不舒服的行为（例如扫描整个仓库）可以通过标志来处理。

总的来说，鉴于我提到的更好的选择，我不推荐 Aider。但它是开源的，因此很容易改进。也就是说，在这一点上，Aider 感觉就像是在枪战中带着一把刀。