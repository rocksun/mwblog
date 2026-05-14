Red Hat believes giving users access to agent skills will be AI’s next inflection point.

At the [Red Hat](https://www.redhat.com/en/summit) [Summit](https://www.redhat.com/en/summit) this week in Atlanta, [Red Hat](https://www.redhat.com/en) announced its new [dedicated AI skills repository](https://catalog.redhat.com/en/ai).

Why the focus on skills? In his keynote, [Matt Hicks](https://www.redhat.com/en/about/company/leadership/matt-hicks), Red Hat’s President and CEO, explains that “We have deployed generative AI to every organization in the company. Each organization is looking for ways to either drive more efficiency for themselves or create more value for its customers.

“For example, you might have heard of or used Ask Red Hat, our interactive chatbot. It now runs on our Customer Support Portal. This chatbot has been trained on over two decades of Red Hat support information, knowledge base, and work capabilities.”

> “This chatbot has been trained on over two decades of Red Hat support information, knowledge base, and work capabilities.”  —Red Hat President and CEO Matt Hicks

While based on a [Retrieval-Augmented Generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) approach, it’s not just RAG. By enabling its AI agents to work with its RAG-enriched Large Language Models (LLMs), these agents can reason, plan, and execute against real Red Hat estates, with guardrails that map directly to existing subscription, security, and lifecycle rules.

## Skills over bigger models

So, Red Hat is moving fast to transform today’s AI “copilots” into full‑fledged enterprise superusers. Red Hat’s not doing this by chasing ever‑larger models. That’s not Red Hat’s game.  Instead, by productizing a new layer of *agent skills,* skill packs, and tooling on top of [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift), and [Ansible](https://docs.ansible.com/), you’ll be better able to let AI run your infrastructure for you.

If all this sounds familiar, it should. That’s because last year, [Red Hat LightSpeed brought AI to its programs’ DevOps toolkits](https://thenewstack.io/red-hat-goes-all-in-on-ai-powered-lightspeed-system-admin-tools/). This year, Red Hat is combining that approach with agentic AI. That means you’ll be able to solve problems and carry out complex tasks with limited supervision by orchestrating the tools, data, and services already in the environment. In other words, the goal is to turn generative AI from a chatty assistant into an orchestrator that can perceive, decide, and run end‑to‑end workflows while staying within enterprise policy.

To support that shift, Red Hat has quietly assembled a dedicated agentic skills repository that exposes curated behaviors—skills, in agent‑speak—that encode how an AI agent should use Red Hat’s platforms and knowledge sources. Rather than just giving agents raw access to tools and APIs, these skills bundle task understanding, planning steps, and guardrails into reusable building blocks.

The flagship example is an [**agentic skill**](https://www.redhat.com/en/agentic-skills) [**pack**](https://www.redhat.com/en/agentic-skills) that trains agents to behave like seasoned RHEL subscription admins. By wiring in Common Vulnerabilities and Exposures (CVE) feeds, errata, product lifecycles, and support policies, the pack enables the agent AI to answer questions and propose changes that are both technically accurate and contractually compliant.

> “If models are the brains, these skills are the institutional memory that turns them into true subscription superusers.” —Red Hat

Red Hat pitches it as a way to “connect your coding assistant to live Red Hat data—CVE lookup, patch advisory, product lifecycle, and support guidance,” giving agents the context they need to maximize the value of existing subscriptions. The underlying message: if models are the brains, these skills are the institutional memory that turns them into true subscription superusers.

## RHEL as the agent foundation

How does this work? Something like this:

First, Red Hat is positioning RHEL and [Red Hat’s AI stack](https://thenewstack.io/red-hat-ai-maas/) as the hardened base layer for running these agents in production. In particular, Red Hat recommends people use hardened, image-based RHEL. with controlled execution paths and observability, echoing long‑standing RHEL design principles for critical infrastructure.

If RHEL is the base, OpenShift and OpenShift AI are where those agents scale out. Red Hat AI and OpenShift AI provide model hosting, distributed inference, and integration with [Llama Stack](https://www.redhat.com/en/blog/generative-ai-applications-llama-stack-notebook-guided-journey-intelligent-operations-agent) and [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) so that agents can discover tools, skills, and data sources in a standardized way. In other words, OpenShift AI serves as a control plane for model endpoints, agent runtimes, and skill registries, with Kubernetes providing the usual knobs for isolation, scaling, and multi‑tenancy.

## Ansible bridges intent to action

Finally, Red Hat is explicitly making Ansible the execution engine for agent decisions. In interviews and partner briefings, Red Hat executives describe [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) as the trusted bridge between agentic intent and real changes on production systems.

## Governance built in from the start

To protect this new agentic stack from trouble, Red Hat emphasizes robust security and governance. Specifically, skills are treated as high‑value artifacts that encode not just access to tools. Still, the behaviors agents will exhibit pose new classes of risk related to misuse, privilege escalation, and data exposure.

Don’t worry about AI taking away sysadmin and DevOps jobs, well, not quite yet anyway. After all, Hicks adds, “we’ve had plenty of successes, but have also had plenty of failures, and that’s easy to do when the technology is changing practically weekly now. But those lessons are being actively fed back into the platforms we provide to you, with the belief that we can be the right foundation for your journey. It’s not just a market position; it’s what we are actually doing. Now, about a year ago, we moved from building chatbots to building AI agents. Specifically, we wanted to build an agentic system that could go through a massive body of internal knowledge and return something genuinely useful, not a summary, but an actual answer.”

That said, Red Hat’s developer guidance stresses the need for identity, scoped permissions, and human‑in‑the‑loop checkpoints when deploying agents that use skills in production. Additionally, observability and policy enforcement should be treated as first‑class features of any agent deployment.

> “You are not getting replaced by AI, but where you spend your time and energy will drastically change—figuring out how to build and shape evaluations for these AI-created systems.” —Matt Hicks

Hicks sums up, “This is fundamentally changing how we operate at Red Hat, and our learnings go directly back into the platforms that we provide for you all. And I want to be direct on this, to these software developers in the room. You are not getting replaced by AI, but where you spend your time and energy will drastically change—figuring out how to build and shape evaluations for these AI-created systems.

All of this fits into a broader Red Hat narrative that the real “next inflection point” for AI isn’t another bump in parameter counts, but the operationalization of agents that can safely touch production systems. With its agentic skills repository, subscription‑aware skill packs, and a stack that runs from metal to agents, Red Hat is betting that its value lies in turning today’s copilots into governed superusers that understand both the technology and the support contracts underneath.

In short, for enterprises already standardized on RHEL, OpenShift, and Ansible, the message is clear: The tools you use to run your infrastructure today are being retooled to run your agents tomorrow.

As someone who cut his tech teeth on writing Borne and C shell scripts–Bash was still in the future–I’m feeling a little uneasy about this. But let’s face it. I managed at most a handful of servers. Today, system administrators oversee hundreds of server instances and more containers than you can shake a stick at. Red Hat-style, AI-enabled DevOps is the future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)