**I always wonder about the end goal** when companieslaunch products so close together and undercut each other by claiming the new one is “so much better.”

[GLM-5.3](https://thenewstack.io/glm-5-3-post-training-coding/) and [GLM-5.3-Flash](https://thenewstack.io/glm-5-3-flash-chinese-chips/) are a great example of this. Z.AI launched GLM-5.3-Flash on August 26 with a [bold marketing claim](https://docs.z.ai/guides/vlm/glm-5.3-flash): stronger intelligence “at an exceptionally low cost,” and a 3x improvement in serving speed, built on an architecture that cuts attention computation by 3x compared to the GLM-5.3 flagship released earlier in the month.

On [OpenRouter](https://thenewstack.io/stripe-acquires-openrouter-tokens/), Flash costs $0.075 per million input tokens and $0.25 per million output tokens. GLM-5.3 costs $1.188 and $4.18, making it nearly 16 times more expensive. It definitely looks cheaper, but our tests will confirm, since it ultimately comes down to token usage.

If it uses more tokens, then we’ll have to equate the lower cost to pricing manipulation, meaning it could very well end up being more expensive if Z.AI changes their pricing structure (aka the end of the freemium we’re all living in right now).

I wanted to get to the bottom of this, so I tested each model on three tasks and 27 questions to determine which model is better and whether GLM-5.3-Flash has earned its place in the market.

## The tests

I tested both models on topics that replicate real work users will ask them to do:

* **Coding** – spec for a Python date-parsing function with strict edge cases: multiple input formats, two-digit years, invalid dates that must return None. I graded by running each model’s code against a hidden 12-case test suite I wrote and verified before either model saw the spec.
* **Reasoning** – a scheduling puzzle placing five people into five meeting slots under seven interlocking rules. I brute-forced all 120 possible schedules in advance to confirm exactly one solution exists.
* **Information extraction** – a three-email vendor negotiation with 10 facts scattered throughout it, including a trap: an 8% discount that applies to a revised 92-seat price, not the original quote.

I included all prompts in the test sections so anyone can replicate them on their own.

## Test 1: the date parser

Prompt:

```
"Write a Python function parse_event_date(s) that converts a date string to ISO format YYYY-MM-DD. Supported input formats: Month D, YYYY (e.g., March 5, 2026), D Month YYYY, US-style MM/DD/YYYY or M/D/YY, and ISO YYYY-MM-DD. Month names may be full or 3-letter abbreviations, in any letter case. Two-digit years always mean 2000-2099. Ignore leading and trailing whitespace. Return None for dates that don't exist on the calendar, strings missing a year, and anything unparseable. Use only the Python standard library."
```

This was the hardest test, but it produced the strangest numbers. Both models returned code that passed all 12 hidden tests, including the traps. February 30 is correctly rejected; “12/31/99” is correctly read as 2099, and a date with no year correctly returns None.

Getting to the same results cost very different amounts of effort. GLM-5.3-Flash took 455.8 seconds, most of it spent generating 38,677 tokens (that’s a lot of tokens) of reasoning before the final 60-line function. GLM-5.3 took 174.7 seconds and 14,801 tokens for a nearly identical solution. Flash still billed less, $0.019 against $0.065, because its per-token price is so much lower.

> “The ‘budget’ model’s low price is covering for the fact that it works harder to get the same answer.”

If Flash charged the flagship’s rates, its 38,677-token thinking session would have cost $0.16, two and a half times the flagship’s $0.065 bill for the same function. The “budget” model’s low price is covering for the fact that it works harder to get the same answer.

## Test 2: the scheduling puzzle

Prompt:

```
"Five consultants (Ana, Ben, Carla, Dev, Elena) each get exactly one meeting slot: 9am, 10am, 11am, 1pm, 2pm. Rules: 1. Ana is not in the first slot and not in the last slot. 2. Ben's slot is earlier than Carla's. 3. Dev's slot is immediately after Ana's. 4. Elena's slot is not adjacent to Ben's. 5. Carla is not at 11am. 6. Ben is not at 9am. 7. Elena is not at 2pm. Exactly one schedule satisfies all seven rules. State the final schedule."
```

Both models produced the one valid schedule, with all five people in the right slots. GLM-5.3 showed clean case-by-case elimination in its answer, got there in 18.9 seconds, and used 1,804 output tokens. Flash took 33.5 seconds and 1,003 output tokens, answering with just the schedule, with no work shown. Some people may prefer to see the work, but I don’t need to. I prefer short, to-the-point answers (which is sometimes hard to get with AI).

> On light work, the budget model really is the budget model (if you’re budgeting cost, not time).

This was the cheapest test of the run for both: $0.0003 for Flash, $0.008 for the flagship. The token math flipped here. The flagship generated 80% more tokens than Flash, and even if Flash charged flagship rates, this answer would have cost $0.004, about half the flagship’s bill. On light work, the budget model really is the budget model (if you’re budgeting cost, not time).

## Test 3: the vendor emails

Prompt:

```
“A three-email vendor renewal thread (full text in my test kit), with the instruction to extract vendor, renewal date, seat counts, costs, discount, deadline, contract number, and proposed call time into JSON."
```

The email thread hid its trap in the math. An 8% discount that applies to $73,600, the revised quote for 92 seats, not the original $68,000 quote for 85. Both models avoided the trap and returned accurate answers. Each extracted all 10 fields correctly and returned the right final price of $67,712.

And here is the first test where the budget model won on speed and cost. 7.7 seconds against 14.8, on 435 output tokens against the flagship’s 327. It suggests Flash’s slowness is not constant. On easy work, it behaves like a budget model should. Hand it something hard and its reasoning stage balloons.

## Results

|  |  |  |
| --- | --- | --- |
| **Metric** | **GLM-5.3-Flash** | **GLM-5.3** |
| **Accuracy** | 27/27 | 27/27 |
| **Total tokens** | 41050 | 17867 |
| **Total cost** | $0.0198 | $0.0757 |
| **Avg. response time** | 165.7s | 69.5s |

I put both models through a coding task, a logic puzzle, and a data extraction job, each worth 27 graded points, to measure how much accuracy the budget model gives up. It gave up none; both scored 27 out of 27.

Flash’s speed isn’t a guarantee. It depends on the difficulty of the work. On the coding task, the hardest of the three, Flash spent 7.6 minutes and produced 38,677 output tokens to reach an answer the flagship reached in under 3 minutes with 14,801. On the mid-level puzzle, the two came in seconds apart. On the easy extraction job, Flash was the faster model. Z.AI’s efficiency claim should come with a caveat. Use Flash for your easiest tasks, because while it can handle difficult work, it is far less efficient than the flagship.

## What do I think?

I came into this expecting to measure how much accuracy the cheap model loses. It lost none. Across a fussy coding spec, a logic puzzle with one valid answer, and a detail-heavy extraction, the two models were equally correct.

Where they differ is in which tasks they’re best suited. The choice depends on what the model is doing. Flash was faster on extraction but slower on the scheduling puzzle, although both runs finished within seconds.

> Hard jobs come down to whether you would rather spend time or money.

Hard jobs come down to whether you would rather spend time or money. Flash got the same answers at about a quarter of the total cost but took more than twice as long to complete the coding task. And hold the cost math loosely. Flash burns far more tokens to do hard work, so its advantage rests on the current per-token prices, and providers can change those at any time.

#### More on Z.ai from *The New Stack*:






[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)