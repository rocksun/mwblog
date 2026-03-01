We are at an inflection point in enterprise IT. For the last decade, “modernization” has been synonymous with containerization — essentially packaging applications so they can run anywhere. But the goalposts have moved. The challenge is no longer just about running static microservices; it is about preparing for an era of Agentic AI and dynamic, resource-hungry workloads that defy traditional infrastructure planning.

This isn’t just a technical pivot; it’s a survival strategy driven by a few massive shifts in the landscape.

First, we have the AI reality check. We are moving quickly from simple chatbots to autonomous agents -software that plans, reasons, and acts. These agents don’t fit the predictable “9-to-5” usage patterns of legacy apps. They are bursty, demanding massive compute for short inference windows and scaling to zero when idle. Attempting to support these fluid workloads with rigid, ticket-based infrastructure provisioning is a non-starter. You simply cannot manually provision for an agent that needs to scale now.

Then there is the efficiency collapse. Organizations are drowning in the “Day 2” costs of their DIY platforms. By stitching together disparate open-source tools, teams have inadvertently created a massive maintenance burden. Highly paid engineers are spending their days patching ingress controllers and debugging YAML instead of shipping business value. The cost of maintaining the platform has eclipsed the value of the applications it hosts.

Finally, we have the private cloud mandate. As data gravity and sovereignty concerns grow, the public cloud isn’t always the answer. Enterprises need a “Cloud Operating Model” — the ability to vend APIs, not tickets — within their own data centers.

The bottom line is simple: We need to stop building platforms and start consuming them. The infrastructure must become invisible so that the intelligence, both human and artificial, can flourish.

## The end of “roll your own platform”

We’ve spent the last decade stuck in a false binary. Organizations were either “Cloud Native” running [Kubernetes](https://thenewstack.io/how-kubernetes-became-the-new-linux/), or “Legacy” running Virtual Machines. The industry has poured billions of dollars and endless engineering hours into rewriting the laws of physics, convincing ourselves that if we just containerized everything, we’d hit operational nirvana.

Spoiler alert: It didn’t happen.

Instead, we built the “Frankenstein Platform.” Look at your average platform engineering team. They are drowning in complexity, trying to stitch together ArgoCD, Istio, Tekton, Prometheus, and a dozen other CNCF projects just to recreate the developer experience Pivotal Cloud Foundry (now Tanzu Platform) solved back in 2012.

> “The hidden cost of these Frankenstein platforms isn’t just initial engineering; it’s the “Day 2″ nightmare … Your platform team stops innovating and starts firefighting.”

The hidden cost of these Frankenstein platforms isn’t just initial engineering; it’s the “Day 2” nightmare. When a security vulnerability hits a specific version of Istio, or when a Prometheus update breaks your Grafana dashboards, your platform team stops innovating and starts firefighting. They become overworked operators of a fragile stack rather than enablers of business value. We promised developers a self-service experience, but we gave them a ticket queue for a platform team that is perpetually underwater.

But looking at where infrastructure is heading in 2026, we recognize a new pattern. It isn’t about choosing between the stability of the past and the flexibility of the future. It’s about stacking them.

## The universal control plane

The most important development in Kubernetes recently has nothing to do with containers. It is the realization that the Kubernetes API is effectively the universal control plane for the data center. This is the main idea behind the notion that Kubernetes is a platform for building platforms; a better place to start, not the endgame.

It took us longer than it should have to understand this and instead treated Kubernetes as a product sold directly to developers, forcing them to wrangle YAML and figure out pod disruption budgets. Eventually, we understood that Kubernetes was never meant to be the user interface. It’s the assembly code of the modern data center, the invisible layer we build on.

## The missing link: Autonomous operations

While Kubernetes solved the infrastructure API, it arguably made the application lifecycle worse. We traded the guardrails of a Platform as a Service (PaaS) for the raw flexibility of endless configuration. But once again, we look to Cloud Foundry for insight into the future. If the ultimate goal is truly autonomous operations, then you need a platform that enforces standardization to ensure consistency and scale. By delivering standard tools and practices through the platform, we can achieve automation nirvana!

Let’s consider BOSH, the heart of Cloud Foundry. While on the surface, BOSH looks like a deployment tool, it functions more like an Availability Engineer. It not only deploys code but also [monitors system health](https://thenewstack.io/monitor-your-system-health-from-pythons-command-line/), resurrects failed components, rotates credentials, and patches operating systems without downtime.

Unlike standard Kubernetes operators, which often focus on the application layer, BOSH deeply understands infrastructure dependencies. It knows how to drain a node, reprovision the OS, and reattach storage without the application and the developer ever noticing a blip. It provides the “dynamic repair” capability that raw Kubernetes assumes is handled by someone else. In a world of increasing complexity, having a platform that can self-heal at the VM level is not a luxury; it is a prerequisite for scale.

## The AI catalyst

This need for an opinionated, consistent application platform is getting pushed hard by the explosion of Agentic AI.

Look at how the public clouds are solving for [AI Agents](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/). They definitely aren’t handing developers raw Kubernetes clusters. Public cloud agentic platforms abstract the infrastructure entirely. Why? Because AI agents are non-deterministic. They scale fast, chain complex tasks, and need ephemeral environments. Managing the lifecycle of thousands of autonomous agents at the “Pod” level is a nightmare.

> “Public cloud agentic platforms abstract the infrastructure entirely. Why? Because AI agents are non-deterministic. They scale fast, chain complex tasks, and need ephemeral environments.”

Furthermore, the resource demands of Agentic AI surge unpredictably. An agent might sit idle for hours and then suddenly require massive compute to parallelize a complex reasoning chain. Hard-coding this infrastructure is inefficient and expensive. We need a platform that treats these agents as first-class citizens, automatically scaling the underlying compute down to zero when idle and bursting instantly when the agent needs to “think,” without a human operator needing to provision a single server.

The industry is voting with its feet here: AI needs high-level, opinionated platforms. If we want to run these workloads on-premise (where the data lives), we can’t rely on raw plumbing. We need a stack that mimics the public cloud model.

## The post-hype era

The era of “Resume Driven Development” – picking tools because they are trendy – is over. The next wave of thought leadership is about Convergence.

We are entering a phase of “Industrialized Kubernetes.” The tinkering phase is over. The goal is no longer to see if we can build it, but to see how fast we can ship value on top of it. The winners of the next decade won’t be the ones building the most complex Kubernetes clusters. They will be the ones who realize the best platform is the one you don’t have to build yourself.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/06/821fe331-cropped-4bdc0901-oren-penso.jpg)

Oren Penso is a seasoned IT executive and senior product strategist with more than 25 years of experience in automation, security, observability, native public clouds and platform engineering. His leadership roles span across public financial companies and VMware. Beyond his...

Read more from Oren Penso](https://thenewstack.io/author/oren-penso/)