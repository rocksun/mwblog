This week, Sakana AI released [Fugu](https://sakana.ai/fugu-release/), a multi-agent orchestration system designed to deliver frontier-model performance all while reducing the risks of relying on a single provider.

The Japanese AI R&D company says Fugu performs as well as Anthropic’s [Fable 5](https://thenewstack.io/fable-5-opus-comparison/) and Mythos Preview on engineering, scientific, and reasoning benchmarks by breaking up tasks into subtasks and strategically routing them across a swappable pool of expert agents. But early reactions are mixed.

While Sakana positions Fugu’s “collective intelligence” as the blueprint for AI sovereignty, not all users report frontier-model-level performance. Others note fast burn rates and unnecessarily high prices.

Many agree that, though interesting, Fugu likely won’t be the hero to AI sovereignty it hopes to be.

## Is this just another router? Not really.

Sakana says Fugu’s internal routing logic is founded on its own research in learned model orchestration, specifically noting two papers, [Trinity](https://sakana.ai/trinity/) and the [Conductor](https://sakana.ai/learning-to-orchestrate/).

Unlike multi-model routers, such as OpenRouter Fusion, that send a prompt to multiple models and then compare or combine the results, Fugu breaks down user prompts into subtasks and determines which subtask to send to which model. In this way, Fugu “dynamically orchestrates the world’s best models to tackle complex, multi-step tasks,” so Sakana says.

> From the outside, you just see what looks like one model, accessible via a single OpenAI-compatible API.

But what the AI company doesn’t tell you is how it decides which tasks get routed where; that information is proprietary. From the outside, you just see what looks like one model, accessible via a single OpenAI-compatible API.

> “relying on a single company’s model for national infrastructure is a massive risk. As recent export controls have shown, access to top models can disappear overnight.”

Fugu doesn’t have to farm out every task, though. It’s a language model itself, specialized for model selection, delegation, verification, and synthesis internally, so it can also solve requests directly when its own response is sufficient.

## A hero for AI sovereignty, it appears not

In an [X post](https://x.com/hardmaru/status/2068884466056225025), Sakana CEO and co-founder [David Ha](https://www.linkedin.com/posts/hardmaru_sakana-ai-activity-7097940478557384704-AsqW) writes, “relying on a single company’s model for national infrastructure is a massive risk. As recent export controls have shown, access to top models can disappear overnight.”

That “massive risk” comment is likely a jab at [what happened to Anthropic](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/?utm_source=chatgpt.com), when an export control directive forced the AI company to pull Fable 5 and Mythos 5 just three days after launch.

***See also: [Fable 5 ban: 4 open models responded before Anthropic could restore access](https://thenewstack.io/fable-ban-open-weights/)***

Following this news, Sakana positions Fugu as the antidote to single-provider reliance. Because it relies on a pool of “entirely swappable agents,” the idea is that Fugu is less likely to leave users in a bind if one provider suddenly restricts access. It can simply route work to other models.

The AI company considers this capability enough license to claim it’s “delivering the realistic, resilient blueprint required for AI sovereignty.” But some initial reactions call that hyperbolic:

“This is just a highly advanced router/wrapper, not a fundamental leap like Mythos/Fable was,” argues one [Redditor](https://www.reddit.com/r/singularity/comments/1ucassf/japanese_ai_firm_sakana_ai_release_fugu_a_model/).

Though it’s likely not fair to call Fugu a simple multi-model router, its ultimate reliance on other models means it’s not the hero for AI sovereignty it aspires to be. After all, if more than one model provider restricts access at the same time, Fugu’s capabilities also take a hit.

As another user writes on [HackerNews](https://news.ycombinator.com/item?id=48624782): “As a developer outside the US I think it’s vital to have alternatives to OpenAI and Anthropic, but sadly this is not it,” calling out what they describe as the tool’s unfortunate price-to-burn-rate ratio, an “extremely slow” API, and poor quality in comparison to Fable:

“It’s nowhere remotely near usable as a day-to-day workhorse.”

## Not all user reviews back up the benchmarks

Sakana points to coding, reasoning, science, and agent benchmarks to prove Fugu’s value, stating its tool consistently beats Gemini 3.1, Opus 4.8, and GPT 5.5.

![](https://cdn.thenewstack.io/media/2026/06/02d2078d-image-1024x593.png)

Source: Sakana AI

It also highlights what it says is the success of its beta program, where almost 500 early users tested Fugu on lengthy, multi-step computational workflows.

In particular, it claims that one cybersecurity engineer confirmed Fugu successfully operated within parameters and avoided destructive actions, while other teams praised Fugu Ultra for besting GPT 5.5 in code review and maintaining an “unusually strong persona stability across long sessions.”

But moving from benchmarks and PR-ready examples to early community sentiment adds more color to the story.

One user on HackerNews calls Fugu “quite strong” for a few agentic coding tasks, but notes they weren’t able to do many deep reviews before their quota ran out, adding: “For implementation I found it weaker, it made a few mistakes that I haven’t seen frontier models make in a long time.”

A Redditor had a different experience. They, too, bemoan burn rate issues, but note: “It caught things Opus 4.8 ultra and codex 5.5xhigh clearly missed in a fairly large data ingestion / processing project.”

## Some users question the price tag

Furu is generally available today in most regions (save the EU) in two tiers: a low-latency model that integrates with chatbots and tools like Codex for daily tasks and Fugu Ultra, the heavy-hitter that coordinates a deeper pool of experts for more complex, high-stakes tasks. (This is the one that’s supposed to rival Fable 5 and Mythos Preview.)

Subscription plans are available at $20, $100, and $200 monthly rates for both Fugu and Fugu Ultra. Pay-as-you-go pricing is also available, with Fugu billed at standard rates per underlying model, and Fugu Ultra running at $5 per million input tokens and $30 per million output tokens, with higher rates when context exceeds 272k.

Several early users on Reddit and HackerNews deem these price tags too high, especially when they’re experiencing what now feels like the soundtrack of new agent tools: burn rates that get away from you too fast.

As one HackerNews user jabs: “I love when they put a black box in front of the other black boxes so I can get a questionably better black box for slower service and more money!”

## Is collective intelligence the future?

On X, HA posits that large-scale, monolithic models have had their time in the sun and that solving more complex real-world challenges will require a different beast: collective intelligence.

Moving forward, Sakana plans to incorporate new models in its agent pool, which could shore up that resilience Sakana is aiming for. But so far, users seem to question whether paying another company to sit between them and frontier models is really worth the spend.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)