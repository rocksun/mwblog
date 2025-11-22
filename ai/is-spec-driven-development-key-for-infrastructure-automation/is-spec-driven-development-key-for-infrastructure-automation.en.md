Since GitHub Universe and the [announcement of GitHub Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/), spec-driven development (SDD) has taken the dev world by storm. The premise is compelling: Give AI agents structured context through markdown specs before they write code, and you’ll have it all. An end to hallucinations about APIs, rushed coding and low-quality outcomes.

With [SDD](https://thenewstack.io/what-is-an-ai-native-developer/), AI agents will work more like human developers who receive product requirements documents (PRDs), break down tasks and execute systematically.

The concept formalizes what development teams have done for years. A product manager writes requirements. Developers digest the PRD or specifications, break the work into tasks and start coding. SDD simply structures this workflow for the AI era, turning natural language specifications into the context [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) need to generate meaningful code.

As someone who lives and breathes DevOps and platform engineering, I found myself asking the obvious question: What does this mean for infrastructure work? Should we be racing to adopt SDD for our Terraform modules and Kubernetes configurations?

## **Infrastructure Code Isn’t Application Code**

Infrastructure code looks like code, but it behaves very differently from application code.

Look at any Terraform file, Helm chart or CloudFormation template. What do you see? Specifications. Infrastructure as Code (IAC) is already spec-driven by design. It is declarative. We describe the desired state. We say “I want a database with these properties,” not “Execute these commands to create a database.”

But here’s where things get interesting.

* **Application code favors creativity.** Give 10 developers the same feature request, and you’ll get 10 different implementations. Each might be valid, elegant in its own way. The goal is to solve business problems with novel approaches, optimize for user experience or find clever performance improvements. There’s value in that diversity of solutions.
* **Infrastructure code favors reproducibility.** When I spin up infrastructure in us-east-1, eu-west-1 and ap-southeast-1, I need identical configurations. Same networking setup, same security groups, same database configurations. Standardization means predictable costs, interchangeable parts and reliable disaster recovery.

This distinction matters for SDD because AI agents thrive on creative problem-solving but struggle with strict reproducibility. We don’t want an AI agent getting creative with our virtual private cloud (VPC) configuration. We want the exact same blueprint deployed perfectly every time.

More importantly, infrastructure code rarely flows from spec to implementation. Consider how infrastructure actually evolves. FinOps adjusts instance types to optimize costs. Security patches a vulnerability directly in production. Someone scales a database through the console during an incident. Your Terraform still describes the original state, but reality has moved on. This is drift: when your actual cloud resources no longer match your IaC. Infrastructure teams work backward, constantly updating specifications to match reality.

​​SDD assumes a forward flow from requirements to code. But that’s not the way platform teams work. We don’t need AI to write more Terraform from specs; we need something else entirely.

[![](https://cdn.thenewstack.io/media/2025/11/9c7864eb-desktop_image_blog_1_4x-1024x547.webp)](https://cdn.thenewstack.io/media/2025/11/9c7864eb-desktop_image_blog_1_4x-1024x547.webp)

## **The Real Automation Gap Is Deployment Orchestration**

SDD will influence infrastructure work, but not always in ways platform teams will celebrate.

Today, developers are already 10 times more productive with AI copilots than they were just a few years ago. SDD promises to push this even further: complete modules generated from specifications, entire features materialized from markdown plans. The volume of application code will explode.

All this code needs somewhere to run. Every feature needs infrastructure. Every microservice needs its database, message queue and networking. The acceleration in code production creates unprecedented pressure on deployment velocity.

Yet deployment remains stubbornly manual. While developers get AI assistants that turn specs into code, platform engineers still coordinate complex deployments by hand. We can generate a complete microservice in a few hours, but spend days figuring out how to safely set up and [deploy its infrastructure](https://thenewstack.io/what-does-it-take-for-ai-agents-to-deploy-infrastructure/).

[![](https://cdn.thenewstack.io/media/2025/11/cfcc28d4-desktop_image_blog_2_4x-1024x508.webp)](https://cdn.thenewstack.io/media/2025/11/cfcc28d4-desktop_image_blog_2_4x-1024x508.webp)

## **Why AI Agents Can’t Orchestrate Infrastructure Deployment**

The barriers to AI-driven deployment are structural problems in the way infrastructure code is organized today.

* **Terraliths: Monolithic nightmares.** We’ve created massive Terraform files where specifications, values and logic are tangled together. A single file might define networking, databases and application configuration all mixed up. Small changes cascade unpredictably. There’s no way to understand blast radius when everything touches everything else.
* **Heterogeneous tooling.** A single environment uses Terraform for infrastructure, Helm for Kubernetes, as well as Python scripts. Each with different inputs, outputs and state management. Orchestrating across them requires understanding hidden dependencies that aren’t documented anywhere.
* **Working backward from drift.** Infrastructure teams constantly reconcile drift, updating code to match reality. AI agents would first [need to map what actually exists across all clouds](https://thenewstack.io/to-wrangle-cloud-bursting-costs-tools-need-to-evolve/), regions and accounts before even attempting to update anything.

What we really need is to restructure infrastructure to be AI-ready.

## **Blueprint-Driven Deployment: Infrastructure for the AI Era**

The path forward is clear. We need to transform the way infrastructure is packaged, deployed and managed. Here’s how to make infrastructure AI-ready:

* **Transform every piece of infrastructure.** Turn every Terraform module, Helm chart and Python script into artifacts with normalized inputs and outputs. These artifacts become reusable building blocks that assemble into blueprints.
* **Assemble artifacts into clear, versioned blueprints** **with well-defined boundaries.** A database blueprint creates databases. A networking blueprint handles VPCs and subnets. No mixing, no confusion.
* **Publish them to a catalog.** Decide which ones to surface to AI agents so they know what’s safe and allowed to deploy.

[![](https://cdn.thenewstack.io/media/2025/11/5ee1991c-desktop_image_blog_3_4x-scaled.webp)](https://cdn.thenewstack.io/media/2025/11/5ee1991c-desktop_image_blog_3_4x-scaled.webp)  
This approach solves the structural problems we mentioned earlier:

* **Terraliths get decomposed into artifacts and blueprints.** That 10,000-line monolith becomes a collection of focused components, each with its own life cycle and clear interfaces. Changes are scoped. Blast radius is contained. AI works with the blueprints, not the tangled code.
* **Heterogeneous tooling becomes unified.** Terraform, Helm, Python, etc., all become artifacts with standard inputs and outputs through normalization. The orchestration layer doesn’t care what created the artifact.

With that in place, you can tackle the drift problem:

1. Regularly map what exists: Discover actual cloud state across all accounts and regions into a cloud graph.
2. Extract patterns from production and create/update blueprints.

[![](https://cdn.thenewstack.io/media/2025/11/f421ac57-desktop_image_blog_4_4x-scaled.webp)](https://cdn.thenewstack.io/media/2025/11/f421ac57-desktop_image_blog_4_4x-scaled.webp)

The cycle becomes sustainable: Reality informs blueprints, blueprints guide deployment and deployment is tracked in the graph.

Now an AI agent can actually work:

Request: “We need to expand to Asia-Pacific for lower latency.”

The agent queries the blueprint catalog and cloud graph, and finds the standard regional infrastructure blueprint already running in the United States and Europe. It understands dependencies from the graph, networking databases before applications.

“I’ll deploy regional infrastructure blueprint v2.3 to ap-southeast-1. Based on the dependency graph, this takes 12 minutes. No existing resources affected.”

One approval. The orchestrator handles the rest.

[![](https://cdn.thenewstack.io/media/2025/11/30143ffd-desktop_image_blog_5_4x-1024x508.webp)](https://cdn.thenewstack.io/media/2025/11/30143ffd-desktop_image_blog_5_4x-1024x508.webp)

## **Infrastructure Is Different From Application Code**

Spec-driven development makes sense when you’re building features. It doesn’t when you’re building the platform those features run on.

Infrastructure needs:

* **Blueprints, not specs:** Reusable, versioned patterns you can roll out across regions and environments.
* **Orchestration, not just code generation:** Coordinated, multistep workflows across infrastructure, configuration and apps.
* **Clear boundaries, not entangled modules:** Well-defined scopes per blueprint and artifact so changes stay contained.
* **Cloud graphs, not code dumps:** A live view of what actually runs in every account, region and cloud.

The future isn’t AI agents generating Terraform. It’s AI agents executing deployments safely by using prevalidated blueprints.

This is how AI finally enters the deployment game.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/11/8af745dc-cropped-cb829983-idan-yalovich-600x600.jpeg)

Idan Yalovich is cofounder and CEO at Bluebricks, an environment orchestration platform that transforms Infrastructure as Code, configuration tools and scripts into reusable, versioned environment blueprints, ready to be delivered by agents.

Read more from Idan Yalovich](https://thenewstack.io/author/idan-yalovich/)