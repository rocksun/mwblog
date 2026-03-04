Two weeks after launching [Gemini 3.1 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/), its most capable AI model yet, Google on Tuesday [launched](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/) Gemini 3.1 Flash-Lite, the fastest model in the Gemini 3 family so far. At $0.25/$1.50 per million input/output tokens, it’s also Google’s most affordable Gemini 3 model yet.

The model is meant for what Google describes as “high-volume developer workloads at scale” and is now available in preview in the Gemini API in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview) and [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal?mode=prompt&model=gemini-3.1-flash-lite-preview). It won’t be available in the Gemini consumer app.

## Benchmarks

Compared to Gemini 2.5 Flash-Lite, the last model in Google’s family of Flash-Lite models, the new version is significantly more expensive (up from $0.10/$0.40), but also far more capable.

In terms of benchmarks, it generally outperforms Gemini 2.5 Flash, which remains popular among developers, and does so at a lower price.

![Gemini 3.1 Flash-Lite benchmarks (credit: Google).](https://cdn.thenewstack.io/media/2026/03/3debad88-gemini-3.1-flash-lite-table_1-1024x728.gif)

The same holds true when comparing the new model to its most direct competitors, such as GPT-5 mini and Claude 4.5 Haiku. Grok 4.1 Fast is more affordable but also significantly slower. Google promises Gemini 3.1 Flash-Lite can produce up to 363 tokens per second, which is actually three tokens slower than Gemini 2.5 Flash-Lite, but still two to five times faster than any competitor.

As with other Gemini models, one area where it excels is on multimodal benchmarks. Google notes that on the [Arena.ai Leaderboard](http://arena.ai/), 3.1 Flash-Lite scores 1432 Elo points, putting it in company with many open-weight models and last-generation commercial offerings.

![](https://cdn.thenewstack.io/media/2026/03/a38babbc-mmmu_v2.gif)

Credit: Google.

It’s telling that Google did not publish any agent benchmarks with today’s release. This model is intended for high-volume agentic tasks and data processing, not for managing a fleet of other agents.

To tune the model’s reasoning time, developers can use the API to choose how much the model will think for any given task. Given that it is meant for high-volume tasks, that’s an important option to have when cost is likely a factor (at lower reasoning settings, the model will produce fewer tokens, after all).

It’s interesting that Google is launching a Flash-Lite version of Gemini 3.1 first, given that it traditionally launched a more capable (and expensive) Flash version first, or, as with Gemini 3, skipped Flash-Lite entirely.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)