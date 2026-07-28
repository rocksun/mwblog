Block 周二推出了 [Buzz](https://buzz.xyz/)，这是一个免费的开源工作空间，旨在为人类和 AI 智能体提供类似 Slack 的协作服务。

该公司基于 Nostr 构建了 Buzz，Nostr 是一个去中心化的消息传递协议，以作为 Twitter 的抗审查替代方案而闻名，并得到了 Block 创始人 Jack Dorsey 多年的支持。使用 Nostr，每个智能体都能获得与其人类所有者连接的独立加密身份。

起初，Buzz 看起来非常像 Slack 或 Discord，具备频道、讨论串、私信、语音、媒体共享和代码仓库等功能。但不同之处在于，它将智能体视为这些对话的完整参与者。它可以与任何模型和流行的智能体框架配合使用，因此团队可以接入 Claude Code、Codex、[goose](https://thenewstack.io/block-goose-agentic-foundation/)（由 Block 开发）或者接入他们自己的工具。

Buzz 的代码实际上从今年早些时候开始就已在 GitHub 上托管（基于 Apache 2.0 许可证），但最近，Block 决定为 Buzz 托管自己的 Nostr 中继器，随着此次发布，现已开放公众注册。

![](https://cdn.thenewstack.io/media/2026/07/67cb9b69-block-buzz-ai-agents-app-macos-screenshot-2-1024x740.png)

来源：Block。

正如 Block 人工智能能力主管 Bradley Axen 向 *The New Stack* 介绍的那样，使用编码智能体的实际工作大部分是在私下进行的，然后就消失了。

> “每个人都错过了那第二次对话，至少在构建软件时，那是对话真正有趣的地方。那是你做出所有技术决策的地方。”   
> —Bradley Axen, Block 人工智能能力主管。

“现在，你会发布一个帖子，然后和智能体独自工作一小时，然后你可能会把智能体说的话复制粘贴回来，就好像是你自己说的一样，” Axen 说。“每个人都错过了那第二次对话，至少在构建软件时，那是对话真正有趣的地方。那是你做出所有技术决策的地方。”

## 拥有属于自己的身份

在 Nostr 上，每个参与者本质上都是一对公钥和私钥。Buzz 为智能体提供了自己的密钥对，并将其视为一个独立的行动者，但这里重要的是，它还添加了第二个签名，将其与个人联系起来。

“它开始时就像一个人。它有自己的公钥，它可以对事件进行签名，然后我们在中继器上发布一条额外的消息，” Axen 说。“我们有了这个加密的纸质审计追踪，这是我们任何一方都无法单独完成的，它声明，好吧，这是我的智能体，其他人都可以审查并确认这是事实。”

[](https://cdn.thenewstack.io/media/2026/07/7857e254-block-buzz-ai-agents-product-demo-video-4k.mp4)

来源：Block。

该审计追踪允许工作空间强制执行规则，例如仅允许成员拥有的智能体进入私有频道。Block 已向 Nostr 提议将此身份方案作为上游扩展，尽管目前尚未被采纳。

智能体通过 [Agent Client Protocol](https://zed.dev/acp) (ACP) 进行连接，这是 Zed 去年推出的开放标准，用于将编码智能体接入不同的工具。Axen 在 Linux 基金会的 [Agentic AI Foundation](https://thenewstack.io/agentic-ai-foundation-launch/) 指导委员会任职，并表示该组织正在考虑将 ACP 纳入其范畴。

## “你拥有的中继器”

Buzz 需要 Nostr 中继器才能工作，任何团队都可以建立自己的中继器并完全控制其基础设施，无需通过 Block 进行路由。Axen 将其比作 Discord 服务器，只是没有单一公司拥有它。尽管如此，Block 还是在发布前的最后几周构建了一个托管选项，押注于大多数团队不想处理运行自己中继器的额外复杂性。

“我很高兴你可以这样做，但我认为大多数人只是想要一个现成的解决方案，” Axen 说。

Block 的托管中继器在发布时是免费的，Axen 将其称为测试版。该公司尚未设定使用限制。Axen 表示，托管一个 10 人的开源项目成本很低，而作为“企业级 Slack”的替代品，最终需要一种不同的安排。

## 从 goose 到 BuilderBot

值得注意的是，Buzz 并不是 Block 的第一个智能体项目。毕竟，该公司在 2025 年 1 月开源了其智能体框架 goose。该项目现在在 GitHub 上已获得超过 50,000 个星标。
6 月，Block 还详细介绍了 [BuilderBot](https://thenewstack.io/how-block-manages-its-fleet-of-ai-coding-agents-from-slack/)，这是一个工程师通过在 Slack 中对其进行标记来调用的内部系统。该公司表示，它每天运行超过 200,000 次操作，每周合并约 1,500 个拉取请求，约占 Block 生产代码变更的 15%。

## 与 Slack 共存

Block 并不是唯一将智能体接入团队现有工具的公司。Atlassian 已经在 Jira 中添加了智能体，整个行业的公司现在都在 Slack 内部运行编码智能体。Block 内部仍在使用 Slack，Axen 认为两者可以并行使用。

“它能完全替代 Slack 吗？随着时间的推移我们拭目以待，因为 Slack 也编码了许多业务工作流，” 他说。“我们在 Slack 中有十年的历史。”

目前，Buzz 还处于早期阶段。自今年早些时候公开以来，该存储库仅获得了 100 多颗星，仅为 goose 的一小部分。

此次发布正值 Block 围绕 AI 进行重塑之际。2 月份，该公司裁员超过 40%，员工人数从 10,000 多人减少到不足 6,000 人，Dorsey 称 AI 实现了他所谓的“一种新的工作方式”。

Buzz 是 Block 为那家规模更小、更偏向智能体的公司构建的协作层。