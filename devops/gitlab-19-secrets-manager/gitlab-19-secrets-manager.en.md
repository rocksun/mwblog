**There are orchestras… and then there are mere string, horn, or woodwind sections.** As the self-styled intelligent orchestration platform for [DevSecOps](https://thenewstack.io/devsecops-tools-that-offer-security-efficiency-and-quality/), GitLab wants to put on a full show with a new coordinated play that encompasses every possible instrument.

The organization [released GitLab 19.0 last Thursday](https://about.gitlab.com/press/releases/2026-05-21-gitlab-19-extends-intelligent-orchestration-to-close-the-gap-between-writing-code-and-shipping-it/) with a louder, more harmonious score that encompasses expanded [secrets management](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/), agentic merge request workflows, continuous integration (CI) pipeline visibility, support for the self-hosted open-source model, and supply chain visibility.

## Prisoners of the AI paradox

As the amount of AI-driven code starts to surface in working codebases, software engineering teams are aiming to avoid the gravitational pull of the [AI paradox,](https://www.linkedin.com/posts/ai-softwareengineering-developerproductivity-share-7411238038577647616-Mp-Z/) i.e., more AI code means more workflow credentials to secure, more review and merge changes to oversee, more pipeline standards to uphold, more regulatory compliance checks, and so on.

It may feel like intelligent automation and intelligent infrastructure orchestration were never playing from the same sheet of music. GitLab 19.0 has been engineered to combat the production paradox and reduce the handoffs between writing code and shipping it.

> “Today, putting a credential into a CI/CD variable grants that secret to every job in the project, including jobs added later by contributors who weren’t around when the secret was created, GitLab Secrets Manager flips the default.” – Manav Khurana, GitLab.

Key among the updates, [GitLab Secrets Manager](http://about.gitlab.com/blog/secrets-manager-in-public-beta/) (a technology that stores credentials inside the same platform that runs code and pipelines) is now in public beta for GitLab Premium and Ultimate users. The tool scopes each secret to only the jobs authorized to use it. Access control and audit logging use the same group and project structure already in GitLab, with no separate permission model to maintain.

If a credential is compromised, developers (who are likely platform engineers in this instance) can trace every job that used it in the GitLab audit trail, linked to the originating pipeline, without having to correlate logs across separate systems. It works alongside existing integrations with HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, and Google Cloud Secret Manager.

## The principle of least privileged access

Scoping secrets to individual jobs is presented here as a fundamental change to developers’ security posture during pipeline construction.

[Manav Khurana](https://www.linkedin.com/in/mkhurana/), chief product & marketing officer at GitLab, tells *The New Stack* that this move is all about the principle of least privileged access.

“Today, putting a credential into a CI/CD variable grants that secret to every job in the project, including jobs added later by contributors who weren’t around when the secret was created,” says Khurana. “GitLab Secrets Manager flips the default.”

Khurana explains what happens now and says that when a developer creates a credential, they define the conditions under which a job can use it: which branch, which environment, and whether the branch is protected. Anything outside that scope can’t see the secret, so a compromised job stays contained.

## Keeping developers in flow across the lifecycle

GitLab 19.0 also extends Developer Flow across the full merge request lifecycle to address reviewer feedback, resolve conflicts, split oversized merge requests, and implement features at any stage. [Launched by GitLab last year](https://about.gitlab.com/blog/transform-mrs-to-automated-workflow/), Developer Flow (the clue is in the name; it aims to keep programmers in a state of flow) exists to turn an issue into a merge request.

Since the flow reads project-specific standards from [AGENTS.md](https://agents.md/) before committing, the output reflects team context, workflows, and guardrails rather than generic defaults.

“The agent works for a developer’s project, not against a generic template,” says Khurana. “Customization goes as deep as the team specifies. AGENTS.md captures the project-level context the agent wouldn’t otherwise have: conventions, architectural decisions, environment quirks, the commands a new contributor would need someone to explain.”

He further clarifies that [agent-config.yml](https://adk.dev/agents/config/) (a configuration file that defines agent behavior, environment, and parameters) sets up the development environment with the necessary dependencies and tooling, enabling the agent to run tests and pre-commit hooks before committing.

“The point is to give the agent a machine that’s ready to go, so output matches the team’s standards instead of creating rework. Two projects in the same group can produce very different agent behavior because Developer Flow reads each project’s own files, rather than a shared default,” says Khurana.

## Four new open source models

Other updates in this release include Components Analytics, which gives platform engineering teams visibility into which CI/CD catalog components are running across an organization and which versions are in use.

Additionally, the GitLab Duo Agent Platform Self-Hosted now runs its agents on [four additional open-source models](https://about.gitlab.com/blog/more-ai-models-for-duo-agent-platform-self-hosted/), Mistral Devstral 2 123B, GLM-5.1, Kimi-K2.6, and MiniMax-M2.7. Each model was evaluated against the GitLab Duo Agent Platform task requirements, including multi-step tool use, code-generation quality, and reasoning across large code differences. Both on-premises and private cloud deployment options are supported.

“The introduction of four new open source models is about eliminating the choice between compliance and capability. Teams in [air-gapped and regulated environments](https://thenewstack.io/deploying-ai-in-air-gapped-environments-what-it-really-takes/) have stronger local options than before,” says Khurana.

He points out that GitLab users can also set up hybrid deployments, mixing self-hosted and GitLab-managed models by feature, choosing based on data sensitivity, infrastructure cost, latency, and the capability gap between the model they can run locally and the managed option available through GitLab.

GitLab 19.0 also adds security capabilities that give teams more control over governing what ships and who can access the platform. Dependency scanning with a [software bill of materials (SBOM)](https://thenewstack.io/a-good-sbom-is-hard-to-find/) produces an auditable inventory of third-party components that can be matched against GitLab security advisories.

> “This approach doesn’t cover how agents make autonomous decisions across a team’s pipeline and act on permissions that were granted once, then subsequently forgotten about. If software engineering teams don’t have execution governance and observability wired up before they flip the switch on agent deployments, they’re going to learn what someone else decided on a different day – and they’re going to learn it the hard way,” – David Girvin, Sumo Logic.

## Don’t forget forgotten permissions

[David Girvin](https://www.linkedin.com/in/david-a-girvin/), AI security researcher at cloud monitoring and log management [SIEM](https://www.microsoft.com/en-gb/security/business/security-101/what-is-siem) specialist [Sumo Logic](https://www.sumologic.com/), tells *The New Stack* that he concurs with the direction of the work being carried out here.

“Most AI coding tools solve problems that take up about 52 minutes of a developer’s day. GitLab is asking what happens during the other seven hours,” Girvin says. “GitLab 19 is betting on agentic orchestration across the full software lifecycle, not just the editor, which is the right problem to be solving.”

However, Girvin notes that this approach doesn’t address how agents make autonomous decisions across a team’s pipeline and act on permissions that were granted once and then forgotten.

“If software engineering teams don’t have execution governance and observability wired up before they flip the switch on agent deployments, they’re going to learn what someone else decided on a different day – and they’re going to learn it the hard way,” underlines Girvin.

## Fix AI infrastructure first, then code

GitLab has directed its engineering efforts to try to combat the “more AI code equals more headaches” issue that has brought the AI-infrastructure first debate into the spotlight this year.

As GitLab’s Khurana summarizes, “This release means developers spend less time on the manual work that surrounds a merge request, and a compromised credential stays contained to the job that used it. Security teams focus remediation on real exposure, not every package in the manifest, just the ones your code actually calls.”

The core message here is to put security, automation, and governance on the same platform as the code, so that one can be initiated before the other.

As the cartoon says: [first pants, then shoes](https://i.pinimg.com/474x/4d/6f/47/4d6f47b070a2778ed35e18e3e2428ea5.jpg).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)