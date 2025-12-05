
<!--
title: MCP：让Claude AI全面掌控你的本地文件系统
cover: https://cdn.thenewstack.io/media/2025/12/bd43b97c-osarugue-igbinoba-an_icdzkbhu-unsplash.jpg
summary: Claude Desktop利用MCP简化AI与API交互，实现本地文件识别与操作。用户可配置MCP服务器访问本地文件，但需注意安全与付费方案。
-->

Claude Desktop利用MCP简化AI与API交互，实现本地文件识别与操作。用户可配置MCP服务器访问本地文件，但需注意安全与付费方案。

> 译自：[Give Claude AI Full Access to Your Local Filesystem With MCP](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/)
> 
> 作者：David Eastman

我们已经对 [模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 进行了大量讨论，它是一个开源标准，旨在简化 AI 模型与 API 的交互方式。但通过 [Claude Desktop](https://www.claude.com/download)，您可以真正看到它的实际应用。作为一名开发者，您的部分工作流程可能需要跨越您的笔记本电脑文件系统。就其作用范围而言，您通常会希望将开发重点放在 Claude Code 上，并通过移动设备在网络上进行简单查询。但 Desktop 产品可以识别您机器上的文件，其带来的好处我将在本文中探讨。

今天的 Claude Desktop 比它刚出现时更智能一些。首先，您不再需要自己编写服务器代码。Claude Desktop 提供了预构建的连接器到其他服务，尽管基本模式是使用大型语言模型（LLM）来查找文档并以有用的方式转换其中的信息。我们一直想要的是一个大型语言模型（LLLM）能够理解的系统，这样我们就可以让它自己解决问题。

## Claude Desktop 的安装与初始设置

我下载了用于我的 M4 设备的 200MB .dmg 文件，并进行了安装：

[![](https://cdn.thenewstack.io/media/2025/11/c46daaef-image.png)](https://cdn.thenewstack.io/media/2025/11/c46daaef-image.png)

我登录后立即跳转到一个网页。这些页面由应用程序妥善管理，但您可以看到为什么用户会疑惑，为什么他们正在使用的应用程序立即想要使用网络。

接下来，我们看到一些关于在您的实际桌面上使用 Claude 的即时有用的提示，它将在您需要时可用：

[![](https://cdn.thenewstack.io/media/2025/11/82836941-image-1.png)](https://cdn.thenewstack.io/media/2025/11/82836941-image-1.png)

我不确定劫持 Caps Lock 键是个好主意——但如果您将 Mac 视为听写设备，也许我们未来根本不需要怎么打字了？

然后我获得了“更新”到 [Claude Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) 的选项，我接受了。但请记住，我们不一定专注于此应用程序的纯粹编码，因此其他模型可能更适合您的用例。

## 了解付费方案和集成

接下来您会看到付费方案（尽管没有显示使用限制），自然地，有免费方案。我可能已经属于某个方案，但这个界面没有告诉我。根据 Anthropic 控制台（现为 Claude 控制台）的信息，我可能正在使用 API 方案并有一些信用额度。总有一天，所有这些困惑都会消失，但目前我们正处于令牌经济的创新风暴之中。

[![](https://cdn.thenewstack.io/media/2025/11/a52a1a71-image-2-1024x402.png)](https://cdn.thenewstack.io/media/2025/11/a52a1a71-image-2-1024x402.png)

在离开付费方案之前，我注意到的第一件事是这个不起眼的提示：

[![](https://cdn.thenewstack.io/media/2025/11/677771e7-image-3-1024x46.png)](https://cdn.thenewstack.io/media/2025/11/677771e7-image-3-1024x46.png)

现在，我确实想检查 Slack 集成。几年前，我尝试过 [Slack 集成](https://thenewstack.io/how-to-get-started-building-serverless-backends-with-dark/)到一个网络工具，它相当棘手。不幸的是，Slack 连接器似乎只对安装了 Claude 的 Slack 应用程序的 Claude 团队版和企业版客户提供，仅在特定订阅层级可用。这很可能是一个合理的商业产品。

## 配置用于本地文件访问的文件服务器 MCP

但我们不限于预配置的连接器；我们可以自己动手。 [Claude 能够识别技能](https://www.claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)，我们可以制作 MCP 服务器以与我们的本地应用程序通信。这实际上是使用 Opus 4.5 的一个好理由。您还需要付费方案才能使用技能。但我们的目标只是让 Claude 使用您本地驱动器上的文件。

目前，我没有任何连接器在运行。所以让我们检查 Claude 是否能看到我们的本地文件：

[![](https://cdn.thenewstack.io/media/2025/11/470069a4-image-5-1024x703.png)](https://cdn.thenewstack.io/media/2025/11/470069a4-image-5-1024x703.png)

为了改变这一点，我们将更改设置，允许 [文件服务器 MCP](https://modelcontextprotocol.io/docs/develop/connect-local-servers) 操作有限的文件集。在某个时候，服务器需要 Node.js，所以打开终端并确保您可以执行此操作：

[![](https://cdn.thenewstack.io/media/2025/11/58d82025-image-6.png)](https://cdn.thenewstack.io/media/2025/11/58d82025-image-6.png)

现在我们将直接通过 Claude Desktop 的设置（通过应用程序的 Mac 菜单，或从应用程序设置中）进行操作，并转到“开发者”部分：

[![](https://cdn.thenewstack.io/media/2025/11/3798c7c3-image-7-1024x453.png)](https://cdn.thenewstack.io/media/2025/11/3798c7c3-image-7-1024x453.png)

点击“编辑配置”将打开 MCP 配置文件 JSON。您可以看到我的文件是空的：

[![](https://cdn.thenewstack.io/media/2025/11/680eeb13-image-8-1024x350.png)](https://cdn.thenewstack.io/media/2025/11/680eeb13-image-8-1024x350.png)

请记住，Claude Desktop 是“主机”，文件服务器是 Claude 可以调用的 MCP 服务器。所以您需要像这样配置：

|  |
| --- |
| An error has occurred. Please try again later. |

我叫 eastmad，但你可能不是；所以显然，请使用您的名字代替。我已授予服务器访问我的“下载”文件夹的权限，以强调这通常是有效的——您可以继续在该数组中添加特定目录。您可以看到我们正在使用 npx（因此您需要 Node），并且此服务器称为“filesystem”。这将授予 Claude 完全访问权限，正如我所解释的——尽管需要确认。

好的，这些是初始配置，所以关闭 Claude Desktop 并重新启动它。

重新启动后，Claude Desktop 立刻了解了更多信息：

[![](https://cdn.thenewstack.io/media/2025/11/79462823-image-9-1024x755.png)](https://cdn.thenewstack.io/media/2025/11/79462823-image-9-1024x755.png)

但 Claude 知道它自己知道什么吗？让我们再次尝试那个初始问题。返回该查询并刷新它：

[![](https://cdn.thenewstack.io/media/2025/11/8fd3a817-image-10-1024x799.png)](https://cdn.thenewstack.io/media/2025/11/8fd3a817-image-10-1024x799.png)

一旦您允许该操作：

[![](https://cdn.thenewstack.io/media/2025/11/1ad8b86c-image-11-1024x414.png)](https://cdn.thenewstack.io/media/2025/11/1ad8b86c-image-11-1024x414.png)

这很棒，尽管它没有提到写入磁盘，所以让我们检查它是否可以：

[![](https://cdn.thenewstack.io/media/2025/11/849ae01e-image-12-1024x611.png)](https://cdn.thenewstack.io/media/2025/11/849ae01e-image-12-1024x611.png)

Finder 向我保证这并非幻觉：

[![](https://cdn.thenewstack.io/media/2025/11/8b0de423-image-13-1024x690.png)](https://cdn.thenewstack.io/media/2025/11/8b0de423-image-13-1024x690.png)

是的，经典的俳句不仅是 5-7-5 音节，还应该提及一个季节。

## 安全影响和权限

在您开始见证您全副武装且正常运行的 MCP 服务器的强大功能之前，请确保您了解其安全影响。我们仅在本地工作，但我们仍然在与 Anthropic 来回发送信息，所以请确保您阅读的文档不会将身份信息与任何敏感内容关联起来。您还可以授予 Claude 访问其他工具的权限，使其能够在本地工作——确实，这才是真正的力量所在。

目前，Claude 会在每次访问请求时征求您的许可。所以我要求 Claude 读取一个电子邮件文件的详细信息；它停止了两次以检查权限。

[![](https://cdn.thenewstack.io/media/2025/11/cdc8712e-image-14-1024x211.png)](https://cdn.thenewstack.io/media/2025/11/cdc8712e-image-14-1024x211.png)

一旦您了解更多，您将能够绕过这些检查（如果您确实希望这样做）。

## 使用 Claude 与 MCP 的最终思考

Claude Desktop 可以使用一系列预构建的 MCP 服务器来连接特定服务——但请记住，您仍然需要与第三方一起处理权限、凭据和任何其他管理事宜。

付费方案和令牌使用系统仍然模糊不清，即使实际交易是完全透明的。一方面，很明显这些系统将随着时间的推移变得联邦化和简化——尽管当这种情况发生时，令牌经济很可能成为国家税收的目标。所以温和的混乱目前确实有一些优势。