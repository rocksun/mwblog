
<!--
title: 30年前Java如何引发了一场开源革命
cover: https://cdn.thenewstack.io/media/2025/05/1e51165f-priscilla-gyamfi-jd9dmh1lxea-unsplash-1-1.jpg
summary: Java三十周年引爆开源革命！JAR文件和Maven构建依赖管理，奠定现代编程语言如JavaScript的npm、Python的pip等基础。Go是例外。Maven Central托管超67万开源项目，年增长7%。未来或出现AI专属语言，Java仍是现代语言的祖父！
-->

Java三十周年引爆开源革命！JAR文件和Maven构建依赖管理，奠定现代编程语言如JavaScript的npm、Python的pip等基础。Go是例外。Maven Central托管超67万开源项目，年增长7%。未来或出现AI专属语言，Java仍是现代语言的祖父！

> 译自：[How Java Sparked an Open Source Revolution 30 Years Ago](https://thenewstack.io/how-java-sparked-an-open-source-revolution-30-years-ago/)
> 
> 作者：Darryl K Taft

[Java](https://thenewstack.io/introduction-to-java-programming-language/) 本月迎来了30周年，但它仍然蓬勃发展。根据 [Brian Fox](https://www.linkedin.com/in/brianefox/)（[Sonatype](https://www.sonatype.com/) 的创始人兼 [Maven Central](https://central.sonatype.com/) 的管理者）的说法，该语言最伟大的遗产可能在于它在普及 [开源软件开发](https://thenewstack.io/open-source/) 方面所起的作用。

“这让我觉得自己老了，” Fox 在被问及 [Java 三十周年里程碑](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech) 时笑着承认。但就此而言，年龄带来了智慧和令人印象深刻的业绩，并且还在不断增长。

## 开源催化剂

Fox 说，在 1995 年 Java 出现之前，将开源代码合并到项目中非常困难。开发人员面临着令人沮丧的仪式：寻找 C 文件、复制和粘贴代码，并花费数周时间试图编译任何东西。 “这似乎总是比自己编写代码更费劲，” Fox 告诉 The New Stack。

然而，Java 改变了一切。 Java ARchive ([JAR](https://thenewstack.io/how-to-find-dangerous-log4j-libraries/)) 文件的引入创建了易于使用的模块，而 [Maven](https://maven.apache.org/) 的出现使依赖管理成为可能。 突然，开发人员可以理解和管理任何重要库附带的复杂依赖关系网络——使单个 JAR 文件工作所需的“15 或 100 个其他东西”。 Maven 是一个项目管理和构建自动化工具，主要用于 Java 项目。

“我清楚地记得我第一次能够构建一个开源项目，” Fox 说。 “你可以查看代码并说，‘我想这样更改它’，但你可能要花一个星期才能弄清楚如何构建它。”

其影响是变革性的。 通过降低准入门槛，Java 使一代开发人员能够为开源项目做出贡献。 该语言的模块化和可移植性，加上 Maven 的标准化依赖关系处理方法，创建了一个蓝图，将影响随后的其他编程语言，Fox 说。

## 现代开发的模板

Fox 说，如果你看看当今任何现代编程语言的生态系统，你都会看到 Java 的一些 DNA：[JavaScript](https://thenewstack.io/javascript/) 的 [npm](https://thenewstack.io/is-npm-a-hotbed-of-malware/)、[Python](https://thenewstack.io/python/) 的 [pip](https://thenewstack.io/how-to-use-python-pip-and-why-you-need-to/)、[.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) 的 NuGet 和 [Ruby](https://thenewstack.io/ruby-devs-try-sinatra-before-moving-up-to-ruby-on-rails/) 的 [gem](https://thenewstack.io/ruby-devs-try-sinatra-before-moving-up-to-ruby-on-rails/) 都借鉴了 Java 和 Maven 开创的概念，他说。

“后来的语言基本上复制了所有这些概念，”他说。 “你可以看到，我认为在影响后来的语言方面，Java 和 Maven 出现了一个转折点。”

但 Fox 说，一个值得注意的例外证明了这一规则。 Fox 说，当 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 在没有默认包管理器的情况下启动时，它与 10 到 15 个相互竞争的标准作斗争。 “我认为这实际上减缓了采用，”他指出。 “直到他们真正专注于该生态系统的单一、明确定义的包管理器时，它才开始变得更容易访问。”

## 这么多年后仍在增长

尽管人们经常预测 Java 会消亡，但数字却讲述了一个不同的故事。 Sonatype 运营的 [Maven Central](https://central.sonatype.com/) 托管着超过 671,000 个开源项目——而且这个数字还在以每年 7% 的速度增长，Fox 说。 更令人印象深刻的是，仅在过去一年中，这些项目的下载量就激增了 36%。 Fox 说，Maven Central 是世界上最大的开源 Java 组件存储库。

“我们谈论 Java 已经过时且不再酷了，每个人都想做一些不同的事情，” Fox 说。 “但现实情况是，仍在 Java 上开发的软件数量持续增长。 我们还没有看到曲线的顶部。”

这种持续的增长使 Java 与近年来出现的专业语言区分开来。 Python 在数据科学和人工智能领域占据主导地位，JavaScript 统治着前端开发，而 Go 在云部署中找到了自己的利基市场。 但 Fox 解释说，没有一种语言能像 Java 那样广泛地作为通用语言。

## 成熟度优势
一个主要的干扰来自于从 Java 8 过渡到更新版本，特别是模块系统的引入。这造成了采用上的障碍，让人想起 Python 从 2 版本到 3 版本的痛苦迁移，虽然没有那么严重，Fox 说。许多组织仍然停留在 Java 8 上，但 Fox 指出，一旦他们克服了这个障碍，保持更新就会变得容易得多。

## 通过稳定性实现安全

Java 成熟的生态系统还有另一个优势：安全性。Fox 指出，与 npm 和 Python 仓库中成千上万个潜在恶意组件相比，Maven Central 多年来只出现了少数几个。这并非偶然——这是经过几十年发展而来的既定标准和精心管理的结果。

“部分原因在于 Java、Maven 以及 Sonatype 运行的中央仓库所制定的一些标准，” Fox 解释说。他的公司已经花费了 20 多年的时间来帮助组织负责任地利用开源，同时避免许可违规和安全漏洞。

## 接下来会发生什么？

那么，最终会用什么来取代 Java 呢？Fox 非常坦诚：“显然，在某个时候会有东西取代它，但我已经等了很长时间了。”

他很难在当前的语言中找到一个明确的继任者。Fox 说，Go 在十年前似乎很有希望，但已经稳定在它的云原生领域。下一个重大转变可能根本不是一种新的、人类可读的语言，他说。

“我认为下一种语言很可能只是为 AI 机器人设计的，而不是供人类使用的，” Fox 推测。“也许是我们都无法阅读的东西，因为它是由 AI 生成的胡言乱语。”

## 现代语言的祖父

回顾 Java 的三十年，Fox 认为这是编程历史上的一个分水岭。Java 之前的语言——C、C++、Fortran、Ada——在可重用性和依赖管理方面的方法从根本上是不同的。Java 建立了几乎所有后续语言都采用的标准模式。

“我觉得 Java 就像所有现代语言的祖父，”他反思道。

随着 Java 进入第四个十年，它面临着多年来一直困扰它的问题：它是否太老了？是否会有更新、更闪亮的东西取代它？但如果过去 30 年教会了我们什么，那就是押注 Java 的持久力是一种冒险的行为。