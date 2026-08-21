<!--
title: Slack大幅简化第三方平台构建的智能体安装体验
cover: https://cdn.thenewstack.io/media/2026/08/ac627463-ardian-pranomo-axlaplh7-jm-unsplash-scaled.jpg
summary: Slack推出Add to Slack功能，支持用户无需编写自定义集成，即可快速安装并运行来自第三方平台的AI智能体。该功能简化了权限与配置流程，并兼容现有的工作区安全策略，实现了智能体的高效部署与管理。
-->

Slack推出Add to Slack功能，支持用户无需编写自定义集成，即可快速安装并运行来自第三方平台的AI智能体。该功能简化了权限与配置流程，并兼容现有的工作区安全策略，实现了智能体的高效部署与管理。

> 译自：[Slack makes it easier to install agents built with third-party tools](https://thenewstack.io/add-to-slack-agents/)
> 
> 作者：Frederic Lardinois

Slack周四推出了 [Add to Slack](https://slack.com/blog/news/add-to-slack) 功能，让用户能够更轻松地将使用十个外部平台构建的智能体引入工作区，而无需编写自定义的 Slack 集成。

Slack 表示，用户只需在合作伙伴工具中启动安装（及智能体创建）流程，合作伙伴便会处理 OAuth、应用配置和权限范围设置。运行时本身保留在 Slack 之外，既可以在提供商端，也可以像 NanoClaw 这类工具一样，保留在用户的机器或云账户上。随后，相应的 Slack 应用即可接收消息、提及并加入频道。

Add to Slack 的首发合作伙伴包括 Hyperagent、LangChain、Lovable、n8n、NanoClaw、OpenAI、Runlayer、Skydive、Superhuman 和 Vercel。

这些产品涵盖了从点选式构建器到开发者框架等广泛领域。但最重要的是，安装路径是统一的——这比以往的方法容易得多，过去用户必须繁琐地点击各种设置、启用权限，并祈祷一切顺利。

Slack 表示，安装的智能体将继承工作区的数据边界和权限控制。工作区的 [应用审批策略](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) 仍然适用。每个应用的 OAuth 范围和频道成员资格决定了它可以访问的内容。安装完成后，它们也将出现在 Slack 的应用浏览器中。

![](https://cdn.thenewstack.io/media/2026/08/15569ebd-lovable_1@2x-1024x1024.png)

图片来源：Slack。

## 每个智能体对应一个应用

NanoClaw 是该功能实际运作的一个很好示例。以前连接这个 [开源框架](https://github.com/nanocoai/nanoclaw) 需要创建一个自定义的 Slack 应用，然后完成其配置、范围和身份验证。现在，NanoClaw 的 Marketplace 应用成为了 [管理应用](https://docs.slack.dev/reference/methods/apps.manifest.create/)，有权为每个 NanoClaw 智能体创建一个单独托管的 Slack 应用。

在为 *The New Stack* 进行的演示中，NanoClaw 的创始人 Gavriel Cohen 要求一个 NanoClaw 智能体建立一个以《办公室》角色为原型的团队。

“我说为我创建一个智能体团队，它就创建了所有这些智能体并为它们贴上标签。它们全部出现，然后我们就开始在这里聊天了，” Cohen 对 *The New Stack* 说。

机器人以不同的名字出现。在演示中，Cohen 还将它们聚集在一个带有共享 Canvas 的房间里。

“每个智能体都有自己的机器人。所以它创造了一些新东西。这意味着你可以原生标记它们，” Cohen 说。

NanoClaw 为每个智能体创建一个单独的 Slack WebSocket 连接，其主机将消息路由到 Slack 中相应的智能体。

## 那么 Slack Code 呢？

值得注意的是，Add to Slack 与 [Slack Code](https://thenewstack.io/slack-code-agent-channels/) 是分开的，这是该公司周四推出的另一项新 AI 智能体功能。Slack Code 创建临时项目频道，支持的编码智能体可以在频道归档前展示计划、差异对比（diffs）、拉取请求详情和实时预览。Add to Slack 是安装一个应用，而 Slack Code 则是在安装后组织来自合作伙伴的一小组编码智能体的工作。

*题图来源：Ardian Pranomo (Unsplash+)。*