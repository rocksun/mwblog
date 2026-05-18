<!--
title: Mac mini 正成为 AI 智能体的“基础设施”
cover: https://cdn.thenewstack.io/media/2026/05/cb09ef63-screenshot-2026-05-15-at-16.18.19.png
summary: 本文分析了Mac mini为何成为AI智能体的基座。得益于统一内存和低功耗，Perplexity、OpenClaw等项目均将其列为首选硬件，促使其从个人电脑演变为AI时代的生产力基础设施。
-->

本文分析了Mac mini为何成为AI智能体的基座。得益于统一内存和低功耗，Perplexity、OpenClaw等项目均将其列为首选硬件，促使其从个人电脑演变为AI时代的生产力基础设施。

> 译自：[The Mac mini just became infrastructure](https://thenewstack.io/mac-mini-agent-infrastructure/)
> 
> 作者：Janakiram MSV

在 4 月 30 日，苹果 2026 年第二季度的财报电话会议上发生了一些不同寻常的事情。

Tim Cook 花费了大量篇幅讨论 Mac mini 和 Mac Studio 的供应情况，他告诉分析师，这两款产品的多种配置均已售罄，供需平衡还需要“几个月”的时间。他直接指出了原因。

Cook 将此归功于智能体 AI 工具和工作流。首席财务官 Kevan Parekh 进一步指出，Perplexity 作为一个开发者，选择 Mac 作为企业级 AI 助手的平台。一周后的 5 月 7 日，Perplexity 推出了“Personal Computer”——一款面向所有 Mac 用户的新应用，而完整的智能体体验则需要付费的 Pro、Max 或 Enterprise 订阅。该公司自己的文档将 Mac mini 描述为运行该应用的推荐方式，建议 24/7 全天候运行。

这不仅仅是一个产品发布的故事。在过去的两个星期里，三种不同的智能体运行时（runtimes）同时对开发者近半年来一直在私下询问的一个问题给出了相同的答案：一个全天候在线的智能体应该部署在哪里？Perplexity 明确指向了 Mac mini。OpenClaw 在其官方硬件指南和社区中也推荐 Mac mini。[Hermes Agent](https://github.com/NousResearch/hermes-agent) 虽然不那么特定于 Mac，但其本地优先的 Ollama 路径使 Apple silicon（苹果芯片）成为了天然的选择。这种模式已经难以忽视，而苹果的供应数据进一步加强了这一论点。

## 一种全新的底层架构在无意中浮现

个人计算领域对于新类别总是有参考硬件。IBM PC 定义了办公室，树莓派定义了发烧友服务器。它们之所以成为基础设施，不是因为厂商的宣称，而是因为软件生态系统在其上实现了标准化。Mac mini 是这一血统的最新成员，而催化剂则是持久化智能体。

![](https://cdn.thenewstack.io/media/2026/05/465420a7-apple-mac-mini-thermal-architecture.gif)

持久化智能体不同于聊天会话。它在你不在键盘旁时运行。它在你睡觉时接收 Telegram 消息，在凌晨 3 点起草代码，监控你的收件箱，并根据你的日历执行预定任务。它需要一台能够持续运行、安静运作、与用户已有的操作系统集成，并且一年下来的成本低于云端虚拟机的宿主机。拥有 16 GB 统一内存、安静且低功耗散热设计的 Mac mini 同时满足了这四个条件。苹果列出的 2024 款 M4 Mac mini 待机功率仅为 4 瓦，大约相当于一个小夜灯的电耗。这些都不是苹果的初衷，苹果设计 Mac mini 是为了小型办公室和家庭影院，但智能体生态系统重新定义了它的用途。

> 苹果设计 Mac mini 是为了小型办公室和家庭影院。智能体生态系统重新定义了它的用途。

这一模式不再仅仅是小众行为，最清晰的信号来自 [Decrypt 对财报后短缺现象的分析](https://decrypt.co/366389/openclaw-apple-mac-mini-shortage-ai-2026)。Decrypt 当时报道称，高内存配置的 Mac mini 和 Mac Studio 的等待时间长达 16 到 18 周，此前提供的 512 GB Mac Studio 配置已从商店消失，而 eBay 上的黄牛将基础款的价格挂到了零售价的两倍左右。虽然这些快照细节会发生变化，但其方向与 Cook 在电话会议上的发言是一致的。

## OpenClaw 让 Mac mini 成为默认选项

[OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/) 是自下而上标准化的最清晰案例。该项目到 2026 年 4 月初在 GitHub 上已突破 30 万颗星，并在 Peter Steinberger [加入](https://thenewstack.io/persistent-ai-agents-compared/) OpenAI 后，转由 OpenAI 支持的独立基金会管理。硬件方案并非由 Steinberger 或 OpenAI 提出，而是来自社区。

由 Dirk Paessler 和 Florian Darroman 等开发者编写的安装指南都将 Mac mini 视为默认的部署目标。OpenClaw 的官方文档称 Mac mini 是“运行 OpenClaw 悄然间最好的硬件”，并列举了与 iMessage、快捷指令、苹果备忘录、提醒事项和钥匙串的 macOS 集成作为其他平台无法提供的“杀手级优势”。最后一点是结构性的优势：在 Mac mini 上运行的 OpenClaw 智能体不仅仅是在苹果芯片上运行，它还接入了用户已经在使用的身份、日历和消息界面。

> 在 Mac mini 上运行的 OpenClaw 智能体不仅仅是在苹果芯片上运行。它还接入了用户已经在使用的身份、日历和消息界面。

结果便是一种看起来像基础设施的部署模式，尽管没有人刻意这样设计。一个放在数据机架或架子上的无头（headless）Mac mini，在非管理员用户账户下运行 OpenClaw，通过 Tailscale 从手机远程访问，开启 FileVault（文件保险箱），并谨慎安装各项技能。社区在安全态势和自动启动配置上达成了一致。OpenClaw 意外地让 Mac mini 成为了参考平台。

## Hermes Agent 使苹果芯片成为天然之选

来自 [Nous Research](https://nousresearch.com/) 的 [Hermes Agent](https://hermes-agent.nousresearch.com/) 是这三者中最不特定于 Mac 的，而这恰恰让它出现在这一模式中变得有趣。OpenClaw 是广度优先和重生态系统的，而 Hermes 是深度优先和重学习循环的。该项目在公开发布后的几周内就获得了超过 10 万个 GitHub 星标，目前列出的贡献者超过 800 名。它的标语是“与你共同成长的智能体”，其架构将跨会话记忆与自主技能创建相结合。智能体会持久化存储它所学到的内容，在发现更好的路径时修改自己的技能，并在多个会话中积累用户的模型。

Hermes 被设计为可以随处运行。该项目的 GitHub 描述称 5 美元的 VPS、GPU 集群或无服务器基础设施都是同等有效的部署目标，该框架通过 OpenRouter、OpenAI、Anthropic、Nous Portal 和 Google 等提供商支持 200 多个模型。将 Hermes 拉入 Mac mini 故事的是它的 [Ollama 集成](https://docs.ollama.com/integrations/hermes)，它通过苹果芯片上的本地 OpenAI 兼容端点来路由智能体。

希望使用本地优先智能体且不产生循环 API 费用的用户，往往会因为统一内存架构而倾向于 Mac mini。配备 32 GB 内存的 Mac mini 可以以可接受的 token 速率运行量化后的 30B 参数模型进行推理（取决于上下文窗口和运行时），而配备 128 GB 内存的 Mac Studio 则可以处理一年前还需要多 GPU 阵列才能处理的模型。本地智能体社区注意到了这一点。

这两个开源项目在几乎所有事情上都存在分歧。OpenClaw 是 API 密钥优先的，拥有公开技能注册表和 50 多个消息集成。Hermes 是与供应商无关的，具有封闭的学习循环和受古希腊记忆宫殿（loci）启发的记忆架构。它们的重合点在于宿主机。两个社区都经常告诉新用户，Mac mini 是让智能体 24/7 全天候运行最干净的方式。

## Perplexity 为这一模式冠以商业之名

Perplexity 的产品决策使得这种趋同在开源社区之外也变得可见。Personal Computer 是一种混合了本地和云端的智能体，它运行在用户的 Mac 上，对于重型连接器任务可以使用安全的服务器端执行。该产品于 [3 月份宣布](https://www.perplexity.ai/hub/blog/perplexity-personal-computer)，最初仅限于候补名单上的 Max 订阅者，并于 5 月 7 日通过新应用向所有 Mac 用户推出。

Pro 和 Enterprise 层级同时获得了访问权限，而 Max 层级保留了更重型的自动化功能。宣布正式发布的 Perplexity 博客文章将该产品描述为“将计算机从纯云端世界带到你大部分真实工作所在的设备上”。它点名 Mac mini 作为全天候运行场景的部署目标，在这种场景下，任务可以从 iPhone 发起，在 Mac mini 上运行，并在需要批准时通知用户。

让这件事具有实质意义的是发布它的公司。Perplexity 不是一个开源社区项目。它是一家有风险投资支持、不依赖特定模型、搜索原生的公司，拥有公开的路线图和销售团队。它的外壳程序 [Comet](https://comet.perplexity.ai/) 已经作为浏览器原生智能体发布。Personal Computer 将这一外壳扩展到了本地文件和原生 Mac 应用。Perplexity 本可以为任何宿主机构建，但该公司选择了 Mac 作为底座，并且在苹果的财报会议上由首席财务官大声读出了它的名字。

> Perplexity 本可以为任何宿主机构建，但该公司选择了 Mac 作为底座，并且在苹果的财报会议上由首席财务官大声读出了它的名字。

我认为，这就是 Mac mini 停止作为台式机、开始被视为智能体基础设施的时刻。三个起点完全不同的运行时都选择了同样的底层架构作为推荐宿主，而苹果在供应端的反应也证明了这种需求是持久的。苹果在 2 月份宣布，未来的 Mac mini 生产将移至休斯顿的一家新工厂，这一举措与将 Mac mini 视为一个长期类别而非季度性增长的观点是一致的。

## 三种运行时如何划分设计空间

它们之间的差异比硬件上的趋同所显示的更为明显。它们在对选择运行时的任何人来说都至关重要的三个轴上划分了设计空间。

首先是推理策略。Perplexity 在设计上是混合的，在本地运行并在任务需要更强大的模型或云端连接器时访问 Perplexity 的安全服务器。OpenClaw 在 API 密钥上非常灵活，期望你自带模型提供商，通常默认使用 Anthropic Claude 和 OpenAI，并将 Ollama 作为离线备份。Hermes 在设计上与供应商无关，云端和本地路径都支持，尽管“Mac mini + Ollama”的路径是将其拉入这个故事的原因。

> OpenClaw 严重依赖 macOS，将苹果备忘录、iMessage、提醒事项、快捷指令和钥匙串作为一等公民目标。

其次是集成表面。OpenClaw 严重依赖 macOS，将苹果备忘录、iMessage、提醒事项、快捷指令和钥匙串作为一等公民目标。Hermes 则依赖于消息平台，Telegram、Discord、Slack、WhatsApp、Signal 和电子邮件都通过单个网关到达同一个智能体核心。Perplexity 依赖于用户现有的工作流，通过快捷键启动，观察活动的应用，并跨本地文件、Web 工具和 400 多个连接器进行编排。

第三是持久化模型。Perplexity 将任务状态持久化在其安全环境中。OpenClaw 在用户的家目录下持久化存储每个实例的记忆和技能，需要手动配置。Hermes 通过一个封闭的学习循环持久化存储一切，该循环会自动生成技能，就地修改它们，并在多个会话中建立用户的辩证模型。同一台 Mac mini 可以托管这三者中的任何一个，但在运行一个月后，它们的表现会非常不同。

| 场景 | 可能的选择 | 原因 |
| --- | --- | --- |
| 具有厂商支持的混合本地-云端工作流 | Perplexity Personal Computer | 混合外壳，400+ 连接器，安全服务器执行 |
| 具有深度 macOS 挂钩的消息重型个人智能体 | OpenClaw | 最广泛的集成表面，大型社区，自带模型 |
| 跨会话持久学习的本地优先智能体 | Hermes Agent | 封闭学习循环，跨会话记忆，原生支持 Ollama |

在实践中，许多开发者运行不止一个。Mac mini 成了共享的底层架构，而智能体则共享统一内存池、消息客户端和 FileVault 加密磁盘。

## 下一步行动

Mac mini 从未被定位为开发者基础设施。苹果的营销将其视为入门级 Mac 和媒体服务器。智能体生态系统在未经许可的情况下重新定位了它，而供应数据也开始反映这一新角色。

> 对于开发者来说，实际的结论是：个人 AI 智能体不再是浏览器标签页或云端会话，它们是运行在专用廉价苹果芯片上的持久进程。

对于开发者来说，实际的结论是：个人 AI 智能体不再是浏览器标签页或云端会话。它们是运行在专用廉价苹果芯片上的持久进程，而且成本曲线更倾向于拥有硬件而非租用虚拟机。

剩下的问题是苹果接下来会做什么。休斯顿工厂这一点表明了比季度性修复更长期的承诺。高内存配置的 Mac Studio 一直是最难买到的，该系列的高端配置看起来无法满足当前的需求。

随着外壳层的演进，接下来的 12 个月可能会带来 Windows 移植版、Linux 变体和竞争性的专用硬件。但这并不能改变一个事实：三种独立的智能体运行时已经基于不同的原则将苹果芯片列为推荐宿主，而且苹果的首席财务官在公开财报电话会议上点名了其中之一。