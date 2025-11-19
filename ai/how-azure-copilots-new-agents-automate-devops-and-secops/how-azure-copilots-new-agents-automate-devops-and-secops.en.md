There are over 200 different services available on Azure, with thousands of resource types. At the Ignite conference this week, most of them will be getting new features. [Copilot in Azure](https://learn.microsoft.com/en-us/azure/copilot/capabilities) can already help you get resource information, write scripts, review your cloud bill, and step through basic troubleshooting — but it’s been fairly limited.

Now Microsoft is updating it with a new name, [Azure Copilot](https://www.aka.ms/azurecopilot/agents), and adding six agents — for migration, deployment, optimization, observability, resiliency and troubleshooting — that cover the whole cloud management lifecycle, says [Annie Pearl](https://www.linkedin.com/in/anniepearl/), CVP and GM of Azure Experiences and Ecosystems (including the Azure portal, CLI and Copilot).

“The big technical enhancement is an orchestrator that takes in the natural language and figures out what agent or what multiple agents to call based on the task,” Pearl told The New Stack in an interview. “With Azure Copilot you go from manual workflows to, hey, let me work with an agent to optimize my VM or help me troubleshoot an issue or investigate an alert, or ensure that I’m multi-zone or resilient on all of my most important workloads.”

You’re not just getting a text reply in chat: the new interface looks like the kind of formatted dashboard information and insights you’re used to in the Azure portal, but with custom recommendations for what you’re focusing on — so you don’t have to click through the hierarchy of everything in your tenant.

With so much to do, many admins don’t have the time to check if every workload is provisioned as efficiently or implemented as effectively as it could be, when it’s already running and not causing issues. Instead of waiting till you’ve already noticed a problem, or have gotten a more expensive cloud bill than you were expecting, or heard about a new service and want to understand if it’s useful, agents make proactive suggestions, write scripts and (if you agree) take actions for you.

> “The deployment agent, for example: not only is it trained on the Azure Well Architected Framework and best practices, but it will ask me questions about different trade-offs I might need to be making when I’m deploying.”  
> **– Annie Pearl, CVP for Azure experiences, Microsoft**

“Rather than having to go browse the Learn documentation [for a feature], come back, create my own Bicep template or Terraform file, go pull some API endpoints [to paste in], now the agent can do all that for me,” Pearl explained. “I can give it a task. I can have some back and forth. The deployment agent, for example, not only is it trained on the Azure [Well Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) and best practices, but it will ask me questions about different trade-offs I might need to be making when I’m deploying. It can create the Infrastructure as Code, and then I can — either automatically or with a human in the loop — push it to GitHub.”

If you’re troubleshooting a timeout connecting to an API and the agent suggests changing network access settings, it will give you an Azure CLI command that you can copy and run, but also the option to have the agent go make the changes for you — showing you in advance what it’s going to change.

That explainability is fundamental, argues [Bola Rotibi](https://www.linkedin.com/in/bola-rotibi-a7533226a), Chief of Enterprise Research at CCS Insight. “People don’t want a black box. Yes, I want you to automate it, but I need you to explain to me what you have done, so I can see [if] you’ve done this correctly, how I’m expecting it, and so I know whether it’s right or not.”

She’d like to see that go further, perhaps with the option to have the most important or wide-ranging changes sent to someone else for approval, so that the chain of command is obvious if there turn out to be problems later.

## A New Ops Dashboard

You can use the new interface in the portal (either as a full-screen immersive chat or a sidebar) and in Azure CLI, with some relevant actions available in GitHub Copilot as well; plus a new unified Operations Center dashboard for Azure. In addition to “bringing together a lot of disparate management experiences,” the dashboard puts the new agents right into the different workflows where ops teams need them.

That makes it more useful for the productivity gains that organizations are looking to agentic AI for, [according to IDC](https://www.idc.com/resource-center/futurescape).

“Previously, you could ask Copilot to summarize your costs, but now the optimization agent can proactively suggest cost savings, generate a ready-to-use PowerShell or CLI script, and rightsize your VM or change your VM SKU”, Rotibi explained.

This includes clarifying trade-offs like cost and performance: “It will highlight cost and sustainability actions and compare financial performance and carbon impact, then come up with a recommendation for how you can reduce your cost, improve sustainability impact, as well as maintain or improve performance. It will explain why these suggestions [work] and compare alternatives; and you can have a back-and-forth conversation like ‘I want to add in this variable, I want to remove that variable’ and then it will generate the scripts to go implement them.”

Sometimes the details of how that would change your Azure bill will be fairly broad — like adding resilience, having a medium impact — but suggested changes to VMs will give you the specific dollar and CO2 emissions savings, or a graph of how utilization is expected to change and whether the changes might affect performance.

The observability agent will proactively show alerts about concerning metrics (something a dashboard can already do), but also run investigations in the background to gather details, so that you can drill in.

“It’ll do service-specific telemetry and observability data,” said Rotibi, “looking at things like metrics and traces and logs, and gathering health signals from Azure Monitor and diagnostic tools.”

## Overworked Ops

Developers have had access to coding agents for several years now and [GitHub Copilot and VS Code already connect to the Azure MCP Server](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started/tools/visual-studio-code?tabs=one-click), but agents are becoming popular for ops teams, who are typically overstretched.

Cloud hasn’t necessarily made that better, Microsoft’s Pearl admits. “Today they’re manually pushing through a bunch of different dashboards and all these fragmented tools; cloud complexity has caused more challenges and put more pressure on these roles.”

Rotibi agrees. “When we speak to organizations [about] cloud, it always surprises me how much people are still stuck in the weeds and that they’re trying to figure out things,” she said. Cloud is just one of the laundry list of things they have to deal with alongside security, identity, AI, government strategy, regulation, and the demands of their own industry and vertical sector.

> “Organization teams have got left holding the integration baby and they’re tired of it, because it’s becoming even more complex.”  
> **– Bola Rotibi, Chief of Enterprise Research at CCS Insight**

“Organization teams have got left holding the integration baby and they’re tired of it, because it’s becoming even more complex,” Rotibi noted.

Although she cautions it’s “a little bit too glib” to think agents will fix all your problems, “I think the fundamental premise they’re coming from is actually spot on. Yes, it is difficult. Yes, there is a lot more automation that can happen. And guess what? Microsoft can help with that. Gosh, thank heavens, not a moment too soon. And why didn’t you do this before?”

Getting cloud configuration right for your specific workload will still remain a shared responsibility, but “more things are digitally expressed now, so there’s actually a little bit more Microsoft can do,” Rotibi added.

What Pearl calls “agentic cloud ops” is an attempt to make ops teams more effective by giving them agents to take some of the load.

“We have the ability to have these agents work together in a multi-agent workflow as well,” Pearl said.

Developers will find the deployment agent useful too, of course.

“We’ve got a really nice integration into GitHub,” Pearl continued, “so that you can push the infrastructure as code that’s being built through the deployment agent directly into GitHub. But this is very much focused on agentic cloud ops and really trying to automate IT ops, SecOps, DevOps, data ops, FinOps, all the operation roles.”

GitHub is taking a similarly proactive approach, with Microsoft Defender for Cloud getting integrated into GitHub Advanced Security, so you can filter for runtime risks like workloads with sensitive data, or that are exposed to the public internet, and have developers notified when those issues show up — along with a suggested Autofix.

Copilot has more history than before, so you can look back at previous conversations to see what you’ve used it for in the past, and because some of the tasks you can kick off take time, you can start a new chat while one prompt is still processing.

> “Copilot pulls from data across what a customer has access to: It’s aligned to ARM and RBAC policies, it has access to anything that the user has access to and permission to.”  
> **– Pearl**

It also gets a lot more context about your tenant, though what the agents can do depends on what rights and permissions your account has, notes Pearl.

“Copilot pulls from data across what a customer has access to: it’s aligned to ARM and RBAC policies, it has access to anything that the user has access to and permission to,” she explained. “We have grounding data from Microsoft Learn and the API documentation, as well as our troubleshooting agents. And it calls from data sources like the Azure control plane for orchestration and management context. It’ll call from [the] Azure Resource graph to get real-time inventory of your resources.”

What Pearl calls a “prompt starter” will coach users to give the extra details that make interactions with generative AI more useful (something that can be hard when search engines have spent years training us to use just a few keywords to get relevant results).

“We do context injection on behalf of the user,” Pearl continued. “We can see what page the user is on, where they are in the portal, what resources they are looking at, and then also look across their entire Azure account. And it’s conversational — we’re asking follow-up questions and clarifying.”

But rest assured that if the agent is going down the wrong path, you can redirect them.

## Translating to Microspeak

One perennial problem for users who are new to Azure (or used to on-premises servers) is figuring out which services are useful — or even the equivalent of what they’d use on AWS or GCP.

Pearl runs the Microsoft program for startups and admits that “if a startup founder or AI-native developer is used to AWS, the transition to Azure can require some translation”.

Azure Copilot could be useful for them, as well as helping users figure out if a new service like AKS Automatic or HorizonDB is relevant to them — and what they would need to do to switch an existing, specific workload to a different service, including what that’s likely to do to the cloud bill.

“We could use natural language to, say, deploy a Python Flask app with PostgreSQL backend and enable monitoring for Application Insights and secure secrets in Key Vault,” Pearl said. “You could, just through natural language, tell the deployment agent what infrastructure you’re trying to create, and it will go create those Terraform files for you to review, using Azure Well Architected Framework best practices, and then you could push that to GitHub.”

Because Azure Copilot is grounded in Learn content and API documentation, she suggests the agents will be ready to work with new services “pretty quickly” as they roll out.

Rotibi says Microsoft has chosen the right areas to start with, both for improving productivity and for handholding less experienced staff.

“If you’re inside IT infrastructure operations or even deployment, they’re all functions that everybody has. Anyone with any years of experience will know, these are the things I need to do; and junior people are coming up, and that’s what they’re going to need to be helped with.”

> “Some of the things we hear a lot from customers are around troubleshooting — wanting faster, more proactive issue detection.”  
> **– Pearl**

Also, Copilot itself will continue to evolve. Pearl refers to this [early access preview](https://www.aka.ms/azurecopilot/agents) as the “first phase” to cover common requests and pain points.

“Some of the things we hear a lot from customers are around troubleshooting — wanting faster, more proactive issue detection. Every customer cares about resiliency, so the agent is designed to surface recommendations around high availability, disaster recovery, and generate the code and actions. For deployment, customers really want simpler, more guided experiences. Optimization, customers are really trying to optimize for cost as well as performance. [These] agents are tuned to analyze utilization, and recommend and execute cost savings. Identifying that a VM might be running at 30% utilization and modelling what downsizing could look like, but also making sure that that’s balanced with performance.”

In the future, Azure Copilot might look beyond services you’re already using, to suggest others that might be more useful — like a managed database service instead of running the database yourself.

“We have all this access to all the data that your user themselves has access to,” said Pearl. “Imagine you’re looking at logs and telemetry data and metrics and performance and cost, and you can triangulate all that data to have smart recommendations around either improving the existing product configuration you have, or swapping products out for products that may be a better fit.”

> Microsoft “needs to understand what it looks like in an integrated, hybrid, multicloud world”.  
> **– Rotibi**

Given that a few organizations use only Microsoft and Azure services, Copilot will also need to handle third-party services, and maybe not only on Azure, Rotibi suggests, noting that “[Microsoft] needs to understand what it looks like in an integrated, hybrid, multicloud world”.

Microsoft can build on its partner ecosystem here, particularly with the emerging MCP standard.

“They aren’t doing third-party connectors at the moment,” Rotibi said, “but there are standards inside a big enterprise: you know they’ll be using particular applications and solutions. There’s a list of things you’re going to have to connect, whether it’s Databricks, Snowflake, or whatever.”

Rotibi also expects organizations will want the output of Azure Copilot to integrate into their other logging systems, like Splunk, AppDynamics or Dynatrace, as well as Microsoft’s own observability platform for capturing changes, analyzing them and sometimes even replaying them for testing, to make agents part of that workflow.

“There’s a level of maturity in the market where the level of automation, the level of capturing is allowing a better conversation and a better way of working; and Microsoft is capitalizing on that,” Rotibi said.

Making tools like Azure Copilot successful as a new way to manage cloud configuration will require integration, as well as visibility and transparency into the operations and mechanics of the agents, she suggests. “I think that’s what they’re trying to do; [the question is] what level of maturity and depth they’ve achieved. I think they’ve done a lot and a lot of it’s really good — and I think there’s more to be done.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)