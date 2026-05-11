Anthropic spent its biggest developer day of the year showing what a managed coding harness looks like at full scale.

At the inaugural Code with Claude conference on Wednesday, the company doubled Claude Code’s five-hour rate limits for Pro, Max, Team, and seat-based Enterprise plans, removed peak-hour reductions, raised Opus API limits, and [signed a SpaceX deal for the full capacity of the Colossus 1 data center](https://thenewstack.io/anthropic-spacex-claude-limits/), more than 300 megawatts, and 220,000 Nvidia GPUs coming online within the month.

Updates to Managed Agents added multi-agent orchestration and Outcomes to public beta; dreaming for self-improving memory landed in research preview; and Boris Cherny demonstrated remote agents and [routines](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/) that turn Claude Code into an asynchronous workflow engine.

That announcement is one half of a story. The other half is an open-source coding agent that Anthropic has spent the last three months trying to disconnect from Claude, which has become the most-starred coding harness on GitHub, with 157,000 stars on the [SST OpenCode repository](https://github.com/sst/opencode) compared to roughly 122,000 on `anthropics/claude-code` as of this week.

The two halves are not happening at the same moment. They are happening on the same trajectory, and that trajectory is the thing worth naming.

## The January OAuth lockout ripple

The origin story belongs to January, not May. On January 9, 2026, Anthropic deployed server-side checks that blocked third-party tools from authenticating to Claude Pro and Max subscriptions via OAuth.

The tools affected included OpenCode, Cline, and RooCode. Each had been sending HTTP headers that convinced Anthropic’s servers the request came from the official Claude Code binary, which let users run autonomous agent workflows on a flat $200 monthly Max subscription instead of paying API rates that could run substantially higher for equivalent token consumption.

Anthropic’s case for the block is defensible. Subscriptions exist to subsidize first-party use, and a third-party harness routing the same workloads through subscription OAuth tokens turns that subsidy into a cost center with no upside for the company funding it.

The Hacker News discussion thread on the OpenCode submission contains many comments from developers acknowledging that point, including from people who later starred the repository. Anthropic itself clarified the policy in March, telling developers that subscription OAuth tokens were never meant to be used for routing requests through third-party products.

> What developers reacted to was the execution. There was no advance notice.

What developers reacted to was the execution. There was no advance notice. Some accounts were banned for triggering abuse filters during the cutover. The block landed at 02:20 UTC, mid-workflow for users in some time zones.

The OpenCode team shipped ChatGPT Plus support within hours and started broadening provider coverage. By February 19, Anthropic formalized the rule in its updated Terms of Service. By March 19, OpenCode had received legal demands and merged PR #18186, with the commit message “anthropic legal requests,” removing all references to Claude Pro and Max authentication from the codebase.

The April 4 enforcement deadline extended the restriction to all third-party harnesses, including OpenClaw and NanoClaw, and moved users to pay-as-you-go billing.

Then came the March 21 spike. The SST OpenCode submission topped Hacker News with 1,274 points and 619 comments. Star count growth followed.

By April 4, when Anthropic’s third-party harness restrictions went into full enforcement, OpenCode had crossed 120,000 GitHub stars. As of May 8, the project’s [activity page](https://github.com/anomalyco) reports 156,904 stars, 18,259 forks, 4,788 issues, and 1,656 open pull requests, with the project’s own site claiming more than 850 contributors and 6.5 million monthly developers.

I’d argue the OAuth dispute catalyzed the spike rather than caused the entire run, and the distinction matters. Star counts measure awareness and intent, not active usage, retention, or production reliability. Some share of the post-January growth almost certainly came from developers who never used OpenCode and starred it as a hedge or a protest.

But the timing pattern is real enough that OpenCode itself acknowledges it. The project repositioned from a Claude Pro accelerator into a model-agnostic harness in the weeks following the block, and the messaging on its home page now leads with provider neutrality rather than subscription economics.

## Two coding tracks, deepening at the same time

This week’s Anthropic announcements made the managed track substantially more attractive for developers who have already chosen it. More compute, higher limits, deeper orchestration, and the SpaceX capacity deal are all moves that reinforce a single thesis.

If you want a vertically integrated coding agent backed by frontier-model capacity and managed runtime, Claude Code is now harder to leave. Routines, multi-agent sessions, dreaming, and the [Code Review](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) feature shipped earlier this quarter all assume the developer wants more of the workflow handed to a single vendor, not less.

## Managed power vs. provider neutrality

The sovereign track was already accelerating before this week. OpenCode, Cline, [Aider](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/), and OpenClaw are different projects that optimize for the same property: model neutrality. OpenCode’s README states the design goal directly: that the project is “not coupled to any provider” because “as models evolve, the gaps between them will close and pricing will drop, so being provider-agnostic is important.”

That framing is more strategic than it first appears. Provider-agnosticism does not pitch itself as a capability differentiator. A developer who wants Anthropic’s accuracy points OpenCode at Claude anyway. What it changes is the switching cost.

When OpenAI ships a better coding model, an OpenCode user changes one configuration line. When Anthropic doubles rate limits, that same user benefits without lifting a finger. When Anthropic throttles, blocks OAuth, or shifts pricing, an OpenCode user is mildly inconvenienced. A Claude Code user files a support ticket and waits.

The clearest analogy is Docker and Podman. Docker deepened its platform with Desktop, Hub, and managed services, building a vertically integrated experience for teams that wanted the full bundle. Podman gave control back to users who wanted a daemonless, rootless, drop-in alternative without the platform tax.

Both won in different markets. Neither displaced the other. The relevant question for any individual team became which set of tradeoffs matched their environment, not which tool was better in the abstract. That is the shape AI coding tools are taking now.

## Evaluating the open source trade-offs

A piece arguing that an open-source harness is strategically important should not pretend it ships polished. The same Hacker News thread that pushed OpenCode to the front page also surfaced sharp criticism. Commenters flagged that the TUI uses 1 GB of RAM or more, that the TypeScript codebase is larger and more complex than its function justifies, and that release practices and bug surface have been uneven during the project’s growth.

Security posture is harder to evaluate than for a closed first-party tool because every additional provider integration expands the attack surface, and the OpenCode plugin removal in PR #18186 itself drew 437 thumbs-down reactions from developers unhappy with how the team navigated the legal pressure.

The point is not that OpenCode is bad. The point is that the developer choosing OpenCode over Claude Code is accepting a different tradeoff curve. Claude Code optimizes for vertical coherence backed by Anthropic’s engineering and capacity.

OpenCode optimizes for portability and exit. Neither curve is uniformly better. The choice depends on whether your workflow can tolerate a single vendor owning the harness, model, memory, and runtime.

## A dual-track developer future

The honest read on this week’s news is that Anthropic is going long on the managed-harness bet, and that bet is defensible. Routines, multi-agent sessions, dreaming, and Code Review are moves that only make sense if you assume developers will increasingly hand the orchestration layer to a single vendor.

The SpaceX deal, layered on top of agreements with Amazon, Google, and Microsoft, says Anthropic believes it can keep up with the demand that the bet generates.

What the OpenCode trajectory shows is that a meaningful share of developers will refuse to hand over that layer, regardless of how good the managed version becomes. Not because the managed product is worse, but because the cost of dependence on a single vendor is too high once your workflow is at stake.

That bet is also defensible, and the star count, even with all the caveats about what stars actually measure, suggests the population making it is large enough to matter.

> The decision facing most developers in the next twelve months is not Claude Code versus OpenCode. It is whether their environment can tolerate a single-vendor harness at all.

The decision facing most developers in the next twelve months is not Claude Code versus OpenCode. It is whether their environment can tolerate a single-vendor harness at all.

For some teams, the answer is yes, and the productivity gains from a deeply integrated platform will justify the lock-in. For others, the answer is no, and the portability of an open-source harness will be worth the rougher edges.

> The most-starred AI coding tool on GitHub right now does not need Anthropic. That fact alone does not prove the open-source track is winning.

The most-starred AI coding tool on GitHub right now does not need Anthropic. That fact alone does not prove the open-source track is winning.

What it proves is that the track exists, it is growing, and the population funding its rise is the same population Anthropic has spent the last six months trying to keep inside its walls. The managed and sovereign bets can both be correct at the same time, and the tools sitting on either side of that split are not converging.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)