**薪酬与人力资源数据平台Workday** 涉足AI与代理技术已有时日。然而，与其他业务领域可能容许些许失误不同，在Workday中，薪酬发放必须保证99%的准确率，而这还远不够好。

Workday首席技术官 [Gabe Monroy](https://www.linkedin.com/in/gabemonroy) 告诉 *The New Stack*，企业级AI必须跨越这道门槛，才会被允许接触其人力资源和财务数据。

“在处理人员和资金的系统中，很少有比这更关键、也更不可容忍错误的系统了，”他说。Monroy在采访中表示，这里没有“大部分时间都能正常工作”的容忍度。

在六月初举行的 [DevCon 开发者大会](https://blog.workday.com/en-us/workday-devcon-2026-going-agentic-building-future.html) 上，Workday阐述了其跨越这一正确性门槛的计划。该公司推出了 [Agent-Ready Tools](https://newsroom.workday.com/2026-06-02-Workday-Launches-New-Tools-for-Developers-to-Build,-Connect,-and-Verify-AI-Agents-For-HR,-Finance,-and-IT)，这是一套连接器，允许代理通过模型上下文协议（MCP）在整个平台上执行操作；推出了一个让人们能以自然语言在Workday上构建应用和代理的开发者代理（Developer Agent）；以及 [Agent Passport](https://newsroom.workday.com/2026-06-02-Workday-Launches-Agent-Passport-to-Test,-Verify,-and-Continuously-Monitor-Every-AI-Agent-in-the-Enterprise)，用于在代理进入生产环境前进行测试与验证，并在之后持续进行监控，其中Cisco是首个认证合作伙伴。

## 护栏属于推理引擎

Monroy职业生涯的大部分时间都在基础设施和开发者领域度过：曾先后任职于 Deis、Microsoft、DigitalOcean，最近的一份工作是在Google。在Google，他专注于为大型AI实验室构建可扩展的推理基础设施。对于一个如此专注于基础设施的人来说，来到Workday可能看起来有些奇怪，但Monroy认为，在这一点上，LLM（大语言模型）安全是——或者至少应该是——企业核心基础设施的一部分。

> “在人员和资金的世界里……赌注更高”

“在Workday的世界里，在人员和资金的世界里，赌注更高，这也是我非常兴奋能在Workday专门解决的问题——我确实将其视为核心基础设施，”他说。“我最近做的大部分工作是为大型AI实验室构建可扩展的推理基础设施，你会很快发现推理是概率性的。

“（推理）涉及预填充（prefill）和解码（decode），以及一整套真正用来向终端用户流式传输Token的技术机器，但目前在这个技术栈中，根本没有原生LLM级强制护栏的概念——即作为核心推理一部分的护栏。”

在他看来，要让企业安全地进行大规模推理操作，必须在推理引擎层完成。他认为，在模型外部封装模型的那种代理网关或类似的附加组件，其所在层级是错误的。

![](https://cdn.thenewstack.io/media/2026/06/6858d517-1634663536418.jpeg)

Workday CTO Gabe Monroy

对于像Workday这样的记录系统，系统必须严格执行关于用户身份、预算权限以及其在组织架构中位置的护栏。Monroy说，这些约束可以被深深植入到推理中，而不是事后才去检查。“这些是我们有机会在非常、非常低的层级上将其深度植入推理中的内容，这种方式能产生更安全的结果，”他说。

Workday最近 [对 Pipedream 的收购](https://newsroom.workday.com/2025-11-19-Workday-Signs-Definitive-Agreement-to-Acquire-Pipedream) 在一定程度上印证了这一点。有了 Pipedream，代理可以触达Workday之外的第三方系统，例如从Google Drive拉取政策文档，平台随后可以验证该特定代理是否具备执行此操作所需的所有访问权限。

## “带到我们的店里来”

当然，所有这些代理都需要被管理。尽管许多SaaS公司目前正在 [构建自己的代理平台和代理编排服务](https://thenewstack.io/sap-ai-agent-hub/)，并且看起来都在提供相同的服务，但Monroy认为，编排应该在靠近数据源的地方进行。

“如果你想运行一个与人员和资金集成的代理交互，那么编排循环可能应该发生在更靠近Workday的地方，理想情况下是在Workday平台上，”他说。“我确实认为推理引擎靠近底层系统是有道理的，因为从低级推理引擎和运行时的角度来看，你在推理引擎层可以做一些差异化的事情，而这些事情只有在靠近底层系统时才有可能实现。”

> “我确实认为推理引擎靠近底层系统是有道理的……”

他将其比作汽车修理。如果有人递给你一个工具箱，你可能修得好，也可能修不好。“也许你能得到结果，但我告诉你，如果你真的想让你的车修好，带到我们的店里来。我们有液压升降机，我们有受过培训的工程师知道怎么做这些事，而且我们有工具——我们的工具是业内最好的。”

对于代理编排循环中必须在人力资源和财务数据旁运行的部分，“你真的应该在我们的店里运行它。”

不过，对于更通用的工作流，他认为通用平台也有存在的空间。毕竟，并非所有事情都需要在Workday上运行，Workday确实提供了MCP服务器，第三方工具也可以接入这些服务器以访问其数据和工具。

在某种程度上，每个记录系统供应商目前都在提出某种版本的 [邻近性和上下文论点](https://thenewstack.io/sap-sapphire-ai-context/)。毕竟，拥有AI代理工作的上下文对这些公司来说是一个 [巨大的护城河](https://thenewstack.io/hyland-enterprise-context-engine-agents/)，即使API和MCP服务器允许代理跨供应商获取数据。

与此同时，还有一群其他公司将自己定位为中立第三方，受益于这些供应商现在向第三方代理开放平台的事实。从长远来看，企业似乎不太可能想要管理多个代理平台，但在这一点上，钟摆将向哪个方向摆动仍远未明确。

如果邻近性是Workday认为可以胜出的地方，那么公司有一个不想参与竞争的领域：开发者工具。

“我们不会靠为开发者构建更好的工具来让Workday实现差异化，”Monroy说。“我们将通过安全性、信任感和推理引擎来实现差异化。”一个值得注意的事实是，DevCon上的演示是在 Claude Code、Cursor、OpenAI的 Codex 和 Google 的 Antigravity 上运行的，而不是在任何Workday品牌的工具上。“在工具方面，我很乐意使用 Claude Code、Codex 等工具，”他说。

众所周知，目前 [开发者对AI工具的忠诚度并不存在](https://thenewstack.io/github-wants-developers-back/)。开发者绝对不想要单一供应商的一次性工具，Monroy也指出他不会要求他们采用这种工具。相反，Workday想要拥有技能（skills），他将其称为“我们用来在系统中进行融合的底层通用语言”。

Workday很高兴成为其垂直领域的记录系统，并让其他人去争夺工具市场。"}
}
    }
  }
}
]