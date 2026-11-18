![Gold and green 3D spheres with cut-out holes linked by ribbons, evoking a Claude Fable 5.2 vs. Opus 5.5 comparison](https://cdn.thenewstack.io/media/2026/11/fd7d63c5-steve-a-johnson-cnkk7hrczto-unsplash-1024x576.jpg)

**Anthropic [released Claude Fable 5.2](https://thenewstack.io/anthropic-fable-coding-upgrade/) on November 9** and said it beats [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/) in almost every capability the company measured. In the same announcement, it [recommended starting with Opus](https://www.anthropic.com/claude-fable-and-mythos-5-2) for most coding and knowledge tasks, calling it its “strongest daily driver.” I wanted to find out why a company would steer people away from its best model, and whether the cheaper one really is enough.

> …why a company would steer people away from its best model, and whether the cheaper one really is enough.

On [Anthropic’s coding benchmarks](https://www.anthropic.com/claude-fable-and-mythos-5-2), Fable 5.2 scored 49.1% at Xhigh effort on FrontierCode 2.0, compared with 45.5% for Opus 5.5 at Max. Anthropic also reports that Fable scored 45.3% at High effort at roughly half the cost per task of that Opus run. On FrontierSWE v2, the company reports 69.9% for Fable and 62.3% for Opus. Fable’s [standard API rates](https://platform.claude.com/docs/en/models/opus-5-5/overview) are twice Opus’s: $8 per million uncached input tokens and $40 per million output tokens, versus $4 and $20.

Twice the price should make a meaningful difference, so I gave both models three coding and agent jobs and measured how well they did, how many tokens they used, what they cost, and how long they took. My tests are much smaller than Anthropic’s benchmarks and can’t prove or disprove those scores.

## The tests

I ran each model once per test through Anthropic’s API at default settings, with no turn cap. Anthropic’s API defaults on Fable and Opus aren’t equal. Fable 5.2 runs at high effort, and Opus 5.5 runs at medium, so these results show what a developer gets without tuning anything. I used a script to grade each answer the model gave for each test. The dollar figures are estimated API costs based on reported token usage. Anthropic [prices](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#pricing) uncached input, cache reads, cache writes, and output separately.

Here are the tests I ran:

* **Cron scheduler**: I gave each model a written spec for code that runs when the next scheduled job runs, then sent a change request. I used a hidden suite of 50 tests to grade the final code.
* **Invoicing repo fix**: Each model worked as an agent in a small invoicing library with interacting bugs in rounding, discounts, tax, and shipping. The library also had one wrong test that the model should report but not edit.
* **Incident investigation**: Each model used a terminal to find the cause of a payments outage from logs, metrics, and deployment records. The data included decoy deploys and servers with wrong clocks.

The models tied with perfect scores on the first version of every test, so I made each test harder and reran it twice.

### Cron scheduler

This test checks whether a model can turn a detailed spec into correct code and then absorb a change without breaking it. Here’s what differed between the versions.

* **Version 1**: The spec covered standard cron schedules, such as every 15 minutes or weekdays at 9 a.m.
* **Version 2**: I added rules like “the weekday nearest the 15th” and “the last Friday of the month,” and the change request reversed how two fields combine.
* **Version 3**: The code had to handle time zones and daylight saving time by hand, without Python’s time zone library.

Both models scored 50/50 on all three versions. The difference was in how much work each one did to get there. Fable 5.2 wrote two to three times as much reasoning as Opus 5.5 on every version. The extra reasoning did not raise Fable’s score on any of the three versions.

> The extra reasoning did not raise Fable’s score on any of the three versions.

Across the three scheduler versions, Opus matched Fable’s scores in 358 seconds versus 661 and cost an estimated $0.99 versus $3.29.

The numbers:

* Version 1
  + **Fable 5.2**: 2 turns, 14,471 in, 18,732 out (11,122 reasoning), $0.87, 170 s.
  + **Opus 5.5**: 2 turns, 8,055 in, 9,431 out (3,846 reasoning), $0.22, 80 s.
* Version 2
  + **Fable 5.2**: 2 turns, 20,215 in, 23,990 out (14,627 reasoning), $1.12, 226 s.
  + **Opus 5.5**: 2 turns, 14,090 in, 15,991 out (6,695 reasoning), $0.38, 131 s.
* Version 3
  + **Fable 5.2**: 2 turns, 21,121 in, 28,254 out (17,452 reasoning), $1.30, 265 s.
  + **Opus 5.5**: 2 turns, 12,651 in, 17,205 out (6,533 reasoning), $0.39, 147 s.

### Invoicing repo fix

This bug hunt is similar to the work agents do for developers daily. Here’s how I adjusted the tests with each round:

* **Version 1**: The library had bugs in rounding, discounts, tax, and shipping. It also had one wrong test.
* **Version 2**: I added buy-two-get-one promotions, weight-based shipping, and refunds, each with its own bugs.
* **Version 3**: I added currency conversion and invoice numbering, again with bugs.

This test produced the widest gap in cost and time between the two models. Both models scored 50 of 50 on all three versions, fixing the bugs the grader covered and reporting the wrong test without editing it. Opus 5.5 used fewer reasoning tokens on every version. It finished each version in under a minute, while Fable 5.2 took about one minute and 46 seconds to just under four minutes and cost eight times as much across the three.

On these runs, Fable’s extra reasoning didn’t improve its score.

The numbers:

* Version 1
  + **Fable 5.2**: 4 turns, 17,585 in, 11,511 out (5,909 reasoning), $0.58, 106 s.
  + **Opus 5.5**: 4 turns, 10,585 in, 2,975 out (519 reasoning), $0.09, 28 s.
* Version 2
  + **Fable 5.2**: 6 turns, 88,697 in, 25,980 out (11,820 reasoning), $1.39, 223 s.
  + **Opus 5.5**: 4 turns, 13,938 in, 4,457 out (777 reasoning), $0.13, 39 s.
* Version 3
  + **Fable 5.2**: 4 turns, 29,660 in, 24,020 out (14,022 reasoning), $1.18, 214 s.
  + **Opus 5.5**: 5 turns, 24,208 in, 6,013 out (1,178 reasoning), $0.17, 51 s.

### Incident investigation

This test rewards careful digging more than fast coding, so I expected it to favor Fable 5.2.

Here are the changes I made for each test version.

* **Version 1**: The outage data had decoy deploys and one server whose clock ran seven minutes slow.
* **Version 2**: I added a clock that was corrected partway through the incident, retried requests, a compressed log file, and duplicated log lines.
* **Version 3**: I added a server that logged in Chicago time and an unrelated error spike inside the incident window.

Both models scored perfectly (50 out of 50) across all three versions. Fable 5.2 took fewer turns in every version, 9 to 11 versus Opus 5.5’s 12 to 14. Across all three versions, Fable’s estimated cost was $2.54 versus Opus’s $0.91.

The numbers:

* Version 1
  + Fable 5.2: 9 turns, 155,925 in, 14,309 out (8,638 reasoning), $0.94, 143 s.
  + Opus 5.5: 12 turns, 111,618 in, 7,405 out (2,801 reasoning), $0.25, 73 s.
* Version 2
  + Fable 5.2: 11 turns, 168,913 in, 9,416 out (3,551 reasoning), $0.68, 105 s.
  + Opus 5.5: 13 turns, 188,846 in, 7,218 out (2,518 reasoning), $0.32, 82 s.
* Version 3
  + Fable 5.2: 10 turns, 205,601 in, 11,887 out (4,474 reasoning), $0.92, 127 s.
  + Opus 5.5: 14 turns, 253,958 in, 7,598 out (2,041 reasoning), $0.34, 70 s.

## Results

|  |  |  |
| --- | --- | --- |
| **Test** | **Claude Fable 5.2** | **Claude Opus 5.5** |
| Cron scheduler, 3 versions (of 150) | 150 | 150 |
| Invoicing repo fix, 3 versions (of 150) | 150 | 150 |
| Incident investigation, 3 versions (of 150) | 150 | 150 |
| Total tokens in / out | 722,188 / 168,099 | 637,949 / 78,293 |
| Total estimated cost (sum of displayed estimates) | $8.98 | $2.29 |
| Total time | 1,579 s | 701 s |

The scores were identical across all nine runs per model. Fable 5.2 cost almost four times as much and took more than twice as long.

### What do I think?

These tests give me a reason to start with Opus 5.5 for work like this. It matched Fable 5.2’s score and finished faster on every version, at about a quarter of the estimated cost overall.

That doesn’t make Fable 5.2 a bad model. My tests were hard but short. Anthropic recommends Fable for more open-ended technical work. I tested each model at its API default, so the comparison leaves open how much of the gap comes from the different effort settings.

I’d start with Opus 5.5 and move up to Fable 5.2 only when Opus stops producing ideal results.

The post [Claude Fable 5.2 vs. Opus 5.5: Same scores at almost 4x the cost](https://thenewstack.io/claude-fable-5-2-vs-opus-5-5/) appeared first on [The New Stack](https://thenewstack.io).