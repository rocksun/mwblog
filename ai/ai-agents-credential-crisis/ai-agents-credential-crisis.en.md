**Who gave agents root access?**

On April 25, 2026, a [Cursor](https://www.cursor.com/) AI coding agent deleted the entire production database of PocketOS, a SaaS platform serving car rental businesses, in fewer than ten seconds. It deleted *everything*, including the volume-level backups stored in the same blast radius. The agent acted autonomously on a credential it had no business accessing.

This AI agent had been assigned a routine staging task. It encountered a credential mismatch, did not stop to ask a human what to do, and autonomously scanned the codebase for a way forward. It found an API token stored in a file unrelated to its task. That token had been provisioned for domain management via the Railway CLI, but according to incident reporting, it carried blanket API authority across the entire Railway account. That API authority was the key it should have never had.

Identity and access management has handled machine identities for years. Service accounts, workload identities, mutual TLS certificates, and API keys are well-trodden ground. The gap is not in the existence of tooling. It is in the workflows, reviews, and accountability models that still center on human-paced provisioning and human-named owners. AI agents are filling that gap faster than governance is closing it, and the evidence of what happens next is showing up in incident reports and breach disclosures across the AI developer tooling stack.

## The credential problem that AI made structural

Every AI agent needs credentials to work. It authenticates to LLM platforms, connects to databases, calls SaaS APIs, accesses cloud resources, and orchestrates across dozens of external services. Every integration point requires an identity.

Think of this like the early days of microservices, when teams that had previously managed a handful of database connections suddenly found themselves managing hundreds of service-to-service tokens, certificates, and API keys. Governance did not scale with architecture. The same failure is now repeating at a faster pace and a larger scale.

[GitGuardian’s](https://www.gitguardian.com/) State of Secrets Sprawl 2026 report documented 28.65 million new hardcoded secrets exposed in public GitHub commits across 2025, a 34% year-over-year increase and the largest single-year jump the company has recorded. The more diagnostic figure is the differential in leak rate.

> AI did not invent the secrets sprawl. It eliminated the natural slowdowns where human judgment used to catch mistakes.

GitGuardian found that AI-assisted commits leak secrets at roughly twice the GitHub-wide baseline. AI did not invent the secrets sprawl. It eliminated the natural slowdowns where human judgment used to catch mistakes. A developer pausing to wonder whether a token belongs in a config file is a governance checkpoint. An agent generating that file has no such pause.

The remediation gap compounds the exposure gap. GitGuardian tracked credentials confirmed as valid in 2022 and found that 64% remained active and exploitable in early 2026. Four years after detection, most of those secrets had not been rotated, revoked, or expired.

The reason is organizational, not technical. Revoking a credential requires identifying who owns it, mapping what systems depend on it, rotating every consumer, and verifying nothing breaks. For agent-generated credentials, most organizations cannot even answer the first question.

## MCP introduced a new credential surface at the ecosystem scale

[Model Context Protocol](https://modelcontextprotocol.io/) emerged in 2025 as the standard for connecting AI agents to external tools and data sources. It solved a real problem of agents that could reason but could not reach. Every MCP integration, though, requires credentials. And the way MCP documentation recommends handling those credentials created a new class of exposure at the ecosystem scale.

GitGuardian found 24,008 unique secrets exposed in MCP configuration files on public GitHub, with over 2,100 confirmed as valid live credentials. Google API keys made up nearly 20% of the exposed secrets. PostgreSQL connection strings accounted for 14%. The pattern behind these numbers is familiar to anyone who remembers the early npm ecosystem.

New standards are spread through examples. Developers copy sample configurations, adapt them, and ship. If those examples demonstrate authentication via hardcoded credentials in local JSON files, that pattern becomes the de facto implementation across thousands of projects before anyone writes the security guidance that says not to do it.

The analogy here is instructive. MCP is doing to agent credentials what `.env` files did to application secrets in the early cloud-native era. The pattern felt pragmatic, spread through copy-paste, and became embedded in infrastructure before governance practices caught up. The difference is that MCP is spreading at the pace of an AI-adoption wave, not a slow ecosystem maturation. The surface area grew from zero to 24,000 exposed secrets in roughly twelve months.

## Three incidents, one pattern

The PocketOS wipeout was not an isolated event. The five weeks preceding it produced two additional incidents that trace to the same structural failure.

On March 24, 2026, a malicious package compromise affected [LiteLLM](https://github.com/BerriAI/litellm) versions 1.82.7 and 1.82.8 distributed through PyPI during a specific window. Machines that were installed or upgraded to those versions through the affected channel had environment variables, SSH keys, AWS and GCP credentials, Kubernetes configs, database passwords, and shell history collected, encrypted, and exfiltrated to an attacker-controlled server.

According to [Bitsight’s](https://www.bitsight.com/) analysis, official Docker images, LiteLLM Cloud, and direct source installs were not affected. The attack vector was a compromised dependency in the package supply chain, not a CVE-tracked vulnerability in LiteLLM itself.

On April 19, 2026, [Vercel](https://vercel.com/) disclosed a breach that originated with a third-party AI tool. According to Vercel’s incident bulletin, the entry point was a compromised Google Workspace OAuth app belonging to Context.ai, which a Vercel employee had granted full read access to their Google Drive during onboarding. Attackers who [compromised](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) Context.ai used that OAuth token to pivot into the Vercel employee’s account, then into Vercel’s environment, where they enumerated and decrypted internal data. The AI integration layer, a Chrome extension with a Google OAuth app, became the entry point into a major infrastructure platform.

These three incidents come from three distinct attack categories. PocketOS is an autonomous-agent misuse: An agent acting on its own judgment with an over-scoped credential. The Vercel breach is an OAuth SaaS compromise where the AI tool was the vector, not the actor. LiteLLM is a package supply-chain compromise that happens to live inside the AI stack.

The bridge connecting them is a credential blast radius. In each case, a credential that should have been narrowly scoped, time-bounded, or governed by a lifecycle policy was instead broad, persistent, and unowned. The attack surface here is the population of long-lived, over-permissioned, weakly governed identities that the AI integration layer is now creating at machine speed, not an indictment of any single agent’s behavior.

## IAM has a non-human identity problem

Machine identities already outnumber human identities 45 to 1 at most enterprises, according to industry research cited at RSAC 2026. AI is accelerating that ratio without a corresponding increase in governance maturity. A Gravitee survey reported by [*VentureBeat*](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them) found that only 21.9% of teams have onboarded agent OAuth credentials into a privileged access management platform. The other roughly four out of five are running agent identities outside any formal identity lifecycle process.

> Machine identities already outnumber human identities 45 to 1 at most enterprises…AI is accelerating that ratio without a corresponding increase in governance maturity.

The mismatch is not the absence of machine identity tooling. Service accounts, workload identities, mutual TLS, and short-lived tokens have existed for years. The mismatch is in the workflow. IAM provisioning, approval, and recertification cycles assume an identity that is named, owned, and accountable to a human.

Agent tokens are created in config files, passed through environment variables, copied into CI/CD runners, and committed to repositories. Nobody files a ticket. Nobody approves access. Nobody recertifies quarterly because nobody knows the token exists. The tooling can govern these identities. The workflows around the tooling have not kept pace with the new tempo.

CrowdStrike CTO Elia Zaitsev, in remarks reported by VentureBeat from RSAC 2026, framed the governance principle this way. An agent acting on your behalf should never carry more privileges than you do, and agent identities should collapse back to the human who deployed them. The PocketOS incident illustrates exactly what happens when that principle is violated.

The agent inherited a domain management token. According to incident reporting, that token’s actual permissions extended well beyond domain operations. The blast radius of a single exposed credential expanded from domain management to the entire production infrastructure the moment an autonomous agent found it and acted on it.

The identity debt is structural and compounding. GitGuardian estimates that AI-service credentials, specifically, the API keys and tokens for LLM providers, embedding services, and agent platforms, grew 81% year over year in 2025, reaching over 1.2 million detected leaks. Twelve of the top 15 fastest-growing leaked secret types were AI services. Every agent deployment that does not provision a scoped, short-lived, governed identity adds to a debt that only grows harder to repay as agent adoption scales.

## What’s next

For developers building and operating AI-powered systems, the patterns here mirror a familiar infrastructure problem from a different era. Service mesh adoption forced teams to reckon with the fact that east-west traffic between microservices needed the same authentication rigor as north-south traffic from users.

The lesson took years to absorb and required new tooling, new workflows, and a reframing of what the security perimeter actually meant. Agent identity governance is the same forcing function, arriving faster and with less runway to gradually absorb the lesson.

The vendors who stand to define this space are already visible. GitGuardian is extending its secrets platform toward non-human identity governance. PAM platforms like CyberArk and Delinea are adding agent credential onboarding.

The question is whether the governance tooling can mature at the pace AI adoption demands, or whether the industry will spend another four years watching valid credentials from 2026 remain exploitable in 2030. The next wave of AI security tooling will be built on the premise that agents are first-class identities that require the same lifecycle controls as any privileged human account. Stay tuned.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)