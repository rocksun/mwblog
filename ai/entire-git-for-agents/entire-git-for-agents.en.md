Thomas Dohmke, who [stepped down as GitHub’s CEO](https://thenewstack.io/github-loses-its-ceo-and-independence/) last year to become a founder again, is opening a preview of a distributed Git network on Wednesday that is designed to keep fleets of AI coding agents from overwhelming a single central server — and one that may soon compete directly with GitHub’s core service.

[Entire](https://entire.io/), Dohmke’s post-GitHub startup, is launching a preview of this on Wednesday (but for now, it is behind a waitlist). With this, developers can mirror an existing GitHub repository onto Entire’s own infrastructure in one step.

“In the era of agents, centralized Git hosting has become a fundamental constraint, as the strain of billions of agents and developers hammering a central server shows up in the form of rate limits, high latency, or even outages,” says Dohmke in today’s announcement. “Today, we begin to return Git to its original promise, with a distributed, and soon fully decentralized and open-sourced network of interconnected nodes around the world. By doing so, we enable any developer or agent to host their code in-region, pushing, pulling, and cloning close to where they operate, fast and without bottlenecks, while still part of a global, collaborative network.”

The key here is that the code stays on GitHub, as Entire stresses, but coding agents can work with the Entire mirror and, as the company notes, “build without rate limits.”

Entire’s mirror is meant to absorb the constant flow of traffic that a fleet of agents can generate. That traffic, after all, is part of the reason GitHub is often buckling under pressure these days and startups like Entire have an opening.

Centralized Git hosting, Dohmke says in an interview with *The New Stack*, has become “a fundamental constraint” now that billions of agent and developer operations land on the same servers, showing up as rate limits, latency, and outages.

Given GitHub’s recent availability issues, it’s no surprise that startups are trying to get into this space. Entire is one — and it has the pedigree — but in June, Cursor also announced Origin, its own Git forge rebuilt for swarms of agents that are cloning and committing against a single repository in parallel.

Entire is starting with active regions in the United States, the European Union, and Australia, but the team says that now that is has spun up its first few regions, it will add more soon.

## ‘Git as a database’

To build its network, Entire rewrote the server part of git. GitHub, GitLab, and Bitbucket all wrap the server-side of the Git binary and build their infrastructure around it. Entire started from scratch.

“We see Git really as a database,” Dohmke says. The open source Git project has two halves, he explains: the client an agent uses to talk to a repository, and the server a host runs to manage storage. Rather than build on that stock server, like most companies would do, “we made the decision of not going that route, and instead implemented our own Git backend.”

That only makes sense if Entire’s version has significantly better performance than the stock Git server, of course. Entire says its benchmarks have pushed the network to a sustained 570,000 clones an hour, 586 pushes a second, and roughly 470 combined clone-and-push operations a second.

Pushing to a native Entire branch can run up to 25 times faster than pushing through to GitHub, Dohmke says.

Entire it will open-source both the git backend and the benchmark suite.

## The foundation layer, now real

When Dohmke first described Entire’s plans to *The New Stack* [in February](https://thenewstack.io/thomas-dohmke-interview-entire/), he described a three-layer platform that included a Git-compatible database at the bottom, a semantic reasoning layer in the middle, and an interface on top. Even then, he said that the database, unlike a centralized Git host, could be a globally distributed network of nodes.

But in February, Dohmke also said Entire wouldn’t necessarily end up competing with GitHub, and that code repositories would stay central to the pitch.

Pressed on whether that still holds now that Entire hosts its own copy of the GitHub repo, he calls the mirror complementary, in part because Entire can offer enterprises the ability to keep their code in a local region to fulfill local regulations. He also notes that GitHub has a huge ecosystem and an extended feature set.

“I think the question for the buyer really is, is it not better for me from an availability and reliability perspective, that I have both of these products, so if one of them is down — there’s always going to be single points of failure and human errors — then I have my mirror on the other side,” he says. “But we certainly will, in deals, compete for the dollar spent at a much smaller scale compared to the multi-billion dollar business that is GitHub today.”

![](https://cdn.thenewstack.io/media/2026/07/5df4c80c-dis-git-hosting-1-2-1024x576.png)

Credit: Entire.

For now, that keeps the two complementary. Dohmke argues that GitHub remains the “source of truth,” or “cold storage,” while the working copy lives on Entire. But he also says that Entire will launch native repositories in the coming months, and those wouldn’t need GitHub underneath at all. All of this will be open-sourced as well.

Entire raised its $60 million seed round in February, when it had 15 employees. Felicis led it, with Microsoft’s venture arm among the backers. The company is now past 40 people and aiming for 60 by the end of the year.

## Entire beyond Git: the semantic memory layer

Entire is building its middle layer — the semantic reasoning layer — in parallel with the Git platform.  
The semantic layer now plugs into every major coding agent, including Claude Code, Codex, Cursor, Factory AI, and GitHub Copilot, and records each session, prompt, and tool call in the repository next to the code.

Having this data is useful for agents, and this was the first core service the company launched, but now, it is also building more services on top of that history.

The company is adding Entire Blame, for example, which shows not just who last touched a line but the agent session and prompt behind it. There is also Entire Review, which fans out several agents for an intent-aware review, and the company is adding a code and semantic search feature that lets agents (and developers) search across code changes and the reasoning that produced them.

“Session logs are now the second most important artifact in software development, and they belong in the repository alongside the code,” Dohmke says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)