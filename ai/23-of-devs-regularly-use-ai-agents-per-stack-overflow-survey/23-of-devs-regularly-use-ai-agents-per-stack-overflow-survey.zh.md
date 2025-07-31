[AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 是目前的热门话题，因为据报道它们可以提高生产力，尽管人们对准确性和安全性存在担忧。根据 [2025 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025)，87% 的开发者担心来自 AI 代理的信息的准确性，81% 的开发者担心使用它们时的数据隐私和安全性。AI 代理平台的成本也是 53% 的受访者的障碍。

尽管存在这些担忧，但该研究中已有 23% 的人每周至少使用一次 [AI 代理](https://thenewstack.io/ai-agents/)，另有 8% 的人偶尔使用。另有 17% 的人计划使用 AI 代理，它们是以最少或无需直接人工干预即可运行的自主软件实体。

AI 代理获得了用户，因为 70% 的使用过 AI 代理的开发者认为它减少了在特定开发任务上花费的时间。类似数量（69%）的人至少在一定程度上同意它们提高了生产力。

AI 代理在两个领域的影响较小。只有 17% 的人认为代理改善了团队协作，只有 36% 的人认为它们提高了代码质量。

另一个有趣的与 AI 相关的发现是，只有 15% 的人将 [vibe coding](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) 作为其专业发展工作的一部分。

使用 AI 代理的人也被问到，“您在多大程度上同意以下关于 AI 代理的陈述？” 他们的回答如下图所示：

[![AI 代理的影响](https://cdn.thenewstack.io/media/2025/07/aaf90687-stackoverflow-dev-survey-2025-ai-ai-agents-ai-agent-impact-social.png)](https://cdn.thenewstack.io/media/2025/07/aaf90687-stackoverflow-dev-survey-2025-ai-ai-agents-ai-agent-impact-social.png)

从更广阔的角度来看待 AI，我们发现 78% 的受访者在开发过程中使用 AI 工具，高于去年研究的 62%。这些工具面临的最大问题之一是，46% 的开发者不信任 AI 工具输出的准确性。尽管如此，59% 的人倾向于将 AI 工具作为其开发工作流程的一部分，而持不利观点的人为 21%。我们不知道那些对 AI 工具持否定态度的人中有多少人实际使用过它们。

总体而言，66% 的开发者表示，他们在使用的 AI 工具时遇到的问题或挫折是“AI 解决方案几乎正确，但不完全正确”。这就是为什么其他 [研究](https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025) 发现开发者花费更多时间在代码审查、测试和调试上。在这项研究中，45% 的人表示调试 AI 生成的代码更耗时。

## AI 代理技术路线图

过去一年使用过 AI 代理的开发者被问及他们使用 AI 代理使用过的工具和基础设施。以下是调查结果的快速分解：

* Redis (43%) 和 GitHub MCP Server (43%) 是用于 **AI 代理记忆或数据管理** 的最常用技术。Supabase (21%)、ChromaDB (20%)、pgvector (18%)、Neo4j (12%) 和 Pinecone (11%) 吸引了大量用户。
* Ollama (51%) 和 LangChain (33%) 最有可能用于 **代理编排或代理框架**。采用图表中排名靠前的其他技术包括 LangGraph (16%)、Vertex AI (15%)、Amazon Bedrock Agents (15%)、OpenRouter (13%) 和 Llama Index (13%)。
* [Langsmith](https://www.langchain.com/langsmith) 被 13% 的人引用，是唯一获得显著关注的专门构建的 **AI 代理可观测性、监控或安全解决方案**。该领域的领导者来自处理 *所有* 与开发者相关的可观测性和安全问题的供应商，但此后也添加了与 AI 相关的功能：Grafana + Prometheus (43%)、Sentry (32%)、Snyk (18%) 和 New Relic (13%)。
* ChatGPT (82%)、GitHub Copilot (68%)、Google Gemini (47%) 和 Claud Code (41%) 是最常用的 **开箱即用的代理/副驾驶/助手**。排名较低的是 v0.dev (9%)、Bolt.new (7%)、Lovable.dev (6%) 和 AgentGPT、Tabnine、Replit 和 Auto-GPT（每个都由 5% 的人使用）。

[![AI 代理开箱即用工具](https://cdn.thenewstack.io/media/2025/07/3142bfa2-stackoverflow-dev-survey-2025-ai-ai-agents-ai-agent-external-social1.png)](https://cdn.thenewstack.io/media/2025/07/3142bfa2-stackoverflow-dev-survey-2025-ai-ai-agents-ai-agent-external-social1.png)

使用或开发 AI 代理作为开发工作一部分的人被问到，“您是否使用过以下任何开箱即用的代理、副驾驶或助手？” N=8,323

Stack Overflow 研究已经进行了 15 年。今年的版本基于超过 49,000 名受访者，全球样本与此年度调查的 [先前版本](https://thenewstack.io/salary-pressures-not-ai-vex-developers-says-stack-overflow/) 相似。