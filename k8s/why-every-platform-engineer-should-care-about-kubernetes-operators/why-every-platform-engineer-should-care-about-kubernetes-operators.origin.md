# Why Every Platform Engineer Should Care About Kubernetes Operators
Posted on

In one of my recent talks, I mentioned that the foundation of a successful [Kubernetes](/kubernetes)-powered platform is the use of [Kubernetes Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), as they are a great way to automate operational tasks and the lifecycle of complex applications and services on Kubernetes.

In case you missed the talk, here is the link to the recording:

After the talk, I received feedback from the audience that they would like to have more information about Kubernetes operators and some of the advanced operators I would recommend to use in their Kubernetes-powered platforms. And who am I to reject such a great opportunity to share my knowledge with the community?

As you guess, the base for a Kubernetes Operator is, well, Kubernetes. So, if you are not familiar with Kubernetes, let me give you a brief introduction. Kubernetes, or K8s in short, is by far the most powerful open-source container orchestration platform out there - especially for its capability to maintain a desired state. This means you, as the platform admin, can define how you want your cluster and the workload on top of it to look, and Kubernetes (aka the control plane) executes the necessary steps to ensure the desired state is achieved using a feedback loop.

And how does Kubernetes achieve this complex operational task management? Kubernetes leverages the concept of controllers and operators. Both ensure that the cluster resources are in the desired state. But why is there a distinction between controllers and operators inside the Kubernetes ecosystem? There is also great confusion when folks talk about controllers and operators, as the differences are in the details and operators are a subcategory of controllers.

## Kubernetes Controllers vs. Operators
K8s controllers are control loops that watch your resources and reconcile the current state with the desired state in a continuous loop. Think about how a thermostat works in your house. The thermostat watches the current temperature and, if it is below the desired temperature, it turns on the heating. If it is above the desired temperature, it turns off the heating. This is how a controller works in Kubernetes - it watches the resources and conditions defined in the desired state and executes the necessary steps to make sure the current state matches the desired state.

Here are some typical Kubernetes controller key functions as part of the maintain, observe, and enforce loop of the control loop:

Function | Description |
---|---|
Rollouts and Rollbacks | Deployment controller takes care of rolling out new versions of your application and rolling back to the previous version in case of failure. |
Cluster maintenance | Node controller watches the nodes in the cluster and makes sure that the nodes are in the desired state. |
Event handling | Event controller watches for events and takes action based on the events. |
Schedule | Controller to run jobs and cron jobs at a specific time. |
Resource enforcement | Resource controller watches the resource usage and enforces resource limits in a namespace. |
State enforcement | Different controllers watch the state of the resources and enforce the desired state. |
As you can see, controllers automate the routine operational tasks, enforce policies, handle failures and take actions to continuously maintain the desired state of the cluster.

Some of the typical use cases for controllers are:

**Limit resource usage**- Prevent the overload of the cluster by enforcing resource limits with controllers like ResourceQuota.**Auto-scaling**- Automatically scales the number of pods based on the different metrics with HorizontalPodAutoscaler.**Task scheduling**- Run jobs and cron jobs at a specific time with Job and CronJob controllers.**Run stateful workloads**- Deploy and manage stateful workloads like databases with StatefulSet controller, by ensuring that the pods are created in a specific order and have a stable network identity.**Scaling deployments**- Deploy and manage stateless workloads like web applications with the Deployment controller, by ensuring that the desired number of pods is running and handling the rolling updates and rollbacks.
Controllers, as you see, reduce the manual effort for the platform engineering teams and gives the cluster self-managing capabilities.

With all the above points, the benefits of controllers are clear - Let me list some of the main ones:

