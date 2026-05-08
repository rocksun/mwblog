<!--
title: “真正的成熟度问题”：Anthropic 收购 Bun 后，并非所有开发者都感到兴奋
cover: https://cdn.thenewstack.io/media/2026/05/befaf8d3-screenshot-2026-05-05-at-12.27.34.png
summary: Anthropic 收购 Bun 以驱动 Claude Code，虽其极速启动优势显著，但开发者对其内存占用、大量未解决的 Bug 以及在收购后的发展方向和生产级稳定性表示担忧。
-->

Anthropic 收购 Bun 以驱动 Claude Code，虽其极速启动优势显著，但开发者对其内存占用、大量未解决的 Bug 以及在收购后的发展方向和生产级稳定性表示担忧。

> 译自：["Real maturity problems": Not every developer is thrilled with Bun after Anthropic acquisition](https://thenewstack.io/bun-developers-complaints-anthropic/)
> 
> 作者：Adrian Bridgwater

不断增长和新兴的软件工具集与标准往往容易引发两极分化的反应。[Bun](https://bun.com/) 作为一个全栈式 JavaScript、TypeScript 和 JSX 运行时及工具包，在开发者中引发了不小的争议。

显然，Bun 的命名源于[包子（bao）](https://x.com/bunjavascript)而非[汉堡（burger）](https://theeburgerdude.com/wp-content/uploads/2023/05/Burger-Blog-01-1-1024x1024.jpg)。Bun v0.1.0 于 2022 年 7 月发布，旨在作为广受欢迎的跨平台 JavaScript 运行时环境 [Node.js](http://node.js) 的无缝替代方案。

## Anthropic 的收购

Bun 由 [Jarred Sumner](https://www.linkedin.com/in/jarred-sumner-a8772425/) 创建，Anthropic 于 2025 年 12 月[收购](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)了它，以加速 Claude Code 的能力，并将其作为集运行时、包管理器、打包器和测试运行器于一体的工具。Anthropic 称 Bun 是“AI 驱动的软件工程必不可少的基础设施”。它还将其定义为一种能帮助开发者以史无前例的速度构建和测试应用程序的工具。

作为软件开发者及变现平台 [Meteroid](https://www.meteroid.com/) 的 CEO，[Gaspard Boursin](https://www.linkedin.com/in/gboursin/) 在收购当天发布的一篇 [dev.to 博客文章](https://dev.to/meteroid/anthropic-just-bought-bunjs-heres-why-6bh)中写道：“Claude Code 以 Bun 可执行文件的形式交付。当你安装 Claude Code 时，你实际上就在运行 Bun。这不仅是松散的合作伙伴关系，而是一种依赖关系。”

## Python 显得更慢

据 Anthropic 的 Claude Code 负责人 [Boris Cherney](https://www.linkedin.com/in/bcherny/) 称，Bun 的核心在于极速的启动时间，这为开发者级别的 AI 工具带来了毫秒级的优势。

“当我们开始开发 Claude Code 时，我们研究了许多运行时的选项；Bun 毫无疑问地胜出了，”[Boris Cherney] 在 Bun 官网的一段证言视频中说道。“它的启动时间大约只有 3 毫秒，而 Python 要慢 15 倍。所以对于一个命令行界面（CLI）工具来说，这就是出色用户体验与笨重感之间的区别。”

表面上看，Bun 听起来确实很诱人，那么这款“面包”到底有什么问题呢？

> “Bun 已经变得非常复杂，如果没有这些修复，我怀疑它能否获得像 Node.js 那样生产级的成熟度。” —— Xtergo。

## 过高的内存占用

也许是一个被打造得异常强大、但却不计基础资源代价的工具的典型特征，开发者们一直抱怨 Bun 的内存占用过高。尽管 4 月 20 日发布的 Bun v1.1.13 [宣称减少了 5% 的内存使用](https://x.com/bunjavascript/status/2043841758891741506)，但并非所有人都感到满意。

[Reddit 用户 Xtergo](https://old.reddit.com/r/bun/comments/1snjxyf/bun_is_not_stable_enough_for_production_nor/) 在一篇帖子里抱怨了 Bun 的内存泄漏等问题，尽管他承认这只是对该问题的一次“粗略调查”。

“任何新的运行时都会有真正的成熟度问题，这些问题会随着时间的推移而解决，但我担心 Bun 的开发路线图看起来更像是在不断堆砌功能，而忽视了稳定性问题和 Bug 修复，”[Xtergo] 写道。“Bun 已经变得非常复杂，如果没有这些修复，我怀疑它能否获得像 Node.js 那样生产级的成熟度。”

## 悬而未决的功能性问题

另一个担忧是待处理问题（Open Issues），即软件代码库项目追踪系统中等待处理的未修复 Bug、功能请求或任务。

根据波兰数字忠诚度软件服务公司 Rewardo 的首席技术官 [Wojciech Maj](https://www.linkedin.com/in/wojtekmaj/?locale=en) 的说法，Node.js（作为驱动全球几乎所有设备——可能包括你的牙刷——的运行时）大约有 1,700 个待处理问题。

“Bun 年轻得多，虽然很受欢迎，但采用率远不及前者，却有大约 4,700 个待处理问题，”[Wojciech Maj] 在一篇博客文章中[指出](https://dev.to/wojtekmaj/why-using-bun-in-production-maybe-isnt-best-idea-3deb)。“原始数据永远无法说明全部情况，但这种失衡令人震惊。Node.js 承担着全球性的工作负载，却保持着更精简的待办事项。而尚处于起步阶段的 Bun，已经陷入了泥潭。”

## Bun 已嵌入 Claude Code

Redis 的软件开发者及技术营销主管 [William Johnston](https://www.linkedin.com/in/wwjdev/) 上周在[个人博客](https://wwj.dev/posts/i-am-worried-about-bun/)中发表了看法：他认为 Bun 是一款出色的软件。这主要是因为他发现它既快又实用，而且 Bun 团队更新频繁。对于 [William Johnston] 来说，在小型脚本、应用、测试和工具中使用 TypeScript 是一种“享受”。

但他指出：“Bun 被嵌入到了 Claude Code 中。Claude Code 看起来很‘糟糕’（*此处为脏话*）。所以现在我不得不担心 Bun 也可能变得‘糟糕’。不是因为 Bun 不好，Bun 并不坏。Bun 非常优秀。也不是因为 Bun 团队不再关心它了，我不相信会那样。”

[William Johnston] 认为问题在于，随着 Bun 及其团队进一步融入 Anthropic，其政策也将随之改变。

“正是这些政策导致了 Claude Code 的崩塌。我们是否会看到 Bun 开始出现一些让人觉得团队甚至没有在‘吃自己家狗粮’（亲自试用产品）的问题？我不知道，但为了以防万一，我不确定是否要继续使用它，”[William Johnston] 写道。

## 快乐的 Bun 用户

虽然其他开发者也抱怨过该技术的垃圾回收能力（本质上又是内存管理问题）以及 Bun 被认为[缺乏 Windows 支持](https://chyshkala.com/blog/the-bun-story)，但重要的是要记住，外边也有[一大群非常快乐的 Bun 用户](https://news.ycombinator.com/item?id=47713219)。

围绕 Bun 的激烈争论可能源于 AI 基础设施服务的重要性、它旨在取代的那些根深蒂固且近乎标准化的技术，以及它现在与 Anthropic 一起在 Claude Code 中扮演着前线角色。如果这足以招来一些反对者，那也是意料之中的事。