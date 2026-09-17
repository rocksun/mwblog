**Bob from finance built a scheduling tool last month.** He described it to an AI assistant on a Sunday afternoon, wired it into Slack and three internal APIs before dinner, and by Monday three departments depended on it. That story is funny right up until you check what token it is running on.

## **What changed a few weeks ago**

On July 28, 2026, the [Model Context Protocol’s maintainers shipped a specification update](https://thenewstack.io/mcp-release-candidate-rewrite/) built almost entirely around authorization: issuer validation, issuer-bound client credentials, and Client ID Metadata Documents as the preferred way for clients to register. Put plainly, that is the protocol’s own stewards admitting the original trust model didn’t survive contact with production.

If the people who wrote the spec needed a security overhaul this deep in, the tool Bob built on a Sunday does not get a pass either, and Bob has never heard of issuer validation.

## **Three ways this actually breaks**

Tool descriptions carry instructions, not just documentation. In May 2025, researchers at Invariant Labs showed that GitHub’s own MCP server could be hijacked through a poisoned public issue: an attacker’s text in an issue body was read as an instruction by the agent and used the victim’s token to pull data from private repositories. No compromised code, no malicious tool, just a description field nobody thought to sanitize.

A 2026 benchmark called MCPTox tested this pattern against 45 live MCP servers and 20 models, measuring a 36.5 percent average attack success rate and 72.8 percent against the worst-performing model. Bob’s tool has the same basic shape: it reads Slack messages and ticket text to decide what to reprioritize. It can’t tell the difference between a coworker’s request and a string engineered to look like one, because nobody asked it to.

Scopes default to everything. The common failure isn’t a missing permission model; it is an ignored one. A server that needs read-only calendar access asks for read, write, and admin across the board because that is what the tutorial used. Across the MCP ecosystem, 88 percent of servers require credentials to function, but only 8.5 percent actually use OAuth.

Most of what is running was never scoped in the first place, so there is no scope left to creep. Bob did not sit down and choose a scope. He reused the admin-level API key already sitting in his password manager from a reporting dashboard he set up two years ago, because requesting a narrower one meant filing a ticket, and filing a ticket was the entire bureaucracy he was trying to avoid.

Static tokens do not rotate, and nobody is watching them not rotate. Splunk’s own MCP Server app logged session and auth tokens in cleartext until it was patched in version 1.0.3, tracked as CVE-2026-20205. That vendor has a security team.

By some estimates, over half of MCP servers in the wild run on static API keys or personal access tokens that are rarely rotated, and close to half of enterprise AI activity runs through personal accounts rather than service accounts, meaning the credential doing the work belongs to somebody’s identity, not the system’s.

Bob’s token is that same reporting-dashboard key. It has been valid since it was issued; it will stay valid until somebody remembers to kill it, and the only record of what it has touched this month lives in Bob’s memory — which is not a log.

## **What we have actually seen**

While setting up our own MCP integrations across customer and prospect environments over the past several months, we found that more than 20 percent of the MCP-related access policies we reviewed were either broken or missing entirely.

> We found that more than 20 percent of the MCP-related access policies we reviewed were either broken or missing entirely.

In most cases, the MCP server in question was authenticated with someone’s personal token rather than a service account. None of those tokens had a documented rotation schedule. None of the servers had logs of what they touched. If Bob’s tool had been in that batch, and statistically it probably would have been, nobody would have known until something went wrong, because right now nothing is watching for it to go wrong.

## **The honest caveat**

None of this means every vibe-coded integration needs a change advisory board. Most of what Bob built is harmless, and gating every weekend project behind a formal review process is exactly how you get back to the eighteen-month procurement cycle nobody missed. Governance has its own cost, paid in the good ideas that never ship because process ate the weekend momentum that made them possible.

The problem is not that these tools exist. It is that most organizations currently cannot tell the difference between the harmless ones and the ones holding a token that reaches production, and they are trying to solve that with the same review board that made Bob route around them in the first place.

## **The actual decision**

The question in front of every platform team right now is not whether to allow AI-built integrations. That decision was already made over a weekend, without anyone in the room. It is whether you find out what a given MCP server can touch from an inventory you built on purpose, or from an incident report after the fact. Bob’s scheduling tool is still running. It has not caused an incident, and it probably never will.

But the difference between Bob’s tool and the next one that makes the news isn’t the code; it is whether anyone can say what token it holds, what it can reach, and when it was last rotated.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/610c28f9-shawn-petty-600x600.jpeg)

Shawn Petty is Chief Customer Officer at CloudBolt, where he's passionate about how automation and orchestration drive enterprise digital transformation. He joined CloudBolt from IBM, where he led cloud solutions delivery.

Read more from Shawn Petty](https://thenewstack.io/author/shawn-petty/)