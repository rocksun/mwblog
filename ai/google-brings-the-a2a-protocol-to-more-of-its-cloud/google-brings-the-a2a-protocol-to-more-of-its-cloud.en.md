In early April, Google launched its [Agent2Agent (A2A) protocol](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/), which is meant to help AI agents communicate with each other. Since then, Google [donated the protocol](https://github.com/a2aproject/A2A?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) to the Linux Foundation and at this point, the project has the support of over 150 companies, including the likes of [Amazon](https://aws.amazon.com/?utm_content=inline+mention), Microsoft, [Salesforce](https://www.salesforce.com/?utm_content=inline+mention) and [ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention).

Today, Google is taking its next step in its own A2A journey by adding support for it to many of its own agent-centric and adjacent developer tools and services. This includes adding native A2A support in its Agent Development Kit (ADK) and to Agentspace, its no-code agent builder for the enterprise.

Google is also adding new deployment options, making it easier to deploy A2A agents to Cloud Run or the Google Kubernetes Engine (GKE). Google is also adding support for A2A agents to its [Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/reasoning-engine), the company’s managed runtime for agents.

[![A diagram illustrating the principles of AI agent collaboration and the A2A protocol, showing a Client Agent and a Remote Agent interacting. The process is supported by four pillars: Secure Collaboration, Task and State Management, User Experience Negotiation, and Capability Discovery.](https://cdn.thenewstack.io/media/2025/07/dad234e3-image5_vkag0kd.original.png)](https://cdn.thenewstack.io/media/2025/07/dad234e3-image5_vkag0kd.original.png)

How the A2A protocol works. Image credit: Google.

## A2A Spec Update

In addition to these product updates, the team is also launching the latest version of the A2A spec, which is now up to version number 0.3.

“One of the things we did is we wanted to start with being enterprise-ready when we launched,” [Rao Surapaneni](https://www.linkedin.com/in/raosurapaneni/), Google Cloud’s A2A and Business Platform VP, told me. “Security, identity, monitoring — we baked all of that into the spec. As people started using our A2A SDK, we got feedback that, okay, we need slight tweaks here. We need additional capabilities to apply it for high-performance scenarios.”

For these customers, the spec now includes support for the high-performance [gRPC framework](https://grpc.io/) for connecting services. Surapaneni noted that one of Google’s customers is trialling A2A and the gRPC framework in a mobile scenario with a very large fleet of AI agents.

On the security side, the spec now includes updates around handling unauthenticated and authenticated agents, as well as agents with elevated and delegated privileges.

## Deploying A2A

At this point, many of Google’s customers are quickly moving beyond experimenting with agents and A2A and into production, Surapaneni said. That means they are looking for easier ways to deploy these agents, as well as additional tools for monitoring them in production.

“As customers started deploying into production, they’re looking for options. So we incorporated this into ADK, which is our Agent Development Kit. We made it super easy — like a couple of lines, or even one line with the defaults — to convert an agent into A2A agent. Then once you build it, you want to deploy it somewhere.”

Customers want to have choice, he noted, so they get to choose between the managed Agent Engine, or deploying into a container that is then managed by Cloud Run, Google Cloud’s fully managed serverless platform, or the GKE service for users who want full control over their deployments.

Google is also taking another approach to deployment by bringing A2A agents into Agentspace. Soon, businesses will be able to publish their agents into AgentSpace so that enterprises can use the service to access and manage their home-grown agents as well as third-party agents.

Also, Google is launching an [AI Agent Marketplace](https://console.cloud.google.com/marketplace/browse?filter=category:ai-agent), where Google Cloud customers will be able to discover and purchase agents from ISVs, GSIs and others. Those agents have to run on the Google Cloud Platform, of course, and Google will vet the individual agents.

“Our approach of giving enterprise users the ability to access the right content, right actions and relevant agents all in one surface is received amazingly well,” Surapaneni said.

Once deployed, Google’s Vertex GenAI Evaluation Service, which regularly benchmarks the applications against a set of evaluation criteria set by the developer, can now also test these A2A agents thanks to its newly added support for the protocol.

## A2A and MCP

One thing I do keep hearing in the conversation I have, though, is that there is still some confusion about how A2A and Anthropic’s Model Context Protocol (MCP) relate to each other. Given that Surapaneni was instrumental in creating the A2A protocol. I asked him about how it came to be and how he thinks of the two protocols.

“The insight was that as customers and all these technology vendors build their own agents, you’re suddenly getting into, I would say, world intelligence that they’re providing,” he explained. “But if you look at it from a customer perspective, I’m deploying Salesforce, ServiceNow, Google, and maybe something else. If these agents cannot talk to each other, they can only do what they do, and I cannot leverage them easily. That’s the key insight that led me to think of how I can make these agents talk to each other?”

He also noted that one of the key differences between MCP and A2A is that when you make an MCP call, you are essentially still making an API call using code.

“You’re missing out on the natural language capability and the autonomous intelligence that these agents have,” he said. “So I wanted to bake that into the protocol. So just like a human is typing and chatting with an agent, another agent can do this ambiguous conversation and drive towards a goal. I did not want to lose a semantic exchange that is happening, and I wanted to bring that to the agents.”

MCP, he said, is great for structured data and invoking tools, “but when you want to have a human-to-human, or, in this case, agent-to-agent communication, it is much more nuanced, ambiguous. There’s a back and forth to fill the gaps, right? All of those are baked into the A2A protocol.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)