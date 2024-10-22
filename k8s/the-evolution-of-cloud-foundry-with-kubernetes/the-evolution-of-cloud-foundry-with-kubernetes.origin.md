# How Cloud Foundry Has Evolved With Kubernetes
![Featued image for: How Cloud Foundry Has Evolved With Kubernetes](https://cdn.thenewstack.io/media/2024/10/38422f4b-railroad-1024x576.jpg)
Cloud Foundry (CF) has evolved significantly, particularly in its relationship with Kubernetes (K8s). Cue proverb about change being the only constant.

Initially seen as separate entities, [CF and K8s gradually integrated](https://thenewstack.io/kubernetes-and-cloud-foundry-better-together/), with projects like KubeCF and [Eirini](https://thenewstack.io/with-project-eirini-cloud-foundry-adapts-to-a-new-open-source-ecosystem/) enabling CF to run natively on K8s. This evolution led to the development of [cf-for-k8s](https://thenewstack.io/cloud-foundry-aims-to-bring-the-ease-of-cf-push-to-kubernetes/), a cloud native CF distribution that embraces Kubernetes components and offers a streamlined developer experience.

While CF remains a powerful platform for managing large-scale, homogenous workloads, its integration with K8s has expanded its capabilities and solidified its position in the cloud native landscape.

## Cloud Foundry and Kubernetes: Over the Years
At the Cloud Foundry Summit Europe 2017, our members SAP, IBM and SUSE floated the idea of containerizing Cloud Foundry, leading to the creation of Eirini and [Quarks](https://thenewstack.io/cloud-foundry-containerized-project-quarks-and-project-eirini/). In the following year, discussions began regarding the compatibility and integration of Cloud Foundry and Kubernetes.

Initial attempts to run CF on K8s using a cloud provider interface (CPI) encountered difficulties due to the “split-brain orchestrator” issue. Projects like Fissile and SCF offered a more native approach to deploying CF on K8s by eliminating the BOSH runtime aspects.

The concept of nested containers was investigated, emphasizing that containers are peers rather than truly nested. A prototype named “Cube” was developed to enable the deployment of Cloud Foundry applications using other container schedulers, with the goal of combining CF and K8s.

## The Emergence of KubeCF
The tipping point for getting a Cloud Foundry substrate working over Kubernetes occurred in 2019. KubeCF emerged as a stable and reliable containerized Cloud Foundry implementation, directly using and repurposing BOSH release artifacts. [VMware](https://tanzu.vmware.com?utm_content=inline+mention) released an alpha version of Pivotal Application Service (PAS) powered by Kubernetes, showcasing the integration of Kubernetes as the underlying container orchestration for PAS.

The Cloud Foundry Foundation announced KubeCF as a new incubating project, signifying a significant milestone in the collaboration between the Cloud Foundry and Kubernetes communities. The Eirini project enabled the execution of Cloud Foundry applications as standard Kubernetes workloads, eliminating the necessity for a separate container scheduler.

## Are Two Technologies Better Than One?
Two parallel approaches for applying the Kubernetes abstraction were supported in 2020. On the one hand, the community kept working on KubeCF while investing time and resources in a more Kubernetes native approach that used cloud native resources. The community fully embraced Kubernetes with the release of cf-for-k8s 1.0, a Kubernetes native Cloud Foundry distribution. Cloud Foundry’s core components were updated to support kpack, Istio and a wider range of Kubernetes cluster versions.

KubeCF was maintained too, with version 2.5 being released, marking the end of efforts to make Kubernetes an alternative to the Diego container orchestration engine. In addition, the project Stratos 4.2, a web-based management console, was released with enhanced capabilities for managing Kubernetes and Helm chart repositories.

## Third Time’s a Charm
Currently, the Cloud Foundry community is working on the [Korifi project](https://thenewstack.io/cloud-foundry-launches-korifi-to-ease-kubernetes-development/) that envisions a Cloud Foundry on Kubernetes that offers the same developer experience as CF while integrating with Kubernetes technologies. We aim to maintain compatibility with existing CF environments but are also open to pragmatic solutions that might sacrifice some compatibility. We recognize the need for CF on K8s to adhere to Kubernetes practices and cloud native approaches. We have outlined guiding principles for integrating CF with Kubernetes technologies while retaining CF-specific concepts where necessary.

The community believes that Korifi should integrate with projects and technologies from Kubernetes and the cloud native ecosystem as replacements for CF subsystems. Especially in cases where these ecosystem projects demonstrate widespread adoption and operational maturity. Examples include kpack and [Cloud Native Buildpacks](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/) for app artifact generation and Istio for ingress routing and service mesh.

## Same Diff!
There are many technical underpinnings between Cloud Foundry and Kubernetes. Historically, they both share roots in the BORG project from Google. BOSH, one of the cornerstones of Cloud Foundry, was devised as the next generation of BORG and so the nomenclature BOSH (the letter S comes after R and H follows G ― ergo BORG -> BOSH).

The use of containers as the immutable artifact for deployment and orchestrating them for keeping up reliability and availability service-level objectives (SLOs), are the mainstay in both the tools. Both tools assume applications are designed with 12-factor principles and have special support for stateful applications to be deployed. The sidecar pattern is also something that the two technologies have in common.

## The Way Forward
The tech world is certainly big enough for the two technologies to co-exist. I don’t believe that choosing Cloud Foundry or Kubernetes is a zero-sum game. For those who want a converged experience when operating their virtual machines and container-based orchestration, Cloud Foundry will continue to exist as a robust and well-maintained option. For the tinkerers who enjoy working directly with Kubernetes, the ecosystem will offer full support.

There will be those who seek the best of both worlds, for whom an opinionated abstraction that minimizes the cognitive load of the CNCF landscape shall be the best option.

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, on Nov. 12-15.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)