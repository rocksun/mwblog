If you wanted to effortlessly move your AI inferencing and modeling workloads across the clouds, what would you need from Kubernetes?

The [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) wants to know.

CNCF is [creating](https://www.cncf.io/blog/2025/08/01/help-us-build-the-kubernetes-conformance-for-ai/) a program for certifying Kubernetes distributions that can run select types of AI workloads. But it needs a set of requirements and recommendations first. And they are looking for your help.

The idea is to replicate what CNCF has done with the [conformance guide for Kubernetes](https://www.cncf.io/training/certification/software-conformance/). Thus far, well over 100 K8s distributions [have made that list](https://www.cncf.io/training/certification/software-conformance/#logos).

A workload running on a Kubernetes-conformant distribution, whether it is on a public or private cloud, can be moved into another conformant environment with no changes.

“We want to do the same thing for AI workloads,” said CNCF CTO [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/) during [KubeCon + CloudNativeCon China](https://www.youtube.com/watch?v=etvB-QGFtns&list=PLj6h78yzYM2P1xtALqTcCmRAa6142uERl&t=308s) in June. This will require a set of capabilities, APIs and configurations that a Kubernetes cluster *must* offer (on top of the regular conformance).

The idea is to provide a “baseline compatibility” across different environments, the globe-trotting Aniszczyk further explained at [KubeCon + CloudNativeCon Japan](https://www.youtube.com/watch?v=mh7Cmei3pmI&list=PLj6h78yzYM2PsNdcBGWR_mVN-SRLQl6KM&t=405s).

When the “CNCF started, the whole idea was to build infrastructure that would run on every cloud,” be it public or private, he said.

The question of how to define AI requirements is being held in [SIG-Architecture](https://github.com/kubernetes/community/tree/master/sig-architecture), within a newly formed working group for the task.

The goal of this group is “to define a standardized set of capabilities, APIs, and configurations that a Kubernetes cluster must offer to reliably and efficiently run AI/ML [machine learning] workloads,” the working group’s [GitHub page explains](https://github.com/kubernetes/community/tree/master/wg-ai-conformance).

This work will also set the stage for a broader “Cloud Native AI Conformance” definition, including the other aspects of cloud native computing, such as telemetry, storage and security.

[Google](https://cloud.google.com/?utm_content=inline+mention), [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) and other commercial firms are lending resources to the project.

[![screenshot](https://cdn.thenewstack.io/media/2025/08/6701237c-kubeconform-01.jpg)](https://cdn.thenewstack.io/media/2025/08/6701237c-kubeconform-01.jpg)

## Commoditize Kubernetes

In [early virtual discussions](https://docs.google.com/document/d/1hXoSdh9FEs13Yde8DivCYjjXyxa7j4J8erjZPEGWuzc/edit?tab=t.0#heading=h.9j85ih1tpsk), the overall goal is to make AI/ML workload platforms as commoditized as possible. “The hope is to minimize the amount of DIY and framework-specific patches needed to run AI/ML workloads,” a working group contributor wrote.

The group identified three types of workloads well-suited for Kubernetes:

* **Large-scale training and fine-tuning:** Key platform requirements include access to high-performance accelerators, high-throughput and topology-aware networking, gang scheduling and scalable access to data.
* **High-performance inference:** Key platform requirements include access to accelerators, advanced traffic management and standardized metrics for monitoring latency and throughput.
* **MLOps pipelines:** Key platform requirements include a robust batch job system, a queuing system for managing resource contention, secure access to other services like object storage and model registries, and reliable CRD/operator support.

The draft document also lists a set of recommended practices (“should”) and flat-out requirements (“must”), many of which are based on recent [Kubernetes enhancements](https://thenewstack.io/kubernetes-v1-33-advances-in-ai-security-and-the-enterprise/) for the AI crowd.

For instance, a Kubernetes AI-compliant system must support [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) (DRA), which will be fully available in the upcoming Kubernetes 1.34 release later this month. DRA provides more flexible and fine-grained resource controls, such as the ability to [specify GPUs](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/).

It also must support the [Kubernetes Gateway API Inference extension](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/), which [specifies traffic routing patterns](https://thenewstack.io/google-kubernetes-engine-customized-for-faster-ai-work/) for LLMs.

The Cluster autoscaler must be able to scale node groups up/down with specific accelerator types requested.

And so on…

## The Certification Program

A separate, as-yet-unnamed group will be in charge of accreditation.

The certification program will have a public website, listing all the Kubernetes distributions that passed the conformance tests. They will be tested annually. Each distribution will have a completed [YAML-based](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) conformance checklist.

CNCF plans to unveil the finished conformance guide at this year’s [KubeCon+CloudNativeCon North America 2025 in Atlanta](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event), Nov. 10-13.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)