Lauren Tan, an engineer on the Grok team at SpaceXAI, who previously worked at Cursor and Meta, recently published a guide to her personal agent workflow: pstack. The attention-grabbing number is that pstack has let her [ship 2,000 pull requests (PRs) a month to production with high confidence](https://x.com/poteto/status/2094457600259842065). That’s one engineer shipping nearly 100 PRs per working day.

The number is incredible and undeniably an outlier, but the direction is not a surprise. I have argued previously that coding agents would [enable teams to generate ten times the code with similar headcounts](https://thenewstack.io/coding-agents-cicd-fix/). What is surprising is that these are not just code output numbers. These are actual changes landing in production.

According to Tan, the most critical piece of that workflow is verification. A verification skill lets an agent check its own work and keep going until the task is done, and she treats it as “critical infrastructure” rather than one skill among many.

The verification skill rests on something underneath it: a rich runtime the agent can drive, inspect, and get structured answers from. For a single application, that runtime is the application itself, started on demand. For a system made of dozens or hundreds of services, no such runtime exists by default, and providing one that keeps up with hundreds of parallel agents is the hard part.

## Verification is the whole game, and the math says so

Her argument for agentic verification is a throughput argument. An agent that can check its own output keeps working until the task is done. An agent that can’t hand you a diff and wait makes you the slowest component in the loop. That is why she claims strong verification skills can multiply a team’s output by 100 to 1,000 times.

> “An agent that can check its own output keeps working until the task is done. An agent that can’t hand you a diff and wait makes you the slowest component in the loop.”

At [2,000 pull requests a month](https://thenewstack.io/ai-generated-code-crisis/), reviewing every change by hand would allow about five minutes per PR across a full working month. Human review cannot be the verification layer at that volume. Whatever does the checking has to run without a person in the loop, and it has to run in parallel with the agents generating the work.

## The model assumes the agent can run the whole application

The verification skill she describes generates a command line interface (CLI) and a feature map for the application. The CLI lets an agent start the app, navigate it, inspect state, and read structured JSON results back. Each agent gets a complete copy of the application and can test a change end to end.

She is direct about how much rests on that runtime: “I personally feel that agentic verification is so important that I would unironically suggest building your own rich debugging tools, or even choosing a different tech stack, in order to have unfair advantages and extreme productivity in building software.”

Her approach to providing a [runtime for her agent](https://thenewstack.io/agent-runtime-application-server/) works because the application fits in one process. A frontend, a compiler, or a single service with a database can start from a CLI in seconds and be thrown away afterward.

> “I would unironically suggest building your own rich debugging tools, or even choosing a different tech stack, in order to have unfair advantages and extreme productivity in building software.”

For teams building complex distributed applications, their system does not have that property. The application is the interaction between an order service, a payments service, an inventory service, a queue, several databases, and a handful of third-party APIs. At larger shops, the count runs into the thousands. A pull request to one service is only verified by exercising the calls it makes and receives. The CLI can start the changed service. It cannot start the system.

## None of the existing runtimes survive hundreds of parallel agents

Local runtimes with mocks are cheap and can run fully parallel using worktrees or CDEs. Their problem is fidelity. Mocks encode what a dependency did the last time someone looked, and they drift the moment the real service changes. An agent that verifies against mocks closes its loop against fiction, and the failure shows up after merge.

A full copy of the stack per change is faithful and isolated. But its cost scales with the number of services times the number of concurrent changes, and at hundreds of agents that cost is untenable. Time is the bigger problem. A full stack takes minutes to provision, and the loop she describes has the agent testing every iteration of a change while it is still working on it. An environment that is ready after the agent has moved on to its next attempt is no use to it.

Shared staging is faithful and cheap because there is one of it, and that is the whole problem. A single mutable environment cannot host hundreds of concurrent changes. Agents overwrite each other’s deployments, a broken change from one agent becomes failed tests for every other agent, and the loop-closing property that makes the workflow valuable disappears.

![Each existing verification runtime plotted on a chart showing its realism of dependencies against concurrency.](https://cdn.thenewstack.io/media/2026/09/bd6d419a-image-1024x579.png)

## What verification needs when the callers are agents

Read Lauren’s workflow as a requirements document, and five properties emerge:

* The change has to run against real dependencies or the verification means nothing.
* Hundreds of concurrent changes have to be unable to see each other.
* The cost of an environment has to scale with the size of the change, not the size of the system.
* Environments have to come up in seconds, because an agent waiting on provisioning is parallelism you paid for but didn’t use.
* All of it has to be reachable through the [CLI or MCP server](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/) the agent already uses, because the caller is an agent.

The first and third requirements pull in opposite directions. Realism pushes toward complete copies of the system. Cost pushes toward sharing as much as possible. Shared staging resolves that tension by giving up isolation, and a per-change full stack resolves it by giving up cost efficiency. A design that satisfies all five has to share and isolate at the same time.

## Virtualized full-stack environments share the system and isolate the change

The architecture that does this treats an environment as a view of a running system rather than a copy. One shared set of stable services runs continuously, deployed from the main branch and kept healthy the way production is. When an agent needs to verify a change, it runs only the service it modified, on its own machine or as a lightweight deployment in the cluster, and joins it to the shared stack as a new isolated environment.

> “The architecture that does this treats an environment as a view of a running system rather than a copy.”

From inside that environment, the changed service is the version of record, and every other call falls through to the shared stable versions. The agent sees a complete, realistic system, and so do the other hundred agents, each seeing a system that differs from the baseline by only the delta of its own change. Requests carry their environment identity as they cross service boundaries, which keeps one agent’s traffic from reaching another agent’s version under test. Stateful side effects that cannot be shared safely, like queue topics or writable databases, get a per-environment copy where needed.

![Diagram showing "agent 1 env" and "agent 2 env" interacting with the shared cluster.](https://cdn.thenewstack.io/media/2026/09/1b47c76e-image-1024x530.png)

The cost model follows directly. An environment costs one or two running services instead of sixty; it is ready in the time a single service takes to start, and you can create and destroy it from inside the agent’s own loop. This is the [pattern Signadot packages for Kubernetes](https://thenewstack.io/kubernetes-native-ai-infrastructure/), with the shared stable stack running in the team’s existing cluster.

## The loop, end to end, with an agent as the actor

Put the two halves together, and the workflow that enables her to ship 2,000 PRs a month to production carries over to a distributed system almost unchanged. An agent picks up a task and changes one service. It asks for an environment for that change and gets one in the time it takes its service to start. It then drives real requests through the system’s entry point and watches them traverse the real dependency graph, with only its own service running new code. It reads structured results, fixes what failed, and runs again. When the checks pass, it opens the PR, and the environment goes away at merge.

> “Environments stop being something the platform team hands out and become something agents create, use, and discard as needed.”

For the platform team, the unit of work changes. Today it provisions environments, whether that means keeping a shared staging alive or stamping out full copies of it. In this model, it runs one shared stable stack and the layer that virtualizes it: context propagation across every service, isolation for the stateful dependencies that cannot be shared, and the tooling that creates and tears down environments. Environments stop being something the platform team hands out and become something agents create, use, and discard as needed.

## Verification capacity is the new ceiling on throughput

Lauren Tan’s post is not a story about one unusually productive engineer. It shows what happens when agents run the full loop, writing a change, verifying it, and iterating without a person in between. The verification infrastructure is the foundation that the entire loop stands on.

In distributed applications, that infrastructure has to be a runtime environment that gives every agent real dependencies, keeps hundreds of concurrent changes from seeing each other, costs a change rather than a copy of the system, and is ready in the seconds an agent is willing to wait. That is what turns agent parallelism into shipped code rather than a longer review queue. That model of runtime environments is exactly what we built [Signadot](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q3_26_sponsored_content) to enable.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)