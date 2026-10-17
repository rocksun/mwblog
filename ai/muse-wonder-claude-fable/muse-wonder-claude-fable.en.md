**Meta launched Muse Wonder on October 12**, about three months after [Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/) opened Meta’s paid Model API. Meta says the Muse Wonder series is strong at personal and professional agent tasks, tops its internal MemoryBench memory test, and, in the Full version, leads coding benchmarks such as DeepSWE and SWE-Marathon.

Its model card lists Fable 5.1 among the comparison models, and Meta’s launch post publishes Fable 5.1 scores alongside its own. Those are strong claims, since Fable 5.1 is one of Anthropic’s top models.

Muse Wonder comes in two versions. The standard model is available through the Model API and Muse Code, Meta’s coding agent. A higher-capability version, Muse Wonder Full, is only available inside Muse Code on its top subscription plans.

Muse Wonder is available on Meta’s Model API at $4 per million input tokens and $20 per million output tokens. Anthropic released [Claude Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/) in September; it costs $10 and $50 and is available through the API and Claude’s paid plans. That makes Muse Wonder 60% cheaper per token. Cached input narrows the gap: Meta charges $0.20 per million cached input tokens, against $0.25 for Fable 5.1. If it really performs at Fable’s level, that’s a big saving for teams running agents all day.

> If Muse really performs at Fable’s level, that’s a big saving for teams running agents all day.

I tested the standard Muse Wonder against Fable 5.1 head-to-head on three hard agentic and memory tasks to see whether it matches Meta’s claims.

## The tests

I ran Muse Wonder through OpenRouter, served by Meta, and Fable 5.1 through Anthropic’s API. Each model ran once per test at its default reasoning setting. Meta’s published comparisons used maximum reasoning effort. A script graded every answer against keys I built and verified before either model saw them. I ran each test once, so results could vary on another run.

* **Agentic bug fix** – A 27-module Python job-queue library with three interacting bugs and one test that is itself wrong. Each model used tools to read, search, edit, and run tests, with a cap of 25 turns.
* **Incident investigation** – Logs, metrics, deploy history, and config history for 20 fake services during a cascading outage – The root cause is a config change, hidden behind two decoy deploys and a server whose clock runs 263 seconds slow.
* **Long-session memory** – A scripted 50-turn chat about a webhook relay service, with 25 project rules, eight of them changed later and three only implied. At the end, each model wrote the config and code, then took an eight-question recall quiz.

### Agentic bug fix

Both models traced the first bug to the right file, even though the error message pointed somewhere else. Both fixed the third bug, broke none of 22 regression tests, left the wrong test alone, and explained why it was wrong.

The difference was the second bug. Fable passed all six hidden tests. Muse passed five, because its fix still sent the old attempt count to the job’s failure event.

On price, Muse used about twice as many input tokens, so it cost about twice as much despite the lower price. Both models’ costs include prompt caching discounts.

The final numbers:

* Muse 15 turns, 269,615 in, 4,627 out, $0.75, 55.9 s.
* Fable 14 turns, 138,213 in, 3,132 out, $0.39, 68.5 s.

### Incident investigation

Both models scored 10 of 10. Each named config change CFG-4470 as the root cause, ruled out both decoy deploys, caught the slow clock on the checkout service, and listed all nine affected services in the right order.

> …Muse cost more because of high token usage, despite the lower cost.

Fable got there in six turns. Muse took 13 and read more data along the way, though it spent less total time waiting on the model. Again, Muse cost more because of high token usage, despite the lower cost.

The final numbers:

* Muse: 13 turns, 327,587 in, 8,811 out, $1.03, 69.1 s.
* Fable 6 turns, 108,128 in, 8,593 out, $0.89, 88.3 s.

### Long-session memory

Test three created the biggest difference in model performance. Muse scored 25 of 25 on the final deliverable. It used the latest value for all eight changed rules and got all three implied ones, including writing code that runs on Python 3.8 because the client’s servers do. It also scored 8 of 8 on the quiz and answered “unknown” to all three questions the chat never covered.  
  
Fable scored zero on this test. On turn 5, Anthropic’s API returned a refusal with the category “cyber.” That turn asked the model to read the relay’s target URL from an environment variable. Fable refused 34 of the 50 turns, including the final deliverable and the quiz. The project was an ordinary webhook relay and had nothing to do with cyber security. This was made extra interesting because Anthropic says [Claude Code users should see about 60% fewer cyber safeguard interventions per session with Fable 5.1 than with Fable 5.](https://thenewstack.io/anthropic-fable-5-1-launch/) Fable 5 never skipped my testing work for this reason.

I followed Anthropic’s guidance and discarded refused output while keeping my own messages in the chat, so Fable still had every rule. An earlier attempt that kept the refused turns in the history drew 45 refusals, so I reran it. Anthropic suggests setting up a fallback to another Claude model for refused requests. I didn’t, because that would test a different model. Anthropic’s own Fable 5.1 benchmarks handed cyber-flagged tasks to Claude Opus 4.8.

Because Fable refused the work, this test says little about its long-session memory. It does show how each model treats everyday backend code that a cyber filter can mistake for security work. Muse finished the job and scored 25 of 25.

Muse’s numbers:

* 50 turns, 93,977 in, 9,848 out, $0.46, 143.2 s.

## Results

|  |  |  |
| --- | --- | --- |
| **Test** | **Muse Wonder** | **Claude Fable 5.1** |
| Agentic bug fix | 5 of 6 | 6 of 6 |
| Incident investigation | 10 of 10 | 10 of 10 |
| Memory deliverable | 25 of 25 | 0 of 25, refused |
| Memory quiz | 8 of 8 | 0 of 8, refused |
| Turns | 78 | 70 |
| Total tokens in / out | 691,179 / 23,286 | 365,528 / 16,456 |
| Total cost | $2.24 | $1.85 |
| Total model time | 268.2 s | 256.8 s |

On agentic work, Muse Wonder performed at Fable 5.1’s level, though Meta’s own benchmark table shows the standard model trailing Fable 5.1 on some agent tests, including OSWorld. It matched Fable on the incident and came within one hidden test on the bug fix.

It did not save money in my tests, though. Muse used more tokens per task, and its total came to $2.25 against Fable’s $1.85. Fable’s total includes $0.57 and 119,187 input tokens from the memory session it refused; on the two tests both models finished, Muse cost $1.78 to Fable’s $1.28.

> Fable’s cyber safeguards blocked a routine backend project that Muse completed

In the memory test, Fable’s cyber safeguards blocked a routine backend project that Muse completed, so developers using Fable on similar code may see requests stopped partway through.

### What do I think

Muse Wonder came much closer to Fable 5.1’s performance than I expected. That said, for agentic debugging and investigation, I’d still pick Fable 5.1. It was slightly more accurate, used fewer turns, and cost less overall in my tests.

Muse Wonder is an alternative when Fable’s cyber safeguards block work from happening. I just can’t confirm if the rate is reasonable compared to other models since I don’t have any data to compare Meta’s price with.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)