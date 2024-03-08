# KubeCon 24：GUAC 揭示漏洞隐藏之处

![KubeCon 24 特色图片：GUAC 揭示漏洞隐藏之处](https://cdn.thenewstack.io/media/2024/03/df7a3bf0-guac-1024x696.png)
![](https://cdn.thenewstack.io/media/2024/03/8cbb2856-kubecon24-eu-300x206.jpg)

KubeCon

现在，您的安全团队已为其开源应用程序准备了 [软件物料清单](https://thenewstack.io/sboms-sboms-everywhere/)（[SBOM](https://thenewstack.io/a-good-sbom-is-hard-to-find/)）。接下来是什么？如果您参加 3 月 19 日至 22 日在巴黎举行的 [KubeCon + CloudNativeCon EU](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)，请在 [Kusari 展位](https://www.kusari.dev/about)（#M30）了解有关 [理解工件组成图 (GUAC)](https://guac.sh/) 的更多信息，该图将所有 SBOM 数据放入更易于理解的图形数据格式中，并用漏洞数据对其进行扩充。

周四，[开源安全基金会](https://openssf.org/)（OpenSSF）[采用 GUAC](https://openssf.org/projects/guac/) 作为 [孵化项目](https://openssf.org/blog/2024/03/07/guac-joins-openssf-as-incubating-project/)。Open SSF 将为 GUAC 带来越多内容，包括 SBOM 和 [CycloneDX](https://cyclonedx.org/capabilities/vex/) 领域专家的访问权限和反馈。

“有很多工具生成 [安全] 数据，但没有很多工具将所有这些信息汇总在一起并真正利用它们，”Kusari 联合创始人兼首席技术官 [Michael Lieberman](https://www.linkedin.com/in/michael-lieberman-65786ba/) 在接受 The New Stack 采访时说。“GUAC 将所有这些信息汇总到一个图形数据库中，您可以实际使用它来获取可操作的见解。”

Kusari、Google 以及普渡大学和花旗的研究人员开发了 GUAC，并吸引了雅虎、 [Microsoft](https://news.microsoft.com/?utm_content=inline-mention)、 [Red Hat](https://www.openshift.com/try?utm_content=inline-mention)、Guidewire 和 ClearAlpha Technologies 等公司的支持。

到目前为止，该项目已吸引了 50 位贡献者、300 位社区成员，并在 GitHub 上获得了 1,100 多颗星。

Lieberman 说，GUAC 确实是一项社区努力。

安全学者长期以来一直认为依赖关系图可能很有用。Lieberman 是 OpenSSF 管理委员会和 TAC 成员；也是 CNCF 安全 TAG 负责人——他看到商业部门对这种性质的工具非常感兴趣。

“我们没有各自开发不同的东西，而是走到一起开始构建一些东西，”Lieberman 说。

## GUAC 如何工作？

当前版本可用 [作为测试版](https://docs.guac.sh/guac-use-cases/)，通过标准 Rest API、[GraphAPI](https://thenewstack.io/why-graphql-needs-an-open-federation-approach/) 和命令行提供结果。

GAUC 提供数据以显示 [详细图表](https://thenewstack.io/linkedins-real-time-graph-database-is-liquid/)，可视化 SBOM 中的所有软件，包括第一方、第三方或开源软件。该软件以 [SPDX](https://thenewstack.io/improving-open-source-supply-chain-transparency-with-spdx/) 和 [CycloneDX](https://thenewstack.io/2023-the-year-open-source-security-supply-chain-grew-up/) 格式摄取 SBOM。

它有一组收集器，可从诸如 [Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) 等存储库中提取数据。它还可以从本地文件系统、[Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention) 的 S3、[Google Cloud](https://cloud.withgoogle.com?utm_content=inline-mention) 和 GitHub Releases 等外部包存储库中获取数据。

为了扩充这些数据，GUAC 通过 API 从开源见解的 [deps.dev](https://deps.dev/) 和 [开源漏洞](https://osv.dev/) 等来源获取并整合漏洞数据。

“我们正在使用这些其他开源工具丰富 SBOM，”Lieberman 说。

GUAC 整理这些数据并将信息作为一组数据节点和关系返回。这些工件可用于了解软件供应链数据中的差距，并找出软件堆栈中的薄弱环节。

您可以查询图表以找出 SBOM 中的漏洞，包括传递依赖关系，其中一个应用程序依赖于一个库，而该库又依赖于一个易受攻击的元素。

除了安全性之外，它还可以突出显示具有限制性许可证的包（这可能会导致诉讼）。

![](https://cdn.thenewstack.io/media/2024/03/5a1d2c94-expandviewvisualization.png)

您的命令行界面中是否存在漏洞？GUAC [可以显示](https://docs.guac.sh/querying-via-cli/) 给您。

## KubeCon 的意见

在 KubeCon，GUAC 团队正在寻找更多来自那些觉得自己对供应链问题了解不够的人的意见。他们正在寻找尚未发现的用例。
他们正在寻找新的数据源和对新功能或应该添加的功能的反馈。

上个月，OpenSSF [发布了一套原则](https://repos.openssf.org/principles-for-package-repository-security)用于保护软件包存储库，建立分类法和分层安全成熟度，从一到四。

至于 Kusari 本身，它正在基于 GUAC 和其他工具构建一个安全平台。该公司正在考虑将其作为一项服务提供，或者可能销售带有附加分析功能的版本。

“你们的软件环境每年都变得越来越复杂。为了理解这些复杂的环境，你们需要有工具来提供帮助。而这就是 Kusari 的用武之地。”利伯曼说。

![](https://cdn.thenewstack.io/media/2024/03/588996aa-cliimage.png)

GAUC [公开了一张图像](https://docs.guac.sh/querying-via-cli/)，其中包含 log4j 和 text4shell 漏洞。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。