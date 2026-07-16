*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: Workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

Last week I was camping, reading, and losing a one-sided fight with mosquitoes. This week, the AI news treadmill seemed to be running faster than before. I’m struggling to keep up, and I know I’m not alone.

Grok 4.5 on Wednesday. GPT-5.6 on Thursday. Meta released its first paid model, and Anthropic extended Fable’s access on subscription plans. My honest reaction this week wasn’t excitement. It was fatigue.

I’ve spent 20 years covering product launches, iPhones and the show-floor madness of CES, IFA, and MWC. I know the difference between a real breakthrough cadence and a marketing treadmill, and what we’re on now is the treadmill. The announcement ceremony is becoming too much. Each release arrived as another frontier event, but the breakthrough they all shared was economic: similar work for fewer tokens (and fewer dollars). The models were different. Price was the one argument every lab made. And when the whole frontier competes on price, the companies that spent the most to reach it have the most to lose.

## The new models are different, but the shared pitch is pricing

On Wednesday, Elon Musk’s [SpaceXAI launched Grok 4.5](https://thenewstack.io/grok-45-opus-killer-launch/), its first model since the company went public and swallowed the coding startup Cursor. A day later, OpenAI [moved GPT-5.6 to general availability](https://openai.com/index/gpt-5-6/), with a model family arrangement similar to Anthropic’s: Sol at the top, Terra in the middle, Luna at the bottom. Not to be forgotten, Meta shipped its [first-ever paid model](https://thenewstack.io/meta-muse-spark-api) in the same window.

These are not the same type of models. OpenAI led with new frontier benchmarks. Musk called Grok 4.5 xAI’s smartest model yet. Meta Pitched Muse Spark as a coding and agentic system with a broad multimodal range. The capabilities are different. But scan the launch copy, and one argument shows up in all of them: price. OpenAI sold GPT-5.6 on “more intelligence from every token” and bragged that Luna beats Anthropic’s Opus 4.6 at roughly a quarter of the cost. Musk pitched Grok as Opus-class, “but faster, more token-efficient and lower cost.” [Sam Altman went on CNBC](https://www.cnbc.com/2026/07/09/open-ai-sam-altman-chatgpt-5-6-sol.html) and led with a number that had nothing to do with intelligence: Sol is 54% more token-efficient on agentic coding, because “every enterprise now is thinking about spend.”

That’s a different pitch than the one we got until the last few months, when a new frontier model reset what was possible, and price was an afterthought. The engineering is real. The one breakthrough every lab put in its headline this week was the bill. These companies are clearly responding to recent headlines that AI might not be providing a significant enough return on investment.

## The race to the bottom is aimed at the racers

Laid out, this week shows what’s really happening.

Frontier models by price, July 8-10, 2026

| Model | Price (in / out) | Pricing position |
| --- | --- | --- |
| **GPT-5.6 Luna**OpenAI | $1 / $6 | Low-cost OpenAI tier |
| **Muse Spark 1.1**Meta | $1.25 / $4.25 | Meta’s aggressive entry |
| **Grok 4.5**SpaceXAI | $2 / $6 | Opus-class claim at flash-model pricing |
| **GPT-5.6 Sol**OpenAI | $5 / $30 | OpenAI flagship |
| **Claude Opus 4.8**Anthropic | $5 / $25 | Anthropic flagship |
| **Claude Fable 5**Anthropic | $10 / $50 | Premium coding tier |

Published API pricing, per 1M tokens (input / output), as of July 10, 2026.

Meta is the clearest signal because Meta used to give its models away. This week it started charging for the first time, and our own Amanda Caswell caught the way Mark Zuckerberg framed it: Muse Spark 1.1 runs about a quarter of what OpenAI and Anthropic charge for their top-tier models, and “the pricing from some of the other labs is very extreme and has very high margins.” This is a frontier CEO on the record attacking his rivals’ margins. That’s not a product launch. This is a price war.

So who’s paying for all this? Someone has to absorb the economics behind the widening gap between $50-per-million Fable output and $6-per-million Grok output. For now, the customer is benefiting. The scale is visible in SpaceXAI’s infrastructure business alone: Google is the latest to pay Space for compute, [agreeing to pay  $920 million a month](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) beginning in October for access to roughly 110,000 GPUs and related compute.

Investors are asking a similar question. Meta shares [fell after its April earnings](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/), when the company raised its 2026 capex forecast to $145 billion. This week [the stock rose](https://invezz.com/za/news/2026/07/09/meta-stock-rises-as-ai-chip-plans-and-muse-spark-11-rollout-take-focus/) after Muse Space and Meta’s emerging API and infrastructure business gave investors a clearer glimpse of how that spending might pay off. The *Wall Street Journal* [reported OpenAI is weighing](https://www.cnbc.com/2026/06/11/openai-mulls-slashing-prices-ahead-of-competition-from-anthropic-wsj.html) “drastic” token-pricing cuts to fight Anthropic as both companies prepare for the possibility of an initial private offering. [Altman himself said](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-ceo-sam-altman-admits-ai-token-costs-are-becoming-a-huge-issue-company-seeks-improved-value-as-overspending-becomes-a-meme) burning your annual AI budget in the first quarter is “nearly a meme.”

This isn’t a market crash. But a company that keeps cutting the price of what it spent billions to build isn’t necessarily winning. It may simply be running a race it cannot afford to stop.

Anthropic seems to be making the opposite bet: Fable 5, its best coding model, now costs $10 per million input tokens and $50 per million output tokens, double Opus and the most expensive model it has ever listed. The floor is dropping toward a dollar, and the ceiling is rising past fifty. The middle is getting squeezed.

## The advantage belongs to whoever can switch

The price war is good for buyers, but only when they can move between models. A $1 model isn’t cheap if an agent burns through five times the tokens, retries failed tasks, and hands off work to a half-dozen other agents. As Amanda Caswell laid out on TNS, [a single agentic task can run 150,000 to 200,000 tokens](https://thenewstack.io/agentic-ai-token-costs/), up to a thousand times as much as a plain chat costs. I pointed to [the same lesson](https://thenewstack.io/claude-fable-cost-model-triage/) a few weeks back: In one head-to-head test, a job that cost $1.50 on GPT-5.5 ran $9 on Fable.

A $50 model can still be the economical one when it solves an expensive problem in a single pass. The unit that matters is no longer price per toke. It’s the price per finished task.

That changes the skill from finding the best model to building a model portfolio. Route volume work to cheap models. Pay for premium reasoning where your own testing shows it earns its price. Keep one open-weight option for the sensitive, high-volume, or continuity-critical jobs. And keep your prompts, context, and workflow portable so that switching between models isn’t a full rewrite.

The labs are telling us not to get loyal. OpenAI shipped three price-performance tiers at once, and Meta entered by undercutting incumbents. Meanwhile, SpaceXAI’s entire pitch is that it does comparable work with fewer tokens. And Anthropic is betting that coding work is worth a premium.

These are not four versions of the same business model. They’re an invitation to route work among them.

It’s too early to call a winner in this price war. Labs will continue to release models that leapfrog one another in pricing, capabilities, and reasoning.

So I’ll keep reminding you not to become a fanboy.

The best models will keep changing. The durable advantage belongs to the people and organizations that can change with it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)