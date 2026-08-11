<!--
title: AI 代理的工具调用可能合法但错误？AWS 推出的 Dogwood 致力于解决这一问题
cover: https://cdn.thenewstack.io/media/2026/08/d918e48d-getty-images-uegpw7q6uhc-unsplash-scaled.jpg
summary: AWS 推出开源策略语言 Dogwood，旨在通过引入时间维度和序列治理，解决 AI 代理在处理复杂工作流时仅凭单次请求判断带来的安全风险，是对现有 Cedar 授权框架的重要补充。
-->

AWS 推出开源策略语言 Dogwood，旨在通过引入时间维度和序列治理，解决 AI 代理在处理复杂工作流时仅凭单次请求判断带来的安全风险，是对现有 Cedar 授权框架的重要补充。

> 译自：[Your AI agent’s next tool call may be valid but wrong. AWS's Dogwood promises to fix that.](https://thenewstack.io/aws-dogwood-agent-policies/)
> 
> 作者：Frederic Lardinois

**AWS 于周四推出了 Dogwood**，这是一种开源策略语言和参考解释器，旨在让开发者能够治理 AI 代理的工具调用序列，而不是孤立地评估每一个动作。

该公司还将 [Dogwood](https://github.com/dogwood-policy/dogwood) 支持添加到了 [Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) Policy 中，这是其用于控制代理可以调用哪些工具以及在何种条件下进行调用的托管服务。该语言及其参考实现目前均采用 Apache 2.0 许可证。

Dogwood 构建在 [Cedar](https://cedarpolicy.com) 之上，后者是已经为 AgentCore Policy 提供支持的开源授权语言。Cedar 是 AWS 在 2025 年底作为 [沙箱项目](https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project/) 贡献给 CNCF 的，例如，它能够决定用户或代理是否可以使用给定的参数集调用退款工具。Dogwood 更进一步，因为它还能将之前的事件纳入考量。这可能包括某人是否批准了退款、代理在过去一小时内退款了多少金额，或者它之前是否访问了应阻止其联系外部服务的信息。

> “基于时间点的决策在许多形式的访问控制中是有意义的，但当代理将多个动作组合成更长的工作流时，序列本身就成了团队想要治理的对象。”

正如 AWS 团队所解释的那样：“基于时间点的决策在许多形式的访问控制中是有意义的，但当代理将多个动作组合成更长的工作流时，序列本身就成了团队想要治理的对象。Dogwood 为他们提供了一种表达序列策略的语言，以便捕捉对先决条件、速率限制和排序的约束。”

在去年的 re:Invent 大会上，AWS 推出了 [AgentCore Policy](https://thenewstack.io/aws-new-policy-layer-in-bedrock-agentcore-makes-sure-ai-agents-cant-give-away-the-store/)，作为大语言模型之外的确定性控制层。模型提出一个工具调用，策略引擎随后接受或拒绝它。这使得模型本身脱离了执行循环。

AgentCore Gateway 位于代理和这些工具之间。对于每个请求，该服务的策略引擎都会评估 Cedar 规则，描述发起请求的主体、请求的操作、资源以及工具的输入参数。默认情况是拒绝请求，且任何明确的禁止始终优先于许可。

但这些规则只能看到当前的请求。给定相同的请求，Cedar 总是会返回相同的决策，而不管之前的活动或其策略运行的顺序如何。这使得 Cedar 策略更易于分析，但也意味着它们无法表达依赖于动作序列的策略。

[Dogwood](https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/) 添加的内容（除其他事项外）是 [时间条件](https://dogwood-policy.github.io/dogwood/guide/04-temporal-expressions.html)，它可以检查之前的工具请求和响应。时间条件可以查看请求之前发生了什么，以及它发生的时间有多久。

AWS 使用一个股票交易代理作为示例来展示其工作原理。策略可以允许代理仅在批准工具在过去一小时内对相同的股票和数量返回肯定响应时才卖出股票——而且该批准是一个单独的事件，策略引擎必须在代理的近期历史记录中找到它。

开发者可以检查事件是否发生、统计时间窗口内的调用次数、统计不同的值（如支付接收者），或添加值（如转账总额）。这些操作构建在 [度量一阶时序逻辑](https://dl.acm.org/doi/10.1145/2699444) 的子集之上，这是一种用于描述随时间推移的事件属性的形式系统。

使这一切变得更加复杂的是并行工具调用。

在 AWS 的示例中，代理可能被限制每小时转账不超过 5,000 美元。如果策略仅累加已完成的转账，代理可以在第一个请求完成之前提交多个 2,000 美元的请求，从而超过其限额，因为在检查每个请求时，已完成的总额可能仍然为零。

> 如果策略仅累加已完成的转账，代理可以在第一个请求完成之前提交多个 2,000 美元的请求，从而超过其限额，因为在检查每个请求时，已完成的总额可能仍然为零。

但 Dogwood 拥有上下文，可以统计所有转账请求，包括当前正在评估的请求。在 AWS 的示例中，即使前两笔转账尚未返回结果，这也导致第三个 2,000 美元的请求被拒绝。

对于通过 AgentCore Gateway 连接的代理，AWS 可以从网关 MCP 清单中的工具生成 Dogwood 的操作模式。每个工具随后成为策略可以引用的操作。

**值得注意的是**，Dogwood 并没有取代 Cedar，而是扩展了它。据 AWS 称，任何现有的 Cedar 策略也是有效的 Dogwood 策略，因此团队不必重写他们当前的规则。对于时间策略，Dogwood 将依赖于历史的条件转换为 Cedar 上下文字段。在参考实现中，Dogwood 在 Cedar 做出授权决策之前从事件历史中填充该字段。

## Dogwood 需要可靠的事件历史

Dogwood 的运行成本比 Cedar 更高，因为它是有状态的。它必须保留和搜索事件记录，AWS 指出评估时间可能取决于该历史记录的长度。

目前，随附的开源参考解释器旨在探索和测试该语言，而不是用作生产环境的授权引擎。

然而，对于任何想要立即采用该开源项目的人来说，需要注意一些事项。正如存储库中所指出的，用户必须提供可信的时间戳、对事件进行身份验证、保持字段和操作名称一致、持久化存储追踪记录、记录授权决策，以及隔离租户之间的历史记录。团队还需要保留策略，因为工具调用历史记录可能包含敏感数据。

> 对于使用该开源版本的团队来说，更困难的问题是事件历史记录是否完整且足够值得信赖，以用于授权。

将来，AWS 计划添加与绝对时间挂钩的规则，例如在午夜重置的配额，以及检查预期动作是否最终发生的“活跃度”属性。该公司还希望将 Dogwood 从单个代理扩展到多代理系统，例如在多代理系统中，策略可能需要管理移交和共享锁。

截至目前，AWS 不接受直接贡献，但表示欢迎“社区对语言设计和未来方向的反馈”。对于使用该开源版本的团队来说，更困难的问题是事件历史记录是否完整且足够值得信赖，以用于授权。