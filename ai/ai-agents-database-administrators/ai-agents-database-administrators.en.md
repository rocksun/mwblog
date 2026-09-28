**The database administrator of the future** will spend considerably less time administering databases.

That sounds contradictory, but AI agents are taking over that work. For decades, DBAs have handled the decidedly hands-on work of keeping databases available, performant, secure, and affordable. They provision capacity, troubleshoot slow queries, manage migrations, and step in when something inevitably goes sideways.

AI is already taking on some of that work. At the same time, it is creating a much bigger data infrastructure fleet to manage.

The result is likely to be a very different kind of DBA: one who spends less time tending individual databases and more time supervising the autonomous systems doing it for them.

## **Congratulations, you’re managing robots now**

This shift starts with a familiar problem: more infrastructure needs managing than the people available to manage it.

Database automation is hardly new, but agents can potentially go further than the scripts and rules DBAs already rely on. Rather than automating one predetermined task, an agent can inspect what is happening, decide what needs attention, use tools to act on it, and check whether its intervention worked.

That changes the DBA’s relationship with the database. A performance problem that once required someone to dig through metrics, identify the troublesome query, and decide how to respond could increasingly be investigated by an agent before a human gets involved.

It doesn’t remove the DBA from the equation. Someone still has to decide what an agent can do, where human approval is required, and what happens when it gets something wrong. But the work moves up a layer. Instead of personally performing every operational task, DBAs start managing the systems carrying them out.

> Instead of personally performing every operational task, DBAs start managing the systems carrying them out.

And before anyone gets too comfortable with that idea, the number of those systems could become enormous.

## **150,000 agents walk into a database…**

Gartner predicts that the average global Fortune 500 company will have more than 150,000 AI agents in use by 2028, up from fewer than 15 in 2025. Only 13% of organizations currently believe they have the right governance in place to manage them.

Not every agent will need its own database, but plenty will. They will create state, retrieve data, remember previous interactions, and exchange information with other agents. Many will also behave very differently from the applications DBAs are used to supporting: spinning up quickly, sitting idle for long stretches, and suddenly becoming busy when there is work to do.

Nobody is hiring 150,000 DBAs to manage them.

---

**That is the scale problem [Yugabyte](https://www.yugabyte.com/) is targeting with [YugabyteDB AMP](https://www.yugabyte.com/amp/), or Agentic Multitenant PostgreSQL.** Rather than treating each new agent workload as another database for an administrator to provision and babysit, AMP manages databases as a fleet.

The platform packs hundreds of small Postgres workloads onto shared distributed infrastructure while keeping their databases isolated. Lifecycle operations, including provisioning, branching, scaling, migration, and teardown, can be exposed to agents through MCP. Yugabyte has also built specialized agents for setup, migration, performance tuning, and integrations.

In that model, a DBA is no longer provisioning database number 14,372. The interesting job is setting the rules for how database number 14,372 is provisioned, operated, and fine-tuned without them.

## **Do more with less (no, really)**

Scale is only half of the problem. Someone also has to pay for all this stuff.

Agent workloads make traditional capacity planning particularly awkward because many are bursty and frequently idle. Giving every experimental agent permanently provisioned infrastructure could leave companies paying for many databases that spend much of their lives doing very little.

This is where consolidation becomes as much an economic question as an operational one.

AMP’s approach is serverless multitenancy and scale-to-zero. Multiple small workloads share the underlying distributed infrastructure, while customers pay by CPU minute and idle agents consume no compute. Resource governance can impose CPU limits on individual workloads, preventing a single overeager agent from consuming the capacity intended for its neighbors.

The human equivalent matters too. If routine setup, migrations, tuning and other database operations can increasingly be delegated, a smaller database team can potentially look after a much larger estate.

That doesn’t mean companies get to fire the DBAs and hand the keys to the robots. It means scarce database expertise can be spent on architecture, governance, and genuinely difficult problems instead of repeatedly doing the work that software can handle.

## **Your 2028 database problem starts now**

The harder question is what to build underneath all of this when nobody really knows what the enterprise AI estate will look like in two years.

An agent that begins as an experiment today could disappear next month. Another could suddenly become a production application used across the business. Building one infrastructure stack for cheap experiments and another for serious workloads risks creating a migration problem every time an experiment succeeds.

Yugabyte bets that both ends of that journey should sit on the same foundation.

YugabyteDB AMP lets workloads start on serverless Postgres and transition to fully distributed YugabyteDB as their scale and criticality increase, without rewriting the application or migrating data to a different database platform.

Then there is the problem above the individual database: agents need to remember what happened, and not just in a silo.

That’s where [**Meko**](https://mekodata.ai/) fits into the Yugabyte stack. Meko is an agent-native context engine designed for multi-agent AI systems. It provides persistent memory, shared knowledge, decision traces, and autidability across multiple agents, rather than leaving each agent working from its own isolated context. An agent can pick up information learned by another agent instead of retrieving it again or restarting the reasoning process.

Taken together, it delivers a single data stack for an agent’s entire lifecycle: Meko for the context shared among agents, YugabyteDB AMP for agentically managing fleets of Postgres databases, and distributed Postgres-compatible YugabyteDB for workloads that outgrow their serverless beginnings.

Of course, there’s no guarantee that 2028 will look exactly like today’s forecasts. That’s rather the point. The safest architectural bet may be one that doesn’t require you to know in advance which of today’s tiny AI experiments will become tomorrow’s critical applications.

The DBA is still critical in that world, but the job will look different. The DBA of the future may manage fewer databases directly, while taking responsibility for vastly more of them. Instead, managing the autonomous systems that do the administering.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)