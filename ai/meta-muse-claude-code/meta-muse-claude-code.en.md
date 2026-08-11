**Meta [released Muse Code](https://thenewstack.io/meta-muse-code/) on August 5**, its first AI coding agent, built on the new Muse Spark 1.2 model. Mark Zuckerberg [says](https://siliconangle.com/2026/08/05/meta-takes-anthropic-openai-first-ai-coding-agent-muse-code/) it handles “complete software engineering tasks across large repos,” and that big jobs “fan out to separate sub-agents working in parallel.”

Meta’s AI chief Alexandr Wang was blunt about the strategy. The differentiator, he told [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html), is being “more affordable than either Claude or Codex.”

Standard muse-spark-1.2 [runs](https://dev.meta.ai/docs/muse-code/?team_id=2306091636825706&project_id=1082575054202150) $1.25 per million input tokens and $4.25 per million output. For comparison, Fable 5, the Anthropic model my Claude Code ran, lists at $10 and $50. Then there’s the “contributor” tier at $0.10 and $0.20, which Wang says is “more than 10x cheaper.”

He’s right, and here’s the fine print. Contributor means “your content may be used for product improvement.” Your code, your prompts, your sessions, all of it becomes Meta training data. And that tier isn’t buried in a settings menu somewhere. It’s the default.

So the question I tested is half of the claim Wang didn’t finish. More affordable, sure. But affordable at what quality? I gave Muse Code and Claude Code the same three coding jobs and tracked every token.

## Setting up Muse

Setup was quick. One curl command installs Muse, you log in through your regular Meta account, and it refuses to run until you attach a payment card. ([Kimi pulled the same move on me last month](https://thenewstack.io/kimi-k3-fable-coding-benchmark/). These companies will trust an AI with your codebase but not you with an invoice.) The pricing table sits on the same page where you add the card, which is where I spotted the default tier.

I ran my tests on contributor because none of my data was worth protecting. The test repo is public open source code. If your code is proprietary and you switch to the standard tier, expect bills closer to the $2 range for what cost me 6 cents.

## The tests

I used [dayjs](https://day.js.org/), the 2KB JavaScript date library that’s a standard replacement for Moment.js. It’s real production code with a 773-test suite, and date math breaks in ways you don’t notice until someone’s invoice is wrong.

Muse Code (version 0.1.0) ran the Muse Spark 1.2 contributor model. Claude Code (version 2.1.2) ran Fable 5 on a Claude Max plan. Identical prompts, a fresh folder and fresh session for every test, so the agent was the only variable. Here are the three tests I ran:

* a debugging test with three planted bugs
* a multi-file refactor
* an open-ended reasoning test

For every test I recorded time, tokens, and cost.

## Test 1: The bug hunt

**The prompt:** *This JavaScript library’s test suite is failing. Run npx jest to see the failures. Find the bugs causing the failures, fix them, and get the full suite passing. Do not modify or delete any test files, do not skip tests, and do not change any public behavior beyond fixing the bugs. Explain each bug you found and your fix.*

Before this test, I planted three subtle bugs in the library, the kind a careless refactor leaves behind, and wiped the git history so neither agent could diff its way to the answers. The bugs broke 17 of the 773 tests.

Both agents found all three and fixed them with the exact code the library originally had. A rounding error in date differences, an inverted boundary check in one plugin, and an off-by-one in the start-of-week math. Both explained each bug correctly. Muse even called them “injected bugs” in its summary. It knew it was being tested.

Fixing my three bugs wasn’t the complete test, though. On my Mac, two unrelated tests also failed, old ones with timezone assumptions baked in, and each agent had to decide what to do about failures it didn’t cause. Muse identified them, explained they weren’t real bugs, and left them alone. Reasonable. Claude found a way to make them pass without touching the test files, through a settings change. When Claude finished, the whole suite ran clean. Both agents fixed my bugs. Only Claude left behind a test suite that fully passed.

Muse finished in 2 minutes 58 seconds on 2.25 million tokens for 2 cents. Claude took 5 minutes 31 seconds on about 1.46 million tokens for $3.02.

## Test 2: The refactor

**The prompt:** *The file src/index.js contains this library’s entire core: date parsing, the Dayjs class, and all of its methods inline in one 467-line file. Refactor it to improve readability and structure: move the parsing logic and any helper logic it needs into dedicated new modules, and break the large methods into smaller focused functions. Do not change any behavior or the public API. Every existing test must still pass (run TZ=UTC npx jest to check), and ./node\_modules/.bin/eslint src/\* must report no errors.*

Both agents hit both required gates, all 773 tests passing and zero lint errors. What they built under those gates wasn’t the same thing at all.

Muse extracted one new module, a 25-line parsing file, and broke the big methods into smaller helpers inside the original file. The “monolith” went from 467 lines to 465. Claude extracted three modules, for date parsing, locale handling, and format tokens, and the core file dropped from 467 lines to 353. Claude also checked which internal files the test suite imports before moving anything, so nothing it moved could break a test by accident.

Both refactors pass. One reads like the codebase got reorganized (Claude). The other reads like it got tidied (Muse).

Muse finished in 1 minute 44 seconds on 1.18 million tokens for a penny. Claude took 6 minutes 9 seconds on about 448,000 tokens for $2.40.

## Test 3: The reasoning test

**The prompt:** *This library’s test suite passes when run with TZ=UTC npx jest, but fails when run in other time zones, for example TZ=America/New\_York npx jest and TZ=Australia/Sydney npx jest. Investigate why, decide what the right fix is, and make the full suite pass in any timezone without weakening test coverage and without changing the library’s public behavior. Explain your reasoning and the tradeoffs of the approach you chose.*

This test has no single right answer, which is why I like reasoning tests. The library’s tests pass in some timezones and fail in others, 2 failures in New York, 3 in Sydney, none in London. Each agent had to figure out why before deciding what deserved fixing. Both got it right.

The failing tests were written badly, so both rewrote them to work anywhere. And while doing that, both agents found a real bug in the library on their own, a daylight-saving mistake that shows the wrong clock time in certain timezones. Both found it, and both fixed it.

They disagreed, though, about how to repair the badly written tests. Each one explicitly rejected the approach the other chose, without knowing the other existed. Muse rewrote the tests to check dayjs against Moment.js. Claude kept the original expected values and made the tests internally consistent, arguing that fixed values catch the case where both libraries are wrong. Both positions are acceptable.

You can also see the quality differences in how the models finished the jobs. Muse deleted one assertion it considered redundant and left a few of its own edits as dead code. Claude’s changes were exact, and it ran the suite’s full coverage check on top of the required ones. I verified both agents’ work myself in seven timezones, including ones neither tested. Both held up, 773 tests passing everywhere.

Muse used 5.52 million tokens for 3 cents (I didn’t catch the timer on this run). Claude took 9 minutes 8 seconds on about 1.29 million tokens for $3.99.

## The results

|  |  |  |
| --- | --- | --- |
| **The metric** | **Muse Code** | **Claude Code** |
| Bug hunt | 3/3 bugs, suite green | 3/3 bugs, suite green in any timezone |
| Bug hunt numbers | 2m 58s, 2.25M tokens, $0.02 | 5m 31s, 1.46M tokens, $3.02 |
| Refactor | gates pass, 1 new module | gates pass, 3 new modules |
| Refactor numbers | 1m 44s, 1.18M tokens, $0.01 | 6m 9s, 448K tokens, $2.40 |
| Reasoning | Found the hidden bug, left dead code | found the hidden bug, exact |
| Reasoning numbers | time unrecorded, 5.52M tokens, $0.03 | 9m 8s, 1.29M tokens, $3.99 |
| Total tokens | ~8.9M | ~3.2M |
| Total cost (as billed) | $0.06 | $9.41 |

A few notes on that chart. Muse’s costs are contributor-tier prices. At Meta’s standard rates the same three runs work out to roughly $2, call it 5x cheaper instead of 150x. Claude’s cost is the API-equivalent price inside a Max subscription

A few notes on that chart. Muse’s costs are contributor-tier prices. At Meta’s standard rates the same three runs work out to roughly $2, call it 5x cheaper instead of 150x. Claude’s cost is the API-equivalent price inside a Max subscription. And this is three data points, not a benchmark.

### What do I really think?

On correctness, the two agents tied. Same bugs found, same gates passed. On the hardest test, both independently discovered a real library bug nobody told them about. But nobody judges an engineer’s work on surface correctness alone, so I can’t call these two equal.

Depth and polish matter too, and that’s where they split. Claude’s refactor restructured the codebase where Muse’s tidied it. Claude finished the bug hunt completely where Muse finished it adequately. Claude’s changes on the reasoning test were exact where Muse’s left dead code behind. None of that shows up in a pass/fail column. All of it shows up when someone who knows the codebase reads the diff.

> Whatever you save in tokens, you pay back in review time.

And that’s the problem with the discount. Yes, Muse is dramatically cheaper. But every Muse run in this experiment produced work that looked correct on the surface and needed an expert to know whether it was finished underneath. If you can’t run it and then trust the results, even when the tests are green, what’s the point? Whatever you save in tokens, you pay back in review time.

Wang’s affordability claim holds, and then some. The part Meta didn’t say out loud is what the affordability buys you, work that’s correct but not thorough.

Muse Code is brand new. The gap I found is the closeable kind, and Meta has closed gaps before. I’ll rerun these tests when the next model shows up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)