<!--
title: Claude 现在可以直接在聊天窗口中删除您的生产环境语音智能体
cover: https://cdn.thenewstack.io/media/2026/02/18275966-ubaid-e-alyafizi-qcc8h2npx1c-unsplash-scaled.jpg
summary: ElevenLabs 推出了全新的 MCP 连接器，允许开发者通过 Claude 聊天窗口直接管理、修改甚至删除生产环境中的语音智能体。该工具简化了操作流程，但同时也带来了生产环境变更的风险，因此 ElevenLabs 引入了多重权限控制与测试框架，以平衡开发效率与系统安全性。
-->

ElevenLabs 推出了全新的 MCP 连接器，允许开发者通过 Claude 聊天窗口直接管理、修改甚至删除生产环境中的语音智能体。该工具简化了操作流程，但同时也带来了生产环境变更的风险，因此 ElevenLabs 引入了多重权限控制与测试框架，以平衡开发效率与系统安全性。

> 译自：[Claude can now delete your production voice agent from a chat window](https://thenewstack.io/elevenlabs-mcp-voice-agents/)
> 
> 作者：Amanda Caswell

开发者现在可以要求 Claude 检查生产环境的语音智能体、修改其系统提示词、彻底更换语音，或在无需打开 ElevenLabs 仪表盘的情况下，估算使用不同语言模型带来的成本。

周一，ElevenLabs 推出了托管式 MCP 连接器，使 Claude 能够对使用 ElevenAgents 构建的聊天智能体进行读写访问。除了创建智能体和比较配置外，该连接器还可以在应用更改前计算预期的 LLM 使用量和成本。例如，开发者可以问 Claude：“与使用 GPT-4o 相比，我的结账智能体使用 Gemini 2.5 Flash 后每次对话的成本是多少？” 考虑到[仅靠廉价模型并不能保证在涉及智能体编排时降低账单](https://thenewstack.io/agentic-ai-token-costs/)，这类问题现在变得更加重要。

> “与使用 GPT-4o 相比，我的结账智能体使用 Gemini 2.5 Flash 后每次对话的成本是多少？”

## OAuth 取代了本地 API 密钥

ElevenLabs 于 2025 年 4 月为其 Claude Desktop、Cursor 和其他 MCP 客户端发布了最初的开源服务器。开发者此前需在本地运行它，添加 ElevenLabs API 密钥，并用其生成语音、克隆音色或转录音频。而新的服务器专注于管理 ElevenLabs 工作空间中现有的智能体。

开发者可以从 Claude 的目录中安装该连接器，并通过 OAuth 登录，这消除了运行服务器或将 API 密钥粘贴到 Claude 中的必要性，同时限制了对 ElevenLabs 工作空间的访问权限，且仅限于登录时批准的权限。

据 ElevenLabs 称，Claude 可以更新智能体的系统提示词、语言、音色和开场白；检索转录内容；探索对话主题；检查知识库大小；生成样本语音，甚至删除智能体。

由于其中一些工具可能会更改或移除生产环境的智能体，团队被提供了两层访问控制。管理员可以在整个组织内禁用工具，用户也可以为自己的会话设置更严格的限制。ElevenLabs 特别警告称，删除智能体是破坏性的操作，建议在批准工具调用之前进行审查。

这种访问控制模式反映了其他平台在向 AI 智能体开放生产系统时所采用的方案。当 [GoDaddy 发布其开发者平台](https://thenewstack.io/godaddy-developer-platform-domains/)并使域名注册能够由 AI 编程助手编程时，它采用了“报价后执行”模型，结合幂等键和将每笔购买与人工批准挂钩的同意对象，这些保障措施是专门为自动化智能体发起不可逆操作时设计的。AWS 则采取了不同的角度，利用其 [Dogwood 智能体工具调用策略引擎](https://thenewstack.io/aws-dogwood-agent-policies/)来评估工具调用在上下文中是否有效。ElevenLabs 的两层模型介于两者之间。

## 无需验证的批准

使用新的 MCP 连接器，开发者可以要求 Claude 修剪支持智能体的系统提示词以节省 Token。如果修改过程中意外删除了告知智能体将计费纠纷升级给人工处理的行，那么在审查过程中，较短的提示词可能看起来仍然没问题。

确认界面告知团队更改已获批准，但它无法显示提示词是否仍能按预期工作，或模型切换是否更改了智能体的工具调用。成功的工具调用仅表明操作已运行，并不意味着它产生了预期的结果，这呼应了[最近发生的 Claude 容器化失败事件](https://thenewstack.io/anthropic-claude-containment-failure/)，其中模型完成任务的方式越过了操作员设定的边界。

ElevenLabs 通过智能体测试框架解决了这些风险，该框架允许团队在部署前模拟对话，并查看智能体是否按预期响应，包括调用工具时。同样的测试可以通过 CLI 或 API 运行，而不是在仪表盘中手动处理。

> 确认界面告知团队更改已获批准，但它无法显示提示词是否仍能按预期工作，或模型切换是否更改了智能体的工具调用。

## 版本控制与智能体即代码工作流

该平台还提供可选的智能体版本控制，允许开发者在不同的分支上保存配置更改，并将部分生产流量路由到这些分支进行灰度发布或 A/B 测试，尽管 ElevenLabs 表示一旦启用版本控制，则无法禁用。

对于希望将智能体配置纳入代码仓库的团队，ElevenLabs CLI 可以将智能体作为代码进行拉取和推送，并提供包含部署前试运行和部署后状态检查的标准化 CI/CD 工作流。随着供应商对智能体运行方式实施更严格的控制，将智能体配置保持在代码中可能变得更有价值。[微软引入 Copilot Token 配额](https://thenewstack.io/microsoft-copilot-token-budgets/)表明，即使是最大的供应商之一，也在限制其智能体可以使用多少 Token。

托管式 MCP 文档解释了 Claude 如何更改智能体，但未说明该更新是否进入 ElevenLabs 的测试和版本控制工作流，还是直接进入当前配置。目前也不清楚团队是否可以从 Claude 撤销该更改。

## 两种工作流，一个生产智能体

目前，团队需要在用于检查和修改配置的 Claude 对话速度，以及用于自动化测试和版本化发布的 CLI 和 API 流水线之间进行选择。而且，这种分裂状态可能会持续存在。[Anthropic 最近收购 CI/CD 初创公司 Mendral 的人才](https://thenewstack.io/anthropic-mendral-cicd-acquihire/)，突显了原始模型能力以多快的速度超越了既定的开发者工作流，并让团队在企业治理与不断变化的工具之间进行协调。要求 AI 分析基础设施与要求它更改基础设施之间的界限正在消失。

> 要求 AI 分析基础设施与要求它更改基础设施之间的界限正在消失。