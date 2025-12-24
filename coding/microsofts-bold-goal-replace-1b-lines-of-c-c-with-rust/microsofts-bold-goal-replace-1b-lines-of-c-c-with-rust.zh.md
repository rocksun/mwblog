[微软](https://news.microsoft.com/?utm_content=inline+mention) 正在招聘顶级工程师，以帮助淘汰其最大代码库中的 [C 和 C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/)，并用 [Rust](https://thenewstack.io/rust-programming-language-guide/) 替代这些代码。

在 [LinkedIn 上发布的一则招聘信息](https://www.linkedin.com/posts/galenh_principal-software-engineer-coreai-microsoft-activity-7407863239289729024-WTzf/) 中，微软的杰出工程师 Galen Hunt 写道：“我的目标是在 2030 年前从微软代码库中彻底清除每一行 C 和 C++ 代码。”

在回答评论者关于为什么选择 Rust 而不是 [C# 等其他（更熟悉）的语言](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/) 的问题时，Hunt 提到了内存安全和并发性。

他写道：“选择 Rust 而非 C# 有两个原因：1) C# 是内存安全的，但并非并发安全的；2) 性能（无垃圾回收）。仅仅在微软内部，我们就有一大约十亿行代码需要重写。放眼整个行业，可能需要重写的代码量在 200 到 400 亿行之间。”

## 他们将如何做到？

Hunt 表示，微软将结合人工智能和算法来重写微软最大的代码库。

他写道：“我们的北极星目标是‘1 名工程师，1 个月，100 万行代码’。”

Hunt 将这个过程描述为“以前难以想象的”。然而，该公司已经构建了一个强大的代码处理基础设施来应对这项任务。

他写道：“我们的算法基础设施能够大规模地在源代码上创建可扩展的图。然后，我们的人工智能处理基础设施使我们能够应用由算法指导的人工智能代理，进行大规模的代码修改。”

此外，这个基础设施已经在 [代码理解](https://research.google.com/pubs/using-an-llm-to-help-with-code-understanding/) 等问题上大规模运行。

## 加入团队

Hunt 强调了他的团队中技能多样性的重要性。

他写道：“我们承担大胆的风险。”

Hunt 写道：“我们的团队秉持成长型思维。我们是一个多元化的团队，拥有广泛的技能和视角。我们已经认识到，我们的多样性和成长型思维对于在快速变化的人工智能工具世界中取得成功至关重要。”

Hunt 正在招聘一名 [首席软件工程师](https://careerhub.microsoft.com/careers/job?domain=microsoft.com&pid=1970393556639051)，以帮助微软发展和增强其基础设施，从而能够将微软最大的 C 和 C++ 系统翻译成 Rust。

Hunt 说：“这个职位的一个关键要求是具备使用 Rust 构建生产级系统级代码的经验——最好至少有 3 年使用 Rust 编写系统级代码的经验。强烈希望具备编译器、数据库或操作系统实现经验。虽然不要求具备编译器实现经验，但要求有意愿在我们的团队中获取该经验。”

他写道，Hunt 的团队是 [微软 CoreAI](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/) 中 EngHorizons 组织下的“未来可扩展软件工程”小组的一部分。

他说：“我们的使命是构建能力，使微软和我们的客户能够大规模消除技术债务。”

## 逐步转向 Rust

微软转向 Rust 的信号已经发出了一段时间。

早在 2022 年，微软 [Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) 首席技术官 [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) 就在 X（前身为 Twitter）上发帖称，对于需要非垃圾回收语言的场景，“是时候停止所有新的 C/C++ 项目，转而使用 Rust 了”。

此外，在 9 月份举行的 [RustConf 2025](https://rustconf.com/) 大会上，Russinovich 谈到了 Rust 如何帮助微软解决 Windows 的安全问题等。

他指出，C 和 C++ 允许你编写看起来没问题但会严重崩溃，或者更糟的是，被黑客攻击的代码。Russinovich 说，微软自己的内核每月都会通过处理图形和窗口的 Win32k.sys 泄漏权限提升漏洞。

在 RustConf 2025 大会上的主旨演讲“从蓝屏到橙蟹：微软的 Rust 革命”中，Russinovich 将这种情况描述为“一个地下油库，每次只泄漏几滴油，但持续不断。”

因此，该公司开始用 Rust 重写部分代码。不是整个系统，只是其中的一些片段。如果你现在查看你的 Windows System32 文件夹，你会找到一个名为 win32kbase_rs.sys 的文件。那是运行在你内核中的 Rust 代码。

真正重要的是：Russinovich 说，当安全研究人员在新版 Rust 代码中发现一个 bug 时，它导致系统崩溃，而不是让攻击者控制系统。

他说：“我们认为这是一个成功。如果这段代码是用 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 编写的，这个 bug 实际上可能导致潜在的权限提升，而不是一个非常确定且无法被利用的蓝屏崩溃。”