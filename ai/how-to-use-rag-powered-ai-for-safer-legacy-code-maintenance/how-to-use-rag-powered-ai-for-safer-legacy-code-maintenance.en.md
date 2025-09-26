The reality is that generative AI (GenAI) was never “introduced” into enterprise business; it crept in when users discovered it could take some of the more tedious tasks off their to-do list. Before anyone was ready, the enterprise developers who write code for a living were also using AI.

This has put enterprise leaders into a bit of a bind. [Vibe coding](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) to produce a vague minimum viable product (MVP) is tolerable, but there is justified suspicion about using it elsewhere.

But the heavy work in today’s enterprise isn’t greenfield projects. The biggest lift is maintaining the legacy codebase. And many enterprises are exploring whether AI is capable of taking some of that weight off developers without exposing them to common AI-related risks.

## **The Challenges of Maintaining Legacy Code**

Large codebases, built carefully over time, are always full of “legacy code” — old code written by developers using older technology stacks and frameworks. And all of that code has to be patched, updated and integrated as new capabilities are developed around those legacy systems, lest the enterprise business grind to a halt.

All systems follow a similar origin story: An MVP is converted to a product by some smart developers. Next, as use cases expand, a set of technology integrations is layered in. Then, corporate methodologies are implemented.

Meanwhile, the original developers move on to new projects, leaving behind an ops team that knows how to run the system. Then someone realizes that the system doesn’t scale well, or doesn’t work with a new system or a mandate from a recent corporate restructure, acquisition or regulation.

Only a handful of people know more than small sections of the code. There was once some enthusiastic documentation, but that stopped about five years back. Most of the code makes sense locally but the context is mysterious. The integration tests broke some time ago, but no one remembers quite when.

Every developer eventually faces legacy code. It’s not about who gets stuck with it, but how we can all handle it better.

## **How Agentic AI Helps Modernize Legacy Systems**

Recently, companies have been exploring [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) to solve these problems. These products will usually look at your codebase, but all-in-one [large language models (LLMs)](https://thenewstack.io/introduction-to-llms) that have sampled modern code examples from “diverse” sources might struggle to understand old corporate legacy code or local policy.

To solve this, companies including [Tabnine](https://www.tabnine.com/?utm_content=inline+mention) have incorporated [retrieval augmented generation (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary) into their LLMs to increase accuracy and look more closely at the project code.

Tabnine’s RAG-powered [Enterprise Context Engine](https://www.tabnine.com/blog/your-ai-doesnt-need-more-training-it-needs-context/) starts by analyzing the codebase. When your codebase changes, the engine can update its understanding simultaneously.

To understand how Tabnine’s RAG-powered engine works, let’s break down a typical task: Connecting a legacy system to a new data source.

You can start by asking Tabnine: “Where in the codebase do we connect to the database?” This isn’t a generic query about databases; the Enterprise Context Engine must thoroughly understand the codebase to execute this query correctly. Next, you can ask: “Explain what this code does with respect to the rest of the code.” You can even ask the [Tabnine Documentation Agent](https://www.tabnine.com/blog/your-ai-doesnt-need-more-training-it-needs-context/): “Generate docs for this function” to help pave the way for the next team working with the legacy code. You can also generate [unit tests](https://docs.tabnine.com/main/software-development-with-tabnine/accelerate-unit-testing) via the Tabnine standard chat box, if you don’t have the time for test-driven development (TDD).

To make it easier for developers to get started, they can launch the Tabnine [Onboarding Agent](https://www.tabnine.com/blog/introducing-tabnines-onboarding-agent-revolutionizing-developer-onboarding/) from the chat box as a built-in command (`/onboarding`) or when starting a new conversation. When triggered, the agent returns a concise summary of the project’s key aspects, enabling developers to quickly grasp its structure and functionalities. It then suggests further relevant paths to explore, rather than generating an impressive-looking but overwhelming summary “info dump,” like some agentic command-line tools do.

## **Prioritizing Security, Privacy, and Compliance in Enterprise AI**

Security is not a side matter for enterprises. They run on known infrastructure, so they can be certain of things like the geographical locations of components to ensure legal compliance. While Tabnine comes as a plugin for AI code assistants, like [others I’ve looked](https://thenewstack.io/author/david-eastman/) at recently, it puts more focus on keeping code private, secure and compliant. Tabnine can be instructed to only use permissively licensed code, with strict guardrails, rules and ongoing review processes that censor out restricted licenses and coach the models toward safe, compliant outputs.

Enterprises choose their vendors carefully, rarely using a small team, and must be certain that each technology they use works across their entire tech stack. To support cross-platform requirements, Tabnine does not mandate any particular LLM or even an IDE. It works as a plugin for VS Code and IntelliJ, as you would expect, but also Eclipse and quite a few others.

Because its Enterprise Context Engine can be placed anywhere, Tabnine can sit in your corporate network air gap, if that’s what is needed:

[![Enterprise Context Engine enables a Tabnine cluster to sit in a private customer environment (on prem or virtual private cloud) if needed](https://cdn.thenewstack.io/media/2025/09/5d314876-image.png)](https://cdn.thenewstack.io/media/2025/09/5d314876-image.png)

Source: Tabnine

It can be set up within the enterprise, on premises or in a private cloud. Note that the connection back to Tabnine servers is optional. Otherwise, Tabnine sits behind the corporate wall and keeps information confidential.

Tabnine doesn’t lock users into a single proprietary model. It works with the top LLMs, including Claude, GPT and open source options, while allowing only permissively licensed code to be used. This helps reduce your legal risk and [protect your code insights](https://www.tabnine.com/code-privacy/).

It connects to Git and other source control systems, as well as local Jira and Confluence instances, and project knowledge is often stored in Confluence. I appreciate this because I still think Atlassian’s corporate wiki tool is the best in class for team knowledge capture.

Tabnine’s visibility tools also include governance, risk and compliance (GRC) capabilities, which is an important issue for most enterprises.

[![Tabnine includes GRC capabilities including auditability, setting pricing thresholds, access control to LLMs, MCP governance, and code provenance](https://cdn.thenewstack.io/media/2025/09/553f9f29-image-1.png)](https://cdn.thenewstack.io/media/2025/09/553f9f29-image-1.png)

Source: Tabnine

The code generation provenance GRC tool is a story all in itself: Just as you don’t want your secret sauce to leak out, you have to prevent unaccountable code from breaking in. Many LLMs are trained on general open source code, which can be problematic. Tabnine can ensure that non-permissively licensed code is not used in your enterprise codebase, avoiding costly copyright lawsuits or other claims of IP infringement.

## **An AI Toolset for Enterprise Development**

Legacy systems have different issues from projects built from scratch. Tabnine isn’t a new LLM or a new IDE, but an integrated platform that leverages leading IDEs and LLMs for enterprise development. With its set of AI tools, led by the Enterprise Context Engine, Tabnine helps developers acquire the critical expertise they need to tackle modernization projects. It does this by offering the types of AI assistance enterprise developers need to tackle legacy codebases while keeping attention on preventing common risk factors.

Its story isn’t quite the same narrative as the bleeding edge of agentic AI, but as technology boards in larger companies come to grips with their LLM policies, Tabnine will be quite a welcoming port in the storm of AI disruption.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)