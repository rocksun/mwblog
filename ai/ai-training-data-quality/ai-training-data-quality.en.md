Large language models have moved quickly from novelty to daily infrastructure in software development. We are no longer using AI just to answer isolated questions in a chat window. We are using it to generate services, infrastructure configurations, test cases, and production code, often at a speed that traditional review processes were never designed to handle.

It’s been proven that models can generate code; the question is whether teams can trust what they produce. A big part of that challenge starts far upstream, in the [data used to train the models](https://thenewstack.io/better-context-will-always-beat-a-better-model/) themselves – a clear example of the “Garbage In, Garbage Out” paradigm. This is a phenomenon the AI research team at Sonar has explored extensively and has built technology called [SonarSweep](https://www.sonarsource.com/products/sonarsweep/) to solve.

Public code repositories give models enormous breadth across languages and frameworks, but they also contain outdated libraries, insecure patterns, brittle implementations, and poor maintenance habits. Models learn from all of it. They do not reliably distinguish between examples that reflect sound engineering and examples that merely compile.

That matters because functional code is not the same as production-ready code. In an enterprise setting, code also needs to be secure, maintainable, and resilient under real-world conditions. If those qualities are inconsistent in the training data, they will also be inconsistent in the output.

### The risk of unvetted code

LLMs are essentially sophisticated statistical systems. They do not possess an inherent understanding of “good” versus “bad” engineering. They optimize for the most probable solution based on the provided context and the patterns learned from the training data.

That means weaknesses in the training corpus can persist in model behavior in ways that are easy to underestimate. Research, including [findings from Anthropic](https://www.anthropic.com/research/small-samples-poison) late last year, suggests that even relatively small samples of “poisoned” or low-quality data can be encoded into models’ inner representations and lead to dangerous behaviors.

In a paper I co-authored last year, *“*[Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis](https://arxiv.org/abs/2508.14727)*,”* we observed this exact issue. All models considered in our study generated a mixture of simple and sophisticated bugs, vulnerabilities, and code smells (maintainability issues), and there are some interesting trends between models: with certain labs prioritizing security performance while others succeed in writing maintainable code.

To highlight the complexity of these issues, consider path traversal vulnerabilities. These typically require taint analysis (following an input source to a sensitive sink) in order to detect them. While an LLM might generate a block of code that performs a specific function correctly, it may fail to account for how unvalidated user input could manipulate file paths or inject malicious commands three functions down the line.

> “A model can produce code that looks correct, passes a narrow test, and still introduces issues that increase review time, technical debt and security exposure.”

For enterprise teams, this is the real risk. A model can produce code that looks correct, passes a narrow test, and still introduces issues that increase review time, [technical debt](https://thenewstack.io/hidden-agentic-technical-debt/) and security exposure. At scale, those flaws do not stay isolated. They spread through pull requests, internal tools and downstream systems.

## Why data quality engineering matters

Organizations are becoming increasingly interested in building and owning their AI. If they want their AI-assisted coding to be context-aware, trustworthy, and cost-effective, they need to treat their code and other data as critical assets. That means applying quality controls before the model ever learns from their datasets.

This is where data quality engineering becomes essential. Rather than accepting public code corpora (and even their own data) as-is, teams can inspect, filter, and improve training data so the model learns from stronger examples.

My team has put this into practice with SonarSweep, an approach that “sweeps” datasets before the model ever sees them. This ensures training data is properly scrutinized, which is crucial for companies seeking to understand and improve their agentic development practices. There are four key phases to sweeping datasets:

1. Analyze the code deeply. This goes beyond keyword filtering. Static analysis can identify bugs, security vulnerabilities, and maintainability issues across large datasets.
2. Synthesize examples. Create high-quality training examples for underrepresented tasks and domains. Optionally, an organization may use their codebase to embed specific understanding into the model.
3. Remediate what can be remediated. If insecure or outdated patterns can be automatically corrected, the model can learn from the improved version instead of the flawed one.
4. Curate aggressively. Not every example deserves equal weight in a training set. A quality gate removes low-signal data and maximizes diversity.

## The payoff is measurable

This is not just a theoretical argument. Training on “swept” data in our [model release](https://huggingface.co/SonarSource/SonarSweep-java-gpt-oss-20b) from the end of last year led to a 41% reduction in the density of security vulnerabilities and a 41% reduction in the density of bugs in the model’s generated output.

That kind of improvement matters because the ROI is not only technical. It is operational. Within an agentic coding session, when the model writes code containing fewer bugs and vulnerabilities, the agent will spend less time and fewer tokens in the loops of the [Agent Centric Development Lifecycle](https://www.sonarsource.com/blog/the-future-is-ac-dc-the-agent-centric-development-cycle?utm_medium=referral&utm_source=newstack&utm_campaign=ss-agent-centric-dev-cycle-acdc26&utm_content=media-training%20data-2606-&utm_term=&s_category=Organic&s_source=External%20Referral&s_origin=press) (AC/DC) — a framework built for how software is developed today. Within the AC/DC method, AI agents generate most of the code, and teams manage the development loops in three core stages: Guide, Verify, and Solve.

Furthermore, training the model on your codebase will reduce token usage and help it get up to speed with your architecture and best practices at the start of a session. Additionally, cleaner, better-structured code reduces token use, as agents will spend less time re-reading files, rebuilding context, and working around unnecessary complexity.

Sonar’s [research](https://www.sonarsource.com/blog/a-cleaner-codebase-results-in-less-token-usage) supports that point: Across six matched pairs of codebases and roughly 660 Claude Code task runs, agents working in SonarQube-verified codebases used about 7% fewer input tokens and 8% fewer output tokens, with no meaningful change in task completion.

## Generating quality from the ground up

The [next frontier in AI coding](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) is not simply bigger models or faster generation. It is better foundations. We are reaching the point where the limiting factor is no longer how much code AI can produce. It is how quickly organizations can verify that code and decide whether it deserves to move forward.

> “The next frontier in AI coding is not simply bigger models or faster generation. It is better foundations.”

To close the trust gap, organizations must build quality into their system from the beginning, including the datasets that shape model behavior before deployment. The teams that do this well will be the ones that get the most value from AI-assisted development, because their agents will be more efficient, spend less time correcting preventable defects, and have more time to put trustworthy software into production.

For engineer leaders and developers, the mandate is clear: development teams need to understand the implications of different agent configurations on their token spend and development output.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/e4db1ec7-joe-tyler_sonar-600x600.jpeg)

Joe Tyler is a specialist in Large Language Models with a background in natural language processing and real-world AI applications. He is currently an AI Researcher at Sonar based in London, leveraging generative AI to revolutionize code quality and security....](https://thenewstack.io/author/joe-tyler/)