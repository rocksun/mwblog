A year ago, [Pulumi](https://www.pulumi.com) CEO Joe Duffy says, VPs of infrastructure didn’t think “agentic AI” and “infrastructure” belonged in the same sentence. Today, AI agents already drive 20 percent of all operations on Pulumi’s platform, up from virtually zero a year ago, and Duffy thinks it could be 100 percent in the future.

On Tuesday, the company is shipping a bundle of capabilities the company specifically built for what Pulumi describes as the “agentic infrastructure era.”

![](https://cdn.thenewstack.io/media/2026/05/3c6865e8-pulumineocli_static1-1024x554.png)

Pulumi Neo in the CLI. Credit: Pulumi.

## A product designed for an agent’s workflow

To ensure that agents can do their work with Pulumi, they need seamless access to its tools and platform. Because of this, Pulumi is rolling out free, ephemeral Pulumi Cloud accounts that an agent can spin up on its own without going through a traditional sign-up flow. An agent-registered account expires after 72 hours, but a human can claim it later to make it permanent.

The company is also publishing an npm package that turns the Pulumi CLI into a one-shot invocation: `npx pulumi <anything>` skips the install steps the binary normally requires.

A new imperative verb in the CLI, `pulumi do`, lets an agent provision a single cloud resource without scaffolding. In Plum’s example, `pulumi do create eks:Cluster` creates an Amazon EKS cluster. The operations are stateful and subject to the same policy framework as a regular Pulumi deployment, but they skip the project structure that would otherwise require the agent to infer files, directories, and tooling versions.

The company is also bringing more than 30 features from its Pulumi Cloud web console to the CLI. The list includes change history, drift detection, audit logs, secrets management, policy enforcement, and other capabilities Pulumi shipped over the last three years.

Duffy compares the result to GitHub’s `gh` CLI, which he says agents tend to reach for naturally. The CLI now also emits JSON output and structured errors, so agents can parse the response.

The idea here is to provide the agent with all the tools to step through its workflow without a human in the loop.

![](https://cdn.thenewstack.io/media/2026/05/5f4f2d62-pulumineocli_static2-1024x553.png)

## The right language for IaC

In an interview with *The New Stack*, Duffy notes that large language models are fluent in Python, TypeScript, and Go because they have been trained on vast amounts of production code in those languages. But they are less fluent in HashiCorp Configuration Language (HCL), the domain-specific language that Terraform uses, because publicly available HCL examples tend to come from tutorials rather than real production systems (since most companies have no reason to share their IaC files).

This is where Pulumi’s bet on using general-purpose programming languages is paying off, Duffy argues. As it turns out, providing an infrastructure tool that focuses on what humans want was, by coincidence, also a bet on what agents would need almost ten years after Pulumi first launched.

## A HITRUST audit and 400,000 violations

About a month after Pulumi launched its in-house infrastructure agent, Neo, in September 2025, a large healthcare customer ran an audit against the company’s policy framework to prepare for HITRUST compliance certification, Duffy says. The audit surfaced 400,000 violations. The customer had a board deadline of less than a year to clear them.

“They were kind of like, we have no hope. And then we said, well, we’ve got this thing, Neo. Without the AI, they probably had no hope,” Duffy says.

The company also points to a customer who migrated 500 Terraform workspaces to Pulumi in an hour using Neo. Many HashiCorp customers have been reevaluating their stack since the IBM acquisition.

## Day 2, too

Pulumi is also using the launch to push Neo past provisioning into ongoing operations. A new Neo Integration Catalog wires the agent into Atlassian, Datadog, Honeycomb, Linear, PagerDuty, and Supabase through remote MCP servers (with more partners on the way).

The catalog also adds a kubectl CLI integration that lets Neo act directly on running Kubernetes clusters. Scheduled Neo tasks can now run drift detection, dependency updates, and compliance audits on a cadence and ship the results as pull requests.

Duffy says the most interesting agentic infrastructure work is the boring kind. “Aside from dependency management, it’s seldom the case I go and say: across all my applications, I want to go make some giant refactoring,” he says. “But it happens all the time for infrastructure. You think of upgrading versions or changing IAM policies, or some compliance fix that I need to make globally.”

In this context, he mentions conversations with a large financial institution that needs to replace identity and access management policies across its AWS accounts. “Hundreds of thousands, if not millions, of IAM policies that need to be changed,” he says. That kind of long-horizon, high-blast-radius work, Duffy says, is the next frontier.

## And there is more

Pulumi is also moving Neo out of its own cloud console and into the surfaces where developers already work. A new pulumi neo command runs the agent from the local terminal, sharing the same agentic loop as the cloud version but with direct access to the developer’s source tree and local tools.

A Neo GitHub App lets teams ping @neo on pull requests to investigate failed deployments, propose fixes, and review changes alongside human reviewers. A Neo Slack App brings the same @neo invocation into the channels where incident threads and infrastructure conversations already happen.

Read-only Neo sessions are also new, letting teams confine the agent to inspection-only work for lower-stakes reporting and compliance checks.

Separately, Pulumi is shipping its first infrastructure-as-code providers for NVIDIA’s AI Cluster Runtime and CoreWeave’s GPU platform, aimed at AI labs and other teams running large training and inference workloads.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)