![A finger on the button, depicting roll-backs and kill-switches.](https://cdn.thenewstack.io/media/2026/11/2876cde1-public-domain-vectors-grxqbf6y-dq-unsplash-1024x646.jpg)

Anthropic 推出了其用于构建和运行 AI 智能体平台的自托管版本。

这个名为 [自托管 Claude 托管智能体](https://platform.claude.com/docs/en/managed-agents/self-hosted) 的服务目前已推出私有测试版。客户可以在自己的云账号或本地数据中心中，同时托管用于协调智能体的服务器以及运行智能体工具的沙箱。凭证和会话历史记录保留在其自己的基础设施上，而对 Claude 的请求则发送至他们配置的推理提供商。

虽然自托管的好处显而易见，特别是对于处理敏感数据的公司而言，但[随附的许可证](https://www.anthropic.com/legal/self-hosted-managed-agents-license)附带了许多值得注意的注意事项，可能会让一些客户犹豫不决——这包括对响应安全通知的严格期限、客户可使用的模型的限制，以及禁止阻止将某些类型的数据发送给 Anthropic 的规则。

## Claude走向本地化部署之路

早在 4 月份，Anthropic 就[推出了 Claude 托管智能体](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/)，这是一项用于构建和运行 AI 智能体的托管服务。次月，该公司[推出了自托管沙箱](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)，允许客户在自己的基础设施上运行智能体的工具，而 Anthropic 继续运行 Claude 托管智能体服务器。

随着自托管 Claude 托管智能体的加入，客户现在也可以自己运行该服务器，并将会话历史记录存储在他们自己的数据库中。

在标志着该服务发布的[博客文章](https://claude.com/resources/articles/self-hosted-managed-agents)中，Anthropic 表示智能体正在承担更多重要的工程任务，包括修复失败的构建、检查发布以及决定哪些警报需要关注。这项工作可能需要访问敏感系统，例如私有代码库以及内部构建和发布系统。

> “对于拥有这种级别访问权限的智能体，一些团队希望整个服务都在他们自己的环境中，而不仅仅是沙箱。”

该公司写道：“它们在您的代码上无人值守运行，并且需要访问您的内部系统。对于拥有这种级别访问权限的智能体，一些团队希望整个服务都在他们自己的环境中，而不仅仅是沙箱。在此之前，这意味着必须自己构建平台。”

几家公司正是这样做的。Spotify [开发了 Honk](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint)，它通过 Spotify 自身架构内的 Agent SDK 运行 Claude。该公司在其云环境中的 Kubernetes Pod 中部署 Honk，使其能够访问其内部 CI 系统，以便运行构建并验证其代码更改。

Anthropic 的新产品将大部分此类工作打包成了一个产品。客户可以在自己的云端或数据中心运行 Anthropic 的服务器和沙箱工作节点，如果他们希望在重启之间保留会话历史记录，还可以配合 PostgreSQL 使用，同时他们的开发人员可以使用与托管服务相同的核心 APIs。本地服务器可以通过 Anthropic 的 API、诸如 Amazon Bedrock 或 Microsoft Foundry 等云服务提供商或公司自己的网关将请求发送到 Claude。

## 细节中的魔鬼：8 小时内必须采取行动

虽然 Anthropic 的正式公告强调了公司可能希望自己托管该服务的*原因*，但深入研究许可证的细节就会发现，Anthropic 在软件部署后对该软件保留了多大的控制权。

首先，Anthropic 将服务器作为一个专有二进制文件交付，客户无法修改，这意味着他们无法自行修补或定制服务器代码。他们*可以*通过自己的网关路由请求，但仅限于 Claude 模型。该许可证还禁止使用来自其他开发人员的模型，除非 Anthropic 明确允许，并且[公开的推理文档](https://platform.claude.com/docs/en/managed-agents/self-hosted/inference-provider)仅列出了 Claude 模型。

该许可证中最引人注目的条款之一是，客户对 Anthropic 的安全通知做出反应的时间非常短。如果该公司以书面形式标记了安全、防护或滥用风险，客户只有八个小时的时间来禁用受影响的功能或在每个部署中回滚版本。他们还必须在交付后的一个工作日内安装指定的安全更新。

![§5.3 八小时内回滚或禁用](https://cdn.thenewstack.io/media/2026/11/a589ff56-safety-rollback-screenshot-with-torn-edges-1024x172.png)

§5.3 八小时内回滚或禁用

[Moor Insights & Strategy](https://moorinsightsstrategy.com/) 的创始人兼首席分析师 [Patrick Moorhead](https://www.linkedin.com/in/patmoorhead/) 表示，八小时的期限比大多数大型企业通常允许进行生产更改的时间还要紧迫。

Moorhead 告诉 *The New Stack*：“自托管通常意味着客户拥有更改窗口。这个许可证颠倒了这一点。”

> “自托管通常意味着客户拥有更改窗口。这个许可证颠倒了这一点。”

即使在 Claude 模型阵容本身中，访问权限也可能有所不同。许可证规定，Anthropic 可以出于安全原因决定，某个或所有被许可方的客户*只能*通过 Anthropic 的托管服务访问某些 Claude 模型。

![§5.6 Anthropic 可以为托管访问保留模型](https://cdn.thenewstack.io/media/2026/11/407f225c-5.6-access-path-original-screenshot-1024x289.png)

*§5.6 Anthropic 可以为托管访问保留模型*

此外，许可证禁止客户阻止或更改其所谓的“使用信号”，即软件可能发送给 Anthropic 的可观测性数据。该公司可以使用这些数据来衡量软件的使用情况并监控对协议的遵守情况。

> “其想法是，如果你构建了一个违法的或造成危害的智能体，你无法阻止我们[模型实验室]弄清楚这一点并采取任何措施。”

Moorhead Insights & Strategy 的另一位分析师 [Jason Andersen](https://www.linkedin.com/in/jasontandersen/) 表示，遥测条款和维护 Anthropic 指定的安全防范措施的单独要求，与云供应商试图防止滥用的方式大致相符。

Andersen 告诉 *The New Stack*：“其想法是，如果你构建了一个违法的或造成危害的智能体，你无法阻止我们[模型实验室]弄清楚这一点并采取任何措施。”

![§5.9 客户不能阻止使用信号](https://cdn.thenewstack.io/media/2026/11/a8419896-5.9-usage-signals-screenshot-1024x270.png)

*§5.9 客户不能阻止使用信号*

## 安全背景

7 月份，[Anthropic 透露](https://thenewstack.io/anthropic-claude-containment-failure/)，Claude 模型在网络安全评估期间获得了对真实计算机系统的未授权访问。同月，[OpenAI 透露](https://thenewstack.io/openai-huggingface-sandbox-breach/)，接受内部测试的模型绕过了隔离控制并攻破了 Hugging Face 的系统。

虽然模型提供商可以自行解决问题，但在客户服务器上运行的智能体可能会继续运行。因此，客户可能还需要采取行动来遏制该问题。

Andersen 说：“我确实认为这是 Anthropic 在安全性方面加大力度以限制其风险暴露，这实际上就是许可证的作用。它并没有真正改变它制造的技术或那些用它来制造智能体的人的风险。”

## 企业买家可能会如何反应

总而言之，现在的托管智能体有三种形式：Anthropic 完全托管、Anthropic 托管且带有客户运行的沙箱，以及现在的完全自托管。

第三种选择是否适合买家，取决于他们最初对自托管的需求是什么。Moorhead 预计受监管的买家会对回滚期限和遥测条款提出反对意见。

他说：“对于已经习惯将 Claude 作为云服务运行的公司来说，这是行得通的碰巧放在他们数据中心里的云服务。对于银行、政府和主权买家，预计采购和法务部门会对第 5.3 节（安全回滚）和第 5.9 节（使用信号）提出反对。”

就 Andersen 而言，他认为这些条款对企业来说是“合理的请求”，并怀疑它们总体上会减慢采用速度，因为需要对其智能体进行完全控制的买家可能已经在寻找其他地方了。

他说：“如果你对智能体需要这种级别的控制，你可能会考虑一个更加独立、可能是开放权重的解决方案。”

原文链接：[Anthropic 现在允许您自托管 Claude 托管智能体。代价是什么？如果软件标记了安全风险，必须在 8 小时内采取行动](https://thenewstack.io/self-hosted-claude-managed-agents/)，发布于 [The New Stack](https://thenewstack.io)。