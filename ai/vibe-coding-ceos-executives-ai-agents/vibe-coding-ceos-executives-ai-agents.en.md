While software developers seem to have wholly adopted AI coding assistants, the business side of organizations — the C-suite and other executives high up in the chain of command — is adopting these tools to “[vibe code](https://thenewstack.io/beginners-guide-to-vibe-coding/)” a variety of agents and productivity applications.

The trend runs from simple workflow automations to full production systems serving hundreds of users. The tools are [Claude](https://thenewstack.io/anthropics-claude-interactive-visualizations/), [Cursor](https://thenewstack.io/cursor-3-demotes-ide/), and increasingly the AI features embedded in the platforms these executives already run. The motivations range from impatience with IT queues to genuine curiosity about what the technology can do. And the results are more varied than the enthusiasm surrounding them might suggest.

## 140,000 lines, 10 touched

[Moshe Bar](https://www.linkedin.com/in/moshebar/), CEO and co-founder of [Codenotary](https://thenewstack.io/codenotary-adds-background-vulnerability-scanning/), built a bulletin board system (BBS) for IBM 3270 mainframe terminal users starting in March 2025. He is not a programmer. He specified the database structure — tables for users, messages, topics, posts, chat — and handed the rest to Claude. The system now runs to 140,000 lines of code. Bar has personally edited roughly 10 of them.

“A project of this size, with this reliability, with this usefulness in such a short time would have been unthinkable just two years ago,” Bar said.

The system lives at moshix.tech:3270, has 500 users, thousands of active discussions, and has never gone down, he tells *The New Stack*. Bar runs security audits through Claude every eight weeks. He open-sourced the code, and others have since spun up their own BBS instances from it, he says.

The 10 lines Bar edited himself? Menu text he changed during Cursor rate-limit timeouts on a transatlantic flight. He hasn’t touched a source line since moving fully to Claude.

The 3270 protocol — an arcane, bit-precise IBM standard from the early 1970s — has been the one persistent challenge. Claude still occasionally reverts to Unicode or misplaces cursor positions, problems Bar has had to correct hundreds of times. “You’ve got a kindergartner with a doctorate,” he said. But the application runs on 23 megabytes of memory and has had no security incidents in over a year. Bar’s estimate of what it would have cost to build conventionally: three or four senior developers at $400,000 to $500,000 each.

## The CEO who built it twice

[Woodson Martin](https://www.linkedin.com/in/woodsonmartin/), CEO of [OutSystems](https://thenewstack.io/ai-agents-need-more/), took a more structured approach to his own vibe coding experiment. He built a personal mobile app wrapper on top of [MCP services](https://thenewstack.io/mcp-maintainers-enterprise-roadmap/) his team had created — and he built it twice in parallel, once using OutSystems’ own AI coding tool, [Mentor](https://www.outsystems.com/low-code-platform/mentor-ai-app-generation/), and once using Claude, connecting to the same backend both times.

“I was tired of explaining it to somebody who was supposed to build it for me,” Martin said. “I was just like, ‘I’ll do this myself.'”

The app is a personal chief-of-staff system that consolidates customer account intelligence — buying signals, website activity, internal data — into a pre-meeting briefing he can pull up on his phone. It replaced what had been a 45-minute PowerPoint session plus multiple prep meetings from his sales team.

Martin also runs the company on a goal-setting framework called [V2MOM](https://www.salesforce.com/blog/how-to-create-alignment-within-your-company/) (adopted from Salesforce, where he used to work), which his team has since productized as an MCP service. Before executive one-on-ones, he queries it to surface alignment gaps between individual and corporate goals. An agentic layer built around the framework now helps cascade organizational change company-wide.

At Codenotary, Bar’s mandate to his engineering organization stemmed from his experience with AI-assisted coding; he tells *The New Stack* that three to four months ago, he declared that all development at the company would be LLM-only going forward. His reasoning is straightforward — cloud computing compressed time-to-market from three years to one; LLMs compressed it again to three months.

“If you cannot come to market with a new application from scratch within three months, you’re probably already missing the market,” he said.

Asked if he felt like a programmer after having successfully vibe coded a BBS, Bar said, “No, I don’t. Sadly, I don’t, because when I look at the code, some of the things it does, I have no idea, no idea.”

## Eating their own cooking

Other executives are working on a smaller scale but with a similar intent. [Wade Foster](https://www.linkedin.com/in/wadefoster/), co-founder and CEO of the AI orchestration platform Zapier, described building a personal AI chief of staff using the Zapier SDK within Cursor. “The SDK handles auth for every tool I use at work,” Foster [writes on LinkedIn](https://www.linkedin.com/pulse/how-i-built-my-ai-chief-staff-zapier-sdk-wade-foster-rudbc/). “The coding agent handles everything else. I just describe what I want.”

[Jessica Stefanowicz](https://www.linkedin.com/in/jstefanowicz/), external communications manager at Anaconda, vibe-coded an awards tracking dashboard in Claude — her first such project. The tool automatically updates weekly, monitors application deadlines and submission requirements, and recommends award programs suited to specific business updates and products. It replaced roughly an hour of manual work per week.

[David Slater](https://c67dcd9a.streak-link.com/C2964Ywf32lJ4lqrYwEATwuN/https%3A%2F%2Fwww.linkedin.com%2Fin%2Fslaterdavid%2F), chief marketing officer at [Front](https://c67dcd9a.streak-link.com/C2964-O39_GjOlwSSQmKU22q/https%3A%2F%2Ffront.com%2F), which provides a customer service and operations platform, said he built a two-agent system using Claude to manage 50 to 70 Objectives and Key Results (OKRs) items across a 90-day cycle. One agent is to prep for biweekly check-ins by flagging areas needing attention and generating questions for owners ahead of meetings, a second is to produce status reports tailored to three different audiences — product, sales, and the executive team — after reviews are complete. No code was written.

“I’m not a technical user. I didn’t build these agents by writing code,” Slater tells *The New Stack*. “But this system has fundamentally changed how I run a core part of our department’s operating rhythm.”

## The skeptics have a point

Analysts watching the trend are not uniformly enthusiastic.

[Andrew Cornwall](https://www.linkedin.com/in/acornwall/), an analyst at Forrester, confirmed that non-technical executives are building significant web apps, but also cataloged the risks: vibe-coded apps are typically not hardened against attacks, often lack controls that satisfy auditors, and frequently get dumped on CIOs or CTOs without budgets or maintenance plans. In the worst cases, an executive uses an unapproved AI provider and leaks corporate data.

“If vibe coders and their users understand the limitations of their apps, they’re not riskier than the spreadsheets they built in the past.” The harder problem, he notes, is that a polished-looking app may obscure whether it’s professionally supported or something held together with prompts.

His Forrester colleague [Ken Parmelee](https://www.linkedin.com/in/kparmelee/) added two skeptical notes. First, executives are often not building alone — an IT person is typically involved, though the executive takes the credit in internal communications. Second, and more fundamentally, most non-developers hit a wall. “Non developers are not systems thinkers,” Parmelee tells *The New Stack.* The moment a project requires a database, persistent memory, or a backend integration, most can’t proceed independently.

“Can they do very simple applications or flows,” he said, “but many times that doesn’t equate to real value.”

Constellation Research analyst [Holger Mueller](https://www.linkedin.com/in/holgermueller/) says he sees a meaningful upside to the skeptics undercount: executives building their own automation don’t commandeer developer budgets or engineering capacity. “Projects stay on course” for the rest of the enterprise, he said.

Meanwhile, [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, said his firm is seeing a rapid outward expansion of agentic coding (e.g., vibe coding).

According to their recent Decision Maker survey of 818 data professionals, 75% are already spending more time on business concerns rather than on coding pipelines using generative and agentic AI tools.

And they are not alone, Shimmin indicated.

“Anecdotally, we are seeing this same acceleration and expansion among non-IT professionals, especially executives,” he tells *The New Stack*. “No, these folks are not writing software in the traditional sense. On one end of the spectrum, they’re automating a wide range of tasks to free up time and energy. And on the other end, they’re using these tools to drive change and explore new opportunities. Instead of calling a meeting to discuss a new idea (e.g., a new product or a revised workflow), executives are building their own working prototypes to stress-test their ideas and, if successful, accelerate time-to-market by handing over these early assets to IT for refinement and implementation.”

## A new floor, or an outlier?

Bar is clear-eyed about his own position in the distribution. “I think I’m a little bit of an outlier due to the scope of the application,” he said. Most vibe coders, in his observation, are scratching a specific itch — a small, well-defined app. Whole systems serving hundreds of users are rare.

But the floor for what’s possible keeps moving. Bar said he’s rethinking a conversation from a few years back in which he confidently told a neighbor that demand for developers would always be strong.

“I’m starting to think maybe that was a mistake,” he said, “because I start to think maybe we’re slowly coming to an end of this oversized demand for developers.”

[Gene Kim](https://www.linkedin.com/in/realgenekim/), whose book *[Vibe Coding](https://www.amazon.com/Vibe-Coding-Building-Production-Grade-Software/dp/B0FPGHVGD8/ref=sr_1_2?adgrpid=186412553677&dib=eyJ2IjoiMSJ9.v9_Oe2RCDcAJ1OxHYNXt94yT_JuJdsvdiFMM0rbLvkbqNj9dVfQ-ebhVYgSKtPpYuJ4PAczgdFU6FJx-NuIQAXT5rplixZ3cuZIzrp5fYA2ht8tnEHeLh96-yZeo9zeGb3DpIKNndinCre3IUqz-fLTnVVpiwJa-zwIpYu9RwgKAsji1QNdMcDtB4SiegYLlC-dYBgO-LyEKUtbXiAZuTw.D-HcSIfeZ1PqfnRNle99tLFaI4X4TrlpzXYYsZPTln0&dib_tag=se&hvadid=779657810078&hvdev=c&hvexpln=0&hvlocphy=9007907&hvnetw=g&hvocijid=15607065160011506336--&hvqmt=e&hvrand=15607065160011506336&hvtargid=kwd-2435698919933&hydadcr=16400_13457160_8572&keywords=gene+kim+vibe+coding&mcid=a6a8db8d14f13713be7831ec62db55c6&qid=1777292464&sr=8-2)* frames the [moment](https://www.linkedin.com/in/realgenekim/) expansively, puts it this way: “We’re witnessing a software revolution that may make the 1990s internet boom look like a warm-up act.”

In an interview with *The New Stack* last year, Kim said AI coding represents a transformation “[10 to 100 times bigger than DevOps](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/)” — and he’s betting his reputation on the [potential of “vibe coding.”](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)

The executives vibe coding in their off hours might be the leading edge of that.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)