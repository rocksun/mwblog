Whether you love it or hate it, by now most software developers have tried out some version of AI-coding tools. However, once we look beyond the vanity metrics of daily or weekly AI-tools usage, the adoption in enterprise is all over the place.

There are developers who swear by it and report 10x productivity (except when they run out of token usage), and there are those skeptical of whether this even adds any value or just increases the tech debt.

The truth is, both of these behaviors can be experienced at the same company.

## **Problems With Enterprise AI Adoption**

There are a few problems with the current approach of AI adoption in enterprises:

1. **Lack of context:** Working in large, messy code bases of enterprises is far from “[vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/).” No matter how good the models get or how well we design the next coding agent, we cannot make progress without providing correct and complete context to the [large language model (LLM) agents](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/).
2. **Learning curve**: Using coding agents effectively requires at least certain training that most organizations don’t provide today. This leads to varying usage and success with these tools. Some developers who have tried and tested various approaches now have their handy cookbooks on how to get the best out of these tools, while others are still dipping their toes with limited success.
3. **Tribal knowledge**: Enterprises are not built overnight. People come and go, sending a lot of tribal knowledge out the door regularly. When we think about context, we always think of docs and specifications of what and how. A lot of tribal knowledge revolves around the “why.” The evolution of an organization involves thousands of micro-decisions made every day, forming the decision trees that are reflected in the code. Understanding why the product is built in such a way is just as important as how it’s built. This information may sometimes not even be captured in the product specs.

## **Remote Agentic Environments**

Recently, I talked about the rise of [AI-coding environments](https://thenewstack.io/the-rise-of-remote-agentic-environments/) that code autonomously. These coding agents can take instructions from the developers and execute them with little hand-holding. This means that, unlike the coding agents tied to your IDE, these can scale exponentially, performing hundreds of parallel operations, only limited by the amount of work that can be assigned to them, and of course, the LLM budgets of your organization.

However, this is just the infrastructure side of the equation. The problems of the lack of context, lost tribal knowledge and varying levels of engineers’ familiarity with AI remain.

Ultimately, the engineers who know how to work well with the IDE-based agents would get value out of this, but remote agents themselves don’t solve the real enterprise problem: lack of developer-AI collaboration.

## **Spec-Driven Development**

Spec-driven development represents perhaps the most significant paradigm shift from traditional “vibe coding” to structured, specification-first AI development. This approach treats specifications as “super prompts”: Version-controlled, human-readable documents that serve as comprehensive context for AI agents. Think of these documents as detailed product specs that act as a contract between humans and AI agents that cover business context, edge cases with clear guidance of how to navigate the code.

With that in mind, specs become more critical and binding than the code. If that’s the case, it’s time we treat these specs as first-class citizens.

## **Stop Reinventing Prompts**

I also wrote about the [value of code reviews](https://www.aviator.co/blog/the-anatomy-of-slow-code-reviews/). More than finding bugs, code reviews help with knowledge sharing. This is how tribal knowledge gets pushed out from one person to another. I’m also a big fan of occasional pair programming as an alternative that helps align ideas quickly. However, if we look at our patterns of AI-coding, we do everything the opposite way:

We work on the prompts in our IDEs, provide feedback to the coding agents back and forth, generate the code, submit the code for review and then throw away the prompts.

These prompts are the context, these prompts are the tribal knowledge. It’s time we start preserving these prompts.

## **Multiplayer Remote Agentic Environments**

This is where the concept of runbooks comes in. [Runbooks for agentic AI](https://runbooks.aviator.co/) are a way to save the context, collaborate on prompts, share execution workflows and maintain audit trails and pre-configured remote agentic environments.

The real power of runbooks shows when more than one engineer is involved. Building software with AI agents isn’t a solo sport, especially when projects touch multiple repos, services and prompt engineering knowledge.

Runbooks let teams switch from single-player to multiplayer mode to:

* Collaborate on prompts
* Share execution workflows
* Maintain audit trails

These runbooks bridge the gap between product specs and the code:

* You can take someone’s runbook and build on top of it.
* Apply context from one code path or repository to another.
* Create your own specs and get feedback from the team.
* Collaborate with all stakeholders in a single session with the coding agents.

## **Version Controlled**

Reusable Runbooks capture the team’s AI prompting knowledge and execution patterns that evolve. If these are living, breathing documents, it’s important to maintain versioning.

There are several benefits:

* Understand how the specs evolved.
* Track any code change to the exact version of the runbook.
* Let others fork the runbooks to create their custom versions and contribute back.
* Roll back changes when AI goes wrong (and it will go wrong).

Specs are the new code. Once we learn to collaborate on the specs the way we have learned to collaborate on the code in the last few decades, we will be able to fully use the power of AI agentic tools. Try [Runbooks](https://runbooks.aviator.co/) and turn AI coding from individual experiments into team-wide engineering projects.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/d5d9b6e2-cropped-c9449920-ankit-jain-profile-photo-linkedin.jpeg)

Ankit Jain is a cofounder and CEO of Aviator, an AI-powered, low-config developer portal that automates ownership, code reviews, merges and deploys. He also leads The Hangar, a community of senior DevOps and senior software engineers focused on developer experience,...

Read more from Ankit Jain](https://thenewstack.io/author/ankitjain/)