Organizations struggling with massive backlogs of infrastructure policy violations can now look to Pulumi for relief, as the company today announced that its Neo AI [platform engineer](https://thenewstack.io/what-makes-the-ideal-platform-engineer/) can automatically identify and fix [compliance issues](https://thenewstack.io/5-best-practices-for-devsecops-teams-to-ensure-compliance/) across cloud infrastructure at scale.

According to [Craig Symonds](https://www.linkedin.com/in/csymonds/), vice president of Pulumi Insights, the new offering addresses a key pain point for [platform teams](https://thenewstack.io/streamlining-your-platform-teams-workloads/): While security and governance tools excel at detecting policy violations, remediating them has remained a manual, time-consuming process. For companies pursuing frameworks like [HITRUST](https://info.hitrustalliance.net/cybersecurity-framework) or [FedRAMP](https://www.fedramp.gov/), those backlogs can exceed 100,000 violations.

“Platform teams tell us they can’t keep pace with the volume of policy violations their tools identify,” said [Joe Duffy](https://www.linkedin.com/in/joejduffy/), CEO and co-founder of Pulumi, in a statement. “Detection is necessary but not sufficient. Neo addresses the remediation gap by understanding policy violations in context, generating appropriate [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) [IaC] fixes, and applying them automatically when teams choose.”

## From Detection to Remediation

Pulumi’s approach tackles what IDC analyst [Jim Mercer](https://www.linkedin.com/in/jim-mercer/) calls a critical shift in [infrastructure governance](https://thenewstack.io/governance-as-code-your-infrastructures-missing-guardrail/).

“The infrastructure governance challenge has shifted from detection to remediation at scale,” Mercer said in a statement. “Organizations are drowning in policy violation backlogs that grow faster than teams can manually address them.”

The new capabilities extend Pulumi’s [Policy as Code](https://thenewstack.io/is-policy-as-code-the-cure-for-multicloud-config-chaos/) framework beyond prevention into active remediation. While the platform already blocked noncompliant infrastructure from being deployed, it now scans existing infrastructure, identifies violations and uses AI to generate fixes, Symonds told The New Stack in a briefing.

Neo analyzes policy violations in context, generates appropriate IaC changes, and can either apply them automatically with configurable guardrails or route them through approval workflows for human review. The AI agent also has built-in safeguards — it cannot make changes that violate organizational policies, as those guardrails are baked into Pulumi’s IaC engine itself.

## Real-World Impact

Symonds said one customer facing 30,000 HITRUST compliance violations — work they estimated would take over a year to remediate manually — has already resolved approximately 20% of those issues in just a few weeks using Neo’s bulk remediation capabilities.

[Michael Hunter](https://www.linkedin.com/in/mikehunter45/), CEO at [Spear AI](https://spear.ai/), highlighted the broader compliance benefits. “We gave our auditors access to our policy packs because it’s far easier to understand and prove controls in code than in docs and diagrams,” Hunter said in a statement. “With Pulumi’s Policy as Code approach, that manual review process has gone away. We’ve reduced our ATO [Authority to Operate) timeline from a year and a half to expecting approval in three months.”

## Audit, Remediate, Prevent

The enhanced platform follows a three-stage workflow:

* **Audit:** Pulumi scans infrastructure across any cloud provider — including resources not yet managed through Pulumi — and identifies policy violations against pre-built compliance frameworks, including CIS, NIST, PCI DSS, HITRUST, ISO 27001 and SOC 2.
* **Remediate:** Teams can assign violations to Neo in bulk. The AI agent generates pull requests with the necessary IaC changes. For resources not yet under IaC control, Neo first imports them into code, then remediates the violations.
* **Prevent:** Once clean, teams apply the same policies at deployment time, integrating them into CI/CD pipelines to block noncompliant changes before they reach production.

## Developer-Centric Security

Pulumi’s strategy differs from traditional security operations tools by embedding compliance directly into developer workflows, Symonds said. Rather than requiring engineers to context-switch into separate security tools, policy violations appear in the same IaC platform they use daily.

“Developers love doing things the right way initially, if they’re given the information,” he noted. “They hate having to go back three months to work they did three months ago, bring it back up and figure out how to fix security issues they should have fixed then.”

This [shift-left](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/) approach aims to bridge the gap between security teams that identify violations and engineering teams that must fix them — a friction point that has spawned billions of dollars in security tooling investment, Symonds said.

## Availability

The policy capabilities are available to all Pulumi Cloud customers, including Team, Enterprise and Business Critical tiers. Audit scanning and AI-powered remediation through Neo are included for Enterprise and Business Critical customers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)