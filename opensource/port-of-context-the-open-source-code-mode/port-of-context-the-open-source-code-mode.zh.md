[模型上下文协议（MCP）](https://thenewstack.io/why-the-model-context-protocol-won/)已迅速成为连接基于[大型语言模型（LLM）](https://thenewstack.io/introduction-to-llms/)的AI代理与外部数据和工具的广受采纳的标准。

因此，许多开发者在其环境中堆叠了MCP工具。根据2025年末[Zuplo发布的一项研究](https://zuplo.com/mcp-report)，70%的MCP用户配置了2到7个MCP服务器。

但每增加一个MCP都会消耗内存，随着上下文窗口必须存储聊天历史和配置文件，内存资源变得日益稀缺，同时代理会将多个MCP链接成工作流。

在一次[独立实验](https://selfservicebi.co.uk/analytics%20edge/improve%20the%20experience/2025/11/23/the-hidden-cost-of-mcps-and-custom-instructions-on-your-context-window.html)中，微软Power BI咨询公司[One Day BI](https://www.onedaybi.com/)的创始人Mihály Kávási计算得出，在运行任何命令之前，这种“隐性开销”占用了Claude Code中200,000个令牌上下文窗口的51%，其中MCP工具本身消耗了超过16%。

[MCP服务器](https://thenewstack.io/when-is-mcp-actually-worth-it/)的响应大小也可能无法预测，经常会淹没上下文窗口。

“一个响应中可能有数千或数十万个令牌，而且无法提前将其过滤掉，”API文档和工具维护平台[Sideko](https://sideko.dev/)的联合创始人兼首席执行官Patrick Kelly告诉The New Stack。

为了解决这一痛点，MCP的创建者Anthropic推荐一种[代码执行风格](https://www.anthropic.com/engineering/code-execution-with-mcp)，其中代理编写并执行代码来调用工具，而不是直接调用工具。Anthropic声称这种方法可以将令牌使用量减少98.7%。

Cloudflare推出了一项架构相似的功能，即[代码模式](https://blog.cloudflare.com/code-mode/)。这是Cloudflare所描述的“使用MCP的更好方式”这一更广泛的“代码模式”架构方法的一个例子。

“当你构建执行复杂任务的AI代理时，代码模式是使用工具和MCP服务器的最佳方式，”Kelly补充道。

迄今为止，代码模式在很大程度上仍受限于特定供应商。[Port of Context](https://portofcontext.com/)是一个于去年12月开源的项目，旨在通过提供一种与供应商无关且与LLM无关的实现来改变这一现状。

## 什么是代码模式？

代码模式代表了超越直接MCP工具调用的演进，因为如果LLM被自由运行，直接调用可能导致不确定的结果。

相反，代码模式在代理和MCP服务器之间提供了一个更受控制的接口。“它确定性地为每个工具生成函数以及类型化的输入和输出，”Kelly说。

通过预先为代理提供结构化上下文，代码模式使其能够执行脚本来执行工具调用，例如发送电子邮件、共享日历邀请或更新客户关系管理（CRM）表。

这种方法更强调沙盒执行环境，它在构建和启动适当调用时优化了上下文使用。

## 介绍 Port of Context

“Port of Context的目标是让设置、测试代码模式变得非常容易，并使其能够100%在本地与任何AI模型一起运行，”Kelly说。“它是一种具有出色本地开发体验的替代方案。”

Port of Context，或简称pctx，将MCP和工具转换为类型化的沙盒代码。截至撰写本文时，其[GitHub仓库](https://github.com/portofcontext/pctx)已拥有近200颗星和20多个分叉。

Kelly表示，该项目源于与代理构建者反复交流，他们一致指出上下文窗口耗尽是一个长期存在的问题。

Pctx相对容易运行。它作为一个Rust二进制文件发布，不含任何依赖项。你只需安装它，以开发模式运行，并使用命令行界面（CLI）连接并向上游MCP服务器进行身份验证。

该工具随后为代理提供了一个可供引用的URL，以及一个用于管理工具的仪表板。代码执行在一个安全的[Deno JavaScript](https://thenewstack.io/deno-2-arrives-with-long-term-support-node-js-compatibility/)运行时环境中运行，该环境仅有权访问用户明确授予的MCP服务器。

## 独立代码执行层的优势

pctx的主要优势是减少令牌使用量。维护者表示，pctx提供的令牌节省量与Anthropic报告的相似。

另一个优势是工具无关性。Cloudflare的代码模式要求在Cloudflare Workers内部执行，该模式在V8隔离环境中运行代码。Anthropic的方法也类似地依赖于与Claude模型绑定的Python沙盒。

标准化的开源代码模式层允许开发者使用他们选择的任何代理或模型。Pctx还可以取代为防止MCP响应淹没上下文窗口而构建的自定义代码层。

“我认为对这种本地且模型无关的代码模式版本有需求，”Kelly说。然而，维护者已在Anthropic和Cloudflare版本之上添加了功能以保持兼容性。

他们还在创建与[LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)和[CrewAI](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/)等AI代理框架的原生集成。Kelly表示，这将允许开发者在不离开其框架的情况下编写本地函数并注册MCP服务器。

代码模式还可以解锁额外的自动化。“我们认为代码模式将在自动生成和使用MCP服务器方面解锁大量自动化，”Kelly说。

他补充说，如果没有代码模式，从[OpenAPI规范](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/)自动生成MCP服务器可能会失败，如果服务器在设计时没有考虑上下文窗口限制的话。顺序使用10个或更多MCP工具的工作流尤其会堵塞上下文。

最后，由于pctx引入了额外的身份验证层，它还可能在企业场景中（无论内部还是外部）实现对MCP使用的更强治理。

## 早期使用与权衡

Port of Context仍处于早期阶段。尽管兴趣日益增长，但大多数用户仍处于实验阶段。

Kelly表示，部分用户目前正在测试该工具，以减少上下文溢出并取代用于处理MCP响应的自定义代码。

一个特定的早期采用者是[Sentient Foundation](https://sentient.foundation/)，这是一个开源的通用人工智能（AGI）组织。该组织正在其[递归开放元代理](https://github.com/sentient-agi/ROMA)（ROMA）（一个用于协调多个代理间推理的框架）及其其他代理产品中测试pctx。

尽管pctx的早期使用看起来很有前景，但一个潜在的缺点是维护者集中度。虽然pctx是开源的并设计为跨平台工作，但它主要由Sideko维护。

Kelly表示，运行时定制和核心代码模式功能将保持完全开源，但云部署和云身份验证组件将保持闭源。

然而，维护者计划向外部贡献者开放路线图，这可能导致AI构建者开发出新的扩展功能。

最后，pctx——以及更广泛的代码模式变体——不适用于涉及单个工具调用的简单代理场景。“对于非常简单的工具和简单的用例，”Kelly警告说，“它实际上会让你变慢。”

## 下一步：减少MCP工具臃肿

AI代理生态系统正在迅速发展。虽然代码模式技术目前有助于优化MCP使用，但其他策略和标准也可能会出现。

其他优化技术，如[语义缓存](https://thenewstack.io/what-is-semantic-caching/)、减少正在使用的服务器或精简内存状态，也可能带来效果。

总而言之，代码模式和pctx等变体项目的出现，表明MCP的使用量正在上升，以及在实际操作中部署大量MCP所面临的瓶颈。

鉴于效率的提升，开发者应考虑进行此类架构更改。如果基准测试结果准确，这可能意味着在使用MCP时实现有意义的优化。