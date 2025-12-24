“Our AI prototypes are brilliant, but getting them to production takes six months — if we’re lucky.” Sound familiar?

Teams today ship prototypes in days, if not hours, but it can take months to reach production to get a return on the investment. This is while watching competitors launch AI-powered features daily or weekly while your teams remain paralyzed by the unknown risk and antiquated processes meant for static-deployment applications.

When it’s not an AI model problem, a talent problem or even a budget problem, then what is the root cause? Enterprises get jammed up in decision and process gridlock at the intersection of velocity and trust. If they move too fast, they fear that they will risk their security and compliance policies, but if they move too slowly, they risk becoming irrelevant.

Organizations that break out of this cycle have stopped forcing new workloads through antiquated processes or onto outdated foundations. Instead, they’re building and adopting systems designed for the complexity of the direction AI is headed today, not the static application constraints of five years ago.

## **When Compound AI Meets Fragmented Infrastructure**

Early AI-powered applications were simple compared to those of today. They commonly used one AI model to complete a specific task running in just one environment. That’s not the case anymore. Most AI workloads today consist of [multiple agents coordinating workflows](https://thenewstack.io/4-reasons-agentic-ai-is-failing/), chaining large language models (LLMs) for complex tasks, and running across distributed systems. Each new layer multiplies complexity. The systems powering modern AI stacks evolve faster than the infrastructure that supports them.

This is where things start to break.

Here’s a real-world example. The brilliant prototype your data science and software development teams built together last week includes over 50 open source packages they have selected. [Each package carries its own dependencies](https://thenewstack.io/the-challenges-of-securing-the-open-source-supply-chain/), with each new dependency having its own potential vulnerabilities and license implications. Most organizations struggle to track which of those packages have vulnerabilities, which are in use, not up to date, or which quietly introduce latency within mission-critical production environments. As AI workloads become more complex, every new AI model, AI agent and integration multiplies security risk faster than governance can keep up.

Even when security risk is managed, the environment itself becomes an obstacle. A prototype that runs flawlessly in a data scientist’s notebook can [fail mysteriously in staging](https://thenewstack.io/ai-code-doesnt-survive-in-production-heres-why/) or behave unpredictably in production. The culprit is usually “environment drift.” This is when a dependent package version is different, a configuration has changed or an orchestration layer behaves differently. Traditional software pipelines were built on stable and visible components; however, those boundaries dissolve when it comes to AI workloads. Teams find themselves debugging not one environment, but many, with little visibility into what’s running, where or why.

And when something goes awry months later, troubleshooting problems compound further. A vulnerability surfaces. AI model output starts behaving unexpectedly. But which version of which AI model or agent was in operation at that moment? What was the AI bill of materials ([AIBOM](https://csrc.nist.gov/presentations/2024/securing-ai-ecosystems-the-critical-role-of-aibom)) at the time of the incident? Which datasets were in use? Without a reliable lineage, teams can’t trace deployments, roll back safely or learn from failures. In the era of compound AI, missing provenance isn’t a minor inconvenience but exposure to security risk.

## **The Not-So-Hidden Cost of Fragmented Toolchains**

The business implications are hard to ignore. [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-03-25-gartner-survey-reveals-84-percent-of-cmos-report-high-levels-of-strategic-dysfunction#:~:text=Marketing%20Leaders%20Challenged%20By%20Unclear,and%20execute%20effective%20marketing%20strategies.%E2%80%9D) reports that 84% of technology executives made unplanned strategic pivots in 2025, many driven by AI projects that ran headlong into these infrastructure limits. Not because the AI models failed, but because the systems around them couldn’t sustain production at enterprise scale.

But AI will continue to scale, with [72% of organizations reporting their teams use AI tools weekly](https://ai.wharton.upenn.edu/wp-content/uploads/2024/11/AI-Report_Full-Report.pdf). This high level of use may pose a security risk, especially when teams are moving fast without a clear view of how AI is being used or applied. In fact, [only 13%](https://www.cyera.com/research-labs/2025-state-of-ai-data-security-report) of enterprises have clear visibility into how AI is actually being used across their organization, and 1 in 80 generative AI (GenAI) prompts expose sensitive data. Additionally, 7.5% of all prompts include sensitive or private details, according to [Check Point Research](https://engage.checkpoint.com/2025-ai-security-report).

Right now, every new AI model, AI agent and AI-powered workflow requires reestablishing trust from scratch. But as leadership demands faster AI results, compliance teams demand tighter controls. Unfortunately, existing toolchains make both virtually impossible. This results in either promising prototypes that never ship or risky workarounds that bypass governance entirely.

## **What Actually Changes the Pattern**

The organizations breaking free from this AI gridlock aren’t patching old processes, but rebuilding their foundations, treating AI as a unified foundation built for compound complexity from Day 1.

These organizations don’t treat governance and security as afterthoughts. Every dependency must be traceable, every AI model vetted and every environment reproducible before they start building. When trust is the first consideration, velocity follows. Security teams have full visibility in project risk, platform engineering teams are ready on Day 1, data science teams operate at scale and development teams deliver results efficiently. In these organizations, all teams don’t have to choose between velocity and trust.

Teams also want to build consistent applications and services that can survive complexity. “Environment drift” isn’t just a nuisance at this scale, but a blocker that forces teams to go rogue to ship quickly or ship at all. With compound AI, “it’s basically identical” equals lack of scale or a potential production outage, and creating consistency becomes the only way for teams to maintain velocity.

Finally, organizations are able to establish visibility across the entire ecosystem and workflow. To increase confidence, teams need to know exactly what’s running, where it’s running and which dependencies make up their AIBOM at any given moment. If or when things break, [knowing precisely when security issues emerged and what’s affected](https://thenewstack.io/llms-broke-the-sre-runbook-now-what/), rather than guessing which of the hundreds of dependencies caused the cascading risk, will help reduce the time spent remediating the incident tremendously.

These unglamorous parts of the application stack, including dependency management, on-demand reproducible environments and automated security and governance, will empower compound AI workloads to scale without collapsing under their own complexity — all while not getting stuck at the intersection between velocity and trust. That’s the difference between organizations that demo AI-powered prototypes and those that build, secure, deploy and monitor AI-native applications and workloads that unlock efficiency and innovation for their teams and customers.

## **The Choice Ahead**

The barrier to AI success isn’t capability, but infrastructure and process maturity. The organizations pulling ahead are led by those choosing to invest in modern foundations where trust and velocity coexist and where built-in security and governance accelerate rather than obstruct. Fragmented toolchains and environments force you to choose between the two, but modern, unified infrastructure and [modern AI processes](https://www.anaconda.com/press/anaconda-launches-comprehensive-enterprise-ai-development-suite) let you have both. Today, removing bottlenecks is creating your competitive edge. This is not just a technical ambition; it’s a business imperative to compete and survive in today’s market.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/09/efc62a63-cropped-b28c697a-david-desanto-headshot.png)

David DeSanto is chief executive officer at Anaconda, where he leads the company’s mission to empower the world’s data science and AI communities through open-source innovation and secure enterprise solutions. A proven product and technology executive, David brings more than...

Read more from David DeSanto](https://thenewstack.io/author/david-desanto/)