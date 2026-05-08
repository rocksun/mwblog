ServiceNow built its reputation on automating business workflows, but today, the company calls itself “the AI control tower for business reinvention.”

It’s a theme that’s on full display at the company’s Knowledge 2026 conference this week. On Wednesday, ServiceNow announced new governance features, free access to its low-code app management tool for all customers, new integrations with third-party development tools, and updates to its [agent-building tools](https://www.servicenow.com/docs/r/intelligent-experiences/ai-agent-studio.html).

ServiceNow first introduced the control tower metaphor at last year’s event, but since then, it has become increasingly clear that what enterprises — and really all businesses — need to put AI agents into production is better guardrails and governance. At the same time, they don’t want to lock themselves into a set of tools that may be state-of-the-art today but become outdated in only a few months.

[Jithin Bhasker](https://www.linkedin.com/in/jithinbhasker/), the group vice president and general manager of Creator Workflows and App Engine at ServiceNow, tells *The New Stack* in an exclusive interview that while everybody in this space is investing in agent builders and AI-centric app-building tools, ServiceNow wants to offer not only those tools but also the tools to manage them.

> “We have our own vibe coding offering, but we are thinking ahead… how do we make sure when agents and applications are built on our platform, [they] have the right security guardrails and controls.”

“We have our own vibe coding offering, but we are thinking ahead,” Bhasker says. “I think the next big phase is […] how do we make sure when agents and applications are built on our platform, [they] have the right security guardrails and controls. We are investing in Agent Studio, but also making sure the right governance and controls are really coming together so that the CIOs do not have to worry about ‘shadow AI.'”

At the core of how ServiceNow is approaching this is the realization that there is no developer loyalty anymore. While ServiceNow may offer its own agent and app builders, employees will want to use Claude Code, Codex, Cursor, Windsurf, and whatever the next wave of agentic coding tools may look like in a month or two.

> “We fundamentally believe that while AI agentic solutions and vibe coding are a great way to get started, the real enterprise value comes from the actual enterprise-grade controls.”  
> —Jithin Bhasker

“What this is really creating is a sprawl of AI assets and agents, which is getting deployed in some of the production instances and environments,” Bhasker says. “That’s where we fundamentally believe that while AI agentic solutions and vibe coding are a great way to get started, the real enterprise value comes from the actual enterprise-grade controls.”

## ServiceNow in the age of zero developer loyalty

At Knowledge, ServiceNow is launching new integrations with agent-first IDEs like Cursor, Windsurf and GitHub Copilot, plus a separate set of MCP-client integrations into Figma, GitHub, and Miro that let Build Agent pull design specs, code context, and requirements directly from those tools. The point, as the company notes, is to give “developers expanded skills and context wherever they build for ServiceNow.”

> “It doesn’t matter whether you’re a GitHub Copilot user or a Cursor [user] or a Claude [user], you can start to build anywhere with our SDK skills.”

“It’s about making it easy for any tool to get access, to be able to build on the ServiceNow platform,” says Bhasker. “We gain two advantages right there: one, our persona has multiplied or quadrupled. In the past, we heavily invested in our own studios and IDEs and all of it. Now, we are saying it doesn’t matter whether you’re a GitHub Copilot user or a Cursor [user] or a Claude [user], you can start to build anywhere with our SDK skills.”

For developers, this means they can now take the core skills from ServiceNow’s Build Agent — which inside ServiceNow Studio is now powered by Anthropic’s Claude Opus 4.6 — and use them natively in their preferred IDE without having to switch context. Build Agent is ServiceNow’s AI agent for creating and updating ServiceNow applications from natural language prompts, and until now, it was only available in the ServiceNow IDE.

## Build Agent goes portable

With the Knowledge 2026 release, the company is also embedding Build Agent inside ServiceNow Studio for the first time, alongside a new Global Scope mode that lets Build Agent modify out-of-the-box ServiceNow applications like ITSM, HRSD, and customer service, not just generate net-new apps in custom scopes. That last piece matters more than it sounds: the bulk of enterprise spend on ServiceNow goes into customizing those existing applications, not greenfield builds.

Once they’ve built the application, developers can take those agents and apps they built and have them managed — for free — by ServiceNow’s App Engine Management Center (AEMC), the company’s service for managing the full lifecycle of applications that run on its platform. AEMC also picks up a self-healing test loop that writes tests, diagnoses failures, and patches broken builds automatically until quality gates pass, plus Agent Packs that let customers encode their own development standards into the Build Agent. By making AEMC available to all users, no matter what ServiceNow license they have, the company is removing the friction of using it, Bhasker argues.

“The reason why I decided to open up the App Engine Management Center is that I felt it’s the need of the hour — because you have so many applications and agents which are getting built, and we feel responsible to make sure those agents and applications are built in the right way, with the enterprise-grade governance controls and security,” Bhasker explains.

In practice, this means a developer could write an application in Claude Code, push it into a ServiceNow instance, and from there, AEMC will run tests and scan the application to make sure it’s ready to run in production. ServiceNow Studio and a reimagined AI Agent Studio, the company’s conversational creation surface for AI agents, also no longer require a special license to use.

## **Every app gets an agent**

One interesting aspect of all this is that going forward, anytime an application is built on the ServiceNow platform, ServiceNow will automatically recommend an AI agent that can live inside of that application.

“Whether you’re from finance, trying to process hundreds of invoices every day and matching receipts. Imagine you have an agentic, autonomous specialist who is alongside you, who is getting you through it,” Bhasker says. “You can build anywhere, host it on ServiceNow’s platform, and every app that is built on the platform now will have an automated recommendation for an autonomous AI Agent specialist with the components and controls.”

## ServiceNow’s not alone in this

In many ways, the pitch here isn’t unique to ServiceNow. Salesforce shipped Agentforce Vibes 2.0 and Headless 360 at TDX 2026 in April with a similar build-anywhere-deploy-here framing. Microsoft is making the same case with Copilot Studio and Power Platform’s managed environments. What separates ServiceNow’s version of the argument is the size of its existing footprint, the company argues. It’s services already run the workflows for IT, HR, legal, and customer service inside most of the Fortune 500, and that reach across departments is hard for any rival to match from what is typically a much narrower starting point.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)