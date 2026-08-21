[Nvidia](https://thenewstack.io/nvidia-local-frontier-models/) first introduced its [Agentic Variation Operators (AVO)](https://arxiv.org/pdf/2603.24517) general-purpose coding agent system in late March 2026. The company has now unravelled the architecture and the system-level mechanisms that enable AVO to sustain long-running autonomous work and applied it to the open platform advanced AI reasoning benchmark [ARC-AGI-3](https://arcprize.org/arc-agi/3).

In a [team blog](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/) released on Friday, a five-person team of Nvidia software engineers, machine learning specialists and AI research interns describe how AVO elevated [Claude Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/) from a reported 30.2% model baseline score on ARC-AGI-3, to 100% when run as part of the complete AVO agent system.

“[This result] shows that system design – not model capability alone – can unlock frontier-level long-horizon performance,” wrote the team.

## What tasks does Nvidia’s AVO handle?

Evolving from the core DNA of what constitutes an [agent harness](https://thenewstack.io/agent-harness-distributed-feedback-problem/), AVO handles the agentic architecture tasks associated with inspecting and editing code, running commands, consulting documentation, and validating its work through execution. AVO’s distinguishing focus is said to be “sustained in-context autonomous operation” across extended, multistep tasks on long horizons.

Non-profit AI research and benchmarking body [ARC Prize](https://arcprize.org/) used an [analysis post this July](https://arcprize.org/results/anthropic-claude-opus-5) to report the 30.2% score for Claude Opus 5 at high reasoning effort on the public set of environments and tasks on the ARC-AGI-3 system. According to ARC Prize, this “demonstrates strong logical reasoning” and, when Claude Opus 5 was run at Max reasoning effort, it scores 97.5% on ARC-AGI-1 and 90.4% on ARC-AGI-2 semi-private.

The ARC-AGI-3 benchmark uses [Relative Human Action Efficiency](https://docs.arcprize.org/methodology) (RHAE), a metric that combines task completion with per-level action efficiency relative to first-time human baselines, where performance is aggregated across different levels and environments.

“AVO achieved a 100.00 RHAE score across all 25 environments in the ARC-AGI-3 public set, completing all 183 levels. The result illustrates a broader point: evaluating a model is not the same as evaluating an agent. Model capability matters enormously, but the surrounding system determines how effectively that capability can be converted into sustained autonomous progress,” stated the Nvidia blog team, headed by principal engineer [Terry Chen](https://www.linkedin.com/in/terry-chen-11a85310a/).

> “Model capability matters enormously, but the surrounding system determines how effectively that capability can be converted into sustained autonomous progress.”

## How an agent decides on its next candidate

AVO was first demonstrated on difficult software engineering and GPU-kernel optimization tasks. In this work, AVO replaces what Chen and team describe as the “predefined variation step of conventional evolutionary-search systems” with an autonomous agent that decides how to generate the next candidate i.e. what to inspect, what to change, what to test, and what to commit.

The team used that work as a foundational research cornerstone to then progress to the ARC-AGI-3 benchmark.

“GPU-kernel optimization and the ARC-AGI-3 benchmark appear very different on the surface,” noted the Nvidia team. “One involves source code, compilers, profilers, and throughput. The other involves unfamiliar interactive environments in which an agent must infer the effects of available actions, discover objectives, and act efficiently enough to make progress. But the underlying computational pattern is similar. “

In both settings, the agent must:

* Build hypotheses from incomplete evidence
* Take actions through an external interface
* Observe the consequences
* Preserve useful state
* Revise its model of the problem
* Recover from incorrect assumptions
* Continue making progress over a long horizon

Preserving state and progress, reworking backwards past incorrect assumptions and working on long-horizon tasks beyond a single model’s context window with an incomplete picture of what’s in front of the system requires two specific mechanisms to be present in AVO: [persistent memory](https://thenewstack.io/how-to-add-persistence-and-long-term-memory-to-ai-agents/) and supervision.

> “Preserving state and progress [and] working on long-horizon tasks beyond a single model’s context window with an incomplete picture of what’s in front of the system requires two specific mechanisms to be present: persistent memory and supervision.”

Persistent memory is used here to carry forward prior implementations, evaluation results, [compiler](https://thenewstack.io/meta-releases-open-source-react-compiler/) and profiler outputs, and accumulated reasoning. It allows the agent to resume from the current state, instead of having to repeatedly reconstruct the search – exactly the sort of “sustained autonomous progress” that Chen and team have made their holy grail.

Supervision is also key; a supervisor (a programmatic software module within the AVO system, not a human in this case) monitors the broader search trajectory and can intervene when progress stalls.

## Nvidia AVO paired with GPT-5.6 Sol

AVO is also designed to operate across frontier models. While the team’s full public-set result used Claude Opus 5, it additionally paired AVO with [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/) on what it has classified as a “challenging subset of games” for further experimentation. In these tests, Sol reached matched levels faster in wall-clock time in several cases, while Opus used fewer environment actions in matched-level comparisons.

A quirky-sounding term perhaps, wall-clock time (obviously) refers to real world time as experienced by humans. It differs from CPU/GPU time, which may be divided by multiple cores (let’s say 8-cores) so that 80 seconds of compute time becomes 10 seconds of wall-clock time.

“These preliminary results suggest complementary operating profiles across models, and we leave a broader systematic comparison to future work,” noted Chen and team. “These results cover the 25-environment ARC-AGI-3 public set using the official scorecard and RHAE metric. They are not results on the semi-private or fully private competition sets.”

## What the team learned from benchmarking AVO on ARC-AGI-3

The assembled engineers have said that the most important result was not simply the 100.00 score, but the fact that the same agent architecture transferred from highly specialized GPU-kernel optimization to a very different interactive reasoning task.

The team reminds us that in GPU optimization, feedback comes from compilers, tests, profilers, and performance benchmarks. In ARC-AGI-3, feedback comes from environment transitions and action outcomes. This means that, essentially, the interfaces differ, but the loop is the same i.e. the loop works to form a hypothesis, act, observe evidence, update state, and continue.

“This suggests that generality can come not only from domain knowledge, but from the machinery that allows reasoning and feedback to compound over time. More broadly, long-horizon capability is a property of the full system. Memory determines what survives, tools determine what actions are possible, feedback grounds progress, and recovery allows work to continue beyond a single model invocation,” concluded the Nvidia AI ensemble.

The Nvidia blog team in full included the above-noted Terry Chen, Nvidia director and distinguished engineer in competitive machine learning [Jean-Francois Puget](https://www.linkedin.com/in/jfpuget/), VP of high-performance AI [Humphrey Shi](https://www.linkedin.com/in/humphreyshi/), and AI research interns [Yeyin (Eva) Zhu](https://www.linkedin.com/in/yeyin-zhu-571b072a4/) and [Zhifan Ye](https://www.linkedin.com/in/zhifan-ye/).

The team’s final words restate the crux of the investigation here: the model matters, but the model is not the entire agent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)