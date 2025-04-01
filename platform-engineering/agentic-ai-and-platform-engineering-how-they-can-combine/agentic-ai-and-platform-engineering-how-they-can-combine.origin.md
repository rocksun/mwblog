# Agentic AI and Platform Engineering: How They Can Combine
![Featued image for: Agentic AI and Platform Engineering: How They Can Combine](https://cdn.thenewstack.io/media/2025/04/d688f5d6-ai-agents-platform-engineering-2-1024x576.jpg)
More than [a decade after Kubernetes was introduced](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/), and even as adoption of the container orchestrator has skyrocketed, a skills gap persists.

This is a big problem for enterprises that need K8s to scale. For[ Sebastian Kister](https://www.linkedin.com/in/sebastiankister/), [Kubernetes](https://thenewstack.io/kubernetes/) has become the public transport for compute.

“Kubernetes makes it possible to supply computing power automatically, at scale and, most of all, securely and reliably — which is not the case for many, many of the other technologies that we had before,” said Kister, product team lead of the container competence center, platforms and operations team at the car maker [Audi](https://www.audi.com/en/company/) and transformation consultant for other enterprises.

But that doesn’t mean Kubernetes has become easier to work with.

“The challenge is especially in the skillset of people using it,” he said. “The market makes it difficult to find truly senior [people who have a deep understanding of Kubernetes](https://thenewstack.io/talent-shortages-shouldnt-kill-your-cloud-native-journey/).”

It all came to a head recently when one of his teams wanted to add 12 new clusters, and the [site reliability engineering](https://thenewstack.io/google-sre-site-reliability-engineering-at-a-global-scale/) team responded: We need time to find and hire two more SREs.

With all the automation around Kubernetes in place, Kister was surprised by so many barriers to scaling. In the face of these perpetuating complexities, vulnerabilities and incidents, Kister looked toward [AI](https://thenewstack.io/ai/).

Six months ago, Kister adopted the [Kubiya ](https://www.kubiya.ai/)agentic AI platform to support security responses that are, as he put it, “real-time, context-aware and continuously updated.” This adoption of agentic AI not only took an enterprise he works with from risk acceptance to active, intelligent remediation — it decreased team friction and stopped the blame game.

## Agentic AI Aids Asymmetric Scaling
Like most companies of late, Kister’s [platform engineering](https://thenewstack.io/platform-engineering/) and operations teams felt urgent pressure to scale while facing shrinking budgets and rigid processes.

“We couldn’t hire fast enough, and educating junior talent at scale was too slow and unpredictable. The market made it nearly impossible to attract top-tier talent,” Kister said.

“We had to find another way — an asymmetric way to scale that didn’t rely on scarce resources.”

Kister aimed to leverage [AI agents](https://thenewstack.io/ai-agents/) to get rid of toil and incident remediation, to free senior developers from operations tasks and all developers from focus drift. He looked to agentic AI platforms, where AI agents can be trained on special tasks to get rid of repetitive tasks and shift focus more on features, innovation and enablement of projects using the platform.

## Building an Army of Very Specific AI Agents
The plan to leverage AI agents is not about deploying an AI agent for every use case.

It does not even follow the common [platform engineering](https://thenewstack.io/platform-engineering/) practice of covering use cases that affect 80% of engineers. Right now, Kister’s team is prioritizing AI agent use cases around runtime security, reliability and incident remediation that affect all engineering teams.

Kubiya has an “agentic native” [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) for programmable agents that are configured to act as dedicated SRE AI agent soldiers for software development teams. There are 200 AI agent use cases out of the box but, like all platform engineering initiatives, organizations can build on top with custom agents for specific use cases.

Kubiya runs within this company’s [Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline+mention) clusters, scaling across its environments and integrating within its [identity and access management (IAM)](https://thenewstack.io/10-best-practices-for-building-a-robust-iam-strategy-in-2024/) and [role-based access control (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) policies, with all the production-ready security and compliance guardrails in place.

“We have full visibility and control, and we trust these agents to do exactly what they’re supposed to — no more, no less,” Kister said.

Unlike other AI agent platforms that are still prone to [hallucinations](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/), Kubiya has added programmability and predictability controls, so even when a developer asks the AI agent to do something out of scope, it will limit the response to only the tool calls and permissions granted to it.

That scope is very specific to a policy or environment to which it has access. It is [Open Policy Agent](https://thenewstack.io/the-open-policy-agent-journey-from-sandbox-to-graduation/) enforced, therefore working within on-premise or in air-gapped environments.

“It’s not a Software as a Service,” Kister said. “It’s your very special trained little Navy SEAL, sitting there doing this one job every day, every night, 24/7.” It heavily contributes to enterprise resiliency, he added.

In addition, by relying on Kubiya’s in-house SREs to create an AI agentic workforce, some of his clients’ platform teams were able to scale the technology without adding another training — or “an enormous team,” as he put it — to learn these nascent skills.

Kubiya has a full-stack AI platform that allows organizations to build on top of or bring their own AI agents for production-ready use cases. It also offers an enterprise version that includes on-premise deployments, a choice of large language models, and service assistance, which Kister’s team leaned on to avoid adding another skills gap.

“I bought an AI ‘platform engineer’ to deploy agentic workflows in a production-grade environment,” he said. “Then, as the requirements expand, we can take leverage of this asymmetric way to scale our workforce into new areas of the business.”

“Right now, as I don’t have the people or the knowledge to scale horizontally, I use their repository of pre-built AI agents to augment my teams’ efforts in running operations without needing to think twice about it.”

## Measuring the Success of an AI Agent Platform
An engineering strategy is only as good as it is measured to be.

Before Kubiya, common vulnerabilities and exposures (CVEs) would sit in Jira, Kister said, treated like routine tasks — although they are anything but that.

“That backlog delayed responses and exposed risks,” he said. “With Kubiya, we automated mission-critical operations — on-call handling, real-time remediation and operational deflection — freeing our top developers from context overload so they can focus on innovation.”

In just six months, security at scale is proven:

- Mean time to resolution (MTTR) dropped from eight hours to 30 minutes.
- Weekly resolution time went from 64 hours to four.
- Incidents reduced by 80%, due to proactive, AI-powered troubleshooting.
- Repetitive requests for engineers dropped by 80%.
- Annual run-rate for cloud infrastructure costs dropped by 20%, by identifying failed deployments running unnecessarily.
- Compliance audits and security checks now take half the time to generate.
The project doubled the team’s value proposition, Kister said, because the cost of tooling increased by only 10%, all managed by his small, focused team.

## AI Agents Help Developers Communicate
Kubiya didn’t just remove some of the biggest technical frustrations. It removed a lot of the interpersonal ones, too.

“This little agent talks to your junior developer and it can provide insights, and we got rid of finger pointing,” Kister said, because if something doesn’t meet standards, the platform won’t allow it to be deployed, and the developer knows exactly why.

Developers simply have a conversation with the AI agent, asking: What happened here? What’s your advice? In the future, he said, his team will test making remediation more automated, too.

Now, “80% of troubleshooting is just off the table because it’s instantly clear through the AI, through the little agent that sits there,” he said. “You ask it, what happened here? And it’s like: Do you have a root cause for that? Yes, and it tells you the root cause and you just know what happened.”

Many of these [core developer productivity metrics](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) are conduits for cost because it reduces engineering hours spent on the frustration of finding what went wrong and reallocating that time to creating new features faster.

With Kubiya’s new AI agent platform, Kister’s team — and its internal developer customers — unlock visibility, scale builds asymmetrically, and truly do more with less. Or, better put: Do more with exactly the team he has.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)