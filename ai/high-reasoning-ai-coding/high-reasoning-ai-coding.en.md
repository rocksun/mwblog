**Ask an AI model what comes next after “bacon-double”**, and the return is fairly unanimously “cheeseburger.” It’s a pattern-matched, single-pass output for the user, and it’s the one that we expect.

Above digital burger joint simplicity, we enter the world of high-reasoning, where multi-step problem-solving sees models execute [chain-of-thought processes](https://www.ibm.com/think/topics/chain-of-thoughts).

Going beyond a single pass is more akin to human reasoning, as it breaks down elaborate problems into more manageable, sequentially executed intermediate steps (with backtracks on errors) to provide an answer.

![](https://cdn.thenewstack.io/media/2026/07/2fbec2c1-screenshot-2026-07-21-at-13.09.56.png)

*OpenAI*

The [trade-off is a higher volume](https://thenewstack.io/gpt-5s-enhanced-reasoning-comes-with-a-steep-hidden-cost/) of more complex code, which is harder to detect errors in at code review, but the model itself will typically perform better.

The question now becomes, when do we introduce (or perhaps even insist upon) high reasoning as part of the frontier model mix, and is it the next chasm to cross?

## Relegating single pass to the simple end of the workload

[CloudBees](https://tracking.us.nylas.com/l/ce4f024bd5de4b2fb296222148eda1d8/0/d18384216df65cf934d912d6b5a95488d54b80f858d443a7a0aa0510020568d8?cache_buster=1784122535)‘ CEO [Moritz Plassnig](https://tracking.us.nylas.com/l/ce4f024bd5de4b2fb296222148eda1d8/1/ae2830a51c7316d11f1ac47df7182b9fe8f44df786df91cc7049ea17ae17e780?cache_buster=1784122535) tells *The New Stack* that single-pass AI coding is like “answering with the first thing that comes to mind” in the reasoning debate. That means it’s fine for simple problems, but not for ones with real depth or ambiguity.

> Single-pass AI coding is like “answering with the first thing that comes to mind.”

“I don’t think single-pass is dead, but I do think it’ll be relegated to the simpler end of the workload,” Plassnig says. “What’s more interesting is teams routing work intelligently: lower-end models for boilerplate [routine predictable] tasks, but high-reasoning for anything architecturally complex or security-critical, rather than just treating ‘more reasoning’ as a universal upgrade.”

Plassnig confirms that he fully expects the “current trajectory of developers demanding more high-reasoning to evolve into the harness itself”, before those same software engineers then being happy to choose the right model for the task at hand.

> “What’s interesting is teams routing work intelligently: rather than just treating ‘more reasoning’ as a universal upgrade.”

## Sometimes the first response is the right one

General manager of ‘[The Shop](https://www.teamsparq.com/insights/sparq-opens-the-shop/)’ (a practical use case company division) at AI software operations engineering company [Sparq](https://www.teamsparq.com/), [Jackson Stakeman,](http://linkedin.com/in/jackson-stakeman) tells *The New Stack* that he’s somewhat (but not wholly) in consensus with CloudBees CEO Plassnig’s thoughts. Rather than defining single-pass AI coding as blurting the first thing that comes to mind, he defines it as “responding when you think you actually have something of value to add” to a query.

He reminds us that single-pass blurt or not, sometimes the first response is the right one, so pretending otherwise just adds cost and latency to problems that didn’t need it.

“That said, I agree that routing work intelligently beats treating more reasoning as a universal upgrade — I’d just frame where we are a bit differently,” Stakeman says. “We’re still early in AI adoption at enterprise scale. The simple workloads are the thick part of the bell curve, and the complex multi-agent orchestration tasks are the long tail. For companies that aren’t primarily technology businesses, but that use technology to drive value, what they mostly need from AI is for it to work.”

> “We’re still early in AI adoption at enterprise scale. The simple workloads are the thick part of the bell curve, and the complex multi-agent orchestration tasks are the long tail.”

## The catch is that the model becomes a black box

In his essentially practical, hands-on role, Stakeman underlines the fact that high-reasoning tools let organizations that never built strong prompt engineering skills skip that step, for a price.

“The catch is that the model becomes a black box,” he warns. “It might solve your problem, but it won’t tell you whether a custom orchestration would have solved it better. In the conversations we’re having with customers, it’s rare to hear about a custom LangChain-style build that’s actually kept pace with how fast the frontier models keep improving.”

He restates his view that frontier model labs seem to be moving faster than most in-house stacks can keep up. It’s a development that’s starting to force a financial conversation that’s only just getting going: real skepticism about whether the premium on models like GPT-5.6 Sol or Fable 5 are worth it for a given task.

As of now, [OpenAI appears to talk](https://openai.com/index/gpt-5-6/) more directly about “medium, max, and scientific” reasoning, rather than high reasoning, even in relation to GPT-5.6 Sol. In a somewhat similar vein, [Anthropic talks about chain-of-thought faithfulness](https://www.anthropic.com/research/reasoning-models-dont-say-think) when discussing why reasoning models don’t always say what they think.

“In our view, the deciding factor isn’t really the model; it’s whether a team has a clear way to measure ROI on AI spend. Teams with that mechanism can experiment and compare a cheap, fast model against a high-reasoning one, task by task. Teams without it tend to default to whatever’s marketed as ‘best’, and those are exactly the teams most likely to get steered away from high-reasoning the moment the bill comes due. Not because it’s the wrong tool, but because they can’t prove it is the right one,” Stakeman clarifies.

## High reasoning is not rocket science, or FrontierMath

By way of clarification, high reasoning is not the same as FrontierMath, but there is a degree of overlap between these two occasionally connected cousins.

OpenAI commissioned Epoch AI to produce 300 math questions for the FrontierMath benchmark, which [the nonadvocacy research nonprofit confirmed](https://epoch.ai/latest/openai-and-frontiermath) at the start of 2025. In terms of use, FrontierMath can act as a benchmark for evaluating advanced mathematical reasoning in AI of the type that features high reasoning.

What do developers think of high-reasoning? It might still be early days; there’s precious little ascerbic commentary out there just now.

That may be down to the still-emerging nature of these functions, or it could be because “high-reasoning” is sometimes used to describe [governmental policymaking](https://news.ycombinator.com/item?id=31072931) and even [Machiavellianism](https://www.psypost.org/evil-geniuses-people-high-in-machiavellianism-may-have-superior-reasoning-abilities/).

What (arguably) matters most in the immediate months (and yes, this is AI, so it could be weeks or days) ahead is how well enterprise organizations are able to assess any given AI tool for its worth. That measure of worthiness comes down to correctness and effectiveness, multiplied by cost and divided by its ability to integrate and orchestrate before it attempts to accelerate and (dare we even say the word?) innovate.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)