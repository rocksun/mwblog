**When Google announced** [Gemini 4 Argon](https://thenewstack.io/google-gemini-4-argon/) to a small group of testers on September 30, it came with a benchmark table that put Argon ahead of [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/) on 14 of 18 tests. Those include DeepSWE (77.9% vs. 74.2%) and GraphWalks at 256K to 1 million tokens (84.2% vs. 66.8%). Two weeks later, on October 13, Google opened Argon to paid Gemini API developers.

To its credit, Google also showed where Opus 5.5 wins. Opus leads on the other four benchmarks, including Terminal-bench 4.0 (66.4% vs. 57.4%), which tests agentic work in a command line.

Google is also undercutting Anthropic on price, at least for now. Through November 30, Argon costs $2 per million input tokens and $10 per million output tokens, half the price of Opus 5.5. On December 1, it rises to $4 and $20, matching Opus. That gives developers about six weeks to decide whether Argon is better or just cheaper.

> That gives developers about six weeks to decide whether Argon is better or just cheaper.

Benchmarks don’t always match real work, and a half-price window only matters if the model matches the competitor on quality. To see whether Argon is better or just cheaper (for now), I tested both models head-to-head on three hard tasks from categories where Google claims a lead.

## The tests

I ran each test once per model through OpenRouter, on Google’s and Anthropic’s own servers, at default reasoning settings. A script graded every answer against keys I built and verified before testing either model. The answer key adds more scoring areas to help ensure the quality and thoroughness of each test.

* **Bug hunt** – A 3,500-line Python library with 14 planted logic bugs and five decoys. Each model reviewed the code, then fixed what it found.
* **Billing spec** – A spec for a subscription billing engine, graded by 80 hidden tests on daylight saving, month-end dates, and rounding. A follow-up added two currencies and 20 more tests.
* **Long context** – A fake wiki of 400 services with scattered dependencies, at three sizes. Each model answered three graph questions with planted traps.

### Bug hunt

This one was a tie. Both models found all 14 bugs, including four that only show up when you follow a value across three or more files. Neither flagged a decoy. In the follow-up, both fixed all 14 bugs without breaking any of the 93 existing tests.

Argon was cheaper. Its review cost averaged 1 cent per bug found, compared to Opus’s 2.4 cents, an average I calculated from the per-call total rather than measured per bug. Argon would still come out cheaper at its full Dec. 1 price, because it used fewer tokens.

* The numbers:
  + Review
    - Argon 53,031 in, 3,964 out, $0.15, 43.0 s.
    - Opus 64,572 in, 4,053 out, $0.34, 38.9 s.
  + Fix
    - Argon 54,923 in, 24,292 out, $0.35, 186.6 s.
    - Opus 66,465 in, 34,263 out, $0.95, 219.8 s.

## Billing specs

Here’s where accuracy began to differ between the two models. Opus passed all 80 hidden tests, then all 100 after the currency follow-up. Argon passed 11 of 80, then 20 of 100.  
  
Argon didn’t fail the majority of the tests because its logic was bad. It failed because it made a small mistake early on. Its code passed an extra argument to Python’s `datetime.combine()`, which raises an error, and most of the module depends on that helper. When I corrected that one line myself, Argon scored 80/80 and 100/100. I kept the official scores as graded but wanted to explain what happened, not just list the scores, on this one.

Overall, Argon was cheaper, but the difference between Opus and Argon pricing will disappear once the lower-cost period ends, though Argon’s lower token use would still make it cheaper on this test.

* The numbers:
  + Build
    - Argon 3,907 in, 3,727 out, $0.05, 54.1 s.
    - Opus 5,236 in, 7,763 out, $0.18, 63.0 s.
  + Follow-up
    - Argon 8,881 in, 4,673 out, $0.06, 41.5 s.
    - Opus 11,807 in, 7,267 out, $0.19, 51.9 s.

## Long context

Each vendor counts tokens differently. My 500K document came to 549,483 tokens on Argon and 784,087 on Opus. My 900K document came to 1.4 million tokens on Claude’s tokenizer, so Anthropic’s API rejected it. I added a third document of about 600K tokens, the largest that both models could fit.

Both models answered two of the three questions perfectly at every size they ran. The split came on the blast radius question, which asks for every service that goes down when one fails. The answer is 33 services.

Opus got all 33 at 500K and 32 at 600K, with no wrong entries. At 500K, Argon got 20 right and 8 wrong; at 600K, 19 right and 16 wrong; and at 900K, 23 right and 2 wrong. At 600K and 900K, it treated a dependency as removed after the wiki reinstated it. Unlike the billing bug, this wasn’t a small slip. Argon got the reasoning wrong at every size. This is a big red flag.

> Unlike the billing bug, this wasn’t a small slip. Argon got the reasoning wrong across the entire answer. This is a big red flag.

Another thing I noticed is that Argon raced through this long-context test. Argon answered quickly without showing any step-by-step work, and Opus took longer because it reasoned first. This shows up in token usage. Opus used over 5,000 tokens, most for reasoning, vs. Argon’s 243-425. That likely connects to Argon’s wrong answers, though I can’t prove the cause from one run.

Argon was cheaper here, but it’s not worth using it on a similar task, as it was largely inaccurate and sloppy.

* The numbers:
  + 500k
    - Argon 549,483 in, 264 out, $1.10, 24.2 s.
    - Opus 784,087 in, 5,532 out, $3.25, 68.3 s.
  + 600k
    - Argon 652,492 in, 425 out, $1.31, 32.4 s.
    - Opus 935,332 in, 5,158 out, $3.84, 69.1 s.
  + 900K
    - Argon 982,367 in, 243 out, $1.97, 41.5 s.
    - Opus not run.

## Results

|  |  |  |
| --- | --- | --- |
| **Test** | **[Gemini 4 Argon](https://thenewstack.io/google-gemini-4-argon/)** | **[Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/)** |
| Bug hunt review | 14 of 14, 0 false positives | 14 of 14, 0 false positives |
| Bug hunt fix | 14 of 14, 93 of 93 tests kept | 14 of 14, 93 of 93 tests kept |
| Billing spec | 11 of 80 | 80 of 80 |
| Billing follow-up | 20 of 100 | 100 of 100 |
| Blast radius, 500K | 20 of 33, 8 wrong | 33 of 33 |
| Blast radius, 600K | 19 of 33, 16 wrong | 32 of 33 |
| Blast radius, 900K | 23 of 33, 2 wrong | Rejected, over 1M tokens |
| Total tokens in / out | 2,305,084 / 37,588 | 1,867,499 / 64,036 |
| Total cost | $4.98 | $8.75 |
| Total time | 423.3 s | 511.0 s |

My results didn’t match Google’s benchmarks. Argon tied Opus on code review and fixing at under half the cost. It lost the spec test over one bad line of code, and it missed or invented services on every long-context blast-radius question.

## What do I think?

Based on these tests, I wouldn’t use Argon. Yes, it was cheaper and as accurate as Opus on the bug hunt, but after working with it on the other tests, I wouldn’t unquestioningly trust Argon on any task.

> I wouldn’t unquestioningly trust Argon on any task.

Opus 5.5 is one of Anthropic’s leading models, and Artificial Analysis’s independent index ranks it at 58, ahead of Argon’s 53.

While Google is working hard to catch up, it hasn’t yet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)