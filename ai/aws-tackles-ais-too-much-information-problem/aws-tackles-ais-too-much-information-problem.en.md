[AWS](https://aws.amazon.com/?utm_content=inline+mention)’ [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) is enabling users to give agents specialized knowledge without drowning them in context.

The company’s new [powers system](https://kiro.dev/powers/), launched this week at the [AWS re:Invent](https://reinvent.awsevents.com/) conference, dynamically loads framework expertise and tools only when developers need them. Instead of cramming every possible tool definition into an [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)‘s context window upfront, powers activate based on what you’re actually working on, the company said.

“We were observing developers over the past year since MCP [Model Context Protocol] was announced, and one of the things we observed is that lots of MCP servers were being added into the context, and the context was getting bigger and bigger,” said [Amit Patel](https://www.linkedin.com/in/amit-patel-040453/), general manager and director of agentic AI at AWS, in an interview with The New Stack. “Not all of the tools that were in those MCP tools were necessary for the job that the developer was trying to do.”

## The Context Overload Problem

The issue stems from how [MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) servers traditionally work. Connect five MCP servers to your development environment and you might load more than 100 tool definitions before writing a single line of code. That can consume over 50,000 tokens — roughly 40% of a typical context window — before you even start your first prompt, the company said.

AWS’ own MCP server illustrates the challenge. It exposes over 150 tools covering services from Aurora to DynamoDB to S3. Load that server and every one of those tool definitions sits in your agent’s context, whether you’re working on databases, storage or something else entirely, the company said.

Powers solve this through keyword-based activation. Mention “database” or “[postgres](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/)” in your conversation, and the [Supabase](https://thenewstack.io/how-supabase-is-building-its-platform-engineering-strategy/) power loads its tools and best practices. Switch to deployment work, and the [Netlify](https://thenewstack.io/netlify-makes-preview-servers-available/) power activates while Supabase deactivates. Your baseline context usage stays near zero until you actually need specific tools, AWS said.

## What Makes a Power

Each power bundles three components: an MCP server configuration, a POWER.md steering file that acts as an onboarding manual for the agent and optional hooks that trigger on IDE events or slash commands.

The POWER.md file includes frontmatter with keywords that trigger activation, onboarding steps for initial setup and a map to workflow-specific steering files. When you’re writing Row-Level Security (RLS) policies in Supabase, the agent loads documentation specific to RLS. When you switch to Edge Functions, it loads different context, according to AWS.

“The power is basically a combination of MCP servers, steering files and agent hooks, which are the three features that we have inside Kiro,” Patel explained. “You can combine those three things together and define that as something that either you can use directly yourself, or you can share with the community.”

“As AWS rightfully mentions, using MCP servers to equip LLMs with specific context, guidelines, resources, constraints, etc., in building out complex software, software that often depends upon a wide-ranging and complex toolchain, is a bit like reading the entire encyclopedia every time you want to look something up,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group, told The New Stack.

“What AWS is doing here is something we’re seeing more frequently from agentic tooling providers. [Google](https://cloud.google.com/?utm_content=inline+mention) Gemini CLI, for example, incorporates extensions; [OpenCode](https://thenewstack.io/terminal-user-interfaces-review-of-crush-ex-opencode-al/) does the same with plugins,” Shimmin said. “It’s all about ‘activating’ the relevant information at the right time, adding it to the context windows only when appropriate … and presumably removing it afterward. I’m not sure if AWS’ idea here with Kiro Powers leaps forward to do away with all of the different techniques and tools available for developers, but I do like where they’re pointing here with POWERS.md as a standard way to package, activate and transfer knowledge.”

[David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of Arcjet, a developer security tool provider, noted the importance of context limits.

“Kiro Powers feel like [VS Code](https://thenewstack.io/5-ai-extensions-to-help-improve-your-vs-code-experience/) extensions for AI agents: You drop in domain-specific expertise exactly when you need it,” he said. “Loading and unloading on demand is really about dodging LLM context limits. Instead of clogging up the context window with every tool and instruction, you only pay the per-token cost for the ones that are relevant.”

Moreover, “It’s good to see competition with Claude Skills,” Mytton said. “This is clearly where MCP-based tooling is heading: extensions you can move between editors and agents, rather than loading every possible tool at the same time.”

## Launch Partners and Ecosystem

Kiro launched powers with partners spanning the application development life cycle: Datadog, Dynatrace, Neon, Netlify, Postman, Supabase, Strands Agents and Amazon Aurora. The company positions this as a “Swiss army knife of capabilities” available through one-click installation.

Developers can browse powers in the Kiro IDE or on kiro.dev and install them without editing [JSON](https://thenewstack.io/working-with-json-data-in-python/) configuration files or running command line setup. If a power needs API keys or environment variables, it prompts you on first use.

The system also supports community-built powers imported from GitHub URLs, as well as private team powers from local directories or private repositories. Kiro emphasizes that anyone can build and share powers using their tooling, Patel said.

While powers currently work only in the Kiro IDE, the company is building toward cross-compatibility with other AI development tools, including Kiro CLI, Cline, Cursor and Claude Code. The goal is for companies to write one POWER.md file that works across any AI coding assistant.

## Beyond Just Packaging

Kiro frames powers as more than a packaging format — they’re positioning it as a model for continual learning in AI agents. As frameworks evolve and teams build internal tools, agents need ways to expand their capabilities without starting from scratch.

“Neo didn’t learn kung fu once and stop,” AWS wrote in a [blog post](https://kiro.dev/blog/introducing-powers/), referring to the movie [“The Matrix.”](https://en.wikipedia.org/wiki/The_Matrix) “Throughout ‘The Matrix,’ he downloaded new capabilities as he needed them.”

The vision is that when Supabase ships updated RLS patterns, agents automatically get them. When your team builds an internal design system, you package it as a power and every developer’s agent knows how to use it, the company said.

Powers arrive alongside Kiro’s announcement of three “[Frontier Agents](https://thenewstack.io/aws-frontier-agents-handle-code-security-ops-without-you/)” — autonomous agents for software development, security and [DevOps](https://thenewstack.io/introduction-to-devops/) that can work without human intervention. While those agents handle large-scale, multiday tasks, powers address the opposite end of the spectrum: targeted, specific development work where precision and token efficiency matter.

“At one end of the spectrum, you have these massive, days-and-hours tasks that are learning and scaling,” Patel said during the briefing. “But at the other end, developers are working on specific tasks where they need to be targeted and precise. That’s what powers are for.”

The powers system is available in Kiro IDE. Cross-compatibility with other development tools is planned but not yet available, the company said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)