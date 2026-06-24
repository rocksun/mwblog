Chainguard is expanding its push to secure the fast‑growing world of AI coding agents with a new public registry of more than 1,000 hardened agent skills, a private registry, and a hardening service for internal, organization‑specific skills.

Blink twice, and there’s a new, major AI development. And, alas, a security vulnerability to go with it. That’s why software supply chain security company [Chainguard](https://www.chainguard.dev/) Co‑Founder and CEO [Dan Lorenc](https://www.linkedin.com/in/danlorenc) recently introduced [Chainguard Agent Skills](https://www.chainguard.dev/agent-skills). This is a [continuously maintained catalog of hardened AI agent skills](https://www.zdnet.com/article/how-chainguard-is-fixing-trust-in-ai-built-software/) meant to bring “secure by default” practices to the emerging agent ecosystem. Now, Chainguard has taken Agent Skills to its next level.

With this update Agent Skills offers customers secured community skills and a home for an organization’s internal skills.. In addition, it now provides a hardening‑as‑a‑service tier for teams that want Chainguard to do the heavy lifting to ensure their homebrew agents are safe.

[Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland), Chainguard’s SVP of engineering, told me Agent Skills enables teams to plug agents directly into their software build and review pipeline without worrying that a compromised skill might introduce vulnerabilities or exfiltrate data: “That’s what we’re insulating our customers against.”

This new release offers hardened versions of more than a thousand of the most popular community skills, with new ones added every week. The [public catalog and its secure agents are available for anyone to pull today](https://www.chainguard.dev/agent-skills).

The company’s hardening pipeline scans public skills against a ruleset designed to catch common and emerging attack patterns. These include:

* Over‑permissioned scopes and capabilities
* Obfuscated commands and base64 execution
* Credential harvesting behavior
* Downloads from untrusted or suspicious domains

In short, the idea is simple: Treat agent skills as first‑class software artifacts with the same governance, provenance, and hardening that [Chainguard containers](https://thenewstack.io/chainguard-and-the-hunt-for-truly-zero-cve-container-images/) and [open source packages](https://thenewstack.io/chainguard-repository-ai-agents/) already deliver.

## Hardening as a continuous process, not a one-time gate

This updated service does more than just scan for problems. Chainguard is not positioning this as yet another scanning or “find‑and‑flag” service. When the ruleset detects a problem, the system uses AI to actually rewrite and harden the skill. Each hardened skill ships with a HARDENING.md document that serves as an audit log: which rules ran, what was found, what was changed, and confirmation that the changes didn’t break the skill’s behavior in material ways.

A key design principle here is to treat hardening as a continuous process rather than a one-and-done static approval gate. Chainguard is explicit that “a skill that’s safe today can be compromised in tomorrow’s update.” Welcome to the world of AI-enabled development, where security vulnerabilities arise daily.

Whenever an upstream skill changes, the Chainguard pipeline automatically re‑evaluates and re-hardens it. At the same time, the company continuously updates its hardening rules to catch new attack patterns; when the ruleset changes, previously hardened skills are re‑run through the process. For end users, that means they’re always pulling the current hardened version, rather than relying on a one‑off scan that may be months out of date.

Developers can browse and install hardened skills into a range of agentic coding tools. Specifically, the service is available for Claude Code, Cursor, GitHub Copilot, and the Gemini CLI via its chainctl command‑line tool. The goal is to make switching from “raw community skills” to “hardened skills with audit trails” a drop‑in change for teams already experimenting with agent workflows in their IDEs and CLIs.

Chainguard is also trying to solve the related problem of the growing sprawl of internal agent skills within organizations. Today, many of those skills live in Slack threads, ad‑hoc shared folders, and individual developer environments, with little or no versioning, access control, or observability. This is a pathetic practice.

Chainguard’s answer is to provide internal skills with a proper registry namespace. Skills live at skills.cgr.dev/<org>/<skill\_name>:<version>, and teams can push and pull them with chainctl, installing locally in a single command.

This centralizes discoverability, so teams stop rebuilding workflows that already exist elsewhere in the company. It also brings versioning discipline to agent behavior. Organizations can pin agents to specific skill SHAs, roll back when changes cause issues, and diff what changed between versions.

Entitlements are scoped to the organization’s namespace. Thus, only that org can push or pull skills from its registry space. That boundary matters for teams working under strict compliance regimes or handling sensitive data. Internal agent skills can be shared and reused across the company without leaking outside it.

The company is also opening a closed beta for customers who want Chainguard to automatically harden their in‑house skills. This comes complete with audit trails, MCP integration, and supply-chain-style controls over agent behavior.

With this beta, customers can submit their own skills into Chainguard’s hardening pipeline and layer custom checks on top of the standard ruleset. In return, they get:

* Automated review and remediation of their internal skills.
* The same HARDENING.md audit trails as community skills.
* A continuous hardening loop as upstream code or rules change.

The beta also ships with [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) integration. This is handy for organizations that surface and enforce skills through MCP servers and policy engines. Early participants will be among the first to use Agent Skills capabilities via these channels. This connects hardening directly to how skills are exposed to agents and governed in production.

This isn’t for everyone. Its target users are teams building internal agent tooling at scale, or operating in environments where custom skills carry “real compliance weight.” For those organizations, being able to show regulators or auditors a concrete hardening pipeline and per‑skill audit logs could become as important as SBOMs and provenance attestations are for more traditional software components.

If all this sounds familiar, you’re right. Chainguard is positioning Agent Skills as a direct continuation of the company’s earlier work on containers and language ecosystems. Chainguard sees a familiar pattern reappearing. That is a new class of third‑party artifact arrives, adoption races ahead of governance, and the attack surface expands before the ecosystem really knows how to respond. In their view, agent skills are squarely in that window today.

Chainguard is making the public catalog of hardened skills and the private skills registry available as standard features to anyone with a [Chainguard Console](https://c67dcd9a.streak-link.com/C7TcucEnp5LVE__5ugXNRoZ_/https%3A%2F%2Fedu.chainguard.dev%2Fchainguard%2Fchainguard-images%2Fhow-to-use%2Fimages-directory%2F) account. The company is also inviting high‑stakes users into the closed beta for custom skill hardening. [You can sign up for the closed beta today.](https://c67dcd9a.streak-link.com/C7KRc2i_f2amC3LIoQtzgcCs/https%3A%2F%2Fwww.chainguard.dev%2Fagent-skills)

This approach makes perfect sense to me. Anyone doing AI agent-enabled development — is anyone not? —Should check out this new service.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)