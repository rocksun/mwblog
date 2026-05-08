In April, Anthropic launched the public beta of [Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/), its platform for running AI agents on its infrastructure.

On Wednesday, the company announced it is [expanding Managed Agents](https://claude.com/blog/new-in-claude-managed-agents) with the ability to dream, focus on outcomes, and orchestrate multiple agents. These new features, the company says, will “make agents more capable at handling complex tasks with minimal steering.”

## What do AI agents dream about?

The marquee feature here is “dreaming,” which is now in research preview. While you may not think of sleeping as a feature that will make agents more capable, the idea here is that, just like the human brain updates its memory network while a person sleeps, Claude in Managed Agents will now run a scheduled process that allows it to process and review any recent work it did. It will review recent sessions, look for patterns, and then store those updated observations in its memory.

There are controls to run this as a completely automated process, or to have users review any changes before Claude writes them into its memory.

![](https://cdn.thenewstack.io/media/2026/05/2e99c0e6-claude-managed-agents-blog-followup-dreaming-1024x576.png)

Credit: Anthropic

The practical advantage here is that by taking a more holistic look at all recent workflows — and the mistakes the agent may have made — we can find patterns an individual agent isn’t likely to see.

> “Together, memory and dreaming form a robust memory system for self-improving agents.”  
> —Anthropic

“Together, memory and dreaming form a robust memory system for self-improving agents,” Anthropc writes. “Memory lets each agent capture what it learns as it works.”

## Outcomes

The other major new feature is [outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes). The idea here is to focus on the agent’s actual intent.

“Agents do their best work when they know what ‘good’ looks like,” Anthropic says in its announcement.

To do so, they need to know the criteria for what “good” means for a given task, so users can create those for the agent, and then a separate grader agent will evaluate this output against them (that grader has its own context window, so there’s no cheating).

> “Agents do their best work when they know what ‘good’ looks like.”  
> —Anthropic

Anthropic notes that this is especially useful for having the agent work on tasks “that require attention to detail and exhaustive coverage,” but also where there is a more subjective quality to the result (like following a brand’s voice in marketing copy).

In the company’s own testing, using outcomes improved task success by up to 10 points compared to a standard prompting loop.

![](https://cdn.thenewstack.io/media/2026/05/cd88a14c-claude-managed-agents-blog-followup-sessions-ui-1024x576.png)

Credit: *The New Stack*

## Multi-agent orchestration

One area many AI labs are currently working on is orchestrating multiple agents to work in parallel. It’s no surprise then that Anthropic, too, is bringing this to its managed agent platform. Managed Agents can now break down tasks and have a lead agent assign them to subagents.

That’s something Claude Code and Cowork often do by default, but they don’t have all that many ways to actually manage them. In Managed Agents, users now have access to an area in the Claude Console where they can see exactly what each agent did, step by step.

## Availability

Both outcomes and multi-agent orchestration are now part of the public beta of Managed Agents. Users who want access to dreaming can request it [here](https://claude.com/form/claude-managed-agents).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)