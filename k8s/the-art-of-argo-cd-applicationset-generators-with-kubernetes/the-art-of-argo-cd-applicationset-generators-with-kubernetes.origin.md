## The Art of Argo CD ApplicationSet Generators with Kubernetes
![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-20-at-10.36.10.png?fit=2298%2C1292&ssl=1)
This article will teach you how to use the Argo CD ApplicationSet generators to manage your Kubernetes cluster using a GitOps approach. An Argo CD ApplicationSet is a Kubernetes resource that allows us to manage and deploy multiple Argo CD Applications. It dynamically generates multiple Argo CD Applications based on a given template. As a result, we can deploy applications across multiple Kubernetes clusters, create applications for different environments (e.g., dev, staging, prod), and manage many repositories or branches. Everything can be easily achieved with a minimal source code effort.

Argo CD ApplicationSet supports several different generators. In this article, we will focus on the [Git generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Git/) type. It generates Argo CD Applications based on directory structure or branch changes in a Git repository. It contains two subtypes: the Git directory generator and the Git file generator. If you are interested in other Argo CD ApplicationSet generators you can find some articles on my blog. For example, the following [post](https://piotrminkowski.com/2025/01/14/continuous-promotion-on-kubernetes-with-gitops/) shows how to use List Generator to promote images between environments. You can also find a [post](https://piotrminkowski.com/2023/10/06/handle-traffic-bursts-with-ephemeral-openshift-clusters/) about the Cluster Decision Resource generator, which shows how to spread applications dynamically between multiple Kubernetes clusters.

## Source Code
Feel free to use my source code if you’d like to try it out yourself. To do that, you must clone my sample GitHub [repository](https://github.com/piomin/argocd-showcase.git). You must go to the `appset-helm-demo`
directory, which contains the whole configuration required for that exercise. Then you should only follow my instructions.

## Argo CD Installation
Argo CD is the only tool we need to install on our Kubernetes cluster for that exercise. We can use the official Helm [chart](https://artifacthub.io/packages/helm/argo/argo-cd) to install it on Kubernetes. Firstly. let’s add the following Helm repository:

`helm repo add argo https://argoproj.github.io/argo-helm`
ShellSessionAfter that, we can install ArgoCD in the current Kubernetes cluster in the `argocd`
namespace using the following command:

`helm install my-argo-cd argo/argo-cd -n argocd`
ShellSessionI use OpenShift in that exercise. With the OpenShift Console, I can easily install ArgoCD on the cluster using the OpenShift GitOps operator.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.02.56.png?resize=696%2C274&ssl=1)
Once we installed it we can easily access the Argo CD dashboard.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.03.26.png?resize=696%2C347&ssl=1)
We can sign in there using OpenShift credentials.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.04.03.png?resize=696%2C404&ssl=1)
## Motivation
Our goal in this exercise is to deploy and run some applications (a simple Java app and Postgres database) on Kubernetes with minimal source code effort. Those two applications only show how to create a standard that can be easily applied to any application type deployed on our cluster. In this standard, a directory structure determines how and where our applications are deployed on Kubernetes. My example configuration is stored in a single Git repository. However, we can easily extend it with multiple repositories, where Argoc CD switches between the central repository and other Git repositories containing a configuration for concrete applications.

