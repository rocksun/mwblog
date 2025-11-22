Running the [Ingress Nginx controller](https://github.com/kubernetes/ingress-nginx/) for your Kubernetes clusters? You have until March to migrate to the Gateway API, or some other option, the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) decreed [KubeCon+CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) last week.

It was news that many knew was coming but were still surprised by, especially [the quick turnaround](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement) asked of them.

“So you’ve got a lot of people scrambling around the conference today looking for a replacement, because Ingress is the default ingress controller for Kubernetes,” said HAProxy’s vice president of engineering and operations, [Frank Mancina](https://theorg.com/org/haproxy-technologies/org-chart/francesco-mancina), in a booth interview with TNS at the event.

Kubernetes SIG Network and the Security Response Committee plan to put Ingress Nginx to rest in March 2026. After that, the software will not be supported: No further releases, no bugfixes, and no updates to resolve any security vulnerabilities.

The code will remain on [GitHub](https://github.com/kubernetes/ingress-nginx) for archival purposes, as well as supporting software such as the [Helm operator](https://github.com/nginx/nginx-ingress-helm-operator).

Those who continue to operate the controller after March do so at their own risk.

Wondering if your cluster runs Ingress Nginx? At a command line with cluster administration rights, type this:

```

kubectl get pods \--all-namespaces \--selector app.kubernetes.io/name=ingress-nginx
```

## Networking for Kubernetes

Networking support came late for Kubernetes. The CNCF had worked on the Gateway API for four years, releasing version 1 last year. The Gateway routes traffic on and off the cluster, both Layer 4 (the TCP/IP layer) and Layer 7 traffic (for application traffic).

The Ingress itself is a set of API rules to direct external network traffic accessing a cluster. The Ingress Nginx controller was born as a Kubernetes project. It used the open source Nginx reverse proxy, [now managed by network company F5 Inc.](https://techcrunch.com/2019/03/11/f5-acquires-nginx-for-670m-to-move-into-open-source-multi-cloud-services/), as the base. The [Ingress Nginx controller](https://github.com/kubernetes/ingress-nginx) went on to be one of a number of controllers that popped up to implement the Ingress API.

The Kubernetes networking and security groups in charge of the project found it a challenge to maintain, however. Finding folks to help maintain the code base was a challenge, especially after the Gateway API project got underway. Plus, the ability to add arbitrary NGINX configuration directives, [known as snippets](https://docs.nginx.com/nginx-ingress-controller/configuration/ingress-resources/advanced-configuration-with-snippets/), became a security issue.

Built on a set of Kubernetes [Custom Resource Definitions](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) (CRDs), the [Gateway API](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/) was introduced in 2023, and it has since become CNCF’s preferred and future-proof way of doing ingress (inbound) and egress (outbound traffic) for Kubernetes.

“You have much more specification and control with Gateway API spec. That’s why people would probably migrate to it. And Kubernetes moves very, very quickly, and this seems to be the specification that’s gaining the most traction,” Mancina further explained.

## Companies Respond

Reverse proxy software provider [HAProxy Technologies LLC](https://www.haproxy.com/?utm_content=inline+mention)  is one company responding to the Gateway API initiative. It has long offered [HAProxy Ingress](https://github.com/haproxytech/kubernetes-ingress) and has expanded its support for Gateway API with the newly-launched [HAProxy Unified Gateway](https://www.haproxy.com/blog/announcing-haproxy-unified-gateway-beta) — a free, open source product providing Kubernetes-native application routing for both Gateway API and Ingress.

“What we’ve seen is that we have customers who have their workflow which is already established with Ingress rules, and they don’t want to change it,” HAProxy director of product [Baptiste Assmann](https://www.linkedin.com/in/bassmann/?originalSubdomain=fr), in an interview with TNS.

The Unified Gateway is designed to provide a way to easily transition into the Gateway API as time permits. Or run both side-by-side.

“Instead of having one product for Ingress rules and one product for Gateway APIs and having people choose one or the other, the strategy is to have the new product also support Ingress rules, so people can start using Ingress rules and then switch to Gateway API when they are ready,” Assmann said.

Switching from one to another may take some work, he advised, because of their different architectures.

While Ingress runs on a central controller model, the Gateway API runs on the Kubernetes operator model. “It’s a totally different way to configure things,” he added.

The Gateway API has superior separation of concerns, further explained Mancina. For instance, it distinguishes between objects that can be controlled by the platform team, those that are controlled by the operations team, and those by the applications team.

HAProxy is also working, bringing over a select number of Nginx annotations over to the unified gateway.

Other platforms offering Gateway API support include the [Nginx Gateway Fabric](https://github.com/nginx/nginx-gateway-fabric) (read TNS analysis Janakiram MSV’s deep dive [here](https://thenewstack.io/cncf-deprecates-the-ingress-nginx-controller/)) as well as [Envoy](https://gateway.envoyproxy.io/docs/tasks/traffic/gatewayapi-support/), [Istio](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/), [Cilium](https://youtu.be/dqyBoqJYveQ), and CNCF’s own [KGateway](https://www.cncf.io/blog/2025/11/18/kgateway-v2-1-is-released).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)