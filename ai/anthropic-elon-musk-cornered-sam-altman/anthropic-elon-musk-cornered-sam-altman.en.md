*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

The AI race used to be about who had the best model. This week, it looked more like a fight over power plants, data centers, and who gets access to the GPUs first. Anthropic’s new SpaceX deal doubled Claude Code’s power-user limits, but that’s the small story. The bigger story is that Anthropic [just rented the full computing power](https://thenewstack.io/anthropic-spacex-claude-limits/) of Elon Musk’s Colossus 1 facility in Memphis. Meanwhile, Musk and Sam Altman were in federal court this week, where Musk is trying to unwind OpenAI’s transformation into a for-profit company.

Let’s remember the larger picture: Elon Musk co-founded OpenAI with Sam Altman, and Anthropic’s CEO, Dario Amodei, was a very early employee at OpenAI as its VP of Research. Both Musk and Amodei split from OpenAI, built rival labs, and traded public criticism themselves. Now they’re partnered on a common cause plaguing every frontier AI company, including OpenAI: compute. ​

As Alex Wilhelm writes in *Cautious Optimism* this week, [I thought Elon hated Anthropic](https://www.cautiousoptimism.news/i-thought-elon-hated-anthropic/). Maybe he does, but it’s also possible Musk hates Altman even more because on Wednesday, he rented Anthropic all the compute capacity at the facility he built for xAI to train Grok.

Musk and Altman’s trial is the show. The SpaceX deal is the move.

## The Anthropic/SpaceX deal exposed the new moat

If you want a play-by-play – the new rate limits, the 220,000-GPU specs, what developers are saying – Meredith Shubel has [the definitive read](https://thenewstack.io/anthropic-spacex-claude-limits/) on our site. I want to talk about what the deal means, because the rate-limit story is small in comparison.

I run Claude Cowork sessions most days, and recently, I’ve been hitting limits in the early afternoon (which forces me to take a lunch). The fix was never going to be a throttle tweak. The fix was always going to be capacity. Anthropic’s Colossus 1 deal grants them [access to the whole facility](https://x.com/eliebakouch/status/2052066609896808473) — over 300 megawatts and 220,000-plus NVIDIA GPUs. Stack it on top of their other recent compute deals, and Anthropic now has, by [Aakash Gupta’s math](https://x.com/aakashgupta/status/2052072411894563142), roughly 15 gigawatts of committed capacity, the equivalent of 11 million homes’ worth of power, queued up to run Claude. And buried in the same announcement is the line worth circling: Anthropic said it has “expressed interest” in partnering with SpaceX to develop multiple gigawatts of orbital AI compute capacity.

The right way to read all of this is simple: compute velocity is the story. Anthropic’s annualized revenue went from $9 billion at the end of 2025 to [more than $30 billion by April](https://www.bloomberg.com/news/articles/2026-04-06/broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic), and [Axios called it the fastest revenue ramp](https://www.axios.com/2026/04/13/anthropic-revenue-growth-ai) in American business history. Remember Anthropic’s March? Constant product launches along with constant outages. Tuesday’s deal cost Anthropic a partnership with the guy who had been publicly mocking Dario’s writing on AI consciousness eight weeks ago. That should tell you that compute outranks everything else right now.

## Dario and Elon just picked the same side

For comic relief, the Musk v. Altman trial in Oakland delivered all week. [A 2017 email surfaced in court](https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/) in which Musk told a Tesla VP, referring to OpenAI’s leadership: “The OpenAI guys are gonna want to kill me, but it had to be done.” Brockman [testified he thought Musk was about to physically attack him during the 2018 power struggle](https://www.nbcnews.com/tech/elon-musk/openai-co-founder-says-feared-musk-physically-attack-rcna343736). Musk [appeared to acknowledge on the stand](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/) that xAI used OpenAI’s models through distillation. And Musk [texted Brockman about settling two days before the opening arguments](https://techcrunch.com/2026/05/04/elon-musk-sent-ominous-texts-to-greg-brockman-sam-altman-after-asking-for-a-settlement-openai-claims/). I cannot stop thinking about that last one. It’s the most Elon thing he’s ever done, which is saying something.

The fun part is what’s happening underneath the fight. Elon co-founded OpenAI and walked off the board in 2018 after losing a power struggle with Sam Altman. Dario was OpenAI’s head of research and left in 2021 to start Anthropic. The two of them have gone on to build the best-funded rivals to Sam’s company. The three of them have spent years criticizing each other in public. Remember when Sam and Dario stood next to each other awkwardly at a major event in India? And Elon had strong words about Dario during Anthropics’ fight with the DoW. But this week, all that is in the past, as Anthropic became the marquee customer for Musk’s massive data center.

This deal isn’t a one-off. Three weeks ago, [Cursor announced it was training](https://cursor.com/blog/spacex-model-training) its Composer models on xAI’s Colossus infrastructure, citing the same “bottlenecked by compute” problem Anthropic is now describing. I wrote about [Cursor’s $60 billion bet the week after](https://thenewstack.io/cursor-sdk-harness/): SpaceX has either a $10 billion payment due to Cursor or a $60 billion acquisition option on the company by year-end. Stack Cursor and Anthropic together, throw in orbital compute ambitions, and SpaceX is clearly positioning itself as the compute layer.

## The memes get it

## Claude’s dreaming agents need 15 gigawatts

Look at Anthropic’s product roadmap to understand why the company locked down Colossus and is talking about space-based data centers. On Wednesday, the same day the Colossus deal was announced, [we reported that Anthropic is expanding Managed Agents](https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/) with three new capabilities: dreaming, outcomes-based evaluation, and multi-agent orchestration. Frederic Lardinois has been all over the story, and the piece is worth your time.

“Dreaming” is the headline feature. It’s a scheduled background process where Claude reviews recent work, looks for patterns across sessions, and writes those observations into its memory. The company says it’s modeled on how the human brain consolidates during sleep. “Together, memory and dreaming form a robust memory system for self-improving agents,” Anthropic told Frederic. The outcomes feature lets you tell an agent what “good” looks like and uses a separate grader agent – its own context window, no cheating – to check the work. Anthropic says outcomes alone improved task success by up to 10 points in their internal testing. Multi-agent orchestration lets a lead agent break down a job and assign subagents to work in parallel.

The three new features speak to the SpaceX deal. Every one of them multiplies compute consumption during the task. Dreaming is a continuous background workload that runs even when you aren’t asking the agent anything. Outcomes add a second graded inference loop on top of the first. Multi-agent orchestration is, by definition, the simultaneous execution of multiple agents. This is the same pattern across the whole industry – agents do their best work when they have more time to think, more attempts to grade, and more peers to consult. The frontier labs are moving beyond selling just tokens to selling sustained, parallel, ambient cognition. And that requires a lot of megawatts.

Right now, most users are focused on the AI model, and for good reason. But the megawatts are what determine who gets to use it, how often, and at what price. That’s why this deal matters. Anthropic did not just buy relief from rate limits, but rather bought more room for agentic capacity and ambient features.

Compute is the limiting factor facing AI power users. We’re early in the age of AI. The tools are going to keep getting better, which likely means each task will require more compute, not less. Anthropic is trying to provide what heavy users want: no limits. This deal is a big step toward that reality.

The open question is who pays. Public estimates put Anthropic’s Colossus lease at billions a year, and the bills are already steep on the user end. On *Towards Data Science* last week, [Ida Silfverskiöld broke down agentic token costs](https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/) and found that an unoptimized agent running 100 messages a day can hit roughly $2,490 a month on Claude Opus 4.6 — about 25x what the same agent costs once it’s tuned. The math gets harder once agents start dreaming and orchestrating each other in the background. Someone has to cover those megawatts. Whether that’s the labs eating margin, enterprises absorbing higher contracts, or individuals watching their bills climb is the part of this story I’d be paying closest attention to from here.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)