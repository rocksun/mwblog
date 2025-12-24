It’s been 10 years since [Infrastructure as Code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/) became the backbone of cloud provisioning. Terraform, CloudFormation, Pulumi and Ansible gave us a structured way to define infrastructure state. They’ve also given us a way to think about version changes and made cloud environments reproducible.

In short, IaC gave us the entire era of [DevOps maturity](https://thenewstack.io/where-are-you-on-the-devsecops-maturity-curve/).

But today, a lot has changed. Systems have become vastly more complex. We’ve got more:

And, of course, IaC alone has started to show its limits.

Now, teams depend on dozens of interconnected services. Configuration, security and [runtime behavior](https://thenewstack.io/hardened-containers-arent-enough-the-runtime-security-gap/) can’t be captured purely as code. Meanwhile, developers expect self-service and operational velocity. And those expectations will only keep rising.

In response, we now have a new operational stack to move forward with.

It consists of a combination of three distinct layers:

1. IaC
2. Platform / orchestration layer
3. AI agents for Day 2 operations

These layers aren’t replacements, but more an evolution of what we’ve already seen. Each one solves a different part of the operations problem. And together they define a modern pattern for how teams will operate cloud infrastructure over the next decade.

[![Layer 1: Infrastructure as Code; Layer 2, Platform & Orchestration; Layer 3, AI Agent Execution](https://cdn.thenewstack.io/media/2025/12/2154b56a-image2.png)](https://cdn.thenewstack.io/media/2025/12/2154b56a-image2.png)

## 1. The IaC Era: Provisioning Was the First Big Challenge

So here’s what happened: IaC brought order to chaos.

It did so by solving three foundational problems:

* **Declarative provisioning:** Engineers describe what they want, not how to build it.
* **Versioning:** Changes flow through git, not tribal knowledge.
* **Reproducibility:** Environments match because the code matches.

For static or slowly changing infrastructure, of course, this worked beautifully.

But the modern cloud isn’t static.

### Where IaC Struggles Today

As systems grew, teams quickly realized that IaC does not fully solve things like:

* State drift and misconfiguration.
* Rotating secrets or identity and access management (IAM) updates.
* Ephemeral environment creation.
* Incident remediation.
* Dependency wiring for observability.
* Compliance enforcement.
* Identity scoping and network boundaries.
* Operational debugging.
* Multistep workflows that require sequencing, approvals or context.

The bottom line is that IaC was never meant to handle so much. It couldn’t take on runtime behaviors, adaptive workflows or continuous operations.

After all, it describes objects, not actions.

Fortunately, the next layer arrived just in time to fill this gap.

## 2. The Platform Era: Guardrails, Standardization and Context

Around 2018-2020, engineering organizations started building internal developer platforms (IDPs). The goal wasn’t to replace IaC. It was, instead, to wrap it in a consistent operational model.

A platform is a set of orchestrated systems that provide:

* **Identity boundaries:** IAM roles and policies applied consistently.
* **Network boundaries:** Controlled ingress/egress and micro-segmentation.
* **Compliance guardrails:** Controls for SOC 2, HIPAA, NIST, PCI.
* **Automated wiring:** Logs, metrics, traces, dashboards, alarms.
* **Environment templates:** One-click environment or namespace creation.
* **Service catalogs:** Consistent provisioning of databases, queues, APIs.

The platform layer sits on top of IaC but below developer workflows.

But IaC is still the authoritative description of the resources.

The platform now becomes the authoritative description of how operations work.

### Why Platforms Emerged

Three structural shifts made this necessary:

1. **Microservices produce exponential complexity:** Each additional service adds monitoring requirements, IAM roles, network rules, deployment workflows, service-level objectives (SLOs) and policy surfaces.
2. **Compliance demands continuous evidence:** Modern audits require continuous monitoring, not annual snapshots. IaC can define security policies, but platforms have to enforce them.
3. **Developer velocity cannot depend on specialists:** Developers need self-service environments and services. Platforms abstract cloud primitives into predictable workflows.

### Platform ≠ Platform as a Service (PaaS)

Contrary to popular belief, a platform doesn’t hide the cloud. It organizes it.

It creates opinions around identity, networking and life cycle automation that IaC alone can’t enforce. Most importantly, it introduces logical boundaries like Tenants (more in Part 2 of this series), where guardrails can attach.

This platformization set the stage for the next era.

## 3. The AI Era: Automating Day 2 Operations

The next major shift in cloud operations arrived when AI became capable of:

* Correlating logs, metrics and traces
* Understanding natural language requests
* Mapping symptoms to root causes
* Applying runbook-style remediations
* Generating infrastructure changes
* Orchestrating multistep workflows

Its job isn’t to replace DevOps engineers. It’s to replace the repetitive tasks that typically overload DevOps engineers.

### What AI Agents Actually Do

AI agents in operations can:

* Diagnose incidents using signals across systems.
* Remediate known patterns (such asrestart, config patch, scale).
* Create or tear down ephemeral environments.
* Enforce compliance or security policies.
* Generate Terraform or YAML for new infrastructure.
* Propose changes with explanations and request human approval.

These tasks follow patterns that AI can reliably identify.

### But There’s a Catch: AI Without Guardrails Is Dangerous

An unconstrained AI agent is like a root user with no context.

Here’s why:

* It may generate unsafe IAM changes.
* It may modify resources it shouldn’t see.
* It may attempt fixes that violate compliance requirements.
* It may misinterpret topology due to drift or partial visibility.

This is why the AI layer can’t sit directly on top of IaC or raw cloud APIs.

AI needs:

* A predictable identity model
* Scoped permissions
* Consistent network boundaries
* Audit logs
* Drift detection
* Known topology
* Approval workflows

In other words, AI needs a platform just beneath it. It needs a structured layer with guardrails. Without this, the agent can’t act safely.

## 4. The Three-Layer Model

### Layer 1: IaC

Defines state.

Provisioning, templates, versioning.

### Layer 2: Platform / Orchestrator

Defines behavior.

Guardrails, boundaries, identity, network, compliance, orchestration.

### Layer 3: AI Agent Execution Layer

Defines action.

Troubleshooting, remediation, environment management and workflow automation.

This layered stack mirrors the evolution of software:

* IaC = code.
* Platform = operating system.
* AI agent = runtime process acting on the system.
* Without the OS, the process has no structure.
* Without IaC, the OS has nothing to orchestrate.

## 5. Organizational Implications

* **DevOps bottlenecks shrink:** The most repetitive, interrupt-driven tasks shift to AI agents.
* **Developers get real self-service:** They interact with the platform, not individual cloud APIs.
* **Compliance becomes continuous:** Checks run inside the platform boundary, and AI helps maintain controls.
* **Production becomes more resilient:** AI agents catch issues before humans see them.
* **Teams with small DevOps headcounts can operate like much larger ones:** Scale moves from human labor to layered automation.

## Wrapping Up

IaC gave teams a declarative foundation.

Platforms gave teams structure and guardrails.

AI agents now give teams operational execution.

This is the new operational stack. It’s not a simple tooling trend. Rather, it’s a structural shift.

Organizations that recognize and adopt this three-layer architecture will operate faster, safer and with far less operational friction.

No more scaling DevOps through headcount because now you can scale through structure.

No need to rely on heroics and tribal knowledge. You can rely on platforms and automation.

AI doesn’t have to be a risky experiment. Deploy it as a controlled execution layer bounded by identity, policy and context.

The three-layer combination is what will define the next decade of cloud operations.

At DuploCloud, we’re excited to be part of AI advancements, learning, stumbling, learning some more, and most importantly, creating and participating in the innovation that is shaping the future.

We’d love for you to try out our [AI DevOps Agents Sandbox](https://duplocloud.com/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/311ffaca-cropped-be78f843-fahmid-kabir.jpeg)

Fahmid Kabir leads product and go to market at DuploCloud, an AI-powered DevOps platform. He has worked with deep AI technologies, cloud infrastructure and compliance for the past 18 years.

Read more from Fahmid Kabir](https://thenewstack.io/author/fahmid-kabir/)