*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

***Update, Friday evening**: [Anthropic disabled access to Fable 5 and Mythos 5 for everyone](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) to comply with a US government export-control directive. This happened *hours after I finished the column and before it publishes Saturday morning.* The government says it learned of a method for jailbreaking Fable; Anthropic reviewed the technique, called it minor, and noted that other public models – including OpenAI’s GPT-5.5 – surface the same things without any bypass. Anthropic calls the order a misunderstanding and says it’s working to restore access. By the time you read this Saturday morning, Fable may be back, or it may not. Either way, the point of the original column below got sharper on the news: a model you were leaning on can vanish overnight, and knowing which model to reach for next is the whole game.*

Anthropic shipped Claude Fable 5 on Tuesday, and the most useful reactions I’ve seen are routing diagrams, not benchmarks.

Fable’s capability and its price, taken together, just made model selection the skill that separates effective AI users from expensive ones. The people getting the most out of the best model available are the ones disciplined enough not to run it by default. They use Fable to plan, orchestrate, and review, then hand the actual work to models that cost a tenth as much.

And with Fable coming off subscription plans on June 23 and a price war forming underneath it, that skill is about to matter for everyone, not just developers.

## The smartest Fable users only use Fable part-time

These two tweets are at the top of my bookmarks this week. Dan McAteer [shared a workflow](https://x.com/daniel_mac8/status/2065066247448821841) for using Fable in Claude Code without immediately hitting plan limits: Set Fable as the orchestrator and let Opus handle the reasoning-heavy phrases. His explanation is the whole story in one line: “Fable is so overpowered that you don’t need its intelligence for every step.” CJ Zafir [went further](https://x.com/cjzafir/status/2065104422762684745), saying he cut his weekly Claude Code limit burn in half by running Fable for planning, OpenAI’s Codex 5.5 for execution, and Fable again for review.

Mitchell Hashimoto put numbers on why. After days of head-to-head testing, [he reported](https://x.com/mitchellh/status/2064773611647574429) that for ordinary “implement this feature” work, Fable, GPT-5.5, and Zhipus’ budget GLM-5.1 produced equally acceptable results – but GLM costs under a dollar and finished in a couple of minutes, GPT-5.5 ran about $1.50, and Fable churned for 40 minutes and cost $9. Then he gave Fable a problem the others couldn’t touch: Optimizing a SwiftUI-layout resolver he’d written in Go. Two hours and $40 later, it had reached a performance level he says he couldn’t hit himself. His verdict: reserve Fable for “targeted, surgical analysis and work,” not daily driving.

(And I say that’s no fun. While Fable is on the subscription, I’m going to use it as much as possible.)

Look at [Morgan Linton’s tweet](https://x.com/morganlinton/status/2064874883298013467) on this benchmark: “Fable low is better than Opus and GPT high. Try it.” Don’t take that as a model review. It’s a routing instruction.

Here’s what Hashimoto found.

![](https://cdn.thenewstack.io/media/2026/06/7af563e1-model_triage_hashimoto_share_graphic_rounded-1024x576.png)

## The economics make triage permanent, not a launch quirk

Fable’s API pricing is $10 per million input tokens and $50 per million output tokens — exactly double Opus 4.8. Inside subscription plans, it counts roughly twice Opus’s usage against your limits. And it’s only included in Pro, Max, Team, and Enterprise plans through June 22. Starting June 23, Fable requires usage credits billed at full API rates. Anthropic says this is about capability and that it intends to restore Fable to subscriptions when it can. Maybe so. But the subscription window looks less like a launch perk than a two-week subsidy for a model Anthropic cannot yet afford to make the default. Frederic Lardinois covered the launch and its unusually short windows for *The New Stack* — [his piece](https://thenewstack.io/anthropic-claude-mythos-fable-5/) is a great rundown of what Fable is and what the catch is.

This is the part Citadel Securities saw coming. Its new [Tokenomics report](https://www.citadelsecurities.com/news-and-insights/global-macro-strategy/tokenomics/) argues that expectations for agentic AI were built around an “unrealistic expectation of frictionless deployments costs,” and points to a divergence already underway: Frontier inference is concentrating among organizations that can justify the spend, while everyone else is shifting toward cheaper models.

The recent decline in Silicon Data’s LLM Expenditure Index may reflect that shift. Silicon Data notes the index can fall when model prices decline, when users choose more efficient models, or when the market moves away from expensive concentration. [A new arXiv study](https://arxiv.org/abs/2604.22750) makes the same point at the task level: Agentic coding can consume 1,000x the tokens of ordinary code chat, identical runs can vary by up to 30x, and more tokens don’t reliably buy more accuracy. That’s model triage showing up in the data, micro and macro.

One aside: I’m not convinced tokens are priced anywhere near the value they create. Hashimoto’s $40 optimizations run would have cost multiples of that in engineering time; by that measure, Fable is underpriced, not overpriced. I don’t have the data to settle it, and I notice the market is currently arguing the opposite. But if frontier tokens are mispriced in both directions — too expensive for routine work, too cheap for surgical work — that makes selection more valuable, not less.

## The price wars make routing hard, not optional

On Wednesday, *The Wall Street Journal* reported that [OpenAI is considering drastic cuts to token prices](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e) — discussions, not decisions yet — to anticipate a battle over users with Anthropic as both companies head toward IPOs. Sam Altman told an enterprise audience this month that token costs have become a “huge issue” and that it’s nearly a meme for a company to burn its annual AI budget in the first quarter; Uber’s CTO said exactly that happened. Chris J. Preimesberger wrote on our site [about the cleanup business](https://thenewstack.io/revenium-ai-cost-observability/) that spending anxiety is already creating.

Cheaper tokens sound like relief, but they don’t remove the selection problem; they multiply it. Every price cut changes the answer to the only question that matters now: Which model should run this? And the volume of these decisions is exploding because the work is moving in loops. Janakiram MSV published the best piece I’ve read on this shift on our site this week: “[Loop engineering](https://thenewstack.io/loop-engineering/),” the practice of designing automated agent workflows instead of prompting directly. Boris Cherny, who leads Claude Code at Anthropic, put it this way: “I don’t prompt Claude anymore. I write loops and the loops do the work.” Read Janakiram’s piece and notice how many of the decisions inside a loop are model choice — which model orchestrates, which executes, which certifies. McAteer’s and Zafir’s workflows are loop engineering with a cost function attached.  
  
Matt Shumer [offered the supervision layer](https://x.com/mattshumer_/status/2065102622604787857): Have a days-long Fable run and append timestamped updates to a persistent HTML page so you can follow along. I tried a version of it this week on a personal project. It works, and changes the feeling of the process. The job has subtly shifted from writing prompts to supervising a small team, in which each model costs different amounts, and someone has to decide who gets the work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)