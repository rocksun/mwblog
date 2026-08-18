Multi-tenancy has moved in one direction for 60 years: the tenant keeps getting smaller. Mainframe time-sharing carved a single machine into slices so an organization’s departments could share it, and the tenant was the org. Virtualization gave each team its own fleet of virtual machines, and the tenant became the team. Containers and Kubernetes namespaces shrank it again, until a platform team could hand every developer an isolated environment on a shared cluster.

That last step, an environment per developer, became the target state of platform engineering in the 2020s. A namespace per developer, capacity planned by seat, golden paths sized to headcount. Underneath all of it sits one assumption: a person produces one stream of work at a time, so isolating people isolates work.

Coding agents broke that assumption. A developer running five agent sessions has five changes in flight at once, each needing its own working version of the system. Anthropic’s engineers, building a C compiler with a fleet of parallel agents, [ran nearly 2,000 Claude Code sessions across two weeks](https://www.anthropic.com/engineering/building-c-compiler). Cursor’s documentation tells developers to [run as many agents as you want in parallel](https://cursor.com/docs/background-agent). None of those concurrent workstreams is a person.

> “The tenant has shrunk one more time. It is no longer the developer. It is the change.”

The tenant has shrunk one more time. It is no longer the developer (or even the agent). It is the change.

## Tenancy demand scales with changes in flight, not headcount

Capacity planning by seat worked because changes arrived at human pace, roughly one per developer at a time. That denominator is gone. A Microsoft study of command-line coding agent adoption found that developers [merged roughly 24% more pull requests](https://arxiv.org/abs/2607.01418) over four months, and merged pull requests understate the pressure. Every change that reaches merge is preceded by iterations and abandoned attempts, and each of those also needed somewhere to run.

Run the seat math against the change math. A 50-developer organization where each engineer supervises a few agent sessions has hundreds of changes in some stage of validation on a busy day. Each one wants data it can migrate and write to without asking permission, its own view of shared message topics, and a running version of the services it touched. That is the demand of a 300-person (or more) engineering org on a 50-tenant platform.

Every layer built on the person-tenant assumption misprices this. A per-developer namespace hands one tenant slot to what is now five concurrent workstreams. Shared staging serializes all of them into a single queue. Seat-based capacity plans budget for the number of employees while the bill tracks the number of changes in flight.

## The new tenant is the change, not the agent

The tempting candidate for the new tenant is the agent, and it is the wrong one. Agents are interchangeable workers. Two agents can collaborate on one change, one agent can rotate through five changes, and a crashed agent gets replaced mid-task without anything downstream noticing. Give each agent its own environment, and you have repeated the old mistake at a new scale: isolating workers when the thing that must not leak is work.

> “Give each agent its own environment, and you have repeated the old mistake at a new scale: isolating workers when the thing that must not leak is work.”

The durable unit is the change. It comes into existence when work on it starts. It accumulates state that no other tenant should see: a schema migration, test writes, new versions of one or two services, the messages it produced during validation. It needs to [observe a version of the system](https://thenewstack.io/debugging-observable-ai-systems/) that includes its own edits and nobody else’s. And it is torn down when it merges or is abandoned, taking all of that state with it.

![Diagram showing a company's growing tenant count](https://cdn.thenewstack.io/media/2026/08/99d0b0f7-image-1024x476.png)

Naming the change as the tenant turns a vague scaling problem into a design target, because change-level tenancy has three requirements that person-level tenancy never had to meet:

* Creating a tenant must be near free.
* Isolation must cover only what changed.
* The tenant’s lifecycle must be bound to the change itself, not to a ticket or a timer.

## Platform teams already run this playbook in production

The discipline these requirements call for is not new. Anyone operating a multi-tenant production service already knows the rules: tenants share the substrate, each tenant privately owns only what makes it distinct, creating a tenant is self-service and cheap, and a tenant’s resources are reclaimed the moment it leaves. Nobody stands up a private copy of the product per customer, and nobody files a ticket to onboard one.

Those same organizations run pre-production on the opposite rules. Environments are provisioned by ticket or by seat, capacity is planned per person, and isolation is achieved by duplicating the stack when it is achieved at all. The multi-tenancy playbook that runs the product has never been applied to the platform that builds the product.

Change-level tenancy is that playbook, applied. Treat every change as a [tenant of the development platform](https://thenewstack.io/tenants-the-missing-backbone-of-modern-developer-platforms/), and the three requirements stop being novel. They are the standard properties of any competently run multi-tenant system.

## The tenant owns what changed and shares everything else

A SaaS tenant owns its data and configuration, never a copy of the application. A change tenant is sized the same way. It owns the one or two services it modified and an isolated database branch it can migrate and write against, and nothing else. Everything the change did not touch resolves against one shared stable environment, continuously deployed from main, so every tenant validates against real, current dependencies without owning a copy of them.

A footprint that small makes tenant creation nearly free, and creation cost is what decides whether the model scales to agent demand. Isolated data no longer requires copying a database: Neon and Xata create copy-on-write branches in seconds regardless of dataset size, consuming storage only for the data that diverges. The runtime side costs one deployment, because starting the modified services is all that is left to do. A tenant that costs one deployment can be created hundreds of times a day.

![Diagram showing how each tenant only contains what changed, while stable environments are shared between tenants](https://cdn.thenewstack.io/media/2026/08/dc541baa-image-1024x563.png)

## Tenants onboard and offboard themselves

Multi-tenant platforms scale because nobody provisions tenants by hand. Signup creates the tenant, cancellation removes it, and no operator sits in the loop. Change tenants need the same contract. The tenant comes into existence when work on the change starts and disappears when the change merges or is abandoned, with no ticket at the front and no cleanup script at the back.

Offboarding is the half that platform teams underestimate. At person scale, an orphaned environment was a minor waste found in a quarterly cleanup. At change scale, orphans accumulate as fast as agents abandon experiments, and the leak outgrows the cleanup.

Automatic offboarding also keeps the accounting accurate. When tenants are created and destroyed by the change’s own lifecycle events, the number of live tenants equals the number of changes in flight, and platform capacity becomes a quantity you can measure and plan against instead of a pile of environments nobody is sure anyone still uses.

## Re-measure the platform in changes, not seats

The practical shift for platform teams starts with measurement. Count changes in flight at peak, not seats: [open pull requests](https://thenewstack.io/ai-generated-code-crisis/) with activity in the last day is a fine proxy, and for most teams the number is already several times headcount. Then price the marginal tenant: What does one more concurrent change cost in dollars and in minutes of setup? If the answer is a full environment and tens of minutes, the platform is still doing person-level tenancy.

Those two numbers expose where the old assumptions live. Namespace quotas sized per developer, staging booked by team calendar, database seeds refreshed nightly for everybody at once: each is a seat-denominated policy waiting to fail under change-denominated load. The fix in every case is the same three requirements: near-free creation, isolation sized to the change, lifecycle bound to the change, applied to whichever part of the platform still assumes the tenant is a person.

## Change-level tenancy is the prerequisite for an agent-native SDLC

Every previous definition of the tenant named a person or a group of people, and that held because only people produced changes. A platform could equate one seat with one workstream, plan capacity from the hiring plan, and keep a human in the provisioning loop. [Coding agents break](https://thenewstack.io/coding-agents-cicd-fix/) all three of those properties at once: one person now operates several concurrent workstreams, those workstreams are created and abandoned at machine pace, and no human is positioned to provision or clean up each one.

> “The change is the only unit of isolation that stays stable when the workers become software.”

That is why the software development lifecycle (SDLC) needs its tenant redefined around the change rather than around whoever, or whatever, wrote the code: the change is the only unit of isolation that stays stable when the workers become software.

Organizations that keep person-sized tenancy will watch agent-generated changes queue behind infrastructure built for a fraction of the load. The ones that re-platform around the change will convert agent throughput into merged work. If you’re exploring the second path, that is exactly what [we built Signadot to support.](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q3_26_sponsored_content)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/b231156a-arjun-iyer.jpg)

Arjun Iyer, CEO of Signadot, is a seasoned expert in the cloud native realm with a deep passion for enhancing the developer experience. Boasting over 25 years of industry experience, Arjun has a rich history of developing internet-scale software and...

Read more from Arjun Iyer](https://thenewstack.io/author/arjun-iyer/)