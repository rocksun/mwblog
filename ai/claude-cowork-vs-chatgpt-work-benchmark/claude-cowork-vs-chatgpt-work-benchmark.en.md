When Anthropic [merged Claude chat and Cowork](https://thenewstack.io/anthropic-claude-unified-interface/) into a single interface last week, it removed an increasingly irrelevant decision users had to make about which mode to choose.

Now, to use both tools, just ask a question, then hand off a multi-step task in the same thread, and Claude routes it. Anthropic made this update because it says customers often struggled to choose the right tab for the right task, so the merged app now routes each request itself instead of asking you to pick a mode — for now, the unified experience is rolling out to Pro and Max subscribers first, with free and team tiers to follow.

But this isn’t new. OpenAI has offered the same promise since earlier this summer. [OpenAI introduced Work mode](https://thenewstack.io/openai-codex-work-atlas/) alongside Chat on July 9, then phased out the older, separate Agent mode the following month. Work mode is a sandboxed environment with a browser, code execution, and file output, sitting next to a Chat toggle in the same window — though reviewers note it can’t yet hand a live, logged-in browser session back to the user mid-task the way Agent mode could, e.g., for logins or payments. OpenAI built Work mode on its Codex coding agent after OpenAI reported that roughly a fifth of Codex’s 5 million weekly users were non-developers — a share it said was growing three times faster than developers.

As OpenAI and Anthropic get closer to feature parity, accuracy, reliability, and token usage matter even more.  What better way to find out which tool is better than to run head-to-head tests?

## The tests

I ran three tests, covering different areas of real developer work.

* **API research** -Look up four real developer APIs and tabulate their documented rate limits, whether a free tier exists, and the current version identifier. I checked the answers against the vendors’ docs the same day.
* **Build from a spec** – Write a small command-line duration parser from a spec with strict edge cases. I ran each app’s code against a hidden 16-case test suite.
* **The handoff** – Ask which of two stack traces indicates a race condition, then in the same thread hand off a real job: pull a log file from Google Drive, compute latency percentiles and error rates per endpoint, and deliver a spreadsheet with a chart. I generated the log data, so I knew every number in advance.

I recorded token cost and time in each test and included the prompts for anyone interested in replicating this work.

### API research

*The prompt:**Research the current public documentation for these four developer APIs and build me a table with one row per API and these columns: documented rate limit for authenticated requests, whether a free tier exists (yes/no), and the current API version identifier or date shown in the docs. APIs: GitHub REST API, Stripe API, Twilio Messaging API, OpenAI API. Cite the documentation page you used for each row.*

Both Claude and ChatGPT answered correctly on the twelve graded fields, but Claude was more thorough. It included GitHub’s separate limit for Actions tokens, Twilio’s queue window, and OpenAI’s tier thresholds, plus a note about one page it couldn’t reach.

ChatGPT, in Work mode, finished in 1 minute 17 seconds and wrote 649 output tokens. Claude took 1 minute 44 seconds and wrote 1,042 tokens, read eight pages, listed nine sources, and offered to export the table as a spreadsheet. Claude wrote nearly double the tokens and took longer, but in this case, it’s warranted because of the added detail.

### Build from a spec

*The prompt:*  
*Build the command-line tool described in the spec below. Deliver a single file named durparse.py that follows every rule. Test it yourself before returning it. Show the complete final code in your reply. (Followed by the spec: a duration parser with units d/h/m/s, largest first, one of each, decimals allowed, bare numbers are seconds, everything else returns None.)*

Both apps returned a `durparse.py` file that passed all 16 hidden tests, including the traps. The traps included units out of order, a repeated unit, a trailing number with no unit, and negative values. The 517-token spec went to both. ChatGPT finished in 1 minute 17 seconds on 769 output tokens. Claude took 1 minute 45 seconds and 989 output tokens. Claude reported running 35 of its own test cases before returning the file. Both delivered a download and showed the code in the reply.

The code came out nearly identical, both using exact-precision arithmetic and a fixed-order regex. Claude flagged a judgment call the spec never settles on: that rounding 0.5 seconds up is a choice and Python’s built-in round would go the other way. ChatGPT reported only that its tests passed. Once again, Claude was just a little more thorough.

### The handoff

*The prompt:*  
*Which of these two stack traces points to a race condition, and in one sentence why? (with the two traces) Then: Now take the file api\_logs.csv from my Google Drive (columns: time, endpoint, status, latency\_ms) and produce a downloadable spreadsheet with one row per endpoint showing request count, p50, p95, and p99 latency in milliseconds, and error rate as the percentage of requests with status 500 or above. Add a bar chart of p95 latency by endpoint. Also show the table in your reply.*

I started each thread in plain chat with the stack-trace question, 135 tokens. Both answered correctly in seconds: Trace B, the dictionary that changed size during iteration. ChatGPT spent about 10 seconds and 48 output tokens. Claude spent 118 in about 25 seconds, adding a caveat that the same error can happen without threads if the loop body edits the dictionary itself. Then, without switching modes, I handed off the log analysis.

Claude pulled the file, computed the table, and built an .xlsx with a p95 bar chart in about 4 minutes on 319 output tokens. ChatGPT produced the same spreadsheet and chart in 28 seconds, using 467 output tokens. All 30 numbers matched my ground truth on both sides. Claude also named its percentile method (linear interpolation) and noted the numbers would match if I recomputed them in Google Sheets. ChatGPT gave the same correct table but didn’t provide as much detail as Claude did.

## Results

|  |  |  |
| --- | --- | --- |
| **The test** | **ChatGPT (Work mode)** | **Claude (merged app)** |
| API research | 12/12, 1:17, 125 in / 649 out | 12/12, 1:44, 125 in / 1,042 out |
| Build from spec | 16/16 tests, 1:17, 517 in / 769 out | 16/16 tests, 1:45, 517 in / 989 out |
| Handoff, question | Correct, ~10 s, 135 in / 48 out | Correct, ~25 s, 135 in / 118 out |
| Handoff, task | 30/30, 28 s active, 133 in / 467 out | 30/30, ~4 min, 133 in / 319 out |
| Total tokens (visible) | 910 in / 1,933 out | 910 in / 2,468 out |

Both Claude and ChatGPT were equally accurate. Every field, every test case, every number matched on both sides, and both cited real documentation.

The differences are in speed and answer detail. ChatGPT was faster on every task and produced 1,933 visible output tokens, compared with Claude’s 2,468. Some of Claude’s extra output was filler, but not all of it. It added context the prompts didn’t ask for, named the percentile method behind its numbers, and flagged two judgment calls the specs left open. ChatGPT gave the same right answers but with less context.

### What do I think?

I’d pick Claude, and here’s the reasoning. On time, ChatGPT won every task, but the gaps were seconds on the short tasks (1:17 vs 1:44, 1:17 vs 1:45), not a noticeable difference. On tokens, ChatGPT used about 22% less output than Claude, which is positive, but not when you consider how important detail/context is.

On detail, Claude provided more meaningful detail on all three tests. This included the extra API context, the rounding judgment call, and the percentile method. In today’s world, where AI can fabricate, detail matters.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)