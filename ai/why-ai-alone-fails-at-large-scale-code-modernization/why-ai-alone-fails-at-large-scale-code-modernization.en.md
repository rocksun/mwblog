Modern software teams face a double bind: deliver business value faster while maintaining aging, complex codebases. For executives, delivery speed is the most clear-cut indicator of software quality. When it slows, it’s a sign that quality is eroding beneath the surface. And the result of this slowdown is predictable — rising technical debt, growing cognitive load, and slow, risky upgrade cycles.

Code modernization has always been complex. Now, with AI entering developer workflows, the question arises: Does it enhance modernization or merely accelerate it and increase its risks?

In this article, I’ll explain where AI helps, where it falls short, and why pairing it with deterministic automation is critical to moving fast without breaking everything. This is not a debate between man and machine. It’s about building systems where each part does what it’s best at — and can be trusted to do so.

## The Code Modernization Bottleneck

Most enterprises carry years, sometimes decades, of technical debt. The code may still work, but it’s hard to change. Why? Dependencies are outdated, interfaces are fragile, and code is written for obsolete versions, such as Java 6 or early Spring Boot. These foundations now limit your ability to evolve.

Over time, all software tends to become increasingly complex. Teams make tradeoffs to meet deadlines. Organizations scale, business domains evolve, and supporting tools become outdated. Some of this debt is internal, but much of it is imposed externally. OSS projects are updated frequently, vendors deprecate APIs, and you’re left running on outdated frameworks full of CVEs.

In the past, we treated software like projects — built once and shelved. But today’s systems are assembled and interdependent. To keep them functional, we have to treat them like products: continuously maintained, regularly updated, and constantly evolving.

As a result, developers now spend nearly half their time on code maintenance. This includes addressing upgrades, deprecations, bug fixes, and [security patches—often across multiple](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/) repositories and with inconsistent tooling. Worse, many of these changes are never implemented at all. They’re logged, deprioritized, or partially completed, leaving a trail of risk and inconsistency.

The challenge isn’t a lack of developer effort. It’s that the systems we’ve built are not designed for frequent, safe, and scalable change.

## What AI Can (and Can’t) Do for Modernization

AI is being integrated into almost every part of the software development lifecycle. Over 90% of [developers now use tools like GitHub Copilot](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/), Amazon Q, or other AI assistants. These tools are helpful. They help with boilerplate, autocomplete, documentation, and navigating unfamiliar libraries.

But AI alone is not enough for modernization work. Models are probabilistic. They don’t have a native understanding of your build system, dependency graph, or code formatting rules. They don’t know which changes are safe to make across hundreds of repositories or how those changes might break a downstream service.

In regulated industries or mission-critical systems, even a small error introduced by AI can have outsized consequences. That’s why human developers still need to review, test, and validate every change. The result is a slower process and limited trust. It’s simply not a process that can scale to the needs of today’s enterprise codebases.

## The Missing Ingredient: Determinism

AI is great for pairing on new features. But for large-scale code modernization, precision is more important than creativity.

