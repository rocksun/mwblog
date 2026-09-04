Skills, agent configurations, prompt instructions, and rules files. These artifacts now determine what your coding agents produce. They shape every line of generated code, every architectural decision, every convention the agent follows or ignores. They are, functionally, software.

Nobody treats them that way. Teams write a skill, commit it to a repo, and never test whether it still works after a model update. Agent configurations are copied and pasted across teams without versioning. Rules files drift out of sync with the codebase they describe. When something breaks, the signal is a developer noticing weird output and complaining on Slack.

> “If context is the new code, what is its software development lifecycle?”

Patrick coined a framework for what’s missing: [the Context Development Lifecycle](https://tessl.io/blog/context-development-lifecycle-better-context-for-ai-coding-agents). The CDLC is not about context window management or fitting more tokens into a prompt. It’s about managing the quality of the pieces that go into the context window. Is a skill up to date? Does the model actually react to it correctly? Are you providing context the model already knows? If context is the new code, what is its software development lifecycle?

## The four phases of the context development lifecycle

The CDLC has four phases that map directly onto what we already do with code.

**Generate** is where everyone starts. Writing skills, building prompt configurations, setting up agent rules. It’s the equivalent of writing code, and it’s where most of the time goes today.

**Evaluate** is testing. Checking whether the linting on the front matter is correct or whether the syntax is too long. At the sophisticated end, you run scenarios: load a skill, ask a specific question, check whether the agent produces the expected result. You test across models and versions. You check whether you’re writing in context the model already knows, which wastes tokens. You verify that the skill activates on the right trigger words.

This is a TDD loop for context. Write the skill, write the scenario, check the output, iterate.

**Distribute** is shipping. At the simplest level, it’s committing a skill to a repo. At the mature end, teams publish skills to an installable registry with versioning, discoverability, and access controls. Pasting a skill into a Slack channel is not distribution, the same way emailing a .jar file is not dependency management.

**Observe** is production monitoring. Is the skill being used? Is it producing the right results? How many turns does the agent take before a developer intervenes? Where are developers overriding the agent or correcting its output? It’s observability for your context.

## Don’t skip the testing

The maturity curve here is identical to what happened with software development practices over the past two decades. Organizations generate and distribute first. They skip evaluation entirely. They ship skills to production, meaning to the developers using them, and wait to see what happens.

It’s directly comparable to teams skipping test-driven development, despite being told to do it.  
They don’t know the pain, so they go immediately to production.

The pain arrives when a skill works on one model version but breaks on the next, or when it triggers on the wrong question and [gives a developer confidently wrong](https://thenewstack.io/rag-retrieval-scaling-architecture/) instructions. When a convention that the skill enforced was correct six months ago, but the codebase has since moved on, these are the same failure modes we see in untested code. Regressions, false positives, stale assumptions.

> “You cannot scale code quality by asking humans to review more carefully. You scale it by investing in the guardrails that codify your standards at both ends.”

Every codebase has patterns that AI consistently gets wrong. Convention blindness, hallucinated APIs, cargo-cult code, over-engineering. At Aviator, these are called [Invariants](https://docs.aviator.co/verify/concepts/invariants), or the [AI slop register](https://www.aviator.co/blog/how-an-anti-slop-registry-stops-ai-generated-code-from-violating-your-engineering-standards/). Both the skill register and the AI slop register exemplify the same underlying principle at both ends of the development lifecycle: catalog your engineering standards and feed them to agents.

Before code generation, that means skills. At [code review](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness), it’s a catalog of patterns AI consistently gets wrong in your codebase. The slop register informs automated checks that catch what slipped through. You cannot scale code quality by asking humans to review more carefully. You scale it by investing in the guardrails that codify your standards at both ends.

## From 1x to 50x

A developer who optimizes their own [agent loop](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/) gets better individual results, but the improvement stays with them. When they fix a skill, nobody else benefits. When they discover a failure mode, nobody else learns from it. The ROI is 1x.

Patrick frames the scaling question using two metrics that sit atop traditional DORA measures.

The first is **human touch**: how often does a developer need to intervene in a given agent workflow? Every intervention is a signal that context is missing or wrong. Reducing human touchpoints is a direct measure of how autonomous your agentic coding loop actually is, and it’s often correlated with cost, since more turns mean more agent spend.

> “Reducing human touchpoints is a direct measure of how autonomous your agentic coding loop actually is.”

The second is the **reuse multiplier**: how many developers benefit when you improve a single skill? If one developer fixes a skill and only they benefit from it, that’s 1x. If that fix goes into a shared registry and 50 developers get it, that’s 50x.

These two metrics together force an organization toward shared infrastructure. You can’t reduce human touches at scale without shared, well-tested context. You can’t get a reuse multiplier without distribution and versioning.

## Your platform team already knows how

The organizational structure for this already exists. [Platform teams](https://www.aviator.co/blog/every-software-company-will-become-a-dev-tools-company/) have spent a decade building the infrastructure that enables development teams to ship code reliably: version control, CI/CD pipelines, artifact registries, security scanning, dependency management, and access controls. The playbook transfers almost directly.

What a platform team does for code repositories, it does for skills. Provide a registry. Configure access control and group permissions. Set up the evaluation infrastructure. Run security scanning and report findings. Build the dashboards that show which skills are performing well and which are degrading. Track ownership so that when a skill breaks after a model update, there’s someone responsible for fixing it.

What the platform team does not do is write the skills or fix them when they break. The team that owns the domain owns the skill. The platform team provides the governance layer and the tooling, the same division of responsibility that works for code.

> “Don’t build the tool. Build the tool that builds the tool.”

The orphaned-skills problem is already emerging. A developer writes a skill, shares it, moves to another team, and now nobody maintains it. A model update breaks it, and the platform team inherits the problem by default. This is orphaned GitHub repos all over again. The solution is the same: ownership policies, maintenance requirements, deprecation paths.

Patrick draws the layers concisely: “Don’t build the tool. Build the tool that builds the tool. The [platform team builds](https://thenewstack.io/internal-platforms-are-products/) the tool for people building the tool that builds the tool.

## Closing the loop with observability

The least developed phase in most organizations is observation, though it’s the most important. Without it, there’s no learning system. You’re generating and distributing context manually, hoping it works, and fixing things when somebody files a complaint.

Agent observability is still early. Standards are forming. Agent MD is broadly adopted. Skill and plugin standards are newer. The tooling isn’t mature, but the pattern is clear: instrument your agents, centralize the signals, and analyze them across teams.

We’ve argued before that production feedback loops are the missing piece in AI-assisted development. When something breaks in production, trace it back to the change, identify the error category, and feed it back into both the prompting and verification layers. The CDLC observability phase extends that idea from code quality into context quality. The signals collected from agent logs, developer corrections, and turn counts feed directly back into generating better skills, writing more targeted evals, and distributing improved versions.

## Self-improving agentic development

The fully closed loop looks like a system where agent logs feed into analysis that identifies gaps. Those gaps generate new skills or updates to existing ones. The updated skills run through evaluations before they ship. They distribute through a registry with version control. And the cycle repeats.

Patrick is realistic about the end state. The “dark factory” vision, where agents produce code with zero human involvement, is what he calls “a noble direction, but a risky game.” The teams that get closest — the ones that can confidently say that they [don’t read the code anymore](https://thenewstack.io/future-of-code-reviews/) — are the ones that invested heavily in the context, testing, and observability infrastructure that makes their agents reliable enough to need fewer human touches per cycle.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, a developer productivity platform used by modern engineering teams to ship AI-generated code at scale. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)

[![](https://cdn.thenewstack.io/media/2026/08/d5203274-patrick-debois.webp)

Patrick is a true pioneer, credited with coining the term DevOps, co-authoring the DevOps Handbook, and launching the very first DevOpsDays back in 2009. Since then, he’s been shaping the tech industry with his unmatched ability to bring development, operations,...

Read more from Patrick Dubois](https://thenewstack.io/author/patrick-dubois/)