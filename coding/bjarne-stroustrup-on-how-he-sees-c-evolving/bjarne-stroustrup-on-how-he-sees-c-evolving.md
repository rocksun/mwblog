
<!--
title: Bjarne Stroustrup 谈 C++ 的演变
cover: https://cdn.thenewstack.io/media/2025/03/27c57b7a-colorized-bjarne_stroustrup_2013-by-victor-zavyalov-icpcnews-creative-commons-via-wikipedia-copy.jpg
-->

C++ 之父 Bjarne Stroustrup 正在倡导采用强制执行指南的配置文件，以增强该语言的安全性和安全性。

> 译自：[Bjarne Stroustrup on How He Sees C++ Evolving](https://thenewstack.io/bjarne-stroustrup-on-how-he-sees-c-evolving/)
> 
> 作者：David Cassel

“[Bjarne Stroustrup](https://stroustrup.com/) 告诉 TNS，“我希望向广大社区，特别是 WG21 的成员，普及我对 C++ 预期发展方向的看法。”

这位 74 岁的 C++ 创建者，用 40 年的时间观察着他于 1985 年设计的语言的成长。

为了鼓励一些长期以来渴望实现的功能，上个月 Stroustrup 在 *Communications of the ACM* 上发表了“[21st Century C++](https://cacm.acm.org/blogcacm/21st-century-c/)”，这是一篇 6,300 字的文章，承诺展示现代的、类型安全的“21 世纪 C++”的关键概念，以创建“打了兴奋剂的 C++”。例如，在文章中，Stroustrup 强调了在诸如使用[指导原则强制执行配置文件](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3081r1.pdf)编写更安全代码等方法中的长期实验。为了保持与数十年已编写的 C++ 代码的兼容性，Stroustrup 写道：“我们不能改变语言，但我们可以改变它的使用方式……”

然而，这种演变并不完全取决于他。在[文章结尾的一个章节中](https://cacm.acm.org/blogcacm/21st-century-c/#future)，Stroustrup 承认了 [WG21，即标准化工作组](https://isocpp.org/std/the-committee)，以及它将不可避免地在语言的改变程度上发挥作用。“我不愿意对未来做出预测，”Stroustrup 写道，“部分原因是这本身就具有风险，特别是由于 C++ 的定义是由一个庞大的 ISO 标准委员会通过共识控制的。”

“上次我查看时，会员名单上有 527 个条目。这表明了热情、广泛的兴趣和广泛的专业知识，但对于编程语言设计来说并不理想，并且 ISO 规则不能被大幅修改。”

尽管如此，当涉及到关键受众时，Stroustrup 告诉 TNS，“有些人不了解历史，因此错过了关键点，例如指导原则和配置文件符合 C++ 的长期发展方向。”因此，他正在采取措施教育他们，“为此，我必须展示关键功能的位置。”

他详细的文章是一个好的开始，但这只是多管齐下努力的一部分。最终，这一切都可能改变[整个 C++ 生态系统](https://thenewstack.io/introduction-to-c-programming-language/)的轨迹，同时为程序员带来他们长期以来一直渴望的高性能、类型安全和灵活的语言。

并在实现 Stroustrup 自己从 1980 年代就持有的长期目标的同时……

## 紧急行动呼吁

Stroustrup 还直接与 WG21 进行了沟通。[The Register 指出](https://www.theregister.com/2025/03/02/c_creator_calls_for_action/)，“在过去的三年或四年里，行业和政府的网络安全专家一直在劝阻使用 C 和 C++，同时大力推广具有更好内存安全性的语言。”因此，在他发表文章三天后，Stroustrup 向 C++ 标准委员会留下了一份正式说明，他将其描述为“部分是为了应对前所未有的、对 C++ 的严重攻击而发出的紧急行动呼吁”。

“我认为 WG21 需要做一些重要的事情，并且要让人们看到它在这样做。配置文件是一个可以做到这一点的框架。”

Stroustrup 的愿景很明确。他在文章中写道：“指导原则很好而且有用，但在大型代码库中始终如一地遵循它们基本上是不可能的。”需要的是某种强制执行机制，可以实际标记和防止悬空指针、范围错误和空指针解引用等问题。

幸运的是，这种强制执行机制已经以[指导原则强制执行配置文件](https://cacm.acm.org/blogcacm/21st-century-c/#guide)的形式提供。一个脚注提供了它们在 Visual Studio 2019 中的使用示例，它[实现了“Lifetime”配置文件的早期版本](https://habr.com/en/companies/microsoft/articles/437660/)，该配置文件检查 C++ 中悬空指针和引用以及对象生命周期中的其他常见错误……

基本上，每个配置文件都会验证是否满足实现特定结果的要求，通常在编译时进行。除了“Lifetime”检查配置文件外，还有更多计划，包括一个“Bounds”配置文件，该文件确保所有访问数组的代码都包含范围检查安全检查。

在我们的电子邮件采访中，Stroustrup 指出，C++ 已经通过其新的 [span](https://www.geeksforgeeks.org/cpp-20-std-span/) 类模板（于 2020 年推出）支持更好地防止范围错误。“Bounds”配置文件只是确认那些确保边界安全性的函数实际上已经到位。

###
“其中大部分是标准的，并且今天就可以使用，”Stroustrup 告诉我。还有一些计划用于其他几个配置文件，以帮助代码避免类型或算术错误。Stroustrup 认为，“在不久的将来，[Profiles](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3589r0.pdf) 将为强制执行各种约束提供一个框架。”

希望这能为 C++ 提供人们所寻求的[安全保证](https://thenewstack.io/secure-coding-in-c-avoid-buffer-overflows-and-memory-leaks/)。但这也是 Stroustrup 最初的、40 年前对 C++ 的愿景的自然发展。

## “一个更好的近似”

类型安全等特性一直是 Stroustrup 为 C++ 设定的[安全和性能目标](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/)之一。

“自从最早的时候起，这一点就没有改变，”他在文章中写道，并在脚注中引导读者阅读他 1994 年出版的著作 [The Design and Evolution of C++](https://www.stroustrup.com/dne.html)。但与早期版本的 C++ 相比，当代的 C++ 可以更好地实现这些长期目标，部分原因是该语言“被设计为可以进化的”，Stroustrup 在文章结尾写道。因此，经过几十年的改进，他称像 C++ 23（10 月发布的版本）这样的“当代 C++”是他最初理想的“一个更好的近似”。

![](https://cdn.thenewstack.io/media/2025/03/185397eb-cover-of-the-book-the-design-and-evolution-of-c-plus-plus-from-stroustrup-dot-com-202x300.jpg)

他还强调了他在敦促 WG21 采用 Profiles 的说明中的这一点：“正如我之前所说，这也是一个机会，因为类型安全和资源安全（包括内存安全）从一开始就是 C++ 的关键目标。”

“我对此深信不疑。请不要被我相对平静的语言所迷惑。”

Stroustrup 的文章指出，一种不断发展的语言存在一个问题：“许多人对 C++ 的看法仍然停留在过时的观点上”。“今天，我们仍然看到无休止地提到神话般的 C/C++ 语言，通常暗示着一种将 C++ 视为 C 的次要扩展的观点，它体现了 C 的所有最坏的方面，以及对复杂 C++ 特性的怪诞滥用……”但 C++ 正在继续发展，Stroustrup 强调说，改进工作正在进行中，并且已经提供了实验性功能，例如 [异步计算的通用模型](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3109r0.html) 和 [SIMD](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p1928r9.pdf)。

“一个严重的担忧是如何将不同的想法整合到一个连贯的整体中，”Stroustrup 写道。与大多数软件项目（甚至大多数学术界的 CS 工作）不同，设计一种语言需要在“无法得知所有相关因素，并且在数十年内无法显着改变已接受结果的空间中做出决策”。

简而言之，这是一个难题——而且这仍然是一个已知的问题。“几十年来几乎所有语言设计工作都失败这一事实证明了这个问题的重要性。”

但这并不意味着 C++ 已经停止尝试进化……

## 显著的改进

Profiles 并不是 21 世纪 C++ 改进的唯一方式。“我还要指出 [modules](https://en.cppreference.com/w/cpp/language/modules) 是一种用于更简洁的代码和大大缩短编译时间的机制，”Stroustrup 在我们的电子邮件采访中说。

Stroustrup 的文章引用了导入已编译模块而不是使用老式的 *#include* 语句时，速度“提高了 7 到 10 倍”。

“大多数人今天可以通过使用 C++23 提供的功能来显着改进他们的代码，”他告诉我。展望未来，Stroustrup 预测未来会有更多提高性能的功能。“在 C++26 中，我们可能会看到改进的并发支持、静态反射和契约，以及许多小的改进和标准库组件。”

这种前瞻性的希望可能解释了为什么 Stroustrup 希望将他对 Profiles 的呼吁建立在 C++ 更大的历史背景下。Stroustrup 告诉我，他的文章“展示了 C++ 演进的方向。安全保证即将到来，这在 C++ 的背景下并不是一个新颖的想法，而是长期目标的一部分。完全的类型安全和资源安全是 C++ 最初的目标之一，但推动如此广泛的应用领域向前发展需要时间和逐步完成。”

他意识到已经安装的代码库非常广泛，并且 C++“如今涵盖了广泛的应用领域。安全保证必须并将解决 C++ 已经用于交付高质量应用程序的那些领域。

“关注内存安全的人应该注意到 C++ 不是 C，并且基于更安全的编程风格和强化的库的解决方案已经在 C++ 中得到广泛部署。”
我问他的 *ACM* 文章是否产生了影响——尽管这显然很难量化。“我不愿意对未来做出预测，” Stroustrup 说，“但我们已经看到了对泛型编程的更好支持，形式为 [concepts](https://en.cppreference.com/w/cpp/language/constraints)。”

如果你正在寻找有影响力的改进，Stroustrup 指出你也可以关注语言本身之外的东西。目前 C++ 开发人员可以使用各种工具。

“一种语言不仅仅是你在语言规范或正式标准中找到的东西。”