OpenAI于周一详细介绍了它是如何为其单体代码库（monorepo）构建一个新的Git后端，以支持其开发者和他们的智能体现在创建的日益增加的提交。

这个团队将新后端命名为Pando，该公司表示，它将推送延迟降低了近5倍，目前在OpenAI每天处理近1PB的Git数据。

显然，OpenAI是氛围编程工具的早期采用者。该公司表示，与2024年第一季度相比，到今年年底，其单体代码库的季度提交量将增长2,400%以上。但它所面临的问题与许多其他企业和像GitHub这样的Git托管平台现在所看到的问题类似。

随着开发速度的加快，Git本身正在成为一个瓶颈。例如，GitHub在其最近的 [Universe主题演讲](https://thenewstack.io/?p=22842113) 中花了很多时间来讲述它如何 [改进其基础设施](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) 以变得更快、更可靠，同时每月服务数十亿个拉取请求（PR）。

这催生了一些初创公司，比如 [Entire](https://thenewstack.io/entire-git-for-agents/)（由前GitHub CEO Thomas Dohmke创立）以及诸如 [来自Cursor的Origin](https://thenewstack.io/cursor-origin-github-alternative/) 等项目。就像OpenAI的工作一样，这些项目都基于Git，但其他项目，如 [Anthropic](https://thenewstack.io/anthropic-scion-git-replacement/)，则基本上是从零开始采用新的客户端和架构。

## 为什么OpenAI选择留在Git生态中

OpenAI团队明确指出，他们希望保持与Git的兼容性。该团队发现其Git后端的可靠性跌至90%以下，伴随着缓慢的获取（fetch）和失败的合并，但他们还是决定留在Git生态系统内。

正如OpenAI的Aaron Friel、Taylor Blau和Ted Nyman在公告中所问的那样，团队自问的问题是他们是否“达到了Git本身的极限，还是我们服务单体代码库方式的极限？”OpenAI的答案是，Git客户端和协议并不是真正的问题（尽管团队也在那里做了一些调整），而是传统Git服务器的构建方式。

“二十多年来，随着构建软件方式的改变，开发者一直在围绕Git调整他们的工具，”他们写道。“当我们开始在自己的单体代码库中感受到摩擦时，能够继续在这项工作的基础上进行构建对我们来说很重要。”

## Pando是如何工作的

Pando抛弃了大多数Git服务器视为要求的两件事。首先是同时保持仓库中的每个分支处于一致状态。其次是为每个获取代码的客户端构建一个自定义包文件（packfile，即Git用于打包压缩对象的格式）。

在 Git 中，分支本质上是指向最新提交的指针。移动该指针是推送中唯一需要协调的部分。传统的 Git 服务器在整个代码库中对这些更新进行排序，因此当有许多开发人员并行工作时，推送到一个智能体的分支最终可能会等待另一个智能体的分支。

另一方面，Pando 不会跨整个代码库协调每个写入操作。相反，它会单独处理每个分支。正因为如此，对不相关分支的推送就不必互相等待。

该团队承认，这里存在权衡。当客户端同时查看多个分支时，可能会在略微不同的时间点看到它们。然而，OpenAI 认为，在实践中，用户和智能体只关心单个分支的更新顺序。

当客户端推送时，Pando 在将传入的 packfile 流式传输到 blob 存储中时对其进行验证，而无需将其解包到本地仓库中。它在元数据存储中记录新的分支尖端、packfile 的位置及其依赖项。默认情况下，Pando 仅将 trunk 分支通告为功能分支推送的基础。这使得每个 pack 都可以被其他已经拥有通告的 trunk 历史记录的客户端重复使用。

然后，当另一个客户端获取该分支时，Pando 会根据它已经拥有的历史记录选择所需的存储 pack。然后，它通过 packfile-uri（一种 Git 协议功能，允许客户端单独下载 pack）返回下载链接。

![](https://cdn.thenewstack.io/media/2026/11/da899961-screenshot-2026-11-02-at-2.23.37-pm-1024x457.png)

Pando 将编写者的 packfile 存储在 blob 存储中，并在共享的键值存储中记录引用版本。在获取时，Pando 选择读取器所需的 pack，并由 Express 提供服务。图片来源：OpenAI。

该公司表示，一个名为 Express 的缓存服务随后会从区域缓存中提供这些 pack，命中率超过 99%。在标准的云虚拟机上，克隆和获取操作可以跑满 10 Gbps 的网络链路。

否则，繁忙的单体代码库会导致客户端每天下载数万个小 pack，因此后台工作人员会随着时间将它们合并成更大的 pack，这很像日志结构化数据库（log-structured database）压缩其数据的方式。这也让 Pando 能够在对数时间内计算出客户端需要的 pack。

## Pando 与标准 Git 服务器的对比

在标准的 Git 服务器上，每次获取都意味着计算出客户端缺少哪些对象，并专门为该客户端压缩一个新的 packfile。OpenAI 表示，这些 pack 生成成本高且难以缓存。Pando 大多只是分发它已经拥有的字节。

在推送之前，常规的 Git 服务器还会列出它拥有的每个分支，以便客户端可以跳过服务器已经拥有的对象。据 OpenAI 称，仅凭数百万个分支，该列表本身就可以增长到超过 100 MiB。仅通告 trunk 可以保持其较小体积，但这意味著对同一分支的重复推送会重新发送不在 trunk 上的所有内容。该团队表示这是一个公平的权衡，因为其单体代码库中的中位数 pack 仍然小于 20 KiB。

常规的 Git 服务器还必须重新打包和进行垃圾回收（garbage-collect）仓库以保持其高速运行，这会消耗计算资源和磁盘 I/O。Pando 绝不会丢弃 pack。它在每个压缩级别都保留 pack，并从所有级别提供服务。

对于开发者来说，这些几乎是不可见的。他们继续使用标准的 Git 命令，尽管 OpenAI 现在在其开发人员机器上以及 ChatGPT 桌面应用程序内部发布了自己的 Git 构建版本。

OpenAI 用 Rust 语言在 10 周内构建了 Pando，其中一名工程师设计了核心，Codex智能体团队负责实现。它于 4 月投入生产。

## 哪些内容会回馈给开源 Git？

基于 Git 构建也意味着会遇到 Git 自身的一些粗糙边缘，OpenAI 表示它正在将许多修复回馈给该项目。由于 Pando 极度依赖 packfile-uri（由一位 Google 工程师 [在 2019 年首次提出](https://lore.kernel.org/all/871s1stlf4.fsf@evledraar.gmail.com/)），该团队不得不修复 Git 客户端如何处理并发 pack 下载、在中断的传输后进行清理以及恢复已经完成的下载。它还为这些下载添加了跟踪功能，这使得更容易判断缓慢的获取是将时间花在生成 pack 上还是传输上。

并非所有这些工作都已进入 Git。OpenAI 表示，其多项更改已经进入上游，而许多其他更改目前仅存在于公司的公共 Git 代码库中。这些更改包括对并行下载和索引 pack 的支持，以及一项新的“显式 haves”功能，该功能允许服务器告诉推送客户端分支当前指向哪里，而无需客户端将该历史记录排除在其 pack 之外。该公司正在公共补丁跟踪器中跟踪所有这些内容。

不过 Pando 本身并不属于开源部分。OpenAI 并未将该后端开源，截至目前，它仅表示正在寻找与用户分享底层技术的途径。Anthropic 也曾表示没有计划发布 Scion。

[AI 工程师
2026年AI工程师成长分步指南

简介
使用大语言模型
上下文工程
AI 模型
嵌入与向量数据库
嵌入模型
检索增强生成 (RAG)
智能体
AI 安全与伦理
评估与可观测性](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=openai-pando-git-backend)