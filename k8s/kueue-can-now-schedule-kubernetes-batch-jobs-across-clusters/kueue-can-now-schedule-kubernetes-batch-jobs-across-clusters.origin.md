# Kueue Can Now Schedule Kubernetes Batch Jobs Across Clusters
![Featued image for: Kueue Can Now Schedule Kubernetes Batch Jobs Across Clusters](https://cdn.thenewstack.io/media/2024/11/59ad16fe-kueue-1024x683.png)
A batch scheduler from the K8s [Kubernetes Batch Working Group](https://github.com/kubernetes/community/blob/master/wg-batch/README.md) now has the ability to schedule workloads on external clusters, promising to simplify operations management and potentially expand the range of available computational resources, certainly a much-desired feature for orgs with computationally-heavy AI workloads.

The new beta capability, called [MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/), was deftly demonstrated in a [KubeCon+CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) keynote last week by [Ricardo Rocha](https://ricardorocha.io/), platform engineering lab engineer at [CERN](https://home.cern/science/computing), no stranger to[ large computational workloads](https://thenewstack.io/how-cern-accelerates-with-kubernetes-helm-prometheus-and-coredns/).

Such software could go a long way in helping “manage a very complex infrastructure, with multiple clusters across multiple administrative domains,” he said.

## What Is Kueue?
An [open source project](https://github.com/kubernetes-sigs/kueue) under the Apache 2 license, [Kueue](https://kueue.sigs.k8s.io/) is a Kubernetes [resource quota manager](https://kueue.sigs.k8s.io/docs/overview/), providing a workload queue for Kubernetes clusters, which can be both elastic and heterogeneous.

It decides when pods [should be created](https://kueue.sigs.k8s.io/docs/concepts#admission) to start a job and when the job should stop and its pods deleted. It can also pre-empt jobs. The set of APIs provides the language to set quotas and policies for fair sharing among tenants.

From the [Kueue overview](https://kueue.sigs.k8s.io/docs/overview/) page.

Different types of computational resources, such as GPUs or spot instance-based virtual machines, are described as “ResourceFlavors” or objects that can then be used to fit the workload of the resources and are [also captured as objects](https://www.youtube.com/watch?v=HWTNCTaKZ_o).

Kueue can be installed atop any vanilla Kubernetes cluster. It builds on existing K8s technologies for autoscaling, pod-to-node scheduling and job lifecycle management.

## Kubernetes Scheduling with MultiKueue
On its own, Kubernetes will schedule multiple jobs in the queue in a random order. It will also schedule partial workloads, which can be problematic given the type of workload that needs to be executed.

Kueue executes all-or-nothing scheduling. Workloads are queued and are run in their entirety only when there are sufficient resources.

Other all-or-nothing scheduling tools include [Apache YuniKorn](https://yunikorn.apache.org/) and [Volcano](https://volcano.sh/en/).

But Kueue is also advantageous in that it supports multiple queues for different teams. Each research team can get its own dedicated portion of the cluster with its own namespace, and Kueue provides the ability to temporarily share each team’s portion if it is not being used.

Such queueing can be extremely valuable given the size of AI processing jobs and the relative scarcity of GPUs to run them, noted [Marcin Wielgus](https://github.com/mwielgus), software engineer at Google, also in the keynote presentation.

With MultiKueue, Kueue can manage clusters not only on-premises but also from external cloud providers and [other High-Performance Computing](https://link.springer.com/article/10.1007/s41781-020-00052-w) (HPC) centers.

A job can be submitted to a control cluster, which searches for a home in one of a number of available clusters, placing the job when sufficient capacity is found.

If a job requires GPUs, then that limit is designated in the workload description, so Kueue will know to place that job only on nodes with sufficient GPUs.

## Clusters Near and Far
Currently, MultiKueue is a beta feature turned on by default in v. 9 of Kueue.

One organization taking a serious look at incorporating MultiQueue has been CERN.

The European Nuclear Research Agency, CERN (which stands for “Conseil Européen pour la Recherche Nucléaire”) is currently designing its next particle accelerator. Currently, the research facility generates 100PBs of data a year, but with new particle accelerators incoming, this number could grow by a factor of 10 or more.

Rocha is part of an engineering team that is looking at building a system to [schedule jobs](https://arxiv.org/abs/2309.06782) against multiple resources, be they in-house, public cloud providers, or via CERN’s [Worldwide LHC Computing Grid](https://home.cern/science/computing/grid), a network of [HPC supercomputers](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/) around the globe.

Such a system would be built for batch jobs using parameter optimization and work with existing schedulers, such as [Slurm](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/) and [KubeFlow](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/), centralized through a Kueue entry point.

Rocha demonstrated how this project would work with MultiKueue. Within a dashboard, Rocha showed a number of active clusters, one in-house and one located in Germany.

All the jobs for these clusters are queued up and appear in the master cluster. One job Rocha tee’d up was too large for the local cluster, Kueue automatically started it on the remote cluster, which had the computational resources available.

“The idea is to submit jobs and not care where they run,” Rocha said.

Enjoy the entire keynote talk here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)