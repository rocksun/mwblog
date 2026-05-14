The security industry has spent decades and billions of dollars building tools to protect systems. The founders of [Cimento](https://cimento.ai/), which came out of stealth mode on Wednesday, think the industry has been looking in the wrong place.

“Humans are one of the continuous weakest links,” [Zain Rizavi](https://www.linkedin.com/in/zainrizavi/), co-founder and CEO of Cimento, tells *The New Stack*. “The cost of AI attacks is going down asymptotically. And the existing tools are not prepared for it.”

Rizavi knows something about building at internet scale. Before founding Cimento, he was on the special projects team at [Cloudflare](https://thenewstack.io/cloudflare-mesh-agent-networking/), where the team’s job was to look beyond the company to determine what the network infrastructure giant should build. What he took from that experience — and applied to Cimento — is the value of an intelligence layer built on real behavioral data.

“What made Cloudflare really good was the intelligence we got on the network,” he says. “We’re now building that same kind of intelligence layer around human behavior inside the enterprise.”

To hear Rizavi explain it, Cimento is an AI-native human risk management platform that builds a living risk profile for every employee. The platform integrates with tools employees already use, such as email, IDPs, cloud providers, and most existing security tools, to provide a unified risk profile for security and compliance teams, helping them understand how individuals typically work within an organization, Rizavi tells *The New Stack*.

Cimento, which raised approximately $3 million in pre-seed funding from Bowery Capital, Indie VC, and angels from Cloudflare, Palo Alto Networks, Nvidia, and Okta, ingests signals from an enterprise’s existing security stack — VPN, endpoint agents like CrowdStrike, DLP tools, cloud data lakes — and runs a Bayesian model to build unified, per-user risk scores.

The goal is to replace the category’s traditional output, such as a phishing email and a two-hour training module, with something that actually reflects how people behave, Rizavi says.

“If I say, ‘Darryl hasn’t taken a two-hour training,’ I don’t think that means ‘zero risk,'” Rizavi says. “That just means no one wants to take a two-hour training.”

“We believe the human layer should be managed with real-time monitoring, responses, and automated remediation. Instead of asking whether an employee completed training,” writes Rizavi in a [blog post](https://cimento.ai/articles/human-behavior-is-security-s-blind-spot.-we-built-cimento-to-fix-it) and asks: “How likely is this employee to be successfully attacked right now, and what should be done about it?”

## Multi-turn phishing

The product’s most distinctive feature is what Cimento calls multi-turn phishing simulation. Rather than sending a single [phishing email](https://thenewstack.io/using-mql-to-stop-novel-email-phishing-attacks/), which is the industry norm, the platform runs iterative, multi-channel campaigns against high-risk user segments: contractors in specific countries, disgruntled employees, people who gave two weeks’ notice and still have production access, the company says.

> “Really good attackers don’t send one phishing email and move on.” —Zain Rizavi

“Really good attackers don’t send one phishing email and move on,” he tells *The New Stack*. He invoked the security concept of “[pig butchering](https://dfpi.ca.gov/news/insights/pig-butchering-how-to-spot-and-report-the-scam/)” — the long-con approach where attackers invest time building trust before striking. “You give it time, and then it becomes much better.”

In practice, a high-risk employee might receive a phishing email, then an SMS, then a voice call, then an encrypted WhatsApp message — each step designed to learn from whether the employee engaged, reported, or ignored the previous one. “You have five or six touchpoints to learn from,” Rizavi says. “And at the end of that, you’re protecting complete trade secrets for your highest-risk users.”

When a risk threshold is crossed, Cimento can trigger automated responses — such as revoking access via [Okta](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/) or another identity provider — without requiring a security team member to intervene manually.

“You don’t need teams spending time actually figuring out what’s going on,” Rizavi says. “We surface the risk, and they press a button.”

## The agent problem

The harder problem, and the one Rizavi said he sees as Cimento’s long-term mission, is extending that risk framework to [AI agents](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/). Today, the company maps agent risk to the human operating the agent: a CFO using an agentic finance tool inherits whatever risk profile the CFO carries. Full agent simulation, Rizavi says, is on the roadmap but not yet shipping.

For [Together AI](https://www.together.ai/), an AI infrastructure company and early Cimento customer, the agent risk question is not theoretical. [Derek Chamorro](https://www.linkedin.com/in/derekchamorro/), Together AI’s head of security, tells *The New Stack* the problem with existing tools isn’t that they’re bad — it’s that they were built for a different threat model.

> “Agents are derived identities. They inherit your permissions, they carry implied trust, and there’s no birthright identity, no immutable fingerprint.” —Derek Chamorro

“The gap I couldn’t close with [KnowBe4](https://www.knowbe4.com/) or [Proofpoint](https://www.proofpoint.com/us) was exactly this,” Chamorro says. “Agents are derived identities. They inherit your permissions, they carry implied trust, and there’s no birthright identity, no immutable fingerprint. Traditional training platforms teach people to spot a phishing email. They’re not built for a world where an agent you trusted last month is operating with all the access you granted it, and neither you nor your security team has any real visibility into what it’s doing.”

Chamorro’s threat model centers on a behavioral pattern he says he sees as nearly universal: once a person has granted an agent access, they stop scrutinizing it.

“They said yes once, so whatever the agent does from there gets implicit approval,” he says. “I’d guarantee 90%-plus failure on a simulation of this attack type — not because our people are careless, but because implied trust is the natural human response after you’ve already granted access.”

The Okta integration is a key reason the architecture made sense to Together AI. “Most tools give you a dashboard,” Chamorro says. “Having a direct path from a risk signal to Okta — where you can actually disable an app or quarantine a user — is how you close the loop.”

For security leaders evaluating Cimento against established players, Chamorro positions the comparison carefully.



“The established players are good at what they were built for. If your threat model is still primarily email phishing and compliance-checkbox training, KnowBe4 and Proofpoint will serve you well,” he says. “But if your org is moving fast on AI, and most are, whether security has caught up or not, you’re dealing with a fundamentally different problem. Don’t evaluate Cimento as a replacement for what you already have. Evaluate it for the risk surface those tools can’t see.”

## Personalization at scale

Rizavi says he sees personalization as the core unlock that prior-generation security tools missed. “There’s never been this level of personalization,” he says, noting that salespeople tend to click on outbound-style lures while engineers at large companies skip email but click links in Slack. “If there’s anything I know about learning, data would always suggest that one-to-one personalization is where the models come in.”

The name Cimento reflects that spirit. Rizavi said he landed on it during a flight back from San Francisco, reading about European scientific innovation in the 1600s. The [Accademia del Cimento](https://en.wikipedia.org/wiki/Accademia_del_Cimento) — Galileo’s scientific society — was built around a core principle: Form a hypothesis, test it, deduce, repeat. “Test and deduce,” Rizavi said. “That’s exactly what we’re doing.”

The name Cimento, Rizavi explains, “has deep roots in the history of scientific rigor.

“Galileo’s own disciples founded the Accademia Del Cimento in Florence, one of the world’s first scientific institutions. Their guiding principle is Provando e riprovando — testing and retesting. Nothing was accepted as true until it had been challenged, observed, and proven under real conditions,” Rizavi writes in his post. “That’s exactly how we believe human risk (and AI agents) should be managed. Not assumed but continuously tested, measured, and refined.”

The company is currently working with a small set of enterprise customers and targeting regulated industries and AI-native companies. Rizavi says the vision is to eventually simulate an attack three months before it happens, based on behavioral data patterns — training the employee before the threat materializes rather than after.

“The attack surface is just increasing,” he says. “At some point, they can gamify the simulations. But you, as a security team, need to exist, because it looked like a text message. It looked like an ex-employee on LinkedIn trying to reconnect. We’ll give security teams the ability to simulate like that.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)