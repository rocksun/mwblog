Anthropic on Tuesday launched [Claude Sonnet 4.6](https://www.anthropic.com/claude/sonnet), the latest version of its mainstream model.

This new version promises to almost match the company’s flagship [Opus 4.6 model](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/), which launched barely two weeks ago, in most tasks, but at the significantly lower price of $3/$15 per million input/output tokens (compared to $5/$25 for the Opus model).

Just like the previous version and Opus 4.6, Sonnet 4.6 offers a 1-million-token context window in beta.

## Benchmarks

Compared to the older Sonnet model, Sonnet 4.6 easily outperforms it on virtually all the usual benchmarks. When it comes to performing office tasks (using OpenAI’s [GDPval benchmark](https://openai.com/index/gdpval/)), it even beats the latest Opus model, as well as Google’s Gemini 3 Pro and OpenAI’s GPT-5.2.

On coding tasks, where Anthropic has long had an advantage over its competitors, Sonnet 4.6’s benchmark results are often within a percentage point or less of Opus 4.6. Anthropic notes that some of the improvements include better overall consistency and instruction following.

> Sonnet 4.6… even beats the latest Opus model, as well as Google’s Gemini 3 Pro and OpenAI’s GPT-5.2.

In its announcement, Anthropic notes that in its own tests, developers prefer Sonnet 4.6 to the last-generation Opus 4.5 model, which launched last November, 59% of the time. That’s reflected in the published benchmarks, where the new Sonnet model is far ahead of the older version of Opus. But Anthropic also notes that developers who used the model found that it was less likely to overengineer solutions and far less likely to hallucinate or claim success when it didn’t actually find the right solution.

![](https://cdn.thenewstack.io/media/2026/02/5addb4ce-anthropic-sonnet-46-benchmarks.png)

## Computer use

As for computer use, another area Anthropic has focused quite a bit on lately, the new model also gets very close to Opus on the OSWorld computer use benchmark. Benchmarks don’t always tell the full story, though, Anthropic argues. In its announcement, the company notes that what users are seeing when they use the model is “human-level capability in tasks like navigating a complex spreadsheet or filling out a multi-step web form, before pulling it all together across multiple browser tabs.”

> Developers who used the model found that it was less likely to overengineer solutions and far less likely to hallucinate or claim success when it didn’t actually find the right solution.

But even Anthropic acknowledges that even as the models get good at performing some tasks in the browser, and getting close to the human baseline on those benchmarks, they can’t quite match the most skilled humans yet.

![](https://cdn.thenewstack.io/media/2026/02/5a6220d8-claude-sonnet-4.6-demo-video.gif)

For developers who use the Claude API through the Claude Developer Platform, Sonnet 4.6 now supports context compaction to help it keep track of longer sessions (now in beta), as well as [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking), so the model can set the token budget for extended thinking based on its own evaluation of the complexity of the task. This feature launched with Opus 4.6.

## Availability

With earlier updates, Sonnet [occasionally](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/) performed well ahead of Opus, but that isn’t the case here. Still, going forward, Sonnet 4.6 will become the default model on [claude.ai](https://claude.ai) for users on the free and Pro plans, as well as for Claude’s Cowork mode, which makes sense, given that the model outperforms Opus 4.6 on many of these office tasks that Cowork will likely be used for.

## Where’s Claude Haiku 4.6?

The one model left for Anthropic to update to a 4.6 release is Haiku, its smallest, fastest and most affordable model. Haiku 4.5 launched in October 2025, so it’s due for an update, but Anthropic has typically updated Haiku at a slower pace and often skipped a few version numbers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)