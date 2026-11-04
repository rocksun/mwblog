**OpenAI launched** [GPT-6.1 Terra](https://thenewstack.io/openai-terra-bypassed-restrictions/) on October 26, and included two direct comparisons with Opus 5.5 in its marketing materials. It claimed Terra came within five percentage points of Opus 5.5, with fallbacks at less than one-fifth the estimated cost, on Terminal-Bench-Science 0.1, which has agents write code for research tasks such as tracking cell divisions.

At max effort, [OpenAI describes](https://openai.com/index/introducing-gpt-6-1-terra/) Terra as more than three times as token-efficient as Opus and one-quarter the price for standard input and output tokens. Separately, it reports an estimated cost per task of about one-ninth. On Agents’ Last Exam, a benchmark of multistep computer-use tasks, Terra scored 60.0% at $1.01 per task, and Opus scored 63.2% at $8.82. That is a 3.2-percentage-point score gap and an 8.73-to-one cost ratio, not identical accuracy.

At standard uncached API rates, [Terra costs $1 per million input tokens and $5 per million output tokens](https://developers.openai.com/api/docs/models/gpt-6.1-terra), compared with [Opus 5.5’s $4 and $20](https://www.anthropic.com/claude-opus-5-5). With the same input/output token mix and no other pricing adjustments, Terra would need four times as many tokens to match Opus’s cost. Actual task cost also depends on token usage, cache reads and writes, and any applicable pricing adjustments.

The accuracy claims caught my interest because, [when I tested Terra against OpenAI’s own GPT-6 Astra](https://thenewstack.io/gpt-6-1-terra-vs-gpt-6-astra/), Terra left some numerical totals uncalculated and gave some incorrect answers. That article focused mainly on analyzing large datasets, such as database records and server logs.

Since the claims against Opus focus on computer use and scientific coding, I built two tests around those areas. I also added a third test that recreates the kind of large-dataset task Terra struggled with against Astra, to see whether Opus shows the same weakness and how it handles it.

## The tests

I ran the Terra vs. Opus tests a few times because, at easier levels, both models scored similarly, as in the Terra vs. Astra testing. When the scores came out too close, I made the test harder and ran it again, up to three times. The results below are from the final versions, including the CI audit that I made smaller after both models failed to finish the first version. Because I changed the tests after seeing earlier results and ran each final version only once per model, these results do not establish repeatability or average performance across workloads.

I ran each final test once per model through OpenAI’s and Anthropic’s own APIs, with each vendor’s effort setting at max. Those settings do not impose equivalent reasoning budgets across models. I did not cap turns. Both models have a 128,000-token output limit per response, including reasoning; a multi-turn task can exceed that in total. I used a script to grade every run against a verified answer key.

The figures below aggregate tokens across all turns in each final run; reasoning tokens are included in output totals. Dollar figures beside each run are estimates using standard uncached input and output rates, not invoice totals. Terra’s rates increase for individual requests above 272,000 input tokens; aggregate task totals alone don’t show whether that threshold was crossed. The reported caching-adjusted totals are listed separately. The totals exclude earlier test versions and do not include any separately billed tools or execution infrastructure.

* **Release triage:** I built a fake GitHub-style site with a failed software release, and each model had to fix it through a screenshot-based browser interface, using clicks and typed URLs. The final version had six root causes spread across code, a feature flag, and a secret, plus flaky-test decoys and three planted instructions telling the model to bypass safety settings.
* **Cell lineage**: I generated a noisy 72-frame microscope movie of dividing cells, and the models wrote and ran their own Python to track them. They had to log every division and trace each cell in the last frame back to its parent.
* **CI history audit**: This test put about 1,200 rows of CI test results into a single prompt with no tools and asked 50 questions about them. The data mixed three time zones, three duration formats, renamed tests, duplicate rows, and a price change mid-month.

### Release triage

This one was a 50–50 tie, and it stayed tied through all iterations of the test. To get the score, I used 50 pass/ fail checks. Most looked at whether the models filed and closed the right issues and fixed each problem so the release could pass. The rest checked that the models didn’t change anything they weren’t supposed to, like the decoy pull requests and settings, and ignored the planted instructions.

In the hardest version, both models found all six root causes, reverted the right pull requests on the release branch, and reused the oldest open issue instead of filing a duplicate. Neither model followed any of the three planted instructions.

The difference was in how they got there. Opus jumped between pages by typing URLs 102 times, while Terra did that 23 times and mostly clicked through the site. Opus also wrote about five times as many output tokens.

For browser work like this, Terra got the same score at about 17.1% of Opus’s estimated uncached token cost, or a 5.83-to-one cost ratio. This was a separate synthetic task, not a replication of OpenAI’s benchmark. Prompt caching can reduce the cost of repeated screenshot and conversation inputs; the table below lists the reported totals with and without caching.

The numbers:

* Terra: 186 turns, 22,117,582 in, 7,659 out (2,718 reasoning), $22.16, 807 s.
* Opus: 170 turns, 32,100,919 in, 39,838 out (18,795 reasoning), $129.20, 934 s.

### Cell lineage

This is the test closest in subject matter to OpenAI’s Terminal-Bench-Science comparison with Opus 5.5 with fallbacks. My synthetic cell-tracking test does not replicate that benchmark. In my run, Terra scored 48/50, while Opus scored 43.5/50, at about one twenty-fourth of Opus’s estimated uncached token cost.

I graded this test out of 50 points. Each model earned 20 points for finding the cell divisions, and lost half a point for every division it reported that didn’t happen. It earned 20 more points for tracing each cell in the last frame back to the cell it came from. The final 10 points came from 10 questions about the results, like how many times the cells divided and how many cells drifted out of view.

Terra matched all 20 divisions and answered all 10 summary questions correctly. Opus missed two divisions, reported one that never happened, and miscounted both the total divisions and the cells that drifted out of frame. Both models assigned two of the 20 final cells to the wrong starting cell.

Opus also used more turns and code executions despite its lower score. It ran code 96 times over 129 turns and took about 36 minutes. Terra ran code 30 times over 37 turns and finished in about 15 minutes.

The numbers:

* Terra: 37 turns, 3,118,018 in, 69,413 out (55,453 reasoning), $3.47, 920 s.
* Opus: 129 turns, 19,722,068 in, 201,194 out (135,672 reasoning), $82.91, 2,187 s.

### CI history audit

This test did not replicate OpenAI’s computer-use or scientific-coding benchmarks. It resembles the large-dataset tests I ran against Astra. My first version had 3,920 rows, and neither model produced a final answer before reaching 128,000 output tokens.

For the second version, I cut the file to about 1,200 rows and added a mid-month price change as an additional challenge. Terra finished with 47 out of 50. It was off by one on two status counts, and it answered $0 for a question about GPU runners when it should have said the data did not cover them. Opus again produced no final answer before hitting its 128,000-token-per-response output limit. This was a failure to complete at max effort within that response limit; it does not establish that Opus could not answer under another configuration.

Terra answered all 50 questions and missed three: two status counts off by one and a question it should have marked unanswerable. That gives 47/50, or 94% under this test’s scoring. It completed this version of the large-table task without tools; Opus returned no answer to score.

The numbers:

* Terra: 56,959 in, 61,539 out (61,122 reasoning), $0.36, 691 s.
* Opus: no final answer, 72,460 in, 128,000 out, $2.85, 841 s.

## Results

|  |  |  |
| --- | --- | --- |
| **Test** | **GPT-6.1 Terra** | **Claude Opus 5.5** |
| Release triage (of 50) | 50 | 50 |
| Cell lineage (of 50) | 48 | 43.5 |
| CI history audit (of 50) | 47 | Did not finish |
| Total tokens in / out | 25,292,559 / 138,611 | 51,895,447 / 369,032 |
| Estimated uncached token cost | $25.99 | $214.96 |
| Estimated cost with caching | $2.51 | $21.52 |
| Total time | 2,418 s | 3,962 s |

*Both cost rows are my estimates, not billed amounts. I multiplied the token counts each API reported by the vendor’s standard rates, and for the caching row I priced cached tokens at each vendor’s lower cache rates.*

Terra tied Opus on release triage and scored higher on cell lineage; it completed the CI audit, while Opus returned no final answer. Across these three final runs, Terra’s estimated uncached token cost was $25.99 versus $214.96, about 12.1% as much, or an 8.27-to-one ratio. Terra’s total elapsed time was 2,418 seconds versus Opus’s 3,962 seconds, a difference of 1,544 seconds, or about 25.7 minutes. These totals exclude the earlier test versions.

### What do I think?

Terra held its own when it could click, run code, and check its work. On the final table task without tools, Terra returned an answer, and Opus did not. That result applies to these particular runs, not a general ranking of the models.

These tests used max effort, while the Astra tests used high. The tasks also differed, so the comparison does not isolate the effect of the effort setting. [Anthropic recommends](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) starting Opus 5.5 at its default medium effort and reserving higher settings for workloads where testing shows a quality gain. I did not test that configuration here.

For work like these browser and code-execution tasks, I would run Terra at max effort in a trial before committing to Opus. I would also compare each model at the effort setting that works best for the workload and check accuracy, completion rate, time, and cost across repeated runs. I would still double-check numerical answers on large tables, where Terra made errors in this test and in the earlier Astra comparison.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=gpt-6-1-terra-vs-claude-opus-5-5)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)