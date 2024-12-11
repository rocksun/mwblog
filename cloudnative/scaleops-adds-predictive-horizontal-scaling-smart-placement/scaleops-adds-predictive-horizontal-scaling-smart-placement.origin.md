# ScaleOps Adds Predictive Horizontal Scaling, Smart Placement
![Featued image for: ScaleOps Adds Predictive Horizontal Scaling, Smart Placement](https://cdn.thenewstack.io/media/2024/12/a4fa2d88-toggles-1024x576.jpg)
The Israeli startup [ScaleOps](https://scaleops.com/) has added horizontal scaling and other features to its offering to [dynamically allocate container resources at runtime](https://thenewstack.io/scaleops-dynamically-right-sizes-containers-at-runtime/).

Its predictive horizontal pod autoscaling uses AI to forecast application loads to scale in real time.

“One of the problems today is that once you need to scale horizontally for an application, and you need more replicas, to handle the load, the problem is that it takes a very long time for the application to horizontally scale. … We predict that and scale ahead of time, and then when the load already kicks in, you already have the amount of replicas that you need up and running, and they can handle the changing demand,” said Yodar Shafrir, ScaleOps co-founder and CEO, in an interview.

By providing a context-aware platform with a holistic view of the [cluster and each application’s needs](https://thenewstack.io/why-kubernetes-cluster-management-needs-to-be-easier-for-developers/), it can remove the friction between developers and DevOps teams about real-time resource allocation, according to the company.

“We realized that no one in the market was solving the problem; they were just providing visibility and bringing awareness to it. The process of resource allocation was still completely broken,” Shafrir said in an announcement.

Using AI and machine learning, the system can ascertain from a previous week or month the [container](https://thenewstack.io/containers/)’s normal behavior and predict when traffic spikes will occur and scale accordingly.

It integrates with other autoscalers such as open source [Karpenter,](https://thenewstack.io/how-aws-supports-open-source-work-in-the-kubernetes-universe/) Cluster Autoscaler, HorizontalPodAutoscaler (HPA) or [Keda](https://thenewstack.io/kubernetes-autoscaling-keda-moves-into-cncf-incubation/) to determine the optimal number of replicas for every workload.

It also announced intelligent pod placement, which optimizes resource allocation by considering application constraints and cluster status, reducing the number of active nodes required.

“Some of the pods today that run within the cluster have a limitation [that] might prevent the node from scaling down. Usually, it would be for workloads that cannot be preempted and cannot tolerate a node scaledown,” Shafrir explained.

“So what do companies do? They add annotations that tell the Kubernetes cluster to never scale down the node [that] the pod is currently running on. We are aware of the need of every application and all the limitations, and we also have the holistic view of the whole cluster, so we make sure that all the pods that have this limitation will be scheduled on the same nodes. This way, those nodes will remain static and will not be able to scale down, but then the rest of the cluster will be much more dynamic, and then you can have nodes scale down when it’s necessary.”

The company maintains that real-time predictive scaling and intelligent pod placement together can save organizations 50% in cloud costs and improve application performance.

A third new feature is a set of dashboards for engineering teams to help them quickly analyze and understand the root cause of the issue, and then manage the workloads accordingly.

ScaleOps works in any Kubernetes environment, including the major cloud platforms like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud, as well as on-premises and air-gapped servers.

Founded in 2022, Tel Aviv-based ScaleOps recently announced $58 million in Series B funding, bringing the company’s total funding to $80 million.

“Today, we’re mostly focused on the production and staging use cases, and we are going to expand to traditional resources, to network, to storage, to GPUs, in addition to the compute and memory where we were working today,” Shafrir said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)