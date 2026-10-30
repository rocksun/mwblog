A pod-level walkthrough of admission routing, dedicated scheduling, and network isolation, no worker nodes required

Serverless Kubernetes changes who manages the node, not what Kubernetes expects from it. Kubernetes expects a node to register with the control plane, report capacity, run a Kubelet, provide networking, and host workloads. AWS Fargate provides those behaviors without asking customers to create, patch, scale, or replace a [fleet of worker nodes](https://thenewstack.io/eks-zonal-shift-resilience/).

[Amazon Elastic Kubernetes Service](https://thenewstack.io/eks-kubernetes-upgrade-rollback/) (EKS) Fargate solves that problem by making the pod the unit of infrastructure. When a pod is selected for Fargate, EKS provisions a dedicated compute environment, boots the Kubernetes components it needs, gives the pod an Elastic Network Interface (ENI) in the customer’s virtual private cloud (VPC), and tears the environment down when the pod is gone.

> “Serverless Kubernetes changes who manages the node, not what Kubernetes expects from it.”

That customer experience depends on several coordinated design choices. Admission-time routing prevents the default scheduler from claiming a Fargate pod. A Fargate-specific scheduler provisions capacity instead of selecting from a pre-existing node pool. A focused runtime image supplies the Kubernetes node components, while separate network namespaces keep the platform path distinct from the workload path. An admission handler on the node limits workloads to patterns that fit a one-pod, one-environment model.

This article follows the components that make pod provisioning possible, from admission and scheduling through the node runtime and networking.

![Diagram illustrating how EKS Fargate works](https://cdn.thenewstack.io/media/2026/10/a71f1ab0-image1-1024x489.png)

*Figure 1. The diagram shows how EKS routes the pod before scheduling, requests dedicated capacity, and starts the Kubernetes runtime that validates and runs the pod.*

## Routing a pod before scheduling

An EKS cluster can use nodes from Amazon Elastic Compute Cloud (Amazon EC2) and Fargate at the same time. Placement therefore needs to be explicit before the ordinary scheduling flow begins.

EKS provides a Fargate profile, an AWS resource that indicates which pods run on Fargate. A profile expresses that intent by selecting a namespace and, optionally, pod labels. It also specifies the private subnet and security group used for the pod’s Elastic Network Interface, so placement and network access are chosen together.

For clusters with Fargate enabled, AWS manages and operates an admission webhook as part of the Kubernetes control plane. When a pod matches a profile, the mutating webhook adds the matching profile’s name to the pod’s label. It also sets the pod’s scheduler name to the Fargate scheduler, so the pod follows the Fargate scheduling path. This decision happens before the pod object is persisted in the Kubernetes database (etcd) and before the default scheduler can claim it.

A profile also specifies the pod execution role, an AWS Identity and Access Management (IAM) role used by the Fargate infrastructure to register its kubelet and pull images from Amazon Elastic Container Registry (Amazon ECR). That role is distinct from the application identity containers use. Because this is a serverless infrastructure, EC2 instance metadata is not available to Fargate pods, so applications that call AWS services should use IAM roles for service accounts.

### Provisioning a node for the pod

The Fargate scheduler is a dedicated scheduler that runs on the Kubernetes control plane. It requests new capacity for a pod based on the pod’s resource requirements and its matching Fargate profile, rather than searching a pool of existing nodes.

> “The Fargate scheduler is a dedicated scheduler that runs on the Kubernetes control plane. It requests new capacity for a pod rather than searching a pool of existing nodes.”

Once capacity is requested, the scheduler tentatively associates the pod with a nominated node. This prevents a retry or resync from provisioning a second environment for the same pod. The Fargate runtime registers the Kubernetes Node object when the environment is ready, and the scheduler performs the final bind after the node reports ready. The runtime then starts the pod and reports its status through the API server.

When the pod terminates, the runtime removes the node and releases its capacity. If provisioning or binding fails, reconciliation clears the tentative assignment and reclaims the capacity before retrying.

## One pod, one network interface

Fargate connects each pod to the customer’s VPC through its ENI. The Fargate profile defines the private subnet and security group used for that interface. Security-group rules and VPC routing therefore apply to the pod’s ENI rather than to a shared customer-managed worker node.

An ENI gives the pod a first-class place in the VPC. VPC flow logs can identify the interface, and security-group rules can express the intended workload boundary.

The network path has to serve two audiences at once. The Fargate platform needs a path for managed telemetry, credentials, and provisioning. Kubernetes components need a path to the API server, and the customer pod needs a path to the VPC. Fargate keeps these paths connected where Kubernetes requires them while separating platform traffic from workload traffic.

![Diagram illustrating EKS Fargate's pod execution environment.](https://cdn.thenewstack.io/media/2026/10/ce6eb4f2-image2-1024x509.png)

*Figure 2. The execution environment separates platform, Kubernetes components, and pod network namespaces, while the customer ENI carries the Kubernetes and VPC-facing paths.*

Fargate provisions three logical Linux network namespaces. The platform namespace carries the Fargate platform services, including telemetry, credential vending, and provisioning. The node namespace carries the Kubernetes core data-plane components and customer ENI. The workload namespace runs the customer workload. The underlying Fargate implementation can change, but this separation keeps the managed platform, Kubernetes node components, and workload on distinct paths.

The customer ENI is moved into the node namespace, where it provides the path for Kubernetes control-plane communication and pod traffic. The task metadata endpoint is reachable from the node namespace, allowing the node runtime’s AWS authentication path to obtain the credentials needed to register the node with the API server, while access from the workload namespace is blocked. A bridge and virtual Ethernet (veth) pair created by the [Container Network Interface](https://thenewstack.io/cloud-native-networking-as-kubernetes-starts-its-second-decade/) (CNI) connect the node namespace to the workload namespace. The node namespace handles traffic destined for Kubernetes management endpoints; all other traffic is delivered to the workload namespace and exits through the customer ENI. Filtering prevents the pod from reaching platform metadata and management processes.

## The runtime image is a Kubernetes node in miniature

The runtime image matches the Kubernetes control-plane version, so the kubelet and its supporting components remain compatible. It provides the kubelet and Kubernetes node components needed to register the node, receive pod specifications, start and restart containers, run probes, report status, and serve operations such as logs and exec.

During kubelet startup validation, the default scheduler can place a pod before the Fargate kubelet completes initialization. EKS runs a custom PodAdmitHandler that validates a pod before it starts and admits only a pod intended for the Fargate scheduling path. This protects the one-pod-per-node model when another pod is observed while the kubelet is coming up and provides a second validation boundary after API-server admission.

The managed kubelet does not need every capability available on a general-purpose node. Kubernetes provides controls to disable the logs, profiling, and debug-flags handlers, and EKS uses them to keep the runtime surface limited to the operations the service needs. We contributed some of these controls upstream through changes that disable the logs handler and changes that disable profiling and debug flags.

## Fargate patching and considerations

Fargate’s managed runtime is maintained continuously, and EKS periodically replaces Fargate pods so they receive the latest available security patch without customer-managed node operations. When a Fargate environment needs patching, EKS identifies the affected pod, notifies the customer, and uses the Kubernetes Eviction API to gracefully remove the pod before recycling the environment. For controller-managed workloads, this gives a replacement pod an opportunity to become ready before the old environment is retired.

A customer’s PodDisruptionBudget controls how much application capacity can be unavailable during that process. EKS respects the budget when it requests eviction and retries when eviction would violate it. The budget must leave room for planned disruption; if eviction still cannot succeed by the scheduled termination time, EKS can eventually delete the pod so it can create the patched environment. Replicas and readiness probes determine whether the application continues serving traffic.

Customers must design around this independent pod lifecycle. Every pod must match a Fargate profile.

Customers should plan ENI and subnet capacity accordingly. A design that works on EC2 because many pods share a node’s interface must account for one ENI per Fargate pod. Fargate profiles use private subnets, and Fargate pods are not assigned public IP addresses. Internet or AWS-service access normally uses the private subnet’s network address translation (NAT) gateway or VPC endpoint design. Because the customer ENI carries both Kubernetes data-plane and pod traffic, its security group must allow the Kubernetes management traffic needed for operations such as kubectl logs and kubectl exec.

## A workload contract that fits the model

Most Kubernetes application workloads fit naturally on Fargate, including Deployments, Jobs, and multi-tenant applications whose isolation boundary is the pod. Workloads that require node-level control, such as DaemonSets, host networking, host ports, privileged operations, or GPUs, fall outside the Fargate pod contract and require an execution model that provides node-level access.

Storage follows the same boundary. HostPath and host-attached block storage depend on a persistent node, and Amazon Elastic Block Store (Amazon EBS) cannot be mounted to Fargate pods. For durable shared file storage, Amazon Elastic File System (Amazon EFS) is the supported pattern. For supported Kubernetes features, read the current [EKS Fargate documentation](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html).

> “Making Kubernetes serverless required more than hiding the worker node. EKS had to preserve Kubernetes behaviors while changing the underlying lifecycle.”

Making Kubernetes serverless required more than hiding the worker node. EKS had to preserve Kubernetes behaviors while changing the underlying lifecycle. Admission establishes placement intent before schedulers compete. A scheduler provisions capacity and waits for a node to prove readiness. Runtime components supply the node contract, while node-level admission protects the pod boundary. VPC networking gives each pod a direct, controllable identity, while namespace and VM boundaries keep the managed platform separate from the workload.

These decisions are mostly invisible when they work. A deployment selects a profile, a pod starts with the expected VPC access, logs and exec behave like Kubernetes operations, and the underlying environment disappears when the workload is gone.

That invisibility is the point of the service. Customers can use familiar Kubernetes objects and workflows while EKS and Fargate absorb the work of provisioning, isolation, node lifecycle, and runtime maintenance. The infrastructure is managed, but the contract remains Kubernetes: a pod is admitted, scheduled, connected, and observed as a first-class workload.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/7f8a61d7-srisaranbalaji-600x600.png)

Sri Saran Balaji Vellore Rajakumar is a Principal Engineer at Amazon Web Services and a founding engineer of Amazon EKS, where he has spent nearly a decade building the infrastructure that keeps the EKS control plane available and performant at...

Read more from Sri Saran Balaji Vellore Rajakumar](https://thenewstack.io/author/sri-saran-balaji-vellore-rajakumar/)