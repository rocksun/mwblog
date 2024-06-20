
<!--
title: 解锁Prometheus替代品VictoriaMetrics的强大功能
cover: https://developer-friendly.blog/assets/images/social/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative.png
-->

了解监控至关重要的原因，探索 VictoriaMetrics 和部署步骤，并从 Prometheus 无缝迁移。适用于所有监控工作负载。

> 译自 [Unlocking the Power of VictoriaMetrics: A Prometheus Alternative - Developer Friendly Blog](https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/)，作者 None。

在任何组织中，运维团队的主要任务之一是为平台、应用程序和整个基础设施提供一个可靠且强大的监控解决方案。

监控使企业主能够了解其应用程序在生产环境中的行为方式、如何优化应用程序以及如何主动微调和预测平台的未来增长。

在这篇博文中，我们将探讨 Victoria Metrics 提供的功能，以及如何对其进行设置和配置，使其成为 Prometheus 的替代方案和 Grafana 的数据存储。

## 为什么监控至关重要？

监控至关重要，因为它可以让你实时和历史性地了解系统的运行状况和性能，帮助你在问题升级为更大问题之前发现问题。

将监控视为对系统和基础设施的持续健康检查，确保一切顺利高效地运行。

通过成功的监控，可以优化资源使用，防止宕机，快速解决意外行为，并进行容量规划，最终节省时间并降低成本。

此外，它还为提高未来性能和规划容量提供了有价值的数据，使其成为管理任何技术环境不可或缺的一部分。

## Victoria Metrics 简介

Victoria Metrics 是一个高性能、经济高效的时间序列数据库，专为监控和可观察性而设计。它以其速度、效率和可扩展性而闻名，使其成为轻松处理海量数据的绝佳选择。

此外，它与 Prometheus 完全兼容，为那些希望迁移其当前监控设置的人提供了轻松的过渡。

## 为什么选择 Victoria Metrics？

Victoria Metrics 脱颖而出是因为多种因素。

首先，它具有可扩展性，是处理大量时间序列数据的完美选择。

此外，它被设计为 Prometheus 的替代方案，提供**更快的查询**、更好的压缩和多租户支持。

对我个人而言，我遇到 Victoria Metrics 是在为 Prometheus 寻找长期存储解决方案。在查看可用工具时，最引人注目的工具是 Victoria Metrics 和 Thanos。

我选择 Victoria Metrics，因为它更节约资源，并且更容易设置和配置。使用 Thanos，有一个巨大的学习曲线，而且开销和可维护性成本超过了收益。

## Victoria Metrics 的主要功能

- 提供高性能和快速查询功能。
- 提供高效的数据压缩以节省存储空间，例如，它在 HDD 存储上提供了不错的性能。
- 确保使用多租户支持平稳处理多个数据源。
- 提供与 Prometheus 的轻松兼容性，便于集成。
- 轻松扩展以管理大型数据集。

## Victoria Metrics 与 Prometheus

