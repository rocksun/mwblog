Ramp 花费了数月时间测试托管智能体 API、开源框架和第三方平台，最终得出结论：自己动手构建会更好。其成果便是 Laminar，这是一个内部智能体底座，仅用六周时间就推出了第一个版本，现在为这家金融科技公司的所有智能体产品提供支持。

> “我们研究了市场上的其他产品，认为通过内部构建，我们可以做得更好、行动更快，并且与我们想要发展的方向保持更强的一致性。”

平台背后的 Ramp 工程师 [Sam Kronick](https://www.linkedin.com/in/sam-kronick-534075117/) 在公司的[工程博客](https://builders.ramp.com/post/building-laminar)中写道：“我们研究了市场上的其他产品，认为通过内部构建，我们可以做得更好、行动更快，并且与我们想要发展的方向保持更强的一致性。”

在周二发布的一篇文章中，Ramp 详细介绍了 Laminar 如何将智能体执行、沙盒隔离、可观测性和异步工作流整合到一个单一平台中。这种架构引起了 LangChain 首席执行官 [Harrison Chase](https://www.linkedin.com/in/harrison-chase-961287118/) 的注意，他在其 [X 帖子](https://x.com/hwchase17/status/2112650555852275951)中赞扬了几个设计选择，同时指出了 [LangChain 的 Deep Agents](https://github.com/langchain-ai/deepagents) 中正在进行的类似工作。

Ramp 和 LangChain 正从不同的方向解决这个问题，但两者都指向了[智能体基础设施](https://thenewstack.io/kubecon-agent-harness-koordinator/)中更大的转变。随着底座承担更多的责任，企业必须决定他们想要自己构建和维护多少基础设施。

## Ramp 为什么选择自研

Ramp 不想被锁定在单一的模型提供商上。它需要根据成本、速度和性能灵活切换模型的灵活性，以及更好地了解智能体的行为方式。工程师们已经需要翻阅追踪日志来寻找不必要的工具调用、臃肿的上下文和错误，但现有的可观测性工具让这项工作变得比实际需要的更加困难。因此，Ramp 在 Laminar 中构建了自己的调试界面。将开发保留在内部还意味着底座团队可以直接与产品工程师合作，而不必等待供应商做出更改。

Chase 赞同 Ramp 的优先级，特别是模型独立性和可观测性，LangChain 在其自己的工作中也强调了这两点。此外，Laminar 架构的其他部分也引起了他的注意。

> 将开发保留在内部还意味着底座团队可以直接与产品工程师合作，而不必等待供应商做出更改。

## 会话与沙盒分离

Laminar 运行着从客服智能体到公司的云编码智能体 [Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent) 以及处理长期运行的协作工作的 Glass 等各种产品。支持这些产品需要一个能够管理持久会话、人工审批并在不同环境中工作的底座。

Chase 强调了 Kronick 的观察，即生产级底座的作用远不止运行一个简单的执行循环。他在谈到 LangChain 对 Deep Agents 的投资时写道：“[对此 +100](https://x.com/hwchase17/status/2112650555852275951)。”

Ramp 将智能体会话与代码运行的沙盒隔离。对话历史记录和执行状态被独立存储，允许沙盒启动和关闭而不会中断会话。

Chase 将[沙盒即工具的方法](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes)视为一种增长趋势，并指出 Deep Agents 使用了类似的设计。它还将凭据和编排保留在沙盒之外，随着开发人员努力[隔离运行不受信任代码的智能体](https://thenewstack.io/webassembly-sandboxing-ai-agents/)，这是一个重要的考虑因素。

## 默认异步智能体

Laminar 允许智能体继续工作，而无需等待每个步骤完成。Chase 将非阻塞的异步智能体描述为未来，并表示 LangChain 正在为 Deep Agents 开发类似的功能。

Ramp 的连接器服务（Connectors Service）也引起了他的注意。它在共享 API 背后集中了身份验证、凭据、访问控制和工具执行。

Chase 表示，LangChain 正在探索托管 Deep Agents 的可比功能。集中这些功能还为平台团队提供了一个一致的地方来管理访问和凭据处理，而不是为每个智能体单独实现它们。

底座也是团队可以削减推理成本的地方，LangChain 直接提出了这个论点。在 10 月 1 日的一篇[工程文章](https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness)中，它描述了将模型选择转移到其开源编码智能体 [Open SWE](https://github.com/langchain-ai/open-swe) 的底座中。路由器检查初始请求，并根据预期的任务复杂度分配三个模型之一，将最简单的任务发送给 GLM-5.3-Flash，中级任务发送给 GPT-5.6 Sol，最苛刻的请求发送给 GPT-6 Astra。

## 路由削减推理成本

在 973 个智能体线程中，路由器将每个线程的中位 LLM 成本从 2.61 美元降至 0.94 美元，与对每个任务使用 GPT-6 Astra 相比下降了 64%。这种节省并没有带来可测量的性能影响。路由线程的合并拉取请求率为 29.2%，对照组为 27.3%，这一差异在统计上并不显著。百分之九十的请求流向了两个较便宜的模型层。

> LangChain 认为，在底座内部进行路由比在对智能体正在做什么缺乏上下文的通用 LLM 网关中进行路由效果更好。

LangChain 认为，在底座内部进行路由比在[通用 LLM 网关](https://thenewstack.io/respan-rust-ai-gateway/)中进行路由效果更好，后者对智能体正在做的事情缺乏上下文。底座已经知道涉及哪些提示词、工具和领域上下文，从而为其做出该选择提供了更多信息。LangChain 使用[模型选择中间件](https://docs.langchain.com/oss/python/langchain/agents)在每个线程开始时选择模型。

这些结果并未告诉我们构建自定义底座是否比使用现有框架更便宜。Ramp 并没有参与这项实验。但它们确实表明，通过在底座级别做出更聪明的模型选择，公司可以节省多少成本，特别是当他们的智能体处理具有截然不同需求的任务时。

## 底座所有权困境

Ramp 的决定也表明了编码智能体如何改变了基础设施成本。Kronick 表示，智能体生成了 Laminar 的所有初始代码，由经验丰富的工程师指导架构和实现。

但是，在六周内构建第一个版本是一回事。维护它是另一回事。Ramp 仍然需要工程师来处理事故、更新平台并支持其产品团队。该公司还未发布运营成本比较或与竞争平台的基准测试，这使得很难判断自研是否更便宜。

LangChain 提供了另一种选择。公司无需从头开始构建底座，而是可以使用能够处理大部分底层基础设施的框架，随着其他供应商[开源其自己的底座](https://thenewstack.io/aws-strands-harness-agent/)，其他供应商也正在采取这种方法。