# Why Infrastructure Must Be Serverless in the AI Age
![Featued image for: Why Infrastructure Must Be Serverless in the AI Age](https://cdn.thenewstack.io/media/2024/11/8699427a-arian-darvishi-wh-rpfr_3_m-unsplash-1024x682.jpg)
[Arian Darvishi](https://unsplash.com/@arianismmm?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/person-using-laptops-wh-RPfR_3_M?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
[Replit’s new AI agent](https://blog.replit.com/introducing-replit-agent) will write your code, then configure, provision, build, and deploy that code *in seconds*. You can go from natural language description to implemented, working application before VS Code has loaded all your extensions.
If an AI agent can build and deploy an app in seconds, minutes are too long to spin up the resources. If an AI agent can spin up and spin down thousands of these apps each hour, $10 per database becomes an extreme overhead. Suddenly, we’ve gone from a team of developers deploying a single app to a single developer deploying a team of apps, all working under the direction of AI agents.

This approach changes the perspective on development and demands a new view of infrastructure. Traditional infrastructure is too slow, too permanent, and too complex for agentic workflows. The future of infrastructure demands instantaneous, serverless, and simplified tooling — this is what must be built.

## The Core Needs of AI Agent Infrastructure
AI agents operate at a scale and speed that makes traditional infrastructure management technically and economically impractical. A good “Agentic Experience” will emphasize three core features.

-
### Simplicity
Any [code and integration will need](https://thenewstack.io/why-infrastructure-as-code-needs-cloud-asset-management/) to be simple. This world will be built on straightforward API calls rather than IAM policies and multistep provisioning. Consider starting a new RDS instance: a VPC, security groups, rules, subnet groups, and IAM roles. Each step requires multiple API calls, deliberation of options, and troubleshooting.

A [human DevOps engineer](https://thenewstack.io/ai-coding-human-engineers-are-more-important-than-ever/) understands these dependencies and can debug issues when they arise. An AI agent needs everything to work perfectly the first time and every time. This complexity isn’t just a barrier to entry; it’s a barrier to automation. This is what starting a database on Neon requires:

![](https://cdn.thenewstack.io/media/2024/11/6a2bcdf0-unnamed.png)
Code example from [@neondatabase/toolkit](https://github.com/neondatabase/toolkit) SDK

Three lines of code to provision a database, one API call, and immediate availability. This isn’t just better DevEx — it’s the only way to make infrastructure accessible to AI agents. This simplicity also helps with two factors:

**Cost:**More steps = more cost. Every API call an agent makes consumes tokens, and[complex infrastructure operations](https://thenewstack.io/codiac-kubernetes-doesnt-need-to-be-that-complex/)can require dozens of calls. Simple APIs are more than just more straightforward to use; they’re fundamentally more economical at scale.**Security**: Though the AWS RDS setup is highly secure, you can’t give away your root keys to a machine. Modern infrastructure needs to be sandboxed and self-contained, with clear boundaries that let agents experiment freely without risking production systems.
-
**Immediacy**
The above code can spin up a new database in under a second, ready for use by an agent.

Traditional infrastructure timelines simply need to be revised in an agent-driven world. Code creation speed used to be the rate-limiting factor in development, but when an AWS RDS instance takes 10 minutes to provision, that infrastructure becomes that rate-limiting factor.

Moving to an immediacy model opens up what is possible just as much as AI does. The core principle of agent-driven development is disposability. An agent might create an application, test it, and discard it within minutes. Infrastructure needs to match this lifecycle — spinning up instantly when needed and disappearing just as quickly when it’s not. An agent should be able to build and destroy a disposable app in the [time it takes a traditional database](https://thenewstack.io/columnar-storage-a-developers-key-to-real-time-analytics/) to spin up.

-
### Ephemerality
This also leads to the critical component of disposable apps — ephemerality. A traditional approach presumes an app is permanent, so it needs permanent infrastructure.

Not so. Look at how developers already use Vercel’s [v0](https://v0.dev/), a dev tool for generating apps from text prompts. Instead of searching for a “mortgage calculator” online, you can instead ask [v0](https://v0.dev/chat/ObNYNZmQCoJ?b=b_rOkttQVXY8h) to create one for you:

This works. It needs no infra, but that’s a likely next step. Most importantly, a user can build a massive amount in a single session with AI. The vast majority will be discarded and never used again, but some might be shared and turned into long-lived applications. This is the future of tooling — you use AI and AI agents to build precisely what you want, with a trail of abandoned alternates in its wake.

This demands an infrastructure that can scale to zero. When a resource isn’t being used, its cost should drop to zero. With this capability, the economics of disposable apps will work. Consider a company spinning up dozens of databases per hour in the process of building with AI. Who is going to delete the unused ones? Who is even going to decide which are unused?

When infrastructure can genuinely scale to zero, it enables new development patterns. Agents can freely experiment with different approaches, testing multiple solutions in parallel without worrying about cleanup or ongoing costs. This removes economic constraints from the development process — you no longer need to carefully consider the cost implications of each new database or service.

The result is a development environment where resources are truly disposable. Create what you need, use it for as long as you need it, and let it disappear when you’re done. This isn’t just more efficient — it’s the only way to make agent-driven development economically viable at scale.

## Simpler, Faster, Cheaper — Pick Three
In six months, we’ve gone from a demo of [Cognition AI’s Devin AI programmer](https://www.cognition.ai/blog/introducing-devin) to Replit’s AI developer/DevOps agents working in the wild. What will SOTA be like this time next year?

Nobody knows, but it’s clear what kind of infrastructure will get us there. That infrastructure must move from the human developer to the AI agent as a builder. But creating good AgentEx will also make us build good DevEx, as simpler, faster, and cheaper will also work for the humans in the loop. This virtuous cycle — where improvements for AI agents create better tools for humans, and vice versa — will accelerate the transformation of how [developers build and deploy software](https://thenewstack.io/go-big-or-go-home-what-github-learned-building-copilot/).

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.
*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)