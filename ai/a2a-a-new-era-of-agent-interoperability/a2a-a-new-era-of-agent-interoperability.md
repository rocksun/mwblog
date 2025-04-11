<!--
title: Agent2Agent协议(A2A)发布
cover: https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Agent2Agent-Interoperability.2e16d0ba.fill-1200x600.png
summary: 重磅！Google 联合 50+ 伙伴推出 Agent2Agent (A2A) 开放协议，赋能 AI 代理跨平台协作！基于 HTTP、SSE、JSON-RPC 等标准，A2A 旨在实现企业级身份验证和授权，支持长时间任务和多种模式，构建更强大、通用的 Agent 系统，加速企业 AI 应用落地！
-->

重磅！Google 联合 50+ 伙伴推出 Agent2Agent (A2A) 开放协议，赋能 AI 代理跨平台协作！基于 HTTP、SSE、JSON-RPC 等标准，A2A 旨在实现企业级身份验证和授权，支持长时间任务和多种模式，构建更强大、通用的 Agent 系统，加速企业 AI 应用落地！

> 译自：[Announcing the Agent2Agent Protocol (A2A)](None)
> 
> 作者：Rao Surapaneni; Miku Jha; Michael Vakoc; Todd Segal

2025年4月9日

## 代理互操作性的新时代

AI 代理提供了一个独特的机会，通过自主处理许多日常重复或复杂的任务来帮助人们提高工作效率。如今，企业越来越多地构建和部署自主代理，以帮助扩展、自动化和增强整个工作场所的流程——从订购新笔记本电脑，到协助客户服务代表，再到协助供应链规划。

为了最大限度地发挥代理 AI 的优势，至关重要的是，这些代理能够在动态的、多代理的生态系统中跨孤立的数据系统和应用程序进行协作。即使代理是由不同的供应商构建的或在不同的框架中构建的，也能够实现代理之间的互操作性，这将提高自主性并成倍地提高生产力，同时降低长期成本。

**今天，我们推出了一个新的开放协议，名为 Agent2Agent (A2A)，得到了 50 多家技术合作伙伴的支持和贡献**，如 Atlassian、Box、Cohere、Intuit、Langchain、MongoDB、PayPal、Salesforce、SAP、ServiceNow、UKG 和 Workday；以及领先的服务提供商，包括 Accenture、BCG、Capgemini、Cognizant、Deloitte、HCLTech、Infosys、KPMG、McKinsey、PwC、TCS 和 Wipro。A2A 协议将允许 AI 代理相互通信，安全地交换信息，并在各种企业平台或应用程序之上协调行动。我们相信 A2A 框架将为客户增加显著价值，他们的 AI 代理现在将能够在整个企业应用程序领域中工作。

这种协作努力标志着一个共同的愿景，即无论底层技术如何，AI 代理都可以无缝协作，以自动化复杂的企业工作流程并推动前所未有的效率和创新水平。

A2A 是一个开放协议，是对 Anthropic 的模型上下文协议 (MCP) 的补充，后者为代理提供了有用的工具和上下文。借鉴 Google 在扩展代理系统方面的内部专业知识，我们设计了 A2A 协议，以解决我们在为客户部署大规模多代理系统时发现的挑战。A2A 使开发人员能够构建能够与使用该协议构建的任何其他代理连接的代理，并为用户提供了灵活地组合来自各种提供商的代理的能力。至关重要的是，企业可以从一种标准化方法中受益，该方法用于跨各种平台和云环境管理其代理。我们相信这种通用的互操作性对于充分实现协作 AI 代理的潜力至关重要。

![](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image1_yEPzdSr.original.png)

## A2A 设计原则

A2A 是一个开放协议，它提供了一种标准的代理之间协作方式，而不管底层框架或供应商如何。在与我们的合作伙伴设计协议时，我们坚持了五个关键原则：

