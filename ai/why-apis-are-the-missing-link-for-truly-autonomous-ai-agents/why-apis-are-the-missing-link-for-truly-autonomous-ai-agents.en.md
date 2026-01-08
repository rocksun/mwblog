Recent breakthroughs in AI have caught the eyes of executives who are eager to realize new efficiencies through automation. Though the potential gains of AI will be measured in the trillions of dollars, there are significant hurdles that must be overcome first.

While chatbots and copilots have the potential to help customer service and software engineers, reasoning models give us the potential to have [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) that can handle a wide range of tasks, potentially with full autonomy.

Though the technology is definitely promising, we are still missing important pieces to the agentic AI puzzle — namely, a secure and reliable way to enable the agents to communicate.

## A Historical Parallel: The Rise of APIs in Web 2.0

As developers adopted [Web 2.0](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/) and mobile technologies in the mid-to-late 2000s, APIs emerged. First-generation languages and protocols, such as the bulky XML and complex Simple Object Access Protocol (SOAP), gradually gave way to better and easier-to-use tools, such as JavaScript Object Notation (JSON) and Representational State Transfer (REST).

By about 2010, JSON and [REST](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/) were cemented as the new standards for application integration. They also changed the way developers built applications. Instead of developing large monolithic applications with tightly contained business logic exposed through proprietary APIs, REST and JSON enabled them to expose business applications to the outside world as microservices.

This ushered in the new age of cloud native computing. In the early 2010s, instead of using the waterfall development method to build tightly coupled applications that run in rigid virtual machines (VMs), cloud native computing encouraged the development of applications as a collection of loosely coupled microservices running in containers managed by Kubernetes, all created using new DevOps technologies and methodologies, like git, Jenkins and CI/CD.

The agentic AI world needs something similar to REST and JSON. We’re not there yet, but we’re close.

## MCP, A2A and ACP — Oh, My!

If the world of agentic AI is going to deliver the 50% efficiency gains that early promoters are promising, we’re going to need better technological glue to bring it all together. We are still in the early days of the agentic AI world, and there are several proposed standards.

Anthropic struck first with the release of [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) in November 2024, which it likened to a USB 3.0 port for AI. Google struck next in early 2025 with [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/), a new protocol designed to build atop MCP and provide high-level coordination among agents or groups of agents. IBM proposed a third protocol, dubbed the [Agent Communication Protocol (ACP)](https://thenewstack.io/ai-agents-can-talk-but-can-we-trust-them/), to function as a universal protocol that enables multiple AI agents to work together.

> The early work developing protocols for agentic AI is promising. But like the early days of XML and SOAP, the level of complexity is still too high for widespread adoption.

The early work developing protocols for agentic AI is promising. But like the early days of XML and SOAP, the level of complexity is still too high for widespread adoption. We must move toward the JSON and REST equivalents of agentic AI to realize the full benefits that agentic AI promises.

So what does that look like? It looks like the classic API.

## APIs: The Real Connectivity Layer for Agentic Enterprise

APIs are already the data backbone of global software connectivity. Without them, the systems behind AI, modern applications and cloud platforms could neither communicate nor scale. In reality, APIs have quietly become the essential infrastructure powering today’s AI models — and they will be even more critical as autonomous agents become mainstream.

APIs are far more than endpoints or integration tools; they are the invisible highways through which data travels and agentic systems interact. Preparing for the agentic era means elevating APIs to the forefront and making them secure, discoverable, governed and designed for multiagent collaboration.

## What Next-Gen AI Protocols Look Like

The early work on MCP is promising, and many AI tools providers and database developers have incorporated MCP clients and MCP servers into their products. However, we’re still a long way from being able to realize the full potential of agentic automation.

There are concerns with the protocols themselves. For instance, MCP, as it currently stands, is not secure. That’s not the fault of Anthropic’s developers; it’s merely a reflection of its very young age. Getting the functionality right is important, but for autonomous agentic AI to become ubiquitous, the transactions must be secure. That is non-negotiable.

Governance is another area of concern. Generative AI (GenAI) has a well-documented tendency to make things up. Hallucinations are unavoidable to an extent. They’re features of how probabilistic systems like GenAI work — not bugs. However, businesses cannot and should not implement autonomous agents that are prone to saying hateful things or doing dangerous things. That means building guardrails directly into the protocols and the systems that we use to control them.

> APIs will mask the underlying complexity that’s involved with invoking various protocols and make it easier for developers to work with AI agents in a secure, governed and well-managed way.

There are other technical challenges that must be solved, such as token and session management, testing and debugging, and [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "monitoring and observability"). For many of these areas, developers will be able to extend existing software engineering technologies and techniques to the world of AI.

APIs will also be extended to support the new agentic world. In fact, APIs will form the critical link between AI agents and existing data and applications. In the same way that APIs form the connective tissue that allows data and applications to be called and used in the modern Internet, APIs will be relied upon to coordinate groups of agents that execute tasks on our behalf.

Just as businesses use APIs to expose a limited set of data or application functions to their customers and partners, businesses will also use APIs to expose AI and agentic functions to the outside world. These APIs will mask the underlying complexity that’s involved with invoking various protocols (MCP, A2A, ACP) and make it easier for developers to work with AI agents in a secure, governed and well-managed way.

## API 2.0: Emergence of the Agentic Programming Interface

There are good indications that we are on the cusp of a major shift, from single-task AI assistants to truly autonomous multiagent systems capable of complex and company-wide collaboration.

Chatbots and copilots are already handling jobs previously done by people, and this level of automation will continue. But a much bigger revolution is underway that will result in a transformation of the way software is developed and used. The humble API, which was so instrumental to realizing the potential of the internet with Web 2.0-era technologies, will play a starring role in this AI agentic revolution.

However, there is still a lot of work to do building the underlying communication mechanisms that enable all of this to happen. While the underlying protocols are being developed now, companies will need to develop new APIs that enable them to expose existing functionality through these protocols. They’ll also need new software stacks that allow for efficient management and governance of these AI APIs.

The promise of agentic AI is great. However, if we’re going to replicate the Web 2.0 revolution with agentic AI, we’re going to need better APIs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/dd42f4ed-cropped-f340d0c1-arash-nourian.jpeg)

Arash Nourian is global head of AI at Postman, where he is helping build Postman into an AI native integration fabric for APIs and agents. Previously, he was general manager and director of engineering for AI Engines Infra & Operations...

Read more from Arash Nourian](https://thenewstack.io/author/arash-nourian/)