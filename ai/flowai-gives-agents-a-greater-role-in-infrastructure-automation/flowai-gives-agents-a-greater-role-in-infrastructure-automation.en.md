The future of infrastructure management will include using reasoning-based agents to take over a greater portion of the deterministic layer in their stack, according to network and infrastructure orchestration vendor [Itential](https://www.itential.com/).

To that end, it has opened a customer preview of [FlowAI](https://www.itential.com/resource/white-papers/architecting-hybrid-ai-for-infrastructure-operations/), which allows customers to build AI agents that can reason, plan and orchestrate. Used together with its Model Context Protocol (MCP) server to ensure strict validation, auditability and control, it can provide a unified model to adopt AI safely, predictably and at scale, according to the company.

It recently [unveiled FlowAI](https://www.itential.com/resource/demo/building-and-running-your-first-flowagent-in-the-itential-platform-with-flowai/) at AutoCon 4 in Austin, Texas.

“When people deal with infrastructure, if you do a lot of infrastructure as code-type of discussions, you know a pipeline is very deterministic. It says these 12 things are going to happen in this exact order,” explained Chris Wade, Itential CEO.

“And what we’re saying is that AI is going to provide a reasoning layer on top. So the combination of non-deterministic reasoning with deterministic, we think, is going to be kind of the Goldilocks situation of balancing all these things. … If I write a lot of deterministic logic in a pipeline, if I want to change that pipeline in any small way, I have to go modify it, test it and push it to production.

“But if I take that deterministic layer and look at it more like a set of recipes, where I give it small, deterministic flows and let the AI reason through the process, then I’m going to have a much more flexible operating model where I can basically handle more variety. I can have less technical debt as I as I start to introduce AI in our platform.

“So we’re thinking of putting AI reasoning very high in the architecture, so that it can kind of augment what humans do today. They’re looking at an outage or they’re provisioning something, they want to check this, they want to check that … those [reasoning models](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/) are very, very good at doing that, is what we found.”

[FlowAgent Builder](https://www.itential.com/resource/white-papers/architecting-hybrid-ai-for-infrastructure-operations/) provides the tools, models, and integrations that allow users to define agent personas, attach [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) for reasoning, assign tool access and embed guardrails that shape how agents operate. The [agents then can](https://www.itential.com/blog/company/ai-networking/itential-flowai-the-new-operating-model-for-infrastructure/) access existing automations and data models on the platform, giving them insight into customer network, cloud and security systems.

[FlowMCP](https://www.itential.com/blog/itential-mcp-where-conversational-ai-meets-enterprise-automation/) serves as the controlled interface between all agents and infrastructure, enforcing strict schemas, policies, permissions and audit rules, while the Itential platform actually executes any actions.

“If we’re modifying infrastructure, you might have a situation where maybe the command failed, or maybe the device was busy, or stuff like that. So in the deterministic layer, you used to have to hard-code all that stuff. You would have to say, ‘If this happens, try again. If this happens, try again. Wait 10 seconds, wait a minute.’ That’s the stuff that we think is going to be very beneficial to have in that reasoning layer,” Wade said.

“So the macro story, I think, industrywide, is trying to find out, how do we balance reasoning and deterministic layers, or [managing infrastructure](https://thenewstack.io/how-to-use-ai-to-design-intelligent-adaptable-infrastructure/). And obviously, our strong opinion is that we need to take those deterministic layers and break them into small components and then let the AI reasoning work its way through it.”

Itential expects customers to build these agents and decide which assets they will be exposed to.

They might be templates, pre-checks, post-checks, workflows that update Slack or update [ServiceNow](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/), a ticket creation agent.

“So the customers have full control over the scope and what that agent can do, and they can feel confident that that agent’s not going to go do whatever it wants. It’s only going to do the things that the Itential platform exposed to that agent. So if I say all you can do is do a read command on infrastructure and open a ticket, then that’s all that agent can do. And then a customer will have a whole set of agents that can work independently and then can be exposed within their organization,” Wade said.

[Scott Raynovich](https://www.linkedin.com/in/scott-raynovich-9a40784/), chief analyst at Futuriom Research, said of the offering*, “*As enterprises work to understand how to safely adopt agentic orchestration and automation, Itential’s FlowAI delivers not only a development platform with tools that accelerate the process, but also the guardrails and governance needed to adopt agentic automation with confidence.”

[Join the private preview here](https://www.itential.com/flowai/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)