Here’s a directory structure and files for deploying our two applications. Both the custom app and Postgres database are deployed in three environments: `dev`
, `test`
, and `prod`
. We use Helm charts for deploying them. Each environment directory contains a Helm values file with installation parameters. The configuration distinguishes two different types of installation: apps and components. Each app is installed using the same Helm chart dedicated to a standard deployment. Each component is installed using a custom Helm chart provided by that component. For example, for Postgres, we will use the following Bitnami [chart](https://artifacthub.io/packages/helm/bitnami/postgresql).

```
.
├── apps
│ ├── aaa-1
│ │ └── basic
│ │ ├── prod
│ │ │ └── values.yaml
│ │ ├── test
│ │ │ └── values.yaml
│ │ ├── uat
│ │ │ └── values.yaml
│ │ └── values.yaml
│ ├── aaa-2
│ └── aaa-3
└── components
└── aaa-1
└── postgresql
├── prod
│ ├── config.yaml
│ └── values.yaml
├── test
│ ├── config.yaml
│ └── values.yaml
└── uat
├── config.yaml
└── values.yaml
```
ShellSessionBefore deploying the application, we should prepare namespaces with quotas, Argo CD projects, and ApplicationSet generators for managing application deployments. Here’s the structure of a global configuration repository. It also uses Helm chart to apply that part of manifests to the Kubernetes cluster. Each directory inside the `projects`
directory determines our project name. On the other hand, a project contains several Kubernetes namespaces. Each project may contain several different Kubernetes Deployments.

```
.
└── projects
├── aaa-1
│ └── values.yaml
├── aaa-2
│ └── values.yaml
└── aaa-3
└── values.yaml
```
ShellSession## Prepare Global Cluster Configuration
### Helm Template for Namespaces and Quotas
Here’s the Helm template for creating namespaces and quotas for each namespace. We will create the project namespace per each environment (stage).

```
{{- range .Values.stages }}
---
apiVersion: v1
kind: Namespace
metadata:
name: {{ $.Values.projectName }}-{{ .name }}
---
apiVersion: v1
kind: ResourceQuota
metadata:
name: default-quota
namespace: {{ $.Values.projectName }}-{{ .name }}
spec:
hard:
{{- if .config }}
{{- with .config.quotas }}
pods: {{ .pods | default "10" }}
requests.cpu: {{ .cpuRequest | default "2" }}
requests.memory: {{ .memoryRequest | default "2Gi" }}
limits.cpu: {{ .cpuLimit | default "8" }}
limits.memory: {{ .memoryLimit | default "8Gi" }}
{{- end }}
{{- else }}
pods: "10"
requests.cpu: "2"
requests.memory: "2Gi"
limits.cpu: "8"
limits.memory: "8Gi"
{{- end }}
{{- end }}
```
chart/templates/namespace.yaml### Helm Template for the Argo CD AppProject
Helm chart will also create a dedicated Argo CD `AppProject`
object per our project.

```
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
name: {{ .Values.projectName }}
namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
clusterResourceWhitelist:
- group: '*'
kind: '*'
destinations:
- namespace: '*'
server: '*'
sourceRepos:
- '*'
```
chart/templates/appproject.yaml### Helm Template for Argo CD ApplicationSet
After that, we can proceed to the most tricky part of our exercise. Helm chart also defines a template for creating the Argo CD ApplicationSet. This ApplicationSet must analyze the repository structure, which contains the configuration of apps and components. We define two ApplicationSets per each project. The first uses the Git Directory generator to determine the structure of the `apps`
catalog and deploy the apps in all environments using my custom `spring-boot-api-app`
chart. The chart parameters can be overridden with Helm values placed in each app directory.

The second ApplicationSet uses the Git Files generator to determine the structure of the `components`
catalog. It reads the contents of the `config.yaml`
file in each directory. The `config.yaml`
file sets the repository, name, and version of the Helm chart that must be used to install the component on Kubernetes.

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
name: '{{ .Values.projectName }}-apps-config'
namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
goTemplate: true
generators:
- git:
repoURL: https://github.com/piomin/argocd-showcase.git
revision: HEAD
directories:
{{- range .Values.stages }}
- path: appset-helm-demo/apps/{{ $.Values.projectName }}/*/{{ .name }}
{{- end }}
template:
metadata:
name: '{{`{{ index .path.segments 3 }}`}}-{{`{{ index .path.segments 4 }}`}}'
spec:
destination:
namespace: '{{`{{ index .path.segments 2 }}`}}-{{`{{ index .path.segments 4 }}`}}'
server: 'https://kubernetes.default.svc'
project: '{{ .Values.projectName }}'
sources:
- chart: spring-boot-api-app
repoURL: 'https://piomin.github.io/helm-charts/'
targetRevision: 0.3.8
helm:
valueFiles:
- $values/appset-helm-demo/apps/{{ .Values.projectName }}/{{`{{ index .path.segments 3 }}`}}/{{`{{ index .path.segments 4 }}`}}/values.yaml
parameters:
- name: appName
value: '{{ .Values.projectName }}'
- repoURL: 'https://github.com/piomin/argocd-showcase.git'
targetRevision: HEAD
ref: values
syncPolicy:
automated:
prune: true
selfHeal: true
---
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
name: '{{ .Values.projectName }}-components-config'
namespace: {{ .Values.argoNamespace | default "argocd" }}
spec:
goTemplate: true
generators:
- git:
repoURL: https://github.com/piomin/argocd-showcase.git
revision: HEAD
files:
{{- range .Values.stages }}
- path: appset-helm-demo/components/{{ $.Values.projectName }}/*/{{ .name }}/config.yaml
{{- end }}
template:
metadata:
name: '{{`{{ index .path.segments 3 }}`}}-{{`{{ index .path.segments 4 }}`}}'
spec:
destination:
namespace: '{{`{{ index .path.segments 2 }}`}}-{{`{{ index .path.segments 4 }}`}}'
server: 'https://kubernetes.default.svc'
project: '{{ .Values.projectName }}'
sources:
- chart: '{{`{{ .chart.name }}`}}'
repoURL: '{{`{{ .chart.repository }}`}}'
targetRevision: '{{`{{ .chart.version }}`}}'
helm:
valueFiles:
- $values/appset-helm-demo/components/{{ .Values.projectName }}/{{`{{ index .path.segments 3 }}`}}/{{`{{ index .path.segments 4 }}`}}/values.yaml
parameters:
- name: appName
value: '{{ .Values.projectName }}'
- repoURL: 'https://github.com/piomin/argocd-showcase.git'
targetRevision: HEAD
ref: values
syncPolicy:
automated:
prune: true
selfHeal: true
```
chart/templates/applicationsets.yamlThere are several essential elements in this configuration, which we should pay attention to. Both Helm and ApplicationSet use templating engines based on `{{ ... }}`
placeholders. So to avoid conflicts we should escape Argo CD ApplicationSet templating elements from the Helm templating elements. The following part of the template responsible for generating the Argo CD Application name is a good example of that approach: `'{{`{{ index .path.segments 3 }}`}}-{{`{{ index .path.segments 4 }}`}}'`
. First, we use the AppliocationSet Git generator parameter `index .path.segments 3`
that returns the name of the third part of the directory path. Those elements are escaped with the ```
char so Helm doesn’t try to analyze it.

### Helm Chart Structure
Our ApplicationSets use the “Multiple Sources for Application” feature to read parameters from Helm values files and inject them into the Helm chart from a remote repository. Thanks to that, our configuration repositories for apps and components contain only `values.yaml`
files in the standardized directory structure. The only chart we store in the sample repository has been described above and is responsible for creating the configuration required to run app Deployments on the cluster.

```
.
└── chart
├── Chart.yaml
├── templates
│ ├── additional.yaml
│ ├── applicationsets.yaml
│ ├── appproject.yaml
│ └── namespaces.yaml
└── values.yaml
```
ShellSessionBy default, each project defines three environments (stages): `test`
, `uat`
, `prod`
.

```
stages:
- name: test
additionalObjects: {}
- name: uat
additionalObjects: {}
- name: prod
additionalObjects: {}
```
chart/values.ymlWe can override a default behavior for the specific project in Helm values. Each project directory contains the `values.yaml`
file. Here are Helm parameters for the `aaa-3`
project that override CPU request quota from 2 CPUs to 4 CPUs only for the `test`
environment.

```
stages:
- name: test
config:
quotas:
cpuRequest: 4
additionalObjects: {}
- name: uat
additionalObjects: {}
- name: prod
additionalObjects: {}
```
projects/aaa-3/values.yaml## Run the Synchronization Process
### Generate Global Structure on the Cluster
To start a process we must create the ApplicationSet that reads the structure of the projects directory. Each subdirectory in the `projects`
directory indicates the name of our project. Our ApplicationSet uses a Git directory generator to create an Argo CD Application per each project. Its name contains the name of the subdirectory and the config suffix. Each generated Application uses the previously described Helm chart to create all namespaces, quotas, and other resources requested by the project. It also leverages the “Multiple Sources for Application” feature to allow us to override default Helm chart settings. It reads a project name from the directory name and passes it as a parameter to the generated Argo CD Application.

```
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
name: global-config
namespace: openshift-gitops
spec:
goTemplate: true
generators:
- git:
repoURL: https://github.com/piomin/argocd-showcase.git
revision: HEAD
directories:
- path: appset-helm-demo/projects/*
template:
metadata:
name: '{{.path.basename}}-config'
spec:
destination:
namespace: '{{.path.basename}}'
server: 'https://kubernetes.default.svc'
project: default
sources:
- path: appset-helm-demo/chart
repoURL: 'https://github.com/piomin/argocd-showcase.git'
targetRevision: HEAD
helm:
valueFiles:
- $values/appset-helm-demo/projects/{{.path.basename}}/values.yaml
parameters:
- name: projectName
value: '{{.path.basename}}'
- name: argoNamespace
value: openshift-gitops
- repoURL: 'https://github.com/piomin/argocd-showcase.git'
targetRevision: HEAD
ref: values
syncPolicy:
automated:
prune: true
selfHeal: true
```
YAMLOnce we create the `global-config`
`ApplicationSet`
object magic happens. Here’s the list of Argo CD Applications generated from our directories in Git configuration repositories.

![argo-cd-applicationset-all-apps](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.25.38.png?resize=696%2C326&ssl=1)
First, there are three Argo CD Applications with the projects’ configuration. That’s happening because we defined 3 subdirectories in the `projects`
directory with names `aaa-1`
, `aaa-2`
and `aaa-3`
.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.29.05.png?resize=696%2C302&ssl=1)
The configuration applied by those Argo CD Applications is pretty similar since they are using the same Helm chart. We can look at the list of resources managed by the `aaa-3-config`
`Application`
. There are three namespaces (`aaa-3-test`
, `aaa-3-uat`
, `aaa-3-prod`
) with resource quotas, a single Argo CD AppProject, and two `ApplicationSet`
objects responsible for generating Argo CD Applications for `apps`
and `components`
directories.

