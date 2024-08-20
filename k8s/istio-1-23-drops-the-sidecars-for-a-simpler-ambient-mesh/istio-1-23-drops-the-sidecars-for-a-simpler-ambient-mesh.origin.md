# Istio 1.23 Drops the Sidecar for a Simpler ‘Ambient Mesh’
![Featued image for: Istio 1.23 Drops the Sidecar for a Simpler ‘Ambient Mesh’](https://cdn.thenewstack.io/media/2024/08/0400bf13-istio.png)
![Louis Ryan.](https://cdn.thenewstack.io/media/2024/08/1b2fa23a-louis-ryan-300x225.jpg)
Louis Ryan, CTO, Solo.io

The [new release](https://istio.io/latest/news/releases/1.23.x/announcing-1.23/?ref=dailydev) of the open source [Istio](https://istio.io/latest/) service mesh software offers a potentially big change in how to handle [Kubernetes](https://www.thenewstack.io/Kubernetes) traffic, with the introduction of an [ambient mesh](https://thenewstack.io/traffic-routing-in-ambient-mesh/) option.

Although the technology has been offered as an experimental feature for several releases, the core development team taking feedback from users, this is the first release to offer the feature as a production-grade capability.

It’s a new architecture entirely, explained [Louis Ryan](https://github.com/louiscryan), who is the CTO of commercial Istio provider [Solo.io](https://www.solo.io/), as well as a member of [Istio Technical Oversight Committee and Steering Committee](https://github.com/istio/community/blob/master/TECH-OVERSIGHT-COMMITTEE.md), in a TNS interview. “It’s cheaper, faster, easier to deploy more scalable, better.”

An “ambient” service mesh is one that, unlike traditional approaches, does not require a separate sidecar to accompany each application.

Istio is a project of the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), making it a building block of many Kubernetes deployments.

## Istio Sans Sidecar
The sidecar was a necessary byproduct of [microservices architecture](https://thenewstack.io/year-in-review-was-2023-a-turning-point-for-microservices/), noted [Idit Levine](https://www.linkedin.com/in/iditlevine/), founder and CEO of Solo.io. Once applications are decomposed into individual services, these services require a way to communicate. Hence it made sense to festoon each service with a sidecar to handle all the networking traffic.

The sidecar provides security, improved reliability, and dynamic networking capabilities for each application.

Sidecars solved “a real problem,” Levine noted. The sidecar provided the functionality, but the designer “overlooked” how much overhead they would bring to the machine itself.

In contrast, the ambient approach “is reducing costs because there is no sidecar everywhere. But it’s still giving you the security that you’re looking for, and all the functionality,” Levine said. “So it’s actually really amazing.”

Solo.io engineers have been working on refining the ambient approach for several years now.

## How Ambient Mesh Works
“This innovative approach makes networking in Kubernetes even easier. No more extra steps with sidecars. Services can now communicate more directly and simply,” wrote AWS community builder [Seifeddine Rajhi](https://x.com/RajhiSaifeddine), [in a post](https://itnext.io/kubernetes-networking-with-ambient-istios-sidecarless-innovation-0ef5fcc267f8) explaining the technology.

Ambient Mesh is built on a [zero trust architecture](https://thenewstack.io/beyondcorp-google-ditched-virtual-private-networking-internal-applications/). The [ztunnel](https://github.com/istio/ztunnel) zero trust tunnel, a [daemonset](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) pod written in [Rust](https://thenewstack.io/rust-meets-dart-with-release-of-rust_core-1-0-0/), is installed on each cluster to handle Layer 3 and Layer 4 traffic. Then, the [Envoy](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/)-based [Waypoint Proxies](https://istio.io/latest/blog/2023/waypoint-proxy-made-simple/) to handle more complex Layer 7 traffic for each [namespace](https://thenewstack.io/leveraging-namespaces-for-cost-optimization-with-kubernetes/), Rajhi explained

So, as an example, for 50 pods, with each pod only receiving 50 requests per second, you can have a single proxy handle all of them. “That’s a massive resource savings,” Ryan pointed out.

There are other advantages as well. Upgrades are a lot easier, as applications do not need to be taken offline to assign a sidecar. Instead, updates of the daemonsets can be done on a rolling basis. This is where the “ambient” name comes in, meaning there are far fewer endpoints to manage. The functionality is built into the cluster itself.

“The user experience is just simple. It’s easy to install, it’s easy to operate. You don’t have a lot of overhead like we had with a sidecar model,” Levine enthused.

![Diagram of Ambient Waypoint.](https://cdn.thenewstack.io/media/2024/08/d86b6902-waypoint-architecture.png)
Running independent of the application, the waypoint proxy operates independently of the application itself.

## Istio Ambient Could Be Faster too
And, despite its experimental nature, the ambient mesh, at least in some cases, can reduce latency, compared to a traditional Istio setup.

In a [contributed post](https://thenewstack.io/ambient-mesh-can-sidecar-less-istio-make-applications-faster/) for The New Stack, [Lin Sun](https://thenewstack.io/author/lin-sun/), Solo.io director of open source and also a member of Istio Technical Oversight Committee and Steering Committee, demonstrated that Istio can actually reduce the latency of user applications in some cases.

To run the tests, she used both the [Fortio](https://github.com/fortio/fortio) load testing library and Istio’s own [Bookinfo](https://istio.io/latest/docs/examples/bookinfo/) sample app.

“We’ve been taught that service meshes add latency,” Sun wrote. These results “show a case where a workload is faster when running through a service mesh.”

In this test, Sun replicated the results of an [earlier test](https://a-cup-of.coffee/blog/istio/#with-istio-ambient) from site reliability engineer [Quentin Joly](https://github.com/QJoly), who found that:

*Istio Ambient: 2.35ms latency;*
*Without Istio: 2.8ms latency;*
*Istio Sidecar: 39.3ms latency.*
“It’s quite amazing that Istio Ambient manages to reduce latency compared to a cluster without Istio,” he wrote. “This shows that the ‘Ambient’ mode is a viable solution that can potentially improve the performance of your Kubernetes cluster.”

## Other New Features to Istio 1.23
**DNS auto-allocation improvements**: Address allocation has been revamped, solving a number of issues for service routing. “In the new approach, the allocated IP addresses are persisted in the*ServiceEntry*status field, ensuring that they are never changed,” the notes state.**Retry Improvements**: The retry policy has been revamped, with the changes now in preview, which aim to reduce[503 errors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503). To date, retries were only done with outbound traffic, with retries going to a different pod. A new detection routine has been added to determine if the destination application has closed the connection.**Bookinfo revamp**: The sample application used to test Istio deployments has been revamped.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)