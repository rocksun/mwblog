[Nx](https://nx.dev), the company behind the open-source [monorepo](https://thenewstack.io/monorepos-hal-9000-approved-code-management-and-collaboration/) build system of the same name, on Tuesday launched Polygraph, a service that connects multiple repositories into what it calls a single “synthetic monorepo” that [AI coding agents](https://thenewstack.io/ai-coding-tool-stack/) can work on as if it were a regular monorepo.

In an interview with *The New Stack*, NX’s founders argue that while agents can do a lot within a single repository, they tend to stall when a change involves other repositories or depends on work someone else has already done. Polygraph, which combines multiple repos with context from agent traces, wants to change this.

Co-founders [Victor Savkin](https://ca.linkedin.com/in/victorsavkin) and [Jeff Cross](https://www.linkedin.com/in/jeffbcross/), the company’s CTO and CEO, are former Google engineers from the Angular team. They tell *The New Stack* that Polygraph began as an enterprise-only feature inside Nx but was distinct enough that the team decided to ship it as a separate product.

It’s currently available for free during early access.

## Why Nx built Polygraph

As Savkin notes, a coding agent that is 10 times faster doesn’t make an engineer 10 times faster, because coding is only part of the job. By Nx’s own modeling, a solo developer working mostly alone sees about a 4.3-fold speedup from using agentic coding tools, whereas a large organization, where developers spend far more time coordinating with each other, sees only a 1.3-fold speedup.

> “The limits of agents are set by how autonomous they can be.”

“The limits of agents are set by how autonomous they can be,” Savkin says. An agent runs for a few minutes, then “runs out of stuff to do,” and hands control back to a person. The team argues that this is because the agent can only work on the repo it sits in and forgets everything between sessions.

## The synthetic monorepo

Polygraph first analyzes a company’s repositories — internal ones plus the open-source packages they depend on — and uses that to build a dependency graph of what publishes which packages, and what defines and consumes which APIs. No code ever moves, and all Polygraph creates is its own graph.

> “What I mean is simply that you can read everything you want to read and write everything you want to write at the same time, in the same place.”

“Monorepo has a negative connotation to some people. It means big,” Savkin says. “What I mean is simply that you can read everything you want to read and write everything you want to write at the same time, in the same place.” With Polygraph, you can now, for example, change the producer of an API in one session, and the agent can see and update every consumer because all of the code is accessible to the agent.

## A shared memory for every session

The synthetic monorepo is already quite useful because it’s much easier for the agent to work with, but the shared memory, the team argues, is what brings it all together.

“Every conversation any engineer in your organization has with an agent will be captured,” Savkin says — “kind of like a meta graph of how the work came to be.” Polygraph relates those sessions, so a new one surfaces relevant past work by what it was trying to do, not just which files it touched. The aim, he says, is an organization where “all your employees contribute to one hive mind of knowledge,” rather than every session starting from scratch.

It’s important to note that the memory is portable. Polygraph can rebuild a session’s exact state on another machine, including the repos, the logs, and the running agent.

> “He gets my state, with my repos, with everything, with my session, with my traces… It’s sort of like a *Star Trek* teleport.”

This means another developer can now easily resume the session. “He gets my state, with my repos, with everything, with my session, with my traces,” Savkin says. “It’s sort of like a *Star Trek* teleport.”

## Coordinating the change

Pulling code together is only half of a cross-repo change, though. The other half is shipping it. In one session, Polygraph sets up the affected repos, pushes the change to downstream consumers so the agent can verify it before anything merges, and then opens pull requests for each.

There is a caveat, though. The pull requests still merge separately, so this is not a single atomic commit across repos.

## Agnostic about agents

Nx calls Polygraph a “meta-harness,” because it sits around the coding agents rather than being one. It supports [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), [Codex](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/), and [OpenCode](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/) today, wiring them together over the [agent-to-agent (A2A) protocol](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/), with [Google’s Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/) and other coding agents on the roadmap.

Because sessions are portable, a developer can switch models mid-task, which helps when an agent runs out of ideas — or tokens.

## Getting started

At launch, Polygraph works only with GitHub. The Polygraph command-line tool detects which agents are installed and adds the matching plugin to those agents. Sessions start from the CLI, or mid-task with a /polygraph slash command inside an agent like Claude Code.

For enterprises, there is also a security advantage, Cross says. A single prompt can tell Polygraph to find everything that depends on a vulnerable library version and update it, opening as many pull requests as that takes. That drops the CVE response time, he says, “from days or weeks to something that could be done in hours.”

## Pricing

Pricing will come later and will likely be based on usage and metered by how often a company indexes repos and creates sessions, with a free tier and higher charges as repo counts climb.

Nx can afford to wait, Cross says. “We’re a lot more interested in just getting a lot of people using it than surpassing Nx’s revenue,” he says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)