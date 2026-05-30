This week, solo researcher [Udit Akhouri](https://www.linkedin.com/in/udit-akhouri-10160a168/) took to [r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/i_gave_claude_code_adhd_and_it_thinks_2x_better/) on Reddit to launch a new third-party Agent SDK tool with the headline: “I gave Claude Code ADHD.. and it thinks 2x better now.”

As described on [GitHub](https://github.com/UditAkhourii/adhd), ADHD is a skill for coding agents built on Claude Agent SDK; it “fans out parallel divergent thoughts under different cognitive frames, scores, prunes traps, deepens the survivors.”

The tool is already seeing fast traffic on GitHub, but some researchers remain dubious about its novelty and that “2x better” claim.

## What Claude Code looks like with ADHD

Akhouri is founder of Brane Labs, an AI compliance and safety research lab in AI-assisted healthcare, drug discovery, and life sciences, as well as founder of Exthalpy, a clinical autonomy platform for outpatient clinics and hospitals.

His [paper](https://uditakhourii.github.io/adhd/), “ADHD: Parallel Divergent Ideation for Coding Agents,” describes ADHD as “tree-of-thought with cognitive-frame branching, generator-critic separation, and pruning.” In his Reddit post, Akhouri says the tool was “inspired by how the mind of someone with ADHD works — think in a lot of directions and go deep in a few.” In other words, Claude Code with ADHD fans out into several isolated reasoning branches, scores them, and develops the most promising.

When asked where the tool’s purpose really lies, Akhouri tells *The New Stack* ADHD is “good for brainstorming and planning, not coding.”

Specifically, he positions ADHD as a “reasoning and planning layer for AI agents.” It’s not designed to help write code faster but to support architectural choices and research decisions before code gets written.

## Is this really something new?

Yes and no, it’s fair to say.

When asked what novelty ADHD brings to the table, [Sean Robinson, Ph.D.](https://www.linkedin.com/in/sean-robinson-phd/), CTO and co-founder of Empromptu.ai, tells *The New Stack*, “I don’t think it’s strictly new as an agent pattern. It looks like a familiar parallel sampling and selection strategy, but packaged in an interesting way for engineering decisions.”

In the Reddit thread where Akhouri dropped his creation, there is some community sentiment to echo Robinson’s comment. One Redditor [says](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/comment/onxwgmn/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), “Isn’t that exactly what GPT Pro does? It runs multiple xhigh eval concurrently and then evaluates them all and use[s] the highest score one.” Another [chimes in](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/comment/onxptf2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), “I thought this was the concept behind agent teams already?”

> “I don’t think it’s strictly new as an agent pattern. It looks like a familiar parallel sampling and selection strategy, but packaged in an interesting way for engineering decisions.”

When asked directly how ADHD differentiates itself, Akhouri tells *The New Stack*, “GPT Pro’s parallel eval pattern and CrewAI agent teams are implementations of parallel processing, but they are closed, opaque, and not composable by the end user.” In contrast, he says ADHD is “an explicit, readable layer that lives in your Claude environment.” When stacked against GPT Pro and CrewAI-style agent teams, he says ADHD stands out for its “transparency and composability.”

When asked for his take, [Andrew Moore](https://www.linkedin.com/in/andrew-moore-016b751/), the current CEO of Lovelace AI, a former Google vice president, and a former dean and professor at Carnegie Mellon University, seems to understand where Akhouri is coming from. He tells *The New Stack*, “The genuinely new idea [in ADHD] is finding another way to create diversity in a set of parallel thinkers.”

## Does it really make Claude Code “think 2x better”?

That’s where there seems to be some disagreement.

When asked how he arrived at that “2x” claim, Akhouri points to the evals: “The 2x framing came from averaging across dimensions.”

That is, five out of six test problems show ADHD outscoring the baseline. The rubric on [GitHub](https://github.com/UditAkhourii/adhd/blob/main/EVALS.md) gives the following deltas: +4.17 for breadth; +5.17 for novelty; +7.67 for trap\_detection; +3.00 for actionability; +0.83 for builder\_usefulness.

![](https://cdn.thenewstack.io/media/2026/05/88a11732-claude-code-adhd-aggregate-scores.png)

Image Source: [GitHub](https://github.com/UditAkhourii/adhd/blob/main/EVALS.md)

Akhouri says the evals are fully transparent, documented on GitHub, “and can be reproduced independently at any time by running npm run evals.”

But it’s worth noting how much trap\_detection is swinging the curve. With a delta of +7.67, trap\_detection is a heavy hitter in the average calculation; removing it shrinks the average from 2.52x to 1.85x.

> “A ‘2x better’ claim needs more than a few open-ended wins. It needs a validated evaluation set, multiple judges, ablations, and evidence that the method improves without just rewarding verbosity, novelty, or branch diversity.”

And then there are concerns about the benchmark size. “Six engineering problems is interesting, but it is not enough to treat the result as general,” says Robinson. “A ‘2x better’ claim needs more than a few open-ended wins. It needs a validated evaluation set, multiple judges, ablations, and evidence that the method improves without just rewarding verbosity, novelty, or branch diversity.”

[Noe Ramos](https://www.linkedin.com/in/noe-ramos-psyd-3a1808178/), vice president of AI operations at Agiloft, when asked about ADHD’s evaluations, tells *The New Stack* a similar story: “Without established inter-rater reliability, the gains on dimensions like trap detection and novelty are interesting but not yet stable findings. The ‘2x better’ framing needs more than six problems to carry that weight.”

There’s also the question of whether or not same-stack familiarity, i.e., the fact that the method is built on Claude’s stack and judged by a Claude-family model, has anything to do with the scores. Both Robinson and Noe indicate same-stack bias may be at play — “that does not mean the result is invalid,” says the former, “but it means the paper should test external judges and other model families.”

## Where things go from here

Despite certain eyebrow-raising about novelty or eval scores, it seems Claude Code with ADHD is already off to the races. Akhouri tells *The New Stack* Repowire “is actively integrating ADHD into their stack as of this week.” And at the time of writing, GitHub shows 286 stars for the skill and 12 forks.

But [Nikolaos Vasiloglou](https://www.linkedin.com/in/vasiloglou/), vice president of research ML at RelationalAI, tells *The New Stack* Claude Code with ADHD “is yet another exploration method sitting on top of LLMs,” arriving on the scene when the industry is already facing a token-consumption problem: “While ADHD has impressive results, it comes at a point where organizations are suffering from excessive token spending.”

## And what about that name?

Naming a skill for coding agents after a neurodevelopmental disorder is a bold move — certainly one that will capture attention. But Akhouri insists the title was organic, not marketing-driven:

“We [Brane Labs] were using Claude Code heavily for research workflows and kept hitting the same wall: The reasoning was deep but narrow. Linear. It would go far down one path and miss lateral connections entirely. That’s when the ADHD framing clicked.”

Describing himself as “personally familiar with how the ADHD brain works,” Kahouri tells *The New Stack* he wanted to emulate the structure of ADHD thinking inside the LLM sandbox and hopefully “reveal patterns that purely linear thinkers miss” — though he clarifies the moniker is intended as a metaphor, not a neuroscience claim.

When asked where it stands on third-party Agent SDK tools branding themselves around clinical conditions, Anthropic did not respond.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)