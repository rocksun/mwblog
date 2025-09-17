According to the most recent [Open Source Security and Risk Analysis Report (OSSRA)](https://www.resilientcyber.io/p/the-2025-open-source-security-landscape), 97% of all scanned codebases contain [open source components](https://thenewstack.io/open-source/), with an average of more than 900 such components per application. Moreover, nearly two-thirds of these components are transitive dependencies. That means they’re libraries that are pulled in indirectly — and many teams may not even realize they’re using them.

This widespread reliance on open source, with each open source component following its own support policy and timeline, exposes organizations to dormant risks that extend beyond security vulnerabilities. If not managed, these risks can surface unexpectedly and at an unexpectedly large scale. Comprehending these risks is the first step, but consistently and effectively controlling them is crucial.

## **Understanding Open Source Support Life Cycles**

Unlike commercial software that typically brings with it predictable multiyear support timelines, [open source support](https://tuxcare.com/blog/open-source-security/) follows a different path:

1. **Community support phase:** Most projects begin with active development driven by maintainers and contributors. Security fixes, new features and updates are released regularly, but the length and consistency of support timelines vary widely from project to project.
2. **Optional enterprise support extension:** When community support ends, some popular projects offer paid enterprise support extensions with defined life cycles. These can provide security patches and stability updates for several more years, but most projects don’t offer this extension option.
3. **End of life (EOL):** Once all support ends, either at the close of community maintenance for smaller projects or after enterprise support for larger ones, no further fixes are released. At this point, organizations face pressure to upgrade — and it can be on fairly short notice.

This model creates a patchwork of support timelines. In a typical application, each component may be on a different clock, meaning some libraries might be fully supported while others are already out of maintenance. For discerning organizations that place a heavy [focus on security and compliance](https://thenewstack.io/security/), this can cause nearly unending headaches.

## **The Scale of Outdated and Vulnerable Components**

While open source accelerates innovation, keeping components current remains an obvious yet unanswered challenge. The 2025 OSSRA research illustrates just how widespread the problem is:

* 86% of codebases include vulnerable open source components.
* 91% use outdated packages, with most lagging more than 10 versions behind the latest release.
* 81% contain high- or critical-risk vulnerabilities.

These numbers show just how systemic the problem is today. Organizations aren’t just running a few outdated libraries. They’re running hundreds of such libraries, often without realizing how far they’ve drifted from the latest supported versions.

The result is not only a security gap that can be exploited by cybercriminals, but also an operational burden, as teams attempt to manage support timelines for hundreds of different open source components across the stack.

## **EOL and Compliance Risks**

That pressure to remain secure becomes even more serious when viewed through a compliance lens. Mandates, including FedRAMP, PCI DSS, HIPAA, and ISO 27001, require vulnerabilities to be patched within strict timeframes, often just days or weeks for critical flaws. But when a component is already at its end of life, there’s no guarantee a patch will ever be available.

Even if no vulnerabilities are currently known, auditors typically flag [EOL components as a compliance risk](https://tuxcare.com/blog/end-of-life-vs-end-of-support/) because they can’t be reliably patched. And since EOL status is often uncovered late in the cycle, organizations frequently rush upgrades to avoid audit findings or regulatory penalties, and that hasty action can cause additional issues.

These mandates apply to the entire dependency chain, making no distinction between direct dependencies and transitive ones. If EOL components appear in an organization’s [software bill of materials (SBOM)](https://thenewstack.io/how-to-create-a-software-bill-of-materials/) or scanning reports, auditors often flag them, since they represent unpatchable risk. And if a vulnerable component exists anywhere in the supply chain, no matter how deep, it needs to be addressed.

Meanwhile, a new wave of regulations targets a different audience: device and appliance manufacturers. Programs such as the [US Cyber Trust Mark](https://www.fcc.gov/CyberTrustMark) and the [EU Cyber Resilience Act](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) require vendors to provide security patches for all software components running on their hardware, including open source dependencies, for the entire product life cycle.

In other words, traditional frameworks (PCI DSS, HIPAA, ISO 27001, FedRAMP) place the responsibility on software operators, while emerging regulations (Cyber Trust Mark, Cyber Resilience Act) shift that responsibility upstream to the device manufacturers. That’s a significant new burden. Either way, unsupported or outdated open source packages are no longer just a technical liability; they can become a notable regulatory liability as well.

## **Why Upgrades Are Never Simple**

Even when upgrades are carefully planned, they are rarely straightforward. Teams often begin by rewriting application code to address breaking changes or altered behaviors. From there, they must update dependency chains to resolve conflicts and ensure compatibility.

Tooling and infrastructure usually need attention as well. Build systems, [CI/CD pipelines](https://thenewstack.io/introduction-to-ci-cd/), packaging, deployment scripts and even container images often require adjustment to align with a new version. After that comes the testing. Regression, integration, security and performance testing all have to be performed to ensure the upgrade hasn’t introduced unexpected side effects.

Finally, teams must handle the change management process (i.e., planning rollouts, preparing rollback strategies, updating documentation and ensuring staff are trained on the new environment). In practice, what looks like “just an upgrade” can ripple across code, dependencies, tooling, infrastructure and processes, consuming tons of time and resources.

## **The Cost of Rushed Upgrades**

[Compliance service-level agreements (SLAs) and new vulnerability disclosures](https://tuxcare.com/blog/end-of-life-software/) frequently collide with unsupported components, leaving organizations little choice but to rush an upgrade. That urgency typically amplifies risk and cost.

Rushed upgrades can trigger a wave of post-upgrade incidents, as bugs and urgent issues create instability across engineering and operations, pulling teams off roadmap work and slowing delivery. Under deadline pressure, teams may also cut corners, and those shortcuts often harden into lasting technical debt that just piles on top of future maintenance burdens.

The financial impact is no less significant. Shortened timelines translate into unplanned costs, from overtime pay to temporary infrastructure, extended testing environments or emergency consulting. At the same time, hasty implementation can inadvertently introduce new risks, such as misconfigurations or fresh vulnerabilities that end up undermining the security the upgrade was meant to restore. It’s quite the predicament.

So, while upgrades are difficult under the best circumstances, rushed upgrades can transform a necessary maintenance activity into a source of instability, cost and overruns.

## **Options Beyond Just Upgrading**

Not every application can or should be upgraded on the schedule dictated by compliance deadlines or sudden vulnerability disclosures. Business priorities, integration complexity and the risk of disruption often make “just upgrading” an impractical answer.

For years, organizations had limited alternatives. Extended support was sometimes available, but usually only for specific components. The rest of the stack remained uncovered, leaving teams with little choice but to accelerate upgrades once community support ended.

Today, that picture is changing. New services offer extended support for a broad range of open source components across operating systems, runtimes, libraries, development frameworks and applications. By providing ongoing security patches along with compatibility assurance, complete dependency tree coverage and provenance tracking, organizations can remain secure well beyond the official end of life. These capabilities help ensure that the software remains auditable while also continuing to maintain strict compliance through timely remediation across the software supply chain.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/09/133a4732-artemkarasev.jpg)

Artem Karasev is senior product marketing manager for TuxCare’s Endless Lifecycle Support for Open Source Software.

Read more from Artem Karasev](https://thenewstack.io/author/artem-karasev/)