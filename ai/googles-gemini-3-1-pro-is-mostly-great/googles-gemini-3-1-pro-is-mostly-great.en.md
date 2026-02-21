Google on Thursday launched the latest version of its Gemini Pro model. While it’s not the best at every task, Gemini 3.1 Pro, which is officially still in preview, is far better at solving complex problems than Google’s previous mainstream model — at least according to the benchmarks.

Both Anthropic and [OpenAI launched quite a few models](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) in recent weeks. Earlier this month, Google launched Gemini 3 Deep Think, which features a specialized reasoning mode that easily outperforms Gemini 3.1 Pro. But that model is only available to [Google AI Ultra subscribers](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/), and API access is still invite-only (and will likely cost a premium).

According to Google, the ‘core intelligence’ of Gemini 3.1 Pro comes directly from the Deep Think model, which explains why 3.1 Pro performs so well on reasoning benchmarks.

On ARC-AGI-2, which features a set of reasoning tasks that are easy for humans but very hard for large language models, Google’s new model now scores 77.1%. That’s up from only 31.1% for the previous generation of Gemini Pro. [Anthropic’s Opus 4.6 solves](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 68.8% of these challenges, and OpenAI’s GPT-5.2, which is also due for an update, gets 52.9% right.

As is typical, all of these numbers are self-reported by Google, but Artificial Intelligence also now puts Gemini 3.1 Pro [at the top of its leaderboard](https://artificialanalysis.ai/leaderboards/models).

![](https://cdn.thenewstack.io/media/2026/02/cd165179-gemini_3-1-pro__benchmarks-scaled.png)

Gemini 3.1 Pro benchmarks (credit: Google).

## Mostly great

Gemini 3.1 Pro’s reasoning capabilities also show in most benchmarks, with the model leading the competition in most of them.

The one major disappointment, though, is how poorly it does on GDPval-AA, a benchmark that measures a model’s performance on a set of real-world tasks (that could influence a country’s GDP). There, for some reason, the model falls short at 1317 points, far behind Anthropic’s Sonnet 4.6 at 1633 points.

As for coding, Gemini 3.1 now also bests virtually all of the competition in the Terminal-Bench 2.0 agentic coding benchmark, though OpenAI has reported a significantly higher score for its recently launched 5.3-Codex coding model when using its own harness (Google didn’t report a score for using its own harness and only reported a benchmark based on the default [Terminus-2 harness](https://harborframework.com/docs/agents/terminus-2)).

In virtually every other coding benchmark, it’s also either ahead of the competition or within a few percentage points.

Like other Gemini models, the Gemini 3.1 Pro features a 1-million-token context window. Yet, while it can ingest text, photos, videos, and audio, its output is limited to 64,000 tokens.

## Pricing

Pricing for the new model remains unchanged, at $2/$12 per million input/output tokens. That makes it quite a bit more affordable (for a similar or better performance) than Anthropic’s Opus 4.6, which costs $5/$25 per million input/output tokens.

## Availability

Officially, Gemini 3.1 Pro is still in preview, but Google has already made it widely available. For developers, the new model is now accessible via the Gemini API in Google AI Studio, Gemini CLI, Android Studio, and the [Google Antigravity development platform](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/).

Enterprises can use it through Vertex AI and Gemini Enterprise, while consumers can get it via the Gemini app and in NotebookLM.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)