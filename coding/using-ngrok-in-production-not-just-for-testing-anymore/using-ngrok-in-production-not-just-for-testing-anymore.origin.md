# Using ngrok in Production: Not Just for Testing Anymore
![Featued image for: Using ngrok in Production: Not Just for Testing Anymore](https://cdn.thenewstack.io/media/2024/07/f9dd0d0e-network-ingress-api-ngrok-1024x576.jpg)
The biggest challenge in serving digital services across vast, global networks is enabling those services to communicate with each other securely. Securing the endpoints is often not nearly as daunting as securing the routes between them.

If you’ve ever used ngrok to generate an *ad hoc* secure tunnel so that services and browsers can contact your application even when hosted on `localhost`
, you’ve probably asked yourself whether it would be possible to deliver your production apps and APIs in the same frictionless manner.

If you’re staging an API for testing on your dev team’s network or even your personal laptop, ngrok gives you a way to [open up an HTTPS endpoint](https://ngrok.com/docs/http/) on a local port. You launch your app on your laptop, invoke ngrok through a command line and now your beta tester on another continent has a way in.

## The Network Components in Your Neighborhood
When you’re tackling the problem of network ingress at the service level, it doesn’t look this easy at first. You soon come to realize that [messaging protocols for microservices architecture](https://thenewstack.io/securing-microservices-communication-with-mtls-in-kubernetes/) compound this challenge a thousandfold. When microservices are contacted from outside the network, an [API gateway routes messages](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/) using a variety of web protocols, internal protocols and possibly event-streaming protocols used by Kafka. [Optimally](https://stackoverflow.com/questions/61174839/load-balancer-and-api-gateway-confusion), a good API gateway distributes inter-message traffic efficiently enough that you wouldn’t need a separate load balancer.

In modern networked application architecture, every vital function that makes services securely accessible from outside the network (what network engineers call “north/south traffic”) requires a network component dedicated to that function.

So whether you’re an application developer or a cybersecurity engineer, to paraphrase [Bob from Sesame Street](https://muppet.fandom.com/wiki/The_People_in_Your_Neighborhood), these are the units in your neighborhood:

**Network Address Translation (NAT) gateway**: To make private IP addresses public**Secure web gateway (SWG)**: To enforce inbound traffic policies and restrictions**API gateway**: To serve as your API’s switchboard to the outside world**Load balancer**: For equitably distributing requests across active instances of requested services**Ingress controller**: Serving the functions of both a reverse proxy and load balancer for microservices**Identity and access manager (IAM)**: To validate services and provide encryption for traffic between them
The problem with the one-component-per-function approach is that it creates a degree of architectural complexity that, in and of itself, becomes a security issue. Also, deploying specialized proxies to manage north-south traffic increases cost and effort for IT, as each one must be deployed, provisioned and maintained — including ensuring security patches are applied in a timely fashion.

## “The Full Front Door”
The alternative to deploying this plethora of services would be a utility that reduces the number of active components to just those necessary to provide secure ingress. Here’s where ngrok reenters the picture.

It may never have occurred to you that ngrok could actually be your ingress controller. That’s to say, you could make the ngrok component a full-time operator in your application or API, managing HTTPS calls to your API and effectively integrating any authenticated remote application with your local microservices application at a granular level.

“[Ngrok] removes moving pieces that an architecture usually has in production,” said [Shub Argha](https://www.linkedin.com/in/shubcodes/), ngrok’s solution architect. “Those moving pieces usually include setting up some sort of web gateway.”

With a traditional microservices application, Argha said, services are placed behind a web gateway that authenticates users, a load balancer that distributes traffic and a separate NAT gateway (the principal component of a basic firewall) that routes traffic to the final destination addresses. Such a gateway typically enables access to resources by means of a private subnet, which joins a large set of internal IP addresses. How and when these resources may be accessed is determined through a set of policies managed by the firewall. Outgoing traffic would be routed through the same NAT gateway on its way out of the network.

“With ngrok, using our ingress controller or API gateway, it replaces all of those things,” stated Argha. “We are the ‘full front door.’ We’ll provide the load balancing as well as both of those gateways, so you don’t have to set them up.”

Although ngrok does provide the ingress control function, once it’s integrated into a networked application, Argha explained, it also serves the functions of a load balancer, web gateway, NAT gateway and API gateway. In so doing, ngrok also assumes responsibility for all the rules and policies that a security engineer would produce for these components separately — components that, Argha noted, “will have additional security rules that all have to be built by you and managed by a security team.”

Ngrok’s authentication functionality and security policies are all handled by a managed service outside the network called ngrok Edge. “You only set up our ingress controller, which makes an outbound connection to our managed service, which automatically provides you with that connectivity.”

[Installing ngrok as an ingress controller](https://ngrok.com/docs/using-ngrok-with/k8s/), or “ingress operator,” happens by means of the [Helm Kubernetes Package Manager](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) (`helm install`
), using [credentials](https://ngrok.com/docs/k8s/deployment-guide/credentials/) obtained from the ngrok Dashboard service. Using that, you create a namespace, then apply a YAML file that assigns that namespace to a specified network port.
By comparison, said Argha, other ingress controllers such as [HAProxy](https://www.haproxy.com/?utm_content=inline+mention) and [NGINX](https://www.nginx.com?utm_content=inline+mention) require implementers, in addition to setting up the components, establishing firewall rules and policies, setting up load balancers and gateways, and ensuring DNS services are directed to the proper endpoints. “There’s a lot more additional steps you need to take before your application is online,” he added. “With ngrok, you don’t.”

## The 90-Degree Turn
Argha said this ease of implementation enables ngrok to be coordinated with a service mesh. In other words, the services running on a network whose accessible endpoints need to be configured to run with an API gateway become accessible to the ngrok API gateway through the routes ngrok automatically sets up.

![Architecture of network interaction between a client app and a subscription music service built with the ngrok agent](https://cdn.thenewstack.io/media/2024/07/34eb1b02-ngrok-model-1024x439.jpg)
Image by Scott M. Fulton based on a drawing by Shub Argha.

The model Argha drew represents network interaction between a client app and a subscription music service built with the ngrok agent. Ngrok’s API gateway manages traffic to the music service, and the agent forwards requests to the various services within the application.

The ngrok Edge platform in the center of this diagram is a managed service, taking care of all the functions listed in the yellow box in the lower right, including [authentication](https://roadmap.sh/guides/basics-of-authentication) and [authorization](https://roadmap.sh/guides/oauth). The backend application is no longer tasked with these functions, which means the application is no longer vulnerable to attacks on the components that would otherwise be responsible for these functions.

Meanwhile, the ngrok agent becomes capable of forwarding inbound remote requests to the various services. Coupled with whatever service mesh may be in place, this enables a remote client to address the services more directly, as though they were discrete applications unto themselves. For the music service example, it means a client app running on a smartphone could make a request of the playlist service for a playlist-related function. Services in the “search” pod can accept search requests as though they were the “search application.” This changes the nature of traffic itself, elevating the role of [Kubernetes](https://thenewstack.io/kubernetes/) pods to more of a first-class citizen.

“Ngrok can get you ingress to all of these different Kubernetes services in different pods,” Argha explained. “What Kubernetes is so good at is, if one pod just magically dies, [Kubernetes] can automatically start it up. Or if a pod is getting a lot of traffic, it can start creating more pods. What ngrok is really good at is routing that traffic to search [from the diagram] or to the playlist.”

Since ngrok is not a service mesh in itself, it has no intelligence about the health or quantity of pods in service or the traffic levels between pods at any one time. You still need a service mesh. In a recent [YouTube video](https://www.youtube.com/watch?v=yYTKQRaOGEM) co-produced by ngrok and Buoyant, Argha and his Buoyant counterpart Flynn demonstrated integrating ngrok with [Linkerd](https://thenewstack.io/buoyant-revises-release-model-for-the-linkerd-service-mesh/). For the demo, Flynn began by taking a few minutes to install ngrok on the backend, just to show how straightforward and quick the process is.

But Linkerd is not the only service mesh ngrok integrates with. Recently, Argha has experimented by pairing ngrok with an open source project stewarded by [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) called Skupper, which technically does not identify itself as service mesh. Rather, it’s a [Layer 7](https://thenewstack.io/the-osi-7-layer-model-can-help-define-enterprise-application-security/) network service interconnection plane project. In such a pairing, ngrok manages north/south routing, and Skupper handles east/west. “It is ngrok turned 90 degrees,” remarked Argha. However, he added, “ngrok can be paired with any service mesh out there, and it’ll work just the same.

“With ngrok, because we take care of the internet layer,” he continued, “everything else you do with our product makes it so you don’t have to worry about setting up that internet layer. That’s what makes us superior,” Argha said.

*To learn more about ngrok for production, including Kubernetes ingress, API gateway, device gateway and more, sign up for free at ngrok.com, check out ngrok’s product documentation or join an upcoming developer livestream.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)