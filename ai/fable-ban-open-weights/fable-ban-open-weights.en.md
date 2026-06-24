On Friday, June 12, the United States government ordered Anthropic to suspend Claude Fable 5 and Mythos 5 for all foreign nationals. Anthropic complied and pulled both models for all customers worldwide. Within the same week, a cluster of open-weight coding models gave enterprises outside the US a set of fallback candidates. Two of those releases were already in flight when the order landed, and the ban made enterprises treat them as urgent rather than theoretical.

Enterprise buyers have seen this in hardware procurement. When a single supplier gets cut off, the qualified-alternate list suddenly matters. The teams that already second-sourced keep shipping while the rest scramble.

> The teams that already second-sourced keep shipping while the rest scramble.

Open weights are that second source for AI models. Between June 9 and June 13, that hedge became real. Cohere shipped North Mini Code, Moonshot shipped Kimi K2.7-Code, and Zhipu opened GLM 5.2 inside that window. North Mini Code and Kimi K2.7-Code came with downloadable weights. GLM 5.2 went out first through Zhipu’s Coding Plan, with open weights promised the following week. All three cost less than a hosted frontier model, and all three integrate with the agent harnesses developers already use.

---

### Anthropic, Fable, and the US government:

---

## What Washington actually did

The order arrived at 5:21 p.m. Eastern and cited national security authorities under export-control rules. Anthropic says the government believed it had found a way to jailbreak — in this case, to create a bypass that exposes unsafe behavior in a guarded model — Fable 5. The directive covered any foreign national inside or outside the United States, including Anthropic’s own foreign-national staff. Ordinary service could not cleanly separate those users, so Anthropic disabled both models for everyone. The company disputes the finding and says the evidence behind it is narrow and unverified.

> Any enterprise that had built automation on Fable 5 lost its engine in an afternoon.

