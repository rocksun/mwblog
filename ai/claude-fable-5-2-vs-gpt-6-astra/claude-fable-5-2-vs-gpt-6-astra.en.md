![Two floating wireframe towers hold different arrangements of metallic cubes and textured spheres in mint green and lavender.](https://cdn.thenewstack.io/media/2026/11/4d6230a3-igor-omilaev-ufre8j7i8r4-unsplash-1024x800.jpg)

**Anthropic is positioning its new model**, [Claude Fable 5.2](https://thenewstack.io/anthropic-fable-coding-upgrade/), for demanding coding and technical work. Anthropic launched Fable 5.2 on Nov. 9 and reported higher scores than OpenAI’s GPT-6 Astra on two coding benchmarks. Fable 5.2 also has lower standard API rates.

[Anthropic’s launch benchmarks](https://www.anthropic.com/claude-fable-and-mythos-5-2) put Fable 5.2 ahead of Astra, 49.1% to 42.8% on FrontierCode 2.0 and 69.9% to 65.5% on FrontierSWE v2. Fable’s 49.1% came at X high effort. At High, [its default on the Claude API](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2), it scored 45.3%. Benchmark leads don’t always carry over to real work.

The cost side is less simple than the price list. Tokens are the chunks of text a model reads and writes, and AI companies bill by them. At standard API rates, Fable 5.2 costs $8 per million uncached input tokens and $40 per million output tokens. [OpenAI launched GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/) in September at standard API rates of $10 per million uncached input tokens and $50 per million output tokens. “The price per task is what matters,” OpenAI President Greg Brockman said at Astra’s launch. Both APIs charge for [reasoning tokens as output](https://developers.openai.com/api/docs/guides/reasoning) and have [separate rates for cached input](https://developers.openai.com/api/docs/guides/prompt-caching).

In my experience, Anthropic’s models have used more tokens than OpenAI’s. I put this positioning to the test and ran Fable 5.2 against Astra on tasks that simulate real developer work.

## The tests

I ran both models on the same three tasks, once each, through each vendor’s API at default settings. Each test is worth 50 points, and I used a script to grade all the answers. Here are the tests:

* **Bug fix**: I planted 10 bugs in a 2,600-line billing codebase and wrote a support ticket describing 10 customer complaints. The ticket’s guesses about the causes are wrong, two of the codebase’s own tests are wrong, and one bug only shows up after another is fixed.
* **Code review**: I planted 45 defects in its VAT ID checks for 27 countries, its IBAN rules, its European Central Bank payment calendar, and its date formats for 50 locales in an EU invoicing package. The models had to prove each defect with an input the code gets wrong and identify the correct answer. Flagging false alarms cost the models points.
* **Code writing**: The model wrote the same helpers from scratch, including VAT ID validation for 27 countries, IBAN checks for 34 countries, the payment calendar, and long dates.

### Bug fix

Fable 5.2 and Astra fixed all 10 bugs and passed all 50 hidden checks, both in 12 turns (the matching number of turns surprised me).

The difference is in how much each model spent to get there. Fable 5.2 used more than 17,000 reasoning tokens, and Astra used 819 (wow). Astra passed the checks in about two minutes at an estimated cost of 98 cents. Fable 5.2 took more than five minutes and cost an estimated $2.51.

The numbers:

* **Fable 5.2**: 12 turns, 696,863 in, 36,135 out (17,387 reasoning), $2.51, 326 s.
* **Astra**: 12 turns, 231,854 in, 6,823 out (819 reasoning), $0.98, 122 s.

### Code review

This is the only test where the scores differ. Fable 5.2 scored 49, and Astra scored 45. Fable 5.2 proved 44 of the 45 defects and raised no false alarms across 71 findings. Astra proved 41 and incorrectly classified one Spanish ID as valid. Astra missed defects in check-digit rules for Spain, Ireland, and Luxembourg. Both models missed the same Spanish defect: two swapped letters in a 23-letter lookup table.

Fable 5.2’s thoroughness came at a price. It cost more than six times what Astra did and took more than four times as long. If your code handles invoices (or simple approvals), one validation rule the review misses can get real invoices rejected, so Fable 5.2’s four extra points may be worth the higher price. For a routine review, Astra found 91% of the defects for 16% of the cost. Each model ran once, so a four-point gap could shift on another run.

The numbers:

* **Fable 5.2**: 26 turns, 2,207,564 in, 103,240 out (77,641 reasoning), $6.05, 993 s.
* **Astra**: 12 turns, 192,018 in, 8,664 out (4,307 reasoning), $0.95, 227 s.

### Code writing

Both models scored 50 of 50. Each one wrote working checks for 27 countries’ VAT IDs and 34 countries’ IBANs with no libraries to lean on. Neither model had trouble here. Both passed all the checks in one run.

Astra took 23 turns, almost as many as Fable 5.2’s 24. Fable 5.2 still cost 2.3 times as much and took 1.7 times as long for the same score. In this run, the extra tokens didn’t raise the score.

The numbers:

* Fable 5.2: 24 turns, 1,495,712 in, 87,542 out (47,458 reasoning), $4.83, 838 s.
* Astra: 23 turns, 460,271 in, 24,007 out (9,328 reasoning), $2.06, 483 s.

## Results

|  |  |  |
| --- | --- | --- |
| **Test** | **Claude Fable 5.2** | **GPT-6 Astra** |
| Bug fix (of 50) | 50 | 50 |
| Code review (of 50) | 49 | 45 |
| Code writing (out of 50) | 50 | 50 |
| Total tokens in / out | 4,400,139 / 226,917 | 884,143 / 39,494 |
| Estimated cost | $13.39 | $3.99 |
| Total time | 2,157 s | 832 s |

Fable 5.2 led on code review and tied Astra on the other two tasks. Across the two tied tasks, its estimated API cost was 2.4 times Astra’s ($7.34 vs. $3.04), and it took 1.9 times as long (1,164 vs. 605 seconds).

### What do I think?

For tasks like these, I’d start with Astra. It matched Fable 5.2’s scores on bug fixing and code writing at about 41% of the estimated cost, and it finished all three tasks faster. I’d consider Fable 5.2 for a careful code review, where it found three more defects in this test. Both models missed defects.

Fable 5.2’s standard token rates are lower, but it used about five times as many tokens as Astra across these three runs. Brockman’s point about price per task held up here.

The post [Claude Fable 5.2 vs. GPT-6 Astra: A lower list price didn’t mean a lower bill](https://thenewstack.io/claude-fable-5-2-vs-gpt-6-astra/) appeared first on [The New Stack](https://thenewstack.io).