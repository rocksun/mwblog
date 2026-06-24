**Anthropic this week announced a major overhaul of Claude Design**, the design tool it launched in April as a research preview. The update is intended to simplify the handoff between design and engineering teams through a new bidirectional Design-Code integration and make it easier for users to create designs that adhere to brand guidelines.

Plus, Anthropic says it listened to user feedback and [made changes](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work) to address token inefficiencies that irked early users, and it also added a new editor and more connectors for easy sharing with tools like Adobe, Base44, Canva, Gamma, Lovable, Miro, Replit, Vercel, and Wix.

But [Alfie Martin](https://www.linkedin.com/in/alfieisbored/), lead AI product designer at [ABM Industries](https://www.abm.com/), tells *The New Stack* she doesn’t think Claude Design has meaningfully reduced the back-and-forth between departments.

Though she acknowledges the tool could make prototyping easier, she warns that token efficiency may still be a problem — and that asking Claude to make every design update itself isn’t, by default, the most efficient way to get work done.

“Token usage is expensive, and Claude Design uses a lot,” Martin says. “Many times, it takes longer than designing a component or changing that detail yourself.”

## Claude Design and Claude Code get closer

The AI company says the new iteration of Claude Design now works more closely with Claude Code, enabling users to jump back and forth between design and coding while keeping work synced.

Going one way, developers can run the `/design-sync` command in Claude Code to pull design systems directly from local codebases into Claude Design so designers can work off of existing components. When it’s time to ship, designers can easily pass it on to Claude Code, maintaining a continuous line of work.

Going the other way, developers can run the `/design` command to create, edit, and sync design projects directly in Claude Code, without leaving the terminal.

When asked how the Claude Design upgrade could impact workflows, [Roman Martynenko](https://www.linkedin.com/in/roman-martynenko-15b91a141/), a full-stack software engineer at [Henry AI](https://www.henry.ai/), tells *The New Stack* he’s a bit more optimistic about the Design-Code integration, saying he’d likely opt for terminal-based work but values the web interface for designers, project managers, and reviews:

“My ideal workflow is: design exploration in the web UI, then engineering-grade handoff in Claude Code with the actual repo context.”

## Staying on brand is easier now

A main draw in the Claude Design update is that it “now sticks to your design system across projects,” per Anthropic. In other words, it makes brand consistency the default.

Users can import one or several design systems from a GitHub repo, design files, or raw uploads. This way, for every new project Claude Design creates, it automatically inherits brand assets (e.g., typography, color, spacing) and validates its outputs against those guidelines before revealing the final results.

For companies with strict branding rules, the new feature could make a real difference in maintaining consistency, something the April iteration struggled with, Nate Parrott, a designer at Anthropic, told [*Fast Company*](https://www.fastcompany.com/91561193/anthropics-updated-claude-design-gives-vibe-coders-and-their-design-overlords-more-control).

It’s likely a welcome control for design leads who want to rein in off-brand work. As Claude Design Admin, a user can set a standard design system and bar others from making edits.

The update also brings a new editor that allows for more fine-tuning with layout controls that let users “drag, resize, and align elements.”

## No more separate usage limits

In April, [*The New Stack* took Claude Design for a spin](https://thenewstack.io/anthropic-claude-design-launch/) and quickly ran into token trouble. Just building a design system and a news website prototype (plus some tweaks and an explainer video) was enough to burn through over 50% of our weekly allotment.

Anthropic says it heard similar stories and listened.

The tool update ditches separate usage limits and brings Claude Design into a shared pool with Claude Code, chat, and Cowork. Should you exhaust your usage limits, Claude Design will be unavailable — until either your usage resets or you shell out for usage credits.

The shared pool may make it easier to manage token usage, but the jury’s still out on whether it makes a difference in burn rates.

## Anthropic may be trying to put Claude Design everywhere, but it won’t change everything

By adding new connectors and deepening Design-Code integration, it seems Anthropic is intent on making Claude a bigger part of how people work. But while the June update is a decidedly more useful version of Claude Design, it won’t do everything.

Theoretically, connecting Claude Design to more tools designers and developers already use should reduce friction between teams, particularly when final implementations don’t match initial designs. As Martin points out, though, the designer-dev back-and-forth is still very much there, and token costs mean Claude-made isn’t always more efficient than human-made.

At the end of the day, speedier, on-brand designs and faster handoffs may encourage more experimentation, but “let[ting] Claude build the whole thing from start to finish,” as Anthropic suggests, isn’t the future, per Martin. Instead, she expects a hybrid model to emerge, where tools like Claude help with early concept validation, but humans still ultimately lead the charge.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)