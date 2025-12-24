AI was big in 2025, but so were many other developments and worries.

The biggest open source stories in 2025 clustered around AI, licensing/governance, security and the shift in the “commercial open source” business model. Let’s start, shall we?

## 1. Open Source AI Goes Big

While most of the money went to proprietary models, open source AI datasets, orchestration frameworks, evaluation tools and guardrail stacks have all seen gains.

Such open source AI efforts as [Common Corpus](https://huggingface.co/blog/Pclanglais/common-corpus), along with the [dozens of AI projects](https://lfaidata.foundation/projects/) hosted by [the Linux Foundation’s](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) AI & Data group are enabling us to use community infrastructure for generative AI rather than relying solely on proprietary APIs, making open AI stacks a serious option for businesses and users.

While the [open source AI definition remains controversial](https://thenewstack.io/what-is-open-source-ai-anyway/), and very few AI projects fully qualify as open source by the strict requirements of the [Open Source Initiative (OSI) AI definition](https://thenewstack.io/the-open-source-ai-definition-is-out/), [AI remains built on a foundation of open source software](https://www.zdnet.com/article/why-open-source-is-the-cradle-of-artificial-intelligence/). The debate over open weights, data and training code will continue, but even the most proprietary [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) couldn’t exist without open source programs.

[Agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/), owes everything to open source. To orchestrate our latest generation of AI agents, we’re using several programs.

The most important of these, at this early stage of the game, appears to be the [Model Context Protocol (MCP).](https://modelcontextprotocol.io/) This is an open standard and open source implementation for uniformly connecting agents to tools, files, databases and other systems.

MCP is increasingly the “plumbing layer” under many agents and IDE assistants, and there are [numerous open source MCP servers and toolkits](https://thenewstack.io/10-mcp-servers-for-frontend-developers/) that let any compatible agent framework plug into the same tools.

MCP isn’t the only agentic AI middleware that’s speeding up:

## 2. Fights Over ‘Open’  vs. ‘Source Available’ Licenses Rage On

[A Linux Foundation report released in August](https://www.linuxfoundation.org/research/2025-state-of-commercial-open-source) showed that venture capital‑backed commercial open source companies have outperformed comparable closed‑source vendors over the last 25 years.

That report, alongside open source adoption data from [an April OSI survey](https://opensource.org/blog/key-insights-from-the-2025-state-of-open-source-report), which from 96% of organizations are maintaining or increasing open source software use, has cemented commercial open source as the default way to build software.

Together, these reports are driving more funding, more mergers and acquisitions, and more “open core plus services” strategies around critical open source projects.

Of course, we knew that. After all, a 2024 Harvard Business School study already showed that  [96% of commercial programs rely on open source](https://www.library.hbs.edu/working-knowledge/open-source-software-the-nine-trillion-resource-companies-take-for-granted) and that the total value of open source code comes to a cool $8.8 trillion. That still doesn’t stop companies that made the mistake of [confusing open source as a software development model with a business model](https://opensourcewatch.beehiiv.com/p/open-source-not-business-model-never); it never was. It never will be.

So it is that in 2025, we saw more companies move from [open source to fauxpen source](https://www.theregister.com/2024/04/12/linux_foundation_opinion/). For example, the [ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention)team announced in December 2024 that it would [move to a single “ScyllaDB Enterprise”](https://www.scylladb.com/2024/12/18/why-were-moving-to-a-source-available-license/) stream under a source‑available license.

At the library level, there have been high‑profile examples of previously permissive projects switching quietly to source‑available, paid‑for‑commercial‑use terms, such as the [Fluent Assertions .NET testing library](https://devclass.com/2025/01/16/another-open-source-project-shifts-to-restrictive-license-fluent-assertions-following-xceed-partnership/) moving, this past January, from Apache‑2.0 to a proprietary source‑available license with per‑developer fees.

Then, there’s the DevOps program [Puppet](https://puppet.com/?utm_content=inline+mention). Although Puppet’s core codebase is still under the Apache 2.0 open source license, its commercial parent company, [Perforce](https://www.perforce.com/), has changed how official builds are distributed and licensed.

What changed is that new “hardened” binaries and packages built by [Puppet/Perforce are now shipped from a private repository](https://www.puppet.com/blog/open-source-puppet-updates-2025). The [Puppet Core End User License Agreement (EULA)](https://forge.puppet.com/eula) offers a free tier capped at 25 nodes, with commercial licensing required for additional nodes. Effectively, this makes Puppet a source-available program, even though the code is technically still open.

The result in Puppet’s case is the same as we’ve seen in other such attempts to close once open source projects: Unhappy programmers have forked the project. The [fork is known as OpenVox](https://thenewstack.io/openvox-the-community-driven-fork-of-puppet-has-arrived/).

These forked projects, which include Elasticsearch with its fork [OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation), [Redis](https://redis.com/?utm_content=inline+mention) with the [Valkey](https://thenewstack.io/navigating-the-path-from-redis-to-valkey) fork, and Terraform with the [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next) fork, [have been somewhat successful](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/). All four forks have achieved meaningful traction, but at different scales and under different definitions of  “success.”

[OpenSearch appears to be the most successful](https://www.linuxfoundation.org/press/opensearch-software-foundation-marks-1-year-anniversary-with-community-growth-agentic-ai-and-hybrid-search-enhancements). It reports strong growth, including double‑digit, 78%, year‑over‑year download increases and a roster of major members such as [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), Canonical, [SAP](https://www.sap.com/index.html?utm_content=inline+mention) and Uber.

[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") has also proven to be popular. The [latest release, Valkey 9](https://thenewstack.io/valkey-9-0-debuts-multidatabase-clustering-for-massive-scale-workloads/), is reported to be far faster than the newest version of Redis. In particular, Valkey users report that it’s consistently ahead of comparable Redis releases on raw throughput, especially on larger, memory‑heavy workloads where Valkey’s multithreaded I/O and cache‑prefetching kick in.

While OpenSearch and Valkey have both advanced beyond their parent projects, Terraform vs. OpenTofu is another story. People still see [OpenTofu and Terraform as differing only in their licenses.](https://infisical.com/blog/terraform-vs-opentofu) Over the last few months, though, that’s been changing as OpenTofu, which [joined](https://thenewstack.io/opentofu-joins-cncf-new-home-for-open-source-iac-project/) the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) in April, steers more of its own course. [Latest releases now include state encryption](https://spacelift.io/blog/opentofu-vs-terraform#differences-between-opentofu-and-terraform), a feature the Terraform community has wanted for years, and early variable evaluation.

Finally, OpenVox continues to present itself as a “soft fork.” Its directors want it to stay 100% compatible with Puppet so it can serve as a drop-in replacement for Puppet deployments. That, however, appears to no longer be possible, as [Gene Liverman](https://www.linkedin.com/in/geneliverman/), the leader of OpenVox, wrote, “[We can no longer guarantee that our modules will work with Puppet Core](https://www.linkedin.com/pulse/unsupportable-path-gene-liverman-wngje/) or Puppet Enterprise.”

From the project maintainers’ viewpoint, Perforce is breaking compatibility. For now, though, OpenVox is essentially a healthy, community lifeboat rather than a full‑scale Puppet replacement ship.

## 3. Open Source Projects Are Starved for Funding

Despite the simple fact that we all depend on open source, all too many projects remain underfunded. Others, such as [NET 6, are still popular](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/), but their maintainers have quit supporting them. What’s a user to do?

This isn’t a new problem. Back in 2021, [Tidelift](https://tidelift.com/?utm_content=inline+mention), a security company that also financially supported open source maintainers, found that [46% of open source project maintainers received no pay](https://www.zdnet.com/article/hard-work-and-poor-pay-stresses-out-open-source-maintainers/) at all. Almost as bad, even those who were paid, a mere 26% earn more than $1,000 per year for their work.

Things have not improved. In fact, they’ve gotten worse. In 2024, Tidelift’s latest results showed that now [60% of open source maintainers are unpaid](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/).

As  [an open letter signed by 10 open source foundations](https://openssf.org/blog/2025/09/23/open-infrastructure-is-not-free-a-joint-statement-on-sustainable-stewardship/)  and published in September pointed out, “Most of these [open source] systems operate under a dangerously fragile premise: They are often maintained, operated, and funded in ways that rely on goodwill, rather than mechanisms that align responsibility with usage.”

So it is that, according to the open letter, “a small number of organizations absorb the majority of infrastructure costs, while the overwhelming majority of large-scale users, including commercial entities that generate demand and extract economic value, consume these services without contributing to their sustainability.”

A specific example that I’ve been covering is how [FFMpeg, which is used by everyone who watches videos over the Internet, is horribly underfunded](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/), even as major companies such as Amazon, Google and Netflix depend on its code. There are many other such projects. This can not continue.

The answer is that companies must — Must — start financially supporting mission-critical open source projects. The cost to do this is minute compared to the damage they’d suffer if these projects folded or were hit by a major security problem.

## 4. The Open Source Supply Chain Is More Vulnerable Than Ever

In 2024, the xz data compression library code, which had been [deliberately infected with malware](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/), came close to inserting a backdoor into [Fedora](https://www.fedoraproject.org/), [Red Hat’s](https://www.openshift.com/try?utm_content=inline+mention) community Linux. Had it been successful, it might have ended up in Red Hat Enterprise Linux (RHEL) and its clones.

This would have led to the greatest Linux security disaster to date. We dodged a bullet.

Unfortunately, the open source software supply chain security is under sustained, high-volume attack, with npm- and PyPI-focused campaigns escalating.

Several high-impact campaigns in 2025 centered on compromising open source package ecosystems, especially npm.

In November, researchers from Wiz, Aikido, and others detailed a “[Shai-Hulud 2.0](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)” wave of trojanized npm packages that exfiltrated developer and CI/CD credentials from environments using popular libraries tied to major Software as a Service and cloud tooling.

Tens of thousands of malicious repos were spun up as part of the campaign. [GitLab’s](https://about.gitlab.com/?utm_content=inline+mention) vulnerability research team also reported a separate widespread [npm supply chain attack that harvested credentials](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/) for GitHub, npm, and major clouds and propagated by infecting additional packages owned by victims.

These are not one-off instances. Industry threat reports in 2025 describe a surge in software supply chain attacks overall, with October setting a new monthly record, and open source ecosystems featuring prominently among the targets.

Analysis from [Palo Alto Networks’](https://www.paloaltonetworks.com/cloud-security?utm_content=inline+mention) [Unit 42](https://unit42.paloaltonetworks.com/) and other research teams notes that attackers increasingly prefer compromising maintainer accounts and publish pipelines rather than core source repos, because this path can silently poison trusted packages at scale.

[A study by ReversingLabs, released in March,](https://www.reversinglabs.com/sscs-report) reported that, while observed open source malware packages have declined somewhat, the risk has shifted toward leaked developer secrets and build-time exposures.

Researchers examining popular npm, PyPI, and RubyGems components continue to find hard-coded credentials, weak application hardening, and exposed data inside widely used binaries deployed in enterprises. That kind of mistake was stupid back in the ’80s, when I first encountered it in production software, and it’s unforgivable today.

Making matters worse, security companies such as [JFrog](https://jfrog.com/?utm_content=inline+mention) and [Veracode](https://www.veracode.com/) report that exploding dependency graphs, faster release cycles, and heavy reuse of open source libraries mean a single malicious or vulnerable package can ripple through thousands of downstream applications in days.

This dense interconnection makes the blast radius of attacks like the npm-focused campaigns in 2025 significantly larger than that of many earlier open source incidents, especially when the target libraries appear in 20 to 30% of scanned cloud environments.

What can we do about it? We must more broadly adopt [software bills of materials (SBOMs)](https://thenewstack.io/sboms-sboms-everywhere/), [Supply-chain Levels for Software Artifacts (SLSA)](https://thenewstack.io/enhance-your-sbom-success-with-slsa/)-style attestations, and tools from the Open Source Software Foundation ecosystem to track provenance and integrity of open source components.

OpenSSF and its partners highlight initiatives such as [Sigstore](https://thenewstack.io/need-to-sign-your-code-and-havent-a-clue-sigstore-can-help/) for keyless signing, [Scorecard](https://openssf.org/projects/scorecard/) for automated project risk assessment, and the [Open Source Project Security Baseline](https://baseline.openssf.org/), which aim to give both maintainers and consumers clearer security expectations.

Every year, I tell people that they must take security more seriously. Lately, as open source supply chain violations become ever more common, I’ve been saying you must ensure the code in your supply chain is both safe and written by someone trustworthy.

Looking ahead, I can only redouble these warnings. Now we’ve already had serious security breaches in the last few years. You remember: [Solarwinds](https://thenewstack.io/solarwinds-the-worlds-biggest-security-failure-and-open-sources-better-answer/), JetBrains [TeamCity](https://www.wiz.io/blog/jetbrains-teamcity-authentication-bypass-vulnerabilities-cve-2024-27198-cve-2024-27199), and [Apache Log4j](https://thenewstack.io/one-year-of-log4j/) should all come to mind quickly. As bad as those were, worse security disasters lie ahead if we don’t take open source supply chain security much more seriously.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)