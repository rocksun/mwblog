<!-- 
# CI/CD中SBOM的实用方法第一部分 — CycloneDX

 -->

在本文中，我将介绍在CI/CD流水线中实现SBOM生成的实用用例及其益处。本文涵盖了SBOM的概念、其优势、流行格式以及Java和Python项目的实际实现。

> 译自 [A Practical Approach to SBOM in CI/CD Part I — CycloneDX](https://medium.com/@theowni/a-practical-approach-to-sbom-in-ci-cd-f3ce8071c0fa) 。

## 什么是SBOM，为什么需要在CI/CD中使用它？

追踪项目组件的想法并非新概念，多年来已经在各种场景中存在，不仅限于软件开发。然而，2018年美国国家电信和信息管理局(NTIA)承担起定义SBOM的责任。NTIA对**SBOM**的以下[定义](https://www.linuxfoundation.org/blog/blog/what-is-an-sbom)很好地阐述了其含义：

> 软件清单(Software Bill of Materials，SBOM)是一个完整、正式结构化的组件、库和模块列表，这些是构建给定软件所必需的，以及它们之间的供应链关系。这些组件可以是开源或专有的，免费或收费的，可以广泛获取或仅限访问。

2021年，在美国白宫发布《 Executive Order on Improving the Nation’s Cybersecurity》后，SBOM变得更加流行，该行政令包含有关加强软件供应链安全的部分。这些要求是在一系列与供应链相关的安全泄漏事件发生后提出的，包括[SolarWinds事件](https://www.malwarebytes.com/blog/news/2020/12/advanced-cyber-attack-hits-private-and-public-sector-via-supply-chain-software-update)。

这样的组件清单不仅对于国家安全领域的供应链安全非常有用，还为采用DevSecOps方法的任何开发软件的公司带来实际价值。正如我在前一篇[关于osv-scanner的文章](https://medium.com/@theowni/using-open-source-software-composition-analysis-tool-from-google-70fef62ec104)中强调的，使用SBOM来识别开源依赖中的漏洞非常有效。在CI/CD流水线中生成SBOM是最佳时机，因为就是在这里项目工件被创建。SBOM是一个文件，包含SBOM定义中强调的所有信息片段，最常用的格式是[CycloneDX](https://cyclonedx.org/)和[SPDX](https://spdx.dev/)。前者是OWASP的旗舰项目，后者由Linux基金会支持。

使用软件清单的好处:

- 能够追踪专有和开源组件
- 对开源问题进行有效的漏洞扫描
- 改进许可证治理
- 跟踪项目不同版本之间的自定义数据字段
- 可用于各种技术的通用格式

## CycloneDX与SPDX

在实际使用SBOM之前，我想强调两种最流行格式之间的区别。

[OWASP CycloneDX](https://cyclonedx.org/)是一个全栈的清单标准，提供高级的供应链功能以降低网络风险。该规范支持SBOM和其他几种清单，如硬件清单(HBOM)、机器学习清单(ML-BOM)等。CycloneDX轻量级而且是开源项目，受到许多第三方供应商的支持。此外，SBOM可以以JSON或XML表示。

另一方面，存在SPDX格式。[SPDX](https://spdx.dev/)也是一个开源项目。最初，其主要关注许可证管理，因为这是项目的初衷目标。然而，它现在也提供了存储项目依赖关系的功能。

为了让您了解SBOM格式的使用情况:

- [GitLab使用CycloneDX](https://about.gitlab.com/blog/2022/10/25/the-ultimate-guide-to-sboms/#types-of-sbom-data-exchange-standards)
- [GitHub允许以SPDX格式导出SBOM](https://github.blog/2023-03-28-introducing-self-service-sboms/)

选择项目的SBOM格式将取决于您独特的需求。在本文中，我将使用CycloneDX格式，因为它有许多官方支持的专门用于各种技术(如Java、Python、Docker等)的工具。

## 使用CycloneDX生成Java SBOM

为了展示如何为Java项目生成SBOM，我选择了一个支持Maven包管理的开源项目。由于我正在写SBOM，所以选择了[Dependency-Track](https://github.com/DependencyTrack/dependency-track)项目，我希望在单独的文章中对它进行更详细的介绍。Dependency-Track是一个持续的SBOM分析平台，可以帮助组织识别和降低软件供应链中的风险。

让我们克隆存储库以进行本地测试:

```bash
git clone https://github.com/DependencyTrack/dependency-track.git
cd dependency-track
```

现在，让我们运行[CycloneDX Maven插件](https://github.com/CycloneDX/cyclonedx-maven-plugin)来构建SBOM文件。可以如文档所示将Maven插件添加到pom.xml中:

```xml
<!-- uses default configuration -->
<plugins>
    <plugin>
        <groupId>org.cyclonedx</groupId>
        <artifactId>cyclonedx-maven-plugin</artifactId>
        <executions>
            <execution>
                <phase>package</phase>
                <goals>
                    <goal>makeAggregateBom</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
</plugins>
```

但是，上述步骤不是必需的。我建议一种更方便的方法，特别是在CI/CD中，使用Maven CLI运行以下命令：

```bash
mvn org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom
```

该命令为Maven项目生成包含传递(间接)依赖的SBOM，并默认将其保存在target/bom.json文件中。

最初，运行此命令花费了我5分钟多，但当依赖项已经本地存在时，只花了我13秒。在构建工件的CI/CD流水线中，构建SBOM的过程应该非常快。

以下截图显示了SBOM内容。第一个截图显示了JSON文件开头，包含生成文件工具的信息和元数据:

![](https://miro.medium.com/v2/resize:fit:786/format:webp/1*vgsHYhpBnkMTrXtnYY9LFA.png)

*截图显示CycloneDX JSON — 工具部分*

接下来的重要部分是组件，其中显示项目名称、版本、描述、许可证等元数据信息:

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*25BIwh69qdHHdWAEal7i3w.png)

*截图显示CycloneDX JSON — 组件部分*

另外，我们可以看到组件部分，其中列出了构建项目所用的所有组件。组件列表中的每个条目都包括名称、版本、描述和许可证(许可证在下面没有显示)。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*z8zcHi-9Cge7HSwCJvhVvg.png)

*截图显示CycloneDX JSON — 组件部分*

## 生成Python SBOM

在Python方面，我也选择了一个开源项目——这次是FastAPI。这是一个流行的、现代的、快速(高性能)的用于Python 3.7+构建API的Web框架。

让我们克隆存储库:

```bash
git clone https://github.com/tiangolo/fastapi.git
cd fastapi
```

为了为Python项目生成SBOM文件，我选择了[CycloneDX Python SBOM生成工具](https://github.com/CycloneDX/cyclonedx-python)。该工具当前支持Poetry、Pipfile或requirements文件。但是，对于以其他方式指定依赖关系的项目，可能需要进行额外配置才能确保正确处理。

实际上，FastAPI项目使用`pyproject.toml`通过`dependencies`属性指定依赖项。这种方法不被CycloneDX SBOM生成工具支持。然而，可以从当前使用的环境生成Cyclonedx。此外，从当前使用的Python环境生成SBOM还可以识别和添加许可证，这在其他选项中不可用。可以在`fastapi`目录下使用以下命令生成SBOM：

```bash
# create and activate dedicated Python venv
virtualenv -p python3 .venv
source .venv/bin/activate

# install CycloneDX SBOM generation tool for Python
pip3 install cyclonedx-bom

# install dependencies specified in pyproject.toml
pip3 install .

# generate CycloneDX SBOM
python3 -m cyclonedx_py --format json -e

# leave the created venv
deactivate
```

SBOM被生成并存储在`cyclonedx.json`文件中。需要注意，输出文件还包含`cyclonedx-bom`依赖项，在准确跟踪SBOM时这是不需要的，因为这个依赖项不是项目的一部分。我建议从最终的SBOM中删除这些额外的依赖项，并确保安装这种包不会干扰其他依赖项的版本。不幸的是，Python的官方CycloneDX工具在这种情况下可能不是很理想。使用二进制可执行文件的CLI而不是依赖于同一环境中安装的包可能更合适。

此外，Python工具不会用项目名称、描述、版本等信息填充SBOM文件。必须在单独的步骤中将这些信息添加到生成的文件中。可以在`metadata`部分中包含以下字典以向文件添加这些信息:

```json
    "component": {
      "type": "library",
      "bom-ref": "pkg:pypi/fastapi@0.103.1",
      "name": "fastapi",
      "version": "0.103.1",
      "description": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",
      "licenses": [
        {
          "license": {
            "id": "MIT"
          }
        }
      ],
```


最后但同样重要的是，应注意SBOM文件可以使用非对称加密进行签名。这样可以确保SBOM文件的真实性。在工件的生命周期中，可以验证签名以确保工件来自CI/CD流水线且未被篡改。这在保障供应链安全方面非常重要。可以使用官方[CycloneDX CLI](https://github.com/CycloneDX/cyclonedx-cli)工具来实现。

## SBOM生成后，接下来该做什么？

有大量关于SBOM的资料，各种格式，它们的优点，但很少有描述如何存储、跟踪和后续处理SBOM的。在我看来，这是谈论软件清单时的关键部分。

就SBOM的存储和跟踪而言，最有趣的开源项目是OWASP支持的Dependency Track。它可以通过API和专用CLI工具消费SBOM。它还有一个漂亮的用户界面，在开源项目中并不常见。此外，根据几个漏洞数据库，它可以提供对所跟踪项目中的开源漏洞的洞察。

![OWASP Dependency Track](https://miro.medium.com/v2/resize:fit:828/format:webp/0*xGolP82OYBeNjwHd.png)

Dependency Track是另一个故事的话题，在那里我将介绍部署和集成步骤...

继续关注更多DevSecOps内容！
