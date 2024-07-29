# 第四部分：端到端 Java DevOps 自动化项目

**先决条件**: [第三部分：端到端 Java DevOps 自动化项目](/@navin5556/part-3-end-to-end-java-devops-automation-project-63a9cf83935f)

# 使用 Prometheus、Grafana 和 Blackbox Exporter 设置监控

在本教程中，我们将使用 Prometheus、Grafana 和 Blackbox Exporter 设置一个监控系统，以有效地监控您的应用程序和服务。我们还将介绍如何使用 Node Exporter 监控 Jenkins 实例和系统指标。

## 第 1 部分：设置 Prometheus

**1. 安装 Prometheus**

首先，更新您的软件包列表并下载 Prometheus：

```bash
sudo apt update -y
wget https://github.com/prometheus/prometheus/releases/download/v2.53.1/prometheus-2.53.1.linux-amd64.tar.gz
tar -xvf prometheus-2.53.1.linux-amd64.tar.gz
rm -rf prometheus-2.53.1.linux-amd64.tar.gz
cd prometheus-2.53.1.linux-amd64/
./prometheus &
```

Prometheus 将在端口 `9090` 上运行。您可以通过 `http://<您的公共 IP>:9090/` 访问 Prometheus Web 界面。

## 第 2 部分：设置 Grafana

**1. 安装 Grafana**

接下来，安装 Grafana：

```bash
sudo apt-get install -y adduser libfontconfig1 musl
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_11.1.0_amd64.deb
sudo dpkg -i grafana-enterprise_11.1.0_amd64.deb
sudo /bin/systemctl start grafana-server
```

Grafana 将在端口 `3000` 上运行。通过 `http://<您的公共 IP>:3000/login` 访问它，并使用默认凭据（用户名：`admin`，密码：`admin`）登录。登录后更改默认密码。

## 第 3 部分：设置 Blackbox Exporter

**1. 安装 Blackbox Exporter**

下载并安装 Blackbox Exporter 以监控您的网站：

```bash
wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.25.0/blackbox_exporter-0.25.0.linux-amd64.tar.gz
tar -xvf blackbox_exporter-0.25.0.linux-amd64.tar.gz
rm -rf blackbox_exporter-0.25.0.linux-amd64.tar.gz
cd blackbox_exporter-0.25.0.linux-amd64/
./blackbox_exporter &
```

Blackbox Exporter 在端口 `9115` 上运行。通过 `http://<您的公共 IP>:9115/` 访问它。

**2. 为 Blackbox Exporter 配置 Prometheus**

编辑您的 `prometheus.yml` 文件以包含 Blackbox Exporter 配置：

```yaml
scrape_configs:
- job_name: 'blackbox'
  metrics_path: /probe
  params:
    module: [http_2xx]
  static_configs:
  - targets:
    - http://prometheus.io
    - http://3.111.50.86:32106/ # 此应用程序 boardgame 的 Kubernetes 服务的从节点 IP 和端口
  relabel_configs:
  - source_labels: [__address__]
    target_label: __param_target
  - source_labels: [__param_target]
    target_label: instance
  - target_label: __address__
    replacement: 13.200.8.32:9115 # Blackbox Exporter 的真实主机名：端口
```

重新启动 Prometheus：

```bash
pkill prometheus
./prometheus &
```

我们可以在 **Prometheus** -> **状态** -> **目标** 中验证这一点。

**3. 在 Grafana 中添加 Prometheus 作为数据源**

- 登录 Grafana。
- 导航到连接 > 数据源 > 添加数据源。
- 选择 Prometheus 并输入 `http://<prometheus-ip>:9090/` 作为 URL。
- 点击保存并测试。

**4. 导入 Blackbox Grafana 仪表盘**

- 搜索“blackbox grafana dashboard”。
- 复制仪表盘 ID 并将其导入 Grafana。
- 现在您可以在 Grafana 上看到图表。

## 第 4 部分：监控 Jenkins 和系统指标

在 Jenkins 中安装 **Prometheus Metrics 插件**。

**1. 安装 Node Exporter（用于系统级指标）**

在您的 Jenkins 服务器上下载并安装 Node Exporter：

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz
tar -xvf node_exporter-1.8.2.linux-amd64.tar.gz
rm -rf node_exporter-1.8.2.linux-amd64.tar.gz
cd node_exporter-1.8.2.linux-amd64/
./node_exporter &
```

Node Exporter 在端口 `9100` 上运行。通过 `http://<您的公共 IP>:9100/` 访问它。

**2. 为 Node Exporter 和 Jenkins 配置 Prometheus**

编辑您的 `prometheus.yml` 文件以包含 Node Exporter 和 Jenkins 的配置：

```yaml
scrape_configs:
- job_name: 'node_exporter'
  static_configs:
  - targets: ['<jenkins-ip>:9100']
- job_name: 'jenkins'
  metrics_path: '/prometheus'
  static_configs:
  - targets: ['<jenkins-ip>:8080']
```

重新启动 Prometheus：

```bash
pkill prometheus
./prometheus &
```

**3. 在 Grafana 中添加 Node Exporter 数据源并导入仪表盘**

- 在 Grafana 中添加 Node Exporter 作为数据源。
- 搜索“node exporter grafana dashboard”。
- 复制仪表盘 ID 并将其导入 Grafana。

最终结果：

# 结论

通过此设置，您现在拥有一个使用 Prometheus、Grafana 和 Blackbox Exporter 的强大监控系统。您可以有效地监控您的应用程序、网站和系统指标。祝您监控愉快！

**下载链接：**