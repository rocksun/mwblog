Okta has made its AI agent governance platform generally available for FedRAMP- and HIPAA-regulated environments, becoming what it claims is the first independent identity platform to extend AI agent lifecycle management inside the compliance boundaries federal agencies and healthcare organizations already trust.

The product, [Okta for AI Agents – Core](https://www.okta.com/en-au/newsroom/press-releases/okta-for-ai-agents-core-brings-lifecycle-governance-to-regulated-environments/), elevates AI agents to first-class identities managed alongside human and machine workforces. This is a shift from the practice of treating agents as static service accounts or hardcoded API keys. The launch comes as federal agencies face mounting pressure from the recent executive order on AI innovation and security, which directs agencies to deploy AI agents and mandates that they secure them.

“The message to agencies is clear: Adopt AI aggressively, but secure it as you go,” writes [Amy Johanek](https://www.linkedin.com/in/amyjohanek/), Okta’s VP of Federal, in a [blog post](https://www.okta.com/blog/ai/governing-fedramp-ai-agents/). “That puts identity at the center of the mission.”

> “The fastest-growing class of NHI yet, and the hardest to see.”

Johanek also writes that AI agents are “the fastest-growing class of NHI [non-human identity] yet, and the hardest to see.” Anyone can spin one up, agents can spawn additional agents, and each connects across apps, APIs, SaaS tools, MCP servers, and data systems with little visibility, she says.

For organizations under mandates to harden systems and defend against AI-enabled criminal access, an unmanaged agent is not just an operational gap; it is more like an unguarded door, the company says.

> “An unmanaged agent is not just an operational gap; it is more like an unguarded door.”

Johanek laid out four specific risks facing agencies running ungoverned agents: compliance violations when agents touch data outside authorized boundaries; compounding breach risk, where a single compromised credential doesn’t grant access to one system but to everything an agent can reach before a human can intervene; failed audits when agents run as orphaned accounts with no owner or evidence trail; and stalled AI adoption when delay becomes the only compliant option.

Moreover, the platform is organized around three governance questions: Where agents operate, what resources they can access, and what actions they’re authorized to take. Agents are registered in [Okta’s Universal Directory](https://developer.okta.com/docs/concepts/universal-directory/) inside an organization’s regulated cell, each assigned a unique identity and a named human owner, Johanek says. Every agent becomes a known, owned, first-class identity inside the environment, whether it came from a third-party platform or the organization’s own developers.

The platform replaces static credentials with scoped, short-lived tokens enforced at runtime. Least privilege is applied across authorization servers, third-party applications, and MCP servers. The governance layer mirrors existing federal workforce identity controls: access certifications, entitlement reviews, time-bound permissions, and a full audit logging stream that can be streamed to SIEM platforms for U.S. Government Accountability Office reporting requirements, Johanek says.

## The offering also provides a kill switch

The offering also provides a kill switch. When an agent deviates from its intended mission or unexpectedly accesses sensitive data, security teams have a real-time mechanism to contain the risk before it escalates into a larger incident.

Johanek says she sees the offering as continuity rather than new infrastructure.  Agencies already trust Okta to manage human identities. [Okta Identity Governance](https://support.okta.com/help/s/article/Identity-Governance-FAQs?language=en_US) achieved FedRAMP High authorization earlier this year; bringing agents into that same identity fabric, she writes, is the natural next step, not a parallel system to build and defend.

However, there is one caveat: Okta for AI Agents – Core is not authorized in Okta for US Military cells.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)