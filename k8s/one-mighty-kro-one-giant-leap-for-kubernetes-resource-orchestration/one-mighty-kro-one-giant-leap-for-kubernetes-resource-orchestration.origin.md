# One Mighty kro; One Giant Leap for Kubernetes Resource Orchestration
![Featued image for: One Mighty kro; One Giant Leap for Kubernetes Resource Orchestration](https://cdn.thenewstack.io/media/2025/03/f0c11558-kro-kubernetes-giant-leap-moon-1024x576.jpg)
[kro](https://kro.run) — which we spell lowercase like a Linux command-line tool and pronounce “crow” like the bird — extends [Kubernetes core capabilities](https://roadmap.sh/kubernetes) to simplify the management of interdependent Kubernetes resources. [AWS](https://aws.amazon.com/?utm_content=inline+mention) open sourced kro at KubeCon North America in November 2024.
Just two months later, kro packed its bytes and moved to a vendor-neutral home as [Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention) (GCP) and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure joined the project. This cloud native collaboration made kro the first open source project where these three major cloud providers [have come together from the beginning](https://thenewstack.io/kubernetes-gets-a-new-resource-orchestrator-in-the-form-of-kro/).

**Why kro?**
Kubernetes has been extensible since version 1.16, when Custom Resource Definitions (CRDs) graduated to general availability (GA). While you can write any custom controller — including whimsical ones like ordering pizza — teams often develop controllers for practical needs: creating Kubernetes resources in a certain order, passing values between resources and performing logical operations. Developing such controllers from scratch can be complex and time-consuming, requiring deep expertise in both coding and Kubernetes internals.

This is where kro comes in. kro simplifies this process by providing a configuration-based framework that eliminates the need for custom code. Instead of each organization building its own controllers, kro offers a standardized, yet flexible approach that enables solution sharing across the community. Its intuitive design, powered by Simple Schema, [Common Expression Language (CEL](https://kubernetes.io/docs/reference/using-api/cel/)) and robust dependency management, makes complex resource [orchestration accessible](https://thenewstack.io/orchestrate-cloud-native-workloads-with-kro-and-kubernetes/) through simple configuration.

**What Features Make kro Simple to Use?**
**Simple schema:** kro provides a straightforward and human-friendly way to define a new CRD spec. Under the hood, kro uses the Simple Schema definition to automatically generate the OpenAPIv3 schema and create the Kubernetes CRD. This is a significant improvement because Simple Schema is much easier to read and write compared to OpenAPIv3 schemas.
**CEL-based expressions:** kro incorporates CEL for defining logical operations — the same expression language Kubernetes uses for webhooks — due to its simplicity and safety features, such as [runtime cost budgeting](https://kubernetes.io/docs/reference/using-api/cel/#runtime-cost-budget) and [type checking](https://kubernetes.io/docs/reference/using-api/cel/#type-checking). With CEL, you can clearly and concisely express conditions and dependencies and pass values from one resource to another.
**Dependency management: **kro automatically constructs a directed acyclic graph (DAG) for orchestrated resources based on specified CEL expressions. This DAG determines the exact order in which resources are created and deleted.
These features make kro highly intuitive, easy to adapt and a natural fit for those familiar with [Infrastructure as Code (IaC) tools](https://thenewstack.io/introduction-to-infrastructure-as-code/).

**How Does kro Help Manage Cloud Resources?**
kro works with *any* Kubernetes resource and can be installed on *any* Kubernetes cluster. kro interacts *exclusively* with the Kubernetes API, meaning it doesn’t directly interact with any external APIs. Instead, it manages and orchestrates any resources your cluster supports. For example, if Prometheus Operator is installed, you can use kro to package a Prometheus ServiceMonitor with your application.

Similarly, to provision cloud resources, your cluster must include tools that communicate with cloud provider APIs, such as [AWS Controllers for Kubernetes (ACK)](https://aws-controllers-k8s.github.io/community/), [GCP’s Kubernetes Config Connector (KCC)](https://github.com/GoogleCloudPlatform/k8s-config-connector) or [Azure Service Operator (ASO)](https://github.com/Azure/azure-service-operator). Using a **ResourceGroupDefinition (RGD) **— a core kro concept for grouping related resources — you can package applications, their cloud resource dependencies, required permissions and other necessary Kubernetes custom resources into a single, deployable unit.

![kro workflow](https://cdn.thenewstack.io/media/2025/03/d69459b0-kro-architecture.png)
kro workflow


**kro Can Turn Kubernetes Into a Centralized Cloud Platform**
Organizations often struggle to manage multiple fragmented platforms, where each team relies on multiple disjointed tools to manage things like infrastructure, applications and databases. Developers deploying applications to Kubernetes must switch between multiple interfaces — one to deploy to Kubernetes, another to request cloud infrastructure resources, configure databases and provision block storage. Meanwhile, platform teams — typically consisting of networking, database and infrastructure teams — each maintain their own IaC pipelines.

These pipelines lack a standard way to fit together; the output of one often doesn’t seamlessly integrate into another. Worse, they don’t easily connect with the tools used to deploy add-ons to Kubernetes, creating further inefficiencies. The data platform team builds their separate tools, often with overlapping functionality but rarely integrated.

Kubernetes adoption has demonstrated its capability to serve as a backbone for centralized platform operations. kro extends Kubernetes foundation capabilities by providing specific mechanisms for standardizing resource management across development, platform and data platform teams. Through its configuration-based approach to defining custom APIs, kro enables organizations to create standardized, reusable components that provide the following benefits:

**Increased developer velocity:** Platform teams can package applications and their cloud resource dependencies into a deployable unit, embedding organizational best practices and ensuring implicit central governance. This abstraction reduces complexity, allowing developers to focus on delivering features rather than troubleshooting infrastructure pipelines.
**Improved fleet management:** kro simplifies creation of new clusters, enabling your business to expand to new regions, scale capacity on demand and spin up isolated environments for specific workloads. By packaging all necessary Kubernetes resources in an RGD and building the DAG, kro ensures proper creation order. It also enables platform operators to apply changes across the entire fleet, making it easy to update components for compliance requirements.
**Simplified data and MLOps infrastructure management:** Data platform engineers can package all necessary components into kro RGDs, including cloud resources like GPU nodes, networking and storage, along with Kubernetes objects such as StorageClasses, PersistentVolumeClaims, Services and Ingress. This streamlines the deployment process, making it easy for data scientists to run models without worrying about infrastructure setup. For instance, [this LLM example](https://github.com/kro-run/kro/tree/main/examples/aws/llm) demonstrates how to define and orchestrate the required infrastructure using kro.
With kro, Kubernetes can become the platform layer, bringing consistency to how applications, infrastructure and cloud resources are managed uniformly.

**Conclusion**
The launch of kro marks a milestone in cloud native computing, uniting AWS, GCP and Azure to tackle Kubernetes resource management. This collaboration sets the stage for cross-cloud standardization, benefiting the entire ecosystem.

Join this transformative journey: explore [kro](https://kro.run/) in your development environment, connect with our [GitHub](https://github.com/kro-run/kro) community, and contribute via issues or pull requests. Whether building platforms, applications or managing data and machine learning operations, your contributions can shape the future of Kubernetes resource orchestration and advance accessible, standardized and efficient [cloud native development](https://thenewstack.io/cloud-native/).

*To learn more about Kubernetes and the cloud native ecosystem, join us at KubeCon + CloudNativeCon Europe in London on April 1-4. *If you are attending KubeCon EU 2025, meet with us at the AWS Booth
**S300 to see demos on kro.**
*Islam Mahgoub, Senior Solutions Architect, AWS, also contributed to this article.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)