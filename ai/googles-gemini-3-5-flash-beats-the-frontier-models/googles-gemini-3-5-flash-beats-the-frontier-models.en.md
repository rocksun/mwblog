At its I/O developer conference, Google on Tuesday unveiled two new AI models: [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/#gemini-3-5-flash), the newest model in its Gemini series, and Gemini Omni Flash, a new multimodal model that can “create anything from any input,” as Google puts it.

## Gemini 3.5 Flash

Gemini 3.5 Flash is the first model in the Gemini 3.5 series. A Pro version is still in the works and should launch next month, but even 3.5 Flash bests the existing 3.1 Pro model in most benchmarks.

In [TerminalBench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1), for example, 3.1 Pro currently scores 70.3% when using the Gemini CLI to solve coding problems, while 3.5 Flash scores 76.2%.

That’s not quite up there with OpenAI’s GPT 5.5, but for a Flash model, that’s a very solid performance.

The new Flash model gets similar results that outperform 3.1 Pro in other benchmarks, including GDPval-AA (1656 Elo vs 1314), MCP Atlas (83.6% vs 78.2%), and CharXiv reasoning (84.2%).

![](https://cdn.thenewstack.io/media/2026/05/77119212-gemini-3-5__benchmarks__dark-1024x767.jpg)

Gemini 3.5 Flash benchmarks. Credit: Google.

But what is maybe even more interesting is that it is competitive — and sometimes even beats — flagship models like OpenAI’s GPT-5.5 and Anthropic’s Opus 4.7 in quite a few benchmarks, too.

That’s especially true for tool usage benchmarks, and as Google CEO Sundar Pichai noted in a press briefing ahead of today’s launch, Gemini 3.5 Flash is “a first in a series of models combining frontier intelligence with actions.”

He noted that Flash is close to the best frontier models, but also very fast. Artificial Analysis puts it just behind the frontier models of OpenAI and Anthropic, but at significantly faster token per second speeds (close to 280 tokens per second vs. around 60 or 70 for GPT-5.5 and Opus 4.7).

“What’s amazing about Flash is how it delivers frontier-level capabilities at less than half the price, in some cases almost a third of the price of comparable frontier models,” Pichai noted.

Google notes that 3.5 Flash is especially strong when it comes to running long-horizon agentic tasks, including agentic coding. That’s also why this model is at the core of Gemini Spark, the new personal AI agent Google is launching at I/O (and which is currently only available to trusted testers).

Given the capabilities of the Flash model, the Pro model will likely be at least as capable as comparable models from OpenAI and Anthropic — and likely best them in at least some benchmarks.

## Gemini 3.5 Flash availability

Gemini 3.5 Flash is now available via the Gemini API in Google AI Studio and Android Studio, Gemini Enterprise Agent Platform (aka [Vertex AI](https://thenewstack.io/google-gemini-agent-platform/)), and Gemini Enterprise, as well as in Google Antigravity.

For consumers, it is also available in the Gemini app and AI Mode in Google Search.

![Gemini Omni Flash, Google I/O, May 19, 2026](https://cdn.thenewstack.io/media/2026/05/c838ae3b-screenshot-2026-05-19-at-13.30.31-1024x660.png)

Credit: *The New Stack*

## Gemini Omni

Gemini Omni is a bit of a different model. The Gemini models were, to some degree, always meant to be multimodal, but Omni takes this quite a bit further. In its current iteration, it’s a bit more like Veo, Google’s generative model for creating videos, but over time, it will also support images and audio.

So even though Google says Omni can “create anything from any input,” it is starting with only video for now. That has proven to be an area where there has been a lot of progress in the last year or so, and Omni brings many of the capabilities of what users now expect from image models to video.

Omni, which, like Gemini 3.5 is only launching with a Flash model for now, lets users change specific things in a video, for example, and completely reimagine a shot by adding new characters and objects, or changing the environment, angle, and style. Google says it can do this “without ever losing the thread of your original scene.”

As Google stresses (and other frontier labs tend to argue the same about their video models), Omni’s world model has an ‘intuitive’ understanding of gravity, kinetic energy, and fluid dynamics, which should make for realistic scenes.

Because it is multimodal (or will be soon), Omni can take images, text, video, and audio (or any combination of those) as its input to build the final scene.

![](https://cdn.thenewstack.io/media/2026/05/639626ea-rt_wm_omni__sizzle__sailor__260517.gif)

Created with Gemini Omni. Credit: Google.

## A digital avatar for your safety (and those around you)

Generative video lends itself to deepfakes and misinformation campaigns. Google says it is “committed to developing AI responsibly and we have clear policies to protect users from harm and governing the use of our AI tools.” In practice, this means you can currently create videos with your own voice and an avatar of your likeness.

“Beyond the avatar feature, in terms of editing videos to change audio and speech, we are still working to test this and better understand how we can bring this capability to users responsibly,” Google says.

All videos created with Gemini Omni will include Google’s SynthID watermark.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)