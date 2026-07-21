Moonshot AI [released Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/) in mid-July, selling it as a serious professional coding tool that competes head-on with Claude and GPT, at a lower price. It’s a 2.8-trillion-parameter open-weight model, the largest ever out of China. The company says it rivals Anthropic’s [Opus 4.8](https://thenewstack.io/claude-opus-48-release/).

The Kimi K3 API runs $3 per million input tokens and $15 per million output. Anthropic’s top model, Fable 5, costs $10 per million input tokens and $50 per million output. That’s more than three times the price for both input and output.

A model that costs a third as much is only a good deal if the output and user experience meet current expectations. To find out where Kimi K3 stands against the professional tools it’s chasing, I gave Kimi K3 and Fable 5 the same three real coding jobs and tracked every token.

***See also:** [Kimi K3 tops Arena’s coding leaderboard — and it’s open-weight](https://thenewstack.io/kimi-k3-open-weight-coding/)*

## The tests

I used [fd](https://github.com/sharkdp/fd), the Rust file-finder from sharkdp. fd is a fast, friendlier replacement for the Unix find command. I chose it because it is real production Rust with a deep, documented bug history to pull from.

Kimi K3 is not available in coding tools like Cursor yet, so I completed the three tests using native CLIs. I ran Kimi K3 inside Moonshot’s new Kimi Code terminal agent (version 0.27.0), and Fable 5 inside Claude Code (version 2.1.212). I used identical prompts, so the model and CLIs were the only variables. I built a new folder for each test on each model (six total), so each test was standalone.

Here are the three tests I ran (in this order):

* a bug fix
* a multi-file refactor
* a feature build

For every test, I recorded time (using a stopwatch), tokens, and cost from Cursor’s usage dashboard.

*Earlier this week, I ran Grok 4.5 against Claude Opus 4.8 on the same three tasks in the same repo using identical prompts, which you can read here [add link]. Since all four models ran the same tests, you could consider this pair of articles Fable vs Kimi vs Opus vs Grok.*

### Setting up Kimi

This was a very easy setup. The Kimi Code CLI installed with one curl command, and the account setup was simple. There was one hiccup, though. My test command of “say hello” hung for a few minutes without a reply or an error message. The cause showed up later as a 429 error. My brand-new API account had no balance, and Kimi won’t respond until you add a card and top up. The nice surprise was that once I recharged, Moonshot gave me a $5 signup voucher, so new accounts do get some free credit.

> Moonshot AI’s Kimi K3 matched Anthropic’s Fable 5 line for line on three real coding tasks and cost a third as much… but took four times as long to do it.

(I couldn’t write this post without saying the one thing that’s been on my mind during the test. The name Kimi K kept putting Kim Kardashian in my head. I never think about Kim Kardashian. I have now thought about her for two days straight.)

## Test 1: The bug fix

The prompt:

*There is a bug in this codebase (the fd command-line tool). When you pass the –no-ignore-vcs flag, fd also stops respecting ignore files in parent directories. It should not do that. Find the root cause and fix it so –no-ignore-vcs no longer disables parent-directory ignore files. Do not change any other behavior.*

I checked out fd at the commit right before the real 2021 fix for this bug (issue #907) and wiped the git history so neither model could look up the maintainers’ answer. Both models found the root cause and removed the same single line from src/main.rs. The diffs were byte-for-byte identical. Four models, four identical diffs. All 70 tests passed for both.

The difference came down to numbers. Fable finished in 1 minute 4 seconds on about 347K tokens and cost $0.85. Kimi took 3 minutes 7 seconds on 238K tokens and cost six cents. K3’s bug test was the lowest cost but highest time I’ve seen on this test.

## Test 2: The refactor

The prompt:

*In src/main.rs, the construct\_config function is large and does most of its work inline. Refactor it to improve readability and structure: move it, along with any helper logic it needs, into a dedicated new module (for example src/config\_builder.rs), and break the work into smaller focused functions. Do not change any behavior. Every existing test must still pass, and the CLI must behave exactly the same.*

Both models did the same thing: a new `config_builder.rs` module, the big function split into focused helpers, all 264 tests green, diffs within a few dozen lines of each other in size.

The results were the same, but the engineering process wasn’t. Kimi was the more thorough engineer. It snapshotted the old binary before touching anything, then diffed the old and new binaries across roughly 40 CLI scenarios to prove behavior had not changed.

But this came at the cost of efficient time. It took 14 minutes 50 seconds on 928K tokens, the slowest run of any model on any test I’ve run in the last few months. Fable did the same refactor in 3 minutes 11 seconds on about 639K tokens. Kimi cost $0.70, Fable $2.32.

This tells a similar story to the last test. Same results, lower cost, longer time.

## Test 3: The feature build

The prompt:

*Add a new –count flag to fd (the command-line file finder). When –count is passed, fd should not print the matching paths. Instead, it prints a single line: the total number of entries that matched, respecting all the usual filters (so for example “fd –count –extension rs” prints how many .rs files matched). Add the flag to the CLI, wire it through the search and output path, and make sure all existing behavior and tests still pass.*

Both delivered a correct, working `--count flag`. Kimi touched six files and updated the man page. Fable touched seven and went one step further, updating the `zsh` shell completions too. Fable miscounted the test environment twice while writing its own test, guessed 13, then 10, then landed on 11, but it caught and fixed itself both times without my help.

Kimi took almost 5x longer than Fable to deliver the `--count flag`. Their times, tokens, and costs were 10 minutes 21 seconds, 2.1 million tokens, $1.38, and 2 minutes 34 seconds, about 1.46 million tokens, $2.81, respectively.

## The results

|  |  |  |
| --- | --- | --- |
| **The metric** | **Kimi K3** | **Fable 5** |
| Bug fix | identical fix, 70/70 tests | identical fix, 70/70 tests |
| Refactor | 264/264 tests | 264/264 tests |
| Feature | correct, 6 files | correct, 7 files |
| Total time | ~28 min 18 s | ~6 min 49 s |
| Total tokens | ~3.3M | ~2.4M |
| Total cost | $2.13 | $5.98 |

Across the three jobs, Kimi cost $2.13 to Fable’s $5.98, almost exactly a third of the price that Moonshot’s rates promise. But the discount comes from the discounted rates alone. Kimi used more tokens than Fable, 3.3 million to 2.4 million. Then there’s the time cost. Fable finished all three jobs in under 7 minutes. Kimi needed just over 28. I run different tests on models weekly, and this was by far the longest time I’ve seen.

So what do I really think about Kimi? The results are solid, but this is a crowded market with established frontrunners. We’re still in the AI freemium era, so lower costs matter, just not nearly as much as speed. Kimi will need to match the speeds of the other models to compete, which means cutting its time by 5x in some cases.

It’s also worth remembering we’re in the land of done is better than perfect. This is the first public iteration of K3, and it will change.

I don’t see a place for it in the current landscape, but I’m interested in watching it improve over the next few months. Will it speed up enough to earn its seat at the table? I look forward to Moonshot’s next batch of updates so we can benchmark again and find out.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/b0ce81f3-cropped-5f5868db-nick-luchessi-2-600x600.png)

Nick Lucchesi serves as the editor-in-chief of The New Stack, where he directs editorial strategy and oversees coverage of the technologies and professionals driving software development, deployment and management at scale. Before joining The New Stack, Lucchesi held the position...

Read more from Nick Lucchesi](https://thenewstack.io/author/nick-lucchesi/)