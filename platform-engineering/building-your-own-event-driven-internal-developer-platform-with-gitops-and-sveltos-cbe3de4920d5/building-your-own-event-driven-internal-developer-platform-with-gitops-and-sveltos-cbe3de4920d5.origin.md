# Building Your Own Event-Driven Internal Developer Platform with GitOps and Sveltos
## Discover how to create an event-driven cloud environment that mirrors the architecture used by cloud providers
Note:this is a hands-on guide requiring experience with Kubernetes and Helm. To follow along with this tutorial, you’ll also need three running Kubernetes clusters.
If you believe in open source and share this philosophy,[please consider leaving a ⭐️]to support those who make these amazing tools available and enable setups like this!
Imagine you’re a user visiting a portal of an provider XY, exploring their Database as a Service or managed database offerings. You click a button or call an API (if provided), and voilà — your database instance is ready. But have you ever wondered, *Is this database really running on a traditional virtual machine?* It feels more like it’s operating within a **Kubernetes cluster**, doesn’t it? Did you ever ask yourself, how they build this cloud based environment on the backbone of an Internal Developer Platform in make them available in a portal?

Let’s go with that thought: imagine the database is indeed running on Kubernetes. What happens the moment you hit **“create”**? This action triggers an event resource, specifying when and how the database cluster should be deployed. At this point, **Sveltos** steps in, managing deployment to the appropriate cluster, retrieving necessary configurations, and providing the details you need to connect to your database seamlessly.

While I can’t reveal every technical detail behind building a cloud like the major providers (let’s avoid any legal headaches!) or maybe I will build my own IDP solution. I’ll guide you through setting up a similar event-driven cloud architecture. We’ll break down each component, and by the end, you’ll have a solid understanding — and maybe even a new cloud based on a IDP of your own in the making!

# Quick Overview
Before we dive in, here’s what you need to know: This guide is fully hands-on, starting from scratch! All you’ll need are three running clusters:

**Management Cluster****Service Cluster****Workload/Application Cluster**
We’ll be walking through the following steps:

**Install Prerequisites**: Set up`sveltosctl`
,`cert-manager`
, and`sveltos`
, and apply the necessary labels on the management cluster.**Register the Service Cluster**: Prepare the service cluster for managing deployments.**Deploy Database Operator**: Install the`cloudnative-pg`
operator on the service cluster.**Automate Database Deployment**: Instruct Sveltos to automatically deploy a Postgres database instance.**Register the Workload Cluster**: Connect the workload cluster to the architecture.**Deploy an Application**: Launch an application that connects to the Postgres database.
Let’s get straight to it. There are two sections A and B below. A is a detailed guide that also explains what happens behind the scenes. B is a short way to quickly deploy things without really understanding them and believe whatever you want to believe.

Let’s get started with Path A or B!

# Path A: The Deep Dive
In this section, we will go together step-by-step, explaining each command and its purpose to give you a deeper understanding of what’s happening behind the scenes

