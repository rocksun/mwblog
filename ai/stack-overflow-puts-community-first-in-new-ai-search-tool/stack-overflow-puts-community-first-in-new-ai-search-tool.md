
<!--
title: Stack Overflow AI搜索工具：社区优先，共创未来
cover: https://cdn.thenewstack.io/media/2025/12/f3bfc754-philip-oroni-4bh1xljd1_0-unsplash.jpg
summary: Stack Overflow 发布 AI Assist，一个对话式 AI 搜索工具。它优先社区验证知识，结合 RAG+LLM，提供透明归因，免费使用。
-->

Stack Overflow 发布 AI Assist，一个对话式 AI 搜索工具。它优先社区验证知识，结合 RAG+LLM，提供透明归因，免费使用。

> 译自：[Stack Overflow Puts Community First in New AI Search Tool](https://thenewstack.io/stack-overflow-puts-community-first-in-new-ai-search-tool/)
> 
> 作者：Darryl K. Taft

[Stack Overflow](https://stackoverflow.co/) 已宣布正式发布 [AI Assist](http://stackoverflow.com/ai-assist)，这是一款对话式 [AI 搜索工具](https://thenewstack.io/why-ai-search-platforms-are-gaining-attention/)，它优先考虑人类验证的社区知识而非纯粹的 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 响应。此次正式发布是在 [WeAreDevelopers](https://www.wearedevelopers.com/) 2025 大会上 [成功发布测试版](https://stackoverflow.blog/2025/07/10/a-new-era-of-stack-overflow/) 之后进行的。

随着 [生成式 AI (GenAI)](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 的出现，一些人认为 Stack Overflow 可能已经“玩完”了。然而，该公司不会不战而退。事实上，Stack Overflow 的首席产品和技术官 Jody Bailey 表示，它根本不会退出。

## 差异化优势

实际上，Stack Overflow 的产品与纯粹基于 LLM 的解决方案之间的关键差异化优势在于该产品采用社区优先的方法。AI Assist 首先使用改进的重排序器搜索 Stack Overflow 内容，然后总结结果并明确归功于原始贡献者。AI Assist 主要来源于 Stack Overflow 社区中人类验证的知识，确保开发者能够快速免费地获得准确、可解释的帮助。

另一个差异化优势是该产品采用混合式 [检索增强生成 (RAG)](https://thenewstack.io/beyond-basic-rag-ai-agents-for-context-aware-responses/) + LLM 架构，其中 AI 充当“答案审计员”，仅在必要时补充社区内容，从而在没有相关内容时防止出现死胡同结果。该服务还提供透明的归因。它归功于原始内容创作者，兑现了 Stack Overflow 认可社区贡献的承诺。

“大多数大型语言模型都使用 Stack Overflow 数据，因为它们大多数都与我们签订了协议，”Bailey 告诉 The New Stack。但他表示，这些解决方案往往倾向于得票最高的答案。

这在大多数情况下都很有用。

“但如果你与工程师交流，他们真正想要的答案往往是列表中的第三或第四个答案，可以说是这样，”Bailey 指出。“而真正获得这一点的唯一方法是将归因追溯到信息的原始来源。”

与其他生成式 AI 工具不同，AI Assist 与公共平台上最新的社区问答保持同步。它在 [stackoverflow.com/ai-assist](http://stackoverflow.com/ai-assist) 上免费使用。

超过 25 万名技术专家已经在使用它进行调试、比较库、理解错误和应用程序架构。高级用户每天创建多达 6,400 条消息，其中 75% 专注于高度技术性的内容。

Stack Overflow AI Assist 使用 OpenAI 模型进行生成，并使用专有的 Stack Overflow 模型进行搜索和重排序。它首先搜索 Stack Overflow，然后生成带有归因的摘要答案，仅当没有相关社区内容时才回退到纯 LLM 生成。

Bailey 在一份声明中表示：“通过在 AI 时代提供一个可信赖的人类智能层，我们旨在满足所有技术专家更广泛的需求，同时仍然支持我们培养社区、赋能学习并释放增长潜力的更大使命。”“通过构建这款优先考虑社区内容并提供不可协商归因的混合式 AI 模型产品，我们不仅是在‘正确的方式’下做 AI，我们还在向整个行业发出信号，即人类创造的知识必须得到认可和验证，以改善技术格局和整个世界。”

## AI Assist 的重点

根据 Stack Overflow 的说法，AI Assist 的重点是：

*   **提供一种新的入门方式：** 提供现代、对话式的替代方案，以获得更相关的结果。为用户，尤其是寻求技术帮助的新用户，创造更易于访问的体验。
*   **实现主动学习：** 在用户所在之处提供推理和上下文。这是朝着整合教育功能以增强学习效果迈出的一步。
*   **深化连接性：** 为 AI Assist 与其他 Stack Overflow 页面功能（如聊天和编程挑战）的连接铺平道路，并最终扩展到外部工具，如 IDE 扩展和 Discord 应用程序，将其发展成为面向各地开发者的产品。

Bailey 表示，同时，测试版的主要经验包括改进了提示工程以实现高效的 LLM 查询；将范围扩展到 Stack Overflow 之外，包括其他 Stack Exchange 网站（数学、Ubuntu 等）；以及在简洁答案和提供上下文之间取得了更精细的平衡。

此外，Bailey 表示 AI Assist 未来的集成包括一个用于编码代理（Copilot、Cursor、Replit）的 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 服务器；一个公共平台的只读版本；以及一个适用于 Stack Overflow Internal 的双向版本（在 [Microsoft Ignite](https://ignite.microsoft.com/en-US/home) 上宣布）。

Bailey 对“Stack Overflow 毫无意义”说法的回应是：“那假设每个问题都已经被回答了，对吧？根据我的经验，情况并非如此；我们仍然看到很多新问题。”

愿景的一部分是让开发者更容易在该网站上提问。

“在 Stack Overflow 上写一个好问题往往是一件非同小可的事情，”Bailey 说。

此外，“我们过去常说我们是开发者的第三块屏幕，但现在真正的意图是在开发者所在之处满足他们的需求，我们认为 MCP 服务器是实现这一目标的一种方式，”他说。