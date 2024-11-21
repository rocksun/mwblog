# How We Made Fast Cloud-to-Cloud Connections Possible
![Featued image for: How We Made Fast Cloud-to-Cloud Connections Possible](https://cdn.thenewstack.io/media/2024/11/1ec3c11c-connection-1024x576.jpg)
The traditional way to enable things hosted in different clouds to talk to each other has been to order a physical cross-connect (a literal cable) from a colo provider that hosts the clouds’ “onramps” (private connections to the clouds’ networks) to link them.

Various software-defined alternatives have emerged in recent years. Some do essentially the same thing but virtually, while others, like typical SD-WANs, rely on things like IPsec or other encryption protocols to secure connections traversing the internet.

There are other, less mature approaches, including some cloud providers’ own intercloud connectivity services. And there’s always the option to send your cloud-to-cloud API requests over the public internet and hope for the best.

The traditional ways tend to be costly and complex to set up, requiring [specialized networking knowledge](https://thenewstack.io/networking/). A little more than a year ago, we decided to build a cloud-to-cloud private connectivity service that would be easier to use. The goal was to give developers who are proficient in cloud but not in networking a way to create multicloud connections and manage them with familiar tools, like Terraform or Pulumi, without hosting any infrastructure in our data centers.

It was an interesting challenge, not in the least from an architecture perspective. We’re going to highlight some of the [key architectural decisions](https://thenewstack.io/3-key-practices-for-perfecting-cloud-native-architecture/) we made as we built the service and explain the reasons behind them.

## Abstracting Network Configuration
The service, [Fabric Cloud Router](https://aws.amazon.com/marketplace/pp/prodview-l3kzqe5fdbqlw?trk=ce4ea0a3-61d4-484e-aac0-1e6f42b319f9&sc_channel=el&source=equinix) (FCR), is named after Equinix Fabric, our software-defined network that automates private connections between network nodes hosted in our data centers (cloud providers, network carriers, ISPs, enterprises and others). Fabric and FCR both run on the same carrier-grade hardware routers, a deliberate architecture decision that we will return to after we cover a couple of others.

We wanted speed and flexibility in both the FCR user experience and our own process of building and improving that experience over time. We achieved both goals by decoupling the collection of microservices that comprise the user-facing product from low-level network configuration management, creating an abstraction layer for the microservices to interact with instead of interacting directly with the network infrastructure.

This way, the developer team working on the product doesn’t know (and doesn’t need to know) anything about what those hardcore low-level configurations in the carrier-grade Border Gateway Protocol (BGP) stack look like. The team can focus on the product without worrying about the effects of their decisions on functionality at the network level.

This also allowed us to decouple the process of requesting and configuring connections by the user from provisioning those connections, making the process faster and more flexible. The key to this is holding off on applying any configurations in the network until all the necessary details are gathered from the user. They order an FCR, choose what endpoints to connect it to, select connection bandwidth and redundancy and set their routing protocols. There is no waiting for any actions to take place at the network level after each of those steps. No events get sent and consumed unnecessarily, which avoids polluting our network with config messages that aren’t yet needed.

This is very different from the traditionally sluggish process for configuring network connections, where each config step has to materialize in the network before the next one can be taken.

## An Event-Driven Architecture
While the Java-based microservices that comprise the FCR product layer communicate with each other via REST APIs, the product layer communicates with the network abstraction layer using an asynchronous event-driven architecture. Services [publish events to Apache Kafka](https://thenewstack.io/beyond-the-quickstart-running-apache-kafka-as-a-service-on-kubernetes/), where other services find and consume events that are relevant to them. (Fabric microservices also use both REST APIs and Kafka events).

A microservice called Cloud Router Manager, for example, handles all operations around creating, updating and retrieving data about customer FCRs and their connections. Another microservice, called Connection Manager, handles connection requests, collecting information from downstream services that have more insight into the network. The Routing Protocol Manager stores users’ routing protocols in a database. This is just a handful of examples from the dozens of microservices that comprise the solution.

## No Extra Hardware, No VMs
Let’s return to the decision to run FCR on the same hardware routers that Fabric runs on. First, not having to deploy more hardware or virtual machines (the conventional but higher-latency way to host virtual network functions) is in itself a win. Plus, any new sites where Fabric is launched in the future can support FCR out of the gate.

A single FCR is a virtual routing function distributed across physical routers in multiple Equinix data centers within each metro where the service is available. Any endpoints are accessible via Fabric within a metro are accessible to any FCR created there. You can route traffic between the endpoints, which peer with your FCR, using Border Gateway Protocol (BGP).

The closest construct to FCR from the cloud world is the virtual private cloud. You can create a VPC in a cloud availability region that includes multiple subnets, each running in a separate availability zone (its own data center) in that region. You can create another VPC for a different set of workloads and have the two VPCs either completely isolated from each other or configured to connect and exchange data. Likewise, you can create multiple FCRs for different purposes.

One way an FCR is different from a VPC is it abstracts the individual data centers away from the user. They spin up an FCR within metro and choose an endpoint to connect (an Azure onramp, for example). A Layer 2 connection is then provisioned between Azure and Fabric using existing network-to-network interfaces (NNIs). At this point, the user can configure their Layer 3 connection to [Microsoft ](https://news.microsoft.com/?utm_content=inline+mention)Azure via BGP.

When the user wants to connect to another node in the metro (say, an [AWS](https://aws.amazon.com/?utm_content=inline+mention) onramp), they make all the necessary selections, and their configuration gets automatically distributed over our MPLS network to connect their FCR to wherever in the metro that onramp is hosted.

Because Fabric latency between data centers within a metro is very low – for example, the latency on FCR connections in Ashburn (our Washington, D.C. metro) to AWS and Azure in their respective US East cloud regions is less than 2 milliseconds – the physical location of the endpoints doesn’t affect performance.

We’ve only provided a few major highlights of FCR’s architecture here. We haven’t covered all the other microservices in the product layer or how we went about abstracting network configurations. We also haven’t touched on its other capabilities, like connecting [hybrid cloud environments](https://thenewstack.io/how-to-go-about-setting-up-a-hybrid-cloud-environment/), routing between metros or advanced BGP management tools like AS path perpending and MED attributes.

It’s been rewarding to get to think through what multicloud connectivity should look like from the perspective of a user who isn’t a networking expert but needs to build or maintain environments that straddle multiple platforms. If you’re curious about FCR, it’s [free to try for AWS customers](https://aws.amazon.com/marketplace/pp/prodview-l3kzqe5fdbqlw?trk=ce4ea0a3-61d4-484e-aac0-1e6f42b319f9&sc_channel=el&source=equinix).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)