**1. Install sveltosctl, cert-manager, sveltos and add labels on the management cluster**
First, let’s [install ](https://github.com/projectsveltos/sveltosctl)
, the command-line tool for interacting with Sveltos. This tool will help us manage deployments across our clusters.[sveltosctl](https://github.com/projectsveltos/sveltosctl)

Here’s how to install it:

`#MacOs`
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-darwin-arm64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
#Linux
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-linux-amd64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
Now, let’s install [Cert-Manager](https://cert-manager.io) using [Helm](https://helm.sh). This tool manages certificates for us, which is crucial for secure communication between clusters.

`helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.16.1 --set crds.enabled=true`
Next, we’ll deploy the [Sveltos stack](https://projectsveltos.github.io/sveltos/getting_started/install/install/) itself via Helm. This step will set up the core Sveltos components on our management cluster.

`helm install projectsveltos projectsveltos/projectsveltos -n projectsveltos --create-namespace`
Labeling the management cluster helps Sveltos identify and organize clusters by type, simplifying deployments later on.

`kubectl label sveltoscluster -n mgmt mgmt type=mgmt`
To allow Sveltos to work with resources like *ConfigMaps* and *Secrets*, we need to add specific permissions. Here’s how to patch the `addon-controller-role-extra`
*ClusterRole* for this purpose:

`kubectl patch clusterrole addon-controller-role-extra --type='json' -p='[`
{
"op": "add",
"path": "/rules",
"value": [
{
"apiGroups": [""],
"resources": ["configmaps", "secrets"],
"verbs": ["*"]
}
]
}
]'
Congratulations! You’ve completed the foundational setup. Let’s continue with Step 2.

**2. Register the service cluster**
This step is straightforward, thanks to `sveltosctl`
. Here’s how to connect the management cluster to the service cluster:

`kubectl create ns service-cluster`
sveltosctl register cluster --namespace=service-cluster --cluster=service-cluster --fleet-cluster-context=service-cluster --labels=type=services
In this step we created the connection between the management cluster and the managed service cluster. But lets take a look on the provided parameter to get a better understand:

`--namaespace=service-cluster`
: will create the namespace for the managed cluster in the management cluster
`--cluster=service-cluster`
: will add a name to the managed cluster in the CustomResource sveltoscluster
`--fleet-cluster-context=service-cluster`
: will use your context name to access the cluster that should be managed by sveltos. In my case it is service-cluster
`--labels=types=services`
: will add label to the added managed cluster into the CustomResource sveltoscluster, which allow deploy apps based on the labels.
To verify the labels, use the following command:

`kubectl get sveltoscluster -A --show-labels`
NAMESPACE NAME READY VERSION LABELS
mgmt mgmt true v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=mgmt
service-cluster service-cluster true v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=services
This setup enables Sveltos to recognize and manage the service cluster based on labels, which will come in handy for deploying applications.

If you’re curious about how Sveltos manages add-ons, feel free to explore [further resources](https://projectsveltos.github.io/sveltos/addons/addons/). For now, let’s continue by deploying the
operator to help set up the managed service on the service cluster.[cloudnative-pg](https://cloudnative-pg.io)

**3. Deploy cloudnative-pg Operator on the service cluster**
To deploy the CloudNative-PG operator, we’ll apply a `ClusterProfile`
*CustomResource* on the management cluster. This `ClusterProfile`
instructs Sveltos to deploy the operator on clusters that match specific labels.

Run the following command to apply the `ClusterProfile`
:

`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/cloudnative-pg.yaml`
After this step, our setup will look like this:

**What is a ClusterProfile?**
A `ClusterProfile`
acts like a blueprint that defines which resources should be deployed on clusters that match certain labels. In this case, the profile targets clusters labeled as `type=services`
and instructs Sveltos to install the [CloudNative-PG Helm chart](https://github.com/cloudnative-pg/charts) there. Here’s what it looks like:

`---`
apiVersion: config.projectsveltos.io/v1beta1
kind: ClusterProfile
metadata:
name: deploy-cnpg
spec:
clusterSelector:
matchLabels:
type: services
syncMode: Continuous
helmCharts:
- repositoryURL: https://cloudnative-pg.github.io/charts
repositoryName: cloudnative-pg
chartName: cloudnative-pg/cloudnative-pg
chartVersion: 0.22.1
releaseName: cnpg
releaseNamespace: cnpg-system
helmChartAction: Install
In this example, any cluster with the label `type=services`
will have the CloudNative-PG Helm chart automatically installed, continuously synchronizing as specified.

To check the resources deployed on the service cluster, you can use:

`sveltosctl show addons `
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| CLUSTER | RESOURCE TYPE | NAMESPACE | NAME | VERSION | TIME | PROFILES |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| service-cluster/service-cluster | helm chart | cnpg-system | cnpg | 0.22.1 | 2024-11-02 11:35:40 +0100 CET | ClusterProfile/deploy-cnpg |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
This confirms that the CloudNative-PG operator has been successfully deployed on the service cluster.

**4. Instruct Sveltos to automatically deploy Postgres DB**
In this step, we’ll configure Sveltos to automatically deploy a PostgreSQL database on clusters labeled with `postgres=required`
. Whenever Sveltos detects a managed cluster with this label, it will:

- Create a PostgreSQL instance on the cluster.
- Expose the database via a LoadBalancer service.
- Retrieve the credentials and connection details, including the external IP and port.
To enable this, apply the following configurations:

`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/auto-deploy-postgres-cluster.yaml`
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/fetch-postgres-data.yaml
These configurations set up two workflows:

**Auto-Deploy PostgreSQL Cluster**: Deploys PostgreSQL on clusters labeled with`type=services`
when triggered.**Fetch PostgreSQL Cluster Data**: Retrieves connection data and credentials for PostgreSQL clusters based on specific events.
The **first workflow** will be like:

**Auto-Deploy PostgreSQL Cluster**
In Sveltos, the **EventSource** defines specific events (such as creation or deletion of resources) to watch in Kubernetes clusters, while the **EventTrigger** specifies which add-ons or applications to deploy in response to these events.

This how the applied resources looks like:

`# Anytime a SveltosCluster with label postgres: required`
# is created, deploys a postgres cluster.
# Source cluster is the management cluster.
# Destination cluster is the cluster with label type:services
apiVersion: lib.projectsveltos.io/v1beta1
kind: EventSource
metadata:
name: detect-cluster-requiring-postgres
spec:
collectResources: true
resourceSelectors:
- group: "lib.projectsveltos.io"
version: "v1beta1"
kind: "SveltosCluster"
labelFilters:
- key: postgres
operation: Equal
value: required
---
apiVersion: lib.projectsveltos.io/v1beta1
kind: EventTrigger
metadata:
name: deploy-postgres-cluster
spec:
sourceClusterSelector:
matchLabels:
type: mgmt
destinationClusterSelector:
matchLabels:
type: services
eventSourceName: detect-cluster-requiring-postgres
oneForEvent: true
policyRefs:
- name: postgres-cluster
namespace: default
kind: ConfigMap
---
apiVersion: v1
data:
cluster.yaml: |
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
name: cluster-{{ .Resource.metadata.name }}
namespace: {{ .Resource.metadata.namespace }}
labels:
cluster: {{ .Resource.metadata.namespace }}-{{ .Resource.metadata.name }}
spec:
instances: 3
bootstrap:
initdb:
database: todo
storage:
size: 1Gi
managed:
services:
disabledDefaultServices: ["ro", "r"]
additional:
- selectorType: rw
serviceTemplate:
metadata:
name: cluster-rw-lb
spec:
type: LoadBalancer
kind: ConfigMap
metadata:
annotations:
projectsveltos.io/instantiate: ok
name: postgres-cluster
namespace: default
And here is the explaination what will happen and how Sveltos handle it.

**EventSource Definition**: The EventSource`detect-cluster-requiring-postgres`
monitors the creation of any`SveltosCluster`
object labeled with`postgres: required`
. When such a labeled cluster is created, Sveltos detects this as a significant event.**EventTrigger Definition**: The EventTrigger`deploy-postgres-cluster`
is triggered when the above event occurs. It is configured to deploy the PostgreSQL cluster in a target cluster labeled`type: services`
, with the source being the management cluster labeled`type: mgmt`
.**PostgreSQL Cluster Deployment**: The EventTrigger references a`ConfigMap`
(`postgres-cluster`
) that contains a template to define a PostgreSQL cluster. When the event is triggered, Sveltos uses this template to create a new PostgreSQL cluster in the target cluster. The template dynamically incorporates details like the name and namespace of the originating cluster.
In summary, Sveltos watches for specific labels on clusters and, when it detects a match, automatically deploys a PostgreSQL cluster in a designated target cluster.

The **Second workflow** composite of two workflows and looks like:

**Fetch PostgreSQL Cluster Data**
In this setup, Sveltos is configured to retrieve PostgreSQL credentials and load balancer information from a services cluster and make them accessible in the management cluster:

**Fetching PostgreSQL Credentials**:
**EventSource**:`detect-credentials-secret`
monitors for`Secret`
objects in the services cluster that have the label`cnpg.io/reload: true`
. This label indicates that the secret contains PostgreSQL credentials.**EventTrigger**:`credentials-secret`
is activated when such a`Secret`
is detected in any cluster labeled`type: services`
. It initiates the creation of a`Secret`
in the management cluster (labeled`type: mgmt`
) with the PostgreSQL credentials.**ConfigMap Template**: The`credentials`
ConfigMap contains a template to create a`Secret`
named`pg-credentials`
in the management cluster. This template dynamically pulls the username and password from the original Secret in the services cluster, allowing Sveltos to replicate these credentials securely.
**Fetching Load Balancer Information**:
**EventSource**:`detect-loadbalancer`
monitors for`Service`
objects in the services cluster labeled`cnpg.io/isManaged: true`
, indicating they are managed PostgreSQL load balancers.**EventTrigger**:`cnpg-loadbalancer-data`
triggers when such a Service is detected, and it creates a ConfigMap in the management cluster to store the load balancer’s external IP and port information.**ConfigMap Template**: The`loadbalancer-data`
ConfigMap template is used to generate a ConfigMap named`pg-loadbalancer-data`
in the management cluster. It populates this ConfigMap with the load balancer’s external IP address and port, enabling external access to the PostgreSQL instance from the management cluster.
This setup allows the management cluster to have **secure and dynamic** access to PostgreSQL credentials and connection details for instances deployed in the services cluster.

Next, let’s register the workload cluster to trigger events in the following steps.

**5. Register the workload cluster**
Now, let’s register the workload cluster with Sveltos. By labeling this cluster with `postgres=required`
, we instruct Sveltos to deploy a new PostgreSQL instance on the service cluster and gather the necessary connection details. Here’s how to register the workload cluster:

`kubectl create ns workload-cluster`
sveltosctl register cluster --namespace=workload-cluster --cluster=workload-cluster --fleet-cluster-context=workload-cluster --labels=postgres=required
Once the cluster is registered, Sveltos automatically triggers the workflows (Events) we set up in Step 4. Here’s what happens behind the scenes:

**Triggering Deployment and Data Collection**
Sveltos creates`ClusterProfiles`
and`ConfigMaps`
using the templates defined in the previous`EventTrigger`
configurations. Based on these templates, it deploys a PostgreSQL cluster in the service cluster under the`workload-cluster`
namespace. It also retrieves and stores the database’s connection information (such as credentials and load balancer IP) in the management cluster’s under the workload-cluster namespace.**Automatic Creation of ClusterProfile and ConfigMap**
Sveltos generates a`ClusterProfile`
that targets the`type=services`
cluster, referencing the new ConfigMap created from the template. Here’s an example of the generated`ClusterProfile`
:
This will looks like:

So Sveltos create *ClusterProfiles* based that matches the destination cluster. It also have this *ClusterProfile* reference the newly created *ConfigMap* from the Template.

So you can see a new *ClusterProfile* is created like:

`apiVersion: config.projectsveltos.io/v1beta1`
kind: ClusterProfile
metadata:
finalizers:
- clusterprofilefinalizer.projectsveltos.io
generation: 1
labels:
eventtrigger.lib.projectsveltos.io/clusterNamespace: mgmt
eventtrigger.lib.projectsveltos.io/clustername: mgmt
eventtrigger.lib.projectsveltos.io/clustertype: Sveltos
eventtrigger.lib.projectsveltos.io/eventreportname: detect-cluster-requiring-postgres
eventtrigger.lib.projectsveltos.io/eventtriggername: deploy-postgres-cluster
eventtrigger.lib.projectsveltos.io/resourcename: workload-cluster
eventtrigger.lib.projectsveltos.io/resourcenamespace: workload-cluster
projectsveltos.io/cluster-name: service-cluster
projectsveltos.io/cluster-profile-name: sveltos-j7dn263no745a5e58uya
projectsveltos.io/cluster-type: Sveltos
name: sveltos-j7dn263no745a5e58uya
spec:
clusterSelector:
matchLabels:
type: services
continueOnConflict: false
policyRefs:
- deploymentType: Remote
kind: ConfigMap
name: sveltos-bnnnp8dv2ndb8i7dx1vo
namespace: projectsveltos
reloader: false
stopMatchingBehavior: WithdrawPolicies
syncMode: Continuous
tier: 100
and here you can see that reference *ConfigMap*, that have the *CustomResource* for creating a *Cluster* inside:

`apiVersion: v1`
kind: ConfigMap
metadata:
labels:
eventtrigger.lib.projectsveltos.io/clusterNamespace: mgmt
eventtrigger.lib.projectsveltos.io/clustername: mgmt
eventtrigger.lib.projectsveltos.io/clustertype: Sveltos
eventtrigger.lib.projectsveltos.io/eventreportname: detect-cluster-requiring-postgres
eventtrigger.lib.projectsveltos.io/eventtriggername: deploy-postgres-cluster
eventtrigger.lib.projectsveltos.io/refname: postgres-cluster
eventtrigger.lib.projectsveltos.io/refnamespace: default
eventtrigger.lib.projectsveltos.io/resourcename: workload-cluster
eventtrigger.lib.projectsveltos.io/resourcenamespace: workload-cluster
name: sveltos-bnnnp8dv2ndb8i7dx1vo
namespace: projectsveltos
data:
cluster.yaml: |
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
name: cluster-workload-cluster
namespace: workload-cluster
labels:
cluster: workload-cluster-workload-cluster
spec:
instances: 3
bootstrap:
initdb:
database: todo
storage:
size: 1Gi
managed:
services:
disabledDefaultServices: ["ro", "r"]
additional:
- selectorType: rw
serviceTemplate:
metadata:
name: cluster-rw-lb
spec:
type: LoadBalancer
Of course, this is just one example — you can do much more, such as using Helm to install a chart via triggers, eliminating the need to specify it in a *ConfigMap (*More on this at the end).

Now, let’s verify that Sveltos has successfully deployed the PostgreSQL instance and fetched the connection details. To check the credentials, use:

`kubectl get secret -n workload-cluster`
#output
Name TYPE DATA AGE
workload-cluster-sveltos-kubeconfig Opaque 1 47h
pg-credentials Opaque 2 47h
The `pg-credentials`
secret contains the PostgreSQL credentials:

`data:`
password: bTloa....
user: d...
To check the connection details (external IP and port), use:

`kubectl get configmap -n workload-cluster service-cluster-loadbalancer-data -oyaml 04.11.24 11:32:44 management-cluster/default ⎈`
#output like
apiVersion: v1
data:
external-ip: 212.2.....
port: "5432"
This completes the setup, with the management cluster now able to access the PostgreSQL instance’s connection details and credentials securely and automatically.

**6. Deploy an application that access the Postgres DB**
Sveltos can now be used to deploy a *Job* in the workload-cluster cluster. This *Job* will access the Postgres DB running on the services-cluster.

This *Job* is expressed as a template and will be deployed by Sveltos in any cluster with the label `type=app`
.

`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/job-to-create-table.yaml`
kubectl label sveltoscluster -n workloadcluster workload-cluster type=app
The change will then look like this:

It establishes a connection to the workload-cluster, creating a new ClusterProfile, which instructs Sveltos to deploy a *Job* on the cluster matching `type=app`
.

If you take a closer look at the *ClusterProfile*:

`apiVersion: config.projectsveltos.io/v1beta1`
kind: ClusterProfile
metadata:
finalizers:
- clusterprofilefinalizer.projectsveltos.io
name: deploy-job
spec:
clusterSelector:
matchLabels:
type: app
continueOnConflict: false
policyRefs:
- deploymentType: Remote
kind: ConfigMap
name: job-to-create-table
namespace: default
reloader: false
stopMatchingBehavior: WithdrawPolicies
syncMode: Continuous
templateResourceRefs:
- identifier: Credentials
resource:
apiVersion: v1
kind: Secret
name: pg-credentials
- identifier: LoadBalancer
resource:
apiVersion: v1
kind: ConfigMap
name: pg-loadbalancer-data
tier: 100
Here’s what happens:

- Sveltos uses the ConfigMap
`job-to-create-table`
in the`default`
namespace. - It replaces values in the template with data from the Secret
`pg-credentials`
and*ConfigMap*`pg-loadbalancer-data`
, setting the namespace based on the matching label`type=app`
(workload-cluster). - Sveltos then creates a Job using the fetched information on the remote cluster that matches the label
`type=app`
(in our case workload-cluster).
You can check if the provisioning is working as expected with:

`kubectl get clustersummaries -A -owide`
NAMESPACE NAME HELMCHARTS KUSTOMIZEREFS POLICYREFS
mgmt sveltos-1a6ec1ce3bandndeqixd-sveltos-mgmt Provisioned
mgmt sveltos-p46z943e935h2vtev56i-sveltos-mgmt Provisioned
service-cluster deploy-cnpg-sveltos-service-cluster Provisioned
service-cluster sveltos-xind5b6qvvrnbeur2flf-sveltos-service-cluster Provisioned
workload-cluster deploy-job-sveltos-workload-cluster Provisioned
You should now see the* Job *`todo-table`
running in the workload-cluster.

# Path B: The Shortcut
**1. Install sveltosctl, cert-manager, sveltos and add labels on the management cluster**
`#MacOs`
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-darwin-arm64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
#Linux
sudo wget https://github.com/projectsveltos/sveltosctl/releases/download/v0.41.1/sveltosctl-linux-amd64 -O /usr/local/bin/sveltosctl
sudo chmod +x /usr/local/bin/sveltosctl
#Cert-Manager
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.16.1 --set crds.enabled=true
#Sveltos
helm install projectsveltos projectsveltos/projectsveltos -n projectsveltos --create-namespace
#Label management cluster
kubectl label sveltoscluster -n mgmt mgmt type=mgmt
#grant extra permission.
kubectl patch clusterrole addon-controller-role-extra --type='json' -p='[
{
"op": "add",
"path": "/rules",
"value": [
{
"apiGroups": [""],
"resources": ["configmaps", "secrets"],
"verbs": ["*"]
}
]
}
]'
## 2. Register the Service Cluster
`kubectl create ns service-cluster`
sveltosctl register cluster --namespace=service-cluster --cluster=service-cluster --fleet-cluster-context=service-cluster --labels=type=services
Check labels:

`kubectl get sveltoscluster -A --show-labels`
NAMESPACE NAME READY VERSION LABELS
mgmt mgmt true v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=mgmt
service-cluster service-cluster true v1.29.2+k3s1 projectsveltos.io/k8s-version=v1.29.2,sveltos-agent=present,type=services
## 3. Deploy CloudNative-PG Operator on the Service Cluster
`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/cloudnative-pg.yaml`
Now you can see the deployed resources on the service cluster with:

`sveltosctl show addons `
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| CLUSTER | RESOURCE TYPE | NAMESPACE | NAME | VERSION | TIME | PROFILES |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
| service-cluster/service-cluster | helm chart | cnpg-system | cnpg | 0.22.1 | 2024-11-02 11:35:40 +0100 CET | ClusterProfile/deploy-cnpg |
+-----------------------------------+----------------------------+------------------+-----------------------------------+---------+-------------------------------+---------------------------------------------+
## 4. Instruct Sveltos to Automatically Deploy a PostgreSQL Database
`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/auto-deploy-postgres-cluster.yaml`
kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/fetch-postgres-data.yaml
## 5. Register the Workload Cluster
`kubectl create ns workload-cluster`
sveltosctl register cluster --namespace=workload-cluster --cluster=workload-cluster --fleet-cluster-context=workload-cluster --labels=postgres=required
Now Verify Sveltos deployed the Postgres Cluster and fetched the necessary info to connect:

`kubectl get secret -n workload-cluster`
#output
Name TYPE DATA AGE
workload-cluster-sveltos-kubeconfig Opaque 1 47h
pg-credentials Opaque 2 47h
## 6. Deploy an Application that Accesses the PostgreSQL Database
`kubectl apply -f https://raw.githubusercontent.com/projectsveltos/sveltos/main/docs/assets/job-to-create-table.yaml`
kubectl label sveltoscluster -n workload-cluster workload-cluster type=app
Check if provisioning worked as expected:

`kubectl get clustersummaries -A -owide`
NAMESPACE NAME HELMCHARTS KUSTOMIZEREFS POLICYREFS
mgmt sveltos-1a6ec1ce3bandndeqixd-sveltos-mgmt Provisioned
mgmt sveltos-p46z943e935h2vtev56i-sveltos-mgmt Provisioned
service-cluster deploy-cnpg-sveltos-service-cluster Provisioned
service-cluster sveltos-xind5b6qvvrnbeur2flf-sveltos-service-cluster Provisioned
workload-cluster deploy-job-sveltos-workload-cluster Provisioned
You should now see the Job `todo-table`
running in the workload-cluster.

**Congratulations!** You’ve created an event-driven, managed Database-as-a-Service! You can further extend this setup by defining jobs that trigger credential sharing with users or services referenced by the UI, as shown in the initial example.
# Wrapping Up
I can imagine you’re now wondering, where’s the GitOps part? The headline was meant to catch your attention? No. In reality, the Sveltos Addon-Controller workflow is based on the GitOps approach, but for a full GitOps experience, you can pair [Sveltos with Flux CD — it’s already integrate](https://projectsveltos.github.io/sveltos/addons/example_flux_sources/)d. Why use Flux CD? To deploy *ClusterProfiles* and apply another Sveltos *CustomResources*, you’ll need GitOps Tools like [Flux CD](https://www.google.com/search?client=safari&rls=en&q=flux+cd&ie=UTF-8&oe=UTF-8).

This was just a small part of how you could implement it. Sveltos offers many different possibilities for providing event-driven managed services. At the same time, the managed service can be integrated into an internal developer platform to offer teams a self-service approach.

We have depicted the following scenario:

Thus, we have created a 1:1 relationship between a workload cluster and a PostgreSQL cluster on the service cluster because we configured our ClusterProfiles based on the clusters’ labels.

There’s also an option to build something like this:

Instead of responding to the cluster’s labels, you could use a ConfigMap, for example, that indicates the need for a PostgreSQL cluster. Based on this, Sveltos can then create multiple PostgreSQL clusters per namespace/ConfigMap. This would be too much for this blog, but you can find instructions on [how to do it HERE:](https://projectsveltos.github.io/sveltos/events/db-as-a-service-multiple-db-per-cluster/)

Furthermore, if you want to address security concerns and don’t want the credentials for all managed services to reside in the management cluster, you can implement the following:

Here, the credentials are stored in the respective workload cluster.
Hopefully, you can see that the possibilities are enormous, and your imagination might be the only limiting factor here.

If you’re building exciting solutions, feel free to share them in the form of a blog, tutorial, etc. But even more important, if you believe in open-source and live by this philosophy, [please leave a ⭐️](https://github.com/projectsveltos/addon-controller)! Even cooler would be contributing through a blog or, if you’re skilled enough, directly to the [Projectsveltos](https://github.com/projectsveltos) itself.

**P.S.** Please leave a Comment which Path you choose — are you the “I need to know every detail” type, or the “just hit deploy and pray” type? 😬
# Contact Information
Got questions, want to chat, or just keen to stay connected? Skip the Medium comments and let’s connect on [LinkedIn](http://www.linkedin.com/in/lajko) 🤙. Don’t forget to subscribe to the [Medium Newsletter](/@artem_lajko/subscribe) so you never miss an update!