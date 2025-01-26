# Powerful Load Balancing Strategies: Kubernetes Gateway API
### Episode #41: From ClusterIP to Ingress and Gateway API. Discover the most common strategies to load balance services in Kubernetes.
There are many ways to expose HTTP applications running in Kubernetes.

A typical setup involves creating a deployment and an associated service.

The type of Service decides the visibility of your application.

The most common types of [Kubernetes Services](https://kubernetes.io/docs/concepts/services-networking/service/) are:

`ClusterIP`
: default value (if no type is provided) that only exposes an application internally to other services in the same Kubernetes cluster.`NodePort`
: primarily used for testing to expose a service externally at every cluster node at a chosen port.`LoadBalancer`
: used for production use cases in the cloud to expose the service outside your cluster.
This is it, right?

That's what I thought for a while since that is what I learned when I took the Certified Kubernetes Admin (aka CKA) exam more than two years ago.

In this article, we will briefly introduce CluterIP and LoadBalancer Service types and discuss the alternatives of [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) and [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/).

We will briefly discuss each option and its pros and cons and provide some code samples to get you started.

This article has the following sections:

A small caveat

ClusterIP: exposing a service internally

LoadBalancer: exposing a service in the cloud

Ingress: a single gateway for all services

Gateway API: the modern alternative to Ingress

**Want to connect?**
👉 Follow me on [LinkedIn](https://www.linkedin.com/in/santorogiuseppe/) and [Twitter](https://twitter.com/gsantoro15).

If you need 1-1 mentoring sessions, please check my [Mentorcruise profile](https://mentorcruise.com/mentor/giuseppesantoro/).

**A small caveat**
The code samples in this article are working examples, even if just a toy application.

They are kept as simple as possible since there is a lot to cover, and we only want to focus on the load-balancing strategies.

We will use a container image called [traefik/whoami](https://github.com/traefik/whoami) that returns the content of an HTTP request with all its headers and parameters as output.

This container image is used by the Reverse Proxy [Traefik](https://traefik.io/traefik/) in their official documentation. Since Traefik is my Reverse Proxy of choice (since it comes as default in [K3d](https://k3d.io/)), this is what we are going to use in this article.

Even if those code samples have been tested with K3d and Traefik, they should be working with any Kubernetes distribution or any Reverse Proxy.

More info on setting up those code samples is not part of this article. I'll write about it in the future.

This article doesn't mean to be an exhaustive tutorial to load balancers in Kubernetes. There would be too much to cover.

I would like to introduce you to the concepts so that you know those things exist in the first place.

I'll provide some external resources to keep the learning going.

**ClusterIP: exposing a service internally**
The bare minimum to create and expose an HTTP application is to create a Kubernetes Deployment and an associated service.

Throughout the article, we will use the same Kubernetes Deployment, the code provided in the following image.

As discussed above, this is just a toy application that is useful for debugging HTTP network routing.

We will see what the output of this application looks like later in the section for Ingress.

Aside from the boilerplate code for a deployment, you should notice:

we are creating three replicas of the same pod. This is so that when running the client, you will be returned a different internal IP for each pod responding.

The container port used by the application is configured by the environment variable

`PORT`
and then referenced by the`containerPort: 80`
We will use the Kubernetes label

`label: my-app`
for deployment, service, and pods.
Once you have a deployment, you can create an associated service with no type.

By default the type of the Service is `ClusterIP`
, and the Service will only be accessible from other services and pods inside the same Kubernetes cluster.

There is not much to notice from this Service except that it exposes an HTTP application at port 80.

As per the above deployment, the Service above will be used (mostly as it is) in the following chapters.

**LoadBalancer: exposing a service in the cloud**
As discussed at the beginning, if you want to expose a service externally to the internet for a production use case, you need to create a Service of type `LoadBalancer`
.

The cloud provider where you are running your Kubernetes cluster will provide a Load balancer associated with this Service.

A different load balancer will be created for each Service you want to expose.

As you can notice, the only difference from the Service in the previous section is the type of Service in `spec.type = LoadBalancer`
.

**Pros and Cons**
While this solution is straightforward, it starts to be a problem when you have many microservices and don't want to create a single Load balancer for each of those external services.

While this solution is perfect when running in the cloud, it doesn't work when running your Kubernetes cluster locally on your machine, for example, with K3d.

Suppose you, like me, firmly believe that a local Kubernetes cluster should be able to allow you to replicate a production use case. In that case, you are out of luck here.

Alternatively, you could use a Service Mesh provider like [Istio](https://istio.io/). Still, for simple use cases, there is a much simpler alternative.

**Ingress: a single gateway for all services**
A while ago, Kubernetes decided that a good alternative to a single Load Balancer for each Service was to create a resource called [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) that would allow Reverse Proxies like Traefik or Nginx to create complex routing rules.

This Ingress resource points to the service definition that we defined in the section `ClusterIP: exposing a service internally`
and the related deployment. For brevity, the code is not duplicated here.

To reach the Service from your laptop, you will have to run the following curl command:

```
curl -H "Host: my-app.example" http://localhost:8080
```
As you might have noticed, `my-app.example`
is the hostname defined in the Ingress resource at `spec.rules.host`
.

As a reference, the output of the curl command is the following.

The example provided in this section is officially called `Host-Based Routing (Virtual Hosting)`
and it is only one of the many use cases for Ingress:

Path-Based Routing

SSL/TLS Termination

Load Balancing and Traffic Management

Authentication and Access Control

**Pros and cons of using Ingress API**
Between the pros of using Ingress:

Well-established API supported by all major Reverse Proxies (e.g. Traefik, Nginx)

Works on a local Kubernetes cluster with K3d as well as in the cloud

Between the cons:

Only support L7 Load balancing. There is no support for L4 protocols like TCP and UDP

From the L7 network stack it only supports HTTP/S. It doesn't support GRPC. This might be inconvenient if you want to support microservices.

Ingress is not a standard API between all Reverse Proxies. There might be some differences in the spec and ways to implement some routing strategies.

**Gateway API: the modern alternative to Ingress**
The problem with `Ingress`
is that most Reverse Proxies have their way of implementing those routing rules.

Each one of the Reverse Proxies would require the user to provide either a custom Kubernetes annotation, a custom middleware extension or some custom Kubernetes Custom Resources (CRDs).

This was the case until a new Kubernetes API was introduced called [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/).

As you can see from above, instead of an Ingress you can replicate the same outcome with a `HTTPRoute`
.

In this scenario, you will be able to hit the backend service with a command like:

`curl -H "Host: load-balance.example" http://localhost:8080`
**Pros and cons of Gateway API**
Between the pros:

Similar concept to Ingress. A single network endpoint for all services instead of a single load balancer per Service.

Support both L4 and L7 network protocols (eg. UDP, TCP, HTTP/S and GRPC).

Standard API across multiple Reverse Proxies (eg. Traefik, Nginx, etc).

Between the cons:

it is a much newer API, so not all features are implemented by all Reverse Proxies. As an example, for the complete list of features supported by the latest version of Traefik v3.2.2 visit

[gateway-api/conformance/reports/v1.2.1/traefik-traefik/experimental-v3.2.2-default-report.yaml at main · kubernetes-sigs/gateway-api](https://github.com/kubernetes-sigs/gateway-api/blob/main/conformance/reports/v1.2.1/traefik-traefik/experimental-v3.2.2-default-report.yaml).
Well written🔥👍