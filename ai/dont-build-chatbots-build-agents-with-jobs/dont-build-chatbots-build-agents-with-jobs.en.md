You wouldn’t give every employee root access to your production servers. So why give [AI agents](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/) unfiltered access to your business?

There’s a growing fantasy in the AI world: fully autonomous agents that can handle any task, in any domain, with zero oversight. It’s a compelling vision, but one of the biggest reasons enterprise adoption continues to stall.

[Large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) are powerful, but fundamentally unreliable. This isn’t just about occasional errors; [hallucination is an “inevitable” limitation of the underlying tech](https://arxiv.org/abs/2401.11817). One prompt might return something useful, the next complete nonsense. A recent Stanford study found [hallucination rates as high as 88% in legal scenarios](https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive). Businesses see this, and trust is fragile. Promising open-ended intelligence only distracts from the value these systems can reliably deliver today.

If you want useful AI, you have to work with the grain of the technology. That means embracing constraints: closed-world problems, purpose-built agents, scoped tools, strong evals and layered governance.

## LLMs Will Never Know You Unless You Tell Them

We love to compare LLMs to human brains. They seem smart, articulate, even insightful. But as much as we like the comparison, LLMs aren’t like people, and expecting them to behave that way sets you up for disappointment.

In the first wave of AI, systems were trained for one job at a time.

You’d take your company’s data, label it and train a model to do something very specific, like predict churn or classify support tickets. The result was a model that really understood your domain, because it had your data baked right into its weights. The trade-off was flexibility. You couldn’t use that same model to write blog posts or analyze images. It was good at one thing and only that thing.

[![The purpose-built model training pipeline](https://cdn.thenewstack.io/media/2025/07/28efcf1d-image3-1024x494.png)](https://cdn.thenewstack.io/media/2025/07/28efcf1d-image3-1024x494.png)

The purpose-built model training pipeline.

Foundation models are the opposite.

They’re flexible, capable of handling a huge range of tasks. But they weren’t trained on your systems, your processes or your customer data. So while they’re great generalists, they’re really very dumb about your business.

That’s where prompt design and contextualization come in. To get useful results, you have to give the model everything it needs to know, every single time. There’s no memory between prompts. Every interaction starts from scratch.

[![Contextualizing prompts for app-specific answers](https://cdn.thenewstack.io/media/2025/07/ffd775be-image4-1024x579.png)](https://cdn.thenewstack.io/media/2025/07/ffd775be-image4-1024x579.png)

Contextualizing prompts for app-specific answers.

The key is this: Reliability doesn’t come for free. It has to be engineered. And it’s not binary. Reliability is a spectrum, and what’s “reliable enough” depends entirely on the use case.

If you’re fully automating financial transactions or medical records processing, you may need near-perfect accuracy. In that world, LLMs either aren’t ready (and may never be) or you need to wrap them in many layers of validation, testing and fallback logic to make them safe. On the other hand, if you’re generating meeting notes, surfacing helpful support docs or summarizing internal comms, an occasional error may be acceptable as long as the overall signal is useful.

Understanding that difference is what separates AI that works in the real world from prototypes that fall apart in production. If you want consistent, reliable outputs, treat context like a first-class input. Keep it tight, stay on task and give the model just enough to succeed at the job you’ve asked it to do.

## LLMs Are the New OS; Don’t Give Everyone Terminal Access

In his speech “[Software is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ),” [Andrej Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/), former director of AI at Tesla, compares LLMs to operating systems. Just as apps run on macOS or Windows, AI apps now run on GPT, Claude and Gemini. In that analogy, ChatGPT is the terminal: powerful, flexible, and open-ended.

But terminals aren’t for end users. They’re for developers. In real systems, we don’t give people raw access; we build structured interfaces. The same applies here. AI needs guardrails, not root access.

You wouldn’t let employees poke around your production database using raw SQL. You’d give them scoped access through tools, like dashboards or apps, that help them do their job without exposing everything underneath. The same logic applies here.

For business AI systems, the ideal UX isn’t a chat box. It’s not about someone typing questions into a prompt window and hoping for a helpful answer. The real opportunity is in AI systems that are always on, quietly working behind the scenes. These systems don’t wait for a human to ask a question. They react to signals: a new support ticket, a customer abandoning their cart, an incident alert. And when those signals show up, they act with purpose, context and constraints.

This shift, from human-prompted to signal-driven, requires a different approach to UX.

You’re not building general-purpose chatbots. You’re building agents with a job to do. That means giving them access to just the right data, at just the right time, for a clearly defined purpose.

To effectively use AI, prioritize tackling closed-world problems.

## Focus on Closed-World Problems

One of the biggest mistakes teams make with AI agents is trying to solve open-world problems when they should be solving closed-world ones.

Open-world problems are things like “teach me math” or “write me something interesting.” There’s no clear input, no fixed output and no single way to measure whether the result is good or bad. The model might give you something clever or it might completely miss the mark.

Closed-world problems are different. You can define the inputs, the expected outputs and the criteria for success. Think about things like:

* Processing an insurance claim
* Troubleshooting an IT ticket
* Onboarding a new customer or employee

These are bounded tasks with rules, constraints and measurable outcomes. That’s what makes them suitable for LLM-based systems, not just because they’re easier to automate, but because they’re easier to trust.

It’s no coincidence that code generation has been one of the most successful LLM use cases so far. The inputs are clear, the outputs are testable and correctness is verifiable. You can run the code. That same pattern, clear expectations and tight feedback loops are exactly what make closed-world business use cases viable.

When you focus on closed-world problems, you get:

* **Better testability:** You can write test cases and know what a good response looks like.
* **More explainability:** It’s easier to debug or audit the system when things go wrong.
* **Tighter guardrails:** You can limit what the AI is allowed to see, say or do.

The more you can reduce ambiguity, the more reliable your AI systems become. It’s all about designing with intent. Solve problems where the path is clear, the scope is defined and the stakes are known. Add as much determinism to the inherently nondeterministic process as you can. That’s how you build AI that delivers results instead of surprises.

## Purpose-Built Agents, Not General Chatbots

Once you’ve narrowed the problem space, the next step is to break it down.

Trying to build a single, all-knowing AI that handles everything from customer service to sales forecasting is a fast track to complexity and chaos. Instead, treat AI like software: modular, composable and scoped to specific jobs.

That’s where purpose-built agents come in.

A purpose-built agent is an AI system with a clearly defined responsibility, like triaging support tickets, monitoring system logs or generating weekly sales reports. Each agent is optimized to do one thing well.

[![Building purpose-built agents](https://cdn.thenewstack.io/media/2025/07/38efa2d9-image1-1024x480.png)](https://cdn.thenewstack.io/media/2025/07/38efa2d9-image1-1024x480.png)

Building purpose-built agents.

And just like in software, the power comes from composition.

Take a closed-world problem like processing an insurance claim. It’s not just one step. It’s a series of structured, interconnected tasks: validating inputs, checking eligibility, fetching relevant policy details, summarizing the case and escalating exceptions. Instead of building one monolithic agent to handle all of it, you can design atomic agents, each handling a specific piece, and orchestrate them into a multiagent system.

This kind of decomposition makes your AI systems more reliable, more secure and easier to evolve. And just like with software microservices, the magic happens not just within each agent but in the way they work together.

## Build Tools for LLMs, Not People

Once you’ve broken down your system into purpose-built agents, the next step is giving them the right tools, just like you would for any team.

With LLMs, they rely entirely on what you expose them to and how well it’s described. So if you want your agents to behave predictably, your tools need to be designed with that in mind.

[![Thinking loop to decide on tool use](https://cdn.thenewstack.io/media/2025/07/d04d2a00-image2-1024x881.png)](https://cdn.thenewstack.io/media/2025/07/d04d2a00-image2-1024x881.png)

Thinking loop to decide on tool use.

And it’s not just a matter of exposing your existing API endpoints. A generic tool, like an open-ended SQL interface to your production database, might seem powerful, but it’s incredibly hard for an LLM to use safely.

Imagine what it takes for an agent to write a query with a generic SQL tool:

1. Ask for the schema.
2. Parse a large, potentially messy schema response.
3. Infer the right table to use.
4. Guess at the necessary joins across related tables.
5. Construct the correct SELECT statement.
6. Try to decide how much data to return.
7. Format the result in a useful way.
8. Handle edge cases or ambiguous fields.

Each of those steps introduces risks like wrong assumptions, incomplete context, ambiguous naming and high potential for hallucination. Worse, if the query fails, most agent frameworks will retry the entire sequence, often with slight prompt tweaks. That leads to token bloat, cascading retries and increased cost without improving the result.

You end up with all the downsides of open-world problems: unclear intent, wide decision space, unpredictable behavior. Like agents, tools should be purpose-built. They should be designed specifically to help the agent solve a well-scoped task. Think “fetch today’s unshipped orders” instead of “run any query you want.”

The more you reduce ambiguity, the more reliably the model can get the job done.

That means building tools that are:

* **Strongly typed:** No ambiguity in what goes in or what comes out.
* **Constrained:** Small, focused tools are easier for agents to reason about and harder to misuse.
* **Self-describing:** Tools should include metadata, examples and descriptions to help the model know when and how to use them.
* **Access-controlled:** Just like with users, not every agent should have access to every tool. Scope matters.

This is where protocols like the Model Context Protocol (MCP) come in. MCP helps standardize the way tools are defined and described so agents can reason about them more effectively. If you do this right, you’re giving LLMs the right context to use tools safely and correctly.

When you design tools correctly, you can force reliability. The model stops improvising and starts operating more like software should: with clear rules, defined behavior and predictable outcomes.

## Governance, Testing and the Need for AI Testers

In traditional software, testing is about whether the output is correct. With AI agents, that’s just the beginning. You also need to test how the agent discovers tools, how it decides to use them and whether it uses them correctly.

That means spending real time on evaluations.

If you’ve built your agents and tools to be purpose-built and scoped, then writing good evals should be straightforward. You know the inputs, you know the expected outputs, and you can run consistent checks across edge cases and common workflows. This isn’t something you can just eyeball. You need repeatable, deterministic tests, just like any other production system.

And for many use cases, human-in-the-loop should be part of the system. You should think through what can be fully autonomous and what requires human oversight. You may need people involved for escalation, validation and learning. Let AI handle the routine, predictable tasks, and let humans step in when things get messy.

## Control Is a Feature, Not a Limitation

LLMs are most effective when they’re scoped, structured and grounded in clear context. Predictability is what makes AI reliable at scale. If you want AI that delivers real results, design for control and purpose, not open-ended freedom.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/12/0417379b-cropped-a5739559-sean-falconer-600x600.jpg)

Sean Falconer is an AI Entrepreneur in Residence at Confluent where he works on AI strategy and thought leadership. Sean's been an academic, startup founder and Googler. He has published works covering a wide range of topics from AI to...

Read more from Sean Falconer](https://thenewstack.io/author/sean-falconer/)