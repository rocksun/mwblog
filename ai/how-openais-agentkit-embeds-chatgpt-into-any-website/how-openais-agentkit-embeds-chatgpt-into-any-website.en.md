[AgentKit](https://openai.com/index/introducing-agentkit/) is a comprehensive toolkit that allows developers to integrate ChatGPT-powered agents into websites and applications. It was introduced at [OpenAI’s 2025 DevDay](https://openai.com/devday/) as a way to build AI agents that not only chat but also perform actions such as browsing, making API calls and completing multistep tasks.

In essence, AgentKit provides the architecture and building blocks needed to embed ChatGPT-based assistants directly in your product. This article dives into AgentKit’s architecture, including its core components, and demonstrates how it enables ChatGPT-like functionality to be seamlessly embedded into any website.

## Foundations of OpenAI AgentKit

At its core, AgentKit is built on a robust foundation comprised of two primary backend components: the [Responses API](https://platform.openai.com/docs/api-reference/responses) and the [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk). These form the engine that powers all AgentKit features:

**Responses API:** Handles structured outputs and OpenAI’s function-calling interface (i.e., tool usage). When an agent needs to use an external tool or API, the Responses API formats the request, executes the function call and returns results in a structured format that the agent can understand. This removes the need for developers to parse outputs or manually handle tool integration errors.

**Agents SDK:** Provides the runtime and orchestration layer for agents. It manages conversation state across multiple turns, sequences multistep tool calls, handles retries and errors, and enforces the agent’s control flow logic. This SDK lets the agent maintain memory and reasoning across steps without the developer writing boilerplate code to chain prompts or track context. The Agents SDK can be used directly in code for complete control or accessed via higher-level tools like the visual builder.

> In practice, Responses API plus Agents SDK means developers don’t have to reinvent low-level infrastructure for conversation management or tooling.

Everything else in AgentKit is built on top of these two layers. In practice, this architecture means developers don’t have to reinvent low-level infrastructure for conversation management or tooling – those capabilities are provided out of the box. AgentKit workflows can be defined visually or in code, and the platform handles streaming responses, state and tool orchestration behind the scenes. This architecture accelerates development by handling common agent patterns and improves reliability by providing a tested runtime with built-in error handling and safety checks.

Safety and guardrails are also integral to AgentKit’s architecture. The platform includes input validation, output filtering and PII (personally identifiable information) masking features to prevent malicious prompts and sensitive data leaks. These guardrails act as a security layer around the agent, scanning what goes into and comes out of the model. While not foolproof, they significantly reduce risks when deploying AI agents on real user data by blocking jailbreak attempts and redacting private information from logs. Developers can adjust guardrail strictness per use case. For instance, tightening constraints for a finance chatbot versus a less sensitive internal tool. This safety-first design ensures that embedded ChatGPT agents behave responsibly on websites and in apps.

## Building Blocks of AgentKit

AgentKit provides a set of modular components that work together to let you build, deploy and embed ChatGPT-powered agents quickly. These components abstract common functionality — like building conversation flows or connecting to data sources — so you can focus on your use-case logic rather than infrastructure.

Below are the core components and what they do:

**Agent Builder:** A visual workflow editor for designing an agent’s logic and conversation flow. Instead of writing orchestration code, developers can drag and drop nodes representing prompts, tool calls, branches and other actions onto a canvas. You connect nodes to define the agent’s decision logic and configure each node’s parameters. The Agent Builder supports versioning and preview runs, which means you can iterate on your agent’s design safely. You can test new workflow versions without affecting production and even export the visual flow to code once you’re ready to fine-tune or extend it in your own codebase. This visual approach significantly speeds up prototyping of complex multistep agents, making it easier for developers and non-developers alike to collaborate on agent logic.

[![](https://cdn.thenewstack.io/media/2025/10/c505fe83-agent-kit-0-1024x298.png)](https://cdn.thenewstack.io/media/2025/10/c505fe83-agent-kit-0-1024x298.png)

**Connector Registry:** A library of pre-built integrations for connecting agents to external systems and APIs. Real-world agents often need to fetch data or trigger actions in other services such as databases, SaaS apps and internal APIs. The Connector Registry provides out-of-the-box connectors for common services like Dropbox, Google Drive, SharePoint, Microsoft Teams and more.

Each connector comes pre-coded to handle authentication, API calls, rate limits and errors, so you can select a connector, configure permissions and plug it into your workflow without writing custom integration code. This central registry lets admins govern data access in one place – you can control which connectors are enabled, manage credentials securely and monitor usage centrally. If a needed integration isn’t available, developers can create custom connectors that conform to the same interface and share them across projects. The Connector Registry simplifies linking your ChatGPT agent to the rest of your tech stack, a critical capability for embedding the agent into real business workflows.

[![](https://cdn.thenewstack.io/media/2025/10/73036d36-agent-kit-1-656x1024.png)](https://cdn.thenewstack.io/media/2025/10/73036d36-agent-kit-1-656x1024.png)

**ChatKit:** An embeddable chat UI toolkit for deploying the agent’s frontend on your website or app. ChatKit handles the entire chat interface – message display, streaming responses, user input box, conversation history, etc. – so you don’t have to build a chat UI from scratch. Developers simply drop in the ChatKit component and point it to their agent’s API endpoint, instantly getting a ChatGPT-style assistant in their product. This means you can embed a ChatGPT-powered assistant directly into any website or application with minimal effort.

ChatKit is highly customizable in appearance, allowing you to match the widget’s design to your site’s branding (colors, fonts, layouts). Under the hood, it uses WebSockets to stream token-by-token responses for a smooth, interactive experience. By using ChatKit, developers embed ChatGPT-style assistants into websites and apps, so the same AI experience follows users wherever they work.

In short, ChatKit enables ChatGPT integration on any site by providing a ready-made chat interface. Developers just embed it and let it talk to your AgentKit backend. This dramatically cuts down on frontend development time (saving “weeks” of work in building a real-time chat UI yourself). If needed, teams can still build a custom interface for unique use cases, but ChatKit covers the majority of conversational agent scenarios.

[![](https://cdn.thenewstack.io/media/2025/10/067dfc3a-agent-kit-2-1024x648.png)](https://cdn.thenewstack.io/media/2025/10/067dfc3a-agent-kit-2-1024x648.png)

**Evaluation and Tracing Tools:** Building an AI agent is an iterative process, and AgentKit includes tools to evaluate and debug agent performance. The platform allows you to create evaluation data sets (sets of test queries and expected answers or outcomes) and run your agent against them to measure accuracy, response quality and other metrics. It supports custom “graders” – automated checks or human review functions – to score the agent’s responses for correctness, relevance and safety. This helps pinpoint where the agent might be making mistakes.

AgentKit also provides trace logs for each conversation, showing the agent’s step-by-step reasoning: which tools it tried, what data it received and how it decided on the next step. Trace grading allows developers to inspect and debug complex multistep workflows by replaying what the agent was “thinking” at each step. These eval and tracing features are essential when embedding a ChatGPT agent into a production website. They give developers visibility into the agent’s decisions and a way to improve it systematically. In fact, AgentKit can even suggest prompt improvements automatically based on evaluation feedback, speeding up the refinement cycle for your agent.

> AgentKit supports continuously improving agents through feedback.

**Reinforcement Learning and Improvement Loops:** Beyond one-off evaluations, AgentKit supports continuously improving agents through feedback. Developers can define reward functions or custom success metrics and use them to fine-tune the agent’s behavior over time. This reinforcement fine-tuning mechanism uses feedback signals to adjust the agent’s strategy.

AgentKit provides the infrastructure to collect real user feedback, log interactions and perform iterative retraining without building a separate pipeline. While developers must carefully define what “good” behavior means, this loop allows an embedded agent to get smarter and more tailored to your domain as it interacts with users. In practical terms, an agent on your website could gradually learn to handle your users’ queries more accurately by incorporating feedback, all managed through AgentKit’s tooling.

**Built-in Guardrails:** As mentioned earlier, safety features are a core component. AgentKit integrates OpenAI Guardrails, an open source safety library, directly into agents, providing configurable policies for content filtering and safe actions. You can enable guards to automatically check user inputs for disallowed content or patterns that attempt to trick the AI, and, similarly, sanitize the agent’s outputs.

There are options for masking personal data, preventing specific tool usage (for example, limiting an agent’s access to read-only data rather than delete it), and requiring human approval for high-stakes actions. These guardrails are customizable per workflow and help ensure that a ChatGPT agent embedded on a website operates within acceptable bounds, providing reliable assistance without going rogue. For instance, a customer support bot could have strict filters to avoid giving financial advice or revealing account details, whereas an internal research bot might be allowed more freedom. By bundling guardrail features, AgentKit saves developers the trouble of implementing their own safety checks and makes it easier to deploy agents with confidence.

[![](https://cdn.thenewstack.io/media/2025/10/7999f7c2-agent-kit-3.png)](https://cdn.thenewstack.io/media/2025/10/7999f7c2-agent-kit-3.png)

## Components Working Together

All these components work together. When you embed ChatGPT into a website using AgentKit, you use Agent Builder (or code) to define what the agent should do, Connectors to link the agent with external data/services it needs, ChatKit to put a chat interface on your site for users to talk to the agent and Evals/monitoring to track and improve the agent’s performance.

The heavy lifting – such as managing dialogue state or calling GPT-4/GPT-5 under the hood – is handled by the Responses API and the Agent SDK foundation so you can focus on building features rather than plumbing.

[![](https://cdn.thenewstack.io/media/2025/10/4c28413e-agent-kit-4-879x1024.png)](https://cdn.thenewstack.io/media/2025/10/4c28413e-agent-kit-4-879x1024.png)

## Conclusion

OpenAI’s AgentKit represents a significant step in making ChatGPT-style AI ubiquitous in everyday software. Its architecture abstracts the heavy lifting of building an AI agent into a platform that developers can easily plug into their own products.

The core components — such as Agent Builder, Connector Registry and ChatKit — provide a high-level toolkit for designing what the agent should do and deploying it to any website or app with minimal custom code. Real-world use cases show that companies are using AgentKit to create agents that automate customer support, augment productivity tools and streamline business processes, all by embedding ChatGPT’s capabilities in places where users need them.

For developers, AgentKit offers a faster, more reliable path from an idea to a production-ready AI agent, effectively enabling ChatGPT to live on your website or application as a helpful, action-taking assistant. With built-in evaluation and improvement loops, these agents can continually get better, making the prospect of an AI assistant on every website not just hype, but an achievable reality with the right tools.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)