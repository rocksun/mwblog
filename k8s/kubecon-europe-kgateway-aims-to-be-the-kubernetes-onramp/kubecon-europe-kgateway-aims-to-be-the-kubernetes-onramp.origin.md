# KubeCon Europe: Kgateway Aims To Be the Kubernetes Onramp
![Featued image for: KubeCon Europe: Kgateway Aims To Be the Kubernetes Onramp](https://cdn.thenewstack.io/media/2025/04/de9b2a5c-soloio-kubecon-1024x683.jpg)
Kubernetes network administrators at [KubeCon + CloudNativeCon EU](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/) this week in London should drop by the [Solo.io booth #S150](https://x.com/soloio_inc/status/1907379381896372553) to learn about an open source Kubernetes API Gateway implementation, called kgateway, that could [ease the management](https://www.solo.io/blog/donating-gloo-gateway-to-the-cncf-introducing-kgateway-and-advancing-cloud-connectivity) of moving traffic to and from clusters.

Built on top of [Envoy proxy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy) and the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/), the open source [kgateway](https://kgateway.dev/) is a Kubernetes-native ingress controller and next-generation API gateway.

The gateway was built by cloud native connectivity company [Solo.io](https://www.solo.io/company/about-us), and went under the name [Gloo Gateway](https://thenewstack.io/with-gloo-enterprise-1-0-solo-io-builds-the-stepping-stones-to-service-mesh/).

At last year’s KubeCon +_ CloudNativeCon North America 2024, the company announced that it would be donating the software to the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF), changing the software’s name to kgateway in the process.

In March, CNCF[ accepted](https://www.cncf.io/reports/etcd-project-journey-report/) kgateway as a sandbox project, the entry point for early stage cloud native software projects.

By moving to a vendor neutral governance, users, and contributors do not have to worry about the software being donated by a single vendor.

The [Gloo open source repository](https://github.com/solo-io/gloo) will be deprecated over time.

## The Importance of the Kubernetes Gateway API
In 2023, the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) achieved [version 1.0 production release](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/). The API Gateway is a specification of how to control the traffic in and out of Kubernetes clusters, as well as how to shuttle traffic internally between pods.

Kgateway is a fully conformant implementation of the Kubernetes Gateway API. The API is a specification for how to route traffic, both on the “layer 4” control plane and the “layer 7” data plane.

It is actually an interface to the [Envoy proxy](https://thenewstack.io/the-envoy-proxy-finds-a-home-at-the-cncf-amazon-web-services/), which manages L7 data traffic for a Kubernetes cluster. Programming Envoy directly, however, is difficult. What kgateway does is provide a more intuitive interface to program network traffic for end users, which could include infrastructure providers, cluster operators, and application developers.

Kgateway reads the Gateway API rules set by the administrators and then executes them using Envoy.

“Kgateway supports the Kubernetes Gateway API so that user can use this intuitive user interface that’s composed of the Gateway HTTP route,” said [Lin Sun](https://www.linkedin.com/in/lin-sun-a9b7a81/), Solo.io’s director of open source, in an interview with TNS.

## An AI Roadmap for Kubernetes
According to Sun, the goal for kgateway is to be the default gateway for all-direction Kubernetes traffic (both north-south and east-west internal traffic).

The project is working on expanding the capabilities of the software as well.

For instance, kgateway is positioning itself as an “AI Gateway” to address the unique security and management challenges of integrating applications with LLMs.

Project developers are on the [Kubernetes Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network), which is working on a new project, the “[Gateway API Inference extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension).”

This extension will give Kubernetes inference-specific routing capabilities, allowing K8s deployments to work more easily with [generative AI-driven](https://thenewstack.io/how-generative-ai-is-reshaping-the-sdlc/) workloads through routing, secret management, backup LLMs and other capabilities.

Kgateway is also being tightly integrated with the[ Istio Ambient mesh](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/), which seeks to do away with sidecars entirely. For Istio in Ambient Mode, kgateway can function as a [waypoint proxy](https://youtu.be/B8oZ1seIDIM?list=TLGGDmuUB1z53FMwMjA0MjAyNQ), providing advanced L7 features not available in Istio itself, such as request transformation, retries, traffic control for AI workloads.

Sun explains further here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)