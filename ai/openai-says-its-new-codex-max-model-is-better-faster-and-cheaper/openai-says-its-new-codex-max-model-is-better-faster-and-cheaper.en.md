OpenAI today launched GPT-5.1-Codex-Max, a new variant of its GPT-5.1-Codex foundation model that was specifically trained to excel at coding tasks and which powers OpenAI’s Codex agent.

The original [Codex model](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) launched about two months ago and, at the time, it was extremely competitive — and often led the competition — on most benchmarks. But nobody in this field is standing still. OpenAI itself launched the 5.1 versions of its GPT models, including Codex, just a few days ago, and [Google’s Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/), which launched earlier this week, also pushed the envelope for coding with frontier models.

Codex-Max, OpenAI said, was specifically trained on agentic tasks related to software engineering, math, research  and more. It’s meant to handle long-running tasks; OpenAI stressed that this is also the first model it trained to work across multiple context windows. Using compaction to compress context into more manageable units, OpenAI claims the Codex agent can now work “over millions of tokens in a single task.”

[![A graph showing the performance of OpenAI's Codex-Max model on the SWEbench-verified benchmark.](https://cdn.thenewstack.io/media/2025/11/22f94223-openai-codex-max-swe.png)](https://cdn.thenewstack.io/media/2025/11/22f94223-openai-codex-max-swe.png)

Source: OpenAI.

## What Are Codex-Max’s Benchmarks?

That’s likely part of why Codex-Max does quite well on the standard coding benchmarks, too. Codex-Max, on its highest settings, scores 77.9% on the SWE-Bench Verified benchmark, for example, which tests how well the agent can handle real-world pull requests from a number of popular Python projects.

The GPT-5.1-Codex model on its high setting scored 73.1%, [Anthropic’s Sonnet 4.5](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/) got to 77.2% (though with test-time compute added, it got to 82%) and Google’s new Gemini 3 comes in at 76.2%.

On TerminalBench, Codex-Max scores 58.1%, while GPT-5.1-Codex achieved 52.8%, Sonnet 4.5 hit 50% and Gemini 3 scored 54.2%.

[![](https://cdn.thenewstack.io/media/2025/11/847cf7d6-codex-bench.png)](https://cdn.thenewstack.io/media/2025/11/847cf7d6-codex-bench.png)

GPT-5.1-Codex-Max benchmarks (Credit: OpenAI).

## Is Codex-Max Better and Cheaper?

Like with most modern models, Codex-Max will feature different reasoning modes that govern how many reasoning tokens the model can use to perform a given task. For Codex-Max, OpenAI is adding a new extra high (“xhigh”) mode, which lets developers push the model’s rephrasing efforts even further. This obviously increases the latency and may not be ideal for all use cases, but it does improve accuracy by a few percentage points.

Benchmarks aren’t everything, though. How well the model performs on real-world tasks remains to be seen.

What’s maybe even more important for developers, though (and especially those who use the API), is that in OpenAI’s tests, Codex-Max was often able to produce similar or better results with fewer tokens and tool calls — and it produced fewer lines of code to get to the same results. Because of this, OpenAI argues that Codex-Max is 27 to 42% faster on real-world coding tasks than its predecessor.

One place where it will surely do well, though, is on Windows machines. OpenAI notes that this is the first model the company has trained to operate in Windows environments.

## What’s Codex-Max’s Availability?

The new model is now available in Codex in the CLI, IDE extension, cloud and code review, and will be available for all users with ChatGPT Plus, Pro, Business, Edu and Enterprise plans. Access for users who want to use it in Codex via their API key is coming soon.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)