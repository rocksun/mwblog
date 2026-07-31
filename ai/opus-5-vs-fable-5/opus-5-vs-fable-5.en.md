Anthropic [released Claude Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/) last week, with this pitch: It comes “close to the frontier intelligence of Claude Fable 5 at half the price.”

Opus 5 runs $5 per million input tokens and $25 per million output tokens, unchanged from Opus 4.8. Meanwhile, Fable 5 runs $10 and $50. It also became the default model on Claude Max, which means a lot of people started using it whether they noticed or not.

Anthropic compared the two and reported Opus 5 winning eight of them. It also published a sentence that most of the launch coverage skipped past. “Claude Opus 5 is not more capable overall than our most capable general-access model, Claude Fable 5.”

I was confused. Is Opus 5 *better*, *cheaper*, or *the same* as Fable 5? I had to get to the bottom of this, so I ran all reasoning-based tasks. Since differences between the two models seem hard to identify, I decided to test reasoning tasks because, in my opinion, those are the hardest tasks for AI models to complete successfully.

| Benchmark | Opus 5 | Fable 5 | Opus 4.8 | GPT-5.6 Sol |
| --- | --- | --- | --- | --- |
| **Agentic terminal coding** Frontier-Bench v0.1 | **43.3%** | 33.7% | 18.7% | 37.5% |
| **Knowledge work** GDPval-AA v2 | **1861** | 1747 | 1593 | 1736 |
| **Agentic search** BrowseComp | **90.8%** | 87.4% | 84.3% | 90.4% |
| **Multidisciplinary reasoning** Humanity’s Last Exam | 56.3% no tools  **64.7%** with tools | **56.5%** no tools  63.9% with tools | 49.8% no tools  57.9% with tools | —  — |
| **Computer use** OSWorld 2.0 | **70.6%** | 66.1% | 55.7% | 62.6% |
| **Agentic coding** DeepSWE v1.1 | 68.8% | 69.7% | 59.0% | **72.7%** |
| **Agentic coding** FrontierCode v1.1, Main | **53.4%** | 53.5% | 46.5% | 47.5% |
| **Business workflows** AutomationBench | **26.0%** | 17.4% | 17.0% | 18.1% |
| **Legal** Legal Agent Benchmark, Held-out | 11.7% | **13.3%** | 10.4% | 2.5% |
| **Health** HealthBench Professional | 59.8% | Mythos 5 **66.0%** | 57.4% | 60.5% |
| **Biology** BioMysteryBench | **49.4%** hard  **90.1%** human solved | 46.5% hard  Mythos 5 89.0% human solved | 42.4% hard  88.5% human solved | —  — |

*Credit: Anthropic*



---

## The tests

I used the same prompts, fresh terminal sessions, and made sure there was no cross-contamination between models. Here are the three tests I ran (in this order):

* A diagnosis-only bug hunt on a live open source bug
* An analytics job on a financial statement I rigged with 27 planted errors
* A synthesis memo on conflicting claims in AI marketing

For every test, I recorded API time, output tokens, and cost from the /cost command in Claude Code.

## Test one: diagnosis-only bug hunt

