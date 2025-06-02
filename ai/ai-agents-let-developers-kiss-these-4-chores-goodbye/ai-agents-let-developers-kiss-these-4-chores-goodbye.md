<!--
title: AI代理让开发者告别这4个繁琐的任务
cover: https://cdn.thenewstack.io/media/2025/05/c00d132d-ai_programming_buddy.jpg
summary: 开源AI代理来袭！All Hands AI联手Mistral AI发布Devstral，解放开发者！告别合并冲突、PR反馈等繁琐任务，利用OpenHands在Docker沙箱中安全运行，轻松搞定TerraForm、Kubernetes，提升测试覆盖率。拥抱LLM驱动的Agentic循环，释放云原生开发效率！
-->

开源AI代理来袭！All Hands AI联手Mistral AI发布Devstral，解放开发者！告别合并冲突、PR反馈等繁琐任务，利用OpenHands在Docker沙箱中安全运行，轻松搞定TerraForm、Kubernetes，提升测试覆盖率。拥抱LLM驱动的Agentic循环，释放云原生开发效率！

> 译自：[AI Agents Let Developers Kiss These 4 Chores Goodbye](https://thenewstack.io/ai-agents-let-developers-kiss-these-4-chores-goodbye/)
> 
> 作者：Loraine Lawson

[All Hands AI](https://www.all-hands.dev/) 的 CEO [Robert Brennan](https://www.linkedin.com/in/robert-a-brennan/) 在本月早些时候于迈阿密举行的 [Infobip Shift Conference](https://shift.infobip.com/) 上告诉开发者，开发者对 AI 的关注一直非常具有战术性。All Hands AI 创建开源 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)，用于软件开发。

他表示，战术性部署意味着 AI 主要在 IDE 中执行自动完成功能。

“你在你的 IDE 中，你正在积极地处理一个问题，而 AI 基本上——无论你的光标指向哪里——它都在预测接下来的几行代码作为自动完成，”他说。

他承认这非常有用——但 AI 可以做更多的事情来成为程序员最好的朋友，他在展示如何在编程中使用 AI 的演示中解释道。

All Hands AI 创建了 [OpenHands](https://github.com/All-Hands-AI/OpenHands)，这是一个 MIT 许可的、由大型语言模型驱动的软件开发代理，可以编写代码、运行命令、浏览网页，甚至解决 GitHub 问题。

最近，本月 All Hands 宣布与 [Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) AI 合作，这促成了 [名为 Devstral 的编码代理的开源模型](https://www.all-hands.dev/blog/devstral-a-new-state-of-the-art-open-model-for-coding-agents) 的发布。

“软件工程师们，很明显，我们两年前的工作方式与今天的工作方式不同，”Brennan 说。“而我们两年后的工作方式将会非常非常不同。我们认为软件工程社区在改变成什么样子方面有发言权，我们在两年后我们的工作看起来像什么方面有发言权，这一点非常重要。”

Brennan 认为，开源方法将为软件开发解锁那些有价值的未来 AI 用例。

“你给代理提供一两行英语，说，请重构这个文件，请添加一个单元测试，请修复这个 PR 上的合并冲突；然后代理会自行工作 5、10、15 分钟，无需监督，然后 [它] 会带着答案回来找你，”他说。“与此同时，你可以专注于不同的编码任务。你可以在 Slack 上与你的队友交谈。你可以在 Reddit 上闲逛。”

## 分解 AI 代理：Agentic 循环

但在开发者能够实现那个特殊的梦想之前，还有工作要做。

Brennan 解释说，AI 代理的核心是运行在 agentic 循环上的。这基本上是一个 [大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) 之间的循环——它为 AI 提供“大脑”或“引擎”——以及代理采取行动的外部世界。

“基本的循环是我们问 LLM，‘你可以采取的下一个行动是什么？’”他说。

该操作可能是浏览网页以查找文档、运行命令或读取和编辑文件。一旦 LLM 返回工作，软件开发人员会将该工作反馈到 LLM 中以进行下一步循环。基本上，开发人员会不断地转动该循环，直到 LLM 最终表示它已完成任务，他说。

“深入研究这些操作，在幕后发生了很多有趣的事情，以使软件开发代理真正做好这项工作，”他说。

他解释说，在代码编辑的早期，最简单的实现是将它想要编辑的整个文件粘贴到 LLM 中，然后取回一个全新的文件版本。这意味着使用更多的 token，这使得它既昂贵又缓慢且容易出错。代理可能会替换所有制表符和空格，或忘记行。

“现在有更复杂的策略来执行基于差异的文件编辑或字符串‘查找和替换’——现代 agentic 框架对文件编辑有更复杂的解决方案，”他说。

> “通过 OpenHands，我们已经决定，默认情况下，代理始终在沙箱中运行。它有一个 Docker 运行时，它有自己的文件系统和自己的终端。”
>
> — Robert Brennan, CEO of All Hands AI

他说，许多 agentic 工具将在你的笔记本电脑上本地运行。它也在你的终端中运行，他承认这可能有点可怕。这就是为什么在使用 AI 代理时，权限变得非常重要，他说。

通常，AI 代理以某种确认模式运行——当代理说它想要运行一个命令时，开发人员必须点击 Y 按钮才能继续下一步。他补充说，这可能有点乏味，因为它会恢复到战术模式。
OpenHands 找到了一个变通方法，甚至可以保护您免受运行 `/rm -rf /` Linux 命令的侵害，该命令会强制且递归地删除文件和目录。

“通过 OpenHands，我们决定默认情况下，代理始终在沙箱中运行，”他说。“它有一个 Docker 运行时，它有自己的文件系统和自己的终端，即使它试图运行 `/rm -rf /`，也不会搞砸你的文件系统，这使得代理更加自主和无人监督地运行。”

这导致了一些考虑，例如应该给 AI 代理授予什么样的凭据访问权限。

“你想给它 API 密钥吗？”他问道。“也许你希望它能够从 S3 存储桶中读取数据，但你不希望它能够直接关闭你的生产 Kubernetes 集群。”

## AI 微代理

他还分享了一些关于微代理的信息，微代理是将较大的 AI 任务分解为较小的任务的一种方式，这些较小的任务可以交给专门的微代理来自主解决。

企业面临的实际挑战在于使微代理可靠、安全并针对特定工作流程进行定制。工具仍在不断发展，但 Brennan 特别提到了一些工具，例如 AI 驱动的代码编辑器中提供的 [Cursor Rules](https://docs.cursor.com/context/rules)，或者 `clon.md` 文件，它是一个包含 AI 或机器学习上下文中使用的特定指令或策略的 markdown 文件，特别是在 [mlem.ai 框架](https://github.com/iterative/mlem.ai/blob/main/content/docs/command-reference/clone.md) 中。

## AI 代理的开发者用例

Brennan 重点介绍了他最喜欢的一些 AI 代理和微代理的用例：

**1. 解决合并冲突**

“这是我作为开发人员最不喜欢做的事情，”他说。“我有一个 PR 已经获得批准，测试通过了，准备就绪了，但是其他人编辑了我编辑的同一个文件，Git 无法自动解决合并。” 这需要他整理旧代码和新代码，以尝试将其合并。

“这是一项非常死板的任务，没有太多的创造力，而且 AI 在这方面做得非常好，”他说。“所以现在只要有合并冲突，我就会让 AI 来为我做。”

因此，他已经好几个月没有主动手动解决合并冲突了。

**2. 解决 PR 反馈**

“其他人已经给出了他们想要什么的非常清晰的描述，”他说。

这样做，他们基本上为你编写了提示。他建议 AI 修复它并立即解决他们的反馈。“我还要求它同时修复合并冲突，”他说。

**3. 基础设施变更**

他补充说，AI 可以很好地处理基础设施变更。Helm 是 Kubernetes 的一个流行的软件包管理器。

“这是我最喜欢的任务之一，因为我讨厌使用 TerraForm，而且 Helm 通常涉及一些奇怪的、深奥的更改，需要去文档中寻找一些 Helm chart 等，”他说。“同样，代理往往做得很好。”

他使用 OpenHands 来修复内存问题，因为 AI 非常擅长遵循围绕构建数据库和迁移的所有最佳实践，他说。

**4. 测试**

Brennan 还使用 OpenHands AO 来修复失败的测试并扩大测试覆盖率。

“这真的很棒，因为有一个非常明确的完成定义：测试失败了，”他说。“AI 基本上可以不断迭代，更改代码或更改测试，直到达到它可以运行该命令并且以退出代码零通过的点。”

如果你的代码库的某个区域完全没有被测试覆盖，它也可以扩展测试，他补充说。

“这只是使用代理 AI 的一个非常简单、快速的胜利 […] 它可以不断迭代，直到测试通过，”他说。