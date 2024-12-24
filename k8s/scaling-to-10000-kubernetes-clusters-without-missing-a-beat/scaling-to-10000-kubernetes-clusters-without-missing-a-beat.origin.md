# Scaling to 10,000 Kubernetes Clusters Without Missing a Beat
![Featued image for: Scaling to 10,000 Kubernetes Clusters Without Missing a Beat](https://cdn.thenewstack.io/media/2024/10/8fb30933-datacenter2-1024x576.jpg)
When we talk about scaling in Kubernetes, we naturally think about scaling up or down within a cluster, either manually or using one of the many types of autoscalers (and we [have a blog post on that](https://www.spectrocloud.com/blog/kubernetes-autoscaling-patterns-hpa-vpa-and-keda), by the way).

But there’s another kind of scaling that’s increasingly common: scaling the number of clusters you have in your estate.

Our annual research found that the typical business using [Kubernetes](https://thenewstack.io/kubernetes/) now has more than 20 clusters; 6% of companies have more than 100 clusters.

And the limit is certainly not in the hundreds. Famously, Mercedes-Benz was running close to 1,000 Kubernetes clusters in 2023, according to [this CNCF case study](https://www.cncf.io/case-studies/mercedes-benz/).

[Edge use cases](https://thenewstack.io/the-challenge-of-scaling-the-intelligent-edge/) take the number even higher: One of our customers, Dentsply Sirona, uses Kubernetes in [thousands of dental offices](https://kccnceu2024.sched.com/event/1YeS4).
There are [many reasons why you’d choose to run lots of clusters ](https://www.spectrocloud.com/blog/why-you-need-kubernetes-multi-cluster-management)— not just separating dev/test from production, but supporting multicloud Kubernetes strategies, multiregion deployments, and application isolation (blast radius) plus security and compliance needs.

## Lots of Clusters … a New Bottleneck?
If you’re running dozens, hundreds or thousands of Kubernetes clusters, you’ve probably adopted a [Kubernetes management platform](https://www.spectrocloud.com/blog/what-is-an-enterprise-kubernetes-management-platform) to centralize and automate how you deploy and operate your clusters.

And this is where things get really interesting, because most Kubernetes management platforms are simply not architected to scale effectively.

Once you get beyond, say, 40 or 50 clusters, the management platform itself becomes a bottleneck. Under the load of API calls and new instructions every second, its performance degrades.

You end up with errors, timeouts and web interfaces and APIs becoming unresponsive. The platform itself may suffer downtime, leaving you scrambling to scale its resources or recover it — and in the meantime, you’re unable to build new clusters or make changes to existing ones.

How do we know this? Because our customers have shown us and told us, many times, that when they get past the initial proof of concept with a vendor, things quickly fall apart. In some cases, we’ve tested these platforms ourselves and seen them struggle under load.

## What Do the Vendors Say?
The guidance from the vendors of these platforms (if they admit the limitation at all) is usually to run multiple instances of the management platform, for example one per region, per environment or per group of clusters.

Kubermatic, for example, [advises](https://docs.kubermatic.com/kubermatic/v2.26/architecture/) that *“*instead of running the KKP master and seed components in a single cluster, it is advisable for large-scale deployments to have multiple, dedicated seed clusters.”

In a [lengthy guide](https://ranchermanager.docs.rancher.com/reference-guides/best-practices/rancher-server/tuning-and-best-practices-for-rancher-at-scale) to scaling, Rancher calls out the computation bottleneck of its “upstream cluster”: *“*When scaling up Rancher, one typical bottleneck is resource growth in the upstream (local) Kubernetes cluster. The upstream cluster contains information for all downstream clusters. Many operations that apply to downstream clusters create new objects in the upstream cluster and require computation from handlers running in the upstream cluster.*”*

We think that this kind of architectural workaround defeats the whole point of a centralized management platform. When you have multiple management servers, you no longer have a single pane of glass experience, not to mention the complexity you’re introducing. And when you get to edge scale, it’s simply infeasible.

## 10,000 Clusters. Can We Measure Up?
Recently a customer came to us with a challenge: Their current management platform vendor (not one of the two we’ve just named, incidentally) was struggling to scale to just a few hundred clusters.

This was a problem, because the customer wanted to deploy edge Kubernetes to 10,000 retail locations.

Having been burned before, they asked us: Can Palette really scale as we need it to?

## The First Ingredient: The Right Architecture
Palette was architected specifically for this kind of hyper-scale scenario. We have a [decentralized architecture](https://www.spectrocloud.com/product/decentralized-architecture), which puts the computational burden on a smart agent running in each local cluster, rather than relying on the single management plane to perform the work.

The main multitenant SaaS deployment of the Palette management plane already happily runs more than 1,400 clusters (many of our customers have their own dedicated instances or self-host the Palette software, so naturally they don’t count toward the total stress-test on the main instance).

But that’s still a long way off the 10,000 target. How can we prove that Palette can scale to that extent?

## Introducing Spectro Cloud’s Performance Practice
Performance and scalability are so important to us that we have invested heavily in establishing a performance practice: a set of processes that enable us to analyze our system behavior under load, so we can push the limits of what Palette can do, continuously optimize, and then validate positive impacts.

This way, customers can scale with confidence, knowing that our max numbers are more than just wishful thinking or marketing hyperbole.

We also use performance testing to drive product efficiency and validate the reliability and stability of the system under varying load conditions. By simulating real-world scenarios and stress-testing the system at scale, we can identify and address potential bottlenecks, ensuring that the platform remains stable and responsive even during peak usage periods.

## Meeting the 10k Challenge
To meet this customer’s 10k cluster challenge, we fired up a new performance testing simulation.

We stood up a dedicated SaaS instance of Palette, identical to what our customers use. This is important: We didn’t tune the management plane for performance, and Palette wasn’t aware that it was being tested. We didn’t rig the experiment.

Next, we needed 10,000 three-node clusters, and at least 30,000 machines to make up our edge Kubernetes hosts and run the local Palette agents.

Unfortunately, our CFO wouldn’t sign off on purchasing a warehouse full of new servers, so we created a synthetic environment. Enter two frameworks that we created for just this purpose.

**An in-house developed performance testing framework,**an API service with endpoints to create tenants, projects, edge hosts and clusters on the environment configured. It precisely mimics the complete cluster life cycle and makes all the API calls that real agents would make to Palette, sending data about events, machine health, heartbeats and pack status.**A load-generation and metrics capture framework**based on[K6](https://k6.io/)with additional custom development and extensions. This generates the load, capture metrics and test data required for the test load specification. We can specify the number of concurrent virtual users and many other options, and see the effect on Palette’s physical resources and performance.
Everything is configurable in the frameworks, allowing us to test and validate many scenarios, and overall the simulated agents behaved exactly like the real [Palette edge and cluster agents](https://thenewstack.io/virtual-kubernetes-clusters-with-spectro-cloud-palette/) installed in production clusters.

![This is what 1,000 edge nodes looks like if you go crazy in PowerPoint.](https://cdn.thenewstack.io/media/2024/10/47e0ecf1-image4-1024x599.png)
This is what 1,000 edge nodes look like if you go crazy in PowerPoint.

Using this setup, we ramped up until we were simulating 10,000 clusters and 36,000 edge nodes, all managed by a single Palette instance and accessible from a single user interface.

Our testing suite monitored the stability of Palette’s components, responsiveness of the API (which also powers our UI) and performance of the UI experience when performing standard operations. We also had our engineering and QA teams performing human validation at every step of the testing process.

## Passed With Flying Colors
The result was very clear. The UI and API remained responsive. We encountered no performance degradation, no instability, no downtime, no strange errors, no bottlenecking.

In fact, we saw no signs that we were even approaching Palette’s scaling limits at 10,000 clusters. We only stopped there because that was the target our customer had set for us.

And as you’ll see from the screenshot below, to reach this scale we didn’t have to throw a lot of hardware at the problem. Our Mongo database server was a 16-core CPU with 64 GB of memory

Watch the video below for a quick real-time, unedited tour of the Palette interface where you can see us navigating the clusters, filtering, drilling down, switching projects and performing other normal operations with full responsiveness.

## How Many Clusters Will You Be Running Next Year?
If your Kubernetes environment is ever likely to scale into the hundreds or thousands of clusters, you will certainly be using a multicluster management platform — and you need to be asking questions now about whether that platform can scale with you.

Palette was architected for ludicrous scale from Day 1, and we have built up a robust performance practice, enabling us to quickly test any scenario and optimize our platform continuously.

So when we came back to our customer and demonstrated, live, Palette running 10k three-node clusters, without breaking a sweat, their jaws were on the floor.

So if scale is on your mind, come put us to the test. [Request a demo](https://www.spectrocloud.com/get-started), tell us how many clusters you’ve got and we will demo Palette supporting your estate.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)