- **拥抱代理能力**：A2A 专注于使代理能够以其自然的、非结构化的模式进行协作，即使它们不共享内存、工具和上下文。我们正在实现真正的多代理场景，而不会将代理限制为“工具”。
- **建立在现有标准之上**：该协议建立在现有的、流行的标准之上，包括 HTTP、SSE、JSON-RPC，这意味着它更容易与企业每天已经使用的现有 IT 堆栈集成。
- **默认安全**：A2A 旨在支持企业级身份验证和授权，并在发布时与 OpenAPI 的身份验证方案保持对等。
- **支持长时间运行的任务**：我们将 A2A 设计为灵活的，并支持各种场景，在这些场景中，它可以出色地完成从快速任务到可能需要数小时甚至数天（当有人参与时）的深入研究的所有任务。在整个过程中，A2A 可以向其用户提供实时反馈、通知和状态更新。
- **模式不可知**：代理世界不仅限于文本，这就是为什么我们将 A2A 设计为支持各种模式，包括音频和视频流。

## A2A 的工作原理

A2A 促进了“客户端”代理和“远程”代理之间的通信。客户端代理负责制定和传达任务，而远程代理负责执行这些任务，以尝试提供正确的信息或采取正确的行动。这种交互涉及几个关键功能：

- **能力发现**：代理可以使用 JSON 格式的“代理卡”来宣传其能力，从而允许客户端代理识别可以执行任务的最佳代理，并利用 A2A 与远程代理进行通信。
- **任务管理**：客户端和远程代理之间的通信面向任务完成，代理在其中努力完成最终用户的请求。这个“任务”对象由协议定义，并且具有生命周期。它可以立即完成，或者对于长时间运行的任务，每个代理都可以进行通信，以与彼此保持同步，了解完成任务的最新状态。任务的输出称为“工件”。
- **协作：** 智能体可以相互发送消息，以传递上下文、回复、工件或用户指令。
- **用户体验协商：** 每条消息都包含“部件”，这是一个完全形成的内容片段，例如生成的图像。每个部件都有指定的内容类型，允许客户端和远程智能体协商所需的正确格式，并明确包括用户 UI 功能的协商——例如，iframe、视频、Web 表单等。

