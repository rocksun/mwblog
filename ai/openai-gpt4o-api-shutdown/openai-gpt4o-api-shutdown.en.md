**OpenAI is retiring four GPT-4 models from its API on January 14, 2027.** The deprecation notice the company sent developers Wednesday covers GPT-4o, GPT-4o mini, GPT-4.1, and GPT-4.1 mini, along with their dated snapshots and every fine-tuned model built on top of them.

With just three months to migrate production traffic, OpenAI’s recommended replacement, GPT-6 Luna, handles reasoning and tool calls differently enough that swapping the model ID may be the easiest part of the migration.

> With just three months to migrate production traffic, OpenAI’s recommended replacement, GPT-6 Luna, handles reasoning and tool calls differently enough that swapping the model ID may be the easiest part of the migration.

## GPT-4o’s long goodbye

GPT-4o arrived on May 13, 2024, as OpenAI’s flagship and built a following loyal enough to change the company’s plans. When GPT-5 replaced it in August 2025, Reddit filled with complaints, and OpenAI brought it back for paying ChatGPT subscribers the very next day. That reprieve lasted until February 13, 2026, when GPT-4o and GPT-4.1 disappeared from ChatGPT. Both remained available through the API, but that access now is sunsetting.

By then, OpenAI said just 0.1% of daily ChatGPT users were still choosing GPT-4o, although the model continued serving API requests for applications built around it.

GPT-4.1 was a different kind of release, arriving on April 14, 2025, as an [API-only family](https://openai.com/index/gpt-4-1/) that skipped ChatGPT entirely and went straight after developers with stronger coding, better instruction following, room for up to a million tokens of context, and more reliable diff formats for anyone letting a model loose on large files.

[Kevin Weil](https://www.linkedin.com/in/kevinweil/), OpenAI’s chief product officer, called them models [“trained just for developers”](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) during the launch livestream, and [Sam Altman went on X](https://x.com/sama/status/1911830886896799931) to say developers “seem very happy” with them.

## Luna pricing has fine print

Luna is the fastest and cheapest tier of GPT-6, and on paper it covers the basics GPT-4.1 offered, with a [1.05 million-token context window](https://developers.openai.com/api/docs/models/gpt-6-luna), structured outputs and function calling. At $0.10 per million input tokens and $0.50 per million output tokens, it’s cheaper than [GPT-5.6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/), which charged twice as much for input and $1.20 per million output tokens.

Once a prompt passes 272,000 input tokens, the input rate doubles the output rate raises by 50% for the entire request. That could eat into the savings for RAG pipelines and coding agents working with large codebases.

OpenAI’s [migration guide](https://developers.openai.com/api/docs/guides/latest-model) says GPT-6 Luna defaults to medium reasoning effort but supports function calling through Chat Completions only with `reasoning_effort=none.` Combining reasoning and tool calls requires the Responses API. Enabling reasoning also rules out temperature, `top_p, top_logprobs,` and `logprobs,` all supported by GPT-4.1.

The company recommends using its Docs skill in Codex to update API calls across a project, but those changes won’t account for differences in model behavior. Anthropic ran into a similar problem last month when [Opus 5.5 introduced four breaking changes](https://thenewstack.io/claude-opus-agent-migration/), causing 400 errors in existing agent integrations. Other changes altered how agents behaved without triggering errors, making those regressions harder to catch.

## No fine-tuning on Luna

New self-serve fine-tuning jobs end on January 6, 2027, eight days before the GPT-4 models retire. Existing fine-tuned models will continue serving inference requests until January 14, leaving a short window to run replacements alongside them.

> New self-serve fine-tuning jobs end on January 6, 2027, eight days before the GPT-4 models retire.

## Six months’ notice, three delivered

Other deadlines are on [OpenAI’s deprecation schedule](https://developers.openai.com/api/docs/deprecations), which includes GPT-4.1 nano, the first GPT-4o snapshot, and older GPT-3.5, GPT-4, and o-series models retiring October 23. GPT-5 and o3 snapshots follow December 11, with selected legacy audio, real-time, and transcription models scheduled for January 20, 2027. GPT-5.1, GPT-5.3-Codex and GPT-5.4-Nano are set to retire April 1.

The List models API now includes a `shutdown_date` field, making it possible to check upcoming retirements automatically. Customers who need more time may be able to keep older models running through dedicated capacity, although they’ll have to arrange that with OpenAI’s sales team.

The three-month warning also falls short of OpenAI’s own deprecation policy, which promises at least six months’ notice for generally available models. The policy allows exceptions for safety or compliance reasons, but there’s no explanation for why GPT-4o and GPT-4.1 are getting only half that time.

> The three-month warning also falls short of OpenAI’s own deprecation policy, which promises at least six months’ notice for generally available models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)