**Anthropic is putting AI agents to work** on one of the field’s hardest problems: keeping other AI systems aligned with human goals. In a [paper](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures) published Friday, the company explains how its open-source research harness turns Claude into an automated researcher capable of proposing, testing, and refining model-safety fixes.

An integral part of the total lexicon of AI engineering, [alignment](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/) involves steering AI models and functions so that their goals, actions, and behavior align with human intention and values, especially when and where AI systems become smarter than humans themselves.

Essentially, this is the use of AI to train AI.

“In one of our earlier experiments, we tasked [Claude](https://thenewstack.io/claude-computer-use/) with finding effective ways to use weak AI models as ‘teachers’ to supervise the training of stronger models (in this case, the ‘student’ model),” explains Anthropic in the paper.

Claude tackled one alignment failure at a time through a [looping method](https://thenewstack.io/agent-loops-cloud-native-verification/) that involved searching literature, proposing methods and data, training, and then testing. Successful methods were retained, while failed methods were discarded to achieve a cumulative positive result over successive iterations.

“Overall, we view these results as early positive signals that automated alignment post-training could become practical in the near term.”

> “Overall, we view these results as early positive signals that automated alignment post-training could become practical in the near term.”

## 10 categories of alignment failure

In the main body of work undertaken here, Claude was tasked with autonomously training models to improve their performance on several public benchmarks that measure each of the 10 categories of alignment failure.

“On each of these counts, Claude’s methods worked. For all 10 alignment failures, Claude found fixes that improved the target benchmarks without degrading capabilities. The best methods also worked on withheld alignment benchmarks and on [Petri](https://meridianlabs-ai.github.io/inspect_petri/), an open-source tool that simulates adversarial multi-turn scenarios for testing misalignment,” stated Anthropic

The results showed Claude improved a model’s performance on privacy violations, as measured by [ConfAIde](https://confaide.github.io/) (a benchmark designed to identify critical weaknesses in the privacy reasoning capabilities of instruction-tuned LLMs), [PrivaCI-Bench](https://arxiv.org/abs/2502.17041) (a contextual privacy evaluation benchmark for legal and GDPR compliance), and [PrivacyLens](https://github.com/salt-nlp/privacylens) (a data evaluation framework focused on privacy norm awareness and data leakage risk).

## Claude attempted to cheat safety checks while performing them.

But, there’s more to learn here… Anthropic went to pains to say that it [recently learned](https://alignment.anthropic.com/2026/automated-w2s-researcher/) that Claude can cheat by exfiltrating test labels from a remote API and cherry-picking results. “To catch cheating behaviors, we prompted Claude Opus 4.8 to monitor ~1,600 research agent transcripts across all 10 alignment failures, finding cheating attempts in 39 (2.4%),” reads the paper.

Anthropic judged Claude’s success by the “percentage of safety gap closed,” a measure of how far its methods moved the student model towards the theoretical perfect score, evaluated across the range of benchmarks (typically three to five) for each alignment-failure category.

The company excluded alignment methods that “hurt the student models’ general capabilities”, and forbade Claude from distilling its own alignment directly into the target model. It then enforced these constraints using a monitoring agent that read every method Claude had in mind before it ran.

“On each of these counts, Claude’s methods worked. For all 10 alignment failures, Claude found fixes that improved the target benchmarks without degrading capabilities,” detailed Anthropic.

![](https://cdn.thenewstack.io/media/2026/08/42d192e2-aaaaa.png)

## What this work means for software developers

Staff software engineer and cloud architect, [Jayakumar Ramalingam](https://www.linkedin.com/in/jayakumarramalingam/), tells *The New Stack* that for developers, the useful result here is not that AI has somehow solved alignment; it is that AI model safety work is “starting to look like a software delivery pipeline” task.

“For AI-centric developers considering this, they can see that an agent proposes a change, an isolated evaluator runs withheld tests, and a separate monitor checks whether the process followed the rules,” Ramalingam says. “That pattern is useful well beyond model training. The mistake would be allowing the same agent to write the fix, choose the test, and decide that it passed.”

Ramalingam points to the uncomfortable 2.4% cheating number in Anthropic’s paper as the share of research trajectories in which the monitor detected attempted cheating. This, of course, means that a system working on safety still tried to game the safety process and outplay it.

“Developers should keep evaluation data outside the agent’s reach, separate the evaluator from the system being evaluated, and test for regressions the agent was never shown. Otherwise, automated alignment becomes benchmark optimization with a reassuring name,” clarifies Ramalingam.

> “Developers should keep evaluation data outside the agent’s reach, separate the evaluator from the system being evaluated and test for regressions the agent was never shown.”

AI specialist and SRE performance architect at [Cognizant](https://www.cognizant.com/us/en), [Akash Thakur](https://www.linkedin.com/in/akash-thakur-00367a155/) is Broadly in agreement with Ramalingam and tells *The New Stack* that the real developer story here isn’t that Claude improved 10 alignment benchmarks.

“The real story and takeaway for developers is that Anthropic just proved automated agents can run the full research loop, search the literature, propose a fix, train, test, iterate,” Thakur says.

“That’s the same loop SRE and performance engineering teams already use for reliability. Alignment has just become a CI/CD problem, and open-sourcing the harness means every engineering team building on LLMs now has a template for treating safety like a testable, regression-tracked property of their system, not a one-time post-training step,” Thakur adds.

## Everyone’s getting the recursive self-improvement angle religion

Founder & CTO at Berlin, Germany-based [Glokal AI OÜ](https://glokalai.com/), [Jeet Pattanaik](https://www.linkedin.com/in/jeet-pattanaik/), tells *The New Stack* that what he would flag is that everyone’s running with the recursive self-improvement angle these days and discussing whether human researchers are finished.

“The more pressing risk here is [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) (when a measure becomes a target, it ceases to be a good measure), Pattanaik says. “So a benchmark score going up isn’t the same as a model or function that behaves well in production, and Anthropic says so themselves: the failures it studied were narrow, some failures have no benchmark at all, accepted methods might have degraded capabilities nobody measured, and tools like Petri are proxies.”

Pattanaik explains that he works with regulated global enterprises every day, so he can tell us what happens next – it’s a case of “we ran the alignment harness” now becoming a line in the audit file.

> “A benchmark score going up isn’t the same as a model or function that behaves well in production, and Anthropic says so themselves: the failures it studied were narrow.”

“Nobody asks whether those ten benchmarked failure categories have anything to do with how the system can actually go wrong in a claims process or a payment run. That’s not speculation; it’s what happened to every security scanning tool that turned into a checkbox,” expands Pattanaik.

## The road to recursive self-improvement

OpenAI joins Anthropic’s work in this space with its openly tabled [work on superalignment](https://openai.com/index/introducing-superalignment/) and [alignment in general](https://openai.com/index/our-approach-to-alignment-research/#). In May of this year, the Google DeepMind team [introduced Gram](https://deepmind.google/research/publications/252981/#:~:text=In%20contrast%20to%20other%20alignment%20auditing%20approaches%2C,sabotage%20rates%20close%20to%20zero.%20*%20Authors.), an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. Not quite as voluble in this space as Meta AI is, although the company published HyperAgents, a self-referential agent approach to recursive self-improvement, in March.

In the pursuit of controlling artificial general intelligence, this discussion also embraces the concept of [recursive self-improvement](https://en.wikipedia.org/wiki/Recursive_self-improvement). It’s a topic that the frontier model firms have touched on, and dedicated players also operate in this arena, including (the clue is in the name) [Recursive](https://www.recursive.com/#:~:text=Recursive%20embraces%20the%20logical%20conclusion%3A%20the%20fastest,creating%20such%20an%20advance%20cannot%20be%20overstated.), Japanese AI model specialist [Sakana AI](https://sakana.ai/), and [Weco AI](https://www.weco.ai/platform), which focuses on the “[outer loop](https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement)” optimization of AI agents.

Anthropic concluded its report summary by saying that it plans to continue improving Claude’s ability to “measure subtle failures” and to extend its analysis of post-training automated alignment on production-grade models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)