
<!--
title: 超越WebAssembly：Ben Titzer的新编程语言Virgil
cover: https://cdn.thenewstack.io/media/2024/06/2c344377-microarch.png
-->

在最近一次对 Microarch 的访问中，Ben Titzer 将 Virgil 描述为一种为构建轻量级高性能系统而设计的语言。

> 译自 [Beyond WebAssembly: Ben Titzer's New Programming Language, Virgil](https://thenewstack.io/beyond-webassembly-ben-titzers-new-programming-language-virgil/)，作者 David Cassel。

WebAssembly 联合创始人 [Ben Titzer](https://www.linkedin.com/in/ben-l-titzer-6b78584/) 一直在思考大问题……

他目前是卡内基梅隆大学 [WebAssembly 研究中心](https://www.cs.cmu.edu/wrc/) 的主任（Titzer 也是该校软件和社会系统系的 [首席研究员](https://s3d.cmu.edu/people/core-faculty/titzer-ben.html)）。该中心专注于推进学术界的 WebAssembly 研究、教授和培训学生，以及广泛支持 WebAssembly 在新领域的应用。

但 Titzer 也继续从事其自创编程语言 [Virgil](https://github.com/titzer/virgil) 的长期工作——以及一个名为 [Wizard](https://github.com/titzer/wizard-engine) 的特殊 [WebAssembly](https://thenewstack.io/webassembly-adoption-its-complicated-says-cncf-survey/) 运行虚拟机，它可能在改变我们运行软件的方式方面发挥作用。

上个月，Titzer 在一个名为 [Microarch Club](https://microarch.club/) 的新 YouTube 频道上 [特别亮相](https://youtu.be/QEB6-V7iTqY?si=84JJU2fEcfYn1JId) 中讨论了他的工作，并接受了物联网平台 [Golioth](https://golioth.io/) 的首席云工程师 [Dan Magnum](https://www.linkedin.com/in/danielmangum/) 的长时间采访。

但这是一个毕生的兴趣。在采访中，Titzer 透露，即使在高中时，他也在 [用 x86 汇编代码编写解释器](https://thenewstack.io/its-no-longer-about-how-you-write-code-but-how-you-operate-it/)，用于一些字节码“我自己编写的”。

在进入研究生院时，Titzer 已经知道他想编写一种名为 Virgil 的新编程语言……

> 在微控制器上安装高级语言
>
> @TitzerBL 描述了可用于将高级语言特性引入微控制器的优化技术，例如引用压缩、ROM 化和可达成员分析。 
> — Microarch Club (@MicroarchClub)
> [2024 年 5 月 24 日]

## Virgil

Virgil 在 GitHub 上的存储库将其描述为“专为构建轻量级高性能系统而设计”的语言（其编译器生成快速的本机可执行文件、WebAssembly 模块或用于 JVM 的 JAR）。“我希望让 Virgil 成为一种出色的系统编程语言，”Titzer 在电子邮件采访中告诉我，“它摒弃了旧有的累赘，但具有编写健壮系统代码的强大功能……例如虚拟机、编译器、内核、网络堆栈等。

“Rust 备受关注，但它无法做到 Virgil 所做的事情。”

Titzer 在播客中深入探讨了更多细节。作为一种用于在最低级别进行编写的语言，Virgil “需要具有允许做‘令人讨厌’和‘危险’的事情的功能，从纯编程语言人员的概念来看。例如，如果你真的深入了解类型安全和类型理论，那么你可能会被你可以使用指向堆栈的指针并以这种方式遍历堆栈这一事实所吓倒。或者你可以将某些东西映射到内存，并且你有一个指向它的指针。或者你可以调用内核。因此，这使它与众不同。”

还有一个更有趣的功能。“我添加了一个功能，你基本上可以只获取机器代码，然后说，‘这是一个函数。这是一个 Virgil 函数——它具有 Virgil 的 ABI。”

Titzer 在播客中迅速承认，这是一个“绝对毫不掩饰的非安全操作”，但“你需要能够做到这一点，因为有一些指令我永远无法说服我的编译器发出，例如 [POPCNT](https://www.felixcloutier.com/x86/popcnt) 或所有 [SIMD 指令](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)……”

这是一个令人兴奋的项目。“C 的统治并非绝对，”Titzer 曾经 [写道](https://news.ycombinator.com/item?id=30705383) 在 2022 年对 Hacker News 的评论中。“Virgil 编译为微小的本机二进制文件，并在三个不同平台的用户空间中运行，没有一丝 [C 代码](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/)，并在 Wasm 和 JVM 上运行以启动。我投入了 12 年以上的时间从无到有引导它，只是为了表明它可以完成，并且我们至少可以拥有一个完全不同的用户空间环境。”

![Virgil 编程语言示例代码（来自 UCLA 页面截图）](https://cdn.thenewstack.io/media/2024/05/df0b6345-virgil-programming-language-example-code-screenshot-from-ucla-page.png)

*变量的类型在其声明语句之后放置。来自 [UCLA](http://compilers.cs.ucla.edu/virgil/overview.html) 页面截图（Titzer 在那里获得了硕士和博士学位）*

在播客中，Titzer 补充说，经过十多年的工作，“这绝对是我坚持最久、投入时间最多的工作……很多个夜晚和周末，都在做这件事。”他还称 Virgil “毫不掩饰地是一种系统编程语言……我的意思是，这是你编写虚拟机时会用到的东西。”

然后他开玩笑说，“我现在正在做这件事，因为我无法*停止*自己编写虚拟机，就像我的一种瘾一样……”

## Wizard

当在播客中被问及 Virgil 是否在任何应用程序中使用时，Titzer 说他是其最大的粉丝。“那里有一个解析器组合器库，那里有套接字库，还有类似的一些东西。它主要是我用它构建系统——你知道，就像大教堂管风琴中的孤独狂人。

*[他笑了。]*带着烛光和斗篷。

“但是，因此，我构建了 Wizard，这是一个运行 WebAssembly 的研究引擎，并且全部用 100% 的 Virgil 编写——没有 C 代码。”

当被问及他对 Virgil 的目标是什么时，Wizard 的重要性出现了。它只是为了进一步研究，还是他正在寻找更广泛的采用？

**Titzer：**我确实喜欢更多采用的想法，但我绝对不想受制于有需求的用户。*[他们笑了。]* **Magnum：**那确实会让事情变得复杂，不是吗？ **Titzer：**“所以请使用它，但不要要求任何东西……”我的意思是，这显然不是一个站得住脚的立场。我确实会处理问题并回复问题之类的事情。但我绝对不是在寻求成功。我不想与 Rust 竞争。我不想与 Zig 竞争。我不想让人们在他们的下一个生产系统中使用它。与此同时，我确实很享受人们使用它并用它做一些很酷的事情，回馈……我的目标是 WebAssembly 研究。因此，我在语言层面上所做的一切都必须集中在改进 Wizard 上，仅仅是因为我没有时间不断地循环解决语言设计问题。

Wizard 的存储库称其引擎/虚拟机为“第一个对 Wasm 字节码进行快速就地解释的 Wasm 引擎”。（“为了快速周转测试和调试，程序还可以直接在内置解释器上运行。”）

但在我们的电子邮件采访中，Titzer 详细阐述道，“我对 Wizard 的主要目标是为研究构建一个足够完整且足够快的灵活 Wasm 引擎。研究与生产有点不同，因此简单、灵活、易于使用、拥有良好的内省和调试工具以及更少的遗留代码都有助于实现这一目标。

“我不想在动态程序分析功能方面与生产引擎竞争。例如，一个合理的用例是从生产中获取一个程序，记录一个跟踪，然后使用其更完整的工具集在 Wizard 中分析该跟踪。”

## “我们必须这样做”

在播客的结尾，Titzer 被问及他对 WebAssembly 未来愿景——如果他看到它在增长并成为我们计算堆栈中更基本的一部分。

“当然……”Titzer 说。“我认为 WebAssembly 应该是通用的软件基底——它应该是软件底层的东西，从这个意义上说，每种语言都编译成它。如果你能够运行它，那么你就能运行所有东西……

“所以这意味着——它需要有更多功能，但它还需要有更多的生态系统渗透和更多工具之类的东西。”

是的。

机器码虽然很有趣，但让我们让它（大部分）消失在通用的可移植软件抽象层之下。

[https://t.co/4XUuFC9S2g](https://t.co/4XUuFC9S2g)
— Ben L. Titzer (@TitzerBL)
[2024 年 5 月 14 日]

除此之外，这将使*分析*每个程序变得容易。“它内置了这种安全模型——就像你对程序所做的事情有一个控制，你通过导入/导出机制有明确的输入和输出。我认为它有如此多不同维度的潜力，我认为——我们必须这样做。”

“显然，CPU 不会消失，”Titzer 澄清道，并补充说，“我们现在拥有的任何指令集架构都不会消失……未来还会有更多的 CPU。”但是当你拥有一个软件基底时，“它会非常清楚应用程序想要什么。而它下面的所有东西，你都可以换掉。这就是虚拟化的全部意义，对吧？”

我问 Titzer 他看到哪些迹象表明我们
[正在走向 WebAssembly](https://thenewstack.io/the-promise-of-webassembly-heads-to-ruby/) 可能成为“软件的最终基底”的世界。

“我看到很多兴趣在非 Web 或无服务器的领域中使用 Wasm，”Titzer 回答道。“作为一种可移植、快速且规范良好的字节码，有许多语言针对它，它有可能以以前的方式对一个领域（例如嵌入式系统、网络物理系统、电子游戏的插件系统）进行编程。
**更正后的 Markdown 格式：**

“轻量级沙盒属性是明确封装的衍生，它允许以各种新方式运行不受信任的 Wasm 代码。”

然后我问他的 WebAssembly 运行引擎 Wizard 是否在将我们带入这个世界中发挥了作用……Titzer 同意它“通过突破引擎空间的限制”使之成为可能，称 Wizard 是“一个研究和孵化平台，用于基于引擎的工具，这些工具在生产引擎中更难探索……”

具体来说，“快速就地解释使所有动态分析和调试工具易于使用。对于生产引擎，这意味着更快的启动和更低的内存消耗，因此动态加载代码的设置可以扩展到更大的模块并具有更快的响应时间；这为使用 Wasm 进行短暂的、短暂的计算解锁了新的可能性，其中大量的 [预先编译](https://en.wikipedia.org/wiki/Ahead-of-time_compilation) 成本会使之变得非常昂贵。”

在播客的结尾，Titzer 说他享受学术界的长期观点，与 CMU 的所有聪明人合作，并为“人类知识的前沿做出贡献。这正是研究的意义所在……”

还有一个考虑因素。“下一代学生？他们需要接受指导，你知道，展示方法……否则，他们最终会从事——LLM 或其他工作。”

*[他笑了]* “他们应该从事 VM 工作……他们应该从事机器代码和优化以及编译器等工作！我想让他们对此感到兴奋……”

我问 Titzer 他是否看到 Wizard 被用于教育环境中——他说他将在下学期自己教授虚拟机的课程中使用它。

而且——始终着眼于未来——Titzer 补充说，“我希望对它进行更多打包，以便其他讲师在其他课程中也能做到这一点……”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。