请参阅我们的[草案规范](https://github.com/google/A2A)，了解协议如何运作的完整详细信息。

## 一个真实的例子：候选人招聘

通过 A2A 协作，可以大大简化招聘软件工程师的过程。在像 Agentspace 这样的统一界面中，用户（例如，招聘经理）可以指示其智能体查找符合职位列表、地点和技能要求的候选人。然后，该智能体与其他专业智能体交互，以寻找潜在的候选人。用户收到这些建议后，可以指示其智能体安排进一步的面试，从而简化候选人搜寻流程。面试过程完成后，可以聘请另一个智能体来协助进行背景调查。这只是 AI 智能体需要跨系统协作以寻找合格求职者的一个例子。

## 智能体互操作性的未来

A2A 有潜力开启智能体互操作性的新时代，促进创新并创建更强大、更通用的智能体系统。我们相信，该协议将为智能体可以无缝协作以解决复杂问题并改善我们生活的未来铺平道路。

我们致力于与我们的合作伙伴和社区合作，以开放的方式构建该协议。我们将以开源方式发布该协议，并建立明确的贡献途径。

查看[完整规范草案](https://github.com/google/A2A)，试用代码示例，并在 [A2A 网站](https://google.github.io/A2A)上查看示例场景，并了解如何参与贡献。

我们正在与合作伙伴合作，于今年晚些时候推出该协议的生产就绪版本。

## 来自我们 A2A 合作伙伴的反馈

我们很高兴拥有一个不断壮大且多元化的合作伙伴生态系统，他们积极为 A2A 协议及其技术规范的定义做出贡献。他们的见解和专业知识对于塑造 AI 互操作性的未来至关重要。

以下是我们的一些主要合作伙伴对 A2A 协议的评价：

### 技术与平台合作伙伴

**ask-ai.com**

> Ask-AI 很高兴与 Google 合作开发 A2A 协议，塑造 AI 互操作性和无缝智能体协作的未来，从而提升其在企业 AI 客户体验领域的领导地位。
>
> – CEO Alon Talmor PhD

**Atlassian**

> 凭借 Atlassian 对 Rovo 智能体的投资，像 A2A 这样的标准化协议的开发将帮助智能体成功地发现、协调和推理彼此，从而实现更丰富的授权和大规模协作形式。
>
> – Brendan Haire VP, Engineering of AI Platform. Atlassian

**Articul8**

> 在 Articul8，我们认为 AI 必须协作和互操作才能真正跨企业扩展。我们很高兴支持 A2A 互操作性协议的开发——该计划与我们提供跨复杂系统和工作流程无缝运行的特定领域 GenAI 功能的使命完美契合。我们正在使 Articul8 的 ModelMesh（“智能体中的智能体”）将 A2A 视为一等公民，从而实现智能智能体之间的安全、无缝通信。
>
> –Arun Subramaniyan, Founder & CEO of Articul8

**Arize AI**

> Arize AI 很荣幸与 Google 合作，成为 A2A 互操作性协议的启动合作伙伴，从而推进跨 AI 智能体的无缝、安全交互，这是 Arize 对开源评估和可观测性框架承诺的一部分。
>
> – Jason Lopatecki, Cofounder & CEO, Arize AI

**BCG**

> BCG 帮助重新设计以智能为核心的组织。像 A2A 这样开放和可互操作的功能可以加速这一进程，从而实现可持续的、自主的竞争优势。
>
> –Djon Kleine, Managing Director & Partner at BCG

**Box**

> 我们期待扩大与 Google 的合作，使 Box 智能体能够使用 A2A 与 Google Cloud 的智能体生态系统协同工作，共同创新以塑造 AI 智能体的未来，同时使组织能够更好地自动化工作流程、降低成本并生成值得信赖的 AI 输出。
>
> – Ketan Kittur, VP Product Management, Platform and Integrations at Box

**C3 AI**

> 在 C3 AI，我们认为开放、可互操作的系统是使企业 AI 发挥作用并在现实世界中交付价值——A2A 有潜力帮助客户打破孤岛，并安全地使 AI 智能体跨系统、团队和应用程序协同工作。
>
> –Nikhil Krishnan - C3 AI SVP and Chief Technology Officer, Data Science

**Chronosphere**

> A2A 将支持可靠且安全的 Agent 专业化和协调，为计算编排的新时代打开大门，使公司能够更快、更可靠地交付产品和服务，并使他们能够将工程工作重点放在推动创新和价值上。
> – Rob Skillington, Founder /CTO

**Cohere**

> 在 Cohere，我们正在构建企业采用自主 Agent 所需的安全 AI 基础设施，而开放的 A2A 协议可确保无缝、可信的协作——即使在气隙环境中——以便企业能够大规模创新，而不会影响控制或合规性。
> – Autumn Moulder, VP of Engineering at Cohere

**Confluent**

> A2A 使智能 Agent 能够建立直接的实时数据交换，简化复杂的数据管道，从根本上改变 Agent 的通信方式并促进决策。
> – Pascal Vantrepote, Senior Director of Innovation, Confluent

**Cotality (formerly CoreLogic)**

> A2A 为智能、实时通信和协作的新时代打开了大门，Cotality 将其带给家庭贷款、保险、房地产和政府领域的客户——帮助他们提高生产力，加快决策速度。
> – Sachin Rajpal, Managing Director, Data Solutions, Cotality

**DataStax**

> DataStax 很高兴能成为 A2A 的一部分，并探索它如何支持 Langflow，这代表着朝着真正可互操作的 AI 系统迈出的重要一步，这些系统可以协作完成跨多个环境的复杂任务。
> – Ed Anuff, Chief Product Officer, DataStax

**Datadog**

> 我们很高兴看到 Google Cloud 推出 A2A 协议，以简化复杂 Agent 系统的开发，这将帮助 Datadog 使其用户能够构建更具创新性、优化性和安全性的 Agent AI 应用程序。
> – Yrieix Garnier, VP of Product at Datadog

**Elastic**

> 为了支持开放、可互操作的 Agent 生态系统的愿景，Elastic 期待与 Google Cloud 和其他行业领导者合作开发 A2A，并提供其数据管理和工作流程编排经验来增强该协议。
> – Steve Kearns, GVP and GM of Search, Elastic

**GrowthLoop**

> A2A 有潜力加速 GrowthLoop 为我们的客户实现复合营销的愿景——使我们的 AI Agent 能够与其他专业 Agent 无缝协作，更快地从企业数据中学习，并快速优化整个营销生态系统中的活动，同时尊重客户云基础设施上的数据隐私。
> – Anthony Rotio, Chief Data Strategy Officer, GrowthLoop

**Harness**

> Harness 很高兴支持 A2A，并致力于通过将 AI 驱动的智能集成到软件生命周期的每个阶段来简化开发人员体验，从而使团队能够从运行时数据中获得更深入的见解，自动化复杂的工作流程并提高系统性能。
> – Gurashish Brar, Head of Engineering at Harness.

**Incorta**

> Incorta 很高兴支持 A2A 并推进客户的 Agent 通信，使企业自动化的未来更智能、更快且真正以数据驱动。
> – Osama Elkady CEO Incorta

**Intuit**

> Intuit 坚信，像 A2A 这样的开源协议将支持复杂的 Agent 工作流程，加速我们的合作伙伴集成，并通过有效协作的跨平台 Agent 推动行业发展。
> – Tapasvi Moturu, Vice President, Software Engineering for Agentic Frameworks, at Intuit

**JetBrains**

> 我们很高兴成为 A2A 的启动合作伙伴，这是一项增强 Agent 协作并使我们更接近真正的多 Agent 世界的计划，从而增强了 JetBrains IDE、团队工具和 Google Cloud 中的开发人员的能力。
> – Vladislav Tankov, Director of AI, JetBrains

**JFrog**

> JFrog 很高兴加入 A2A 协议，我们认为该协议将有助于克服当今的许多集成挑战，并将成为下一代 Agent 应用程序的关键驱动力。
> – Yoav Landman, CTO and Co-founder, JFrog

**Kolena**

> A2A 是朝着充分发挥 AI Agent 潜力迈出的关键一步，它支持 AI 能够真正增强人类能力、自动化复杂工作流程并推动创新的未来。
> – Manu Sharma Founder & CEO

**LangChain**

> LangChain 认为 Agent 与其他 Agent 交互是指日可待的未来，我们很高兴与 Google Cloud 合作，提出一个满足 Agent 构建者和用户需求的共享协议。
> – Harrison Chase Co-Founder and CEO at LangChain

**MongoDB**

> 通过将 MongoDB 强大的数据库基础设施和混合搜索功能与 A2A 和 Google Cloud 的前沿 AI 模型相结合，企业可以释放零售、制造等行业的新可能性，从而重新定义 AI 应用程序的未来。
> – Andrew Davidson, SVP of Products at MongoDB

**Neo4j**

> Neo4j 很荣幸与 Google Cloud 合作，将我们的图技术知识图谱和 GraphRAG 功能与 A2A 相结合，以帮助组织释放新的自动化和智能水平，同时确保 Agent 交互在上下文中保持相关、可解释和值得信赖。
> – Sudhir Hasbe, Chief Product Officer at Neo4j

**New Relic**

> 我们相信，Google Cloud 的 A2A 协议与 New Relic 的智能可观测性平台之间的协作，将通过简化集成、促进跨不同系统的数据交换，并最终创建一个更统一的 AI 代理生态系统，为我们的客户提供显著价值。
> – Thomas Lloyd, Chief Business and Operations Officer, New Relic

**Pendo**

> 我们很荣幸能与 Google Cloud 的 A2A 协议合作，这将是使 AI 代理能够有效协同工作，同时保持大规模信任和可用性的关键一步。
> – Rahul Jain, Co-founder & CPO at Pendo

**PayPal**

> PayPal 支持 Google Cloud 的 A2A 协议，这代表着开发人员和商家创建由代理 AI 驱动的下一代商业体验的新方式。
> – Prakhar Mehrotra, SVP & Head of Artificial Intelligence at PayPal

**SAP**

> SAP 致力于与 Google Cloud 和更广泛的生态系统合作，通过 A2A 协议塑造代理互操作性的未来——这是使 SAP Joule 和其他 AI 代理能够跨企业平台无缝工作，并释放端到端业务流程的全部潜力的关键一步。
> – Walter Sun, SVP & Global Head of AI Engineering

**Salesforce**

> Salesforce 正在率先支持 A2A 标准，以扩展我们的开放平台，使 AI 代理能够在 Agentforce 和其他生态系统中无缝协作，将脱节的功能转化为精心设计的解决方案，并为客户和员工提供增强的数字化劳动力。
> – Gary Lerhaupt, VP Product Architecture

**ServiceNow**

> ServiceNow 和 Google Cloud 正在合作，为代理间互操作性设定新的行业标准，我们相信 A2A 将为更高效和互联的支持体验铺平道路。
> – Pat Casey, Chief Technology Officer & EVP of DevOps, ServiceNow

**Supertab**

> 借助 Google Cloud 的 A2A 协议和 Supertab Connect，代理将能够像人类企业一样支付、收取和交换服务。
> – Cosmin Ene, Founder of Supertab

**UKG**

> 我们 UKG 很高兴与 Google Cloud 合作开发新的 A2A 协议，该框架将使我们能够构建更智能、更具支持性的人力资本和劳动力体验，以前所未有的方式预测和响应员工需求。
> – Eli Tsinovoi, Head of AI at UKG

**Weights & Biases**

> Weights & Biases 很荣幸与 Google Cloud 合作开发 A2A 协议，该协议设定了一个关键的开放标准，使组织能够自信地部署、协调和扩展各种 AI 代理，而无需考虑底层技术。
> – Shawn Lewis, CTO and co-founder at Weights & Biases

### 服务合作伙伴

**Accenture**

> Google Cloud 的多代理 A2A 协议是将跨不同平台的特定领域代理连接起来以解决复杂挑战的桥梁，从而实现无缝通信和集体智能，以实现更智能和有效的代理解决方案。
> – Scott Alfieri, AGBG Global lead, Accenture

**Deloitte**

> 代理间互操作性是实现代理 AI 架构演进的基础要素，Google Cloud 发起的 A2A 倡议将技术行业参与者聚集在一起，共同开发和支持该协议，将极大地加速代理 AI 的采用。
> – Gopal Srinivasan, Deloitte

**EPAM**

> 我们已经在 A2A 领域处于领先地位，专注于提供真正的商业价值的行业解决方案——节省时间、减少管理费用，并帮助我们的客户推动收入和增强流程，例如药物发现过程中 FDA 文件的开发。
> – Marc Cerro, VP of Global Google Cloud Partnership at EPAM

**HCLTech**

> HCLTech 处于代理企业的前沿，我们很荣幸与 Google Cloud 合作，通过开放的 A2A 标准定义代理间互操作性并推进代理 AI 的可能性。
> – Vijay Guntur, Chief Technology Officer and Head of Ecosystems, HCLTech

**KPMG**

> 在 KPMG，我们很高兴能参与这项新兴计划，因为 A2A 提供了不同 AI 代理真正有效和负责任地协作所需的基本标准，这将使客户和企业能够无缝地利用 AI 来实现创新和效率提升。
> – Sherif AbdElGawad, Partner, Google Cloud & AI Leader, KPMG

**Quantiphi**

> 代理动态发现跨平台功能并构建用户体验的能力对于释放企业的真正潜力至关重要。我们认为 A2A 协议是支持企业构建此类可互操作代理的关键一步。
> – Asif Hasan, Co-founder of Quantiphi

**TCS (Tata Consultancy Services)**

> A2A 协议是代理自动化下一个时代的基础，语义互操作性将在其中占据突出地位，我们很荣幸能够引领这一变革之旅。
> – Anupam Singhal, President, Manufacturing business, Tata Consultancy Services (TCS)

**Wipro**

> 因为 AI 的未来在于无缝协作，所以像 A2A 这样的开放协议将成为 AI 代理大规模推动创新的生态系统的基础。
> – Nagendra P Bandaru，管理合伙人兼全球主管 – 技术服务 (Wipro)

## 了解更多关于 A2A 的信息

要了解更多关于 A2A 框架的信息，请深入研究[完整规范草案](https://github.com/google/A2A)并探索。

我们鼓励您通过[提交想法](https://docs.google.com/forms/d/e/1FAIpQLScS23OMSKnVFmYeqS2dP7dxY3eTyT7lmtGLUa8OJZfP4RTijQ/viewform)、[贡献文档](https://github.com/google/A2A/blob/main/CONTRIBUTING.md)以及与社区互动，为协议的演进做出贡献，并帮助我们定义 Agent 互操作性的未来。