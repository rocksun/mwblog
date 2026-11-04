OpenAI on Monday detailed how it built a new Git backend for its monorepo to power the ever-increasing number of commits its developers and their agents now create.

Pando, as the team calls the new backend, cut push latency by nearly 5x, the company says, and it currently serves close to a petabyte of Git data per day at OpenAI.

OpenAI is obviously an early adopter of agentic coding tools. Compared to the first quarter of 2024, the quarterly commits to its monorepo will have increased by over 2,400% by the end of this year, the company says. But the issues it is facing are similar to what many other enterprises and Git forges like GitHub are now seeing.

With the pace of development increasing, Git itself is becoming a bottleneck. GitHub, for example, spent much of its recent [Universe keynote](https://thenewstack.io/?p=22842113) on how it is [improving its infrastructure](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/) to become faster and more reliable, all while serving billions of pull requests every month.

That has given rise to startups like [Entire](https://thenewstack.io/entire-git-for-agents/) (from former GitHub CEO Thomas Dohmke) and projects like [Origin from Cursor](https://thenewstack.io/cursor-origin-github-alternative/). Like OpenAI’s work, those are based on Git, but others, like [Anthropic](https://thenewstack.io/anthropic-scion-git-replacement/), basically start from scratch with a new client and architecture.

## Why OpenAI stayed with Git

The OpenAI team explicitly notes that it wanted to retain compatibility with Git. The team was seeing the reliability of its Git backend fall below 90%, with slow fetches and failed merges, but decided to stay within the Git ecosystem.

As OpenAI’s Aaron Friel, Taylor Blau, and Ted Nyman ask in the announcement, the question the team asked itself was if it had “reached a limit of Git itself, or of the way we served our monorepo?” The answer for OpenAI was that the Git client and protocol weren’t really the problem (though the team is also making some tweaks there), but the way conventional Git servers are built.

“For more than two decades, developers have adapted their tools around Git as the way they build software has changed,” they write. “When we started to feel friction in our own monorepo, it mattered to us that we could keep building on that work.”

## How Pando works

Pando drops two things most Git servers treat as requirements. The first is keeping every branch in the repository in a consistent state at once. The second is building a custom packfile, Git’s format for bundling compressed objects, for every client that fetches code.

In Git, a branch is simply a pointer to that latest commit. Moving that pointer is the only part of a push that requires coordination. Conventional Git servers order those updates across the entire repository, so when there are many developers working in parallel, a push to one agent’s branch can end up waiting on another’s.

Pando, on the other hands, doesn’t coordinate every write across the whole repository. Instead, it handles each branch on its own. Because of this, pushes to unrelated branches then don’t have to wait on each other.

There’s a tradeoff here, the team acknowledges. When a client is looking at several branches at once, it may see them at slightly different points in time. In practice, however, users and agents only care about the order of updates to a single branch, OpenAI argues.

When a client pushes, Pando validates the incoming packfile as it streams it into blob storage, without unpacking it into a local repository. It records the new branch tip, the packfile’s location, and its dependencies in a metadata store. By default, Pando advertises only the trunk branch as a base for feature-branch pushes. That makes each pack reusable by other clients that already have the advertised trunk history.

Then, when another client fetches the branch, Pando selects the stored packs it needs based on the history it already has. It then returns download links through packfile-uri, a Git protocol feature that lets clients download packs separately.

![](https://cdn.thenewstack.io/media/2026/11/da899961-screenshot-2026-11-02-at-2.23.37-pm-1024x457.png)

Pando stores the writer’s packfile in blob storage and records the ref version in a shared key-value store. On fetch, Pando selects the packs the reader needs, and Express serves them. Credit: OpenAI.

A caching service called Express then serves those packs from regional caches, with a hit rate above 99%, the company says. On standard cloud VMs, clones and fetches can max out a 10 Gbps network link.

A busy monorepo would otherwise leave clients downloading tens of thousands of small packs a day, so background workers merge them into larger ones over time, much like a log-structured database compacts its data. That also lets Pando work out which packs a client needs in logarithmic time.

## Pando vs. standard Git servers

On a standard Git server, every fetch means working out which objects the client is missing and compressing a fresh packfile just for that client. Those packs are expensive to generate and hard to cache, OpenAI says. Pando mostly hands out bytes it already has.

Before a push, a regular Git server also lists every branch it holds so the client can skip objects the server already has. With millions of branches, that list alone can grow past 100 MiB, according to OpenAI. Advertising only trunk keeps it small, but it means repeat pushes to the same branch resend everything that isn’t on trunk. The team says that’s a fair trade, since the median pack in its monorepo is still under 20 KiB.

Regular Git servers also have to repack and garbage-collect repositories to keep them fast, which eats up compute and disk I/O. Pando never throws a pack away. It keeps packs at every compaction level and serves from all of them.

For developers, little of this is visible. They keep using standard Git commands, though OpenAI now ships its own Git build to developer machines and inside the ChatGPT desktop app.

OpenAI built Pando in Rust in 10 weeks, with one engineer designing the core and teams of Codex agents implementing it. It went into production in April.

## What goes back into open source Git?

Building on Git also meant running into some of Git’s own rough edges, and OpenAI says it’s sending many of its fixes back to the project. Because Pando leans so heavily on packfile-uri, which a Google engineer [first proposed in 2019](https://lore.kernel.org/all/871s1stlf4.fsf@evledraar.gmail.com/), the team had to fix how the Git client handles concurrent pack downloads, cleans up after interrupted transfers, and resumes downloads that had already finished. It also added tracing for those downloads, which makes it easier to tell whether a slow fetch is spending its time generating packs or transferring them.

Not all of that work has landed in Git yet. OpenAI says several of its changes are already upstream, while many others for now only live in the company’s public Git repository. Those include support for downloading and indexing packs in parallel and a new “explicit haves” feature, which lets a server tell a pushing client where a branch currently points without letting the client leave that history out of its pack. The company is tracking all of this in a public patch tracker.

Pando itself isn’t part of that, though. OpenAI isn’t open sourcing the backend, and as of now, it only says that it’s looking into ways to share the underlying technology with its users. Anthropic, too, has said it has no plans to release Scion, either.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=openai-pando-git-backend)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)