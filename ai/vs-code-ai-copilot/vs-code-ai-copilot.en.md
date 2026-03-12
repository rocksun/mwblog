Earlier this year, [Pierce Boggan](https://www.linkedin.com/in/pierceboggan/), the Product Lead for [VS Code](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/) and [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) at Microsoft, quietly dropped a bombshell on the product management world: His team was building tooling that lets PMs — not engineers — define, prototype, and evaluate user-facing features using AI agents. “The real power is how this changes the PM workflow,” he writes in the January 9 [LinkedIn post](https://www.linkedin.com/posts/pierceboggan_the-visual-studio-code-product-team-is-exploring-share-7415482603446824961-O8tT/), describing a loop where a PM defines a scenario, hands it to GitHub Copilot to implement, self-hosts the build for days, and iterates until the prototype is production-ready.

The reactions were swift and pointed. Some were enthusiastic. In fact, a fellow Microsoft PM called it a feeling of having “super powers.” Others pushed back. “I think you need to go the other way,” wrote [Alnur Ismail](https://www.linkedin.com/in/alnurismail/?originalSubdomain=ca), a former Microsoft engineer. “Your engineers should be the ones [who] use this tool. They know the code base, so the leverage here is helping them get closer to the customer.”

Now, two months later, *The New Stack* caught up with Boggan to see how the experiment was playing out in practice. His answers were candid, specific, and at times surprising — touching on a 10-year release cadence that AI helped break, a PM-authored PR that shipped to tens of millions of users, and why he thinks “agent-ready codebase” is the meta-skill every engineering team needs right now.

*This interview has been edited for clarity and brevity.*

**What specific AI tools, models, or internal agents are the VS Code team currently using to assist Product Managers and engineers in their day-to-day work?**

**Pierce Boggan:** A core principle of the VS Code team has always been that we use VS Code to build VS Code. The same is true now with AI — as a product manager, I try to always self-host with VS Code and GitHub Copilot. VS Code is one of the largest open source repositories, shipping stable releases weekly to tens of millions of users.

My morning starts with a prompt file that pulls in my calendar, emails, and Teams messages using [Work IQ](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/workiq-overview) and uses the GitHub MCP to fetch relevant context about product and engineering updates. I rely on this prompt file to summarize everything that’s new in VS Code over the past 24 hours.

Most of our core PM workflows run in VS Code and Copilot too — dedicated prompts to analyze our feedback repo, purpose-built web apps to analyze social media, AI-powered automations to keep docs and release notes current.

On the engineering side, [Peng Lyu](https://www.linkedin.com/in/rebornix/), principal software engineering manager, VS Code, and others have built custom agents and slash commands tailored to their workflows — summarizing the last 24 hours of commits, grooming and deduplicating issues without leaving VS Code. We use [Copilot Code Review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review) on every PR as a mandatory first pass before human review. The team also built a custom agent called ‘demonstrate’ that allows GitHub Copilot to self-validate by actually launching VS Code, navigating to a feature, taking screenshots, and evaluating whether a change works as expected.

On the model side, we have our own internal benchmark — vsc-bench — to inform how different models perform in the VS Code harness. For commit summarization, we use a faster model. For code generation or review, we’ll use the most capable one available. Sometimes we spawn multiple models in parallel subagents and let them grade each other’s work.

The tooling is evolving fast, so what we’re using today is probably different from what we’ll be using a month from now — and that’s kind of the point!

**Can you elaborate on how you are prototyping solutions to PRs?**

The shift for me has been fundamental: the equivalent of a spec or PRD is now a prototype, and that prototype is a PR.

Someone gives us feedback — on X, Reddit, a GitHub issue, wherever — and instead of writing a doc about what we think the experience should be, I open plan mode in VS Code and start building it. The spec sharpens as I use the product, not just write about it.

For example, the day before our [Agent Sessions Day](https://developer.microsoft.com/en-us/reactor/events/26588/) recording, I sent a PR for forking conversations in Copilot Chat. One of our engineers gave me feedback, we worked through a couple of CSS changes together, and merged it. That’s in VS Code now.

Where this works best is UI and interaction-level changes — things where the “is this right?” question is really about the experience, not deep architectural decisions. I want to be clear, though: engineers are still accountable for code quality and architecture. If Peng looks at my PR and says “this isn’t architected right,” that’s totally fair — I’m fine with my code getting thrown away and rebuilt.

What’s really happening is that the boundaries of the role are collapsing. I always had product thinking, but was limited by building skill — that’s no longer the bottleneck.

**What specific metrics are the team tracking to quantify the direct impact of AI adoption?**

One of the most concrete proof points is visible to every VS Code user: after 10 years of monthly releases, we moved to weekly. The overhead of a release cycle — triage, testing, release notes, stabilization — used to require a full month of rhythm. Now, enough of that is automated or agent-assisted that we can sustain a weekly cadence and still maintain quality.

Commit velocity has seen a real and sustained increase — it used to be 20 or 30 commits when you’d git fetch. Now it’s regularly 100+ per day. PR cycle times have compressed. And our agent-based triage pipeline handles the initial sorting, duplicate detection, and owner assignment that used to require a dedicated human rotation every week.

On quality, we’re watching regression rates closely because velocity can hurt you if you’re not careful. The metric we care most about is, “Are we shipping fewer regressions to stable than we were before?” So far, the answer is yes — but it requires constant attention.

**How does the team envision roles evolving over the next year or two as AI tools become more deeply integrated into the development process??**

The boundary between “person who thinks about the product” and “person who builds the product” is genuinely blurring. Everyone is becoming a more full-stack contributor to the outcome.

On the engineering side, when agents can help anyone contribute to any component, the traditional model of “this is my area, stay out” doesn’t hold. You need harnesses — tests, documentation, clear ownership boundaries — not to keep people out, but to welcome them in safely.

The mechanical parts of the job — writing boilerplate, triaging routine issues, catching common bugs in review — are increasingly handled by agents. What becomes more valuable is taste, judgment, and the ability to evaluate whether something actually delights the person using it. The teams that invest in making their codebase agent-ready are going to see compounding returns. That’s the meta-skill every engineering team needs to be developing right now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)