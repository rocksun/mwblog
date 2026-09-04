**When teams price an AI coding agent,** they tend to scrutinize the model. But three recent benchmarking efforts suggest the harness — the software that steers it through tasks — may matter just as much.

The reason will be familiar to any web developer: Each inference request needs context. The relevant history must either be supplied again or reconstructed by the serving system. As a result, the provider processes large, overlapping blocks of text on every turn, including the harness’s system prompt and tool descriptions.

In June, an independent [benchmark](https://www.eishanlawrence.com/blog/harness-efficiency-bench) compared 12 configurations across two models on the same 12 Python tasks. In August, Composio [compared](https://composio.dev/content/best-agent-harness-deepseek-v4-flash) eight harnesses using DeepSeek V4 Flash on 30 enterprise workflows. Artificial Analysis, meanwhile, continuously tracks harness-model pairings in its [coding-agent index](https://artificialanalysis.ai/agents/coding-agents).

## What the three benchmarks measured

[Composio](https://composio.dev/) reported thirty workflows spanning Airtable, Gmail, Google Calendar, Google Sheets, GitHub, Slack, and PostHog. Each task ran under a 900-second ceiling. A programmatic verifier, rather than an LLM judge, graded the outcome, using isolated fixtures seeded with decoys and near-identical keys.

Composio reported 240 runs, of which 129 workflows completed successfully. Cost per successful task ranged from $0.028 for Pi Agent up to $0.195 for Claude Code. DeepAgents matched Claude Code’s pass rate exactly while costing a quarter as much per success.

The control was not perfect, and Composio disclosed that transparently. Pi ran a different reasoning setting across two model providers, and Prime Agent produced only 24 gradable runs out of 30. Those caveats rule out calling this a clean single-variable experiment.

The June benchmark measured tokens rather than dollars, and it stretched further. Its author reported runs of Aider, Claude Code, Codex, Goose, Hermes, Kilo, Kimi Code, Nanobot, OpenClaw, Opencode and Qwen Code, counting Aider’s architect mode separately. All twelve configurations ran through [OpenRouter](https://openrouter.ai/about) on the same tasks, so each harness used the same API and model. The suite ran on DeepSeek V4 Flash and then Nvidia’s Nemotron 3 Ultra. The second model offers a free tier on OpenRouter so that you can rerun it at no cost.

The post reported tokens per solved task ranging from roughly 3,500 for Aider in architect mode to 292,000 for OpenClaw. What makes that range usable is its stability, since the ordering barely moved between two unrelated models. That points to the harness software rather than model behavior.

Artificial Analysis approaches the same question with more statistical weight. Artificial Analysis reported an index combining DeepSWE, Terminal-Bench v2.1 from the Laude Institute, and Scale AI’s SWE-Atlas-QnA. That comes to 326 tasks, with pass rates averaged across three attempts each. It reports cost per task, token use, and wall time for each pairing. It also publishes a controlled comparison that holds Claude Opus 4.7 fixed while swapping between Claude Code, Cursor CLI, and Opencode.

## The startup tax

At its core, the spread stems from a single measurement: the June benchmark, the startup tax. Before a prompt does any work, the harness ships its own baggage. That baggage is the system prompt, the tool descriptions, and the environment setup. The benchmark reported around 700 tokens for Aider in architect mode, against around 26,000 for OpenClaw.

A 40x overhead would be tolerable if it were paid once, but the resend pattern makes it otherwise. The author noted that a harness carrying a 26,000-token floor through fifteen turns spends roughly 390,000 input tokens on scaffolding alone.

The math behind that holds up under testing. The startup tax multiplied by the turn count predicts tokens per solved task, with an R-squared of 0.99 across both models. Developers looking to cut agent spend should look first at the prompt floor and the turn count before touching anything more sophisticated.

One caveat belongs on that regression figure. The June benchmark ran a single pass per harness, task, and model combination, so it carries no variance estimates, and agent runs are stochastic. Artificial Analysis carries more weight there, since it averages three attempts per task across 326 tasks. Consider the June overhead finding as evidence for the mechanism, and the larger index as the better instrument for comparing current production-scale pairings.

> The expensive harnesses are not hoarding context; they are simply carrying a heavier floor.

What is surprising is what does not explain the spread. Every harness grew its context at a similar rate of a few hundred tokens per turn, so growth is not what separates them. The expensive harnesses are not hoarding context; they are simply carrying a heavier floor.

## Cached tokens reorder the leaderboard

The two harness experiments converged on a second mechanism, and Artificial Analysis treats it as substantive in its methodology. It is the one platform teams are most likely to get wrong.

Composio disclosed that Claude Code drew only 1.5% of its input tokens from cache, against roughly 70% for Codex and 57% for OMP. Fresh input costs about five times as much as cached input. Claude Code’s token consumption, therefore, was comparable to its rivals’, while its invoice was not.

The June benchmark found a similar asymmetry in its own setup. On the DeepSeek run, Codex billed over a million tokens for the suite. Cache reads made up 77% of that, charged at roughly a tenth of the normal rate. Priced the way an invoice actually arrives, Codex came out cheaper per solved task than Claude Code, a harness that used half as many raw tokens.

The author attributed Claude Code’s near-zero cache share to the serving path rather than to its prompts. In that setup, Claude Code was the only harness communicating with OpenRouter via the Anthropic-style messages endpoint. The gateway’s translation of that dialect appeared to reduce the cache hits that identical traffic would have earned through the OpenAI-style endpoint. Gateway behavior changes, so treat that as one observed path.

Artificial Analysis builds that assumption into its cost model rather than discovering it. It warns that prompt cache hit rates vary widely with provider routing. Its cost model prices cached input and cache writes separately, rather than billing every prompt token at the uncached rate. A benchmark that has to price cache writes separately is telling developers how much the serving path matters.

## Where the heavy harnesses earn their cost

Explaining the cost gap is not the same as crowning the cheapest harness. The agentic loop of look, act, check, and repeat is a cost multiplier. It helps most with unfamiliar code, failing tests, and changes across several files. On a small, well-described edit, the loop mostly re-confirms what a single call could have assumed.

But the hard-task test did not go the way the scaffolding argument predicts. Four harnesses spanning the cost range ran ten SWE-bench Lite tasks with generous limits, and all four resolved exactly one task, the same one. The author reported that Aider arrived at 0.8 million tokens, while Codex spent 15 million tokens. Ten tasks on one model is a thin basis for generalization, so consider it suggestive.

Quality is where the harness-sets-the-price framing needs qualifying, because the benchmarks argue against it. Composio reported pass rates across the eight harnesses, ranging from 46.7% for OpenCode to 66.7% for Pi Agent, a 20-point spread on one model. Artificial Analysis publishes the same kind of gap on a larger task set. Harness choice moves cost by multiples and moves task success by percentage points, which are different magnitudes rather than different directions.

## What should platform teams measure?

Enterprises are already finding that owning the harness does not settle the cost question. Teams that [built](https://thenewstack.io/enterprise-ai-agent-harness/) their own coding agents still pay for the underlying inference. Cost control has moved into the platform layer rather than the model contract.

| Question | What to measure | Why the obvious metric misleads |
| --- | --- | --- |
| Which harness is cheaper? | Cost per verified outcome | Token counts ignore pass rate and cache tier |
| Are we paying list price? | Cached share on live traffic | The discount depends on the gateway and endpoint, not the harness alone |
| Will it survive a large prompt? | Bytes transmitted versus bytes sent | Silent truncation reads as success in the output |

### Cost per successful task, not cost per task

A pass rate and a token count, read independently, will incorrectly rank harnesses. Claude Code and DeepAgents finished the same number of Composio workflows, yet a successful Claude Code run cost more than four times as much. Procurement teams should ask for cost per verified outcome and refuse per-token comparisons.

### Cached share on the actual serving path

Cache discounts are not a property of the harness alone. They depend on the endpoint dialect, the gateway, and the provider.

> Cache discounts are not a property of the harness alone. They depend on the endpoint dialect, the gateway, and the provider.

Platform teams can verify the cached fraction on their own traffic in an afternoon, and that exercise is worth more than a model migration.

### Prompt fidelity under load

The June benchmark injected 100,000 tokens of irrelevant log noise before each task and reported five distinct behaviors. Seven of the twelve configurations transmitted the prompt faithfully. Kilo and Opencode dropped 83%-89% of it while still reporting success.

> Silent truncation is the dangerous one, because it looks exactly like success in the harness output.

OpenClaw refused to run, Kimi Code crashed, and Claude Code sent everything and then performed poorly. Silent truncation is the dangerous one, because it looks exactly like success in the harness output.

## What comes next

Anthropic, OpenAI, Google, and Microsoft have already [split](https://thenewstack.io/ai-agent-harness-pricing-split/) on how to charge for the harness layer. DeepSeek then made every component of its own runtime swappable under an MIT license. Developers can now compare harness-model pairings in a publicly available, continuously updated index. That is the condition under which model pricing became contested in the first place.

For enterprises standardizing an agent platform this quarter, the harness deserves the same scrutiny as the model. In these experiments, harness choice produced cost spreads large enough to rival big differences in model pricing on workloads where the model held roughly steady. Developers, platform teams, and finance owners now have something reproducible to argue from. That is more than the harness conversation offered three months ago.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)