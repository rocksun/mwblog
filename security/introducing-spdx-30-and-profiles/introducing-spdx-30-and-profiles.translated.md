# 认识系统包数据交换：SPDX 3.0，带配置文件

![用于：认识系统包数据交换：SPDX 3.0，带配置文件的特色图片](https://cdn.thenewstack.io/media/2024/04/49c2dc2b-spdx_logo_emblem-2-1024x576.png)

**西雅图 —**

“系统”物料清单的开放标准 [SPDX](https://thenewstack.io/spdx-software-supply-chain-spec-becomes-an-iso-standard/) 迈出了重要一步。

多年来，我们需要一种标准方法，让公司能够在 [软件物料清单 (SBOM)](https://thenewstack.io/how-to-create-a-software-bill-of-materials/) 中标准化其许可证和组件信息（元数据），以便轻松发现和标记其产品中的开源组件。

该问题的答案是 [软件包数据交换 (SPDX)](https://spdx.dev/)，又称国际标准化组织 (ISO) 标准：[ISO/IEC 5962:2021](https://www.iso.org/standard/81870.html)。现在，在西雅图举行的 [北美开源峰会](https://events.linuxfoundation.org/open-source-summit-north-america/) 上，最新版本 SPDX 3.0 已正式亮相。

[Mitre Corporation](https://www.mitre.org/) 的高级首席软件和供应链保障工程师 [Bob Martin](https://www.linkedin.com/in/robert-martin-589579/) 表示：“这已经是一场持续了六年的拉锯战，但 SPDX 现在不仅规定了软件物料清单的格式，还规定了所有内容的格式。”

因此，SPDX 今后将被称为系统包数据交换——表明其用途已不仅仅局限于软件。

新的系统包数据交换如何涵盖“所有内容”？通过添加 SPDX 配置文件。它从包含所有程序、硬件项目、人工智能、软件即服务等内容的核心 SPDX 配置文件开始。在其之上是用于安全、许可和构建信息的附加元数据的配置文件。

SPDX 已通过 SPDX 配置文件变得更加有用。它提供了针对流行用例（例如安全、精确许可、人工智能模型训练等）微调的信息子集。此增强功能简化了 SPDX 的使用，赋能了开发、安全、数据科学和法律领域的利益相关者。

如果这听起来很棒但很复杂，那么，你说的没错。为了让 SPDX 3.0 更易于使用，它包含了开箱即用的配置文件模板。这将简化开发人员和最终用户的采用和实施。

## 寻求开发人员的采用

[GitHub](https://github.com/) 也在竭尽全力让程序员更容易采用它。“我们向 GitHub 的依赖关系图添加了 SPDX 导出，以便开发人员能够轻松满足监管要求，并且我们已经看到社区对此做出了热情的回应，”GitHub 的产品管理高级总监 [Justin Hutchings](https://github.com/jhutchings1) 说。

“提高 [软件供应链](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/) 的透明度是构建一个更安全世界的基础。”

这一点很重要，因为 SPDX 不仅仅是一个好主意；它是一项法律——至少在美国是这样。

[第 14028 号行政命令](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity) 要求“一份正式记录，其中包含用于构建软件的各种组件的详细信息和供应链关系”，类似于包装上的食品成分标签。简而言之，即 SBOM。

SBOM 不必使用 SPDX。还有其他标准 SBOM 格式，例如 [CycloneDX](https://cyclonedx.org/) 和 [通用平台枚举 (CPE)](https://cpe.mitre.org/about/)。然而，作为 ISO 标准，并且通过配置文件将 SPDX 扩展到基本上任何平台或流程，SPDX 似乎是成为主导标准的稳妥选择。

正如 [英特尔](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) 软件和高级技术集团副总裁 [Melissa Evers](https://www.linkedin.com/in/melissaevers/) 所说，“英特尔采用开放的国际标准，以帮助提供安全信息的透明度和披露，符合新兴法规。

“SPDX 版本 3 的发布是一个重要的里程碑，因为其模块化设计允许记录软件组件的多个方面的信息，包括安全和许可。”

在众多其他软件和安全公司及组织的支持下，SPDX 3.0 似乎肯定会成为未来几年的 SBOM 标准。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等内容。
](https://youtube.com/thenewstack?sub_confirmation=1)