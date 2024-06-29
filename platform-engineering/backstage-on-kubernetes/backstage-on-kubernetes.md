
<!--
title: Kubernetes上的Backstage
cover: ./cover.png
-->

本文将介绍如何使用 Helm Chart 在 Kubernetes 上部署 Backstage，并与 Argo CD 和 Prometheus 集成。

> 译自 [Backstage on Kubernetes - Piotr's TechBlog](https://piotrminkowski.com/2024/06/28/backstage-on-kubernetes/)，作者 Piotr Minkowski。

本文将介绍如何将 Backstage 与 Kubernetes 集成。我们将通过两种不同的方式运行 Backstage。首先，它将在集群外部运行，并通过 API 与 Kubernetes 连接。在第二种情况下，我们将使用官方的 Helm Chart 直接将其部署到集群中。我们的 Backstage 实例将连接到 Kubernetes 上部署的 Argo CD 和 Prometheus，以可视化 Argo CD 同步状态和与应用程序相关的基本指标。

本练习延续了我之前[文章](https://piotrminkowski.com/2024/06/13/getting-started-with-backstage/)中描述的关于 Backstage 的工作。因此，在开始之前，您应该阅读那篇文章以了解整个概念。在很多地方，我会提到之前文章中描述和完成的内容。我在那里描述了如何配置和运行 Backstage，以及如何为示例 Spring Boot 应用程序构建基本模板。您应该熟悉所有这些基本术语，才能完全理解当前练习中发生的事情。

## 源代码

如果您想自己尝试，可以随时查看我的源代码。我们的示例 GitHub [仓库](https://github.com/piomin/backstage-templates) 包含使用 Backstage 技术 Skaffolder 编写的软件模板。在本文中，我们将分析一个专门针对 Kubernetes 的模板，该模板位于 `templates/spring-boot-basic-on-kubernetes` 目录中。克隆此仓库后，您只需按照我的说明操作即可。

以下是我们仓库的结构。除了模板之外，它还包含 Argo CD 模板，其中包含要应用于 Kubernetes 的 YAML 部署清单。

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

还有一个与本文相关的 Git [仓库](https://github.com/piomin/backstage.git)。它包含修改后的 Backstage 源代码，其中安装和配置了多个插件。本文详细介绍了使用插件扩展 Backstage 的过程。因此，您可以从头开始，一步一步地按照我的说明操作。但您也可以克隆该仓库中提交的代码的最终版本，并在您的笔记本电脑上运行它。

## 运行和准备 Kubernetes

在开始使用 Backstage 之前，我们需要运行和配置我们的 Kubernetes 集群实例。例如，它可以是 Minikube。一旦您拥有运行的集群，您就可以通过执行以下命令获取其控制平面 URL。如您所见，我的 Minikube 可在 `https://127.0.0.1:55782`
地址下访问，因此我以后需要在 Backstage 配置中设置它。

```
$ kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:55782
...
$ export K8S_URL=https://127.0.0.1:55782
```

我们需要在 Kubernetes 上安装 Prometheus 和 Argo CD。为了安装 Prometheus，我们将使用 `kube-prometheus-stack` Helm Chart。首先，我们应该使用以下命令添加 Prometheus Chart 仓库：

```
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

然后，我们可以运行以下命令在 `monitoring` 命名空间中安装 Prometheus：

```
$ helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
--version 60.3.0 \
-n monitoring --create-namespace
```

与 Prometheus 相同，对于 Argo CD，我们首先需要添加Chart 仓库：

`$ helm repo add argo https://argoproj.github.io/argo-helm`

对于 Argo CD，我们需要在 `values.yaml` 文件中提供额外的配置。我们必须为 Backstage 创建用户，该用户具有使用 `apiKey`
身份验证调用 HTTP API 的权限。这需要从 Skaffolder 模板自动创建 Argo CD `Application`
。

```yaml
configs:
  cm:
    accounts.backstage: apiKey,login
  rbac:
    policy.csv: |
      p, backstage, applications, *, */*, allow
```

让我们使用 values.yaml 文件中的配置在 argocd 名称空间中安装 Argo CD：

```
$ helm install argo-cd argo/argo-cd \
  --version 7.2.0 \
  -f values.yaml \
  -n argocd --create-namespace
```

除此之外，我们还需要为 `backstage` 用户生成 `apiKey`。首先，让我们为 Argo CD 和 Prometheus 服务启用端口转发，以便通过本地主机访问它们的 API。

```
$ kubectl port-forward svc/argo-cd-argocd-server 8443:443 -n argocd
$ kubectl port-forward svc/kube-prometheus-stack-prometheus 9090 -n monitoring
```

为了为 backstage 用户生成 apiKey，我们需要使用 `argocd` CLI 以 `admin` 用户身份登录 Argo CD。然后，我们需要为 backstage 帐户运行以下命令，并将生成的令牌导出为 `ARGOCD_TOKEN` 环境变量：

```
$ argocd account generate-token --account backstage
$ export ARGOCD_TOKEN='argocd.token=<generated_token>'
```

最后，让我们通过创建秘密来获取 Kubernetes 的长期 API 令牌：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: default-token
  namespace: default
annotations:
  kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
```

YAML然后，我们可以使用以下命令将其复制并导出为 `K8S_TOKEN` 环境变量：

```
$ export K8S_TOKEN=$(kubectl get secret default-token -o go-template='{{.data.token | base64decode}}')
```

仅出于测试目的，我们将 `cluster-admin` 角色添加到默认的 `ServiceAccount`。

```yaml
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

## 修改应用程序源代码框架以适应 Kubernetes

首先，我们将修改应用程序源代码框架中的几个方面。为了构建容器镜像，我们在 Maven `pom.xml` 中包含 `jib-maven-plugin`。此插件将在 `jib` Maven 配置文件中激活。

```xml
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

XML我们的源代码存储库还将包含 Skaffold 配置文件。使用 Skaffold，我们可以轻松地构建镜像并将应用程序部署到 Kubernetes，只需一步即可。镜像地址取决于 Skaffolder 模板中的 `orgName` 和 `appName` 参数。在镜像构建过程中，我们跳过测试并激活 Maven `jib` 配置文件。

```yaml
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

YAML为了在 Kubernetes 上部署应用程序，Skaffold 正在寻找 `k8s/deployment.yaml` 清单。我们只将此部署清单用于开发和自动化测试目的。在“生产”环境中，我们将 YAML 清单保存在单独的 Git 存储库中，并通过 Argo CD 应用它们。一旦我们在源代码中提供更改，CircleCI 将尝试将应用程序部署到临时 Kind 集群。因此，我们的 `Service` 在 `30000` 端口下作为 `NodePort` 公开。

```yaml
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

YAML让我们切换到 CircleCi 配置文件。它还包含与 Kubernetes 相关的几个更改。我们需要包含 `image-build` 作业，该作业负责使用 Jib 构建应用程序镜像并将其推送到目标注册表。我们还包含 `deploy-k8s` 作业以执行对 Kind 集群的测试部署。在此作业中，我们必须在 CircleCI 执行器机器上安装 Skaffold 和 Kind 工具。一旦 Kind 集群启动并准备就绪，我们通过执行 `skaffold run` 命令将应用程序部署到那里。

```yaml
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

## 安装 Backstage Kubernetes 插件

在上一篇关于 Backstage 的文章中，我们学习了如何安装 GitHub、CircleCI 和 Sonarqube 集成的插件。我们仍然会使用这些插件，但也会将我们的 Backstage 实例扩展一些额外的插件，主要用于 Kubernetes 原生环境。我们将安装以下插件：Kubernetes（后端 + 前端）、HTTP 请求操作（后端）、Argo CD（前端）和 Prometheus（前端）。让我们从 Kubernetes 插件开始。

### 安装 Kubernetes 插件
第一步，我们安装 Kubernetes 前端插件。它允许我们在 Backstage UI 中查看在 Kubernetes 上运行的应用程序 Pod。为了安装它，我们需要执行以下 `yarn` 命令：

```
$ yarn --cwd packages/app add @backstage/plugin-kubernetes
```


然后，我们需要在 `packages/app/src/components/catalog/EntityPage.tsx` 文件中进行一些更改。我们应该导入 `EntityKubernetesContent` 组件，然后将其包含在 `serviceEntityPage` 对象中，作为前端上的新路由。

```typescript
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
我们还需要安装 Kubernetes 后端插件，以使其在前端站点上正常工作。以下是所需的 `yarn` 命令：

```
$ yarn --cwd packages/backend add @backstage/plugin-kubernetes-backend
```


然后，我们应该在 `packages/backend/src/index.ts` 文件中注册 `plugin-kubernetes-backend` 模块。

```typescript
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

## 安装 HTTP 请求操作插件

该插件与 Kubernetes 无关。它允许我们通过 HTTP API 服务与第三方解决方案集成。正如你可能记得的，我们已经在 Backstage UI 中与 Sonarcloud 和 CircleCI 集成了。然而，我们并没有在那里创建任何项目。我们只能查看 Sonarcloud 或 CircleCI 中先前创建的项目的构建或扫描历史。是时候在我们的模板中更改它了！借助 HTTP 请求操作插件，我们将通过 REST API 创建 Argo CD 应用程序。和往常一样，我们需要执行 yarn add 命令来安装后端插件：

```typescript
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

接下来，我们可以使用前一篇文章中用到的一些附加步骤来修改一个 Skaffolder 模版。

## 准备 Kubernetes 的后台模板

一旦将所有内容放到位, 我们可以修改标准 Spring Boot 应用程序的先前模板, 以便将其适应 Kubernetes 要求。 
 
### 创建 Skaffolder 模板

首先, 我们添加一个单一的输入参数, 该参数表示运行我们的应用程序的 Kubernetes 中的目标命名空间 (1)。然后, 我们添加一些其他操作步骤。在其第一个步骤中, 我们生成 Argo CD 的 YAML 配置清单存储库 (2)。然后, 我们将在 GitHub 上发布该存储库, 仓库名为 ${{parameters.appName}}-gitops (3)。

之后, 我们将使用 HTTP 请求操作插件在 CircleCI 中自动跟踪新存储库 (5)。一旦我们在上一步中创建了此类存储库, CircleCI 便会在检测到该存储库后自动开始构建。我们还使用 HTTP 请求操作插件在 Sonarcloud 上创建与 ${{parameters.appName}} 相同名称的新存储库 (4)。最后, 我们通过 API 与 Argo CD 集成, 以创建一个新的应用程序, 该应用程序负责将应用程序部署应用到 Kubernetes (6)。此 Argo CD 应用程序将使用先前发布的配置存储库, 仓库名中带有 -config 后缀, 并应用 manifests 目录内的清单 。

```yaml
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

### 创建目录组件

我们的 catalog-info.yaml 文件应该包含与之前章节安装的插件相关的更多注释。argocd/app-name 注释表示负责在 Kubernetes 上部署的目标 Argo CD 应用程序的名称。backstage.io/kubernetes-id 注释包含用于在 Backstage UI 中显示的 Kubernetes 上搜索 Pod 的标签值。最后，prometheus.io/rule 注释包含 Prometheus 查询的逗号分隔列表。我们将创建显示应用程序 Pod CPU 和内存使用情况的图形。

```yaml
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

### 提供配置设置

我们需要在 app-config.yaml 文件中包含一些配置设置。它包括 proxy 部分，应包含 HTTP Request 动作插件和前端插件所需的所有 API。我们应该包含 CircleCI (1)、Sonarcloud (2)、Argo CD (3) 和 Prometheus (4) 的代理地址。之后，我们包括 Skaffolder 模板 (5) 的地址。我们还必须包含具有 Minikube 集群地址和先前生成的 service 帐户令牌的 kubernetes 部分 (6)。

```yaml
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

## 构建 Backstage 镜像

我们的 Backstage 源代码存储库包含所有必需的插件和配置。现在，我们将使用 yarn 工具构建它。这里列出一些执行构建所需的命令。

```shell
$ yarn clean
$ yarn install
$ yarn tsc
$ yarn build:backend 
```

后端已经包含了 Backstage 的存储库。它在 packages/backend 目录。

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

为了使用 packages/backend 目录中的 Dockerfile 构建镜像，我们需要从项目根目录运行以下命令。

```
$ yarn build-image
```

如果您看到类似结果，表示生成已成功完成。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-13.01.06.png?w=1392&ssl=1)


镜像可作为 backstage:latest 本地获取。使用以下命令可在 Docker 中运行它：

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

不过我们今天的目标是直接在 Kubernetes 中运行它。我的 Docker 注册表中提供了我们自定义的 Backstage 镜像：piomin/backstage:latest。

## 在 Kubernetes 上部署 Backstage 

我们将使用官方 Helm Chart 来在 Kubernetes 上安装 Backstage。在第一步中，让我们添加下列图表存储库：

```
$ helm repo add backstage https://backstage.github.io/charts
```

以下是用于 Helm 安装的 values.yaml 文件。我们需要将所有必需的令牌设置为 Backstage pod 中的额外环境变量。我们还将安装中使用的默认映像更改为之前构建的自定义映像。为了简化练习，我们可以禁用外部数据库并使用内部 SQLite 实例。不必重建 Docker 映像（my-app-config），只要将额外配置文件定义为 ConfigMap，即可对其进行传递。

```yaml
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

我们将通过修改 app-config.yaml 文件来将 Kubernetes 集群、Argo CD 和 Prometheus 的地址更改为内部集群位置。

```yaml
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

然后，我们将创建幕后命名空间和额外的 ConfigMap，其中包含 Kubernetes 集群内部运行的幕后的新配置。

```
$ kubectl create ns backstage
$ kubectl create configmap my-app-config \
  --from-file=app-config.extra.yaml=app-config-kubernetes.yaml -n backstage
```

最后，执行以下命令在 backstage 命名空间中安装我们自定义的后端实例：

```
$ envsubst < values.yaml | helm install backstage backstage/backstage \
  --values - -n backstage
```

因此，在 Kubernetes 中有一个正在运行的 Backstage pod：

```
$ kubectl get po -n backstage
NAME                         READY   STATUS    RESTARTS   AGE
backstage-7bfbc55647-8cj5d   1/1     Running   0          16m
```

启用端口转发以在 http://localhost:7007 访问 Backstage UI：

```
$ kubectl port-forward svc/backstage 7007 -n backstage
```

这次我们给我们实例 Backstage 所使用的后台命名空间的默认 ServiceAccount 增加权限：

```yaml
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

## 最终测试

通过访问后台 UI，我们可以从模板创建新的 Spring Boot 应用。选择“创建 Kubernetes 的 Spring Boot 应用”模板，如下所示：

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-14.43.35.png?w=1392&ssl=1)


如果您想自行尝试，则需要将组织名称更改为您的 GitHub 帐户名称。然后点击下一页上的“Review”和“Create”。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-14.46.44.png?w=1392&ssl=1)

将创建两个 GitHub 存储库。第一个存储库包含示例应用程序源代码。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.35.20.png?w=1392&ssl=1)


第二个包含用于 Argo CD 部署的 YAML 清单。Argo CD 应用程序将自动创建。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.35.58.png?w=1392&ssl=1)

我们可以在 Backstage UI 中验证同步状态。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.53.37.png?w=812&ssl=1)


我们的应用程序在 demo 命名空间中运行。我们可以“KUBERNETES”选项卡中显示 Pod 列表。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.38.17.png?w=1392&ssl=1)


我们还可以验证每个 Pod 的详细信息状态。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.56.13.png?w=938&ssl=1)

或者查看日志。

![](https://i0.wp.com/piotrminkowski.com/wp-content/uploads/2024/06/Screenshot-2024-06-28-at-16.56.31.png?w=1392&ssl=1)

## 最终思考 

在本文中，我们学习了如何使用 Argo CD 或 Prometheus 等 Kubernetes 原生服务安装并集成 Backstage。我们使用 Backstage 构建了自定义镜像，然后使用 Helm Chart 将其部署到 Kubernetes 上。