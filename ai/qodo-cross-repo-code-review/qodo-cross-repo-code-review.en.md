**Late-night debugging sessions** aren’t a rare edge case anymore. They are what happens when reviews can’t keep up with volume. Which is exactly why the review process has to understand cross-repository context, not just the differences that sit directly in front of it.

[Itamar Friedman](https://www.linkedin.com/in/itamarf/), co-founder & CEO of Qodo, tells *The New Stack* that monolithic application stacks have given way to a multi-repository backbone for modern enterprise applications. And the effects of application fragilities and corruption stemming from repository interconnects land hardest on people, not on the pipeline.

A software engineer might now lose two days “bisecting a transitive bump” that broke a downstream service, he says.

“A one-line change in one repo silently violates an architectural invariant (a condition that is always true at a specific point in a program) another team relied on, and nobody caught it because the reviewer was skimming a 500-line code listing difference with their own deadline looming,” Friedman says.

As AI floods us with more and larger pull requests, Friedman suggests the “blast radius only grows” from here.

**Because AI agents have fundamentally changed** how software is built, the governance systems that enterprises created for human-paced development were not designed for the agentic software development lifecycle. Pull requests from teams with high AI adoption are already 154% larger, taking 91% longer to review, and shipping 9% more bugs, according to the “[Google DORA 2025](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report?hl=en&region=US) State of AI-assisted Software Development” report.

## AI-generated code at enterprise scale

[Qodo](https://www.qodo.ai/) wants to enable software engineering teams to stay in control against this backdrop. The company announced three new platform capabilities on Monday: Cross-Repo Code Review, Custom Rules Miner, and Skill Review Standards. These new capabilities address a set of governance gaps that have emerged as [AI-generated code](https://thenewstack.io/ai-generated-code-crisis/) reaches enterprise scale.

[Multi-repo advocates](https://www.thoughtworks.com/en-gb/insights/blog/agile-engineering-practices/monorepo-vs-multirepo) talk about the separation of concerns made possible by disaggregating software based on different functional domains (authentication in one place, search in another, etc.), different stack disciplines (database drivers in one place, user interface controls in another), or quite simply a separation based upon different teams’ ownership status.

Useful for isolating changes and sometimes helpful for compliance reasons, a more heterogeneous code environment also comes with a cost in complexity, reduced navigability, and more onerous maintenance. With AI now creating its own new streams of code, multi-repo setups are likely to become more prevalent in the immediate future.

The mechanics in motion here mean that as software engineering teams grow, the most important and consequential bugs are rarely contained within a single repository; more often, they have tentacles in several places. A change to a shared library, an exported API, a data schema, or an infrastructure file can introduce breaking changes across dozens of downstream services, with no warning surfaced at the point of merge.

Because coding standards often reside in wikis, developer annotations and comments, and the institutional memory of senior engineers, Qodo Custom Rules Miner is designed to disrupt the status quo. Rather than requiring teams to define standards before enforcement can begin, it automatically discovers coding patterns from existing codebase behavior and pull request history, then surfaces them as structured, enforceable rules within the Qodo platform.

## Standards in people’s heads, “subjective tribal knowledge”

“These kinds of standards were previously unenforceable, all because they lived in people’s heads or across system boundaries that no single tool could see: cross-repository architectural invariants, the subjective tribal knowledge of senior engineers, and AI agent workflows running outside any organizational visibility or control,” explains Friedman

> “[One team] gamed the metric perfectly while testing nothing. That’s tribal knowledge failing twice over: the real standard (tests must assert behavior) lived in one senior engineer’s head and was never encoded, so the organization optimized the proxy instead of the thing.”

Qodo’s Skill Review Standards service is designed to formalize and simplify standardization procedures. When software teams use agent skills to encode development workflows and best practices, they also need to manage those skills, creating a governance challenge of its own. Qodo now provides centralized management for skills that contain code review instructions, coding standards, and engineering best practices. The platform discovers skills across repositories, surfaces them in a dedicated portal experience, and enables teams to control and measure their impact.

## How bad can a slip in code quality get?

Friedman shares a personal favorite example of code quality checking gone wrong in an anecdote related to code coverage, i.e., the measure of how much of a developer’s codebase is executed when automated tests are run, which many would consider a proxy or even a vanity metric.

A friend of his needed to reach 80% code coverage. One day, he checked one of the repos, and they had achieved 85% coverage; “he was so proud”, until he noticed there were no asserts (an assertion is an automated verification test that checks whether code produced the result expected) at all.

“They had gamed the metric perfectly while testing nothing,” Friedman recounts, somewhat gleefully. “That’s tribal knowledge failing twice over: the real standard (tests must assert behavior) lived in one senior engineer’s head and was never encoded, so the organization optimized the proxy instead of the thing. That’s precisely the gap the rules system in Qodo closes, by learning the real patterns from how good engineers work and making them enforceable.”

> “Speed without independent verification isn’t velocity; it’s technical debt in disguise.”

## What developers should think next

There’s a lot to change here; it’s a question of new tools, new workflows (re-engineered human-coded ones and AI-generated ones), and new workplace practices. We’re at an inflection point, seeing a shift from stateless AI tools to stateful systems with persistent organizational memory.

Friedman suggests that we can capitalize upon this. He says that as the volume of AI-generated code quickly outpaces human review, governance systems that can learn, remember, and enforce organizational standards are becoming a near-term necessity rather than a future aspiration.

“Cross-repo review and centralized agent management matter, but without memory, they’re still stateless. You can’t be good at code review without a very strong context engine underneath it, and memory is that engine,” he surmises.

The bottom line from Qodo is that developers should realize that they can’t trust the same generalist model that wrote the code to objectively grade its own work. We already know that LLMs will confidently tell us that code works when it does not.

Friedman’s bid for a t-shirt slogan here is: Speed without independent verification isn’t velocity; it’s technical debt in disguise. As the volume of AI-generated code has already outpaced human-paced review, the challenge is to embed governance into the development system itself through machine-readable standards, verification loops, and cross-system visibility, so that humans can oversee the process rather than inspect every line of code.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)