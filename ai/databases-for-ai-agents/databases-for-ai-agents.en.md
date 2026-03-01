In the past, we judged enterprise [databases](https://thenewstack.io/introduction-to-databases/) by how useful they were to people like us. We rated them on how well they helped architects create schemas, DBAs plan capacity, and analysts build queries.

We expected databases to last a long time — years, probably — powering sales reports and quarterly projections, growing with the organization.

> “But now comes a new kind of user: the AI agent. It has different needs. It operates at a different pace. It uses databases to do its work. But once its task is complete, the database can be discarded.”

But now comes a new kind of user: the AI agent. It has different needs. It operates at a different pace. It uses databases to do its work. But once its task is complete, the database can be discarded.

We might imagine a database designed for humans as a time-lapse cityscape viewed from above. Throughout the scene, cranes and bulldozers are busy adding and removing structures, leaving most buildings intact. The details change, but the overall shape of the city and the relationships among its parts remain relatively stable.

A database designed with agents in mind would look quite different. Rather than an interconnected network of streets and buildings — analogous to a traditional relational database — the scene is constantly shifting. Apartments and city blocks with no relation to one another pop in and out of existence faster than the eye can register. High-speed photography reveals that the structures are oddly sculpted. They’re not designed for human use. Their shape, location, and above all, their ephemerality, serve the needs of digital users.

All signs suggest that, in the near future, agents, not humans, will be the primary users of databases. So, how will databases need to change?

## Databases will need to prioritize speed over ease of use

Like humans, agents plan tasks, execute actions, observe outcomes, and adapt based on what they learn. But unlike humans, agents operate faster than thought. They don’t care about ease of use.

First and foremost, the AI agent values speed. Availability, too, and responsiveness. But speed most of all.

Agents access data continuously. They generate furious spikes in activity and discard their workspace once their work is complete. Their work “habits” strain databases optimized for the infinitely slower, more deliberate interactions of a human user.

As my colleague and cofounder Ed Huang [put it](https://www.pingcap.com/blog/agentic-ai-database-trends-that-will-define-2026/): “Agents do not slow down, and they do not optimize unless you force them to. Their natural state is a combinatorial explosion.”

A database platform designed for AI agents needs to respond as fast as AI can act.

## We will also have to build for elastic ephemerality

Typically, scaling up a cloud database involves copying entire clusters of data. As we’ve discussed [elsewhere](https://thenewstack.io/4-data-architecture-decisions-that-make-or-break-agentic-systems-2/), this is due to the limitations of enterprise networks. To keep performance high, data needs to live near compute. But replicating and persisting data takes time and adds cost.

In human-centric databases, these inefficiencies are undesirable; in AI-centric databases, they’re untenable.

> “Agents do not slow down, and they do not optimize unless you force them to. Their natural state is a combinatorial explosion.”

It’s impractical and wasteful to spin up new data clusters whenever an agent spikes CPU usage. AI-friendly databases will need to scale compute up and down while minimizing the impact on local storage and storage costs.

Architectures that separate compute from storage address this requirement directly — especially architectures like TiDB X, which uses [cloud object storage](https://thenewstack.io/object-storage-is-key-to-taming-cloud-costs/) as its backbone. In TiDB X, compute scales elastically based on workload intensity and type. Cold data remains in object storage, where costs are minimal. Frequently accessed data is cached near the computer for low-latency performance.

This [design](https://www.pingcap.com/press-release/pingcap-launches-tidb-x-new-ai-capabilities/?utm_source=chatgpt.com) supports rapid scale-up during periods of activity and rapid scale-down when demand subsides — exactly how AI works.

## And we’ll have to enforce safety through isolation

Agents can be unpredictable. They need guardrails. To support agentic users, databases must provide environments where agents can operate safely, without fear of damaging anything important.

Serverless branching can be a useful approach. A branching-capable database like TiDB Cloud can create isolated, copy-on-write environments where an agent can work with real data without fear of overwhelming the system’s capacity or corrupting data.

The [experience](https://www.pingcap.com/case-study/manus-agentic-ai-database-tidb/) of Manus, a general-purpose agentic AI platform that amassed millions of users in weeks, illustrates this well. Manus’s “Context Engineering” model generated thousands of iterations per task, each storing state as it went. This required extraordinary read/write performance.

Furthermore, Manus wanted to create agentic swarms capable of solving complex problems in parallel. Its engineering team needed to support massive concurrency while avoiding “noisy neighbor” conflicts.

But this level of concurrency would have been impossible with a non-branching architecture. With TiDB Cloud, Manus enabled each agent — or group of agents — to fork the database, run experiments, and commit results independently.

This enabled Manus’s agents to evaluate alternative approaches concurrently, compare outcomes, and retain only the results that mattered.

## Preparing for an agent-first future

Most enterprises are still in the early stages of adopting agentic AI. Yet the infrastructure choices they make now will determine the speed and success of their efforts.

As human users give way to agents, it no longer makes sense to optimize databases for durability, visibility, or ease of use. Agent thrives in environments optimized for rapid creation and teardown, object-based storage, and strong isolation. Ephemerality is the new watchword. Speed is the first priority.

Letting agents into your database doesn’t mean giving up control. It just means control will be enforced through architecture and automation rather than manual human intervention. Databases — and organizations — that embrace these principles will be able to get the most out of their agentic employees. Those who do not will inevitably [fall behind their peers](https://thenewstack.io/adopt-world-models-today-or-fall-behind-tomorrow/) in a world where AI sets the pace.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/6a7f3a53-cropped-bc64a625-max-liu.png)

Max Liu is the co-founder and CEO of TiDB, powered by PingCAP. He has more than 10 years of experience in system infrastructure and software technologies. He is the co-author of the following open source projects: TiDB, TiKV and Codis,...](https://thenewstack.io/author/max-liu/)