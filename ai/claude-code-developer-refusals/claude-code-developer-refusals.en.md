**Anthropic has confirmed that it added new restrictions to Claude Code** to prevent users from recreating existing video games. But developers say Claude Opus 5.5 is also refusing reverse-engineering and software-analysis tasks it previously handled, raising questions about what else Anthropic may have changed.

For some developers, the refusals are already affecting their work. One developer [says paid client projects have stalled](https://github.com/anthropics/claude-code/issues/106167) because Claude Code won’t work on existing games, [while others say the model is refusing](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks) to analyze software. At least one developer got back to work by switching to an older Claude model.

On Friday, [Addy Osmani](https://www.linkedin.com/in/addyosmani/), a member of Anthropic’s technical team, confirmed [on X](https://x.com/addyosmani/status/2116213240363729013) that the company had deliberately modified Claude Code’s instructions.

> “We added two sentences to Claude Code’s prompt on Opus 5.5 to steer it away from recreating someone else’s specific game because using Claude to infringe IP is against our usage policy.”

“We added two sentences to Claude Code’s prompt on Opus 5.5 to steer it away from recreating someone else’s specific game because using Claude to infringe IP is against our usage policy,” Osmani writes.

He clarifies that developers should still be able to create original games, build within established genres and work with their own designs and assets.

“We’ll continue to iterate to ensure we’re striking the right balance,” he adds, inviting developers to contact him if Claude refuses work involving their own creations.

Anthropic has not publicly confirmed whether the reverse engineering refusals are tied to the new instructions or to separate cybersecurity restrictions.

## Reverse engineering hits a wall

The complaints extend beyond game development. Developers say Opus 5.5 is refusing software-analysis tasks that previously worked. Technical writer for Phison Electronics USA, [Jarred Walton](https://www.linkedin.com/in/jarred-walton-6290a72/) encountered [refusals while testing software](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks) he was developing, but switching to Opus 4.8 allowed him to continue.

While Anthropic is trying to prevent misuse without blocking legitimate development work, developers are left unable to do tasks as Claude Code suddenly refuses what it once handled, with little explanation for the change.

> developers are left unable to do tasks as Claude Code suddenly refuses what it once handled, with little explanation for the change.

## Paid client work stalls out

On October 30, [Ray Weiss](https://www.linkedin.com/in/ray-weiss-992777125/), founder and CEO of Conflict Simulations LLC, [reported on GitHub](https://github.com/anthropics/claude-code/issues/106167) that Claude Code had stopped working on paid client projects it had supported for months.

His company creates custom digital versions of board wargames for clients who own the physical games. Weiss says the projects use original code and client-supplied materials, but Claude Code now refuses to continue the work because of its restrictions on recreating existing games.

Weiss wants Anthropic to distinguish between infringement and commissioned development, offer a verification process, and document major changes to Claude Code’s instructions.

## The hosted agent risk

The complaint highlights a larger problem with hosted coding agents. Anthropic can change what Claude Code will or won’t do without developers changing their code, tools, or prompts. Work that was possible one day may suddenly be blocked the next.

> Work that was possible one day may suddenly be blocked the next.

On October 6, Anthropic [expanded its Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program), giving vetted security researchers access to fewer restrictions after acknowledging that its safeguards can block legitimate cybersecurity work.

It’s still unclear whether those safeguards are behind the latest refusals, especially since developers say they can complete some of the same tasks using older Claude models.

## Developers are left guessing

Reverse engineering has legitimate uses well beyond security research. In October, Red Hat engineering director [Christian Schaller](https://www.linkedin.com/in/cschalle/) used Claude Code to help reverse [engineer a scanner driver](https://thenewstack.io/claude-code-linux-driver/), bringing Linux support to hardware whose manufacturer had changed its chipset.

Anthropic has acknowledged that its game-cloning restrictions need refinement, but developers still don’t know why Claude Code is refusing some reverse-engineering tasks that previously worked, or which workflows could be affected next.

*The New Stack* reached out to Anthropic regarding whether the refusals are tied to its new game-cloning restrictions or other safeguards. The company did not respond before publication.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=claude-code-developer-refusals)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)