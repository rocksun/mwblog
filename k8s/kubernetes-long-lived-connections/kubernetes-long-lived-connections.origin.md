# Load balancing and scaling long-lived connections in Kubernetes
June 2024
*TL;DR: Kubernetes doesn't load balance long-lived connections, and some Pods might receive more requests than others. Consider client-side load balancing or a proxy if you're using HTTP/2, gRPC, RSockets, AMQP, or any other long-lived database connection.*
Kubernetes offers two convenient abstractions for deploying apps: Services and Deployments.
**Deployments describe a recipe for what kind and how many copies your app should run at any given time.**
Each app is deployed as a Pod, and an IP address is assigned.
**Services, on the other hand, are similar to load balancers.**
They are designed to distribute the traffic to a set of Pods.
- 1/4
In this diagram, you have three instances of a single app and a load balancer.
- 2/4
The load balancer is called Service and has an IP address. Any incoming request is distributed to one of the Pods.
- 3/4
The Deployment defines a recipe to create more instances of the same Pod. You rarely deploy Pod individually.
- 4/4
Pods have an IP address assigned to them.
**It is often helpful to consider Services as a collection of IP addresses.**
Whenever you request a Service, one of the IP addresses on that list is selected and used as the destination.
- 1/3
Imagine issuing a request such as
curl 10.96.45.152to the Service.
- 2/3
The Service picks one of the three Pods as the destination.
- 3/3
The traffic is forwarded to that instance.
If you have two apps, a front-end and a backend, you can use a Deployment and a Service for each and deploy them in the cluster.
**When the front-end app makes a request, it doesn't need to know how many Pods are connected to the backend Service.**
It could be one Pod, tens or hundreds.
The front-end app isn't aware of the individual IP addresses of the backend app either.
When it wants to make a request, that request is sent to the backend Service with an IP address that doesn't change.
- 1/4
The red Pod issues a request to an internal (beige) component. Instead of choosing one of the Pods as the destination, the red Pod issues the request to the Service.
- 2/4
The Service selects one of the ready Pods as the destination.
- 3/4
The traffic flows from the red Pod to the light brown Pod.
- 4/4
Notice how the red Pod doesn't know how many Pods are hidden behind the Service.
*But what's the load-balancing strategy for the Service?* *It is round-robin, right?*
Sort of.
## Load balancing in Kubernetes Services
**Kubernetes Services don't exist.**
There's no process for listening to the IP address and port of the Service.
You can check that this is the case by accessing any node in your Kubernetes cluster and executing
netstat -ntlp.
Even the IP address can't be found anywhere.
The IP address for a Service is allocated by the control plane in the controller manager and stored in the database — etcd.
That same IP address is then used by another component: kube-proxy.
Kube-proxy reads the list of IP addresses for all Services and writes rules in every node.
The rules are meant to say, " If you see this Service IP address, rewrite the request and pick one of the Pods as the destination."
The Service IP address is used only as a placeholder, so no process is listening on the IP address or port.
- 1/8
Consider a cluster with three Nodes. Each Node has a Pod deployed.
- 2/8
The beige Pods are part of a Service. Services don't exist, so the diagram has the component greyed out.
- 3/8
The red Pod wants to issue a request to the Service and eventually reaches one of the beige Pods.
- 4/8
But Services don't exist. There's no process listening on the Service's IP address.
*How does it work?*
- 5/8
Before the request is dispatched from the Node, it is intercepted by iptables rules.
- 6/8
The iptables rules know that the Service doesn't exist, so replace its IP address with one of the IP addresses of the Pods connecting to that Service.
- 7/8
The request has a real IP address as the destination, and it can proceed normally.
- 8/8
Depending on your network implementation, the request finally reaches the Pod.
By default, Kubernetes uses iptables to implement Services.
*Does iptables use round-robin for load balancing?*
No, iptables are primarily used for firewalls and are not designed for load balancing.
However, you could
[craft an intelligent set of rules to make iptables behave like a load balancer](https://scalingo.com/blog/iptables#load-balancing).
And this is precisely what happens in Kubernetes.
If you have three Pods, kube-proxy writes the following rules:
- With a likelihood of 33%, select Pod 1 as the destination. Otherwise, proceed to the following rule.
- With a probability of 50%, choose Pod 2 as the destination. Otherwise, proceed to the following rule.
- Select Pod 3 as the destination (no probability).
The compound probability is that Pod 1, Pod 2, and Pod 3 have a one-third chance (33%) of being selected.
Also, there's no guarantee that Pod 2 is selected after Pod 1 as the destination.
Iptables use the
[statistic module]with
randommode. So, the load balancing algorithm is random.
You might have heard of alternatives to iptables, such as ipvs and eBPF.
While the technology differs, the core idea is similar: how can the traffic be redirected to the right pod?
In the case of eBPF,
[the network packets are processed in the kernel in the eBPF virtual machine, and it's the eBPF program that defines the load balancing algorithm.](https://github.com/lizrice/lb-from-scratch)
Now that you know how services work, let's look at more exciting scenarios.
## Long-lived connections don't scale out of the box in Kubernetes
**With every HTTP request started from the front-end to the backend, a new TCP connection is opened and closed.**
If the front-end makes 100 HTTP requests per second to the backend, 100 different TCP connections are opened and closed in that second.
You can improve the latency and save resources if you open a TCP connection and reuse it for subsequent HTTP requests.
The HTTP protocol has a feature called HTTP keep-alive, or HTTP connection reuse that uses a single TCP connection to send and receive multiple HTTP requests and responses.
It doesn't work out of the box; your server and client should be configured to use it.
The change itself is straightforward, and it's available in most languages and frameworks.
Here are a few examples of how to implement keep-alive in different languages:
*What happens when you use keep-alive with a Kubernetes Service?*
Let's imagine that front-end and backend support keep-alive.
You have a single instance of the front-end and three replicas for the backend.
The front-end makes the first request to the backend and opens the TCP connection.
The request reaches the Service, and one of the Pods is selected as the destination.
The backend Pod replies and the front-end receives the response.
But instead of closing the TCP connection, it is kept open for subsequent HTTP requests.
*What happens when the front-end issues more requests?* **They are sent to the same Pod.** *Isn't iptables supposed to distribute the traffic?*
It is.
A single TCP connection is open, and the iptables rule was invoked the first time.
One of the three Pods was selected as the destination.
Since all subsequent requests are channelled through the same TCP connection,
[iptables isn't invoked anymore.](https://scalingo.com/blog/iptables#load-balancing)
- 1/5
The red Pod issues a request to the Service.
- 2/5
You already know what happens next. Services don't exist, but iptables rules intercept the requests.
- 3/5
One of the Pods that belong to the Service is selected as the destination.
- 4/5
Finally, the request reaches the Pod. At this point, a persistent connection between the two Pods is established.
- 5/5
Any subsequent request from the red Pod reuses the existing open connection.
**So you have now achieved better latency and throughput but lost the ability to scale your backend.**
Even if you have two backend Pods that can receive requests from the front-end Pod, only one is actively used.
*Is it fixable?*
You could fix it yourself since Kubernetes doesn't know how to load balance persistent connections.
**Services are a collection of IP addresses and ports called endpoints.**
Your app could retrieve the list of endpoints from the Service and decide how to distribute the requests.
As a first try, you could open a persistent connection to every Pod and round-robin requests to them.
Or you could
[implement more sophisticated load-balancing algorithms](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html).
The client-side code that executes the load balancing should follow the logic below:
- Retrieve a list of endpoints from the Service.
- For each of them, open a connection and keep it open.
- Pick one of the open connections When you need to make a request.
- At regular intervals, refresh the list of endpoints and remove or add new connections.
- 1/4
Instead of having the red Pod issue a request to your Service, you could load balance the request on the client side.
- 2/4
You could write some code that asks what Pods are part of the Service.
- 3/4
Once you have that list, you could store it locally and use it to connect to the Pods.
- 4/4
You are in charge of the load balancing algorithm.
*Does this problem apply only to HTTP keep-alive?*
## Long-lived database connections
**HTTP isn't the only protocol that can benefit from long-lived TCP connections.**
If your app uses a database, the connection isn't opened and closed whenever you wish to retrieve a record or a document.
Instead, the TCP connection is established once and kept open.
If your database is deployed in Kubernetes using a Service, you might experience the same issues as the previous example.
**One replica in your database is utilized more than the others.**
Kube-proxy and Kubernetes don't help to balance persistent connections.
Instead, you should take care of load-balancing the requests to your database.
At this point, you have two options:
- Change your app to support connecting to multiple backends.
- Introduce a
*real*load balancer to distribute the load.
In the first option, you move the load-balancing decision to the app.
In pseudo-code, this is what you should do if you want to connect to a database with multiple replicas:
Before issuing an SQL query:
- Retrieve all replica IPs from the Services.
- Pick a different replica from the previous one.
- Dispatch the SQL query
This logic may already be present depending on the library you use to connect to your database.
In the case of
[JDBC](https://jdbc.postgresql.org/documentation/use/#connection-fail-over), the following line allows to load balance queries to three Postgres replicas:
jdbc:postgresql://node1,node2,node3/database?loadBalanceHosts=true
[SQLAlchemy supports providing multiple IP addresses](https://github.com/sqlalchemy/sqlalchemy/issues/4392) but doesn't offer load balancing (the IP addresses are tried in sequence until one works. At that point, the connection remains stable). *In this case, what could you do?*
You could open several different SQL connections and cycle through them.
Or you could use an external load balancer like
[pgpool](https://www.pgpool.net/mediawiki/index.php/Main_Page).
In this scenario, your app connects to a single endpoint: pgpool.
[Then, pgpool load balance the queries against all available Postgres replicas.](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html) **So, even if the connection between the app and pgpool is persistent (i.e. long-lived), the queries still utilize all available replicas.**
We solved long-lived connections in Postgres, but several other protocols work over long-lived TCP connections.
Here you can read a few examples:
- Websockets and secured WebSockets
- HTTP/2
- gRPC
- RSockets
- AMQP
*What should you do with those?*
It boils down to two options:
- You handle the load balancing client-side or
- You use an external tool that does that for you.
Let's look at two more common examples: gRPC and WebSockets.
[You can load balance gRPC requests in your app](https://itnext.io/grpc-name-resolution-load-balancing-everything-you-need-to-know-and-probably-a-bit-more-77fc0ae9cd6c), or you can use a [proxy like Envoy to load balance gRPC requests.](https://svkrclg.medium.com/grpc-load-balancing-using-envoy-e8972214da2c)
When it comes to WebSockets, things are more complex.
You can only balance the connection on the client side if you open several tunnels and cycle through them.
You are left with using a
[load balancer like HAProxy.](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/load-balancing/websocket/) **Notice how solving the persistent connection on the server side is mostly about finding a suitable proxy to balance connections, whereas load-balancing on the client side requires more thinking.**
But there are ways to solve that.
## Load balancing long-lived connections in Kubernetes
Kubernetes has four different kinds of Services:
- ClusterIP
- NodePort
- LoadBalancer
- External
They all have a virtual IP address that kube-proxy uses to create iptables rules.
**But the fundamental building block of all kinds of the Services is the Headless Service.**
The headless Service doesn't have an assigned IP address and is only a mechanism to collect a list of Pod IP addresses and ports (also called endpoints).
Every other Service is built on top of the Headless Service.
The ClusterIP Service is a Headless Service with some extra features:
- The control plane assigns it an IP address.
- kube-proxy iterates through all the IP addresses and creates iptables rules.
You could ignore kube-proxy and always use the list of endpoints collected by the Headless Service to load balance requests from the client side.
*But can you imagine adding that logic to all apps deployed in the cluster?*
This might sound like an impossible task if you have an existing fleet of applications.
But there's an alternative.
## Service meshes to the rescue
You probably already noticed that the client-side load-balancing strategy is relatively standardized.
When the app starts, it should
- Retrieve a list of IP addresses from the Service.
- Open and maintain a pool of connections.
- Periodically refresh the pool by adding and removing endpoints.
As soon as it wishes to make a request, it should:
- Pick one of the available connections using a predefined logic such as round-robin.
- Issue the request.
That's similar to how pgpool worked in the previous example.
And the steps above are valid for WebSockets connections, gRPC, and AMQP.
You could extract that logic in a separate library and share it with all apps.
Instead of writing a library from scratch, you could use a Service mesh such as
[Istio](https://istio.io/) or [Linkerd](https://linkerd.io/).
Service meshes augment your app with a new process that:
- Automatically discovers IP addresses from Services.
- Inspects connections such as WebSockets and gRPC.
- Load-balance requests using the correct protocol.
**Service meshes can help you manage the traffic inside your cluster, but they aren't lightweight.** *What happens if you ignore it?*
You can ignore the load balancing and still don't notice any change.
There are a couple of scenarios that you should consider.
**If you have more clients than servers, there should be limited issues.**
Imagine you have five clients opening persistent connections to two servers.
Even if there's no load balancing, both servers are likely utilized.
The connections might be distributed unevenly (perhaps four ended up connecting to the same server), but overall, there's a good chance that both servers will be utilized.
What's more problematic is the opposite scenario.
**If you have fewer clients and more servers, you might have some underutilized resources and a potential bottleneck.**
Imagine having two clients and five servers.
At best, two persistent connections to two servers are opened.
The remaining servers are not used at all.
**If the two servers can't handle the client traffic, horizontal scaling won't help.**
## Summary
Kubernetes Services are designed to cover the most common uses for web applications.
However, they fall apart as soon as you start working with application protocols that use persistent TCP connections, such as databases, gRPC, or WebSockets.
Kubernetes doesn't offer any built-in mechanism to load balance long-lived TCP connections.
Instead, you should code your application to retrieve and load balance upstreams client-side.
Or you should consider a proxy that can load balance connections.
Many thanks to
[Daniel Weibel](https://medium.com/@weibeld), [Gergely Risko](https://github.com/errge) and [Salman Iqbal](https://twitter.com/soulmaniqbal) for offering some invaluable suggestions.
And to
[Chris Hanson](https://twitter.com/CloudNativChris), who suggested including a detailed explanation (and flow chart) on how iptables rules work in practice.