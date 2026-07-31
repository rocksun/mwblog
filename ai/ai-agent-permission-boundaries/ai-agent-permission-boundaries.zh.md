AI代理在仅生成文本时看起来无害，但一旦它调用工具，风险状况就会立即改变。

起初，该工具可能看起来微不足道：读取日志、总结工单、搜索文档或分类事件。然而，范围蔓延几乎是不可避免的。很快，代理就需要更新工单、发起部署请求、重启工作进程或查询内部系统。

此时，代理不再仅仅是一个聊天界面。它成为了一个执行界面。

许多团队在这里仍然几乎完全专注于[提示词工程](https://thenewstack.io/prompt-engineering-for-developers/)。提示词固然重要，但它们不再是最强的控制手段。一旦代理通过工具进行操作，工具访问权就变成了生产访问权。架构必须回答一系列不同的问题：

* 谁在请求此工具调用？
* 该工具是否已注册并被有意暴露？
* 该操作是否被不可变的策略所阻止？
* 调用者的角色是否具有所需的权限范围？
* 参数是否有效？
* 该操作是只读的、可逆的、有风险的，还是破坏性的？
* 该操作是否需要人工审批？
* 系统是否会原生审计该决策？

> “一旦代理通过工具进行操作，工具访问权就变成了生产访问权。”

**如果你的系统依赖自然语言工具描述来回答这些问题，那么它对于生产环境来说太脆弱了。**

工具描述很有用，因为它们有助于模型决定何时使用相关工具。然而，描述绝不是权限边界。

考虑一个名为 `infra_tool` 的工具。它的描述声称它可以“帮助检查和管理基础设施”。这对于本地演示来说可能足够了，但作为执行契约则完全不够。 “管理”是指读取日志、重启工作进程、发起部署请求还是删除资源？谁有权执行每项操作？

安全的架构将工具选择与授权解耦。模型提议进行工具调用，但[确定性策略层](https://thenewstack.io/harness-ai-agent-dlc/)决定调用是否继续。

最小可行架构如下所示：

```

Agent request
  ↓
Trusted tool registry lookup and risk metadata
  ↓
Static risk policy
  ↓
Role/scope authorization
  ↓
Strict argument validation
  ↓
Approval gate
  ↓
Tool executor
  ↓
Audit log

```

*（你可以在 [GitHub](https://www.google.com/search?q=https://github.com/fdaniel-alvarez-dev/agent-tool-governance-lab) 上查看此模式的离线参考实现。）*

至关重要的是，代理从不直接调用工具。它只是请求调用。治理层拥有最终的执行决策权。

## 一个小小的策略包装器改变了故障模式

该参考实现使用了一个确定性的 Python 包。它避免了云调用和外部 API 密钥，以展示一个狭窄的目标：在执行前阻止不安全路径。

核心角色策略特意设计得很简单：

```

python
DEFAULT_ROLE_SCOPES = {
    "viewer": frozenset({"logs:read"}),
    "operator": frozenset({"logs:read", "worker:restart:request"}),
    "admin": frozenset(
        {"logs:read", "worker:restart:request", "deploy:request"}
    ),
}

```

这种映射并不是一个全面的企业 IAM 系统。它只是验证了边界。查看者（viewer）读取日志。操作员（operator）请求工作进程重启。管理员（admin）发起部署请求。未知角色会被阻止，因为它们收到的范围集为空。该实验室还完全阻止了破坏性工具，即使有人试图通过注册中心暴露它们。

从受信任的注册中心检索到工具规范后，策略会以“快速失败”的顺序评估请求：

```

python
# 1. Enforce immutable static policies first.
if spec.risk_level == RiskLevel.DESTRUCTIVE:
    return block(
        call,
        spec.risk_level,
        "destructive tools are disabled",
    )

# 2. Enforce identity and role-based authorization.
allowed_scopes = role_scopes.get(call.user_role, frozenset())
if spec.scope not in allowed_scopes:
    return block(
        call,
        spec.risk_level,
        "role does not have required scope",
    )


# 3. Validate caller-controlled arguments after cheaper policy checks.
schema_errors = registry.validate_arguments(spec, call.arguments)
if schema_errors:
    return block(
        call,
        spec.risk_level,
        "; ".join(str(error) for error in schema_errors),
    )

# 4. Require approval for risky or explicitly gated actions.
if spec.requires_approval or spec.risk_level == RiskLevel.RISKY:
    approval_status = approval_gate.status_for(
        call.approval_id,
        call.request_id,
    )
    if approval_status != ApprovalStatus.APPROVED:
        return approval_required(call, spec.risk_level)

```

## 模式校验可捕捉另一类错误

仅靠授权是不够的。授权用户仍然可能传递无效参数。

例如，一个 `read_logs` 工具接受 `service` 和 `limit`。`service` 必须匹配已知值，系统必须拒绝意外的参数。这可以防止模糊的工具接口悄悄扩大其自身范围。

在实验室中，系统允许此请求：

```

json
{
  "user_role": "viewer",
  "tool_name": "read_logs",
  "arguments": {
    "service": "api",
    "limit": 5
  }
}

```

但它会在执行前阻止此请求：

```

json
{
  "user_role": "viewer",
  "tool_name": "read_logs",
  "arguments": {
    "service": "api",
    "limit": 5,
    "write": true
  }
}

```

不要将额外的 `write` 字段视为无害。在生产环境中，意外参数可能会在下游代码解释它们时导致意外的权限提升。严格的模式强制将歧义转化为明确的工程决策。

顺序在这里很重要。校验仍然发生在执行之前，但仅在请求通过静态风险和授权检查之后。未经授权的调用者不应消耗校验资源或接收关于工具接受负载的不必要细节。

## 风险分类应属于注册中心

代理绝不能决定操作是否有风险。受信任的注册中心拥有该定义。

> “代理绝不能决定操作是否有风险。受信任的注册中心拥有该定义。”

在参考实现中，每个工具都带有硬编码的风险级别：`read_only`（只读）、`reversible_write`（可逆写入）、`risky`（有风险）或 `destructive`（破坏性）。策略在评估调用者控制的参数之前会读取该元数据。

重启工作进程或发起部署请求是 `risky` 的，需要人工审批。注册中心中存在 `destructive` 工具，仅为了证明策略会原生阻止它。

这种区分很重要。代理可能会为危险的请求幻觉出一个安全的描述，或者用户可能会将破坏性操作伪装成例行维护。策略层必须忽略那些文字描述，并依赖工程控制的元数据。

## 审批不是 UI 细节

产品团队通常将人工审批视为一种 UI 功能：按钮、模态框或 Slack 消息。用户体验固然重要，但审批本质上是一个架构问题。

审批门必须与请求 ID 进行状态绑定或加密绑定。通用的审批令牌是不够的，因为它可以在不相关的操作之间重放。

系统产生三种有效结果：`allow`（允许）、`block`（阻止）或 `approval_required`（需要审批）。

第三种状态至关重要。没有它，团队会将工作流简化为二元的成功或失败。挂起等待审批的有风险操作并不是失败。这是一个有效的工作流状态，表明调用者有权请求该操作，负载有效，且执行仍需要人工验证。

## 审计被阻止的调用，而不仅仅是成功的调用

大多数系统记录成功的执行，但很少有系统捕捉预防性决策。对于 AI 代理，被阻止的调用通常会产生最有价值的遥测数据。

强大的审计记录包含：

* 请求 ID
* 用户 ID
* 用户角色
* 工具名称
* 参数
* 决策
* 风险级别
* 原因
* 执行结果（如有）

如果查看者尝试进行部署，系统会记录 `block` 决策。有风险的重启会触发 `approval_required` 记录。获批的重启记录 `allow` 决策。这条线索允许安全团队重建代理做了什么以及它尝试做什么。

生产系统还应对审计记录应用数据最小化。参数可能包含敏感值，因此保留、脱敏、访问控制和防篡改是治理边界的一部分。

## 此模式解决的问题

这种架构并不能神奇地保护代理免受提示词注入、身份欺骗或合规性失败的影响。它通过移除代理对执行的最终授权，消除了一个[危险的缺口](https://thenewstack.io/webassembly-sandboxing-ai-agents/)。

它还改变了安全对话。工程团队不再希望“提示词能稳住”，而是可以指出确定性的注册中心、静态策略、严格的模式、角色控制、审批状态和审计追踪。这是进行生产安全审查的基础。

## 它带来的困难

权衡在于摩擦力。

严格的模式需要维护。角色映射需要清晰的归属。风险级别需要定期审查。审批流程增加了延迟，审计日志需要保留和访问策略。宽松的工具演示起来比受管制的工具快，但生产风险就隐藏在宽松的工具中。

> “让模型提议；让确定性策略决定。”

指导原则很简单：随着工具改变状态的能力增加，对模型授权判断的信任度必须降低。让模型提议；让确定性策略决定。

## 将代理连接到内部工具之前的核对清单

在授予代理访问真实工具的权限之前，请确保你能回答以下问题：

* 该工具是否仅从具有明确名称、操作、范围和风险级别的受信任注册中心检索？
* 不可变的策略是否在负载处理前阻止了禁用的破坏性操作？
* 系统是否对未知角色采取“默认拒绝”？
* 在进行详细负载校验之前，是否根据调用者的角色或范围检查了访问权限？
* 系统是否在执行前校验了所有参数？
* 系统是否能原生拒绝意外参数？
* 校验错误在向外暴露前是否已脱敏？
* 写入操作是否与只读操作在物理上分离？
* 有风险的操作是否强制执行了人工审批？
* 审批是否直接绑定到请求 ID 和操作上下文？
* 系统是否审计了被阻止和需要审批的调用？
* 执行器是否只能通过策略层访问？

如果上述任何问题的回答为“否”，说明你连接代理到生产环境为时尚早。

## 工具访问就是生产访问

最初的 AI 代理演示可能感觉像是一个巧妙的 UI。生产环境的现实则不同。一旦代理调用工具，它就成为了真实系统的控制平面的一部分。

这并不意味着工程团队应该放弃使用工具的代理。这意味着他们必须停止将其仅仅视为提示词设计问题。工具访问就是生产访问。请进行相应的架构设计。