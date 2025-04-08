<!--
title: 为何云原生基础设施对于GenAI而言不可或缺
cover: https://cdn.thenewstack.io/media/2025/04/4591c32c-mohammad-rahmani-w-lqbauhe64-unsplash-scaled.jpg
summary: GenAI爆火，云原生基础设施成刚需！容器化是黄金标准，微服务架构利于快速迭代。Kubernetes、LangChain等框架崛起，GPU资源需求大。企业需重视平台工程和数据准备，解决技能短缺，拥抱云原生生态，方能决胜GenAI时代！
-->

GenAI爆火，云原生基础设施成刚需！容器化是黄金标准，微服务架构利于快速迭代。Kubernetes、LangChain等框架崛起，GPU资源需求大。企业需重视平台工程和数据准备，解决技能短缺，拥抱云原生生态，方能决胜GenAI时代！

> 译自：[Why Cloud Native Infrastructure Is Non-Negotiable for GenAI](https://thenewstack.io/why-cloud-native-infrastructure-is-non-negotiable-for-genai/)
> 
> 作者：Debojyoti Dutta

在 2025 年初，一些重要的趋势正在塑造着生成式 AI 这个充满活力的领域，其中包括 Agentic AI 的崛起。这项强大的技术提高了 GenAI 在推理、规划和工具使用方面的能力，使 LLM 能够根据它们提出的建议采取行动。与此同时，人们正在对核[能源进行大量投资，以满足数据中心对能源的巨大需求](https://thenewstack.io/how-much-energy-is-really-being-consumed-by-data-centers/)。GenAI 正在成为机器人技术中越来越重要的因素，但同时也日益成为一种网络安全威胁。

然而，在这些引人注目的趋势中，有一个问题更值得关注：需要云原生架构来支持 GenAI 的应用程序。如果没有这些基础，项目的投资回报率可能会远低于预期，甚至更糟，会以失败告终。

挑战已经变得显而易见。[Gartner](https://thejournal.com/articles/2024/08/06/gartner-30-of-gen-ai-projects-will-be-abandoned.aspx?utm_source=chatgpt.com) 预测，到 2025 年底，至少有 30% 的 genAI 项目将在概念验证阶段失败。

为了解决这些问题，构建允许容器化的基础设施至关重要。然而，这[需要一种根据 GenAI 的独特需求量身定制的全新方法](https://thenewstack.io/trust-in-genai-requires-an-open-data-movement-platform/)。另一个挑战是如何吸引、再培训和重新培养团队。

## 容器化是黄金标准

容器化可能看起来是另一个流行语，但它的概念却出奇地简单。它是关于将应用程序的代码及其所有依赖项打包在一起。这使得应用程序可以无缝运行，无论是在云中、私有数据中心还是在边缘设备上。

现代应用程序依赖于复杂的依赖项，从管理身份验证的模块到与 ERP 和 CRM 系统连接的模块。定期的更新和补丁是必不可少的。否则，即使是很小的问题也可能意外地破坏应用程序。

这就是容器化的用武之地。容器化通过允许资源共享（CPU、内存、存储），同时为提高安全性提供隔离，从而[改变软件开发](https://thenewstack.io/ebooks/generative-ai/how-generative-ai-transforms-software-development/)。

容器化对于 GenAI 应用程序来说是必不可少的，这些应用程序通常纠缠在复杂的依赖关系中。通过将应用程序分解为微服务（独立的、可测试的组件），开发人员可以快速迭代、有效地扩展和灵活地部署。

这种趋势并没有被忽视。[最近的研究](https://www.nutanix.com/enterprise-cloud-index)强调了容器采用率的激增，部分原因是 GenAI 的需求。该报告显示，近 90% 的组织报告说，他们至少有一些应用程序现在已经容器化，而且随着 GenAI 等新应用程序工作负载的快速采用，这个数字预计还会增长。然而，64% 的组织发现[云原生和容器应用程序开发](https://thenewstack.io/simplifying-cloud-native-application-development-with-ballerina/)具有挑战性。

## GenAI 世界的现代基础设施

传统的[软件开发遵循高度结构化的](https://thenewstack.io/pythons-collection-module-for-specialized-data-structures/)过程。关键步骤包括需求分析、系统设计、编码、调试、代码审查和部署。这是一个经过时间考验的过程，经过了几十年的改进。但是，当应用于 GenAI 应用程序时，这本剧本就开始崩溃了。这主要是由于 AI 开发的独特方面，例如清理数据、微调和检索增强生成 (RAG)。

基础设施的需求也并不容易。训练和部署这些模型通常需要 GPU 密集型环境，这会增加成本。然后是多个 AI 模型的编排。当然，Kubernetes 长期以来一直是开发人员的最爱，但在过去几年中，LangChain、AutoGen 和 CrewAI 等新框架已经出现。

灵活性是另一个难题。GenAI 应用程序需要无缝地融入云原生生态系统和容器化环境。根据 ECI 调查，超过 80% 的受访者将基础设施现代化列为首要任务。

## 解决技能差距

GenAI 正在造成巨大的技能缺口。ECI 的一项研究（包括 IT 和 DevOps 部门的 C 级决策者）显示，只有 21% 的受访者认为他们的组织具备支持 GenAI 应用程序和基础设施所需的技能。额外的人手不易获得，而且成本很高。

GenAI 专家通常是这些 AI 项目的最终用户和客户，他们不能或不想管理 GenAI 的交付方式。重点培养内部在[平台工程和数据](https://thenewstack.io/50-of-engineers-lack-trust-in-the-data-they-rely-on-most/)准备方面的专业知识，并利用简单但功能强大的企业级工具。好消息是，有很多培训资源，从在线课程到强化训练营。

## 结论

GenAI 蓄势待发，将重塑许多行业，但其成功依赖于一些关键因素：容器化、现代化的基础设施以及一支掌握 GenAI 需求的熟练劳动力。这些不仅仅是待办事项清单上的复选框。它们是可扩展性、效率和适应性的支柱。能够正确理解这一点的企业公司将把今天的挑战转化为明天的机遇，并为可持续的、面向未来的增长铺平道路。