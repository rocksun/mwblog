For nearly a decade, cloud architecture has been shaped by a simple rule: Keep everything stateless. AWS Lambda and other [serverless](https://thenewstack.io/serverless/) platforms encouraged teams to carve workloads into tiny, short-lived functions with no persistent state and minimal local resources. This model scaled well, was cost-efficient and became the backbone of modern [microservices](https://thenewstack.io/microservices/).

By 2025, [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) were pushed directly into production across sectors such as finance, healthcare, energy, e-commerce and software development. As they began tackling real business workflows — investigating incidents, analyzing documents, coordinating multistep tasks, running tests or navigating internal systems — one pattern became unavoidable: The Lambda-style approach could not support them. The assumptions that made serverless attractive were exactly the assumptions agents violated.

Two lessons defined 2025 as enterprises tried to operationalize agents safely and predictably.

**Lesson 1**: Virtual private cloud (VPC) and on-premises became the default for sensitive agent workloads.

In high-stakes environments, the shift toward private cloud and on-premises execution became especially clear. Early stage experimentation with public large language model (LLM) APIs gave way to hard questions from risk, compliance and security teams: Where is the data going, who can see it, what is logged and can we enforce audit requirements? For agent workflows that touched customer information, internal APIs or sensitive documents, public endpoints were no longer acceptable.

[Snowflake](https://www.snowflake.com/?utm_content=inline+mention)’s continued 2025 expansion of [Cortex](https://thenewstack.io/stack-overflow-on-snowflake-cortex-answers-without-attitude/) illustrated how the industry responded. Historically, Snowflake operated a centralized, cloud-hosted model in which compute and storage were closely tied to Snowflake-managed infrastructure. Cortex marked a departure from that pattern. Instead of running models in Snowflake’s environment, Cortex executes directly inside a customer’s existing Snowflake VPC. That means embeddings, model inference, logs and agent-driven tool calls all stay within the enterprise’s own network perimeter. This shift was not just a convenience. Snowflake framed it as essential for industries with strict audit rules and zero tolerance for external [data movement](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/), but agentic risk management was implicit.

A similar transition was visible in other sectors. Sana’s analysis of industrial and financial deployments in late 2025 emphasized that enterprises increasingly demanded VPC or on-premises installations of their agent platforms. These organizations needed their agents to authenticate using internal identity providers, respect internal permission structures and operate entirely within pre-existing cloud security boundaries. Anything else introduced unacceptable operational and regulatory risk.

This trend reflects a broader realization: Once an agent gains the ability to interact with sensitive data or take actions within production systems, it becomes a privileged software component. And privileged systems cannot live outside the enterprise perimeter.

**Why it matters**: Enterprise AI programs [must now assume that agent workloads touching internal data](https://thenewstack.io/ai-agents-must-learn-from-chatgpts-data-wrongs/) will require VPC-native or on-premises deployment. This shift shapes vendor selection, cost planning, network architecture, identity design and how organizations structure the pipeline for agent development and monitoring.

**Lesson 2**: Agent execution moved away from stateless functions toward persistent cloud workstations.

The second defining shift of 2025 was architectural. AI agents do not operate in milliseconds. They work across sequences of steps, referring to past context, creating intermediate files, running validations, calling multiple tools and returning to tasks over extended periods. This workflow is fundamentally incompatible with the serverless assumption that nothing persists once an invocation ends.

Where traditional serverless presumes functions will run briefly, never retain local state and reload tooling each time, agent workflows require something closer to a long-lived workspace. They need stable access to their tools. They must retain context across steps. They cannot afford to rebuild their environment for every action. And they must be observable as a continuous unit of work, not a series of isolated events.

Frontier model labs demonstrated this shift throughout 2025. Public demos from OpenAI and Anthropic showed agents capable of writing and executing code, navigating browser interfaces, searching through documents and coordinating across tools. These workflows only made sense within persistent execution environments that preserved state and tooling across steps. The underlying infrastructure looked more like lightweight cloud workstations than ephemeral functions.

Research from Google DeepMind reflected the same pattern. Its tool-using agents for debugging, code execution and browser-based tasks all relied on stable environments where dependencies, caches and test runners remained available across repeated attempts. Without continuity, the workflows would fail or become prohibitively slow.

Many enterprises discovered this firsthand. Attempting to force [agents into stateless architectures](https://thenewstack.io/agents-meet-databases-the-future-of-agentic-architectures/) led to environment rebuilds, slow warm-up times, inconsistent behavior and debugging challenges. As teams embraced persistent environments, they gained predictable performance, easier troubleshooting and the ability to observe agent trajectories rather than isolated logs.

**Why it matters**: Moving to persistent execution environments changes the way organizations think about orchestration, resource management, cost and security. The core unit of compute is no longer a micro-invocation. It is a session. Enterprises need tooling that can schedule, pause, resume, audit and retire entire agent sessions while preserving isolation and governance.

## Where Cloud Architecture Is Heading

These two shifts point toward a new cloud pattern for AI agents:

1. Deployment must align with data residency, auditability and regulatory requirements.
2. Execution must support stateful, multistep workflows.
3. Orchestration must treat an agent’s full session — not individual prompt calls — as the unit of reliability and control.

This represents a departure from 10 years of cloud design built around dividing work into small, stateless pieces. Agents forced enterprises to accept a simple reality: Meaningful automation requires continuity, context and control.

Looking ahead, the organizations that adapt to this new architecture will run agents that are reliable, governed and ready for production. Those who try to stretch serverless-era patterns around agent workloads will find that their infrastructure — not their models — is the real bottleneck.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/0ec621a8-cropped-7b1a405a-abigail-wall.jpeg)

Abigail Wall is AI product and go to market leader at Runloop.AI, where she drives development of infrastructure and tools powering next-generation AI agents. She holds an M.S. in computational data analytics from Georgia Institute of Technology and an MBA...

Read more from Abigail Wall](https://thenewstack.io/author/abigail-wall/)