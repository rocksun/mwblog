![Several hands guide an oversized pen, paintbrush and pencil to draw a heart on an easel, illustrating team collaboration](https://cdn.thenewstack.io/media/2026/11/83c51965-ghariza-mahavira-5biac69ve_g-unsplash-1024x768.jpg)

**Docusign rolled out AI coding tools across its engineering teams, expecting them to help developers write code faster and do more. Initial enthusiasm was high, but early gains plateaued.**

By June 2025, Docusign had reached a sticking point. According to its [engineering team’s account](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it), 49% of engineers were actively using AI coding tools, while a reported 18% improvement in developer productivity had leveled off. Engineers still needed time to experiment, guidance tailored to Docusign’s codebase, and help fitting the tools into their day-to-day work.

Docusign now reports that all of its more than 1,100 engineers are onboarded to and actively using AI coding tools

![Sagnik Nandy, Chief Technology Officer, Docusign](https://cdn.thenewstack.io/media/2026/10/5e11eb07-docusign-cto.jpeg)

Docusign CTO Sagnik Nandy

CTO [Sagnik Nandy](https://www.docusign.com/blog/author/sagnik-nandy) believes getting people to use the technology is only the beginning.

“There’s a big difference between trying to get a few wins versus doing it consistently and doing it right,” Nandy tells *The New Stack*.

Docusign responded by changing how it introduced and measured AI across engineering, moving beyond coding assistants toward reusable agents and automated workflows.

## **Why Docusign turned to its engineers**

Instead of making AI adoption mandatory, Docusign established a six-person Eng AI Champions team to develop guardrails, share engineering practices, and run workshops. Docusign reports that adoption reached 65% by October 2025. The company then extended that work through AI Multipliers embedded in individual development teams. Nandy says around 75 Multipliers helped teammates put the shared practices into use and fed problems back to the central team.

“They were tasked with two things,” Nandy explains. “The decisions, the solutions we built, they had to deploy it within their team, and also get feedback in terms of what’s working, what’s not working, and what’s missing.”

Docusign’s [account of the initiative](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it) showed that [active usage reached 93%](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it) within two months of introducing the Multipliers, while lines of code updated per developer increased by approximately 52% from the company’s starting point. That code-volume measure does not, by itself, establish a matching improvement in delivery speed or software quality.

Nandy believes the combination of central coordination and feedback from individual teams has helped sustain the program, an approach he has also discussed in an [engineering leadership podcast](https://sfelc.com/podcasts/best-practices-for-scaling-ai-adoption-across-a-large-org-and-the-trade-offs-you-will-have-to-make-sagnik-nandy-docusign).

> “When I speak to many of my peers, a lot of AI programs start well, and then fizzle out.”

“When I speak to many of my peers, a lot of AI programs start well, and then fizzle out,” he says. “I think the reason that hasn’t happened for us … is because we already have such a rich body of information and feedback flowing in, and people acting on it and then redeploying things.”

## **Teaching AI to ‘speak Docusign’**

Once engineers were comfortable using AI for coding, Docusign began looking at entire development workflows. That required tools with access to its repositories, architecture, telemetry, and internal practices, so assistants could work with the company’s own context.

“Our solutions and agents, we joke, they speak Docusign,” Nandy says. “They know which internal tools to go look into, what our internal coding guardrails are, guidelines are, what system choices we make, where information resides for disambiguating between different pieces of information.”

Nandy describes several internal tools for different engineering tasks: Kody for Docusign-specific coding work, Chronicle for observability and incident investigation, and DocuWiki for code-aware internal documentation. Docusign’s [engineering blog](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it) also describes an AI-assisted code review tool for identifying potential architectural and security issues during review.

[Krew brings these capabilities together](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates), allowing teams to build agents called Krewmates for recurring tasks and more complex workflows.

“One of the things that the Eng AI Champions and Multipliers did is they identified end-to-end flows, and we wanted to improve the entire flow,” Nandy says.

He describes an internal agent that runs overnight, searches error logs for problems, and prepares proposed fixes.

“Come morning, the engineer is greeted with, ‘Hey, here’s a PR. This was an issue we found, and this is the fix.’ It’s magical.”

In Nandy’s example, Krew coordinates the workflow, drawing on telemetry from Chronicle and Kody’s coding capabilities. The engineer then reviews the proposed pull request.

Docusign [gives another example](https://www.docusign.com/blog/how-we-built-an-autonomous-coding-agent-for-repetitive-engineering-tasks). For a task involving infrastructure configuration files, the agent correctly modified 10 of 12 files on its first pass in about 15 minutes, using a sample commit as guidance. The company says the process previously took roughly a week of engineer time. The first pass still left two files to correct; it was not a finished, approved change in 15 minutes.

## **Making successful workflows reusable**

An agent built for one team has limited value if everyone else has to recreate it.

Docusign’s [Krew orchestration platform](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates) allows engineers to discover, copy, and extend Krewmates connected to internal systems. These agents can handle recurring tasks, respond to triggers, and involve people when needed.

“We’ve taken a very open approach,” Nandy says. “All the Krewmates are visible to everyone. You can see how much they are getting used. It’s extremely easy to copy and extend them.”

Frequently used Krewmates become more visible, helping teams find existing solutions rather than building their own from scratch.

> “If something is good, you can try to teach 1,000 other people to do it, or you can make it easy for 1,000 other people to inherit it.”

“If something is good, you can try to teach 1,000 other people to do it, or you can make it easy for 1,000 other people to inherit it. And we went for the latter.”

The approach also depends on maintaining those shared tools, documenting changes, and feeding problems back to the teams responsible for improving them. Docusign’s [Krew team reports](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates) that apparently successful runs sometimes left duplicate posts or partial outputs, prompting improvements to run tracking and observability. For leaders adopting this model, a durable workflow needs a named owner, a way to report failures, and periodic checks on quality and running costs.

## **Measuring what matters**

Docusign’s adoption figures show how widely AI has spread, but Nandy is wary of treating usage as the ultimate measure of success.

“We’ve been very focused on value as opposed to anecdotes or gimmicks,” he says. “The way to do that is you keep moving up the value chain.”

Initially, Docusign measured how many engineers were using AI, followed by how much code they were generating. Nandy says the next questions concern whether teams are actually delivering better results.

“Adoption, so what? … Are you doing more?” he says. “Then you look at feature velocity. Are you shipping things sooner?”

Docusign also considers customer satisfaction and reliability, particularly whether faster development introduces problems elsewhere.

For engineering leaders, that means examining delivery times, review latency, testing, rework, and incident investigation rather than relying solely on adoption percentages or lines of AI-generated code.

## **Guardrails before speed**

Giving agents more responsibility doesn’t mean removing human accountability.

“Any PR, it’s the responsibility of the individual signing off on it,” Nandy says. “No code goes unreviewed into the system.”

Docusign says its autonomous coding agent runs tests before submitting pull requests, with human review, AI-generated-code labels, and quality gates required before merging. Its [AI Innovation Principles](https://www.docusign.com/products/platform/ai/innovation-principles) emphasize human oversight and safeguards. [Krew’s documentation](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates) makes the boundary explicit: an agent cannot merge a pull request or take an irreversible action without a person’s approval.

Nandy compares AI to a chainsaw: a powerful tool that can accomplish more than traditional alternatives, but requires appropriate safeguards.

> “You need very different gear when you have a chainsaw, otherwise you can hurt yourself.”

“You need very different gear when you have a chainsaw, otherwise you can hurt yourself,” he says. “It’s important to get that right.”

He also warns against introducing AI where conventional software would work better. Some of Docusign’s internal solutions were developed using AI but run as deterministic processes without continually invoking a model.

“I often see people throwing AI at problems that probably don’t need AI,” Nandy says.

## **Beyond the rollout**

For Nandy, Docusign’s approach rests on five principles: measure value, make successful solutions reusable, keep costs and governance sustainable, establish guardrails and build in the organization’s own context.

Together, these principles support a shift from encouraging engineers to try AI to workflows that teams can maintain, measure, and improve across teams. The practical next step for an engineering leader is to choose a well-defined workflow, agree on the outcome to measure, assign an owner, and specify where human approval is required before expanding it.

The lesson for engineering leaders is that adoption alone won’t deliver lasting results. Teams also need shared tools, clear ownership, engineer feedback, and measures that show whether the work is actually getting better.

More details are available on Docusign’s [Engineering blog](https://www.docusign.com/blog/topics/engineering), alongside its current [engineering opportunities](https://careers.docusign.com/careers-home/jobs/categories/Engineering).

### More Docusign in *The New Stack*

The post [Moving from AI adoption to an AI operating model: How Docusign engineering went beyond tool rollout](https://thenewstack.io/docusign-ai-engineering-adoption/) appeared first on [The New Stack](https://thenewstack.io).