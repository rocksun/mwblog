As enterprise IT systems grow more complex, maintaining visibility, performance and resilience across distributed architectures has never been more critical. The rise of agentic AI — AI capable of autonomous analysis and action — is redefining how organizations approach observability and operational resilience. The result is a more proactive, adaptive operations model that dramatically lowers mean time to resolution (MTTR) and allows teams to focus on innovation rather than incident response.

[Agentic AI](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) refers to systems that can autonomously perform complex, multistep tasks by planning, reasoning and acting with minimal human input. Unlike traditional AI, which reacts to direct commands, agentic AI is proactive and goal-driven, capable of adapting to changing conditions.

But autonomy alone isn’t progress. The capabilities that make [AI agents](https://thenewstack.io/ai-agents-in-it-from-hype-to-hands-on-impact) so valuable can also make their behavior difficult to monitor, understand and control. Achieving agentic AI’s potential depends on embedding security and accountability into every stage of automation and using [observability](https://thenewstack.io/observability/) tools that are designed to monitor an AI agent’s performance and flag any deviations from standards. Without those foundations, the same systems that deliver speed and efficiency can introduce new operational risks.

## Balancing Automation and Human Oversight

Enterprises must consider human in-the-loop (HITL) architecture when they begin designing agentic systems — not as an afterthought. The objective is to combine automation’s efficiency with the reliability and governance required for trust.

At IBM, as I’ve said before, this balance follows a three-step continuum:

* **Automated execution:** Low-risk, reversible tasks — such as log analysis or test-environment operations — can be fully automated with minimal oversight.
* **Supervised automation:** Medium-risk processes require a review-and-approve step, where humans validate AI actions before they execute.
* **HITL execution:** High-risk operations — such as customer communications or production changes — must remain under direct human control.

As trust in automation grows, organizations can move more supervised processes into the automated category, especially in nonproduction environments. My experiences with customers has revealed that about 60% to 70% of automation currently occurs in development and test systems, with 30% to 40% in production.

## The Double-Edged Sword of Autonomous Observability

[Observability platforms](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342025;dc_trk_aid=627069060;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) have evolved from simple log collection to advanced AIOps capable of anomaly detection and correlation. The next frontier should include agentic observability — systems that can interpret telemetry, detect failures and act to correct them.

> Automation without accountability is a risk at scale.

These capabilities could transform IT operations by eliminating manual triage and enabling proactive resolution. But they also introduce new risks; an AI process might misinterpret a traffic spike as an attack or infer a false correlation between service logs.

Automation without accountability is a risk at scale. In my view, every AI-driven decision must be traceable, explainable and governed. Without transparency and oversight, black-box automation can erode trust and slow adoption of otherwise transformative technologies.

## Metrics and Frameworks for AI Accountability

Several frameworks have emerged over the last two years to promote transparency and accountability in AI systems:

These frameworks help organizations track AI behavior, document compliance and ensure explainability — understanding *why* the system acted, not just what it did.

Additional initiatives such as [Google’s Model Cards](https://modelcards.withgoogle.com/) offer templates for documenting model provenance and behavior. Together, these standards can help make AI systems traceable and auditable.

## Why Agentic AI Needs New Safeguards

Unlike traditional analytics tools, agentic AI doesn’t just observe, it acts. This autonomy requires new safeguards across several dimensions:

* **False positives and hallucinations:** Generative models can [misidentify patterns](https://arxiv.org/abs/2509.04664), causing unnecessary or harmful interventions. Modern observability tools use AI-specific telemetry to surface anomalous responses or repeated retries that indicate poor model grounding, prompting retraining or parameter updates.
* **Loss of oversight:** [Overreliance on automation](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/) can obscure underlying system drift. Observability tools can help detect drift by monitoring changes in response patterns or variations in output, then alert teams to update configurations or documentation to eliminate the deviations.
* **Security exposure:** Agents with excessive data access can become [attack surfaces.](https://arxiv.org/pdf/2506.07153) For example, as cybercriminals develop new tactics, agents may become less reliable at detecting fraud. Observability tools can identify when agents access or invoke services beyond authorized boundaries, so teams can retrain the model to close security gaps.
* **Compliance risks:** Unexplainable AI decisions can trigger regulatory violations under frameworks like the EU AI Act. An observability tool can provide trace data to support auditability and explainability requirements under these frameworks.

Each of these challenges underscores the same principle: [Trustworthy automation](https://thenewstack.io/automated-systems-scalability-reliability-and-security/) depends on transparency, explainability and accountability.

> Trustworthy automation depends on transparency, explainability and accountability

## Blueprint: AI Built With Guardrails

IBM sees agentic AI as both an opportunity and an obligation. From my view, the next generation of observability platforms needs to be designed around three key components:

* **Transparency by design:** Every AI action must be auditable, with clear data lineage showing what informed a decision and why.
* **Security by design:** Observability data, often highly sensitive, must be protected with encryption, identity controls and strict permissions.
* **Governance by design:** Policies should dictate when AI can act autonomously and when human validation is required — what IBM calls policy-driven automation.

These guardrails define responsible automation, combining AI’s efficiency with enterprise-grade trust.

## Practical Guardrails for Responsible AI Ops

In addition to general [best practices](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798594;dc_trk_aid=627070515;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) for augmenting human intelligence with AI, consider these strategies for integrating agentic AI into observability and operations.

* Deploy [AI gateways](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798591;dc_trk_aid=627070806;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) that validate and authorize actions before execution, ensuring compliance with security and change policies.
* Establish [AI observability pipelines](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433799998;dc_trk_aid=627070512;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1). Treat AI models and agents as first-class observable components. Capture MELT for every agent action, model inference and data interaction to enable full lineage tracking and explainability.
* Monitor model drift and reasoning transparency. Implement continuous validation and drift detection for [large language models](https://thenewstack.io/taming-llm-sprawl-why-enterprises-need-an-ai-gateway-now) and agentic AI systems. Observability tooling can provide the trace data that helps highlight deviations in reasoning or decision-making pathways.
* Implement [secure data governance](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342457;dc_trk_aid=627070800;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) so that AI models access only the telemetry data they need.
* Tie [resilience scoring](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798597;dc_trk_aid=627069063;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) to observability metrics for unified visibility into system health and recovery readiness.
* Maintain a [human-in-the-loop architecture](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434342022;dc_trk_aid=627070803;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) for high-impact or customer-facing systems. AI should assist, not replace, human judgment.

These principles are quickly becoming operational necessities as enterprises move toward self-healing, AI-driven environments.

## Building Confidence in the Next Era of Observability

AI must extend human intent, not replace it. With strong guardrails and transparent design, enterprises can use agentic AI to [automate IT resilience](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798594;dc_trk_aid=627070515;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1), reduce MTTR, and [build operational confidence](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434004125;dc_trk_aid=626964671;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1).

Ultimately, observability is about assurance — knowing systems perform as expected and automation acts responsibly when it matters most. When implemented with transparency and governance, agentic AI can build confidence to a new level.

The organizations that succeed in the next wave of digital operations will be those that pair intelligence with integrity — harnessing AI to drive innovation without compromising accountability.

The future of observability isn’t just autonomous. It should be accountable, explainable and secure — the foundation of resilient enterprise systems built to last.

*Learn more about how [IBM Observability](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.433798585;dc_trk_aid=627069066;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) can help drive resilience, cut costs, and optimize IT with integrated, AI-powered operational intelligence.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/11/458db02c-cropped-dd86a287-2672-4fb6-85ac-395e138c9b86-600x600.jpg)

Vikram Murali is VP of Product Management, Development and Design for IBM Automation, specializing in IT Automation and Observability. IBM Automation develops and provides several leading enterprise offerings to increase IT Operational Efficiency, Securely Integrate Apps & Systems to Remove...

Read more from Vikram Murali](https://thenewstack.io/author/vikram-murali/)