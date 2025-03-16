# 内存安全 C：TrapC 向 C ISO 工作组的提案

![Featured image for: Memory-Safe C: TrapC’s Pitch to the C ISO Working Group](https://cdn.thenewstack.io/media/2025/03/db26f4e4-getty-images-cuaygar6ujk-unsplash-1024x683.jpg)

![From Rowe's paper.](https://cdn.thenewstack.io/media/2025/03/bbe14992-screenshot-from-trapc-whitepaper-2025-1-300x144.png)

来自 Rowe 的论文。

两周前，C 编程语言的国际标准化工作组听取了企业家 [Robin Rowe](https://www.linkedin.com/in/robinrowe/) 关于 TrapC 的提案，TrapC 是 C 编程语言的一项突破性的*内存安全*扩展。

“在我的演讲之后，有人告诉我应该要求更多的时间，”Rowe 在接受 TNS 的电子邮件采访时说，“30 分钟是不够的。所以是的，有很好的兴趣。”

Rowe 的扩展将与现有的 C 代码“高度兼容”，甚至与 C++“有些兼容”，为世界上大量的现有内存不安全代码提供了另一种前进的道路。

根据 [Rowe 提交的白皮书](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3423.pdf)，最终目标是“使遗留 C 代码能够重新编译成设计上安全且默认安全的执行文件”，而只需很少的代码重构。

C 和 C++ 编程语言在[过去几年](https://thenewstack.io/bjarne-stroustrup-on-how-he-sees-c-evolving/)中一直[受到审查](https://thenewstack.io/secure-coding-in-c-avoid-buffer-overflows-and-memory-leaks/)，因为它们允许开发人员无意中编写带有内存错误的程序，[有缺陷的代码](https://thenewstack.io/google-retrofits-spatial-memory-safety-onto-c/)允许恶意用户用他们自己的恶意代码覆盖内存块。TrapC 可以结束这一整类错误。

## TrapC 的设计方式

为了实现这一切，Rowe 正在领导 Fountain Adobe，这是一个位于华盛顿特区附近的非营利研究机构。它于 11 月成立，“用于维护 TrapC 语言规范并发布免费的开源 TrapC 编译器”，Rowe 告诉我，该非营利组织“今年的资金已到位”，但欢迎公司赞助持续开发。

Rowe 在他的电子邮件中证实，已经有一个编译器可以从标准 C 代码生成 x86、x64 或 ARM 可执行文件，他们现在也在努力支持 TrapC 的其他语言扩展。（他们正在添加关键字 *trap* 以提供默认安全错误处理和 *alias* 以方便运算符和类型重载，同时重用 C++ 代码安全功能，如构造函数、析构函数、*new* 和 [成员函数](https://www.ibm.com/docs/en/i/7.3?topic=only-member-functions-c)。）

最初，Rowe 计划删除两个 C 关键字：*goto* 和 *union*（在论文中被描述为“不安全且已被广泛弃用”）。但“有趣的是，我收到的关于删除这两个功能的反对意见最多，而不是关于新功能的！”Rowe 本周告诉我们——“关于 *union* 的事情是它在 C 中被广泛用于 SSO 短字符串优化……比我想象的更常见。”

所以 Rowe 有了一个新的计划。“TrapC 不会完全删除 *unions*，而只会禁止在 unions 中使用指针。”*goto* 也不会被删除。“如果 TrapC 指针和句柄是安全的，即使遇到 goto，TrapC 也应该进行正确的清理。”

“[C 和 C++ 程序员可能根本不需要学习 Rust 也能参与到内存安全的推进中来](https://www.theregister.com/2024/11/12/trapc_memory_safe_fork/)，”[The Register 写道](https://www.theregister.com/2024/11/12/trapc_memory_safe_fork/)。

## 性能安全

Rowe 周六告诉我，TrapC“有望在 2025 年发布”。他承诺“当有足够的演示时，我们会将其在线发布——这样任何人都可以尝试 TrapC。”

这是一个雄心勃勃的项目。Rowe 将 TrapC 的目标描述为不亚于“在语言层面使 C/C++ 软件无法被黑客入侵，编译出不会被意外行为利用且永远不会崩溃的软件。”

但是有一些具体的技巧可以实现它。

“[当使用 TrapC 编译器编译 C 代码时，所有指针都将成为内存安全指针并受到检查](https://www.theregister.com/2025/03/02/c_creator_calls_for_action/)，”Rowe 在 ISO C 标准机构会议上说，根据 [The Register](https://www.theregister.com/2025/03/02/c_creator_calls_for_action/)。在 TrapC 中，编译器确定哪些指针会超出范围——并将它们设置为零。

根据白皮书，这样做的一个结果是，TrapC 指针“始终指向有效的内存”并且“不会溢出或包含垃圾”。由于 TrapC 知道（并监视）缓冲区大小，因此它知道何时错误的代​​码“会尝试触摸空终止符之后的无效内存”。
但这也能带来性能提升吗？“与 C 编译器不同，TrapC 编译器拥有关于其指针所持有的内存区域的完美信息，”Rowe 告诉我 —— 这意味着它可以更好地进行优化。TrapC 编译器不是逐个检查每个指针访问，而是“TrapC 编译器可以通过使用 AI 代码推理来避免大多数内存安全指针边界检查。”

这让他提出了一个引人深思的断言。“专家们认为内存安全代价高昂，”Rowe 告诉我，“但这一定是真的吗？” Rowe 告诉我，最终 TrapC 的编译代码可能更小 *且* 更快 —— 这意味着在计算性能成本时，TrapC 内存安全“可能 *比* 免费更好……”

性能增强也可能来自其他 TrapC 语言特性。例如，某些编程语言有一个 *try* 关键字，如果尝试不成功，则会抛出一个错误，从而导致该异常的代码分支。但白皮书指出，“在 TrapC 中，引用《星球大战》中尤达的话，‘没有 *try*，只有做或不做’。”

从无错误函数调用返回只会跳过错误处理 *trap* 代码块。该论文承认这是一种新的语法，在 C 或 C++ 中找不到。

因此，与 C 不同，TrapC 通过终止并显示有用的错误消息来响应缓冲区溢出（和其他错误）。

虽然这听起来像是一个微小的变化，但 Rowe 告诉我，TrapC 的 “trap” 错误处理机制“在时间和空间上都优于 C 或 C++ 异常中可用的任何现有错误处理机制。”

## 更多安全改进

Rowe 的白皮书包含了一个代码示例，该代码通常会导致缓冲区溢出错误，但在 TrapC 中，它会终止程序“并显示有用的错误消息”。

但对于任何其他意外的错误情况也是如此，该论文补充道（包括，例如，除以零错误）—— 除非程序员明确创建自己的捕获错误处理程序。

该白皮书还指出了 TrapC 的其他几个安全特性：

- 为了避免常见错误，TrapC 提供了许多现代语言中发现的自动内存管理。
- 虽然 C 也可以通过附加到字符串来触发缓冲区溢出，但“TrapC 字符串会扩展”。
- TypeC 在使用说明符“{}”时，在 `printf` 语句中提供自动类型检查，即`printf("{}",var);`。
- “TrapC `printf()`和`scanf()`是类型安全的、可重载的，并且内置了 JSON 和本地化支持。”
- TrapC 还为其他标准 [C POSIX 库](https://en.wikipedia.org/wiki/C_POSIX_library)函数提供了“包装器”函数。
- C 编程语言包含一个 `free()` 关键字，用于释放内存 —— 如果指针随后访问该位置，则可能会产生错误。但由于 TrapC 的内存管理是自动进行的，因此这永远不是问题，该论文解释说。因此，“为了 C 兼容性，可以在 TrapC 中调用`free()`，但它会被忽略。”
- TrapC “具有基于整数的 ‘十进制’ 定点数据类型，适用于金融交易”
- 该白皮书补充说，将来 TrapC 甚至可能尝试添加线程安全功能，以帮助防止竞争条件。

总之，TrapC “是一种从 C 分叉出来的编程语言，对其进行了更改，使其具有 LangSec 和内存安全，”该论文总结道。“为了实现这一目标，TrapC 试图消除 C 编程语言中的所有未定义行为……”

## AI 驱动的 IDE？

2024 年 3 月，Rowe 还成立了一家名为 TRASEC 的营利性初创公司，该公司致力于生成式 AI 编程技术。

Rowe 告诉 TNS，“到目前为止的资金来自亲朋好友，”并补充说他正在“与风险投资公司聊天”。

TRASEC 正在帮助开发 TrapC 编译器，但这仅仅是个开始。该白皮书称，这家初创公司还希望最终发布一个特殊的 trapc 网络安全编译器 *具有 AI 代码推理* —— 并在 2025 年的某个时候完成。

正如 Rowe [告诉 The Register](https://www.theregister.com/2024/11/12/trapc_memory_safe_fork/) 的那样，“商业计划是将编译器作为免费开源软件提供，并拥有一个 AI IDE，这是我们的付费产品。”

Rowe 在 1 月份 [在 Reddit 的 “Entrepreneurs” subreddit 中回答问题](https://www.reddit.com/r/Entrepreneur/comments/1hnjxf2/ai_research_scientist_and_entrepreneur_robin_rowe/) 时说，他的最终目标是“让 AI 创建无法破解和无法崩溃的软件”。

Rowe 告诉我，“在世界上，生成式 AI 在编写 Python 代码方面取得了长足的进步，”但在编写 C 代码方面仍然“不太擅长”。但是，如果 AI 生成的代码组织得如此良好，以至于它为“模块化”编程提供了全面的支持，并且应用程序的所有单独功能都整齐地隐藏在单独的文件中，该怎么办？Rowe 建议，甚至可以自动生成单元测试：“带有单元测试的模块化代码，而不是意大利面条式代码。”

因此，与 C 不同，TrapC 通过终止并显示有用的错误消息来响应缓冲区溢出（和其他错误）。
他也在研究这个问题。Rowe 的白皮书指出，C 语言目前没有像 Rust 的 Cargo 工具链那样，作为语言本身一部分的标准构建系统。因此，展望未来，“对于 TrapC 来说，拥有像 Rust 这样便携、易于使用的工具链至关重要，这样程序员可以快速轻松地创建可在各种操作系统上运行的构建系统。”

幸运的是，Rowe 已经有一个用于生成 [cmake](https://en.wikipedia.org/wiki/CMake) 构建文件的工具链，这是他为长期运行的（并且是开源的）图形软件项目 [CinePaint](https://en.wikipedia.org/wiki/CinePaint) 创建的。Rowe 领导了 GNU 图像处理程序（或 GIMP）的开源分支，并告诉我“GIMP 维护者放弃 GIMP 的好莱坞分支（后来更名为 CinePaint）的原因是它存在太多错误。可以公平地说，在用 C 语言编写的 CinePaint 中消除内存错误的难度，给了我创建 TrapC 的经验和动力。”

这也让他拥有了一个定制的工具链，它不仅可以生成 cmake 文件的代码，还可以生成类、应用程序代码甚至单元测试的样板代码。（Rowe 的论文指出，它甚至可以“追溯用于可能缺少构建系统的现有项目”。）

根据该论文，“Cmaker 目前支持 C++”，但“对 C 和 TrapC 的支持即将到来。”

## 兼容性和性能

Rowe 的演示文稿中的一张幻灯片承认 TrapC“保留”了 C 语言的极简主义——这意味着它不提供 C++ 版本的模板、异常、函数重载、继承或多态。

Rowe 在我们的电子邮件采访中解释说：“C 程序员告诉我，C 兼容性和高性能是内存安全语言成为可接受替代品的绝对要求。”“20 世纪 70 年代，在 C 语言中放弃内存安全性是一种设计上的妥协。这是性能、普遍性和安全性之间艰难的设计选择——选择两个。我的 TrapC 使命是选择所有三个。

“与 C 高度兼容，并且具有与 C 中的手动内存管理相比不花费任何代价的内存安全性。”

无论其缺点如何，Rowe 的演示文稿中的最后一张幻灯片明确指出 TrapC“保护 C/C++ 指针、*scanf*、*printf* 和 *malloc*。”

它包括 TrapC 的使命宣言。“强化遗留代码：将普通的 C/C++ 代码编译成无法缓冲区溢出、无法崩溃的程序。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)