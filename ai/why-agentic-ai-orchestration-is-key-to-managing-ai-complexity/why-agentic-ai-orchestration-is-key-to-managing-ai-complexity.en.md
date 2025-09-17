Over the last four years, [Orkes](https://orkes.io/?utm_content=inline+mention) has gained popularity for its ability to integrate data and microservices orchestration within a single platform. But its newer role — as a proper agentic AI to orchestrate enormously complex AI workflows — might be bringing Orkes to the forefront of the AI boom.

According to the company’s founders, agentic AI-based orchestration is an essential component of all things AI, from the AI models Anthropic creates to the custom [large language models (LLMs)](https://thenewstack.io/introduction-to-llms) that organizations are building.

“If you want to build agents, the agents need to orchestrate long-running workflows. These workflows need to maintain state,” [Viren Baraiya,](https://www.linkedin.com/in/virenb) Orkes’ co-founder and CTO, told me. “And the moment you go beyond proof of concept, you also have to run them at scale. This is where pretty much every framework struggles.”

## From Netflix Conductor To AI Agent Orchestration

Orkes was founded in 2021 by Baraiya, [Dilip Lukose](https://www.linkedin.com/in/diliplukose/) and [Jeu George](https://www.google.com/url?q=https://www.linkedin.com/in/jeugeorge/&sa=D&source=docs&ust=1757530028814278&usg=AOvVaw3ruxKxKtC7qqI54xo1Vbdl) — the co-creators of the open source Netflix Conductor — to provide enterprise support and features for Netflix’s open source workflow orchestration platform.

Under Netflix’s creation and control, [Conductor flourished](https://thenewstack.io/orkes-to-maintain-conductor-project-as-netflix-steps-back/) into a wildly successful and popular way to orchestrate the automation of workflows by integrating data and various automation stacks. The most important components involved the integration of data services and microservices. This helped operations teams consolidate two management steps into one, which contributed to Orkes’ popularity.

Since then, [the project](https://conductor-oss.org/) has evolved to unify data and microservices orchestration under a much more integrated and robust framework. This is not just another so-called “single pane of glass,” as both orchestration domains represent and automate management and remediation, as I’ll explore further below.

That’s where Orkes began. And then [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers) orchestration entered the fray.

## State Management in Agentic AI Systems

The integration of LLMs for data orchestration has become a key part of modern workflow orchestration platforms. In 2023, Orkes integrated LLM orchestration into its data and microservices orchestration platform. This essentially made Orkes Conductor Enterprise a precursor of the AI boom by enabling complex stateful workflows to be managed across diverse AI and related services components. Orkes’ work laid the foundational architecture for long-running, reliable and debuggable AI agent workflows — core to what later became known as agentic AI systems, Baraiya said.

Unlike most frameworks, Orkes doesn’t struggle to maintain state in long-running workflows as they scale, he explained. “Scale is in the DNA in our platform; no need to think about it, it’s a by-product of whatever is done.”

[![Orkes AI agentic orchestrator handles security, scalability, observability and auditability](https://cdn.thenewstack.io/media/2025/09/a33f1fa9-orkes-architecture.png)](https://cdn.thenewstack.io/media/2025/09/a33f1fa9-orkes-architecture.png)

Source: Orkes.

Having a proper AI agentic orchestrator is necessary for building any agent. “An agent essentially is the sum of knowledge, tools and a language model as a controller. Orchestration happens across these components,” Baraiya said. “To run an agent, distributed state management is needed. A notion of workflow is needed, because control loops and everything must be coordinated. The ability to debug and see exactly what is going on is also needed.”

Model providers like OpenAI, Gemini and Anthropic offer a fantastic foundation, and the workflow engine also remains critical, Baraiya said. “Without a workflow engine, operating an agent in production is impossible,” Baraiya said. “That is the fit — to be the platform for running agents. That is how those agents can be run.”

## Human-in-the-Loop: Building Trust in AI

A proper AI agentic orchestrator must be able to reliably manage long-running workflows at scale. But, more importantly, it must have the organization’s trust, which means keeping [humans in the loop](https://orkes.io/blog/operators-loops-waits-human-tasks/). In Orkes’ case, observability is provided through a dashboard, so performance metrics relating to workflows can be monitored in real time by humans.

“Keeping humans in the loop is now a very strong sentiment around AI implementations. It blends nicely into this idea of maintaining trust, or building trust with more stringent use cases — situations where relying on the LLM or the brain to give sound advice is not possible,” Baraiya said. “The task needs to be upleveled to a human to step in and do the workflow execution. That is something that is being done strongly with native implementations around human-in-the-loop workflows.”

> “Without a workflow engine, operating an agent in production is impossible. That is the fit — to be the platform for running agents. That is how those agents can be run.”

However, the moment a human is added to the loop, things slow down. But state has to be maintained for however long it takes for that person to respond, Baraiya explained. “A good example would be that an agent tries to make a decision but needs confirmation from the user. While a typical program might complete a task in seconds, the moment a human is added, those seconds go into minutes, hours or days, depending on the situation,” Baraiya said. This creates concerns around maintaining state in long-running jobs.

In practice, he said, “adding humans in the loop … is really hard because of maintaining long-running states, incorporating the feedback loop and then building the entire system around it. What was supposed to be simple suddenly becomes a long project.”

As an enabler of AI-controlled automation, Orkes Conductor integrates workflows with LLMs (such as Claude, OpenAI GPT-4 and Google Vertex AI) and [vector databases](https://thenewstack.io/top-vector-database-solutions-for-your-ai-project/). Its AI orchestration capability supports “agentic” workflows: AI agents execute tasks but include human checkpoints for oversight. “This ensures workflows adapt dynamically with AI, keeping humans involved for compliance and governance as automation moves toward autonomy,” according to a recent [Orkes blog post](https://orkes.io/blog/scaling-complex-agentic-workflows/).

## Building Trust Through Observable AI Workflow Automation

[Gartner describes](https://www.gartner.com/doc/reprints?id=1-2LGK9A81&ct=250715&st=sb&utm_campaign=18097788-WEB-CC-304-EN-Gartner-Hype-Cycle-for-Enterprise-Process-Automation-07-2025&utm_medium=email&_hsenc=p2ANqtz--G2vjzhuiOECiiS0YJBnQmsmY2TjZ-BsnUH7R_scd9McmUzblgT9B53Grl26mDjoqxzaJHTDzQ_i3QNOV3QlNC2JzrDA&_hsmi=373295109&utm_content=373295109&utm_source=hs_automation) the business impact of enterprise process orchestration tools as a way to automate workflows, identify errors and system disruptions, and accelerate integration in workflows. These tools also support adaptation to evolving backend architecture and digital requirements. Gartner includes Orkes in this category.

Today, at the juncture of DevOps and IT, agentic AI orchestration tools are in critical demand for process orchestration. These tools help companies manage AI complexity, particularly those developing LLMs, AI applications and related systems.

Orkes Conductor is designed to handle agentic AI orchestration and, by providing transparency and allowing human oversight in critical decision-making processes, it is an essential element for building trust in AI, Orkes’ founders say.

“Orchestration remains the essential component that binds it all,” Baraiya said. “Unifying automation silos in IT systems remains highly relevant, and the orchestration piece has now evolved into a distinct category. That is the core contribution of Orkes, and this orchestration for AI agents has become essential for managing AI processes.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)