- **资源利用率**：Victoria Metrics 比 Prometheus 更省内存和 CPU，使其成为一种经济高效的解决方案。我个人在切换到 Victoria Metrics 时看到内存占用减少了 50%。
- **长期存储**：Victoria Metrics 本身支持长期存储，而使用 Prometheus，你需要设置一个单独的解决方案，如 Thanos。[⁷](#fn:prometheus-long-term-storage)
- **可扩展性**：Victoria Metrics 被设计为在垂直和水平方向上都具有可扩展性。另一方面，Prometheus 在这方面做得不够，需要额外的工具（如 Thanos）来扩展。

## 部署 Victoria Metrics

对于本指南，我们将使用[Kubernetes](/category/kubernetes/) 部署 Victoria Metrics。随意选择一种简单的方法来创建你的集群，例如 Minikube、Kind 或 K3s。

如果你有兴趣，我们存档中还有其他指南来设置 Kubernetes 集群：

- [Kubernetes 困难之路](../../../03/03/kubernetes-the-hard-way/)
- [如何在 Ubuntu 22.04 上安装轻量级 Kubernetes](../../../03/22/how-to-install-lightweight-kubernetes-on-ubuntu-2204/)
- [使用 OpenTofu 创建 Azure AKS 集群](../../../04/29/external-secrets-operator-fetching-aws-ssm-parameters-into-azure-aks/#step-0-setting-up-azure-managed-kubernetes-cluster)

下图显示了这篇博文的安装架构。

![](https://yylives.cc/wp-content/uploads/2024/06/p1.png)

### Victoria Metrics Operator

官方提供的 Victoria Metrics Operator 与替代的一次性安装方法相比有很多优势。9

使用 Victoria Metrics Operator，你可以使用一个或多个 CRD 资源来决定 Victoria Metrics 的架构。从长远来看，它更灵活。

我们使用 [FluxCD](/category/fluxcd/) 作为我们选择的 [GitOps](/category/gitops/) 工具，但你可以随意使用你熟悉的任何其他工具。

**victoria-metrics-operator/namespace.yml**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: monitoring
```

**victoria-metrics-operator/repository.yml**

```yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmRepository
metadata:
  name: victoria-metrics
spec:
  interval: 60m
  url: https://victoriametrics.github.io/helm-charts/
```

**victoria-metrics-operator/release.yml**

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: victoria-metrics-operator
spec:
  chart:
    spec:
      chart: victoria-metrics-operator
      sourceRef:
        kind: HelmRepository
        name: victoria-metrics
      version: 0.x
  interval: 30m
  maxHistory: 10
  releaseName: victoria-metrics-operator
  timeout: 5m
```

victoria-metrics-operator/kustomization.yml

```yaml
resources:
  - namespace.yml
  - repository.yml
  - release.yml
  ```

**victoria-metrics-operator/kustomize.yml**

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: victoria-metrics-operator
  namespace: flux-system
spec:
  force: false
  interval: 5m
  path: ./victoria-metrics-operator
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-system
  targetNamespace: monitoring
  wait: true
```

最后，要部署此堆栈：

```
kubectl apply -f victoria-metrics-operator/kustomize.yml
```

### Victoria Metrics CRD

安装了 Victoria Metrics Operator 后，我们可以查询并查看 Kubernetes 集群中提供了相应的 CRD。

```
kubectl api-resources | grep victoriametrics
```

输出如下：

![点击放大 Victoria Metrics Operator CRD](https://developer-friendly.blog/static/img/2024/0016/vm-api-resources.webp)

*Victoria Metrics Operator CRDs*


只需查看此处的 CRD，你就可以快速了解这种安装模式有多么强大以及它提供了多少灵活性。因为在任何时间点，你都可以扩展 VictoriaMetrics 实例组件，调整大小或使用不同的架构完全替换它们。

例如，在任何 Victoria Metrics 组件实例上提供身份验证的最快速方法之一是创建
VMAuth 作为代理和一个或多个 VMUser CRD。

请参阅以下示例。

```yaml
---
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAuth
metadata:
  name: auth-proxy
spec:
  selectAllByDefault: true
---
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMUser
metadata:
  name: john-doe
spec:
  generatePassword: true
  targetRefs:
    - static:
        urls:
          - http://victoria-metrics.monitoring:8428
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: vmproxy
spec:
  hostnames:
    - vmproxy.developer-friendly.blog
  parentRefs:
    - group: gateway.networking.k8s.io
      kind: Gateway
      name: developer-friendly-blog
      namespace: cert-manager
      sectionName: https
  rules:
    - backendRefs:
        - kind: Service
          name: vmauth-auth-proxy
          port: 8427
      filters:
        - responseHeaderModifier:
            set:
              - name: Strict-Transport-Security
                value: max-age=31536000; includeSubDomains; preload
          type: ResponseHeaderModifier
      matches:
        - path:
            type: PathPrefix
            value: /
```

应用这些资源后几秒钟，将在目标命名空间中创建一个新的 Kubernetes 服务和一个 Secret。

我们可以通过运行以下命令获取用户的相应密码：

```bash
kubectl get \
  -n monitoring \
  secret/vmuser-john-doe \
  -o jsonpath='{.data.password}' | \
  base64 -d -
```

有了从 Secret 中获取的密码和 HTTPRoute 资源中的地址，我们将在首次访问该地址时收到基本 HTTP 身份验证提示。

![点击放大 VMAuth 身份验证代理](https://developer-friendly.blog/static/img/2024/0016/vmauth-basic-auth.webp)

此架构最好的地方在于它的任何部分都可以由你首选的工具替换。如果你选择使用不同的身份验证代理服务器，例如 [Ory Oathkeeper](/category/oathkeeper/) 来利用你当前的身份 provider，你当然可以。

## 从 Kube Prometheus 堆栈迁移

在这一点上，我们将假设你在集群中安装了 Kube Prometheus 堆栈。由于 Kube Prometheus 堆栈被广泛采用，因此这个假设并不牵强。

该堆栈附带了许多 CRD，这些 CRD 使得为 Prometheus 服务器发现新目标变得更加容易。
### Installing Victoria Metrics Operator

By default, unless explicitly disabled, you opt in to automatic conversion of every Prometheus Stack CRD to a Victoria Metrics Operator CRD.13
Essentially, this means that the following conversion table applies to you:

| Kube Prometheus Stack CRD | Victoria Metrics Operator CRD |
|---|---|
| ServiceMonitor | VMServiceScrape |
| PodMonitor | VMPodScrape |
| Probe | VMProbe |
| PrometheusRule | VMRule |
| AlertmanagerConfig | VMAlertmanagerConfig |
| ScrapeConfig | VMScrapeConfig |

With this table in mind, the overhead of moving from Prometheus to Victoria Metrics is minimal. All of your current scrape targets (e.g.,14 ServiceMonitors and PodMonitors) will continue to work when you replace your Prometheus server with a VMAgent instance; the Victoria Metrics Operator takes care of the CRD conversion, and the VMAgent will scrape those targets.
Your Grafana dashboards will also continue to work as expected, you just need to change the data source address from your Prometheus URL to the Victoria Metrics address.

## Using Victoria Metrics to Scrape Targets

At this point, we should be down to the last goal of this blog post. Our goal is to use Victoria Metrics components to scrape targets and send them to storage for later querying.
Therefore, our goal is to provide the following variations:
- Shipping metrics from kube-state-metrics and node-exporter to Victoria Metrics, as you saw earlier in the [diagram above](#deploy-victoria-metrics).
- Shipping metrics from the same sources to Grafana Cloud.
- Shipping metrics from another Prometheus instance or VMAgent elsewhere to a standalone Victoria Metrics deployment.

### Deploying Victoria Metrics to a Kubernetes Cluster

For a Victoria Metrics storage deployment, you can choose to deploy each component individually or all in one instance. The former gives you greater scalability, while the latter gives you greater simplicity.15
We will deploy a VMCluster in this section, and leave VMSingle for the [last section](#monitor-standalone-hosts-with-victoria-metrics).
We start by deploying the storage component, the query component (select), and the ingestion component (insert). These components are the core of Victoria Metrics.16
```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMCluster
metadata:
  name: vmserver
spec:
  retentionPeriod: 1d
  vmstorage:
    replicaCount: 1
    storage:
      volumeClaimTemplate:
        spec:
          resources:
            requests:
              storage: "1Gi"
  vmselect:
    replicaCount: 1
    storage:
      volumeClaimTemplate:
        spec:
          resources:
            requests:
              storage: "1Gi"
  vminsert:
    replicaCount: 1
```

Next, we deploy a VMAgent, which will scrape metrics from any discovered targets and send them to the cluster created using VMCluster.
```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAgent
metadata:
  name: vmscrape
spec:
  extraArgs:
    promscrape.maxScrapeSize: 32MiB
  selectAllByDefault: true
  remoteWrite:
  - url: http://vminsert-vmserver.monitoring:8480/insert/0/prometheus
```

Note that in the VMAgent, the URL we pass to remote-write comes from our VMCluster instance, which can be verified via the kubectl get service command, as well as by looking at the Victoria Metrics endpoints documentation.17
```yaml
remoteWrite:
- url: http://vminsert-vmserver.monitoring:8480/insert/0/prometheus
```

Finally, we need to be able to access the UI from a browser. As you can see below, the remaining components are there to do just that.18
```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAuth
metadata:
  name: auth-proxy
spec:
  selectAllByDefault: true
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMUser
metadata:
  name: vmadmin
spec:
  generatePassword: true
  targetRefs:
  # vmui + vmselect
  - crd:
      kind: VMCluster/vmselect
      name: vmserver
      namespace: monitoring
    target_path_suffix: "/select/0"
    paths:
    - "/vmui"
    - "/vmui/.*"
    - "/prometheus/api/v1/query"
    - "/prometheus/api/v1/query_range"
    - "/prometheus/api/v1/series"
    - "/prometheus/api/v1/status/.*"
    - "/prometheus/api/v1/label/"
    - "/prometheus/api/v1/label/[^/]+/values"
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: victoria-metrics
spec:
  hostnames:
  - victoria-metrics.developer-friendly.blog
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: Gateway
    name: developer-friendly-blog
    namespace: cert-manager
  sectionName: https
  rules:
  - backendRefs:
    - kind: Service
      name: vmauth-auth-proxy
      port: 8427
    filters:
    - responseHeaderModifier:
        set:
        - name: Strict-Transport-Security
          value: max-age=31536000; includeSubDomains; preload
      type: ResponseHeaderModifier
    matches:
    - path:
        type: PathPrefix
        value: /
```

### Resources
- [vmcluster.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/vmcluster.yml)
- [vmagent.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/vmagent.yml)
- [vmuser.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/vmuser.yml)
- [vmauth.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/vmauth.yml)
- [httproute.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/httproute.yml)
- [kustomization.yml](https://github.com/VictoriaMetrics/operator/blob/main/config/samples/kustomization.yml)
### Corrected Markdown Format

**Deploying the Stack**

**targetNamespace: monitoring**
**wait: true**

Finally, to deploy this stack:

- Open the target address at the `/vmui` endpoint, and we should see the Victoria Metrics query dashboard, as shown below.
  ![Click to enlarge Victoria Metrics UI](/static/img/2024/0016/vm-cluster-ui.webp)
  ![Click to enlarge Victoria Metrics UI](/static/img/2024/0016/vm-cluster-ui.webp)

This concludes [our first objective](#scrape-targets-with-victoria-metrics), scraping and sending metrics from the same cluster.

### Remote Write Victoria Metrics to Grafana Cloud

[¶](#remote-write-victoria-metrics-to-grafana-cloud)

Grafana Cloud makes it super easy to send metrics with minimal overhead. You are only responsible for the scraping targets. The rest is handled by their infrastructure, including storage, querying, scaling, availability, etc.

Let's create a `VMAgent` to scrape all metrics and send them to Grafana Cloud.

**Grafana Cloud Account**

If you don't have an account yet, they offer a generous free tier for you to try out their service.
. 19

For Prometheus servers, you will have a remote write URL, similar to the one you see below.

```yaml
remote_write:
- url: https://prometheus-prod-24-prod-eu-west-2.grafana.net/api/prom/push
basic_auth:
username: 123456
password: <Your Grafana.com API token>
```

Let's use this configuration to create such a `VMAgent` instance.

```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMAgent
metadata:
name: vmscrape
spec:
extraArgs:
promscrape.maxScrapeSize: 32MiB
selectAllByDefault: true
remoteWrite:
- url: https://prometheus-prod-24-prod-eu-west-2.grafana.net/api/prom/push
basicAuth:
password:
key: password
name: grafana-cloud-secret
optional: false
username:
key: username
name: grafana-cloud-secret
optional: false
```

This agent will also scrape all `VMServiceScrape` and `VMPodScrape` resources, just like the previous one.

However, the difference is that this agent will send the metrics to Grafana Cloud's remote write URL, and we no longer have to manage any storage or [Grafana](/category/grafana/) instances.

### Monitor Standalone Hosts with Victoria Metrics

[¶](#monitor-standalone-hosts-with-victoria-metrics)

To address [the last objective](#scrape-targets-with-victoria-metrics), our goal is to do things a bit differently, as we will scrape target hosts from a standalone machine (outside of [Kubernetes](/category/kubernetes/)) and send those hosts to the in-cluster Victoria Metrics that we created using the `VMSingle` CRD resource.

Since this is considered a standalone machine, we will use our beloved tool [Ansible](/category/ansible/). This helps with reproducibility and documents the steps for future reference.

---
```yaml
vmutils_url: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.101.0/vmutils-linux-arm64-v1.101.0.tar.gz
---
vmutils_url: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.101.0/vmutils-linux-amd64-v1.101.0.tar.gz
```

```ini
[Unit]
Description=Victoria Metrics - VMAgent
Documentation=https://github.com/VictoriaMetrics/VictoriaMetrics
[Service]
ExecStart=/usr/local/bin/vmagent-prod \
-promscrape.config=/etc/victoria-metrics/vmagent.yml \
-remoteWrite.url={{ remote_write_url }} \
-influxListenAddr='' \
-httpListenAddr='' \
-remoteWrite.tmpDataPath=/var/lib/victoria-metrics/remote-write-data
Restart=always
RestartSec=5
[Install]
WantedBy=multi-user.target
```

```yaml
global:
scrape_interval: 30s
scrape_configs:
- job_name: node-exporter
static_configs:
- targets:
- localhost:9100
labels:
instance: {{ ansible_hostname }}
- name: Include host-specific variables
ansible.builtin.include_vars:
file: vars-{{ ansible_architecture }}.yml
- name: Download vmutils
ansible.builtin.get_url:
url: "{{ vmutils_url }}"
dest: "/tmp/{{ vmutils_url | basename }}"
mode: "0444"
owner: root
group: root
register: vmutils_download
- name: Extract binaries
ansible.builtin.unarchive:
src: "{{ vmutils_download.dest }}"
dest: /usr/local/bin/
remote_src: true
mode: "0755"
owner: root
group: root
extra_opts:
- vmagent-prod
- vmalert-prod
- vmalert-tool-prod
- vmauth-prod
- vmbackup-prod
- vmrestore-prod
- vmctl-prod
- name: Ensure victoria-metrics related directories exist
ansible.builtin.file:
path: "{{ item }}"
state: directory
owner: root
group: root
mode: "0755"
loop:
- /var/lib/victoria-metrics
- /etc/victoria-metrics
- name: Copy service file
ansible.builtin.template:
src: vmagent.service.j2
dest: /etc/systemd/system/vmagent.service
owner: root
group: root
mode: "0644"
notify: Restart vmagent service
- name: Copy config file
ansible.builtin.template:
src: vmagent.yml.j2
dest: /etc/victoria-metrics/vmagent.yml
owner: root
group: root
mode: "0444"
notify: Restart vmagent service
- name: Start vmagent service
ansible.builtin.systemd:
name: vmagent
state: started
enabled: true
daemon_reload: true
---
- name: Restart vmagent service
ansible.builtin.systemd:
name: vmagent
state: restarted
daemon_reload: true
```
有了这个 Ansible 角色，我们现在可以使用它来监控我们的目标主机。

但是，在执行此操作之前，让我们将一个 VMSingle 实例部署到我们的 Kubernetes 集群，如前所述。

```yaml
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMSingle
metadata:
  name: standalone
spec:
  retentionPeriod: "1"
  removePvcAfterDelete: true
  extraArgs:
    dedup.minScrapeInterval: 10s
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: victoria-metrics
spec:
  hostnames:
    - vmsingle.developer-friendly.blog
  parentRefs:
    - group: gateway.networking.k8s.io
      kind: Gateway
      name: developer-friendly-blog
      namespace: cert-manager
  sectionName: https
  rules:
    - backendRefs:
        - kind: Service
          name: vmsingle-standalone
          port: 8429
      filters:
        - responseHeaderModifier:
            set:
              - name: Strict-Transport-Security
                value: max-age=31536000; includeSubDomains; preload
            type: ResponseHeaderModifier
          matches:
            - path:
                type: PathPrefix
                value: /
```

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: victoria-metrics-standalone
  namespace: flux-system
spec:
  force: false
  interval: 5m
  path: ./victoria-metrics-standalone
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-system
  targetNamespace: monitoring
  wait: true
```

最后，要部署此堆栈：

```
kubectl apply -k ./victoria-metrics-standalone
```

现在，我们准备运行以下 Ansible 剧本。

```yaml
- name: 使用 Victoria Metrics 监控目标
  hosts: monitoring
  roles:
    - victoria-metrics
  vars:
    remote_write_url: https://vminsert.developer-friendly.blog/api/v1/write
```

所有这些方法只是使用 [Victoria Metrics](/category/victoriametrics/) 监控基础架构的众多方法中的一部分。我们介绍了一些通常用于监控生产设置的最典型方法。这应该让你对如何开始使用 Victoria Metrics 有一个很好的了解。

## 结论

[¶](#conclusion)

Victoria Metrics 是一款功能强大、高性能且资源高效的监控解决方案，可以轻松替换监控堆栈中的 Prometheus。它提供了广泛的功能，使其成为处理大规模数据和优化监控性能的理想选择。尽管我们在这篇博文中没有介绍，但 VictoriaMetrics 还提供了一款日志记录产品，其功能与他们的指标产品一样强大。

通过按照本指南中概述的步骤，你可以毫不费力地迁移或集成当前的监控设置与 Victoria Metrics，并利用其高级功能和优势。

我们介绍了一些最常见的模式，用于监控目标主机并使用 Victoria Metrics 提取指标。你可以使用这些示例以适合你环境的方式构建自己的监控解决方案。

如果你正在寻找一款高性能、可扩展且经济高效的监控解决方案，那么 Victoria Metrics 绝对值得考虑。

今天就试一试，看看它如何改变你的监控体验！

祝黑客愉快，下次再见，

*ciao*。如果你喜欢这篇博文，请考虑使用这些按钮分享它。请在最后给我们留言，我们阅读并喜爱所有留言。

**[分享到 ](https://news.ycombinator.com/submitlink?u=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/&t=Unlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A)**

**[分享到 ](https://www.linkedin.com/sharing/share-offsite/?url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/)**

**[分享到 ](https://www.reddit.com/submit?url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/&title=Unlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A)**

**[分享到 ](https://twitter.com/intent/tweet?text=%40devfriendly_%0AUnlocking%20the%20Power%20of%20VictoriaMetrics%3A%20A%20Prometheus%20Alternative%0A&url=https://developer-friendly.blog/2024/06/17/unlocking-the-power-of-victoriametrics-a-prometheus-alternative/)**

-
-
-
[https://medium.com/@seifeddinerajhi/victoriametrics-a-comprehensive-guide-comparing-it-to-prometheus-and-implementing-kubernetes-03eb8feb0cc2](https://medium.com/@seifeddinerajhi/victoriametrics-a-comprehensive-guide-comparing-it-to-prometheus-and-implementing-kubernetes-03eb8feb0cc2) [↩](#fnref:seifeddinerajhi-medium)
-
-
[https://docs.victoriametrics.com/single-server-victoriametrics/#prominent-features](https://docs.victoriametrics.com/single-server-victoriametrics/#prominent-features) [↩](#fnref:vm-prominent-features)
-
-
[https://victoriametrics.com/blog/comparing-agents-for-scraping/](https://victoriametrics.com/blog/comparing-agents-for-scraping/) [↩](#fnref:vm-blog-comparing-agents)
-
### MARKDOWN TEXT CORRECTED

[https://zetablogs.medium.com/prometheus-vs-victoria-metrics-load-testing-3fa0cc782912](https://zetablogs.medium.com/prometheus-vs-victoria-metrics-load-testing-3fa0cc782912) [↩](#fnref:vm-vs-prom-perf)

-

[https://prometheus.io/docs/prometheus/latest/storage/#operational-aspects](https://prometheus.io/docs/prometheus/latest/storage/#operational-aspects) [↩](#fnref:prometheus-long-term-storage)

-

-

[https://artifacthub.io/packages/helm/victoriametrics/victoria-metrics-operator/0.32.2](https://artifacthub.io/packages/helm/victoriametrics/victoria-metrics-operator/0.32.2) [↩](#fnref:vm-operator)

-

-

-

[https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack/60.1.0](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack/60.1.0) [↩](#fnref:k8s-prom-stack)

-

[https://docs.victoriametrics.com/operator/migration/#objects-conversion](https://docs.victoriametrics.com/operator/migration/#objects-conversion) [↩](#fnref:vm-object-conversion)

-

-

[https://docs.victoriametrics.com/cluster-victoriametrics/#architecture-overview](https://docs.victoriametrics.com/cluster-victoriametrics/#architecture-overview) [↩](#fnref:vm-cluster-arch)

-

[https://docs.victoriametrics.com/operator/quick-start/#vmcluster-vmselect-vminsert-vmstorage](https://docs.victoriametrics.com/operator/quick-start/#vmcluster-vmselect-vminsert-vmstorage) [↩](#fnref:vm-cluster)

-

[https://docs.victoriametrics.com/cluster-victoriametrics/#url-format](https://docs.victoriametrics.com/cluster-victoriametrics/#url-format) [↩](#fnref:vm-url-formats)

-

[https://docs.victoriametrics.com/operator/quick-start/#vmauth](https://docs.victoriametrics.com/operator/quick-start/#vmauth) [↩](#fnref:vm-operator-vmauth)

-