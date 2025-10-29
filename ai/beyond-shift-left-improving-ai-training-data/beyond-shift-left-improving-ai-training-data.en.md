The software development world is grappling with a new “engineering productivity paradox.” On one hand, AI-powered coding assistants are generating a staggering volume of code. For example, Google has said that [30% of its code uses AI-generated suggestions](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/). However, the engineering velocity has not seen a proportional jump, with productivity gains being estimated at 10%.

This discrepancy highlights a critical bottleneck: All that AI-generated code must be reviewed, verified and often fixed by human developers. The core issue isn’t the quantity of AI-generated code; it’s the quality.

“Garbage in, garbage out” has been a maxim in computing for decades. Today, it’s the central challenge for coding  [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), which are trained on vast, unfiltered data sets of public code repositories. The inconvenient truth is that these repositories are riddled with bugs, security vulnerabilities and “[code smells](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)” that contribute to technical debt. When an LLM learns from this flawed data, it learns to replicate these flaws.

Recent studies confirm this. [Analyses of leading LLMs](https://www.sonarsource.com/the-coding-personalities-of-leading-llms/) by Sonar show they all share common blind spots, consistently producing code with [high-severity vulnerabilities](https://thenewstack.io/gpt-5s-enhanced-reasoning-comes-with-a-steep-hidden-cost/) and a deep-seated tendency to write code that is hard to maintain.

This flood of problematic code places an even greater burden on human reviewers, shifting the bottleneck rather than eliminating it and creating the very productivity paradox we’re trying to solve.

## **Shifting Left of ‘Shift Left’**

For years, the industry has championed the “shift left” movement — a practice focused on identifying and fixing quality and security issues as early as possible in the software development life cycle (SDLC). We moved testing from a final pre-production phase to an integrated part of CI/CD pipelines, and static analysis tools were integrated directly into the developer’s IDE. The goal was simple: Find it early, fix it cheaply.

But AI-assisted code generation breaks this model. The “beginning” of the life cycle is no longer when a developer writes the first line of code. The life cycle now begins before that — inside the LLM itself, with the data it was trained on.

If an AI tool generates code that is already insecure or buggy, the “shift left” battle is already half-lost. We are, in effect, playing defense, using our best developers as a final backstop to catch the mistakes of our most “productive” new tools.

The logical, necessary evolution of this concept is to shift even further left. We must move our focus from only reviewing AI-generated code to improving the source. The new frontier for code quality and security is the LLM’s training data.

## **Curating the AI’s ‘Education’**

A new approach is emerging to tackle this problem head-on. The concept involves applying a “sweep” to the massive data sets used to train and fine-tune coding models.

Imagine using a powerful, large-scale static analysis engine — one that understands thousands of bug patterns, security vulnerabilities and maintainability issues — and turning it loose on petabytes of training data. This engine can identify, remediate and filter out problematic code before it ever becomes part of the LLM’s “education.”

The results of this approach are profound. At Sonar, our early findings with our new service, [SonarSweep](https://www.sonarsource.com/products/sonarsweep/), have shown that models fine-tuned on such remediated data produce code with significantly fewer flaws. In one [analysis](https://www.sonarsource.com/blog/announcing-sonarsweep-improving-training-data-quality-for-coding-llms/), this “sweeping” process led to models that generated code with up to 67% fewer security vulnerabilities and 42% fewer bugs, all without degrading the functional correctness of the output.

This represents a fundamental change in our approach to AI-assisted development. Instead of just generating more code faster and creating a downstream review bottleneck, we can train models to generate better code from the start.

True velocity isn’t just about raw output; it’s about the amount of high-quality, secure and maintainable code that makes it to production with minimal human friction. By ensuring our AI models learn from our best examples, not our worst, we reduce the review burden and free human developers to focus on what they do best: solving complex problems and building what’s next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/10/ca962631-cropped-f28d9fad-manish-kapur.jpg)

Manish Kapur is a technical product leader with a strong background in product management, developer relations, marketing, and strategy. He is currently a senior director of technical product marketing at Sonar, based in Austin, Texas.

Read more from Manish Kapur](https://thenewstack.io/author/manish-kapur/)