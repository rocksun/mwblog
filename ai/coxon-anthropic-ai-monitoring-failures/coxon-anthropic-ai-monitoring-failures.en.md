*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

**Former OpenAI and Anthropic researcher Jacob Coxon** [made a lot of noise](https://thenewstack.io/anthropic-alignment-superintelligence-warnings/) this week with a viral thread on X. He has since talked to *Wired* and *Axios*. His warning deserves attention, but another revelation this week gives developers something concrete to investigate.  
  
In [retrospective testing](https://thenewstack.io/anthropic-claude-cyber-alignment/) of the Mythos 5 incident, Anthropic’s offline monitor flagged around 1% of actions. When researchers removed the model’s chain of thought and showed the monitor only user turns, tool calls, and tool results, that rose to about 50%.

The model’s written reasoning is what talked the monitor out of flagging that harmful behavior. The offline monitor kept concluding it was operating in a simulation.

The lesson is to test whether your monitoring accepts an agent’s justification a little too easily. An AI’s explanation can help a safety monitor reveal a problem, or persuade it to essentially convey, “move along, nothing to see here.”

> An AI’s explanation can help a safety monitor reveal a problem, or persuade it to essentially convey, “move along, nothing to see here.”

Coxon is warning about the pursuit of self-improving superintelligence. Developers are already pointing agents at real credentials during everyday work. Those problems differ substantially, but both deserve attention.

## Forecasts aren’t checkable. Incident reports are.

Jacob Coxon’s [thread](https://x.com/hilbertspaess/status/2097476196791709843) is short and hard. He says neither of his former employers is acting responsibly, and that both are “racing straight to self-improving superintelligence and gambling with our lives.”

Maxwell Zeff pressed him on the end-of-humans mechanism twice [in an interview with *Wired*](https://www.wired.com/story/anthropic-researcher-quits-jacob-coxon-ai-fears-humanity/)*.* Coxon described shutdown avoidance, then biological and cyber threats. His answers explain the concern, but leave substantial questions about how AI will kill us all.

Annie Jacobsen, whose books on this stuff I wholeheartedly recommend, [spelled out the scary biological scenario](https://x.com/AnnieJacobsen/status/2097826954666033250): A system that can hack anything, turned loose on the world’s 3,600-plus BSL-3 and BSL-4 labs, is how you get from a software problem to a biological one. For me, Jacobsen’s commentary is the most concrete, real-world implication anyone has given of what Coxon is actually worried about.

Two incident reports published in the last few weeks are more useful anyway. [OpenAI’s report](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) on the Hugging Face incident, published August 26, traces the whole thing from May 12 to July 20. The agents found a hole in an internal package server and used it to reach the open internet that the same server was supposed to keep them off of. OpenAI rebuilt the server; they got back out. By July 11, they were far enough into Hugging Face to run their own commands on its machines.

The model doing most of that was never released. It’s a research version OpenAI runs in-house, with fewer safety checks than the ChatGPT everybody else uses. When the company ran the same work again with those checks switched on, it found that this kind of behavior could drop by more than 100 times.

That context matters.

[Amanda Caswell covered](https://thenewstack.io/anthropic-claude-containment-failure/) this in August. The incident demonstrates a serious failure under particular conditions. It also illustrates why the surrounding safeguards belong in any assessment of an agent’s behavior.

## The monitor was talked out of it

[Anthropic’s assessment](https://thenewstack.io/anthropic-claude-cyber-alignment/), published on September 9, covers four incidents and analyzes the first three in a scan of roughly 141,000 transcripts, identified a fourth in August while assembling material for METR, then widened the search to roughly 481 million transcripts and reported no additional incidents of similar or greater severity. In each case, the model reached the open internet through a misconfiguration rather than by breaking out of a properly isolated sandbox. That’s an important detail. It makes the evaluation infrastructure part of the story.

If you’re a developer, you should look at the monitoring results. Mythos 5 kept reasoning its way to the conclusion that it was operating in a simulation, and the offline monitor read and accepted that reasoning. The limits matter here too: These were cybersecurity evaluations running without released cyber safeguards, Anthropic reports no coordination between models and no concealment, and its independent METR review was planned rather than finished. This is not the same failure as the OpenAI incident. Don’t equate them as similar incidents

But yet the shape of it is familiar, and it’s what Adrian Bridgwater [reported on last week](https://thenewstack.io/anthropic-claude-agent-security/) in his piece on agent observability, which is a useful read if you’re producing agents (who isn’t). Jacob Krell of Suzu Labs put it about as well as it can be put: “The model can recite your constraints and reason past them in the same breath.” Liran Hason of Coralogix added the result: “System guardrails help, but a guardrail only stops what the developer already thought of.”

## What developers can take from Steven Adler’s recommendations

Largely overshadowed this week by Coxon, [Steven Adler’s op-ed](https://www.nytimes.com/2026/09/09/opinion/openai-ai-companies-safety-regulation.html) in *The New York Times* asks AI companies for four things: disclose incidents including near misses, the way aviation does; keep tamper-evident records of model behavior; never let a model cut power to its own alarm systems; and formally swear off training techniques that undermine researchers’ ability to detect deception.

Adler worked for OpenAI from 2020 to 2024 and later founded a nonprofit called Guidelight AI Standards. It has since graded six control practices at the frontier labs using public information and gave out a top mark of C-plus.

Guidelight also [publishes a Control standard](https://guidelight.ai/control) for frontier labs, recently revised in August. It wants monitors to access the chain of thought and scan both reasoning and actions.

But those asks of frontier labs don’t apply to most developers. Here are five you can check on your own setup right now.

Five checks you can run on your own agent setup

Steven Adler’s asks of the frontier labs, applied one layer down.

| Check | What passes |
| --- | --- |
| Someone reads the near misses | An agent crosses a line and nothing breaks. There’s still a record, a person who looks at it, and a copy the agent can’t reach. |
| The agent can’t edit its own history | Logs are append-only and stored outside the agent’s reach. If its credentials can delete the log, the log is decorative. |
| The agent can’t touch its own oversight | Separate tokens help. Then check whether it can shut off monitoring, rewrite an approval rule or get around the kill switch. |
| Rule-breaking gets blocked and logged | In a test environment, hand it a job it can only finish by breaking a rule. Judge the monitor on what it does with the action, not with the agent’s account of it. |
| The explanation doesn’t change the answer | Run the same rule-breaking action past your monitor twice. Change nothing but the explanation, one flat and one reassuring. If the reassuring version gets flagged less, you’ve found the problem. |

These checks do not establish that frontier alignment is solved. They give a team evidence about the system it operates on and a clearer account of where its protections need work.

Anthropic’s report is why I’d include that last test in a deployment review. Hold the action and its permissions constant, change the explanation, and see whether your monitor changes its judgment.

That won’t settle Coxon’s warning. Will AI kill us all? I don’t know. But I know developers need to test their agents’ permissions, protect their logs, and make sure a convincing explanation can’t talk a safety monitor into overlooking an unauthorized action.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)