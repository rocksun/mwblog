# 制造最佳实践如何塑造软件开发

![Featued image for: How Manufacturing Best Practices Shape Software Development](https://cdn.thenewstack.io/media/2024/10/33b15275-manufacturing-best-practices-shape-software-dev-1024x576.jpg)

传统的制造最佳实践提供了宝贵的见解，丰富了我们对[现代软件开发](https://thenewstack.io/where-is-the-complexity-of-modern-software-coming-from/) 的方法。

制造商依赖质量控制、供应链管理和严格的标准来实现高效生产。软件开发人员在将开源组件纳入其开发流程时，可以采用这些原则。

随着软件开发越来越像从较小的部分（[其中许多是开源的](https://www.linuxfoundation.org/blog/blog/a-summary-of-census-ii-open-source-software-application-libraries-the-world-depends-on)）组装复杂产品，我们可以从制造商如何优化其流程以确保质量和降低风险中吸取经验教训。

让我们探索这些经验教训，看看它们如何帮助组织管理其[软件供应链](https://www.sonatype.com/resources/articles/what-is-software-supply-chain)。

## 了解软件供应链

就像传统的供应链涉及采购、组装和分发实物商品一样，软件供应链包括收集、集成和维护软件组件以构建应用程序。

在这两个行业中，质量、可靠性和透明度直接影响成功。物理供应链中的断链会导致生产延误或缺陷。

同样，脆弱或过时的软件组件会使软件面临[安全风险](https://thenewstack.io/navigating-open-source-software-risks-whose-job-is-it-anyway/)、许可证问题或性能问题。

## 软件组件的质量控制

从制造业借鉴的一个基本原则是质量控制。在传统制造业中，公司依赖来自信赖供应商的高质量组件，以确保最终产品的安全性和可靠性。

在软件开发中，这涉及仔细选择维护良好、安全且没有[漏洞](https://thenewstack.io/vulnerabilities-versus-intentionally-malicious-software-components/) 的开源组件。

制造商在流程早期进行质量检查，以识别和解决问题，防止问题升级。在软件开发中，这种方法反映在自动化测试、代码审查和[软件成分分析 (SCA)](https://www.sonatype.com/resources/articles/what-is-software-composition-analysis) 等实践中，以持续监督组件的健康状况和安全性。

为了使用制造业的原则来增强软件开发，请考虑以下几点：

- 使用高质量组件，包括安全可靠的开源元素。
- 在早期阶段及时解决缺陷。
- 阻止已知缺陷向下游发展，尤其是进入生产环境。

## 供应商管理和开源项目

在制造业中，公司通常遵循结构化的流程来选择和评估供应商。他们优先考虑那些符合严格质量标准并以提供可靠组件而闻名的供应商。

在选择要集成到您的软件中的组件时，您通常会评估其可维护性、安全实践和更新频率。开源组件的质量各不相同。一些组件受益于庞大而活跃的社区，而另一些组件可能被忽视或很少更新。

就像制造商通过选择可靠的供应商来降低风险一样，软件团队应该避免依赖未维护或管理不善的开源组件。

在选择高质量组件时，请考虑以下标准：

- 定期维护和更新频率。
- 一群积极且响应迅速的贡献者。
- 经过验证的安全性和可靠性历史。
- 透明的贡献指南和开放式治理。

## 使用 SBOM 进行跟踪和透明度

制造商依赖物料清单 (BOM) 来跟踪其产品中的每个组件。这种透明度使他们能够迅速查明任何问题的根源，确保他们对供应链有全面的了解。

在软件开发中，软件物料清单 (SBOM) 充当软件组件的清单，提供有关其来源、版本和依赖关系的信息。SBOM 对于理解软件供应链、识别潜在的漏洞和管理许可证合规性至关重要。

通过采用制造业的最佳实践，软件开发团队可以提高其软件的质量、安全性和可靠性。通过关注质量控制、供应商管理和透明度，组织可以构建更强大的软件供应链，从而为客户提供更可靠和安全的软件。
在软件中，同样的原则通过[软件物料清单 (SBOM)](https://www.sonatype.com/resources/articles/what-is-software-bill-of-materials) 应用，其中列出了软件应用程序中使用的所有组件、[依赖项](https://thenewstack.io/a-guide-to-software-dependencies/) 和许可证。SBOM 越来越成为[管理软件供应链](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) 的关键资源，使开发人员和安全团队能够保持对应用程序中使用内容的可见性。

没有 SBOM，组织可能会不知道其软件中过时或存在漏洞的组件，从而难以解决安全问题。

## 自动化：扩展质量和安全性
与制造业一样，自动化可以简化流程并提高效率，软件开发也依赖于自动化来管理现代应用程序的复杂性。

以规模化方式手动监控开源组件几乎是不可能的。但借助软件成分分析，开发人员可以自动化[识别安全风险](https://thenewstack.io/a-guide-to-open-source-software-security/) 并确保合规性的过程。

自动化不仅可以加速开发，还可以降低人为错误的风险，因此团队可以高效地管理大量组件和依赖项。

自动化可以增强软件供应链的机会包括：

- 持续监控开源组件的安全漏洞。
- 自动更新和修补已知问题。
- 自动生成和验证 SBOM。
## 回收和主动问题解决
在制造业中，产品召回用于解决已分发产品的缺陷或安全问题。虽然召回软件并不像召回产品那样简单，但主动解决已知问题同样至关重要。制造商的目标是尽早发现缺陷并防止对客户造成影响。

同样，软件团队可以专注于在漏洞到达生产环境之前识别和解决漏洞。

通过在整个开发过程中纳入安全和质量检查——称为“[左移](https://www.sonatype.com/resources/articles/what-is-shift-left)”——软件组织可以最大程度地减少因安全漏洞或严重故障而不得不“召回”其软件的可能性。

## 利用制造原则实现成功的软件开发
通过采用制造业最佳实践，例如严格的质量控制、谨慎的供应商管理以及通过 SBOM 进行透明的跟踪，软件组织可以提高安全性、效率和可靠性。

随着开源软件在现代开发中仍然不可或缺，实施这些原则将有助于维护强大且有弹性的软件供应链。

通过借鉴制造业的成功经验，软件团队可以有效地应对开源消费的复杂性，并大规模创建更可靠的应用程序。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)