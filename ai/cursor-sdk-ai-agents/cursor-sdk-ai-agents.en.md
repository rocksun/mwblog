Cursor, the AI-powered code editor, released last Wednesday a dedicated SDK that lets developers build agents using the same runtime, harness, and models that power Cursor itself — part of what appears to be a broader push to [grow beyond its IDE roots](https://thenewstack.io/cursor-sdk-harness/).

This comes as Cursor CEO [Michael Truell](https://www.linkedin.com/in/michael-t-5b1bbb122/) welcomes what it has heralded as the “[third era](https://cursor.com/blog/third-era?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)” of software development, now driven by AI-assisted code tools.

Positioning the Cursor harness (that part of the [AI code generation](https://thenewstack.io/ai-code-generation-trust-and-verify-always/) model’s ability to execute predefined test validations and provide performance benchmarks) as the defining USP for tools in this space, the organization has said that coding agents can now form part of a developer’s “programmatic infrastructure” layer.

## What infrastructure does Cursor SDK automate?

By giving developers a way to circumvent agent stack overhead chores, the Cursor SDK harness provides additional automation services.

Those services span MCP server connections, agent skills management (which itself is automated), hooks to observe, control, and extend an agent’s “loop” (the agent’s journey through perception, reasoning, action and result observation); and subagent controls to delegate smaller tasks to named subagents with their own prompts and models, driven by main “[agent spawns](https://thenewstack.io/hidden-agentic-technical-debt/),” i.e., actions to direct specialized and often isolated agent sub-actions.

## No agentic free lunch?

All good news then. What do developers think about this development? How appealing is this new level of abstracted efficiency, and are there any tradeoffs that come with it (after all, there’s still no such thing as a free agentic lunch)… and what are the pain points to watch for?

[George Jacob](https://www.linkedin.com/in/georgepjacob/), senior engineering manager at the retail software development company Faire, said in [Cursor’s blog post](https://cursor.com/blog/typescript-sdk) announcing the changes that this move is key to running many agents in parallel from both the editor and the CLI.

“We’re excited about the [Cursor] SDK as a path to running our own programmatic agents on that same cloud runtime, without [managing VMs](https://thenewstack.io/from-pets-to-cattle-the-new-mindset-for-managing-vms/) or working around memory limits, to keep our codebase healthy without constant developer intervention,” said Jacob.

## Snaking around with Python

More granular are comments made by [Khalid Abdelaty](https://www.linkedin.com/in/khalidabdelaty/), lead of the Cursor Egypt community. In his [Cursor SDK user tutorial](https://www.datacamp.com/tutorial/cursor-sdk) posted May 1, Abdelaty addressed the question of whether the Cursor SDK works with Python, or indeed any other language.

“Not officially. The SDK is TypeScript only as of the public beta; Python users should call the [Cloud Agents REST API](https://cursor.com/docs/cloud-agent/api/endpoints) directly,” instructed Abdelaty.

Further, on the question of how robust this technology is and whether it’s suitable for live production, the answer is yes, with caveats.

“Use it first for low-risk tasks. The SDK surface is still in public beta,” he said.

Expanding on his already published clarifications, Abdelaty tells *The New Stack* that for him, the interesting part of the Cursor SDK is not just that it lets developers use AI agents from code – it is that it brings those agents closer to where developers already work, like CI, internal tools, GitHub issues, code review, and small maintenance scripts.

“That is useful, but it also means teams need to be careful,” Abdelaty says. “The hard part is not only writing a good prompt. It is deciding what the agent can change, where a human should review it, how secrets are handled, and what tests need to pass before the change is trusted.”

Underlining his thoughts thus far, Abdelaty says he would not use this as a reason to allow agents to freely change production code. He would start with safer tasks, like fixing tests on a branch, checking old docs, summarizing changes, or preparing a pull request for review. His bottom line is that the direction is clear: Coding agents are starting to move from chat windows into the normal developer workflow.

## Expect API changes

Abdelaty also noted that scope secrets (sensitive credential data related to defined environments, projects, or users) require review and that developers should “expect API changes” before general availability.

> “Teams considering the SDK for production automations should treat it as a promising but still-moving platform… tool call schemas are not stable and should be parsed defensively.”   
> —Curtis Pyke, Kingy AI.

Widely accredited deep learning and AI specialist [Curtis Pyke](https://www.linkedin.com/in/curtis-pyke-4b52a420/) is also the founder of [Kingy AI](https://kingy.ai/). Initially upbeat, Pyke has said that the Cursor SDK is an attempt to “productize the hard parts” of running coding agents, i.e., repository context, workspace management, cloud execution, streaming events, model selection, MCP integration, subagents, hooks, artifacts, and lifecycle management.

## Known limitations

But he cautioned in an [April 30 analysis](https://kingy.ai/ai/cursor-sdk-review-cursors-coding-agent-becomes-programmable-infrastructure/), “Teams considering the SDK for production automations should treat it as a promising but still-moving platform. Cursor’s own docs include several known limitations, [including:] team admin API keys are not yet supported for SDK authentication; and tool call schemas are not stable and should be parsed defensively. Those are not dealbreakers, but they define the maturity level.”

More forward-looking is kage18, [writing on Hacker News](https://news.ycombinator.com/item?id=47750940), who says that this progression “makes sense architecturally” and that the Claude Code SDK is “well-designed for agentic use” with its sub-agents, hooks, and session management, all of which work cleanly.

> “The interesting question is what Cursor adds on top — its UX and context management decisions are where differentiation actually lives.”   
> —kage18.

## Differentiation lives in the UX

“If you’re building an IDE on top of it, you’d want that foundation rather than rolling your own,” stated kage18. “The interesting question is what Cursor adds on top – its [User eXperience] UX and context management decisions are where differentiation actually lives.”

Who will win the AI coding platform race is a tough call to make. But as *The New Stack’s* [Matt Burns](https://thenewstack.io/author/matthew-burns/) pointed out in his initial story, this development at Cursor is all about how developers weigh up its toolkit when comparing it to competing technologies from Anthropic, OpenAI with Codex, and its Microsoft-aligned work with GitHub Copilot… and the other frontier model mavericks.

The fact that these vendors are competing for headspace inside developer workflows first and foremost – rather than resulting app functionality for end users – shouldn’t necessarily be an issue. After that, that’s the natural direction of the food chain from software engineer to consumer. It may all come down to who scales best and which vendor handles token-based consumption pricing most sympathetically.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)