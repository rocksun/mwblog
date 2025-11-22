The Kubernetes ecosystem is undergoing a fundamental shift in how it manages external traffic. On Nov. 12, 2025, Kubernetes [announced](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/) the retirement of Ingress Nginx, one of the most widely deployed components in cloud native infrastructure. Best-effort maintenance [continues until March 2026](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/), after which the repository will move to read-only status, with no further security patches, bug fixes, or feature releases.

This marks a critical inflection point for organizations running Kubernetes clusters. The traditional Ingress API, while battle-tested and familiar to generations of engineers, has reached the limits of its design. It lacks support for advanced traffic management patterns, forces teams to wrestle with vendor-specific annotations, and cannot express sophisticated routing rules needed for modern applications.

The [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) emerges as the successor, which is a standardized, extensible framework that addresses these fundamental limitations. Rather than relying on fragmented implementations and proprietary annotations, Gateway API introduces a unified model that supports multiprotocol routing (L4 and L7), fine-grained traffic control, header-based pattern matching, request mirroring, and native traffic metrics.

Achieving General Availability in 2023, Gateway API represents the Kubernetes community’s answer to the ingress problem. For a detailed comparison of Ingress controller and Gateway, refer to my previous article published in The New Stack.

One of the early implementations of the Gateway API is [Nginx Gateway Fabric](https://github.com/nginx/nginx-gateway-fabric), which is an open source, conformant implementation of the Kubernetes Gateway API that uses Nginx as its high-performance data plane. It separates control plane and data plane concerns, dynamically provisioning Nginx instances for each Gateway resource while translating Gateway API resources into Nginx configurations. Unlike traditional [Ingress controllers](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/), Nginx Gateway Fabric delivers advanced capabilities out of the box, including blue-green and canary deployments, A/B testing, request/response manipulation, and multitenant role-based governance.

This tutorial will guide you through implementing the [Gateway API](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/) based on Nginx Gateway Fabric, helping you prepare your infrastructure for the post-Ingress era. We will start with a familiar Kubernetes deployment with two services: one for the web and one for the API. We will use the Gateway API to route HTTP traffic to these two internal ClusterIP services.

For this tutorial, I am using a [K3s](https://k3s.io/) cluster running inside a [Multipass VM](https://thenewstack.io/multipass-fast-scriptable-ubuntu-vms-for-modern-devops/). But you can use any Kubernetes environment to complete the steps explained in this guide.

## Step 1: Define and Deploy the Sample App

We will define two deployments and services to expose the web and api endpoints as ClusterIP services in the demo namespace.

Apply the YAML and check if the pods and services are up and running.

```

kubectl get pods,svc -n demo
```

![](https://cdn.thenewstack.io/media/2025/11/b4d4c445-gw-api-0-1024x441.png)

Our goal is to route traffic to the demo-api and demo-app endpoints through the Gateway API.

## Step 2: Deploy Nginx Gateway Fabric

We will first install the CRDs required by the gateway.

```

kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v2.2.1" \
  | kubectl apply -f -
```

```

kubectl get crd | grep gateway.networking.k8s.io
```

![](https://cdn.thenewstack.io/media/2025/11/00d54d12-gw-api-1-1024x337.png)

Then, we will deploy Nginx Gateway Fabric through the Helm chart.

```

helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
  --create-namespace \
  -n nginx-gateway \
  --set nginx.service.type=NodePort
```

Notice that we are exposing the service type as NodePort. If you are using a managed Kubernetes environment, change this to `LoadBalancer`.

Verify the installation by checking the `nginx-gateway`

```

kubectl get pods,svc -n nginx-gateway
```

![](https://cdn.thenewstack.io/media/2025/11/184c369f-gw-api-2-1024x254.png)

The next step is to deploy the Gateway that application developers will use to define the route to their services running within their namespaces.

Apply the YAML file and verify that the gateway is created correctly.

```

kubectl apply -f gateway.yaml
```

```

kubectl get pods,svc -n nginx-gateway
```

![](https://cdn.thenewstack.io/media/2025/11/ed62af7d-gw-api-3-1024x303.png)

We can see that the gateway has been created and is exposed via the `NodePort` 31678.

## Step 3: Define the Route to the Sample App

With the gateway in place, it’s time to create the route. This is typically done by the developers who are deploying their app in Kubernetes. Route runs within the same namespace as the application.

Define the route and deploy it.

```

kubectl apply -f route.yaml
```

This created an `HTTPRoute` for the endpoints exposed by the sample application.

## Step 4: Access the HTTP Endpoints Exposed by the Gateway

We are ready to test the routes defined by the gateway.

Given that my VM’s IP address is `192.168.2.5` and the `NodePort` is 31678, I can make a cURL request to test the endpoints.

![](https://cdn.thenewstack.io/media/2025/11/d1e836d7-gw-api-4.png)

We have successfully implemented the Gateway API to expose internal endpoints to the external users. In the upcoming tutorials, I will walk through the steps to implement TLS-based routing. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)