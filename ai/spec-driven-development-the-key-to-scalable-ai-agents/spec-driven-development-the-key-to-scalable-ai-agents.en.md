“The person who communicates the best will be the most valuable programmer in the future. The new scarce skill is writing specifications that fully capture your intent and values,” [Sean Grove](https://www.riseos.com/) from OpenAI said recently at the [AI Engineer conference](https://youtu.be/8rABwKRsec4?si=P8vnlkJsRruhjw7d).

[Specifications, not prompts or code](https://thenewstack.io/test-driven-development-with-llms-never-trust-always-verify/), Grove says, are becoming the fundamental unit of programming, and writing specs is the new superpower.

As AI makes it easier than ever to generate code, two things have become clear. The first is that generating more code with AI does not [remove complexity from software engineering](https://www.aviator.co/blog/throwing-ai-at-developers-wont-fix-their-problems/); it just abstracts it away to debugging, testing and deployment pipelines. And that writing code was never the bottleneck.

## **Writing Code Isn’t the Bottleneck**

The bottleneck is knowing what to build, gathering requirements, knowing why to build it, and, ultimately, knowing if it has been built correctly and achieved its intentions. Engineering organizations are going to feel that squeeze the more advanced the AI models get, Grove points out.

Design alignment across teams, resolving conflicting requirements, eliminating tech debt, bringing rigor to code reviews and preserving institutional knowledge when senior engineers leave are listed as the fundamental challenges that make building software difficult in [Amazon’s announcement for its AI IDE](https://kiro.dev/blog/introducing-kiro/) and the concept of spec-driven development.

The main thing that determines whether an agent succeeds or fails is the quality of the context it’s given. And, if we want agents to succeed not only at [vibe coding](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) cool apps from scratch, but in messy, brownfield enterprise codebases, giving agents the right context — or context engineering — is the missing piece to make it happen.

But getting context is hard. Even as [large language models’ (LLMs’)](https://thenewstack.io/what-is-a-large-language-model/) context windows are increasing, we already know that providing larger context to LLMs actually drops the quality. The secret is the quality of the provided context.

Specs are “refined context” that provides just enough information to the LLMs to be effective without being overwhelmed.

## **What Is Spec-Driven Development?**

Spec-driven development is the practice of writing specifications before writing code — or asking an AI tool to write code. Instead of just trying your luck with prompts, no matter how carefully crafted, and then prompting for fixes, spec-driven development starts with clear and structured documents that capture requirements, intentions and constraints.

In the AI coding era, a specification acts as a guide for AI agents, something they can reference, validate their work against and use to stay oriented. It’s a North Star that enables agents to take on larger, more complex tasks without losing track of intent.

Spec-driven development replaces the chaos of ad hoc, prompt-driven vibe coding with a structured, durable way for programmers to express their goals. It allows developers to be more specific about particular details, and for the agent to communicate its plan ahead of time.

A specification becomes a kind of version-controlled, human-readable super prompt.

## **How Does Spec-Driven Development Work?**

If you simply prompted AI to “implement user permissions,” it might create a standard role-based access control (RBAC) system with admin and user roles. On the surface, the code might look polished and production-ready. But it won’t stop to ask if you need fine-grained permissions, temporary access windows or hooks into an existing identity provider. The generated code looks professional and complete, masking the fact that it solves the wrong problem.

Spec-driven development requires engineers to slow down, think clearly about what they’re building and communicate in a clear and structured way about:

* Specific input/output formats and data types.
* Explicit business rules and edge cases.
* Integration constraints and existing system dependencies.
* Performance requirements and expected scale.
* Error handling and validation rules.
* Security and compliance requirements.

From there, the agents create a task list of things to do to build the code according to the specifications. Engineers can still interact with agents via prompts and steer them.

## **From Developer-Agent Collaboration to Multiplayer Coding**

Building software with AI agents isn’t a solo sport, especially in larger engineering organizations. Modern projects often span multiple repositories, microservices, prompts and specs. Imagine adding a “Share” button to your specs to share expertise across your team and delegate execution.

That’s where [Runbooks](https://runbooks.aviator.co/) come in. A concept we’ve been developing is to turn AI-assisted coding from a single-player activity into a [multiplayer one](https://thenewstack.io/the-future-of-agentic-coding-is-multiplayer/). Runbooks give teams a shared space to collaborate on prompts, align on execution workflows and maintain a clear audit trail of decisions.

Think of Runbooks as the missing link between product specifications and code. A runbook isn’t just documentation, it’s a living knowledge base that others can pick up, extend and adapt. You can build on top of someone else’s Runbook, transfer context across repositories or code paths, draft your own specs and get feedback, or bring stakeholders and coding agents together in a single, structured session.

Try [Runbooks](https://runbooks.aviator.co/) and turn AI coding from individual experiments into team-wide engineering projects.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)