# Reddit No Longer Haunted by Drifting Kubernetes Configurations
![Featued image for: Reddit No Longer Haunted by Drifting Kubernetes Configurations](https://cdn.thenewstack.io/media/2025/01/ec2bcf77-reddit-1024x683.png)
When [Reddit](https://www.reddit.com/r/NewToReddit/comments/1aldxtm/can_anyone_explain_what_is_reddit_and_how_it_works/) went down on March 13, 2022, it was a rude reminder that the company needed to manage its infrastructure in a different way.

The notorious [“Pi Day” site-wide outage,](https://www.reddit.com/r/RedditEng/comments/11xx5o0/you_broke_reddit_the_piday_outage/) which, coincidentally, [lasted for 314 minutes](https://thenewstack.io/how-the-world-celebrated-pi-day/), came from a cluster-wide upgrade from [Kubernetes 1.23 to 1.24](https://thenewstack.io/kubernetes-1-24-drops-dockershim-makes-space-for-stateful-workloads/), that resulted in some subtle unpredictable behavior, forcing the infrastructure team to do a rollback, itself a high-risk action.

Even by then, though, company engineers knew a change in operations was needed.

The massively popular social news forum was expanding its server stack to work across multiple regions for greater reliability, with the goal of offering the service on a global scale. Other initiatives around ad delivery and machine learning came with their own challenges as well. Plus, company execs were preparing for an IPO.

The company needed a new platform abstraction, noted [Karan Thukral](https://www.linkedin.com/in/thukralk/), a senior software engineer at Reddit who works on the infrastructure team. As companies grow, they need new platform abstractions to continue to operate efficiently.

Thukral, along with Reddit Software Engineer [Harvey Xia](https://www.linkedin.com/in/harveyxia/), gave a presentation at the most recent KubeCon+CloudNativeCon North America on how the infrastructure team created a new platform abstraction to get ahead on planning and out of a reactive, fire-fighting mode.

“Technically, we’ve been able to do much more challenging problems with fewer people,” Thukral said. “Because of the amount of investment we’ve done over the past few years, it’s allowed us much more dedicated engineering time to proactively tackling problems rather than reactively firefight.”

## The Mystery Namespace
In 2022, the company ran 20 Kubernetes-driven production clusters. The infrastructure team had 92 engineers, considerably fewer than the 706 application engineers the company deployed. And much of their work consisted of helping the app engineers.

One issue was namespace creation. In Reddit, each application running on Kubernetes needs a [namespace](https://thenewstack.io/leveraging-namespaces-for-cost-optimization-with-kubernetes/), which can be specified by [Helm chart](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/) or [Kustomize manifest](https://github.com/kubernetes-sigs/kustomize). App developers weren’t experts in writing these specifications.

This led to a lot of cutting and pasting. As a result, errors crept in that weren’t always caught by reviewers. The review process added an extra 24 hours to the app review process.

It could take almost an entire week just to get the namespace out because of time-zone differences, Thukral said. And still bad configuration settings seeped into the entire [continuous integration](https://thenewstack.io/ci-cd/) process, which could result in downtime.

Reddit’s management of the namespaces was not consistent. “We couldn’t reason about the source of the namespace, whether it was being used or not,” Thukral said. Because of this, the company made a rule not to destroy any namespaces because engineers couldn’t tell if a namespace was still being used somewhere or not.

And all the outdated namespaces — of which there were plenty as the company moved its monolithic applications into microservices — still took up Kubernetes resources.

## Artisanal Clusters and Haunted Infrastructure
Meanwhile, the infrastructure team had its own challenges, Xia related.

It would take 30+ hours for an engineer to spin up a cluster, including over 100 steps, including those of configuring a network, provisioning hardware or picking a cloud vendor, installing a control plane, and adding on tools for observability and autoscaling.

Moreover, in-place upgrades of clusters were precarious, as Pi Day illustrated, and there was no process at all for decommissioning a cluster. Configurations of clusters still working had drifted and become bespoke in undocumented ways.

Decommissioning a cluster amounted to an “expensive archeology hunt to find all the different infrastructure that had to be decommissioned,” Xia said.

“It was a self-reinforcing cycle of inefficiency” — Reddit’s Harvey Xia

The organization had no good way to manage clusters across a fleet. Sometimes, infrastructure would drift so off from the specified configuration that it would be called “haunted,” Xia said.

“It was very hard for any engineer to reason with confidence reason about how the cluster ought to behave, or does behave, making all lifecycle operations extremely dangerous,” Xia said.

As a result, the infrastructure team’s hours were dominated by just keeping everything running and fixing outages.

This “reactive, firefighting mindset” made it hard to “imagine, plan or build for a more sustainable future,” Xia said.

## Why Reddit Chose K8s Controllers Instead of IaC
An abstraction hides complexity by separating the concerns of the user from the underlying implementation. A platform, by Xia’s definition, is an ecosystem of composable tools that developers can build off of. It is opinionated with the best practices of the company developers.

Reddit decided to implement a platform through a set of declarative APIs backed by Kubernetes control processes. The interfaces are defined as custom resources. The desired state is the specification, and the observed state is reported through the status.

The custom resources actuate Kubernetes controllers, which implement their APIs by mutating the active state towards the desired state.

The engineers originally considered an [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) tool but then went with one based on Kubernetes controllers instead.

With standard IaC, it is difficult to represent arbitrary business logic, which was a major requirement for building out Reddit infrastructure.

“I can’t model a workflow where I provision a TLS certificate from a cert authority, offload it to Amazon certificate manager, and attach it to a load balancer,” Xia said. Nor are standard IaC platforms dynamic. You can’t rely on IaC to renew lapsed certificates.

The Kubernetes controllers, in contrast, would ensure that the current state would always be at, or at least always be moved towards, the desired state. This would include all lifecycle operations.

## Brains and Workload Clusters
Today, Reddit infrastructure engineers spend less time managing the fleet. They have a set of APIs to manage multiple clusters through a “single pane of glass.”

The company has two types of clusters. One is the control cluster, which can be thought of as the brains of the operation. It generates configuration for the other, easily replaceable “workload” clusters.

“We started thinking of these clusters as cattle, not pets,” Thukral said.

This way, clusters have well-defined properties and all applicable configuration updates automatically flow into that cluster. Multicluster operations can be executed.

Each workload cluster has its own custom resource with labels for properties such as its operational phase (testing, production or staging), geographical location, and backing cloud vendor. This sets the stage for the multicluster API control. A federated controller manages clusters by K8s label selectors.

Cluster targeting is dynamic. If a new test cluster is spun up, it automatically joins the test namespace.

“This saves our engineers a ton of time,” Xia said.

There are some potential downsides to this approach. For one, the orchestration cluster is a single point of failure. But the system was designed so that the worker clusters can keep operating and self-healing, even if they can’t be updated. Limiting the kind of clusters that can be spun up also limits the variety of clusters that can be built, making them easier to manage overall.

[FluxCD](https://thenewstack.io/deploy-stateful-workloads-on-kubernetes-with-ondat-and-fluxcd/) is used to synchronize source configuration with the clusters. [Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/) is used to bridge Kubernetes APIs to cloud vendor resources. And [Cluster API](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/) provides the API for managing the Kubernetes control plane.
Each of these resources, or foundational primitives, is intermediated by Reddit’s own custom resources, allowing the company to swap implementations if it needs to.

Namespace creation has also been made easier for developers. Now, instead of learning Helm or Kustomize, Reddit app devs just create a customized resource called a Reddit Namespace, and target it to a group of clusters. For users, Role-Based Access Control (RBAC) is simplified to two options: operator or reader status.

## No Achilles Heel
To help infrastructure engineers create controllers and operators more easily, Reddit built the [Achilles SDK](https://github.com/reddit/achilles-sdk), which is built on top of the Kubernetes controller runtime.

This SDK represents the entire reconciliation loop as a finite state machine, Thukral said. Presently, this is handled by a single function, which can get rather unwieldy. A cluster built from Achilles requires far fewer steps than one an identical assembled under Terraform, Thukral said.

Achilles automatically tracks all child resources and state conditions.

“We wanted to enable our infrastructure engineers to just focus on building the business logic without having to become Kubernetes experts,” Thukral said.

## Results
Reddit is still in the process of building out the new infrastructure, though the company is already seeing results, the engineers boast.

The platform is much more scalable: No more headaches over namespace writing and management. Gains in security and app stack simplicity are also being realized.

The turn-around time for standing up a new cluster is now about two hours. An upgrade can be done in an hour. Thanks to Achilles, a controller can be created and tested in less than two weeks, “a huge success for us,” Thukral said.

The company started the year off with 4 Kubernetes controllers in production, and, as of KubeCon, the company has 12. These controllers manage aspects of the infrastructure, including the Kubernetes Ingress stack, [AWS networking](https://aws.amazon.com/?utm_content=inline+mention), Redis, Cassandra, HashiCorp Vault and Kubernetes itself.

“Investing in platform abstractions has already paid off,” Xia said. “Self-service interfaces have replaced the lion’s share of our former
white glove processes. A lot of our heavy internal workflows have been replaced by automation.”

In this presentation, Xia also offered some tips for when to automate a workflow. First step: everything must be programmable.

The platform has allowed the engineers to focus on those “impactful problems that we want to spend our time solving,” he said.

You can view the entire presentation here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)