<!--
title: Kubernetes中Argo CD ApplicationSet Generators的艺术
cover: https://piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-20-at-10.36.10-1024x576.png
summary: 🚀解锁云原生新姿势！本文详解如何用 Argo CD ApplicationSet 和 Git Generator，基于 GitOps 轻松管理 Kubernetes 集群。通过 Helm chart 模板化部署，实现跨环境应用和组件的自动化配置与同步，告别手动部署烦恼！
-->

🚀解锁云原生新姿势！本文详解如何用 Argo CD `ApplicationSet` 和 `Git Generator`，基于 `GitOps` 轻松管理 `Kubernetes` 集群。通过 `Helm chart` 模板化部署，实现跨环境应用和组件的自动化配置与同步，告别手动部署烦恼！

> 译自：[The Art of Argo CD ApplicationSet Generators with Kubernetes - Piotr's TechBlog](https://piotrminkowski.com/2025/03/20/the-art-of-argo-cd-applicationset-generators-with-kubernetes/)
> 
> 作者：Piotr Minkowski

本文将教你如何使用 Argo CD ApplicationSet 生成器，通过 GitOps 方法来管理你的 Kubernetes 集群。Argo CD ApplicationSet 是一种 Kubernetes 资源，允许我们管理和部署多个 Argo CD 应用程序。它基于给定的模板动态生成多个 Argo CD 应用程序。因此，我们可以跨多个 Kubernetes 集群部署应用程序，为不同的环境（例如，开发、测试、生产）创建应用程序，并管理许多存储库或分支。通过最少的源代码工作，一切都可以轻松实现。

Argo CD ApplicationSet 支持几种不同的生成器。在本文中，我们将重点介绍 [Git 生成器](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Git/)类型。它基于 Git 存储库中的目录结构或分支更改生成 Argo CD 应用程序。它包含两个子类型：Git 目录生成器和 Git 文件生成器。如果你对其他 Argo CD ApplicationSet 生成器感兴趣，你可以在我的博客上找到一些文章。例如，以下[文章](https://piotrminkowski.com/2025/01/14/continuous-promotion-on-kubernetes-with-gitops/)展示了如何使用 List Generator 在环境之间提升镜像。你还可以找到一篇关于集群决策资源生成器的[文章](https://piotrminkowski.com/2023/10/06/handle-traffic-bursts-with-ephemeral-openshift-clusters/)，该文章展示了如何在多个 Kubernetes 集群之间动态传播应用程序。

## 源代码

如果你想自己尝试，请随时使用我的源代码。为此，你必须克隆我的示例 GitHub [存储库](https://github.com/piomin/argocd-showcase.git)。你必须转到 `appset-helm-demo` 目录，其中包含该练习所需的完整配置。然后，你只需按照我的说明进行操作即可。

## Argo CD 安装

Argo CD 是我们唯一需要在 Kubernetes 集群上安装的工具。我们可以使用官方 Helm [chart](https://artifacthub.io/packages/helm/argo/argo-cd) 在 Kubernetes 上安装它。首先，让我们添加以下 Helm 存储库：

```shell
helm repo add argo https://argoproj.github.io/argo-helm
```

之后，我们可以使用以下命令在 `argocd` 命名空间中的当前 Kubernetes 集群中安装 ArgoCD：

```shell
helm install my-argo-cd argo/argo-cd -n argocd
```

我在本练习中使用 OpenShift。使用 OpenShift 控制台，我可以轻松地使用 OpenShift GitOps operator 在集群上安装 ArgoCD。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.02.56.png?resize=696%2C274&ssl=1)

安装完成后，我们可以轻松访问 Argo CD 仪表板。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.03.26.png?resize=696%2C347&ssl=1)

我们可以使用 OpenShift 凭据在那里登录。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.04.03.png?resize=696%2C404&ssl=1)

## 动机

在本练习中，我们的目标是在 Kubernetes 上部署和运行一些应用程序（一个简单的 Java 应用程序和 Postgres 数据库），并尽量减少源代码工作。这两个应用程序仅展示了如何创建一个标准，该标准可以轻松应用于部署在集群上的任何应用程序类型。在此标准中，目录结构决定了我们的应用程序在 Kubernetes 上的部署方式和位置。我的示例配置存储在单个 Git 存储库中。但是，我们可以使用多个存储库轻松地对其进行扩展，其中 Argoc CD 在中央存储库和其他包含具体应用程序配置的 Git 存储库之间切换。

这是用于部署我们的两个应用程序的目录结构和文件。自定义应用程序和 Postgres 数据库都部署在三个环境中：`dev`、`test` 和 `prod`。我们使用 Helm chart 来部署它们。每个环境目录都包含一个带有安装参数的 Helm values 文件。该配置区分了两种不同的安装类型：应用程序和组件。每个应用程序都使用专用于标准部署的相同 Helm chart 进行安装。每个组件都使用该组件提供的自定义 Helm chart 进行安装。例如，对于 Postgres，我们将使用以下 Bitnami [chart](https://artifacthub.io/packages/helm/bitnami/postgresql)。

```
.
├── apps
│   ├── aaa-1
│   │   └── basic
│   │       ├── prod
│   │       │   └── values.yaml
│   │       ├── test
│   │       │   └── values.yaml
│   │       ├── uat
│   │       │   └── values.yaml
│   │       └── values.yaml
│   ├── aaa-2
│   └── aaa-3
└── components
    └── aaa-1
        └── postgresql
            ├── prod
            │   ├── config.yaml
            │   └── values.yaml
            ├── test
            │   ├── config.yaml
            │   └── values.yaml
            └── uat
                ├── config.yaml
                └── values.yaml
```

在部署应用程序之前，我们应该准备带有配额的命名空间、Argo CD 项目和 ApplicationSet 生成器，以管理应用程序部署。以下是全局配置仓库的结构。它还使用 Helm chart 将清单的该部分应用于 Kubernetes 集群。`projects` 目录中的每个目录都决定了我们的项目名称。另一方面，一个项目包含多个 Kubernetes 命名空间。每个项目可能包含几个不同的 Kubernetes 部署。

```
.
└── projects
    ├── aaa-1
    │   └── values.yaml
    ├── aaa-2
    │   └── values.yaml
    └── aaa-3
        └── values.yaml
```

## 准备全局集群配置

### 用于命名空间和配额的 Helm 模板

以下是用于为每个命名空间创建命名空间和配额的 Helm 模板。我们将为每个环境（阶段）创建一个项目命名空间。

```yaml
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

`chart/templates/namespace.yaml`

### 用于 Argo CD AppProject 的 Helm 模板

Helm chart 还会为我们的每个项目创建一个专用的 Argo CD `AppProject` 对象。

```yaml
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

`chart/templates/appproject.yaml`

### 用于 Argo CD ApplicationSet 的 Helm 模板

之后，我们可以继续进行我们练习中最棘手的部分。Helm chart 还定义了一个用于创建 Argo CD ApplicationSet 的模板。此 ApplicationSet 必须分析存储库结构，其中包含应用程序和组件的配置。我们为每个项目定义两个 ApplicationSet。第一个使用 Git Directory 生成器来确定 `apps` 目录的结构，并使用我的自定义 `spring-boot-api-app` chart 在所有环境中部署应用程序。可以使用放置在每个应用程序目录中的 Helm 值覆盖 chart 参数。

第二个 ApplicationSet 使用 Git Files 生成器来确定 `components` 目录的结构。它读取每个目录中 `config.yaml` 文件的内容。`config.yaml` 文件设置 Helm chart 的存储库、名称和版本，该 chart 必须用于在 Kubernetes 上安装组件。

```yaml
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


`chart/templates/applicationsets.yaml` 在此配置中有几个重要的元素，我们应该注意。Helm 和 ApplicationSet 都使用基于 `{{ ... }}` 占位符的模板引擎。因此，为了避免冲突，我们应该从 Helm 模板元素中转义 Argo CD ApplicationSet 模板元素。模板中负责生成 Argo CD 应用程序名称的以下部分是该方法的一个很好的例子： `'{{`{{ index .path.segments 3 }}`}}-{{`{{ index .path.segments 4 }}`}}'`。首先，我们使用 AppliocationSet Git 生成器参数 `index .path.segments 3`，它返回目录路径的第三部分的名称。这些元素使用 ``` 字符进行转义，因此 Helm 不会尝试分析它。

### Helm Chart 结构

我们的 ApplicationSets 使用“应用程序的多个来源”功能从 Helm values 文件中读取参数，并将它们从远程存储库注入到 Helm chart 中。因此，我们的应用程序和组件的配置存储库仅包含标准化目录结构中的 `values.yaml` 文件。我们存储在示例存储库中的唯一 chart 已在上面描述，它负责创建在集群上运行应用程序部署所需的配置。

```
.
└── chart
    ├── Chart.yaml
    ├── templates
    │   ├── additional.yaml
    │   ├── applicationsets.yaml
    │   ├── appproject.yaml
    │   └── namespaces.yaml
    └── values.yaml
```

ShellSession 默认情况下，每个项目定义三个环境（阶段）：`test`、`uat` 和 `prod`。

```
stages:
- name: test
  additionalObjects: {}
- name: uat
  additionalObjects: {}
- name: prod
  additionalObjects: {}
```

`chart/values.yml` 我们可以覆盖 Helm values 中特定项目的默认行为。每个项目目录都包含 `values.yaml` 文件。以下是 `aaa-3` 项目的 Helm 参数，它仅针对 `test` 环境将 CPU 请求配额从 2 个 CPU 覆盖为 4 个 CPU。

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

`projects/aaa-3/values.yaml`

## 运行同步过程

### 在集群上生成全局结构

要启动一个过程，我们必须创建读取项目目录结构的 ApplicationSet。`projects` 目录中的每个子目录都指示我们项目的名称。我们的 ApplicationSet 使用 Git 目录生成器为每个项目创建一个 Argo CD 应用程序。它的名称包含子目录的名称和 config 后缀。每个生成的应用程序都使用先前描述的 Helm chart 来创建项目请求的所有命名空间、配额和其他资源。它还利用“应用程序的多个来源”功能，允许我们覆盖默认的 Helm chart 设置。它从目录名称读取项目名称，并将其作为参数传递给生成的 Argo CD 应用程序。

```yaml
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

YAML 一旦我们创建了 `global-config` `ApplicationSet` 对象，奇迹就会发生。以下是从 Git 配置存储库中的目录生成的 Argo CD 应用程序的列表。

![argo-cd-applicationset-all-apps](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.25.38.png?resize=696%2C326&ssl=1)

首先，有三个带有项目配置的 Argo CD 应用程序。这是因为我们在 `projects` 目录中定义了 3 个子目录，名称为 `aaa-1`、`aaa-2` 和 `aaa-3`。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.29.05.png?resize=696%2C302&ssl=1)
那些 Argo CD 应用程序所应用的配置非常相似，因为它们使用的是同一个 Helm chart。我们可以查看由 `aaa-3-config` `Application` 管理的资源列表。这里有三个命名空间（`aaa-3-test`、`aaa-3-uat`、`aaa-3-prod`），它们带有资源配额，一个单独的 Argo CD AppProject，以及两个 `ApplicationSet` 对象，负责为 `apps` 和 `components` 目录生成 Argo CD 应用程序。

![argo-cd-applicationset-global-config](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.33.23.png?resize=696%2C459&ssl=1)

在这个配置中，我们可以验证 `request.cpu` `ResourceQuota` 对象的值是否已从 2 个 CPU 覆盖为 4 个 CPU。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-15.39.58.png?resize=696%2C491&ssl=1)

让我们分析一下发生了什么。以下是 Argo CD ApplicationSets 的列表。`global-config` `ApplicationSet` 为 `projects` 目录中检测到的每个项目生成 Argo CD 应用程序。然后，这些应用程序中的每一个都使用 Helm 模板将两个 `ApplicationSet` 对象应用到集群。

```
$ kubectl get applicationset
NAME                    AGE
aaa-1-components-config   29m
aaa-1-apps-config         29m
aaa-2-components-config   29m
aaa-2-apps-config         29m
aaa-3-components-config   29m
aaa-3-apps-config         29m
global-config             29m
```

以下是已创建的命名空间的列表：

```
$ kubectl get ns
NAME        STATUS   AGE
aaa-1-prod  Active   34m
aaa-1-test  Active   34m
aaa-1-uat   Active   34m
aaa-2-prod  Active   34m
aaa-2-test  Active   34m
aaa-2-uat   Active   34m
aaa-3-prod  Active   34m
aaa-3-test  Active   34m
aaa-3-uat   Active   34m
```

### 生成和应用部署

我们的示例配置仅包含两个 Deployment。我们在 `aaa-1` 项目中的 apps 目录中定义了 basic 子目录，在 components 目录中定义了 postgres 子目录。为了简化，`aaa-2` 和 `aaa-3` 项目不包含任何 Deployment。但是，我们在其中创建的带有 `values.yaml` 文件的子目录越多，部署在集群上的应用程序就越多。以下是使用标准 Helm chart 部署的简单应用程序的典型 `values.yaml` 文件。它定义了镜像仓库、名称和标签。它还设置了 Deployment 名称和环境。

```yaml
image:
  repository: piomin/basic
  tag: 1.0.0
app:
  name: basic
  environment: prod
```

对于 `postgres` 组件，我们必须在 Helm values 中设置更多参数。以下是最终列表：

```yaml
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

以下 Argo CD 应用程序由 `aaa-1-apps-config` `ApplicationSet` 生成。它检测到 `apps` 目录中的 basic 子目录。`basic` 子目录包含 3 个子目录：带有 `values.yaml` 文件的 `test`、`uat` 和 `prod`。因此，我们有每个环境的 Argo CD 负责在目标命名空间中部署 `basic` 应用程序。

![argo-cd-applicationset-basic-apps](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.15.31.png?resize=696%2C188&ssl=1)

以下是由 `basic-prod` `Application` 管理的资源列表。它使用我的自定义 Helm chart 并将 `Deployment` 和 `Service` 对象应用到集群。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.16.01.png?resize=696%2C222&ssl=1)

以下 Argo CD 应用程序由 `aaa-1-components-config` `ApplicationSet` 生成。它检测到 `components` 目录中的 basic 子目录。`postgres` 子目录包含 3 个子目录：带有 `values.yaml` 和 `config.yaml` 文件的 `test`、`uat` 和 `prod`。ApplicationSet Files 生成器从 `config.yaml` 文件中的配置读取仓库、名称和版本。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.17.48.png?resize=696%2C182&ssl=1)

以下是带有 Bitnami Postgres chart 设置的 `config.yaml` 文件。我们可以将我们想要在集群上安装的其他任何 chart 放在这里。

```yaml
chart:
  repository: https://charts.bitnami.com/bitnami
  name: postgresql
  version: 15.5.38
```

以下是由生成的 Argo CD 应用程序使用的 Bitnami Helm chart 安装的资源列表。

![argo-cd-applicationset-postgres](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2025/03/Screenshot-2025-03-19-at-16.18.41.png?resize=696%2C416&ssl=1)

## 最后的想法

本文证明了 Argo CD ApplicationSet 和 Helm 模板可以一起使用来创建高级配置结构。它展示了如何使用 ApplicationSet Git Directory 和 Files generators 来分析 Git config 仓库中目录和文件的结构。通过这种方法，我们可以提出整个组织中配置结构的标准化，并将其类似地传播到 Kubernetes 集群中部署的所有应用程序。一切都可以在集群管理员级别轻松管理，只需使用访问许多不同配置仓库的单个全局 Argo CD ApplicationSet。