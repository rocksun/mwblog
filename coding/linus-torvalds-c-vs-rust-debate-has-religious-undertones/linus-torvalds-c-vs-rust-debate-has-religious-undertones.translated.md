# Linus Torvalds：C 与 Rust 之争带有“宗教意味”

![Linus Torvalds：C 与 Rust 之争带有“宗教意味”的特色图片](https://cdn.thenewstack.io/media/2024/09/36a0458b-ahmed-nxtgbruyq34-unsplash-1024x683.jpg)

维也纳 —

[C](https://thenewstack.io/can-darpas-tractor-pull-c-to-rust-for-memory-safe-overhaul/) 和 [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) 为 [Linux 内核](https://thenewstack.io/rust-in-the-linux-kernel-by-2023-linus-torvalds-predicts/) 做出贡献的人员发生了冲突，引发了一场争议，[Linus Torvalds](https://www.linkedin.com/in/linustorvalds/)（[Linux](https://thenewstack.io/rust-in-the-linux-kernel/) 的创建者）将其描述为具有“几乎带有宗教战争意味”。在今天在此举行的 [开源峰会](https://events.linuxfoundation.org/open-source-summit-europe/) 主题演讲中，Torvalds 表示，虽然这场争论涉及一些有益的争论，但其中一些争论变得非常消极。

这场争论始于内核维护者之一（也是一名 C 程序员）因涉及为 Rust 调整 C 插件的“非技术性无稽之谈”而退出。

Torvalds 将这场争论比作关于哪个是更好的文本编辑器的 [vi](https://thenewstack.io/get-to-know-vi-a-text-editor-for-the-ages/) 与 [emacs](https://www.gnu.org/software/emacs/) 之间的文化战争，也被称为“编辑器战争”。

“我认为我实际上很享受。我喜欢争论。我认为 Rust 的一个优点在于它如何活跃了一些讨论，而一些争论变得很激烈……我认为这表明人们有多么关心。与此同时，我不太确定为什么 Rust 一直是一个如此有争议的领域，”Torvalds 说。“这让我回想起我年轻的时候，人们争论 vi 与 emacs，但出于某种原因，Rust 与 C 之间的整个讨论在某些领域几乎带有宗教意味。”

内核开发者：

[@Linus__Torvalds]在 [#OSSummit] 上说：“出于某种原因，整个 [@rustlang] 与 C 之间的讨论几乎带有宗教意味。”[@thenewstack] [pic.twitter.com/6TL7CaViRK]

— BC Gain (@bcamerongain)

[2024 年 9 月 16 日]

## 文化冲突

问题在于，在跨语言边界提交更改时，C 语言和 Rust 语言之间存在文化冲突。从 Rust 的角度来看，修改 C 接口中的内容可能是合理的（反之亦然），而 C 语言人员则希望 Rust 贡献可以插入到 C 中。

这场争论可以追溯到三年前，当时有人提出 Rust 可以提供 C 所没有的某些安全优势，可以成为内核的一部分并可能取代它。尽管如此，该项目并没有停滞不前。

例如，以前可以用 C 和 CPU 生成的著名的缓冲区溢出攻击或漏洞现在几乎过时了。虽然 Rust 提供了某些安全功能和缺点，但与更容易理解的 C 相比，它也更难学习。

本月早些时候，

[Miguel Ojeda](https://github.com/ojeda) 在一条消息中写道，他将“辞去” Linux Rust 项目维护者的职务。

“我将退出该项目。经过近四年的时间，我发现自己缺乏精力和热情来回应一些非技术性的无稽之谈，所以最好把它留给那些仍然有精力和热情的人。

“致 Linux Rust 团队：谢谢你们，你们很棒。与你们所有人共事是一种荣幸；我们花时间讨论技术问题，寻找解决健全性漏洞的方法等，这些都是我始终乐于去做并期待的事情。我很幸运能与如此有才华和友好的团队合作。

“我祝愿该项目一切顺利。我真心相信内核的未来在于内存安全语言。我不是有远见的人，但如果 Linux 没有内化这一点，恐怕其他内核会对它做它对 Unix 所做的事情。”

他还引用了关于 Rust 中文件系统的 [YouTube 视频](https://www.youtube.com/watch?v=WiPp9YEBV0Q&t=1529s&ab_channel=TheLinuxFoundation)：“重申一下，没有人试图强迫其他人学习 Rust 或阻止 C 代码的重构，”Ojeda 写道。

正如 Torvalds 今天所描述的，C 是一种相对“简单的语言”，而且“这是我喜欢 C 的原因之一，也是许多 C 程序员喜欢 C 的原因——即使这幅图画的另一面是，因为它简单，所以也很容易出错，”Torvalds 说。“另一方面，Rust 是一种非常不同的东西。有很多人习惯了 C 模型，他们不一定喜欢这些差异，这没关系。”

## 分歧的学派
与此同时，C 和 Rust 阵营分歧很大。“有些人就是不喜欢 Rust 的概念，也不喜欢 Rust 侵占他们的领域……人们甚至谈论 Rust 集成是一个失败。我提到过我不这么认为——我们已经做了几年了，所以现在说还为时过早，”Torvalds 说。“但我认为即使它成为一个失败（我不认为会），这也是你学习的方式。所以，即使论点不一定总是如此，我也认为外展是一件积极的事情。”

Torvalds 说，挑战在于内存安全架构对基础设施做出某些假设。“例如，基础设施人员可能会害怕，但它已经变得非常公开。似乎是基础设施人员抵制一些改变。公平地说，我的意思是，我们也对 C 基础设施做了很多改变，”Torvalds 说。“内核执行的代码类型不是正常的 C。我们不仅以某种方式编写内容，还因为我们在 C 端有很多工具，这些工具强制执行不属于该语言的基础设施规则，”Torvalds 说。“其中一部分是我们的锁定安全性。我们实际上在 C 端有很多内存安全基础设施，这些基础设施在技术上不属于 C 本身——它们是我们内核的基础设施的一部分，我们有调试版本，可以让内核运行得慢得多，但它们测试了更多内存安全内容。”

显然，Rust 和 C 各有优势，Rust 爱好者提供了有利于他们的有力论据（一旦编译，代码就很好，更广泛等），而主力 C 更容易学习，并且受益于数十年的使用。该上下文适用于以内核为中心的 [eBPF](https://thenewstack.io/what-is-ebpf/) 开发。

正如 [Liz Rice](https://uk.linkedin.com/in/lizrice)，Isovalent 在 [Cisco](http://cisco.com/?utm_content=inline+mention) 的首席开源官告诉 The New Stack，Rust 较新，并且具有“非常强大的优势，但并非每个人都立即知道如何编写 Rust。在内核中处理 eBPF 子系统的很多人不会突然转身学习 Rust，以便他们可以完成自己的工作，对吗？”Rice 说。“我看到人们谈论它，比如‘哦，好吧，我们为什么要 eBPF 验证器？如果我们在 Rust 中完成所有事情，那么你就可以删除它了，”Rice 说。“但我认为当人们这么说时，并没有完全理解 eBPF 验证器的全部目的。你可以用 Rust 编写 eBPF 代码并编译成 eBPF 字节码，所以如果你是一个想要编写 eBPF 的 Rust 开发者，你可以这样做。”

正如 Polar Signals 首席执行官兼创始人 [Frederic Branczyk](https://de.linkedin.com/in/frederic-branczyk) 告诉 The New Stack：“Rust 中有很多示例，你必须做一些不安全的事情，然后在上面构建一个安全的抽象，”Branczyk 说。“所以，就像，我绝对不认为 Rust 将成为一切的救星。顺便说一句，我是 Rust 的忠实粉丝，但我认为 C 实际上是一种非常好的语言来编写操作系统，但 Rust 也可以完成很多工作。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。