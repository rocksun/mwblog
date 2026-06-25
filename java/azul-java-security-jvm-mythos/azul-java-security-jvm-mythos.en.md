[Azul Systems](azul.com) is offering a free [Java Virtual Machine (JVM)](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) vulnerability risk assessment designed to reveal Java runtime exposure before AI-assisted attackers can crack their systems, but the company’s threat framing leans heavily on Anthropic’s unverified [Mythos](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) model as its lead.

Azul, a Sunnyvale, California-based Java runtime vendor, is pitching the risk assessment tool to [DevOps](https://thenewstack.io/devops/) and [SecOps](https://thenewstack.io/how-azure-copilots-new-agents-automate-devops-and-secops/) teams that lack full visibility into their Java estates. Here’s how it works: The tool scans networks to identify JVM instances — including embedded and unmanaged runtimes that standard asset discovery tools often miss. After the scan, it returns a prioritized remediation roadmap cross-referenced against the CISA Known Exploited Vulnerability (KEV) catalog and the U.S. National Vulnerability Database, the company says.

Azul, of course, makes its own JVM and sells support for it, and the free scan is a lead-gen play that converts to Azul Core subscriptions.

This posture targets Azul’s security-only Critical Patch Updates, which the company claims is the only OpenJDK distribution to ship security fixes exclusively, with no new features or bundled bug patches — not [AWS Corretto](https://www.theserverside.com/news/252452738/Amazon-Corretto-extends-OpenJDK-support) or [Eclipse Temurin](https://thenewstack.io/why-bloomberg-chose-vendor-neutral-java-over-big-tech/), [Eric Costlow](https://www.linkedin.com/in/costlow/), Azul’s senior director of product management, tells *The New Stack*. The value proposition for customers is lower risk of breakage when patching long-running Java estates, he says.

“One of the reasons people haven’t updated their JVMs in a long time is they’re worried about breaking something,” Costlow says. “So they look at it and say, ‘It ain’t broke, don’t fix it.’ What Core offers is a version of Java that only contains security patches — all it does is fix security vulnerabilities. The risk of breaking your application by applying the security-only release is really low, because all it does is fix security bugs.”

That’s the differentiation pitch against Corretto, Eclipse Temurin, and other OpenJDK distributions.

“If you grab a Corretto or an Eclipse JVM, they’re very nice people,” Costlow says. “But they just include everything in their build. Everything that changes, it’s in there. Let’s say it has a 1% chance of breaking something — you update 100 apps, one of them breaks. Our breakage rate might be like 0.1% or something, because we don’t do that other stuff.”

## The AI threat argument

The core security argument is that AI tooling has shortened mean time to exploit from months to days or hours, making unpatched Java estates more dangerous than they were even 18 months ago. Costlow describes it as AI had lowered the barrier to both discovery and weaponization.

“You can build crawlers that look for older Java versions because you can identify them through a lot of signatures,” he says. “And the exploits — where you used to say, ‘I have a version of an exploit that will attack a certain version of [Spring](https://thenewstack.io/production-worthy-ai-with-spring-ai-1-0/), it used to only work in certain scenarios’ — the AI has made it a lot easier to generalize those exploits. The stuff’s easier to find and easier to attack. Unfortunately.”

In a [blog post](https://www.azul.com/blog/get-your-java-estate-ready-for-the-growing-agentic-ai-threat/), [Dana Crane](https://www.linkedin.com/in/danamcrane/), product marketing director for Platform Core, delivers research to back that up. A [2024 University of Illinois Urbana-Champaign study](https://arxiv.org/pdf/2404.08144) found that GPT-4, given appropriate scaffolding, could autonomously exploit 87% of known critical-severity CVEs with no human in the loop, at roughly $8.80 per successful exploit. A follow-up from the same group showed AI agent teams hitting zero-day vulnerabilities at a 53% success rate. More recently, an AI system called ARTEMIS placed second against human penetration testers on a live enterprise network of 8,000 hosts, finding valid vulnerabilities at $18 per hour versus $60 per hour for the humans it outperformed, the study shows.

What’s harder to assess is Azul’s lead claim, which leans heavily on Anthropic’s Mythos model — a frontier AI system that has not been publicly released and that Anthropic has kept gated to a small number of trusted organizations.

The Azul press release states that “Anthropic’s Claude Mythos demonstrates that AI can autonomously uncover previously unknown vulnerabilities and generate working exploit paths at scale.”

Moreover, Azul CEO [Scott Sellers](https://www.linkedin.com/in/ssellers/), in a statement says, “Anthropic’s Mythos has shown that AI can now discover and weaponize vulnerabilities on its own — including flaws that survived decades of human review.”

Azul’s FAQ goes further, noting “how quickly Mythos-class capability escaped its intended containment” as a reason to patch faster. However, when asked in the briefing whether the company had actually tested Mythos against JVM vulnerabilities, Costlow notes that he didn’t have access to the model. “That’s gated by a lot of government stuff,” he tells *The New Stack*. “It’s only for select organizations now.”

In other words, Azul is using a model it hasn’t tested, and that no one outside a handful of vetted organizations has used, as the key to its threat narrative.

## What the assessment actually finds

The tool itself is a network scanner that Azul says runs over a few days with no performance impact. It identifies JVM versions and ages across the full stack, including app servers, serverless containers, and databases.

The output package includes a security dashboard broken down by risk tier, publisher, and Java version; KEV and CVE exposure analysis cross-referenced against real-world threat data; end-of-life runtime identification (Java 5, 6, and 7 instances in production, which Crane notes are “more common than most IT leaders assume”); and a patch currency gap report showing how far deployed instances are from current CPU baselines.

The regulatory angle targets PCI-DSS, SOX, HIPAA, DORA, NERC CIP, and FedRAMP. These frameworks require demonstrable visibility into deployed software versions and documented patch history.

“A lot of people in the PCI DSS space are supposed to be patching their JVMs, but aren’t,” Costlow says. “If you haven’t patched in eight years, it’s really built up. I refer to it as a CDE tsunami.”

Meanwhile, Crane says: “A typical assessment reveals that a small number of Java versions — often just two or three — account for the lion’s share of risk across an enterprise estate. That makes mitigation far more tractable than it initially appears.”

The assessment is available at no cost from Azul and through select partners, at azul.com/jvm-vulnerability-risk-assessment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)