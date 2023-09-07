# 无处不在的 SBOM

OWASP 和 OpenSSF 等安全组织正在努力使工具更易于访问和对开发者更友好，以推动采用和更广泛的使用。

![](https://cdn.thenewstack.io/media/2023/09/f0ac224f-inventory-1024x683.jpg)
*图片来自 Shutterstock 的 Danita Delimont*

随着近几年发生的许多供应链攻击，对软件清单或 SBOM 的讨论变得更加普遍。软件供应链攻击可以针对你的软件的上游元素，如开源库和包，SBOM 是了解你的应用程序或容器镜像中的内容的一种方式。

但是，虽然 SBOM 是一项有用的信息，但团队对它仍有很多疑问: 我们需要 [SBOM](https://thenewstack.io/sbom-everywhere-the-openssf-plan-for-sboms/) 吗？我们在生成它们后对它们做什么？我如何在安全事件期间使用它们？

为了回答这些和其他问题，让我们从SBOM实际上是什么开始。

## 什么是 SBOM ？

软件清单是软件应用程序或系统中使用的所有软件组件和依赖项的全面库存。这使安全团队以及开发人员能够更好地了解他们正在使用的第三方资源和导入，特别是当不断发现开源包中的新漏洞时。要从这些威胁中保护你的组织，你首先要知道你的技术栈中有什么。

容器已经成为开发人员在当今云原生环境中打包和交付软件的默认方式。在容器和 SBOM 的上下文中，容器中的软件清单等价物是一个 JSON 文件，其中列出了应用程序和周围容器中使用的所有包、库和组件。这个 `package.json` 文件包括这些组件的所有版本信息，其中包是机器可读的，这一点同样重要。

如果我们把这跟我们都熟悉的东西进行比较，这个 JSON 文件几乎就像包装食品上的营养标签，只不过是针对你的容器化应用程序。这个 JSON 文件也是一个时间点工件，这意味着它与容器的特定 SHA256 摘要绑定。这与诸如 `latest` 之类的可变标签不同，因为可变标签的 SBOM 会随时间变化，但对于特定的 SHA256 摘要则不会。

您的 `package.json` 提供的另一个重要方面是最终由 git 管理的所有历史信息，这为您提供了容器在任何给定版本中运行的内容的关键回溯知识。这将使您能够在发现漏洞时采取行动，了解当前在生产中运行的容器中都有什么。这也使数据更易于搜索，以便快速清查 0-day 攻击。

2021 年 12 月发生的 [Log4j 0-day 攻击](https://thenewstack.io/one-year-of-log4j/)被认为已经影响了超过 1 亿个软件环境和应用程序。[CISA](https://www.cisa.gov/) 认定这次攻击对全世界的政府和组织构成威胁。OpenSSF 和 Linux 基金会支持的 [Log4j 事后报告](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf)鼓励该行业使用诸如 SBOM 之类的软件组件工具来减少漏洞识别和缓解之间的时间。

SBOM 将使公司更容易理解他们在生产中运行的是哪个版本的容器，以及当发生 Log4j 类型的事件时，他们的生产系统会面临多大的风险。与软件供应链的许多其他领域一样，有大量出色的开源工具可以为您生成 SBOM，例如 Syft、Trivy、BOM 和 CycloneDX，以及提供商业服务的其他工具。

## 展示代码

在下面你会看到一个来自 Docker Hub 的 Node 容器镜像的 SBOM 片段，该镜像的拉取量超过 14 亿次。我们跳入 Slim 平台(portal.slim.dev/login)来搜索公共 Node 镜像，分析镜像中的漏洞，然后直接从平台上以 CycloneDX JSON 格式下载 SBOM。

```yaml
 "$schema": "http://cyclonedx.org/schema/bom-1.4.schema.json",
 "bomFormat": "CycloneDX",
 "specVersion": "1.4",
 "serialNumber": "urn:uuid:aaf2dfd5-5294-4277-8cc1-f7fe6f6d514b",
 "version": 1,
 "metadata": {
   "timestamp": "2023-06-21T13:26:31Z",
   "tools": [
     {
       "vendor": "slim.ai",
       "name": "slim",
       "version": "0.0.1"
     }
   ],
   "component": {
     "bom-ref": "b1ef6d159e61300a",
     "type": "container",
     "name": "index.docker.io/library/latest:latest",
     "version": "sha256:b3fc03875e7a7c7e12e787ffe406c126061e5f68ee3fb93e0ef50aa3f299c481"
   }
 },
 ```

您可以看到高亮显示的元数据。SBOM 下载的完整示例将包括所有相关组件、包、库、关于其用途/用途的简短描述、发布者、分发类型及其依赖项。

所以，这一切都引出了我们一开始的问题: 我们到底该拿 SBOM 怎么办？事实是，这仍在进行中，许多高级开发人员和安全工程师对此有完美的答案。在大多数情况下，SBOM 的目标是使这份库存可访问、备份和安全。许多时候，您会发现 SBOM 存储在工件存储库中，备份到 S3 存储桶中，或由提供商托管，以便在知道容器中运行的内容变得至关重要时可以轻松访问。

![](https://cdn.thenewstack.io/media/2023/09/5ac73ef6-image2a.jpg)
*[Slim.AI 2022 年公共容器报告](https://www.slim.ai/blog/container-report-2022/)*

不仅存在如何真正从这些类型的工件中提取价值的问题，而且随着容器继续增长规模和复杂性，团队将如何管理它们也是一个问题。这种增长可能会导致更长的 CI/CD 处理时间和 DevSecOps 团队的工作量增加。SBOM 的使用和管理在软件供应链管理中将继续受到关注。

## 软件透明度的迫在眉睫的重要性

Chris Hughes 和 Tony Turner 在他们最新的书《软件透明度》中分解了 SBOM 所封装的基本原则，其中 SBOM 的功能被描述为实现软件透明度的基础元素，使组织能够识别潜在的漏洞并积极解决它们。尽管人们担心 SBOM 为攻击者提供了可见性，但 Hughes 指出“拥有 SBOM 会让软件使用者处于一个更好的位置，以便了解软件使用的初始风险以及消费的软件中的软件组件相关的新出现的和涌现出的漏洞。”

根据 [Gartner](https://www.gartner.com/en) 的说法，到 2025 年，SBOM 将成为 60% 软件提供商的必需品，因为它们将成为实现软件供应链安全的关键组成部分。这一预测性见解证明了在不可避免的需求增长之前生成 SBOM 的必要性。

[AWS](https://aws.amazon.com/about-aws/whats-new/2023/06/software-bill-materials-export-capability-amazon-inspector/) 最近宣布其支持 Amazon Inspector 的 SBOM 导出功能，这是一种漏洞管理服务，可以扫描整个 AWS 组织中的 AWS 工作负载，以洞悉您的软件供应链。像[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline-mention)(AWS)或 [Docker](https://www.docker.com/blog/announcing-docker-sbom-a-step-towards-more-visibility-into-docker-images/) 之类的重量级公司发布 SBOM 可导出性功能的是一个明显的暗示，即预计从软件供应商那里提供软件透明度的需求和紧迫性会增加。 Slim.AI 也为您的容器镜像提供了生成和管理 SBOM 的途径。

## Slim 为 SBOM 激增提供解决方案

在不断发展的软件供应链安全(SSCS)环境中，确保领先于未来要求至关重要。 Slim 使用高级扫描和分析功能生成您可以立即下载的 SBOM。 我们彻底检查整个堆栈以提取关键信息并构建组件的详细清单。 这使组织能够在确保遵守不断发展的监管要求的同时维持强大的安全态势。

NTIA 建议在构建时或在容器镜像中生成和存储 SBOM，以备新版本发布。 在 Slim 平台上，您可以[连接到容器 registries](https://www.slim.ai/docs/connectors) (如 AWS、Docker Hub、Google Container Registry 等)，为每个容器镜像存储 SBOM。 作为平台上可访问的许多工件的一部分，为原始容器镜像和经过强化的容器镜像生成 SBOM。 在平台上完成容器强化流程，以生成应用程序真正需要的关键包的更小、更优化和更不易受攻击的容器镜像版本，以部署到生产环境。

## SBOM 的不断发展的未来

在 Log4J 之后举行的[国会听证会](https://www.hsgac.senate.gov/hearings/responding-to-and-learning-from-the-log4shell-vulnerability/)上，云原生行业的消息很清楚: SBOM 只是一个起点。 尽管在发生攻击时，进行风险评估需要完整的软件清单，但它们本身并不能防止攻击。 人们对将 SBOM 作为其事实来源的新工具感到兴奋。

在那之前，大多数 registries 都在努力直接在您选择的 registries 内存储和管理 SBOM 的功能。

随着广受欢迎的容器和包内置和维护 SBOM，从野外获取的资源开始缓解和降低风险将变得更加容易和快速。 此外，许多安全组织如 OWASP 和 OpenSSF 正在努力使工具更易于访问和对开发者更友好，以推动采用和更广泛的使用。

[像缩减和强化容器](https://www.slim.ai/docs/example-nginx)这样的额外措施也可以为确保您只将应用程序实际所需的关键包运送到生产中提供更大的安全性。 这将为我们对第三方包和导入提供更大的信任，并为我们的整个软件供应链提供更大的安全性。
