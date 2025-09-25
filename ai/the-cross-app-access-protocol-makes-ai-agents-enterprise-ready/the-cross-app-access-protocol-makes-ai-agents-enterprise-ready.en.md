*Okta provided this writer with travel assistance to attend its Oktane conference.*

LAS VEGAS — Most enterprises are now using [AI agents](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/) in some form, but few have any governance systems in place to control them. A new open protocol, Cross App Access (XAA), backed by the likes of Okta, [AWS](https://aws.amazon.com/?utm_content=inline+mention), Box, Glean, Grammarly, Miro and Writer, aims to bring agents into existing [identity management](https://thenewstack.io/banking-on-identity-management-to-boost-revenue/) solutions to govern what kind of data they can access.

XAA treats agents as first-class entities inside existing security and identity management services like [Okta](https://www.okta.com/). This, in turn, also means that security teams can claw back some of the controls and visibility they are currently losing as developers trial and deploy agents with very little oversight.

The protocol is meant to be complementary to existing ones like Anthropic’s Model Context Protocol (MCP) and Google’s Agent2Agent (A2A). XAA isn’t about how the agents talk to their tools but about ensuring that these agents can securely access applications and only get access to the applications and data that they’re supposed to have access to.

“Companies have a massive exposure right now when agents are getting from prototype into production without proper governance to make sure that the agentic identity is properly managed, that it’s in a directory, that it’s authenticated, that it’s authorized and that there’s proper governance in place,” [Eric Kelleher](https://www.linkedin.com/in/erickelleher/), the president and COO of identity management service Okta, said earlier this week at his company’s annual Oktane user conference.

Currently, if an agent needs access beyond anything the primary users access, there are essentially two ways to do this. Most developers will simply use an API key. “That’s terrifying for a CISO, because you effectively have to give this agent — this nondeterministic entity — the keys to the kingdom,” [Jack Hirsch](https://www.linkedin.com/in/jackhirsch/), Okta’s VP of product, told me.

![cross app access control diagram](https://cdn.thenewstack.io/media/2025/09/d33613ae-caa-okta.png)

Image credit: IETF.

The other option is user-controlled OAuth grants, but those can quickly become overwhelming and very difficult to track for a security team. “It shifts the burden of security from the security organization down to the end user — and in the enterprise, it’s a horrible user experience,” Hirsch added, because a new employee, for example, would have to go through dozens if not hundreds of OAuth flows to even get started on doing real work.

XAA is meant to make all of this much easier by giving the security operators control over the access control for these agents, and since it’s an [extension of the OAuth standard](https://oauth.net/cross-app-access/), from a developer’s perspective, XAA shouldn’t be too much of a disruption either.

“It shifts the burden of authorization from end users in the enterprise up to the admins. And from a builder standpoint, all it is is, before you do the OAuth dance, check with the [identity provider],” Hirsch explained.

As it turns out, Okta started working on the XAA protocol well before AI agents or even large language models (LLMs) were industry buzzwords. And it’s not limited to AI agents either, of course, but the proliferation of AI agents has now pushed the problem XAA is trying to solve to the forefront.

Okta and others are now trying to push the industry to adopt XAA. Internally, Okta and Auth0, Okta’s developer platform that makes it easier for developers to build authentication and authorization into their applications, will use XAA to implement fine-grained permissions. Auth0 will support XAA in its APIs and SDKs soon, and Okta will make it a core part of its platform fabric.

“As autonomous AI agents take on increasingly complex tasks across mission-critical operations, from finance and compliance to customer service, enterprises need full visibility and governance over every interaction between agents, models and tools,” said [Adi Kuruganti](https://www.linkedin.com/in/adikuruganti27/), chief product officer of XAA backer Automation Anywhere. “Cross App Access provides a critical new standard for building the trust required to securely scale these powerful capabilities across the enterprise.”

The core problem XAA is solving is very real and not something that MCP or A2A currently tackle. As with all new standards, though, and especially in this quickly evolving AI ecosystem, it remains to be seen what the industry finally agrees on.

XAA has powerful enough backers to have a good chance to become that standard, but as we’ve seen with protocols like MCP, a completely new protocol may suddenly become available and get rapidly adopted by the community without any industry group ever getting involved.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)