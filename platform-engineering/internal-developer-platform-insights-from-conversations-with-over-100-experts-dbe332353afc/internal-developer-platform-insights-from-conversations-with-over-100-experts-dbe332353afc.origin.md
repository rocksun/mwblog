# Internal Developer Platform: Insights from Conversations with Over 100 Experts
## Is an Internal Developer Platform the Next Right Step for You?
Note:Thank you for the great input on this topic. I’ve received insights from Internal Developer Platform operators, companies that failed, companies that regret it, companies that are happy with it, and those that turned it into a product or SaaS solution. I’ve explored the value it brings and found that, in the end, many solutions share a similar logic.
# What have I learned, and what’s my opinion on the IDP Hype?
I’ll get straight to the consolidated output from my conversations. I’ve already written an article on what makes up an IDP and how it fits together: [ Internal Developer Platforms: A Real Thing or Just a Trend?](https://medium.com/me/stats/post/ee9c97870dcc)”

## 1. Internal Developer Platforms Can Be Anything and Nothing
You heard it right. There is no definitive definition of what an Internal Developer Platform (IDP) is. Many attempts have been made to define a maturity model for an IDP based on attributes, automation levels, and the value it provides.

I’ll keep it simple and show you what different companies understand by an IDP.

An IDP can simply be a documentation or guide with a blueprint provided to other teams. In this context, companies are not talking about [Terraform modules](https://www.terraform.io), [Helm charts](https://helm.sh), or package tools like [APT](https://wiki.ubuntuusers.de/APT/). What they really mean is something like:

Yes, you see it right. There are companies that say if we provide a blueprint with placeholders that can be used by different developers, then it qualifies as an IDP for us. I somewhat agree with this perspective. Team X provides a template to one or more teams with instructions on how to consume a service as self-service.

An IDP can also consist of Terraform modules that a team member configures and deploys locally based on a guide for the other users. It would look like this:

This aligns more closely with my understanding of what an IDP is. You provide Infrastructure as Code or Configuration as Code, and only user-defined configurations need to be set up.

An IDP can also be a portal that has achieved a relatively high level of automation. This means that I can request a template in a specific T-shirt size with a click or through an API and get everything deployed automatically. This refers to something like:

You can see that different companies have varying understandings of this, and there are also some reasonable justifications for those differences. I’ll address that later.

Below, I’ve attempted to capture the different states of the companies I’ve spoken with.

## 2. Maturity level of Automatization
In this section, we’ll examine the different states of the companies. This is not about the quality of the level but rather a classification of where one sees oneself or operates.

There is an excellent piece of work from the CNCF WG Platforms, which contributed to the white paper and developed this great graphic titled [ Capabilities of Platforms](https://tag-app-delivery.cncf.io/whitepapers/platforms/):

If you understand the capabilities of platforms, you likely have a broader perspective than many small to medium-sized enterprises whose core business is not software or product development.

That’s why I tried to abstract it to simplify the concept. I created a stack that should be familiar to everyone. In the next step, we’ll look at different levels of automation.

**Level 0: ClickOps**
There are still many companies that prefer [ClickOps](https://blog.equinix.com/blog/2022/12/01/what-is-clickops-and-how-can-you-prevent-it/), whether on-premises or in the cloud, because they believe it is faster. I won’t judge this approach; it is simply the case.

**Level 1: Scripting: Bash, Python or PowerShell**
Many companies understand automation as running scripts. Since this isn’t done through clicks, they see it as automated. Again, I won’t pass judgment on this.

**Level 2: Infrastructure as Code and Configuration as Code**
The next level from scripting, in my opinion, is using tools like Terraform to provision infrastructure and tools like Ansible to configure it.

**Level 3: Pipelines: IaC + CI/CD or Operators with CRDs**
Taking a step further, IaC would no longer be executed locally from the client device, but through a pipeline, or you would use a tool like Crossplane, which automatically provisions the corresponding resources.

**Level 4: Terraform Modules, Helm Charts and GitOps**
When professionalizing, you would package recurring parts of infrastructure into Terraform modules to provision infrastructure or a Kubernetes cluster, for example. Subsequently, you would use a GitOps approach to deliver infrastructure as an application to the respective clusters. The level of automation here is quite high. By “quite high,” I mean:

- Can I scale with growing projects?
- Can I also scale maintenance and operations to avoid technical debt?
- Can I scale the setup without needing to increase the number of employees?
This is still executed by people, specifically the platform team.

**Level 5: Replace Human with Portal**
The next level would involve replacing the human component at Level 4 with an abstraction layer. This doesn’t mean that the platform teams are replaced; someone still needs to build the Terraform modules, Helm charts, pipelines, etc., so that these can be rolled out via a template.

I find it important to understand which level you are at, as I often correlate this level with the skills and resources within companies. From my observations, there seems to be a **correlation** between a **low level of automation** and **heterogeneous infrastructures**, which in turn interacts with companies often facing resource bottlenecks and scaling through employees.

This also often reflects the skill level. This doesn’t mean that the people are poorly skilled; quite the opposite, in fact. It refers to where my company currently stands on the cloud-native roadmap (are we using Git, are we using containers, CI/CD, do we have IaC and CaC, etc.).

I’ve attempted to map this, and I believe many will understand it. First, let’s look at some important skill set points on the cloud-native roadmap. Low is bad, and high is good.

Now we are trying to identify these points at the automation level.

**Imperative **refers to a command or directive that instructs someone to perform a specific action or task.
**Imperative**
**Containerization** is the process of packaging applications and their dependencies into containers, allowing them to run consistently across different computing environments.
**Containerization like with Docker**
**Deklarative** refers to a programming approach where you specify *what* the desired outcome is without explicitly outlining the steps to achieve that outcome, allowing the system to manage the implementation details automatically.
**Deklarative**
**API-Driven** refers to a design approach that prioritizes the use of application programming interfaces (APIs) as the primary means of interaction between different software components, enabling seamless communication and integration across systems.
**API-Driven**
**Package-Management** is the process of automating the installation, upgrading, configuration, and removal of software packages, ensuring that software dependencies are correctly managed and maintained across different environments (Helm Charts, APT, etc.).
**Package-Management like Helm Charts**
**Orchestration** refers to the automated coordination and management of complex processes or workflows, often involving multiple services and systems, to ensure that they work together efficiently and effectively (Kubernetes).
**Orchestration like Kubernetes**
As you can see, there is a correlation that can be summarized as follows:

**Level 0–1:**Primarily imperative approaches, with no containerization or orchestration.**Level 2–3:**Transition between imperative and declarative, with initial steps toward containerization and API integration.**Level 4–5:**Strong focus on declarative approaches, extensive use of containerization, orchestration, and API-driven environments, along with package management.
## 3. How IDPs Fit In and What They Offer
Most solutions I’ve seen are logically structured in a similar way. A portal is offered, typically based on an Internal Developer Platform, which is generally held together by an [Operator](https://www.redhat.com/en/topics/containers/what-is-a-kubernetes-operator). This means there is a way to transform infrastructure into a template, making it usable. In other words, there is an abstraction layer that simplifies usage.

Thus, there are usually at least two sides involved. For example, there is the **platform team that defines templates** so developers can use them more easily. **The developers then become users of these templates or can use the same tools to abstract their own applications**. But what does abstraction mean in this context?

Let’s take a look at the following diagram:

It is clear here that the platform team abstracts and defines everything necessary to deploy a web application service. The developer only sets 2–3 values instead of wrestling with the entire Kubernetes manifests, and a web application is deployed by an operator. This has been presented in a simplified manner, but a portal based on an IDP essentially does nothing different — just more complex. If you replace the simple diagram above with the orchestrator from Humanitec, you will see a certain similarity in logic:

## 4. For Whom is the Use of an IDP Suitable?
Before I attempt to answer this question, let me show you the following diagram. Please take a minute to think about it:

I personally believe that before delving into the topic of Internal Developer Platforms and portals, one should first **assess the level of automation**. The term “automation level” should not be taken literally here but rather understood as a synonym for understanding where we currently stand and why. If you find yourself at **Levels 0–1**, I personally question what you want to integrate into the portal — scripts? If you’re at** Levels 2–3**, you might consider investing more to reach **Levels 3–4 before** tackling the IDP topic. It’s better to close the gaps, including skill gaps, to create a solid foundation for an IDP with a portal.

Most companies I’ve encountered that built an IDP, for example, based on Backstage, were **at Levels 4–5**. For them, Docker, CI/CD, IaC, Kubernetes, etc., have **become basic skills**, allowing them to move forward with other topics.

When you start learning mathematics, you begin with the basic arithmetic operations and don’t jump straight into advanced university mathematics. I believe the same applies to an IDP + portal. It’s better to **establish a solid foundation** in the company instead of following trends that you can’t afford.

## 5. Make or Buy?
Most companies I’ve spoken with, particularly those listed below as non-providers, tend to favor SaaS solutions or self-hosted options, with SaaS being the preferred choice. Many companies are hesitant to use an IDP because they don’t want to replace the human component associated with Platform Engineering.

**Most of the statements (against MAKE OR BUY) I heard on the subject were like:**
- Providers offer managed services, and their internal teams or external clients have smaller teams, making the effort to implement an IDP not worthwhile.
- However, many companies prefer to professionalize their various layers first before embarking on building an IDP, ensuring a solid foundation.
- Some companies say they are much faster with platform engineering and human component that replaces the portal. Don’t need to MAKE OR BUY and IDP/Portal.
- The complexity is already quite high, and adding another layer would not help a company move forward.
**Personal Assessment to MAKE or BUY:**
- Companies at Level 0–3 face different challenges than those involving an IDP/Portal. ❌
- Service providers should consider → BUY or MAKE (Innovation, new product, etc.)
- In-house IT companies with fewer experts but at Levels 4–5 → BUY.
- Companies with fewer Platform Engineers and small developer teams should consider → BUY or DO Platform Engineering.
- Companies with 10–15 Platform Engineers and 500–1000 developers should → BUY.
It is not an easy decision. I always try to think in terms of values and ask myself, what added value does it give the company?

- Innovation?
- Better time to market?
- Scalability through self-service?
- Reduction of the congitive load on the Platform Enginners?
- etc.
However, one point deeply concerns me about all these topics, which I will briefly address next.

## 6. Why is the focus so heavily on developers?
I don’t understand why everyone talks about enabling developers; sometimes it feels like treating developers as if they were small children trying to ride a bike without training wheels. Are companies in IT really made up solely of developers? To be honest, it annoys me that the rest of the IT professionals in companies are often overlooked. Is the goal to split the culture and then bring it together through DevOps 3.0 in the organization?

We failed to create a culture between developers, operations, and other departments with DevOps, and now there’s Platform Engineering.

To help you understand my frustration, let me share a development that didn’t arise thanks to Platform Engineering, even if it might seem that way, but through GitOps with tools like Argo CD. This year, a new culture has emerged at a large company, and I was there live and involved.

In the past, Platform Engineers/Ops collaborated more closely with developers than with other teams.

Now, however, a form of collaboration is emerging that I never thought would happen.

I see service owners taking a hands-on approach, learning how to manage Grafana dashboards and Prometheus alerting as code and deploy these across different clusters using Argo CD. This increases the quality of the service because they understand how the service should operate. It enhances collaboration with developers and operations, as they suddenly speak a common language (YAML). Additionally, there are service providers who deliver a service across multiple clusters and, as product operators, now deploy their external custom alerting using the same GitOps (multi-tenancy separation) practices.

If IDPs continue to be built with a developer-centric focus, I fear that the emerging culture will crumble, and we will need DevOps 3.0 in the future to rebuild it.

You should definitly take a look at [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)!
Next, I will show you the best-known portal providers, both as SaaS and self-hosted solutions, with many of whom I have had exchanges or received input.

# Which portals exist?
Here is an overview of portals I know from the exchange.

[port](https://www.getport.io)[Mia](https://mia-platform.eu/)[Humanitec](https://humanitec.com/)(Portal based on its own orchestrator + score)[Appsmith](https://www.appsmith.com)[Mogenius](https://mogenius.com/)[Qovery](https://qovery.com/)[OpsVerse](https://opsverse.io)[OpsLevel](https://www.opslevel.com)[Flanksource](https://www.flanksource.com)[Portainer](https://www.portainer.io)[Kubermatic Developer Platform on KCP](https://docs.kubermatic.com/developer-platform/)[GiantSwarm](https://docs.giantswarm.io/vintage/platform-overview/)(Platform based on Backstage)[suXess](https://suxess-it.com)(Platform based on Backstage + Kargo)[kratix](https://www.kratix.io/)[Wayfinder](https://www.appvia.io/wayfinder)
If there are any missing, please write it in the comments!

You want to make a contribution to the topic, then Go! → [https://tag-app-delivery.cncf.io/](https://tag-app-delivery.cncf.io/)

# Contact Information
Got questions, want to chat, or just keen to stay connected? Skip the Medium comments and let’s connect on [LinkedIn](http://www.linkedin.com/in/lajko) 🤙. Don’t forget to subscribe to the [Medium Newsletter](/@artem_lajko/subscribe) so you never miss an update!