Every few months, a new technology gets its premature obituary. Across many developer circles, MCP’s has already been written. Too much overhead and complexity are to blame. For certain small-scale use cases, the skeptics have a point, but their argument breaks down when you move beyond a solo project into the kind of agentic systems that enterprises are trying to build.

## Where the skeptics have a point

When you are the only user and trust is implicit, using an MCP server can add unnecessary complexity. A direct API call is the simpler and often better choice for wiring up a local AI assistant, building a personal automation, or running an isolated script on your own virtual machine. Developers are not wrong in that context.

## Where the argument falls apart

Enterprise agentic systems are not single-developer, single-trust-boundary setups. Agents operate across teams, systems, and organizations, often acting on behalf of users who are not even aware an agent is involved. In those environments, direct API calls start creating problems that no allowlist can reliably solve.

> “Every few months, a new technology gets its premature obituary. Across many developer circles, MCP’s has already been written.”

Credential delegation is one of the first friction points. Building a platform that runs agents on behalf of enterprise customers quickly leads to questions about agent identity, permission inheritance, and whether it runs as a service account. There is no universal right answer, but the wrong choice carries consequences.

An agent with excessive access creates [audit and compliance exposure](https://thenewstack.io/agentic-cicd-audit-compliance-gap/). While insufficient access causes the agent to fail silently, it erodes platform trust over time. Enterprise buyers in regulated industries raise this concern before the formal security review.

In regulated environments, “the AI did it” is not a sufficient audit entry. Teams need to answer what the agent did, on whose behalf, and under what authority. That information needs to be embedded in the system by design, not reconstructed from logs after an incident. A direct API integration can’t provide this, but a well-implemented MCP setup can. It surfaces the necessary context at the tool-call level, capturing which server, credentials, and scope authorized each action.

## An allowlist isn’t governance

When someone asks whether an agent can access things it should not, the instinct is to reach for an allowlist. Define the permitted tools, check against it before executing, complete the task, and move on. This approach feels like governance because it resembles a policy. A policy, however, is only as strong as the system enforcing it. In practice, allowlists break down through misconfiguration, unexpected agent behavior, and edge cases nobody anticipated when the list was originally written.

> “In regulated environments, “the AI did it” is not a sufficient audit entry.”

The more durable option is the structural least privilege. When an [agent’s MCP connection](https://thenewstack.io/mcp-security-risks-multiply-with-each-new-agent-connection/) only exposes the tools required for its specific task, the agent cannot exceed that scope. For security teams in regulated environments, “it structurally cannot exceed its scope” and “it follows the rules” are meaningfully different assurances.

## What still needs work

MCP still creates friction in two areas.

> “For security teams in regulated environments, “it structurally cannot exceed its scope” and “it follows the rules” are meaningfully different assurances.”

Capability-scoped server provisioning remains too manual. When proper configuration requires deep infrastructure knowledge, administrators often skip it and fall back on broad connections with an allowlist as a backstop. Until the industry makes provisioning accessible to non-specialists, broader adoption will stall.

The operational layer for managing MCP connections needs to be accessible to security and platform teams, not just the developers who originally built the integration. An administrator should be able to view every active connection in their environment, understand what each one exposes, and identify who is using it, all without reading a config file or tracking down the original implementer.

For organizations deploying [agents at scale](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/), these requirements are table stakes.

## What enterprise scale actually demands

The conditions that expose a weak governance model announce themselves through incidents. Autonomous agents operating at enterprise scale will find the gaps before you do. If the honest answer is still “we have an allowlist,” the next step is clear. Audit what your agents can access, map it against what they need, and build structural controls before gaps become incidents.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/72048260-amanda-rueda-600x600.jpeg)

Amanda Rueda is a staff product manager, AI Execution, at GitLab.

Read more from Amanda Rueda](https://thenewstack.io/author/amanda-rueda/)