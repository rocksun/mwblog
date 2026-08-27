<!--
title: Anthropic 的 Claude 现在拥有了自己的浏览器
cover: https://cdn.thenewstack.io/media/2026/08/58988b68-tasha-kostyuk-thwad7j9yia-unsplash-scaled.jpg
summary: Anthropic 为 Claude 桌面应用添加了内置的 Chromium 浏览器，使其无需依赖外部扩展即可直接上网。该功能目前面向付费用户开放，支持从主流浏览器导入部分登录信息，并内置了安全防护措施。
-->

Anthropic 为 Claude 桌面应用添加了内置的 Chromium 浏览器，使其无需依赖外部扩展即可直接上网。该功能目前面向付费用户开放，支持从主流浏览器导入部分登录信息，并内置了安全防护措施。

> 译自：[Anthropic's Claude now has a browser of its own](https://thenewstack.io/claude-built-in-browser-cowork/)
> 
> 作者：Frederic Lardinois

Anthropic 正在[赋予](https://claude.com/blog/cowork-built-in-browser/) Claude 专属的浏览器。

正如该公司周三宣布的那样，桌面版 Claude（支持 Mac、Windows 和 Linux）现在可以在 Cowork 中使用内置的基于 Chromium 的浏览器，这让你能够在当前工作环境中直接浏览网页。

此举终于使 Anthropic 的 Claude 桌面应用与 OpenAI 看齐。OpenAI 最近放弃了构建其独立浏览器 Atlas 的野心，转而将其添加到了 [ChatGPT 桌面应用](https://thenewstack.io/openai-codex-work-atlas/)中。

该新功能目前正逐步向付费的 Pro、Max 和 Team 计划订阅用户推出。

## 是浏览器，而不是“你的”浏览器

此前，为了让 Claude 浏览网页，你必须安装一个 [Chrome 扩展程序](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn?hl=en-US&pli=1&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)。虽然它工作得还算不错，但总让人感觉像是一种“黑客”手段。然而，在使用过带有内置浏览器的 ChatGPT 应用（并能快速截取浏览器屏幕内容并与模型讨论）之后，这些应用中内置专属浏览器会让许多工作流程变得更加轻松。

有趣的事实是：最初的 Claude Chrome 扩展程序正好在一年前的 2025 年 8 月 26 日发布。距离 Anthropic [推出](https://thenewstack.io/claude-chrome-cowork-sessions/) Chrome 扩展程序的一次重大更新（本质上将其转变为 Cowork 会话）也才过去两周。但 AI 的发展周期很快，两周已经是很长的一段时间了。

![](https://cdn.thenewstack.io/media/2026/08/4471347a-cowork-browser-1024x576.png)

图片来源：Anthropic。

“到目前为止，让 Claude 能够在 Cowork 中使用网络意味着通过 [Claude in Chrome](http://claude.com/claude-in-chrome) 扩展程序让它访问你的浏览器，”Anthropic 解释道。“当工作内容是在你已经打开的页面上时，这仍然是正确的选择。但许多 Web 任务并不需要‘你的’浏览器，只需要‘一个’浏览器，现在 Claude 有了一个。”

不过，Claude Chrome 扩展程序仍有其用武之地。在侧边栏保留 Claude 以讨论你在浏览器中打开的页面仍然非常有用。

“Claude in Chrome 适用于你已经打开的页面，使用你已经登录的账户，例如更新 CRM、处理收件箱或编辑眼前的文档，”Anthropic 解释道。

此外，如果你已经安装了该扩展程序，它将继续作为 Claude 浏览网页的默认选择，除非你在 Claude 桌面设置中明确更改了你的首选浏览器。

## 迁移你的登录信息

团队指出，这很大程度上是“Claude 的浏览器，而不是你的”。但由于它与你的日常浏览器分离，它没有你的登录信息。为了解决这个问题，Anthropic 允许你从 macOS 上的 Chrome、Edge 和 Firefox，以及 Windows 和 Linux 上的 Firefox 导入登录信息。

该公司非常明确地指出，除非你真的坚持要让 Claude 访问你的 Schwab 账户，否则来自银行和电子邮件提供商的登录信息以及任何单点登录（SSO）站点都被明确排除在外。

这种基于操作系统的列表不一致的原因很可能是 Windows 上的 Chrome 和 Edge 确保了第三方应用程序无法读取你的本地 Cookie，以此作为对抗信息窃取程序的防御措施。Firefox 仍然将这些信息存储在简单的 SQLite 数据库中。在 MacOS 上，Chrome 的密钥存储在钥匙串（Keychain）中，其他应用程序可以向用户请求访问权限。

## 风险并非为零

在此背景下，Anthropic 还强调，在让智能体（Agent）在网络上自由活动时，始终存在提示词注入的风险。该公司在 Chrome 扩展程序和内置浏览器中内置了保护措施，但也指出，尽管做出了最大努力，“风险并非为零”。

由于浏览器不太可能登录许多敏感网站，如果出现问题，这里的爆炸半径（影响范围）有望较小。