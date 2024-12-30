# 2024编程语言大战：Python领跑，Java保持稳定，Rust崛起

![2024编程语言大战：Python领跑，Java保持稳定，Rust崛起](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)

2024年对于编程语言来说是极好的一年。Python在AI/机器学习应用中的使用率上升，Java继续在企业应用开发中占据主导地位，Rust成为内存安全开发的首选语言。

以下是2024年的一些亮点。

## Python 高歌猛进

在编程语言中，[Python](https://thenewstack.io/python/)目前正处于高歌猛进的状态。它很可能成为2024年[TIOBE编程语言指数](https://www.tiobe.com/tiobe-index/)的年度语言。这一成就由当年评级增长最高的语言获得。Python一年的评级增长率为10%。紧随其后的是Java和JavaScript，分别增长了1.73%和1.72%。

TIOBE软件的创始人兼首席执行官[Paul Jansen](https://www.linkedin.com/in/paul-jansen-299429/)指出，这些语言都有“积极”的增长。“但与2024年Python的巨大飞跃相比，这似乎微不足道，”他说。“由于Python支持AI和数据挖掘、拥有大量的库以及易于学习，因此势不可挡。”

### 在AI和生成式技术中的主导地位

IDC分析师[Arnal Dayaratna](https://x.com/cloud4computing)告诉The New Stack，Python仍然是AI和机器学习开发的主要语言，尤其是在生成式AI技术的快速发展中。

“诸如[TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/)和[PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/)之类的框架，以及[Hugging Face](https://huggingface.co/)的Transformers之类的库，继续主导着生成式AI开发者生态系统，使开发者能够快速构建和部署自然语言处理、计算机视觉和生成模型训练等领域的先进解决方案，”Dayaratna说。“Python的简洁性和与各种数据科学工具的集成，使得快速原型设计和部署成为可能，确保了其作为构建下一代AI应用程序的首选语言的地位。”

### 稳定的生态系统

与此同时，提供企业级包管理（作为[PyPI](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/)的替代方案）的[Anaconda](https://thenewstack.io/faster-python-easier-access-to-llms-anacondas-ai-roadmap/)的联合创始人兼首席AI和创新官[Peter Wang](https://www.linkedin.com/in/pzwang/)表示，他见证了2024年Python生态系统的稳定。

“Python仍然是一种非常强大且优秀的用于进行数据分析的语言……它显然是AI的语言，我们非常期待看到明年会为我们带来什么，”Wang说。

Talk Python的创始人兼[Python软件基金会(PSF)](https://www.python.org/)成员[Michael Kennedy](https://www.linkedin.com/in/mkennedy/)在12月10日于[JetBrains](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)的PyCharm博客上发表了一篇广泛的介绍性文章，讲述了[2024年Python的现状](https://blog.jetbrains.com/pycharm/2024/12/the-state-of-python/)。

“几年前，Python成为Stack Overflow上最流行的语言，”Kennedy写道。“然后，Python跃升为[TIOBE指数](https://www.tiobe.com/tiobe-index/)上的第一名语言。目前，Python的流行程度是该指数上第二流行语言(C++)的两倍！最重要的是，在2024年11月，[Github宣布](https://github.blog/news-insights/octoverse/octoverse-2024/?featured_on=pythonbytes)Python现在是GitHub上使用最多的语言。”

### 近期动态

在最近的Python社区动态中，Wang表示他认为合并的多线程Python支持——移除[全局解释器锁(GIL)](https://thenewstack.io/pythons-gil-multithreading-and-multiprocessing/)——是关键。尽管该移除并非默认启用。他还表示，为核心Python解释器添加[WebAssembly后端支持](https://thenewstack.io/reversing-web-assembly-project-extends-web-components/)也很重要。

此外，“Python包生态系统仍然很有趣，”Wang告诉The New Stack。“它可能是一篮子愤怒的猫，或者任何你想称呼它的东西。”

然而，他指出，在Python包领域，[uv](https://github.com/astral-sh/uv)——一个用Rust编写的快速Python包和项目管理器——“确实获得了大量的关注和关注。”
但是，还有其他项目，例如[PDM](https://github.com/pdm-project/pdm)、[Hatch](https://github.com/pypa/hatch)和[Poetry](https://python-poetry.org/)，也在不断发展，并拥有各自的支持者。

此外，尤其是在今年，像[Nvidia](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)这样的大型公司也倾力尝试改进Python的打包方案——部分原因是他们需要支持AI和ML用例的庞大包。“当你把GPU支持代码放入这些包中时，它们会变得非常非常大，”王说。

### 流行带来的代价
Python开始看到更多恶意行为者试图攻击用该语言构建的应用程序。

“我们看到供应链攻击的持续增长，”王说。“现在Python是排名第一的语言……流行有其缺点，越来越多的人开始发动攻击。”

王说，Python的志愿者运营的基础设施与其日益增长的关键全球基础设施作用之间正在出现紧张关系，尤其是在安全和包管理方面。然而，他补充说，双因素身份验证是确保控制你的包的一个选项。

### 快速采用
“多达41%的Python开发者使用Python的时间不到两年，”肯尼迪在他的博客文章中写道。

GitHub对Python增长的洞察表明，“[Python]在过去几年的持续增长——以及Jupyter Notebooks的增长——可能表明[Python开发者]在GitHub上的活动已经超越了传统的软件开发，”他写道。

关于Python框架，他写道：“63%的Web开发者使用[Django](https://thenewstack.io/what-is-pythons-django/)，而使用[Flask](https://thenewstack.io/how-to-use-flask-a-lightweight-python-framework/)的比例为42%。另一方面，数据科学家更喜欢Flask和FastAPI，而不是Django。”

## Java：王者依旧
近30年来，[Java](https://thenewstack.io/java/)仍然是许多企业系统的命脉，这种主力编程语言没有显示出放缓的迹象。

Java将于2025年5月迎来30岁生日，并且在许多报告（包括[TIOBE指数](https://www.tiobe.com/tiobe-index/)）中仍然位列前三名最流行的语言之列。

### Java如何保持其相关性
“[强类型、良好的抽象、核心库、内存安全性能、可观察性和安全性，以及广泛的第三方库、工具和SDK支持，继续使Java成为企业用户的强大选择，而2024年这些原因并没有终结Java的增长，”[Oracle](https://developer.oracle.com/?utm_content=inline+mention) Java平台高级副总裁兼[OpenJDK](https://thenewstack.io/the-hidden-risks-of-unsupported-openjdk-in-financial-systems/)管理委员会主席[Georges Saab](https://www.linkedin.com/in/georgessaab/)告诉The New Stack。

此外，Java平台在2024年交付了两个按时可预测的版本，分别是[JDK 22](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/)和[JDK 23](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/)。这些版本继续提高企业开发人员的性能和生产力，并提供对使用Java进行AI集成的用户有益的功能。

“[一个很好的例子是[JDK 22中对外函数内存API的发布](https://docs.oracle.com/en/java/javase/22/core/foreign-function-and-memory-api.html)，它使与外部函数的交互更容易、更快和更安全，以及随后启动的[Babylon项目](https://openjdk.org/projects/babylon/)，该项目旨在将Java的应用范围扩展到外部编程模型，例如在GPU上运行的那些模型，”Saab说。

### Java用于AI和机器学习
Java平台提供商[Azul](https://www.azul.com/?utm_content=inline+mention)的首席技术官副总裁[Simon Ritter](https://www.linkedin.com/in/siritter/)告诉The New Stack，Java通过不断发展以满足现代软件开发的需求，继续证明其作为领先编程语言的弹性和相关性。

“在2024年，Java引入了重大改进，进一步巩固了其在AI、机器学习和云计算等关键领域的领先地位，”Ritter说。“[Java 21](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/)中的虚拟线程和结构化并发等功能彻底改变了性能和可扩展性，使开发人员能够更高效地构建高性能并发应用程序。改进的工具，例如改进的[Visual Studio Code](https://thenewstack.io/building-with-flutter-using-visual-studio-code-a-dev-guide/)集成，简化了工作流程，提高了开发人员的生产力，并为更复杂的AI实现铺平了道路。”
与此同时，Java强大的生态系统也取得了关键进展，使其成为AI和机器学习的突出平台。

“诸如[Deep Java Library (DJL)](https://djl.ai/)和[langchain4J](https://docs.langchain4j.dev/)之类的库提供了构建AI解决方案的强大工具，而与[AWS](https://aws.amazon.com/?utm_content=inline+mention)和[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud等云原生平台的无缝集成支持大规模分布式AI应用，”Ritter说。

此外，量子安全加密等进步解决了未来的安全挑战，并确保Java仍然是保护敏感AI数据的可靠选择。

“凭借这些创新，”Ritter说，“Java继续在企业应用、数字化转型和尖端的[AI/ML](https://thenewstack.io/kubernetes-1-31-arrives-with-new-support-for-ai-ml-networking/)解决方案中处于领先地位，证明了其作为下一代技术平台的适应性和实力。”


### Java用于企业和关键任务系统
在谈到Java持续的现代化和企业重点时，IDC的Dayaratna表示，Java在9月份发布JDK 23后，巩固了其作为企业和关键任务应用程序基石的地位。

“这个最新的功能版本引入了一些增强功能，包括对虚拟线程的改进，[垃圾收集](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/)的改进以及扩展的模式匹配功能，”Dayaratna告诉The New Stack。“虚拟线程最初是通过[Project Loom](https://openjdk.org/projects/loom/)在早期版本中引入的，它在简化高并发应用程序开发方面发挥了重要作用，显著提高了开发人员的生产力。

“这些进步使Java更适用于现代云原生架构，同时保持了对遗留系统至关重要的向后兼容性和可靠性。通过JDK 23等创新，Java持续发展，突显了其在为企业提供可扩展和安全解决方案方面的持久重要性。”

[Eclipse基金会](https://www.eclipse.org/)通过[Jakarta EE](https://projects.eclipse.org/projects/ee4j.jakartaee-platform)等项目支持企业Java开发人员，并领导Temurin和Adoptium项目，今年取得了显著进展，基金会执行董事[Mike Milinkovich](https://www.linkedin.com/in/mikemilinkovich/)表示。“在Eclipse基金会，我们在2024年庆祝了一个重要的里程碑，我们实现了[Eclipse Temurin](https://adoptium.net/temurin/) OpenJDK发行版的5亿次总下载量。自三年前成立以来，[Adoptium](https://adoptium.net/)通过提供免费、完全兼容、社区支持的企业级Java运行时，对Java生态系统产生了重大影响。”

Eclipse Temurin是基于OpenJDK的开源Java SE构建。Jakarta EE是一套规范，它使用分布式计算和Web服务等企业功能的规范扩展了[Java SE](https://en.wikipedia.org/wiki/Java_SE)。Jakarta EE应用程序运行在参考运行时上，这些运行时可以是微服务或应用程序服务器，它们处理事务、安全、可扩展性、并发性和它们部署的组件的管理。


### Java社区和生态系统演变
与此同时，关于Java社区和行业的进展，在整个2024年，我们看到许多不同的组织与Java的管理者Oracle在OpenJDK社区一起合作，继续在全球范围内推动Java的发展。

“例如，今年新增了25个[Java用户组(JUGs)](https://dev.java/community/jugs/)，全球共有347个认可的JUG，”Saab说。“这种广泛的行业支持有助于提高Java的开发速度，扩大开发者基础，并在Java即将于2025年5月迎来30周年之际，提高版本的可预测性。”


## 需要内存安全？依靠Rust
与此同时，[Rust](https://thenewstack.io/rust-programming-language/)已成为系统编程的领导者。Rust在TIOBE指数中排名第14位。

IDC的Dayaratna告诉The New Stack，Rust在2024年继续获得关注，成为性能关键型和安全型应用程序的首选语言。

“它的所有权模型和借用检查器保证了内存安全，而无需垃圾收集，这使其成为构建嵌入式系统、云原生基础设施和汽车应用等领域可靠软件的理想选择，”他说。
此外，Dayaratna 指出：“Rust 能够防止数据竞争和内存泄漏等常见的编程错误，使其成为需要高可靠性的行业的热门选择。”“此外，其现代化的工具生态系统，包括 [Cargo 包管理器](https://doc.rust-lang.org/cargo/)，简化了开发工作流程，进一步提高了其在各种用例中的采用率。”

根据最近的 [JetBrains 开发者调查](https://thenewstack.io/developers-testing-more-jetbrains-study-finds/)，Rust 继续逐步获得用户。2024 年，11% 的受访者报告在过去 12 个月内使用过 Rust，高于 2023 年的 10% 和 2022 年的 9%。然而，C++ 的采用率并没有下降。The New Stack 的研究总监指出，这可能是因为从 C++ 迁移到 Rust 并非一次性完成的。

此外，在 C++ 用户中，21% 已经在某种程度上使用 Rust，另有 14% 计划采用它。而 11% 的 Rust 开发人员在同一个项目中同时使用 C++ 和 Rust，但只有 5% 主要使用 C++ 的开发人员在同一个项目中同时使用 Rust 和 C++。

在主要使用 C++ 的开发人员中，那些在同一项目中使用 Rust 的开发人员中，有 58% 计划在未来 12 个月内将更多代码迁移到 Rust。然而，在使用 Rust 的项目中，使用其他语言的开发人员更少了。2024 年，41% 的 Rust 开发人员在其 Rust 项目中不使用其他语言，低于 2023 年的 49%。

### Rust 会取代 C++ 吗？
[JetBrains 的研究](https://www.jetbrains.com/lp/devecosystem-2024/) 表示：“今年最流行的语言中，唯一创下新使用记录的语言是 Rust。”“Rust 凭借其严格的安全性和内存所有权机制，力求取代 C++，其用户基础在过去五年中稳步增长。根据我们的数据，每六个 [Go](https://thenewstack.io/go/) 用户中就有一个正在考虑采用 Rust。”

研究发现，Rust 和 Go 是采用率最高的语言。“受访者最计划采用的语言显然是 Go 和 Rust，”研究报告说。“这两种语言都是着眼于性能和并发性而构建的，并具有编译器安全保证，有助于减少错误。然而，虽然我们看到 Rust 的普及率正在增长，但 Go 开发人员的比例保持稳定。”

### 态度转变
来自新西兰惠灵顿的科技咨询公司 [Accelerant.dev](https://accelerant.dev/) 的创始人兼“[Rust in Action](https://www.amazon.com/Rust-Action-TS-McNamara/dp/1617294551)”一书的作者告诉 The New Stack：“对我来说，最大的变化是态度的转变。”

“看到 Rust 社区的许多成员都拥有成就感和成功感，这很好。Rust 经历了几年的阵痛。由于许多人的默默努力和小的互动逐渐创造了一个更健康的生态系统，社区似乎正处于一个非常健康的状态。”（更多关于 McNamara 对该语言现状的看法，请查看“[Rust 2024 的重要时刻](https://thenewstack.io/big-moments-in-rust-2024/)”。）

### Rust 基金会的管理
Rust 基金会的执行董事兼首席执行官告诉 The New Stack：“2024 年是 Rust 的里程碑式的一年，它再次确立了其作为 [顶级编程语言](https://www.tiobe.com/tiobe-index/)在安全性和性能方面的领先地位，同时保持其作为 [最受赞赏的语言](https://survey.stackoverflow.co/2024/technology/#admired-and-desired) 的地位。”“在过去的一年中，我们见证了 Rust 在扩展规模方面取得了显著进展，为更多开发人员和组织带来了好处。”

与此同时，2024 年全球对 Rust 的热情高涨，新的聚会小组和会议在世界各地涌现——从 [肯尼亚](https://github.com/RustaceansKenya) 到 [土耳其](https://github.com/rustturkey)，遍及欧洲其他地区和英国——这反映了开源社区渴望学习和交流 Rust 的热情，Rumbul 指出。Rust 基金会还通过其社区资助计划支持其中一些组织者以及项目维护者。
今年，对Rust的机构投资也达到了新的高度，Rumbul说道。“[白宫国家网络总监办公室](https://thenewstack.io/rust-on-the-rise-new-advocacy-expected-to-advance-adoption/) 二月份倡导使用Rust等内存安全的语言来增强安全性。行业领导者做出了大胆的承诺：AWS通过向我们的安全倡议捐款投资于Rust生态系统的安全；谷歌对我们互操作性倡议的支持将有助于推进[Rust-C++互操作性](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/)；而[微软通过一笔慷慨的无限制捐款](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/) 倡导了Rust项目的一些关键优先事项。这些只是2024年企业投资Rust的几个例子。”

Rumbul补充说，Rust维护者贡献和工作包太多，无法一一列举，但对[即将发布的Rust版本之前的Rust项目目标](https://rust-lang.github.io/rust-project-goals/2024h2/Rust-2024-Edition.html) 的深入反思，就是一个清晰的成熟、增长和远见的标志。

“从Rust项目贡献者到Rust社区组织者，再到Rust基金会，整个Rust生态系统在2024年都取得了进步，这将帮助Rust满足2025年日益增长的需求。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。