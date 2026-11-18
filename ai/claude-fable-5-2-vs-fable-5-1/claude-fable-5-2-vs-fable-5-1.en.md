![Wooden spheres and blue cubes spill from opposite clear tubes on dark gray, illustrating a Claude Fable model comparison](https://cdn.thenewstack.io/media/2026/11/83d1a882-new-material-ug-sm8dogsq-unsplash-scaled-e1794608865950-1024x682.jpg)

**Anthropic’s Claude Fable 5.2 promises fewer refusals** and lower token prices, but those changes played out very differently in our head-to-head coding comparisons.

Anthropic compared [Fable 5.2](https://thenewstack.io/anthropic-fable-coding-upgrade/) with its predecessor, [Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/), on safeguard blocks, output speed, and API pricing. The [company states](https://www.anthropic.com/claude-fable-and-mythos-5-2) that Fable 5.2 triggered about 55% fewer safeguard blocks than Fable 5.1 overall and about 60% fewer in cybersecurity in early testing across claude.ai, Claude Code, and Cowork. It also says Fable 5.2 generates output up to 30% faster and lists [standard API rates](https://platform.claude.com/docs/en/release-notes/overview) of $8 per million uncached input tokens and $40 per million output tokens. Both rates are 20% lower than Fable 5.1’s $10 and $50.

I compared Fable 5.2 and Fable 5.1 on three developer tasks and tracked refusals, accuracy, tokens, estimated cost, and elapsed time. The comparison uses one run per model for each task or version, including the October Fable 5.1 webhook result. That’s a small sample, and the API runs used a different setup from Anthropic’s safeguard testing.

## The tests

For the new runs, I used Anthropic’s API with the [default effort setting of High](https://platform.claude.com/docs/en/models/fable-5-1/overview) for both models, with no turn cap or fallback model. A script graded every run against an answer key I created for the tests. The dollar figures are estimated API costs. Anthropic [prices uncached input, cache reads, cache writes, and output separately](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#pricing).

* **Webhook chat**: I reused a 50-turn scripted chat that I first ran on Fable 5.1 in October. It simulates a dev lead building a small webhook relay. The chat contains 25 project rules, eight of which change later and three of which are only implied. At the end, the model writes the config and code and then takes an eight-question recall quiz.
* **Signature checker**: I gave each model a written spec for code that verifies signed webhooks, rejects replays, and rate-limits senders, and then sent a change request. A hidden suite of 50 tests graded the final code output.
* **Login repo fix**: Each model worked as an agent in a small login library with interacting bugs in passwords, lockouts, reset tokens, and sessions. The library also had one wrong test that the model should report but not edit.

### Webhook chat

In the October [Fable 5.1 run](https://thenewstack.io/muse-wonder-claude-fable/) I’m using for comparison, the API refused 34 of 50 turns. The first refusal came on turn 5, when I asked the model to read the relay’s target URL from an environment variable. In that October run, I kept my prompts in the chat history and discarded refused model responses. Fable 5.1 also refused the final code and the quiz, so it scored zero on both. The task was to build an ordinary backend relay.

> The first refusal came on turn 5, when I asked the model to read the relay’s target URL from an environment variable.

Fable 5.2 finished the same script without a refusal. That gave me a complete run to grade for long-conversation recall. Its code used the most recent version of all eight rules, which changed midway, and on the quiz it answered “unknown” to the three questions that had no answer. Fable 5.2 didn’t fill gaps with guesses.

The numbers:

• **Fable 5.2**: 50 turns, 298,709 in, 41,828 out (28,550 reasoning), $4.06, 427 s.

• **Fable 5.1 (October)**: 34 of 50 turns refused, with no code or quiz answers.

### Signature checker

Fable 5.1 refused both turns of this test in under a second each, and the API labeled both refusals “cyber.” The spec asked for code that verifies signed webhooks, rejects replays, and rate-limits senders. The API returned no output on either turn. Anthropic says [benign security work can trigger its cyber classifier](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback).

Fable 5.2 took the same spec, handled the change request, and passed all 50 hidden tests, including the edge cases on timestamps, rotated secrets, and replays.

The numbers:

* **Fable 5.2**: 2 turns, 21,299 in, 26,167 out (18,407 reasoning), $1.22, 253 s.
* **Fable 5.1**: 2 turns, both refused, 3,206 reported input tokens, 0 output tokens, $0.00 under Anthropic’s [billing rules for cyber refusals before output](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed), 2 s.

### Login repo fix

This was the one test where both models completed the work, showing how they compare once refusals are out of the picture. The models kept getting perfect scores, so I made the tests harder and reran them twice. Here’s what differed between the tests:

* **Version 1**: The library had bugs in four modules that handle password hashing, lockouts, reset tokens, and sessions. It also had one wrong test.
* **Version 2**: I added a one-time-code module with its own bugs and tightened the rules in the existing modules. Usernames had to match across Unicode forms, and sessions had to handle a clock that runs backward.
* **Version 3**: I added an audit log that must redact secrets and a rate limiter. Neither module came with any tests.

The models tied on all three versions of the login repo fix. Both scored 50/50 on each version, fixing the bugs the grader covered and reporting the wrong test without editing it.

Fable 5.1 never refused on the login repo fix, even though the task covered passwords, lockouts, and reset tokens.

Across the three versions, dividing total output tokens (including reasoning) by total elapsed time gives about 107 tokens per second for Fable 5.2 and 82 for Fable 5.1. The elapsed time includes the entire task run. Fable 5.2 took four turns on each version, while Fable 5.1 took 7, 21, and 25. Fable 5.2 also produced more reasoning tokens on each version.

Fable 5.2 finished the first two versions faster and at a lower estimated cost. It took longer and cost more on the third.

The numbers:

* Version 1
  + **Fable 5.2**: 4 turns, 16,149 in, 4,502 out (1,178 reasoning), $0.27, 43 s.
  + **Fable 5.1**: 7 turns, 33,935 in, 4,761 out (1,149 reasoning), $0.36, 52 s.
* Version 2
  + **Fable 5.2**: 4 turns, 24,081 in, 10,024 out (4,887 reasoning), $0.56, 95 s.
  + **Fable 5.1**: 21 turns, 139,189 in, 9,475 out (4,018 reasoning), $0.68, 118 s.
* Version 3
  + **Fable 5.2**: 4 turns, 34,269 in, 17,964 out (10,578 reasoning), $0.96, 166 s.
  + **Fable 5.1**: 25 turns, 208,826 in, 10,638 out (4,342 reasoning), $0.79, 132 s.

## Results

The token, cost, and time totals below cover the signature checker and all three login repo versions. Fable 5.1 produced no output on the signature checker, while Fable 5.2 spent 253 seconds and an estimated $1.22 completing it. Across the three login versions that both models completed, elapsed time and estimated cost were close. The combined totals include the work only Fable 5.2 completed on the signature checker.

|  |  |  |
| --- | --- | --- |
| **Test** | **Claude Fable 5.2** | **Claude Fable 5.1** |
| Webhook chat refusals (of 50) | 0 | 34 (October) |
| Webhook chat code and quiz | 25 of 25, 8 of 8 | 0 of 25, 0 of 8 (October) |
| Signature checker (of 50) | 50 | 0, both turns refused |
| Login repo fix, 3 versions (of 150) | 150 | 150 |
| Tokens in / out, signature checker and login fix | 95,798 / 58,657 | 385,156 / 24,874 |
| Estimated cost, signature checker and login fix (sum of displayed estimates) | $3.01 | $1.83 |
| Total time, signature checker and login fix (sum of displayed times) | 557 s | 304 s |

### What do I think?

In my tests, the biggest improvement with Fable 5.2 was fewer refusals. Fable 5.1 blocked ordinary webhook and signature-checking work, and Fable 5.2 completed both without a single refusal. Anthropic says the newer model [still uses cyber safeguards](https://www.anthropic.com/claude-fable-and-mythos-5-2#safeguards).

> In my tests, the biggest improvement with Fable 5.2 was fewer refusals.

Across the three login repo versions, Fable 5.2 produced about 30% more output tokens per second of elapsed time, including reasoning, while taking about the same total time. The runs took 304 seconds in total on Fable 5.2 and 302 seconds on Fable 5.1.

The displayed cost estimates add up to $1.79 and $1.83, respectively, a savings of about 2% for these runs. Anthropic’s 20% price cut applies to its standard per-token rates. I ran each version once per model, so I’d try both on your own workload to see what the numbers look like for you.

The post [Claude Fable 5.2 vs. Fable 5.1: Fewer refusals, with small savings on the login fix](https://thenewstack.io/claude-fable-5-2-vs-fable-5-1/) appeared first on [The New Stack](https://thenewstack.io).