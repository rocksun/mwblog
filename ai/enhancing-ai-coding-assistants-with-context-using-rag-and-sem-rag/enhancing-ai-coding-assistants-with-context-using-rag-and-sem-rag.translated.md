## 使用 RAG 和 SEM-RAG 增强 AI 编码助手上下文

![增强 AI 编码助手上下文使用 RAG 和 SEM-RAG 的特色图片](https://cdn.thenewstack.io/media/2024/05/6738139e-ai-coding-assistant-context-rag-sem-rag-1024x576.jpg)

基本 AI 编码助手虽然有帮助，但由于依赖对软件语言和编写软件最常见模式的总体理解，因此常常无法提供最相关和上下文准确的代码建议。这些编码助手生成的代码适合解决他们负责解决的问题，但通常不符合各个团队的编码标准、惯例和风格。这通常会导致需要修改或完善其建议，以便将代码接受到应用程序中。

[AI 编码助手](https://thenewstack.io/the-pros-and-con-of-customizing-large-language-models/) 通常通过依靠特定 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 中包含的知识，并在各种场景中应用通用编码原则来发挥作用。因此，典型的 AI 助手通常缺乏理解项目特定上下文的的能力，从而导致建议在语法上正确，但可能与团队的独特指南、预期方法或架构设计不一致。支持生成式 AI 系统的 LLM 基于一组固定的训练数据运行，该数据不会随着项目的进行而动态演变。这种静态方法可能导致生成的代码与项目的当前状态或要求不匹配，从而需要开发人员进行进一步的手动调整。

## 使用 RAG 优化 LLM

有一种误解，即 AI 助手只是与 LLM 交互以生成用户正在寻找的结果。无论您是生成文本、图像还是代码，最好的 AI 助手都会使用一组复杂的准则来确保用户要求的内容（例如，完成特定任务的软件功能）和生成的内容（Java 函数，在正确的版本中，具有正确的应用程序参数）保持一致。

从任何 LLM 获得最佳输出的已验证技术之一是使用提示提供附加上下文。这种方法称为 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/)，已成为聊天机器人、AI 助手和成功服务于企业用例的代理的关键组成部分。

“使用对现有代码库和编码标准了解不足的 AI 编码助手就像从街上雇用一名训练有素的软件工程师：乐于助人且用心良苦，但可能会创建需要修改才能适合您应用程序的代码”

— Peter Guagenti，Tabnine

AI 编码助手与所有生成式 AI 工具一样，使用 LLM 作为代码生成的基础。为编码助手带来高度定制的 RAG 使他们能够生成更高质量且与公司的现有代码库和工程标准更紧密对齐的代码。

在聊天机器人的领域中，RAG 考虑了以结构化和非结构化格式提供的现有数据。通过全文或语义搜索，它仅检索足够多的上下文，并将其注入发送到 LLM 的提示中。

AI 编码助手可以使用类似（尽管更复杂）的方法，通过集成开发环境从现有代码库中检索上下文。高性能 AI 编码助手可以抓取项目工作区以访问当前文件、打开文件、Git 历史记录、日志、项目元数据甚至连接的 Git 存储库中的其他上下文。

RAG 赋能 [AI 编码助手提供高度相关和精确的结果](https://thenewstack.io/5-strategies-for-better-results-from-an-ai-code-assistant/)，方法是考虑项目的特定方面，例如现有的 API、框架和编码模式。AI 助手不会提供通用解决方案，而是根据项目的既定实践调整其指导，例如建议与当前实现一致的数据库连接，或提供无缝集成私有 API 的代码建议。通过利用 RAG，助手甚至可以生成反映现有测试的结构、样式和语法的测试函数，确保代码在上下文上准确且符合项目的需要。

这种方法可以带来无与伦比的个性化，开发人员可以立即接受。

## RAG 在编码助手中的工作原理

让我们来看看在编码助手上实现 RAG 所涉及的步骤。
## 第一阶段：索引和存储

最初，当编码助手安装并集成到开发环境中时，它会执行搜索并识别所有可以添加上下文的相关文档。然后，它将每个文档拆分为块，并将它们发送到嵌入模型。嵌入模型负责将每个块转换为向量，而不会丢失其语义表示。生成的向量存储在向量数据库中以供将来检索。编码助手可能会定期扫描工作区并将文档添加到向量数据库中。

## 第二阶段：编码

在下一阶段（编码）中，开发人员可能会创建注释或使用聊天助手生成特定函数。助手使用提示对存储在向量数据库中的先前索引集合执行相似性搜索。检索此搜索的结果并用于 [使用相关上下文扩充提示](https://roadmap.sh/prompt-engineering)。当 LLM 收到增强提示和上下文时，它会生成与上下文中已有的代码对齐的代码片段。

## RAG 在编码助手中的应用

将 RAG 应用于编码助手可以提高 LLM 生成的代码的性能、准确性和可接受性。它显著增强了该工具的实用性，并减少了开发人员重写或调整 AI 生成的代码所花费的时间。与项目的现有代码库直接对齐，可以提高代码建议的准确性，并极大地提高开发人员的生产力和代码质量。

“使用一个对你的现有代码库和编码标准不够了解的 AI 编码助手就像在街上雇用一个训练有素的软件工程师：乐于助人且用心良苦，但可能会创建需要修改才能适合你的应用程序的代码。当你分层加入适当级别的上下文（包括本地文件、项目或公司的代码库以及相关的非代码信息来源）时，就像让一位在你的公司拥有多年经验的高级工程师与你的开发人员坐在一起，”[Tabnine](https://www.tabnine.com/?utm_content=inline+mention) 总裁 [Peter Guagenti](https://www.linkedin.com/in/peterguagenti/) 说。“数字证明了这一点。允许我们使用其现有代码作为上下文的 Tabnine 用户接受了多 40% 的代码建议，而无需修改。当 Tabnine 连接到公司的整个存储库时，这个数字会更高。”

这是 RAG 解决阻碍传统编码助手的可扩展性和适应性限制的一种方式。随着项目的增长和演变，配备 RAG 的工具会不断学习和适应，根据从代码库中收集到的新模式和信息优化其建议。这种演变能力使 RAG 成为动态开发环境中非常强大的工具。

## 使用语义记忆增强 RAG

语义检索增强生成 (SEM-RAG) 是 RAG 技术的高级迭代，旨在扩展 RAG 的准确性和语境化。它通过使用语义记忆而不是向量搜索来增强编码助手，从而将语义理解集成到检索过程中。

与主要依赖向量空间模型来检索相关代码片段的传统 RAG 不同，SEM-RAG 采用了一种更细致的语义索引方法。此方法利用静态分析来深入理解代码库的结构和语义，识别代码元素中的关系和依赖性。

例如，SEM-RAG 可以分析 Java 和 TypeScript 等语言中的导入语句，使其能够从库中提取上下文相关的代码元素，即使无法直接访问源代码。此功能允许 SEM-RAG 理解和利用导入库的字节码，有效地使用这些见解来丰富提供给语言模型的上下文。

虽然传统的 RAG 通过将代码片段的矢量化表示与查询进行匹配，极大地提高了代码建议的相关性，但它有时缺乏完全掌握复杂软件项目语义细微差别的深度。SEM-RAG 通过关注代码中的语义关系来解决此限制，从而与项目的编码实践实现更精确的对齐。例如，通过理解项目架构中定义的关系和依赖性，SEM-RAG 可以提供不仅在上下文上准确，而且在架构上也一致的建议。这通过生成与现有系统无缝集成的代码来增强性能，从而降低引入错误或不一致的可能性。
## SEM-RAG：一种更深入的代码理解方法

SEM-RAG 的方法是将代码视为相互关联的元素，而不是孤立的片段，这比传统的 RAG 提供了更深入的语境化。这种理解深度促进了编码任务中更高程度的自动化，尤其是在代码库中相互依赖性至关重要的复杂领域。因此，SEM-RAG 不仅保留了传统 RAG 的所有优点，而且在理解代码的更深层次语义和结构方面至关重要的环境中超越了它。这使得 SEM-RAG 成为大规模和企业级软件开发的宝贵工具，其中维护架构完整性与代码正确性一样重要。

## 利用人工智能增强代码质量和开发人员生产力

选择通过 RAG 和 SEM-RAG 等高级技术融入上下文感知的人工智能编码助手，标志着软件开发工具演变中的变革性一步。通过嵌入对代码库上下文的深入理解，这些助手显着提高了他们生成的代码的准确性、相关性和性能。这种上下文集成有助于确保建议不仅在语法上正确，而且还符合您的特定编码标准、架构框架和特定于项目的细微差别，从而有效缩小了人工智能生成代码与人类专业知识之间的差距。

支持 RAG 的人工智能助手显着提高了开发人员的生产力并提高了代码质量。开发人员可以依靠这些增强的 AI 助手来生成不仅适合任务的代码，而且无缝融入更大的项目上下文中，从而最大程度地减少修订的需要并加速开发周期。通过以高度精确度自动化编码的更多方面，这些具有上下文感知的编码助手正在为软件开发设定新标准，推动人工智能工具像开发人员自己一样全面地理解和适应项目环境的复杂动态。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。