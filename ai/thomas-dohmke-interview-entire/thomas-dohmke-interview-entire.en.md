When GitHub CEO Thomas Dohmke [left](https://thenewstack.io/github-loses-its-ceo-and-independence/) the Microsoft-owned company in August of 2025, he said he did so to return to his startup roots. Now, after a few months of development, he is launching [Entire](https://entire.io/), a new open-source developer platform that reimagines what collaboration between developers and agents could look like if built from scratch.

Entire is backed by a $60 million seed round, the largest in developer tools history, led by Felicis, with participation from Madrona, Basis Set, and M12, Microsoft’s venture arm.

That’s an outsized round by any standard, but Dohmke’s reputation, having led GitHub’s evolution from code repository to an AI-centric platform built around Copilot, surely helped. Also, given the rapid pace of software development, a significant investment is required to keep up with the market’s evolving needs.

In an interview with *The New Stack*, Dohmke explained his vision behind Entire. “We’re moving away from engineering as a craft, where you build code manually and in files and folders — which is effectively what a Git repository was for the last 15 years, right? If you look at any given repo, it’s literally a file browser, and you can click through the files in this search and all that,” Dohmke says. “We are moving from that to a much higher abstraction, which is specifications — reasoning, session logs, intent, outcomes. And we believe that requires a very different developer platform than what GitHub is today.”

Dohmke notes that GitHub was built for human-to-human interaction. The entire system, from issues to pull requests to deployment, was not designed for this new era of AI agents. Yet today’s most advanced developers often use a dozen agents in parallel, and even the way we define software projects is changing quickly. Building that on GitHub — and bringing its existing user base along — would have been a ‘very different endeavor,” Dohmke says.

![](https://cdn.thenewstack.io/media/2026/02/ac7c1b59-entire-checkpoints.gif)

## Leaving GitHub to become a founder again

It’s worth noting that Dohmke stressed that his departure from GitHub was entirely amicable. He didn’t leave GitHub to build a competitor.

“After over ten years at Microsoft, seven of those at GitHub and four as CEO, I felt like the itch to be a founder again and build something new,” he says. “And I had a very nice conversation with [Microsoft CEO] Satya [Nadella] in June, and I outlined to him where my head is at. And his response was,’ Hey, you know, one, please keep pushing until your last day. And two, let’s see what we can do together in the Microsoft ecosystem.”

Given that, it’s no surprise that Microsoft’s venture arm invested in Entire.

## What is Entire building?

It’s also worth noting that while it is a platform play, Entire will not necessarily end up competing with GitHub. Dohmke says the idea is to build a layer higher in the stack where developers can manage agents’ reasoning processes and collaborate with them. Code repositories will remain central to that.

What Entire is building is a three-layer platform, with a new Git-compatible database built from scratch as its foundation, a semantic reasoning layer in the middle, and a user interface on top.

The team believes a new database layer is necessary because the information stored in these new repositories is different — specifically, the agents can emit a lot more context than humans do when using these tools. This new database will allow humans and agents to query not just the code but also the reasoning behind it.

Since agents will likely use this database and its API endpoints far more often than humans could ever use a Git repository, the team also needs to consider performance.

Dohmke also says that this new database, unlike traditional centralized Git repositories, can be a globally distributed network of nodes. For users who need to (or want to) ensure data sovereignty, that’s a major selling point.

## Checkpoints

The first product the team is launching is part of the middle layer. Dubbed Checkpoints, this new open-source tool integrates with Claude Code and Google’s Gemini CLI (with Open Codex support coming soon) and automatically extracts and logs the agent’s reasoning, intent, and outcomes.

“The middle [layer] is all about providing both to humans and to agents all the information that led to the software product,” Dohmke explains. “And today, in the GitHub repository, that’s all the code and sometimes documentation and dependencies, but it’s essentially missing all the [information about] how you got there.”

![](https://cdn.thenewstack.io/media/2026/02/dc91247f-entire-cli-scaled.png)

Entire’s Checkpoint tool in the CLI (credit: Entire).

That’s because those systems were built for human developers, and while developers may write test cases and documentation after they finish writing the code, documenting their exact reasoning steps was never part of the process. But in the traditional, non-agentic workflow, a lot of institutional knowledge is never written down.

“That’s the first step in our larger vision, which is providing the semantic reasoning layer over the life cycle of a software project, so you can trace — both as a human and as an agent — at any point in time, in the future, why decisions were made the way they were,” Dohmke explains.

With all this data saved, Checkpoints will allow developers to review how the agents produced the code.

While the user interface is still a work in progress, Entire has built parts of it that help visualize the checkpoints stored in Git. For now, though, the team is mostly focused on the command line experience.

## The review bottleneck

One issue Dohmke stresses in the current developer/agent workflow is something we hear a lot about these days: the bottleneck for shipping code isn’t writing code, it is reviewing the code written by the agents. That’s already leading to [developer burnout](https://thenewstack.io/is-ai-creating-a-new-code-review-bottleneck-for-senior-engineers/).

The future, Dohmke argues, is more agents.

“If you keep that going through the software life cycle, the next thing you do after writing code is reviewing code — either your own code or your team member’s code in a pull request,” says Dohmke. “But a pull request has the same problem [when it comes to understanding the code]. It shows me changes to files that I never wrote in the first place. And the code review agents, like Copilot agent, give me feedback on their code, which is great when I still have some fundamental understanding, but becomes pointless or superfluous if I don’t actually understand what that code does.”

When there is more code and less context, the solution may be to use agents and deterministic tools to test the code and ensure it’s compliant and secure.

“It’s becoming more and more of a bottleneck, and so you have to remove that step out of the process,” he explains. “And that’s, I think, one of the biggest challenges in the industry, because at the same time we are struggling with more and more cyber attacks, many organizations have introduced zero trust as a process, which means nothing gets deployed without a human review. And so that’s, I think, where we believe, in our vision, a lot of innovation will happen, and we want to be part of that.”

## Hiring humans and agents

With this funding round closed, Entire plans to double its headcount from currently fifteen employees to about thirty and build up its platform as fast as possible. But as Dohmke stresses, it’s not just human employees that matter anymore. Even in its press release, the Entire team notes that it plans to expand its team to “hundreds of agents.”

“I think in 2026, any leader needs to think about head count no longer just as salaries and benefits and travel and expenses, but tokens. And I’ve spoken to engineers, both on my own team, but also in the Bay Area here that are talking about 1,000s of dollars in tokens per month,” Dohmke says.

As for the business model, Dohmke tells us that the team plans to follow the well-established open source playbook of making most of the platform available under a permissive license and then offering a hosted service with additional features to monetize.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)