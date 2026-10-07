**OpenAI launched [GPT-6.1 Sol](https://thenewstack.io/openai-gpt-6-1-sol/) on September 29**, just a week after it launched [GPT-6 Sol](https://thenewstack.io/openai-gpt-6-sol-luna-release/). OpenAI marketed 6.1 as an upgrade to 6 and as a cheaper near-match for Astra. OpenAI says the new model nearly matches Astra on agentic coding, computer use, and professional work. It also says GPT-6.1 Sol makes fewer factual errors than GPT-6 Sol at low reasoning effort. OpenAI calls it “near-Astra intelligence for a fifth of the price.” OpenAI also halved cached-input pricing, from GPT-6 Sol’s $0.20 to $0.10.

GPT-6.1 Sol costs $2 per million input tokens and $10 per million output tokens, with cached input at $0.10. GPT-6 Astra costs $10 per million input tokens, $50 per million output tokens, and $1 per million cached input tokens. That puts GPT-6.1 Sol at one-fifth of Astra’s price for input and output tokens, and one-tenth for cached input.

These claims are a lot for my skeptical self to take in. Does the price gap hold up once real token use is measured? And how close does GPT-6.1 Sol actually come to Astra’s intelligence? To find out, I ran both models through the same three tests I ran on [GPT-6 Sol and Opus 5.5](https://thenewstack.io/gpt-6-sol-vs-opus-5-5/).

## The tests

I called both models through the OpenAI Responses API with identical prompts, reasoning effort set to max, and a 64,000-token output limit. These are the same settings I used for GPT-6 Sol. The tests work for GPT-6.1 Sol vs Astra because they each map to one of OpenAI’s marketing claims for GPT-6 Sol and GPT-6.1 Sol.

* **CI triage** – The model reads 40 failed CI job logs and a runbook with conditional rules. For each job, it decides whether to retry, block, or page.
* **Incident logs** – The model reads 3,664 lines of logs from five services during a two-hour outage and answers seven postmortem questions. The answers depend on exact counting, a timezone conversion, and a red herring.
* **Resolver spec** – The model writes a dependency resolver for a fictional package manager from a two-page spec, without running any code. A hidden suite of 120 tests grades the result.

I didn’t include prompts for this because I used multiple files, repos, and lengthy prompts rather than something that copies/pastes easily.

## CI triage

Both models made all 40 calls correctly on all five runs. Astra was faster, averaging 24 seconds per run to GPT-6.1 Sol’s 31 seconds. Both read 3,867 input tokens per run, and output was close, with 1,381 tokens for GPT-6.1 Sol and 1,431 for Astra. GPT-6.1 Sol cost about 2 cents per run, and Astra cost 11 cents.

Accuracy was a tie. Astra won on speed, and GPT-6.1 Sol won on cost.

## Incident logs

This test gave GPT-6 Sol the most trouble last month. It missed a customer on two runs and miscounted failed checkouts on another. GPT-6.1 Sol and Astra both answered all seven questions correctly on every run.

GPT-6.1 Sol averaged 2 minutes and 20 seconds per run, about 19% faster than Astra’s 2 minutes and 53 seconds. Each run read 113,966 input tokens. Output was nearly even, at 8,316 tokens for GPT-6.1 Sol and 8,539 for Astra. GPT-6.1 Sol cost $0.31 per run, and Astra cost $1.57.

Accuracy was a tie. GPT-6.1 Sol won on speed and cost.

## Resolver spec

Last month, GPT-6 Sol left a stray parenthesis in one run that crashed the resolver. This time, both models passed all 120 hidden tests on every run.

This test showed the biggest gap. GPT-6.1 Sol averaged 7 minutes and 7 seconds per run, about 30% faster than Astra’s 10 minutes and 6 seconds. Astra wrote 25,207 output tokens per run to GPT-6.1 Sol’s 19,637, or 28% more. Counting input and output, that added up to $1.28 per run, compared with $0.20 for GPT-6.1 Sol.

Accuracy was a tie. GPT-6.1 Sol won on speed, tokens, and cost.

## Results

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Test** | **Model** | **Perfect runs** | **Avg. time** | **Avg. tokens (in / out)** | **Avg. cost** |
| CI triage | GPT-6.1 Sol | 5/5 | 0:31 | 3,867 / 1,381 | $0.02 |
| CI triage | GPT-6 Astra | 5/5 | 0:24 | 3,867 / 1,431 | $0.11 |
| Incident logs | GPT-6.1 Sol | 5/5 | 2:20 | 113,966 / 8,316 | $0.31 |
| Incident logs | GPT-6 Astra | 5/5 | 2:53 | 113,966 / 8,539 | $1.57 |
| Resolver spec | GPT-6.1 Sol | 5/5 | 7:07 | 1,687 / 19,637 | $0.20 |
| Resolver spec | GPT-6 Astra | 5/5 | 10:06 | 1,687 / 25,207 | $1.28 |
| **Total (15 runs)** | **GPT-6.1 Sol** | **15/15** | **49:54** |  | **$2.66** |
| **Total (15 runs)** | **GPT-6 Astra** | **15/15** | **1:07:07** |  | **$14.77** |

Both models were perfect on all 15 runs. GPT-6.1 Sol’s runs took 49 minutes and 54 seconds and cost $2.66 in total. Astra’s took 1 hour, 6 minutes, and 55 seconds and cost $14.77. GPT-6.1 Sol cost 18% of what Astra did, close to the one-fifth price OpenAI advertises. Output tokens were nearly the same on CI triage and incident logs, and Astra used 28% more on the resolver spec.

## What do I think?

OpenAI’s claim held up in my tests. GPT-6.1 Sol matched Astra on every run, cost less than a fifth as much, and was faster on the two longer tests.

I’d use GPT-6.1 Sol for this kind of work. It got every answer right on all three tests, like Astra, for less than a fifth of the price. My tests can’t show the two models are equal on everything, and Artificial Analysis’ index still puts Astra slightly ahead at max effort, but nothing I ran gave me a reason to pay for Astra.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)