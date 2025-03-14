# Go 的力量：微软在更快的 TypeScript 工具上的大胆尝试

![Featued image for: Go Power: Microsoft’s Bold Bet on Faster TypeScript Tools](https://cdn.thenewstack.io/media/2025/03/0ca6f42e-highway-393492_1280-1024x682.jpg)

微软已经启动了一项计划，将 [TypeScript](https://thenewstack.io/typescript/) 编译器和工具移植到原生 [Golang](https://thenewstack.io/golang-1-22-redefines-the-for-loop-for-easier-concurrency/) 实现，代号为 “Corsa”。

通过原生实现，微软承诺性能将大幅提升，最高可达 10 倍，这将增强 [开发者体验](https://thenewstack.io/improving-developer-experience-drives-profitability/) 并支持新的 AI 驱动功能。

微软技术院士兼 TypeScript 联合创始人 [Anders Hejlsberg](https://www.linkedin.com/in/ahejlsberg/) 在一篇 [博客文章](https://devblogs.microsoft.com/typescript/typescript-native-port/) 中写道，这项工作还解决了大型代码库中的扩展挑战，在这些代码库中，TypeScript 用户目前会遇到加载时间长、类型检查慢和内存限制等问题。

微软通过将 TypeScript 编译器移植到 [Go 语言](https://thenewstack.io/introduction-to-go-programming-language/)，成功实现了性能提升并应对了扩展挑战。

## 性能

关键的性能改进包括：构建时间缩短约 10 倍，项目加载时间提高 8 倍，内存使用量约为当前实现的一半（预计会有进一步的优化），以及语言服务改进，包括显着加速完成、快速信息、转到定义和查找所有引用。

“原生实现将大大缩短编辑器启动时间，将大多数构建时间缩短 10 倍，并大幅减少内存使用，”Hejlsberg 写道。

新的原生版本在各种流行的代码库中显示出令人印象深刻的性能指标：

- VS Code (1,505,000 LOC): 77.8s → 7.5s (快 10.4 倍)
- Playwright (356,000 LOC): 11.1s → 1.1s (快 10.1 倍)
- TypeORM (270,000 LOC): 17.5s → 1.3s (快 13.5 倍)
- date-fns (104,000 LOC): 6.5s → 0.7s (快 9.5 倍)
- tRPC (18,000 LOC): 5.5s → 0.6s (快 9.1 倍)
- rxjs (2,100 LOC): 1.1s → 0.1s (快 11.0 倍)

事实上，“10 倍的性能提升代表了 TypeScript 和 JavaScript 开发体验的巨大飞跃……”，Hejlsberg 写道。

在一段 [视频](https://www.youtube.com/watch?v=pNlq-EVld70) 中，Hejlsberg 指出，JavaScript（TypeScript 基于它）主要用于“UI 和浏览器使用，而不是像编译器和系统级工具这样的计算密集型工作负载”。他补充说，微软可能已经达到了“我们可以从 JavaScript 中榨取的极限”。

## 移植还是重写

Hejlsberg 说，他的团队知道他们想要做的是移植，而不是将 TypeScript 编译器重写为 Go。

在 TypeScript 工作的 [FAQ](https://github.com/microsoft/typescript-go/discussions/410) 中，TypeScript 团队的开发负责人 [Ryan Cavanaugh](https://www.linkedin.com/in/ryan-cavanaugh-aa4a37106/) 写道：

“广义上讲，更改语言时可以采取两种可能的策略：

- 在“重写”中，您从零开始，实现一个新系统，该系统尝试解决与原始系统相同的问题，而忽略原始代码库的实现策略
- 在“移植”中，您采用现有的代码库并将其转换为新语言，同时尝试尽可能多地保持相同

移植执行速度更快，但要求新语言在架构上至少与原始语言兼容……”

## 为什么选择 Go？

Hejlsberg 说，微软尝试了所有常见的嫌疑目标语言（C#、C++、Rust 等）的原型设计，但发现 Go 是他们试图完成的特定工作负载最合适的语言。

“非常有趣！JS 开发者不幸地习惯了慢速工具，因此更快的编译器可以缩短编辑器启动时间，这非常受欢迎，”Arcjet 的 CEO [David Mytton](https://www.linkedin.com/in/davidmytton/) 告诉 The New Stack。“迁移到原生编译器很有意义，尽管 Go 对于这种类型的项目来说是一个不寻常的选择。当我看到这个公告时，我以为它会像大多数其他 JS 工具重写一样使用 Rust：[Rolldown](https://rolldown.rs/), [Turbo](https://turbo.build/) (它 [从 Go 迁移到 Rust](https://vercel.com/blog/how-turborepo-is-porting-from-go-to-rust)), [Deno](https://github.com/denoland/deno)… 我想知道这个决定背后的原因。”

在 FAQ 中，Cavanaugh 在回答这个问题时写道，在考虑特定于这种情况的多个标准时，Go 做得最好。
“到目前为止，最重要的方面是我们需要保持新代码库尽可能地兼容，无论是在语义方面还是在代码结构方面，”他写道。“我们希望在未来相当长的一段时间内维护这两个代码库。允许结构相似的代码库的语言为进行代码更改的任何人提供了显著的优势，因为我们可以轻松地在两个代码库之间移植更改……”

基于 Go 的实现可在 GitHub 上找到（typescript-go 仓库），目前能够加载许多流行的 TypeScript 项目，包括 TypeScript 编译器本身。

## 版本

Microsoft 预计将在 2025 年年中发布原生 `tsc` 的预览版，该版本能够进行命令行类型检查。`tsc` 是 TypeScript 编译器。预计到 2025 年底，将实现用于项目构建和语言服务的完整功能。

最新的 TypeScript 版本是 TypeScript 5.8，TypeScript 5.9 即将推出。基于 JS 的代码库将继续开发到 6.x 系列，TypeScript 6.0 将引入一些弃用和重大更改，以与即将推出的原生代码库保持一致，Hejlsberg 说。

“当原生代码库与当前的 TypeScript 达到足够的对等时，我们将将其作为 TypeScript 7.0 发布，”他说。

并且，“为了清楚起见，我们将简单地将它们称为 TypeScript 6 (JS) 和 TypeScript 7 (native)，因为这将是可预见的未来的命名法，”Hejlsberg 写道。“您可能还会看到我们在内部讨论或代码注释中提到 ‘Strada’（最初的 TypeScript 代码名称）和 ‘Corsa’（此工作的代码名称）。”

与此同时，除了速度之外的好处还包括支持跨整个项目的即时、全面的错误列表以及更高级的重构功能。它还能够提供以前计算成本过高的更深入的代码见解，并为增强开发的下一代 AI 工具奠定基础。Microsoft 还在转向语言服务器协议 (LSP)，以便更好地与其他语言保持一致。

“TypeScript 的核心价值主张是卓越的开发者体验，”Hejlsberg 写道。“随着您的代码库的增长，TypeScript 本身的价值也会增长，但在许多情况下，TypeScript 一直无法扩展到非常大的代码库。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。