Every enterprise company is seemingly trying to adopt the [Model Context Protocol (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/) to connect its AI agents to tools. But so far, authorizing those connections has meant employees clicking through an OAuth prompt for every server. For a while now, the MCP project has been working on the [“Enterprise-Managed Authorization”](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) extension, with the goal of allowing enterprises to control MCP server access centrally through their existing identity provider.

This extension is [now stable](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) and Anthropic and Microsoft are among the first to support it in their clients, including Claude, Claude Code, Claude Cowork, and Visual Studio Code, with Okta as the first identity provider.

After its launch, MCP quickly grew organically, but as is so often the case, [the original spec wasn’t designed for enterprise use cases](https://thenewstack.io/model-context-protocol-roadmap-2026/). The standard MCP authorization model was built for individuals. Authorizing servers, even today, means connecting service after service by hand, but this also means security teams can’t enforce consistent policy or keep a single audit trail — and there is always the risk of an employee connecting a personal account to a work tool.

“Logging in once and automatically having all your MCP connectors automatically set up is pretty magical,” says Tom Moor, the Head of Engineering at Linear, in today’s announcement.

## The token handoff

Enterprise-Managed Authorization makes the identity provider the decision-maker for which servers a client can reach. An administrator sets the policy once, and employees sign in with the corporate identity they already use.

Unlike with OAuth, the exchange runs without a consent screen. During single sign-on, the client obtains a signed assertion from the identity provider that vouches for both the user and the application requesting access. It then presents that assertion to the MCP server’s own authorization server, which returns a scoped access token the client can then use to make its calls.

That assertion is actually an emerging OAuth extension called the [Identity Assertion JWT Authorization Grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/), or ID-JAG, now an IETF draft. Okta’s branded version is [Cross App Access](https://www.okta.com/identity-101/cross-app-access-securing-ai-agent-and-app-to-app-connections/). Because ID-JAG is an open standard, any identity provider could implement it, though Okta is the only one to have shipped support so far.

## Giving control back to IT

![](https://cdn.thenewstack.io/media/2026/06/9dbbb5d9-ema-comparison-1024x563.png)

Credit: MCP

For an IT team, this ideally means an end to the inevitable sprawl of individual approvals. Now, an admin can enable a server for the organization (or specific teams or even individuals), and employees and their agents inherit access to it, scoped to the groups and roles they already hold.

Control and audit move into the identity provider’s console. Access decisions leave one trail across every connector, and revocation runs the same path as everything else, so deactivating a user cuts their MCP access at the same time.

Since corporate IT now controls this connection, mixing and matching personal and work accounts — whether by accident or on purpose — becomes much harder.

In practice, this looks like Anthropic’s and Okta’s implementation, which means Claude Managed Agents can now also be imported into the corporate directory and treated as identities with human owners, while a compliance interface feeds risk signals like dormant agents or misconfigured accounts back to security teams.

## Identity, not authorization

In today’s announcement, Aaron Parecki, Okta’s director of identity standards, calls the result making the identity provider “a centralized governance plane” for MCP access. That governance plane decides who connects to what. It does not decide whether a given action is allowed, though.

It’s worth noting that the permissions the extension hands over are broad. Whether a particular agent should be allowed to run a specific action on a specific resource at a given moment is a decision that is managed by the policy engines and gateways that now typically sit between an agent and the tools it calls.

## What’s next

Beyond Anthropic, Okta and Microsoft, companies like Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase now support the extension. Slack and a number of other companies will soon add support, too.

Okta is also bringing native support for the protocol to its [Auth0 developer platform](https://auth0.com/), letting developers expose their MCP servers without implementing it from scratch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)