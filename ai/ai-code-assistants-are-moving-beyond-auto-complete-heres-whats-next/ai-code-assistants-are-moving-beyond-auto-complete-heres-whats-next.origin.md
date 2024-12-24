# AI Code Assistants Are Moving Beyond Auto-Complete: Here’s What’s Next
Until recently, the term AI coding assistant was synonymous with the auto-complete functionality. There was good reason for that. The AI-assisted code completion feature, which predicts and suggests the following few characters, words, or lines as developers type, was a beautiful example of offering relevant help in the context of their workflow and when needed. I have been [writing and maintaining code](https://thenewstack.io/its-no-longer-about-how-you-write-code-but-how-you-operate-it/) professionally for over 20 years. Before AI-assisted code completion, various developer tools already provided similar functionality through reliance on built-in language server features within the IDE. So, AI-powered code completion felt like a natural next step in the evolution of IDEs and the assistance they offered developers.

The other popular AI interaction, the chat interface, was not considered super valuable for [developers since it primarily answered only generic queries](https://thenewstack.io/openais-chatgpt-now-formats-output-to-developer-queries/) like “How do I reverse a linked list?” which no developers need in their regular work.

As a result, the Completion Acceptance Rate (CAR), a metric that calculates the percentage of AI-suggested completions that developers accept, became a key performance indicator for many AI coding tools. Marketing materials for coding tools featured their auto-complete capabilities, often showcasing how they could save [developers time by reducing](https://thenewstack.io/how-sdks-can-reduce-api-integration-time/) keystrokes.

However, that is changing now.

**The ‘Flow’ That Makes Auto-Complete Useful Also Limits It**
It can be a genuinely Flow-like experience when you sit down to write a piece of code, and the code continues to appear magically on your screen. However, the same “in context” quality — help right when you need it, right where you need it — that makes auto-complete helpful is also what limits its utility:

**Limited scope**: Typing code — an extremely human-driven activity — moves at the pace of a human. Besides, typing code is not even the primary developer activity all the time.**Narrow context**: Auto-complete works on a line-by-line basis, lacking an understanding of the broader context of the code or the developer’s intentions**Latency sensitive**: Completions must be provided as quickly as possible, limiting the AI models that can be used. Any delay in delivering suggestions disrupts the developer’s flow.
As a result, the resulting improvement in [software development velocity](https://thenewstack.io/optimize-your-inner-dev-loop-to-increase-developer-velocity/) is incremental at best.

**Solving Complex Software Problems Requires More Than Just Typing Code**
We’re seeing a [shift in how developers](https://thenewstack.io/how-ai-is-shifting-developer-culture-and-work-at-github/) want to use AI tools in development. It’s no longer enough for an AI coding assistant to simply finish your lines of code. Engineering teams are demanding more. They want to [solve more complex problems](https://thenewstack.io/the-complexity-of-solving-performance-problems/). They want to generate entirely new functionality, refactor legacy code, modernize their code to newer language and framework versions, increase code test coverage, improve compliance with security and coding standards, and so on. All of this cannot be accomplished through auto-complete. It requires a more sophisticated understanding of an organization’s broader codebase (beyond the few files a developer works on simultaneously). Most AI coding assistants lack this capability.

As of today, the best interface for such tasks is the good old AI-enabled chat. Developers realize that the same chat that can be a little too generic to be helpful without context (remember reversing linked lists?) turns into a powerful machine when armed with the proper context. This explains why developers turn to chat-oriented programming (CHOP) or coding via iterative prompt refinement to solve their problems.

Let’s look at a recent example of how chat-oriented programming helped me. I was working on an application that processed a lot of video content. Users would upload videos, and my service would need to encode them in various formats, create clips, extract the audio into .mp3 files, and more.

Many of these operations would be very compute-intensive, so I needed to build a queuing system that could schedule jobs, work on tasks when resources were available, and update the queue as tasks were completed. I initially built all the functionality by relying on Redis, a powerful key-value store for creating a queue system.

While my implementation worked great in testing, once we went to production and started using the queuing system I had built, I quickly realized that my implementation would be better suited for a relational database. The system relied on various attributes I needed access to, which meant having to query a ton of unnecessary data to get the key/value pairs I needed from Redis. Rewriting everything to use SQLite would have been quite an undertaking. Still, thanks to chat-oriented programming, I could make this codebase-wide change with just a few chat messages between my coding assistants using my codebase as a context.

The AI coding assistant not only gave me step-by-step instructions on what needed to happen but also generated the working code, replacing existing Redis calls with SQLite database queries, generating the proper schema that matched what I had with Redis, and giving me exact instructions on where to go and what to update saving me countless hours of manual migration. Speaking of migration, I also had my coding assistant write new functionality to migrate all of the existing job data in Redis to SQLite so that no data would be lost when the new version was deployed.

**Success Is Measured by Outcome, not Output**
With this evolution, the metrics for success have also changed. Completion Acceptance Rate (CAR) is still important but no longer the gold standard. Instead, engineering teams are looking at more holistic measures:

**Time saved**: How much overall development time is reduced using this tool?**Problem-solving capability**: Can this tool help tackle complex coding challenges?**Code quality improvements**: Does this tool help improve the overall quality and maintainability of the codebase?**Learning and adaptation**: How well does this tool adapt to project-specific requirements and coding styles?
**Looking Ahead **
Even in the first two years of AI usage becoming mainstream in coding, the usage pattern has evolved swiftly from a more “code typing” activity to a more iterative design or transformation activity. As we move forward, it’s clear that auto-complete, while still useful, is just the tip of the iceberg in AI-assisted coding. The days of coding being synonymous with vigorously typing away in an editor are behind us.

The future belongs to more comprehensive, context-aware AI systems that can truly understand and assist with software development. How we define coding skills and what training for software jobs looks like in the future might differ significantly from today’s. Making the most efficient use of AI through intelligent prompting and incorporating other tools that help make sense of code might become important aspects of how software gets built.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)