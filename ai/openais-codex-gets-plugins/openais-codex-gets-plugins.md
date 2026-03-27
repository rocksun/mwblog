<!--
title: OpenAI Codex迎来插件时代
cover: https://cdn.thenewstack.io/media/2026/03/043fcf31-codex_share-image_v1.png
summary: OpenAI Codex新增插件，拓展其功能至编码之外的规划与协调，旨在成为“超级应用”，与Anthropic和谷歌的类似系统竞争。
-->

OpenAI Codex新增插件，拓展其功能至编码之外的规划与协调，旨在成为“超级应用”，与Anthropic和谷歌的类似系统竞争。

> 译自：[OpenAI's Codex gets plugins](https://thenewstack.io/openais-codex-gets-plugins/)
> 
> 作者：Frederic Lardinois

OpenAI本周宣布，其正在为[Codex添加插件](https://developers.openai.com/codex/plugins)。这些适用于Box、Figma、Linear、Notion、Sentry、Slack、Gmail和Hugging Face等第三方服务的插件，将可重用工作流、MCP服务器和应用集成打包成可安装的捆绑包，供Codex应用使用。

此举让人联想到Anthropic使用Claude Code及其桌面应用以及谷歌的Gemini CLI所做的事情，两者都已提供了类似系统。但也许更重要的是，这也是OpenAI将更多非直接编码相关的工具引入Codex的一步，这将使该应用对那些可能考虑转向Anthropic桌面应用中的Claude和Claude Cowork的用户更具吸引力。

如果Codex成为[OpenAI“超级应用”](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d)的核心，它就需要超越编码。这感觉是朝着这个方向迈出的第一步。

![](https://cdn.thenewstack.io/media/2026/03/3e0c5bd6-directory-2-1024x671.png)

*来源：OpenAI。*

当然，许多新插件都与编码相关，但值得注意的是，第一批新插件将Codex推向了编写代码之前和之后的规划、研究和协调阶段。

插件可以将所有内容打包成一个安装包，供团队在所有开发人员中进行标准化，而无需每个人单独组装，而不是将独立的MCP服务器和自定义指令拼凑在一起。

从本质上讲，Codex插件将技能（几乎所有AI公司现在都支持的基于Markdown的常见工作流）、可选的应用连接器以及用于外部工具的MCP服务器捆绑在一起。发布时有20多个插件可用，用户可以在Codex应用、CLI和OpenAI的VS Code扩展中使用它们。

有趣的是，OpenAI将这些插件放在Codex UI的中心位置，在“新线程”按钮下方设有一个专用选项卡。点击该选项卡会进入应用中精选的目录。自助发布功能尚未推出，但对更多插件的支持即将到来。

在Codex CLI中，`/plugins`命令允许您从终端安装它们。

![](https://cdn.thenewstack.io/media/2026/03/4daf18fe-codex-local-plugin-light-1024x464.png)

*来源：OpenAI。*

目录中目前可用的一个更复杂的插件示例是“构建网络应用”插件。它捆绑了Stripe、Supabase和Vercel的MCP服务器，并附带了专门的技能，用于部署到Vercel、构建前端以及网络设计和使用这些第三方服务的最佳实践。

## Anthropic和谷歌呢？

Anthropic的Claude Code自今年早些时候以来就提供了插件，同样将MCP服务器、技能、斜杠命令和钩子捆绑到一键安装中。Anthropic也类似地在其应用中附带了一个内置市场，开发人员也可以发布到仓库级或个人市场（此功能即将登陆Codex）。

谷歌的Gemini CLI和该公司以AI为中心的IDE Antigravity将这些插件称为“[扩展](https://geminicli.com/extensions/)”，但它们与Anthropic和OpenAI的实现非常相似：MCP服务器、自定义命令、代理技能、钩子和主题，通过GitHub或内置注册表分发。谷歌[最近](https://developers.googleblog.com/making-gemini-cli-extensions-easier-to-use/)还添加了扩展设置，在安装时提示用户配置（如API密钥），并将其存储在系统密钥链中。

绝大多数情况下，这三大供应商现在都为这些插件/扩展使用了相同的架构。在它们和Codex之间切换也相当容易。OpenAI明确指出，“如果您已经拥有来自其他生态系统或自己构建的插件，您可以使用`@plugin-creator`将其添加到本地市场。”

例如，这个插件创建器也模仿了Claude Code和Cowork中的类似功能，它允许您通过简单描述所需功能来构建新插件——或至少创建其骨架。