![argo-cd-applicationset-global-config](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.33.23.png?resize=696%2C459&ssl=1)
In this configuration, we can verify if the value of the `request.cpu`
`ResourceQuota`
object has been overridden from 2 CPUs to 4 CPUs.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.39.58.png?resize=696%2C491&ssl=1)
Let’s analyze what happened. Here’s a list of Argo CD ApplicationSets. The `global-config`
`ApplicationSet`
generated Argo CD Application per each detected project inside the `projects`
directory. Then, each of these Applications applied two `ApplicationSet`
objects to cluster using the Helm template.

```
$ kubectl get applicationset
NAME AGE
aaa-1-components-config 29m
aaa-1-apps-config 29m
aaa-2-components-config 29m
aaa-2-apps-config 29m
aaa-3-components-config 29m
aaa-3-apps-config 29m
global-config 29m
```
ShellSessionThere’s also a list of created namespaces:

```
$ kubectl get ns
NAME STATUS AGE
aaa-1-prod Active 34m
aaa-1-test Active 34m
aaa-1-uat Active 34m
aaa-2-prod Active 34m
aaa-2-test Active 34m
aaa-2-uat Active 34m
aaa-3-prod Active 34m
aaa-3-test Active 34m
aaa-3-uat Active 34m
```
ShellSession### Generate and Apply Deployments
Our sample configuration contains only two Deployments. We defined the basic subdirectory in the apps directory and the postgres subdirectory in the components directory inside the `aaa-1`
project. The `aaa-2`
and `aaa-3`
projects don’t contain any Deployments for simplification. However, the more subdirectories with the `values.yaml`
file we create there, the more applications will be deployed on the cluster. Here’s a typical `values.yaml`
file for a simple app deployed with a standard Helm chart. It defines the image repository, name, and tag. It also set the Deployment name and environment.

