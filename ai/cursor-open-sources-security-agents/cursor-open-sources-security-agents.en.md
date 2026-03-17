[Cursor](https://cursor.com/)‘s security team has built a fleet of AI agents that continuously monitor and secure the company’s codebase, and it is releasing the templates and Terraform behind them so other security teams can do the same.

[Travis McPeak](https://www.linkedin.com/in/travismcpeak/), Cursor’s Head of Security, tells *The New Stack* that this project grew out of a familiar frustration. Traditional security tooling, such as code owners, linters, and static analysis, wasn’t keeping pace with the rate of change at a company where engineers ship code as fast as AI coding tools evolve.

“We’ve always had this struggle in security, where there’s more demand for our attention than we can scale ourselves,” McPeak says. “So the idea was: How can we leverage agents in a more focused way for security and show up in those places at the right time?”

> “So the idea was: How can we leverage agents in a more focused way for security and show up in those places at the right time?”

Focusing on code owners’ features, for example, was too imprecise at Cursor’s scale, and often pulled security teams into irrelevant Pull Requests while missing changes that actually mattered. Linting generated too many false positives. The core idea behind Cursor’s new approach: Agents can now reason semantically about what a code change actually does, rather than triggering on more traditional keywords or pattern rules.

The agents run on [Cursor Automations](https://cursor.com/blog/automations), the company’s recently launched platform for always-on coding agents. Automations sits on top of Cursor’s cloud agent platform and provides those agents with integrations for receiving webhooks, responding to GitHub pull requests, and monitoring codebase changes. These agents run continuously in the background and step forward when triggered by a PR, a webhook event, or a cron schedule.

McPeak’s security team gained early access to an internal version of Automations late last year and became among its first heavy users, he tells us. To make those agents work for the team’s security workflows, they built a custom MCP tool and deployed it as a serverless Lambda function.

## Four security agents

The team released the blueprint for four of its security agents on Monday: Agentic Security Review, Vuln Hunter, Anybump, and Invariant Sentinel.

The first and likely most visible of these new agents is Agentic Security Review, which now runs on virtually every pull request and can block continuous integration if necessary. It started as a fork of Cursor’s existing [Bugbot](https://cursor.com/bugbot), the company’s general-purpose code review agent. But McPeak and his team then tuned it specifically for the security team’s needs.

He wanted something high-signal enough to actually block merges, he says. “When this thing says this is a problem, we have the confidence in it that we can block.” In just two months, it has run on thousands of PRs and blocked hundreds of issues from reaching production, he says.

The second, Vuln Hunter, scans the existing codebase daily. The idea here is that if Agentic Security Review had existed when the older code was written, it would have caught issues that are now running undetected in production. Vuln Hunter divides the code into logical segments and instructs agents to trace vulnerabilities through to their root causes. As McPeak notes, the agent can’t report a finding to the security team unless it can prove it’s real.

Anybump handles dependency patching. As McPeak noted, too often security tools look for issues in third-party libraries for components that aren’t actually in use.”Before any of the stuff that we’re doing here, we have a reachability analysis service, and it finds out if we are actually using the component in a way where the vulnerability matters to us or not?”

The agent then traces through code paths, runs tests, and opens a PR if tests pass. McPeak says the agents produce more thorough analysis than humans would typically be willing to do — and they do it without interrupting anyone’s workflow.

The fourth agent, Invariant Sentinel, monitors for drift against a set of security and compliance properties the team has defined: privacy guarantees, legal requirements, and high-impact controls. It runs daily and uses Automations’ memory feature to track state across runs.

## What the agents found

Among many other issues, Vuln Hunter, for example, flagged an email-sending service lacking proper input validation that could have been used as a spam relay. It found a forgotten just-in-time service with overly broad access permissions that the infrastructure team had lost track of — “everybody here had forgotten about it,” McPeak says. And it caught a server-side request forgery vulnerability that required tracing requests across multiple services, the kind of logic-based issue that static analysis tools struggle with because it depends on full cross-service context rather than a single code path.

McPeak says his engineering team’s response has been unusually positive. “I started showing it to engineers, and they said, ‘Wow, this is a great catch. When can we have this on everything?'” he says. “Which is very unusual for security products — that engineers [are like], ‘I like this. I want to have it.’”

## Why release the templates?

McPeak notes that part of why the company is releasing these templates now is in response to the attackers’ actions. Those attackers, after all, are also using AI to find vulnerabilities.

“If we don’t scale ourselves, things are going to get worse for security as a whole,” McPeak says.

Because the automations are prompt-based agents with customizable tools, other teams should be able to adapt them to their own threat models.

“If I gave you a binary, it does security stuff exactly the way I want it done at Cursor, then you can’t customize it,” McPeak says.

## What does this mean for security startups?

One interesting aspect of all of this is what it means for security startups that focus on code reviews and dependency scanning. Pundits have lately spent a lot of time discussing the [SaaSpocalypse](https://thenewstack.io/dawn-of-a-saaspocalypse/), after all.

McPeak is pretty open about the dynamic. “My observation now is, if you just drop [an LLM] in and give it the right tools, it’ll do a lot of good stuff.” Startups whose value proposition was purely coaching models to behave in the right way may find that there isn’t a lot of long-term value in that, McPeak notes, but he does believe there’s still room for companies that package the end-to-end workflow. Prompt engineering, however, is not much of a moat.

Over time, McPeak says Cursor plans to expand the approach to include vulnerability report intake, privacy compliance monitoring, on-call alert triage, and access provisioning. The Agentic Security Review has already evolved from a single agent into an orchestrator that calls specialized sub-agents, including a dedicated privacy check, with more domains planned. The company that makes the tool developers use to write AI-assisted code is now using that same tool to secure it.

> [Is the SaaSpocalypse nigh? The era of paying for software seats may be ending.](https://thenewstack.io/dawn-of-a-saaspocalypse/)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)