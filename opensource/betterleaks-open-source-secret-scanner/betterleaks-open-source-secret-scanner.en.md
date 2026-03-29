A new open-source secret-scanning tool from the creator of [Gitleaks](https://github.com/gitleaks/gitleaks) aims to pick up where its widely used predecessor left off, with a reworked detection approach, more flexible validation, faster scanning, and greater control over its development.

The project, dubbed somewhat modestly “[Betterleaks](https://github.com/betterleaks/betterleaks),” has secured sponsorship from [Aikido](https://www.aikido.dev/), a [billion-dollar](https://www.aikido.dev/blog/aikido-funding-series-b) security startup that’s backing a broad array of open source tooling.

For those unfamiliar with the intricacies of system security, secrets sit at the centre of modern software infrastructure, enabling services to authenticate with one another, access databases, and call external APIs. These credentials — keys, passwords, and tokens — are often stored in code during development, whether in configuration files, scripts, or test environments. The intention may be to move them to a safer place later, but at an early stage, it is often easier to hard-code them, leaving them vulnerable to being carried into places they were never meant to be.

This becomes a problem when code is shared more widely than intended. Repositories are made public, logs are exported, or code is copied between environments, including credentials. Once exposed, those strings can be picked up automatically by bots that scan code-hosting platforms and other public sources for usable credentials.

This becomes a problem when code is shared more widely than intended. Repositories are made public, logs are exported, or code is copied between environments, including credentials. Once exposed, those strings can be picked up automatically by bots that scan code-hosting platforms and other public sources for usable credentials.

In the wrong hands, those credentials can be used to access cloud infrastructure, spin up additional compute resources, extract data, or commit all manner of nefarious deeds.

## An open secret

The volume of code being written is now increasing that pressure. AI tools can generate large amounts of code quickly, often with less manual review, which increases the likelihood that credentials will make their way into the open.

[Zach Rice](http://www.linkedin.com/in/zricethezav/), creator of Gitleaks and now its successor, [Betterleaks](https://betterleaks.com/), tells *The New Stack* he sees this happening when developers over-rely on AI assistants during development. He described a common pattern where developers briefly insert real credentials into code for testing, are warned by the assistant, and then override that warning by telling the model to ignore it and continue.

> “And I guarantee you, most people are doing that, rather than taking the time to properly manage their secrets.”

“And I guarantee you, most people are doing that, rather than taking the time to properly manage their secrets,” Rice says.

The behaviour is reinforced by the pace and feedback loop of AI-assisted development. Developers can generate and iterate on code rapidly, a style often referred to as [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/), where output is accepted and refined without close inspection.

More broadly, some practitioners describe this feedback loop in terms of “[AI psychosis](https://www.psychologytoday.com/gb/blog/urban-survival/202507/the-emerging-problem-of-ai-psychosis),” where constant interaction with AI systems can lead to overreliance and reduced scrutiny of the output. Put simply, AI is becoming a second brain, [often at the expense of the user’s first brain](https://stackoverflow.blog/2026/03/19/ai-is-becoming-a-second-brain-at-the-expense-of-your-first-one/).

“If you’re in this loop of kind of instant gratification of code being churned out…. ” You forget,” Rice says. “You totally forget about those secrets that you told the AI agent not to worry about. I would say LLMs, for sure, increase the risk of secrets leaking.”

## In the beginning

To understand what Betterleaks is striving for today, it’s worth rewinding back to 2018, when Rice committed the first lines of code for Gitleaks, initially a side project in his spare time that he could shape himself from the get-go.

At the time, existing tools such as Python-centric [TruffleHog](https://trufflesecurity.com/trufflehog) were already scanning code for exposed credentials, but Rice saw an opportunity to rewrite the approach in Go, add a configuration system that users could control, and make it faster.

“I wanted a tool that I could have some creative control over, and improve upon,” Rice says.

He credits the original idea to [Dylan Ayrey](https://www.linkedin.com/in/dylanayrey/), creator of TruffleHog and later founder of [Truffle Security](https://trufflesecurity.com/), who was among the first to spot secret scanning as a distinct problem space.

“He identified that problem, and then I just wanted a project to work on after work — a creative outlet for writing code,” Rice says.

Rice released Gitleaks publicly, and the project began to gain attention as awareness of the risks associated with leaked credentials grew. Over time, Gitleaks became a widely adopted tool across engineering teams, attaining more than 25,000 stars and 26 million downloads on GitHub alone.

![Gitleaks has 25K stars and counting](https://cdn.thenewstack.io/media/2026/03/b0c96dd6-gitleaksstarhistory-1024x750.png)

***Gitleaks has 25K stars and counting***

Companies, including GitLab and Red Hat, integrated it into their own systems or ran it internally to scan repositories and pipelines for exposed credentials. Rice, in fact, later joined GitLab as a senior software engineer, where he worked on security tooling, though much of the work on Gitleaks itself still happened outside his day job.

In 2023, Rice joined Ayrey at Truffle Security, a company built around TruffleHog that also brought together other open-source secret-scanning projects, including [Nosey Parker](https://github.com/praetorian-inc/noseyparker), under the same umbrella — an effort to “[unite core stewardship](https://www.intelcapital.com/truffle-blogsecrets-everywhere-why-we-co-led-truffle-securitys-series-b/)” of several of the most widely used tools in the space.

That move, however, changed the context around Gitleaks. At Truffle, Rice’s focus shifted toward TruffleHog, and development on Gitleaks slowed. While he continued to maintain it, the project was no longer something he could push forward in the same way, with most of the support continuing after work.

This is something Rice also alluded to in the [Betterleaks launch post this month](https://www.aikido.dev/blog/betterleaks-gitleaks-successor), in which he described losing control of the project.

“To be transparent, I don’t have full control over the Gitleaks repo and name anymore,” Rice noted. “It sucks, but it also gives me the opportunity to start something fresh. Something… *better*?”

## A drop-in replacement

Rice joined Aikido in early February as head of secrets scanning, with a simple brief: build the best open source secrets scanner.

And so Betterleaks is, by Rice’s own description, a drop-in replacement for Gitleaks: the old CLI commands still work, old configs still work, and teams should be able to switch without reworking their setup.

The clearest shift is in how Betterleaks handles validation. Rather than hard-coding that logic in Go, Betterleaks uses the Common Expression Language ([CEL](https://cel.dev/)) to define the checks that decide whether a candidate string is likely to be a real secret. CEL is designed to be fast, portable, and safe to embed in other applications, making it a tidy fit for writing validation rules without turning the scanner itself into a tangle of custom code. In plain English, this means it offers security teams a more flexible way to define what should count as a live credential and what should be ignored.

Rice is also trying to replace one of the blunter instruments in secret scanning. Traditional scanners often rely on [entropy](https://en.wikipedia.org/wiki/Entropic_security), a measure of how random a string looks. Betterleaks instead uses what Rice calls token efficiency scanning, based on [BPE](https://en.wikipedia.org/wiki/Byte-pair_encoding) tokenization. The idea is that ordinary text and machine credentials break down differently when passed through a tokenizer.

The rest of the changes are more mechanical, but no less important. Betterleaks is written in pure Go, without [CGO](https://go.dev/wiki/cgo) or [Hyperscan](https://www.intel.com/content/www/us/en/developer/articles/technical/introduction-to-hyperscan.html), so it doesn’t rely on external C libraries or specialized scanning engines, making it easier to run consistently across different environments. It also adds default detection for doubly and triply encoded credentials, and supports parallelized Git scanning for faster repository scans.

The Betterleaks roadmap goes further. Rice says future versions will scan more sources beyond Git repos and files, add optional LLM-based classification using anonymized data, support secret revocation where providers expose the right APIs, map what a leaked credential can actually access, and more.

For Rice, the aim is to move development forward without forcing existing users to switch. And while his focus is now on Betterleaks, he says Gitleaks will remain stable for those who choose to keep using it.

“Hopefully it’s not going to cause too much of a backlash to the community – I love the Gitleaks community, and I don’t want to fracture that,” Rice says. “So if you want to continue using Gitleaks, feel free. It’s stable, and security patches and stuff like that, I’ll continue to do. But if you want the next generation of Gitleaks and the evolution, then switch to Betterleaks.”

## ‘Prime for the AI agent era’

While many open source projects are established with a view toward spawning a commercial product, Betterleaks itself is unlikely to move in that direction.

The project is open-sourced under an MIT license, with Rice retaining ownership and Aikido acting as a sponsor rather than an outright owner. The company is backing the work as part of a broader push into open source security tooling, which includes projects such as OpenGrep (a Semgrep fork), Zen, Intel, and [Safe Chain](https://www.aikido.dev/blog/introducing-safe-chain).

“Like what Aikido did with OpenGrep, we’re dedicated to providing really great open source projects for the security community,” Rice explains. “A strong open source project is the backbone of a lot of the security products out there. Yes, it’s beneficial to other companies, but it’s also really beneficial to Aikido to have these stable projects.”

It’s also worth noting that Rice is not building Betterleaks alone. Three long-time contributors from the Gitleaks community — [Richard Gomez](https://www.linkedin.com/in/r-gomez/), director of software development at the Royal Bank of Canada; [Braxton Plaxco](https://www.linkedin.com/in/bplaxco/), a senior information security analyst at Red Hat; and [Ahrav Dutta](https://www.linkedin.com/in/ahrav/), a software engineer at Amazon — are co-maintainers, a shift he says is intended to improve stability and ensure the project is not dependent on a single individual.

> “Betterleaks is prime for the AI agent era … When code is generated, you can check it for secrets — and if it finds one, it’s flagged. That’s really it.”

That structure reflects a broader view of how security tooling is evolving: built in the open and designed to be flexible enough to fit into different environments — including AI-driven development setups.

Rice says that AI agents already rely heavily on command-line tools to navigate and analyse code. Betterleaks is being built with that same pattern in mind, allowing it to slot into automated workflows in much the same way as tools like [Grep](https://en.wikipedia.org/wiki/Grep).

“Betterleaks is prime for the AI agent era,” Rice says. “It’s really easy for AI agents to use. When code is generated, you can check it for secrets — and if it finds one, it’s flagged. That’s really it.”

The result is a security scanner aimed not just at catching leaked credentials after the fact, but at being part of the loop in which code is written in the first place – whether by humans or machines.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)