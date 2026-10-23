OpenAI周四宣布，将其 [Open Responses API 规范](https://www.openresponses.org/)捐赠给开源的 [智能体AI基金会](https://aaif.io/) (AAIF)。

除了 Open Responses 之外，[OpenSandbox](https://open-sandbox.ai/architecture/)、Anthropic 的 [Agent Skills](https://github.com/anthropics/skills) 以及 HuggingFace 用于智能体环境的 [OpenEv](https://github.com/openenv/OpenEnv) 框架也将加入 AAIF。

它们将与 MCP 和 A2A 协议、AGENTS.md（同样来自 OpenAI）、开源AI智能体 goose、agentgateway 以及 Agent Router 等其他 AAIF 项目汇聚一堂。该基金会隶属于 Linux 基金会，于 2025 年 12 月成立，MCP、goose 和 AGENTS.md 是其首批项目。

至于 Open Responses，其核心理念是为开发者提供一组能够跨 LLM 提供商运行的核心 API 调用。当 OpenAI 在 1 月份首次宣布该规范时，该项目背后的团队[指出](https://community.openai.com/t/open-responses-for-the-open-source-community/1371770)，几乎所有 LLM 提供商现在都提供相同的构建模块（消息、工具调用、函数调用等），但它们在各自的 API 中的表示方式却各不相同。

![](https://cdn.thenewstack.io/media/2026/10/6139c52b-img_5847-1024x768.jpg)

智能体AI基金会项目。图片来源：The New Stack。

Open Responses 旨在创建一个标准化这些原语的规范，这样开发者在不同模型之间切换时，就不必在每个供应商的独特 API 之间进行转换。

OpenAI 发言人告诉 *The New Stack*：“当我们共同创立 AAIF 时，我们贡献了 AGENTS.md，这是一种为编码智能体提供项目特定指令的方法。Open Responses 解决了构建智能体的另一个部分，它为开发者提供了一个共享格式，用于通过支持它的端点与模型进行交互，从而让他们减少需要维护的特定供应商集成。Vercel AI Gateway 和 Databricks Model Serving 已经实现了它，而 AAIF 将为开发者和提供商提供一个中立的家园，以共同继续开发该规范。”

## 为什么中立的家园至关重要

正是这种中立的家园，通常是公司将项目捐赠给基金会的原因。AAIF 是 Linux 基金会的一部分事实上的标准，它为流行的开源项目提供供应商中立的家园，并设有[技术指导委员会](https://www.openresponses.org/governance)（最初由项目维护者组成），负责处理技术讨论。

## 谁已经支持它 —— 谁还没有

该规范已经获得了广泛支持，支持者包括 AWS（在 Bedrock 中）、Databricks、LM Studio、Ollama、Hugging Face、Nvidia、OpenRouter、Red Hat、Vercel，以及 vLLM 和 OGC（原 Llama Stack）等开源项目。

这份名单中缺少的名字包括 OpenAI 的竞争对手 Anthropic，后者定义了自己的 [Messages API](https://platform.claude.com/docs/en/api/messages) 以供开发者访问其模型。Anthropic 是 AAIF 的成员，所以也许未来某天我们会看到该公司采用这一规范。

Google 也有其用于让开发者与其模型交互的默认 Interactions API。

Open Responses 并没有掩盖其血统。该项目自身的贡献者指南指出，其核心架构文件是从 OpenAI 的 API 复制而来的。尽管 OpenAI 早期的 Chat Completions API 成为了其他人用来效仿其产品的早期标准，但 Anthropic 的 Messages API 现在也留下了鲜明的印记（在很大程度上归功于 Claude Code 的成功），DeepSeek、Moonshot、Z.ai、MiniMax 等公司也公开了与 Anthropic 兼容的端点。

这种分裂正是像这样供应商中立的规范旨在解决的碎片化问题。