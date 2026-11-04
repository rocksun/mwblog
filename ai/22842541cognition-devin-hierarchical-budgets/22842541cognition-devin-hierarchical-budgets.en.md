**The days of pointing an AI agent at a backlog and letting it burn through compute** without much oversight may be coming to an end. Cognition is introducing hierarchical budgets for Devin so enterprises can manage AI coding agent spending across departments, projects, and individual engineers. Administrators can assign budgets to different teams, track how much each one spends, and approve more capacity based on engineering efficiency. There’s a catch for developers, though; if a budget runs out while Devin is working on a task, the session stops.

> If a budget runs out while Devin is working on a task, the session stops.

The feature grew out of conversations with customers, according to [Lukas Burger,](https://www.linkedin.com/in/lukas-burger/) who works across go-to-market and engineering at Cognition. “Most of what we build starts with our forward deployed engineers (FDEs), who work on-site with customers. Budgets came straight out of those conversations,” Burger tells *The New Stack*. Once Devin moved past pilots and into broader deployments across organizations, he explains, the blunt controls that had worked for a single team — org limits, per-user tiers, and separate Devin Desktop settings — stopped holding up.

## From Pilots to the P&L

The problem Budgets sets out to solve is one of scale and sprawl rather than raw price. “That’s fine for one team. It doesn’t hold up when a bank is dividing a large ACU commitment across hundreds of groups,” Burger tells *The New Stack* of the older spending controls. Some of those customers had started building and maintaining their own internal tools just to parcel out capacity to the leaders of each business line, a workaround that mapped the exact gap Cognition set out to close.

Cognition built the feature with some of the world’s largest enterprises as design partners, testing the model with customers managing millions of [Agent Compute Units](https://docs.devin.ai), the consumption-based units used to measure the work Devin performs.

Burger is keeping quiet on individual customer spending figures, but he is clear about what changes as deployments widen. “Devin stops belonging to one team,” he says. “A pilot might sit with a single platform group. A broad rollout means many departments, each with its own priorities and its own budget owner.”

## Budgets follow the org chart

Budgets is designed to work with the way enterprises already manage spending, meaning, an administrator starts with one overall budget, divides it among business units, and from there, those leaders can distribute funds to their own teams and projects, with budgets extending up to three levels deep. Central IT can still see where the money is going and set limits without approving every request. “The enterprise keeps guardrails and visibility across all of it,” Burger says.

Companies can also set aside budgets for specific projects rather than tying all spending to individual teams. A major legacy modernization effort, for example, could have its own budget even if engineers from several departments are working on it. Separate controls apply to Devin running in the cloud and on engineers’ desktops, so companies can track and limit spending in both environments.

## When a budget runs out

The promise is that none of this should intrude on the work. “We designed Budgets so engineers can do their work without thinking about them,” Burger says, and the mechanics warn engineers before spending limits interrupt their sessions.

Engineers see alerts on their homepage when they are on track to exceed a limit, and they can request more ACUs from the budget owner without leaving the product. Each budget’s administrators decide whether to review those requests manually or clear them automatically.

## Grading engineers on efficiency

That automation is where the feature turns pointed. Admins can enable [efficiency-based approvals](https://devin.ai/blog/efficiency-based-cost-controls), which automatically lift an engineer’s limit when their Efficiency Score is strong, up to a ceiling the admin sets. Cognition introduced the scoring system in October to estimate productive engineering hours relative to Devin consumption, which permits administrators to allocate more capacity to engineers who appear to get more useful work from their usage. The score estimates efficiency, however, and does not directly measure code quality or business outcomes.

When a budget does empty, the session stops, which is why Burger frames the alerts and in-product requests as the first line of defense rather than the last.

> “We’re also working on letting teams switch to lower-cost models after a soft limit, so important work can finish,”

“We’re also working on letting teams switch to lower-cost models after a soft limit, so important work can finish,” Burger tells *The New Stack*. That option is still in development, so for now, budget increases and advance warnings are the most effective ways to avoid interruptions to date.

Cognition is just as wary of the opposite failure, the controls drawn so tight they strangle the productivity they were meant to protect. “We also don’t want controls so tight that customers stop being productive with Devin,” Burger tells *The New Stack*, which is why the company suggests defaults with enough headroom to keep productive users from being blocked unnecessarily.

Much of the surprise in agent spending, he notes, “comes from not knowing where usage lands,” a gap that cheaper tokens alone may not close when agents run complex, multi-step tasks and [a round of price cuts doesn’t necessarily translate into a smaller bill](https://thenewstack.io/minimax-flash-agent-costs/).

## Proof in the Pull Requests

[Consumption pricing](https://thenewstack.io/openai-token-pricing-reversal/) cuts both ways, and Cognition knows it. “With consumption pricing, customers who can’t see value stop using the product, so we’ve put a lot of work into cost control and measurement,” Burger tells *The New Stack.*

> “With consumption pricing, customers who can’t see value stop using the product, so we’ve put a lot of work into cost control and measurement,”

Each Devin session is tied to a specific budget, so companies can see exactly how much individual teams, projects or business units are spending. Instead of looking at one company-wide total, leaders can track the cost of a particular initiative. Some customers also link that spending to internal billing codes or charge it back to individual departments.

Measuring consumption is the easy half of the equation. For the harder question of whether the money is well spent, Burger says most customers fall back on the metrics they already trust, tracking merged pull requests, productive engineering hours, and DORA metrics.

Burger says the teams getting the most out of Devin look at business results, citing “how much faster the roadmap moves, how much unplanned work goes away, and how much less they spend on engineering toil.”

## FinOps for AI agents

Burger doesn’t hesitate when asked whether agent budgeting is becoming a discipline of its own, much like FinOps did for cloud infrastructure. “Yes, and it’s already starting,” he tells *The New Stack*. Because agents are billed by consumption, finance teams are asking familiar questions about who is spending, where the money is going and whether it’s worth it. Burger says the shift is happening faster than it did with cloud computing because companies already have processes in place to manage those costs.

The FinOps Foundation’s 2026 [“State of FinOps”](https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1) report quantifies how far that has spread, finding that 98% of its 1,192 survey respondents now manage AI spending, up from 31% two years ago. Companies are still working out how to connect that spending with measurable returns. What makes Cognition’s approach different is that companies can manage budgets, assign spending limits and track costs directly in Devin instead of relying on separate tools.

Burger expects the responsibility to land squarely on finance teams. “I see this becoming a major new responsibility for strategic finance and FP&A teams,” he tells *The New Stack*. “On top of their day jobs, they’re now managing massive AI budgets and making sure that spend shows up as real impact on the P&L.”

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=cognition-devin-hierarchical-budgets)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)