#### As enterprises grapple with the unpredictability of large language models, the quietly ubiquitous JSON Schema standard is emerging as a critical tool for enforcing structure, aligning teams, and turning probabilistic outputs into reliable, contract-bound systems.

There’s a good chance you’re already using [JSON Schema](https://json-schema.org), but you might not know it.

It quietly underpins the validation logic in your API gateway, sits inside the pipeline your team uses to publish microservices, and lives inside the IDE plugin your developers installed without giving it a second thought. Most people encounter it as a necessary detail to get right before moving on to the ‘real’ work. But while you might have come across it as infrastructure plumbing, its core purpose is validating structured data.

## A long and winding road

The standard has a lengthy history. Since it was first proposed by Chris Zyp in 2007 as a declarative language for annotating and validating the structure, constraints, and data types of JSON documents, the spec has passed through multiple stewards and iterations, accumulating opinions and workarounds along the way. It has also accrued significant complexity — its vocabularies and combinators, like *oneOf*, *anyOf*, and *allOf*, represent a rabbit hole that has surprised many engineers at the wrong moment.

“To be honest, it’s kind of a mess,” Kin Lane, co-founder and chief community officer (CCO) for open source API foundation [**Naftiko**](https://naftiko.io), tells *The New Stack*.

But despite that disarray, it has quietly become foundational to almost every major specification in the API ecosystem. The standards that rely on JSON Schema to define and validate their own structures include [OpenAPI](https://spec.openapis.org) and [AsyncAPI](https://www.asyncapi.com/docs/concepts/asyncapi-document/define-payload), as well as newer ones such as Anthropic’s [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25/basic#json-schema-usage). Similarly, Google’s emerging [A2A Specification](https://a2a-protocol.org/latest/specification/) relies on Protobuf rather than JSON Schema as the authoritative source.

What’s more, adoption continues to grow because the problem JSON Schema solves, establishing shared meaning around structured data, never goes away. “It’s the most important spec out there, but it’s the one that frustrates people the most,” Lane says.

## What validation actually does

To understand why JSON Schema matters now more than ever, it helps to be precise about what validation means in practice. In [an earlier article in this series](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/), we talked about the importance of ubiquitous language.

When you define a JSON Schema for, say, a postal address, you’re making a statement that both machines and humans can read: this is what we mean when we say “address.” Is it an address for the US or somewhere else? Does it require a zip code in a specific format? Can it have a second line? A well-constructed schema answers all of those questions and more, encoding the collective understanding of a team or even an entire organization into something that a gateway, a pipeline, or an IDE can enforce automatically.

“It’s not just for systems,” Lane explains. “The validation is mostly for people. If you don’t have people aligned on what those standards are — what an address is, what PII means, what an invoice looks like — and you haven’t agreed on that as a JSON Schema in a registry, it just doesn’t have the impact it could.”

> “If you don’t have people aligned on what those standards are… and you haven’t agreed on that as a JSON Schema in a registry, it just doesn’t have the impact it could.”

The schema files themselves are the shared vocabulary. The validation is the enforcement mechanism. But the goal is alignment, which, as any enterprise architect knows, is the hardest and most valuable thing to achieve at scale.

## Determinism in a non-deterministic world

Lane believes that the non-deterministic nature of [generative AI](https://thenewstack.io/how-generative-ai-informs-platform-engineering-strategy/) makes JSON Schema more relevant than ever.

Ask an LLM the same question twice, and you may get two meaningfully different answers. That probabilistic behavior is what enables AI to handle ambiguity, synthesize across domains, and generate creative outputs that no rule-based system could produce.

Enterprises, however, generally prefer predictability. So the challenge of integrating AI into enterprise operations involves bridging the deterministic and the non-deterministic. JSON Schema is one of the best tools available for drawing that line.

“The balance between determinism and non-determinism — good old APIs and AI functions — is how the world’s going to be split moving forward,” Lane says. “So if you haven’t done any of that work on your data, to clean it, structure it, type it, you’re at a disadvantage.”

> “The balance between determinism and non-determinism — good old APIs and AI functions — is how the world’s going to be split moving forward…”

During our conversation, Lane refers to “known knowns” (available facts)*,* “known unknowns” (information gaps we’re aware of)*,* and “unknown unknowns” (unforeseen risk factors)*,* a term that entered the zeitgeist when Donald Rumsfeld said it in 2002.

In [AI integration](https://thenewstack.io/the-data-engineers-guide-to-genai-and-ai-integration/), the known knowns are data and outputs that are validatable, typed, and structured. The goal is to push as much as possible into the known-unknown category while minimizing the unknown-unknowns that represent genuine unpredictability and risk.

JSON Schema allows you to make a piece of data a known known, Lane suggests. With a schema, data can be validated, tested, and mocked. If it can be mocked, it forms the foundation of a [contract](https://thenewstack.io/risk-mitigation-agentic-ai/) that your AI-powered system can be held accountable for, regardless of how it generated the result.

“Wherever you can say, ‘that’s an address/ a healthcare record/ or an invoice’ — and if it fits a certain standard — you’ve really shifted the work you’re doing for that 90% AI quality bar,” Lane says. “But that takes work. You’ve got to [clean up your data](https://thenewstack.io/clean-data-trusted-model-ensure-good-data-hygiene-for-your-llms/), have your data pipelines and schemas.”

## Registries as organizational infrastructure

Businesses that have made the most progress in this direction tend to share a common structural feature. “Organizations that have a registry, with champions, systems, gateways, IDEs, and pipelines that use it, tend to be more sophisticated and do better in their AI integration,” Lane observes.

You can think of it like a package manager for meaning. Just as NPM provides developers with a shared, versioned pool of code dependencies, a schema registry provides teams with a shared, versioned pool of data definitions. That analogy can be further extended: Just as code without [dependency management](https://thenewstack.io/unlocking-the-power-of-automatic-dependency-management/) tends toward fragility and drift, data without schema governance tends toward inconsistency and shadow definitions that quietly undermine the systems built on top of it.

The most direct places schemas get applied, such as IDEs, pipelines, and API gateways, are also the highest-leverage points in modern software delivery. Catching a schema violation during development, before it reaches a pipeline or a production gateway, is substantially cheaper than catching it after an AI-powered workflow has already processed a corrupted input and produced a confidently wrong output.

## JSON Structure, the new kid on the block

JSON Schema is not without competition. A newer specification called [JSON Structure](https://json-structure.org) has emerged, aiming to be a simpler alternative without the accumulated complexity that has given JSON Schema some of its rougher edges.

The spec, published in July 2025, was authored by Microsoft’s Clemens Vasters. It takes a deliberately different philosophy: strict typing and determinism over JSON Schema’s more flexible, annotation-driven approach.

JSON Structure remains a draft with no formal IETF standing, but Lane is cautiously optimistic about it.

“I hope it dethrones JSON Schema, which has a lot of baggage and enemies,” he says. “But JSON Structure has 15 years of adoption to take on, which is not trivial.”

So for now, JSON Schema remains the pragmatic choice. It is ubiquitous, supported by every major toolchain, and embedded in every specification that matters.

“Don’t try to use it all because it’s very complex,” says Lane. “But it’s useful at stabilizing, so it can ground your AI efforts, helping you and your teams get on the same page, moving in the right direction to achieve what you’re trying to do.”

In this current moment of AI enthusiasm, there is temptation to focus almost entirely on whatever’s new: models, agents, orchestration frameworks, interfaces. JSON Schema is none of those things. It is a 17-year-old specification that most people don’t think about.

But Lane believes that the enterprises that will integrate AI most successfully over the next few years are those with the strongest foundations, including typed structures, shared vocabularies, and validated contracts between systems. JSON Schema has been quietly building those foundations across the enterprise for nearly two decades.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/09/533ec2dc-cropped-379ef74d-charles-humble-5-600x600.jpg)

Charles Humble is a former software engineer, architect and CTO who has worked as a senior leader and executive of both technology and content groups. He was InfoQ’s editor-in-chief from 2014-2020, and was chief editor for Container Solutions from 2020-2023....

Read more from Charles Humble](https://thenewstack.io/author/charles-humble/)