# Drive Developer Self-Service with Crossplane, K8s and a Portal
![Featued image for: Drive Developer Self-Service with Crossplane, K8s and a Portal](https://cdn.thenewstack.io/media/2024/04/1be90012-green-1024x576.jpg)
There’s a real pain so many engineering organizations are feeling right now: On the operational side, engineers are trying to frantically manage the infrastructure, and in the meantime, the application developers who are consuming the infrastructure are increasingly being asked to understand more about the infrastructure and are therefore facing
[cognitive overload](https://thenewstack.io/devs-and-ops-can-this-marriage-be-saved/). The end result? Low velocity.
The reason for this pain is complexity: first, the emergence of
[Kubernetes](https://roadmap.sh/kubernetes) as the de facto operating system for the cloud, which requires in-depth technical knowledge that most developers simply do not have, and second, developers are drowning under the influx of the numerous tools and frameworks organizations are using.
To combat this issue, many teams may have attempted to use TicketOps to
[abstract away and remove the need for developers to come to grips](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/) with the infrastructure. However, this doesn’t scale for Day 2 operations. While it might initially simplify things for a developer, it can lead to the operations team being a bottleneck.
This is because it can take them days to weeks to respond to a provisioning request, as they need to ensure the request is in line with security requirements, policies, versioning issues and the like.
Operations then still have huge management complexity, and developers are delayed as a result. At the end of the day, developers just want to develop features and improve the products they are working on, and DevOps engineers want to be able to provide them with a way to do this seamlessly.
**It’s Time for a Platform Team**
It’s no wonder that Gartner believes that by 2026, 80% of engineering organizations will have established a
[platform engineering team](https://thenewstack.io/platform-engineering/). The analyst firm believes that platform teams will act as an internal provider of reusable services to application teams. In other words, the underlying [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) has to be able to offer true developer self-service, so that developers can perform actions again and again, with the platform engineers able to set the guardrails in place to ensure they can do this autonomously and securely. Such actions include infrastructure provisioning.
This is where the internal developer portal comes in. It acts as a single pane of glass that brings together all of the tools that make up the
[internal developer platform into one place](https://thenewstack.io/internal-developer-platforms-are-for-devops-too/). It provides an abstract view, giving developers autonomy and platform engineers a place where they can safely expose functionality and views to developers with the right standards in place to improve development velocity and developer experience.
**Platforms Require a Unified Control Plane**
But platform engineers also want a single point of control and management of their platform so they can consistently apply policies, security and other controls. Think of the way cloud service providers like AWS and GCP are able to offer services to end users because they’re designed around a unified control plane. This provides easy-to-consume APIs while automating management tasks for their own operators so they can support this huge platform.
This is exactly what you’d want at the base of your internal developer platform — a unified control plane built on top of the clouds. It should enable you to manage everything consistently and offer services to end users as APIs they can either consume directly or use to power a powerful developer portal interface.
The ideal recipe for a
[platform is an internal developer portal](https://thenewstack.io/how-do-the-internal-developer-platform-and-portal-connect/) equipped with a software catalog that leverages GitOps to control CD that talks to a cloud native platform powered by a control plane that has infrastructure management capabilities.
So how do the platform and the portal work together to expose that self-service functionality that benefits both developers and platform engineers?
Here we explore the use of
[Port](https://www.getport.io/) for your portal needs and [Upbound](https://www.upbound.io/) powered by Crossplane for your control plane needs.
**The Control Plane**
First of all, we can view the Upbound console, which shows us the control plane managed by Upbound. I can see whether my control plane is ready, and details about the configuration, the version and the AWS provider used by the control plane to interact directly with my AWS cloud account. This is the setup from Upbound, and Upbound will do the heavy lifting in the background by provisioning and managing the resources hosted by the cloud provider.
But for developers, this information isn’t really necessary. They don’t need to know the details about control planes and Kubernetes — they just want a simple and easy-to-understand UI where they can see their resources. The internal developer portal provides this abstracted UI, and it can also benefit the platform engineering team.
On the home page, a platform engineer would be able to see an action to request a new cluster. Before they trigger that action, they can take a look at what’s already in the software catalog, including their Upbound control planes and further details about it including all of the clusters that it manages and all of the cluster requests it has.
The question is: Why does it have all those clusters and cluster requests?
To answer this, we can look at the “builder” section to show you how it all works in the backend of Port. This is what the platform engineer uses to configure the way developers use the portal.
Above you can see the three blueprints. A blueprint is a fully configurable data object, a schema that you can model to fit the asset you want to represent. So here, there are three blueprints: Upbound control plane, Amazon Elastic Kubernetes Service (EKS)cluster and EKS cluster requests.
If we focus on a user requesting a new EKS cluster, we can consider some self-service actions for this.
First, we’ll look at two different ways to create a new cluster.
**Creating a New Cluster: Option 1 **
The first approach is for a platform engineer who wants to create a new cluster. They would simply go to the self-service hub and click on the “create new cluster” action. Then they would select their control plane, and put in all of the inputs (name, node size, node configuration). This form can be fully configured by the platform engineer. This means:
- It will make developers’ lives easier as they don’t have to think about the inputs.
- Platform engineers can be sure that the action is secure and complies with policies and standards by setting guardrails, for example, validating that the developer can only input legal values.
Once the engineer fills out the form, they can click on execute, and Port will create a new self-service action. This self-service action will start a GitHub workflow, which will open a pull request for the new cluster.
In this instance, as it is the platform engineer who is managing this — and they’re the ones who have already put all of the inputs and the workflow in place — the self-service action will automatically create that pull request and merge it straight away. This will appear both in the portal and as a new cluster in Upbound. Remember this new cluster, as we’ll circle back and check its progress a little bit later.
**Creating a New Cluster: Option 2**
A developer might need a new cluster as they’re working on a new feature. They may need resources, such as containers, to be able to run a database or a cache, and they want their application running alongside it. If the platform engineer has exposed an action to request a new cluster, the developer can navigate to the self-service hub and click on “request new cluster.” Once again, they can fill in the form, and keep inputs such as node size and node count as the default as they might not mean much to a developer. The platform engineer can resolve this further down the line if needed. Then, they can click on execute and the cluster will be requested and reviewed by the platform engineer, as we’ll see in the next section.
**EKS Cluster Request**
Moving on to the EKS cluster request. This is a way for the platform engineer to keep track of all the requests that he or she has for resources. This can be modified to any sort of cloud resource that Upbound can manage for you so it’s not just restricted to EKS clusters.
The view of this page can be extended and customized so that it can serve both the platform engineer and the developer.
When a new request is created, it’s carried out with two key components. The first is a pull request for the new resource — in this case, the EKS cluster.
And the second component is this new cluster request that we can see here, the status of which is pending.
As a developer, this helps you to stay in the loop and understand what is happening with your request and whether they are still waiting on something before approving the request and triggering the automatic provisioning step.
As a platform engineer, you can see which requests are waiting for approval, and decide whether you should approve them.
Now, if we look at our previous cluster, we can already see some of its resources are starting to reach a ready state, meaning we’ll have a new cluster in just a few minutes. Once a developer gets word that their request is approved, they know that in 10 to 15 minutes they’ll have a cluster up and running and be able to start working on their new feature.
**Personalized Views**
When all this information exists inside the software catalog, engineers, managers and developers can use it.
Below is the services dashboard, which shows the services — mostly GitHub repositories and microservices — that I have inside the portal. And you can see that I’ve added some information here: On the right-hand side it shows the number of EKS clusters that I have, which has been taken directly from the EKS clusters that we’ve deployed and that are managed through Upbound.
**Scorecards**
To take this a step further, I’ve also configured a few scorecards on the EKS cluster blueprint. That allows me to create an EKS readiness dashboard, which shows me all my clusters and how they are performing according to the standards that the organization has configured. In this example, two of the clusters are at the bronze standard and one of them is at silver, so I can see which clusters are failing and what is wrong with the clusters, and I can understand how I can improve their standing to make sure that they are all up to standard and production ready.
An internal developer portal coupled with a control plane can help you with the heavy lifting of infrastructure management and an easy-to-use UI and together can drive developer self-service actions.
The combination enables:
- A better way for platform engineers, developers and managers to view what matters to them.
- A way to reduce cognitive load on developers and time for platform engineers.
- A way to overcome complexity.
- A way to improve developer efficiency and provide them with increased visibility.
- A better developer experience.
Learn more about creating self-service actions in this
[webinar](https://event.on24.com/wcc/r/4516520/784A4348DFFDF36842719AAAD45C1808).
Check out our blog on
[improving developer workflows](https://www.getport.io/blog/improving-developer-workflows-through-a-better-developer-experience) through a better developer experience. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)