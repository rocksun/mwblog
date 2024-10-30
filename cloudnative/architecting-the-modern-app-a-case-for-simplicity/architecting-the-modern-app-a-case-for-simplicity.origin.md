# Architecting the Modern App: A Case for Simplicity
![Featued image for: Architecting the Modern App: A Case for Simplicity](https://cdn.thenewstack.io/media/2024/10/118e9a55-architecting-modern-app-simplicity-1024x576.jpg)
*Complexity*. Avoiding it is one of the first things that draws many of us into [Kubernetes](https://thenewstack.io/kubernetes/) and the Cloud Native Computing Foundation (CNCF) ecosystem. After all, who doesn’t love trying out the latest tools and finding new and creative ways to overcome technical limitations? As techies, when a new challenge knocks, we answer the call.
That said, this is the 2024 CNCF project landscape:

There’s a lot going on here. For nearly every problem we run into when using [cloud native technologies](https://thenewstack.io/cloud-native/), a project — often more than one — is started to solve it. But is this ever-expanding landscape (and our love of the latest and greatest tech) leading us to overly complex solutions?

Perhaps. The swarm of solutions is attractive, and we can easily fall into the trap of wanting to integrate more cloud native products than is strictly necessary.

Let me tell you a story that is probably all too familiar.

## The Overly Complicated Customer Use Case
Our journey starts as a simple web app in a Kubernetes cluster with a [NoSQL](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/) database backend.

The database will need some storage for the stateful data, so we need to find a cloud native storage solution. And we’ll add a messaging queue to improve performance.

We should also add something to handle the app’s identity and access management (IAM), secrets and security. And the Dev team has just advised us they need a relational database.

With all these stateful apps running within the cluster, we’ll need to include a tool for backups and disaster recovery too.

We’ll also include [Argo](https://thenewstack.io/how-the-argo-project-is-avoiding-wordpress-type-problems/), so we can easily roll out all our Helm charts for the various pieces and deploy them anywhere we want.

You see where this is going. All these components are being added to the solution, and many are new tools and projects that are still in development. This means more ramp-up time now — and more technical debt tomorrow.

## But It Doesn’t End There
As the business continues to expand, new requirements come to light — like 15-minute service level agreements (SLAs) for recovery and regional failover. And because of certain application limitations, the application won’t support a hot/hot setup across data centers.

Kasten covers most of the components, but losing even five minutes of Kafka or Cassandra data can cause serious issues with the app. And other issues with IP address conflicts may arise when restoring to the other data center (because of some networking limitations in our data center).

So now we’re exploring even newer projects or tools completely outside CNCF that might be able to solve these new challenges. This causes significant delays due to testing out new tools, which takes even longer due to limited documentation and support. This adds even more points of failure, debugging unfamiliar systems, and risky dependencies. And all of this distracts us from the core business goals and causes delays in delivering the project.

## The Boring Alternatives
None of these problems are new to cloud native tools (well, some might be, but that’s a different article). We’ve faced many of these challenges countless times over the years when building applications, which also means that many of these challenges have been solved already. They might be boring solutions, but they are stable and well-known, thus causing less tech debt.

Or as [Dan McKinley](https://www.linkedin.com/in/mcfunley/), creator of the excellent [Choose Boring Technology](https://boringtechnology.club/) talk, puts it: “Software that’s been around longer tends to need less care and feeding than software that just came out.”

## Boring and Fun Can Work Together!
Rather than taking on all new challenges and rebuilding everything from the ground up, leverage the boring tools and explore the shiny new tech where it makes the most sense. If there is an easy, boring solution available, use it.

A good example of choosing a simpler solution is leveraging a Software as a Service (SaaS) solution for databases if you are planning on deploying in the cloud, or if you have a dedicated database team that already has automation and solutions ready to deploy.

Here’s how that plays out:

Moving state out of the cluster and onto more traditional hosts works well because it moves the automation from something like Argo to something like Jenkins and Ansible — which you are likely already using anyway.

Whether the infrastructure is in a data center or in the cloud, there is likely already a solution in place for backing up and restoring stateful data. And for redundancy and disaster recovery, most databases can easily be configured with replication across multiple data centers.

Doing this removes the need for a cloud native storage solution and a tool to back those up. We’ve also replaced a full-service mesh with something simpler like Envoy (a lightweight proxy we can deploy as sidecars to the application) to address our mTLS needs, as opposed to a full-service mesh like Istio that comes with more complexity, overhead and features than what’s actually needed.

Overall, this reduces technical debt, provides more stability and eases the transition for the support teams, since many of the solutions are either familiar or a centralized solution used organization-wide (such as a shared Vault).

We’re left with a cluster that is basically stateless. This allows us to easily deploy anywhere and fully leverage the benefits of a Kubernetes cluster, alongside some well-vetted technology stacks that developers and operators will be fully comfortable with.

## Simplicity Happens One Step at a Time
Much like general cloud adoption or any other tool we use, the important thing to remember is to use the right tool for the right problem at every decision point. Sometimes, it’s just easier and more reliable to use well-established, non-cloud native tools and leverage them alongside our cloud native solutions.

It might be fun to experiment with all these new toys, but there is always a team that has to support the solution after launch, and there’s nothing an Ops team likes more than a simple, reliable solution.

Ensure you consider the added cost (time, resources, cognitive load) of introducing a new technological choice to your stack. Include all impacted teams in any discussions to fully understand the outcomes of these choices, and consider what long-term support will look like.

More often than not, it’s just better to keep it simple — or as a much smarter person than me said:

“Perfection is achieved not when there is nothing more to add,but when there is nothing left to take away.”Antoine de Saint-Exupéry
—
Have you experienced the pitfalls of overly complex cloud native architectures? We’d love to hear your stories about simplifying Kubernetes deployments. Stop by Booth Q32 at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/) this Nov. 12-15 in Salt Lake City to chat with Aptum about the benefits of keeping it simple — and how we’re tackling complexity in our own projects!

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, on Nov. 12-15, 2024.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)