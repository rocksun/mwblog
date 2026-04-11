Everyone says AI needs guardrails. [Julien Verlaguet](https://www.linkedin.com/in/julien-verlaguet-b5710a20/) wants to know who is actually building them.

Verlaguet, founder of [SkipLabs](https://skiplabs.io/), has spent the last year asking that question, but he doesn’t like the answers he keeps finding. “Every time I look closer at people who claim that they are [bringing guardrails to AI](https://thenewstack.io/galileo-agent-control-open-source/), I see more the same,” he tells *The New Stack*. “I see more prompting — and I don’t see anybody who is trying to build real guardrails and real tooling from scratch.”

His explanation for why is that “It’s a lot of work, and so it’s much easier to make those big claims that you’re going to do these things when, in the end, you don’t.”

Verlaguet has set out to do it. SkipLabs builds Skipper, a specialized coding agent for generating and maintaining backend services — not a code generator in the [Copilot](https://thenewstack.io/microsofts-copilot-llm-team/) mold, but the structural layer underneath [AI-assisted development](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/) that’s supposed to make AI output readable, maintainable, and deployable at speed.

“The first thing to notice is that Skipper is not a model,” Verlaguet says. “So, we’re not doing any AI here. We treat models as a commodity. We use different models, [Anthropic](https://thenewstack.io/pentagon-anthropic-model-orchestration/) for the most part, but not only, but to us, the model is just an API that we call with a context, it comes back with the result.”

Verlaguet’s thesis starts with a latency problem, he says.

“In the next few years, it’s not going to be okay to wait for [CircleCI](https://thenewstack.io/circleci-extends-ci-cd-platform-beyond-the-cloud/) to take half an hour to an hour to validate a diff,” he says. “AI is getting faster and faster, and so you will need the tooling to guardrail the AI, and that tooling will need to be incremental.”

## The incremental advantage

Verlaguet built his career on the idea of incremental development. At Facebook he created [Hack](https://hacklang.org/), the gradually-typed [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/) dialect that put a type system on a dynamic language before [TypeScript](https://thenewstack.io/typescript-6-0-rc-arrives-as-a-bridge-to-a-faster-future/) made that approach fashionable.

“When Julien Verlaguet and the team at Facebook created Hack, they were solving a specific problem: PHP, the language powering the entire Facebook codebase, was fundamentally type-unsafe,” wrote [Hugo Venturini](https://www.linkedin.com/in/venturini/), a software engineer at SkipLabs, in a [blog post](https://skiplabs.io/blog/future_of_tools_for_ai).

Yet, Venturini added: “At the scale Facebook operated, that wasn’t just an aesthetic problem, it was an engineering liability,” he says.

 “So, Julien built Hack: a gradually typed, rigorously annotated replacement that was strictly less pleasant to write than PHP,” Venturini writes. “It was more verbose. It demanded precision. It required you to say exactly what you meant. And then they got every engineer at Facebook to switch.”

Verlaguet then built Skip, a full reactive programming environment organized around the principle that when inputs change, you shouldn’t have to recompute everything from scratch. Seeing there were no similar frameworks available outside of Meta, Julien and the team founded SkipLabs to bring reactivity to the next million software engineers, the company says.

[Lucas Hosseini](https://www.linkedin.com/in/lucas-hosseini-73126a41/?locale=en), a software engineer at SkipLabs, in a blog post offers his definition of reactive programming: “In practical terms, [reactive programming](https://www.baeldung.com/cs/reactive-programming) is a declarative way of expressing computations: instead of manually handling state transitions, you simply describe state as a function of multiple inputs.”

Verlaguet left Meta in 2020 to build his startup around the reactive technology; Skipper is where that work lands.

## Two parts, one stack

Skipper has two components. The first is a development environment built on a new, sound, and incremental implementation of TypeScript. Verlaguet chose TypeScript deliberately.

“AI is very good at TypeScript and [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/),” he says. “I think starting with one of these two is probably where you’re going to get the best results.” The soundness matters technically: a type system with holes can’t support the [reachability analysis](https://help.sonatype.com/en/reachability-analysis.html) — the [call-graph](https://en.wikipedia.org/wiki/Call_graph) mapping of what code changes affect what program state — that sits at Skipper’s core.

“If the type system wasn’t sound, then you don’t know what the types are, you don’t know what you’re calling, you cannot build a call graph,” Verlaguet says. A reactive runtime sits on top, updating live state when code changes so the program never has to restart from scratch.

The second component is the harness — the agentic orchestration layer. Classic in structure (plan, generate tests, generate code), but built on the same incremental framework so that generation and remediation happen in parallel on independent pieces rather than sequentially across a whole codebase, Verlaguet says. The combination means Skipper can ingest diffs at speed, rerun only the tests affected by a change, and update a live service without taking it down.

## Beating Claude Code at its own game

On internal benchmarks, Verlaguet claims Skipper passes more than 90% of tests on their corpus of backend service prompts, against 20% for Claude Code on the same corpus. But he is careful about the scope of that comparison.

“Claude Code does a lot more,” he says. “We are better at what we do.” What they do is generate backend services — general-purpose ones, not a catalog of predefined templates. “All the code is generated from scratch,” he says.

Verlaguet says he believes AI will push more and more software into service architectures, not because that’s how things are built today, but because stateful services are what make iterative AI development tractable. He uses a compiler as illustration.

“In five years from now, I’m pretty sure you will want this compiler to be built by an AI. And what does it mean?” he asks. “It means that every time the AI wants to iterate on that compiler, it has to wait half an hour. It doesn’t make any sense.” Turn the compiler into a service with state, send requests to it, and the AI can iterate without the overhead.

Skipper is still in the early stages, however Verlaguet says the company is poised to make an announcement in the next month. He describes the current user base as “us and our friends.”

Verlaguet characterizes SkipLabs as a specialized coding agent shop — and expects that category to get crowded. “I think we’re going to see different agents with different tools, tool chains, that are better at doing certain things,” he said.

The guardrails question, he argues, is what will separate the real ones from the noise.

“Here’s a company who’s actually built the guardrails you were looking for, for your AI-generated code,” Verlaguet says.

The technical ambition is not lost on industry observers.

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, called SkipLabs’ technical creation: “Very fascinating and a reflection of how software is changing in our current non-deterministic world. Instead of using traditional but sometimes network-heavy declarative frameworks for real-time response, this framework and back-end service basically use a declarative mechanism to just reason over what a code block is supposed to do, tracking any dependencies in a computational graph.”

Meanwhile, [David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of AI security platform provider [Arcjet](https://arcjet.com/), tells *The New Stack* that Skipper is definitely addressing an emerging issue.

“I’ve had multiple conversations with technical leaders recently and the industry is still coming to terms with the death of code review,” he says. “We’re in a new world where the old security model breaks down because it assumes a human wrote the code. Review can’t keep up when agents handle implementation — and they’ll soon manage the full cycle from planning through to deployment. Security must be baked into the whole process, from the development environment to runtime.”

## The end of the readability era

In his post, Venturini says “An agent benefits from verbosity. Long, precise, unambiguous tool outputs are easier to parse than short, clever, human-optimized ones.”

He argues that loud, specific failures are more useful than errors swallowed for the sake of developer experience. Strong type systems matter not as guardrails but as the most information-dense description available of what code is supposed to do, he says.

Moreover, that points toward a split in the tooling landscape, Venturini notes in the blog. Languages and environments built for human authors will persist, as “humans aren’t going anywhere.” But alongside them, a new generation of tools is emerging with the agent as the primary consumer: strict, formally specified, intolerant of ambiguity, he indicates.

Skip Labs positions Skipper in that second camp. SKJS, its TypeScript-compatible type checker, is sound where standard TypeScript is not. This tradeoff makes it harder for humans and more useful for agents. The reactive runtime enforces explicit dependency contracts that would feel excessive to a developer writing by hand and are exactly what an agent needs to reason about cause and effect in a codebase, Venturini notes.

The underlying argument: if agents are generating most of the code, and the tools those agents use were designed around human readability, a significant capability ceiling is being left in place. You’re asking the agent to work in someone else’s medium, he says.

“We made the tools more readable to get more developers,” Venturini writes. “We’ll make them less readable — more precise, more formal, more machine-native — to get better agents. The readability era of programming languages was long and productive and is now coming to an end.”

## A timeline

Here is a timeline of Verlaguet’s accomplishments leading up to the creation of Skipper and a potential product release:

* Verlaguet created Hack in 2012 to provide static types, async and generics to the PHP user community.
* In 2014, Facebook open sourced Hack and HHVM under the MIT license.
* In 2017, he created Skiplang, a programming language designed for reactive programming.
* In 2018, Facebook open sourced Skip under the MIT license.
* In 2019, SKAI (Skip for AI) was developed at Facebook to apply reactivity to AI applications.
* In 2020, Skip adds a language – an independent runtime substituting for other infrastructure used at Facebook.
* In 2024, Skip Framework released: a TypeScript-native framework for writing and running reactive functions and services based on the Skip Runtime
* In 2025, SkipLabs announces $8 million in seed funding from Amplify Partners.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)