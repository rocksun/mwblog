**MiniMax released M3.1 Flash on October 19, 2026, and says** it cuts the overall cost of agentic tasks by 70% and makes online inference nearly three times faster than M3. MiniMax lists Flash at $0.15 per million input tokens and $0.60 per million output tokens.

Those are half M3’s discounted rates of $0.30 and $1.20 for requests with no more than 512K input tokens; cached input and longer M3 requests have separate rates. Online inference speed differs from the time needed to finish a tool-using task.

[Artificial Analysis](https://artificialanalysis.ai/evaluations/automationbench-aa) independently scored [M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) at 72.5% on AutomationBench-AA, a test of multi-step work across simulated business apps. That score measures the share of task objectives completed without guardrail violations. It differs from the percentage of entire tasks completed on Zapier’s own AutomationBench leaderboard.

I didn’t run AutomationBench myself. Instead, I tested M3.1 Flash against M3 on three smaller agent tasks to see how they behaved in work closer to my own. One run per task is too small a sample to measure a general improvement in accuracy, cost, or speed.

## The tests

I ran both models once per test through OpenRouter, pinned to MiniMax’s own servers, at default settings. At the time of testing, I used OpenRouter’s free Flash endpoint, so the dollar amounts below for Flash are estimates at MiniMax’s list prices, not charges I paid. I didn’t use the MiniMax API directly because its credit minimum was too high for this small test. I capped the turns each model could use to complete the job.

Results through OpenRouter may differ from runs through MiniMax’s API, even when routed to MiniMax’s servers. I used OpenRouter because it let me test both models in one place.

* **Agentic bug fix** – A Python job-queue library with three interacting bugs and one wrong test. The model reads, edits, and runs tests through tools, with a 25-turn cap.
* **Incident investigation** – Logs, metrics, and deploy history for 20 fake services during an outage. The cause is a config change hidden behind two decoy deploys and a server clock that runs slow.
* **Long context** – A fake engineering wiki of about 500,000 tokens with three questions about how its services depend on each other.

### The agentic bug fix test

Neither model scored perfectly, both finishing with a 5 of 6, but each missed something different. Flash fixed all three bugs without breaking anything. It then ran out of turns before writing its final answer, so it never reported the wrong test. M3 reported the wrong test but missed one case on the second bug.

The tool logs show two different working styles. Flash read 37 files over its first 14 turns before making a single edit. It had every bug fixed by turn 16, then spent its last four turns writing a scratch test to double-check the docs. M3 ran the tests once and made its first fix on turn 4.

> Flash’s approach got all three bugs right, but it burned through its turns reading and checking and never got to write up what it found.

Flash’s approach got all three bugs right, but it burned through its turns reading and checking and never got to write up what it found. M3 moved faster and missed a case. Flash used more than twice the input tokens and had an estimated cost about 23% lower on this task, helped by discounted cached input.

The numbers:

* **Flash:** 25 turns, 538,718 in, 7,056 out, $0.017, 129.0 s, 55 tokens/s.
* **M3** 17 turns, 203,639 in, 4,327 out, $0.022, 36.8 s, 118 tokens/s.

### The incident investigation test

Both models scored 10 of 10. Each found the config change, ruled out both decoy deploys, caught the slow clock, and listed all nine affected services in order.

They made the same 63 tool calls, but Flash bundled more calls per turn and finished in 17 turns, compared with M3’s 24. Flash used fewer input tokens and had an estimated cost about 68% lower on this test, close to MiniMax’s 70% claim for agentic tasks. Turn count alone does not explain the difference; cache use and token prices also matter.

Flash used fewer input tokens here, but slightly more output tokens.

The numbers:

* **Flash:** 17 turns, 367,401 in, 13,175 out, $0.020, 146.2 s, 90 tokens/s.
* **M3**: 24 turns, 592,377 in, 12,061 out, $0.062, 72.2 s, 167 tokens/s.

### The long context test

Neither model produced an answer. Flash used the 64,000 output tokens I allowed and ran out before writing anything. M3 also stopped after roughly 29,000 output tokens without an answer. [MiniMax](https://www.minimax.io/blog/minimax-m3) lists a roughly 1-million-token context window for M3, but that capacity did not translate into a completed answer in this run.

> MiniMax lists a roughly 1-million-token context window for M3, but that capacity did not translate into a completed answer…

I ran one extra round with reasoning set to low and the same 28,000-token output limit for both. Flash answered this time but found only 3 of 33 affected services. M3 again ran out before answering.  
  
Neither model answered this large-document question reliably under my settings. Flash hit the 64,000-token output limit I set on the first run. When I pushed it to answer with less, it missed 30 of the 33 services. I wouldn’t rely on either result for a task like this.

## The test results

|  |  |  |
| --- | --- | --- |
| **Test** | **MiniMax M3.1 Flash** | **MiniMax M3** |
| Agentic bug fix | 5 of 6 | 5 of 6 |
| Incident investigation | 10 of 10 | 10 of 10 |
| Long context | No answer | No answer |
| Total tokens in / out | 1,401,606 / 84,231 | 1,291,477 / 45,214 |
| Total cost (Flash estimated) | $0.15 | $0.27 |
| Total model time | 661.6 s | 465.0 s |

Both models received the same scores on the two graded tasks, and neither answered the long-context question in the first round. M3 was faster overall. Flash’s estimated total cost was lower, even though it used more input and output tokens. Cache use and different token prices affect that comparison, so token totals alone cannot show which model would cost less at identical rates.

## What do I think?

I noticed differences between MiniMax M3 and M3.1 Flash, but apart from the lower estimated cost, I wouldn’t call them improvements in these runs. Flash was slower overall, and both models scored the same on the graded tasks.

> …apart from the lower estimated cost, I wouldn’t call them improvements in these runs.

Three one-off tests cannot establish whether MiniMax’s benchmark claim holds across other work. I would test more of my own tasks before choosing either model, and I’ll keep an eye on MiniMax’s future updates.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)