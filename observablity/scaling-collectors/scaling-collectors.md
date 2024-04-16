
<!--
title: 使用 Ansible 大规模管理 OpenTelemetry 收集器
cover: https://opentelemetry.io/img/social/logo-wordmark-001.png
-->

您可以通过 [Ansible](https://www.ansible.com/) 在多个 Linux 主机上扩展 [OpenTelemetry 收集器](/docs/collector/deployment/) 的部署，使其在您的可观测性架构中既作为 [网关](/docs/collector/deployment/gateway/) 又作为 [代理](/docs/collector/deployment/agent/)。在此双重身份中使用 OpenTelemetry 收集器能够将指标、跟踪和日志可靠地收集并转发到分析和可视化平台。

> 译自 [Manage OpenTelemetry Collectors at scale with Ansible](https://opentelemetry.io/blog/2024/scaling-collectors/)，作者 OpenTelemetry Authors; Docs CC BY。

我们概述了一种使用 Ansible 在整个基础架构中部署和管理 OpenTelemetry 收集器可扩展实例的策略。在以下示例中，我们将使用 [Grafana](https://grafana.com/) 作为指标的目标后端。

## 先决条件

在开始之前，请确保您满足以下要求：

- 在您的基本系统上安装了 Ansible
- SSH 访问两个或更多 Linux 主机
- 配置了 Prometheus 以收集您的指标

## 安装 Grafana Ansible 集合

[OpenTelemetry 收集器角色](https://github.com/grafana/grafana-ansible-collection/tree/main/roles/opentelemetry_collector) 通过 [Grafana Ansible 集合](https://docs.ansible.com/ansible/latest/collections/grafana/grafana/) 提供，版本为 4.0。

要安装 Grafana Ansible 集合，请运行此命令：

```
ansible-galaxy collection install grafana.grafana
```

## 创建 Ansible 清单文件

接下来，收集与您的 Linux 主机关联的 IP 地址和 URL，并创建一个清单文件。

1. 创建 Ansible 清单文件。

Ansible 清单（位于名为 inventory 的文件中）将每个主机 IP 列在单独的行上，如下所示（显示 8 个主机）：

```
10.0.0.1 # hostname = ubuntu-01
10.0.0.2 # hostname = ubuntu-02
10.0.0.3 # hostname = centos-01
10.0.0.4 # hostname = centos-02
10.0.0.5 # hostname = debian-01
10.0.0.6 # hostname = debian-02
10.0.0.7 # hostname = fedora-01
10.0.0.8 # hostname = fedora-02
```

2. 在与 inventory 相同的目录中创建一个 ansible.cfg 文件，并使用以下值：

```
[defaults]
inventory = inventory # 清单文件的路径
private_key_file = ~/.ssh/id_rsa # 私有 SSH 密钥的路径
remote_user=root
```

## 使用 OpenTelemetry Collector Ansible 角色

接下来，定义一个 Ansible playbook 来在您的主机上应用您选择或创建的 OpenTelemetry Collector 角色。

在与 ansible.cfg 和 inventory 文件相同的目录中创建一个名为 deploy-opentelemetry.yml 的文件：

```yaml
- name: Install OpenTelemetry Collector
  hosts: all
  become: true

  tasks:
    - name: Install OpenTelemetry Collector
      ansible.builtin.include_role:
        name: opentelemetry_collectorr
      vars:
        otel_collector_receivers:
          hostmetrics:
            collection_interval: 60s
            scrapers:
              cpu: {}
              disk: {}
              load: {}
              filesystem: {}
              memory: {}
              network: {}
              paging: {}
              process:
                mute_process_name_error: true
                mute_process_exe_error: true
                mute_process_io_error: true
              processes: {}

        otel_collector_processors:
          batch:
          resourcedetection:
            detectors: [env, system]
            timeout: 2s
            system:
              hostname_sources: [os]
          transform/add_resource_attributes_as_metric_attributes:
            error_mode: ignore
            metric_statements:
              - context: datapoint
                statements:
                  - set(attributes["deployment.environment"],
                    resource.attributes["deployment.environment"])
                  - set(attributes["service.version"],
                    resource.attributes["service.version"])

        otel_collector_exporters:
          prometheusremotewrite:
            endpoint: https://<prometheus-url>/api/prom/push
            headers:
              Authorization: 'Basic <base64-encoded-username:password>'

        otel_collector_service:
          pipelines:
            metrics:
              receivers: [hostmetrics]
              processors:
                [
                  resourcedetection,
                  transform/add_resource_attributes_as_metric_attributes,
                  batch,
                ]
              exporters: [prometheusremotewrite]
```

> 注意：调整配置以匹配您打算收集的特定遥测以及您计划将其转发到的位置。此配置片段是一个基本示例，旨在收集转发到 Prometheus 的主机指标。

之前的配置将配置 OpenTelemetry Collector 以从 Linux 主机收集指标。

## 运行 Ansible Playbook

通过运行以下命令在您的主机上部署 OpenTelemetry Collector：

```
ansible-playbook deploy-opentelemetry.yml
```

## 在后端检查您的指标

在您的 OpenTelemetry 收集器开始向 Prometheus 发送指标后，请按照以下步骤在 Grafana 中对其进行可视化：

### 设置 Grafana

1. **安装 Docker**：确保您的系统上安装了 Docker。

2. **运行 Grafana Docker 容器**：使用以下命令启动 Grafana 服务器，该命令将获取最新的 Grafana 映像：

```
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

3. **访问 Grafana**：在您的网络浏览器中打开 [http://localhost:3000](http://localhost:3000)。默认登录用户名和密码都是 admin。

4. **更改密码**：在首次登录时提示时 - 选择一个安全的密码！

有关其他安装方法和更详细的说明，请参阅 [Grafana 文档](https://grafana.com/docs/grafana/latest/installation/)。

### 添加 Prometheus 作为数据源

- 在 Grafana 中，导航至 **Connections** > **Data Sources**。
- 单击 **Add data source** 并选择 **Prometheus**。
- 在设置中，输入您的 Prometheus URL，例如，`http://<your_prometheus_host>`，以及任何其他必需的详细信息。
- 选择 **Save & Test**。

### 探索您的指标

1. 转到 **Explore** 页面。

2. 在查询编辑器中，选择您的数据源并输入以下查询：

```
100 - (avg by (cpu) (irate(system_cpu_time{state="idle"}[5m])) * 100)
```

此查询计算过去 5 分钟内每个 CPU 核心未处于“空闲”状态的 CPU 时间的平均百分比。

3. 探索其他指标并创建仪表盘以深入了解您系统的性能。

这篇博文说明了如何借助 Ansible 配置和部署多个 OpenTelemetry 收集器跨各种 Linux 主机，以及在 Grafana 中可视化收集到的遥测数据。如果您觉得这有用，GitHub 存储库用于 [OpenTelemetry Collector 角色](https://github.com/grafana/grafana-ansible-collection/tree/main/roles/opentelemetry_collector) 以获取详细的配置选项。如果您有任何问题，您可以使用我的 GitHub 个人资料中的联系方式与我联系 [@ishanjainn](https://github.com/ishanjainn)。