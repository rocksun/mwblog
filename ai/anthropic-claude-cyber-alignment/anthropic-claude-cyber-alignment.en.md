**This week, Anthropic acknowledged that the three cyber incidents** it disclosed this summer weren’t just the result of a misconfigured test environment. It turns out that Claude’s own behavior was part of the problem.

Recall in July when the AI company released a [report](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) on three cases where Claude models reached the open internet from misconfigured test environments and compromised real third-party systems — a telling example of the limits of AI safety tests and [why AI evaluation infrastructure needs production-grade security](https://thenewstack.io/anthropic-claude-containment-failure/).

Upon deeper review, [Anthropic now says](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) that explanation was incomplete. Beyond the operational failure, the models themselves displayed two recurring alignment failures: biased reasoning and recklessness. And, actually, there was a fourth incident that the AI company only found out about after further investigation.

It’s awkward timing, given one of Anthropic’s pretraining researchers, Jacob Coxon, resigned this week due to [concerns about superintelligence that “could kill us all,”](https://thenewstack.io/anthropic-alignment-superintelligence-warnings/) taking to X to write:

“The people building AI earnestly believe that it could kill us all by the end of the decade. This is not a marketing stunt. If anything, many executives and senior researchers will couch their phrasing in the press to sound sensible — but I hear the same people express fear privately.”

The incidents definitely don’t prove this kind of risk, but they do illuminate how models can behave unexpectedly — and how existing evaluations can fail to catch it.

## The problem was more than an operational failure

This summer, when Anthropic shared its initial findings, it said the three cyber incidents were “closer to a harness and operational failure than a model alignment failure,” with Claude seeming to believe it was operating in a simulation without internet access.

But a closer look at the transcripts revealed that the problem was not simply the model reaching the internet by mistake; Claude also showed signs of misaligned reasoning.

> “When we made targeted modifications to the transcript to make it clearer that the model was not in a simulation, Claude Mythos 5 still took offensive actions, despite acknowledging a greater possibility of real-world harm.”

After widening the initial search to about 481 million transcripts, including those from the company’s Frontier Red Team, as well as non-cyber evaluations, reinforcement learning (RL) environments, subagent logs, and others, Anthropic conducted two scans.

First, it scanned these transcripts for signs of internet access, whittling down the pool to 9.2 million flagged for escalation. It then used Claude to review this smaller batch, re-identify the known incidents, and look for others of similar or worse severity.

What did it find? It found more than an operational failure. Anthropic says its investigation identified “two recurring alignment issues, present at varying levels of severity across the incidents.”

It names these issues as biased reasoning, where Claude disregarded or misinterpreted evidence that was, in fact, on the internet, and recklessness, where Claude was willing to take harmful actions to pursue a task.

Anthropic was already concerned that [Claude Mythos 5 uploaded a malicious package to PyPI](https://thenewstack.io/anthropic-claude-containment-failure/), but the model repeatedly said it believed it was operating in a simulation. Anthropic now says the simulation explanation does not fully account for the model’s behavior and that its reasoning appears to have been biased.

“When we made targeted modifications to the transcript to make it clearer that the model was not in a simulation, Claude Mythos 5 still took offensive actions, despite acknowledging a greater possibility of real-world harm.”

## And there was a fourth incident Anthropic missed the first time

Anthropic’s new alignment assessment also contains another less than reassuring revelation: It missed one of the four incidents the first time around.

As the AI company explains, its first review relied on an agentic search due to “the volume of transcripts and [its] desire to disclose incidents quickly.” But that scan missed a set of transcripts that had also had internet access.

How did the cat get let out of the bag? It happened in August when Anthropic was assembling transcripts to share with [METR](https://metr.org/) (Model Evaluation and Threat Research). This research nonprofit measures whether and when AI systems might threaten catastrophic harm to society. The fourth incident dates from January 2026 and involves an early version of Claude Opus 4.6.

Discovering the fourth incident pushed Anthropic to broaden its search to the roughly 481 million transcripts described above, giving it more information to analyze and ultimately surfacing new insights into Claude’s “biased reasoning” and “recklessness.”

While this broader search didn’t turn up any more incidents of what Anthropic describes as “similar or worse severity,” the investigation isn’t over. Per the AI company, it’s signed an agreement with METR, granting the organization wide-ranging access to transcripts and Anthropic employees for eight weeks to investigate the incidents independently. The agreement can be extended if both parties agree.

## Anthropic reproduced the failure to try to understand if newer models would do the same

Beyond reviewing the original incidents, Anthropic is taking other steps to try to understand how things went pear-shaped in the first place. It put Claude Opus 5 and Claude Mythos 5.1 in a simulated replication of the Mythos 5 scenario — the one where the model uploaded a malicious package to PyPI. Anthropic reports:

“Both take harmful actions substantially less often than Claude Mythos 5 did, but they still engage in the same behaviors at concerning rates.”

It notes that both models only took harmful actions after stating that they were, indeed, acting in a simulated environment. Anthropic also says that Mythos 5 appears to be “an outlier in terms of poor performance” on evaluations for biased reasoning, recklessness, and willingness to probe boundaries.

> “Both take harmful actions substantially less often than Claude Mythos 5 did, but they still engage in the same behaviors at concerning rates.”

Still, it’s not such a clear indication of how the newer models would behave in the real world. As the AI company adds, “because the reproduction is, in fact, a simulation, we are cautious about how far these results generalize to the real world.”

Additionally, Anthropic looked back into its training to search for a root cause of Claude Mythos 5’s biased reasoning, but came up short. While it didn’t identify a single root cause, the company says biased reasoning decreased across its production models over time, potentially due to updated RL and alignment training.

Anthropic admits it still has work to do. Since its pre-release auditing didn’t catch misalignment of this severity, it’s since added evaluations to specifically target these behaviors, though reliably doing so is still a challenge.

## Anthropic admits the failures were serious, but says they’re “narrow”

While Anthropic clearly calls out the four cyber incidents as “valuable warning shots,” it also points out that their scope was limited:

“While Claude’s actions were misaligned, they remained within a narrow scope,” the AI company says, pointing to the fact that all incidents included a single Claude instance and the model never attempted to coordinate with other agents or conceal evidence of its actions.

It says these behaviors playing out in ordinary use are “unlikely” and that, if they did, the safeguards shipped with production models would add more defenses that didn’t exist in these evaluations.

But following Coxon’s remarks about the risks of superintelligence, and Anthropic’s own alignment science lead, [Evan Hubinger](https://www.linkedin.com/in/ehubinger/), [responding](https://x.com/EvanHub/status/2097497037956891126) that Anthropic “really do[es] earnestly believe AI could kill all humans,” seeing Claude go off the rails isn’t comforting.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)