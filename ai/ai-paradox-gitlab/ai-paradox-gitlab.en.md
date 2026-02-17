The software industry reached an inflection point in November and December 2025.

Three breakthrough AI model releases, Gemini 3 by Google, Opus 4.5 by Anthropic, and GPT-5.2 by OpenAI, delivered capabilities that forced industry leaders to reevaluate AI’s role in software development. Gergely Orosz reports in his Pragmatic Engineer newsletter that experienced engineers now trust AI to generate 90% or more of their production code.

But here’s the challenge: innovation speed depends on far more than AI writing code faster. Real acceleration requires optimizing the hundreds of steps in business-critical software development processes such as quality assurance, security validation, compliance verification, and maintainability planning to work seamlessly with AI-generated code.

In a GitLab survey, [organizations report](https://about.gitlab.com/software-innovation-report/) a 48% increase in developer productivity, enabling developers to generate functions, identify errors, and ship new features faster than ever before. However, coding represents only 20% of the software delivery cycle.

According to [Amdahl’s Law](https://bittla.medium.com/mastering-amdahls-law-beginner-to-advanced-with-real-code-examples-e0037dc35d92), speeding up coding by 10x yields only a 1.25x overall speedup when the remaining 80%, including code review, testing, security, and deployment, remains unchanged. Organizations that implement AI exclusively for coding will see their productivity plateau. Their teams will report productivity gains while drowning in review backlogs, flaky tests, compliance requirements, and performance optimization.

> With intelligent orchestration, organizations can retire the sequential model in favor of continuous execution loops.

At GitLab, we call this the “AI Paradox.” Though AI makes coding more efficient, the greatest opportunity to accelerate innovation lies in enhancing quality, security, and speed throughout the entire software lifecycle.

## Intelligent orchestration is essential

Traditional software delivery operates in discrete stages with manual handoffs: plan, code, test, secure, deploy, operate. Each handoff introduces delays, context loss, and coordination overhead. When AI accelerates only one stage, coding, the handoffs become the bottleneck. Each transition between stages destroys the velocity gains from faster coding.

With intelligent orchestration, organizations can retire the sequential model in favor of continuous execution loops. Instead of “code, then test, then secure,” teams continuously generate, test, secure, deploy, and verify work in parallel. AI agents operate autonomously within this continuous flow, while humans orchestrate from above, setting direction and governance without making rote decisions.

This shift eliminates the gaps between stages that slow team velocity. Work no longer waits in queues before the next stage begins. Context persists throughout the loop rather than being lost at each handoff.

## The 3 pillars of intelligent orchestration

Addressing the AI Paradox requires intelligent orchestration built on three foundational pillars:

1. **Workflows: Teams and AI agents collaborating.** Software teams establish the rules for AI agents, including which context to rely on, workflows to streamline, and compliance rules to enforce. Teams move beyond one-to-one AI chat experiences to team-level agentic workflows where multiple agents collaborate on complex tasks, issue-to-merge-request flows, security analysis, code reviews, and CI/CD operations. One agent serves multiple developers. Multiple agents work in parallel across teams. Humans provide guidance and direction rather than managing individual AI outputs in detail.
2. **Context: Unified data and intelligence throughout the lifecycle.** Instead of sequential handoffs that interrupt flow, intelligent orchestration maintains continuous execution across stages through a unified data model. Unlike fragmented tools where context disappears across systems, this provides complete context across the entire lifecycle. Teams gain visibility into not just code, but requirements, history, security implications, deployment constraints, and operational feedback. Teams can therefore work on multiple projects and releases simultaneously without losing context. Every stage runs concurrently. What used to be tickets, waiting, handoffs, and remediation sprints becomes continuous generation, continuous compliance, and continuous improvement.
3. **Guardrails: Governance and compliance integrated into the flow.** Flexible deployment options, combined with custom [rules for security and compliance](https://thenewstack.io/security-is-blocking-ai-adoption-is-byoc-the-answer/), provide full control over your data and workflows. Agents evaluate risk and recommend appropriate levels of autonomy for each task, with policy-driven guardrails that ensure higher-risk changes receive more human oversight, all within a single orchestrated system. This allows [teams to maintain velocity](https://thenewstack.io/how-ai-can-help-it-teams-find-the-signals-in-alert-noise/) without sacrificing security or compliance, integrates with workflows, and enables automatic enforcement.

## Human-AI collaboration

The solution doesn’t involve more tools or faster AI. The answer lies in rethinking how humans and AI collaborate and fundamentally redesigning the software delivery process itself. GitLab’s research shows that 76% of DevSecOps professionals believe AI will create more engineers, not fewer. What’s changing is the nature of the work itself.

> These are stories about intelligent orchestration enabling teams to maintain velocity at enterprise scale.

When AI writes most of the code, the skills that become critical are those that teams previously expected of senior or staff-level engineers: delegating work, making sound architectural decisions, taking a customer-minded approach, implementing automated testing and observability, and tracking tech debt. As Gergely Orosz observes, “Tech lead traits will almost certainly be more in demand. When AI can implement any well-defined ticket, who will write the ticket that makes AI correctly create the code?”

In practice, AI agents manage repetitive tasks autonomously across multiple stages, such as generating code, running tests, scanning for vulnerabilities, and deploying changes. Humans establish direction, maintain governance, and make judgment calls. This shift moves developers from writing every line of code to orchestrating systems and guiding AI agents. The valuable human skills, such as creativity, strategic vision, judgment, and architectural thinking, become more critical, not less.

> This shift moves developers from writing every line of code to orchestrating systems and guiding AI agents.

At Ericsson, a leading telecommunications company, managing enterprise software deployments across more than 300 global communications service providers requires seamless orchestration across multiple tools, systems, and workflows. After implementing a unified platform approach, Ericsson achieved 50% faster deployments and saved 130,000 hours over six months, allowing the company to deliver updates in weeks rather than months.

This pattern occurs across industries. Indeed achieved a 79% increase in daily software development pipelines while reducing its hardware costs by up to 20%. At CERN, 10,000 scientists from over 100 countries collaborate on particle physics research, achieving 90x faster job startups. Lockheed Martin eliminated thousands of Jenkins servers and accelerated software delivery, moving from monthly to weekly deployments, with security and compliance built into workflows.

These examples don’t represent stories about AI coding tools that make individual developers faster. These are stories about intelligent orchestration enabling teams to maintain velocity at enterprise scale.

## The future belongs to orchestrated teams

AI coding represents just the beginning of software transformation. Intelligent orchestration amplifies that acceleration across entire teams and complete development ecosystems.

Forward-thinking enterprise leaders evaluating their software delivery approach should ask: Do current tools enable teams to accelerate innovation or create new bottlenecks? The answer determines competitive advantage. When software teams and AI agents work together effectively, the focus shifts from coordination and logistics to vision.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/a70a806f-cropped-262476b0-screenshot-2026-02-11-at-09.11.22.png)

Manav Khurana is the Chief Product and Marketing Officer at GitLab, where he leads GitLab's product, design, and marketing functions. Manav is passionate about building tools that enable engineers to do their best work and build great software. Manav's career...

Read more from Manav Khurana](https://thenewstack.io/author/manav-khurana/)