Anthropic’s Model Context Protocol (MCP) went into production in late 2024. It spread rapidly after that.

Since then, thousands of MCP servers have been created. Microsoft, Google, and OpenAI embraced it. The Linux Foundation took over protocol maintenance. Today, MCP is considered critical infrastructure. It sits between an AI agent and the tools and data it interacts with. Most teams implemented it the same way they implement any other integration standard. People installed it and trusted the defaults.

The understanding that emerged in 2026 is that the problem wasn’t in the infrastructure. The problem is in the permissions below this infrastructure.

This matters because it changes how people approach MCP security problems. A patch solves a specific problem on a particular server. The permission change requires asking a complicated question.

> “The understanding that emerged in 2026 is that the problem wasn’t in the infrastructure. The problem is in the permissions below this infrastructure.”

Why did that particular server require access to something it never needed to be there? According to the SANS 2026 Identity Threats Survey, which surveyed more than 500 security experts, 76 percent of businesses noted an increase in non-human identities. 74 percent of businesses use AI systems that rely on standing credentials to work independently. This same survey revealed that none of the protection measures, such as approval processes, sandboxing, or logging, is used by more than 40 percent of businesses.

Look past the individual disclosures, and the same root cause keeps showing up. In May 2025, an attacker used prompt injection against the [GitHub MCP server](https://invariantlabs.ai/blog/mcp-github-vulnerability) to pull private repository data, not because the server had a bug in the traditional sense, but because the personal access token behind it was scoped far wider than the task required. Days later, a logic flaw in an [Asana MCP integration](https://www.bleepingcomputer.com/news/security/asana-warns-mcp-ai-feature-exposed-customer-data-to-other-orgs/) allowed cross-tenant access because the permission layer never enforced the isolation boundary between customers.

Security researchers now group it under a couple of recognizable patterns: tool poisoning, where a server’s own tool description carries hidden instructions, and the confused deputy problem, where an agent inherits more trust than the task in front of it requires.

## What a permissions redesign actually asks you to check

The solution that keeps coming up isn’t a better scanner, but compartmentalizing access. GitHub’s [Engineering Blog](https://github.blog/ai-and-ml/generative-ai/how-to-build-secure-and-scalable-remote-mcp-servers/), which discusses developing secure remote MCP servers, suggests the following: every instance must have its own secrets for the specific task, all requests must be limited to the acting user, and authorization must be based on action rather than assumed after user authentication. Replace fixed, permanent tokens with dynamic, temporary credentials generated on the fly.

> “Replace fixed, permanent tokens with dynamic, temporary credentials generated on the fly.”

This solution is tiered and has been working until now. In [Webflow](https://webflow.com/), we treat MCP integrations in the same way as we treat other third-party components with access to customer data.

![The MCP server credential scope to review cycle.](https://cdn.thenewstack.io/media/2026/09/22933462-image1-1024x582.png)

Each credential the team gives to an AI agent was probably a good idea when it was provisioned. The tough call isn’t whether that access was a good idea at the time. It’s whether it is anymore, and most teams aren’t in the habit of making it.

Some things to consider while integrating any MCP:

**What can this credential reach now, rather than the scope for which it was intended?** The scope of access is likely to creep. No review will be scheduled until something breaks.

**Is authorization granted on a per-site, per-repository, or per-Workspace basis, or all or nothing?** Be leery of any integration that only provides organizational access. If an integration doesn’t give you control over scope at connection time, that’s the finding, not a footnote.

**Does the AI agent inherit the person’s existing credentials, or create entirely new credentials that bypass those permissions?** The latter is how a GitHub personal access token can have more access to repos than the user who authorized it.

**Does logging assign accountability for what the agent does in the same way it does for a human?** If the agent’s activities are invisible or unattributable, incident response starts at ground zero.

**Do changes from the [agent go straight into production](https://thenewstack.io/agent-runtime-application-server/), or do they pass through a reviewable process like draft, branch, and approval queue first?** This is just applying the security discipline the team already has around human access controls to a newer class of entity.

## Identity comes before access

Before you can talk about what an agent is allowed to do, you have to answer a harder question: what is an agent, identity-wise? Right now the honest answer for most of the industry is “a human’s OAuth token wearing a trenchcoat.” The agent doesn’t have [its own identity](https://thenewstack.io/can-dns-become-the-basis-for-ai-agent-identity/). It inherits the scope, the blast radius, and often the literal credential of whoever spun it up.

That’s a problem the moment agents stop being ephemeral. Most agents today live for minutes to hours: a task starts, the agent runs, it dies. But that’s changing. We’re heading toward agents that run for weeks or months, and a thing that lives that long needs its own identity, not a borrowed one, with permissions that get stricter, not looser, as the lifespan grows.

> “Right now the honest answer for most of the industry is ‘a human’s OAuth token wearing a trenchcoat.'”

Think of it like the difference between a contractor you bring in for an afternoon and a contingent worker embedded in your systems for a quarter. You wouldn’t give the afternoon contractor a permanent badge, and you shouldn’t give the quarter-long agent the same access as a five-minute script.

OAuth wasn’t built for this, and it’s not just a missing feature; it’s a structural mismatch, and at root a UX failure: a consent model built for a human in the loop, applied to a process that has none.

Its whole model assumes a human sits in front of a scope dialog and makes an informed choice, and we all know how that goes: nobody reads the scope list; they click allow. That already-shaky assumption collapses completely when there’s no human reading anything.

The base spec has no concept of “this client is an agent” or “this grant is expected to run for six months,” just a server-set expiry after the fact. A few IETF drafts are starting to sketch a fix: binding token lifetime to a task’s actual lifecycle and tagging [agents with stable identities](https://thenewstack.io/agent-workload-identity-authentication/) distinct from the human who invoked them. Still, those are early-stage proposals, not deployed standard(s).

We don’t have a clean answer for where the line sits between “short-lived task, broad-ish access” and “long-lived agent, locked down tight.” Webflow’s security team is actively working through this, and we’re comparing notes with peers across the industry rather than pretending we’ve solved it. But the framing itself matters: treat agent lifespan as a first-class input to your permission model, not an afterthought.

## Permissions aren’t a checkbox at provisioning

A permissions redesign, a protocol update, and an identity model represent three distinct levels of the same problem. For each level to remain effective, the other two must be effective too.

If you create a credential with the correct scope on Day One, but then no one ever verifies that the credential remains valid, your efforts were wasted. Similarly, if you develop a new protocol that finally distinguishes an agent from the human behind it, but all integrations continue to provide standing, all-or-nothing access by default, you have done little good. Neither approach addresses the deeper question at the root of both: what an agent is permitted to do should depend on how long it will exist.

> “The teams who get this right will be the teams who stopped viewing scope, identity, and lifetime as three separate evaluations, and began treating them as a single setting.”

Right now, nearly all components of the technology stack don’t know how to ask that question, much less answer it. The teams who get this right will not be the ones who developed a [more efficient scanning](https://thenewstack.io/why-docker-scout-is-changing-how-developers-scan-for-vulnerabilities/) tool. Rather, they will be the teams who stopped viewing scope, identity, and lifetime as three separate evaluations that occur once per agent instance, and began treating them as a single setting that must be evaluated each time the agent’s function or existence changes.

*This article was originally published on September 9, 2026, on* [*webflow.com*](https://webflow.com/blog/mcp-security)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/59664e90-cropped-81692684-mohit-headshot-copy-scaled-1-600x600.jpg)

Mohit Bansal is a Senior Security Engineering Leader at Webflow, where he leads programs across security operations. With 12+ years of security engineering experience across startups and larger enterprises, he specializes in scaling security programs and supply chain defenses for...

Read more from Mohit Bansal](https://thenewstack.io/author/mohit-bansal/)

[![](https://cdn.thenewstack.io/media/2026/09/3672437a-topher_chung.png)

Topher Chung is Webflow's Senior Director of Security, a security team leader protecting the platform and its customers. He's spent his career building security programs at Twitter, OneLogin, and Intuit.

Read more from Topher Chung](https://thenewstack.io/author/topher-chung/)