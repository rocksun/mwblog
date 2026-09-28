We all know that producing code is easier than ever thanks to the abundance of AI coding tools and agents. The harder part undoubtedly comes *after* that code is written: making sure changes are safe to ship, spotting regressions in production, and figuring out what went wrong.

And that’s why Cursor is introducing [Rollouts](https://cursor.com/changelog/rollouts-and-security-reviewer), a new agent that follows code changes into production and monitors whether they behave as intended.

## The Firetiger effect

The announcement comes a little over a month after SpaceX [closed its bumper](https://x.com/cursor_ai/status/2088249881718919393) $60 billion acquisition of Cursor, giving the AI coding company access to SpaceX’s vast GPU infrastructure as it develops its own models.

The day before that deal closed, however, Cursor quietly [announced an acquisition of its own](https://cursor.com/blog/firetiger): it snapped up the team behind [Firetiger](https://www.firetiger.com/), a three-year-old startup building AI agents that monitor software changes from pull request through deployment.

At the time, Firetiger co-founder and CEO [Rustam Lalkaka](https://www.linkedin.com/in/lalkaka/) argued that coding agents had dramatically reduced the effort involved in creating software changes, while doing little to reduce the risks involved in actually deploying them.

“Over the last two years, agentic coding has changed software dramatically,” Lalkaka [wrote](https://www.linkedin.com/feed/update/urn:li:activity:7493743431840673793/) in a LinkedIn post following the deal’s announcement. “The cost of creating changes has dropped to near zero. The cost and risk of deploying them has stayed largely the same.”

> “Writing code is no longer the slow part. What hasn’t sped up is everything after the PR goes up: making sure code is secure, watching the deploy, deciding whether a latency bump is real, figuring out which of eleven changes broke checkout.”
>
> Rustam Lalkaka, Cursor

Fast forward to today, and Lalkaka, now at Cursor, has unveiled the first fruits from that acquisition — including Rollouts. In a [blog post](https://cursor.com/blog/rollouts-and-security-reviewer) published on Wednesday, Lalkaka notes that the new agent, or “bot” as the company calls it, is all about helping developers “get safe, reliable code into production faster.”

“Writing code is no longer the slow part,” Lalkaka writes. “What hasn’t sped up is everything after the PR goes up: making sure code is secure, watching the deploy, deciding whether a latency bump is real, figuring out which of eleven changes broke checkout.”

Rollouts is effectively Firetiger’s Change Monitors reborn inside Cursor, rebuilt using a tool dubbed *Bot Development Kit*. This kit, too, appears to be new from Cursor: an early-stage framework for building and serving Cursor bots and agents, [published](https://www.npmjs.com/package/%40cursor/bdk) as the `@cursor/bdk` package on npm. Its documentation says developers can define agents using Markdown and TypeScript, with support for tools, skills, subagents, webhooks and scheduled runs.

Like Change Monitors before it, Rollouts starts working when a pull request opens. It examines the proposed code change, works out which systems could be affected, and produces a monitoring plan covering what the change is supposed to do, the risks it sees, the signals it intends to watch, and any holes in the available instrumentation. Developers can review and edit that plan before the code reaches production.

![Rollouts in action (1)](https://cdn.thenewstack.io/media/2026/09/e009ed6c-gif1.gif)

*Rollouts generates a monitoring plan for a change*

Once the change is deployed, Rollouts checks the resulting telemetry — including logs, metrics and traces — against that plan. Staging and production are assessed independently, with each deployment ultimately receiving one of three verdicts: verified healthy, regression detected or inconclusive.

That means a change could, for example, pass its checks in staging before Rollouts subsequently spots a problem when the same code reaches production.

![Rollouts in action (2)](https://cdn.thenewstack.io/media/2026/09/d24a9950-gif2.gif)

*Rollouts reports deployment status as changes ship*

If Rollouts *does* detect a regression, it can identify the change it suspects, alert the developer responsible and, depending on how it’s been configured, either open a revert pull request for review or hand the problem to a Cursor cloud agent to attempt a fix. There is still a human in the consequential part of that loop for now: Rollouts doesn’t merge fixes or roll back deployments by itself, though it can pause a progressive rollout.

Lalkaka notes that Rollouts is already capable of picking up problems limited to a particular endpoint or region before they trigger a broader alert, while it can also distinguish expected changes in behavior from genuine regressions.

Also “coming soon” to Rollouts, according to Cursor, is an integration with feature flags so it can directly adapt the traffic reaching a change, while support for release trains and deployment freezes is also in the works.

## Enter Security Reviewer

Alongside Rollouts, Cursor is also introducing an upgraded Security Reviewer bot, which first appeared in beta [back in April](https://cursor.com/changelog/04-30-26).

At launch, the bot could automatically inspect pull requests for security vulnerabilities, authentication regressions, privacy and data-handling risks, agent tool auto-approvals, and prompt-injection attacks, leaving findings alongside the relevant code.

As with Rollouts, the idea is that developers don’t have to remember to invoke it manually: Security Reviewer can be set to run whenever a new pull request is opened.

![Security Reviewer in action](https://cdn.thenewstack.io/media/2026/09/83b5f76d-gif3securityerviewr.gif)

*Security Reviewer runs automatically on new pull requests*

In its current guise, Security Reviewer analyzes pull requests in the context of the wider codebase, with a focus on exploitable issues such as injection flaws and broken authentication, and returns a severity rating, attack path and proposed fix.

“Security Review reads code the way a security engineer does,” Lalkaka writes. “Where does user input enter, where does it end up, what does it pass through on the way.”

> “Security Review reads code the way a security engineer does.”

He says that things have sped up considerably, too: average review time has fallen 21%, from 4.8 minutes to 3.8, while developer acceptance of its comments has risen from roughly 45–50% to 60–70%.

Both Rollouts and Security Reviewer are available through Cursor’s Automations tab for customers on its Teams and Enterprise plans.

## The Origin story

Digging into the nuts and bolts of Rollouts reveals how it might serve as a boon for Cursor as it builds out [Origin](https://cursor.com/docs/origin), the fledgling Git-compatible code hosting platform it [launched back in August](https://thenewstack.io/cursor-origin-github-alternative/).

Origin is essentially an effort to build an alternative to GitHub for an agent-heavy software development world. It remains early, with limited functionality, but Cursor has been clear that tighter integration with its own agents is supposed to become one of the main reasons to use it.

When Cursor announced the Firetiger acquisition last month, [Maxime Prades](https://www.linkedin.com/in/pradesmaxime/?locale=en) on the Cursor product team [noted in a blog post](https://cursor.com/blog/firetiger) that the deal was part of a “broader investment in long-running, autonomous, context-aware agents for teams.”

And he pointed to Origin and Change Monitors as two examples of that investment.

“Agents that write code should also be able to tell whether it works in production,” Prades wrote. “Today, those systems are mostly separate. Cursor and Firetiger bring them closer together so an agent can ship a change, see how it behaves, and respond when something goes wrong.”

Rollouts offers an early glimpse of that. It can connect to either Origin or GitHub for source control, pull deployment events from continuous delivery systems, and use signals from Datadog and other telemetry providers. If it spots a regression, it can then pass the problem back to a Cursor cloud agent to investigate or attempt a fix.

Origin [potentially gives Cursor](https://cursor.com/docs/origin/integrations) a native home for more of that loop: its cloud agents can already create branches, commit and push code, and open pull requests against Origin repositories. Rollouts then adds information about what happened after.

That could become increasingly important as more companies take aim at GitHub’s central role in software development. Zed, for example, put [Delta into public beta last week](https://thenewstack.io/zed-delta-github-alternative/), with its own ideas about how source control should change for teams working heavily with agents.

Cursor also faces competition further downstream. Datadog’s [Bits Release](https://www.datadoghq.com/product-preview/bits-release/), launched in [preview in June](https://www.datadoghq.com/blog/bits-release/), similarly follows changes from pull request into production and checks telemetry for regressions. Harness has [long offered automated deployment](https://www.harness.io/products/continuous-delivery/ai-assisted-deployment-verification) verification and rollback based on logs and metrics, while LaunchDarkly’s [Guarded Rollouts](https://launchdarkly.com/docs/home/releases/guarded-rollouts) can [monitor feature releases for regressions](https://thenewstack.io/ship-fast-break-nothing-launchdarklys-winning-formula/) and automatically reverse them.

What Cursor can potentially bring to the table is proximity: the coding agent, repository, pull request, security checks, and production feedback can all sit much closer together. Rollouts doesn’t require Origin — GitHub remains supported — but owning the forge gives Cursor more room to integrate those pieces over time. And that may prove more compelling than simply recreating GitHub’s existing feature set.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)