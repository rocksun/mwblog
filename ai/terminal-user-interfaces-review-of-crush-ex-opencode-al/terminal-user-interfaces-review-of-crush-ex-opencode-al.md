<!--
title: 终端用户界面：Crush (前OpenCode Al) 评测
cover: https://cdn.thenewstack.io/media/2025/08/a6a37561-marko-brecic-b-uijdf_pzk-unsplashb.jpg
summary: Crush 是一个基于 Go 的开源 CLI 应用程序，通过 TUI 将 AI 辅助引入终端，用于编码任务和调试。它支持多种模型，可以添加自定义语言服务器协议。安装简便，但 Warp 终端存在一些问题。尽管UI尚不完善，但具有创新性。
-->

Crush 是一个基于 Go 的开源 CLI 应用程序，通过 TUI 将 AI 辅助引入终端，用于编码任务和调试。它支持多种模型，可以添加自定义语言服务器协议。安装简便，但 Warp 终端存在一些问题。尽管UI尚不完善，但具有创新性。

> 译自：[Terminal User Interfaces: Review of Crush (Ex-OpenCode Al)](https://thenewstack.io/terminal-user-interfaces-review-of-crush-ex-opencode-al/)
> 
> 作者：David Eastman

我最初想看看 OpenCode 的 Agentic 命令行界面 (CLI)，但现在它已更名为 [Crush](https://github.com/charmbracelet/crush?tab=readme-ov-file)。 鉴于该存储库仅在 2025 年 7 月 29 日更换了所有者，因此本文的标题反映了最近的过渡。

所以：Crush 是一个基于 Go 的开源 CLI 应用程序，它将 AI 辅助引入您的终端。 它提供了一个终端用户界面 (TUI)，用于与各种 AI 模型交互，以帮助完成编码任务、调试等。 或者正如他们所说：“您新的最佳编码伙伴。”

[![](https://cdn.thenewstack.io/media/2025/08/2c5c79f2-image.png)](https://cdn.thenewstack.io/media/2025/08/2c5c79f2-image.png)

[Charm](https://charm.land/)，我想就像制作漂亮的（或俗气的，取决于你的品味）文本用户界面一样。

既然[我最近写了关于 TUI 的文章](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)，我应该指出这个项目在底层使用了 [BubbleTea](https://github.com/charmbracelet/bubbletea) 项目。 Crush 是多模型的，并且基于会话，因此您可以从各种大型语言模型 (LLM) 中进行选择或添加您自己的模型，并且您可以在会话中切换 LLM，同时保留上下文。

您还可以大致以与编辑器相同的方式添加您自己的语言服务器协议。

## 安装

与某些条目不同，它很高兴通过 homebrew 安装。 因为我使用的是我的 MacBook M4，所以我选择该选项：

[![](https://cdn.thenewstack.io/media/2025/08/6ae5dcf5-image-1.png)](https://cdn.thenewstack.io/media/2025/08/6ae5dcf5-image-1.png)

虽然 Crush 会在第一次运行时询问有关密钥的信息，但我们可以通过环境变量设置我们想要使用的 LLM。 让我们为来自 [Anthropic](https://console.anthropic.com/settings/keys) 的新密钥执行此操作：

[![](https://cdn.thenewstack.io/media/2025/08/3fda7959-image-2.png)](https://cdn.thenewstack.io/media/2025/08/3fda7959-image-2.png)

支持多种模型：预期的模型，以及一些我不知道的模型，包括“Groq”（[与 Grok 无关](https://www.byteplus.com/en/topic/404694?title=does-elon-musk-own-groq)）。 但它也包括 Grok。

输入“crush”即可开始：

[![](https://cdn.thenewstack.io/media/2025/08/471052aa-image-3-1024x788.png)](https://cdn.thenewstack.io/media/2025/08/471052aa-image-3-1024x788.png)

虽然显然拾取了我的 Anthropic 密钥，但我可以从几个模型中进行选择。 我选择了 [Opus 4，因为我熟悉它](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)。 （GPT-5 现在应该可用）。

如果它看不到 Crush 配置文件，它会询问是否可以初始化：

[![](https://cdn.thenewstack.io/media/2025/08/cc46b1ab-image-4-1024x344.png)](https://cdn.thenewstack.io/media/2025/08/cc46b1ab-image-4-1024x344.png)

这是一种非常好的方法，既可以让您在代码库中入门，又可以创建上下文文件。 旁注：虽然使用“yep”和“nope”等非正式语言很有趣，但如果英语不是您的文化语言，这有点对抗性。

从 Crush 中引导到我的项目中很尴尬，因为它在 Crush 中为 OS 命令应用了额外的权限：

[![](https://cdn.thenewstack.io/media/2025/08/102203ad-image-5-1024x349.png)](https://cdn.thenewstack.io/media/2025/08/102203ad-image-5-1024x349.png)

上面，我输入了 `ls` 并得到了回复，然后尝试了 `cd ..`，这导致了权限切换，以检查我是否真的想要移动目录。

## 权限

这确实巧妙地引导我们检查 Crush 如何处理权限。 最初，我想知道它是否可以更改项目目录之外的内容。 但我认为这尚未表达（该项目绝不成熟）。 如果您查看 `crush.json` 配置文件，您可以操作熟悉的“allow”列表：

```
{ 
  "$schema": "https://charm.land/crush.json", 
  "permissions": { 
     "allowed_tools": [ 
       "view", 
       "ls", 
       "grep", 
       "edit" 
     ] 
  } 
}
```

这些条目解释了我上面看到的行为。 您可以使用 `--yolo` 标志跳过所有权限。 （是的，您很可能感觉到这个项目有一种特殊的无忧无虑的氛围。）

## 处理项目

我让它处理我的主 Unity 开发目录，看看 [CRUSH.md](http://CRUSH.md) 会是什么样子以及它的行为如何：

[![](https://cdn.thenewstack.io/media/2025/08/4db3d691-image-6-1024x125.png)](https://cdn.thenewstack.io/media/2025/08/4db3d691-image-6-1024x125.png)

它还在寻找要合并的任何 Cursor 或 Copilot 指令。 我假设它最终会为更多提供程序指令文件执行此操作。 实际上，第一个传递代理会查找配置、测试和项目文件。

底部的命令行包括一个退出命令，这是一个很好的简单添加。 请注意，由于我在 Warp 终端中运行，因此某些命令将被它吞噬。 但这是一个[终端内的终端仿真中的常见问题](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)。 另一个例子是，我不能在使用 Warp 时使用鼠标放置光标来编写命令。 我也无法复制文本。 或复制上一个命令。

我曾以为项目处理已经完成，但没有 [CRUSH.md](http://CRUSH.md) 文件——实际上我用完了~~新黄金~~令牌，所以我补充了 Anthropic 控制台中的仪表。 我删除了 `.crush` 目录并让它再次尝试。 这次它完成了，构建了一个简洁的 CRUSH.md 文件，并将其添加到了 .gitignore 文件中：

[![](https://cdn.thenewstack.io/media/2025/08/0c075d77-image-7-1024x157.png)](https://cdn.thenewstack.io/media/2025/08/0c075d77-image-7-1024x157.png)

为了进行测试，我将要求它在策略集合中生成一个新类。 这与我的正常测试有点不同，但实际上是我需要在我的游戏项目中做的事情。 我将使用一些短语来强制 LLM 拾取项目中的上下文，但总的来说，这并不需要太多的工作。 我只是想基于一种旧类型添加一种新的游戏叙事类型：

[![](https://cdn.thenewstack.io/media/2025/08/96969771-image-8-1024x102.png)](https://cdn.thenewstack.io/media/2025/08/96969771-image-8-1024x102.png)

像往常一样，我不再真正尝试测试 LLM - 只是 Crush 如何表示输出和处理权限。 请注意，我没有添加 C# LSP。

当它确定了添加类的位置并生成了它时，我收到了权限请求：

[![](https://cdn.thenewstack.io/media/2025/08/85fc9d42-image-9-1024x594.png)](https://cdn.thenewstack.io/media/2025/08/85fc9d42-image-9-1024x594.png)

它正确地将“farmer”解释为角色名称和类型。 它还正确地将字符串的名称从“PollutionBad”更改为“FreezingBad”，这是 LLM 的优势之一：它们了解交织在编码上下文中的英语语言上下文。

然后，它要求获得将策略添加到所需列表的权限：

[![](https://cdn.thenewstack.io/media/2025/08/94e5b56f-image-10-1024x381.png)](https://cdn.thenewstack.io/media/2025/08/94e5b56f-image-10-1024x381.png)

然后，它很好地尝试以与项目中其他叙事类似的方式添加新叙事的实例，但它没有足够的信息来正确地做到这一点。 它所做的事情很好，所以我停止了它。

虽然在尝试之前没有以列表的形式呈现单独的任务，但它确实合理地组织了工作，以便我可以按照它所做的事情进行操作。 它允许您使用 Tab 键在请求块和响应块之间切换。

## 结论

虽然 Crush 仍然缺乏一些 UI 必需品，但它确实有一些有趣和新颖的添加。 目前，它肯定比使用 Warp（其 Agentic CLI 集成到终端中）要弱。 但是 Crush 通过其文本用户界面确实具有一致的方法，因此随着后来的创新与通过开源贡献实现的更强大的基础相结合，它很可能会超出其应有的水平。