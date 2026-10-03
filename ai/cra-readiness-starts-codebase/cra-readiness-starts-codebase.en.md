The Cyber Resilience Act (CRA) is often discussed as a policy or reporting challenge. But for organizations that build products with digital elements, its practical impact will be felt much earlier and much closer to the code: in pull requests, build pipelines, release approvals, dependency records, and test suites.

That is because an organization cannot credibly report on an [exploited vulnerability or severe incident](https://thenewstack.io/openai-agents-security-bypasses/) if it cannot first answer basic engineering questions. Which versions are affected? Which component introduced the exposure? Was a security control changed? Can the release be reproduced? Did the fix actually work in the running product?

Manufacturers of products with digital elements in the scope of the CRA must report actively exploited vulnerabilities and severe incidents through the EU’s reporting process since September 11 of this year. Broader CRA obligations begin to apply in December 2027. These dates matter, but the more useful question for engineering leaders is not, “Are we compliant?” It is, “Can our software delivery system produce reliable security outcomes—and prove it?”

The answer is rarely found in a single security tool or a last-minute compliance exercise. It comes from repeatable controls embedded in the software lifecycle.

## Move from policy statements to observable controls

Many organizations already have secure development policies. The gap is often between what the policy says and what the codebase, pipeline, and release evidence can demonstrate.

> “High-risk failures should not depend on someone noticing them; the delivery system should prevent them from progressing.”

A practical way to find that gap is to assess each control at one of four maturity levels:

* **Not evidenced:** The control is absent, or nobody can show that it exists.
* **Ad hoc:** It happens sometimes, often through individual effort or a manual process.
* **Standard:** The control is defined, consistently applied, and supported by evidence.
* **Enforced:** The control is automated & required where it should be and can stop unsafe work from progressing.

“Standard” is an important threshold. A control that depends on a single knowledgeable engineer, a spreadsheet, or a pre-release scramble is not yet dependable at the speed of modern delivery. High-risk failures should not depend on someone noticing them; the delivery system should prevent them from progressing.

## Seven questions that expose readiness gaps

The following questions provide a codebase-focused starting point. They do not substitute for legal advice or a complete CRA program. They do, however, reveal whether the engineering system can prevent avoidable weaknesses and generate the evidence needed when something goes wrong.

### 1. Are secure defaults built into the product?

Security should not rely on a customer, operator, or deployment team remembering to disable unnecessary capabilities, tighten permissions, or turn on protection after installation. Secure-by-default behavior means the safer configuration is the initial configuration.

This is particularly consequential for external-facing products. A feature that is exposed by default can turn a configuration oversight into a vulnerability with a much wider blast radius.

### 2. Can you identify and scrutinize security-sensitive changes?

Not every change needs the same review path. Changes to authentication, authorization, cryptography, secrets handling, update mechanisms, logging, and network exposure deserve additional attention.

Teams need a way to flag those changes, route them for the right review, and test them with risk in mind. During an incident, this discipline also creates a trail for investigators: what changed, who reviewed it, what evidence supported the decision, and which versions inherited the change?

### 3. Can every release be traced to its source and components?

A release label alone is not enough. Organizations need to connect a released artifact to the exact source revision, build inputs, and dependencies that produced it.

This traceability underpins effective impact analysis. When a vulnerability is disclosed, teams must quickly determine whether a component is present, in which versions, under what configuration, and in which customer-facing releases. [Software bills of materials](https://thenewstack.io/lineaje-unveils-sbom360-hub-for-software-bills-of-materials/) (SBOMs) are an essential part of that picture, but the operational goal is broader: mapping a finding to the actual product artifacts in the field.

### 4. Do applicable security checks run before code merges?

Security checks that happen only before a major release find problems late, when the cost and disruption of remediation are greatest. A stronger model brings appropriate checks into the everyday development workflow, including pull requests and continuous integration.

The word “applicable” matters. A small documentation change should not be treated like a modification to access-control logic. But where a check applies, it should run reliably, not only when a developer remembers to request it. Tools like [**SonarQube**](https://www.sonarsource.com/products/sonarqube/) that surface code quality and security findings directly in pull requests help developers address issues while the change is still small and contextual.

### 5. Can serious findings block a build or release?

Visibility is valuable; enforcement changes outcomes. If a serious, unresolved finding only creates a dashboard alert, organizations depend on time, judgment, and competing delivery priorities to keep known risks out of a release.

> “Visibility is valuable; enforcement changes outcomes.”

Teams should define release-blocking thresholds based on their product risk assessment, then make exceptions explicit, time-bound, and accountable. The goal is not to stop shipping indiscriminately. It is to make the organization’s risk decisions visible and intentional.

### 6. Do tests exercise hostile and unexpected behavior?

[Functional tests typically prove](https://thenewstack.io/introduction-to-software-testing/) that software works under expected conditions. Security testing must also ask how it behaves with malformed input, misuse, abuse attempts, and efforts to bypass controls.

That means treating negative testing as a first-class engineering activity, especially around security-critical flows. For example: Can authorization be bypassed? What happens when an update is interrupted? Does an API fail safely under malformed requests? Does rate limiting work under load? The answers help prevent exploitable conditions from reaching production and give teams a clearer view of severity when defects are found.

### 7. Do release tests validate security behavior at runtime?

A code review can establish intent, but it cannot fully prove runtime behavior. Products need release-level evidence that protections such as update integrity, rollback protection, isolation, secure deletion, and resilience under stress behave as designed in their real deployment context.

This matters after an incident, too. Teams must be able to test the proposed corrective measure, understand its effect on the product, and show that it does not introduce a new weakness.

## Prioritize by exposure, not by checklist order

A seven-question assessment should lead to a risk-weighted action plan. A missing secure default in an internet-facing product may deserve immediate attention. A gap in pre-merge automation for a low-risk internal component may be important but less urgent.

The practical prioritization factors are familiar: product exposure, criticality of affected functions, exploitability, data sensitivity, the availability of mitigations, and the number of released versions affected. What changes under the CRA is the value of having those facts available quickly and defensibly.

This is also where organizations should resist treating evidence as paperwork. Evidence is operational capability. Build records, dependency inventories, review trails, test results, and exception decisions shorten the time between discovering a problem and understanding its scope. They help teams make better remediation decisions under pressure.

## Make resilience part of the delivery system

The most durable response to the CRA is not a separate compliance workflow that developers visit occasionally. It’s a delivery system that integrates secure defaults, traceability, testing, and release controls into the work teams already do.

That approach matters more as [agentic development](https://thenewstack.io/coding-agents-developer-neglect/) accelerates code creation. In Sonar’s [State of Code Developer Survey](https://www.sonarsource.com/blog/state-of-code-developer-survey-report-the-current-reality-of-ai-coding/), 96% of developers said they do not fully trust AI-generated code, yet only 48% said they always verify it before committing. This verification gap makes consistent controls essential: regardless of whether code originates with a developer or an agent, teams need automated checks that identify sensitive changes, validate security controls, and preserve release traceability.

> “The CRA is a regulatory obligation, but cyber resilience is an engineering discipline.”

The immediate objective is straightforward: establish which controls are missing, inconsistent, or unenforced, then improve them based on product risk. Revisit the assessment on a regular cadence, because a control that is effective today can erode as systems, teams, and delivery practices change.

The CRA is a regulatory obligation, but cyber resilience is an engineering discipline. Organizations that build evidence-producing controls into their codebases will be better positioned not only to meet reporting obligations, but also to prevent the incidents that make those obligations necessary.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/94226800-ekaterina-okuneva_sonar.webp)

Ekaterina Okuneva is a Product Marketing Manager at Sonar, driving comprehensive go-to-market actions that align product value with diverse customer needs. With over 7 years of experience in B2B SaaS for regulated industries, she crafts use cases that simplify adoption...

Read more from Ekaterina Okuneva](https://thenewstack.io/author/ekaterina-okuneva/)