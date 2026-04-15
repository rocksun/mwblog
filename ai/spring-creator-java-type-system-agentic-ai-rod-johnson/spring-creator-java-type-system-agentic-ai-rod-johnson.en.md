[Rod Johnson](https://github.com/johnsonr), the creator of the [Spring Framework](https://thenewstack.io/spring-framework-has-three-major-pitfalls-heres-what-to-do/), is back with another open source project — and this time he’s aiming to solve what he sees as the central problem of enterprise AI: Making large language model-driven applications predictable enough to actually run a business on.

Johnson showcased [Embabel](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014), an [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) framework for [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/), during a live demo last week at [Microsoft’s JDConf](https://jdconf.com/) developer conference. The framework is Apache-licensed, hosted on GitHub, and built on top of [Spring Boot](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/). This means that Java developers already familiar with the enterprise Java-based Spring ecosystem should find the on-ramp short.

Johnson’s goal with Embabel is to show that Java is just as good, if not better, for agentic systems — particularly enterprise systems — as its [Python](https://thenewstack.io/what-is-python/)-based counterparts.

Python-based agentic frameworks include [LangChain](https://www.langchain.com/) and [Crew.ai](https://crewai.com/), while Java-based agentic frameworks include Embabel, [JetBrains Koog](https://www.jetbrains.com/koog/), [LangChain4j](https://docs.langchain4j.dev/), and [Crew4j](https://crew4j.com/).

[Simon Ritter](https://www.linkedin.com/in/siritter/), deputy CTO at Java runtime provider Azul Systems, tells *The New Stack* that this move could help close a widening gap in the agent world.

“My personal opinion is that the increasing availability of Java frameworks will help close the gap between Python and Java usage and in the AI agent space,” Ritter says.

“I decided that it’d be interesting to see what the ideal framework would look like for building agents,” Johnson tells *The New Stack*. “And I fairly quickly concluded that for what I wanted to do, and what I think is unlocking the value of existing businesses, the [JVM](https://thenewstack.io/java-language-architect-brian-goetz-on-how-java-could-evolve/) [Java Virtual Machine] is going to be a much better place to do that…”

However, “I wouldn’t necessarily regard myself primarily as a Java person,” Johnson said during his JDConf keynote. “I would regard myself as a person who wants to solve problems in enterprise software. Back in the early 2000s, the problem was how to be productive with Java. In the mid-2020s, the problem is how to take GenAI and make it relevant to business applications.”

## Where Embabel comes from

Embabel is a JVM-based framework for building [GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) business applications. Johnson launched it in May 2025, and it currently has over five full-time engineers working on it and more than 3,000 GitHub stars.

Embabel is built on Spring Boot and written in [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/), with excellent Java interoperability, Johnson says. It’s an open-source technology with a planned commercial entity similar to the [SpringSource](https://en.wikipedia.org/wiki/Spring_(company)) model, he tells *The New Stack*.

In a [blog post](https://redmonk.com/jgovernor/java-relevance-in-the-ai-era-agent-frameworks-emerge/), [James Governor](https://redmonk.com/team/james-governor/), co-founder of industry analyst firm RedMonk, writes: “With the distributed systems and cloud revolution, so many of the applications and systems that were built, so much of the infrastructure, were built in Java, new languages like [Go](https://thenewstack.io/introduction-to-go-programming-language/) and [Rust](https://thenewstack.io/rust-programming-language-guide/) notwithstanding. The idea that somehow Java isn’t going to play well with AI doesn’t make any sense.”

Discussing Johnson in that same post, Governor writes: “He’s now created [Embabel](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014), a strongly-typed agent framework written for the JVM. It’s designed to bring determinism to your project plan by using a model that isn’t an LLM, then using autonomous agents to generate code that maps to that plan. Not everything is decided by LLM.”

Meanwhile, in a briefing about [Java 26](https://thenewstack.io/java-26-performance-ai/) – the latest version of Java released last month – [Chad Arimura](https://www.linkedin.com/in/chadarimura/), formerly vice president of developer relations at Oracle, told *The New Stack* that Java 26 supports the “natively agentic” nature of Embabel.

## The determinism problem

Johnson says he views the core challenge of enterprise AI adoption as a spectrum. At one end sits something like OpenAI’s ChatGPT, which is powerful and generative, but not something any sane organization would run a business process on, he says. At the other end sits the structured, deterministic code Java developers have been writing for decades, he notes.

The question Embabel is designed to answer is where on that continuum a given application should land and how to get it there.

Johnson’s answer is decomposition. Break large problems into discrete steps. Some steps run as ordinary code. Others invoke [LLMs](https://thenewstack.io/introduction-to-llms/). Those LLM invocations can themselves call tools. Wiring those steps together in a predictable, auditable way is, in Johnson’s view, the core job of a real agent framework.

Most frameworks handle that wiring one of two ways, he said: let the LLM decide which tools to call at runtime, which sacrifices predictability; or use a state machine defined ahead of time, the approach taken by [LangGraph](https://www.langchain.com/langgraph) in the Python ecosystem. Embabel does neither.

Instead, it uses GOAP — Goal-Oriented Action Planning — a non-LLM AI pathfinding algorithm borrowed from game development — to dynamically select execution paths at runtime via strongly typed Java methods, Johnson explains.

“Java can and is innovating in Gen AI,” Johnson says.

In a [Medium post](https://medium.com/@springrod/ai-for-your-gen-ai-how-and-why-embabel-plans-3930244218f6) from last year, Johnson described GOAP as follows: “GOAP is essentially a path-finding algorithm. It can find paths that were never programmed. However, it is deterministic, and it can only choose paths of individual actions (steps) that were explicitly added to the system. If GOAP finds a path, it can explain why that path is the cheapest valid path.

“GOAP finds paths based on facts, which surface as pre- and post-conditions. Goals (which correspond to real-world goals for our agent flows) have preconditions. Actions have preconditions and expected postconditions. Thus, zero or more chains of actions can be found between a given state and a goal.”

## Java’s type system as a feature

A recurring theme in Johnson’s pitch is that Java developers have an underappreciated asset: their domain models. Embabel is built to exploit that. Structured return types — Java records, Plain Old Java Objects (also known as POJOs), Jakarta EE validation annotations — are understood natively by the framework, he says.

When a field carries a validation constraint, Embabel surfaces that constraint to the LLM as part of the prompt, so the model understands what a valid response looks like before it generates one. If the response fails validation, the framework loops back and tells the model why, Johnson said.

The effect is that the LLM becomes a participant in the application’s type system rather than a black box sitting outside it. “The LLM becomes part of the application, not just an endpoint to have a conversation with,” he said.

Embabel also automatically injects contextual information into every LLM prompt, including the current date and time and the knowledge cutoff of the model being invoked — details that matter when LLM-driven steps need to make time-sensitive decisions.

## Model choice as a design principle

Embabel supports multiple LLM providers out of the box, including OpenAI, Anthropic, and Llama, and Johnson was emphatic that model selection should be a per-step decision, not a global application setting. Different steps in a workflow may warrant different models depending on cost, latency, or capability requirements, he said. The framework makes it straightforward to specify a model by name or role at the individual-step level.

Johnson also noted that Embabel sits at a higher level of abstraction than most agent frameworks — closer to what he called an “agent harness” than a low-level orchestration library. That positioning includes integration points for coding agents such as [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) and GitHub Copilot, allowing Embabel-based applications to incorporate those tools directly.

## Getting started

Embabel is available at github.com/embabel. Johnson also pointed developers to his Medium blog for deeper reading on the framework’s philosophy and the GOAP planning model that underlies its runtime behavior.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)