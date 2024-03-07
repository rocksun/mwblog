# KubeCon 24: Crossplane, a Developer-Friendly Control Plane
![Featued image for: KubeCon 24: Crossplane, a Developer-Friendly Control Plane](https://cdn.thenewstack.io/media/2024/03/8cbb2856-kubecon24-eu-1024x703.jpg)
For those heading to
[KubeCon+CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) later this month in Paris (March 19-22), be sure to stop by the [Crossplane booth](https://thenewstack.io/crossplane-a-package-based-approach-to-platform-building/) (Kiosk PP1-B in the afternoons of March 20-22), to learn about the latest release of the cloud native control plane, [Crossplane 15](https://github.com/crossplane/crossplane/releases/tag/v1.15.0).
Visitors unable to make the kiosk can also stop by the
[Upbound](https://www.upbound.io/) booth, during the entire show floor hours at G14 and at the [Platform Engineering Day](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/co-located-events/platform-engineering-day/) on March 19 at table four. Upbound is the company managing the Crossplane codebase, which is an open source project of the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention).
There will also be a
[number talks about Crossplane](https://kccnceu2024.sched.com/?searchstring=crossplane&iframe=no) at KubeCon as well as at [co-located events](https://colocatedeventseu2024.sched.com/?searchstring=crossplane&iframe=no).
Based on Kubernetes,
[Crossplane](https://github.com/crossplane/crossplane) is a framework designed for building [cloud native control planes](https://thenewstack.io/cloud-native/), though it is not limited to Kubernetes-based resources. It is also extensible, allowing platform engineers to orchestrate new types of infrastructure and applications. A [marketplace](https://marketplace.upbound.io/) provides ready-to-use configurations, such as those for [AWS](https://aws.amazon.com/?utm_content=inline-mention), [Azure](https://news.microsoft.com/?utm_content=inline-mention) and the [Google Cloud Platform](https://cloud.withgoogle.com?utm_content=inline-mention).
## Crossplane for Platform Engineering
No one industry in particular makes up early adopters of Crossplane. Rather the users have been spread pretty evenly across the verticals. One thing they have in common is that they use cloud native resources enough that they need a dedicated control plane to manage it all, said
[Jared Watts](https://www.linkedin.com/in/jared-watts-jbw976/), founding engineer at Upbound and Crossplane maintainer, in an interview with TNS.
Crossplane can be used to “define a consistent platform that gets all the policies, configurations and all the things that your organization needs to be in compliance,” Watts said. “And then offers a nice abstraction to the developers to get them the infrastructure that they need.”
This control plane fits in handily with the emerging popularity of
[platform engineering](https://thenewstack.io/year-in-review-platform-engineering-still-run-by-spreadsheet/). “Crossplane is a huge part of platform engineering for being able to define a consistent platform that is always managing everything you need for your developers in a consistent way,” Watts said.
One advantage that Crossplane offers is its ability to work with non-Kubernetes resources, a growing concern for many shops that may not be willing to move all their resources over to a cloud native infrastructure.
“Crossplane is an extension to Kubernetes. It teaches Kubernetes all about external resources, such as cloud resources and new infrastructure that lives outside of Kubernetes,” Watts said.
## Crossplane for Developers
Releases of Crossplane come quarterly and the latest 1.15, among other things, promises a better experience for developers. Watts said.
The command line interface has been updated, with three new beta command line subcommands:
*to validate composition against a schema using Kubernetes API server’s validation library.* **crossplane beta validate** *initiates a new project in an easier manner.* **crossplane beta init** *provides quick resource utilization checks of Crossplane pods.* **crossplane beta top**
There are also modifications to a number of existing CLIs, all of which were modified with the idea of making it easier for developers to provision cloud infrastructure.
Also, the new release better supports composition functions. First released in version 1.11,
[composition functions](https://docs.crossplane.io/latest/concepts/composition-functions/) have caught the imagination of the Crossplane community. Crossplane functions are custom functions for creating template resources.
To help make composition functions easier to write, Upbound has released a
[Python software development kit](https://docs.crossplane.io/knowledge-base/guides/write-a-composition-function-in-python/) (SDK) to help generate these functions more easily (They also can be written with the [Go programming language](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/)). Composition functions can now request additional cluster-scoped resources that Crossplane has access to, such as a virtual private cloud (VPC).
Functions now have observability support for
[Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/): Crossplane now emits basic function metrics for number of requests sent, number of responses received and histogram of function run duration.
## Crossplane: A CNCF Project About to Graduate
The project may also have good news on the CNCF front. The project, which has been in incubation status since 2021, has applied for graduation status.
“We’re making a statement that the project is matured, it’s grown, it’s scaled, it’s adopted by folks,” Watts said. “It’s got people contributing to it, it’s got a community. It’s mature, and it’s ready to graduate.”
So maybe at KubeCon, we will see Crossplane graduate as a full-fledged CNCF-matured project.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)