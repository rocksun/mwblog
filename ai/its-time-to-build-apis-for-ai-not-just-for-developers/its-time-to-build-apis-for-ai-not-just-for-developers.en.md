For the last two decades, the [principles of API design](https://thenewstack.io/what-are-the-core-principles-of-good-api-design/) have centered around the human developer. We built systems optimized for their convenience, with flexible endpoints and rich [documentation](https://thenewstack.io/bad-documentation-bad-documentation/) that they could interpret.

But a new and powerful class of consumer is already disrupting in the form of autonomous [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) that operate on a fundamentally different set of principles, which require a new approach to the way we build and describe our services.

“This means a new paradigm for us as developers: We must now build APIs optimized for consumption by machines, which requires a fundamentally different design philosophy than the one we use for human-centric development,” says [Srinivasan Sekar](https://in.linkedin.com/in/srinivasan-sekar), a director of engineering at [LambdaTest](https://www.lambdatest.com/), an AI-native software testing platform.

This increasing shift toward an “[AI-first](https://thenewstack.io/ai-first-web-development-model-first-design-and-remix-v3/)” design philosophy prioritizes the explicit clarity and predictability that machines require to reason and act effectively. It underpins a clear framework for redesigning systems for the new agentic world.

## Shift From ‘Developer-First’ to ‘AI-First’

At the heart of this new manifesto is a core cultural shift that must precede any architectural changes: moving from a “developer-first” to an [“AI-first” design](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/). As Sekar explains, for years, we have optimized our APIs for the convenience of human developers.

This approach favors flexibility, often resulting in fewer, multipurpose endpoints and a reliance on external documentation to clarify ambiguity. A human developer can read a guide to understand that a certain parameter is required only when another is present — a nuance we have long taken for granted.

> “We must now build APIs optimized for consumption by machines, which requires a fundamentally different design philosophy than the one we use for human-centric development.”  
> **— Srinivasan Sekar, director of engineering at LambdaTest**

AI agents, however, are fundamentally different consumers. They cannot read external documentation or infer implicit relationships between parameters. An AI operates solely on the explicit, machine-readable contract provided by the API’s schema. This, he argues, is the crux of the “AI-first” philosophy: a design approach that prioritizes the absolute, unambiguous clarity that machines require, leaving no room for interpretation in the contract.

[Sai Krishna](https://www.linkedin.com/in/sai-krishna-3755407b/), working alongside Sekar, adds a practical dimension to this shift: “At LambdaTest, we learned this the hard way. We had a perfectly functional API for configuring test environments that developers loved for its flexibility. But when AI agents started using it, we saw a 40% failure rate because the agents couldn’t interpret the implicit rules we’d documented separately. We had to completely rethink our approach.”

This means favoring more specific, single-purpose endpoints and defining all constraints explicitly within the schema itself. This mindset is the non-negotiable foundation for [building any successful and reliable agentic system](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/).

## Unlearning the Three Habits of Human-Centric APIs

Adopting this “AI-first” philosophy in practice means actively unlearning several ingrained habits of traditional, human-centric API design. Sekar identifies three common patterns that, while convenient for human developers, create [critical failures when consumed by AI agents](https://thenewstack.io/no-apis-no-ai-why-api-access-is-critical-to-agentic-systems/).

First is the habit of overloading single endpoints with multiple behaviors. A developer can handle this flexibility, but an AI agent struggles with the ambiguity. The AI-first approach requires distinct, single-purpose endpoints where the function is explicit.

* **Before:** A single `POST /user` endpoint would ambiguously handle both creating and updating a user based on whether an `id` was present in the payload.
* **After:** The AI-first approach uses two distinct and predictable endpoints: `POST /users` to create a new user and `PUT /users/{id}` to update an existing one.

Second is the reliance on implicit contracts and external documentation. For an agent to act reliably, all parameter relationships and dependencies must be explicitly declared within the machine-readable schema itself.

* **Before:** A traditional schema would list `user_type` and `admin_level` as optional, forcing a developer to read external documentation to learn their conditional relationship.
* **After:** An AI-first schema makes this relationship explicit using conditional logic, allowing a machine to understand the contract without any external context.

Finally, teams must unlearn the habit of providing generic error responses. An AI-first API must provide structured, detailed error responses that allow an agent to self-correct.

* **Before:** A generic JSON response like `{"message": "Bad Request"}` would halt an automated workflow.
* **After:** A structured JSON error provides specific fields for the error `code`, `message` and `details`, indicating exactly which parameter was invalid.

These shifts share the common purpose of eliminating ambiguity. By making endpoints, contracts and errors explicit, developers provide the predictable foundation necessary for autonomous agents to act reliably and effectively.

## The New Pillars of AI-First Design

Beyond simply avoiding old habits, building an AI-first API requires embracing a new set of positive design principles centered on clarity and predictability.

“This begins with semantic clarity,” says [Sean Falconer,](https://www.linkedin.com/in/seanf/) senior director of product, AI strategy at [Confluent](https://www.confluent.io/). A truly AI-native API must do more than just describe its technical function; its machine-readable contract must also describe its business purpose, its prerequisites and any potential side effects. This provides the rich context an [AI agent needs to reason](https://thenewstack.io/4-reasons-agentic-ai-is-failing/) about not just how to use a tool, but when and why.

> A truly AI-native API must do more than just describe its technical function; its machine-readable contract must also describe its business purpose, its prerequisites and any potential side effects.

This means developers must enrich their API schemas, moving beyond simple data types. For example, in an OpenAPI specification, every parameter and endpoint should include a detailed description that explains not just the “what” (for instance, an integer ID), but the “why” (such as the unique customer identifier used for billing and support tickets).

This level of clarity is best achieved by designing what Falconer refers to as small, purpose-built tools rather than exposing large, generic API surfaces. [Yoni Michael](https://www.linkedin.com/in/yonimichael), CTO of [Typedef](https://www.typedef.ai/), agrees with this principle, advocating for a “minimal surface area,” meaning the API should expose only what is absolutely essential for a given task.

For architects, this translates into a clear design mandate: Resist the urge to create monolithic, all-purpose endpoints. Instead, complex business processes should be broken down into their smallest logical components, with a dedicated, constrained API designed for each one. A sprawling `/orders` API, for instance, could be refactored into focused, purpose-built tools like `/create-order`, `/check-order-status` and `/request-refund`. Creating these well-defined tools reduces ambiguity and the cognitive load on the AI, making its behavior easier to govern and evaluate.

All of these principles serve a single, critical goal: achieving what Michael calls deterministic behavior. An autonomous agent cannot afford surprises when it is chaining together multiple tools to execute a complex workflow. The system must be utterly reliable and predictable.

To deliver on this, engineers must prioritize rigorous testing and stateless design where possible. Every API call with the same inputs should consistently produce the same output, free from hidden dependencies or unpredictable side effects. This involves providing clear, idempotent interfaces for any operations that modify data, ensuring that repeated calls do not have unintended consequences.

By building APIs with semantic clarity, a minimal surface area and a clear purpose, architects provide the foundation of trust that allows an AI agent to build upon them effectively.

## Hurdles of Reshaping Data for AI

Even with these forward-thinking design principles in place, there is a final, deeper architectural challenge that underpins all AI-first design. Sekar from LambdaTest identifies this as the most significant hurdle of all: the difficult but necessary task of data model flattening.

He explains that most existing enterprise APIs reflect deep-rooted data platform challenges, as they were designed around complex internal database schemas or nested object models. While a human developer can navigate these intricate structures, they create significant “cognitive overhead” for an AI agent.

A deeply nested data structure forces an AI model to [expend valuable resources simply understanding](https://thenewstack.io/automating-context-in-structured-data-for-llms/) the shape of the data and the relationships between its parts before it can even begin to act on the information.

This complexity introduces a high potential for error and makes the agent’s behavior less predictable. The AI-first solution is to flatten and normalize these data models, redesigning them into simpler, more predictable formats that are optimized for machine consumption.

> “The companies building the most reliable agentic systems aren’t necessarily the ones with the most sophisticated AI models. They’re the ones who’ve done the hard work of redesigning their API foundations to speak the language machines understand.”  
> **— Srinivasan Sekar**

And this is usually the most resource-intensive part of the journey to becoming AI native. Sekar argues that this task goes far beyond simply documenting existing systems. It frequently requires a fundamental redesign of the data access layer and the creation of entirely new, parallel API surfaces that are purpose-built for AI agents.

Krishna shares the practical reality of this transformation: “We maintain two API layers now; our legacy developer API and our AI-optimized API. The AI version takes a test result object that was previously nested four levels deep and flattens it into a single-level structure with explicit relationship IDs. It tripled our schema size but cut agent processing time by 70%. The investment was significant, but necessary.” This ensures that the context provided to the AI is not just semantically clear, but also structurally simple and immediately useful.

## The Future Is a ‘Behavioral Contract’

Taken together, these principles — a cultural shift to an AI-first mindset, the unlearning of old habits and a deep architectural commitment to clarity and simple data models — form a new manifesto for API design. But the impact of this new philosophy extends beyond the initial engineering of our systems and into their entire life cycle.

Sekar predicts that this will ultimately reshape core DevOps practices like API versioning. In a world where autonomous agents are the primary consumers, the focus of API management will shift from tracking simple syntax changes to guaranteeing “behavioral contracts.” The promise to the AI will no longer be just that the API’s structure is stable, but that its behavior is consistent and predictable, ensuring the same inputs always produce the expected type of outcome.

Krishna elaborates on how this plays out operationally: “We’ve started versioning our behavioral contracts separately from our API versions. An agent subscribes to a behavioral contract, say, ‘search capability with pagination,’ and we guarantee that contract’s behavior even as we evolve the underlying implementation. If we need to change behavior, we introduce a new contract version, giving agents time to adapt.”

Both Sekar and Krishna emphasize that this commitment to explicit, predictable and behaviorally consistent APIs is the ultimate expression of the AI-first philosophy.

“The companies building the most reliable agentic systems aren’t necessarily the ones with the most sophisticated AI models,” Sekar notes. “They’re the ones who’ve done the hard work of redesigning their API foundations to speak the language machines understand.”

This foundation is what the next generation of reliable agentic AI applications will be built upon.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/85eac203-cropped-f9e1bb76-screenshot-2025-10-27-at-2.36.21%E2%80%AFpm-600x600.png)

Saqib Jan is a technology analyst with experience in application development, FinOps and cloud technologies.](https://thenewstack.io/author/saqib-jan/)