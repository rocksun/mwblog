This week, OpenAI [launched](https://openai.com/daybreak/) Daybreak, its cybersecurity initiative built around [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/), a tiered access framework, and [Codex Security](https://thenewstack.io/openai-anthropic-open-source/) as the agent harness. The Daybreak page followed an earlier OpenAI announcement that describes how [Trusted Access for Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) would scale GPT-5.5 and GPT-5.5-Cyber for verified defenders.

This week’s news lands six weeks after Anthropic introduced [Project Glasswing](https://www.anthropic.com/project/glasswing), an industry consortium powered by [Claude Mythos Preview](https://thenewstack.io/claude-mythos-preview-simulation/) that promised a similar outcome. Find previously unknown vulnerabilities at machine speed, validate exploitability in authorized environments, and help defenders patch before attackers can act.

Convergence between the two labs has been evident for weeks: Mozilla [disclosed](https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/) in April that Firefox 150 shipped with fixes for 271 vulnerabilities identified during a Mythos Preview evaluation, and the GPT-5.5 results that followed sit in a similar range.

**What stands out in this week’s announcement is the overlap among partners.** Three of OpenAI’s launch partners for Daybreak are already inside Anthropic’s Glasswing consortium. Cisco, CrowdStrike, and Palo Alto Networks are running both stacks in parallel rather than picking a side.

> Three of OpenAI’s launch partners for Daybreak are already inside Anthropic’s Glasswing consortium. Cisco, CrowdStrike, and Palo Alto Networks are running both stacks in parallel rather than picking a side.

## Glasswing went narrow, Daybreak went wide

Daybreak and Glasswing make overlapping promises. Use a frontier model paired with an agentic harness to do secure code review, threat modeling, vulnerability triage, patch validation, and detection engineering. The public workflow language is strikingly similar, even if the underlying harnesses and deployment models differ. OpenAI describes Daybreak as combining “the most capable OpenAI models, Codex, and our security partners.” Anthropic describes Glasswing as giving defenders “a head start with our newest frontier model, Claude Mythos Preview.” Strip the brand names and the product briefs read more alike than apart.

What differs is who gets in the door.

Anthropic built a walled garden. Project Glasswing launched with 12 named partners, including AWS, Apple, Google, Microsoft, Nvidia, JPMorganChase, Cisco, CrowdStrike, and Palo Alto Networks, with access extended to roughly 40 additional organizations that maintain critical software infrastructure. Mythos Preview itself is gated. Anthropic has explicitly said it does not plan to release the model to the public. Pricing is $25 per million input tokens and $125 per million output tokens, with $100 million in usage credits committed to keep the consortium running through the research preview. The model is available only through the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry, and only to participants Anthropic has vetted.

OpenAI built a tiered trust framework. Daybreak runs on three model variants. GPT-5.5 is the default with standard safeguards, intended for general security workflows. GPT-5.5 with Trusted Access for Cyber is meant for verified defenders handling code review, vulnerability triage, malware analysis, detection engineering, and patch validation. GPT-5.5-Cyber is the gated red-teamed variant for authorized red teaming, penetration testing, and controlled validation. Launch partners include Cloudflare, Cisco, CrowdStrike, Palo Alto Networks, Oracle, and Akamai, and organizations can [request](https://www.macrumors.com/2026/05/11/openai-launches-daybreak/) a vulnerability scan directly from OpenAI. The framework reads as designed to let access scale within verified tiers. Glasswing reads, by contrast, as designed to hold a narrower line.

## The three vendors playing both sides

The most revealing detail in the May 11 announcement is the partner overlap. Cisco, CrowdStrike, and Palo Alto Networks were already Glasswing launch partners. They signed up for Anthropic’s vetted consortium in early April. Six weeks later, they signed up for OpenAI’s broader framework. The pattern reads less like hedging and more like a deliberate dual-stack strategy.

Security platforms cannot afford to be wrong about which model wins. If Mythos Preview turns out to be the durable frontier, Cisco wants Claude inside its detection engineering. If Daybreak scales faster because the access model is broader, Cisco wants GPT-5.5-Cyber there, too. The same logic explains why CrowdStrike’s CTO publicly endorsed Glasswing as “day one” critical, and why CrowdStrike then appeared on OpenAI’s launch partner list. Defensive security tooling must be model-agnostic at the platform layer, or the platform is exposed to a single vendor’s roadmap, pricing, and access policies.

The bet underneath the dual-stack strategy is that the model is now a substitutable component. The harness, the integration surface, and the partner network are the real product. OpenAI is betting that Codex Security, plus a wider partner net, wins. Anthropic is betting on a narrower consortium with deeper integration wins. The three security vendors playing both sides are betting that neither bet will be wrong long enough to matter.

> Frontier Labs do not love it when their flagship products are commoditized inside someone else’s platform.

There is a second-order implication that is harder to read but worth naming. Frontier Labs do not love it when their flagship products are commoditized inside someone else’s platform. Anthropic has been clear that Mythos Preview will not be sold as a general-purpose API and is restricted to the Glasswing consortium and a small set of cloud-mediated channels.

OpenAI is going the opposite direction with tiered trust, but the GPT-5.5-Cyber variant is gated by verification and account-level controls that look a lot like Glasswing access rules with the serial numbers filed off. Both labs are trying to keep the value of the cyber-capable model inside their own commercial envelope, and both partner rosters are designed to keep the biggest security vendors close enough that the lab still controls the relationship with the end customer.

## The benchmarks say the models are nearly identical

The UK AI Security Institute [evaluated](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities) GPT-5.5 against the same 95-task capture-the-flag suite it used on Mythos Preview in April. On Expert-level tasks, GPT-5.5 hit a 71.4% average pass rate. Mythos Preview hit 68.6%. The gap falls within the statistical margin of error, and AISI notes that GPT-5.5 may be the strongest model it has tested so far. For comparison, GPT-5.4 landed at 52.4% and Opus 4.7 at 48.6% on the same Expert-tier tasks. The capability jump within six months is large. The gap between the two frontier labs is not.

AISI also ran “The Last Ones,” a 32-step simulated corporate network attack that a human expert needs around 20 hours to complete. Mythos finished it three times in ten attempts. GPT-5.5 finished it two times in ten. The absolute numbers are low, but six months ago, no model could complete the simulation at all. Two different labs, two different access models, two different harnesses. The underlying capability looks the same. AISI itself frames the GPT-5.5 results as evidence that cyber capability is now emerging as a by-product of general autonomy and coding improvements rather than a feature specific to one model.

That is the structural insight worth sitting with. When the capability is nearly identical, and the access models are not, the access model becomes the product. The real differentiation in Daybreak is the trust framework, the partner roster, the audit trail, and the verification workflow that wraps the model. The real differentiation in Glasswing is the consortium, the credit commitment, the disclosure protocols, and the open-source maintainer access layer. The model is the engine, but the access model is the car around it.

## Choosing between Daybreak and Glasswing

Security teams now have to evaluate both. The choice is rarely binary, but the tradeoffs are clear enough to put in a table.

| Requirement | Recommended platform | Rationale |
| --- | --- | --- |
| Broad rollout across many security teams | Daybreak | Tiered access scales to more verified defenders |
| Deep integration with a small set of critical systems | Glasswing | Consortium model includes hands-on Anthropic engagement |
| Open-source maintainer access | Glasswing | Based on currently published commitments. Linux Foundation is a launch partner and $4M is earmarked for open-source security donations |
| Red teaming and penetration testing workflows | Daybreak (with caveats) | GPT-5.5-Cyber is explicitly tiered for offensive workflows, and Glasswing also supports vetted penetration-testing work |
| Cloud-native deployment via existing infrastructure | Either | Mythos available on Bedrock, Vertex, and Foundry, while Daybreak runs through the OpenAI API |
| Hedging against vendor lock-in | Both | Cisco, CrowdStrike, and Palo Alto Networks have signed on to both |

Real-world security operations will combine both. The harness is what differs in practice. Codex Security is a code-aware agent with strong tooling around repository scoping, patch generation, and CI integration. Mythos Preview is exposed through standard Anthropic surfaces, with the consortium layer adding governance and disclosure structure. Teams running both will end up routing different classes of work to different stacks, which is exactly the position Cisco, CrowdStrike, and Palo Alto Networks have positioned themselves for.

## What’s next

The frontier model race has produced a recognizable pattern. A capability ships from one lab. A competitor ships an equivalent capability within weeks. The differentiation moves from the model to the wrapper. Cursor and Replit went through this with coding agents. Anthropic and OpenAI are now going through it with security agents. The harness, the access model, and the partner network are doing the work that the model used to do.

For developers building security tooling, the practical implication is to design for model substitutability from day one. The harness is the long-lived asset. The model under it will rotate. Daybreak and Glasswing are the first two cyber AI platforms shipping at frontier capability. The next ones are coming from Google, which is already running Mythos Preview through Vertex AI and shipping its own Security Operations agents, and from open-weight contenders that AISLE and others have shown can replicate flagship vulnerability analysis at a fraction of the cost. The platform fight is going to play out on access, not capability.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)