**Automation**- Controllers automate the routine operational tasks and enforce policies.**Availability**- Controllers ensure that the resources are always available, addressing failures and taking actions to maintain the desired state.**Efficiency**- Controllers provide an efficient way to manage the resources and workloads in the cluster with quota management and auto-scaling.**Reliablity**- Controllers help to make workload management more reliable with features like replica management,[pod](/registry/packages/kubernetes/api-docs/core/v1/pod/)creation and deletion, and scheduling.**Flexibility**- Controllers provide a flexible way to handle a variety of workloads and resources in the cluster, such as[DaemonSet](/registry/packages/kubernetes/api-docs/apps/v1/daemonset/),[StatefulSet](/registry/packages/kubernetes/api-docs/apps/v1/statefulset/),[jobs](/registry/packages/kubernetes/api-docs/batch/v1/job/),[cron jobs](/registry/packages/kubernetes/api-docs/batch/v1/cronjob/),[deployments](/registry/packages/kubernetes/api-docs/apps/v1/deployment/), and[services](/registry/packages/kubernetes/api-docs/core/v1/service/).**Observability**- Controllers provide a view into the cluster resources and the state of the resources via the[Kubernetes API](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/#kubernetes-components-and-the-kubernetes-api).
With Controllers explained, let’s move on to the next level of automation in Kubernetes and talk about Kubernetes Operators.

## Kubernetes Operators
As mentioned before, Kubernetes Operators are a subcategory of controllers that use API extensions (Custom Resource) to complete the automation task. Operators are a set of independent controllers, with each controller responsible for its own task. And while controllers can share similar functions with a controller, it is only focused on one domain and only uses Custom Resources to manage the domain.

Keep in mind that controllers work without the need for custom resources or a link to a specific domain.

Operators are custom-built controllers that focus on the deployment, management, and operation of a specific application or service. Some key functions of operators include:

Function | Description |
---|---|
Security | Operators integrate security best practices and policies, such as encryption, access control, and
|
Operators are a great way to encode the operational knowledge of the platform engineering team into automated controllers. This way, the platform engineering team can focus on the strategic tasks and let the operators handle the boring routine operational tasks. This reduces the manual effort and increases the reliability of the platform.

Some of the typical use cases for operators are:

**Database management**- Deploy and manage databases such as MySQL, PostgreSQL, and MongoDB.**Storage management**- Deploy and manage storage such as Ceph, GlusterFS, or NFS.**Logging and monitoring**- Simplify the deployment and management of logging and monitoring solutions like Prometheus, Grafana, or ELK stack.**CI/CD**- Automate the deployment and management of CI/CD pipelines like Jenkins, GitLab, or Tekton. - Backup and restore - Automate the backup and restore of applications and data.**Messaging and event streaming**- Simplify the deployment and management of messaging and event streaming solutions like Kafka, RabbitMQ, or NATS.**Machine learning**- Automate the deployment and management of machine learning workloads such as TensorFlow, PyTorch, or Kubeflow.
With the applications-centric approach provided by operators, the platform engineering team can now enable fully automated operations while enhancing the reliability, efficiency, and observability of the platform and ensuring adherence to best practices and compliance requirements.

And similar to controllers, operators also have distinct benefits:

**Simplification**- Operators simplify the deployment and management of complex applications and services by providing a declarative way (via Custom Resources).**Higher Productivity**- Operators increase the productivity of the platform engineering team by automating the routine operational tasks and allowing users to focus on delivering business value.**Extensibility**- Extending the K8s API with Custom Resource Definitions (CRDs) allows administrators to support new applications and services without changing the core Kubernetes code.**Consistency**- Operators ensure that they deploy and run the applications and services consistently across different environments, such as on-premises, cloud, or hybrid.**Modularity**- Operators are modular and focused on a specific domain.**Legacy**Transformation - Operators help to transform legacy applications into cloud-native applications by automating the deployment and management of complex applications.
Here is a visual representation of a Kubernetes Operator in action, which I found very nice and helpful:

![Kubernetes Operators: what are they? Some examples Credit: SparkFabrik](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/operator.png)
Kubernetes Operators: what are they? Some examples Credit: SparkFabrik

## Comparison of Kubernetes Controllers and Operators
Here is a quick summary of the differences between Kubernetes controllers and operators:

Feature | Kubernetes Controllers | Kubernetes Operators |
---|---|---|
Definition | Core control loops within Kubernetes that reconcile the current state with the desired state of resources. | Custom-built controllers with domain-specific logic, typically extending Kubernetes API with Custom Resource Definitions (CRDs). |
Scope | General-purpose automation for cluster-wide resource management and workload operations. | Focused on application or service-specific lifecycle management and operations. |
Custom Resources (CRDs) | Not mandatory. Most controllers work with built-in Kubernetes resources like Pods, Deployments, and StatefulSets. | Mandatory. Operators depend on CRDs to define and manage application-specific resources. |
Domain-Specific Logic | Limited. Primarily focuses on generic Kubernetes operations like scheduling, scaling, and resource enforcement. | Extensive. Includes application-specific tasks such as backups, upgrades, migrations, and disaster recovery. |
Automation | Automates operational tasks like resource scheduling, scaling, and maintaining cluster states. | Automates both operational and domain-specific tasks, often encoding deep operational knowledge of specific applications. |
Complexity | Relatively low complexity as they focus on Kubernetes-native workflows. | Higher complexity due to domain-specific implementations and integrations with external systems. |
Observability | Provides insight into cluster resource states via Kubernetes API and built-in events. | Enhances observability with application-specific metrics, logs, and health checks tailored to the managed application. |
Use Cases | - Pod scaling (e.g., HPA) - Resource enforcement (e.g., ResourceQuota)- Rolling updates and rollbacks- Scheduling jobs (e.g., CronJob). | - Database management (e.g., MySQL Operator) - CI/CD pipelines (e.g., Tekton)- Backup and restore- Monitoring solutions (e.g., Prometheus Operator)- Stateful applications (e.g., Kafka Operator). |
Deployment | Part of Kubernetes core components or extensions like kube-controller-manager. | External tools developed by vendors, community, or in-house, deployed using Custom Resources. |
Key Benefits | - Cluster-wide automation - Ensures resource availability- Efficient and reliable workload management. | - Simplifies application lifecycle management - Increases productivity with domain-specific automation- Consistent deployments across environments. |
Flexibility | Flexible for general Kubernetes operations but limited to built-in resources. | Highly flexible and extensible for custom applications and domain-specific requirements. |
Target Audience | Platform administrators and Kubernetes users looking to automate Kubernetes-native workflows. | Developers and platform engineers needing advanced automation and lifecycle management for specific applications or services. |
Maintenance | Managed and updated by Kubernetes core or community projects. | Requires domain-specific knowledge and regular updates to accommodate application changes and best practices. |
With this detailed explanation of Kubernetes controllers and operators, I would like to share some advanced Kubernetes operators that I recommend for use in your Kubernetes-powered platform.

## Advanced Kubernetes Operators
As we have seen, Kubernetes Operators are the go-to way to automate operational tasks and lifecycle management. I should mention that not all operators are created equal. Some operators are more advanced and provide more features than others. That is why, for example, [OperatorHub.io](https://operatorhub.io/) categorises operators into [five capability levels](https://sdk.operatorframework.io/docs/overview/operator-capabilities/):

**Basic Install**- Installs the application on the cluster.**Seamless Upgrades**- Manages Application upgrades.**Full Lifecycle Management**- Manages the full lifecycle of the application.**Deep Insights**- Provides monitoring and metrics.**Auto Pilot**- Automatically optimizes and tunes the application.
The more advanced the operator, the more features it provides and the more automation it offers. At its most advanced level, the Auto Pilot, the operator automatically optimizes and tunes the application based on the workload and environment.

Here is a list of advanced Kubernetes operators that I recommend using in your Kubernetes-powered platform:

### CloudNativePG Operator
![CloudNativePG Operator Credit: cloudnative-pg.io](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/cloudnativepg.png)
CloudNativePG Operator Credit: cloudnative-pg.io

[CloudNativePG Operator](https://cloudnative-pg.io/) is a PostgreSQL operator that covers the full lifecycle of PostgreSQL databases on Kubernetes. It simplifies the deployment, management, and scaling of PostgreSQL databases by providing a declarative way to define and manage PostgreSQL clusters using custom resources.
Some of the key features of CloudNativePG Operator are:

**Automated Backups**- Schedule and manage backups of PostgreSQL databases.**High Availability**- Deploy and manage high-availability PostgreSQL clusters.**Scaling**- Scale the number of PostgreSQL instances based on the workload.
#### Installation
Either use the Helm chart or the Kubernetes manifests to deploy the CloudNativePG Operator:

```
helm repo add cloudnative-pg https://cloudnative-pg.io/charts/
helm repo update
helm upgrade --install cloudnativepg cloudnative-pg/cloudnative-pg --namespace cnpg-system --create-namespace
```
Or use Pulumi to deploy the CloudNativePG Operator:

```
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const ns = new k8s.core.v1.Namespace("cnpg-system", {
metadata: {
name: "cnpg-system",
},
});
new k8shelm.Release("cloudnativepg", {
chart: "cloudnative-pg/cloudnative-pg",
namespace: ns.metadata.name,
createNamespace: true,
});
```
```
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");
const ns = new k8s.core.v1.Namespace("cnpg-system", {
metadata: {
name: "cnpg-system",
},
});
new k8shelm.Release("cloudnativepg", {
chart: "cloudnative-pg/cloudnative-pg",
namespace: ns.metadata.name,
createNamespace: true,
});
```
```
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta
ns = k8s.core.v1.Namespace(
"cnpg-system",
meta.ObjectMetaArgs(
name="cnpg-system",
),
)
release = k8shelm.Release(
"cloudnativepg",
chart="cloudnative-pg/cloudnative-pg",
namespace=ns.metadata["name"],
create_namespace=True,
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
pulumi.Run(func(ctx *pulumi.Context) error {
ns, err := corev1.NewNamespace(ctx, "cnpg-system", &corev1.NamespaceArgs{
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("cnpg-system"),
},
})
if err != nil {
return err
}
_, err = helmv3.NewRelease(ctx, "cloudnativepg", &helmv3.ReleaseArgs{
Chart: pulumi.String("cloudnative-pg/cloudnative-pg"),
Namespace: ns.Metadata.Name().Elem(),
CreateNamespace: pulumi.Bool(true),
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
class MyStack : Stack
{
public MyStack()
{
var ns = new Namespace("cnpg-system", new NamespaceArgs
{
Metadata = new ObjectMetaArgs
{
Name = "cnpg-system"
}
});
var release = new Release("cloudnativepg", new ReleaseArgs
{
Chart = "cloudnative-pg/cloudnative-pg",
Namespace = ns.Metadata.Apply(m => m.Name),
CreateNamespace = true
});
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Usage
Here is a simple example of a PostgreSQL cluster with backup configured on S3 API-compatible storage:

```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
name: cluster-example-with-backup
spec:
instances: 3
primaryUpdateStrategy: unsupervised
# Persistent storage configuration
storage:
storageClass: standard
size: 1Gi
# Backup properties
# This assumes a local minio setup
backup:
barmanObjectStore:
destinationPath: s3://backups/
endpointURL: http://minio:9000
s3Credentials:
accessKeyId:
name: minio
key: ACCESS_KEY_ID
secretAccessKey:
name: minio
key: ACCESS_SECRET_KEY
wal:
compression: gzip
```
Or use Pulumi:

```
new k8s.apiextensions.CustomResource("cluster-example-with-backup", {
apiVersion: "postgresql.cnpg.io/v1",
kind: "Cluster",
metadata: {
name: "cluster-example-with-backup",
},
spec: {
instances: 3,
primaryUpdateStrategy: "unsupervised",
// Persistent storage configuration
storage: {
storageClass: "standard",
size: "1Gi",
},
// Backup properties
backup: {
barmanObjectStore: {
destinationPath: "s3://backups/",
endpointURL: "http://minio:9000",
s3Credentials: {
accessKeyId: {
name: "minio",
key: "ACCESS_KEY_ID",
},
secretAccessKey: {
name: "minio",
key: "ACCESS_SECRET_KEY",
},
},
wal: {
compression: "gzip",
},
},
},
},
});
```
```
new k8s.apiextensions.CustomResource("cluster-example-with-backup", {
apiVersion: "postgresql.cnpg.io/v1",
kind: "Cluster",
metadata: {
name: "cluster-example-with-backup",
},
spec: {
instances: 3,
primaryUpdateStrategy: "unsupervised",
// Persistent storage configuration
storage: {
storageClass: "standard",
size: "1Gi",
},
// Backup properties
backup: {
barmanObjectStore: {
destinationPath: "s3://backups/",
endpointURL: "http://minio:9000",
s3Credentials: {
accessKeyId: {
name: "minio",
key: "ACCESS_KEY_ID",
},
secretAccessKey: {
name: "minio",
key: "ACCESS_SECRET_KEY",
},
},
wal: {
compression: "gzip",
},
},
},
},
});
```
```
from pulumi_kubernetes import apiextensions
postgresql_cluster = apiextensions.CustomResource(
"cluster-example-with-backup",
api_version="postgresql.cnpg.io/v1",
kind="Cluster",
metadata=meta.ObjectMetaArgs(
name="cluster-example-with-backup",
),
spec={
"instances": 3,
"primaryUpdateStrategy": "unsupervised",
# Persistent storage configuration
"storage": {
"storageClass": "standard",
"size": "1Gi",
},
# Backup properties
"backup": {
"barmanObjectStore": {
"destinationPath": "s3://backups/",
"endpointURL": "http://minio:9000",
"s3Credentials": {
"accessKeyId": {
"name": "minio",
"key": "ACCESS_KEY_ID",
},
"secretAccessKey": {
"name": "minio",
"key": "ACCESS_SECRET_KEY",
},
},
"wal": {
"compression": "gzip",
},
},
},
},
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
pulumi.Run(func(ctx *pulumi.Context) error {
_, err = apiv1.NewCustomResource(ctx, "cluster-example-with-backup", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("postgresql.cnpg.io/v1"),
Kind: pulumi.String("Cluster"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("cluster-example-with-backup"),
},
OtherFields: k8s.UntypedArgs{
"instances": pulumi.Int(3),
"primaryUpdateStrategy": pulumi.String("unsupervised"),
"storage": pulumi.Map{
"storageClass": pulumi.String("standard"),
"size": pulumi.String("1Gi"),
},
"backup": pulumi.Map{
"barmanObjectStore": pulumi.Map{
"destinationPath": pulumi.String("s3://backups/"),
"endpointURL": pulumi.String("http://minio:9000"),
"s3Credentials": pulumi.Map{
"accessKeyId": pulumi.Map{
"name": pulumi.String("minio"),
"key": pulumi.String("ACCESS_KEY_ID"),
},
"secretAccessKey": pulumi.Map{
"name": pulumi.String("minio"),
"key": pulumi.String("ACCESS_SECRET_KEY"),
},
},
"wal": pulumi.Map{
"compression": pulumi.String("gzip"),
},
},
},
},
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
class PostGreSQLClusterArgs : CustomResourceArgs
{
[Input("postgresql.cnpg.io/v1")]
public Input<string> ApiVersion { get; set; }
[Input("Cluster")]
public Input<string> Kind { get; set; }
public ObjectMetaArgs Metadata { get; set; }
public Dictionary<string, object> Others { get; set; }
[Input("spec")]
public InputMap<object> Spec { get; set; }
public PostGreSQLClusterArgs(string apiVersion, string kind) : base(apiVersion, kind)
{
}
}
class MyStack : Stack
{
public MyStack()
{
var postgresqlCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource("cluster-example-with-backup", new PostGreSQLClusterArgs("postgresql.cnpg.io/v1", "Cluster")
{
ApiVersion = "postgresql.cnpg.io/v1",
Kind = "Cluster",
Metadata = new ObjectMetaArgs
{
Name = "cluster-example-with-backup",
},
Spec = new InputMap<object>
{
{ "instances", 3 },
{ "primaryUpdateStrategy", "unsupervised" },
{ "storage", new InputMap<object>
{
{ "storageClass", "standard" },
{ "size", "1Gi" },
}
},
{ "backup", new InputMap<object>
{
{ "barmanObjectStore", new InputMap<object>
{
{ "destinationPath", "s3://backups/" },
{ "endpointURL", "http://minio:9000" },
{ "s3Credentials", new InputMap<object>
{
{ "accessKeyId", new InputMap<object>
{
{ "name", "minio" },
{ "key", "ACCESS_KEY_ID" },
}
},
{ "secretAccessKey", new InputMap<object>
{
{ "name", "minio" },
{ "key", "ACCESS_SECRET_KEY" },
}
},
}
},
{ "wal", new InputMap<object>
{
{ "compression", "gzip" },
}
},
}
},
}
},
}
});
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Summary
CloudNativePG Operator is a great way to deploy and manage PostgreSQL databases on Kubernetes. It simplifies a wide range of tasks, including backups, high availability, and scaling, making it a must-have for PostgreSQL users.

### Flux Operator
![Flux Operator Credit: fluxcd.control-plane.io/operator](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/flux-operator.png)
Flux Operator Credit: fluxcd.control-plane.io/operator

The [Flux Operator](https://fluxcd.control-plane.io/operator/) is a full autopilot solution that provides an alternative to the traditional Flux Bootstrap procedure, removing the operational burden of managing Flux across multiple clusters by automating the installation, configuration, and upgrade of Flux fully.

Some of the key features of Flux Operator are:

**GitOps Deployment**- Automate the deployment of applications and services using GitOps.**Lifecycle Management**- Manage the full lifecycle of Flux, including upgrades and rollbacks.**Deep Insights**- Provide deep insights into the state of Flux and the applications deployed with Flux.
#### Installation
Use the Helm chart to deploy the Flux Operator:

```
helm upgrade -i flux-operator oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator --namespace flux-system --create-namespace
```
Or use Pulumi to deploy the Flux Operator:

```
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const namespace = new k8s.core.v1.Namespace("flux-system", {
metadata: {
name: "flux-system",
},
});
new k8s.helm.v3.Release("flux-operator", {
chart: "flux-operator",
version: "latest",
namespace: namespace.metadata.name,
repositoryOpts: {
repo: "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
createNamespace: true,
});
```
```
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");
const namespace = new k8s.core.v1.Namespace("flux-system", {
metadata: {
name: "flux-system",
},
});
new k8s.helm.v3.Release("flux-operator", {
chart: "flux-operator",
version: "latest",
namespace: namespace.metadata.name,
repositoryOpts: {
repo: "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
createNamespace: true,
});
```
```
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta
namespace = k8s.core.v1.Namespace(
"flux-system",
meta.ObjectMetaArgs(
name="flux-system",
),
)
flux_operator = k8shelm.Release(
"flux-operator",
chart="flux-operator",
version="latest",
namespace=namespace.metadata["name"],
repository_opts={
"repo": "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
create_namespace=True,
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
pulumi.Run(func(ctx *pulumi.Context) error {
namespace, err := corev1.NewNamespace(ctx, "flux-system", &corev1.NamespaceArgs{
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("flux-system"),
},
})
if err != nil {
return err
}
_, err = helmv3.NewRelease(ctx, "flux-operator", &helmv3.ReleaseArgs{
Chart: pulumi.String("flux-operator"),
Version: pulumi.String("latest"),
Namespace: namespace.Metadata.Name().Elem(),
RepositoryOpts: &helmv3.RepositoryOptsArgs{
Repo: pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/charts"),
},
CreateNamespace: pulumi.Bool(true),
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
var namespaceFluxSystem = new Namespace("flux-system", new NamespaceArgs
{
Metadata = new ObjectMetaArgs
{
Name = "flux-system",
},
});
var fluxOperator = new Release("flux-operator", new ReleaseArgs
{
Chart = "flux-operator",
Version = "latest",
Namespace = namespaceFluxSystem.Metadata.Apply(metadata => metadata.Name),
RepositoryOpts = new RepositoryOptsArgs
{
Repo = "oci://ghcr.io/controlplaneio-fluxcd/charts",
},
CreateNamespace = true,
});
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Usage
Here is an example of a FluxInstance Custom Resource that defines a Flux instance:

```
apiVersion: fluxcd.controlplane.io/v1
kind: FluxInstance
metadata:
name: flux
namespace: flux-system
annotations:
fluxcd.controlplane.io/reconcileEvery: "1h"
fluxcd.controlplane.io/reconcileTimeout: "5m"
spec:
distribution:
version: "2.x"
registry: "ghcr.io/fluxcd"
artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"
components:
- source-controller
- kustomize-controller
- helm-controller
- notification-controller
- image-reflector-controller
- image-automation-controller
cluster:
type: kubernetes
multitenant: false
networkPolicy: true
domain: "cluster.local"
kustomize:
patches:
- target:
kind: Deployment
name: "(kustomize-controller|helm-controller)"
patch: |
- op: add
path: /spec/template/spec/containers/0/args/-
value: --concurrent=10
- op: add
path: /spec/template/spec/containers/0/args/-
value: --requeue-dependency=5s
```
Or use Pulumi:

```
new k8s.apiextensions.CustomResource("flux", {
apiVersion: "fluxcd.controlplane.io/v1",
kind: "FluxInstance",
metadata: {
name: "flux",
namespace: "flux-system",
annotations: {
"fluxcd.controlplane.io/reconcileEvery": "1h",
"fluxcd.controlplane.io/reconcileTimeout": "5m",
},
},
spec: {
distribution: {
version: "2.x",
registry: "ghcr.io/fluxcd",
artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
},
components: ["source-controller", "kustomize-controller", "helm-controller", "notification-controller", "image-reflector-controller", "image-automation-controller"],
cluster: {
type: "kubernetes",
multitenant: false,
networkPolicy: true,
domain: "cluster.local",
},
kustomize: {
patches: [
{
target: {
kind: "Deployment",
name: "(kustomize-controller|helm-controller)",
},
patch: `
- op: add
path: /spec/template/spec/containers/0/args/-
value: --concurrent=10
- op: add
path: /spec/template/spec/containers/0/args/-
value: --requeue-dependency=5s
`,
},
],
},
},
});
```
```
new k8s.apiextensions.CustomResource("flux", {
apiVersion: "fluxcd.controlplane.io/v1",
kind: "FluxInstance",
metadata: {
name: "flux",
namespace: "flux-system",
annotations: {
"fluxcd.controlplane.io/reconcileEvery": "1h",
"fluxcd.controlplane.io/reconcileTimeout": "5m",
},
},
spec: {
distribution: {
version: "2.x",
registry: "ghcr.io/fluxcd",
artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
},
components: ["source-controller", "kustomize-controller", "helm-controller", "notification-controller", "image-reflector-controller", "image-automation-controller"],
cluster: {
type: "kubernetes",
multitenant: false,
networkPolicy: true,
domain: "cluster.local",
},
kustomize: {
patches: [
{
target: {
kind: "Deployment",
name: "(kustomize-controller|helm-controller)",
},
patch: `
- op: add
path: /spec/template/spec/containers/0/args/-
value: --concurrent=10
- op: add
path: /spec/template/spec/containers/0/args/-
value: --requeue-dependency=5s
`,
},
],
},
},
});
```
```
from pulumi_kubernetes import apiextensions
flux_instance = k8s.apiextensions.CustomResource(
"flux",
api_version="fluxcd.controlplane.io/v1",
kind="FluxInstance",
metadata={
"name": "flux",
"namespace": flux_namespace.metadata["name"],
"annotations": {
"fluxcd.controlplane.io/reconcileEvery": "1h",
"fluxcd.controlplane.io/reconcileTimeout": "5m",
},
},
spec={
"distribution": {
"version": "2.x",
"registry": "ghcr.io/fluxcd",
"artifact": "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
},
"components": [
"source-controller",
"kustomize-controller",
"helm-controller",
"notification-controller",
"image-reflector-controller",
"image-automation-controller",
],
"cluster": {
"type": "kubernetes",
"multitenant": False,
"networkPolicy": True,
"domain": "cluster.local",
},
"kustomize": {
"patches": [
{
"target": {
"kind": "Deployment",
"name": "(kustomize-controller|helm-controller)",
},
"patch": [
{
"op": "add",
"path": "/spec/template/spec/containers/0/args/-",
"value": "--concurrent=10",
},
{
"op": "add",
"path": "/spec/template/spec/containers/0/args/-",
"value": "--requeue-dependency=5s",
},
],
}
]
},
},
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
pulumi.Run(func(ctx *pulumi.Context) error {
_, err = apiv1.NewCustomResource(ctx, "flux", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("fluxcd.controlplane.io/v1"),
Kind: pulumi.String("FluxInstance"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("flux"),
Namespace: pulumi.String("flux-system"),
Annotations: pulumi.StringMap{
"fluxcd.controlplane.io/reconcileEvery": pulumi.String("1h"),
"fluxcd.controlplane.io/reconcileTimeout": pulumi.String("5m"),
},
},
OtherFields: k8s.UntypedArgs{
"distribution": pulumi.Map{
"version": pulumi.String("2.x"),
"registry": pulumi.String("ghcr.io/fluxcd"),
"artifact": pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"),
},
"components": pulumi.StringArray{
pulumi.String("source-controller"),
pulumi.String("kustomize-controller"),
pulumi.String("helm-controller"),
pulumi.String("notification-controller"),
pulumi.String("image-reflector-controller"),
pulumi.String("image-automation-controller"),
},
"cluster": pulumi.Map{
"type": pulumi.String("kubernetes"),
"multitenant": pulumi.Bool(false),
"networkPolicy": pulumi.Bool(true),
"domain": pulumi.String("cluster.local"),
},
"kustomize": pulumi.Map{
"patches": pulumi.Array{
pulumi.Map{
"target": pulumi.Map{
"kind": pulumi.String("Deployment"),
"name": pulumi.String("(kustomize-controller|helm-controller)"),
},
"patch": pulumi.Array{
pulumi.Map{
"op": pulumi.String("add"),
"path": pulumi.String("/spec/template/spec/containers/0/args/-"),
"value": pulumi.String("--concurrent=10"),
},
pulumi.Map{
"op": pulumi.String("add"),
"path": pulumi.String("/spec/template/spec/containers/0/args/-"),
"value": pulumi.String("--requeue-dependency=5s"),
},
},
},
},
},
},
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
class FluxInstanceArgs : CustomResourceArgs
{
public string ApiVersion { get; set; }
public string Kind { get; set; }
public ObjectMetaArgs Metadata { get; set; }
public Dictionary<string, object> Spec { get; set; }
public FluxInstanceArgs(string apiVersion, string kind) : base(apiVersion, kind)
{
}
}
var flux = new Pulumi.Kubernetes.ApiExtensions.CustomResource("flux", new FluxInstanceArgs("fluxcd.controlplane.io/v1", "FluxInstance")
{
ApiVersion = "fluxcd.controlplane.io/v1",
Kind = "FluxInstance",
Metadata = new ObjectMetaArgs
{
Name = "flux",
Annotations =
{
{ "fluxcd.controlplane.io/reconcileEvery", "1h" },
{ "fluxcd.controlplane.io/reconcileTimeout", "5m" },
}
},
Spec =
{
{ "distribution", new Dictionary<string, object>
{
{ "version", "2.x" },
{ "registry", "ghcr.io/fluxcd" },
{ "artifact", "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests" }
}
},
{ "components", new[]
{
"source-controller",
"kustomize-controller",
"helm-controller",
"notification-controller",
"image-reflector-controller",
"image-automation-controller"
}
},
{ "cluster", new Dictionary<string, object>
{
{ "type", "kubernetes" },
{ "multitenant", false },
{ "networkPolicy", true },
{ "domain", "cluster.local" }
}
},
{ "kustomize", new Dictionary<string, object>
{
{ "patches", new[]
{
new Dictionary<string, object>
{
{ "target", new Dictionary<string, object>
{
{ "kind", "Deployment" },
{ "name", "(kustomize-controller|helm-controller)" }
}
},
{ "patch", new[]
{
new Dictionary<string, object>
{
{ "op", "add" },
{ "path", "/spec/template/spec/containers/0/args/-" },
{ "value", "--concurrent=10" }
},
new Dictionary<string, object>
{
{ "op", "add" },
{ "path", "/spec/template/spec/containers/0/args/-" },
{ "value", "--requeue-dependency=5s" }
}
}
}
}
}
}
}
}
},
});
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Summary
The Flux Operator is another excellent example of an advanced Kubernetes operator, providing full lifecycle management with numerous automation features.

### Strimzi Operator
![Strimzi Operator Credit: strimzi.io](/blog/why-every-platform-engineer-should-care-about-kubernetes-operators/strimzi.png)
Strimzi Operator Credit: strimzi.io

Last but not least, the [Strimzi Operator](https://strimzi.io/) is a full lifecycle management operator for Apache Kafka on Kubernetes. As event-driven architectures are becoming increasingly popular, Apache Kafka has become the de-facto standard for building scalable and reliable event streaming platforms. The Strimzi Operator makes it easier to deploy, manage, and scale Apache Kafka clusters on Kubernetes.

Some of the key features of Strimzi Operator are:

**Cluster Management**- Deploy and manage Apache Kafka clusters.**Mirror Clusters**- Deploy and manage mirror clusters for disaster recovery.**Streaming Capabilities**- With Kafka Connect you can stream data between Kafka and other systems.
#### Installation
Use the Helm chart to deploy the Strimzi Operator:

```
helm repo add strimzi https://strimzi.io/charts/
helm repo update
helm install strimzi strimzi/strimzi-kafka-operator -n kafka --create-namespace
```
Or use Pulumi to deploy the Strimzi Operator:

```
import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";
const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
metadata: {
name: "kafka",
},
});
new k8s.helm.v3.Release("strimzi-kafka-operator", {
chart: "strimzi-kafka-operator",
version: "latest",
namespace: namespaceKafka.metadata.name,
repositoryOpts: {
repo: "https://strimzi.io/charts/",
},
createNamespace: true,
});
```
```
"use strict";
const k8s = require("@pulumi/kubernetes");
const k8shelm = require("@pulumi/kubernetes/helm/v3");
const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
metadata: {
name: "kafka",
},
});
new k8s.helm.v3.Release("strimzi-kafka-operator", {
chart: "strimzi-kafka-operator",
version: "latest",
namespace: namespaceKafka.metadata.name,
repositoryOpts: {
repo: "https://strimzi.io/charts/",
},
createNamespace: true,
});
```
```
import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta
namespace_kafka = k8s.core.v1.v1.Namespace(
"kafka",
meta.ObjectMetaArgs(
name="kafka",
),
)
strimzi_kafka_operator = k8shelm.Release(
"strimzi-kafka-operator",
chart="strimzi-kafka-operator",
version="latest",
namespace=namespace_kafka.metadata["name"],
repository_opts={
"repo": "https://strimzi.io/charts/",
},
create_namespace=True,
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
namespaceKafka, err := corev1.NewNamespace(ctx, "kafka", &corev1.NamespaceArgs{
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("kafka"),
},
})
if err != nil {
return err
}
_, err = helmv3.NewRelease(ctx, "strimzi-kafka-operator", &helmv3.ReleaseArgs{
Chart: pulumi.String("strimzi-kafka-operator"),
Version: pulumi.String("latest"),
Namespace: namespaceKafka.Metadata.Name(),
RepositoryOpts: helmv3.RepositoryOptsArgs{
Repo: pulumi.String("https://strimzi.io/charts/"),
},
CreateNamespace: pulumi.Bool(true),
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
class MyStack : Stack
{
public MyStack()
{
var namespaceKafka = new Namespace("kafka", new NamespaceArgs
{
Metadata = new ObjectMetaArgs
{
Name = "kafka",
}
});
var strimziKafkaOperator = new Release("strimzi-kafka-operator", new ReleaseArgs
{
Chart = "strimzi-kafka-operator",
Version = "latest",
Namespace = namespaceKafka.Metadata.Apply(ns => ns.Name),
RepositoryOpts = new RepositoryOptsArgs
{
Repo = "https://strimzi.io/charts/",
},
CreateNamespace = true,
});
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Usage
Here is an example of a Kafka Custom Resource that defines a Kafka cluster:

```
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaNodePool
metadata:
name: example-kafka-node-pool
labels:
strimzi.io/cluster: example-kafka-cluster
spec:
replicas: 1
roles:
- controller
- broker
storage:
type: ephemeral
---
apiVersion: kafka.strimzi.io/v1beta2
kind: Kafka
metadata:
name: example-kafka-cluster
annotations:
strimzi.io/kraft: enabled
strimzi.io/node-pools: enabled
spec:
kafka:
replicas: 1
version: 3.8.0
storage:
type: ephemeral
metadataVersion: 3.8-IV0
listeners:
- name: plain
port: 9092
type: internal
tls: false
- name: tls
port: 9093
type: internal
tls: true
config:
offsets.topic.replication.factor: 1
transaction.state.log.replication.factor: 1
transaction.state.log.min.isr: 1
default.replication.factor: 1
min.insync.replicas: 1
entityOperator:
topicOperator: {}
userOperator: {}
```
This example defines a Kafka cluster with one replica and two listeners, one for plain and one for TLS and uses ephemeral storage.

To create a topic, you can use the following KafkaTopic Custom Resource:

```
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
name: example-kafka-cluster
labels:
strimzi.io/cluster:
spec:
partitions: 5
replicas: 1
config:
retention.ms: 7200000
segment.bytes: 1073741824
```
Or use Pulumi:

```
new k8s.apiextensions.CustomResource("example-kafka-node-pool", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "KafkaNodePool",
metadata: {
name: "example-kafka-node-pool",
labels: {
"strimzi.io/cluster": "example-kafka-cluster",
},
namespace: "kafka",
},
spec: {
replicas: 1,
roles: ["controller", "broker"],
storage: {
type: "ephemeral",
},
},
});
new k8s.apiextensions.CustomResource("example-kafka-cluster", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "Kafka",
metadata: {
name: "example-kafka-cluster",
annotations: {
"strimzi.io/kraft": "enabled",
"strimzi.io/node-pools": "enabled",
},
namespace: "kafka",
},
spec: {
kafka: {
replicas: 1,
version: "3.8.0",
storage: {
type: "ephemeral",
},
metadataVersion: "3.8-IV0",
listeners: [
{
name: "plain",
port: 9092,
type: "internal",
tls: false,
},
{
name: "tls",
port: 9093,
type: "internal",
tls: true,
},
],
config: {
"offsets.topic.replication.factor": 1,
"transaction.state.log.replication.factor": 1,
"transaction.state.log.min.isr": 1,
"default.replication.factor": 1,
"min.insync.replicas": 1,
},
},
entityOperator: {
topicOperator: {},
userOperator: {},
},
},
});
new k8s.apiextensions.CustomResource("example-kafka-topic", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "KafkaTopic",
metadata: {
name: "example-kafka-topic",
labels: {
"strimzi.io/cluster": "example-kafka-cluster",
},
namespace: "kafka",
},
spec: {
partitions: 5,
replicas: 1,
config: {
"retention.ms": 7200000,
"segment.bytes": 1073741824,
},
},
});
```
```
new k8s.apiextensions.CustomResource("example-kafka-node-pool", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "KafkaNodePool",
metadata: {
name: "example-kafka-node-pool",
labels: {
"strimzi.io/cluster": "example-kafka-cluster",
},
namespace: "kafka",
},
spec: {
replicas: 1,
roles: ["controller", "broker"],
storage: {
type: "ephemeral",
},
},
});
new k8s.apiextensions.CustomResource("example-kafka-cluster", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "Kafka",
metadata: {
name: "example-kafka-cluster",
annotations: {
"strimzi.io/kraft": "enabled",
"strimzi.io/node-pools": "enabled",
},
namespace: "kafka",
},
spec: {
kafka: {
replicas: 1,
version: "3.8.0",
storage: {
type: "ephemeral",
},
metadataVersion: "3.8-IV0",
listeners: [
{
name: "plain",
port: 9092,
type: "internal",
tls: false,
},
{
name: "tls",
port: 9093,
type: "internal",
tls: true,
},
],
config: {
"offsets.topic.replication.factor": 1,
"transaction.state.log.replication.factor": 1,
"transaction.state.log.min.isr": 1,
"default.replication.factor": 1,
"min.insync.replicas": 1,
},
},
entityOperator: {
topicOperator: {},
userOperator: {},
},
},
});
new k8s.apiextensions.CustomResource("example-kafka-topic", {
apiVersion: "kafka.strimzi.io/v1beta2",
kind: "KafkaTopic",
metadata: {
name: "example-kafka-topic",
labels: {
"strimzi.io/cluster": "example-kafka-cluster",
},
namespace: "kafka",
},
spec: {
partitions: 5,
replicas: 1,
config: {
"retention.ms": 7200000,
"segment.bytes": 1073741824,
},
},
});
```
```
from pulumi_kubernetes import apiextensions
kafka_node_pool = k8s.apiextensions.CustomResource(
"example-kafka-node-pool",
api_version="kafka.strimzi.io/v1beta2",
kind="KafkaNodePool",
metadata={
"name": "example-kafka-node-pool",
"labels": {
"strimzi.io/cluster": "example-kafka-cluster",
},
"namespace": kafka_namespace.metadata["name"],
},
spec={
"replicas": 1,
"roles": ["controller", "broker"],
"storage": {
"type": "ephemeral",
},
},
)
kafka_cluster = k8s.apiextensions.CustomResource(
"example-kafka-cluster",
api_version="kafka.strimzi.io/v1beta2",
kind="Kafka",
metadata={
"name": "example-kafka-cluster",
"annotations": {
"strimzi.io/kraft": "enabled",
"strimzi.io/node-pools": "enabled",
},
"namespace": kafka_namespace.metadata["name"],
},
spec={
"kafka": {
"replicas": 1,
"version": "3.8.0",
"storage": {
"type": "ephemeral",
},
"metadataVersion": "3.8-IV0",
"listeners": [
{
"name": "plain",
"port": 9092,
"type": "internal",
"tls": False,
},
{
"name": "tls",
"port": 9093,
"type": "internal",
"tls": True,
},
],
"config": {
"offsets.topic.replication.factor": 1,
"transaction.state.log.replication.factor": 1,
"transaction.state.log.min.isr": 1,
"default.replication.factor": 1,
"min.insync.replicas": 1,
},
},
"entityOperator": {
"topicOperator": {},
"userOperator": {},
},
},
)
kafka_topic = k8s.apiextensions.CustomResource(
"example-kafka-topic",
api_version="kafka.strimzi.io/v1beta2",
kind="KafkaTopic",
metadata={
"name": "example-kafka-topic",
"labels": {
"strimzi.io/cluster": "example-kafka-cluster",
},
"namespace": kafka_namespace.metadata["name"],
},
spec={
"partitions": 5,
"replicas": 1,
"config": {
"retention.ms": 7200000,
"segment.bytes": 1073741824,
},
},
)
```
```
package main
import (
k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)
func main() {
pulumi.Run(func(ctx *pulumi.Context) error {
_, err = apiv1.NewCustomResource(ctx, "flux", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("fluxcd.controlplane.io/v1"),
Kind: pulumi.String("FluxInstance"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("flux"),
Namespace: pulumi.String("flux-system"),
Annotations: pulumi.StringMap{
"fluxcd.controlplane.io/reconcileEvery": pulumi.String("1h"),
"fluxcd.controlplane.io/reconcileTimeout": pulumi.String("5m"),
},
},
OtherFields: k8s.UntypedArgs{
"distribution": pulumi.Map{
"version": pulumi.String("2.x"),
"registry": pulumi.String("ghcr.io/fluxcd"),
"artifact": pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"),
},
"components": pulumi.StringArray{
pulumi.String("source-controller"),
pulumi.String("kustomize-controller"),
pulumi.String("helm-controller"),
pulumi.String("notification-controller"),
pulumi.String("image-reflector-controller"),
pulumi.String("image-automation-controller"),
},
"cluster": pulumi.Map{
"type": pulumi.String("kubernetes"),
"multitenant": pulumi.Bool(false),
"networkPolicy": pulumi.Bool(true),
"domain": pulumi.String("cluster.local"),
},
"kustomize": pulumi.Map{
"patches": pulumi.Array{
pulumi.Map{
"target": pulumi.Map{
"kind": pulumi.String("Deployment"),
"name": pulumi.String("(kustomize-controller|helm-controller)"),
},
"patch": pulumi.Array{
pulumi.Map{
"op": pulumi.String("add"),
"path": pulumi.String("/spec/template/spec/containers/0/args/-"),
"value": pulumi.String("--concurrent=10"),
},
pulumi.Map{
"op": pulumi.String("add"),
"path": pulumi.String("/spec/template/spec/containers/0/args/-"),
"value": pulumi.String("--requeue-dependency=5s"),
},
},
},
},
},
},
})
if err != nil {
return err
}
_, err = apiv1.NewCustomResource(ctx, "example-kafka-node-pool", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
Kind: pulumi.String("KafkaNodePool"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("example-kafka-node-pool"),
Namespace: pulumi.String("kafka"),
Labels: pulumi.StringMap{
"strimzi.io/cluster": pulumi.String("example-kafka-cluster"),
},
},
OtherFields: k8s.UntypedArgs{
"replicas": pulumi.Int(1),
"roles": pulumi.StringArray{
pulumi.String("controller"),
pulumi.String("broker"),
},
"storage": pulumi.Map{
"type": pulumi.String("ephemeral"),
},
},
})
if err != nil {
return err
}
_, err = apiv1.NewCustomResource(ctx, "example-kafka-cluster", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
Kind: pulumi.String("Kafka"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("example-kafka-cluster"),
Namespace: pulumi.String("kafka"),
Annotations: pulumi.StringMap{
"strimzi.io/kraft": pulumi.String("enabled"),
"strimzi.io/node-pools": pulumi.String("enabled"),
},
},
OtherFields: k8s.UntypedArgs{
"kafka": pulumi.Map{
"replicas": pulumi.Int(1),
"version": pulumi.String("3.8.0"),
"storage": pulumi.Map{
"type": pulumi.String("ephemeral"),
},
"metadataVersion": pulumi.String("3.8-IV0"),
"listeners": pulumi.Array{
pulumi.Map{
"name": pulumi.String("plain"),
"port": pulumi.Int(9092),
"type": pulumi.String("internal"),
"tls": pulumi.Bool(false),
},
pulumi.Map{
"name": pulumi.String("tls"),
"port": pulumi.Int(9093),
"type": pulumi.String("internal"),
"tls": pulumi.Bool(true),
},
},
"config": pulumi.Map{
"offsets.topic.replication.factor": pulumi.Int(1),
"transaction.state.log.replication.factor": pulumi.Int(1),
"transaction.state.log.min.isr": pulumi.Int(1),
"default.replication.factor": pulumi.Int(1),
"min.insync.replicas": pulumi.Int(1),
},
},
"entityOperator": pulumi.Map{
"topicOperator": pulumi.Map{},
"userOperator": pulumi.Map{},
},
},
})
if err != nil {
return err
}
_, err = apiv1.NewCustomResource(ctx, "example-kafka-topic", &apiv1.CustomResourceArgs{
ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
Kind: pulumi.String("KafkaTopic"),
Metadata: &metav1.ObjectMetaArgs{
Name: pulumi.String("example-kafka-topic"),
Namespace: pulumi.String("kafka"),
Labels: pulumi.StringMap{
"strimzi.io/cluster": pulumi.String("example-kafka-cluster"),
},
},
OtherFields: k8s.UntypedArgs{
"partitions": pulumi.Int(5),
"replicas": pulumi.Int(1),
"config": pulumi.Map{
"retention.ms": pulumi.Int(7200000),
"segment.bytes": pulumi.Int(1073741824),
},
},
})
if err != nil {
return err
}
return nil
})
}
```
```
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;
class KafkaNodePoolArgs : CustomResourceArgs
{
public string ApiVersion { get; set; }
public string Kind { get; set; }
public ObjectMetaArgs Metadata { get; set; }
public Dictionary<string, object> Spec { get; set; }
public KafkaNodePoolArgs(string apiVersion, string kind) : base(apiVersion, kind)
{
}
}
class KafkaClusterArgs : CustomResourceArgs
{
public string ApiVersion { get; set; }
public string Kind { get; set; }
public ObjectMetaArgs Metadata { get; set; }
public Dictionary<string, object> Spec { get; set; }
public KafkaClusterArgs(string apiVersion, string kind) : base(apiVersion, kind)
{
}
}
class KafkaTopicArgs : CustomResourceArgs
{
public string ApiVersion { get; set; }
public string Kind { get; set; }
public ObjectMetaArgs Metadata { get; set; }
public Dictionary<string, object> Spec { get; set; }
public KafkaTopicArgs(string apiVersion, string kind) : base(apiVersion, kind)
{
}
}
class MyStack : Stack
{
public MyStack()
{
var kafkaNodePool = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaNodePool", new KafkaNodePoolArgs("kafka.strimzi.io/v1beta2", "KafkaNodePool")
{
ApiVersion = "kafka.strimzi.io/v1beta2",
Kind = "KafkaNodePool",
Metadata = new ObjectMetaArgs
{
Name = "example-kafka-node-pool",
Labels =
{
{ "strimzi.io/cluster", "example-kafka-cluster" }
}
},
Spec = new Dictionary<string, object>
{
{ "replicas", 1 },
{ "roles", new List<string> { "controller", "broker" } },
{ "storage", new Dictionary<string, object> { { "type", "ephemeral" } } }
}
});
var kafkaCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaCluster", new KafkaClusterArgs("kafka.strimzi.io/v1beta2", "Kafka")
{
ApiVersion = "kafka.strimzi.io/v1beta2",
Kind = "Kafka",
Metadata = new ObjectMetaArgs
{
Name = "example-kafka-cluster",
Annotations =
{
{ "strimzi.io/kraft", "enabled" },
{ "strimzi.io/node-pools", "enabled" }
}
},
Spec = new Dictionary<string, object>
{
{ "kafka", new Dictionary<string, object> {
{ "replicas", 1 },
{ "version", "3.8.0" },
{ "storage", new Dictionary<string, object> { { "type", "ephemeral" } } },
{ "metadataVersion", "3.8-IV0" },
{ "listeners", new List<Dictionary<string, object>> {
new Dictionary<string, object> {
{ "name", "plain" },
{ "port", 9092 },
{ "type", "internal" },
{ "tls", false }
},
new Dictionary<string, object> {
{ "name", "tls" },
{ "port", 9093 },
{ "type", "internal" },
{ "tls", true }
}
}},
{ "config", new Dictionary<string, object> {
{ "offsets.topic.replication.factor", 1 },
{ "transaction.state.log.replication.factor", 1 },
{ "transaction.state.log.min.isr", 1 },
{ "default.replication.factor", 1 },
{ "min.insync.replicas", 1 }
}}
}},
{ "entityOperator", new Dictionary<string, object> {
{ "topicOperator", new Dictionary<string, object>() },
{ "userOperator", new Dictionary<string, object>() }
}}
}
});
var kafkaTopic = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaTopic", new KafkaTopicArgs("kafka.strimzi.io/v1beta2", "KafkaTopic")
{
ApiVersion = "kafka.strimzi.io/v1beta2",
Kind = "KafkaTopic",
Metadata = new ObjectMetaArgs
{
Name = "example-kafka-topic",
Labels =
{
{ "strimzi.io/cluster", "example-kafka-cluster" }
}
},
Spec = new Dictionary<string, object>
{
{ "partitions", 5 },
{ "replicas", 1 },
{ "config", new Dictionary<string, object> {
{ "retention.ms", 7200000 },
{ "segment.bytes", 1073741824 }
}}
}
});
}
}
class Program
{
static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
```
#### Summary
The Strimzi Operator demonstrates the power of Kubernetes Operators by providing full lifecycle management for Apache Kafka on Kubernetes. It takes care of the heavy lifting of deploying and managing Kafka clusters, making the Strimzi Operator a valuable tool that should be part of every Kubernetes-powered platform, as it covers a wide range of use cases.

## Conclusion
In this blog post, I highlighted the importance of Kubernetes Operators for platform engineers and how they can harness the advanced automation capabilities of operators to simplify deploying, managing, and scaling applications and services on Kubernetes.

I provided some examples of advanced Kubernetes operators that I recommend, but if you want to try using Kubernetes Operators in your Kubernetes-powered platform, here are some great guides to get you started with Pulumi and Kubernetes:

## Get Started with Pulumi
Use Pulumi's open-source SDK to create, deploy, and manage infrastructure on any cloud.