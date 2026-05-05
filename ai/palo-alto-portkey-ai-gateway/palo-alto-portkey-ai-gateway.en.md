For the first three years of the LLM era, the AI gateway was a developer’s problem. You had 10 model providers, each with 10 different SDKs and 10 authentication schemes. The gateway unified them.

Portkey, LiteLLM, Kong AI Gateway, and Cloudflare AI Gateway each solved the same fragmentation problem in slightly different ways. Developers picked one, got a single OpenAI-compatible endpoint, and moved on. The security team was not in the room.

Palo Alto Networks just pulled up a chair.

Last week, Palo Alto Networks announced its intent to [acquire](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-acquire-portkey-secure-rise-ai-agents) [Portkey](https://portkey.ai) and integrate it into [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) as a unified control plane for securing every AI transaction across an enterprise. The deal has not closed, but the strategic signal is clear: The layer that sits between your agent and every model it calls is no longer plumbing. It is a checkpoint.

> The deal has not closed, but the strategic signal is clear: The layer that sits between your agent and every model it calls is no longer plumbing. It is a checkpoint.

Think about what an AI gateway actually sees. Every prompt your agent sends. Every model response it gets back. Every tool call, every memory read, every MCP server interaction. Nothing in your enterprise AI stack generates a more complete picture of what your agents are doing than the gateway layer. The security industry recognized this before most developers did.

Portkey was already processing trillions of tokens per month across Fortune 500 customers when Palo Alto made its move. Three lines of code to implement. Support for 3,000 LLMs, MCP servers, and agents. The developer’s story was clean.

> What Palo Alto is adding to Portkey’s offering is identity, authentication, artifact scanning, automated red teaming, and runtime security.

What Palo Alto is adding is identity, authentication, artifact scanning, automated red teaming, and runtime security. All of it is enforced at the point where every agent call passes through. The gateway becomes the place where you find out what your agents were actually doing, not what you hoped they were doing.

## Security has rewritten the rules before

This is not the first time a security major has rewritten the rules in a developer-owned infrastructure category. The web application firewall started as a network team’s problem. Then developers started routing every HTTP request through it. Cloudflare turned it into a platform. The pattern is the same: developer convenience, then visibility, then control, then acquisition.

What makes this moment specific is the agents. A single agentic workflow can make dozens of LLM calls per task. Each call traverses the gateway. At that volume, the gateway is not a proxy. It is a log of everything your autonomous system decided to do and why. For regulated industries (financial services, healthcare, government), that log is not optional. It is the audit trail.

Kong is already pushing agent gateway capabilities and A2A traffic governance. Cloudflare extended its AI Gateway with unified billing and edge caching in 2026. [LiteLLM](https://github.com/BerriAI/litellm) remains the open-source entry point for teams that have not yet hit production scale.

None of them made a security acquisition. Palo Alto just established that the serious enterprise play in this space sits at the intersection of gateway and security, not gateway and API management.

## The version of this story we’re most likely wrong about is the timing.

The version of this story we’re most likely wrong about is the timing. If agents take longer than expected to reach regulated enterprise workloads, the security layer remains a checkpoint for edge cases. But the trajectory is set.

The AI gateway used to be where your tokens were routed. After this acquisition, it is where your agents are governed.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)