## Backstage on Kubernetes
![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-10.06.05.png?fit=1990%2C1118&ssl=1)
In this article, you will learn how to integrate Backstage with Kubernetes. We will run Backstage in two different ways. Firstly, it will run outside the cluster and connect with Kubernetes via the API. In the second scenario, we will deploy it directly on the cluster using the official Helm chart. Our instance of Backstage will connect Argo CD and Prometheus deployed on Kubernetes, to visualize the status of Argo CD synchronization and basic metrics related to the app.

This exercise continues the work described in my previous [article](https://piotrminkowski.com/2024/06/13/getting-started-with-backstage/) about Backstage. So, before you start, you should read that article to understand the whole concept. In many places, I will refer to something that was described and done in the previous article. I’m describing there how to configure and run Backstage, and also how to build a basic template for the sample Spring Boot app. You should be familiar with all those basic terms, to fully understand what happens in the current exercise.

## Source Code
If you would like to try it by yourself, you may always take a look at my source code. Our sample GitHub [repository](https://github.com/piomin/backstage-templates) contains software templates written in the Backstage technology called Skaffolder. In this article, we will analyze a template dedicated to Kubernetes available in the `templates/spring-boot-basic-on-kubernetes`
directory. After cloning this repository, you should just follow my instructions.

Here’s the structure of our repository. Besides the template, it also contains the Argo CD template with YAML deployment manifests to apply on Kubernetes.

```
.
├── skeletons
│ └── argocd
│ └── manifests
│ ├── deployment.yaml
│ └── service.yaml
├── templates
│ └── spring-boot-basic-on-kubernetes
│ ├── skeleton
│ │ ├── README.md
│ │ ├── catalog-info.yaml
│ │ ├── k8s
│ │ │ ├── deployment.yaml
│ │ │ └── kind-cluster-test.yaml
│ │ ├── pom.xml
│ │ ├── renovate.json
│ │ ├── skaffold.yaml
│ │ └── src
│ │ ├── main
│ │ │ ├── java
│ │ │ │ └── ${{values.javaPackage}}
│ │ │ │ ├── Application.java
│ │ │ │ ├── controller
│ │ │ │ │ └── ${{values.domainName}}Controller.java
│ │ │ │ └── domain
│ │ │ │ └── ${{values.domainName}}.java
│ │ │ └── resources
│ │ │ └── application.yml
│ │ └── test
│ │ ├── java
│ │ │ └── ${{values.javaPackage}}
│ │ │ └── ${{values.domainName}}ControllerTests.java
│ │ └── resources
│ │ └── k6
│ │ └── load-tests-add.js
│ └── template.yaml
└── templates.yaml
```
ShellSessionThere is also another Git [repository](https://github.com/piomin/backstage.git) related to this article. It contains the modified source code of Backstage with several plugins installed and configured. The process of extending Backstage with plugins is described in detail in this article. So, you can start from scratch and apply my instructions step by step. But you can clone the final version of the code committed inside that repo and run it on your laptop as well.

## Run and Prepare Kubernetes
Before we start with Backstage, we need to run and configure our instance of the Kubernetes cluster. It can be, for example, Minikube. Once you have the running cluster, you can obtain its control plane URL by executing the following command. As you see, my Minikube is available under the `https://127.0.0.1:55782`
address, so I will have to set it in the Backstage configuration later.

```
$ kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:55782
...
$ export K8S_URL=https://127.0.0.1:55782
```
ShellSessionWe need to install Prometheus and Argo CD on our Kubernetes. In order to install Prometheus, we will use the `kube-prometheus-stack`
Helm chart. Firstly, we should add the Prometheus chart repository with the following command:

`$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
ShellSessionThen, we can run the following command to install Prometheus in the `monitoring`
namespace:

```
$ helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
--version 60.3.0 \
-n monitoring --create-namespace
```
ShellSessionThe same as with Prometheus, for Argo CD we need to add the chart repository first:

`$ helm repo add argo https://argoproj.github.io/argo-helm`
ShellSessionFor Argo CD we need an additional configuration to be provided inside the `values.yaml`
file. We have to create the user for the Backstage with privileges to call HTTP API with the `apiKey`
authentication. It is required to automatically create an Argo CD `Application`
from the Skaffolder template.

```
configs:
cm:
accounts.backstage: apiKey,login
rbac:
policy.csv: |
p, backstage, applications, *, */*, allow
```
YAMLLet’s install Argo CD in the `argocd`
namespace using the settings from `values.yaml`
file:

```
$ helm install argo-cd argo/argo-cd \
--version 7.2.0 \
-f values.yaml \
-n argocd --create-namespace
```
ShellSessionThat’s not all. We still need to generate the `apiKey`
for the `backstage`
user. Firstly, let’s enable port forwarding for both Argo CD and Prometheus services to access their APIs over localhost.

```
$ kubectl port-forward svc/argo-cd-argocd-server 8443:443 -n argocd
$ kubectl port-forward svc/kube-prometheus-stack-prometheus 9090 -n monitoring
```
ShellSessionIn order to generate the apiKey for the backstage user we need to sign in to Argo CD with the `argocd`
CLI as the `admin`
user. Then, we need to run the following command for the backstage account and export the generated token as the `ARGOCD_TOKEN`
env variable:

```
$ argocd account generate-token --account backstage
$ export ARGOCD_TOKEN='argocd.token=<generated_token>'
```
ShellSessionFinally, let’s obtain the long-lived API token for Kubernetes by creating a secret:

```
apiVersion: v1
kind: Secret
metadata:
name: default-token
namespace: default
annotations:
kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
```
YAMLThen, we can copy and export it as the `K8S_TOKEN`
environment variable with the following command:

`$ export K8S_TOKEN=$(kubectl get secret default-token -o go-template='{{.data.token | base64decode}}')`
ShellSessionJust for the testing purposes, we add the `cluster-admin`
role to the default `ServiceAccount`
.

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
name: default-admin
subjects:
- kind: ServiceAccount
name: default
namespace: default
roleRef:
kind: ClusterRole
name: cluster-admin
apiGroup: rbac.authorization.k8s.io
```
YAML## Modify App Source Code Skeleton for Kubernetes
First of all, we will modify several things in the application source code skeleton. In order to build the container image, we include the `jib-maven-plugin`
in the Maven `pom.xml`
. This plugin will be activated under the `jib`
Maven profile.

```
<profiles>
<profile>
<id>jib</id>
<activation>
<activeByDefault>false</activeByDefault>
</activation>
<build>
<plugins>
<plugin>
<groupId>com.google.cloud.tools</groupId>
<artifactId>jib-maven-plugin</artifactId>
<version>3.4.3</version>
<configuration>
<from>
<image>eclipse-temurin:21-jdk-ubi9-minimal</image>
</from>
</configuration>
</plugin>
</plugins>
</build>
</profile>
</profiles>
```
XMLOur source code repository will also contain the Skaffold configuration file. With Skaffold we can easily build an image and deploy an app to Kubernetes in a single step. The address of the image depends on the `orgName`
and `appName`
parameters in the Skaffolder template. During the image build we skip the tests and activate the Maven `jib`
profile.

```
apiVersion: skaffold/v4beta5
kind: Config
metadata:
name: ${{ values.appName }}
build:
artifacts:
- image: ${{ values.orgName }}/${{ values.appName }}
jib:
args:
- -Pjib
- -DskipTests
manifests:
rawYaml:
- k8s/deployment.yaml
deploy:
kubectl: {}
```
YAMLIn order to deploy the app on Kubernetes, Skaffold is looking for the `k8s/deployment.yaml`
manifest. We will use this deployment manifest only for development and automated test purposes. In the “production” we will keep the YAML manifests in a separate Git repository and apply them through Argo CD. Once we provide a change in the source CircleCI will try to deploy the app on the temporary Kind cluster. Therefore, our `Service`
is exposed as a `NodePort`
under the `30000`
port.

```
apiVersion: apps/v1
kind: Deployment
metadata:
name: ${{ values.appName }}
spec:
selector:
matchLabels:
app: ${{ values.appName }}
template:
metadata:
annotations:
prometheus.io/path: /actuator/prometheus
prometheus.io/scrape: "true"
prometheus.io/port: "8080"
labels:
app: ${{ values.appName }}
spec:
containers:
- name: ${{ values.appName }}
image: ${{ values.orgName }}/${{ values.appName }}
ports:
- containerPort: 8080
readinessProbe:
httpGet:
port: 8080
path: /actuator/health/readiness
scheme: HTTP
timeoutSeconds: 1
periodSeconds: 10
successThreshold: 1
failureThreshold: 3
resources:
limits:
memory: 1024Mi
---
apiVersion: v1
kind: Service
metadata:
name: ${{ values.appName }}
spec:
type: NodePort
selector:
app: ${{ values.appName }}
ports:
- port: 8080
nodePort: 30000
```
YAMLLet’s switch to the CircleCi configuration file. It also contains several changes related to Kubernetes. We need to include the `image-build`
job responsible for building and pushing the app image to the target registry using Jib. We also include the `deploy-k8s`
job to perform a test deployment to the Kind cluster. In this job, we have to install Skaffold and Kind tools on the CircleCI executor machine. Once the Kind cluster is up and ready, we deploy the app there by executing the `skaffold run`
command.

```
version: 2.1
jobs:
analyze:
docker:
- image: 'cimg/openjdk:21.0.2'
steps:
- checkout
- run:
name: Analyze on SonarCloud
command: mvn verify sonar:sonar -DskipTests
test:
executor: machine_executor_amd64
steps:
- checkout
- run:
name: Install OpenJDK 21
command: |
java -version
sudo apt-get update && sudo apt-get install openjdk-21-jdk
sudo update-alternatives --set java /usr/lib/jvm/java-21-openjdk-amd64/bin/java
sudo update-alternatives --set javac /usr/lib/jvm/java-21-openjdk-amd64/bin/javac
java -version
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
- run:
name: Maven Tests
command: mvn test
deploy-k8s:
executor: machine_executor_amd64
steps:
- checkout
- run:
name: Install Kubectl
command: |
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
- run:
name: Install Skaffold
command: |
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
chmod +x skaffold
sudo mv skaffold /usr/local/bin
- run:
name: Install Kind
command: |
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
- run:
name: Install OpenJDK 21
command: |
java -version
sudo apt-get update && sudo apt-get install openjdk-21-jdk
sudo update-alternatives --set java /usr/lib/jvm/java-21-openjdk-amd64/bin/java
sudo update-alternatives --set javac /usr/lib/jvm/java-21-openjdk-amd64/bin/javac
java -version
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
- run:
name: Create Kind Cluster
command: |
kind create cluster --name c1 --config k8s/kind-cluster-test.yaml
- run:
name: Deploy to K8s
command: |
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
skaffold run
- run:
name: Delete Kind Cluster
command: |
kind delete cluster --name c1
image-push:
docker:
- image: 'cimg/openjdk:21.0.2'
steps:
- checkout
- run:
name: Build and push image to DockerHub
command: mvn compile jib:build -Pjib -Djib.to.image=${{ values.orgName }}/${{ values.appName }}:latest -Djib.to.auth.username=${DOCKER_LOGIN} -Djib.to.auth.password=${DOCKER_PASSWORD} -DskipTests
executors:
machine_executor_amd64:
machine:
image: ubuntu-2204:2023.10.1
environment:
architecture: "amd64"
platform: "linux/amd64"
workflows:
maven_test:
jobs:
- test
- analyze:
context: SonarCloud
- deploy-k8s:
requires:
- test
- image-push:
context: Docker
requires:
- deploy-k8s
```
YAML## Install Backstage Plugins for Kubernetes
In the previous article about Backstage, we learned how to install plugins for GitHub, CircleCI, and Sonarqube integration. We will still use those plugins but also extend our Backstage instance with some additional plugins dedicated mostly to the Kubernetes-native environment. We will install the following plugins: Kubernetes (backend + frontend), HTTP Request Action (backend), Argo CD (frontend), and Prometheus (frontend). Let’s begin with the Kubernetes plugin.

### Install the Kubernetes Plugin
In the first step, we install the Kubernetes frontend plugin. It allows us to view the app pods running on Kubernetes in the Backstage UI. In order to install it, we need to execute the following `yarn`
command:

`$ yarn --cwd packages/app add @backstage/plugin-kubernetes`
ShellSessionThen, we have to make some changes in the `packages/app/src/components/catalog/EntityPage.tsx`
file. We should import the `EntityKubernetesContent`
component, and then include it in the `serviceEntityPage`
object as a new route on the frontend.

```
import { EntityKubernetesContent } from '@backstage/plugin-kubernetes';
const serviceEntityPage = (
<EntityLayout>
...
<EntityLayout.Route path="/kubernetes" title="Kubernetes">
<EntityKubernetesContent refreshIntervalMs={30000} />
</EntityLayout.Route>
...
</EntityLayout>
);
```
TypeScriptWe also need to install the Kubernetes backend plugin, to make it work on the frontend site. Here’s the required `yarn`
command:

`$ yarn --cwd packages/backend add @backstage/plugin-kubernetes-backend`
ShellSessionThen, we should register the `plugin-kubernetes-backend`
module in the `packages/backend/src/index.ts`
file.

```
import { createBackend } from '@backstage/backend-defaults';
const backend = createBackend();
backend.add(import('@backstage/plugin-app-backend/alpha'));
backend.add(import('@backstage/plugin-proxy-backend/alpha'));
backend.add(import('@backstage/plugin-scaffolder-backend/alpha'));
backend.add(import('@backstage/plugin-techdocs-backend/alpha'));
backend.add(import('@backstage/plugin-auth-backend'));
backend.add(import('@backstage/plugin-auth-backend-module-guest-provider'));
backend.add(import('@backstage/plugin-catalog-backend/alpha'));
backend.add(
import('@backstage/plugin-catalog-backend-module-scaffolder-entity-model'),
);
backend.add(import('@backstage/plugin-permission-backend/alpha'));
backend.add(import('@backstage/plugin-permission-backend-module-allow-all-policy'));
backend.add(import('@backstage/plugin-search-backend/alpha'));
backend.add(import('@backstage/plugin-search-backend-module-catalog/alpha'));
backend.add(import('@backstage/plugin-search-backend-module-techdocs/alpha'));
backend.add(import('@backstage/plugin-scaffolder-backend-module-github'));
backend.add(import('@backstage-community/plugin-sonarqube-backend'));
backend.add(import('@backstage/plugin-kubernetes-backend/alpha'));
backend.start();
```
TypeScript### Install the Argo CD Plugin
We also integrate our instance of Backstage with Argo CD running on Kubernetes. Firstly, we should execute the following `yarn`
command:

`$ yarn --cwd packages/app add @roadiehq/backstage-plugin-argo-cd`
ShellSessionThen, we need to update the `EntityPage.tsx`
file. We will add the `EntityArgoCDOverviewCard`
component inside the `overviewContent`
object.

```
import {
EntityArgoCDOverviewCard,
isArgocdAvailable
} from '@roadiehq/backstage-plugin-argo-cd';
const overviewContent = (
<Grid container spacing={3} alignItems="stretch">
...
<EntitySwitch>
<EntitySwitch.Case if={e => Boolean(isArgocdAvailable(e))}>
<Grid item sm={4}>
<EntityArgoCDOverviewCard />
</Grid>
</EntitySwitch.Case>
</EntitySwitch>
...
</Grid>
);
```
TSX### Install Prometheus Plugin
The steps for the Prometheus Plugin are pretty similar to those for the Argo CD Plugin. Firstly, we should execute the following `yarn`
command:

`$ yarn --cwd packages/app add @roadiehq/backstage-plugin-prometheus`
ShellSessionThen, we need to update the `EntityPage.tsx`
file. We will add the `EntityPrometheusContent`
component inside the `seerviceEntityPage`
object.

```
import {
EntityPrometheusContent,
} from '@roadiehq/backstage-plugin-prometheus';
const serviceEntityPage = (
<EntityLayout>
...
<EntityLayout.Route path="/kubernetes" title="Kubernetes">
<EntityKubernetesContent refreshIntervalMs={30000} />
</EntityLayout.Route>
<EntityLayout.Route path="/prometheus" title="Prometheus">
<EntityPrometheusContent />
</EntityLayout.Route>
...
</EntityLayout>
);
```
TSX### Install HTTP Request Action Plugin
This plugin is not related to Kubernetes. It allows us to integrate with third-party solutions through the HTTP API services. As you probably remember, we have already integrated with Sonarcloud and CircleCI in the Backstage UI. However, we didn’t create any projects there. We could just view the history of builds or scans for the previously created projects in Sonarcloud or CircleCI. It’s time to change it in our template! Thanks to the HTTP Request Action plugin we will create the Argo CD `Application`
through the REST API. As always, we need to execute the yarn add command to install the backend plugin:

`$ yarn --cwd packages/backend add @roadiehq/scaffolder-backend-module-http-request`
ShellSessionThen, we will register it in the `index.ts`
file:

```
import { createBackend } from '@backstage/backend-defaults';
const backend = createBackend();
backend.add(import('@backstage/plugin-app-backend/alpha'));
backend.add(import('@backstage/plugin-proxy-backend/alpha'));
backend.add(import('@backstage/plugin-scaffolder-backend/alpha'));
backend.add(import('@backstage/plugin-techdocs-backend/alpha'));
backend.add(import('@backstage/plugin-auth-backend'));
backend.add(import('@backstage/plugin-auth-backend-module-guest-provider'));
backend.add(import('@backstage/plugin-catalog-backend/alpha'));
backend.add(
import('@backstage/plugin-catalog-backend-module-scaffolder-entity-model'),
);
backend.add(import('@backstage/plugin-permission-backend/alpha'));
backend.add(
import('@backstage/plugin-permission-backend-module-allow-all-policy'),
);
backend.add(import('@backstage/plugin-search-backend/alpha'));
backend.add(import('@backstage/plugin-search-backend-module-catalog/alpha'));
backend.add(import('@backstage/plugin-search-backend-module-techdocs/alpha'));
backend.add(import('@backstage/plugin-scaffolder-backend-module-github'));
backend.add(import('@backstage-community/plugin-sonarqube-backend'));
backend.add(import('@backstage/plugin-kubernetes-backend/alpha'));
backend.add(import('@roadiehq/scaffolder-backend-module-http-request/new-backend'));
backend.start();
```
TypeScriptAfter that, we can modify a Skaffolder template used in the previous article with some additional steps.

## Prepare Backstage Template for Kubernetes
Once we have all the things in place, we can modify a previous template for the standard Spring Boot app to adapt it to the Kubernetes requirements.

### Create Skaffolder Template
First of all, we add a single input parameter that indicates the target namespace in Kubernetes for running our app **(1)**. Then, we include some additional action steps. In the first of them, we generate the repository with the YAML configuration manifests for Argo CD **(2)**. Then, we will publish that repository on GitHub under the `${{parameters.appName}}-gitops`
name **(3)**.

After that, we will use the HTTP Request Action plugin to automatically follow a new repository in CircleCI **(5)**. Once we create such a repository in the previous step, CircleCI automatically starts a build after detecting it. We also use the HTTP Request Action plugin to create a new repository on Sonarcloud under the same name as the `${{parameters.appName}}`
**(4)**. Finally, we integrate with Argo CD through the API to create a new Application responsible for applying app Deployment to Kubernetes **(6)**. This Argo CD Application will access the previously published config repository with the `-config`
suffix in the name and apply manifests inside the `manifests`
directory

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: spring-boot-basic-on-kubernetes-template
title: Create a Spring Boot app for Kubernetes
description: Create a Spring Boot app for Kubernetes
tags:
- spring-boot
- java
- maven
- circleci
- renovate
- sonarqube
- kubernetes
- argocd
spec:
owner: piomin
system: microservices
type: service
parameters:
- title: Provide information about the new component
required:
- orgName
- appName
- domainName
- repoBranchName
- groupId
- javaPackage
- apiPath
- namespace
- description
properties:
orgName:
title: Organization name
type: string
default: piomin
appName:
title: App name
type: string
default: sample-spring-boot-app-k8s
domainName:
title: Name of the domain object
type: string
default: Person
repoBranchName:
title: Name of the branch in the Git repository
type: string
default: master
groupId:
title: Maven Group ID
type: string
default: pl.piomin.services
javaPackage:
title: Java package directory
type: string
default: pl/piomin/services
apiPath:
title: REST API path
type: string
default: /api/v1
# (1)
namespace:
title: The target namespace on Kubernetes
type: string
default: demo
description:
title: Description
type: string
default: Spring Boot App Generated by Backstage
steps:
- id: sourceCodeTemplate
name: Generating the Source Code Component
action: fetch:template
input:
url: ./skeleton
values:
orgName: ${{ parameters.orgName }}
appName: ${{ parameters.appName }}
domainName: ${{ parameters.domainName }}
groupId: ${{ parameters.groupId }}
javaPackage: ${{ parameters.javaPackage }}
apiPath: ${{ parameters.apiPath }}
- id: publish
name: Publishing to the Source Code Repository
action: publish:github
input:
allowedHosts: ['github.com']
description: ${{ parameters.description }}
repoUrl: github.com?owner=${{ parameters.orgName }}&repo=${{ parameters.appName }}
defaultBranch: ${{ parameters.repoBranchName }}
repoVisibility: public
- id: register
name: Registering the Catalog Info Component
action: catalog:register
input:
repoContentsUrl: ${{ steps.publish.output.repoContentsUrl }}
catalogInfoPath: /catalog-info.yaml
# (2)
- id: configCodeTemplate
name: Generating the Config Code Component
action: fetch:template
input:
url: ../../skeletons/argocd
values:
orgName: ${{ parameters.orgName }}
appName: ${{ parameters.appName }}
targetPath: ./gitops
# (3)
- id: publish
name: Publishing to the Config Code Repository
action: publish:github
input:
allowedHosts: ['github.com']
description: ${{ parameters.description }}
repoUrl: github.com?owner=${{ parameters.orgName }}&repo=${{ parameters.appName }}-config
defaultBranch: ${{ parameters.repoBranchName }}
sourcePath: ./gitops
repoVisibility: public
# (4)
- id: sonarqube
name: Follow new project on Sonarcloud
action: http:backstage:request
input:
method: 'POST'
path: '/proxy/sonarqube/projects/create?name=${{ parameters.appName }}&organization=${{ parameters.orgName }}&project=${{ parameters.orgName }}_${{ parameters.appName }}'
headers:
content-type: 'application/json'
# (5)
- id: circleci
name: Follow new project on CircleCI
action: http:backstage:request
input:
method: 'POST'
path: '/proxy/circleci/api/project/gh/${{ parameters.orgName }}/${{ parameters.appName }}/follow'
headers:
content-type: 'application/json'
# (6)
- id: argocd
name: Create New Application in Argo CD
action: http:backstage:request
input:
method: 'POST'
path: '/proxy/argocd/api/applications'
headers:
content-type: 'application/json'
body:
metadata:
name: ${{ parameters.appName }}
namespace: argocd
spec:
project: default
source:
# (7)
repoURL: https://github.com/${{ parameters.orgName }}/${{ parameters.appName }}-config.git
targetRevision: master
path: manifests
destination:
server: https://kubernetes.default.svc
namespace: ${{ parameters.namespace }}
syncPolicy:
automated:
prune: true
selfHeal: true
syncOptions:
- CreateNamespace=true
output:
links:
- title: Open the Source Code Repository
url: ${{ steps.publish.output.remoteUrl }}
- title: Open the Catalog Info Component
icon: catalog
entityRef: ${{ steps.register.output.entityRef }}
```
YAML### Create Catalog Component
Our `catalog-info.yaml`
file should contain several additional annotations related to the plugins installed in the previous section. The `argocd/app-name`
annotation indicates the name of the target Argo CD Application responsible for deployment on Kubernetes. The `backstage.io/kubernetes-id`
annotation contains the value of the label used to search the pods on Kubernetes displayed in the Backstage UI. Finally, the `prometheus.io/rule`
annotation contains a comma-separated list of the Prometheus queries. We will create graphs displaying app pod CPU and memory usage.

```
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
name: ${{ values.appName }}
title: ${{ values.appName }}
annotations:
circleci.com/project-slug: github/${{ values.orgName }}/${{ values.appName }}
github.com/project-slug: ${{ values.orgName }}/${{ values.appName }}
sonarqube.org/project-key: ${{ values.orgName }}_${{ values.appName }}
backstage.io/kubernetes-id: ${{ values.appName }}
argocd/app-name: ${{ values.appName }}
prometheus.io/rule: container_memory_usage_bytes{pod=~"${{ values.appName }}-.*"}|pod,rate(container_cpu_usage_seconds_total{pod=~"${{ values.appName }}-.*"}[5m])|pod
tags:
- spring-boot
- java
- maven
- circleci
- renovate
- sonarqube
spec:
type: service
owner: piotr.minkowski@gmail.com
lifecycle: experimental
```
YAML### Provide Configuration Settings
We need to include several configuration settings inside the `app-config.yaml`
file. It includes the `proxy`
section, which should contain all APIs required by the HTTP Request Action plugin and frontend plugins. We should include proxy addresses for CircleCI **(1)**, Sonarcloud **(2)**, Argo CD **(3)**, and Prometheus **(4)**. After that, we include the address of our Skaffolder template **(5)**. We also have to include the `kubernetes`
section with the address of the Minikube cluster and previously generated service account token **(6)**.

```
app:
title: Scaffolded Backstage App
baseUrl: http://localhost:3000
organization:
name: piomin
backend:
baseUrl: http://localhost:7007
listen:
port: 7007
csp:
connect-src: ["'self'", 'http:', 'https:']
cors:
origin: http://localhost:3000
methods: [GET, HEAD, PATCH, POST, PUT, DELETE]
credentials: true
database:
client: better-sqlite3
connection: ':memory:'
integrations:
github:
- host: github.com
token: ${GITHUB_TOKEN}
proxy:
# (1)
'/circleci/api':
target: https://circleci.com/api/v1.1
headers:
Circle-Token: ${CIRCLECI_TOKEN}
# (2)
'/sonarqube':
target: https://sonarcloud.io/api
allowedMethods: [ 'GET', 'POST' ]
auth: "${SONARCLOUD_TOKEN}:"
# (3)
'/argocd/api':
target: https://localhost:8443/api/v1/
changeOrigin: true
secure: false
headers:
Cookie:
$env: ARGOCD_TOKEN
# (4)
'/prometheus/api':
target: http://localhost:9090/api/v1/
auth:
providers:
guest: {}
catalog:
import:
entityFilename: catalog-info.yaml
pullRequestBranchName: backstage-integration
rules:
- allow: [Component, System, API, Resource, Location]
locations:
- type: file
target: ../../examples/entities.yaml
- type: file
target: ../../examples/template/template.yaml
rules:
- allow: [Template]
# (5)
- type: url
target: https://github.com/piomin/backstage-templates/blob/master/templates/spring-boot-basic-on-kubernetes/template.yaml
rules:
- allow: [ Template ]
- type: file
target: ../../examples/org.yaml
rules:
- allow: [User, Group]
sonarqube:
baseUrl: https://sonarcloud.io
apiKey: ${SONARCLOUD_TOKEN}
# (6)
kubernetes:
serviceLocatorMethod:
type: 'multiTenant'
clusterLocatorMethods:
- type: 'config'
clusters:
- url: ${K8S_URL}
name: minikube
authProvider: 'serviceAccount'
skipTLSVerify: false
skipMetricsLookup: true
serviceAccountToken: ${K8S_TOKEN}
dashboardApp: standard
caFile: '/Users/pminkows/.minikube/ca.crt'
```
YAML## Build Backstage Image
Our source code repository with Backstage contains all the required plugins and the configuration. Now, we will build it using the `yarn`
tool. Here’s a list of required commands to perform a build.

```
$ yarn clean
$ yarn install
$ yarn tsc
$ yarn build:backend
```
ShellSessionThe repository with Backstage already contains the Dockerfile. You can find it in the `packages/backend`
directory.

```
FROM node:18-bookworm-slim
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
--mount=type=cache,target=/var/lib/apt,sharing=locked \
apt-get update && \
apt-get install -y --no-install-recommends python3 g++ build-essential && \
yarn config set python /usr/bin/python3
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
--mount=type=cache,target=/var/lib/apt,sharing=locked \
apt-get update && \
apt-get install -y --no-install-recommends libsqlite3-dev
USER node
WORKDIR /app
ENV NODE_ENV production
COPY --chown=node:node yarn.lock package.json packages/backend/dist/skeleton.tar.gz ./
RUN tar xzf skeleton.tar.gz && rm skeleton.tar.gz
RUN --mount=type=cache,target=/home/node/.cache/yarn,sharing=locked,uid=1000,gid=1000 \
yarn install --frozen-lockfile --production --network-timeout 300000
COPY --chown=node:node packages/backend/dist/bundle.tar.gz app-config*.yaml ./
RUN tar xzf bundle.tar.gz && rm bundle.tar.gz
CMD ["node", "packages/backend", "--config", "app-config.yaml"]
```
DockerfileIn order to build the image using the Dockerfile from the `packages/backend`
directory, we need to run the following command from the project root directory.

`$ yarn build-image`
ShellSessionIf you see a similar result, it means that the build was successfully finished.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-13.01.06.png?resize=696%2C375&ssl=1)
The image is available locally as `backstage:latest`
. We can run it on Docker with the following command:

```
$ docker run -it -p 7007:7007 \
-e GITHUB_TOKEN=${GITHUB_TOKEN} \
-e SONARCLOUD_TOKEN=${SONARCLOUD_TOKEN} \
-e CIRCLECI_TOKEN=${CIRCLECI_TOKEN} \
-e ARGOCD_TOKEN=${ARGOCD_TOKEN} \
-e K8S_TOKEN=${K8S_TOKEN} \
-e K8S_URL=${K8S_URL} \
-e NODE_ENV=development \
backstage:latest
```
ShellSessionHowever, our main goal today is to run it directly on Kubernetes. You can find our custom Backstage image in my Docker registry: `piomin/backstage:latest`
.

## Deploy Backstage on Kubernetes
We will use the official Helm chart for installing Backstage on Kubernetes. In the first step, let’s add the following chart repository:

`$ helm repo add backstage https://backstage.github.io/charts`
ShellSessionHere’s our `values.yaml`
file for Helm installation. We need to set all the required tokens as extra environment variables inside the Backstage pod. We also changed the default image used in the installation into the previously built custom image. To simplify the exercise, we can disable the external database and use the internal SQLite instance. It is possible to pass extra configuration files by defining them as `ConfigMap`
, without rebuilding the Docker image (`my-app-config`
).

```
backstage:
extraEnvVars:
- name: NODE_ENV
value: development
- name: GITHUB_TOKEN
value: ${GITHUB_TOKEN}
- name: SONARCLOUD_TOKEN
value: ${SONARCLOUD_TOKEN}
- name: CIRCLECI_TOKEN
value: ${CIRCLECI_TOKEN}
- name: ARGOCD_TOKEN
value: ${ARGOCD_TOKEN}
image:
registry: docker.io
repository: piomin/backstage
extraAppConfig:
- filename: app-config.extra.yaml
configMapRef: my-app-config
postgresql:
enabled: false
```
YAMLWe will change the addresses of the Kubernetes cluster, Argo CD, and Prometheus into the internal cluster locations by modifying the `app-config.yaml`
file.

```
proxy:
.
'/argocd/api':
target: https://argo-cd-argocd-server.argocd.svc/api/v1/
changeOrigin: true
secure: false
headers:
Cookie:
$env: ARGOCD_TOKEN
'/prometheus/api':
target: http://kube-prometheus-stack-prometheus.monitoring.svc:9090/api/v1/
catalog:
locations:
...
- type: url
target: https://github.com/piomin/backstage-templates/blob/master/templates/spring-boot-basic-on-kubernetes/template.yaml
rules:
- allow: [ Template ]
kubernetes:
serviceLocatorMethod:
type: 'multiTenant'
clusterLocatorMethods:
- type: 'config'
clusters:
- url: https://kubernetes.default.svc
name: minikube
authProvider: 'serviceAccount'
skipTLSVerify: false
skipMetricsLookup: true
```
app-config-kubernetes.yamlThen, we will create the backstage namespace and extra `ConfigMap`
that contains a new configuration for the Backstage running inside the Kubernetes cluster.

```
$ kubectl create ns backstage
$ kubectl create configmap my-app-config \
--from-file=app-config.extra.yaml=app-config-kubernetes.yaml -n backstage
```
ShellSessionFinally, let’s install our custom instance of Backstage in the `backstage`
namespace by executing the following command:

```
$ envsubst < values.yaml | helm install backstage backstage/backstage \
--values - -n backstage
```
ShellSessionAs I result, there is a running Backstage pod on Kubernetes:

```
$ kubectl get po -n backstage
NAME READY STATUS RESTARTS AGE
backstage-7bfbc55647-8cj5d 1/1 Running 0 16m
```
ShellSessionLet’s enable port forwarding to access the Backstage UI on the `http://localhost:7007`
:

`$ kubectl port-forward svc/backstage 7007 -n backstage`
ShellSessionThis time we increase the privileges for `default`
`ServiceAccount`
in the `backstage`
namespace used by our instance of Backstage:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
name: default-admin
subjects:
- kind: ServiceAccount
name: default
namespace: backstage
roleRef:
kind: ClusterRole
name: cluster-admin
apiGroup: rbac.authorization.k8s.io
```
YAML## Final Test
After accessing Backstage UI we can create a new Spring Boot app from the template. Choose the *“Create a Spring Boot app for Kubernetes”* template as shown below:

![backstage-kubernetes-create](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-14.43.35.png?resize=696%2C309&ssl=1)
If you would like to try it by yourself, you need to change the organization name to your GitHub account name. Then click *“Review”* and *“Create”* on the next page.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-14.46.44.png?resize=696%2C368&ssl=1)
There are two GitHub repositories created. The first one contains the sample app source code.

![backstage-kubernetes-repo](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.35.20.png?resize=696%2C394&ssl=1)
The second one contains YAML manifests with `Deployment`
for Argo CD.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.35.58.png?resize=696%2C262&ssl=1)
The Argo CD `Application`
is automatically created. We can verify the synchronization status in the Backstage UI.

![backstage-kubernetes-argocd](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.53.37.png?resize=696%2C669&ssl=1)
Our application is running in the `demo`
namespace. We can display a list of pods in the *“KUBERNETES”* tab.

![backstage-kubernetes-pod](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.38.17.png?resize=696%2C379&ssl=1)
We can also verify the detailed status of each pod.

![backstage-kubernetes-pod-status](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.56.13.png?resize=696%2C848&ssl=1)
Or take a look at the logs.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.56.31.png?resize=696%2C252&ssl=1)
## Final Thoughts
In this article, we learned how to install and integrate Backstage with Kubernetes-native services like Argo CD or Prometheus. We built the customized image with Backstage and then deployed it on Kubernetes using the Helm chart.

## Leave a ReplyCancel reply