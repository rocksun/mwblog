AI leaders have, for the last couple of years, obsessed over benchmarks, debating whether [GPT-4](https://thenewstack.io/we-used-gpt4-during-a-hackathon-heres-what-we-learned/), Claude or [Gemini](https://thenewstack.io/google-launches-gemini-3-pro/) holds the crown. This enterprise AI conversation has been dominated by a single metric: Model performance. But this fixation on raw “intelligence” overlooks the most critical factor in successful deployment.

As these models converge in capability, the battleground is shifting. The differentiator for the next generation of enterprise applications won’t be the model itself; it will be the context. In a landscape where every enterprise has access to the same frontier models, the “intelligence” of the model is no longer a sustainable moat. Instead, the winner will be the organization that can most effectively ground that intelligence in its proprietary reality.

“[Context](https://thenewstack.io/why-context-aware-ai-is-quickly-replacing-code-only-tools/) is the new source code,” says [Srinivasan Sekar](https://www.linkedin.com/in/srinivasan-sekar/), director of engineering at [TestMu AI](https://www.testmu.ai/) (Formerly LambdaTest), an AI native software testing platform. He exposits that while the industry is fixated on model size, the real challenge lies in data delivery.

“We are finding that a model’s intelligence is only as good as the environment we build for it,” he explains. “If the context is cluttered, even the most advanced model will fail.”

Feeding enterprise data into these models is therefore proving to be far more dangerous and complex than initially thought. It is not just about piping in documents; it is about preventing the AI from [“choking” on the noise](https://thenewstack.io/why-agentic-ai-needs-a-context-based-approach/).

This requires a shift from viewing AI as a “know-it-all” oracle to viewing it as a reasoning engine that requires a high-fidelity information environment to produce business value.

I spoke to notable engineering leaders who shared their perspectives about how the future of AI is found in the precision of the architecture surrounding it. In essence, the model acts as the processor, while the architecture serves as the fuel that determines speed, accuracy and enterprise-grade reliability.

## The Rise of ‘White Coding’ and the Governance Gap

The stakes of this transition are high because the role of AI has fundamentally changed. We have moved beyond simple auto-complete into a paradigm that [Brian Sathianathan](https://www.linkedin.com/in/briansathianathan), cofounder of [Iterate.ai](http://iterate.ai), calls “white coding.” In this environment, tools don’t just complete a line of code; they generate entire architectures, multi-file edits and complex logic from a single prompt. A task that once required days of human effort is now accomplished in 20 minutes.

However, this unprecedented speed creates a terrifying governance gap. When a human writes code, they govern it line by line. When an AI generates 5,000 lines in a single session, that granular oversight vanishes.

Sathianathan warns that if developers do not have the right context and security guardrails in place from the start, they risk generating technical debt at machine speed. Without intentional context, a model might introduce frameworks with known vulnerabilities or create fundamentally insecure logic flows. These are risks that may not be discovered until it is too late.

To address this, engineering teams must move away from retrospective code reviews toward “pre-emptive context governing.” This involves embedding security standards directly into the environment the AI “sees,” ensuring that generated logic remains within safe, predefined boundaries.

## The Fallacy of ‘More is Better’

The natural instinct for most developers is to solve inaccuracy by providing the AI with more information. If the AI understands the entire codebase, the logic goes, it cannot make mistakes. [Neal Patel](https://www.linkedin.com/in/neal-k-patel/), cofounder and CEO of [Scaledown](https://scaledown.ai/), warns that this is a dangerous fallacy. His research into context engineering reveals that across enterprise workloads, roughly 30% to 60% of tokens sent to models add no value.

“People think more tokens mean more accuracy, but in practice, the opposite often happens,” Patel says. “When a model is overloaded with loosely related or irrelevant context, its attention mechanisms get diluted.”

This isn’t just a theoretical concern; it is backed by empirical research. Patel cites the “[Lost in the Middle](https://aclanthology.org/2024.tacl-1.9.pdf)” study (Stanford/Berkeley), which showed that model accuracy drops when relevant details are buried in the center of a long prompt. Furthermore, [research from Mila/McGill](https://aclanthology.org/2025.acl-long.1458.pdf) found that adding unrelated text caused 11.5% of previously correct AI answers to become wrong.

This creates a phenomenon Patel calls “context rot.” As a system serves a user over months or years, it accumulates history and metadata. The same use case becomes exponentially heavier, slower and more expensive.

“The goal isn’t to stuff the window; it’s to extract the signal,” Patel notes. Smarter, high-fidelity context, achieved by isolating only what is truly needed for the query, consistently beats larger, noisier context.

## Fighting ‘Context Poisoning’ With Structure

This is where the engineering reality hits the road: How do you build a system that gives the AI exactly what it needs, and nothing more? Sekar identifies the root issue as “opaque systems.” When an engineer dumps an entire codebase or schema into context, the AI is forced to search through a haystack of data to find the needle that matters, often losing sight of security constraints during the process.

To overcome this, teams should adopt a structured retrieval approach. [Sai Krishna V,](https://in.linkedin.com/in/sai-krishna-3755407b) also a director of engineering at TestMu AI and working alongside Sekar, describes a method of “flattening” complex data structures before they ever reach the AI. Instead of feeding deep, nested objects that increase the cognitive load on the model, TestMu AI normalizes data into single layers.

Implementing this requires a mindset of “curating the memory” of the AI. By using intelligent retrieval to fetch only the specific notes or logic required for a current problem, engineers can create a clean environment for the AI’s reasoning process. This ensures the model stays focused on the task at hand without being “poisoned” by distant, unrelated data structures.

## Context Caching and ‘The Notebook’

The final piece of the puzzle is operational efficiency. If an AI agent has to re-read and re-analyze the same project context for every single query, the system becomes prohibitively expensive and slow. Patel of Scaledown points out that this inefficiency has a human cost as well; every redundant token increases latency, leading to abandoned searches and slower product flows. And to solve this bottleneck, Sekar advocates for a technique called context caching.

Sekar describes this with a practical analogy. Think of the agent as a student with a notebook. The first time the agent solves a complex architectural problem, it shouldn’t just output the code; it should cache its “understanding” of that problem, essentially taking a note. The next time a similar request comes in, the agent retrieves that cached context rather than deriving the solution from scratch.

So while Patel highlights the necessity of reducing token waste to maintain responsiveness, Sekar’s approach provides the technical blueprint for how enterprises can actually “curate the memory” of their systems. This shift ensures that the AI is not just repeating calculations, but building a persistent, efficient knowledge base over time.

## Cognition for Humans and AI

Context is more than just an architectural mechanism for efficiency; it is an active layer in the workflow that helps people work with AI more deliberately. [Bhavana Thudi](https://www.linkedin.com/in/bthudi/), founder and CEO of [Magi](https://www.magihq.com/), a context-aware operating system for AI native marketing teams, describes this as designing “moments of pause” into the human–machine loop. These pauses create space to reflect, reconsider and learn as part of the flow of work, forming a shared loop of reasoning that makes both humans and machines better at the task.

When AI systems are designed around context and deliberate pause in the workflow, teams intentionally build a thoughtful work environment, and cognition emerges across the human-machine system. Thudi notes that these moments of pause are not just cognitive, but cumulative, allowing work to carry memory forward rather than resetting with each interaction. That is the future of work.

The implication for those building AI systems is clear: Progress will not come from removing humans from the loop, but from designing systems that preserve intent, memory and judgment over time. Systems built with context at the core make better work possible, and compound in value.

## Filtering as the Competitive Advantage

As enterprises move from experimenting with chatbots to deploying autonomous agents, the focus must shift from the model to the data pipeline. The companies building the most reliable systems are not necessarily those with the most sophisticated AI models. They are the ones that have done the hard work of redesigning their data foundations to speak the language that machines understand.

As Krishna concludes, in an era of infinite noise, the ability to filter is the ultimate competitive advantage. That filtering does not happen at the model level; it happens at the architecture level, specifically in how you structure data, retrieve context and validate outcomes. The message for the next year of AI development is clear: The model provides the reasoning, but the engineer must provide the context.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/85eac203-cropped-f9e1bb76-screenshot-2025-10-27-at-2.36.21%E2%80%AFpm-600x600.png)

Saqib Jan is a technology analyst with experience in application development, FinOps and cloud technologies.](https://thenewstack.io/author/saqib-jan/)