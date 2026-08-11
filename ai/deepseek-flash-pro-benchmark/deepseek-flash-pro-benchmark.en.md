**DeepSeek, the Chinese AI lab that’s been undercutting OpenAI and Anthropic** on price since it arrived, recently refreshed V4-Flash, moving it out of preview. DeepSeek [documentation](https://api-docs.deepseek.com/updates/) promised that this refreshed Flash model topped the V4-Pro preview on coding and agentic benchmarks.

The prices make that claim strange, though. V4-Flash runs $0.14 per million input tokens and $0.28 per million output. V4-Pro runs $0.435 and $0.87. That is almost exactly one-third the price on both input and output.

If [the budget model beats the flagship](https://thenewstack.io/deepseek-v4-flash-open-weights/) at a third of the price, why does the flagship exist? I had to get to the bottom of this, so I gave both models the same three professional coding jobs and tracked every token.

## The tests

I used rich, the Python terminal-formatting library from Textualize. I chose it because it’s real production Python with a [massive install base](https://pypistats.org/packages/rich) and enough internal complexity (style spans, render pipelines, cell-width math) to make a model work for it.

Both models ran inside [OpenCode](https://thenewstack.io/anthropic-claudecode-opencode-split/), the open source terminal coding agent — like Claude Code except you can plug in any model. One setup note: OpenCode’s built-in DeepSeek list only ships with Flash, and there’s a [closed-as-not-planned GitHub issue](https://github.com/anomalyco/opencode/issues/30177) about it. To get Pro into the model picker, I had to add a small config file to the project folder ([this guide](https://haimaker.ai/blog/deepseek-opencode-setup/) has the JSON). It only took about two minutes, mentioning just in case you try to test pro on OpenCode and can’t find the model.

I built a separate clone of the repo for each model, started a fresh session for every test, and used identical prompts, so the model was the only variable. Here are the three tests I ran (in this order).

* a bug fix
* a feature build
* a performance optimization (to test reasoning skills)

For every test, I recorded time from OpenCode’s session timer and tokens, API requests, and cost from DeepSeek’s usage dashboard.

## Test 1: The bug fix

**The prompt:** *A user reports that importing Rich crashes on macOS. Their environment: Rich 15.0.0, Python 3.14, macOS on Apple Silicon, VS Code integrated terminal with the working directory inside a Dropbox File Provider folder. [traceback] Commands using only absolute paths otherwise work in that terminal. The import itself is what fails, so python -m rich.diagnose cannot run. Find the root cause in this codebase, fix it, add a regression test, and run the test suite. Explain the cause and your fix.*

The bug is real and nasty in a quiet way. Rich calls `os.getcwd()` at import time and only guards against `FileNotFoundError`, but macOS File Provider folders (Dropbox, iCloud) make `getcwd()` raise `PermissionError` instead, so the entire library dies before a single line of user code runs.

Both models found the same root cause and wrote the same one-line fix, broadening the exception handler to `OSError`. Both wrote a regression test that mocks the failure, and both finished with all 957 tests passing. I confirmed the fix myself by simulating the blocked `getcwd()` against each patched copy.

The fixes were identical. The only difference was where each model put its test. Pro read the repo’s existing test files first and added its regression test to the existing suite, matching the project’s conventions. Flash created a brand-new test file. Both work but Pro’s is what a maintainer would ask for in review. Flash’s is what a contributor in a hurry would ship.

Flash finished in 59 seconds on 6 API requests and 119.9K tokens, for less than a cent. Pro took 1 minute 1 second, 13 requests, and 159.2K tokens, for about a cent. Same fix, but Pro made twice the API calls to get there. I call this one a tie.

## Test 2: The feature build

**The prompt:** *Rich’s Text class has an rstrip() method that removes trailing whitespace while preserving styles. Add a matching lstrip() method that removes leading whitespace while preserving styles, and a strip() method that does both. Requirements: 1. Match the existing code style of the Text class 2. Styles on remaining characters must be preserved correctly 3. Add tests covering plain text, styled text, and text that is all whitespace 4. Run the test suite and confirm everything passes 5. Explain your implementation decisions*

In rich, text can carry formatting, so characters 4 through 9 might be bold. The task was to add a method that trims blank space off the front of text. Trimming the end is easy because nothing moves. Trimming the front is harder because every character slides over, and the formatting is pinned to positions, not characters. If the positions don’t slide too, the bold lands on the wrong letters.

Both models got it right. I ran both implementations through the same battery of eight edge cases (partial spans, all-whitespace text, no-op inputs) and both passed all eight.

The interesting part was watching how. Pro delegated its initial codebase exploration to a subagent that made 13 tool calls on its own, then wrote an implementation whose first draft had a real bug. It dropped style spans that started inside the stripped whitespace. Its own tests caught it, and it fixed it in one iteration. That’s the system working as intended, but it’s also more machinery. Flash just read the files and wrote the code.

Flash finished in 1 minute 29 seconds on 6 requests and 191.2K tokens, again for less than a cent. Pro took 1 minute 43 seconds, 23 requests, and 333.6K tokens, for about two cents. That’s nearly four times the API calls and 75% more tokens for the same feature.

Flash came out the winner of this one but based only on efficiency. Same code quality (both passed all eight edge cases), but Flash got there faster, with a quarter of the API calls, half the tokens, and at half the cost. Tie on the code, Flash on efficiency.

## Test 3: The performance job

**The prompt:** *The maintainers want faster rendering for large tables. Write a small benchmark script that measures rendering a Table with 5,000 rows and 6 columns to a string Console. Record the baseline time, profile it to find the dominant hot path, and optimize that hot path without changing any public behavior or output. Show before/after timings from your benchmark, explain what you changed and why it’s faster, and run the full test suite to prove nothing broke.*

The first two tests had the right answer. This one is open-ended. This open-ended test is where the two models stopped being interchangeable.

Flash went big. It worked for 27 minutes, made 128 API requests, and burned 15.4 million tokens, all for about eight cents. It didn’t just speed up the code. It built its own testing rig to compare the old and new output across 37 kinds of tables, caught and fixed one of its own bugs along the way, noticed twice that its benchmark was accidentally measuring the wrong copy of the library, and cleaned up 13 type-checker errors. Flash said its version was 1.84x faster. I measured it myself and got 1.83x, so I flag as accurate.

Flash also said its new output was identical to the old output down to the byte, and I found one case where it isn’t. In one specific table setup on a color terminal, the invisible color codes get written in a slightly different order. On screen the two outputs look exactly the same, and no user would ever notice. But identical was the claim, and identical is false. This is interesting because Flash did the best engineering of the experiment here, then described its work as more airtight than it was when it really didn’t need to.

> Flash did the best engineering of the experiment here, then described its work as more airtight than it was when it really didn’t need to.

Pro treated the same prompt like a code review. It worked for 15 minutes 21 seconds across 57 requests and 4.7 million tokens, costing about seven cents. It found one step in the table-drawing code that was doing work that had already been done, deleted it, tightened one busy stretch of code, and reported a 3.3% improvement. I measured 1.06x, and its output really is identical to the original, down to the byte.

It even got right the one case Flash got wrong. Everything Pro said about its work was true. There just wasn’t much work. The big speedup Flash found was sitting in the same measurements Pro was looking at, and Pro missed it.

> The cheaper model got creative with this one, and the expensive model kept the work more on the surface.

Tldr; the cheaper model got creative with this one and the expensive model kept the work more on the surface.

This test is where the numbers get fun. Flash’s 27-minute run burned 15.4 million tokens and cost about eight cents, because 98.6% of those tokens were cache reads billed at a quarter-penny per million. Pro’s run used less than a third of the tokens and cost about seven cents anyway, because Pro’s rates are three times higher. Flash’s fifteen million tokens sound expensive but it only translated to 8 cents.

## Results

|  |  |  |
| --- | --- | --- |
| The metric | V4-Flash | V4-Pro |
| Bug fix | identical one-line fix, 957/957 tests | identical one-line fix, 957/957 tests |
| Bug fix numbers | 59 s, 119.9K tokens, <$0.01 | 1 min 1 s, 159.2K tokens, ~$0.01 |
| Feature | correct, 8/8 edge cases | correct, 8/8 edge cases |
| Feature numbers | 1 min 29 s, 191.2K tokens, <$0.01 | 1 min 43 s, 333.6K tokens, ~$0.02 |
| Optimization | 1.83x faster (my measurement) | 1.06x faster (my measurement) |
| Optimization numbers | 27 min, 15.4M tokens, ~$0.08 | 15 min 21 s, 4.7M tokens, ~$0.07 |
| Total time | ~29 min 28 s | ~18 min 5 s |
| Total API requests | 140 | 93 |
| Total tokens | ~15.7M | ~5.2M |
| Total cost (as billed) | $0.09 | $0.10 |

The chart shows how each model did on the three tests, what each test cost in time, tokens, and money, and the totals at the bottom.

Read down the columns and the story jumps out. The first two tests are ties. The third is where Flash pulls ahead, 1.83x faster against 1.06x. Then look at the bottom rows. Flash used three times the tokens, yet the final bills are nine cents and ten cents. The cheaper rates and the heavier token use cancel each other out almost exactly.

### What do I really think?

Both models were identical on the simple tasks. They only split on the reasoning-heavy one, and reasoning is objectively the hardest thing for AI models. Flash reasoned better and used three times the tokens doing it (closing the cost gap completely).

> If better reasoning means more tokens, we’re all about to send a whole lot of cash money to AI companies, especially now that we’re hooked.

If better reasoning means more tokens, we’re all about to send a whole lot of cash money to AI companies, especially now that we’re hooked.

![](https://cdn.thenewstack.io/media/2026/08/f309e29e-screenshot-2026-08-09-at-21.30.36-scaled.png)

This reminds me of my [Opus 5 vs. Fable 5](https://thenewstack.io/opus-5-vs-fable-5/) test. The parent company sets the pricing, so the price tells you about strategy, not cost. And there’s a banner on DeepSeek’s usage page right now warning that prices are about to go up by a lot (screenshot above). I wonder if Flash is priced low so we get used to its better reasoning before the bill arrives.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)