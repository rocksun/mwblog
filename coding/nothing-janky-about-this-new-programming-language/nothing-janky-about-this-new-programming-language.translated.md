# 全新编程语言，绝非蹩脚之作

![Featued image for: Nothing Janky About This New Programming Language](https://cdn.thenewstack.io/media/2025/01/1d056ff7-fredrick-tendong-hvyepjyehdq-unsplash-1-1024x683.jpg)

由于 [编程语言 ](https://thenewstack.io/programming-languages/) 是 TNS 读者最感兴趣的内容之一，因此我们一直在寻找可能对开发人员产生潜在影响的新语言。[Jeaye Wilkerson](https://www.linkedin.com/in/jeaye/) 的 [jank](https://jank-lang.org/) 是 [Clojure](https://thenewstack.io/stack-overflow-rust-remains-most-favored-but-clojure-pays-the-most/) 的一种方言，他说它可以在 C++ 和 Lua 使用的任何地方使用。它是一种通用的语言，旨在用于游戏和其他用例。

jank 包括 Clojure 的代码即数据理念和强大的宏系统。[Wilkerson] 说，它是一种函数优先的语言，建立在 Clojure 丰富的持久、不可变数据结构之上。

TNS 新闻编辑 Darryl K. Taft 采访了 [Wilkerson]，他最近辞去了在 Electronic Arts (EA) 的工作，专注于 jank 的全职工作，谈论了他的创作。

**是什么引爆点让你决定全职从事 jank 的工作？**

**Wilkerson:** 自从我转到 EA 兼职以来，jank 在过去两年中一直在加速发展。在这一点上，对于一个尚未发布的东西来说，它是一个非常受欢迎的项目，但我仍然觉得我没有足够的时间来处理它。我一直在考虑全职从事 jank 的工作好几个月了。我想引爆点是我妻子说了类似“好吧，你打算做还是不做？”之类的话。

**开发 jank 的主要技术挑战是什么？**

**Wilkerson:** jank 正在将 Clojure 和原生世界结合起来。两者截然不同。为了让 Clojure 在原生环境中运行，我们首先需要能够 JIT 编译原生代码。围绕这个的工具仍然很年轻，我不得不与多个 [LLVM](https://llvm.org/) 开发人员密切合作来解决问题。

除此之外，Clojure 构建在 [JVM](https://www.ibm.com/docs/en/b2b-integrator/6.1.1?topic=management-java-virtual-machine) 之上，该 JVM 已经投入了数十年的开发。为了在原生环境中复制它，我需要有效地构建一个迷你 VM。这包括对象模型、模块加载器、JIT 编译器和垃圾收集器等等。我尽可能使用现成的解决方案，但所有东西都需要手动组合在一起。

最后，jank 旨在从完全动态的语言提供与 C++ 的无缝互操作。这需要在运行时 JIT 编译 C++，以便我们知道值的类型，查找存在哪些函数，进行重载解析，实例化模板，并执行 C++ 的 RAII 保证。据我所见，没有主流的动态语言具有这种级别的与 C++ 的互操作性。主要原因是它非常困难。

**您对 jank 未来一年的发展有什么愿景？**

**Wilkerson:** 在 2025 年，我将发布 jank 的 alpha 版本，供人们开始使用。我将收集反馈，提高稳定性，并开始改变 Clojure 生态系统，使其成为一个对原生具有一流支持的生态系统。

**您如何处理 jank 开发的可持续性/资金问题？**

**Wilkerson:** 今年，我只专注于让 jank 发布。我已准备好不接受任何资金，如果没有任何资金进来。但是，过去，jank 曾收到来自 [Clojurists Together](https://www.clojuriststogether.org/) 的开源资助，我将继续申请这些资助。我的梦想是能够获得报酬来全职从事 jank 的工作，但为了做到这一点，我需要 jank 开始提供价值，并成为 Clojure 生态系统中不可或缺的一部分。如果这没有发生，也没问题。我会在需要的时候找到另一份工作，但我会继续从事 jank 的工作。

**您是完全单干，还是有任何合作者/贡献者？**

**Wilkerson:** 我是唯一一个全职从事 jank 工作的人，但我确实有一些常规贡献者。我还有三位学员，作为 [SciCloj](https://scicloj.github.io/) 指导计划的一部分，我每周与他们会面，并给他们分配任务，以进一步开发 jank 和他们的编译器黑客技能。
建立一个健康的社区对我来说很重要。鼓励人们提供帮助，并让他们更容易做到这一点，是其中的一部分。

**您是否希望围绕 jank 建立一个社区？如果是这样，什么样的贡献最有价值？**

**Wilkerson:** 当然。在接下来的几周内，jank 将变得越来越容易安装。例如，截至今天，它现在可以通过 homebrew 安装，这在上个月是不可能的。随着 jank 变得更容易访问，让人们尝试它，提供反馈，更重要的是，报告错误，对于 jank 今年晚些时候的稳定发布至关重要。
**[Jank 如何处理性能优化，特别是对于资源密集型应用程序？]**

**Wilkerson:** Jank 是用 C++ 编写的，并且具有无缝的 C++ 互操作性，但它不是 C++。它不是一种系统编程语言。它是一种 Clojure 方言，并且具有与 Clojure 相同的性能特征。Jank 在 Clojure 表现良好的任何地方都会表现良好，甚至在其他地方也可能表现良好，因为它在内存使用方面更轻巧并且启动速度更快。

话虽如此，在我达到与 [Clojure](https://thenewstack.io/from-c-to-clojure-new-language-promises-best-of-both) 的对等之后，并且我继续开发 jank 的功能集之外，我将添加对动态性频谱的更多控制，以便 jank 的某些部分可以被锁定，几乎没有动态分配，使用静态类型和单态化函数。

从历史上看，Clojure 并没有强烈关注优化其编译器。它依赖 JVM 来完成所有繁重的工作。Jank 不会遵循这条道路；我认为更智能的编译器可以发挥重要作用，并且每一个唾手可得的成果都将被采摘。

**[您做出的任何特定的技术决策或权衡，您认为其他开发人员会感兴趣了解吗？]**

**Wilkerson:** JVM 是一台经过高度优化的机器。从头开始与之竞争是很困难的，即使从原生开始也是如此。在我所做的微基准测试中，jank 与 Clojure 具有很强的竞争力，但我通过利用以下事实做到了这一点：我正在构建一个专门为 jank 构建的系统，而 JVM 是一个更通用的系统。一个例子是 jank 的对象模型，它不使用虚拟分派来避免 vtables 的成本。[这在 [https://jank-lang.org/blog/2023-07-08-object-model/](https://jank-lang.org/blog/2023-07-08-object-model/) 中有记录。

**[对于考虑对其项目进行类似迁移的其他开发人员，您会提供什么建议？]**

**Wilkerson:** 你只能活一次。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。]