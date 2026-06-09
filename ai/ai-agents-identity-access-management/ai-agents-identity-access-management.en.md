**Almost everyone’s workplace experience is now set** to welcome AI-agent-driven actions through the applications we use daily, and this rapid evolution has some serious implications for how [identity and access management](https://thenewstack.io/getting-started-with-identity-and-access-management/) (IAM) works.

While traditional IAM models were developed with human users and their predictable access patterns in mind, AI agents operate differently.

AI agents can quickly perform reasoning functions that impact the way business analytics feeds into board-level management dashboards; they can invoke tools that fuse new connections to an API, update a database, or run a new software script; and they can access other software services and data resources across an organization’s infrastructure and total software stack in dynamic, continuous, and sometimes unpredictable ways.

Cloud infrastructure automation and security company [HashiCorp](https://www.hashicorp.com/en) has sought to provide IAM services capable of servicing the agentic age for some time.

Before [it became an IBM company](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) in February last year, HashiCorp [introduced Boundary](https://www.hashicorp.com/en/blog/hashicorp-boundary) in 2020 as an open-source project to allow software engineers to securely access dynamic hosts and services with fine-grained authorization without direct network access.

IBM senior solutions engineer [Andre Faria](https://www.linkedin.com/in/fariaandre/) and HashiCorp senior technical product marketing manager [Van Phan](https://www.linkedin.com/in/van-phan-726a823/) [blogged on June 4](https://www.hashicorp.com/en/blog/rethinking-infrastructure-access-in-the-age-of-agentic-ai) to explain that as agents now go into live production systems, they will have access to “critical infrastructure resources” such as internal web services, cloud platforms, and other operational systems.

The pair say this is concerning if agents are improperly provided with long-lived static credentials that are poorly managed, rarely rotated, and tough to audit.

## Credentials that are poorly managed: “a dangerous combination.”

“This creates a dangerous combination of broad access and limited oversight. Without proper guardrails, AI agents may autonomously make decisions or execute actions that negatively impact production workloads, corrupt data, trigger outages, or unintentionally expose sensitive information,” write Faria and Phan.

They further note that organizations need a way to monitor which sessions are active, which systems AI agents access, when they access them, what actions they perform, and whether their behavior deviates from policy.

> Because agentic runtimes and individual execution behavior are so inherently fluid and prone to change, we can no longer set identity management, authorization, and session control policies at the point of deployment — every agent needs a unique identity and just-in-time privileges that act as a secure point-of-use access layer.

## It’s time for just-in-time

Because agentic runtimes and individual execution behavior are inherently fluid and prone to change, we can no longer set identity management, authorization, and [session control policies](https://thenewstack.io/how-to-handle-sessions-with-cookies-and-tokens/) at deployment. Every agent needs a unique identity and just-in-time (JIT) privileges (a zero-trust-based secrets management technique that acts as a secure point-of-use access layer) to ensure software systems don’t become brittle or susceptible to attack as they scale.

“With Boundary’s authorization flow, access to a specific resource is granted only when needed, for a specific action, and only for the duration of that session. This helps organizations strengthen governance and maintain tighter control over how AI agents access critical infrastructure,” wrote Faria and Phan.

Boundary applies similar principles to ensure non-human and agentic identities do not have overprivileged access or handle static long-lived credentials. The software also provides monitoring, audit logs, and session recordings that can be used to play back and reveal detailed actions taken by AI agents during session access.

## Adopting dynamic credential brokering

Underlining his original blog, IBM’s Faria tells *The New Stack* that the [IBM 2025 Cost of a Data Breach Report](https://www.ibm.com/reports/data-breach) states that the global average breach costs organizations $4.4 million. He says it also shows that 97% of organizations that reported an AI-related security incident lacked dedicated AI access controls, and 63% did not have any AI governance policies to manage AI or prevent shadow AI.

“The risk highlighted by those statistics, plus the fact that agent compromise is now the fastest-growing attack vector in the industry, showcases why it is urgent to define a solid and secure infrastructure access strategy for agentic AI workflows,” says Faria, who also points to the role [HashiCorp Vault](https://www.hashicorp.com/en/products/vault) plays regarding dynamic credential brokering for Boundary.

Boundary can facilitate the use of dynamic credentials rather than static credentials. When paired with HashiCorp Vault, access with dynamic credentials becomes a reality because Vault’s secrets engines generate short-lived credentials that expire after use. Even if a credential is intercepted, it cannot be used to cause damage.

But is all of this enough?

> “Agents are non-deterministic and operate at machine speed. To contain them, they need hardened, isolated runtimes that govern their behavior before they ever touch production. Cryptographic identity, just-in-time, short-lived privileges, plus ephemeral, trusted runtimes for agents to operate in – that’s the bar.” – Ev Kontsevoy, Teleport.

## An immutable cryptographic hardware root of trust

[Ev Kontsevoy](https://linkedin.com/in/kontsevoy), CEO and co-founder of AI infrastructure identity specialist [Teleport](https://goteleport.com) tells *The New Stack* that just-in-time privileges and auditable control for AI agents aren’t new ideas per se. He advises that every agent today needs its own identity, cryptographically secured by a “hardware root of trust,” i.e., immutable cryptographic keys that reside at the chip level.

“To enforce policy consistently across infrastructure, software engineering teams need a unified identity layer — one that treats humans, machines, workloads, and AI agents the same way, as first-class identities,” Kontsevoy says. “Agents are non-deterministic and operate at machine speed. To contain them, they need hardened, isolated runtimes that govern their behavior before they ever touch production.”

Looking at the live working accounts it touches, the Teleport team reports that credential sprawl in service accounts and tooling remains one of the biggest attack surfaces in production infrastructure today.

“It’s not enough to manage credentials better; we need to eliminate them entirely so they can’t result in standing privileges or unintended actions. Cryptographic identity, just-in-time, short-lived privileges, plus ephemeral, trusted runtimes for agents to operate in – that’s the bar,” Kontsevoy insists.

> “Developer and agent identities often sit on attack paths to critical systems because they can provision infrastructure, retrieve secrets, trigger pipelines, query data stores or inherit trust from other services.” – Justin Kohler, SpecterOps.

## Defining attack paths to critical systems

As we seek to tame the Wild West of agentic access and actions through identity services, we may be overlooking that identity itself can act across cloud, developer, and production environments.

[Justin Kohler](https://www.linkedin.com/in/justin-kohler-49467110/), chief product officer at identity attack path management (IAPM) company [SpecterOps,](https://specterops.io/) tells *The New Stack* that developer and agent identities often “sit on attack paths to critical systems”, meaning they can provision infrastructure, retrieve secrets, trigger pipelines, query data stores, or inherit trust from other services.

“Organizations need to understand where these identities can actually take them, continuously prioritize the paths that create the most risk and then enforce and audit access at the point it is used,” Kohler says. “If those identities are over-permissioned, impersonated or manipulated, the compromise follows the same relationships an attacker would, from one identity, to one system, to the next trust boundary.”

## Integrated authentication & authorization in automated applications

If now seems like the right time to talk about this, the Cloud Native Computing Foundation (CNCF) TAG Security and Compliance committee posted [a blog](https://www.cncf.io/blog/2026/06/04/identity-and-access-management-whitepaper/) to showcase a [new whitepaper](https://www.cncf.io/wp-content/uploads/2026/06/Identity-and-Access-Management-Whitepaper.pdf) last Thursday. The whitepaper supports the foundational security philosophy outlined in the HashiCorp blog above, but underscores the need to embrace open-source, vendor-neutral standards rather than proprietary software.

According to the whitepaper, “Controlling access to systems and data is a fundamental requirement in any environment; in cloud-native environments, this requirement is shaped by characteristics such as highly dynamic and short-lived workloads, the collapse of perimeter-based trust models, and the need to integrate authentication and authorization into automated application lifecycles.”

The takeaway here seems pretty clear: Short-lived workloads and long-lived credentials don’t mix, but just-in-time, short-lived privileges — a period that used to be 90 days, but shrunk to 24 hours, then to minutes, and now down to a period we can call the “ephemeral lifespan” — is now the clock we need to run to.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)