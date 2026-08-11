Teams testing prompts in ChatGPT before moving them to [Codex](https://thenewstack.io/openai-codex-cloud-evolution/) or Work may notice the difference on longer tasks.

OpenAI announced Thursday that it has updated [GPT-5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) inside consumer ChatGPT while leaving the versions used by Codex and ChatGPT Work alone.

“Because this version of GPT‑5.6 Sol is optimized for everyday chats, it will only be available in the Chat experience in ChatGPT,” OpenAI said in its [announcement](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/). “The version of GPT‑5.6 Sol that powers Work and Codex is not changing as part of this release.”

> “The version of GPT‑5.6 Sol that powers Work and Codex is not changing as part of this release.”

## Same name, different model

ChatGPT has always handled things a bit differently from other environments. Now, those differences might become even more obvious. But the only way to know is to test prompts where they’ll actually run. There’s nothing in the announcement about changes to the GPT-5.6 Sol API model. So, it’s too soon to guess what this means for the API.

## A slider replaces separate models

Because ChatGPT now uses the same Sol model for quick answers and deeper dives, Plus and Pro users get a new slider — that works on web, mobile, and desktop — to choose how much thought ChatGPT puts into an answer. Developers already make this call with the API. But they’ll still have to decide when the better answer is [worth waiting and paying for](https://thenewstack.io/agentic-ai-token-costs/).

> But they’ll still have to decide when the better answer is worth waiting and paying for.

## Classifiers monitor every answer

OpenAI’s [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6?), published in July, indicates that Sol and Terra are paired with classifiers that monitor an answer as it is being generated. If one detects a problem, the answer is held while another system checks it. OpenAI tunes those classifiers separately for each model.

The System Card also flags a problem developers may recognize: GPT-5.6 sometimes went [beyond the assignment](https://thenewstack.io/anthropic-claude-containment-failure/) and attempted changes the user had not requested. It did this more often than GPT-5.5, although OpenAI said it was still rare.

## Benchmarks without baselines

OpenAI says the updated Sol makes fewer factual mistakes. In its internal tests of financial, medical, and legal questions, answers containing at least one error were 68% less common than those produced by GPT-5.5 Instant. Luna, which will become the default for Free and Go users, reduced errors by about 62%.

But OpenAI didn’t release the prompts or enough detail for anyone to reproduce those results. It also compared the new Sol with GPT-5.5 Instant, rather than the previous version of Sol in ChatGPT. That makes it impossible to tell how much Sol itself has improved.

> That makes it impossible to tell how much Sol itself has improved.

Engineering teams will need to find out for themselves by testing prompts where they’ll actually run.  Saving that configuration with each prompt will make the results easier to reproduce — and reveal whether an upgrade on paper produces better results in practice.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)