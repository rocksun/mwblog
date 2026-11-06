**Connecting an AI agent to enterprise software is relatively easy.** Making sure it can find the right information, carry out the intended task, and stay within a user’s permissions is where things get complicated.

That’s what Docusign discovered while developing its Model Context Protocol (MCP) Server, which [entered open beta in May  2026](https://support.docusign.com/s/document-item?bundleId=mapc0a3127f-be83-4596-81a0-037932669a9a&language=en_US&topicId=con78724664-54e8-49b4-b03c-99123c9e09f7.html), and reached global general availability on September 30, 2026.

> “There’s a big difference between building tools and solving actual customer problems.”

![Sagnik Nandy, Chief Technology Officer, Docusign](https://cdn.thenewstack.io/media/2026/10/5e11eb07-docusign-cto.jpeg)

Docusign CTO Sagnik Nandy

The Docusign MCP Server lets compatible AI assistants and agents access select Docusign capabilities to create, sign, and manage contracts without requiring users to switch applications. Someone could ask an assistant to find a contract, check its status, or prepare an agreement for signature, with Docusign handling the underlying work. A human remains ultimately responsible for reviewing and approving the transaction and its outcome.

“There’s a big difference between building tools and solving actual customer problems,” [Sagnik Nandy](https://linkedin.com/in/sagnik-nandy), Docusign’s chief technology officer, tells *The New Stack*.

## **From APIs to AI agents**

Traditional REST APIs let developers connect applications and automate tasks through predefined requests. AI agents work differently. A user describes what they want in natural language, and the agent works out which tools to use.

MCP is an open standard that lets AI applications connect to external data and tools. A server exposes capabilities that a connected AI application can discover and invoke.

Docusign wanted to make its [Intelligent Agreement Management (IAM)](https://thenewstack.io/docusign-contract-ai-agents/) platform available inside the AI tools their customers use, helping organizations create, commit to, and manage agreements. Through MCP, selected Docusign capabilities are accessible from the AI environments customers already use.

Docusign announced the open beta at its Momentum conference in New York in May 2026. Preparing it for wider use revealed challenges beyond the early demos.

## **What the beta revealed**

Nandy says engineers working closely with customers can usually anticipate the prompts they’ll submit and the responses they expect. That gets harder when a wider audience has access to the same tools.

“Once you put it out there, you have to really get it right,” he says. “There are different kinds of prompts that come in. The different tools have to work together, both between themselves, but also across our tool boundary and the customer bringing in other tools.”

Feedback led Docusign to expand the contract data, workflow actions, and administrative controls  available through MCP.

“We added support for local files coming in, so a lot of people wanted to upload local data and interact based on that,” Nandy says.

That expanded access to information inside Docusign’s Contract Lifecycle Management (CLM) software, the company’s most advanced set of contract-related capabilities built on the IAM platform for customers with the most complex agreement lifecycle needs and added support for local document uploads through the MCP Apps interface in supported clients. That lets users work with documents that are not already stored in Docusign, subject to the client and workflow support available.

“We also added account-level settings and options,” Nandy explains. “Adding support for people being able to do certain things or turn off certain things at that level, that was also useful.”

On September 4, 2026, Docusign [announced](https://www.docusign.com/blog/agreement-layer-modern-agentic-enterprise) plans for global availability, which its release notes confirm began on September 30. By GA, the server supported broader agreement workflows and AI-client connections, alongside account-level administration; local uploads use the MCP Apps interface where supported.

Docusign has also reported growing uptake. During its second-quarter fiscal 2027 earnings call, the company said cumulative active accounts using MCP had more than quadrupled during the quarter, although it acknowledged that adoption was still in its early stages.

Reliability was another concern. In an [October engineering account](https://www.docusign.com/blog/developers/making-mcp-reliable-and-safe-in-production), Docusign described using guided interfaces, automated evaluations, and security testing to check how agents select and use its tools. Changes to an AI model or client can affect those interactions even when the underlying integration stays the same.

## **Keeping permissions intact**

Giving external AI tools access to contract data raises security concerns, particularly when documents contain sensitive business information.

Nandy says Docusign uses OAuth 2.0 for authentication. Each tool call must have the [required OAuth scopes](https://support.docusign.com/s/document-item?bundleId=ug3906200f-95c6-4a6b-90b1-f928c85961c6&language=en_US&topicId=ref1a2e4d33-36be-49d5-89d2-5566741be566.html) and remain within the user’s Docusign permissions.

“There’s this fundamental principle that an MCP server strictly operates within the user’s Docusign permissions and authorization,” he explains. “So you should not be able to do anything that you wouldn’t be able to do in the product.”

The same restrictions apply when agents take action, while underlying API calls remain subject to Docusign’s existing logging and monitoring policies. These controls don’t govern how a third-party AI provider stores or uses data it receives; customers must also assess that provider’s data policies.

> “Even though an agent is performing it, it doesn’t mean the agent should have any extra privileges.”

“Even though an agent is performing it, it doesn’t mean the agent should have any extra privileges,” Nandy says.

Account administrators can enable or disable MCP access for an account. Additional connector settings may vary by AI client. But permissions alone cannot prevent an agent from misunderstanding a request, so how it handles ambiguous instructions matters just as much.

## **One server, multiple AI clients**

Docusign supports AI environments including Anthropic Claude, OpenAI ChatGPT, Google Gemini Enterprise, Microsoft Copilot Studio, Slackbot, Salesforce Agentforce, and Perplexity.

The company maintains a shared MCP Server behind its client connectors, giving those integrations a common interface to Docusign contract data and agreement workflows..

“One of the design choices we made is we have a single MCP server, and the layer between our internal systems and MCP is pretty thin,” Nandy says.

“We also have a single MCP solution server as opposed to multiple specific to each client, which allows us to maintain consistency.”

Different AI clients may interpret requests or present information differently, and connectors may expose new tools at different times. The shared server gives Docusign a common place to maintain its capabilities and also supports custom agent integrations. [Docusign recommends official connectors for production accounts](https://support.docusign.com/s/document-item?bundleId=ug3906200f-95c6-4a6b-90b1-f928c85961c6&language=en_US&topicId=cond8e12198-79cf-4eae-93d9-24046c907dc3.html) and custom connectors for developer-account testing.

## **When an agent needs to ask questions**

Someone might ask an agent to prepare an agreement without specifying which template to use, or request a document without saying whether they want the file or a link.

Nandy says Docusign has worked to support conversations where agents can ask for clarification instead of allowing an AI client to guess..

“One of the things we try to do is add support for user-guided feedback,” he says. “It can ask you questions like: Should you use a template for this? Or, if you want information back, do you want the entire file or a URL?”

That back-and-forth is one advantage of agent-based interactions over conventional API calls, where the application typically has to supply the required parameters.

“You can have these back-and-forth conversations. You can have that guided flow, and we leverage that strongly,” Nandy says.

For contract workflows, clarifying before acting could keep an agent from selecting the wrong document or proceeding with incomplete instructions. Guided MCP Apps provide structured steps in supported contract workflows, but the experience depends on the host’s capabilities.

## **MCP doesn’t replace APIs**

Despite Docusign’s investment in MCP, Nandy doesn’t see it replacing traditional APIs. The company has long taken an API-first approach, and he argues that the choice depends on what developers are building.

“APIs often provide a certain level of determinism,” he says.

For processes with clearly defined inputs and outputs, a direct API call may make more sense. MCP helps when an agent needs to choose between tools as part of a broader request, though teams can use both approaches together.

“We’ve also seen solutions where both are used in tandem,” Nandy says, describing agents that can recognize when a single API endpoint handles a task better.

> “APIs often provide a certain level of determinism.”

For engineering teams, the decision comes down to where an AI agent adds useful context or flexibility and where conventional automation already does the job.

Docusign’s move to general availability shows how much work sits behind an enterprise MCP integration for enterprise contract workflows. Supporting different AI clients is one challenge; making sure AI contract workflows behave reliably, respect permissions, and route ambiguity for clarification is another.

Developers can explore supported clients, authentication requirements, and available tools in Docusign’s [MCP Server documentation](https://developers.docusign.com/platform/mcp-server/).

### More Docusign in *The New Stack*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)