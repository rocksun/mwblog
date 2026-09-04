Every application has always needed a place to keep its state. That is not new. What is new is who creates that place, how many get created, and how long they have to survive after everyone has stopped looking.

> “Separating durable state from ephemeral compute is the new requirement, and the idle cost trap is only half of it.”

Consider the agents built by Kimi, the AI platform from Moonshot AI. A non-technical user describes an application in plain language. An agent builds the frontend, backend, and database, then deploys them in minutes. The user never thinks about infrastructure. They asked for a tool and received a running one.

Then the agent does something the [previous generation of coding assistants](https://thenewstack.io/inside-gemini-code-assist-googles-copilot-alternative/) never did. It does not hand over code and walk away. It keeps the application running and comes back to maintain it. That last word is where the old assumptions break. Build once and hand off, and state is almost an afterthought.

Build, deploy, and maintain across tens of millions of applications, most idle most of the time, and persistence stops being a database feature and becomes the central economic problem of the whole system.

I have written before about what happens to a database when its user is an agent rather than a human. Kimi is the clearest production example I have seen, and it surfaces a requirement that the industry has not really been asked to meet: keep state alive cheaply in two very different places at once. The problem is not performance. It is the economics of persistence.

## The number that changes the question

When you serve thousands of tenants, the questions are familiar. How fast are queries? How do we fail over? How do we back up? The industry has good answers for all of them. When you serve tens of millions, most created by agents and most idle most of the time, a different question moves to the front, and it is the one nobody planned for: what does it cost to keep something alive that nobody is using right now?

Ask it once, and you are talking about idle databases. Ask it again, one layer up, and you are talking about the agent’s own half-finished work sitting between maintenance sessions. Same question, two surfaces. At a thousand you absorb it. At ten thousand it stings. At tens of millions it is fatal.

> “In a human-driven product, what you provision and what people use track each other. In an agent-driven product, they diverge wildly.”

This is the shift agents force. In a human-driven product, what you provision and what people use track each other. In an agent-driven product, they diverge wildly, because agents create far faster and more casually than humans ever did, and most of what they create goes idle immediately.

## One principle, two places

There is a single move underneath everything that follows: separate durable state from ephemeral compute. State is the part you must never lose, so it belongs on a shared, cheap, effectively infinite foundation.

I have argued before that object storage is becoming the new network layer of the data stack, and this is what that looks like, built for agents: durable data at rest costs almost nothing. Compute is the part you should be able to throw away, summoned when work arrives and released when it stops.

Couple the two and you pay to keep compute running for state that is doing nothing. Decouple them, and your cost stops tracking how much you have created and starts tracking how much work is happening.

Every hard number in the Kimi deployment comes from getting this separation right in the two places an agent-scale product needs it: the databases the agent provisions for its users and the workspace the agent lives in.

## The first place: the idle tenant

The instinct most teams start with is the one that has worked for a decade: give each tenant its own database instance. It is clean and easy to reason about. Kimi’s earlier shape was close to this, with single-instance PostgreSQL behind the product. It works beautifully until the tenant count climbs into the tens of thousands, and then the economics invert. The reason is structural.

A per-tenant instance couples the logical experience of an isolated database to the physical reality of dedicated, always-on compute. The tenant needs the first. The business cannot afford the second at scale. Cost grows with tenants created, not tenants active, and in an agent-driven product those two numbers are worlds apart.

> “The agent experiences a dedicated, isolated database, while a virtual layer beneath provides each one its own namespace. The agent does not need a dedicated instance. It needs the experience of one.”

I have started calling this the idle cost trap, because teams walk into it without seeing it, and by the time they feel it, the architecture that created it is load-bearing. The way out is the principle. The agent experiences a dedicated, isolated database, while a virtual layer beneath provides each one its own namespace and isolation guarantees over a shared substrate, with object storage holding durable data and a routing layer sending requests where they belong. The agent does not need a dedicated instance. It needs the experience of one.

There is a catch worth being honest about. If compute is summoned on demand, then when a request arrives for an idle tenant something has to spin up, and if that is slow, you have traded a cost problem for [a latency problem](https://thenewstack.io/agentic-ai-latency-infrastructure/).

Kimi provisions a database in about a second, from a warm pool of pre-initialized resources kept ready and replenished behind each claim, so database setup drops out of the delivery pipeline entirely. That number is not a benchmark to brag about. It is the evidence that ephemeral compute over shared, persistent storage can stand in for the always-on model, because it appears fast enough to feel always-on.

## The second place: the agent’s own workspace

The maintenance half of the lifecycle drags the same problem into a place most teams never look: the agent’s own working environment. An agent that builds once can treat its workspace as disposable: spin up a sandbox, write code, ship, discard. An agent that maintains cannot work that way.

It has to return days or weeks later and pick up where it left off: source code, Git history, checkpoints, the record of what it was in the middle of doing. If that context is lost, the agent does not resume work. It is reconstructing it.

And execution environments are ephemeral on purpose, because keeping millions alive between sessions is the idle cost trap in a different costume. So the environment gets torn down. If the work goes with it, every maintenance session begins by rebuilding state the agent already had: wasted compute, wasted tokens, and a user watching an agent relearn its own project.

The fix is the same separation, one layer up. Kimi uses a persistent filesystem that keeps development state alive independently of the compute that produced it. Source code, Git history, checkpoints, and task progress persist after the environment is destroyed, so the agent resumes rather than starting over. Compute is ephemeral and cheap to discard. State is durable and cheap to keep. Same trade as the idle tenant, seen from the builder’s side.

## The database choice becomes a quality input

There is a further effect that surprised me, because it shows up in the quality of what the agent builds. Every infrastructure decision is a chance to get something wrong. If each task forces the agent to reason from scratch about which database to use and how to configure it, it is improvising on every run, and improvisation is where errors enter.

When the stack is unified, it applies known-good patterns instead. Kimi saw [code generation](https://thenewstack.io/ai-agents-software-engineering/) success rates improve from standardizing on a unified data layer, and that is the mechanism: fewer places for the output to go wrong.

> “The choice of database is no longer just an infrastructure decision. It is a quality input to the agent’s work.”

This is a version of an argument I keep returning to. Agents need guardrails, and the most effective ones are built into the infrastructure rather than bolted on as instructions. A database that behaves consistently every time is a guardrail. The choice of database is no longer just an infrastructure decision. It is a quality input to the agent’s work.

## Four properties that have never been requried together

Step back from Kimi and the shape of the requirement is clear. An agent-scale product needs four things from its data layer at once:

* **Tenant isolation:** every agent-created database must be logically separate, so millions of tenants never bleed into one another.
* **Instant provisioning:** a new tenant has to exist in about a second, because an agent will not wait and neither will the user behind it.
* **Cost elasticity:** an idle tenant, and an idle workspace, has to cost almost nothing, because most things are idle most of the time.
* **Persistent state independent of compute:** the tenant’s data and the agent’s development state alike must survive the ephemeral environments that produced them.

Each has been solved before in isolation. Databases have offered isolation for decades. Serverless systems provision quickly. Object storage is cheap at rest. What is new is the demand for all four at once, at a scale where any one failing breaks the product. That is the real [infrastructure competition of the agent era](https://thenewstack.io/ai-ready-infrastructure/), and it is not the one the industry is used to having. It is not about who has the fastest single query. It is about who can hold all four together at tens of millions of tenants without one collapsing the others.

## The pattern is bigger than one product

I do not think Kimi is a special case. It is an early, unusually clear instance of a pattern that will repeat across every product where agents build for non-technical users at scale. The shape is always the same. One agent, one workspace, one database, repeated millions of times. Each instance feels independent.

The infrastructure underneath is shared, and it works only because a virtual layer separates the logical experience of isolation from the physical cost of compute, and because durable state is allowed to outlive the compute that produced it.

Kimi is the version where the agent hands a finished application to an end user and then stays on to maintain it, which is harder in two ways at once. The tenant does not go away when the run ends; it persists, idle, waiting, multiplied by tens of millions. And the agent does not go away either, so its own working state has to survive every gap between sessions. Persistence is no longer a property of one component. It is the property the whole system is organized around.

> “The database conversation in the agent era is no longer really about speed. Get it wrong, and no amount of model quality will save the margins.”

Teams building in this direction will hit the idle cost trap on both surfaces, whether they plan for it or not. The only choice is whether they see it coming. Design for all four from the start and you scale past the point where the per-tenant-instance model collapses. Do not, and you hit that ceiling at tens of thousands of tenants, exactly where Kimi’s earlier architecture did, and sooner than you expect, because agents fill a tenant table faster than any human-driven product ever has.

The database conversation in the agent era is no longer really about speed. It is about whether the economics of persistence can survive the scale that agents create in both the database and the workspace. Get that right early, and the rest of the product has room to grow. Get it wrong, and no amount of model quality will save the margins.

If you are building a product where agents provision infrastructure for end users and then stay on to maintain it, four things make that economically viable: isolation, instant provisioning, near-zero idle cost, and durable state on a shared substrate. That is what we have built into TiDB’s serverless and agent workloads. It is the pattern these teams keep arriving at from different directions.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/6a7f3a53-cropped-bc64a625-max-liu.png)

Max Liu is the co-founder and CEO of TiDB, powered by PingCAP. He has more than 10 years of experience in system infrastructure and software technologies. He is the co-author of the following open source projects: TiDB, TiKV and Codis,...](https://thenewstack.io/author/max-liu/)