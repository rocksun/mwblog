Amazon Web Services (AWS) 正在[揭开](https://strandsagents.com/blog/introducing-strands-harness/)一款全新开源通用 AI 代理的神秘面纱，旨在为开发者提供一个可本地运行或部署到云端的现成基础。

这款名为 [Strands Harness](https://strandsagents.com/docs/user-guide/harness/) 的工具，建立在 AWS 于 [2025 年 5 月推出](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)的开源 Python SDK——[Strands Agents](https://github.com/strands-agents/) 基础之上，用于构建 AI 代理。Strands 采用了 AWS 所称的“模型驱动方法”：开发者提供模型、工具和指令，而模型决定如何处理任务以及何时调用这些工具。AWS 后来[将 Strands 引入 TypeScript](https://strandsagents.com/blog/strands-agents-typescript-v1/)，并于 2 月份[创建了 Strands Labs](https://thenewstack.io/aws-strands-labs-launch/)，作为更多实验性项目的独立孵化基地。

AWS 副总裁兼杰出工程师 [Marc Brooker](https://www.linkedin.com/in/marc-brooker-b431772b/) 告诉 *The New Stack*，Strands Harness 本质上位于[现有 Strands SDK](https://github.com/strands-agents/harness-sdk) 之上，为开发者提供了一个预配置的 Strands Agent。它汇集了代理在处理长期运行任务时所需的工具和配套设施，并由 AWS 为这些组件的协同工作提供默认设置。

> “你仍然需要决定如何管理上下文、持久化对话、集成工具以及引导代理的行为。”

“像 Strands Harness SDK 这样的工具包为你提供了构建模块，但你仍然需要决定如何管理上下文、持久化对话、集成工具以及引导代理的行为，”Brooker 解释道。

## 解构 Strands Harness

开箱即用，Strands Harness 为开发者提供了一个功能完备的代理，具备文件、Shell 和 Web 工具，并内置了对上下文、内存、持久会话、提示词缓存以及向其他代理委派任务的处理能力。

开发者可以通过 `pip install strands-harness` 或 `npm install @strands-agents/harness` 将 Strands Harness 安装为 Python 或 TypeScript 包。

AWS 还提供了 Strands CLI，作为原型设计和配置代理的交互式方式。开发者可以选择模型、添加提示词、工具和其他功能，然后使用 `/export` 将生成的代理导出为 Python 或 TypeScript 代码。

![使用 Strands CLI 配置代理。](https://cdn.thenewstack.io/media/2026/09/f7835bc7-giffy2.gif)

*使用 Strands CLI 配置代理。*

单个代理可以根据不同的工作进行定制，开发者可以更改其指令、选择使用的模型、控制其可用的工具和功能，并决定是否可以将工作移交给另一个代理。

![Strands Harness 在桌面上运行的演示](https://cdn.thenewstack.io/media/2026/09/2baca1eb-giffy.gif)

*Strands Harness 在桌面上运行的演示 (图片来源: AWS)*

Strands Harness 的大部分功能并不依赖 AWS 基础设施。代理循环、工具、上下文管理、会话处理和委派功能都包含在开源版本中，AWS 表示这些流程默认在运行代理的机器上执行。

唯一的例外是对底层模型的调用。不出所料，AWS 通过其用于访问和运行基础模型的托管服务 [Amazon Bedrock](https://thenewstack.io/mcp-summit-aws-bedrock/) 路由模型访问。然而，虽然 Brooker 表示这是唯一与 AWS 基础设施特别绑定的开箱即用默认设置，但它也可以被替换。

“只需一行代码，就可以轻松覆盖它以使用其他模型提供商，”他说。

Strands Harness 可以使用 Anthropic、OpenAI 或 Google 作为模型提供商，也可以通过 [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 使用本地运行的模型。更换提供商并不一定意味着更换底层模型，但 Brooker 指出，选择不同的模型显然会影响代理的行为。

“不同的模型在推理、工具使用和成本方面各有优势，”他继续说道。“不变的是：无论提供商是谁，上下文管理、会话、工具和委派的工作方式都是一样的。没有任何功能需要绑定 Bedrock。”

值得注意的是，所有其他默认设置也可以更改。开发者可以引入自己的工具和技能，连接 MCP 服务器，改变上下文处理方式，并选择会话状态的存储位置。

> “开发者可以专注于应用程序的任务和领域专业知识，同时自定义需要不同行为的组件。”

“开发者可以专注于应用程序的任务和领域专业知识，同时自定义需要不同行为的组件，”Brooker 说。

## AWS 对其代理进行的基准测试

AWS 表示，Strands Harness 的定位是通用代理，而不是编码助手，尽管它从 Claude Code 和 Codex 等工具中汲取了灵感。AWS 表示，区别在于开发者可以将 Strands Harness 部署到他们选择的任何云提供商——解决了 Claude Code 和 Codex 用户普遍希望能在云端运行相同设置的需求。

根据其内部测试，AWS 表明，即便底层模型相同，代理处理周围配套设施的方式也会显著影响成本和性能。对于每个工具，AWS 在六个基准测试（ALFWorld、ContextBench、GAIA、WebShop、τ³-bench 和 Terminal-Bench 2.1）中对其得分进行了平均，并比较了这些测试中的平均单任务成本。公司表示，与 Claude Code 和 Codex 相比，Strands Harness 的成本降低了 45%，且准确率大体相当。

然而，一旦纳入 [DeepSeek Harness](https://thenewstack.io/deepseek-harness-open-source-plugins/)——AWS 称其在匹配运行中比 Strands Harness 成本低约 14%——这一降幅在更广泛的对比中降至 28%。

![Strands Harness 基准测试结果。](https://cdn.thenewstack.io/media/2026/09/62791a1e-screenshot-2026-09-21-at-18-06-20-introducing-strands-harness-frontier-performance-with-28-lower-token-cost-strands-agents.png)

*Strands Harness 基准测试结果。(图片来源: AWS)*

AWS 特别指出其上下文管理默认设置是取得该结果的主要原因。Strands Harness 会截断特别大的工具输出，在可用窗口超过设定阈值时压缩上下文，并在上下文溢出时尝试在代理循环内恢复。

特别是在 Terminal Bench 2.1 测试中，AWS 表示运行 Fable 5 的 Strands Harness 成本比 Claude Code 低 77%（89 次试验中为 56.29 美元 vs 248.05 美元），得分则为 69.7 vs 61.8。DeepSeek Harness 成本更低，为 40.30 美元，但得分较低，为 59.5。

![Terminal Bench 2.1 结果。](https://cdn.thenewstack.io/media/2026/09/7e38a4c9-screenshot-2026-09-21-at-18-06-29-introducing-strands-harness-frontier-performance-with-28-lower-token-cost-strands-agents.png)

*Terminal Bench 2.1 结果。(图片来源: AWS)*

对于 AWS 而言，这些结果有助于证明封装和调优上下文管理等功能的重要性，而不是要求每个开发者都使用 SDK 独立进行这些决策。

> “让原型工作只是第一步；评估这些选择如何影响性能和成本是另一回事。”

“让原型工作只是第一步；评估这些选择如何影响性能和成本是另一回事，”Brooker 说。“我们看到的机遇是将这些工程工作封装成一个完整的、通用的代理。”

## 对 AWS 有什么好处？

AWS 还有一个运行所得代理的明确去处。[Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) 是其用于部署和操作代理的托管服务，提供身份和访问控制、可观测性以及托管它们所需的基础设施。

事实上，开源项目与该托管产品之间存在着紧密的技术联系。AgentCore Harness 和 Strands Harness 由同一个团队构建，尽管它们位于不同的代码库中。Brooker 表示，一个项目的进展可以为另一个项目提供改进，这为 AWS 提供了一条途径：开源项目中开发的技术可以为托管服务提供参考，反之亦然。

Brooker 再次强调，Strands Harness 可以独立于 AgentCore 部署，甚至完全在 AWS 之外运行。

“对于希望由 AWS 管理基础设施方面的团队来说，AgentCore 是一个可选的托管层，”他说。“然而，所有部署路径都对开发者开放，由他们自行选择。”

尽管如此，这种安排为 AWS 提供了一条清晰的商业路径：开发者可以自由采用 Strands Harness，而 AgentCore 则为那些最终希望由 AWS 管理其基础设施的团队提供了一个自然的目的地。