It’s exciting to see how thriving and dynamic the Cloud Native industry is nowadays. CNCF Sandbox greatly helps it, serving as a unique place for Open Source projects to start or continue their journey in the ecosystem. At the same time, so many things are emerging there that it’s a bit overwhelming to stay on top of.

Hence, we’d like to start this series of articles that will introduce the projects recently added to the CNCF Sandbox. Our first batch will cover 13 projects accepted to Sandbox in the first half of 2023 — on March 8th, May 17th, and June 22nd. We’ll list them by their formal categories, starting from the most popular ones.

We will accompany all projects’ descriptions with additional information and links, including their original authors and GitHub issues for the sandbox submissions and onboarding process. This will help you dive deeper into the project’s path and the formal process of joining CNCF.

## Observability
### 1. Inspektor Gadget
[Website](https://inspektor-gadget.io/);[GitHub](https://github.com/inspektor-gadget/inspektor-gadget)- 2100+ GH stars, ~50 contributors
- Initial commit: Mar 3, 2019
- License: Apache 2.0
- Original owner/creator: Kinvolk (acquired by Microsoft in 2021)
- Languages: C, Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/7);[onboarding issue](https://github.com/cncf/toc/issues/1021);[DevStats](https://inspektorgadget.devstats.cncf.io/)
Inspektor Gadget is a collection of eBPF-based tools (called “gadgets”) for debugging applications and resources in Kubernetes.

These gadgets package, deploy and execute eBPF programs, including those based on [BCC](https://github.com/iovisor/bcc) tools, within the cluster. They also automatically map low-level kernel primitives to high-level Kubernetes resources, simplifying and speeding up essential information retrieval.

Inspektor Gadget operates on each K8s node as a *DaemonSet*. It leverages eBPF programs embedded in the kernel to monitor events related to system calls from userspace programs in Pods. The eBPF programs run within the kernel to gather log data, which Inspektor Gadget’s userspace tools then retrieve and display.

Here are some examples of built-in gadgets:

[advise network-policy](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/advise/network-policy)monitors network activity in the namespaces and summarizes the TCP and UDP traffic information in a file, which can be used to generate Kubernetes network policies;[advise seccomp-profile](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/advise/seccomp-profile)watches the system calls executed in the selected Pod and creates appropriate seccomp profiles based on that;[profile block-](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/profile/block-io)[io](https://github.com/inspektor-gadget/inspektor-gadget/blob/main/docs/builtin-gadgets/profile/block-io.md)collects information on disk input/output usage and creates an I/O latency distribution histogram;[profile cpu](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/profile/cpu)analyzes CPU performance by sampling stack traces;[top tcp](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/top/tcp)visualizes ongoing TCP activity;[trace dns](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/dns)outputs the DNS queries and responses for selected Pods;[trace exec](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/exec)shows how new processes are created;[trace fsslower](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/fsslower)identifies and shows slow-performing file operations;[trace oomkill](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/trace/oomkill)monitors the OOM (out-of-memory) killer actions;[trace ssl](https://www.inspektor-gadget.io/docs/latest/gadgets/trace_ssl)logs the OpenSSL functions usage;[traceloop](https://www.inspektor-gadget.io/docs/latest/gadgets/builtin/traceloop)logs system calls performed in the containers.
The full list of gadgets is available in the [documentation](https://www.inspektor-gadget.io/docs/latest/gadgets/) and [Artifacts Hub](https://artifacthub.io/packages/search?kind=22).

Once Inspektor Gadget is installed in the cluster, you can list all its components using the following command:

```
$ kubectl gadget --help
Collection of gadgets for Kubernetes developers
Usage:
kubectl-gadget [command]
Available Commands:
advise Recommend system configurations based on collected information
audit Audit a subsystem
completion Generate the autocompletion script for the specified shell
deploy Deploy Inspektor Gadget on the cluster
help Help about any command
profile Profile different subsystems
prometheus Expose metrics using prometheus
run Run a gadget (experimental)
script Run a bpftrace-compatible scripts
snapshot Take a snapshot of a subsystem and print it
sync Synchronize gadget information with server
top Gather, sort and periodically report events according to a given criteria
trace Trace and print system events
traceloop Get strace-like logs of a container from the past
undeploy Undeploy Inspektor Gadget from cluster
version Show version
…
```
The project’s README provides a [nice list](https://github.com/inspektor-gadget/inspektor-gadget#talks) of talks where you can learn about the practical usage of Inspektor Gadget and other eBPF-related technologies.

### 2. Headlamp
[Website](https://headlamp.dev/);[GitHub](https://github.com/headlamp-k8s/headlamp)- ~2000 GH stars, ~60 contributors
- Initial commit: Dec 19, 2019
- License: Apache 2.0
- Original owner/creator: Kinvolk (acquired by Microsoft in 2021)
- Languages: TypeScript (React), Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/25);[onboarding issue](https://github.com/cncf/toc/issues/1056);[DevStats](https://headlamp.devstats.cncf.io/)
Headlamp is a powerful Kubernetes user interface. You can run it as a local desktop app or deploy it in your Kubernetes cluster and access it via a web browser.

Headlamp lets you see your K8s clusters’ overall state and resource usage, scroll through your K8s resources and modify their manifests, view the logs, and exec to the containers.

![](https://blog.palark.com/wp-content/uploads/2024/08/headlamp-workloads-list-1024x617.png)
From a security point of view, it respects RBAC user roles to prevent unauthorized actions. It also allows you to undo modifying operations.

Headlamp offers a robust plugin system to extend and customize its features. Official plugins are available in [this repo](https://github.com/headlamp-k8s/plugins). Currently, there are three of them: *app-catalog* for managing Helm charts, *prometheus* for detailed information about your workloads, and *kompose* for the tool converting your `docker-compose`
manifests. Artifact Hub also hosts a [plugin for OpenCost](https://artifacthub.io/packages/headlamp/headlamp-plugins/headlamp_opencost).

### 3. Kepler
[Website](https://sustainable-computing.io/);[GitHub](https://github.com/sustainable-computing-io/kepler)- ~1100 GH stars, 50+ contributors
- Initial commit: Feb 2, 2022
- License: Apache 2.0
- Original owner/creator: Red Hat
- Languages: Go, C
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/19);[onboarding issue](https://github.com/cncf/toc/issues/1054);[DevStats](https://kepler.devstats.cncf.io/)
Kepler (**K**ubernetes-based **E**fficient **P**ower **L**evel **E**xporte**r**) is a Prometheus exporter that leverages eBPF to probe system stats related to energy consumption, such as CPU performance counters. It collects data and statistics from *cgroupfs* and *sysfs* and uses ML (machine learning) models to estimate energy consumed by Kubernetes.

Kepler exports all these metrics for your Kubernetes Pods and nodes to Prometheus. They include:

`kepler_container_joules_total`
— total energy consumption of the CPU, DRAM, GPUs, and other host components for a specific container;`kepler_container_core_joules_total`
and`kepler_container_gpu_joules_total`
— total energy consumption of CPU cores/GPUs for a container;`kepler_container_cpu_cycles_total`
— CPU cycles used by the container via hardware counters;`kepler_node_core_joules_total`
— the same as for the relevant container metrics, but aggregated for all containers on the node;- and much more.
You can find the full list of metrics exposed by Kepler in the [documentation](https://sustainable-computing.io/design/metrics/#kepler-metrics-overview).

Here is an excellent diagram of how Kepler works:

![](https://blog.palark.com/wp-content/uploads/2024/08/kepler-architecture-1024x505.png)
You can install Kepler in your cluster using its [Helm chart](https://github.com/sustainable-computing-io/kepler-helm-chart) or [Kubernetes operator](https://github.com/sustainable-computing-io/kepler-operator). When it’s done, you can leverage the pre-generated Kepler Dashboard to visualize your energy-related Kubernetes metrics in Grafana.

## Security & Compliance
### 4. SlimToolkit
[Website](https://slimtoolkit.org/);[GitHub](https://github.com/slimtoolkit/slim)- 19000+ GH stars, 60+ contributors
- Initial commit: Sep 10, 2015
- License: Apache 2.0
- Original owner/creator: Kyle “kcq” Quest
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/22);[onboarding issue](https://github.com/cncf/toc/issues/1055);[DevStats](https://slimtoolkit.devstats.cncf.io/)
SlimToolkit (originally known as *DockerSlim*) is your go-to tool for optimizing as well as exploring and debugging containers. It streamlines the way containers are created, customized, and used, rendering them smaller, more secure, and more efficient.

SlimToolkit works seamlessly with Elixir, Go, Java, Node.js, PHP, Python, Ruby, and Rust applications on Alpine, CentOS, Debian, Ubuntu, and even distroless containers. As its name suggests, the original idea was to make containers slim. To achieve this, several actions are performed in a fully automated fashion:

![](https://blog.palark.com/wp-content/uploads/2024/08/slimtoolkit-workflow.jpg)
Processing containers this way results in reducing Node.js app images by 30x (for `ubuntu:14.04`
) and 16x (for `debian:jessie`
) times. The promised reduction for Go apps is even more impressive since a 700 MB image based on `golang:latest`
can become as small as 1.5 MB(!) only. The project features a specific [examples](https://github.com/slimtoolkit/examples) repo where you can find various applications and how SlimToolkit reduced their images’ size.

Since it’s a *toolkit*, `slim`
comes with numerous commands you can perform against your containers, such as:

`xray`
— static analysis for the image;`lint`
— analyzing container instructions in Dockerfiles;`vulnerability`
— vulnerability-related actions based on the EPSS (Exploit Prediction Scoring System) information;`registry`
— registry-related operations;- and more.
SlimToolkit also features an interactive mode that provides hints for each command or flag as well as ready-to-use integrations with CI/CD (based on Jenkins or GitHub Actions).

### 5. SOPS
[Website](https://getsops.io/);[GitHub](https://github.com/getsops/sops)- 16000+ GH stars, 140+ contributors
- Initial commit: Aug 14, 2015
- License: MPL 2.0
- Original owner/creator: Mozilla
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/28);[onboarding issue](https://github.com/cncf/toc/issues/1057);[DevStats](https://sops.devstats.cncf.io/)
SOPS (**S**ecrets **OP**eration**S**) is a well-known editor for encrypted files, originally created by Mozilla in 2015. It helps you automate encrypting secrets and infrastructure credentials and their distribution. It supports numerous formats (YAML, JSON, ENV, INI, and binaries) and performs encryption with Hashicorp Vault, AWS KMS, GCP KMS, Azure Key Vault, `age`
, and PGP.

It is also capable of key rotation and numerous features for various use cases, such as:

- writing secrets to stdout, files on disk, environment of a child process, and temporary files;
- key groups — multiple master keys to decrypt files;
- key service — forwarding a socket to access encryption keys on a remote machine;
- generating audit logs for analyzing all activity on encrypted files.
SOPS integrates seamlessly with Git, allowing you to decrypt files while comparing their different versions. This is particularly useful for reviewing changes or visualizing history.

By the way, there is a well-known [helm-secrets](https://github.com/jkroepke/helm-secrets) plugin for Helm that allows you to use SOPS to encrypt Helm value files and store them in Git.

## Scheduling & Orchestration
### 6. Clusternet
[Website](https://clusternet.io/);[GitHub](https://github.com/clusternet/clusternet)- 1300+ GH stars, ~50 contributors
- Initial commit: Jun 10, 2021
- License: Apache 2
- Original owner/creator: Tencent
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/10);[onboarding issue](https://github.com/cncf/toc/issues/1022);[DevStats](https://clusternet.devstats.cncf.io/)
Clusternet simplifies the access to and management of many Kubernetes clusters, offering a unified approach across various environments: on-prem, public or private clouds, hybrid clouds, and edge.

When Clusternet is deployed, it allows you to perform various actions on your Kubernetes clusters (e.g., listing/creating/deleting resources, making a port forward, etc.) via simple `kubectl`
commands and deploying applications across them. It can automatically discover, register, and label new clusters.

Technically, Clusternet extends Kubernetes with a set of components (hub, scheduler, and controller manager) for the parent cluster and agents in the child clusters. These child clusters are managed through requests to the parent cluster’s API server, creating a seamless process for operators.

![](https://blog.palark.com/wp-content/uploads/2024/08/clusternet-architecture-1024x568.png)
The project has a [quick start](https://clusternet.io/docs/quick-start/) for setting up Clusternet locally (using `kind`
), which can be followed by other tutorials guiding you through deploying applications to multiple K8s clusters.

### 7. Eraser
[Website](https://eraser-dev.github.io/eraser/docs/);[GitHub](https://github.com/eraser-dev/eraser)- ~500 GH stars, 30+ contributors
- Initial commit: Jun 1, 2021
- License: Apache 2
- Original owner/creator: Microsoft (Azure)
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/24);[onboarding issue](https://github.com/cncf/toc/issues/1092);[DevStats](https://eraser.devstats.cncf.io/)
Eraser has a simple mission — to prevent Kubernetes nodes’ disks from becoming cluttered by deleting unused and vulnerable images from all cluster nodes.

While Kubernetes has its own [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images) mechanism, Eraser gives you more options to select the images to be removed, including their vulnerability state. *(If you also wonder why it shouldn’t be a part of Kubernetes, you can find an answer here.)*

By default, Eraser starts the cleanup at regular intervals and deletes images based on the results of the vulnerability scan performed by Trivy or a custom scanner. You can choose which security checks should be performed and which vulnerabilities are unacceptable in your cluster. You have the option to disable vulnerability scanning as well, in which case Eraser will function as a regular garbage collector.

Here is a nice diagram demonstrating how Eraser works in the automatic mode:

![](https://blog.palark.com/wp-content/uploads/2024/08/eraser-automated-workflow.png)
You can also remove your images manually using Eraser by specifying which images to delete.

## Continuous Integration & Delivery
### 8. PipeCD
[Website](https://pipecd.dev/);[GitHub](https://github.com/pipe-cd/pipecd)- 1000+ GH stars, ~90 contributors
- Initial commit: Jun 12, 2020
- License: Apache 2
- Original owner/creator: CyberAgent, Inc.
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/12);[onboarding issue](https://github.com/cncf/toc/issues/1053);[DevStats](https://pipecd.devstats.cncf.io/)
PipeCD is a GitOps-based platform for consistent deployments across different environments. The latter means it allows you to deploy not just to Kubernetes, but to four other targets as well: Terraform, GCP CloudRun, AWS Lambda, and AWS ECS.

To use PipeCD, you will need to define your application (resources and configurations) by committing it to a Git repository, “register” it in PipeCD (e.g., specify its platform provider), and customize its pipeline if needed. When it’s done, PipeCD will start delivering this app and its changes following the GitOps pull-based approach.

PipeCD integrates effortlessly with CI tools and provides automated deployment analysis, rollback mechanisms, and configuration drift detection. You can use it across multi-cloud environments, within multicluster and multitenancy setups.

![](https://blog.palark.com/wp-content/uploads/2024/08/pipecd-automatic-rollback-1024x465.png)
It also supports essential security features (such as single sign-on, RBAC, and built-in secrets management) and provides great visibility thanks to the deployment pipelines UI and real-time application state visualization.

The project’s [quickstart](https://pipecd.dev/docs-dev/quickstart/) explains how to start with PipeCD on Kubernetes. Overall, its documentation is extensive, covering a rich set of features the tool provides.

## Application Definition & Image Build
### 9. Microcks
[Website](https://microcks.io/);[GitHub](https://github.com/microcks/microcks)- 1300+ GH stars, ~50 contributors
- Initial commit: Feb 23, 2015
- License: Apache 2
- Original owner/creator: Laurent Broudoux (later, sponsored by Postman, Inc.)
- Languages: Java, TypeScript (Angular)
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/37);[onboarding issue](https://github.com/cncf/toc/issues/1096);[DevStats](https://microcks.devstats.cncf.io/)
Microcks is a cloud-native tool for API testing, allowing you to create live mocks easily. It supports various formats and specifications, including SoapUI Project (XML) 5.1+, Postman collections (JSON) 1.0/2.x, Apicurio (Studio) OpenAPI 3.x, OpenAPI (YAML, JSON) 2.x/3.x, gRPC (protobuf) 3.x, and GraphQL (schema IDL).

Microcks will ingest your existing artifacts — i.e., your API specifications, schemas, collections, and projects in the supported formats — to build its knowledge base. Based on that base, it produces:

- mocks that are immediately available on specific endpoints to be used by your consumers (without even knowing this is a fake API);
- tests that can validate whether your actual API implementation fits the expectations (as described in artifacts).
Microcks allows multiple artifacts to be ingested for a better outcome. For example, a primary artifact (based on OpenAPI) will provide the main metadata for your services and operations. Secondary artifacts (a Postman collection) will enrich existing operations with additional requests, responses, and event samples.

You can manage Microcks using a clean web UI. For example, after importing all your artifacts, you can see your APIs and services controlled by the tool, initiate testing with a simple click, browse the detailed testing results for each resource, etc.

![](https://blog.palark.com/wp-content/uploads/2024/08/microcks-api-testing-ui-1024x637.png)
Microcks can be installed in a Kubernetes cluster as an operator or using a Helm chart. Alternatively, you can deploy it locally using Docker Compose, `kind`
, or Minikube. The project’s [vast documentation](https://microcks.io/documentation/) has examples of integrating Microcks with CI/CD (GitHub Actions, Jenkins, GitLab CI/CD, and Tekton) and other tooling, such as Postman Workspaces and Backstage (the latter one is still to be done, though).

## Automation & Configuration
### 10. kpt
[Website](https://kpt.dev/);[GitHub](https://github.com/kptdev/kpt)- ~1700 GH stars, 100+ contributors
- Initial commit: Sep 17, 2019
- License: Apache 2
- Original owner/creator: Google
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/34);[onboarding issue](https://github.com/cncf/toc/issues/1095);[DevStats](https://kpt.devstats.cncf.io/)
kpt is a comprehensive suite of tools designed to create, automate, and deliver configurations in the WYSIWYG *(What You See Is What You Get)* fashion for Kubernetes and related infrastructure.

Most K8s users manage their resources using either command-line tools (`kubectl`
), GUIs, and automation tools (such as K8s operators) that work directly with Kubernetes APIs, or declarative customization tools such as Helm, Terraform, [cdk8s](https://blog.palark.com/cdk8s-framework-for-kubernetes-manifests/), etc. By allowing users to manage configurations via WYSIWYG, kpt renders this process more convenient.

The declarative *configuration as data* approach is central to kpt. It treats configuration data as the source of truth and stores it separately from the live (actual) state. It relies on a unified data model to represent configurations and abstracts configuration structure and storage from any configuration data manipulations. To achieve that, kpt performs configuration transformations similarly to Kustomize, but renders it *in place*, not *out of place*.

kpt allows you to deploy configurations via GitOps or direct apply. It comes with a catalog of ready-to-use functions and SDKs to create new ones (in Go, Typescript, and Starlark). It also supports packaging configurations and even has a specific package orchestrator (called [Porch](https://github.com/nephio-project/porch)) to handle them.

Finally, kpt has an experimental [Backstage plugin](https://github.com/GoogleContainerTools/kpt-backstage-plugins):

![](https://blog.palark.com/wp-content/uploads/2024/09/kpt-backstage-plugin-1024x399.png)
You can also [combine](https://github.com/kptdev/kpt/tree/main/package-examples/kustomize) kpt with kustomize, using the former for packaging and the latter for customization.

## Coordination & Service Discovery
### 11. Xline
[Website](https://xline.cloud/);[GitHub](https://github.com/xline-kv/Xline)- ~600 GH stars, 20+ contributors
- Initial commit: May 5, 2022
- License: Apache 2
- Original owner/creator: DatenLord Technology
- Languages: Rust
- CNCF Sandbox:
[sandbox](https://github.com/cncf/sandbox/issues/31)[request](https://github.com/cncf/sandbox/issues/11);[onboarding](https://github.com/cncf/toc/issues/1105)[issue](https://github.com/cncf/toc/issues/1093);[DevStats](https://xline.devstats.cncf.io/)
Xline is a high-performance distributed key-value (KV) store for managing metadata across multiple clusters.

This Cloud Native solution supports geo-distributed deployments and relies on the CURP consensus protocol to provide high performance and consistency even in a global network environment. You can get more details about CURP and learn how it compares to other consensus protocols (such as Raft, which is used in etcd) in the [project’s blog](https://datenlord.github.io/xline-home/#/deep-dive/Consensus).

![Xline architecture](https://blog.palark.com/wp-content/uploads/2024/09/xline-architecture.png)
Xline features a comprehensive set of KV interfaces that are fully compatible with the etcd API. Moreover, it is marketed as a basis for seamless migration for the existing etcd users, offering both better performance and advanced capabilities (for handling indexes, permissions, and configurations) in geo-distributed, multi-cluster environments.

You can install Xline manually following [this quickstart](https://github.com/xline-kv/Xline/blob/master/doc/QUICK_START.md) (interestingly, `etcdctl`
is used here to send basic requests) or by leveraging [xline-operator](https://github.com/xline-kv/xline-operator).

## Cloud Native Storage
### 12. HwameiStor
[Website](https://hwameistor.io/);[GitHub](https://github.com/hwameistor/hwameistor)- 500+ GH stars, 40+ contributors
- Initial commit: Mar 7, 2022
- License: Apache 2
- Original owner/creator: DaoCloud
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/29);[onboarding issue](https://github.com/cncf/toc/issues/1094);[DevStats](https://hwameistor.devstats.cncf.io/)
HwameiStor is a flexible local storage system designed for Cloud Native stateful workloads in Kubernetes. It:

- creates a centralized local resource pool for managing various types of disks;
- relies on CSI (Container Storage Interface) to provide distributed services with local volumes, enabling persistent storage for stateful applications.
By doing so, it aims to become a lightweight and cost-effective substitute for expensive SAN-like storage.

*Note. If you’re interested in running stateful applications in Kubernetes, you might enjoy our recent article, “Stateful apps in Kubernetes. From history and fundamentals to operators”.*
HwameiStor supports HDDs, SSDs, and NVMes and automates disks’ discovery, allocation, and management.

![](https://blog.palark.com/wp-content/uploads/2024/09/hwameistor-architecture-1024x403.png)
This solution comes with:

- disk status monitoring and audit for all resources (CRDs);
- LVM volume snapshots/restores and auto-resizing;
- affinity-based scheduling;
- HA (high availability) mode that is based on DRBD and achieved through cross-node replicas that synchronize data;
- Web-based GUI.
The recommended way of installing HwameiStor involves using [its operator](https://hwameistor.io/docs/install/operator).

## Platform / Certified Kubernetes – Installer
### 13. KubeClipper
[Website](https://kubeclipper.io/en/);[GitHub](https://github.com/kubeclipper/kubeclipper)- ~300 GH stars, ~20 contributors
- Initial commit: Jul 2, 2022
- License: Apache 2
- Original owner/creator: 99Cloud
- Languages: Go
- CNCF Sandbox:
[sandbox request](https://github.com/cncf/sandbox/issues/31);[onboarding issue](https://github.com/cncf/toc/issues/1105);[DevStats](https://kubeclipper.devstats.cncf.io/)
KubeClipper is a web service that implements a user-friendly GUI, API, and CLI tool for managing Kubernetes clusters. Covering the full cluster’s lifecycle and various setups, the project has an ambitious aim to help operators “manage Kubernetes the most light and convenient way”.

Particularly, KubeClipper helps with:

- cluster installation/uninstallation, upgrades, scaling, backups/restores, and remote access;
- deploying clusters on any infrastructure: clouds, VMs, and bare metal;
- auto-registration of new cluster nodes;
- access management: RBAC-based permissions, OIDC integration.
Moreover, the project’s roadmap includes going much further with providing application lifecycle management and integrating numerous plugins for load balancers and ingress, monitoring, Kubernetes dashboard, etc.

Technically, KubeClipper is comprised of four main components: `kc-agent`
(deployed on K8s nodes), `kc-server`
(collects information from agents), `kc-etcd`
(the backend database for *kc-server*), and `kcctl`
(a CLI tool to manage clusters).

You can install KubeClipper via `kcctl`
by entering the login and password credentials or SSH key. After installation, you can manage your setup through the web interface or CLI tool.

![](https://blog.palark.com/wp-content/uploads/2024/09/kubeclipper-create-cluster-1024x608.png)
The project’s [documentation](https://kubeclipper.io/en/docs/tutorials/) includes tutorials on creating new Kubernetes clusters and connecting existing ones, managing clusters and their nodes, and controlling access.

## Afterword
Based on these new CNCF projects, we can see that most are written in Go, licensed under Apache 2.0, and coming from big companies. Not all of them, though. What’s more intriguing to see is *when* they decided to land in the Sandbox:

- most projects are 2-3 years old;
- four are pretty new (born a year — or even less — before their application): Kepler, HwameiStor, Xline, and KubeClipper;
- three are 7+(!) years old projects (initiated in 2015): Microcks, SlimToolkit, and SOPS.
The latter clearly indicates that even mature software is looking for a reliable, vendor-neutral home.

It would be interesting to see how these projects will evolve under the CNCF’s guidance. Which of them will gain more community traction and boost its development? Feel free to share your experience using any of those 13 CNCF projects!

## Comments