2025 has been [the year of AI agents](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/), and most of the developer attention so far has been on the frameworks and tools to build these agents. We’ve seen a flurry of launches in this space recently: OpenAI’s [AgentKit](https://openai.com/index/introducing-agentkit/) and [Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/), Anthropic’s [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview), Google’s [Agent Development Kit](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) (ADK) and [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder).

What about the distribution of agents? We’ve seen the beginnings of an app-store-like model in the form of OpenAI’s new [Apps SDK](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/), which lets developers publish agents inside ChatGPT. But will there be a way to make agents available that isn’t reliant on a commercial platform like OpenAI’s? A group at MIT hopes to provide exactly this with Project NANDA.

[Project NANDA](https://nanda.media.mit.edu/) — short for Network of AI Agents and Decentralized Architecture — is an MIT Media Lab initiative to build a decentralized infrastructure for an “Internet of AI Agents.” The goal is an agent ecosystem that will include cross-platform or cross-vendor discovery, federated registries and open identity and trust layers.

## **What Is NANDA?**

The first thing to note is that NANDA builds on Anthropic’s Model Context Protocol (MCP) and Google’s Agent2Agent (A2A) Protocol. But there’s much more besides those two open source projects. In [a presentation earlier this year](https://www.youtube.com/watch?v=yXxHb3LMygw), NANDA’s director, [Ramesh Raskar](https://www.linkedin.com/in/raskar/), associate professor at MIT, likened the overall project to a quilt.

[![NANDA quilt](https://cdn.thenewstack.io/media/2025/10/46a6df5e-nanda-quilt-2025.png)](https://cdn.thenewstack.io/media/2025/10/46a6df5e-nanda-quilt-2025.png)

NANDA quilt; via Ramesh Raskar

NANDA’s architecture consists of four major layers: discovery, identity, federation, and interoperability. Together, they aim to enable a world of autonomous but verifiable agents. Here’s a breakdown of each layer:

### **The NANDA Index**

At the base sits **the Index**, a [globally distributed reference index](https://arxiv.org/pdf/2507.14263) that maps an agent handle to a verified metadata file or endpoint.

In [an MIT Media Lab overview](https://www.media.mit.edu/projects/mit-nanda/overview/), the Index is described as a “DNS for agents” that enables “discovery, authentication, and verifiable interaction across the network.”

The idea is that when one agent queries another, the Index routes the request to the relevant registry, validates cryptographic signatures and returns the requested data — all without a central bottleneck.

Currently, the Index is hosted at 15 universities and partner institutions worldwide.

### **AgentFacts**

Every agent must be identifiable and accountable. This is where **AgentFacts** comes in: signed, schema-validated JSON-LD documents describing what an agent can do, who operates it and how to connect securely.

This mechanism brings a “zero trust” mindset to the agentic web. And yes, there is an unfortunate tendency to use the term “Web3” in the various NANDA academic papers, which is a little off-putting. In any case, the point is that agents will verify credentials before engaging.

### **The Registry Quilt**

Perhaps the most evocative metaphor in the NANDA literature is the **Registry Quilt**, a federated fabric of independently run agent registries.

[Mahesh Lambe](https://www.linkedin.com/in/maheshlambe/), a researcher on Project NANDA, [describes the Registry Quilt](https://medium.com/@maheshlambe/deep-dive-project-nanda-part-4-the-registry-quilt-federating-agent-registries-with-gossip-fb30a4179859) as “a federation layer that stitches many autonomous agent registries (Web2 and Web3) into one globally discoverable fabric — without creating a single point of control.”

Somewhat similar to how products like Mastodon and PeerTube operate [on the ActivityPub open standard](https://thenewstack.io/the-creator-of-activitypub-on-whats-next-for-the-fediverse/), the idea is that each entity or organization can host its own registry while remaining discoverable through the global Index.

### **Cross-Protocol Interoperability**

As noted, NANDA already supports Anthropic’s [MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) and Google’s [A2A](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/). It also supports [Natural Language Web](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/) (NLWeb), Microsoft’s emerging standard to integrate AI chat in websites.

In a recent LinkedIn post, Raskar [described A2A](https://www.linkedin.com/feed/update/urn:li:activity:7347037374851301377/) as “roads” and the NANDA Index as “the directory of houses and businesses” in the “city of agents” that Project NANDA is building. The metaphors in such projects can quickly pile up and overwhelm, but the key point is that protocols like MCP and A2A are the technological foundation for NANDA — as they should be if this is to be truly interoperable with agent frameworks from the likes of Anthropic, Google and OpenAI.

## **Developer Activity**

Although research-led, Project NANDA has attempted to kickstart the developer community with several associated projects:

* [Join39](https://join39.org/how-it-works) invites users to “create your personal AI agent, get agent facts, and start representing yourself in the NANDA network.” The [directory](https://join39.org/agents) currently lists over 1,000 agents.
* [List39](https://list39.org/) is an “Agent Facts Registry” that allows you to register your agent as a JSON document.
* The [aidecentralized GitHub project](https://github.com/aidecentralized/) hosts papers, code and registry adapters.
* The [projnanda GitHub site](https://projnanda.github.io/projnanda/#/) contains documentation and demos.

## NANDA’s Controversial AI Business Report

While it’s not directly relevant to the technical architecture of Project NANDA discussed in this article, it is worth mentioning that NANDA released a report in July that was widely publicized. The [report](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) claimed that “95% of organizations are getting zero return” from generative AI (GenAI).

Wharton professor [Kevin Werbach](https://www.linkedin.com/in/kevinwerbach/) disputed this finding in [a LinkedIn post](https://www.linkedin.com/posts/kevinwerbach_state-of-ai-in-business-2025-activity-7365026841759215616-SQWD/) and said the report was “deeply problematic.” [Ajit Jaokar](https://www.linkedin.com/in/ajitjaokar/), a researcher and teacher of Applied Artificial intelligence at the University of Oxford, concurred and [called the report](https://www.linkedin.com/pulse/mit-nanda-report-clever-marketing-gimmick-ajit-jaokar-uiufe/) “a clever marketing gimmick.” More germane to the actual NANDA project, Jaokar noted:

“Uniquely, the report is claiming that the lack of learning, memory etc is holding up enterprise deployment. Of course, NANDA fulfills that objective through a distributed architecture. This ties the conclusion to a product feature.”

## Will NANDA Gain Traction?

NANDA’s statistics might be debatable, but the architecture of the project looks solid enough. Whether that will ultimately matter or not is another story.

Academic institutions like MIT have a history of inventing forward-looking platforms that either never turn into commercial platforms or the ideas are taken by Silicon Valley startups and then become proprietary. The most famous example is, of course, Xerox PARC and the graphical user interface (GUI), which Steve Jobs happily took and brought to market.

It’s clear that some kind of decentralized architecture for agent development and usage would be preferable to one or two big companies owning the ecosystem — as happened with smartphone applications. And with [OpenAI’s nascent ChatGPT application platform](https://webtechnology.news/openai-turns-chatgpt-into-a-web-app-platform/), there’s already a risk that agents will follow the smartphone apps blueprint. So from that perspective, I hope NANDA does help steer agents to an open web future.

Whether or not NANDA itself becomes a mainstream platform, its open design at least provides a credible blueprint for how an *agentic web* might evolve. The ideas here matter: federated discovery, verifiable identity, protocol bridges. Those ideas echo the early web’s design and also the still-emerging world of the open social web (a.k.a. fediverse).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)