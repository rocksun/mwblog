# Java：安全无虞之地

![Featured image for: Java：安全无虞之地](https://cdn.thenewstack.io/media/2024/10/210626fb-monster-1024x576.jpg)

过去十年，OpenJDK 社区显著提升了 Java 的用户安全性，同时简化了软件工程师的开发流程。这种结合减少了安全问题，并为处理所有软件中不可避免的安全问题提供了更清晰的流程。

具体来说，以下三点促成了这一改进：

- 一个安全的 Java 开发工具包 (JDK)，能够及时修补漏洞并按计划发布。
- 一个模块化的 JDK，通过创建信任边界并帮助移除不必要的模块来减小攻击面。
- 一个管理良好的社区，对软件库拥有明确的所有权。

## 及时更新的安全的 JDK

Java 开发工具包每年发布四次，遵循预先发布的计划。每次发布都会进行标准改进，并修补任何新的安全风险。专门的 OpenJDK 漏洞小组帮助分类和优先处理漏洞，以便能够迅速修复它们。与报告漏洞的研究人员的协调确保了及时修补。

安全的 JDK 并不意味着不会出现任何漏洞；这意味着当漏洞出现时，它们会得到及时和正确的处理。

### 定期修补

安全性和改进每年发布四次，所有日期都预先公布。这些日期允许项目经理和其他人员将 Java 修补计划安排为已知的季度活动。用户无需订阅电子邮件列表并对警报做出反应，而可以在每三个月（一月、四月、七月和十月）的第三个星期二或之后安排时间。

处理和修补漏洞的关键部分是跟踪它们是什么以及告诉人们它们是什么。社区工作的一个关键部分是将功劳归于发现安全问题并妥善披露它们以帮助开源项目的研究人员。

### 常见漏洞和披露 (CVE) 通告

OpenJDK 漏洞小组维护着 [每个 Java 版本中已修补的 CVE 列表](https://openjdk.java.net/groups/vulnerability/advisories/)，并向参与负责任披露的不同研究人员表示感谢。这使下游 Java 用户能够回答一个简单的问题：如果我使用旧版本的 Java，我会承担什么风险？

OpenJDK 漏洞小组在这些通告中做的另一个出色方面是按组件跟踪 CVE，因为并非所有 Java 用户都利用每个组件。

简而言之，仅仅说旧的 Java 安装包含 CVE 并不能充分说明该漏洞存在于该系统上。

### 一致的命名

在 2019 年初，Docker 上的主要 OpenJDK 分发版提供的是“[神秘肉 Java](https://www.infoq.com/news/2019/06/docker-vulnerable-java/)”，这是一个与修补程序计划不同步的源代码版本，错过了各种安全修补程序，但仍然使用了包含安全漏洞的 JDK 版本号。结果，Docker 镜像的用户是不安全的，而已知下游 Java 分发的用户是安全的。

通过认识到漏洞披露的必要性并使用预先发布的季度修补程序节奏，在 OpenJDK 上工作的 Java 供应商通过 [JEP 322](http://openjdk.java.net/jeps/322)（基于时间的版本）围绕相同的编号方案进行工作。通过协调围绕季度修补程序计划的版本号，大多数 Java 供应商使用相同的数字，这些数字可以相互理解和比较，以了解哪个版本发布较晚以及该版本中存在哪些安全修补程序。

这种协调的替代方案将是半可预测但毫无意义的数字，这需要特殊的查找表来了解哪些安全修补程序存在于哪里。

## 基于模块的 JDK 减少了攻击面

Java 8 及以下版本的原始文档提供了一个 [概念图](https://docs.oracle.com/javase/8/docs/)，说明某些功能位于何处。从威胁建模的角度来看，这也是漏洞存在的位置。

一些片段很容易识别：

- 驱动下载或执行的风险完全集中在部署插件中，该插件在现代 Java 运行时环境 (JRE) 中不再可用。
- 只有当应用程序使用 Java 数据库连接 (JDBC) 时，才会发生 SQL 注入。不使用 SQL 的应用程序不会受到 SQL 注入的攻击。
- 针对 XML 的攻击，例如 [XXE](https://www.youtube.com/watch?v=x6QQzgf0j7o&feature=emb_logo)，发生在 XML JAXP 区域内。[反序列化攻击](https://github.com/frohoff/ysoserial) 源于反序列化组件和 IO 结构。
开发人员和运行应用程序的人员从中受益，因为他们可以查看应用程序并缩减需要担心的内容，只关注正在使用的部分。这突显了 OpenJDK 漏洞小组季度安全公告中模块信息的重要性。

开发人员可以查看这些模块并检查每个模块中与其应用程序相关的风险。例如，敏感数据和暴露风险；这在日志记录模块中很常见，但在像 Image/IO 这样的模块中则少得多。核心好处是简单地了解存在的风险以及风险所在的位置，而不是担心模糊且无法识别的威胁，以及防御措施部署在错误的位置。

另一点是要认识到概念图中没有出现什么，并关注其出现的地方。例如，在核心 Java 图表和模块中，没有“web”或 HTML 的概念。这意味着针对 web 威胁（例如跨站点脚本 (XSS)）的工作属于提供该功能的框架或工具。

### 通过移除模块来降低风险
黑客无法攻击不存在的东西。与其防御应用程序免受无数威胁的攻击，不如简单地移除不需要的模块，这可以 100% 缓解任何需要该模块的威胁。

一个 [概念图](https://docs.oracle.com/javase/8/docs/) 展示了这些模块的外观以及它们之间的关系。创建应用程序或服务的开发人员可以使用 jlink 等工具 [创建自定义 JRE](https://www.baeldung.com/jlink)，从而移除某些模块。

- 移除 JDBC（数据库连接）将阻止 SQL 注入攻击，因为数据库查询将不再存在。
- 移除 ImageIO 将阻止任何与图像相关的漏洞，例如 [CVE-2020-14562](https://nvd.nist.gov/vuln/detail/CVE-2020-14562)。该 CVE 存在于 ImageIO 中，因此当移除 ImageIO 时，攻击面就不复存在了。
- 移除 XML JAXP 区域可以减轻 [XXE](https://www.youtube.com/watch?v=x6QQzgf0j7o&feature=emb_logo) 漏洞，因为 XML 不再存在。（XML 在 Java 9 中已弃用，在 11 中已移除，因此现在这是默认设置。）
使用模块化时，JDK 的默认安全性要高得多。标记为“易受攻击”的 JDK 版本实际上可能并不易受攻击。

这种区别至关重要，因为许多软件团队都需要以开源依赖项的形式进行漏洞扫描。扫描程序通常只查看库名称，然后假设所有使用的库都包含所有 CVE。对于自定义 jlink-ed JRE，任何报告 JRE 易受此缺陷攻击的扫描程序都是不正确的。移除组件会移除该组件中的漏洞和风险。黑客无法攻击不存在的东西。

## 受管理的社区明确拥有软件库
大多数 Java 依赖项来自 Maven Central，其中的库由三部分组成：组、构件和版本。通过提供明确的拥有级别，[Sonatype](https://www.sonatype.com/?utm_content=inline+mention)（运行 Maven Central）创建了一个环境，使 Java 开发人员无需担心其他社区中发生的 [依赖关系混淆](https://fossa.com/blog/dependency-confusion-understanding-preventing-attacks/) 之类的攻击。

所有 Maven 依赖项都由三部分组合标识：组、构件和版本。组表示命名空间，通常使用 Java 的反向 DNS 样式。要发布构件，开发人员需要与命名空间有一定的连接。例如，为 example.com 工作的开发人员无法在他们没有关联的已建立组（不是 com.example）下发布构件。

此外，拥有一个主要的库来源可以阻止另一个系列从互联网上的随机位置获取组件，这些位置的域名会过期并被出售。这种情况发生在 JavaScript 社区中，[一家公司收购了 Polyfill](https://arstechnica.com/security/2024/07/384000-sites-link-to-code-library-caught-performing-supply-chain-attack/)，并将原始库替换为立即提供给数十万个网站的新代码。当代码被交换或组不完全匹配时，Java 使检测变得非常容易。

## 战术要点
最终，团队可以采取三个行动来确保其应用程序和系统保持安全。
- 每季度根据发布的计划修补 Java，理想情况下为一次。
- 使用模块化来减小其应用程序的攻击面。
- 定期从可信来源修补依赖项。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
Tech moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.