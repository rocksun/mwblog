During the California Gold Rush of the mid-1800s, the people who benefited most were not those who came West to dig treasure out of the ground, but those who sold them the tools to do that.

[Rob Whiteley](https://www.linkedin.com/in/rwhiteley/) believes that the organization he runs, Coder, is positioned to be a “picks and shovels” company for the great AI rush of the 2020s.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Whiteley, Coder’s CEO, discussed the evolving landscape of AI and development tools — and his company’s new open source contribution, [Mux](https://coder.com/blog/running-parallel-self-hosted-coding-agents) — in this On the Road episode of The New Stack Makers, hosted by TNS Publisher [Alex Williams](https://thenewstack.io/author/alex/) and recorded at [AWS re:Invent](https://thenewstack.io/welcome-to-ais-messy-middle-where-36x-gains-require-distinguished-engineers/) in Las Vegas.

As a 25-year veteran of the tech world, Whiteley calls our current AI moment the craziest he’s ever seen, in terms of sheer velocity of change.

“The one thing constant is: Developers are always adopting new tools,” he noted, adding, “What I’m seeing is pressure from these new platform teams to quickly bless those tools and make them part of the stack.”

Adding to the pressure on platform teams, he said: “The days of telling developers ‘no’ are gone.“

The rush to adopt AI-based tools, he said, carries echoes of the transition to cloud native, when companies tried to [“lift and shift”](https://thenewstack.io/app-modernization-why-lift-and-shift-isnt-good-enough/) their old workloads and ways of doing things onto the new cloud platforms. Just as cloud native companies emerged, building from scratch on the new tech, Whiteley said, so too are [AI native](https://thenewstack.io/from-cloud-native-to-ai-native-where-are-we-going/) entities likely to emerge.

“What I fear, is that gap between those that are getting value and those that aren’t is widening at an alarming rate, and so we’re going to end up with the haves and have nots, where so many companies are gonna throw up their hands and say, ‘ I don’t know how to get value from AI,’” he said.

“That scares me a little bit, because then you’re gonna get these companies that just leap forward in capability. And whenever you have a disruptive technology, there’s always this skills gap.”

## Why Developers Are Becoming ‘Team Managers’

As a student of tech history, Whiteley said, he’s worried that companies are currently not investing heavily enough in helping their workers build AI-related skills.

Having a [platform engineering](https://thenewstack.io/whats-the-future-of-platform-engineering/) team in place, he said, can help an organization wring benefit from AI tools. But even that, he said, isn’t going far enough.

“There’s two things you have to think about,” he said. “There’s the developer is naturally, organically, going to put [AI tools] in their workflow. Then there’s going to be the backend company that can allow it or not. And so in a lot of cases, they’re just going to start blocking tools.”

Cursor, for instance, often gets blocked by companies outright, he said: “And so here is this potential to transform the way you develop software, and we’re not going to let you use it because it’s not secure, or it can’t be governed.”

It’s all part of the growing problem of achieving AI parallelization in the enterprise: figuring out why and how to run multiple AI coding agents safely and securely, at scale.

“There’s an emerging trend that I’m seeing my most progressive customers doing, where they will spin up 10 instances of an agent — Claude Code, Cursor, background agents,” Whiteley said. “And all of them are in their own isolated environments, but they’re identical to each other, so we’ll just spin up 10 of the same thing, and then we’re going to feed them the same prompt.”

In those cases, the agents will create 10 unique solutions; the customer will select the one they want and throw the rest away.

At the pace agentic AI is moving and the pressure to get value from it, Whiteley said, this practice is within a year of going mainstream. As a result, he noted, “parallelization and just the whole maintaining state of your agents is going to be probably one of the top five problems we face in 2026.”

In an organization that uses agentic AI, individual developers are really team managers, he said, building and tracking several— even hundreds— of agents. Companies haven’t fully grasped that yet.

“In a rush to get the technology up and running, a lot of companies are bypassing the kind of tried-and-true things they would put in place for a human developer,” Whiteley said. “They’re not putting in place for its agentic equivalent.”

## Introducing Mux, a Coding Agent Multiplexer

To help developers maintain multiple AI agents, Coder has announced [Mux](https://github.com/coder/mux), an open source desktop coding agent multiplexer.

Mux “is really just born out of the idea that for a lot of developers, the center of gravity is moving away from a traditional code editor, to more of a chat interface, where I’m just going to be keeping my virtual team on boil.” Whiteley said. “I just want them constantly producing. Now, the second it produces code, I’m going to open it up in an editor and check the work.

The new platform can be a complement rather than a replacement to a developer’s IDE, he added: “We needed a separate interface for managing agentic output than from actually checking the work of that agent. They’re two different tools.”

One of Whiteley’s team members, he said, calls Mux a shovel, as opposed to an excavator. “Just because you have an excavator that can move massive amounts of Earth doesn’t mean you’re going to be able to go do your backyard with it. And just like you’re not going to want to go clear an entire field with a little hand shovel. They’re just two different levels of kind of work.

“Agents excavate code. They produce a lot of it, and then you have to bring it into a refined area, where you go through it with a more shovel-like tool.”

Check out the full episode for more about Mux and about why fears of a developer surplus in the AI era are unfounded.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/7bbd1cfd-cropped-4b732d2f-heatherjoslyn.jpg)

Heather Joslyn is editor in chief of The New Stack, with a special interest in management and careers issues that are relevant to software developers and engineers. She previously worked as editor in chief of Container Solutions, a Cloud Native consulting...

Read more from Heather Joslyn](https://thenewstack.io/author/hjoslyn/)