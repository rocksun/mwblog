**Enterprises continue to face an autonomous cloud bottleneck** that breaks autonomous operations and leads to failure. This architectural flaw leaves AI agents without complete cross-domain context, including Infrastructure as Code (IaC), application topology, security, cost, and policies, creating shadow infrastructure.

At [**env zero**](https://www.envzero.com/), we’ve found the fix isn’t a smarter AI model but a shared context layer that connects declared intent with what’s actually running in the cloud. We combine IaC management capabilities with CloudQuery’s cloud inventory and context capabilities, and early customers are already using the combined architecture.

[EZ Control](https://www.envzero.com/blog/env-zero-launches-ez-control-the-autonomous-cloud-control-plane-for-the-ai-era) is the next step: an autonomous control loop that correlates declared and discovered state, recommends or executes remediation under policy controls, and verifies the change resolved the original issue. We are targeting general availability by the end of December 2026. EZ Control is currently in early access.

That distinction matters because several autonomous workflow elements are still capabilities env zero is building toward. In the envisioned loop, the system reconciles infrastructure intent with live cloud resources, associates those resources with environments and policies, proposes a code change, runs plan checks, applies or merges the change, and performs a fresh scan to verify that the drift or other issue has been resolved.

AI agents continuously querying cloud APIs raises an enterprise’s API tax, including [rate limits](https://thenewstack.io/how-to-prepare-your-api-for-ai-agents/), query-sequence failures, and potential downtime for CI/CD or autoscaling pipelines. Beyond rate limiting, this continuous polling generates significant runaway cost and latency penalties that degrade agent response times. An API tax can hamper a cloud project or solution.  
  
Implementing a context layer includes optimizing query sequences to eliminate redundant calls.

Cloud infrastructure state remains fragmented across state files, tags, spreadsheets, and tribal knowledge. Bridging IaC (declared intent) with the runtime reality observed by cloud security posture management (CSPM) tools via an ontology layer is essential for AI automation. This requires a continuous control-plane loop to manage its current state.

Here’s a high-level overview of the end-to-end loop:

* Declared intent
* Discovery
* Reconciliation
* Policy verification
* Code pull requests (PRs) for review and execution
* Validation scan

## Model intelligence vs. architectural context

In our early age of AI systems, it’s common to blame models for bottlenecks. The drumbeat of AI hype, of course, says a strong AI model is the solution of choice. Unfortunately, that’s far from the case; these bottlenecks stem from system architecture, and no amount of model intelligence can fix them.

> …these bottlenecks stem from system architecture, and no amount of model intelligence can fix them.

When planning AI agent deployment, teams must recognize that CI/CD pipelines and AI agents are already accelerating infrastructure changes faster than humans can adapt.

As changes increase, traditional self-service tools show only IaC pieces and miss application topology, governance, and related cost variables. For example, Wiz might enforce a strict high-availability policy requiring multiple instances, but an AI agent working solely within IaC sees only a single standalone EC2 instance and remains completely blind to the compliance violation. Adding a context layer stitches IaC to applications, policies, and governance, providing the central brain needed for autonomous decisions so teams don’t have to troubleshoot and firefight.

Large language models (LLMs) are only as good as the [context they receive](https://thenewstack.io/context-engineering-going-beyond-prompt-engineering-and-rag/). Organizations have spread-out cloud accounts and tools; connecting them in a governed way is critical.

## The API tax and live querying liabilities

The context layer does not eliminate cloud API calls. Instead, it changes how often agents need to make them. Our model combines synchronized context with targeted live queries. Relatively stable information, such as ownership, can be retained and refreshed on an appropriate cadence, while live queries can be reserved for questions that require current state. The goal is to reduce redundant API traffic and lower the risk of hitting provider rate limits as agentic workflows scale.

That risk can extend beyond the agent itself. At env zero, we argue that repeatedly using operational APIs for inventory-style questions could consume rate-limit capacity that other automation also depends on. CI/CD and autoscaling are examples of critical functions that might face operational risk or delays when competing for the same API capacity. An API tax is incurred when software, such as AI systems, rerun queries across external APIs for similar prompts without optimized sequencing. You need to design intelligent query architectures to avoid hitting APIs redundantly with workflow and racking up that nasty API tax.

The difference between humans and AI agents starts with how they query systems. Humans tend to ask targeted questions, whereas agents tend to explore. Our CEO Steve Corndell has a favorite example: “We’ve seen a failure mode in which an agent could complete 90 queries, fail on the 91st, and then have to restart the sequence. That compounds the API tax because the workflow repeats work it has already completed.”

> …an agent could complete 90 queries, fail on the 91st, and then have to restart the sequence.

Another benefit of transitioning to a context layer is that it balances cached state data syncs with selective live queries to mitigate rate-limit risk while preserving operational continuity.

## Declared state vs. live reality

In our view, traditional IaC platforms and standalone CSPM tools often struggle to fully own the join between [declared intent and live reality](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift). A central context layer combines IaC intent with runtime discovery to map resource ownership, policy context, and application boundaries across [multicloud environments](https://thenewstack.io/multi-cloud-blind-spots).

Based on our experience with customers, infrastructure state is the enterprise’s largest ungoverned context. Code has Git, identity has an IDP, money has an ERP, and infrastructure has a tagging convention.

> Code has Git, identity has an IDP, money has an ERP, and infrastructure has a tagging convention.

If you can’t name an owner, you can’t enforce policy. Typically, infrastructure ownership is unclear across state files, ClickOps changes, tags, cloud APIs, spreadsheets, and tribal knowledge. When an enterprise brings this context together into a knowledge graph, it can enable software, such as env zero, to take control within defined guardrails.

## Architecture of an autonomous cloud control plane

The architecture of an autonomous control plane can best be explained as an end-to-end loop involving:

* Capturing declared intent
* Discovery of actual cloud state
* Reconciling uncodified resources to unified concepts
* Applying policy checks
* Proposing pull-request code changes for review
* Re-scanning to validate resolution and prevent future drift

Connecting CloudQuery data ingestion with an ontology layer in the middle creates the brain that drives automation engines down to execution tools like [Terraform](https://roadmap.sh/terraform), OpenTofu, or Pulumi.

That changes what an autonomous cloud control plane has to do. Detection is only the first step. A control plane for autonomous operations must own the whole loop: understand intent, discover actual state, reconcile the two, apply governance, remediate the problem, and verify the fix worked to deliver end-to-end drift detection and remediation.

A tool that stops at detection still leaves the hard part to humans. That’s why we think the category should be judged on time to remediation (TTR). For this model, “time to remediation” is the elapsed time from identifying an infrastructure problem that requires action to verifying that the corrective change has resolved it.

Detection alone does not complete the loop. We describe a sequence that moves from discovery and reconciliation through policy context, proposed changes, review or plan checks, execution, and a fresh scan confirming that the drift or original finding is gone. That final validation separates time to remediation from the simpler measure of time to change. This loop maps the blast radius before proposing a fix, addressing root causes rather than applying temporary band-aids.

Env zero also automatically suggests preventative policies that can prevent the same class of problem from recurring. That belongs naturally to prevention or root-cause improvement alongside the core remediation timer itself.

## Adding a control layer without replacing IaC

We see this architecture as a way to move cloud automation beyond the limits of traditional IaC workflows.

CloudQuery, which merged with env zero in March 2026, brings together data from cloud accounts and external systems such as Wiz, ServiceNow, and Datadog, while an ontology layer correlates infrastructure, policy, ownership, and application context.

CloudQuery thinks it; env zero does it. We then use that context to drive automation, governance, self-service, and compliance across the environment. The advantage is that teams do not have to replace Terraform or another IaC platform to gain that broader control layer. Instead, our platform sits above the existing toolchain, connecting declared intent with discovered state and giving autonomous workflows the context they need to decide what happens next.

To learn more about env zero, book a [technical demo](https://www.envzero.com/early-access-project-introspect), request early access to EZ Control, read our [Agentic Experience blog post](https://www.envzero.com/blog), or explore the [docs.envzero.com](https://docs.envzero.com) documentation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/75945e03-cropped-35e959f0-screenshot-2026-02-23-at-15.14.59.png)

Oleg Danilyuk is the VP of Product at env zero, where he leads product vision, roadmap, and cross-functional collaboration to solve real-world cloud management challenges. He brings over a decade of product experience spanning cloud infrastructure, AI-powered advertising, and medtech....

Read more from Oleg Danilyuk](https://thenewstack.io/author/oleg-danilyuk/)