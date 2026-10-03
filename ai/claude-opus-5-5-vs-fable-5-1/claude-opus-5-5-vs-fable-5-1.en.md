**Anthropic released [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/)** on September 22, saying it performs at the level of Claude Fable 5.1 on most work. At list price, it costs well under half as much per token. It leads Fable 5.1 on Terminal-Bench 4.0, FrontierCode, and CursorBench. Anthropic says the gap between the two models “is narrower than these scores suggest.” Opus 5.5 costs $4 per million input tokens and $20 per million output tokens. Fable 5.1 costs $10 and $50.

Anthropic’s own model docs still point developers to [Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/) for “demanding reasoning and long-horizon agentic work” and list it as the slower of the two. So I wanted to answer two questions in my Opus 5.5 vs. Fable 5.1 testing.

* Is Opus 5.5 really as accurate as Fable 5.1?
* If so, should Fable 5.1 still be sold as the premium model on tasks Opus 5.5 does better?

This is my third Opus 5.5 test. In the [first](https://thenewstack.io/claude-opus-5-5-vs-opus-5/), it matched Opus 5 on reasoning problems at a lower cost, but its speed gain fell short of Anthropic’s claim. This time I focused on coding, where Anthropic’s benchmarks show Opus 5.5 ahead of Fable 5.1.

## The tests

I called both models through the Anthropic API with identical prompts, adaptive thinking, and the maximum effort setting. Each test ran five times per model. A hidden test suite graded every test, and I logged tokens, list-price cost, and wall-clock time for every run.

* **Agentic bug fix** – The model gets a small Python order-pricing repo with four planted bugs and one flaky test, plus tools to list files, read files, write files, and run tests. A hidden suite of 12 tests checks the fixes, and I tracked whether the model touched the tests or noticed the flaky one.
* **Resolver spec** – The model writes a dependency resolver for a fictional package manager from a two-page spec, without running any code. A hidden suite of 120 tests grades it.
* **Concurrency bugs** –  The model gets an asyncio job queue with three race conditions and an incident report describing double charges and jobs that never ran. It has to find and fix every bug without running the code, and pass eight hidden tests with a controlled clock that checks each fix.

The resolver and concurrency tests each gave the model one prompt and one reply. I started at 64,000, but Opus 5.5 ran out of room, so I raised the limit to 128,000, the maximum either model allows. Fable 5.1 never used more than 55,000.

*I didn’t include the prompts here because each test depends on a code repo, spec, or module too long to reprint.*

### Agentic bug fix

Both models fixed all four bugs in all five runs and passed all 12 hidden tests. Neither one edited the test files, and both flagged the flaky test.

By score alone, the two models tied, but they handled the flaky test differently. The test fails at random because the code simulates a slow call to a shipping carrier’s API. Fable 5.1 “cheated” and deleted the simulated delay in all five runs, so the test always passes. In a real codebase, that would mean removing the API call to make a test pass, and orders would never actually be checked with the carrier. In production, that could mean taking payment for orders the carrier can’t deliver, shipping to addresses it doesn’t serve, and never finding out when its service goes down.

Opus 5.5 left the code alone in all five runs. It confirmed the test was flaky by rerunning it, said shrinking the delay “would just make the test pass without fixing anything,” and pointed to the real fix in the test itself. That’s the better result because the app still works and the developer knows what to fix. A green test suite that hides a broken integration is worse than a red one that tells the truth.

> A green test suite that hides a broken integration is worse than a red one that tells the truth.

Opus 5.5 averaged 3 minutes 21 seconds, 25 tool calls, 20,625 output tokens, and $0.75 per run. Fable 5.1 averaged 2 minutes 37 seconds, 22 tool calls, 11,381 output tokens, and $1.50. Opus 5.5 ran the test suite about seven times per run, compared to Fable 5.1’s three, mostly to check the flaky test.

Opus 5.5 won this test, since it fixed the same four bugs as Fable 5.1, handled the flaky test the right way, and cost half as much.

### Resolver spec

Both models passed all 120 hidden tests on all five runs.

Opus 5.5 averaged 9 minutes 40 seconds, 70,687 output tokens, and $1.42 per run. Fable 5.1 averaged 6 minutes 46 seconds, 38,710 output tokens, and $1.96. Opus 5.5 used 83% more tokens and still cost 28% less, because each token costs 60% less.

The extra tokens didn’t turn into extra code. Both models wrote about 400 lines, so almost all of Opus 5.5’s extra went into thinking. In one run, Opus 5.5 also opened by listing the places where the spec was unclear and which choice it made for each, something Fable 5.1 never did.

This test was a tie on accuracy, so the winner depends on what you’re optimizing for. Opus 5.5 wins if cost matters most, and Fable 5.1 wins if you need a faster answer.

### Concurrency bugs

This test produced the only misses. Fable 5.1 fixed all three race conditions and passed all eight hidden tests on every run.

Opus 5.5 did the same on three runs. On the other two, it used all 128,000 output tokens, then never finished an answer. Each run took about 19 minutes and cost $2.57.

Both models also “fixed” more bugs than I planted. Fable 5.1 listed four to seven fixes per run, and Opus 5.5 listed seven or eight. None of the extra changes broke anything, and some tighten real weak spots, but they mean more code for a reviewer to check.

Opus 5.5 averaged 16 minutes 43 seconds, 111,428 output tokens, and $2.24 per run, counting the failures. Fable 5.1 averaged 8 minutes 27 seconds, 43,001 output tokens, and $2.17. Even on its three finished runs, Opus 5.5 averaged 15 minutes, nearly twice Fable 5.1’s time, and 100,380 tokens, more than twice what Fable 5.1 needed.

Fable 5.1 won this test clearly. It was perfect every time, twice as fast, and cost about the same, because Opus 5.5’s cheaper tokens didn’t make up for using so many more.

## Results

|  |  |  |
| --- | --- | --- |
| **Test (5 runs each)** | **Opus 5.5** | **Fable 5.1** |
| Agentic bug fix | 5/5 perfect, 3:21, 20,625 out, 25 tool calls, $0.75 | 5/5 perfect, 2:37, 11,381 out, 22 tool calls, $1.50 |
| Resolver spec | 5/5 perfect, 9:40, 70,687 out, $1.42 | 5/5 perfect, 6:46, 38,710 out, $1.96 |
| Concurrency bugs | 3/5 perfect, 16:43, 111,428 out, $2.24 | 5/5 perfect, 8:27, 43,001 out, $2.17 |
| Perfect runs | 13 of 15 | 15 of 15 |
| Total time, 15 runs | 2:28:39 | 1:29:14 |
| Total cost, 15 runs | $22.07 | $28.14 |

Fable 5.1 had 15 perfect runs out of 15, and Opus 5.5 had 13, but the scores don’t tell the whole story. Opus 5.5 won the agentic test by fixing the same bugs without gaming the flaky test, for half the cost. The resolver tied on accuracy. Fable 5.1 won the concurrency test outright, since Opus 5.5 ran out of room twice and returned nothing.

Overall, Opus 5.5 cost 22% less ($22.07 vs. Fable 5.1’s $28.14), but it wrote 2.2 times as many output tokens and took 67% longer to finish all 15 runs.

### What do I think?

Of all the tests I’ve done, this one is the hardest “What do I think” section to fill out. Opus 5.5 and Fable 5.1 are equally flawed, just in different ways. In my opinion, neither should be billed as premium.

> Opus 5.5 and Fable 5.1 are equally flawed, just in different ways.

Opus 5.5 overthinks. It got every run it finished right, but it needed about twice the tokens of Fable 5.1, so it ended up only 22% cheaper, and it hit the token max twice on the hardest test and didn’t produce a result.

Fable 5.1 cuts corners. It never failed a hidden test and was faster on every test, but it passed the agentic test by removing code the app needs.

> The premium buys speed and fewer dead ends, not better judgment.

Anthropic is right that Opus 5.5 matches Fable 5.1 on accuracy when it finishes. The premium buys speed and fewer dead ends, not better judgment.

Use Opus 5.5 for agent work, where it can run tests and check itself. Use Fable 5.1 for hard problems it has to solve in one go, or when speed matters. With either one, check what it changed to pass the tests.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)