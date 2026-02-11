就在 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) [宣布推出 Chainguard Factory 2.0](https://thenewstack.io/chainguard-admitted-factory-1-0-was-brittle-heres-how-2-0-fixes-it/) 一周后，该公司达到了一个重要的里程碑，展示了目前在生产环境中运行的系统规模。

上周，Chainguard 表示，其围绕 [DriftlessAF](https://c67dcd9a.streak-link.com/Cwrwy4caWmL0IF9LOQzCv3K1/https%3A%2F%2Fgithub.com%2Fdriftlessaf) 开源代理协调重建的软件工厂，迄今已生成超过 5 亿个独特的容器构建清单。DriftlessAF 是一个代理框架，使机器人能够使用传统和代理人工智能评估方法，大规模自动化协调。

Chainguard 在一篇[博客文章](https://www.chainguard.dev/unchained/driftlessaf-introducing-chainguard-factory-2-0)中指出：“Chainguard 内部尖端人工智能生产力工具的出现和采用，在我们的工程团队中积累了代理专业知识。”

Chainguard 不扫描或修补上游二进制文件，而是在检测到更改时直接从源代码重新生成容器和库。Factory 2.0 推动了所有这一切。

该公司表示，它作为一个大规模的自校正系统运行：每个容器构建清单都代表了系统的可重现输出，涵盖了初始构建、依赖项和漏洞驱动的重建、工具更改以及生成的 [SBOMs](https://thenewstack.io/sboms-sboms-everywhere/) 和签名，所有这些都旨在实现默认安全的狀態。

## 超越清单

除了每月生成数百万个更多容器构建清单，并已超过 5 亿个，Factory 2.0 还持续维护着：

*   **2,000+**（本次采访时为 2,069 个）开源项目，为包括 go、nginx 和 [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) 在内的项目提供最小化、低 CVE 或零 CVE 的 Chainguard 镜像
*   **340,000+** 容器镜像版本，随着上游项目和架构的发展，提供新版本的快速可用性和对历史版本的访问
*   **27,000+** 基础操作系统包，随着时间的推移进行组装和维护

Chainguard 高级副总裁 [Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland/) 告诉 *The New Stack*，这一里程碑是稳定性的标志。

Kirkland 说：“目前，我们在向目录中添加镜像方面走上了一条相当可预测的道路。”“我们已经突破了 2,000 个独特镜像的数量，这些镜像在版本、风格和架构之间完全去重。”

这是一个原始数字，显示了 Chainguard 已经强化并维护的独特镜像包项目的范围，为其客户提供了零 CVE。

Kirkland 说：“但最大的新闻，也是里程碑时刻，是我们突破了 2000 个镜像的关口。我们不会止步于此。”“目前，我们每月向目录中添加近 100 个镜像。

## 五亿

Kirkland 表示，除了 5 亿个容器构建清单，Chainguard 每天还增加近百万个排列组合，昨天增加了 130 万个。这还包括修改了其镜像或正在使用 Chainguard 自定义组装功能的客户所使用的镜像。

这是 Chainguard 去年宣布的一项功能：它允许客户从其镜像中添加，或在某些情况下删除镜像或配置，同时仍通过 Chainguard 的构建系统运行它们，并继续享受 Chainguard 的服务水平协议覆盖。

Chainguard 首席执行官兼联合创始人 [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) 表示：“保护整个软件供应链需要深厚的技术实力和自动化。”“我们的软件工厂持续地直接从源代码重建工程团队所依赖的每一个开源组件，并随着时间的推移持续维护这些组件。”

## 400 家组织

近 400 家组织，从财富 500 强企业到初创公司，都使用 Chainguard Containers。在过去的一个季度中，像 Black Duck、Nelnet、Rocket Lab 和 SolarWinds 这样的公司开始使用 Chainguard 进行构建。

[Second Front](https://www.secondfront.com/) 的高级平台工程师 [Jeff Davis](https://www.linkedin.com/in/jefedavis/) 在一份声明中表示：“在 Second Front，我们让向安全不容置疑的政府团队和任务交付安全、合规的软件变得更快更容易。”“访问 Chainguard 的完整目录使我们能够访问一个庞大的安全、可信的开源镜像库。没有意外，无需繁琐的步骤，只需在内置安全性和信任的情况下自由快速行动。”

Chainguard 还增加了新功能以简化客户体验，包括改进 Helm Chart 用户体验，并通过 Chainguard 新的生命周期结束更新实现可预测的生命周期管理。