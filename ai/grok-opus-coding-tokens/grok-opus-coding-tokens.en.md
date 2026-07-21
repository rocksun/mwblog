Can Grok 4.5 really match Opus for a quarter of the tokens?

xAI released [Grok 4.5](https://thenewstack.io/grok-45-opus-killer-launch/) on July 8. It was trained with Cursor session data added in training. xAI says the model roughly matches Claude [Opus 4.8](https://thenewstack.io/claude-opus-48-release/) on coding. It just uses about [4.2 times fewer output tokens](https://x.ai/news/grok-4-5) to do it. xAI’s pitch is aimed straight at developers now watching their token spend.

Grok is also cheaper to run out of the box. It costs $2 per million input tokens and $6 per million output. Opus is $5 and $25. That is less than half the price on both.

> xAI says Grok 4.5 matches Opus 4.8 on real coding for a fraction of the tokens. I gave both the same three jobs in one Rust repo. Both models wrote nearly identical code but Opus used 4.3 times more tokens.

The benchmarks mostly back xAI’s marketing. [Terminal-Bench 2.1](https://x.ai/news/grok-4-5) measures how well a model handles real work at the command line. There, xAI puts Grok 4.5 at 83.3%, just above Opus 4.8’s 78.9%. SWE-Bench Pro is the harder one. It scores how well a model fixes real bugs pulled from open-source projects. On that test, Opus still wins. So the marketing claim is not “better.” It is “as good, for far less.”

Just by reading these benchmarks and looking at pricing, it appears as if xAI wants to take some of Anthropic’s market share. Anthropic is the current fan favorite when it comes to AI companies, so for this to become a possibility, the marketing claims will need to hold up.

> So the marketing claim is not “better.” It is “as good, for far less.”

In pursuit of this answer, I put Grok 4.5 and Claude Opus 4.8 head-to-head on three jobs in the same codebase and tracked every token.

## The tests

I used [fd](https://github.com/sharkdp/fd), the popular Rust file-finder from sharkdp. fd is a fast, friendlier replacement for the Unix find command, and I chose it because it is real production Rust with a deep, documented bug history to pull from.

Grok and Opus both ran inside Cursor in Agent mode. The tool and the prompts stayed identical, so the model was the only variable. I built a new folder for each test on each model (six total), so each test was a stand-alone test.

Here are the three tests I ran (in this order):

* a bug fix
* a multi-file refactor
* a feature build

For every test, I recorded time (using a stopwatch), tokens, and cost from Cursor’s usage dashboard.

### Test 1: The bug fix

The prompt:

*There is a bug in this codebase (the fd command-line tool). When you pass the –no-ignore-vcs flag, fd also stops respecting ignore files in parent directories. It should not do that. Find the root cause and fix it so –no-ignore-vcs no longer disables parent-directory ignore files. Do not change any other behavior.*

For the bug fix, I checked out fd at the commit right before a real 2021 fix (issue #907), where the `–no-ignore-vcs` flag wrongly switched off ignore files in parent directories too. I reset the git history first so neither model could look up the maintainers’ answer. The refactor and the feature ran on the current fd. For every run, I recorded wall-clock time, tokens, and cost from Cursor’s usage dashboard.

Both models found the bug in the same place and wrote identical fixes. Each removed exactly one line from `src/main.rs`, the byte-for-byte same diff, and both left all 70 tests passing. I rebuilt each one, confirmed the bug was gone, and checked that the neighboring flags still behaved. I even diffed their fix against the maintainers’ real 2021 fix. The official fix from 2021 deleted three lines, while the models deleted one, but when I tested every related flag, the behavior was identical. The extra deletions were just cleanup.

With code being identical, the winner came down to the numbers. Opus finished in 30.43 seconds on 174.1K tokens in a single request. Grok took 46.25 seconds and 210.2K tokens across two requests.

On the smallest of the three tests, the Opus was the clear winner. xAI’s marketing claims don’t hold up here.

### Test 2: The refactor

The prompt:

*In src/main.rs, the construct\_config function is large and does most of its work inline. Refactor it: move it, along with any helper logic it needs, into a dedicated new module, and break the work into smaller focused functions. Do not change any behavior. Every existing test must still pass.*

The code quality story remains the same from test 1. Both models produced identical results. They moved `construct_config` into a new `config_builder.rs`, split it into focused helpers, and left all 264 tests green. The two diffs were within six lines of each other in size.

The numbers tell a different story. Grok did it in 1 minute 23 seconds on 197.1K tokens. Opus took about 5.5 minutes and 953.7K tokens. That is 4.8 times the tokens for the same result. Cost tracked it: Grok’s run billed at $0.27, Opus at $1.67. Because Opus was so much faster and cheaper in the first test, these results surprised me.

### Test 3: The feature build

The prompt:

*Add a new –count flag to fd. When –count is passed, fd should not print the matching paths. Instead it prints a single line: the total number of entries that matched, respecting all the usual filters. Add the flag to the CLI, wire it through, and make sure all existing behavior and tests still pass.*

Here’s where the code details diverge for each model. Both delivered `–count`, correctly. Grok touched six files, added a test, and updated the changelog. Opus touched seven, added more test coverage, and went one better by writing the man page entry.  Opus’s version was the more thorough of the two. I ran both binaries and confirmed `–count` returned the right number and matched `fd | wc -l`, with and without filters.

Though there was a slight difference in the code quality, the numbers show a much wider gap. Grok completed the feature build in 1 minute 37 seconds, using 602.6K tokens and costing $0.54. Opus did it in about five and a half minutes, using 3.2 million tokens and costing $3.25. On the largest job, Opus burned more than five times the tokens to deliver a slightly more thorough but functionally similar result.

## The results

Here are the quick stats on where each model landed on each test

|  |  |  |
| --- | --- | --- |
| **Test** | **Grok 4.5** | **Opus 4.8** |
| Bug fix | identical fix, 70/70 tests | identical fix, 70/70 tests |
| Refactor | 264/264 tests | 264/264 tests |
| Feature | –count correct, 6 files | –count correct, 7 files |
| Total time | ~3 min 46 s | ~11 min 40 s |
| Total tokens | 1.01M | 4.33M |
| Total cost (as billed) | $1.00 | $5.14 |

Across the three jobs, Opus used 4.3 times as many tokens as Grok did. That is almost exactly, but marginally wider than the 4.2x gap xAI advertised. Let me say, this result was very surprising. I use Claude as my primary AI model, and while I have my issues with it, I just assume it’s always the best. I don’t know where I got that idea, but it’s what my brain tells me.

> I use Claude as my primary AI model, and while I have my issues with it, I just assume it’s always the best. I don’t know where I got that idea…

Now for some testing FYIs I think are important to mention. These are Cursor’s blended token counts, not raw API numbers, so they fold in the context each agent re-sends every turn. Grok ran on Cursor’s “fast” tier and Opus on its “thinking” tier, so some of Opus’s token pile is extended reasoning rather than waste. Grok’s dollar figures also carried a 50 percent promo. Even doubled to full rate, its three jobs came to about $2 against Opus’s $5.14. And this is three tasks in one repo, not three hundred.

All those things considered, the pattern held in the main scoring criteria. On the code, these two models were interchangeable: same bug fix, same refactor, same feature, with Opus a shade more thorough on the docs.

**This leads me to conclude that Grok did the same work for roughly a quarter (23%) of the tokens, a third of the time, and a fraction of the price.**

If you’re a developer who’s no longer interested in tokenmaxxing, Grok might be the model for you.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)