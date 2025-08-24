<!--
title: Auggie CLI开发者实战：Agentic终端应用
cover: https://cdn.thenewstack.io/media/2025/08/c58041b2-andras-vas-iq2a48crn7e-unsplashb.jpg
summary: 文章介绍了 Augment Code 的 Auggie CLI 测试版，它使用 Node，并通过终端登录。文章测试了 Auggie CLI 的功能，包括总结项目、应用 Bootstrap 到 Rails 应用程序，并指出了其在项目理解和快速洞察方面的优势。同时，也提到了成本透明度、使用情况统计和用户界面等方面的改进空间。
-->

文章介绍了 Augment Code 的 Auggie CLI 测试版，它使用 Node，并通过终端登录。文章测试了 Auggie CLI 的功能，包括总结项目、应用 Bootstrap 到 Rails 应用程序，并指出了其在项目理解和快速洞察方面的优势。同时，也提到了成本透明度、使用情况统计和用户界面等方面的改进空间。

> 译自：[Developer Walk-Through of Auggie CLI, an Agentic Terminal App](https://thenewstack.io/developer-walk-through-of-auggie-cli-an-agentic-terminal-app/)
> 
> 作者：David Eastman

上次我在二月份 [分析 Augment Code](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/) 时，发现它是比较好的 LLM 扩展之一。虽然该公司最近更新了其产品，但发布真正的 Agentic CLI 花费了更长的时间。但我们现在有了测试版 [Auggie CLI](https://docs.augmentcode.com/cli/overview)。你需要等到 8 月 28 日才能看到 Auggie CLI，但我一直在试用私人测试版。

常见的是，[Auggie 使用 Node](https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli)，他们建议使用 22 或更高版本，以及“像 zsh、bash 或 fish 这样的兼容 shell”。像往常一样，我将在我的 Warp 终端中安装它：

[![](https://cdn.thenewstack.io/media/2025/08/aadb23e5-image.png)](https://cdn.thenewstack.io/media/2025/08/aadb23e5-image.png)

Augment 列出了一些它推荐的“现代”终端，包括 [Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/)、iTerm2、Alacritty 和 Kitty。

当我通过终端登录时，我被转发到一个具有类似登录的网站，该网站似乎给了我一个代码作为 JSON 字符串：

[![](https://cdn.thenewstack.io/media/2025/08/cfc705a1-image-1-1024x628.png)](https://cdn.thenewstack.io/media/2025/08/cfc705a1-image-1-1024x628.png)

这确实反映在终端中：

[![](https://cdn.thenewstack.io/media/2025/08/9fc3e2d6-image-2-1024x515.png)](https://cdn.thenewstack.io/media/2025/08/9fc3e2d6-image-2-1024x515.png)

我重新登录到 Augment Code，却被告知我之前的订阅已过期，并且“社区计划目前不可用”。我在网站上解决了这个问题，并在 Augment 的帮助下意识到我崩溃了一个封闭的测试版。

在开发的这个阶段，这些从终端到浏览器的跳转是合理的；显然，人们认为跳出终端在未来不会是主要的体验。

像往常一样，你也可以使用环境变量 `AUGMENT_SESSION_AUTH` 设置你的 token。

最后，我们看到了 Auggie 的全部荣耀：

[![](https://cdn.thenewstack.io/media/2025/08/b0329acc-image-3-1024x998.png)](https://cdn.thenewstack.io/media/2025/08/b0329acc-image-3-1024x998.png)

因为我不在一个有效的项目中，并且不想要索引开销（它自动启动），所以我快速退出了。使用我的 [“生活质量”期望](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)，如果介绍屏幕提到正在索引哪个目录以及正在使用哪个模型，我会更高兴。此外，我不知道我有多少 token 或请求要花费。它确实提到命令将自动运行 —— 虽然这不是一个很明智的默认状态。（仔细检查后，它确实在右侧的查询框下告诉你 Auggie 在哪个目录中打开，但不是很清楚。）

在我们回到交互模式之前，让我们尝试一个一次性的、静默的或非交互模式命令。这应该只使用不需要权限的安全命令来完成。我将要求它总结我的 Ruby on Rails 工具项目，我在其中为我的游戏开发对话。我的假设是它会在后台对其进行索引。这花了大约 30 秒才返回（正如你所看到的，Warp 将其计时为大约 38 秒）—— 风险在于你不知道它会花费多少时间，也不知道它的进展情况。因此，对于可能开放的任务来说，这不是一个好主意。

[![](https://cdn.thenewstack.io/media/2025/08/36ec5b19-image-4-1024x618.png)](https://cdn.thenewstack.io/media/2025/08/36ec5b19-image-4-1024x618.png)

markdown 段落包括 *Key Features* 和 *Technical Stack*。唯一的错误是它看到了 [Kamal](https://thenewstack.io/how-to-exit-the-complexity-of-kubernetes-with-kamal/) 的一些模板部署代码（因为这是 Rails；并且 Kamal 也来自 [37 Signals](https://37signals.com/)），并错误地认为这是部署方法。它不是。

此外，它还尝试了 *Use Case*，并且正确地理解了它是一个供游戏开发者管理分支对话和多角色交互的工具。

它还添加了一个有趣的最后告别语：“大量的备份 SQL 文件表明这是一个积极开发的工具，具有定期的数据快照，可能在生产中用于内容创建。”这完全正确，但也是一个很大的福音，因为“生命证明”相当重要。作为一名顾问，我经常浪费时间查看非常好的代码，但我后来才意识到这些代码几乎从未使用过。

## 工作区

与其他 Agentic CLI 相比，Auggie 对项目目录或工作区的识别稍微成熟一些。如果你从 .git 目录运行，它将索引该目录。否则，它将为你创建一个上下文工作区。这对于限制 LLM 可以漫游的位置以及了解项目中所有代码非常重要。

像往常一样，将你的代码发送到第三方云会引发安全问题。你可以使用 **.augmentignore** 来阻止某些文件的这种索引行为。我没有看到的是一个指令文件。

## 交互式

在终端中以交互方式工作是我们关联使用 Agentic CLI 的方式。我很想知道它是否记录了摘要 —— 但如果它记录了，我找不到它在哪里。然而，该项目显然已被索引，因此在第一个非交互式命令上花费了时间。

当我在查询框中编写一个 unix 命令时，它执行了该命令并添加了一些额外的信息：

[![](https://cdn.thenewstack.io/media/2025/08/6047dd8b-image-5-1024x885.png)](https://cdn.thenewstack.io/media/2025/08/6047dd8b-image-5-1024x885.png)

这里存在一个组织问题。虽然它做了正确的事情并执行了我的 shell 查询（[在一个 shell 中的 shell 的奇怪世界中](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)），但它为了提出自己的观察结果而缩减了响应。如果你从一个多标签终端工作，显然，你可以在一个单独的标签中执行 shell 命令 —— 但因为我确实要求了一个列表，我不确定它为什么要缩减它。

正如我为 [Google 的 Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/) 所做的那样，我将要求 Auggie 将 Bootstrap 应用到 Ruby on Rails 应用程序的一部分，我在那里还没有完成它。

在启动应用程序后，一个快速的并排比较可以看到，对于一个视图，Tags，我有漂亮的 Bootstrap 按钮用于标准的 CRUD 链接：

[![](https://cdn.thenewstack.io/media/2025/08/11d3ae23-image-6-966x1024.png)](https://cdn.thenewstack.io/media/2025/08/11d3ae23-image-6-966x1024.png)

但它们尚未在 Voice 视图中重现：

[![](https://cdn.thenewstack.io/media/2025/08/f023b11a-e71a-4edf-9257-f5dce7092b93-1024x282.png)](https://cdn.thenewstack.io/media/2025/08/f023b11a-e71a-4edf-9257-f5dce7092b93-1024x282.png)

这是相关的 *show.html.erb view*，用于显示单个标签的信息：

```
<div> 
  <%= link_to "Edit this tag", edit_tag_path(@tag), :class => "btn btn-warning" %> 
| <%= link_to "Back to tags", tags_path, :class => "btn btn-outline-success" %> 
  <%= button_to "Destroy this tag", @tag, method: :delete, :class => "btn btn-danger mt-2" %> 
</div>
```

这些 class 条目足以改变外观。当然，等效的 Voice 视图文件目前还没有这些。

所以让我们要求 Auggie 将 bootstrap 应用到 Voice 视图：

[![](https://cdn.thenewstack.io/media/2025/08/eca4ee5b-image-7-1024x57.png)](https://cdn.thenewstack.io/media/2025/08/eca4ee5b-image-7-1024x57.png)

我是公平的，并直接指向了这两个文件。

Auggie 首先正确地读取这两个文件和相关部分：

[![](https://cdn.thenewstack.io/media/2025/08/bcb1f833-image-8-1024x561.png)](https://cdn.thenewstack.io/media/2025/08/bcb1f833-image-8-1024x561.png)

然后它生成 diff：

[![](https://cdn.thenewstack.io/media/2025/08/9c6e3fc0-image-9-1024x180.png)](https://cdn.thenewstack.io/media/2025/08/9c6e3fc0-image-9-1024x180.png)

我喜欢它说“Now I can see the pattern”。这告诉我它从根本上理解这是一个通过比较所做的改变。然后它给出了更改的摘要：

[![](https://cdn.thenewstack.io/media/2025/08/05ea4655-image-10-1024x226.png)](https://cdn.thenewstack.io/media/2025/08/05ea4655-image-10-1024x226.png)

请注意，它不遗余力地找出这些类将对链接产生什么视觉效果。

它没有停下来征求更改的权限 —— 记住这在开始屏幕中已经说明了。我们可以看到一切都井然有序：

[![](https://cdn.thenewstack.io/media/2025/08/7b32486d-0f11-429b-8173-bff8962795a4-1024x470.png)](https://cdn.thenewstack.io/media/2025/08/7b32486d-0f11-429b-8173-bff8962795a4-1024x470.png)

在此之后，我有信心要求它在所有模型视图上不间断地工作。

## 结论

无论是 Augment 还是通过模型提供商，都没有人试图告诉我使用了什么成本。事实上，我仍然不知道曾经使用了什么模型 —— Google 告诉我他们在主模型中使用 Claude 3.7 Sonnet —— 但这需要提前说明，即使它是自制的。

默认情况下也应该启用报告使用情况统计信息。我无法看到如何更改权限模型，但是 —— 正如我应该重复的那样 —— 这在技术上仍然处于封闭测试阶段，所以还有足够的时间添加更多的结构。

你可以循环浏览响应，但是单行查询框并不是我真正想要在其中编写复杂提示（可能包括代码）的内容。

我喜欢的是 Augment 正在更加努力地弄清楚你的项目以及它是如何工作的。从注意到备份文件的数量，到理解我要求比较视图，响应更加智能。快速洞察力应该是 LLM 的全部意义所在，我认为 Augment 明白了这一点。我期待看到这在 Agentic CLI 繁忙的一年中如何发展。