
<!--
title: Java 25：Oracle让Java更易学，为AI开发做好准备
cover: https://cdn.thenewstack.io/media/2025/09/8f935504-getty-images-sg2eggqll14-unsplash.jpg
summary: Java 25 发布，简化了初学者入门，通过 JEP 512 减少了样板代码，并支持 AI 开发，包括用于 AI 推理的向量 API 和结构化并发。Oracle 还更新了 AP 计算机科学课程，并推出了 Learn.java 网站。
-->

Java 25 发布，简化了初学者入门，通过 JEP 512 减少了样板代码，并支持 AI 开发，包括用于 AI 推理的向量 API 和结构化并发。Oracle 还更新了 AP 计算机科学课程，并推出了 Learn.java 网站。

> 译自：[Java 25: Oracle Makes Java Easier To Learn, Ready for AI Development](https://thenewstack.io/java-25-oracle-makes-java-easier-to-learn-ready-for-ai-development/)
> 
> 作者：Darryl K. Taft

[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 一直以来都以其对新程序员来说有些令人生畏而闻名，但随着本周发布的 [Java 25](https://www.oracle.com/news/announcement/oracle-releases-java-25-2025-09-16/)，[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 对此有一些看法。

虽然 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) 允许学生用一行代码编写他们的第一个程序，但 Java 传统上会强迫他们通过一连串令人困惑的语法才能打印出“[Hello World](https://thenewstack.io/how-to-define-and-use-your-own-functions-in-python/)”。Oracle 的 Java 25 解决了这个问题。

核心是 [JDK 增强提案 (JEP) 512](https://openjdk.org/jeps/512) **Compact Source Files and Instance Main Methods（紧凑的源文件和实例 Main 方法）**，它消除了令初学者困惑了几十年的令人生畏的 `public static void main(String[] args)`。现在学生可以从以下代码开始：

```py
void main() {

    println("Hello World");

}
```

这不仅仅是删除字符。“学生可以用简洁的方式编写他们的第一个程序，而无需理解为大型程序设计的语言特性，”Oracle 说。[Rémi Forax](https://github.com/forax) 来自 [Université Gustave Eiffel](https://www.univ-gustave-eiffel.fr/en/)，称 JEP 是一个改变游戏规则的提案。

JEP 512 “通过允许初学者编写程序而无需传统的样板代码，从而大大简化了 Java，”他在一份声明中说。

Oracle 对预览版本做出了重要的调整。最初，他们自动导入 IO 方法以使事情更加简单，但后来又撤回了。[Chad Arimura](https://www.linkedin.com/in/chadarimura/) 是 Oracle Java 开发者关系副总裁，他告诉 The New Stack：“我们觉得，为了摆脱这几个字符而使其变得隐式并隐藏起来，会导致当你想扩展你的程序时不得不倒退。”

目标是创建 Oracle 称之为“平滑入口”的东西——帮助初学者入门的功能，但不会在他们的程序变得更复杂时成为障碍。

“JEP 512 背后的想法不仅仅是减少样板代码，尽管这是它的一个极好的副作用，而且它使得对于正在学习 Java 的人来说，语言更加简洁，在概念方面，人们不需要学习很多东西就能编写他们的第一行代码，或者，我应该说，在屏幕上显示他们的第一个 Hello World，”Arimura 说。

该公司表示，除了学生之外，可能不是 Java 专家的系统和 IT 管理员也可以减少编写小型程序（如脚本和命令行实用程序）的正式程度。

“我喜欢 Java 25 如何以一种更易于访问和更具表现力的方式发展该语言，从而摆脱了该语言的一些繁琐的方面（例如，样板代码），”The Futurum Group 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 告诉 The New Stack。

“例如，你不需要将所有内容都包装在源文件中的一个类中，而且你不必在构造函数的开头包含 `super()` 或 `this()` 函数调用，”他说。“这些可能看起来微不足道，但由于现在有如此多的对开发者友好的系统和后端语言可供选择，Java 需要不断发展，以提供新的功能，而不会让开发者陷入繁琐的开销中。这是一项艰巨的工作，但正如你从这两个例子中看到的那样，语言维护者正专注于使 Java 易于采用和愉快地使用。”

## 支持学习生态系统

与此同时，Oracle 通过教育基础设施支持了语言的改变。该公司与大学理事会合作更新了 AP 计算机科学 A 课程，确保高中生学习最新的 Java 而不是过时的版本。Arimura 说，许多学校仍然使用 Java 7 和 8 进行教学。

该公司还推出了 [Learn.java](https://learn.java/)，这是一个专门为编程初学者提供的网站，与以开发者为中心的 [Dev.java](https://dev.java/) 门户网站分开，他说。Java Playground 现在包括代码片段分享功能，允许教师创建编码练习，学生可以直接在他们的浏览器中运行这些练习，而无需安装任何东西。

“学生现在可以从简单的程序开始，并随着他们的成长逐步将他们的理解扩展到更高级的概念，从而创建一个从基本编程概念到完全面向对象编程的平滑学习路径，”Forax 指出。

此外，圣何塞州立大学的荣誉退休教授 [Cay Horstmann](https://www.linkedin.com/in/cay-horstmann-659a4b/?originalSubdomain=de) 说，他看到了更广泛的好处。

“我最喜欢的 Java 25 部分是紧凑的源文件、实例 Main 方法和模块导入声明，因为这些特性为初学者创建了一个低仪式感的 Java 入口，”他在一份声明中说。“它们也使经验丰富的程序员受益，将 Java 的范围扩展到小型、日常的任务。”

随着 Java 接近其第四个十年，Oracle 似乎认识到，语言的采用在很大程度上取决于第一次编程体验，而不是企业能力。

## 尽早培养 AI 技能

Java 25 对初学者的关注也延伸到了 AI 开发。虽然 Python 在机器学习 (ML) 研究中占据主导地位，但 Java 对于企业级生产 AI 系统仍然至关重要。

在与 The New Stack 的一次简报中，Arimura 概述了 Java 与 AI 工作相交的三种模式：

首先，AI 工具越来越多地生成 Java 代码。诸如 [Oracle 的 Code Assist](https://thenewstack.io/oracles-code-assist-fashionably-late-to-the-genai-party/) 之类的服务和具有 AI 功能的流行编辑器可以帮助开发者更快地编写 Java。“有很多 Java 代码正在被 AI 构建和生成，”他说。“我们需要确保它继续是一流的代码。”

其次，现有的应用程序需要添加 AI 功能。Arimura 开玩笑说：“也许你的 CEO 说，我们需要让你的所有应用程序都集成 AI。”“我们在 Oracle 对此并不陌生。”[LangChain4J](https://github.com/langchain4j/langchain4j) 和 [Spring AI](https://thenewstack.io/production-worthy-ai-with-spring-ai-1-0/) 等框架都已在最近发布了 1.0 版本，从而使这种集成变得更加容易。

第三，专门的团队使用 Java 构建定制的 ML 系统，从而利用其性能特征和生态系统。

简化的语法尤其有助于 AI 脚本编写和原型设计。[JEP 511](https://openjdk.org/jeps/511) **Module Import Declarations（模块导入声明）**使得一次性导入整个模块变得更加容易，Arimura 指出，这“有利于将来自流行库的 AI 推理和工作流拼接在一起的简单应用程序。”

此外，[虚拟线程](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) 是在 [Java 21](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) 中引入的，它在 AI 工作负载中得到了广泛采用，因为 ML 推理通常涉及许多不需要完整 OS 线程的并发操作，Arimura 说。

## 从课堂到职业

从对初学者友好的 Java 到 AI 就绪的 Java 的路径变得越来越清晰。从简单语法开始的学生可以逐步学习更高级的功能，例如模式匹配——[JEP 507](https://openjdk.org/jeps/507) **Primitive Types in Patterns, instanceof, and switch（模式、instanceof 和 switch 中的原始类型）** 将其扩展到 Java 25 中的原始类型，并且 [JEP 505](https://openjdk.org/jeps/505) **Structured Concurrency（结构化并发）** 和 [JEP 508](https://openjdk.org/jeps/508) **Vector API（向量 API）** 用于优化计算以及 AI 推理和计算场景。

此外，[Oracle 的 VS Code 扩展](https://inside.java/2023/10/18/announcing-vscode-extension/) 已经接近 400 万次下载，并且获得了 5.0 的评分，从而弥合了这一差距。Arimura 指出，之所以实现增长“是因为有很多新的开发者，很多人正在学习 Java，而且在 AI 领域也正在进行很多工作。[VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 周围集中了很多 AI 开发环境，从而将 Java 开发者引入到这个生态系统中。”

该版本还包括对 AI 工作负载有重要意义的性能改进。[Project Leyden](https://openjdk.org/projects/leyden/) 的提前编译功能（[JEP 514](https://openjdk.org/jeps/514) **Ahead-of-Time Command-Line Ergonomics（提前命令行人体工程学）** 和 [JEP 515](https://openjdk.org/jeps/515) **Ahead-of-Time Method Profiling（提前方法剖析）**) 可以在不更改代码的情况下加快应用程序的启动速度。[JEP 519](https://openjdk.org/jeps/519) **Compact Object Headers（紧凑的对象头）**通过缩小对象头来减少内存使用量。这些优化有助于 Java 应用程序在云环境中高效运行，在云环境中，资源效率直接影响成本。

JDK 25 与 AI 相关的 JEP 包括：

* **模式、instanceof 和 switch 中的原始类型** JEP 507，它使得将业务逻辑与来自 AI 推理的原始类型进行集成变得更加容易。
* **模块导入声明** JEP 511，更轻松地将业务逻辑与 AI 推理、库和/或服务调用集成。
* **向量 API** JEP 508，通常用于 AI 推理和计算场景。
* **结构化并发** [JEP 453](https://openjdk.org/jeps/453)，用于通常涉及并行运行多个任务的 AI 开发。
* **作用域值** JEP 506 使得可以在线程内部和线程之间共享不可变数据，与线程局部变量相比，空间和时间成本更低。

## Java 生态系统加强

Arimura 指出，Java 和 AI 生态系统已经取得了很大的进展，包括 LangChain4j 发布了其 1.0 GA 版本，引入了虚拟线程、模型扩展、代理模式、增强的推理支持、多模态等等。

此外，Spring AI 发布了 1.0 GA 版本，其中包含模型扩展、[模型上下文协议 (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) 集成、工具调用等等。

此外，[Spring Creator](https://www.eweek.com/development/springsource-gains-momentum-in-enterprise-java/) [Rod Johnson](https://www.linkedin.com/in/johnsonroda/?originalSubdomain=au) 的 [Embabel](https://thenewstack.io/meet-embabel-a-framework-for-building-ai-agents-with-java/) [代理框架](https://thenewstack.io/java-for-agentic-ai-app-development-what-you-need-to-know/) 于 5 月份发布，具有面向目标的行动计划、无缝的 LLM 集成等等。

“我们可以看到越来越多地使用 AI 来超越仅仅基于提示的交互。随着情况的变化，自主代理能够学习和适应的想法既有趣（也有点 令人害怕），”Java 平台提供商 Azul Systems 的副 CTO [Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk) 告诉 The New Stack。“我们将需要观察这些工具如何在现实世界的应用程序中发展，以及它们是否按预期工作。”

与此同时，Oracle Java 平台高级副总裁兼 [OpenJDK](https://thenewstack.io/the-hidden-risks-of-unsupported-openjdk-in-financial-systems/) 管理委员会主席 [Georges Saab](https://www.linkedin.com/in/georgessaab/) 表示：“Java 25 突显了 Oracle 在功能和能力方面的持续投资，这些功能和能力为 AI 解决方案提供支持，并简化了语言，使新的开发者和 IT 团队更容易学习 Java。”

一位著名的行业分析师表示，他看到 Oracle 将继续提供新功能，以使 Java 与现代开发保持同步。

IDC 软件开发研究副总裁 [Arnal Dayaratna](https://www.linkedin.com/in/nextgenai/) 在一份声明中说：“随着 Java 迈入第四个十年，它将继续提供各种功能，以帮助确保应用程序（包括那些由 AI 功能提供支持并与 AI 功能集成的应用程序）在硬件平台上高效且可扩展。“Java 处于有利地位，可以提供源源不断的现代功能，以满足下一代由 AI 驱动的应用程序开发的需求。”

## 长期投资

Java 25 是一个长期支持 (LTS) 版本，在 2028 年 9 月之前提供免费更新，并且至少在 2033 年 9 月之前提供商业支持。

该公司表示，这使组织可以灵活地保持应用程序在生产环境中运行更长时间，同时保持最低限度的维护，并最终按照自己的意愿进行迁移。根据 Oracle 免费条款和条件 (NFTC)，Oracle JDK 25 计划在 2028 年 9 月之前每季度收到安全和性能更新，并且根据计划，此日期之后发布的 JDK 25 更新将在 Java SE Oracle Technology Network (OTN) 许可下提供，直至至少 2033 年 9 月。