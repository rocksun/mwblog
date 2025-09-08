
<!--
title: Rust采用为何可能失败（以及如何逆袭）
cover: https://cdn.thenewstack.io/media/2025/09/61794dda-the-blowup-un4paddppau-unsplash.jpg
summary: 亚马逊高级软件工程师 Cohen 指出，许多团队采用 Rust 失败。成功的关键在于：有使用 Rust 的理由；培养 Rust 实用主义者；学习新工具；尽早构建运营能力。Rust 适用于尾部延迟、内存使用等问题，但需预料前期痛苦并做好计划。
-->

亚马逊高级软件工程师 Cohen 指出，许多团队采用 Rust 失败。成功的关键在于：有使用 Rust 的理由；培养 Rust 实用主义者；学习新工具；尽早构建运营能力。Rust 适用于尾部延迟、内存使用等问题，但需预料前期痛苦并做好计划。

> 译自：[Why Your Rust Adoption Will Probably Fail (And How To Beat the Odds)](https://thenewstack.io/why-your-rust-adoption-will-probably-fail-and-how-to-beat-the-odds/)
> 
> 作者：Darryl K. Taft

在过去的十年里，[Russell Cohen](https://www.linkedin.com/in/russell-cohen-b75b9927/) 观察了亚马逊的数百个团队尝试采用 [Rust](https://thenewstack.io/rust-programming-language-guide/)。他们中的大多数都搞砸了。

Cohen 是一位高级软件工程师，负责领导 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 的 Rust 采用工作，他对此毫不掩饰。在本周的 [RustConf 2025](https://rustconf.com/) 活动上，他准确地阐述了为什么大多数组织在 Rust 方面会失败，以及少数成功的组织有哪些不同的做法。

Cohen 表示，他从 [Rust 项目](https://thenewstack.io/rust-project-reveals-new-constitution-in-wake-of-crisis/) 的成功中总结了四个关键见解。团队必须：有使用 Rust 的真正理由；寻找、培养和授权 Rust 实用主义者；学习（或构建）新工具；以及尽早构建运营能力。

## 无人问津的 10 万美元重写

与此同时，Cohen 描述了通常出错的情况。2024 年，亚马逊的一位 Rust 爱好者说服他们的团队用 Rust 而不是 [Python](https://thenewstack.io/what-is-python/) 构建一项新服务。该服务运行良好。三个月后，该项目被重组到另一个团队下。

Cohen 说：“他们采用了一项完全正常运行的服务，并用 Java 从头开始重写。”

为什么会有人丢弃可用的代码？因为新团队看到 Rust 代码库时，发现这是一个陌生的生态系统，他们必须从头开始学习。他们有截止日期要赶，并且已经拥有相当可观的 Python 内部专业知识。他指出，Rust 的重写没有任何商业意义。

Cohen 解释说：“当这个团队继承这项服务时，他们看到的不仅仅是 Rust 代码，而是一整套堆栈。”

## 实际产生重要影响的 10 倍改进

但 Cohen 也讲述了另一个故事。[亚马逊的 Fire TV](https://www.amazon.com/Amazon-Fire-TV-Family/b?ie=UTF8&node=8521791011) 团队正在处理老化的硬件——数百万台设备正在逐渐老化。内存是瓶颈，而且多年的 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 优化已经达到了收益递减的地步，他说。

然而，一位工程师尝试了 Rust。“差异是巨大的。他们能够减少内存使用量，不仅仅是一点点，而是 10 倍，”Cohen 补充道。

这种程度的改进引起了管理层的注意。但他补充说，关键的区别在于“他们没有试图用 Rust 重写整个世界”。他们找到了清晰的 API 边界，并逐个替换组件。

这项工作成功的原因是 Fire TV 确实存在一个 Rust 能够显著解决的问题。Cohen 认为，第一个团队只是觉得 Rust 很酷。

## “我们喜欢 Rust”不是商业案例

Cohen 的规则是，你需要“比现有技术至少高出一个数量级的改进”。

“这很多了。这不是 10% 的速度提升，”他说。“如果你的问题是一个你未来可能会遇到的理论问题，我认为你很难达到这个标准。”

在亚马逊，团队主要选择 Rust 是为了 [尾部延迟](https://thenewstack.io/an-introduction-to-new-linux-filesystem-bcachefs/) 和内存使用，而不是通用的性能。如果你是从 Java 过来的，用 Rust 重写并不会自动使事情变得更快。Cohen 指出：“[JVM](https://thenewstack.io/introduction-to-java-programming-language/) 是一项令人难以置信的工程壮举。”多年的 Java 优化不会因为你切换了语言而消失。

此外，他解释说，他知道一个团队花了数年时间试图重写一项 Java 服务，因为 GC 暂停正在扼杀他们的 [P99 性能](https://thenewstack.io/rust-linux-slos-and-all-things-performance-at-p99-conf/)。这似乎是一个完美的 Rust 用例。但是“他们花了数年时间才达到与 Java 同等的水平，因为他们试图重写的服务已经有了数十年的优化。”

更糟糕的是，“在他们进行多年重写工作的过程中，Java 代码一直在变得更快，”他说。

## 专家问题

根据 Cohen 的说法，拥有 Rust 专家的团队提前放弃的可能性降低 40%。没有专家的团队报告说，使用 Rust 构建和部署更困难。

但是你不能仅仅通过招聘来解决这个问题。Cohen 说：“你需要让 Rust 采用取得成功的人；他们不是空降到你公司的 Rust 专家。”“而是那些知道如何在你的组织中有效工作，现在又成为 Rust 专家的人。”

这些人不是在 Reddit 上发布关于内存安全信息的传道者。他们是实用主义者，他们会编写 bash 脚本来使 Rust 与你的构建系统一起工作，他指出。他们进行教学，构建缺失的工具，并弄清楚如何将 Rust 与你已有的任何基础设施集成。

## 三个月的苦干

Cohen 描述了一个学习 Rust 的模式。第一个月包括阅读书籍，可能还会提交一个小的 pull request。第二个月：“与借用检查器进行一些深刻的灵魂探索，一些黑暗的地方，人们要么坚持下去并学会用 Rust 思考，要么放弃，”他说。

第三个月：终于开始高效工作。“他们不是专家，但他们知道足够多的知识来摆脱困境。”

但这只有在他们有地方可以寻求帮助的情况下才成立。如果没有支持，“时间线可能会变得更长，或者人们会放弃。”

Fire TV 团队通过集体编程会议解决了这个问题——[Advent of Code](https://adventofcode.com/) 问题，每个人都在一个房间里，一个人主导，每个人都在观看。“初学者可以直接学习，专家可以通过教学来学习。”

## 工具轮盘赌

Cohen 承认：“Rust 不像许多其他语言生态系统那样成熟。”这意味着存在差距。很多差距。

当 Fire TV 在二进制文件大小方面遇到困难时，他们找到了 [cargo-bloat](https://crates.io/crates/cargo-bloat)——一个可以准确显示是什么使你的 artifacts 膨胀的工具。事后看来这很明显，但是“每个人都必须在某个地方学习这些知识。”

具有讽刺意味的是，该工具在他们的嵌入式平台上不起作用。因此，他们对其进行了修复并向上游贡献了代码。他说，这就是实用主义者的思维方式的体现。

然而，有时差距更大。例如，[亚马逊的 Aurora 数据库](https://thenewstack.io/amazon-aurora-vs-redshift-what-you-need-to-know/) 团队需要在网络故障下测试分布式系统。没有适用于异步 Rust 的好工具。因此，他们花了几个月的时间构建了 “[turmoil](https://tokio.rs/blog/2023-01-03-announcing-turmoil)”，Cohen 说，“它仍然是他们能力的一个关键组成部分，也是许多团队测试其系统的能力的关键组成部分。”

## 凌晨 2 点的现实检验

工具问题在生产环境中变得危险。Cohen 讲述了一个团队的故事，他们的服务在负载测试中速度很慢：“我们的服务很慢。你有没有看过 [火焰图](https://thenewstack.io/async-rust-in-practice-performance-pitfalls-profiling/)？”

从 [无服务器](https://thenewstack.io/serverless/) 环境中获取火焰图并不容易。该团队必须学习新工具，如何阅读它们以及哪些指标重要。但他们找到了问题。“他们正在为每个请求编译一个正则表达式，”他说。他们解决了这个问题，并将性能提高了 10 倍。

Cohen 说：“如果没有火焰图，他们就只能做出有根据的猜测。”他指出，另一种选择是在凌晨 2 点你的服务崩溃时才弄清楚这一点，这要糟糕得多。

另一个团队在几周内遇到了神秘的性能问题，然后才发现他们的内存分配器在 drop 操作期间将内存返回给操作系统，从而导致整个异步运行时停顿。他们花了“数周时间使用深奥的 Linux 工具”来追踪问题。

## 现在付款还是以后付款

Cohen 赞扬了一位亚马逊工程师，他在 2016 年编写了亚马逊的第一个 Rust 提交，他简单地说：“Rust 迫使你在成本最低的时候预先支付你的技术债务。重新设计你的应用程序以避免竞争条件比在前面进行调试更便宜。使用 Rust 取得成功的团队必须预料到一定程度的前期痛苦，因为他们知道这是值得的。”

事实上，成功的团队会预料到前期痛苦并为此做好计划。他们为学习安排时间。他们尽早投资于工具。他们接受现有的 Java/Python 剧本不适用，他说。

失败的团队将 Rust 视为一个可以直接替代的工具，然后对其并非如此感到惊讶。

## 令人不安的真相

Cohen 表示，他并不想劝退任何人不要使用 Rust。但他说，他已经看到了太多失败的采用案例，不能假装这很容易。

他说：“你不能低估将 Rust 引入组织的成本。”这种语言可能很棒，但组织变革的成本很高。非常昂贵。

对于正确的问题——尾部延迟、内存使用、可靠性——Rust 可以带来变革。但是“如果你要将 Rust 或任何新技术引入组织，你需要有一个真正的理由，”Cohen 说。

Rust 的未来不仅仅是更好的语法或更快的编译。而是“构建一个非常好的生态系统，以至于选择 Rust 变得显而易见，”他说。