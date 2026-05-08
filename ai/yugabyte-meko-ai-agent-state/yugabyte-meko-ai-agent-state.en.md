Roughly 37% of multi-agent system failures aren’t reasoning failures — they’re state failures. Agents working from inconsistent views of what’s already happened, what’s currently true, and what’s already been decided. The MAST taxonomy from Cemri et al. is the first systematic look at this, and the number is a wake-up call: The bottleneck in agentic systems isn’t the model. It’s the memory layer underneath it.

That’s the tension **[Yugabyte](https://www.yugabyte.com/)** is trying to tap into with the launch of **[Meko](http://mekodata.ai/)**, an open source, agent-native data infrastructure aimed at one of the least glamorous, most stubborn problems in modern agentic AI systems: state.

> “It is the state. It is very difficult to manage the state and keep it on point and actually transfer everything.”

For all the noise around models, prompts, and orchestration frameworks, [Karthik Ranganathan](http://linkedin.com/in/kranganathan), co-founder and co-CEO of Yugabyte, tells *The New Stack* that most teams building AI agents are tripping over something far more mundane.

“It is the state,” he says. “It is very difficult to manage the state and keep it on point and actually transfer everything.”

It’s not the part people get excited about. But once you’re running this stuff for real, the cracks tend to show up in the data layer, not the models.

## **When the DIY stack stops being cute**

Most teams working on agentic AI right now are doing what developers usually do, pulling together a stack from tools they already know. A relational database, a vector store, and some object storage. It works for a while. Until it doesn’t.

“What happens is your experimentation loop gets completely slowed down and sidetracked by the implementation behind it,” Ranganathan says. “And even worse, the research behind the implementation.”

At the start, it’s all about moving fast and trying things out. But as the system grows, more and more time gets pulled into wiring things together and keeping the data infrastructure from falling apart. Before long, teams that set out to build intelligent systems are stuck chasing issues in their pipelines.

There’s also a quieter shift. Not long ago, most teams only needed to reason about one data system. Today, that’s no longer true. “Before, we used to just take a Postgres database and try to figure out the optimal way to lay out data,” Ranganathan says. “Now we have a Postgres database and a graph database and a vector database… the problem complexity has gone up by a few orders of magnitude.”

The DIY approach hasn’t just become messy; it’s become a mess.

## **Agents don’t fail like apps**

Agent systems don’t behave like traditional applications.

An app has defined inputs and outputs. AI agents, especially in multi-agent setups, are far looser. They continuously generate and consume context, build memory over time, and collaborate across tools and users.

That introduces a new class of problems.

“Multi-agent systems… ” It’s just teams,” Ranganathan says. “Ultimately, you have to work as a team, whether you’re an agent or human.”

And the hardest part of teamwork isn’t computation. It’s coordination. It’s a shared understanding. It’s knowing what’s already been done and why.

In today’s stacks, that context is fragile. It gets lost between steps. And when something breaks, reconstructing what happened is difficult.

Which makes the question of what to keep – and what to throw away – harder than it sounds.

## **Memory, knowledge, and the mess in between**

Much of Meko’s design revolves around memory and knowledge.

Not everything an agent encounters is useful. Some information is relevant, some is broadly helpful, and some is just noise. The challenge is filtering and structuring that data so it remains useful over time.

The system’s job is to extract what matters and make it reusable across agents and humans.

This is where Meko leans into collective memory.

In most setups, agents operate in silos. Context isn’t easily shared, so teams repeat work and lose learning. Meko introduces “datapacks” – scoped containers for direct data (conversations, decisions, and outputs) and indirectly extracted data (learnings that fuel collective memory and shared knowledge) tied to a project.

“You’d be able to share this datapack and say, ‘Why don’t you look for yourself what I did?’” Ranganathan says.

Instead of passing context fragments, teams can work from a shared record.

## **From logs to decision traces**

Meko treats that problem — not just deciding what matters, but preserving it in a usable way – as a core challenge.

Instead of just logging events, it captures what Ranganathan calls “decision traces” — what an agent planned to do, how it executed, and what happened.

“If you don’t agree with the plan, what’s the point of doing the whole thing?” he says.

This also ties into cost and accountability. If a workflow burns through resources, teams need to understand why. “Somebody comes and says, ‘Why did you spend $1,000 yesterday?’” he says. Without context, there’s no clear answer.

For CTOs, that level of visibility isn’t optional.

## **While it’s still early, patterns are emerging**

Ranganathan is candid about where things stand.

“I think they’re still figuring it out,” he says. “We need repeatable use cases to mature this into a general-purpose data infrastructure for agents.”

Much of today’s agent work is still experimental. Still, Ranganathan is already seeing several patterns, such as collective learning across runs, an auditable record of what was learned, and resumability for long-running agents.

For example, in the collective learning pattern, when Agent A updates a shared fact and Agent B reads a stale state, the question becomes: what consistency model do you want? Yugabyte took the position that this is a memory consistency problem in the computer architecture sense, and built around it.

Internally, Yugabyte already uses agents for tasks such as issue triage and code analysis. The common thread is persistence – letting agents run longer, accumulate context, and produce useful outputs.

“Can I make my agent work longer without me?” he asks. That’s where the state becomes critical again.

## **A shift from models to infrastructure**

Meko builds on Yugabyte’s roots in distributed PostgreSQL, extending that foundation into an open source, agent-native architecture for AI agents.

> In the next year, every agent framework will have a memory layer — its effectiveness will be determined by whether that memory infrastructure enables agents and humans to function as a team by learning continuously.

It signals a broader shift. The focus is shifting from models to infrastructure – specifically, the data layer that determines whether systems are usable and scalable.

Yugabyte bets that this layer needs to be redesigned for agents, not adapted from existing tools.

As Ranganathan puts it, “It’s not what models can do… It’s not the orchestration… It’s the state. In the next year, every agent framework will have a memory layer — its effectiveness will be determined by whether that memory infrastructure enables agents and humans to function as a team by learning continuously. This requires purpose-designed agentic infrastructure designed for it from day one.”

And right now, that’s exactly where things are starting to break.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)