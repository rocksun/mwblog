The Linux Foundation on Tuesday declared its intent to launch the Agent Name Service (ANS), an open standard that gives AI agents [verifiable identities](https://thenewstack.io/ai-agent-identity-crisis/) by tying them to the internet’s domain name system (DNS).

The idea behind the ANS has actually been around for a while. It began as a research paper published in May 2025 by the [OWASP GenAI Security Project](https://genai.owasp.org/), written by a group of application-security researchers. Its authors include Ken Huang, the CEO of security consultancy DistributedApps.ai and a co-author of the widely cited OWASP Top 10 for LLM Applications that chronicles the top security risks related to LLMs, and Akram Sheriff, an AI security engineer at Cisco.

ANS is a bit of a redesign of the original idea, which has gone through a few iterations since it was published. The [2025 original](https://arxiv.org/abs/2505.10609) described ANS as a “universal directory” — basically a central registry with naming borrowed from DNS. A second version, published as an [individual draft](https://datatracker.ietf.org/doc/draft-narajala-courtney-ansv2/) at the Internet Engineering Task Force in April, takes this a step further and ties each agent instead to a real domain its operator already controls.

## How it would work

The design essentially copies how websites already prove who they are today. An operator demonstrates control of a domain like example.com through ACME, the automated protocol behind Let’s Encrypt, and a registration authority issues the agent a pair of certificates. Every change to the agent’s status, from registration to renewal to revocation, is written to an append-only log. A client checking an agent can choose how much assurance it wants, from a basic certificate check to a tier that also consults the log.

It’s worth noting that the ANS system separates identity from discovery and hands the job of finding agents to other services built on top.

## The DNS industry and AI agents

Discovery is actually handled by [DNS-AID](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/), a separate discovery standard the foundation took in on May 27. It lets agents publish their endpoints as DNS records so other agents can find them. DNS-AID was originally built by Infoblox, and GoDaddy, which is also involved in ANS, is among its backers.

Agent identity and discovery projects based on DNS aren’t limited to these two Linux Foundation projects, though. Including those two, there are now at least four similar proposals. There is DNSid, for example, a durable-identity scheme from the registry operator Identity Digital, and AID, a minimal discovery draft that came out of the developer community.

Vineeth Sai Narajala, a co-author of ANS now with OWASP, says in the announcement, “we didn’t need to reinvent the wheel, we needed to extend the foundational trust of the internet to a new generation of autonomous technology.”

Not reinventing the wheel also means basing this system on the registrars and certificate authorities that come with it and the trust hierarchy they built, which security researchers have long considered [fragile](https://meetcyber.net/dns-is-still-one-of-the-internets-most-fragile-control-planes-a2b89a6530ab).

Maybe it’s no surprise that many agent identity and discovery solutions are coming out of the domain industry. GoDaddy, after all, registers domains, Identity Digital operates top-level domains, and Infoblox, which backs ANS, sells DNS infrastructure. For all of them, DNS-linked agent identity and discovery extends a (profitable) business they already run.

## What about A2A and co.?

As is so often the case, the Linux Foundation is playing host to [several alternative](https://thenewstack.io/agentic-ai-foundation-launch/) systems. Google’s [A2A protocol,](https://thenewstack.io/google-donates-the-agent2agent-protocol-to-the-linux-foundation/) for example, gives agents a signed “Agent Card” they can publish at a known web address, with an agent registry on its roadmap. Cisco’s [AGNTCY](https://thenewstack.io/cisco-donates-the-agntcy-project-to-the-linux-foundation/) ships an agent directory and its own cryptographic identity service. Outside the foundation, Microsoft’s Entra Agent ID and [Okta for AI Agents](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/), both generally available since the spring, treat an agent as an identity managed inside the corporate directory, with short-lived tokens that tie each action back to the person who authorized it.

And while Cisco is backing both ANS and AGNTCY, some names are missing here, including major players like Google, Anthropic, Microsoft, and Amazon. Given their outsized role in the agent ecosystem, it’ll be interesting to see if they’ll join in this effort or decide on their own standards (insert obligatory xkcd comic [here](https://xkcd.com/927/)).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)