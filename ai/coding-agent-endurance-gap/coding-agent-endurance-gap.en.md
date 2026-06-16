A coding agent that scaffolds a working app over lunch will routinely stall around 30 steps into a production refactor. It locks onto a hypothesis early and keeps patching a wrong assumption, so small errors compound until the run comes apart.

It’s a scenario that Xiaomi’s MiMo AI team may soon resign to history, as it has now open-sourced [MiMo Code](https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks), a terminal-native harness that the company claims outperforms Anthropic’s Claude Code on agentic tasks that run beyond 200 steps. The benchmark is self-reported, drawn from Xiaomi’s own beta and a survey of 576 developers, so it reads as a marker rather than a finding.

> “The endurance gap names that distance, the steps an agent survives before it drops the task.”

The number matters less than the axis on which Xiaomi chose to compete. Long-horizon reliability — holding a task together across hundreds of dependent steps — is the new front in coding agents. The field is only now learning to measure how far an agent gets before it loses the thread. The endurance gap names that distance, the steps an agent survives before it drops the task.

## Where long-horizon agents break

Ask any agent to build a small app from a clean prompt, and it performs. Carrying a single objective through a few hundred steps of editing, testing, and revision is where the failure modes show up on schedule.

Three failures recur in the long run:

1. Hypotheses harden too early, so the agent keeps patching a wrong assumption.
2. Step 40 inherits the mistakes of step 12, and the errors compound.
3. The context that mattered at the start drifts out of view by the middle of the run.