That’s where [OpenRewrite](https://openrewrite.org/) comes in. OpenRewrite is an open-source refactoring framework designed to enable safe, scalable, and automated code transformation. It analyzes source code using a compiler-accurate parser. It produces a Lossless Semantic Tree (LST) — a structured representation that captures the full fidelity of the code, including syntax, semantics, types, and formatting.

At the heart of OpenRewrite are recipes: deterministic programs that encode search and transformation logic. These recipes can be tested, versioned, and applied consistently across a single application or thousands of repositories. They follow well-defined rules to transform code with accuracy and reproducibility.

When you use OpenRewrite, you’re not hoping that the code will compile after the fact. You’re using a framework that understands the code deeply and applies changes in a way that’s structurally and semantically correct.

With the latest [generation of AI coding agents](https://thenewstack.io/better-llm-agent-quality-through-code-generation-and-rag/), such as Claude Code, the cost of creating custom recipes has dropped significantly. What once took hours to write can now be drafted in minutes.

## Grounding AI in Your Codebase’s Data

AI models are not natively aware of your codebase. They don’t see your dependency graph, build system, or architectural conventions. They generate output based on probability, not structure. To modernize reliably with AI, you need more than a prompt. You need structured access to your own, compiler-accurate code data.

For example, when Moderne introduced Moddy, our multi-repo AI agent, the goal was not to replicate [coding assistants like Copilot](https://thenewstack.io/testing-copilot-and-chatgpt-as-coding-assistants-what-we-found/) or Amazon Q. Instead, we enabled Moddy to leverage the rich semantic [data unique to each customer’s codebase to summarize and reason](https://thenewstack.io/why-choose-a-nosql-database-there-are-many-great-reasons/) about entire systems.

Moddy’s job is to orchestrate modernization at scale. It starts with a prompt — something like “Upgrade all Spring services to version 3” or “Find usages of deprecated crypto.” From there, it analyzes recipe outputs across your codebase, identifies where change is needed, and directs safe changes to the source code using deterministic recipes.

Moddy is grounded in the richness of the actual codebase via OpenRewrite (whereby recipes become tools that can extract structured insights and execute accurate transformations). That grounding matters. Language models are probabilistic, and while they’re evolving quickly, that limitation isn’t going away.

As LLMs become more commoditized, the long-term value lies not in the models, but in the [data and systems](https://thenewstack.io/cloud-native-computing-now-has-its-own-file-system-cubefs/) that feed them. They’re only as useful as the context they’re given. Without that access, AI is working in the dark — disconnected from the full structure of the entire system.

## How to Use AI for Modernization the Right Way

Executives are inundated with AI product pitches and internal pressure to adopt the latest coding assistants. But if the goal is to improve [software quality and accelerate engineering productivity](https://thenewstack.io/tacos-the-key-to-remote-software-engineer-productivity/), what actually works?

It depends on the kind of modernization problem you’re solving:

* **Use generative AI** for replatforming and net-new [code generation](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/). It’s especially useful when reverse engineering legacy systems, designing new components, or rewriting code across languages. (Think COBOL to Java or Perl to Python).
* **Use deterministic refactoring automation** like OpenRewrite (and platforms built on it) for modernizing existing systems. These are best suited for tasks like removing deprecated APIs, upgrading frameworks, or remediating vulnerable libraries with the goal of making safe, repeatable change at scale.

And regardless of the use case, [keep these strategies](https://www.moderne.ai/blog/large-scale-code-changes) in mind:

* **Put developers in control of large-scale change.** Use deterministic tools and tested recipes to [build trust in automation](https://thenewstack.io/ebooks/security/trust-no-one-and-automate-almost-everything-building-a-modern-zero-trust-strategy/). When developers can see exactly what’s changing and why — across one or a thousand repositories — they gain confidence to approve and apply transformations at scale.
* **Harness your most valuable asset: structured code data.** Accurate, lossless representations of your code unlock everything else — searchability, automation, and safe modernization. Structured code data should be treated as infrastructure.
* **Combine AI with deterministic execution.** Let AI assist with navigation, pattern discovery, summarization, and orchestration, but use rules-based recipes to search with precision, gather [source code data](https://thenewstack.io/use-your-data-in-llms-with-the-vector-database-you-already-have/), and make accurate, verifiable changes.
* **Make modernization continuous.** Don’t treat it as a one-time project. Build it into your software lifecycle so your systems evolve safely over time.

If you want AI to be a friend to modernization, provide it with the right tools, data, and boundaries to create safer, cleaner, and more adaptable code at any scale.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/06faf03b-olga-kundzich-headshot-11-19-24-600x600.png)

Olga has extensive experience building enterprise software solutions. Previously, she worked as a technical product manager at Pivotal focused on application delivery and management solutions (e.g., Spinnaker), and was a lead software engineer and manager at Dell EMC, working closely...

Read more from Olga Kundzich](https://thenewstack.io/author/olga-kundzich/)