Test one was a diagnosis-only bug hunt (I asked the models not to code anything). I used [Hypothesis](https://github.com/HypothesisWorks/hypothesis), the Python property-based testing library, and checked out version 6.130.10 where a real assertion bug was still live (issue #[4339](https://github.com/HypothesisWorks/hypothesis/issues/4339)). The bug causes a user’s test to crash with an internal assertion, which is a check Hypothesis runs on itself, so the user’s test crashes inside library code they never wrote. The bug is so nuanced that two maintainers couldn’t reproduce it themselves.

I gave each model the traceback and the reproducer and told it to work from the codebase with no web access and no code changes. The maintainers’ real fix shipped in [PR #4349](https://github.com/HypothesisWorks/hypothesis/pull/4349), so I had something to measure the models’ responses against.

Both models found the same root cause. It was a strategy built inside a composite that gets rebuilt on every test run and labeled by its memory address. The same value gets two different labels across two runs. A cleanup step compares those labels and crashes when they do not match.

Both proposed the maintainers’ fix. Fable suggested it as its first-choice fix. Opus listed it second, behind a different approach targeting the same cause one step earlier. There were two main differences in the models’ responses.

Only Fable explained the intermittency of the bug and why it was so challenging for maintainers to reproduce. Only Opus wrote code, monkeypatching a fix in memory and running the suite against it despite being told not to modify anything.

Opus finished in 14 minutes 13 seconds of API time on 58.6K output tokens for $4.90. Fable took 18 minutes 18 seconds on 68.5K tokens for $8.97.

Both models satisfied the prompt’s requirement of identifying the root cause. Fable went one step further and explained why the bug only shows up sometimes, but Opus went ahead and tested the fix. Fable wins reasoning. Opus wins attention to detail.

## Test two: the rigged spreadsheet

Test two was built to mirror a test I did on [Claude for Small Business](https://thenewstack.io/claude-small-business-test/) earlier this summer. I created a fake B2B SaaS company and built a financial statement that included seven months of numbers across eleven tabs and twenty customers.

Then I planted 27 problems ranked easy, medium, and hard. Easy problems are obvious, like a customer billed the month after they churned. Hard problems need three facts chained across separate tabs to identify. I also planted three red herrings, things that look like problems and aren’t, so that I could count false positives.

### What they did right

Both caught every hard problem I expected them to miss. They spotted the same customer entered twice under slightly different names, because the usage rows were identical to the last digit. They caught the partner account booked at full price when the notes and the invoice both say net. Both flagged the euro contract summed into dollars at one to one, and the retention table claiming nobody churned from a group that lost a customer. Neither missed the CAC number divided by trial starts instead of conversions.

Fable went one step further than Opus when it came to reasoning over the data. It rebuilt the monthly revenue numbers as they should have been reported, which showed a business that was flat to shrinking rather than growing. It then noticed that every error it found worked in the business’s favor. Fable explained this by saying, “every distortion in the reported numbers happens to flatter the business.”

### Where it went wrong

Both models missed a Simpson’s paradox in the trials funnel. That’s where self-serve trials convert at around 13% and sales-assisted at around 45%, and both rates improved over the seven months, but self-serve grew as a share of the total, so the blended rate fell from 22.5% to 16.9%. The headline says conversion is getting worse. Both channels say it is getting better.

Fable also missed a customer billed $449 against a $499 list price and flagged one downgrade without noticing the second. Both are small, checkable numbers sitting in a single tab. Neither one required the kind of thinking Fable had already proven it could do.

Opus cost $0.98 on 4 minutes 59 seconds of API time and 22.8K output tokens. Fable cost $1.76 in 4 minutes 36 seconds and 20.3K tokens.

The results of this test repeat the pattern from test one. Opus found 26 of the 27; Fable found 24. Fable is stronger when it comes to “thought” and reasoning; Opus is stronger on attention to detail.

This test also reconfirmed the same thing as the original test: You still need an expert to review financial data.

## Test three: models recommending models

Test three focused on my favorite topic, conflicting claims in AI marketing. I saved four files from this month’s launches, two vendor announcements, plus Artificial Analysis measurements and five aggregators. Every independent number in this test came from Artificial Analysis. I found 16 contradictions and asked Opus and Fable which model a developer should run. Or, to put it in other terms, can AI replace my job?

TL;DR: No.

Opus caught 15 of the conflicting claims, and Fable caught 12. I’m not going to go line by line on right vs wrong. I’ll just point out what stood out the most.

Both ruled correctly on the biggest one. Google says 3.6 Flash improves on coding and knowledge work, Artificial Analysis says it does not improve at all, and both models sided with the independent measurement. Both also caught that Google cites Artificial Analysis four times, never once for intelligence.

Like the last test, Opus pulled ahead on facts. It ran the binomial on Anthropic’s eight-of-thirteen claim and found that thirteen coin flips give eight or more heads 29% of the time. It found that Anthropic’s ten-point win came from a 74-task test, small enough that the gap could be luck. Then it noticed the test was version 0.1 and launched the same day as the model, which it called “the fingerprint of an eval developed alongside the model it validates.” Is the monster turning against Frankenstein?

Also like the last test, Fable was slightly stronger when it came to overall reasoning. Fable’s memo ran half the length of Opus’s (I love a rare short AI answer) and was the only one to point out that every independent number in those files came from one company, Artificial Analysis. Its recommendation “is one benchmark-provider failure away from needing a rewrite,” meaning if Artificial Analysis turns out to be wrong or compromised, Fable’s model recommendation becomes inaccurate.

Much to my dismay, both Opus and Fable recommended the same model, Opus 5 (more on that in the key takeaways section). Neither noticed it was an Anthropic model recommending an Anthropic model.

Opus cost $0.79 in 4 minutes 12 seconds and 18.5K output tokens. Fable cost $1.03 in 2 minutes 3 seconds and 9.5K tokens.

It’s hard to judge which was better when neither caught every conflicting claim. After seeing the same pattern in all three tests, I’m confident in saying Fable is better at reasoning, but Opus sees more of the small details. And for now, my job is safe.

## Key takeaways

Here are the results and cost chart:

|  |  |  |
| --- | --- | --- |
| **The metric** | **Opus 5** | **Fable 5** |
| Bug diagnosis | correct root cause, matches shipped fix | correct root cause, matches shipped fix |
| Analytics | 26/27, zero false positives | 24/27, zero false positives |
| Recommendations | 15/16 | 12/16 |
| Total API time | 23 min 24 s | 24 min 57 s |
| Total output tokens | 99.9k | 98.3k |
| Total cost | $6.67 | $11.76 |

One thing to note before reading that chart. Those counts measure how many items each model found, not how well it thought. Every problem Fable missed was a small, checkable number. Every insight neither model was asked for came from Fable.

> Every problem Fable missed was a small, checkable number. Every insight neither model was asked for came from Fable.

Across three tests, the two models produced nearly identical token output volume, 99.9k against 98.3k. Opus’s lower list rates explain much of the cost difference, but billable token mix and model configuration also matter. What I’d love to know (and likely never will) is what makes Opus 5 so much cheaper? Is it the build? Is it purely a play to get people to use Opus 5? Is it part of the AI freemium where it starts cheaper but becomes increasingly more expensive over time?

## What do I really think?

For my final thoughts, I’m going to look at the chart above and read between the lines. For best results, use both. And have an expert review the data.

> If the job is catching every fact in front of you, use Opus 5. It missed almost nothing across three tests and cost 43% less overall.

Reasoning still hasn’t been perfected when it comes to AI. If the job is catching every fact in front of you, use Opus 5. It missed almost nothing across three tests and cost half as much.

If the job is understanding what the facts add up to, Fable is the clear winner. It was the only model to rebuild the revenue numbers, the only one to explain why the bug was so hard to reproduce, and the only one to name the weakness in its own recommendation.

> If the job is understanding what the facts add up to, Fable is the clear winner.

But it still needs work. Fable’s two misses on the spreadsheet were basic, the kind of thing you catch by reading carefully rather than thinking hard. Reasoning can only be so strong if some facts are missing. Fable shows real potential but still needs improvements.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)