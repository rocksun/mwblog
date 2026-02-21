It has never been easier to quickly and at scale find security vulnerabilities. [Linus’s Law](https://en.wikipedia.org/wiki/Linus%27s_law), Eric Raymond’s famous dictum about open source software, states that “given enough eyeballs, all bugs are shallow.” In other words, if enough people look at a piece of code, someone will eventually spot the problems.

AI has supercharged this principle, powering new tools that accelerate and expand the ability to find vulnerabilities.

The question is, who will find them first: your security team or threat actors?

## AI red teaming: No longer theoretical or optional

XBOW’s ascent to the top of [HackerOne’s US leaderboard](https://xbow.com/blog/top-1-how-xbow-did-it) marked a milestone for application security (AppSec). In just 90 days, its autonomous AI penetration tester submitted over 1,060 vulnerabilities, surpassing the output of thousands of human researchers.

Unlike much of the [unskilled AI slop](https://www.nytimes.com/2024/06/11/style/ai-search-slop.html), these findings weren’t theoretical. Bug bounty programs helped companies resolve 130 critical vulnerabilities found by XBOW, with 300+ more triaged and awaiting resolution.

What makes XBOW’s achievement particularly significant is its economies of scale. The [system operates autonomously](https://thenewstack.io/operations-shift-assistants-to-autonomous-multiagent-systems/), requires no sleep, and addresses thousands of targets simultaneously.

While human researchers cherry-pick high-value targets, AI systems can [methodically test entire attack](https://thenewstack.io/modern-attack-methods-jeopardize-cybersecurity-strategies/) surfaces. HackerOne [reports](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy) that autonomous agents submitted more than 560 valid reports in 2025 alone.

Known vulnerabilities that once required skilled security researchers to exploit are now discoverable at machine scale and speed.

## Threat modeling at the speed of AI

JPMorgan Chase’s release of its [AI threat modeling Co-Pilot research](https://www.jpmorganchase.com/about/technology/blog/aitmc) demonstrates how enterprise application security teams are already deploying AI to address velocity constraints. Its [Auspex system](https://arxiv.org/pdf/2503.09586) captures threat modeling tradecraft in specialized prompts that guide AI through system decomposition, threat identification, and mitigation strategies, enabling developers to then address them through a self-service model.

Auspex combines generative AI with expert frameworks, industry best practices, and JPMorgan’s institutional knowledge. The system encodes this context directly into AI prompts through a technique called “tradecraft prompting.”

It processes architecture diagrams and textual descriptions, then chains prompts to generate threat matrices that specify scenarios, types, security categorizations, and potential mitigations.  
Traditional threat modeling can take weeks or months. AI-driven approaches, such as the one JPMorgan employs, collapse this timeline to minutes while improving the [quality of human analysis](https://thenewstack.io/level-up-your-software-quality-with-static-code-analysis/).

## A security human in the loop

Emerging AI use cases illustrated by XBOW and Auspex offer AppSec teams an alternative to the traditional AppSec model, which consumes enormous resources during development while providing limited coverage.

Code review backlogs grow, security debt accumulates, and critical vulnerabilities slip into production because humans remain [bottlenecks in the software development](https://thenewstack.io/ai-use-cases-that-actually-fix-engineering-bottlenecks/) lifecycle. A recent [GitLab survey](https://about.gitlab.com/developer-survey/) found teams lose 7 hours per week to inefficient processes.

AI changes this equation. Security teams can now systematically redeploy resources away from manual, repetitive activities toward building security-engineered solutions that integrate AI directly into developer workflows.

A few proven, AI-driven strategies can help a modern AppSec team scale efficiently:

* **Build queryable security intelligence:** Ingest every security bug, vulnerability report, and incident into structured data stores that support semantic search. This will transform historical security findings into embeddings that enable AI systems to identify similar patterns across codebases. When a new vulnerability class emerges, your AI can instantly query whether similar issues exist elsewhere.
* **Fine-tune models for your environment:** Rather than relying on generic commercial tools, your AppSec team should leverage RAG (Retrieval-Augmented Generation) approaches to augment LLMs with security anti-patterns and architectural standards specific to your organization. Recent [research](https://arxiv.org/html/2502.06633v1) shows that combining static analyzers such as PMD and Checkstyle with fine-tuned LLMs significantly improves code review accuracy while reducing false positives.
* **Integrate AI into your developer toolchains:** Security findings that arrive days or weeks after code is written create friction and require developers to do more context switching. Instead, embed AI-powered analysis directly into your IDEs, CI/CD pipelines, and pull-request workflows. Developers will receive real-time security guidance as they write code, not after they’ve moved on.
* **Apply AI to threat modeling at scale:** Following JPMorgan’s lead, implement AI-powered threat modeling that can analyze every new system design, API specification, and infrastructure change. The goal isn’t perfection but breadth: It’s better to have AI-generated threat models for 100% of your systems than expert-reviewed models for 10%.
* **Leverage AI to improve your Static Application Security Testing (SAST):** Traditional SAST tools generate high volumes of false positives, which can desensitize developers and create triage overhead. AI can dramatically [improve the accuracy of these tools by understanding code context](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), analyzing data flows, and identifying real vulnerabilities that pattern-matching tools miss.

## Security prioritization for AI

Security teams face a pivotal moment. The old playbook of adding more engineers at code review doesn’t work when development moves this fast. AI can match the pace, protecting software as quickly as teams create it.

But this shift won’t happen by accident. Security leaders need to proactively redirect their teams’ focus, redesign workflows, and rethink what skills matter when humans and AI collaborate. The organizations that put in the effort up front are more likely to get this right and emerge with stronger security, lower costs, and faster shipping cycles.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/af8914a1-cropped-fcbb0ca2-josh-lemos-600x600.jpeg)

Josh Lemos is the chief information security officer at GitLab Inc., where he brings 20 years of experience leading information security teams to his role. Josh has led security teams at numerous high-growth technology companies including ServiceNow, Cylance and most...

Read more from Josh Lemos](https://thenewstack.io/author/josh-lemos/)