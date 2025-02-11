# OpenAPI Initiative：新标准及路线图一览

![Featued image for: OpenAPI Initiative: New Standards and a Peek at the Roadmap](https://cdn.thenewstack.io/media/2025/02/62ff094f-openapi-standards-2-1024x576.jpg)

OpenAPI 是一种以标准方式为人类和机器受众描述你的 [API](https://thenewstack.io/api-management/) 的方法。从 OpenAPI 描述中，API 生产者可以检查他们的 API 是否合规，为他们的 API 运行自动化测试工具，并发布即时文档。API 消费者也可以使用这些文件来支持他们自己的集成。

虽然 OpenAPI 标准本身并不新，但近几个月来，[OpenAPI Initiative](https://www.openapis.org/) 发布了一些更新，包括 OpenAPI 规范的更新和两个新标准的发布。

10 月份发布的 OpenAPI Overlay Specification 描述了一系列应用于 OpenAPI 描述的编辑，从而更容易重复对描述进行相同的更新。几乎同样新的 OpenAPI Arazzo Specification 于 5 月份发布，它提供了一种机制来概述 API 调用的序列，以及如何执行涉及多个 API 操作的过程。

## OpenAPI 更新

作为补丁版本，10 月份发布的 [3.1.1 版本的规范](https://spec.openapis.org/oas/v3.1.1.html) 仅收到了一些小的更新。但作为自 2021 年初以来的首次更新，这些更新确实表明该项目运行良好。许多更改也包含在 OpenAPI 3.0 的更新中，现在版本为 3.0.4。

这些补丁版本中的大多数更改都是 [对规范文档中措辞的改进](https://github.com/OAI/OpenAPI-Specification/releases/tag/3.1.1)，澄清了许多模棱两可的条款，并添加了示例。一些章节被重构为五个新的附录，并添加了新的介绍性文本。

文档的某些部分被扩展和重新措辞，以解决来自社区的常见问题或疑问，并为工具和最终用户社区提供更清晰的指导。特别是文档解析、数据类型和序列化方面的一些领域已经受益于关注。

除了规范本身的更改之外，发布的 [JSON Schema representations](https://spec.openapis.org/#openapi-specification-schemas) 也收到了一些更新。

## 新的 Overlay Specification

Overlay Specification 已经起草了一段时间，并在 10 月份正式发布。Overlay 是一个 JSON 或 YAML 文档，描述了要对 OpenAPI 文档执行的一系列操作。

Overlay 的一些好的用例可能是：

- 更新操作、参数或标签的描述，以在发布文档之前澄清和改进措辞。
- 将分页参数添加到 OpenAPI 描述中的所有 `GET` 端点。
- 删除所有标记为 `deprecated` 的操作，或匹配某些其他条件
- 添加特定于工具的扩展，例如文档工具的显示名称或 SDK 生成器的方法和模块名称。

Overlay 可以针对特定的 OpenAPI 描述，也可以用于任何/许多 OpenAPI 描述。以下示例 Overlay 将许可证添加到 OpenAPI 描述：

虽然“设计优先”被认为是 API 开发的最佳实践，但许多项目使用“代码优先”方法，并从 API 应用程序的代码自动创建 OpenAPI 描述。以这种方式工作使得改进 OpenAPI 描述变得困难，因为它会在代码更改时重新生成。Overlay 允许对重新生成的 OpenAPI 进行可重复的更改。

多种 API 工具包括对使用 Overlay 的生产就绪支持。尝试来自 [Speakeasy](https://www.speakeasy.com/docs/speakeasy-reference/cli/getting-started) 或 [Bump.sh](https://github.com/bump-sh/cli) 的 CLI 工具，或访问 [OpenAPI Overlays repository](https://github.com/OAI/Overlay-Specification/) 以获取更多选项。

## 新的 Arazzo Specification

如前所述，Arazzo 规范于去年 5 月发布，但今年 1 月发布了该规范的补丁版本（最次要的更新），至 [1.0.1 版本](https://spec.openapis.org/arazzo/latest.html)。Arazzo 描述是一个 JSON 或 YAML 文档，详细说明了 API 调用的序列，将它们链接到更复杂的工作流程中。

对于我们的现代应用程序，其中操作比进行单个 API 调用更复杂，Arazzo 有助于连接各个点，以便描绘更大的图景。

Arazzo 文档描述了一个或多个工作流程，每个工作流程包含一系列步骤。每个步骤都是一个 API 调用，可以引用现有的 OpenAPI 文档以获取调用的详细信息。每个步骤都包含成功的标准；只有在满足标准时才会执行下一步。
表示更复杂流程对于创建交互式文档以引导用户完成各个步骤、生成可将多个 API 调用作为单个函数执行的 SDK 或测试实际 API 工作流程非常有用。

Arazzo 的工具尚处于早期阶段，但在 [Arazzo 规范存储库](https://github.com/OAI/Arazzo-Specification/tree/main/examples/1.0.0) 中有一些很棒的示例，可以作为任何想要使用新格式的人的良好起点。[Spectral](https://meta.stoplight.io/docs/spectral/) 和 [Redocly CLI](https://redocly.com/docs/cli) 也已将 Arazzo 支持添加到其 linting 工具中，这对于了解和使用该格式是一个很大的推动作用。

大多数 API 工具提供商的路线图上都有 Arazzo，其中包含用于记录和测试 API 工作流程的工具，因此这是 2025 年“值得关注”的主题。

## OpenAPI 的下一步是什么？

OpenAPI 是一个活跃的项目，有宏伟的计划。OpenAPI 主要规范的下一个议程是 3.2 版本，预计将在未来几个月内发布。3.2 版本将包括安全方案的更新、扩展的标签功能和其他改进。

目前处于早期规划阶段的是 OpenAPI 4.0 项目，代号为“Moonwalk”。该项目值得关注。

OpenAPI 规范是开放标准，开发这些规范的项目也是开放的，欢迎贡献者和旁观者。查看项目网站以了解有关存储库、公开会议和 Slack 社区的信息。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。