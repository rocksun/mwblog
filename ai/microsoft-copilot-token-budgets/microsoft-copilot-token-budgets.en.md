**Microsoft spent the first phase of the AI coding boom** pushing its engineers to use the tools. Now it wants to know whether all those tokens are producing anything worthwhile.

The company has introduced AI token budgets for its divisions to manage coding like any other expensive computing resource. It’s given employees a way to monitor their own spending, and instructed engineers to use OpenAI’s GPT-5.6 Sol as the default model in GitHub Copilot.

“As we accelerate our use of GitHub Copilot to deliver on our goals, we all need to be aware of how we consume tokens,” [Jay Parikh](https://www.linkedin.com/in/jayparikh), an executive vice president at Microsoft, writes in an internal email first [reported by 404 Media](https://www.404media.co/microsoft-tells-engineers-tokenmaxxing-is-not-what-we-are-optimizing-for/).

“Tokenmaxxing is not what we are optimizing for,” Parikh continues in the memo. “I want all of us focused on maximizing outcomes that move the needle for our customers and our business.”

> “Tokenmaxxing is not what we are optimizing for. I want all of us focused on maximizing outcomes that move the needle for our customers and our business.”

Microsoft confirmed the changes to [CNBC](https://www.cnbc.com/2026/08/05/microsoft-makes-openai-gpt-5point6-sol-default-in-github-copilot-for-staff.html). Internal Copilot guidelines say every Microsoft division has had an “AI token budget target” since July. Employees can track their individual spending, while Microsoft’s data shows many engineers consume anywhere from hundreds to several thousand dollars in tokens each month.

The company has not announced the size of those budgets or said that engineers will automatically lose access when they reach them. The guidelines leave room for tighter controls, however, warning that individual divisions may introduce further restrictions as Microsoft monitors spending.

“As such, we are updating our internal guidance and managing token spend with the same discipline we apply to every other critical resource,” Parikh wrote.

## GPT-5.6 Sol is the default now

Microsoft’s decision to make GPT-5.6 Sol the default complicates the idea that this is simply a cost-cutting exercise. It’s still the most expensive model in OpenAI’s GPT-5.6 family even if it does cost less than some of the models Microsoft has previously used. OpenAI charges $5 per million input tokens and $30 per million output tokens for Sol. Following [price cuts announced July 30](https://thenewstack.io/gpt-5-6-api-price-cuts/), Terra costs $2 and $12, respectively, while Luna costs $0.20 and $1.20.

So now it’s not just about which model tops the benchmarks; teams have to figure out [which one is worth it for each job, and what extra capability is actually worth the price](https://thenewstack.io/agentic-ai-token-costs/).

Parikh makes clear the distinction in the email this way: “We are not optimizing for fewer tokens. We are optimizing for more impact per token.”

> “We are not optimizing for fewer tokens. We are optimizing for more impact per token.”

## Defaults are starting to act like guardrails for AI use

GitHub has been moving in a different direction with automatic model selection. Copilot can route requests to models from several families based on the task, the user’s subscription, and policies set by an administrator. GitHub says the feature routes around natural cache boundaries to avoid unnecessary costs, and that its evaluations found better [token efficiency without a decline in quality.](https://github.blog/changelog/2026-07-01-copilot-cli-auto-model-selection-routes-based-on-task/)

According to CNBC, Copilot’s automatic selection had sometimes routed Microsoft employees to [Anthropic models](https://thenewstack.io/opus-5-agentic-coding-cost/). Setting Sol as the default gives Microsoft greater control over where its internal token spending goes, while employees retain access to other models when needed.

The company had already started consolidating its internal coding stack. In May, Microsoft began eliminating most Claude Code licenses in its Experiences and Devices division and instructed engineers to move to GitHub Copilot CLI by June 30, reports [*The Verge*](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad). Claude models remain available through Copilot, but bringing engineers into [Microsoft’s own tool](https://thenewstack.io/microsoft-mistral-sovereign-ai/) gives the company more control over access policies, model selection and usage data.

## Token costs outpace productivity measurement

Microsoft has some evidence that coding agents can increase developer output. A [study](https://arxiv.org/abs/2607.01418?) from Microsoft researchers examined the rollout of Claude Code and GitHub Copilot CLI across tens of thousands of engineers, and those who adopted the tools merged roughly 24% more pull requests than researchers estimated they otherwise would have during the four-month study.

The findings give Microsoft a reason to spend on coding agents, but merged pull requests are only a proxy for output. The study did not determine whether the additional code reduced bugs, improved security, saved developer time, or delivered more value to customers. A team can merge more code without [producing a better product](https://thenewstack.io/meta-metacode-engineer-training/).

## Agents multiply the spending problem

The challenge grows as coding tools move beyond the “autocomplete” phase. For instance, [agents can now explore repositories, build implementation plans, run commands, execute tests, and revise their own work.](https://thenewstack.io/openai-codex-cloud-evolution/) Each step can add more context and output tokens to the bill. An agent that repeatedly reads a large codebase or takes an unsuccessful approach can consume a significant amount of tokes before a developer intervenes.

GitHub moved Copilot to usage-based billing on June 1 and introduced user-level budget controls for organizations. Administrators can set a universal budget or adjust limits for particular employees. GitHub said longer agent runs, multistep tasks, and more capable models were putting pressure on included usage when it announced its new Copilot plans. The company activated usage-based billing and user-level controls on June 1.

> An agent that repeatedly reads a large codebase or pursues an unsuccessful approach can consume a significant amount before a developer intervenes.

## Industry-wide controls are emerging

Microsoft is not the first company to discover that encouraging employees to consume more AI does not guarantee a matching increase in productivity.

Uber [reportedly](https://www.businessinsider.com/uber-cto-praveen-neppalli-tokenmaxxing-era-end-2026-8) exhausted its entire 2026 AI coding budget during the first four months of the year following rapid adoption of tools including Claude Code and Cursor. The company has since focused on cheaper default models, prompt caching and better visibility into employee spending.

Amazon encountered another version of the problem. An internal Claude Sonnet project intended to match author records with product listings reportedly cost $1.8 million, exceeding its planned budget by 860%. The overrun went undetected for months, and the project never shipped.

Two other internal AI projects reportedly exceeded their budgets by a combined $675,000, [according to reporting based on an internal Amazon presentation](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics). Similarly, Adobe, Atlassian and Citi are rolling out their own controls to rein in waste.

The industry seems to be moving past the point when using more AI was enough to claim progress. Companies now have to show that the money they are spending on it is producing something worthwhile.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)