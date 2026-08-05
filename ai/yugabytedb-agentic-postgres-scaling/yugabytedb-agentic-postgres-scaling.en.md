**The next database scaling problem** may not be how big a database gets, but how many databases an enterprise suddenly has to run.

That’s the inspiration behind YugabyteDB AMP, or Agentic Multitenant Postgres, a new serverless PostgreSQL tier designed for a world in which companies could be running hundreds or thousands of AI agents, each generating its own data layer demands. For [Yugabyte](https://www.yugabyte.com/), that means rethinking what scale looks like.

[Karthik Ranganathan](https://www.linkedin.com/in/kranganathan), co-founder and co-CEO of [Yugabyte](https://www.yugabyte.com/), tells *The New Stack*, “The dimension of scale is shifting. It’s not just large databases; it’s also a proliferation of databases.”

> “The dimension of scale is shifting. It’s not just large databases; it’s also a proliferation of databases.”

[YugabyteDB AMP](https://www.yugabyte.com/amp/) extends Yugabyte’s reach to the smaller end of that spectrum, while maintaining the distributed architecture the company has traditionally built for large, mission-critical workloads. It uses serverless multitenancy and what Yugabyte calls Enhanced Colocation to pack hundreds of workloads onto shared infrastructure, while giving each agent an isolated PostgreSQL database.

The economics make sense for fleets of databases, including those that underpin AI agents. An experimental agent might hammer its database for a few minutes, and then the database might sit untouched for days or even be destroyed after the task was completed. YugabyteDB AMP scales to zero when that workload is idle and charges by CPU minute when it is running.

Yugabyte is also seeing another problem will appear alongside all those databases: the need for someone (or something) to manage them.

## **Four agents walk into a database**

YugabyteDB AMP ships with four custom built-in agents: Architect, Voyager, Perf Advisor, and Nexus.

Yes, Yugabyte’s answer to the infrastructure needed by AI agents is, in part, more AI agents.

YugabyteDB Architect handles database creation and provisioning. A company might have rules about where development and staging databases live, how much compute they receive, or whether a particular workload needs to span multiple regions. Architect retains that organizational context and applies it when an agent asks for infrastructure.

> “There’s a lot of context that we build up as humans that needs to get harnessed by this agent.”

“It needs to have context about your organization, about your specific group, about the details of your application,” Ranganathan says. “There’s a lot of context that we build up as humans that needs to get harnessed by this agent.”

YugabyteDB Voyager handles migration and modernization. It’s designed to bring existing databases into the fold. Voyager works out sizing and scaling requirements, as well as any changes needed to move workloads from other databases onto PostgreSQL.

Then there’s YugabyteDB Perf Advisor, which looks after databases once they are running. It can investigate an outage or performance problem, search information about the database and its environment, and attempt to determine the root cause. Yugabyte also wants it to catch problems earlier, including warning developers when a query is likely to cause trouble before it reaches production.

Finally, YugabyteDB Nexus handles the ecosystem around the database: connecting it to warehouses, data streams, key management systems, and other external infrastructure.

Ranganathan says those four agents are just the starting point: “These were the four that it ships with today, with the substrate to be able to do more.”

The more interesting part is what sits between them. The agents share context about the organization and maintain a record of why they made particular decisions. If somebody later asks, as Ranganathan puts it, “What the hell was that?” Yugabyte wants you to be able to reconstruct what happened.

> “This is what the person said. This is what your context said. This is what I inferred. This is what I ended up doing.”

“This is what the person said. This is what your context said. This is what I inferred. This is what I ended up doing,” he says, describing the decision traces [Meko](https://mekodata.ai/) maintains around agent actions for YugabyteDB AMP.

## **Giving agents the keys, with conditions**

There is an obvious catch to letting AI agents provision, tune, and otherwise fiddle with databases: sometimes they do stupid things.

Ranganathan describes the autonomy YugabyteDB AMP gives its agents as a “guarded amount of freedom,” with the level of control depending on the environment.

A disposable development database might be configured so the agent can get on with the job without repeatedly asking permission. A production system holding financial information would be treated very differently.

“There would be a dry run mode. It’ll tell you what it wants to do,” he says. “So you can always say, ‘Ask me permission before you do something, and ask me permission, especially if the operations fall in this category.’”

He doesn’t pretend those controls make mistakes impossible. “It’s how you configure and use the thing that matters.”

## **What happens if the prototype actually works?**

There is another problem YugabyteDB is trying to support: successful experiments.

Teams can start an AI project on a small serverless database because it’s cheap and convenient. Auto-scaling down to fractional vCPUs keeps those early-stage deployments inexpensive, while database branching lets developers spin up isolated copies to test new ideas, agents, or features without affecting production.

If the application becomes heavily used or business-critical, however, the infrastructure it started with may no longer be enough. YugabyteDB AMP is designed so that developers don’t have to switch databases at that point.

As the workload grows, YugabyteDB can move to YSQL, its distributed PostgreSQL layer, adding horizontal write scaling, multi-master replication and geo-distribution. Yugabyte says this doesn’t require an application rewrite or a conventional database migration, and that the agent continues to connect in the same way.

It will also give companies some choice about where all this runs. YugabyteDB AMP can operate inside a customer’s own cloud, connected back to YugabyteDB’s control plane. Yugabyte calls the latter BYOC, or bring your own cloud. Future deployment options will include an unsharded PostgreSQL managed service.

The idea is that metering, management, and learnings can still flow through the control plane while the customer’s data remains in its own environment. “We still want it to be secure enough and for customers to feel secure enough to run it wherever their data is,” Ranganathan says.

## **How Yugabyte manages its own database sprawl**

YugabyteDB AMP is still in its early stages and isn’t broadly available yet. Yugabyte is using it internally and has opened it up to a small number of selected partners, with wider availability expected soon.

The company is already running agents internally for coding, support, and go-to-market work. Its support agent is called Hagen, while Growth Vector handles go-to-market tasks. YugabyteDB AMP is also being used for development, and Ranganathan says Yugabyte is starting to move other internal databases onto it.

“We’re trying to consolidate all our databases as well,” he says. “Same problem, right?”

Whether most enterprises end up with [enormous fleets of agents with enormous fleets of databases](https://www.yugabyte.com/blog/data-backbone-for-thousands-of-agents/) remains an open question. The agent market is still moving quickly enough that today’s indispensable architecture can become tomorrow’s abandoned experiment.

Yugabyte doesn’t need every agent to survive for YugabyteDB AMP’s premise to make sense, though. Quite the opposite. Its bet is that companies will create lots of them; most will spend time doing nothing; some will disappear; and a small number will unexpectedly become important.

If that happens, the database problem becomes less about finding somewhere to put one enormous workload and more about keeping track of many little ones.

And if humans can’t reasonably manage them all, Yugabyte already has four agents volunteering for the job.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)