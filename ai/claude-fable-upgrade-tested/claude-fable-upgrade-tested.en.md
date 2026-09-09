**Anthropic launched Claude Fable 5.1 this week**, calling it “[our most advanced model for coding and knowledge work](https://thenewstack.io/anthropic-fable-5-1-launch/).”

There was quite a lot of excitement surrounding the launch. Every CEO Dan Shipper [posted](https://x.com/danshipper/status/2094848951568474186) that after a week of testing, it was “the strongest coding model we’ve used.”AI commentator Min Choi [collected examples](https://x.com/minchoi/status/2094990525912752547) of people “one-shotting games, building 3D worlds + creating insane simulations” within 24 hours of release.

The announcement highlights the Terminal-Bench-Science benchmark, an agentic research benchmark, where 5.1 scores 52.6% against Fable 5’s 24.7%. Terminal-Bench-Science gives a model a terminal and a set of multi-step scientific research tasks, then scores what percentage it completes correctly.

The Terminal-Bench-Science score gap illustrates the main measurable difference between Fable 5 and 5.1. Fable 5 finishes about a quarter of them. 5.1 finishes about half. With the new model costing exactly what the old one does — $10 per million input tokens and $50 per million output — this score is the reason to upgrade, if it’s true.

> > Benchmark scores don’t always translate to real-world work.

Benchmark scores don’t always translate to real-world work. They measure narrow task sets under conditions vendors help define. Some companies have been known to tune models toward the tests they get graded on. I’m not saying Anthropic did that, but the possibility is baked into how benchmark marketing works.

 A score of 52.6% on a research benchmark tells me nothing about whether AI’s output on the work I need it to do gets better. So I wanted to see what these numbers and strong claims mean for a real user doing real work.

## The tests

I tested both models on four tasks that mimic real work that people use AI for.

* **Agentic research**: Experiment data with five bad rows; the lab notes explain how to catch them. The model has to exclude them, compute the batch averages, and write up its findings.
* **Agentic coding**: A small Python project with two planted bugs and a failing test suite. The model has to find the bugs and fix the code until every test passes.
* **Reasoning**: Two math problems with exact answers I verified in advance. This includes no terminal work, only thinking.
* **Sensor data audit**: Messy readings from five sensors, with every problem documented in an equipment log: a fast clock, a mid-run hardware swap, corrupted rows, one sensor in Fahrenheit. Added as a tiebreaker; more on that later.

I usually paste my prompts so you can rerun my tests. I was unable to do that for these tests. These tests require folders of data files with planted errors, and the prompts are useless without them.

## Agentic research

Both models finished the task correctly in 3 turns. Each read the lab notes and excluded exactly the right five rows, including the subtle case where a duplicated trial’s first entry is corrupt, and its rerun is valid. Both produced batch means that matched the correct answers to the decimal.

Fable 5.1 was slightly faster (19.2s vs. 20.6s) and slightly cheaper ($0.086 vs. $0.100). On the benchmark this task imitates, Fable 5 supposedly fails three-quarters of the time. On my machine, it didn’t make any mistakes.

## Agentic coding

The coding test went the same way. Both models ran the suite and spotted the loud bug, a remove function that added stock instead of subtracting it. Both also caught the quiet one, an off-by-one in a threshold comparison. Each fixed both bugs and finished with 8 of 8 tests passing in 3 turns.

Fable 5.1 finished in 13.6 seconds, and Fable 5 took 17.2, with both runs costing $0.07. The new model was faster, but nothing else separated them.

## Reasoning

Anthropic’s numbers predicted a near-tie here. I saw the same result. Both models answered the two challenges correctly, with correct step-by-step work. Fable 5.1 was slightly faster on both problems: 12.0 seconds against 12.5 on the first, and 9.7 seconds against 10.7 on the second. It was also more concise, using 771 output tokens against Fable 5’s 1,045 on the first problem and 647 against 798 on the second.

## Sensor audit data

AKA the tiebreaker. After three rounds of perfect ties on accuracy, I added a fourth test. I built this test to be harder than the first three, because a model that supposedly doubles its predecessor should reveal that somewhere.

Both models handled every trap. Each shifted the fast clock back before filtering the time window, which also excluded two hot readings from the data. Each split the swapped sensor’s calibration at the right moment, dropped the corrupted rows, and converted Fahrenheit after calibrating rather than before. Once again, the two result files were identical and fully correct.

The difference between the two was in the timing, cost, and token usage. Fable 5 finished in 4 turns, 23.9 seconds, and $0.134. Fable 5.1 needed 5 turns, took 28.4 seconds, and cost $0.304, more than double. The extra turn is what did it. Every turn resends the entire conversation so far, so Fable 5.1 pushed 23,602 input tokens through the API, compared to Fable 5’s 7,940.

> > Fable 5 was as accurate, cheaper, and faster on the hardest task of the set. I wasn’t expecting that.

Fable 5 was as accurate, cheaper, and faster on the hardest task of the set. I wasn’t expecting that.

## Results

|  |  |  |
| --- | --- | --- |
| Metric | Fable 5 | Fable 5.1 |
| **Accuracy** | 24/24 | 24/24 |
| **Total tokens** | 22219 | 37809 |
| **Total cost** | $0.398 | $0.533 |
| **Total time** | 84.9s | 82.9s |

Both models scored a perfect 24 out of 24 across the four tests. Fable 5.1 finished the full run slightly faster, 82.9 seconds against 84.9, but used 70% more tokens and cost 34% more (these results were skewed after I did the sensor test, but it still counts).

These results also don’t mean the Terminal-Bench-Science numbers are wrong. The benchmark was built using long, messy research tasks where Fable 5 allegedly fails most of the time. In my opinion, though, this doesn’t apply to what most users are using Fable 5 for. Some, yes, sure.

*Two caveats I also want to add. The claimed savings rely on cache read prices, which have dropped by 75%. My short tasks didn’t use caching at all, so my cost numbers don’t test that claim. And Anthropic says 5.1 was benchmarked with its production safeguards on, which sometimes lowered its own scores.*

What do I think?

I went looking for a 2x improvement and found a model I couldn’t differentiate from its predecessor. That doesn’t mean there aren’t any differences, but it does mean that for day-to-day tasks you were already using Fable 5 for, it may not look any different.

> > I went looking for a 2x improvement and found a model I couldn’t differentiate from its predecessor.

If you’re on Fable 5 today and your work looks like mine — code fixes, data cleanup, analysis with documented gotchas — this upgrade will not change your results. On a long agentic task, it may even cost more per run. If your work looks like the benchmark, meaning hours-long research agents that fail more than they succeed, Anthropic’s numbers say 5.1 is where the improvement lives. I couldn’t build that test in an afternoon.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)