Verbose changes. Nonsensical descriptions. Pull requests contributors can’t explain. AI is DDoS-ing open source software (OSS) with slop, and some maintainers are calling it quits.

As [Steve Croce](https://www.linkedin.com/in/steve-croce-1060082/), field CTO at [Anaconda](https://www.anaconda.com/), a Python data science platform, tells *The New Stack*, “It’s having a profound effect on maintainer workload.” In response, maintainers are [canceling bug bounty programs](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/) and introducing stricter contributor guidelines, he adds.

Some projects, like [Jazzband](https://github.com/jazzband), have been forced to sunset altogether. [Jannis Leidel](https://www.linkedin.com/in/jezdez/), the lead maintainer and Python Software Foundation chairperson, [writes that](https://jazzband.co/news/2026/03/14/sunsetting-jazzband) the “flood of AI-generated spam PRs and issues” made his project unsustainable.

According to [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/), Ph.D., a senior analyst at the consultancy Red Monk, the barrier to entry is now extremely low, making it easier to game the traditional incentive model for participating in open source. As she tells *The New Stack*, “It’s putting the contract between maintainers and contributors in peril in ways that haven’t existed before.”

For example, Rémi Verschelde, who oversees the open source Godot game engine, [shares on BlueSky](https://bsky.app/profile/akien.bsky.social/post/3meyerixvhs2p) that dealing with AI slop is “draining and demoralizing.” [Other project maintainers](https://www.theregister.com/2026/02/18/godot_maintainers_struggle_with_draining/) report growing apathy and wasted time responding to the deluge.

To be fair, nearly all software developers now use AI, and many communities rely on it to produce legitimate fixes and contributions. But the volume of low-quality submissions is becoming unsustainable, especially given that 60% of maintainers are [unpaid volunteers](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/).

GitHub is [aware of the issue](https://github.com/orgs/community/discussions/185387) and has released tools to aid maintainers and even suggested [disabling PRs entirely](https://www.theregister.com/2026/02/03/github_kill_switch_pull_requests_ai/) while it explores long-term solutions. For now, however, fixes to the core problem remain elusive.

Below, we’ll look at the issue and consider the strategies emerging to manage the crisis — hopefully before it overwhelms the open-source ecosystem that [most of the world depends on](https://thenewstack.io/is-open-source-in-trouble/).

## AI slop betrays the premise of open source

Open source has faced existential threats before, including [licensing shifts](https://thenewstack.io/open-source-is-at-a-crossroads/), [funding gaps](https://www.infoworld.com/article/3557846/how-do-we-fund-open-source.html), and [maintainer burnout](https://thenewstack.io/how-maintainer-burnout-is-causing-a-kubernetes-security-disaster/). But Slopmageddon introduces a new kind of strain.

The most immediate risk is wasted maintainer time. One developer estimates that it takes a reviewer [12 times longer](https://webmatrices.com/post/vibe-coding-has-a-12x-cost-problem-maintainers-are-done) to review and correct a pull request than to generate one with AI.

Generating clean, readable, and maintainable code remains difficult. Low-effort AI contributions require a disproportionate time to evaluate and respond to, decreasing morale and potentially drowning out high-value submissions.

Security risks are another concern. “AI-generated contributions can introduce subtle vulnerabilities, poorly understood dependencies, or incomplete fixes that expand the attack surface,” adds Anaconda’s Croce.

The situation can quickly spiral. In one twisted tale, a vindictive AI agent [published a scathing hit piece](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) on an open source maintainer after its code suggestion was rejected. The maintainer, [Scott Shambaugh](https://www.linkedin.com/in/wsshambaugh/), founder of Leonid Space and contributor to [matplotlib](https://matplotlib.org/), says he felt compelled to respond quickly to protect his reputation.

Shambaugh tells *The New Stack,* “There was a real sense of ‘Oh, I need to get ahead of the story’ so my version of the truth gets out on top.”

For him, the episode reflects a broader erosion of authenticity in open source. In the past, your reputation was tied to your contributions, and people participated to give back to the community, gain recognition, and learn through a collaborative feedback loop, he says.

Maintainers, in turn, took pride in stewardship. But nowadays, attempts to quickly game bug bounty systems or gain credentials in open source with rapidly generated PRs undermine that dynamic.

“If you just point an AI agent at a GitHub issue, it can solve it and write a PR in 30 seconds,” says Shambaugh. “If that’s what we really wanted, the maintainers could do that themselves.”

## Ways to manage AI-generated contributions in open source

So, what can open source maintainers and the tech industry at large do to manage the influx of AI slop?

No single fix exists. Instead, it’ll likely take a combination of new contributor policies, platform tooling, reputation and verification systems, and guidance from foundations and other community-led initiatives.

## Set AI policies for contributors

One response is clearer contributor guidelines. The goal isn’t typically to close the door on external contributions or ban AI outright, but to ensure its use leads to higher-quality submissions.

Effective policies spell out expectations like: what types of AI are allowed, when disclosure is required, and how contributors should validate their work before submitting.

Red Monk’s Holterhoff recently assembled [research on AI policies](https://redmonk.com/kholterhoff/2026/02/26/generative-ai-policy-landscape-in-open-source/) in the open source community, identifying 63 formal approaches across foundations and projects. These include efforts from [Blender](https://devtalk.blender.org/t/ai-contributions-policy/44202), [Fedora](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/), [Firefox](https://blog.mozilla.org/en/mozilla/mozilla-open-source-ai-strategy/), [Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md), [the Linux Kernel](https://canartuc.medium.com/the-linux-kernel-said-no-to-your-ai-coding-assistant-930b87c30447), [and WordPress](https://make.wordpress.org/ai/handbook/ai-guidelines/), as well as guidance from the Eclipse Foundation, [the Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai), [the Electronic Frontier Foundation](https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects), and others.

While approaches vary, organizations tend to permit AI usage if usage is disclosed. Others restrict AI-assisted contributions only to approved issues. 14 projects ban AI contributions outright, while 12 are undecided.

The data also suggests that standards become stricter the closer you are to critical infrastructure. “The farther down the stack you go, the less permissive with AI you have to be,” Holterhoff tells *The New Stack*.

Still, enforcement remains a gray area. For Holterhoff, policies should remain grounded in community norms, regardless of how permissive they are. Each project is so different, too, meaning AI policies will depend on the context.

As such, the issue isn’t so much AI itself, but how it’s used and the intention behind it. “It’s only slop when you don’t understand it or when it’s just thrown out there,” says Holterhoff.

Similarly, for [Ahmet Soormally](https://www.linkedin.com/in/ahmet-soormally), principal solutions engineer at [Wundergraph](https://wundergraph.com/), the focus should be on reinforcing good-faith contributions.

“It’s not about whether AI helped you to write a PR,” Soormally tells *The New Stack*. “It’s about what you hand to the next human or model. If it’s bloated, unclear, or hard to reason about, you are not helping; you are just adding noise.”

Another option is to use GitHub’s own tooling to respond to what it calls open source’s “[eternal September](https://github.blog/open-source/maintainers/welcome-to-the-eternal-september-of-open-source-heres-what-we-plan-to-do-for-maintainers/).” Maintainers can limit PRs to collaborators, disable them entirely, or introduce criteria-based gating.

Some are building custom defenses. One developer has created an [Anti-Slop GitHub Action](https://github.com/peakoss/anti-slop) to filter out sketchy PRs automatically.

Writing for [her personal blog](https://angiejones.tech/stop-closing-the-door-fix-the-house/), Angie Jones, VP of developer experience, Agentic AI Foundation, recommends using an [Agents.MD](http://agens.md) file, deploying AI to moderate AI submissions, having good tests, and automating the detection of low-quality PRs.

Still, for some, these measures aren’t enough. As Flux CD maintainer Stefan Prodan [notes on LinkedIn](https://www.linkedin.com/posts/stefanprodan_updated-ai-usage-policy-for-contributions-activity-7420221057237860352-OuhJ/), GitHub itself lacks a clear incentive to curb AI slop, given its investment in AI-assisted coding.

“This platform incentivizes this kind of behavior,” adds developer Yuri Sizov, [posting on BlueSky](https://bsky.app/profile/yurisizov.bsky.social/post/3mexrz5b5i22x), adding that “it inherently invites more low-quality contributions from drive-by devs.”

As a result, some projects are exploring alternative hosts. For instance, the Linux distribution Gentoo is migrating [from GitHub to Codeberg](https://www.theregister.com/2026/02/17/gentoo_dumps_github_for_codeberg_over_copilot_nagware/).

## Contributor reputation systems

Another approach to maintaining quality and trust in open source is to introduce reputation systems.

One such example is [vouch](https://github.com/mitchellh/vouch), a trust management system designed by HashiCorp founder Mitchell Hashimoto. The [Ghostty project](https://github.com/ghostty-org/ghostty) is currently experimenting with it.

As Hashimoto writes in the vouch README, AI tools make it easy to “trivially create plausible-looking but extremely low-quality contributions.” Vouch addresses this by requiring contributors to be vouched for by a trusted party before interacting with a project.

Another project, [good-egg](https://github.com/2ndSetAI/good-egg), assigns scores to GitHub contributors based on their contribution history, which could be used to validate reputation and authenticity.

## Cryptographic proofs of identity

Beyond human attestation, some argue for tying AI-generated contributions to verifiable identities.

For Shambaugh, the issue of AI agentic identity extends beyond open-source to trust across the broader internet. “Ephemeral identity can change at a keystroke, can be endlessly copied, and is nearly impossible to trace,” he tells *The New Stack*. “I don’t think we’re ready for a million more of these things to be on the internet at scale.”

Emerging approaches aim to address this issue through cryptographic verification. [Treeship](https://www.treeship.dev/), for example, is an open-source project that uses blockchain-based techniques to create privacy-preserving proofs of AI agent actions.

As [Revaz Tsivtsivadze](https://www.linkedin.com/in/tsivtsivadze/), founder of Treeship, tells *The New Stack*, “There’s a trust issue when adopting AI agents. It’s a black box; nobody knows what goes into agents’ decision-making, memory, or tool calls.”

“You could get all kinds of AI agents, like malicious, rogue, or untrusted parties,” he adds. “Cryptographic attestation of AI agents is the key to trusting AI agents as economic actors.”

Tsivtsivadze says that a tamperproof record of agent actions could be used within open source projects to track agent identities, actions, timestamps, and the underlying decision process.

While technologies like Treeship have broader potential applications in agentic commerce, he believes such verification could help reduce AI slop in open-source by ensuring agents are tied to real human actors.

Other community efforts aim to establish higher standards for accountability within open source at large.

One example is the [Open Source AI Manifesto](https://www.human-oss.dev/), spearheaded by Wundergraph, which sets expectations for how generative AI is used in open-source, emphasizing ownership, responsibility, and authenticity. The [project](https://github.com/OSSAIManifesto/manifesto) also provides a badge that maintainers can use to signal responsible AI usage.

“AI can scale code generation, but it can’t scale accountability,” says Wundergraph’s Soormally. “That part still belongs to us.”

Croce also points to a more fundamental issue: many open source projects remain underfunded and understaffed. Initiatives like [NumFOCUS](https://numfocus.org/) and the [Open Source Endowment](https://endowment.dev/about/) (OSE) aim to provide much-needed support.

“Finding ways to provide more resources and capacity for those reviews is definitely a stopgap and absolutely required for the future of OSS,” Croce adds.

## The future of open source hinges on accountability

Open source is still being adopted at a rapid pace, with more pronounced use in the EU than in the US, according to the 2026 [State of Open Source Report](https://www.openlogic.com/resources/state-of-open-source-report). Amid rising [digital sovereignty](https://www.cio.com/article/4038164/why-cios-need-to-respond-to-digital-sovereignty-now.html) concerns, avoiding vendor lock-in is now a top driver for open source.

There’s no doubt that open source is widely relied upon — 96% of commercial codebases contain open source, according to a [2024 Synopsis report](https://www.intel.com/content/www/us/en/developer/articles/guide/the-careful-consumption-of-open-source-software.html). But slopocalypse presents a messy challenge to tackle.

So, the question for open-source maintainers is whether it’s all worth it.

“If you make life a living hell, they won’t do it anymore,” says Holterhoff. “If their labor is not compensated for and they throw in the towel, then the OSS community loses out.”

Worryingly, although maintainers have [sounded the alarm](https://leaddev.com/software-quality/open-source-has-a-big-ai-slop-problem), it remains unclear how foundations or platforms will respond to sustain the ecosystem.

> “If we do not actively manage contribution quality in an AI-driven world, we are not just risking security issues or technical debt. We are putting the ecosystem itself at risk.”

“If we do not actively manage contribution quality in an AI-driven world, we are not just risking security issues or technical debt,” says Croce. “We are putting the ecosystem itself at risk.”

For now, it comes down to contributor accountability. “Accountability is the real standard,” Croce adds. “Contributors need to understand and stand behind what they submit.”

Without a single technical fix, perhaps an appeal to humans to ‘do what’s right’ will help. Because without that basic accountability and trust, the open source model itself starts to break down.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)