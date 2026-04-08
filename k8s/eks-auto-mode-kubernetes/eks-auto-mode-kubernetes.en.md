For this edition of *The New Stack Makers*, we sit down with Alex Kestner, principal product manager at Amazon Elastic Kubernetes Service, Amazon Web Services. Kestner explains how Amazon EKS Auto Mode fits into AWS’s hyperscaler stack and his role in engaging with the Cloud Native Computing Foundation (CNCF). This discussion took place during [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 2026, in Amsterdam.

VIDEO

## Inherent power, inherent complexity

Getting the inconvenient truth out of the way right up front, Kestner agrees that the challenge with Kubernetes is that, because it is so powerful, there’s a certain amount of complexity that comes with any toolset of its muscle. The more welcome news is that, with Amazon EKS, there is a “healthy portion of undifferentiated heavy lifting” that AWS can take on for customers.

But why do complexities arise? Is it down to scaling challenges, service interconnects, or perhaps some spurious set of connections to legacy systems?

> Most of the difficulties come from the day-to-day tasks that take platform teams’ time away from delivering true value for their business.

“To be honest, most of the difficulties come from the day-to-day tasks that take [platform teams](https://thenewstack.io/caught-in-the-middle-the-new-role-of-platform-teams/)‘ time away from delivering true value for their business,” Kestner explains. “These are the things that impede developers when they are trying to create unique and differentiated value in applications that ship faster and serve users better.

“You can think of repeated and ongoing operational tasks, such as handling the lifecycle of the nodes in a cluster, making sure that they’re secure, up to date, and that the right instance types are selected for performance and cost. It’s the tasks needed to make sure all of the software in a cluster that helps it operate is consistent and up to date. It’s so that we get the right fit for the workloads in that [cluster](https://thenewstack.io/part-2-access-aws-services-through-a-kubernetes-dual-stack-cluster/).”

## A foil for infrastructure toil

To address this list of software engineering responsibilities, Amazon EKS Auto Mode has been built to “address infrastructure toil” in live production environments. First introduced at [AWS re: Invent 2024](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-eks-auto-mode/), the technology addresses commonalities in node execution and behavior, spanning the entire node lifecycle from spinning up to [retiring a node after use](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/).

“Fundamentally, Auto Mode is meant to take on a lot of the undifferentiated, heavy lifting that we’re seeing platform teams do just to get the benefits of this incredible ecosystem that we see here with Kubernetes and the CNCF as a whole,” said Kestner.

Detailing more of the mechanics of AWK EKS Auto Mode, we can see that for a Kubernetes cluster to be truly useful in a production environment, there are key elements of operational software that need to run on that cluster that help it interact with all kinds of other [infrastructure primitives](https://thenewstack.io/matt-biilmann-and-netlifys-quest-to-simplify-the-frontend/), or in the case of AWS EKS, other AWS services. AWS takes over the responsibility for those elements and runs them outside the cluster; in doing so, the company alleviates some of the maintenance burden normally shouldered by cloud-native developers.

Also of note here is work carried out with the AWS EC2 team. The result is [Amazon EC2 Managed Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html), which the company positions as a simplified way to run compute workloads on Amazon EC2 with delegated operational control of the instance to a cloud service provider. Every time Amazon EKS Auto Mode launches into a Kubernetes cluster, it uses an EC2 Managed Instance.

## An end to unpredictable workloads?

Assiduous work from AWS then, but will the kinds of operational offloads on offer here signal an end to unpredictable workloads in Kubernetes? Will compliance, security, virtualization management, and overall cloud wastage go down now? Not necessarily clarified Kestner, but that’s primarily down to the varied topography of modern cloud-native deployments.

“While we can’t necessarily influence the diversity of customer use cases, Amazon EKS Auto Mode is there to provide a very application-oriented perspective to scaling and cost optimization… and that’s always going to help with capacity planning,” Kestner says. “Auto Mode is built on a series of open source standards and products, one of which is the [Karpenter project](https://karpenter.sh/), which works to right-size compute resources based on specific workload requirements.

“So this means that customers can have their workload specify the kinds of infrastructure they need and define their compute requirements, all essentially behind the scenes. Auto Mode will then go and look for the optimal and most cost-effective infrastructure to meet those requirements.”

What we have here with Amazon EKS Auto Mode is not quite an end to capacity planning headaches, but it is a step in the right direction. With vendor discussions at this year’s KubeCon + CloudNativeCon Europe so directly focused on companies claiming they have a cloud-native infrastructure approach suited to the age of AI, foundational operations support technologies for platform teams will remain paramount for some time to come.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)