**AWS on Thursday launched Dogwood**, an open-source policy language and reference interpreter that lets developers govern sequences of AI agent tool calls instead of evaluating each action in isolation.

The company has also added [Dogwood](https://github.com/dogwood-policy/dogwood) support to [Amazon Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) Policy, its managed service for controlling which tools an agent may call and under what conditions. The language and its reference implementation are now available under the Apache 2.0 license.

Dogwood builds on [Cedar](https://cedarpolicy.com), the open source authorization language that already powers AgentCore Policy. Cedar, which AWS contributed to the CNCF [as a sandbox project](https://aws.amazon.com/blogs/opensource/cedar-joins-cncf-as-a-sandbox-project/) in late 2025, can decide whether a user or agent may call a refund tool with a given set of arguments, for example. Dogwood takes this a step further because it can also take earlier events into account. That may be whether somebody approved the refund, how much the agent has refunded in the past hour, or whether it previously accessed information that should prevent it from contacting an outside service.

> “Point-in-time decisions make sense for many forms of access control, but when agents compose multiple actions into longer workflows, the sequence itself becomes something teams want to govern.”

As the AWS team explains, “Point-in-time decisions make sense for many forms of access control, but when agents compose multiple actions into longer workflows, the sequence itself becomes something teams want to govern. Dogwood gives them a language for expressing policies over sequences, in order to capture constraints on prerequisites, rate limits, and ordering.”

At its re:Invent conference last year, AWS introduced [AgentCore Policy](https://thenewstack.io/aws-new-policy-layer-in-bedrock-agentcore-makes-sure-ai-agents-cant-give-away-the-store/) as a deterministic control layer outside the large language model. The model proposes a tool call, which the policy engine then accepts or rejects. This keeps the model itself out of the enforcement loop.

AgentCore Gateway sits between an agent and those tools. For each request, the service’s policy engine evaluates Cedar rules describing the principal making the request, the requested action, the resource, and the tool’s input parameters. The default is to deny requests, and any explicit prohibition always takes precedence over a permission.

But those rules only see the current request. Given the same request, Cedar will always return the same decision, regardless of earlier activity or the order in which its policies run. That makes Cedar policies easier to analyze, but it also means they can’t express policies that depend on a sequence of actions.

What [Dogwood](https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/) adds, among other things, is [temporal conditions](https://dogwood-policy.github.io/dogwood/guide/04-temporal-expressions.html) that examine earlier tool requests and responses. A temporal condition can look at what happened before a request and how long ago it happened.

AWS uses a stock-trading agent as its example to show how this works. A policy can allow the agent to sell shares only if an approval tool returned a positive response for the same stock and number of shares during the previous hour — and that approval is a separate event that the policy engine must find in the agent’s recent history.

Developers can check whether an event occurred, count calls during a time window, count distinct values such as payment recipients, or add values such as the total amount transferred. Those operations are built on a subset of [Metric First-Order Temporal Logic](https://dl.acm.org/doi/10.1145/2699444), a formal system for describing properties of events over time.

What can make all of this even more complicated is parallel tool calls.

In AWS’s example, an agent may be restricted from transferring more than $5,000 per hour. If the policy only adds up already completed transfers, the agent could submit several $2,000 requests before the first one finishes, exceeding its limit because the completed total may still be zero when each request is checked.

> If the policy only adds up already completed transfers, the agent could submit several $2,000 requests before the first one finishes, exceeding its limit because the completed total may still be zero when each request is checked.

But Dogwood has the context and can count all transfer requests, including those currently being evaluated. In AWS’s example, that causes the third $2,000 request to be denied even if the first two transfers have not returned a result.

For agents connected through AgentCore Gateway, AWS can generate Dogwood’s action schema from the tools in the gateway’s MCP manifest. Each tool then becomes an action the policy can reference.

**It’s worth noting** that Dogwood doesn’t replace Cedar but extends it. According to AWS, any existing Cedar policy is also a valid Dogwood policy, so teams don’t have to rewrite their current rules. For temporal policies, Dogwood translates the history-dependent condition into a Cedar context field. In the reference implementation, Dogwood fills that field from the event history before Cedar makes the authorization decision.

## Dogwood needs a reliable event history

Dogwood is more expensive to run than Cedar because it is stateful. It must retain and search event records, and AWS notes that evaluation time can depend on the length of that history.

As of now, the included open source reference interpreter is meant for exploring and testing the language, not for use as a production authorization engine.

There are some caveats, though, for anyone who wants to adopt the open-source project right away. As the repository notes, users would have to provide trusted timestamps, authenticate events, keep field and action names consistent, store traces durably, log authorization decisions, and isolate histories between tenants. Teams would also need a retention policy because tool-call histories can contain sensitive data.

> For teams using the open source release, the harder question is whether the event history is complete and trustworthy enough to use for authorization.

In the future, AWS plans to add rules tied to absolute times, such as quotas that reset at midnight, as well as “liveness” properties that check whether an expected action eventually happens. The company also wants to extend Dogwood from individual agents to multi-agent systems, where a policy may need to govern handoffs and shared locks, for example.

As of now, AWS is not accepting direct contributions but says it welcomes “community feedback on the language design and future directions.” For teams using the open source release, the harder question is whether the event history is complete and trustworthy enough to use for authorization.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)