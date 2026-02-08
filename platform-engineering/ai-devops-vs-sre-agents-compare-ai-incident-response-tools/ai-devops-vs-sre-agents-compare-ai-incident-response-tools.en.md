If you’ve seen a new crop of data about ops lately, you may have noticed this new category coming up: AI agents that promise to take charge of incident intervention, diagnose the root cause, and even solve problems themselves. [AWS](https://aws.amazon.com/?utm_content=inline+mention) announced one. [Microsoft](https://aka.ms/modelmondays?utm_content=inline+mention) has one. A dozen startups are [creating them](https://thenewstack.io/as-ai-reshapes-tech-microsoft-others-refocus-dev-structure/).

And the terminology is, to put it mildly, an inconsistent affair: AI DevOps engineer, AI site reliability engineering (SRE) agent, AIOps platform. Are these the same thing? Different things? Marketing fluff? I’ve spent time digging into [what these systems actually do](https://thenewstack.io/how-autonomous-agents-are-changing-infrastructure-management/), how they differ, and what matters when you’re evaluating them. Here’s what I’ve learned.

## ****Why this category exists now****

Let us start with this: Ops teams are drowning. The complexity of microservices architectures has skyrocketed. For example, one user’s request could touch 15 services in three clouds. When it is 2 a.m. and something breaks, you are looking at dashboards from six different tools and matching logs, metrics, and traces trying to connect them all while the Slack explosion is giving “Is the site down?” messages.

Traditional monitoring lets you see what is really happening. It doesn’t tell you why or how to act. That gap — between sight and action — is where AI operations agents dwell. The pitch is clear: Rather than spending 45 minutes figuring out why things went wrong, an AI agent builds the connection in minutes, uncovers the root cause of what possibly went wrong, and proposes a fix. Some take it a step beyond and implement the fix with your consent.

## **What**these agents actually do****

Strip away the marketing, and AI DevOps engineers share a playbook. They connect to your observability stack — Datadog, Splunk, CloudWatch, and whatever you’re running — and consume telemetry. They integrate with your CI/CD pipelines and source control software, so they know which code has been shipped just now. They hook into ticketing systems like [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) or ServiceNow to see event history. If something goes wrong, they correlate signals in these systems.

So they create a timeline: This deployment happened, latency started to rise, errors started to occur, then this downstream service began to fail. They plot your infrastructure topologies to interpret service dependencies and understand failures down the call chain. The better ones learn from mistakes in the past. They identify patterns: “The error signature we saw last time, the root cause was a misconfigured environment variable.” They bring that context to the surface so you can fix issues sooner.

Some agents remain advisory — they investigate and recommend action items, but a human pulls the trigger. Others push toward automation, executing remediation workflows with appropriate guardrails.

## AI DevOps engineer vs. AI SRE agent

The main distinction is marketing and the scope of work. SRE is all about reliability, availability, and error budgets. DevOps looks at the broader delivery life cycle. In reality, most AI operations agents cover both. They manage incidents — SRE territory — and improve pipelines or build Infrastructure as Code (IaC) — DevOps territory. The underlying tech is the same: machine learning (ML) models trained on operational data, natural language, and the interfaces and integration frameworks that plug into your toolchain. Don’t worry about what the vendor calls its product. Evaluate what it actually does.

## How cloud providers are responding to AI ops

AWS DevOps Agent, which [launched in preview](https://thenewstack.io/aws-frontier-agents-handle-code-security-ops-without-you/) late last year, is worth understanding because it illustrates how cloud providers think about this problem.

AWS built an agent that correlates data across CloudWatch, third-party monitoring tools, and CI/CD systems. It maps your infrastructure topology, tracks deployments, and generates recommendations when incidents occur. It integrates with ticketing systems to respond automatically when alerts fire.

The agent is genuinely useful for investigation. It understands AWS resources deeply — EC2 instances, Lambda functions, EKS clusters, the whole catalog — and can trace relationships between them.

There is a difference: AWS thinks in terms of resources, not applications. It knows you have a Kubernetes cluster with certain pods. It doesn’t inherently know that those pods constitute your checkout service, which is distinct from your inventory service, which has different owners and different risk tolerances.

This resource-centric view shapes what the agent can safely do. Without guaranteed application boundaries, automated remediation carries risk. What if scaling one service cascades into another? What if a rollback affects components you didn’t intend to touch?

That’s why AWS DevOps Agent emphasizes investigation and recommendation over automated action. It’s a deliberate design choice, not a limitation. Microsoft’s Azure SRE Agent takes a similar approach.

## The true differentiator: Application context

Context. Here’s what I’ve come to think matters most: the degree of abstraction with which an agent operates. Those acting at the infrastructure level know what resources they own and the relationships among them. They’re good at responding to “What’s happening,” but very careful of “What should we do about it?”

Some platforms also offer explicit application boundaries as a first-class concept. If an agent knows these containers, this database, and these queues, each forming one application with defined ownership, acting on them will be easier; it can more readily scope actions. Rollbacks remain within safe limits. Scale decisions don’t bleed beyond unrelated services. This accounts for the range from advisory to automated. Automation is dangerous without a context (the other way around). It creates clear boundaries and allows agents to think on their feet.

## What engineers should consider when evaluating agents

If you’re evaluating AI operations agents, here’s what I’d think about:

* **Start with investigation, not automation.** Let the agent prove it understands your environment before you give it permissions to change anything. Build trust incrementally.
* **Context quality matters enormously.** These agents are only as good as the data and structure they have access to. Well-tagged resources, clear service ownership, and explicit application boundaries make agents dramatically more effective.
* **Integration depth varies wildly.** Some agents have deep, bidirectional integrations with popular tools. Others have shallow connections that limit what they can see and do. Ask hard questions about how an agent works with your specific stack.
* **This doesn’t replace expertise.** AI agents amplify engineering capability. They don’t substitute for understanding your systems, making judgment calls, or designing for reliability. Treat them as force multipliers, not replacements.

## **Where this is headed**

The category is maturing fast. There is competition from cloud providers, observability vendors, and focused startups: The result is rapid innovation and falling prices. Yes, the opportunity for engineering teams is real. A good agent reduces the average time to resolution to fix a problem, reduces the on-call load, and allows engineers to focus on building resilient systems rather than fighting fires.

But the hype is also real. Assess agents not based on their slide decks, but on how they actually behave in context, in your environment. The teams that experiment with it thoughtfully now will be most well-placed as these tools become the standard part of the operations stack.

At DuploCloud, we’re actively building AI agents designed to execute real DevOps and cloud operations workflows. In [our sandbox](https://duplocloud.com/), you can interact with purpose-built agents that operate across cloud infrastructure, Kubernetes management, and observability — running inside real environments to diagnose issues, apply changes, and automate day-to-day operations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/311ffaca-cropped-be78f843-fahmid-kabir.jpeg)

Fahmid Kabir leads product and go to market at DuploCloud, an AI-powered DevOps platform. He has worked with deep AI technologies, cloud infrastructure and compliance for the past 18 years.

Read more from Fahmid Kabir](https://thenewstack.io/author/fahmid-kabir/)