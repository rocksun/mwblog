<!--
title: 合约即代码：为什么财务团队正在接管你的API合约
cover: https://cdn.thenewstack.io/media/2025/04/ba305032-hands-2088954_1280.jpg
summary: 🔥告别低效！云原生时代，财务团队接管 API 合同？“合同即代码”颠覆传统！通过 API 将法律文档集成 CI/CD pipeline，CFO 主导云成本优化。AI 合同代理提取关键条款，自动监控 API 速率。打破技术与业务合同壁垒，实现合同全流程自动化！
-->

🔥告别低效！云原生时代，财务团队接管 API 合同？“合同即代码”颠覆传统！通过 API 将法律文档集成 CI/CD pipeline，CFO 主导云成本优化。AI 合同代理提取关键条款，自动监控 API 速率。打破技术与业务合同壁垒，实现合同全流程自动化！

> 译自：[Contract-as-Code: Why Finance Teams Are Taking Over Your API Contracts](https://thenewstack.io/contract-as-code-why-finance-teams-are-taking-over-your-api-contracts/)
> 
> 作者：Matt Lhoumeau

在云原生环境中，我们经常讨论微服务之间的合同如何定义稳定的接口和显式的依赖关系。然而，还有另一种类型的合同同样重要，但很少受到开发人员的关注：业务协议。作为 Concord 的创始人，我观察到，管理着数千个供应商关系的企业，如何努力将这些人为合同集成到其自动化工作流程中，从而为 DevOps 团队造成了严重的瓶颈。

采用 [Kubernetes 和容器化架构](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/) 的组织创建了优雅的系统，其中服务通过定义良好的 API 进行通信。团队为这些交互编写合同，确保在各个组件独立演进时保持稳定的接口。

然而，许多 DevOps 团队正在发现一种隐藏的技术债务：管理这些相同系统的业务合同没有集成到他们的自动化管道中。[World Commerce & Contracting](https://www.worldcc.com/Resources/Content-Hub/View/ArticleId/9773) 的研究表明，由于糟糕的管理流程，组织平均损失 9.2% 的合同价值。

## 合同 API 的兴起

具有前瞻性思维的公司现在正在将云原生原则应用于合同管理。正如基础设施通过 Terraform 和 Ansible 等工具变成代码一样，我们看到业务协议也发生了类似的转变，变成了“合同即代码”。

这种转变通过将法律文档管理与运营工作流连接起来的 API 将关键合同信息直接集成到 CI/CD 管道中。[ContractNerds](https://contractnerds.com/how-to-automate-contract-workflows-with-apis/) 的合同专家强调了 API 连接如何实现自动化，并改进工作流程管理，超越了传统合同生命周期管理系统单独所能实现的范围。

## 新的所有者：为什么 CFO 正在领导这场变革

有趣的是，这场云原生合同革命并非由法律部门领导。根据我们与 1,500 多家公司合作的经验，合同所有权正在迅速转移到财务和运营团队，CFO 正在成为合同管理系统的主要利益相关者。

这种权力转移有以下几个原因：

1. **财务可见性**：CFO 需要实时了解整个组织的合同承诺，以建立准确的财务预测，特别是对于具有动态定价的云资源。
2. **运营集成**：与专注于风险缓解的法律团队不同，[运营团队优先考虑自动化工作流程并减少](https://thenewstack.io/use-low-code-to-reduce-friction-for-cloud-operations-teams/) 瓶颈。一家技术公司的运营经理解释说：“我负责所有 CLM 的事务。而我们的法律顾问更多地处理法律本身。”
3. **云成本优化**：根据 [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-04-19-gartner-forecasts-worldwide-public-cloud-end-user-spending-to-reach-nearly-600-billion-in-2023) 的数据，预计 2023 年云支出将达到 5970 亿美元，财务团队需要以编程方式访问合同数据，以有效地管理成本。

## 构建合同管道

我观察到最成功的实施遵循 DevOps 团队熟悉的基础设施即代码模式：

1. **合同存储库作为事实来源**：类似于 git 存储库，所有协议都存储在一个集中的、[versioned system that becomes the single](https://thenewstack.io/nvm-manage-multiple-versions-of-node-js-on-a-single-system/) 事实来源中。
2. **合同模板作为配置**：标准协议被模板化，其中包含可以根据系统参数自动填充的变量，类似于基础设施模板的工作方式。
3. **审批工作流程作为管道门**：正如代码在部署之前必须通过测试一样，合同需要特定的审批工作流程，这些工作流程可以自动化和审计。
4. **合同事件作为触发器**：到期、续订和修订会生成事件，从而触发监控和配置系统中的下游自动化。

## AI 合同代理模式

最新出现的模式是使用 AI 将人为合同与机器可读的 API 连接起来。这些 AI 合同代理可以：

- 从法律文本中提取关键条款和义务，并将其转换为结构化数据
- 创建[合规性的机器可读表示](https://thenewstack.io/a-call-to-use-generative-ai-to-create-more-trustworthy-data/)要求 - 监控软件行为和合同条款，以识别差异。

例如，一家电子商务公司使用人工智能自动跟踪数百个供应商合同中的 [API 速率限制](https://thenewstack.io/how-nuanced-rate-limiting-transforms-your-api-and-business/)，并动态调整其配置，以在合同范围内保持可用资源的最大化。

## 实施挑战

合同即代码的方法面临着几个挑战：

*   **数据提取**：将现有的 PDF 合同转换为结构化数据仍然很困难，需要手动工作或复杂的人工智能。根据 [Fynk](https://fynk.com/en/blog/contract-management-statistics-trends/) 的说法，预计到 2025 年，人工智能将嵌入到 90% 的企业软件中，这将有助于解决这一挑战。
*   **组织孤岛**：法律、财务和工程团队通常使用集成度最低的单独工具。
*   **安全问题**：合同[数据包含敏感的业务信息，需要仔细的访问](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/)控制，类似于代码存储库的挑战。

## 开始使用

对于希望开始此过程的 DevOps 团队，我建议以下三个初始步骤：

1. **API 优先的合同工具**：选择具有强大 API 的合同管理系统，这些 API 可以与现有的 DevOps 工作流程集成。
2. **跨职能所有权**：创建一个由法律、财务和工程代表组成的合同工作组。
3. **从小处着手**：首先自动执行关键合同事件的通知，然后再进行更深入的集成。

## 结论

随着云原生架构的成熟，将业务合同视为代码对于保持速度至关重要。成功的组织将打破技术合同 (API) 和业务合同（法律协议）之间的人为界限，创建统一的系统，使所有义务和依赖关系都可见、可跟踪和可自动化。

未来属于财务、法律和工程部门使用通用合同语言的公司，机器负责翻译。