If you ask engineers how much time they think they’re saving with AI, they’ll often give optimistic answers. But when you compare that sentiment with real quantitative data, the numbers don’t add up.

People tend to think about personal time savings in isolation: “I finished my PR faster.” That pull request (PR) might sit unreviewed for three days before being tested, fail in testing and bounce back for fixes. The result is inefficiencies across the engineering organization that eat up any productivity gained.

Most engineering organizations do not need faster typers. The common engineering bottlenecks are flaky pipelines, no testing strategy, poor documentation or organizational structures — the usual roadblocks to getting to business value. Your team might get marginally faster at writing code, but unless you [address those systemic issues](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness), you’re never going to realize the full value of AI tools.

## ‘If We’re Not Using AI, We’ll Be Left Behind.’

Developer experience was already a tough topic before AI. When we talk about [developer experience (DevEx) in the age of AI](https://thenewstack.io/how-to-think-about-devex-when-ai-writes-the-code/), let’s start by acknowledging that even the definition of [“developer” is changing](https://www.aviator.co/blog/software-engineering-ai-2027/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-engineering-2027&utm_term=net-new&utm_content=awareness). It’s no longer someone getting requirements from the product team and quietly coding away. Instead, they might generate partially working proofs of concept from AI tools or collaborate more fluidly with non-engineers who use AI to prototype ideas.

There’s also the explosion of AI tools. Every day it feels like there’s something new on the market. On one hand, that’s exciting for engineers: shiny new tools, new ways of working. Then there’s pressure from leadership, what I’d call a bit of FOMO. You see executives thinking: “If we’re not using AI, we’re going to be left behind.”

## Don’t Just Pick a Tool, Pick a Problem

Organizations are spending too much time, money and energy focusing on the tools themselves. “Should we use OpenAI or Anthropic? Copilot or Cursor?” We see two broad patterns for how organizations approach AI tool adoption.

The first is that leadership has a relationship with a certain vendor or just a personal preference, so they pick a tool and mandate it. This can work, but you’ll often get poor results — not because the tool is bad, but because the market is moving too fast for centralized teams to keep up.

The second model, which generally works much better, is to allow early adopters to try new tools and find what works. This gives developers autonomy to improve their own workflows and reduces the need for a central team to test every new tool exhaustively.

Comparing the tools by features or technology is less important every day. You’ll waste a lot of energy debating minor differences that won’t matter next year. Instead, focus on what problem you want to solve. Are you trying to improve testing? [Code review](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-4-flexreview&utm_term=net-new&utm_content=awareness)? Documentation? Incident response? Figure out the goal first. Then see if an AI tool (or any tool) actually helps.

If you don’t, you’ll just make DevEx worse: You’ll have a landscape of 100 tools nobody knows how to use, and you’ll deliver no real value.

## Complexity Can’t Be Removed, Only Abstracted

There’s a lot of hype about an AI future without software engineers. The reality is that you can’t remove complexity from engineering. You can abstract it away, but the complexity remains.

Even if this utopia existed, where AI and agents do all the work, we’d still need to create the agents, train them, add new levels of observability, implement better FinOps controls to understand cost and complexity, manage the models they use and add new layers of governance to audit the reasoning that leads to their decisions.

Imagine you let an AI agent handle incident response: It can gather logs and generate a report. That’s a good use case. Another agent or set of agents can then toggle feature flags via [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) or trigger rollbacks. That sounds great — until something goes wrong. Do you have rigorous audits, controls and a plan for what happens if the AI makes the wrong call?

[!["This is fine" meme](https://cdn.thenewstack.io/media/2025/07/f65692c0-this-is-fine.png)](https://cdn.thenewstack.io/media/2025/07/f65692c0-this-is-fine.png)

From “[On Fire](https://gunshowcomic.com/648)” by KC Green

It’s additional layers of complexity. It’s not less work; it’s different work.

In practice, AI tools can add cognitive load rather than reduce it. You might be using five different AI-enhanced integrated development environments (IDEs). Instead of 20 browser tabs, now you have 50. Without thoughtful integration, you’re just making your life harder.

## Reducing Cognitive Load With AI

If you want your engineering organization to get real value from AI, you have to [identify the waste and friction](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness) that are in people’s way and address them in the same old way — by having a good supporting platform (whether you call it [platform engineering or something else](https://thenewstack.io/platform-engineering-vs-devops-misses-the-point/)). The only way to improve developer experience with AI tools is to approach it from the platform perspective and apply that thinking over and over again.

Think about [platform engineering](https://thenewstack.io/platform-engineering/) that not only abstracts away the problems into static dashboards, but also curates the AI-powered layer that summarizes the important problems.

Emphasis on the *important*. There are now AI site reliability engineering (SRE) tools that can help you investigate incidents, but they’ll give you a list of 20 things that could have gone wrong. That’s not helpful from a developer-workflow perspective; devs need one right answer, not 20 possibly right answers.

Be careful about replacing dashboards curated by humans with opaque AI reasoning. Make sure your data model is solid enough to support it. Once you lose that transparency, you introduce new risks, like your AI confidently telling you “everything is fine” when it isn’t.

## The Question Isn’t ‘What’s Your AI Strategy?’

Around 90 to 95% of engineering inefficiencies are caused by flawed systems, not by people. So don’t just throw AI at everything and measure success by asking people, “Did it save you time?” in isolation. Instead, look holistically across your software delivery life cycle:

* Where is friction highest?
* Where does work queue up?
* Where does rework happen?

Only then you can decide if and how AI can help. Because you probably don’t need faster typers. You need [better systems](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/5ad1f17b-chris_westerhold.jpg)

Chris is a Global Practice Director for Engineering Excellence at Thoughtworks. He has over 15 years of technology experience across startups and large enterprises, with a significant focus on building scalable engineering teams, engineering metrics strategies, developer platforms, platform engineering...

Read more from Chris Westerhold](https://thenewstack.io/author/chris-westerhold/)

[![]()

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)