[OpenClaw](https://openclaw.ai/) has undoubtedly been one of the big AI success stories of 2026, an example of how far an open-source AI agent can travel when it’s free for anyone to run locally, extend, and build on.

But when OpenClaw creator [Peter Steinberger](https://www.linkedin.com/in/steipete/) announced in February that [he was joining OpenAI](https://steipete.me/posts/2026/openclaw), it wouldn’t have been unreasonable to assume that OpenClaw’s days would be numbered. However, both Steinberger and OpenAI reassured people at the time that the ultimate plan was to keep OpenClaw alive within an independent foundation, a plan that has now come to fruition with formation of the [OpenClaw Foundation](https://www.openclaw.org/).

By way of a brief recap, OpenClaw is an open-source, self-hosted AI agent that runs on a user’s own machine, giving it direct access to files and messaging apps. That personal, self-hosted design is a big part of why it caught on: people used it to do actual things — automating tasks across WhatsApp, Slack and email, building personal tools on the fly, and giving it the kind of persistent access a human assistant might have.

The project’s [GitHub repository](https://github.com/openclaw/openclaw) today sits in [sixth place for most-starred projects](https://www.star-history.com/) of all time, above esteemed open-source stalwarts [such as Linux and React](https://thenewstack.io/openclaw-github-stars-security/).

The new Foundation is chaired by [Dave Morin](https://www.linkedin.com/in/davemorin/), the entrepreneur, investor, and founder of [now-defunct](https://techcrunch.com/2018/09/17/rip-path/) Facebook-challenger [Path](https://en.wikipedia.org/wiki/Path_(social_network)). In a [blog post](https://openclaw.ai/blog/introducing-openclaw-foundation#why-a-foundation) published on Wednesday, Morin says the Foundation exists to put ownership of AI back in people’s own hands.

“Today AI feels distant and a little frightening, locked in someone else’s cloud, answering to someone else’s interests,” he writes. “We think the future is personal AI that actually does things. It runs on your machine, works with the apps that you already use, and answers to you and you alone.”

> “We think the future is personal AI that actually does things. It runs on your machine, works with the apps that you already use, and answers to you and you alone.”

## The people behind the agent

If truth be told, the Foundation already kinda-sorta existed, but more in an informal capacity.

In [an interview with Jason Calcanis](https://www.youtube.com/watch?v=KEHMoI00q3w) on his In *This Week in Startups* podcast back in March, it was confirmed that Morin would be on the new Foundation’s board, though the process of attaining 501(c)(3) non-profit status was still a work in progress. With that now in place, Morin sets out its ambitions to become the “Switzerland of AI.”

> “Neutral ground where every model and every lab can plug into the technology and collaborate on standards in the era of agents.”

“Neutral ground where every model and every lab can plug into the technology and collaborate on standards in the era of agents,” Morin continues.

We also now know who will be steering the project forward during its embryonic stages. The Foundation has hired its first full-time team: six on engineering, led by chief architect [Vincent Koc](https://www.linkedin.com/in/koconder/), and four on operations, covering partnerships, finance, community and talent. Morin himself is chair of the board.

It’s a relatively lean crew for a project adding 4.5 million new “claws” (i.e. self-hosted instances of OpenClaw) a week, though the Foundation is still hiring — among the eight open roles are a member of technical staff, a forward deployed engineer, and a chief of staff.

Digging into the open-source project itself, we already know that OpenAI, GitHub, and Nvidia are among the main sponsors, while there are more than two dozen core maintainers responsible for the project. This includes four each from Nvidia and Microsoft; three each from OpenAI and Tencent; and personnel from companies such as Atlassian, Xiaomi, Red Hat, and Hugging Face.

![OpenClaw core maintainers](https://cdn.thenewstack.io/media/2026/07/84f4cb4c-screenshot-2026-07-09-at-11-44-02-people-openclaw-foundation.png)

*OpenClaw core maintainers*

What this tells us, of course, is that while OpenClaw is very much an open-source project as per its MIT license, there is a heavy corporate representation behind it, with some of the world’s biggest companies each holding a meaningful stake in how the project is managed.

This isn’t all that unusual for major open-source projects, but it does raise questions of how “independent” or “neutral” OpenClaw can really be when its maintainer resembles a who’s-who of Big Tech.

> “The great open source projects of our time… endure because a neutral steward stands behind them.”

However, for a project of OpenClaw’s magnitude, there is no escaping the fact that it needs the resources and rigor that only big companies can really provide at scale.

Morin notes that the foundation’s core *raison d’être* is to protect OpenClaw and steward it “as open and independent,” comparing its role to other notable projects such as Linux, Apache, and Mozilla.

“The great open source projects of our time… endure because a neutral steward stands behind them,” he writes.

## ‘The open-source flywheel’

OpenClaw’s need for that kind of institutional muscle became clear early, particularly on security. One researcher [found a one-click account takeover](https://thenewstack.io/openclaw-moltbot-security-concerns/) leading to remote code execution in less than two hours, exploiting a default configuration in which the project’s control interface was reachable from the browser even when supposedly bound to localhost.

Separately, a backend misconfiguration at Moltbook, [the agent-centric social network](https://thenewstack.io/moltbook-the-singularity-or-hype/) built on top of OpenClaw, exposed roughly 1.5 million API keys and private messages between agents. By February, OpenSourceMalware [had catalogued 386](https://opensourcemalware.com/blog/malicious-clawhub-skills-target-openclaw-users?utm_source=the%20new%20stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns%20platform) malware-infected “skills” — the plug-ins that extend what an agent can do — out of just over 3,000 known skills in circulation.

Some of that appears to be exactly what the Foundation’s new backers are now being enlisted to fix.

According to Morin, Steinberger now leads a team inside OpenAI called Claw Labs, focused on improvements that benefit both OpenClaw and OpenAI’s own products. OpenAI is also underwriting some of the compute OpenClaw’s agents run on, and in March it [released Codex Security](https://openai.com/index/codex-security-now-in-research-preview/), a tool built specifically to patch the kind of vulnerabilities a volunteer-run project may struggle with on its own.

In June, Microsoft [unveiled Scout](https://thenewstack.io/microsoft-build-scout/), an always-on personal agent built on OpenClaw. Microsoft [says it’s contributing policy](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) conformance work directly upstream to the open-source project, allowing organizations running OpenClaw to check whether their setup meets their own security and compliance requirements and get a verifiable, audit-ready answer.

Chinese tech giant Tencent, meanwhile, has contributed full-time maintainers to work on security, stability and [ClawHub](https://clawhub.ai/) — the project’s public registry where anyone can publish “skills,” or plug-ins — and now coordinates directly with the Foundation’s security team when vulnerabilities are found.

> “When the largest technology companies and research universities in the world build on a community project and contribute back, that’s the open source flywheel working exactly as intended.”

Other tech companies such as Atlassian, Vercel, and Cloudflare are also contributing in different ways, for instance shaping enterprise deployment and access controls, and keeping the underlying infrastructure running day to day.

So, while the corporate-led structure of the project isn’t in keeping with the traditional community ethos of many open source projects, the multi-vendor buy-in is a calculated bet: that spreading dependency across rival companies is the only way to actually keep OpenClaw neutral.

Morin, for his part, views this influx of corporate muscle as a feature rather than a flaw.

“When the largest technology companies and research universities in the world build on a community project and contribute back, that’s the open source flywheel working exactly as intended,” he writes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)