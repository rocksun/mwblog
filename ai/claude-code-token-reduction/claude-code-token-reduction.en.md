A Claude Code skill designed to help developers work with Anthropic’s API was consuming more than 200,000 tokens to load. With Claude Code v2.1.234, Anthropic says it has brought that down to roughly 25,000 tokens.

The change appeared in the [Claude Code changelog](https://code.claude.com/docs/en/changelog) on Monday. Anthropic attributed the reduction, which cuts the initial context cost by at least 85.7%, to loading the skill’s reference documentation on demand. In this case, a single bundled skill could consume more tokens than many coding sessions do from beginning to end.

## Skill loaded everything upfront

The built-in /claude-api skill which loads reference material for developers working with the Claude API and Managed Agents, can be invoked directly, but Claude Code can also activate it when a project imports Anthropic’s Python or TypeScript SDK. Interestingly, developers had already traced the problem before Anthropic documented the fix.

In a [GitHub issue opened July 7](https://github.com/anthropics/claude-code/issues/75197), a developer examining Claude Code 2.1.201 found that /claude-api embedded its shared reference files and the detected language documentation directly into the skill body. The report measured roughly 120,000 tokens of reference material in a single invocation. One migration document accounted for an estimated 36,000 tokens on its own.

> One migration document accounted for an estimated 36,000 tokens on its own.

Once the rest of the skill loaded, even a one-line question could consume roughly 200,000 tokens before Claude started answering — the hidden overhead that, [as with production AI pipelines more broadly](https://thenewstack.io/ai-pipeline-token-optimization/), only surfaces once someone actually measures it. The issue was closed as a duplicate and marked “not planned,” despite similar reports still coming in.

A second [bug report filed August 4](https://github.com/anthropics/claude-code/issues/83818), found a particularly expensive fallback. When the skill could not detect a project language during a prompt audit, it loaded documentation for C#, cURL, Go, Java, PHP, Python, Ruby and TypeScript, along with 26 shared Markdown files. The bundled directory was 812,650 bytes. Only one 32,954-byte file was needed up front for the task used in the reproduction.

A large local reference library provides an agent with useful material to draw on, but inlining it forced the agent to read all 812 KB for every request, even when most of it was irrelevant.

> A large local reference library provides an agent with useful material to draw on, but inlining it forced the agent to read all 812 KB for every request, even when most of it was irrelevant.

## Context window fills silently

Anthropic’s own [Claude Code best-practices guide](https://code.claude.com/docs/en/best-practices) warns that performance degrades as the window fills, with the model more likely to lose earlier instructions or make mistakes. It’s a pattern that extends beyond Claude Code: [the blank-check era of AI coding is ending](https://thenewstack.io/microsoft-copilot-token-budgets/) precisely because unchecked token consumption degrades both quality and cost.

Once a skill loads, its content becomes fixed overhead that developers may never see, [creating an inherited problem at enterprise scale](https://thenewstack.io/speakeasy-enterprise-agent-skills/). Claude Code’s documentation says the skill body stays in context across turns, even though the developer may see only the much smaller request and response.

Cutting the skill to roughly 25,000 tokens leaves a lot more room for the repository and the actual work. Anthropic doesn’t explain how Claude chooses which documents to load, only that the references are now pulled in on demand.

## On-demand approach trades reads for room

Anthropic’s [skill documentation](https://code.claude.com/docs/en/skills) says SKILL.md should contain the core instructions and links, while API specifications, examples, and other detailed material should live in supporting files that Claude opens only when needed.

That guidance divides loading into three stages: a small amount of metadata that is always present, the SKILL.md body when the skill triggers, and bundled resources pulled in during the task. The old /claude-api behavior blurred the last two by loading all of its reference material as soon as the skill ran.

> With on-demand loading, Claude may need an extra file read after it identifies the relevant language or API feature.

With on-demand loading, Claude may need an extra file read after it identifies the relevant language or API feature. But it pays that cost only for material tied to the task, which becomes more important as [agentic workflows make token costs the fastest-growing line item in AI budgets](https://thenewstack.io/agentic-ai-token-costs/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)