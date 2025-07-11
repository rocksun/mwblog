When [Kubernetes](https://thenewstack.io/kubernetes/) came onto the tech scene about a decade ago, it quickly became the shining example of the grassroots, bottom-up developer story.

This open source project was a fast developer favorite as it promised an easy way to orchestrate containers at scale, providing automation, self-healing and simplified deployment processes. It facilitated the separation of constraints that devs were dreaming of while also letting them get as creative and custom as they needed.

But this Kubernetes flexibility doesn’t scale smoothly across teams and organizations so easily. Enterprises continue to struggle with scaling, security, governance and platform consistency. And they’re finding themselves stuck again — unable to move between cloud providers and overwhelmed by the complexity of Day 2 operations.

DevOps and this shift toward the cloud have left developers and operations bearing immense [cognitive load](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/). Organizations have long-standing tool sprawl and Software as a Service (SaaS) subscription fatigue. All while most teams are trying to do more with less, including managing [large-scale AI adoption](https://thenewstack.io/ai/).

Over the last few years, [platform engineering](https://thenewstack.io/platform-engineering/) has risen as a way to abstract away layers of operational complexity through creating golden paths — the simplest, self-serviced routes for developers to accomplish “[non-differential but not unimportant tasks](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/)” like provisioning containers and deploying to the cloud. It’s achieved via an [internal developer platform (IDP](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/)), which creates a single automated operating model for Kubernetes, operated by a centralized platform engineering team. When implemented well, it also enables a common language among technical, business and compliance stakeholders.

I sat down with the team behind [Nutanix Kubernetes Platform](https://www.nutanix.com/en_gb/products/kubernetes-management-platform) (NKP) to further dive into these trends dominating enterprise IT strategy.

## The Kubernetes Complexity Challenge

According to the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), [80% of organizations have adopted Kubernetes](https://www.cncf.io/reports/cncf-annual-survey-2024/). But just because it’s prevalent, doesn’t mean Kubernetes management is easy.

After all, Kubernetes is complex by design, whether you’re deploying across clouds, on premises or in edge environments.

This container orchestrator was originally built and then open sourced by [Google](https://cloud.google.com/?utm_content=inline+mention) to simplify application development by abstracting away the underlying infrastructure. However, this means any team in charge of adopting Kubernetes needs to then not only understand Kubernetes — including pods, deployments, services and ingresses — but also its many interacting components, including the Kubernetes API server, etcd and Redis stores, kubelet, kube-proxy, policy management, controller managers, controller schedulers and more. These measures are incredibly difficult to scale.

While many organizations choose the cloud for simplicity, there are still challenges with Kubernetes due to hidden costs as well as lack of portability.

For example, Kubernetes is known for its flexibility, allowing for a vast array of configuration options, which only adds to variety — and complexity. This makes Kubernetes logging and monitoring particularly challenging without centralized visibility into clusters. Visibility is not only essential for compliance and security, but also for performance.

Managed Kubernetes from cloud providers can provide the necessary monitoring, but that can greatly increase costs — and take away the option of portability, one of the primary benefits of Kubernetes.

There are also state-of-the-art open source solutions available, but using them means increased responsibility for the platform engineering team, including mitigating common vulnerabilities and exposures, testing compatibility and rolling out new versions across a fleet. They must also have a solid grasp of the underlying infrastructure, including the codebases, networking and operating systems, to avoid common cloud migration roadblocks.

Since most enterprises are running Kubernetes in more than one location — on premises, in the cloud and [at the edge](https://thenewstack.io/kubernetes-fleets-beyond-the-iot-edge/) — platform engineering teams have to be ready to deal with varying levels of abstraction, automation and responsibilities, as Kubernetes can be deployed across bare metal, virtual machines (VMs) and/or in the cloud.

Don’t forget enterprise decision paralysis. Most notably, the [Cloud Native Computing Foundation landscape](https://landscape.cncf.io/) seems to be ever-expanding, meaning that these open source tooling options and adoptions are continually adding to this complexity.

“There are a lot of [hidden costs associated with deploying Kubernetes in the cloud](https://webthesis.biblio.polito.it/secure/21146/1/tesi.pdf). While cloud providers focus primarily on Kubernetes orchestration, enterprises still need to integrate additional capabilities to Kubernetes enterprise-grade including observability, networking, service mesh and other tools needed alongside Kubernetes,” said [Dan Ciruli](https://www.linkedin.com/in/danciruli/), cloud native product leader at [Nutanix](https://www.nutanix.com/en_gb) and co-founder of the OpenAPI Initiative.

Even if they adopt the best tool stack available, individual DevOps and platform teams still have to spend time making updates — configuring security patches and new features — then testing compatibility, before rolling out the patches and upgrades across the organization.

And, because Kubernetes doesn’t have built-in tools to audit whether protection is correctly configured, these teams need to work with site reliability engineering (SRE) and cybersecurity teams to integrate the right security policies and monitoring. It’s no wonder that DevOps and platform teams are facing burnout in response to widespread Kubernetes adoption.

However, by establishing consistency across environments, the [Nutanix Kubernetes Platform (NKP)](https://www.nutanix.com/en_gb/products/kubernetes-management-platform) aims to reduce this operational complexity.

## A Return to Stateful Storage

While Kubernetes was originally created with ephemeral, stateless workloads in mind, as more and more workloads are deployed in Kubernetes, the need for stateful workloads becomes greater.

Stateful workloads retain persistent, reliable and consistent data, within context, across sessions, requests and even application restarts. Stateful data is necessary for databases, financial systems, real-time communication, email servers, messaging queues, content management systems and even e-commerce shopping carts. And while cloud providers often provide storage for their hosted solutions, both industry and regional regulations increasingly require on-premises data storage for compliance. It’s also essential for quick and detailed incident management and disaster recovery.

No matter where the data sits, higher volumes of stateful data are being deployed in a Kubernetes environment. And there’s a demand to support both stateful and stateless workloads, despite the industry still lacking “prescriptive guidelines for choosing between stateless and stateful architectures, often leaving architects to rely on contextual judgments and experiential heuristics,” [according to MIT researchers](https://www.researchgate.net/publication/391017476_Stateless_vs_Stateful_Microservices_Design_Considerations) Mei Song and Margaret Joshua.

Kubernetes provides persistent volumes (PVs) and persistent volume claims (PVCs) to address the stateful demand for reliable storage, consistent network identities and stable scheduling. Even so, managing storage access modes, performance and capacity adds [significant complexity](https://www.researchgate.net/publication/392125011_Stateful_Application_Management_in_Kubernetes_Environments) for DevOps teams to manage across stateful workloads in Kubernetes.

Add to this, homegrown IDPs and most out-of-the-box container platforms don’t have integrated storage or data services, or perhaps they don’t have enough storage to meet the demand of new customers or new AI-based workloads.

Enterprises are often left with having to “bolt on” extra storage capacity — either cloud storage, which limits portability, or buying on-premises storage, which introduces yet another vendor, said Ciruli.

This “less-than-duct-tape” approach to extra storage, he continued, usually results in a fragile integration that risks data inconsistencies, which in turn can trigger both finger pointing and tracing problems.

Once you get that data in the cloud or on-premises, it becomes again very difficult to transfer that data to support a hybrid or multicloud strategy.

## AI Accelerates Adoption of Kubernetes and Cloud

Now that AI is scaling both the demand for compute and the sheer size of codebases, it’s all about to get even more complicated.

[Gartner researchers](https://www.gartner.com/en/newsroom/press-releases/2025-05-13-gartner-identifies-top-trends-shaping-the-future-of-cloud) predicted in May that, by 2029, 50% of cloud compute resources will be devoted to AI and machine learning (ML) workloads.

“Now is the time for organizations to assess whether their data centers and cloud strategies are ready to handle this surge in AI and ML demand,” said Joe Rogus, director of advisory at Gartner, at the most recent Gartner IT Infrastructure, Operations and Cloud Strategies conference. “In many cases, they might need to bring AI to where the data is to support this growth.”

Ciruli agreed, telling me, “I think AI is going to be on prem. It’s going to be in the cloud. It’s going to be everywhere. It’s going to be on a mobile phone — it’s already there. All cloud apps are eventually going to be AI apps, right?”

However, he emphasized, AI is hard to implement due to the complexity of Kubernetes.

“With AI applications, it’s good to build them on containers because that gives you scalability and the portability that you would need,” Ciruli said.

“Because AI requires these containers as a foundation, a lot of companies are now starting to think about actually having to manage these containers at scale,” often for the first time.

A lot of organizations still don’t have the basics down, Ciruli added, including microservices and cloud native architecture. Let alone how to do Kubernetes and cloud at scale.

## The Case for Platform Engineering

Enterprises would [need to spend 3.5 times more on software](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4693148) than they currently do if open source software didn’t exist. But by no means does open source translate to free.

The complexity of open source — and especially the cloud computing and Kubernetes that drive that adoption — has triggered massive tool sprawl. Most enterprises don’t have insight into which  tools have been adopted and what data is being exposed across tens of thousands of internal and external APIs. And they are not prepared to scale and maintain Kubernetes.

Most organizations are left with do-it-yourself, ad-hoc ways, as engineers have engineered their own pathways to the cloud. This simply doesn’t scale across hundreds, thousands or tens of thousands of engineers within the enterprise environment.

Perhaps most importantly, Kubernetes management has become toil that distracts from the [true objectives of DevOps teams](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/):

* Flow toward business value.
* Faster feedback loops.
* Continuous experimentation, learning and improvement.

Having DevOps manage Kubernetes quickly becomes inefficient and leads to greater technical debt, including manual processes, a lack of automation and configuration drift, when there’s a disparity between what’s in your repositories and what is actually deployed.

As Govardhana Miriyala Kannaiah wrote in “[Kubernetes Anti-Patterns](https://www.oreilly.com/library/view/kubernetes-anti-patterns/9781835460689/),” this debt then leaves DevOps teams spending a significant portion of their time managing existing systems, instead of innovating: “It’s the interest that accrues as you choose shortcuts, bypass best practices and opt for expedient solutions.”

DevOps teams benefit from the platform’s paved roads as much as application teams do.

Platform engineering has risen as an answer to this complexity at scale, as a way to better abstract that Kubernetes abstraction. And the platform team has formed to ease much of the DevOps workload. Which in turn also eases developers’ cloud native cognitive load.

“There’s a lot of ambiguity, knowledge gaps, things that developers know they don’t know. Developers don’t need to know the infrastructure platform,” Ciruli said. “We are, in fact, asking the platform engineers to build that platform and to serve it to them so that they don’t have to worry about the backend. They just have to worry about applications.”

Then as enterprises approach Kubernetes adoption, he continued, “they want to serve up a platform to DevOps, to make their lives and experience a lot richer and easier, and to streamline that process.”

## What a Platform Engineering Strategy and IDP Deliver

A platform engineering strategy, whether based on a  [build-your-own or a SaaS-based platform offering](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/), is a way to do more with less. It takes away some of the extreme developer autonomy and tool sprawl that marked the 2010s and trades it for the convenience of [golden paths or opinionated workflows for common processes](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/), standardized permissions and greater visibility across organizations.

Often, a platform engineering strategy kicks off with a focus on discoverability. It allows platform engineering, SRE and security teams to get a cross-organizational view of:

* What’s already adopted.
* Where dependencies are.
* Who owns which services and APIs.
* What data is being exposed within and outside the organization.

An [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") emphasizes self-service so that developers can figure things out faster and just get things done. This usually cuts costs because it enables greater reusability of those services and APIs, instead of just building everything from scratch. An IDP is usually built with a search engine or, more recently, a conversational AI overlay, which enables search and documentation, helping get back the average [one day a week developers waste looking for things](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/).

While an IDP intentionally focuses on building what internal DevOps and engineering customers actually want to use, it does include some features of its predecessors, like role-based access control.

An internal developer platform centralizes software life cycle management, enabling single-deploy security patches and upgrades. This is essential because, according to the Infosec Institute, on average, it takes [60 to 150 days to remediate a vulnerability](https://allaboutgrc.com/vulnerability-remediation-timelines-how-fast-should-you-patch/), which, depending on the vulnerability, can threaten your uptime, reputation and more.

Besides IT leadership feeling the need to cut costs while putting up more guardrails and processes in place, Ciruli said, “platform engineering for us is delivering that platform, which is open, complete, easy to install [and] easy to manage for DevOps [teams], to get their applications faster to market with easy-to-use self-service tools and capabilities.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/24668a31-cropped-cfb880a9-jkriggins-2019-headshot-the-new-stack.jpeg)

Jennifer Riggins is a culture side of tech storyteller, journalist, writer, and event and podcast host, helping to share the stories where culture and technology collide and to translate the impact of the tech we are building. She has been...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)