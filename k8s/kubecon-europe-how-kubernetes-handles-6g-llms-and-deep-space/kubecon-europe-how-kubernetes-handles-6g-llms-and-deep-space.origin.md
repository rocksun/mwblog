# KubeCon Europe: How Kubernetes Handles 6G, LLMs and Deep Space
![Featued image for: KubeCon Europe: How Kubernetes Handles 6G, LLMs and Deep Space](https://cdn.thenewstack.io/media/2025/04/1776f030-kubecon-google-bytedance-1024x768.jpg)
LONDON — The final keynotes of the last day of [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) underscored what [Kubernetes](https://www.thenewstack.io/Kubernetes) must support in the very near future.

Even among those who are still struggling with Kubernetes deployments and managing immense containerized infrastructures — often extended across different geographical environments — the future brings a new set of challenges. Solutions for many of these challenges are now being developed.

Community support continues to remain essential in open source development to support the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)’s largest project.

As shown during Friday’s keynote discussions, the immense [reach of Kubernetes infrastructure](https://thenewstack.io/day-2-kubecon-europe-keynotes-users-share-kubernetes-war-stories/) is expanding to support cutting-edge use cases. This includes Telco deployments for current 5G and emerging 6G infrastructure, as well as reducing latency in the tokenization and implementation of [large language models](https://thenewstack.io/kubecon-europe-day-1-keynote-can-observability-keep-up-with-llms/) (LLMs) within Kubernetes environments.

In the case of astrophysicists studying outer space, the infrastructure used to analyze data must theoretically be capable of handling a near-infinite number of calculations.

## Load Balancing on K8s
Load balancing needs improvements as always, but LLMs on Kubernetes offers even more potential latency issues for data transfer.

During “LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency,” Google distinguished engineer [Clayton Coleman](https://www.linkedin.com/in/claytoncoleman/) and Bytedance engineer [Jiaxin Shan](https://www.linkedin.com/in/jiaxin-shan/) discussed the [Kubernetes Gateway API Inference Extension](https://thenewstack.io/kubecon-europe-kgateway-aims-to-be-the-kubernetes-onramp/). It converts Kubernetes gateways into inference gateways, benefiting large and small platform teams, Coleman said.

KubeCon Europe 2025 London Day 3 Keynote: LLMs require load balancing to do more than double duty.

[@ByteDanceOSS]‘ Jiaxin Shan and
‘s Clayton Coleman: “LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency.”[@CloudNativeFdn][@thenewstack][pic.twitter.com/OePrvRzltC]— BC Gain (@bcamerongain)

[April 4, 2025]
The extension, informed by experiments at Google and Bytedance, addresses the shift from proprietary to open models, emphasizing the trade-off between large, cutting-edge models and smaller, efficient ones. Key challenges include unpredictable GPU load, resource-intensive models and hardware heterogeneity, Coleman said.

“Running large models is becoming a fundamental part of application infrastructure, and in the coming years, it will be a standard practice. To prepare for this, we must identify the APIs and components that can be standardized and reused,” Coleman said. “We also need a common framework that bridges the latest research and production environments, ensuring a smooth transition from innovation to deployment. If there is a standard, dynamic and extensible load balancer, it must continue to evolve to meet these needs.”

KubeCon Europe 2025 London Day 3 Keynote: “Cloud Native Evolution in Telecom: 5G, 6G and Beyond!”

[@Swisscom]‘s Joel Studler on[@kubernetesio]infrastructure, w/Faseela K, Ericsson Software Technology; Tom Kivlin, Vodafone; Philippe Ensarguet, Orange.[@thenewstack][#KubeCon2025][pic.twitter.com/222HSOXzOw]— BC Gain (@bcamerongain)

[April 4, 2025]
## Kubernetes for 5G, 6G
During “Cloud Native Evolution in Telecom: 5G, 6G and Beyond!” a panel with Ericsson’s Faseela K, Vodafone’s Tom Kivlin, Orange’s Philippe Ensarguet and Swisscom’s Joel Studler discussed the critical role open source cloud native plays in 5G networks and will play in the future.

Swisscom relies on tools like [Flux for GitOps](https://thenewstack.io/tutorial-a-gitops-deployment-with-flux-on-digitalocean-kubernetes/) and Kubernetes for automation, reducing deployment times from weeks to minutes, Studler said. CNCF proxies are essential in “our network transformation journey,” Studler said.

In telecommunications, we are still accustomed to thinking in terms of physical and black-box solutions,” Studler said. “There is a persistent belief that we need to virtualize traditional systems, which is contrary to the open and simplified approach of [cloud native technologies](https://thenewstack.io/cloud-native/).”

Swisscom’s cloud native tooling includes:

- Flux for CNS deployments.
- NetConf for system management.
- Cert-Manager with its PKI.
- ExternalDNS for automation of DNS management using ExternalDNS.
“By orchestrating everything through the [Kubernetes Resource Model](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md) (KRM), we achieve significant productivity gains — reducing process times from weeks and days down to hours and minutes,” Studler said.

KubeCon Europe 2025 London Day 3 Keynote: LLMs require load balancing to do more than double duty.

[@ByteDanceOSS]‘ Jiaxin Shan and[@CloudNativeFdn][@thenewstack][pic.twitter.com/OePrvRzltC]— BC Gain (@bcamerongain)

[April 4, 2025]
## In the Skies
Under the umbrella of the Square Kilometre Array (SKA) project, Carolina Lindqvist, a system specialist at Swiss Federal Technology Institute of Lausanne (EPFL), described how the Swiss SKA Regional Center (CHSRC) unit within the global SKA Regional Center Network (SRCNet) relies on Kubernetes as a service management plane on which to support extreme data- and compute-intensive astronomy use cases, Lindqvist said.

SKA will receive up to 600PB of data annually, necessitating global storage and distribution, Lindqvist said. The project includes 12 collaborating teams and various partner states. The data will be used for research on topics like the cosmic domain and solar physics. The Swiss site uses a cloud native infrastructure, including a supercomputer, to process and distribute the data, Lindqvist said.

During a demo, Lindqvist presented an astronomy workflow. It involved taking an image from space taken with a telescope, and then processing it for analysis.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)