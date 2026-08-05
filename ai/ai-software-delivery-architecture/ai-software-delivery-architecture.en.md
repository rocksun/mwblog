For the past two years, most of the conversations about AI and software development have centered on security: How do you ensure AI-generated code is secure? How do you prevent intellectual property from leaving the boundaries of your organization? How do you govern prompts, models, and data access?

These are important questions, but they are *not* the questions that will determine whether AI initiatives succeed or fail.

Organizations are discovering that AI is not just another developer productivity tool. It is an entirely new architectural layer within software delivery. When AI moves to production, the biggest risks are shifting from model outputs to system design.

> “When AI moves to production, the biggest risks are shifting from model outputs to system design.”

In other words, AI won’t break your SDLC, but poor AI architecture very well could.

## We are repeating the early cloud adoption cycle

Anyone who worked through the first decade of cloud adoption has seen this movie before.

Everyone felt the pressure to move to the cloud as quickly as possible…and then the bills came. Costs ballooned, governance became increasingly complex, and workload portability became difficult. Some organizations responded by repatriating workloads or adopting hybrid cloud strategies to regain flexibility and control.

We’re seeing something similar play out with AI as some organizations are finding out the hard way what happens when AI usage expands from a handful of developers experimenting with agents to an enterprise-wide software delivery strategy. Every prompt for code generation, test creation, documentation updates, and validation activities consumes LLM inference and compute resources. As adoption scales, so do the associated costs, governance requirements, and operational complexity.

As more organizations move AI to production environments, there is growing consensus that AI must not simply be consumed as a service, but governed as a system with greater visibility and oversight.

## The future isn’t one model; it’s an AI supply chain

Software delivery is not a single activity. It is a collection of specialized activities that span planning, coding, testing, validation, deployment, governance, compliance, and operations. Expecting one model to perform all of those functions efficiently is similar to expecting one service or one platform to manage an entire software stack.

Instead, [AI-native software delivery](https://thenewstack.io/building-ai-native-systems/) will look like a supply chain.

Imagine a future development workflow where different AI systems are responsible for distinct stages of delivery:

* A planning model helps define requirements and generate user stories.
* A coding model generates implementation logic.
* A testing model creates unit and integration tests.
* A validation agent reviews outputs against requirements.
* Compliance agents ensure policies and regulatory controls are met.
* Governance systems monitor activity, costs, and model performance across the pipeline.

In this world, software delivery becomes an orchestrated network of AI capabilities rather than a dependency on a single model.

This shift is already visible in the broader conversation around agentic systems. However, discussions about agents often focus on what they can do rather than where they fit within software delivery and how organizations should govern them.

## Why small models may do more work than frontier models

Large frontier models like Claude, Gemini, and GPT-5 can reason across domains, synthesize complex information, generate detailed plans, and tackle a wide range of tasks. But that doesn’t necessarily mean they are the best tool for every job in the software development lifecycle. In fact, most of the SDLC doesn’t require frontier intelligence.

*Star Wars* actually offers a useful analogy here — C-3PO and R2-D2 are both intelligent machines, but they serve very different purposes.

[Frontier models](https://thenewstack.io/open-weight-models-frontier-costs/) are the C-3POs of AI — highly capable generalists that can support a wide variety of tasks, but also resource-intensive and expensive to operate at scale. Most software delivery tasks, however, need an R2-D2: a specialized system optimized for a specific job. Software delivery doesn’t need one brilliant assistant. It needs a team of specialists.

> “Software delivery doesn’t need one brilliant assistant. It needs a team of specialists.”

Organizations that rely on a single frontier model for every SDLC task will spend more, scale less efficiently, and have less control than those using specialized AI systems. Alternatively, a collection of specialized “R2-D2” models and agents could be optimized for tasks:

* A model focused solely on generating unit tests.
* A model optimized for code review.
* A model responsible for build validation.
* A model dedicated to compliance checks.
* A model trained to evaluate whether requirements have been met.

Many of these tasks don’t require the broad reasoning capabilities of a frontier model. They require consistency, speed, and specialization.

This doesn’t mean frontier models disappear. A large model might be used at the beginning of a workflow to help define requirements, map business objectives, or create an implementation plan. It might also be used at the end of the pipeline as an “AI judge” to assess outputs, validate quality, or verify compliance against organizational policies.

But much of the work in-between may increasingly be handled by smaller, specialized models that are cheaper to run, easier to fine-tune, and more predictable in their outputs.

## AI control plans and orchestration bring governance into the pipeline

Historically, software teams have often treated [governance and compliance](https://thenewstack.io/okta-ai-agents-fedramp/) as downstream activities. Developers write code. Security teams review it. Auditors validate it. Compliance teams verify requirements after the fact.

However, when software is being generated, modified, tested, and validated by multiple AI systems, governance can no longer be a separate workflow. It must become an integrated capability embedded within the delivery lifecycle itself so organizations can easily track:

* Where AI is being used
* Which models are making decisions
* How outputs are validated
* Whether organizational policies are being followed
* How costs are being tracked and optimized
* How compliance requirements are being enforced

Essentially, as AI becomes part of software delivery infrastructure, governance can no longer be bolted on afterward. It must be designed into the system from the beginning.

> “As AI becomes part of software delivery infrastructure, governance can no longer be bolted on afterward. It must be designed into the system from the beginning.”

As AI becomes embedded into every stage of software delivery, development teams will need a way to coordinate models, agents, policies, compliance requirements, testing workflows, and cost controls across an increasingly complex ecosystem. That’s why we’re beginning to see the emergence of AI control planes and orchestration layers that help organizations govern AI interactions, manage token consumption, and maintain trust across the AI-driven development lifecycle.

## What’s next

Across the industry, we are seeing growing demand for:

* Reference implementations that show how frontier models, open source models, agents, data platforms, and governance frameworks fit together.
* Training to help DevOps teams understand how software delivery changes in an AI-native world and how to manage new workflows.
* FinOps tooling to give visibility into AI usage and operational costs so leaders can make informed decisions.

Together, these capabilities provide something many organizations still lack: a practical blueprint for adopting AI in a way that is scalable, governable, and economically sustainable.

This is why the role of experienced technology partners is becoming more important, not less. What organizations really need right now is a strategy for integrating AI into software delivery without creating new forms of technical debt, governance gaps, or runaway costs.

Ultimately, the competitive advantage will come not from any one AI model, but from having the right-sized architecture—and the right partners—to put all the pieces together.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/08/b3f18882-jeffmichael.png)

Jeff Michael is a Senior Director of Product Management at Perforce Software, where he is responsible for Perforce's Development Tools portfolio, including OpenLogic and Zend. He has over 25 years of software delivery experience with a focus on OSS management,...

Read more from Jeff Michael](https://thenewstack.io/author/jeff-michael/)