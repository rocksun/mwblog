An AI agent feels harmless when it only produces text, but the risk profile changes the moment it calls a tool.

At first, that tool might seem minor: reading logs, summarizing a ticket, searching documentation, or classifying an incident. Scope creep is almost inevitable, however. Soon, the agent needs to update a ticket, open a deployment request, restart a worker, or query an internal system.

At that point, the agent is no longer just a chat interface. It is an execution surface.

Many teams still focus almost entirely on [prompt engineering](https://thenewstack.io/prompt-engineering-for-developers/) here. Prompts matter, but they are no longer the strongest control. Once an agent acts through tools, tool access becomes production access. The architecture must answer a different set of questions:

* Who is asking for this tool call?
* Is the tool registered and intentionally exposed?
* Is the action blocked by an immutable policy?
* Does the caller’s role have the required scope?
* Are the arguments valid?
* Is the action read-only, reversible, risky, or destructive?
* Does the action require human approval?
* Will the system audit the decision natively?

> “Once an agent acts through tools, tool access becomes production access.”

**If your system relies on natural-language tool descriptions to answer these questions, it is too soft for production.**

Tool descriptions are useful because they help the model decide when a tool is relevant. A description, however, is never a permission boundary.

Consider a tool named `infra_tool`. Its description claims it can “help inspect and manage infrastructure.” That might be enough for a local demo, but it fails as an execution contract. Does “manage” mean reading logs, restarting a worker, opening a deployment request, or deleting a resource? Who is authorized to perform each action?

A secure design decouples tool selection from authorization. The model proposes a tool call, but [a deterministic policy layer](https://thenewstack.io/harness-ai-agent-dlc/) decides whether the call proceeds.

The minimum viable architecture looks like this:

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

*(You can view an offline reference implementation of this pattern on* [*GitHub*](https://www.google.com/search?q=https://github.com/fdaniel-alvarez-dev/agent-tool-governance-lab)*.)*

Crucially, the agent never calls tools directly. It only requests a call. The governance layer owns the final execution decision.

## A small policy wrapper changes the failure mode

The reference implementation uses a deterministic Python package. It avoids cloud calls and external API keys to demonstrate one narrow purpose: blocking unsafe paths before execution.

The core role policy is intentionally boring:

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

This mapping is not a comprehensive enterprise IAM system. It simply proves the boundary. A viewer reads logs. An operator requests a worker restart. An admin opens a deployment request. Unknown roles fail closed because they receive an empty scope set. The lab also blocks destructive tools entirely, even if someone attempts to expose them through the registry.

After the tool specification has been retrieved from the trusted registry, the policy evaluates the request in a fail-fast order:

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

## Schema validation catches a different class of mistakes

Authorization alone is not enough. An authorized user can still pass invalid arguments.

For example, a `read_logs` tool accepts a `service` and a `limit`. The `service` must match a known value, and the system must reject unexpected arguments. This prevents a vague tool interface from quietly expanding its own scope.

In the lab, the system allows this request:

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

But it blocks this request before execution:

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

Do not treat the extra `write` field as harmless. In production, unexpected arguments can create accidental privilege expansion when downstream code interprets them. Strict schemas force ambiguity into explicit engineering decisions.

The ordering matters here. Validation still occurs before execution, but only after the request passes static risk and authorization checks. An unauthorized caller should not consume validation work or receive unnecessary details about a tool’s accepted payload.

## Risk classification should belong to the registry

The agent must never decide whether an action is risky. The trusted registry owns that definition.

> “The agent must never decide whether an action is risky. The trusted registry owns that definition.”

In the reference implementation, every tool carries a hardcoded risk level: `read_only`, `reversible_write`, `risky`, or `destructive`. The policy reads that metadata before it evaluates caller-controlled arguments.

Restarting a worker or opening a deployment request is `risky` and requires human approval. A `destructive` tool exists in the registry only to prove that the policy blocks it natively.

This distinction matters. An agent might hallucinate a safe description for a dangerous request, or a user might disguise a destructive action as routine maintenance. The policy layer must ignore that prose and rely on metadata controlled by engineering.

## Approval is not a UI detail

Product teams often treat human approval as a UI feature: a button, a modal, or a Slack message. UX matters, but approval is fundamentally an architectural concern.

The approval gate must bind statefully or cryptographically to the request ID. A generic approval token is insufficient because it can be replayed across unrelated actions.

The system yields three valid outcomes: `allow`, `block`, or `approval_required`.

The third state is critical. Without it, teams collapse workflows into binary success or failure. A risky action pausing for approval is not a failure. It is a valid workflow state showing that the caller is authorized to request the action, the payload is valid, and execution still requires human verification.

## Audit blocked calls, not only successful calls

Most systems log successful executions, but fewer capture preventative decisions. For AI agents, blocked calls often produce the most valuable telemetry.

A robust audit record captures:

* Request ID
* User ID
* User role
* Tool name
* Arguments
* Decision
* Risk level
* Reason
* Execution outcome, if any

If a viewer attempts a deployment, the system logs a `block` decision. A risky restart triggers an `approval_required` record. An approved restart logs an `allow` decision. This trail allows security teams to reconstruct both what the agent did and what it attempted to do.

Production systems should also apply data minimization to audit records. Arguments can contain sensitive values, so retention, redaction, access controls, and tamper resistance are part of the governance boundary.

## What this pattern fixes

This architecture does not magically secure agents against prompt injection, identity spoofing, or compliance failures. It closes one [dangerous gap](https://thenewstack.io/webassembly-sandboxing-ai-agents/) by removing the agent’s final authority over execution.

It also changes the security conversation. Instead of hoping that “the prompt holds,” engineering can point to a deterministic registry, static policies, strict schemas, role controls, approval states, and audit trails. That is a much stronger basis for a production security review.

## What it makes harder

The trade-off is friction.

Strict schemas require maintenance. Role mappings need clear ownership. Risk levels require periodic review. Approval flows add latency, and audit logs need retention and access policies. A permissive tool is faster to demo than a governed one, but permissive tools are where production risks hide.

> “Let the model propose; let deterministic policy decide.”

The governing rule is simple: as a tool’s ability to change state increases, trust in the model’s authorization judgment must decrease. Let the model propose; let deterministic policy decide.

## Checklist before connecting an agent to internal tools

Before granting an agent access to a real tool, make sure you can answer the following questions:

* Is the tool retrieved only from a trusted registry with a clear name, action, scope, and risk level?
* Does an immutable policy block disabled destructive actions before payload processing?
* Does the system fail closed for unknown roles?
* Is access checked against the caller’s role or scope before detailed payload validation?
* Does the system validate all arguments before execution?
* Does the system reject unexpected arguments natively?
* Are validation errors sanitized before they are exposed externally?
* Are write actions physically separated from read-only actions?
* Do risky actions enforce human approval?
* Is approval tied directly to the request ID and action context?
* Does the system audit blocked and approval-required calls?
* Can the executor be reached only through the policy layer?

If you answer “no” to any of these, you are connecting the agent to production prematurely.

## Tool access is production access

An initial AI agent demo can feel like a clever UI. Production reality is different. Once an agent calls tools, it becomes part of the control plane for real systems.

This does not mean engineering teams should abandon tool-using agents. It means they must stop treating them only as prompt-design problems. Tool access is production access. Architect accordingly.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/e4a9c860-cropped-da07f690-freddy_alvarez_headshot.jpg)

Freddy Daniel Alvarez Pinto is a Senior Cloud, DevOps, and AI Infrastructure Engineer with more than 20 years of experience designing, operating, and improving mission-critical platforms across telecom, financial services, and cloud environments. His work focuses on cloud infrastructure, Kubernetes,...

Read more from Freddy Daniel Alvarez Pinto](https://thenewstack.io/author/freddy-daniel-alvarez-pinto/)