```
image:
repository: piomin/basic
tag: 1.0.0
app:
name: basic
environment: prod
```
YAMLFor the `postgres`
component we must set more parameters in Helm values. Here’s the final list:

```
global:
compatibility:
openshift:
adaptSecurityContext: force
image:
tag: 1-54
registry: registry.redhat.io
repository: rhel9/postgresql-15
primary:
containerSecurityContext:
readOnlyRootFilesystem: false
persistence:
mountPath: /var/lib/pgsql
extraEnvVars:
- name: POSTGRESQL_ADMIN_PASSWORD
value: postgresql123
postgresqlDataDir: /var/lib/pgsql/data
```
YAMLThe following Argo CD Application has been generated by the `aaa-1-apps-config`
`ApplicationSet`
. It detected the basic subdirectory in the `apps`
directory. The `basic`
subdirectory contained 3 subdirectories: `test`
, `uat`
and `prod`
with `values.yaml`
file. As a result, we have Argo CD per environment responsible for deploying the `basic`
app in the target namespaces.

![argo-cd-applicationset-basic-apps](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.15.31.png?resize=696%2C188&ssl=1)
Here’s a list of resources managed by the `basic-prod`
`Application`
. It uses my custom Helm chart and applies `Deployment`
and `Service`
objects to the cluster.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.16.01.png?resize=696%2C222&ssl=1)
The following Argo CD Application has been generated by the `aaa-1-components-config`
`ApplicationSet`
. It detected the basic subdirectory in the `components`
directory. The `postgres`
subdirectory contained 3 subdirectories: `test`
, `uat`
and `prod`
with `values.yaml`
and `config.yaml`
files. The ApplicationSet Files generator reads the repository, name, and version from the configuration in the `config.yaml`
file.

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.17.48.png?resize=696%2C182&ssl=1)
Here’s the `config.yaml`
file with the Bitnami Postgres chart settings. We could place here any other chart we want to install something else on the cluster.

```
chart:
repository: https://charts.bitnami.com/bitnami
name: postgresql
version: 15.5.38
```
components/aaa-1/postgresql/prod/config.yamlHere’s the list of resources installed by the Bitnami Helm chart used by the generated Argo CD Applications.

![argo-cd-applicationset-postgres](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.18.41.png?resize=696%2C416&ssl=1)
## Final Thoughts
This article proves that Argo CD ApplicationSet and Helm templates can be used together to create advanced configuration structures. It shows how to use ApplicationSet Git Directory and Files generators to analyze the structure of directories and files in the Git config repository. With that approach, we can propose a standardization in the configuration structure across the whole organization and propagate it similarly for all the applications deployed in the Kubernetes clusters. Everything can be easily managed at the cluster admin level with the single global Argo CD ApplicationSet that accesses many different repositories with configuration.

## Leave a ReplyCancel reply