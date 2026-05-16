<!--
title: Anthropic 再次调整计费：Agent SDK 获得独立额度池
cover: https://cdn.thenewstack.io/media/2026/05/dd26538e-subscription-credits-scaled.jpg
summary: Anthropic 宣布从 6 月 15 日起调整计费政策，为 Agent SDK 等编程化使用提供独立积分池。不同订阅方案将获得 20 至 200 美元不等的月度额度，此举旨在区分交互式对话与自动化开发的资源消耗。
-->

Anthropic 宣布从 6 月 15 日起调整计费政策，为 Agent SDK 等编程化使用提供独立积分池。不同订阅方案将获得 20 至 200 美元不等的月度额度，此举旨在区分交互式对话与自动化开发的资源消耗。

> 译自：[Anthropic splits billing again: Agent SDK gets separate credit pools](https://thenewstack.io/anthropic-agent-sdk-credits/)
> 
> 作者：Meredith Shubel

Anthropic 本周宣布，从 6 月 15 日开始，包括基于 Agent SDK 构建的第三方应用在内的编程化使用（Programmatic usage），将从一个新的每月积分池中扣除费用。

## 变化内容

在周三的一篇 [X 帖子](https://x.com/claudedevs/status/2054610152817619388?s=46)中，该公司表示，Claude 付费订阅用户很快将有资格获得每月的 [Agent SDK 积分](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)。该积分涵盖了编程化使用，即：Claude Agent SDK、`claude -p` 命令、Claude Code GitHub Actions 以及基于 Agent SDK 构建的第三方应用。

新政策在编程化使用和交互式使用（Interactive usage）的计费方式之间划清了界限。

例如，在网页端、桌面端或移动端与 Claude 聊天，在终端中使用 Claude Code，以及使用 Claude Cowork 仍将计入典型的订阅限制。但当你使用 Claude Code 中的 `claude -p` 命令、在 Python 或 TypeScript 项目中运行 Claude SDK 使用量，或让第三方应用通过 Agent SDK 进行身份验证时，你很快就会看到这些使用量会从你新的每月 Agent SDK 积分中扣除。

此前，Claude 用户无需关心这种区别；编程化使用和交互式使用都从相同的订阅限制中抽取。

## 运作机制

正如 Anthropic 在 X 上概述的那样，Claude 用户现在必须申领一个独立的每月积分来支持 Agent SDK。但你只需要申领一次。之后，所有的编程化使用都将自动从你的积分中扣除。

如果你用完了这些积分会发生什么？你有两个选择。

如果你开启了使用积分（usage credits），你可以继续工作，不受影响——只需知道你继续使用的部分将按“按需计费”的 API 费率计费。

如果你关闭了使用积分，那么你实际上为该月的编程化使用设定了上限，你必须等待积分在下一个账单周期开始时刷新。

如果账单周期结束时还有剩余的未使用积分怎么办？

那没办法。Anthropic 表示积分不会结转，而是在账单周期结束时直接失效。

## 你能获得多少积分？

你的 Agent SDK 积分池大小取决于你的订阅方案。

Pro 用户获得 20 美元；Max 5x 用户获得 100 美元；Max 20x 用户获得 200 美元。标准团队方案为每个席位 20 美元；高级团队方案为每个席位 100 美元。企业级按量计费账户为 20 美元；企业级高级席位为 200 美元。

值得注意的是，Agent SDK 积分仅适用于个人账户。这意味着你不能在团队之间共享、转移或汇集积分。

此外，使用 API 密钥的 Claude 开发者平台账户不符合该积分条件。相反，这些用户将继续采用按需计费模式。

Anthropic 的开发者沟通账号在 X 上表示：“基于 Agent SDK 构建的第三方工具（如 Conductor 和 OpenClaw）可以配合你的 Claude 方案使用，但会像你自己的脚本一样扣除你的积分。”

这意味着第三方工具的使用很快将从用户新的 Agent SDK 积分池中抽取——这是 Anthropic 在第三方工具使用立场上的又一次转变。

就在一个月前，这家 AI 公司停止允许 Claude 用户将他们的订阅应用于第三方工具。正如 Anthropic 的 Claude Code 负责人 Boris Cherney 在 4 月 4 日发布在 X 上的那样：“Claude 订阅将不再覆盖 OpenClaw 等第三方工具的使用。”相反，当时的新政策意味着用户必须购买额外的额度，或者面临 API 费率的按需计费。

但 Anthropic 再次改变了主意，彻底放弃了上个月的政策，转而采用新的 Agent SDK 积分系统。

该政策将于 6 月 15 日生效。用户目前无需进行任何操作，但应关注 6 月 8 日来自 Anthropic 的电子邮件以申领积分。