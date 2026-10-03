**OpenAI on Tuesday launched GPT-6.1 Sol**, the newest version of its workhorse model, only a week after [launching GPT-6 Sol](https://thenewstack.io/openai-gpt-6-sol-luna-release/).

The company describes the new model as “an upgrade to GPT-6 Sol that nearly matches GPT-6 Astra’s intelligence on agentic coding, computer use, and professional work at one-fifth of Astra’s standard input and output token prices.”

## Same price, near-Astra performance

Pricing for GPT-6.1 Sol remains the same as before, at $2 per million input tokens and $10 per million output tokens, with cached input significantly discounted to $0.10 per million tokens.

![](https://cdn.thenewstack.io/media/2026/09/c0fecfd2-screenshot-2026-09-29-at-18.02.34-1024x587.png)





*Click image to enlarge. (Credit: OpenAI.)*

GPT-6.1 Sol is now available in the API, as well as to all Plus, Pro, Business, Enterprise, and Edu users in ChatGPT Work and Codex. For now, though, the model isn’t available in Chat.

One new feature is that GPT-6.1 Sol will also come in an [Ultrafast version](https://openai.com/index/devday-2026-recap/) in Codex, with token generation that is up to 8x faster than the standard speed.

Although its predecessor is only a week old, the updated model shows significant improvements. In virtually every benchmark OpenAI provided ahead of the announcement, the new model ranks similarly to OpenAI’s costly GPT-6 Astra flagship model, but at a significantly lower cost.

![](https://cdn.thenewstack.io/media/2026/09/19663f21-screenshot-2026-09-29-at-18.03.01-1024x667.png)





*Click image to enlarge. (Credit: OpenAI.)*

For example, on coding benchmarks, GPT-6.1 Sol scores 6.4 percentage points higher than GPT-6 Sol on DeepSWE 1.1, with results that essentially match GPT-6 Astra—but at one-fifth the cost.

In some benchmarks, the new Sol model also beats Anthropic’s Opus 5.5 (with fallbacks), which launched on the same day as GPT-6 Sol. On the GDP.pdf benchmark, for example, which tests how the models answer questions about complex PDF documents, GPT-6.1 Sol tops out around 32%, while Opus 5.5 hits about 29%. Here, too, the results are similar to GPT-6 Astra at about one-fifth the cost per task.

---

###### OpenAI DevDay 2026 coverage:

---

One area where GPT-6.1 Sol performs especially well is computer use. Here, the new model outperforms its predecessor by seven percentage points at maximum reasoning, at half the cost — and once again with performance in line with Astra.

Indeed, given these results, it’ll be hard to justify using Astra for most use cases.

## Mixed results against Sonnet 5.5

Sadly, only a few comparison benchmarks exist for [Sonnet 5.5,](https://thenewstack.io/claude-sonnet-55-launch/) which was released on Monday and costs the same $2/$10 per million input/output tokens. Where benchmarks exist for both models, the results are mixed.

Sonnet 5.5 scores 71% on DeepSWE, while GPT-6.1 Sol scores about 75%. On AutomationBench, GPT-6.1 Sol scores around 36% compared to 44.7% for Sonnet 5.5, but Sol’s price per task is significantly lower ($0.30 vs. $1.14).

## Fewer errors, better alignment

OpenAI also says GPT-6.1 Sol makes fewer factual errors. At low reasoning effort, the share of responses containing at least one factual error fell from 11.4 percent with GPT-6 Sol to 7.7 percent, a reduction of about 32 percent.

These results come from deliberately difficult conversations where users flagged mistakes by earlier models, and they do not represent error rates in typical use.

Given that we’re not quite pacing the frontier (yet), it’s good to see that GPT-6.1 Sol brings Sol’s alignment in line with Astra. In general, it is better at respecting user intent and safety constraints, OpenAI says, and only fails to disclose broken search tools in 2.1% of cases (instead of guessing).

In the company’s tests, the GPT-6.1 Sol-based agents also never tried to work around an automated safety reviewer’s decision to block their agents.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)