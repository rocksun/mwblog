<!--
title: OWASP Dependency Track —— Kubernetes上的组件分析平台
cover: ./cover.png
-->

在快节奏的软件开发世界中，有效管理依赖关系至关重要。

> 译自 [OWASP Dependency Track — Component Analysis platform](https://levelup.gitconnected.com/owasp-dependency-track-component-analysis-platform-23166dd92b98)。作者 Renjith Ravindranathan 。

在快节奏的软件开发世界中，有效管理依赖关系对构建安全可靠的应用程序至关重要。在开源软件安全领域获得认可的一款工具是 OWASP Dependency-Track。本文旨在全面介绍 Dependency Track，深入了解其功能、目的以及在 Kubernetes 上部署的方法。

## 什么是 OWASP Dependency Track？

Dependency-Track 是一个开源组件分析平台，是开放网络应用安全项目（OWASP）的一项倡议。它旨在持续提供对应用程序组件及其相关风险的可见性。该工具帮助开发团队识别、管理和减少由第三方和内部组件引入的风险。

## 主要功能

**1. 组件分析：**

Dependency-Track 分析应用程序中使用的组件，检查其版本、许可证和已知漏洞。这有助于了解与每个依赖关系相关的风险。

**2. 漏洞管理：**

与各种漏洞数据库集成的平台，提供关于组件已知漏洞的实时信息。这有助于团队主动解决安全问题。

**3. 策略管理：**

Dependency-Track 支持基于组织风险容忍度的策略创建和执行。团队可以定义和执行有关可接受组件版本和许可证的规则。

**4. 持续监控：**

通过对持续集成和持续交付（CI/CD）流水线的支持，Dependency-Track 确保组件风险概况在整个开发生命周期中持续监控和更新。

**5. 可扩展性：**

为可扩展性而设计，Dependency-Track 支持大型代码库，并能处理具有大量依赖关系的复杂软件项目。

## 在 Kubernetes 上开始使用 Dependency Track

可以通过 Helm Chart 安装 Dependency Track。有一个旧的由 OSS 驱动的 Chart 可用，我们可以使用最新的镜像数值更新它并执行。

1. 将 Helm Chart 存储库添加到您的机器上

```bash
helm repo add evryfs-oss https://evryfs.github.io/helm-charts/
helm repo update
```

2. 使用编辑过的 values 文件将其应用到您的集群

```bash
helm install dependency-track evryfs-oss/dependency-track --namespace dtrack --create-namespace --values values.yaml
```

```yaml
# Default values for dependency-track.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.
# Since dependency-track 4.0, there are now two separate images. One for frontend, one for the apiserver.

# -- global configuration
global:
  imageRegistry: docker.io
frontend:
  enabled: true
  annotations: {}
  replicaCount: 1
  image:
    repository: dependencytrack/frontend
    tag: 4.10.0
    pullPolicy: IfNotPresent
  # https://github.com/DependencyTrack/frontend/issues/60
  # configmap:
  #  config: |
  #    {
  #      "API_BASE_URL": "http://localhost:8081",
  #      "OIDC_ISSUER": "https://gitlab.com",
  #      "OIDC_CLIENT_ID": "dsds",
  #      "OIDC_SCOPE": "openid profile email",
  #      "OIDC_FLOW": ""
  #    }
  # --See https://docs.dependencytrack.org/getting-started/configuration/ for frontend ENV variables.
  env:
  - name: API_BASE_URL
    value: ""
  - name: OIDC_ISSUER
    value: ""
  - name: OIDC_CLIENT_ID
    value: ""
  - name: OIDC_SCOPE
    value: ""
  - name: OIDC_FLOW
    value: ""
    # See https://docs.dependencytrack.org/getting-started/configuration/ for frontend ENV variables.
#  podSecurityContext:
#    fsGroup: 1000
  securityContext:
    allowPrivilegeEscalation: false
    # rootfs cannot be R/O because there is some messing around with file generation and whatnot
    runAsUser: 101
  service:
    type: ClusterIP
    port: 80
    annotations: {}
  nodeSelector: {}
  tolerations: []
  affinity: {}
  emptyDir:
    sizeLimit: 8Gi
  resources:
  # https://docs.dependencytrack.org/getting-started/deploy-docker/
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 1
      memory: 512Mi
  nameOverride: ""
  fullnameOverride: ""
  initContainers: []
  serviceAccount:
    # Specifies whether a service account should be created
    create: true
    # The name of the service account to use.
    # If not set and create is true, a name is generated using the fullname template
    name: frontend-serviceaccount
    # Annotations to add
    # Example:
    #  iam.gke.io/gcp-service-account: a@b.com
    annotations: {}
  livenessProbe:
    enabled: true
    path: "/"
    initialDelaySeconds: 60
    periodSeconds: 10
    timeoutSeconds: 2
    successThreshold: 1
    failureThreshold: 3
  readinessProbe:
    enabled: true
    path: "/"
    initialDelaySeconds: 60
    periodSeconds: 10
    timeoutSeconds: 2
    successThreshold: 1
    failureThreshold: 3


# -- config of the apiserver
apiserver:
  enabled: true
  annotations: {}
# Max: 1 - DT is not designed for HA
  replicaCount: 1
  image:
    repository: dependencytrack/apiserver
    tag: 4.8.0
    pullPolicy: IfNotPresent
    env:
    - name: ALPINE_OIDC_ENABLED
      value: ""
    - name: ALPINE_OIDC_ISSUER
      value: "
    - name: ALPINE_OIDC_CLIENT_ID
      value: ""
    - name: ALPINE_OIDC_USERNAME_CLAIM
      value: ""
    - name: ALPINE_OIDC_TEAMS_CLAIM
      value: ""
    - name: ALPINE_OIDC_USER_PROVISIONING
      value: ""
    - name: ALPINE_OIDC_TEAM_SYNCHRONIZATION
      value: ""
    - name: ALPINE_CORS_ENABLED
      value: "true"
    - name: ALPINE_CORS_ALLOW_ORIGIN
      value: "*"
    - name: ALPINE_CORS_ALLOW_METHODS
      value: "GET, POST, PUT, DELETE, OPTIONS"
    - name: ALPINE_CORS_ALLOW_HEADERS
      value: "Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count, *"
    - name: ALPINE_CORS_EXPOSE_HEADERS
      value: "Origin, Content-Type, Authorization, X-Requested-With, Content-Length, Accept, Origin, X-Api-Key, X-Total-Count"
    - name: ALPINE_CORS_ALLOW_CREDENTIALS
      value: "true"
    - name: ALPINE_CORS_MAX_AGE
      value: "3600"
    - name: EXTRA_JAVA_OPTIONS
      value: "-Xmx6G"
  persistentVolume:
    accessModes:
    - ReadWriteOnce
    enabled: true
    size: 8Gi
    annotations: {}
    storageClass: ""
  podSecurityContext:
    fsGroup: 1000
  securityContext:
    readOnlyRootFilesystem: true
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
  service:
    type: ClusterIP
    port: 80
    annotations: {}
  nodeSelector: {}
  tolerations: []
  affinity: {}
  emptyDir:
    sizeLimit: 8Gi
  resources:
  # https://docs.dependencytrack.org/getting-started/deploy-docker/
    requests:
      cpu: 1
      memory: 4Gi
    limits:
      cpu: 4
      memory: 4Gi
  nameOverride: ""
  fullnameOverride: ""
  initContainers: []
  serviceAccount:
    # Specifies whether a service account should be created
    create: true
    # The name of the service account to use.
    # If not set and create is true, a name is generated using the fullname template
    name: apiserver-serviceaccount
    # Annotations to add
    # Example:
    #  iam.gke.io/gcp-service-account: a@b.com
    annotations: {}
  # See https://docs.dependencytrack.org/getting-started/configuration/ for backend configuration options.
  livenessProbe:
    enabled: true
    path: "/api/version"
    initialDelaySeconds: 60
    periodSeconds: 10
    timeoutSeconds: 2
    successThreshold: 1
    failureThreshold: 3
  readinessProbe:
    enabled: true
    path: "/"
    initialDelaySeconds: 60
    periodSeconds: 10
    timeoutSeconds: 2
    successThreshold: 1
    failureThreshold: 3

# -- configuration of ingress
ingress:
  enabled: false
  tls:
    enabled: false
    secretName: ""
  annotations: {}
    # kubernetes.io/ingress.class: nginx
    # kubernetes.io/tls-acme: "true"
    ## allow large bom.xml uploads:
    # nginx.ingress.kubernetes.io/proxy-body-size: 10m
  host: chart-example.local
  # ingressClassName: nginx

# -- configuration of postgres
postgresql:
  enabled: true
  postgresqlUsername: deptrack
  postgresqlPassword: deptrack
  postgresqlDatabase: deptrack
```

Deploument 将创建三个 Pod —— 前端、API 服务器 和 后端（PostgreSQL）。请注意 `API_BASE_URL`，我们需要在 values 文件中指定。此值应为 API Pod 的公共端点，如果您提供本地值，将导致通信失败。如果一切正常，您可以通过端口 80 的前端端点登录。

![](https://miro.medium.com/v2/resize:fit:700/1*4nO08O9cBXQmQeICO1M76g.png)

*登录界面 —— Dependency Track*

![](https://miro.medium.com/v2/resize:fit:700/1*YRbj9luQZdl2peT0he39yQ.png)

*在 DT 中创建的项目和列出的 SBOM*

在下一篇文章中，我将展示推送容器镜像 cosigned 的实施工作流程，同时使用 CI/CD 引擎将 SBOM 并行推送到 Dependency Track。敬请关注！

## 结论

OWASP Dependency Track 在安全软件开发工具中扮演着至关重要的角色。通过组件分析、漏洞扫描、策略执行、持续监控和补救支持的结合，Dependency-Track 提供了一个全面的解决方案，用于管理和减轻与软件依赖关系相关的安全风险。其集成、可扩展性和对持续改进的重视使其成为现代软件应用程序中漏洞不断威胁的持续战斗中的宝贵助手。将 Dependency-Track 纳入开发生命周期不仅是一项安全措施；它是朝着构建具有弹性和安全性的软件迈出的积极一步。
