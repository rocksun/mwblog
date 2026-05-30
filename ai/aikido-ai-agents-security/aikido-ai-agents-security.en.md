“There is no accountability.”

It’s how [Willem Delbare](https://www.linkedin.com/in/willemdelbare/), co-founder, CTO, and CEO of [Aikido Security,](https://www.aikido.dev/) describes to *The New Stack* situations in which an AI agent installs a package and nobody has decided who should be responsible for it.

It exposes enterprises to all manner of attacks as people across the org — marketing, sales, product — use AI.

At most companies right now, no one has made the decision, and no one owns the risk. There’s a gap that has opened up, allowing attacks to slip through, Delbare says.

That is the gap Delbare says his Aikido Security is trying to close. As AI coding agents like Claude Code, GitHub Copilot, and Cursor increasingly pull packages, add dependencies, and install tools autonomously, security teams are flying blind.

Last month, Aikido introduced [Aikido Endpoint](https://www.aikido.dev/protect/device-protection), which inspects packages, plugins, and IDE and browser extensions beforeevery installation and automatically blocks malware before it’s downloaded.

Endpoint enables enterprises to securely and at scale embrace AI-native software development workflows by providing security teams with real-time monitoring and policy enforcement, while giving developers the flexibility to safely use packages, MCPs, extensions, AI models, and AI agents to meet the demands of modern development.

In March, the company also debuted [Aikido Infinite](https://thenewstack.io/aikido-self-securing-software/), a continuous AI penetration testing platform designed to make software self-securing. It aims to address the limitations of traditional, manual penetration testing by providing continuous security validation throughout the software development lifecycle.

Akido isn’t alone in this market. Socket, which just closed a $60 million Series C at a $1 billion valuation, focuses on real-time detection and blocking of malicious open source packages — claiming it identified a malicious dependency in the widely used Axios JavaScript package within six minutes and helped organizations block it before it reached production. Endor Labs, meanwhile, launched AURI in March 2026, a Skills plugin, an MCP server, and a CLI designed to detect actual vulnerabilities in real time within coding assistants like Cursor and Claude Code.

[Chainguard](https://thenewstack.io/chainguard-500-million-builds/) takes a different angle entirely, providing hardened minimal container images and curated package repositories — securing the infrastructure layer before a line of code is written. [Earlier this year, Snyk](https://thenewstack.io/security-firm-snyk-tackles-ai-codings-perfect-storm/)‘s security researchers completed what they called the first comprehensive audit of the AI agent skills ecosystem, scanning nearly 4,000 skills and finding that more than a third contained at least one security flaw — underscoring how quickly the attack surface is expanding across the entire market. Also, [Arcjet](https://thenewstack.io/arcjet-wafs-guards-ai-agents-security/) provides runtime enforcement inside agentic workflows, prompt injection, and PII blocking. And [Mobb Security](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/) goes after AI agent skill supply chain vulnerabilities.

Delbare spoke with *The New Stack* about where Aikido fits in that landscape — and why he thinks the accountability gap is the problem the industry has yet to solve.

*The following interview has been edited for clarity and brevity.*

**Who owns the security policy for what an AI coding agent is allowed to install — is that a developer decision, a security team decision, or is it undefined at most companies right now?**

At most companies right now, it’s undefined, and that’s a real risk. When a human developer installs a package, there’s at least implicit accountability. When an agent acts autonomously, there is no accountability unless someone has deliberately assumed ownership.

Our view is that security teams need to set the guardrails (the policies, thresholds, and approved ecosystems), and developers should be able to move freely within them. The agent operates inside that envelope. That’s not a new model; it’s just applying the same shared responsibility model that works for human developers.

**Most enterprises have no visibility into agent-initiated installs. Is Aikido seeing this in customer environments — agents quietly pulling in packages that nobody reviewed?**

Just today, we had a discussion with a customer who wants to make sure even non-developer devices are covered. Less technical teams in product, sales, and marketing are using AI agents to accomplish work without realizing that packages and agent skills are being installed in their local environments. Security teams have essentially no control or visibility into the risk or a way to identify affected machines after an incident.

**AI coding agents pull packages and add dependencies autonomously — how does Endpoint distinguish between a human-initiated install and an agent-initiated one, and does that distinction change how it responds?**

It doesn’t make a distinction. The risk of installing malware is independent of a human or agent-initiated action.

**Which AI coding agents (Copilot, Cursor, Claude Code, Devin, etc.) does Endpoint currently monitor, and how does coverage work as new ones ship?**

Endpoint monitors AI tools and models across Gemini, OpenAI, GitHub Copilot, xAI, MCP Servers, Claude Code, and [skills.sh](http://skills.sh). The agent just needs to be updated when new ones ship.

**AI agent skills marketplaces are listed as a coverage area — which ones specifically, and how mature is that coverage?**

Currently, we cover [skills.sh](http://skills.sh) and the VS Code Marketplace.

**Your press release mentions the “$8 ChatGPT subscription,” lowering the barrier to writing supply chain malware. What does AI-generated supply chain malware actually look like differently from human-written — is it harder to detect, more polymorphic, higher volume?**

AI is fueling much more sophisticated attacks. In twelve months, we went from single-package compromises to self-replicating worms to full CI/CD pipeline hijacks chaining across registries. The principal changes are a reduced barrier to entry and attack velocity. Where a talented hacker might spend significant time probing for vulnerabilities, this work can now be dispatched to AI agents.

**Does [Aikido Intel](https://intel.aikido.dev/), which cites a 100,000 malicious packages/day figure, use AI detection to keep up with AI-generated malware? What’s the methodology?**

Yes, Aikido Intel uses AI and our in-house research team to discover vulnerabilities in the open source supply chain.

Intel works by reviewing all publicly available changelogs and release notes to determine whether security fixes have been made but not disclosed. We use two LLM models to achieve this. One LLM is used to filter the data and remove all unnecessary context. Then, the second LLM focuses on vulnerability analysis. A human security engineer then reviews the LLMs’ discoveries, validates the findings, and releases an Intel when a vulnerability is confirmed.

This methodology has been extremely effective at identifying vulnerabilities while requiring much less computational power than scanning all codebases, systems, or live environments directly for potential security issues with LLMs.

**Endpoint enforces a 48-hour install block. That’s a blunt instrument — lots of legitimate packages ship fast. How many false positives does that generate in practice, and how does the request-and-approval workflow handle developer friction?**In practice, how often does a developer *need* the version that shipped this morning rather than the one from last week? Almost never. The install block targets a window in which the vast majority of malicious packages are caught, and legitimate development is almost never blocked.  
  
Endpoint falls back to an allowed package version. In this case, a version older than the 48-hour install block. But the install block is a configurable setting. Teams can match the install block to their risk tolerance per ecosystem. For example, as many attacks have targeted npm, 48 hours might make sense, whereas for Maven Central, with its GPG signing requirements, you may not need an install block.  
  
Packages or entire groups of packages can be whitelisted, which bypasses the install block, and, for installs that need to move faster, developers can request one-off approvals.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)