Fable 5 was nine days old at that point. [Anthropic had launched it on June 9](https://thenewstack.io/anthropic-claude-mythos-fable-5/) as the first publicly available model in its Mythos-class line. The company claimed a lead on nearly every benchmark it published, with the margin widening on longer tasks. Any enterprise that had built automation on Fable 5 lost its engine in an afternoon. That exposure is exactly what open weights are meant to remove.

## The open field that moved in

None of these models were built in response to the ban. North Mini Code shipped three days before the order, and Kimi K2.7-Code shipped the same day. Zhipu opened GLM 5.2 the next day and timed the release to 5:21 p.m., an echo of the order the day before. Read together, they show how fast enterprises could line up fallback options when a hosted model went dark.

### North Mini Code from Cohere

Cohere shipped [North Mini Code](https://cohere.com/blog/north-mini-code) on June 9, the same day Fable 5 launched. It is a mixture-of-experts model with 30 billion total parameters and only 3 billion active per token. That sparsity lets it run on a single H100 rather than a rack of them.

The license is Apache 2.0, so a company can self-host the weights without a legal review. Cohere aims it at the sovereign developer, the enterprise whose compliance team will not let proprietary code leave the building. It scored 27.6 on the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model), short of frontier numbers. Independent testers also flagged that it emits far more output tokens than rivals, a verbosity that adds up in production. For a model a bank can run on-premises, that tradeoff is often acceptable.

### Kimi K2.7-Code from Moonshot

Moonshot released [Kimi K2.7-Code](https://www.kimi.com/resources/kimi-k2-7-code) on June 12, the same day as the ban, under a Modified MIT license. It is built on the earlier K2.6 base and tuned for long-horizon coding that spans many files and steps. The architecture has a total of 1 trillion parameters and activates 32 billion per token.

Moonshot reports double-digit gains over K2.6 and roughly 30 percent fewer reasoning tokens. Those numbers are vendor-run and await independent confirmation. The hosted API lists 95 cents per million input tokens and $4 per million output tokens. That price sits well under hosted frontier rates. The weights are also downloadable, though the Hugging Face repository runs roughly 595 gigabytes and practical serving needs server-class multi-GPU memory.

### GLM 5.2 from Zhipu

Zhipu opened [GLM 5.2](https://codersera.com/blog/glm-5-2-release-1m-context-coding-2026/) to its Coding Plan subscribers on June 13, one day after the ban. In its launch note, the company argues that frontier intelligence should not belong only to those a government allows to use it. The model carries a one-million-token context window. It ships out of the box compatible with Claude Code, Cline, OpenCode, Crush, and OpenClaw.

The launch itself was unusually thin for a flagship. Zhipu published no benchmarks, exposed no public API, and gated access behind a paid plan priced at about $18 per month. Open weights were promised the following week. A widely shared post then placed GLM 5.2 at the top of the community BridgeBench leaderboard, at a tenth of the cost of the model it displaced. That claim has drawn as many accusations of hype as endorsements. Treat the crown as unverified until the weights and an independent run land.

Xiaomi’s MiMo-V2.5-Pro sits behind these three as the earlier open-weights entrant. It arrived in late April with full weights, positioned against the previous Kimi and GLM versions. Together the four give an enterprise real options. A week earlier, the strongest pick was a hosted model a government could switch off.

## The open field against the suspended Fable

Choosing among these is a procurement exercise. A team qualifies alternates for different jobs, because no single model wins every one. The right alternate depends on what the original was doing. It also depends on how much hardware the buyer controls and how much the license lawyers need to bless. The table lines the open field up against the model it stands in for.

| Scenario | Open option to qualify | Rationale |
| --- | --- | --- |
| Code cannot leave the building | North Mini Code | Apache 2.0 and a single-H100 footprint make on-premises deployment realistic, at the cost of higher token output |
| Long multi-file refactors across many steps | Kimi K2.7-Code | Tuned for long-horizon work, though the trillion-parameter weights need heavy memory and the gains are vendor-reported |
| Lowest hosted cost with a million-token context | GLM 5.2 | Cheap subscription access and a large context window, but benchmarks and open weights were still pending at launch |
| A cheap earlier baseline already in hand | MiMo-V2.5-Pro | Open weights from late April with a known profile, useful as a fallback rather than a frontier bet |
| A hosted frontier model inside the US | Claude Opus 4.8 | Anthropic now routes new sessions to a default model or Opus 4.8, the safe pick for US teams that do not need open weights |

Most teams will not settle on a single model. A bank might run North Mini Code on-premises for sensitive code and call GLM 5.2 for cheaper bulk work. That mirrors how infrastructure teams already mix a hosted model with a local one. Qualifying more than one alternate keeps a withdrawn model from taking the workload down with it.

## Where these models actually plug in

An enterprise can swap models this fast because the agent tooling is standardized around the open field. GLM 5.2, Kimi K2.7-Code, and North Mini Code all speak the same agent protocols. A team pointing Claude Code, Cline, or OpenClaw at one of them changes a model endpoint rather than rebuilding a workflow. Anthropic’s own Claude Code is one of the clients these Chinese models target from day one.

> An enterprise can swap models this fast because the agent tooling is standardized around the open field.

My earlier coverage traced the same pattern. Claude Code, Cursor, Codex, and Antigravity [converged](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) into a single agentic blueprint, and the editor gave way to an orchestration layer. The harness became the durable surface, while the model behind it became a part that a team could replace.

*See also: [Claude Code vs. Cursor vs. Codex vs. Antigravity — six months in](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/)*

The Fable ban is the first event to test that replaceability under real pressure. Teams could swap in an open model cheaply, because the harness stayed put while the model behind it changed. Whether the replacement matched Fable 5 on the hardest tasks is a separate question, and the evidence there is not yet in.

## What the ban hands to enterprises and to Anthropic

Model access outside the US is now a supply decision. Buyers can second-source it the way they second-source hardware. A coding platform wired to one hosted model risks going dark the moment an export order lands. The teams that come out ahead qualified an open alternate before they needed it. Procurement can now ask a sharper question: whether the platform can fail over to open weights without a rebuild.

> For Anthropic, the timing could not be worse.

For Anthropic, the timing could not be worse. The order landed nine days after it called Fable 5 the most capable model it had shipped. The company disputes the finding and expects to restore access, and its hosted lead on the hardest, longest tasks is real. The opening it leaves is narrower than the headlines suggest. GLM 5.2’s benchmark crown is unproven, and the open models still trail on the longest agentic runs. What the week showed is narrower but still real. Enterprises now have open fallbacks good enough to keep work moving when a hosted frontier model disappears.

## What’s next

The next move belongs to Zhipu, and the weights decide it. If GLM 5.2’s open weights land this week and an independent run confirms even part of the BridgeBench claim, the cost case against hosted frontier models gets much harder to ignore. The franchise of downloadable agents that OpenClaw anchors would gain its strongest model yet. If the weights slip or the benchmark deflates under scrutiny, GLM 5.2 becomes one more cheap option rather than a frontier substitute. Kimi K2.7-Code and North Mini Code would then carry the open case on licenses and footprint.

> An export order meant to restrict one model showed how little leverage any single model holds over a team that kept an alternate qualified.

Either way, enterprises are in a better position than they were on June 11. An export order meant to restrict one model showed how little leverage any single model holds over a team that kept an alternate qualified. The open question is whether independent BridgeBench numbers and the GLM weights turn this week’s scramble into a settled second source, and that comparison is where I will look next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)