Practitioners have described this collapse for months. One widely shared [account from the team behind Ejentum](https://x.com/ejentum/status/2064330447752999088) put the breakdown near step thirty, naming hypothesis lock-in and error compounding as the usual culprits. Think of a long batch job run without checkpoints. A crash forces the whole job to restart from the beginning rather than the last saved state.

The cleaner way to assess the gap is to grade shipped work rather than rely on demos. A new benchmark from Berkeley set out to do exactly that.

## Inside Berkeley’s Last Exam

Dawn Song and postdoc Yiyou Sun at UC Berkeley’s RDI lab built [Agents’ Last Exam](https://arxiv.org/abs/2606.05405). The team reported that more than 250 industry experts across 55 occupations shaped it. The benchmark is strict by design, built to expose where agents fall short rather than where they shine. Each task is a real project a professional has already shipped, converted into a code-graded test with no human judge in the loop. The agent gets full access to a graphical interface and a command line. It solves the task however it would, and the benchmark scores only the artifact it leaves behind.

The headline finding undercuts anyone selling agents as ready for work. Berkeley’s team paired Codex with GPT-5.5, the strongest configuration tested. The paper reported below 50 percent even on the easiest tier, and under 10 percent on the hardest. Most mainstream agents, Claude Code among them, record near-zero pass rates at that difficulty. Song put the takeaway plainly: Today’s agents handle a meaningful slice of professional tasks while the hardest long-horizon work stays out of reach.

Berkeley’s results landed the same week Anthropic shipped [Fable 5](https://thenewstack.io/fable-5-developer-reactions/) into a wave of job-ready marketing. The exam answered that pitch with a number rather than a promise.

The value of the exam is that it grades the finished artifact rather than the demo. A model can top a coding leaderboard and still leave a half-finished deliverable when the task runs long, which is the gap a code-graded floor is built to catch.

## The harness layer

The most active work in coding agents now sits in the harness, the layer that holds state, paces the work, and decides which thread to pursue next. Three approaches show where it is heading.

Anthropic reported that its [nested subagents in Claude Code](https://x.com/_mauriciorubio/status/2064329181958443326) run capped at five levels deep. A frontier model plans, while cheaper subagents carry out the work and spawn their own helpers. Researchers at Renmin University of China took a different route with [Arbor](https://ruc-nlpir.github.io/Arbor/). It pairs a long-lived coordinator with short-lived executors and a persistent hypothesis tree, one that checkpoints progress and resumes after an interruption. Xiaomi’s MiMo Code addresses the same problem from the open-source side, tuning a terminal-native harness for runs beyond 200 steps.

These are not interchangeable, and the reported evidence varies widely in confidence.

| Approach | How it extends a run | Reported result | Caveat to weigh |
| --- | --- | --- | --- |
| Claude Code nested subagents | Frontier model plans, cheaper subagents execute and spawn their own | Cost-optimal multi-agent runs, the most-bookmarked developer story of its day | Depth capped at five levels, failure modes at length still unproven |
| Arbor, Renmin University | Long-lived coordinator, short-lived executors, persistent hypothesis tree with resume | 86.36 percent Any-Medal on MLE-Bench Lite, 2.5 times the held-out gain of Codex and Claude Code across six tasks | Self-reported: an internal beta and a 576-developer survey, no third-party run |
| Xiaomi MiMo Code | Open-source terminal harness tuned for 200-plus step tasks | Claims it beats Claude Code on long-horizon coding | Self-reported: An internal beta and a 576-developer survey, no third-party run |
| Kimi K2.7-Code, Moonshot | Model positioned for long-horizon agentic tasks, day-zero on Cloudflare Workers AI | Day-zero infrastructure support signals real demand for endurance | Vendor positioning, independent long-horizon numbers pending |

Every credible answer externalizes state, and Arbor makes that point most plainly of the three. Its design treats the hypothesis tree, not the context window, as the thing that has to survive in the long run. To appreciate why that holds, we need to look at how durable workflow engines solved the same problem years ago. Whatever a system cannot checkpoint must be redone after a failure.

## Why does the endurance gap matter?

For an enterprise wiring agents into a delivery pipeline, the endurance gap is a procurement question rather than a curiosity. An agent that fails at step 30 in production does not announce it. It hands back a plausible artifact built on an early wrong turn. The cost will surface later as rework, silent defects, and reviews that have to assume the worst. A benchmark like Berkeley’s gives buyers a code-graded floor for how far an agent can carry out a task before a human is needed.

> “An agent that fails at step 30 in production does not announce it. It hands back a plausible artifact built on an early wrong turn.”

> Teams should ask how a candidate harness holds state across a long run, whether it can resume from a checkpoint, and where its own published numbers put the ceiling.

Enterprises can now treat endurance as its own line in the evaluation. That means measuring how far an agent carries out a task rather than reading a coding leaderboard score and assuming the rest. Teams should ask how a candidate harness holds state across a long run, whether it can resume from a checkpoint, and where its own published numbers put the ceiling. Some vendors lead with a model benchmark and stay quiet on long-horizon behavior, answering a question the reader stopped asking.

It would be a mistake to wave either result away. Xiaomi’s 200-step claim could hold up once an independent harness runs it. Berkeley’s hardest tier may overweight tasks that no team would hand to an unsupervised agent in the first place. If models keep extending the span over which they stay coherent, part of the gap closes from the model side, and the harness earns a little breathing room. None of that changes the near-term reality, where an agent’s finished output breaks well before its demo ever does.

## What’s next

For developers tracking the tool landscape, the signal has moved away the model headline. It now sits on two numbers: How long an agent stays coherent and who verified it. MiMo Code, Arbor, and Claude Code’s subagents are early entrants in a contest the field has barely learned to score.

> “The leaderboard that matters is the one graded on shipped work rather than self-reported wins…”

The next thing to watch is whether independent runs of Agents’ Last Exam confirm or deflate the endurance claims now stacking up. The other is whether the harness hardens in the place where coding agents are bought and sold, a shift already underway. When the benchmark gets its first contested leaderboard, the figure buyers will check first is the step count an agent survives before a human steps in. That number turns a vendor promise into a procurement test.

In summary, the leaderboard that matters is the one graded on shipped work rather than self-reported wins, and that discipline benefits every team wiring agents into a delivery pipeline.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)