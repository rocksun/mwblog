Two years ago, I started experimenting with AI-assisted development tools. Today, they’re embedded into daily workflows across our engineering organization. Getting there wasn’t about adopting the latest model. It was about separating what meaningfully improves engineering outcomes from what adds noise.

After integrating AI into production development at a large cloud infrastructure company, I’ve learned that success depends far more on where you apply these tools than on the tools themselves.

## **The Friction That Actually Matters**

The problem was never [typing code faster](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/). Senior engineers don’t struggle with syntax. The real friction comes from context switching, unfamiliar stacks and legacy systems with years of implicit decisions baked in.

Learning a new framework carries cognitive overhead. Understanding a large codebase you didn’t write takes time. Working across multiple languages and ecosystems slows momentum even for experienced engineers.

Those are precisely the areas where AI assistance delivers real value. By [lowering the cost of ramping up in unfamiliar territory](https://thenewstack.io/ai-is-evolving-rapidly-heres-how-developers-can-keep-pace/), it changes how quickly you can be productive across a diverse stack.

## **Where AI Delivers Consistent Value**

* **Accelerating adoption of unfamiliar technologies.** When implementing systems outside my immediate expertise, AI has proven useful for understanding core concepts, reviewing common patterns and generating initial scaffolding. The output isn’t production-ready, but it provides enough grounding to navigate official documentation efficiently. Time to a working prototype drops from days to hours.
* **Test scaffolding across frameworks.** Every project uses different testing tools. Instead of rebuilding setup patterns from scratch, I describe requirements and review generated scaffolding. This shifts effort away from framework mechanics toward meaningful test logic. The generated code is a starting point, not a final artifact.
* **Comprehending legacy code.** AI is effective at explaining control flow, surfacing hidden assumptions and suggesting refactors that preserve behavior. It accelerates building a mental model of code you didn’t write, while all changes still require careful human review.
* **Service scaffolding.** New services often require repetitive boilerplate: routing, logging, configuration, error handling. AI can generate initial structure from a specification. The real work is then adapting it to organizational standards, but the initial setup time is significantly compressed.

## **Why Deep Repository Integration Changes the Equation**

Early AI tools operated without context. Each prompt required restating architecture, conventions and dependencies.

Tools that understand your repository change that dynamic. They account for existing patterns, file structure and dependencies when suggesting changes. That context allows them to propose modifications that actually fit your system rather than generic examples.

When debugging, these tools can reason over build errors, configuration and code together. That contextual awareness is what turns AI from a novelty into a workflow accelerator.

## **Where the Productivity Gains Actually Come From**

The gains aren’t from AI “writing code.”

They come from:

* Reduced context-switching cost when moving between stacks
* Faster resolution of blockers through structured problem articulation
* Lower hesitation when working outside primary areas of expertise

The biggest shift is confidence. Tasks that previously required significant ramp-up now feel approachable, which expands what individual engineers can take on.

## **Adoption Challenges Are Real**

Rolling this out across teams isn’t automatic.

Many engineers tried AI tools, got poor results and dismissed them. In most cases, the issue was prompt quality, not tool capability. Asking precise, contextual questions is a skill that improves with practice.

There are also valid concerns about over-reliance. Senior [engineers worry about skill erosion](https://thenewstack.io/5-engineering-skills-to-prioritize-in-the-ai-driven-era/). Junior engineers worry about [learning shortcuts instead of fundamentals](https://thenewstack.io/how-to-build-a-developer-career-when-the-first-rung-is-gone/). Both concerns are legitimate.

What worked was avoiding blanket adoption and instead demonstrating bounded use cases. “Use this to understand an unfamiliar test framework” is actionable. “AI makes you faster” is not.

## **Clear Limits You Can’t Ignore**

AI [struggles with business intent](https://thenewstack.io/ai-adoption-why-businesses-struggle-to-move-from-development-to-production/). It can explain what code does, but it doesn’t know whether that behavior is correct.

Security-sensitive code demands extra caution. Plausible-looking suggestions can hide subtle vulnerabilities. Authentication, authorization and encryption must remain firmly under human control.

Architectural decisions also remain human territory. AI can suggest options, but it doesn’t understand team strengths, operational realities or organizational constraints. Those factors often outweigh technical elegance.

## **What’s Actually Worked in Practice**

* Start with low-risk use cases like test generation and documentation.
* Review generated code with the same rigor as junior developer output.
* Use AI for exploration, not shortcuts into production.
* Ship only code you fully understand and can maintain.
* [Document successful workflows](https://thenewstack.io/platform-teams-win-over-devs-with-quick-wins/) so teams know when and how to use these tools effectively.

## **The Measured Impact**

After two years, the biggest change isn’t increased code output. It’s broader capability.

Engineers move between stacks more easily. New frameworks are hours of learning instead of days. Large, unfamiliar codebases become navigable faster. The cognitive cost of context switching has dropped measurably.

AI doesn’t replace engineering judgment. It reduces friction in the development process and lowers the barrier to effective work outside core expertise.

If you’re evaluating AI for engineering teams, start by identifying your real workflow bottlenecks. Then ask whether AI can meaningfully reduce that friction. The answer depends on context, but the evaluation framework stays the same.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/3256ddb5-cropped-1084930a-nishant-ghan-scaled-1-600x600.jpeg)

Nishant Ghan is a principal software engineer at Oracle Cloud Infrastructure with over 14 years of experience building and operating large-scale distributed systems. He has previously worked at Amazon, Salesforce, IBM and Tableau, focusing on cloud infrastructure, backend systems and...

Read more from Nishant Ghan](https://thenewstack.io/author/nishant-ghan/)