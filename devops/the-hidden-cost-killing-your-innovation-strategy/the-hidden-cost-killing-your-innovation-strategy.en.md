In today’s AI rush, I’ve seen even the most disciplined organizations find it nearly impossible to enforce the hard-won lessons of [DevOps](https://thenewstack.io/devops-is-still-waiting-for-its-cursor-moment/) and [DevSecOps](https://thenewstack.io/unlocking-devsecops-potential-challenges-successes-future/) into AI adoption. These organizations often feel forced to choose between moving fast and staying in control.

As a result, they develop — almost by default — a “wait and see” approach to AI usage and implementation, creating a new, more dangerous form of [technical debt](https://thenewstack.io/technical-debt-vs-architecture-debt-dont-confuse-them/).

I call it the AI blind spot debt.

It’s the most dangerous kind of debt because it’s being accumulated in the dark. Like all debts, it compounds with terrifying interest, but without a clear balance sheet. The chaos is already here. The only question is whether you’re building a foundation to control it or letting it accumulate until remediation becomes impossible.

## **The Anatomy of a Blind Spot: Why You Can’t See the Debt**

Why is this debt so hard to detect? Because the “factory” for producing AI is no longer just your data science team. The walls have come down, the exclusiveness of AI/ML teams as “model makers” has expanded radically and nowadays every employee is a potential AI user.

In the past, you had a centralized team building models. Today, you have a fragmented ecosystem of users and assets operating completely outside of the IT and security teams’ sight. This blind spot is being created by three distinct forces:

1. Model makers (previously known as data science teams) are no longer just writing code on their IDEs. They are acting as supply chain managers. They are pulling thousands of open source models from public hubs like Hugging Face to fine-tune or use locally. Many of these models are unvetted, and a [recent JFrog analysis](https://jfrog.com/software-supply-chain-state-of-union/) showed a massive spike (7X) in malicious models designed to compromise your environment.
2. Application and web developers are quickly becoming attainable titles. Every employee is consuming commercial AI capabilities via APIs (like OpenAI, Gemini or Anthropic) to build intelligent features to improve their daily productivity and efficiency. However, these models could be sending sensitive customer or patent-protected data to public-facing tools, [through personal accounts](https://www.deloitte.com/us/en/insights/industry/telecommunications/connectivity-mobile-trends-survey.html), often without any security guardrails or traffic monitoring.
3. AI models — whether internally developed, open source or commercial — are not the only assets that require governance and security anymore. The new frontier, presented by widely adopted MCP servers and custom-built AI agents, is possibly the biggest blind spot in this rapid AI adoption across organizations. The governance complexity grows even further when admins have to decide which tools each MCP or agent can use. The days when AI could be responsible for a destructive accident (data deletion, data breach, secrets leaked) are already here.

This is the AI blind spot debt. It is not a single pile of bad code or security risk; it is a chaotic, invisible proliferation of custom models, external APIs and rogue agents scattered across your organization. You cannot govern what you cannot see, and right now, most organizations are flying blind.

## **The Compounding Cost of Waiting**

The most common response I hear from platform and security leaders is, “We’ll tackle AI governance and management … eventually.” But in the face of this invisible proliferation, “eventually” is a trap. A full 63% of companies lack any formal [AI governance policies](https://www.ibm.com/reports/data-breach), and by waiting, they aren’t just delaying a problem; they’re actively compounding it.

Every unvetted model pulled from the internet, every unmonitored API connection and every uncatalogued MCP server is a new thread in a tangled web. The longer you wait, the harder it is to even find all the threads, let alone untangle them.

The cost to remediate this chaos won’t be linear. It will be exponential on three fronts:

* **Security:** It creates massive blind spots, exposing the organization to novel attack vectors like malicious model injection or data leakage via third-party APIs.
* **Productivity:** It forces your AI teams to reinvent the wheel. Lacking a “paved road” to production, they waste time on manual infrastructure setup instead of innovation.
* **Compliance:** It leaves you defenseless against audits. Without clear lineage and license tracking, you risk significant fines or non-compliance with emerging regulations.

## **Stop Accumulating Debt. Start Building Your Foundation.**

So, how do we stop accumulating this debt? You cannot remediate what you cannot see, and you can’t “bolt on” AI governance to a fragmented supply chain after the fact. You must build visibility and control into the foundation of your development life cycle. This is the only sustainable path forward — a way to future-proof your organization, not by predicting the next AI trend, but by creating a unified system that can handle any new model or API securely.

In this new reality, clearing the debt relies on a three-pillar strategy:

1. **A system of record for all AI assets (register).** You simply cannot govern a blind spot. The first step to stopping the debt accumulation is moving from a scattered landscape to a single, unified AI registry. This registry must be comprehensive. It cannot just store code or files; it must catalog all asset types identified or detected across the organization.

2. **An automated policy engine (curate).** Before an AI asset is ever made available in your registry, it must be vetted. This is your vetting of supply chain security and regulations. You need automated policy enforcement to scan for vulnerabilities, malicious code and license compliance issues. This allows you to programmatically block malicious or non-compliant AI workloads before they enter your ecosystem, rather than trying to catch them after they are running.

3. **A centralized control plane (access).** Once you can see and manage your assets, you must control how they are used. A universal AI gateway acts as the single, secure entry point for all AI consumption. This is where you manage connections to external APIs and internal models alike. It provides visibility to monitor for data leakage, enforce rate limits and ensure that employees are only using approved, secure routes to adopt AI.

This strategy isn’t about slowing adoption or adding bureaucracy. It’s about replacing accidental, unsafe growth with deliberate and scalable progress. When every model, API and [agent flows through a governed and observable path](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/), innovation stops being a gamble and becomes a capability you can trust.

Ultimately, organizations that build this foundation now will be able to expand their AI use with confidence, take on new technologies without chaos and [eliminate blind spot debt](https://thenewstack.io/how-to-find-and-eliminate-blind-spots-in-the-cloud/) before it becomes irreversible. On the flip side, organizations that don’t will be left managing a sprawling system they no longer control.

The window to choose your path is closing fast.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/01/6c7e99be-cropped-081c131d-yuval-fernbach.jpeg)

Yuval Fernbach is the cofounder and CTO of Qwak and currently serves as vice president and CTO of MLOps following Qwak’s acquisition by JFrog. In his role, he pioneers a fully managed, user-friendly machine learning platform, enabling creators to reshape...

Read more from Yuval Fernbach](https://thenewstack.io/author/yuval-fernbach/)