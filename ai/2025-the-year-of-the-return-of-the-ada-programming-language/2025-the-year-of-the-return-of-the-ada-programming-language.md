<!--
title: 2025：Ada编程语言能否强势复苏？
cover: https://cdn.thenewstack.io/media/2026/01/88ad96d3-year-wrapup-1.png
summary: Ada语言2025年回潮，进入TIOBE和PYPL榜单。其内存安全、SPARK形式验证及在航空航天等关键系统中的应用是主要推动力，生态系统现代化也助其发展。
-->

Ada语言2025年回潮，进入TIOBE和PYPL榜单。其内存安全、SPARK形式验证及在航空航天等关键系统中的应用是主要推动力，生态系统现代化也助其发展。

> 译自：[2025: The Year of the Return of the Ada Programming Language?](https://thenewstack.io/2025-the-year-of-the-return-of-the-ada-programming-language/)
> 
> 作者：Darryl K. Taft

在 2025 年，[Ada 编程语言](https://www.adacore.com/languages/ada)迎来了一次可谓是“卷土重来”的时刻。（[但还不要称之为“回归”](https://www.youtube.com/watch?v=vimZj8HW0Kg)！）

去年三月，Ada 闯入 [TIOBE 索引](https://www.tiobe.com/tiobe-index/ada/)前 20 名（达到第 18 名），到七月，Ada 更是跻身前 10 名（达到第 9 名——其在 TIOBE 上的历史最高位）。现在它又回到了第 18 名。

此外，本月 Ada 也进入了[编程语言流行度指数（PYPL）](https://pypl.github.io/PYPL.html)前 10 名，位列第 9。

尽管 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/)、C/C++ 和 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 等编程语言继续位列最受欢迎的语言之列，但 Ada 兴趣的重新兴起，部分原因可归结为对使用更多[内存安全语言](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)的推动。

[AdaCore](https://www.adacore.com/) 的产品经理 Tony Aiello 表示，在一个日益关注软件安全性的世界中，Ada 脱颖而出，该公司为任务关键型系统提供软件开发工具。

Tony Aiello 说：“Ada 是拥有最悠久、最强大血统的语言：Ada 从一开始就是为安全、关键安全系统设计的。”“Ada 提供强大的静态类型和运行时内存安全，这是两种日益增长的语言特性需求。”

Tony Aiello 告诉 The New Stack，此外，多亏了 [SPARK](https://en.wikipedia.org/wiki/SPARK_(programming_language))，它为 Ada 带来了演绎形式验证，开发者可以在软件执行之前证明静态内存安全性和运行时错误的缺失，从而保证消除大量严重的安全漏洞。SPARK 是一种基于 Ada 的编程语言，旨在开发高完整性软件。

他说，这些能力使 Ada 在最近备受关注的航空航天、国防和汽车行业中尤其受欢迎。

同时，The Futurum Group 的分析师 Brad Shimmin 表示：“Ada 证明了一种能够提供并发性和安全性的语言，可以在近五十年的时间里保持其可行性。”“目前，强类型和健壮内存管理等特性正在全面推动人们对 [Rust](https://thenewstack.io/rust-programming-language-guide/) 和 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 等语言的兴趣，因为开发者可以构建对稳定性与安全性都较少担忧的软件。对于 Ada 而言，很容易看出这些技术和能力，例如运行时和编译时检查，使其成为需要提供性能和稳定性的规模化项目的绝佳选择。”

> 根据一篇[AdaCore 博客文章](https://www.adacore.com/blog/what-would-ada-think-of-the-rise-in-ada-language-popularity)所述，Ada 是一种用于开发安全、可靠、高性能软件的强大语言。它结合了强类型、内存安全、高效代码生成和精确的低级控制，使其成为高完整性系统的理想选择。

该文章还说，“作为一种命令式、过程式语言，Ada 对于有 C、C++ 或 Rust 经验的开发者来说会感到熟悉。”

## 更新 FAA 系统

美国[联邦航空管理局 (FAA)](https://www.faa.gov/) 在其[空中交通管制](https://www.faa.gov/air_traffic) (ATC) 系统中广泛使用了 Ada。1989 年，[IBM](https://www.ibm.com/solutions/automation?utm_content=CPWWW&p1=Display&p2=434371219&p3=227599223&utm_term=20APO&utm_content=inline-mention) 与 FAA 签订合同，开始与该机构合作，交付先进自动化系统 (AAS) 项目，这是一项雄心勃勃的全面现代化 ATC 系统的努力。AAS 计划包含 200 万行 Ada 代码。FAA 对 Ada 的兴趣与美国国防部 (DoD) 要求其系统使用 Ada 的规定不谋而合。

![](https://cdn.thenewstack.io/media/2026/01/8e7fe2f9-a-c-q6lmojl7ofm-unsplash-1.jpg)

美国国防部于 1987 年将 Ada 定为其标准语言，但此规定通过 1991 年《国防拨款法案》成为法律，该法案于 1991 年 6 月 1 日生效，并要求武器系统和其他任务关键型系统使用 Ada。该规定于 1997 年终止。

然而，Ada 继续被用于航空业的关键系统，包括波音 777 等商用飞机，以及全球各种空中交通管制系统。

随着[特朗普政府誓言改革空中交通管制](https://www.faa.gov/new-atcs)，[FAA 将如何处理](https://www.faa.gov/newsroom/brand-new-air-traffic-control-system-bnatcs-fact-sheet)所有这些 Ada 代码的问题随之而来？他们是否正在考虑转向 Rust 或新的语言？

> Shimmin 说：“从 Ada 转向 Rust 听起来像是一项相当艰巨的任务。”他问道：“你认为，基于我们从 IBM 那里看到的一些将 [COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/) 重构为 Java 的早期工作，我们是否会看到越来越多这种重大的迁移/现代化努力？”

Shimmin 补充说，他猜测“生成式和代理式人工智能的兴起实际上会降低公司认为需要‘现代化’已经运行良好且有效的代码的可能性。我认为这归结于这样一个事实，即维护的最大问题是领域专业知识和机构知识，而这两个领域恰好是人工智能大放异彩的地方。”

## Ada 与 AI？

谈到人工智能，AdaCore 的 Aiello 表示，Ada，尤其是 SPARK，是 AI 辅助开发最适合的语言。

他说：“Ada 和 SPARK 都将自检功能嵌入到语言中，允许大型语言模型 [LLM] 在开发代码时更精确地推理，并为用户提供不仅没有常见编程错误，而且功能正确的代码。”

## 推动 Ada 流行度的其他因素

除了 Ada 的内存安全和其他特性，一些观察家认为其近期人气飙升还有其他原因。

AdaCore 社区和宣传经理 Fabien Chouteau 说：“Ada/SPARK 生态系统的现代化，例如 [Alire 包管理器](https://alire.ada.dev/)或 [VS Code 插件](https://marketplace.visualstudio.com/items?itemName=AdaCore.ada)，也可以解释语言流行度指数的近期增长。”Alire 也被称为 Ada 库存储库。

同时，Fabien Chouteau 表示：“我们还目睹了新的 Ada/SPARK 开发者加入社区的良性循环，推动新的协作倡议，从而吸引新人学习和贡献。”

此外，[Nvidia](https://www.nvidia.com/en-us/) 对 Ada 的兴趣也可能在其中近期流行度中起到一定作用。

Forrester Research 的分析师 Andrew Cornwall 表示：“Ada 在 TIOBE 指数中的排名很可能受到 Nvidia 对 Ada 和 SPARK 进行实验的影响，并且可能因为他们也有同名产品而混淆。”

确实，Nvidia 提供其 [DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) 产品和 Nvidia [Ada Lovelace 架构](https://www.nvidia.com/en-us/geforce/ada-lovelace-architecture/)。

## Ada 的历史

Ada 以 [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) 命名，她被认为是世界上第一位计算机程序员。

根据维基百科，“Ada 是一种结构化、静态类型、命令式和面向对象的高级编程语言，灵感来自 Pascal 和其他语言。它内置了契约式设计 (DbC)、极强类型、显式并发、任务、同步消息传递、受保护对象和非确定性的语言支持。Ada 通过使用编译器查找错误而不是运行时错误来提高代码的安全性和可维护性。”

该语言是由法国计算机科学家 Jean Ichbiah 领导的 Honeywell 团队在 1977 年至 1983 年受美国国防部合同委托创建的，旨在取代当时美国国防部使用的 450 多种编程语言。

此外，Ada 最初是为[嵌入式](https://en.wikipedia.org/wiki/Embedded_system)和[实时](https://en.wikipedia.org/wiki/Real-time_computing)系统设计的。随后，由 [Intermetrics](https://en.wikipedia.org/wiki/Intermetrics) 的 S. Tucker Taft 在 1992 年至 1995 年间设计的 [Ada 95 修订版](https://www.adaic.org/ada-resources/standards/ada-95-documents/95intro/)，改进了对系统、数值、金融和[面向对象编程](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP) 的支持。Taft 目前是 AdaCore 的副总裁兼语言研究总监。

## 预防错误的语言

同时，去年由主席 Tobias Philipp、副主席 Christina Unger、Dr. Hubert B. Keller 以及 Ada Deutschland e.V. 的专家撰写的[Ada Germany 的一篇文章](https://gi-radar.de/372-sicherer-durch-ada/)中指出，“像 Ada 这样的编程语言可以通过强类型和广泛的编译时和运行时检查，系统地预防所有类别的错误。在 Ada 中，数组不仅仅是指向第一个元素的指针，而是一个本质上包含其索引类型和边界的语义结构。读写操作都由编译器和运行时进行验证。”

> 此外，[该文章](https://www.adacore.com/blog/safer-with-ada)认为，由[通用弱点枚举](https://cwe.mitre.org/) (CWE) 定义的[25 大软件弱点](https://cwe.mitre.org/top25/index.html)中的 12 个“将被 Ada 及其在编译时和运行时的语法和语义检查机制所排除——仅通过选择编程语言即可预防，无论编码错误如何。”

## 其他 Ada 用户

AdaCore 编制了一份每天依赖 Ada 语言的组织名单，展示了 Ada 如今的各种用途。

其中包括伦敦的[维多利亚线](https://tfl.gov.uk/tube/route/victoria/)，它被誉为世界上第一个全自动地下铁路。其自动列车运行 (ATO) 系统使用 Ada 进行主控制逻辑，而紧急制动系统则使用 SPARK 编写。

此外，[法国巴黎银行](https://group.bnpparibas/en/)，世界领先的银行和金融服务机构之一，使用 Ada 来增强其满足风险计算模型需求的能力。AdaCore 解释说，Ada 赋能了一个健壮可靠的风险计算引擎，该引擎能够以高精度、高性能和高可靠性处理每日数百万次请求。

[Deep Blue Capital](https://deepbluecap.com/) 使用 Ada 来实现每秒执行数千笔交易的交易算法。AdaCore 报告说，该公司的工程师选择 Ada 不仅因为其效率，还因为它具有编译时安全特性、强类型和内存安全保证。

此外，法国软件供应商 [Stratégies Romans](https://www.romans-cad.com/en/company) 使用 Ada 开发了一套全面的 3D 计算机辅助设计 (CAD) 套件。他们的软件支持一系列设计和建模任务，并被工业环境中的工程师和设计师使用。AdaCore 指出，Ada 在这里的应用表明，Ada 同样适用于大型交互系统，而不仅仅是嵌入式控制器。