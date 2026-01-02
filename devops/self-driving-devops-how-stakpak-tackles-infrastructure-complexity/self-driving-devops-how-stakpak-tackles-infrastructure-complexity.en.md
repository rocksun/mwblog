Everything in tech is always changing at what feels like a breakneck pace — everything except DevOps infrastructure, that is.

Actually, [George Fahmy](https://www.linkedin.com/in/george-fahmy-b0978212a/), co-founder and CEO at [Stakpak](https://stakpak.dev/), says managing infrastructure is getting harder — that’s in spite of the AI wave. Or perhaps because of it?

“Since LLMs [large language models] came out… we realized that they’re really good at coding—and most developers actually enjoy coding,” he remarks. “But they suck at all the other stuff developers have to deal with.”

That’s what he and the Stakpak team have set out to change: “to make LLMs reliable at all the stuff developers don’t actually like doing.”

## The ‘Stuff’ Developers Don’t Like Doing (and AI Can’t Handle)

Fahmy believes it’s high time [DevOps infrastructure](https://thenewstack.io/devops/) got an overhaul, remarking that even autonomous vehicles have made more progress in recent years than infrastructure tooling.

As he puts it, “We’re trying to make infrastructure self-driving so developers can spend more time… building actual products.”

So what is this “stuff” developers don’t like doing?

It’s hard to define. DevOps has become a rag-tag assortment of responsibilities, extending beyond coding to include tasks like setting up local machines, configuring cloud environments, and managing deployment pipelines and production systems.

It’s this everything-but-the-kitchen-sink mix that’s made DevOps such an [awkward space](https://thenewstack.io/devops-is-still-waiting-for-its-cursor-moment/) for LLMs.

“[With] coding tasks, you just generate code and it runs… But with DevOps, there are a million things… other than coding, and LLMs are bad at it,” says Fahmy. Worse, developers “hate doing all this stuff.”

There’s trouble at both ends. Not only are DevOps tasks notoriously a drag for developers, the skills to perform these tasks leave the industry wanting. In the [2024 State of Tech Talent Report from the Linux Foundation](https://www.linuxfoundation.org/blog/the-2024-state-of-tech-talent-report?utm_source=chatgpt.com), 51% of organizations named DevOps as one of “the key technology domains prioritized for staffing,” with the average time to fill those roles taking almost six months.

“There’s a huge skill gap in the market globally about this kind of knowledge and expertise,” Fahmy confirms. “People are trying to hire DevOps… and DevSecOps…all the time, and they can’t find the talent.”

These days, the idea is for automation — more specifically, AI — to step up and fill in the gaps when time and skilled hands are in short supply. But Fahmy says that’s not working for infrastructure:

“We saw that coding agents… they’re good at coding, but they were not built for this kind of infrastructure work.”

Where he sits, it boils down to three core challenges.

## Challenge 1: Securing Production Systems and Secrets

DevOps requires working on live systems and handling sensitive data—but Fahmy says the tools most [AI agents](https://thenewstack.io/welcome-to-ais-messy-middle-where-36x-gains-require-distinguished-engineers/) rely on today aren’t up to snuff when it comes to production-grade security.

“That’s why we started to rebuild this tool layer and open source it,” he explains, “because we want to set a standard of how secure these things can be to be able to handle production work.”

He’s referring to Stakpak, a [fully open source DevOps agent](https://github.com/stakpak/agent) that helps developers secure, deploy, and maintain production-ready infrastructure.

According to Fahmy, Stakpak solves this security challenge by enabling LLMs to interact with sensitive systems without exposing secrets: “We handle redacting sensitive information and secrets and allow the LLMs to work with the sensitive data without seeing the actual sensitive data.”

## Challenge 2: Preventing Destructive Operations Across Fragmented Tooling

Security isn’t the only hang-up preventing developers from safely automating infrastructure work. The growing number of infrastructure management tools is also creating headaches.

“There are hundreds of different tools and hundreds of different ways of doing the same thing,” Fahmy explains. “So you can use three or four different tools… or you can stack them together.”

It sounds handy: More options, more flexibility. But in reality, the overwhelming amount of tools (and all the conflicting opinions that come with them) just creates more confusion, friction, and risk.

It’s double trouble when AI agents — the ones that are supposed to help developers manage those tools — end up creating new problems.

Fahmy recalls the now-infamous [Replit fiasco](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/), where an agent accidentally wiped some poor company’s entire code base.

“These agents and the models — they’re super creative,” he says. “They can find a lot of different ways to do the same thing… It’s a nightmare for people trying to keep them under control.”

A nightmare, he claims, Stakpak can put to rest with Warden, a guardrail system that prevents agents from performing destructive operations.

How so? Fahmy says it encapsulates coding agents inside a sandbox where explicit security rules block unsafe operations: “For example, you can list your resources in AWS, but you can’t delete them, regardless of what tool you use to deal with AWS.”

This, he explains, is an about-face from typical agent-control methods, which he claims aren’t working: “You can’t use an agent to prevent another agent from breaking stuff.” Nor can you simply blacklist or whitelist specific actions, which creates the impossible task of manually enumerating every possible scenario.

Instead, Warden provides a deterministic way to prevent agents from carrying out destructive operations, no matter which tool(s) it uses.

Admittedly, Fahmy says this isn’t especially valuable for coding. But he affirms it’s a game-changer for operational tasks, like database migrations, updates, or other infrastructure changes where “you can bring the whole thing down with the wrong command.”

## Challenge 3: Teaching Agents to Learn, Share, and Remember Knowledge

Fahmy doesn’t hold back: “LLMs [are] terrible at infrastructure work.”

He chalks much of this up to fragmentation: DevOps teams are up to their eyeballs in tools, but each speaks a different language. LLMs make matters worse by only reliably handling the most common programming languages.

That’s why Fahmy says Stakpak has directed a lot of their R&D to LLM knowledge gaps: “to teach LLMs to use new tools they were never trained on…; [to] acquire new knowledge that they would never [have seen] before…which is super challenging.”

Unlike coding agents, where you can add knowledge by creating new rule files, DevOps agents need a shared knowledge base to operate effectively—and Fahmy says Stakpak is delivering with centralized rule books and pooled memory:

“We think this is going to be a game-changer because the infrastructure space doesn’t lack a lot of infrastructure tools…; it lacks an efficient way to learn new knowledge and then convey it.”

Stakpak makes it happen with centralized rulebooks that define standard operating procedures, along with internal evaluation benchmarks that measure alignment to ensure agents consistently follow the correct procedures as they adapt to each environment.

That’s just one part of the equation. Meanwhile, pooled memory allows agents to learn from past sessions. When a team member completes a task, reasoning models extract key memories, so when the [agent is used by another team member](https://thenewstack.io/how-crewai-enables-ai-agents-as-collaborative-team-members/), it remembers and applies that learned knowledge.

This shared memory pool breaks down knowledge silos, which Fahmy describes as the biggest obstacle in DevOps: “The platform or infrastructure team [might have] created something, and the developers are still not aware [of it]…[or that it] can make their lives easier.”

## The Next Challenge

Of course, this isn’t the end of the line for infrastructure automation. Fahmy says Stakpak is already tackling the next movement: making agents self-improving.

“What if you can take bad or good examples and feed it back to the system to help it fine-tune its own parameters to get better as you go on?”

As automation advances, DevOps infrastructure may finally be starting to catch up — a welcome upgrade for developers who are tired of handling all this “stuff.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)