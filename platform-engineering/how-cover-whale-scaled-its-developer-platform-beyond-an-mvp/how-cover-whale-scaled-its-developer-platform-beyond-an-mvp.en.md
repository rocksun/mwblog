Platform engineering is gaining traction across industries as organizations grapple with the complexity of cloud native development. Teams want to streamline provisioning, deployment and observability while reducing the burden on application developers. Yet many find that moving beyond a minimum viable platform (MVP) requires a shift in approach.

This case study explores how [Cover Whale](https://www.coverwhale.com/), a U.S.-based firm specializing in truck insurance, built its [internal developer platform (IDP)](https://thenewstack.io/how-do-the-internal-developer-platform-and-portal-connect/) on [Kubernetes](https://thenewstack.io/kubernetes-an-overview/) and [AWS](https://aws.amazon.com/?utm_content=inline+mention), the challenges it faced when scaling beyond an MVP and the lessons learned along the way. From managing sprawling Helm charts to integrating systems like NATS, the journey illustrates the trade-offs many enterprises encounter when growing their platform.

The story also highlights where platform orchestration tools like [Kratix](https://www.kratix.io/) provided a middle ground between writing custom operators and stitching together scripts, and what that meant for long-term maintainability.

## The Platform Engineering Initiative

Recently, Cover Whale initiated a new insurance platform to improve its customer experience. To streamline the application life cycle of the new platform, an IDP has been implemented to handle provisioning, build, test, deployment and observability of each new [microservice](https://thenewstack.io/introduction-to-microservices/) workload.

The IDP is built on top of AWS Elastic Kubernetes Service (EKS), which runs a platform Kubernetes cluster controlling a fleet of workload Kubernetes clusters.

All the clusters and underlying infrastructure are provisioned by OpenTofu and Terramate, and are bootstrapped by [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) using the App of Apps pattern.

Cluster bootstrapping is performed by initializing the cluster with shared tooling, such as Karpenter, external-dns, external-secret operator and an ingress controller. Then, it deploys an `Application` for each system within the IDP, which in turn, deploys another `Application` for each workload inside that system. This entire choreography is encapsulated in a series of Helm charts loaded by Argo CD into the clusters.

## Challenges Encountered

The setup allowed for the quick and efficient development of a minimum viable product.

Deploying and maintaining the entire hierarchy of workloads while eliminating the complexity of creating Kubernetes manifests and build pipelines was a game-changer that proved the initiative’s value to both developers and management.

Nevertheless, going beyond an MVP required us to reconsider our approach for several reasons, which we will detail below.

### Scalability

Argo CD doesn’t offer much choice for generating Kubernetes manifests. As a result, we used Helm charts … a lot of them. To make matters worse, the Helm structure followed the IDP structure of systems and workloads, and had separate charts for what got deployed in the platform cluster or workload cluster.

A consequence of that is that resources for a specific concern would be spread across several Helm charts. As the IDP grew, this led to a very complex codebase with related logic spread across several charts.

For example, the `external-secret` integration was scattered across three different Helm charts.

As a result, gearing up toward a more scalable setup required a paradigm shift.

### Limited Integration With Non-Kubernetes Resources

The MVP relied on a few interactions with non-Kubernetes resources. For example, we generate Elastic Container Registry (ECR) repositories and related identity and access management (IAM) roles using [AWS Controllers for Kubernetes](https://aws-controllers-k8s.github.io/community/).

However, since our workloads rely on the messaging system NATS and Synadia Cloud, dynamically generating NATS users was more than desirable, and there isn’t an operator to do so. We could have used Helm hooks, but that felt unreliable, and writing a full-blown operator seemed a larger undertaking than we would have liked at that time.

### Backend-Frontend Integration

We used [Port.io](https://www.port.io/?utm_content=inline+mention) as a developer portal to present a consistent frontend for developers and enhance our developer experience (DX). The portal provided an overview of deployed workloads, self-service actions that developers could use to manage their workloads and links to observability tools and git repositories.

To accurately represent our systems and workload structure in the portal, we relied on labels and annotations to the Argo CD Applications and ApplicationSet representing the systems. Although functional, this setup was somewhat messy.

For example, a system consists of several Applications and an ApplicationSet. This led to some confusion when we had to add information on the frontend regarding where the labels/annotations needed to be added.

Ideally, we would have liked to have a custom resource definition (CRD) representation of the IDP structure that Port.io could read unequivocally. However, maintaining those CRDs solely for that purpose felt overrated.

On the other hand, using those CRDs to drive the IDP and reduce our reliance on Helm charts made a whole lot of sense!

## Introducing Kratix Into Our IDP

[Kratix](https://www.kratix.io/) offered a nice middle ground between writing our own operator and hooking up some scripts to solve the issues mentioned above.

Kratix monitors the state of our resources and allows for periodic reconciliations, sparing us from having a dedicated workload to watch the kube-apiserver, while enabling us to manage the entire life cycle of our resources.

Using the promises approach, we could also gather specific concerns together without worrying about the IDP hierarchy.

### The Proof of Concept

During the development of the new platform, we had to aggregate APIs from multiple services and expose them externally in a consistent manner, thus creating a nice abstraction layer between external and internal services. This included APIs from both the legacy and new customer portals, as well as webhooks for various external services.

We decided to add support for this in our workload manifest, enabling developers to manage their APIs in a distributed manner and have the IDP aggregate all APIs under a single domain name.

To do so, we created two [Kratix promises](https://docs.kratix.io/main/guides/writing-a-promise):

* ApiAggregator, which would declare the hostname to which the APIs are exposed.
* ApiAggregatorTarget, which attaches to an ApiAggregator and defines a list of paths and the target service to which requests should be sent.

Behind the scenes, Kratix would create all the Gateway API resources to let the magic happen.

We used [ytt](https://carvel.dev/ytt/) to generate the manifests inside our promise pipeline, which made the YAML templating process easier and avoided all [YAML quirks](https://hitchdev.com/strictyaml/why/implicit-typing-removed/) to guarantee a valid YAML object as a result.

Argo CD being already in the map, deploying Kratix was fairly easy. We just created a dedicated state store git repository and added workload clusters as a Destination as part of the cluster bootstrapping process.

In no time, we had a working proof of concept, and after a minor fix to support larger request body sizes, we quickly felt comfortable releasing it into production.

### Declarative NATS Support

Following this proof of concept, we decided to use Kratix’s full setup to eliminate the need for manual management of NATS users and credentials.

The task was a bit more complex, as the promise would have to interact with a SaaS platform to generate users, but also safely store their credentials.

We started by developing a script to manage the life cycle of the NATS users in Synadia Cloud and generate credentials. To simplify interaction with the API, we used [restish](https://rest.sh) instead of raw curl commands.

Integrating the script with the Kratix promise and managing the resource status to track the NATS user ID and credentials expirations was relatively straightforward. We ensured that the concerns for saving and loading the state, creating and deleting users, and credentials were clearly separated.

Nevertheless, manipulating the credentials was the real challenge. The reason is that Kubernetes manifests are stored in a git repository, and storing raw secrets was a clear no-no.

### Manipulating Secrets With Kratix

After exploring multiple options, we settled on using Sealed Secret. This tool uses an asymmetric encryption algorithm to encrypt the secret using a public key known to the platform cluster and decrypt it using a private key known only to the workload cluster.

This setup worked smoothly — for a few hours! We quickly noticed that our workloads had frequent restarts.

Kratix expects your promise to be idempotent. Effectively, after a few hours, Kratix runs a reconciliation job. In our case, this reconciliation run created a new NATS authentication token, which updated the existing authentication secret, triggering a rolling update of the workload.

To make matters worse, we can’t decrypt the existing secret or retrieve it from the Synadia cloud. Additionally, not emitting the sealed secret resource would result in the deletion of the secret from the workload cluster.

To work around this issue, we added the `sealedsecrets.bitnami.com/patch` annotation and generated an empty sealed secret to prevent secret deletion.

## Conclusion

Cover Whale’s journey reflects a challenge that many enterprises face: building an IDP that can grow from proof of concept to a sustainable, scalable platform. An MVP often demonstrates immediate value, but scaling requires rethinking patterns around Helm, CRDs and secret management.

The team found that adopting a “promise”-based approach with Kratix offered a pragmatic path forward. However, the broader lesson is that enterprises should be prepared to evolve their architecture as new requirements emerge. Key takeaways for other teams include:

* Be wary of Helm sprawl; a CRD-driven approach may provide clearer boundaries and reduce complexity.
* When integrating with SaaS systems, plan for life cycle management and idempotency early.
* Secrets management remains a thorny area; reconciliation and rotation strategies must be tested under real conditions.

By reframing the IDP around these lessons, Cover Whale created a more consistent and maintainable platform foundation, one that continues to evolve as developer needs grow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/45881940-cropped-6a97b015-laurentsibilla-600x600.jpeg)

Laurent Sibilla is a freelance platform engineering consultant passionate about DevOps and automation. He actively promotes DevOps best practices and implements internal developer platforms as a foundation for building high-quality software while ensuring high security and reliability standards.

Read more from Laurent Sibilla](https://thenewstack.io/author/laurent-sibilla/)