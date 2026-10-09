**Anthropic launched [Sonnet 5.5](https://thenewstack.io/claude-sonnet-55-launch/)** six days after [Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/). The company says it scores 70.6% on Terminal-Bench 4.0, ahead of Opus 5.5’s 66.4% at xhigh effort. It also says Sonnet 5.5 generates output more than 30% faster than Sonnet 5 and uses fewer tokens per task.

Sonnet costs $2 per million input tokens and $10 per million output tokens, half of Opus 5.5’s $4 and $20.

Half the price per token doesn’t guarantee half the bill, though. If a model needs more tokens to finish the job, the savings shrink. Independent testing from Artificial Analysis found exactly that at max effort, with Sonnet 5.5 costing $7.67 per task to Opus 5.5’s $5.98. My [testing last week](https://thenewstack.io/claude-opus-5-5-vs-opus-5/) suggests Opus 5.5 was the new budget model. Sonnet 5.5 made me test that again.

> Half the price per token doesn’t guarantee half the bill, though.

I was never a fan of Sonnet. I tried it in the past because it was cheaper than Opus 5, but I always ended up going back to Opus 5 because cheaper isn’t a win when the output isn’t that great. I came in unsure whether Sonnet had a real place, so I tested it against Opus 5.5, the model I’d most likely replace with it.

## The tests

I called both models through the Anthropic API with identical prompts, adaptive thinking, and the maximum effort setting. I ran each test five times per model to measure consistency and graded every run against a hidden test suite the models never saw. I logged tokens, cost at list price, and time for every run.

* **Agentic bug fix**: The model gets a small Python order-pricing repo with four planted bugs and one flaky test, plus tools to read files, write files, and run tests. A hidden suite of 12 tests checks the fixes, and I tracked tool calls, since early testers cited by Anthropic said Sonnet 5.5 needs fewer of them.
* **Resolver spec**: The model writes a dependency resolver for a fictional package manager from a two-page spec, without running any code. A hidden suite of 120 tests grades it.
* **Concurrency bugs**: The model gets an asyncio job queue with three race conditions and an incident report describing double charges and jobs that never ran. It has to fix every bug without running the code, and eight hidden tests check each fix.

I didn’t include the prompts here because each test depends on a code repo, spec, or module too long for a quick copy/paste.

### Agentic bug fix

Both models fixed all four bugs in all five runs and passed all 12 hidden tests. Neither one edited the test files, and both flagged the flaky test.

Sonnet 5.5 averaged 5 minutes 8 seconds, 29 tool calls, 42,608 output tokens, and $0.70 per run. Opus 5.5 averaged 3 minutes 21 seconds, 25 tool calls, 20,625 output tokens, and $0.75. Sonnet 5.5 used twice as many tokens, which wiped out almost all of its per-token discount.

Sonnet 5.5 didn’t get there on the first try. In the agentic test, the model works in steps, and each step had a 32,000-token limit. On my first attempt, Sonnet 5.5 thought so long in a single step that it hit that limit in four of five runs, and those runs stopped before finishing. Opus 5.5 ran under the same limit and never came close. I raised the limit to 128,000 and reran the four, and all of them passed. The failed attempts cost about $1.40, which isn’t in the totals. Counting them, Sonnet 5.5 averaged about $0.98 per run on this test, more than Opus 5.5’s $0.75.

> Sonnet 5.5 thought so long in a single step that it hit that limit in four of five runs…

Opus 5.5 won this test. Both models fixed every bug, but Opus 5.5 finished about 35% faster and, counting Sonnet 5.5’s failed runs, cost less per run.

### Resolver spec

Sonnet 5.5 won this one. Both models passed all 120 hidden tests on all five runs, but Sonnet 5.5 got there faster and cheaper.

Sonnet 5.5 averaged 8 minutes 58 seconds, 81,097 output tokens, and $0.82 per run. Opus 5.5 averaged 9 minutes 40 seconds, 70,687 output tokens, and $1.42. Sonnet 5.5 used 15% more tokens but cost 42% less, and it finished a little faster.

### Concurrency bugs

This test surprised me most. Sonnet 5.5 fixed all three race conditions and passed all eight hidden tests on all five runs. Opus 5.5 matched it on three runs. On the other two, it spent all 128,000 output tokens thinking and never produced an answer.

Sonnet 5.5 averaged 12 minutes 13 seconds, 101,788 output tokens, and $1.02 per run. Opus 5.5 averaged 16 minutes 43 seconds, 111,428 output tokens, and $2.24 per run, including failures.

Sonnet 5.5 won this test clearly. It was perfect every time, faster, and less than half the cost.

## Results

|  |  |  |
| --- | --- | --- |
| Test (5 runs each) | Sonnet 5.5 | Opus 5.5 |
| Agentic bug fix | 5/5 perfect, 5:08, 42,608 out, 29 tool calls, $0.70 | 5/5 perfect, 3:21, 20,625 out, 25 tool calls, $0.75 |
| Resolver spec | 5/5 perfect, 8:58, 81,097 out, $0.82 | 5/5 perfect, 9:40, 70,687 out, $1.42 |
| Concurrency bugs | 5/5 perfect, 12:13, 101,788 out, $1.02 | 3/5 perfect, 16:43, 111,428 out, $2.24 |
| Perfect runs | 15 of 15 | 13 of 15 |
| Total time, 15 runs | 2:11:36 | 2:28:39 |
| Total cost, 15 runs | $12.69 | $22.07 |

Sonnet 5.5 was perfect on all 15 runs, and Opus 5.5 was perfect on 13, with both of its misses on the concurrency test. Sonnet 5.5 cost $12.69 to Opus 5.5’s $22.07, 42% less. Counting its four redone runs, it cost $14.09, still about 36% less. It also finished all 15 runs 11% faster overall. It won the resolver and concurrency tests. Opus 5.5 won the agentic test, finishing about 35% faster while Sonnet 5.5 used twice as many tokens.

These results surprised me. I definitely thought Opus 5.5 would do better than Sonnet 5.5.

## What I think

Artificial Analysis found Sonnet 5.5 costs more per task than Opus 5.5 at max effort, while scoring slightly lower on its Intelligence Index. That didn’t happen in my tests. Sonnet 5.5 was the more accurate model, and even counting the four runs I had to redo, it cost about 36% less than Opus 5.5 overall.

Half the price still didn’t mean half the bill. Sonnet 5.5 often needed more tokens to finish, so it came out about 36% cheaper overall, not 50%.

Use Sonnet 5.5 as your default for hard-coding work. It was perfect on every run once I raised its output limit, so set it high, because it thinks longer per step than Opus 5.5 does. For agent loops, stick with Opus 5.5. It finished the agentic test about 35% faster and, once you count Sonnet 5.5’s failed runs, cost less.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)