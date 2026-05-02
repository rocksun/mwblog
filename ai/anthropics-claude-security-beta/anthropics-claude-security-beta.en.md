On Thursday, Anthropic took [Claude Security](https://claude.com/claude-code-security), a defensive security tool in Claude Code on the web that scans codebases for vulnerabilities and suggests fixes, out of closed preview.

It is now available in beta for Claude Enterprise customers, with support for users on the Team and Max plans coming soon (this is new, as the private preview was limited to Enterprise and Team users).

> Claude Security is now available in beta for Claude Enterprise customers.

Anthropic [launched](https://www.anthropic.com/news/claude-code-security) the private preview of Claude Code Security in February. That was before the announcement of [Claude Mythos and Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), but in many ways, we’re talking about a similar tool and mission here.

Since its launch, the company says, “hundreds of organizations” have used Claude Security to fix issues in their production code “that existing tools had missed for years.”

## Mythos Lite

Fixing issues in production code that other tools overlooked has been the pitch for Mythos — and one of the reasons Anthropic hasn’t released it publicly yet. It’s what organizations that have access to Mythos have [said about it](https://thenewstack.io/claude-mythos-preview-simulation/) in [recent weeks](https://www.wired.com/story/mozilla-used-anthropics-mythos-to-find-271-bugs-in-firefox/).

The risk with Claude Security may be reduced because Opus 4.7, which currently forms its backbone, [isn’t quite as smart as Mythos](https://thenewstack.io/claude-opus-47-launch/), but if you can easily scan your own codebase for security vulnerabilities, you could also scan any open-source library for potential zero-day attacks, too (even if Claude Security won’t write the exploit for you).

> Claude Security focuses on scanning an entire codebase using multiple agents that run in parallel

Claude Security focuses on scanning an entire codebase using multiple agents that run in parallel. While some other tools may look for known issues, Claude Security steps through the source code and examines data flows to build a more complete picture of the attack surface.

If the tool detects an issue, it runs an additional validation pipeline to verify that the issue was correctly identified before notifying an analyst. As Anthropic notes, to do this, Claude will challenge its own findings to ensure fewer false positives.

The promise of a tool like this, combined with Claude Code or other coding agents, is, of course, that the gap between finding the issue and fixing it is now a small one.

“Users can open a Claude Code session to work through the patch in context, instead of days of back-and-forth between security and engineering,” Anthropic states in its announcement. By default, every finding includes a recommended patch that security can review and approve.

Among the new features the team added during the preview were the ability to schedule regular scans, the ability to dismiss any findings with comments, and CSV and Markdown exports to bring a scan’s results into existing tools.

## What about Code Review?

It’s worth noting that Anthropic also offers another tool that scans a project’s entire codebase and looks for problems in that code on GitHub: Claude Code Review. Code Review is a [multi-agent code review tool for Claude Code](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) that uses agents to scan a codebase for all kinds of bugs, including security bugs, but its focus is broader.

When Code Review launched, *The New Stack* [asked](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) Cat Wu, the head of product for Claude Code at Anthropic, about the relationship between Code Security and Code Review. At the time, Wu said that while Code Review will flag security issues, “it’s not as thorough as Claude Code Security.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)