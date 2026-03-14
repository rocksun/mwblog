On the heels of [last month’s Perplexity Computer launch](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/), the company on Thursday [announced](https://www.perplexity.ai/hub/blog/computer-for-enterprise) an expansion of the Perplexity API Platform with three new developer tools: Embeddings API, Agent API, and Sandbox API.

These APIs expose more of the system behind Perplexity Computer to developers, including the orchestration layer that coordinates search, tools, models, and execution.

## A unified orchestration to replace fragmented stacks

With modern AI systems increasingly relying on multiple specialized models and tools, it’s this orchestration layer that makes the difference.

It’s become the norm for developers to turn to multiple providers for search, models, embeddings, and compute, cobbling together stacks to build agentic workflows. But with its new suite of APIs, Perplexity aims to give developers the building blocks of its own Computer, so they can replace this patchwork approach with a single API key that unifies the retrieval, intelligence, and compute layers.

Embeddings API, Agent API, and Sandbox API join Search API, the retrieval layer underneath the API platform that indexes 200 billion URLs with tens of thousands of index updates per second, [launched in September 2025](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api). Where the Search API retrieves from the open web, the Embeddings API enables vector search across internal systems and files, thanks to bidirectional, natively quantized encoders that produce 4-32x smaller embeddings.

[James Liounis](https://www.linkedin.com/in/jamesliounis/), member of technical staff at Perplexity, tells *The New Stack,* “Embeddings is a way to essentially take your own proprietary data and create embeddings of them that you can just then retrieve at scale,” says

It’s a solution for when a textual match isn’t enough and developers need semantic similarity to understand context.

“We kind of expanded this technology we have for the web to…these embedding models…to be able to essentially…replicate it on your own internal documents,” Liounis adds.

Together, Search API and Embeddings API feed into the new Agent API, a managed runtime for agentic workflows that orchestrates the full agentic loop: retrieval, tool execution, reasoning, and multi-model fallback.

With integrated search, tool execution, and multi-model orchestration, Agent API gives developers a single integration point to replace fragmented stacks, effectively taking the place of a model router, a search layer, an embeddings provider, a sandbox service, and a monitoring stack with a single endpoint, account, and API key.

But Liounis says the value of Agent API extends beyond just model access; it’s access to the system that decides how to use models and tools together to complete a task. Instead of assembling that stack for themselves, developers can use a more unified system built on the infrastructure Perplexity already uses in production.

> “We want to relieve developers of the plumbing that is required to build agents.”

“We want to relieve developers of the plumbing that is required to build agents,” Liounis says. “We want them to be able to access the best search possible; the same search that powers our core. We want them to be able to essentially build an agent while focusing on what really matters — the capabilities of the agent — as opposed to having to worry about, ‘which model am I going to use?’ or ‘How am I going to integrate all these various models at the same time?'”

Sandbox API, for its part, provides isolated execution across Python, JavaScript, and SQL, with file system access, runtime package installation, and built-in resource limits.

## “Everything is computer” — and computer is for everyone

The new APIs are part of a broader push to expand Perplexity Computer and the company’s philosophy that [“Everything is computer.”](https://www.perplexity.ai/hub/blog/everything-is-computer)

“Computer is a set of a wide range of tools,” Liounis says, adding it is “a wide range of models and a wide range of various connectors that sit…on top of the main orchestrator. And essentially what the Agent API does is…expan[d] these capabilities to developers.”

And across Perplexity’s own ecosystem with Personal Computer and Computer for Enterprise.  
Personal Computer can run 24/7 on a dedicated Mac mini, connecting to local apps and Perplexity’s secure servers to serve as a digital proxy, i.e., working on behalf of users to orchestrate tools, tasks, and files from any device, anywhere. Security checks include full audit trails for each session, required approval for sensitive actions, and a kill switch.

Its enterprise-focused counterpart, Computer for Enterprise, similarly extends Computer’s capabilities.

Computer for Enterprise natively connects to the tools teams already use every day (e.g., Snowflake, Salesforce, and Hubspot, among hundreds of others), fitting naturally into existing workflows. For example, to create financial models, Computer can take over writing and running queries and then give you structured results, without you having to wait on your data or analytics teams.

Here, security levels up with SOC 2 Type II compliance, SAML SSO, audit logs, and secure sandboxing for every query.

Other expansions of Perplexity functionality include deeper research capabilities and tools. Perplexity Finance, Computer’s data and analysis layer, can now access 40+ live financial tools, such as S&P Global and Coinbase. Similarly, Premium Sources lets Computer pull paywalled sources (e.g, Statista, CB Insights) directly into research workflows.

Embeddings API and Agent API are now live, with Sandbox API in beta.

“Perplexity is an orchestrator itself,” says Liounis. “Most of our products…have been built by tying a lot of frontier models together and tuning these very large and complex agent loops… We’ve gotten really deep into this agent space, and we really want to start sharing these learning with developers.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)