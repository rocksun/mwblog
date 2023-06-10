# 创建具有运行时可观测性的 Kubernetes 集群

翻译自 [Creating a Kubernetes Cluster with Runtime Observability](https://opentelemetry.io/blog/2023/k8s-runtime-observability/) 。

[Kubernetes](https://kubernetes.io/) 是一个开源系统，在云原生环境中被广泛使用，用于提供在云中部署和扩展容器化应用程序的方法。它观察日志和指标的能力是[众所周知和有文档记录的](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)，但其对应用程序跟踪的可观测性是新的。

以下是 Kubernetes 生态系统中最近活动的简要概述：

* 第一次讨论始于 2018 年 12 月，即第一个是关于[实现 instrumentation](https://github.com/Monkeyanator/kubernetes/pull/15) 的 PR 。
* KEP（Kubernetes 增强提案）于 2020 年 1 月创建，后来范围限定为 API 服务器（[KEP 647 API Server Tracing](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/647-apiserver-tracing)），而 Kubelet 的新 KEP 于 2021 年 7 月提出（[KEP 2831 Kubelet Tracing](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2831-kubelet-tracing)）。
* [etcd](https://github.com/etcd-io/etcd)（Kubernetes 将其用作内部数据存储）于 2020 年 11 月开始讨论跟踪（[此处](https://github.com/etcd-io/etcd/issues/12460)），并于 2021 年 5 月[合并了第一个版本](https://github.com/etcd-io/etcd/pull/12919)。
* [containerd](https://github.com/containerd/containerd) 和 [CRI-O](https://github.com/cri-o/cri-o) 是两个用于 Kubernetes 的容器运行时接口，于 2021 年开始实现跟踪（[CRI-O 为 2021 年 4 月](https://github.com/cri-o/cri-o/issues/4734)，[containerd 为 2021 年 8 月](https://github.com/containerd/containerd/pull/5731)）。
* API 服务器跟踪在 [v1.22（2021 年 8 月）中作为 alpha](https://github.com/kubernetes/enhancements/blob/master/keps/sig-instrumentation/647-apiserver-tracing/kep.yaml#L26) 版本发布，在 [v1.27（2023 年 4 月）中作为 beta ](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md)版本发布。
* Kubelet 跟踪在 [v1.25（2022 年 8 月）中作为 alpha](https://github.com/kubernetes/enhancements/blob/master/keps/sig-instrumentation/2831-kubelet-tracing/kep.yaml#L29) 版本发布，在 [v1.27（2023 年 4 月）中作为 beta](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md) 版本发布。

在调查 Kubernetes 跟踪的当前状态时，我们发现很少有文章记录如何启用它，比如 Kubernetes 博客上关于 kubelet 可观测性的[文章](https://kubernetes.io/blog/2022/12/01/runtime-observability-opentelemetry/)。我们决定记录我们的发现，并提供分步说明，在本地设置 Kubernetes 并检查跟踪。

您将学习如何将此 instrumentation 与 Kubernetes 一起使用，通过设置本地可观测性环境，然后在启用跟踪的情况下执行 Kubernetes 的本地安装，开始观察其 API（[kube-apiserver](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver)）、节点代理 （[kubelet](https://kubernetes.io/docs/concepts/overview/components/#kubelet)）和容器运行时（[containerd](https://github.com/containerd/containerd)）上的跟踪。

首先，在本地计算机上安装以下工具：

* [Docker](https://www.docker.com/)：允许我们运行容器化环境的容器环境
* [k3d](https://k3d.io/)：一个使用 Docker 运行 k3s（轻量级 Kubernetes 发行版）的包装器
* [kubectl](https://kubernetes.io/docs/reference/kubectl/)：与集群交互的 Kubernetes CLI

## 设置可观测性堆栈以监视跟踪

若要设置可观测性堆栈，你将运行 OpenTelemetry（OTel） Collector ，该工具可从不同的应用接收遥测数据并将其发送到跟踪后端。作为跟踪后端，您将使用 Jaeger ，这是一个开源工具，可收集跟踪并允许您查询它们。

在您的计算机上，创建一个名为 `kubetracing` 的目录并创建一个名为 otel-collector.yaml 的文件，复制以下代码片段的内容，并将其保存在您喜欢的文件夹中。

此文件将配置 OpenTelemetry Collector 以接收 OpenTelemetry 格式的跟踪并将其导出到 Jaeger 。

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
processors:
  probabilistic_sampler:
    hash_seed: 22
    sampling_percentage: 100
  batch:
    timeout: 100ms
exporters:
  logging:
    logLevel: debug
  otlp/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [probabilistic_sampler, batch]
      exporters: [otlp/jaeger, logging]
```

之后，在同一文件夹中，创建一个 [docker-compose.yaml](https://github.com/kubeshop/tracetest/blob/main/examples/tracetesting-kubernetes/kubetracing/docker-compose.yaml) 文件，该文件将有两个容器，一个用于 Jaeger ，另一个用于 OpenTelemetry Collector。

```yaml
services:
  jaeger:
    healthcheck:
      test:
        - CMD
        - wget
        - --spider
        - localhost:16686
      timeout: 3s
      interval: 1s
      retries: 60
    image: jaegertracing/all-in-one:latest
    restart: unless-stopped
    environment:
      - COLLECTOR_OTLP_ENABLED=true
    ports:
      - 16686:16686
  otel-collector:
    command:
      - --config
      - /otel-local-config.yaml
    depends_on:
      jaeger:
        condition: service_started
    image: otel/opentelemetry-collector:0.54.0
    ports:
      - 4317:4317
    volumes:
      - ./otel-collector.yaml:/otel-local-config.yaml
```

现在，通过在 `kubetracing` 文件夹中运行以下命令来启动可观测性环境：

```
docker compose up
```

这将启动 Jaeger 和 OpenTelemetry Collector ，使他们能够从其他应用程序接收跟踪。

## 创建具有运行时可观测性的 Kubernetes 集群

设置可观测性环境后，创建配置文件以在 `kube-apiserver` 、 `kubelet` 和 `containerd` 中启用 OpenTelemetry 跟踪。

在 `kubetracing` 文件夹中，创建一个名为 `config` 的子文件夹，该子文件夹将包含以下两个文件。

首先是 [apiserver-tracing.yaml](https://github.com/kubeshop/tracetest/blob/main/examples/tracetesting-kubernetes/kubetracing/config/apiserver-tracing.yaml) ，它包含 `kube-apiserver` 用于导出包含 Kubernetes API 执行数据跟踪的跟踪配置。在此配置中，将 API 设置为使用 `samplingRatePerMillion` 配置发送 100% 的跟踪。将终端节点设置为 `host.k3d.internal:4317` ，以允许由 `k3d/k3s` 创建的集群调用计算机上的另一个 API。在这种情况下，OpenTelemetry Collector 通过 `docker compose` 部署到了端口 4317 。

```yaml
apiVersion: apiserver.config.k8s.io/v1beta1
kind: TracingConfiguration
endpoint: host.k3d.internal:4317
samplingRatePerMillion: 1000000 # 100%
```

第二个文件是 kubelet-tracing.yaml，它为 `kubelet` 提供了额外的配置。在这里，您将启用功能标志 `KubeletTracing` （ Kubernetes 1.27 中的 beta 版功能，撰写本文时的当前版本）并设置与 `kube-apiserver` 相同的跟踪设置。

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  KubeletTracing: true
tracing:
  endpoint: host.k3d.internal:4317
  samplingRatePerMillion: 1000000 # 100%
```

返回到 `kubetracing` 文件夹，创建最后一个文件 config.toml.tmpl，这是 `k3s` 用于配置 `containerd` 的模板文件。此文件类似于 `k3s` 使用的默认配置，文件末尾还有两个部分，用于配置 `containerd` 以发送跟踪。

```toml
version = 2

[plugins."io.containerd.internal.v1.opt"]
  path = "{{ .NodeConfig.Containerd.Opt }}"
[plugins."io.containerd.grpc.v1.cri"]
  stream_server_address = "127.0.0.1"
  stream_server_port = "10010"
  enable_selinux = {{ .NodeConfig.SELinux }}
  enable_unprivileged_ports = {{ .EnableUnprivileged }}
  enable_unprivileged_icmp = {{ .EnableUnprivileged }}

{{- if .DisableCgroup}}
  disable_cgroup = true
{{end}}
{{- if .IsRunningInUserNS }}
  disable_apparmor = true
  restrict_oom_score_adj = true
{{end}}

{{- if .NodeConfig.AgentConfig.PauseImage }}
  sandbox_image = "{{ .NodeConfig.AgentConfig.PauseImage }}"
{{end}}

{{- if .NodeConfig.AgentConfig.Snapshotter }}
[plugins."io.containerd.grpc.v1.cri".containerd]
  snapshotter = "{{ .NodeConfig.AgentConfig.Snapshotter }}"
  disable_snapshot_annotations = {{ if eq .NodeConfig.AgentConfig.Snapshotter "stargz" }}false{{else}}true{{end}}
{{ if eq .NodeConfig.AgentConfig.Snapshotter "stargz" }}
{{ if .NodeConfig.AgentConfig.ImageServiceSocket }}
[plugins."io.containerd.snapshotter.v1.stargz"]
cri_keychain_image_service_path = "{{ .NodeConfig.AgentConfig.ImageServiceSocket }}"
[plugins."io.containerd.snapshotter.v1.stargz".cri_keychain]
enable_keychain = true
{{end}}
{{ if .PrivateRegistryConfig }}
{{ if .PrivateRegistryConfig.Mirrors }}
[plugins."io.containerd.snapshotter.v1.stargz".registry.mirrors]{{end}}
{{range $k, $v := .PrivateRegistryConfig.Mirrors }}
[plugins."io.containerd.snapshotter.v1.stargz".registry.mirrors."{{$k}}"]
  endpoint = [{{range $i, $j := $v.Endpoints}}{{if $i}}, {{end}}{{printf "%q" .}}{{end}}]
{{if $v.Rewrites}}
  [plugins."io.containerd.snapshotter.v1.stargz".registry.mirrors."{{$k}}".rewrite]
{{range $pattern, $replace := $v.Rewrites}}
    "{{$pattern}}" = "{{$replace}}"
{{end}}
{{end}}
{{end}}
{{range $k, $v := .PrivateRegistryConfig.Configs }}
{{ if $v.Auth }}
[plugins."io.containerd.snapshotter.v1.stargz".registry.configs."{{$k}}".auth]
  {{ if $v.Auth.Username }}username = {{ printf "%q" $v.Auth.Username }}{{end}}
  {{ if $v.Auth.Password }}password = {{ printf "%q" $v.Auth.Password }}{{end}}
  {{ if $v.Auth.Auth }}auth = {{ printf "%q" $v.Auth.Auth }}{{end}}
  {{ if $v.Auth.IdentityToken }}identitytoken = {{ printf "%q" $v.Auth.IdentityToken }}{{end}}
{{end}}
{{ if $v.TLS }}
[plugins."io.containerd.snapshotter.v1.stargz".registry.configs."{{$k}}".tls]
  {{ if $v.TLS.CAFile }}ca_file = "{{ $v.TLS.CAFile }}"{{end}}
  {{ if $v.TLS.CertFile }}cert_file = "{{ $v.TLS.CertFile }}"{{end}}
  {{ if $v.TLS.KeyFile }}key_file = "{{ $v.TLS.KeyFile }}"{{end}}
  {{ if $v.TLS.InsecureSkipVerify }}insecure_skip_verify = true{{end}}
{{end}}
{{end}}
{{end}}
{{end}}
{{end}}

{{- if not .NodeConfig.NoFlannel }}
[plugins."io.containerd.grpc.v1.cri".cni]
  bin_dir = "{{ .NodeConfig.AgentConfig.CNIBinDir }}"
  conf_dir = "{{ .NodeConfig.AgentConfig.CNIConfDir }}"
{{end}}

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  runtime_type = "io.containerd.runc.v2"

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
  SystemdCgroup = {{ .SystemdCgroup }}

{{ if .PrivateRegistryConfig }}
{{ if .PrivateRegistryConfig.Mirrors }}
[plugins."io.containerd.grpc.v1.cri".registry.mirrors]{{end}}
{{range $k, $v := .PrivateRegistryConfig.Mirrors }}
[plugins."io.containerd.grpc.v1.cri".registry.mirrors."{{$k}}"]
  endpoint = [{{range $i, $j := $v.Endpoints}}{{if $i}}, {{end}}{{printf "%q" .}}{{end}}]
{{if $v.Rewrites}}
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."{{$k}}".rewrite]
{{range $pattern, $replace := $v.Rewrites}}
    "{{$pattern}}" = "{{$replace}}"
{{end}}
{{end}}
{{end}}

{{range $k, $v := .PrivateRegistryConfig.Configs }}
{{ if $v.Auth }}
[plugins."io.containerd.grpc.v1.cri".registry.configs."{{$k}}".auth]
  {{ if $v.Auth.Username }}username = {{ printf "%q" $v.Auth.Username }}{{end}}
  {{ if $v.Auth.Password }}password = {{ printf "%q" $v.Auth.Password }}{{end}}
  {{ if $v.Auth.Auth }}auth = {{ printf "%q" $v.Auth.Auth }}{{end}}
  {{ if $v.Auth.IdentityToken }}identitytoken = {{ printf "%q" $v.Auth.IdentityToken }}{{end}}
{{end}}
{{ if $v.TLS }}
[plugins."io.containerd.grpc.v1.cri".registry.configs."{{$k}}".tls]
  {{ if $v.TLS.CAFile }}ca_file = "{{ $v.TLS.CAFile }}"{{end}}
  {{ if $v.TLS.CertFile }}cert_file = "{{ $v.TLS.CertFile }}"{{end}}
  {{ if $v.TLS.KeyFile }}key_file = "{{ $v.TLS.KeyFile }}"{{end}}
  {{ if $v.TLS.InsecureSkipVerify }}insecure_skip_verify = true{{end}}
{{end}}
{{end}}
{{end}}

{{range $k, $v := .ExtraRuntimes}}
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes."{{$k}}"]
  runtime_type = "{{$v.RuntimeType}}"
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes."{{$k}}".options]
  BinaryName = "{{$v.BinaryName}}"
{{end}}

[plugins."io.containerd.tracing.processor.v1.otlp"]
  endpoint = "host.k3d.internal:4317"
  protocol = "grpc"
  insecure = true

[plugins."io.containerd.internal.v1.tracing"]
  sampling_ratio = 1.0
  service_name = "containerd"
```

创建这些文件后，在 `kubetracing` 文件夹中打开一个终端并运行 `k3d` 以创建集群。在运行此命令之前，请替换 `kubetracing` 文件夹的整个路径的 `[CURRENT_PATH]` 占位符。您可以通过在该文件夹的终端中运行 `echo $PWD` 命令来检索它。

```shell
k3d cluster create tracingcluster \
  --image=rancher/k3s:v1.27.1-k3s1 \
  --volume '[CURRENT_PATH]/config.toml.tmpl:/var/lib/rancher/k3s/agent/etc/containerd/config.toml.tmpl@server:*' \
  --volume '[CURRENT_PATH]/config:/etc/kube-tracing@server:*' \
  --k3s-arg '--kube-apiserver-arg=tracing-config-file=/etc/kube-tracing/apiserver-tracing.yaml@server:*' \
  --k3s-arg '--kube-apiserver-arg=feature-gates=APIServerTracing=true@server:*' \
  --k3s-arg '--kubelet-arg=config=/etc/kube-tracing/kubelet-tracing.yaml@server:*'
```

此命令将创建一个版本 `v1.17.1` 的 Kubernetes 集群，并在计算机上的三个 docker 容器中进行设置。如果现在运行命令 `kubectl cluster-info` ，您将看到以下输出：

```shell
Kubernetes control plane is running at https://0.0.0.0:60503
CoreDNS is running at https://0.0.0.0:60503/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://0.0.0.0:60503/api/v1/namespaces/kube-system/services/https:metrics-server:https/proxy
```

回到可观测性环境的日志，你应该看到 OpenTelemetry Collector 中发布了一些内部 Kubernetes 操作，如下所示：

```
Span #90
    Trace ID       : 03a7bf9008d54f02bcd4f14aa5438202
    Parent ID      :
    ID             : d7a10873192f7066
    Name           : KubernetesAPI
    Kind           : SPAN_KIND_SERVER
    Start time     : 2023-05-18 01:51:44.954563708 +0000 UTC
    End time       : 2023-05-18 01:51:44.957555323 +0000 UTC
    Status code    : STATUS_CODE_UNSET
    Status message :
Attributes:
     -> net.transport: STRING(ip_tcp)
     -> net.peer.ip: STRING(127.0.0.1)
     -> net.peer.port: INT(54678)
     -> net.host.ip: STRING(127.0.0.1)
     -> net.host.port: INT(6443)
     -> http.target: STRING(/api/v1/namespaces/kube-system/pods/helm-install-traefik-crd-8w4wd)
     -> http.server_name: STRING(KubernetesAPI)
     -> http.user_agent: STRING(k3s/v1.27.1+k3s1 (linux/amd64) kubernetes/bc5b42c)
     -> http.scheme: STRING(https)
     -> http.host: STRING(127.0.0.1:6443)
     -> http.flavor: STRING(2)
     -> http.method: STRING(GET)
     -> http.wrote_bytes: INT(4724)
     -> http.status_code: INT(200)
```

## 测试群集运行时

通过设置可观测性和 Kubernetes 集群，您现在可以针对 Kubernetes 触发命令，并在 Jaeger 中查看这些操作的痕迹。

打开浏览器，然后导航到位于 http://localhost:16686/search 的 Jaeger UI。您将看到 `apiserver` 、 `containerd` 和 `kubelet` 服务正在发布跟踪：

![Jaeger screen with services dropdown open showing apiserver, containerd and kubelet services as options](https://opentelemetry.io/blog/2023/k8s-runtime-observability/k8s-services-reported-on-jaeger.png)

选择 `apiserver` 并单击“查找跟踪”。在这里，您可以看到来自 Kubernetes 控制平面的跟踪：

![Jaeger screen showing a list of spans found for apiserver](https://opentelemetry.io/blog/2023/k8s-runtime-observability/spans-found-for-apiserver.png)

让我们用 `kubectl` 对 Kubernetes 运行一个示例命令，就像运行 echo 一样：

```shell
$ kubectl run -it --rm --restart=Never --image=alpine echo-command -- echo hi

# Output
# If you don't see a command prompt, try pressing enter.
# warning: couldn't attach to pod/echo-command, falling back to streaming logs: unable to upgrade connection: container echo-command not found in pod echo-command_default
# Hi
# pod "echo-command" deleted
```

现在，再次打开 Jaeger，选择 `kubelet` 服务，操作 `syncPod` ，并添加标签 `k8s.pod=default/echo-command` ，您应该能够看到与此 pod 相关的 span ：

![Jaeger screen showing a list of spans found for the syncPod operation on kubelet service](https://opentelemetry.io/blog/2023/k8s-runtime-observability/syncpod-operations-on-kubelet.png)

展开一条跟踪，您将看到创建此 Pod 的操作：

![Jaeger screen showing a single syncPod expanded](https://opentelemetry.io/blog/2023/k8s-runtime-observability/single-syncpod-expanded.png)

## 总结

即使在 beta 版中，[kubelet](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2831-kubelet-tracing) 和 [apiserver](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/647-apiserver-tracing) 的跟踪也可以帮助开发人员了解 Kubernetes 中发生的事情并开始调试问题。

这对于创建自定义任务的开发人员很有帮助，例如更新内部资源以向 Kubernetes 添加更多功能的 [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 。

作为一个专注于在可观测性领域构建开源工具的团队，帮助整个 OpenTelemetry 社区的机会对我们来说很重要。这就是为什么我们正在研究寻找从核心 Kubernetes 引擎收集跟踪的新方法。由于 Kubernetes 公开了当前的可观测性级别，我们希望发布我们的发现，以帮助其他有兴趣了解 Kubernetes 引擎中分布式跟踪当前状态的人。 Daniel Dias 和 Sebastian Choren 正在开发 Tracetest ，这是一个开源工具，允许您使用 OpenTelemetry 开发和测试分布式系统。它适用于任何 OTel 兼容系统，并允许创建基于跟踪的测试。在 [https://github.com/kubeshop/tracetest](https://github.com/kubeshop/tracetest) 查看。

本文中使用的[示例源代码](https://github.com/kubeshop/tracetest/tree/main/examples/tracetesting-kubernetes/kubetracing)和[设置说明](https://github.com/kubeshop/tracetest/blob/main/examples/tracetesting-kubernetes/setup-k8s-with-k3d.md)可从 Tracetest 仓库获得。

## 参考

* [Kubernetes 系统组件的跟踪](https://kubernetes.io/docs/concepts/cluster-administration/system-traces/)
* [在 ContainerD 上跟踪](https://github.com/containerd/containerd/blob/main/docs/tracing.md)
* [Kubernetes：监控资源的工具](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
* [开始使用 OTel Collector](https://opentelemetry.io/docs/collector/getting-started/)
* [通过 OpenTelemetry 提高 Kubernetes 容器运行时的可观测性](https://kubernetes.io/blog/2022/12/01/runtime-observability-opentelemetry/)