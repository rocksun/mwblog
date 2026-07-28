Google on Tuesday launched three new Gemini models: Gemini 3.6 Flash, a cheaper and faster 3.5 Flash-Lite, and 3.5 Flash Cyber, a model optimized for cybersecurity use cases that generally outperforms [Anthropic’s 4.6 Opus](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) model.

What is sorely missing in this lineup, and now weeks past its promised launch date, is 3.5 Pro, Google’s latest flagship model. Google first announced 3.5 Pro at its I/O conference in May with the promise of launching it in June. Google says the Pro model is “currently in testing with partners” and that it plans to make it broadly available “as soon as it’s ready.”

Never one not to look ahead, Google also says that it has started its pre-training run for Gemini 4.

## 3.6 Flash

Most of us didn’t expect to see an update to the Gemini Flash model before the Gemini 3.5 Pro model, but here we are.

The good news is that 3.6 Flash is a meaningful update to its predecessor — and it’s a bit cheaper. The input price per million tokens remains at $1.50, but Google reduces the price per million output tokens from $9 to $7.50.

> Most of us didn’t expect to see an update to the Gemini Flash model before the Gemini 3.5 Pro model, but here we are.

Google also specifically notes that 3.6 Flash takes fewer reasoning steps and tool calls to achieve its goals in agentic workflows, which should also make it more cost-effective to run. According to Artificial Analysis, it uses 17% fewer tokens.

## 3.6 Flash Benchmarks

In most benchmarks, 3.6 Flash easily surpasses its predecessor, especially when it comes to coding. On the new [DeepSWE software engineering benchmark](https://deepswe.datacurve.ai), 3.6 Flash scores 49% vs [3.5 Flash](https://thenewstack.io/googles-gemini-3-5-flash-beats-the-frontier-models/)‘s 37%, for example. That’s not the greatest result, though. [Anthropic’s Claude Sonnet 5](https://thenewstack.io/claude-sonnet-5-launch/) gets to 54% here, with the top-end frontier models scoring over 70%.

The team also saw large gains in the MLE Bench machine learning research benchmark (63.9% vs 49.7%) and the [OSWorld-Verified](https://benchlm.ai/benchmarks/osWorldVerified) computer use test (83% vs. 78.4%). Most modern models score in a similar range here, which is actually quite impressive for a mid-range model like 3.6 Flash. Claude Fable, in comparison, does only slightly better at 85%.

![](https://cdn.thenewstack.io/media/2026/07/830ad80f-screenshot-2026-07-21-at-8.32.12-am-1024x548.png)

Credit: Google.

For knowledge work, 3.6 Flash hits 1421 on [GDPval-AA v2](https://artificialanalysis.ai/evaluations/gdpval-aa), which is much better than 3.5 Flash at 1349, but at this point, that’s well below other frontier labs’ mid-range models like Anthropic’s Claude Sonnet 5 (at 1600) and Open’s GPT-5.6 Terra at 1581.

What’s important to remember here, of course, is that Google is also competing on price, but even there, the picture is complicated. 3.6 Flash doesn’t always outperform [GPT 5.6 Luna](https://thenewstack.io/openai-gpt-56-live/), for example, and that’s available for $1/$6 per million input/output tokens (but only as long as the context window is under 272,000 tokens). Anthropic’s Sonnet 5 is available for an introductory price of $2/$10 until the end of August, too.

## 3.6 Flash and 3.5 Flash Lite availability

3.6 Flash and 3.5 Flash Lite are now available in the Gemini API via Google AI Studio and Android Studio, while 3.6 Flash is also available in [Google’s Antigravity agentic coding tool](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/) and for enterprise users in the Gemini Enterprise Agent Platform (previously known as Vertex AI).

For consumers, 3.5 Flash-Lite is coming to Google Search.

## 3.5 Flash-Lite

3.5 Flash-Lite is Google’s newest low-end model. Given that 3.1 Flash Lite, the most recent ‘lite’ release, is [almost half a year old](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/), it’s no surprise that 3.5 Flash shows an improvement across the board. But it’s also a bit more expensive, at $0.3/$2.5 per million input/output tokens (up from $0.25/$1.5).

In terms of benchmarks, it’s not going to break any records, but that isn’t the purpose of this model either. It’s meant for high-throughput tasks like agentic search and document processing, not for tasks where reasoning and planning agentic workloads are key.

That said, it is a significantly better model than 3.1 Flash Lite, though. On GDPval-AA v2, it scores 1140 compared to the previous lite models’ 642. SWE-Bench Pro numbers go up from 49.6% to 54.2%, and on OSWorld-Verified, it hits 74% now.

For many companies, it will land in a sweet spot for latency-sensitive workloads, as Ramp’s head of applied AI Veeral Patel notes. “Gemini 3.5 Flash-Lite landed on the Pareto frontier in our receipt extraction benchmark, offering one of the best tradeoffs we’ve tested between accuracy, latency, and cost,” he writes in today’s announcement. “That combination is critical at Ramp, where we need to process receipts quickly and reliably at scale.”

## 3.5 Flash Cyber: same price, limited access

With Gemini 3.5 Flash Cyber, Google is getting deeper into using AI for cybersecurity use cases — without risking any [Fable 5-like fallout](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/).

As Google notes, today’s “AI models have become capable of finding security vulnerabilities faster than current systems can fix them. The company built 3.5 Flash Cyber on top of the regular 3.5 Flash model and is charging the same for it, too, which gives Google the ability to claim that it “offers a cost-efficient and highly capable alternative to large, costly cybersecurity models.”

But you won’t be able to get your hands on the Cyber model just yet. It is only available in a limited-access pilot exclusively for governments and trusted partners, and only in Google’s own CodeMender tool. The plan is to expand access over time.

It seems unlikely that 3.5 Flash Cyber is at the level of an [Anthropic Mythos](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) when it comes to finding and exploiting software vulnerabilities, but this goes to show how nervous frontier labs now are about rolling out these models. “This will give frontline defenders a head start in finding and fixing critical vulnerabilities before they can be exploited, while mitigating against broader misuse,” Google notes.

Meanwhile, many Chinese open-source models like [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/) are probably at the same level as 3.5 Flash Cyber.

Google says it performs at the level of Opus 4.6 and notes that “more recent competitor models perform less well than Claude Opus 4.6 because of guardrails.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)