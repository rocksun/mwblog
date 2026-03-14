AI needs governance. Amid the exponential growth of predictive, generative, and agentic artificial intelligence, humans everywhere have repeatedly asked, “Is it safe? Can we still control it?”

As AI now evolves to integrate into live production software systems, security and governance platform company [SurePath AI](https://www.surepath.ai/) on Thursday launched a new service, which it says will close the visibility gap for intelligent automation and secure every AI interaction. SurePath MCP Policy Controls provides real-time safeguards that control which [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) servers and tools are allowed to be used by a given codebase.

But [Anthropic launched MCP](https://www.anthropic.com/news/model-context-protocol) to a welcoming audience, and the technology has been lauded as the [USB-C of agentic AI](https://medium.com/@priyasrivastava18official/why-mcp-is-called-the-usb-c-of-agentic-ai-f9bcd256968d), so why should developers be concerned about which MCP they use as their USB?

## Why is MCP not always 1-2-3?

[Cyber security specialists](https://www.securityweek.com/anthropic-mcp-server-flaws-lead-to-code-execution-data-exposure/) highlight read/write access via an MCP server as a potential supply chain attack risk; there’s the data exfiltration and leakage path risk, where API keys, security credentials or user identities could be compromised; there’s the opportunity for proprietary logic to be leaked outwards to a third party, perhaps especially where the MCP connection is made by some element of so-called shadow AI that exists without departmental approval and oversight; and we might also remember that rouge MCP actions can connect to agentic services designed to apply destructive code modifications (without visible rollback paths) that developer’s remain unaware of.

But simply blocking MCP is not practical; it needs to be managed securely with techniques that extend beyond traditional firewall and identity and access management (IAM) policies. While cloud-based MCPs offer some guardrails, they also increase surface area. For instance, multiple agents connected to a mix of local and remote MCP servers can create tangled pathways for data sprawl and lateral movement.

Chief product officer and co-founder of SurePath AI is [Randy Birdsall](https://www.linkedin.com/in/randy-birdsall/). Lamenting how much the rise of MCP mirrors the fanaticism seen when [ChatGPT first became available](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/), Birdsall tells *The New Stack* that he’s seeing rapid adoption, little oversight, and a surface-level understanding of risks.

“We see MCP in use in every organization – and not just by developers, but by business leaders and AI power users who click to connect AI clients and agents to critical enterprise systems. In one of our larger enterprise customers, we identified over a thousand risky or malicious MCP tools in use within the first few hours of enabling MCP Policy Controls,” Birdsall says*.*

## MCP calls on a direct line

Birdsall says that MCP can serve as a “direct line” between generative AI clients and the systems that enable a business to operate. These lightweight MCP tools can run locally on a user’s laptop and are often launched silently by AI desktop apps, such as ChatGPT, Claude, and Cursor. They also link to internal tools, such as Google Drive, Salesforce, and AWS management APIs.

> “Without visibility and control of MCP payloads, organizations are left hoping users apply best practices on their own. YOLO mode is not an effective security strategy.”

This, he says, presents new security challenges, i.e., AI is now issuing real commands, authenticated as the end user.

“One of the biggest challenges organizations have in managing MCP is not just standing up approved resources, but trying to monitor and secure usage of diverse systems that have enabled MCP – from supply chain attacks in the local MCP server ecosystem, to poorly validated authentication flows on remote MCP endpoints of existing SaaS products.

“Without visibility into and control over the MCP payloads between the client and the AI model, organizations are left hoping that users apply best practices on their own. As we’ve seen, YOLO mode is not an [effective security strategy](https://thenewstack.io/how-threat-research-can-inform-your-cloud-security-strategy/),” Birdsall tells *The New Stack*.

## Deciphering destructive decisions

SurePath AI was purpose-built to solve these challenges by applying policy-based control over which MCP servers and tools are allowed to be used before any execution occurs. The technology itself is schema-aware enough to transform these requests, so SurePath AI enforces an organization’s policies on which MCP servers and tools are allowed by controlling local MCP hosts and their connections to them. These policies can use built-in classifications of whether a tool is destructive or not, or be customized explicitly to each organization’s security requirements.

To mitigate risk on the remote side, SurePath AI maintains a catalog of known MCP servers and endpoints. All protected MCP traffic is routed through its platform, where access controls are applied in real time, down to the specific tool level.

SurePath AI’s new capability also uncovers supply chain threats by detecting “never-before-seen” MCP tools that could impersonate other tools or attempt to exfiltrate data outside the approved security perimeter.

## Perfecting the MCP payload

More specifically, within the toolset, the company has built an MCP Tool Discovery function that enables teams to discover MCP tools by monitoring MCP usage in AI tools across the workforce. It works by intercepting MCP payloads and removing tools that are either blocked by policy or in violation of capability requirements, such as tools that are not read-only. When a tool violates policy, it is removed from the MCP payload before being sent to the backend service, which means that the service will not have access to leverage that tool.

SurePath MCP Policy Controls also features an MCP tool block list, an MCP tool allow list, an allow read-only function and catch-all action to provide control over how the system handles tools that fall outside of the defined block and allow lists.

As to whether MCP usage is getting safer or more robust, the answer is likely to be both. The industry is telling us that more developers are falling into the convenience trap of MCP, but more governance and control toolsets, such as SurePath’s, are emerging at the same time.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)