Kubernetes is the cornerstone of cloud native architecture, but this container orchestrator is not the only thing that keeps enterprise stacks standing tall.

From the start, any production-ready, cloud native platform engineering strategy demands networking, storage and observability. But then Day 2 maintenance and scalability issues emerge, which are “fixed” by finding and using more tools. This brings on more [Kubernetes complexity](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy/), especially when adding capabilities like GitOps, policy management and a service mesh. Eventually, organizations have to adapt their often ad hoc platform strategy for a better solution.

No matter where you are in your internal developer platform (IDP) journey — and whether you’ve [built or bought it](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/) — you need security, role-based access control (RBAC) and consistent observability throughout the many layers of your modern tech stack.

Here are considerations for what you need — in addition to Kubernetes — for a [platform engineering strategy](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) that improves speed while decreasing developer cognitive load. Hopefully, it lightens your platform engineers’ load, too.

## The Death of DevOps and the Rise of Platform Engineering

“Platform engineering is nothing new. It’s what organizations have been doing for many years, with a specific team having control,” Nutanix’s [Jose Gomez](https://www.linkedin.com/in/pipoe2h/) told me. New technologies, notably containers, have prompted a return to “the idea of a horizontal team, but this time, we are not going to slow down developers,” he said.

According to [Team Topologies](https://thenewstack.io/how-team-topologies-supports-platform-engineering/), platform engineering is a team or group of teams focused on creating and maintaining a platform or set of platforms that enable other teams, including software engineers, to build and deploy software more efficiently.

Based on his 20 years of doing platform engineering, Gomez said the main difference today is the wrapper. By shifting from virtual machines (VMs) to containers, the IDP becomes a speed and portability enabler, not just another hoop for app teams to jump through.

Platform engineering rose in popularity, in part, when the [DevOps](https://thenewstack.io/introduction-to-devops/) principle of “[You build it, you run it](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/)” grew insurmountable in the face of the modern stack’s complexity. DevOps-driven ownership often requires application development teams to understand five-, six-, even seven-layer stacks. These app teams — usually scrum teams of five to nine members — have to manage both development and operations, which comes with a significant cost and usually a lot of duplicate work. Each team needs its own DevOps engineer to get to production. And there are still too many other teams — quality assurance (QA), security, networking — in the loop. This not only slows the path to production further, but it can also introduce security and reliability risks, which can increase downtime and breaches.

DevOps was just too much ops, so the devs felt left behind. App teams are supposed to be focused on driving value to the end users — not finding innovative pathways to production.

DevOps sees “too much cost going into operations, duplicated knowledge,” Gomez said, “instead of having one team that can share all that knowledge and be consistent on the tooling,” as in the platform engineering model. Needing to learn fewer tools “translates into lower risk and cognitive load,” he opined.

## Golden Paths Simplify, Standardize Innovation

A platform engineering team, he continued, brings the networking, backend automation, operations system and security teams together to lay down guardrails and tracks to follow.

In other words, the platform engineering team creates a [golden path to production](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/) as the easiest way to accomplish repeat tasks. That path establishes policies for going into production — but without closing off the path to innovation, Gomez explained.

“Meaning that, if you want to go into production, we are not going to slow you down, but you need to follow these standards” and use the designated tools, Gomez said.

An IDP can also enable innovation by creating a sandbox where app teams and data scientists can safely innovate. Then platform teams can validate new use cases, and, once the value of a proof of concept is established, can make that new feature or dev tool enterprise-ready, add it to the golden path and provide training to encourage adoption.

## Open Source Isn’t Free

[Open source software](https://thenewstack.io/open-source/) (OSS) is ever popular because it’s affordable, easily customizable and expansible. And developers love the autonomy that comes with it.

But just because OSS may not have a licensing cost does not mean it’s free. Precisely because it doesn’t have a direct cost, teams feel more able to adopt OSS, which results in tool sprawl and maintainability costs.

With more than 230 open source choices within the [Cloud Native Computing Foundation (CNCF) Landscape](https://landscape.cncf.io/) alone, engineering teams experience decision overload — not to mention [DevOps burnout](https://thenewstack.io/devops-burnout-try-platform-engineering/), having to update, patch and maintain their choices.

Perhaps most importantly, since OSS is often part of shadow IT, where organizations don’t know what is being used or what data is being exposed, security vulnerabilities often go overlooked. The [mean time to remediate open source vulnerabilities](https://www.arxiv.org/pdf/2504.14026) is now 400 days.

Platform engineering has risen to help rein in open source sprawl, as well as to centrally manage updates.

As organizations scale their platform engineering program and enter Day 2 operations, an opinionated developer platform can help give visibility into the open source supply chain by maintaining software bills of materials (SBOMs). A proprietary platform can also scan images for patches and then automate patching libraries, dependencies and other vulnerabilities. This takes the burden off individual teams to maintain software, while also making sure there are no security holes ready to be exploited.

## Start by Building, Grow by Buying

Organizations usually start by building their own platforms with open source tools. Manual isn’t a bad place for an IDP to begin, Gomez said. It’s not uncommon for an early platform engineering strategy to be about building a platform piecemeal, usually out of open source projects. And, despite working at an IDP vendor, Gomez is not rushing to tell everyone to buy right away. Rather, he sees the value in do-it-yourself early on.

Kubernetes expert [Kelsey Hightower](https://thenewstack.io/tech-works-how-to-build-a-life-long-career-in-engineering/) refers to this as “[Kubernetes the hard way](https://github.com/kelseyhightower/kubernetes-the-hard-way).” He says it is “optimized for learning, which means taking the long route to ensure you understand each task required to bootstrap a Kubernetes cluster.” That might not even be a production-ready pathway, but rather a good way to get platform engineers up to speed with Kubernetes.

At some point, your IDP may grow to include 20 or more open source tools, which must be tested, validated and deployed whenever an update occurs. But platform engineering teams aren’t meant to scale with the rate of IDP adoption, not to mention competing stakeholders and demands.

The cognitive load you are taking off developers ends up resting on your platform engineers’ shoulders. “You have a very expensive team because these people are super skilled, very knowledgeable,” Gomez observed, and you probably don’t want them “spending time on testing and validating, versus taking that developer experimentation from the sandbox and preparing it to add additional value on the golden path on that platform.”

Eventually, platform teams become overwhelmed trying to balance maintenance and new features. During this transition, you’re likely to grow out of your “build your own platform” stage and evolve into the “buy an opinionated platform” stage, one that includes best-in-class or most-used open source projects and handles updates for you.

An opinionated Kubernetes platform like the [Nutanix Kubernetes Platform](https://www.nutanix.com/products/kubernetes-management-platform) (NKP) acts as a centralized control plane to manage your environment, create and upgrade clusters, and deploy applications. This tactic not only enables better fleet management and consistency across your containers, but also efficiency, speed and reusability. This single viewpoint also allows policy management and observability as clusters scale past five to 10 or more.

## Components of an Enterprise-Grade IDP

Kubernetes cannot stand alone. Depending on the scale of your engineering organization, other pieces need to be built into your IDP.

A production-ready, cloud native platform demands the following components from the start:

* Networking with L4 and L7 load balancing and network policy support.
* Storage, as more containerized applications require persistent storage.
* [Observability](https://thenewstack.io/observability/), including metrics, logging and tracing.
* A container registry to privately host container images.
* [Security](https://thenewstack.io/security/) enforced across all layers, with immutable operating systems and self-encrypted disks.
* HTTPS certificates between microservices and RBAC.

This is the [minimum to run Kubernetes in production](https://thenewstack.io/5-tips-to-deploy-production-ready-applications-in-kubernetes/), but as cloud native organizations grow, so do their needs. Day 2 has you scaling out clusters with more nodes, so you soon require:

* Multicluster orchestration
* Consistency and standardization
* Security and compliance
* Operational efficiency

Supporting this scale soon demands more advanced components, such as:

* GitOps with a history of changes, approvals and rollbacks
* Policy management
* Service mesh
* Cost management
* Fleet management

[Service mesh](https://thenewstack.io/introduction-to-service-mesh/) is complex, Gomez advised, so wait to add it until you have to manage and secure communication between microservices in a distributed application. A service mesh is a dedicated infrastructure layer, with features like traffic management, observability and security. A platform that integrates service mesh enables both platform and app teams to see which part of an application is experiencing which load.

Cost visibility, or [FinOps](https://thenewstack.io/finops-the-why-what-and-how/), is another area cloud native organizations are still struggling with, as they often over-resource to ensure scalability. Platform-led fleet management can provide suggestions for (and even automate) resource reallocation, which is better for budgets and the environment.

To simplify setup and management, you may wish to select a platform like NKP, which includes components required to deliver a scalable production stack, built on open standards, so developers can use their preferred toolchains while platform engineers can adapt their environment over time.

## The AI Sandbox on the Platform

Platform engineering has risen from hype to widespread adoption, in part as a way to bridge the gap between business and engineering. Now, in the [age of AI](https://thenewstack.io/ai/), the platform engineering team can bring software engineers and data scientists closer.

For example, platform engineering can better meet data scientists’ compute requirements, Gomez said, because it’s built on automation and Infrastructure as Code (IaC). This enables platform teams to equip data scientists with VMs through Kubernetes, which becomes a way of orchestrating data science jobs, automatically scheduling on infrastructure nodes that have GPUs. This pathway allows data scientists to share resources more efficiently, rather than running processes on individual computers and making requests when they need to scale up.

“Instead of using PCs in a siloed fashion, why not create a pool of servers with GPUs and run Kubernetes on them?” Gomez asked. “With this node pool, Kubernetes can schedule AI jobs coming from data scientists, making better use of your investment in GPU power.”

Plus, so much of the onboarding, RBAC and security across development and data science use cases is the same, so why not manage it within a single platform? Then, when models are ready for production, they can be deployed via the same golden paths.

Developers, on the other hand, want to explore and use AI throughout the software development life cycle to foster intelligent operations. Platform engineers can leverage AI use cases to analyze the quality of code and compare what’s written by developers versus what is generated by AI. Or they can use AI to pull data and make predictions around Jira tickets.

Again, a platform facilitates sandboxed innovation, which can later be turned into applied use cases.

Finally, with all the software development AI use cases tucked within the IDP, it becomes easier to [measure the return on AI investment](https://thenewstack.io/how-to-measure-the-roi-of-ai-coding-assistants/), which many organizations forget to do, Gomez emphasized.

## The Bottom Line: Empowering Developers

While most developers aren’t looking to build platforms, they do want the advantages a platform brings. They also want Kubernetes, but they want it running behind the scenes, where they don’t have to worry about it.

Ultimately, Gomez concluded, success with platform engineering comes down to “how much you embrace the technology and adapt your processes enabled by that technology.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/24668a31-cropped-cfb880a9-jkriggins-2019-headshot-the-new-stack.jpeg)

Jennifer Riggins is a culture side of tech storyteller, journalist, writer, and event and podcast host, helping to share the stories where culture and technology collide and to translate the impact of the tech we are building. She has been...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)