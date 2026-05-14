Most organizations are approaching AI adoption the same way they once bought enterprise software: pick a vendor, standardize on a model, and push it across the organization.

The assumption is that one model will solve every problem. But a model that excels at code generation might struggle with security analysis, while a frontier model that’s perfect for prototyping may not meet your data residency requirements.

> “A model that excels at code generation might struggle with security analysis, while a frontier model that’s perfect for prototyping may not meet your data residency requirements.”

Resolving this mismatch requires flexibility in how you deploy AI models. Some teams need large-scale models for advanced reasoning, while others need specialized models for domain-specific work. And, critically, you need the ability to mix and match based on the task at hand.

## The AI paradox: Optimize the entire software development process

AI adoption today focuses almost entirely on accelerating code generation. But coding represents a fraction of what developers actually do. According to [GitLab’s 2025 Global DevSecOps Survey](https://about.gitlab.com/developer-survey/), developers spend only about 15% of their time writing code. The rest goes to planning, reviewing code, testing, debugging, managing dependencies, coordinating with teammates, and navigating compliance requirements.

This creates an AI paradox, where AI is accelerating coding, but disconnected toolchains and manual coordination slow overall productivity enough to cost nearly a full workday per developer each week.

To break out of that paradox, AI needs to work across the entire development lifecycle, not just code generation. Different activities across the software lifecycle carry fundamentally different performance requirements:

* **Speed-critical tasks** like auto-completing code or suggesting fixes during active development need sub-second response times, which might favor smaller, locally hosted models.
* **Quality-critical tasks** like architectural planning or security analysis justify the cost of frontier models with superior reasoning.
* **Cost-sensitive tasks** at high volume, such as running tests or updating dependencies across hundreds of repositories, require cost-effective options.

This is why multi-model customization is important. Not all tasks across the software lifecycle carry the same value. Standardizing on a single model can lead to overpaying for some functions or underserving others.

The organizations that get this right build systems flexible enough to route each task to the model that best fits its performance, quality, and cost profile.

## Prioritize your premium model usage

The practical move is matching model cost to task value.

For high-volume, routine work such as writing commit messages, summarizing log files, or writing test cases, teams lean toward cheaper, faster options, including open-source models where feasible. For tasks that demand complex reasoning, teams pay for greater capability. For specialized models that are more deterministic, teams might be willing to pay a premium for infrastructure-as-code generation or high-accuracy data transformation.

Being able to choose between different models based on the task provides a hedge against performance differences, pricing swings, and the reality that providers may sunset products or exit the market entirely.

That flexibility comes from three sources, each with tradeoffs.

* Commercial frontier models from Anthropic, OpenAI, and Google deliver strong performance and improve continuously, but create dependence on vendor roadmaps and pricing.
* Self-hosted commercial or [open-source models](https://thenewstack.io/meta-open-source-models/) give you control over data residency, costs, and availability, but require infrastructure management and, in the case of open source, still can’t handle agentic workflows.

Domain-specific models you’ve trained can outperform general models on narrow, high-stakes tasks where you have unique data and clear success criteria. Still, they require specialist expertise and can be operationally expensive.

Each approach involves trade-offs. The key is building systems that let you use all three strategically.

## Treat AI spend like cloud spend

Model flexibility only creates value if you can manage the economics behind it. The price gap between models is substantial. Complex reasoning models can cost 500% more per request than general-purpose models that handle routine tasks well.

> “Complex reasoning models can cost 500% more per request than general-purpose models that handle routine tasks well.”

Model routing, the ability to define which models get used for which tasks, becomes critical here. A code review might route to a frontier model, while commit message generation uses a faster, cheaper option.

But routing alone isn’t enough. Enterprises need the same financial controls they apply to cloud infrastructure, including quotas to prevent runaway spending, limits to enforce budget discipline, and chargeback models that allocate costs to the departments consuming AI resources. Without these guardrails, AI adoption becomes difficult to justify at scale.

This is why [FinOps practices](https://about.gitlab.com/the-source/platform/finops-balancing-financial-responsibility-and-innovation/) are extending to AI. [IDC estimates](https://www.cio.com/article/4107377/cios-will-underestimate-ai-infrastructure-costs-by-30.html) that organizations will underestimate their AI infrastructure costs by 30% through 2027, and that combining GenAI with FinOps processes will be essential for managing this complexity. Organizations that treat AI spend like [cloud spend](https://thenewstack.io/devfinops-and-ai-to-provision-exactly-the-right-cloud-spend/), with visibility, accountability, and governance, position themselves to scale AI successfully.

## Customization is crucial for ROI

Model flexibility also depends on context. AI needs information spread across systems that weren’t designed to work together by default. A [developer debugging an issue](https://thenewstack.io/sentrys-seer-agent-debug/) might need to reference the work backlog, pull recent Slack discussions, and review app performance metrics in Grafana. If every system has its own AI experience and none of them connect cleanly, AI creates friction instead of removing it.

Fortunately, recent open-source developments, such as [Model Context Protocol (MCP)](https://about.gitlab.com/topics/ai/model-context-protocol/), address this by enabling tools to share relevant context and actions within a single workspace.

This shared foundation enables meaningful customization, and the most effective customization works in layers, each one encoding how your organization performs work.

Most developers rely on pre-built agents and workflows that make AI available for common tasks without requiring expertise. Power users shape how a model operates through detailed prompting, essentially teaching it to follow their organization’s playbook. Experts connect multiple agents into governed flows that mirror how humans deliver work, with strict review protocols in place.

Organizations see the strongest ROI when they design systems in which AI operates within defined contexts and accountability structures, and in which teams can connect different models based on their requirements, whether those are frontier commercial models, self-hosted instances for data residency, or specialized models trained for domain-specific work.

## Implement orchestration, not standardization

Enterprise AI succeeds when it produces outputs that hold up inside real systems, under real constraints.

Leading organizations build for model diversity while maintaining strict governance. They treat AI spend like cloud spend, with model routing, quotas, and chargeback. They invest in orchestration, so AI fits naturally into daily workflows and relevant context flows across tools.

A rigorous selection process matters. The best platforms use subagents that evaluate models across quality, performance, and cost for each type of operation and make those evaluations visible to users so teams understand why a given model handles a given task. That transparency builds trust. When teams have requirements that differ from the defaults, they should be able to override model selections or bring their own models entirely.

This gives organizations the ability to use frontier models where performance matters, self-hosted models where data residency is required, and specialized models where domain expertise makes the difference, all governed by a control plane that maintains consistent standards for reliability and security, regardless of the model’s source.

Enterprise AI isn’t a search for one perfect model. It’s the work of building systems that connect the right models to the right tasks, with the governance to back it up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/69f0c09c-cropped-298ecebd-bryanross-600x600.jpeg)

Bryan Ross is a field CTO for GitLab. An accomplished leader, seasoned technologist and public speaker with over 15 years of industry experience as a senior IT leader, he now helps customers realize business value from IT faster. Equally comfortable...

Read more from Bryan Ross](https://thenewstack.io/author/bryan-ross/)