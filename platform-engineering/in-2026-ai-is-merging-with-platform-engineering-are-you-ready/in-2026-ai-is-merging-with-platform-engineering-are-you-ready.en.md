If there’s something we realized in 2025, it’s that AI is an amplifier of human-led software development teams — not a replicant or replacement of human talent.

Over the past year, developer experience (DevEx) has been defined by [platform engineering](https://thenewstack.io/platform-engineering/) and [AI](https://thenewstack.io/ai/) — which is merging into one and the same, as the first emerges as the gold standard for properly, safely and efficiently deploying the second.

But developer productivity, we’ve learned, has been defined by how leadership strategically approaches the adoption of these two trends. Only the organizations that understand AI enablement, via a platform strategy, will stand out in the new year. Here’s how.

## The Role of Operational Platform Engineering in AI Adoption

Platform engineering is the adoption of an internal platform [to create golden paths](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/) that make regular activities — such as deploying to the cloud and requesting services from another team — easier.

Following the [Cloud Native Computing Foundation’s](https://cncf.io/?utm_content=inline+mention) [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/), I asked the experts I interviewed for this post where they were on their platform engineering journey. Overwhelmingly, their responses aligned with the second tier of maturity, called “operational,” which means their organizations have standardized tooling that is centrally tracked by a dedicated platform or DevEx team.

Another quarter was at the final stage of optimization via qualitative and quantitative metrics, integrated and managed services, an enabled ecosystem and a broadly adopted [Platform as a Product mindset](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/). The smallest company I interviewed — [Etiq AI](https://www.etiq.ai/), with fewer than a dozen developers — is still using provisional, custom and ad hoc request processes, which is appropriate while it’s still in its startup phase.

Granted, I generally spoke with platform leads whom I have interviewed over the last couple of years. But my findings could be part of the overall trend that platform engineering is ready to exit the trough of disillusionment. It’s also a natural response to AI adoption demanding at least an internal developer portal, if not a full-fledged platform, laying down guardrails and sometimes gates for this new level of speed.

[Dave Bresci](https://www.linkedin.com/in/dave-bresci-8904846/), senior manager of site reliability engineering at [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention), told me that Backstage and now [Spotify Portal](https://thenewstack.io/confidence-spotify-gives-developers-a-platform-for-experiments/) have acted as a “lynchpin” of platform engineering through “its enablement of golden paths and centralization of technical documentation.”

Within Portal, he said, he has found that “AI coding assistants have been transformative in facilitating experimentation and prototyping for our developers, as well as coding throughput.” Then, on top of that, PagerDuty engineers have built some custom internal tooling with AI to make large-scale changes across the codebase, which he said have been “extremely impactful.”

Of course, any strategy is only as good as how it’s measured.

More than half of those interviewed responded that they run a mix of developer surveys and other qualitative data, with the [core four DORA metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) that track throughput and stability. About a third said they leverage the [SPACE framework](https://queue.acm.org/detail.cfm?id=3454124) and/or the [DX Core 4](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/).

## How AI Is Already Increasing Developer Productivity

While many of the teams consulted for this post are still in the process of deciding which AI tooling, if any, works across their whole engineering organization, some touted big developer productivity wins already.

“These tools don’t just make us faster; they make the work feel lighter,” said [Subho Halder](https://www.linkedin.com/in/subhohalder/), CEO at [Appknox](https://www.appknox.com/), whose security vulnerability detection scale-up has seen the biggest productivity gains so far from what he calls practical AI tools.

“Claude and ChatGPT help our engineers think faster, CodeRabbit speeds up [pull request] reviews and Windsurf/Cursor boosts everyday development,” he continued. “We even allocate a separate budget for AI because the return is clear. And as a security company, every tool is vetted for the highest levels of privacy and compliance.”

For his team at [Spotify](https://engineering.atspotify.com/), [Niklas Gustavsson](https://www.linkedin.com/in/protocol7/), the company’s chief architect and vice president of engineering, said that the tools that really move the needle for them fall into three buckets:

* AI coding tools, with Claude Code, Cursor and GitHub Copilot [used by 90% of developers daily](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/), according to Google’s latest DORA survey.
* Background coding agents integrated into the existing fleet management system.
* Knowledge assistants built into Spotify internal platforms, which are typically dogfooded and then either open sourced or commercialized.

“We plug these AI coding agents into its existing fleet management system as the ‘brain’ that generates code changes from natural-language instructions, while fleet management remains the ‘muscle’ that safely runs those changes across thousands of repos via automated PRs,” Gustavsson said.

At the time of our interview, AI agents had generated more than 1,500 merged pull requests, delivering 60% to 90% time savings on some of Spotify’s larger migrations.

“Under the hood, we have an internal framework that orchestrates prompts, linting, [Model Content Protocol] tools, [large language models] as a judge [of] validation and observability,” he said. “So we can swap the underlying agents and models in and out without disrupting teams.”

Spotify is further ahead of most organizations in its agentic AI journey. And its technical and nontechnical teams are also the first and some of the heaviest users of the [AiKA AI knowledge assistant](https://thenewstack.io/introducing-aika-backstage-portal-ai-knowledge-assistant/), to “find answers to all kinds of Spotify-specific questions, from learning how a particular system or tool works, to getting reference code, to company policies,” Gustavsson said.

He added, “AiKA has helped reduce internal support requests and the number of random questions in Slack and other channels. We’ve seen a 47% reduction in the time it takes to resolve internal support requests at Spotify.”

[Paul Payne](https://www.linkedin.com/in/paulpayne1/), CTO of scale-up [SaaScada](https://saascada.com/), said that Claude Code is completely redefining the software engineering processes of his open API platform for financial services.

“Twelve months ago, we wrote code by hand and we were very proud of that code,” he said. “Today, we rarely write any code — we build specialized agents and skills using Claude Code so that we can operate at a higher level and unlock the massive productivity benefits AI coding agents bring.

“They really are a force multiplier the likes of which we have never seen, and it is allowing us to build entire features and even products in days and weeks that would have taken many months of manual coding.”

This is aligned with the latest [“DORA Report,”](https://dora.dev/research/2025/) released in September, which focused on the impact of AI as an amplifier of software development. Unlike the previous year’s report, which found mixed results for AI in software development, the 2025 survey found that AI assistants had become ubiquitous, triggering a huge impact on individual developer productivity.

An [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") was pinpointed as the best foundation upon which to build AI adoption and to add the guardrails and gates necessary for your own sector’s or your users’ risk profile.

## The Future Is Agentic: Fleets of Autonomous Agents Ahead

While the last couple of years were more about preparing data and systems for generative AI (GenAI) at scale, engineering leaders are really confident in the agentic near future.

Those who are hopeful for what AI brings are definitely looking forward to a greater embracing of agentic AI.

“By 2026, we’ll start seeing AI agents move beyond single-company experiments and into limited cross-organization collaboration, but it will still be cautious and deliberate,” said [Max Marcon](https://www.linkedin.com/in/massimilianomarcon/), [MongoDB’s](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) director of product management. “Right now, most companies are focused on the basics,” which includes important tasks like making sure agents behave safely, access only the right data and operate under clear governance.

“Full interoperability between agents is still early, much like where Open Banking was in its first decade,” he noted.

While 2025 was about early-stage agents, many interviewees predicted that 2026 will be about agentic memory, where these AI agents build on their own past experiences to influence their own decision-making.

“As technology evolves and matures, we will see an increase in examples of true agency where AI agents become more autonomous,” [João Freitas](https://www.linkedin.com/in/jdcfreitas/), general manager and vice president of engineering for AI and automation at PagerDuty, agreed.

Agents, he said, will “adapt better to their context and to the environment, can make better decisions given a wide range of tools and resources, and independently take actions towards a goal.”

The rise of standards like the [Model Context Protocol (MCP) and Agent2Agent (A2A)](https://thenewstack.io/a2a-mcp-kafka-and-flink-the-new-stack-for-ai-agents/), Freitas said, will help establish best practices around agent deployment and monitoring: “This will unlock new use cases and business opportunities, and increase the return on investment from AI.”

Tech leaders tend to be an optimistic bunch, with the startup founders the most doggedly so.

“AI will positively disrupt the entire software development life cycle,” said Payne, of SaaScada. “Existing software engineering teams can achieve significant productivity gains if they embrace this paradigm shift.”

He added that, “10x engineers could become 100x engineers, but each team will need to carefully navigate the intense rate of innovation and change among model and tool providers to fully unlock these gains.”

In response to the speed of change, he predicted that we won’t just see AI infused into traditional project management tools, but 2026 will likely welcome a new era of fully integrated, end-to-end software delivery life cycle tools, “providing all-in-one environments for AI-powered product planning, requirements analysis, technical design, prototyping, coding, deployment and testing.”

He also voiced the common concern that security risks will only rise in this AI-powered near future, but he thinks that AI will be part of the protection, too.

“The best engineering teams will take calculated risks on where and how to constrain AI behavior so their software performs better with each subsequent model release,” Payne said, “allowing them to ride the wave of innovation.”

## Why the Right Developer Experience Is Crucial for Success

The changes roiling the tech world aren’t just technical ones. Communication with your developers — and in fact, your entire organization —  will be the biggest differentiator in 2026.

“It’s easy to get swept up in the excitement of AI, but the biggest differentiator in 2026 will still be leadership that models calm, clarity and structure,” said [Helen Greul](https://www.linkedin.com/in/helengreul/), vice president of engineering at [Multiverse.io](https://www.multiverse.io/en-GB). “Technology is accelerating — people need steadiness. The teams that thrive will be the ones whose leaders remember that.”

This was emphasized this December with the results of [a new white paper by Multitudes](https://www.multitudes.com/data-to-cut-through-the-hype), which determined that leadership’s actions are one of the most important factors in ensuring AI adoption success. Buying a tool does not equal adoption or drive AI usage, the report found. Only when leaders make adoption a vocalized priority or “clear expectation” — mandates aren’t as welcome by developers — did they witness accelerated AI tooling adoption.

“Ask the users what they want,” said [Molly Clarke](https://www.linkedin.com/in/molly-clarke-72b8021/), platform engineering lead at [easyJet](https://careers.easyjet.com/en), who only predicted an increase in prioritization of developer experience in 2026.

In the Age of AI, users include both internal developers and any external customers — don’t go shoving features, especially AI-enriched ones, on your users until you know they want them. Security and other gates should be mandatory, but everything else serving your internal developers — including any platform engineering strategy — must be optional.

The goal of any developer productivity strategy should be to make it easiest to do the right thing, so developers don’t want to leave that golden pathway.

For the last three years, DORA research has proven that user centricity is a huge amplifier of organizational performance. The 2025 “DORA Report” focused on the state of AI-assisted software development, but still found a “user-centric focus” as core to positive outcomes.

The more the survey respondents agreed with the following, the more successful they were with AI adoption:

* Creating value for users is their focus.
* Users’ experience is their top priority.
* Focusing on the user is the key to the success of the business.

In terms of serving internal users, the report further found that internal developer platforms became “nearly universal” over the past year, and that it’s imperative to make your platform the foundation for your AI strategy.

When trying to improve developer productivity in 2026, especially via AI adoption and/or a platform engineering approach, make sure that you listen to your internal developers. They likely know better than anyone else what increases their productivity. This also creates a safe environment for them to innovate and experiment to build great new things.

“We’re entering a phase where small teams can do previously unthinkable things. The playing field is flattening,” Greul said. “I’m excited for the rise of creativity, all sorts of weird ideas and side projects that become billion-dollar companies.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)