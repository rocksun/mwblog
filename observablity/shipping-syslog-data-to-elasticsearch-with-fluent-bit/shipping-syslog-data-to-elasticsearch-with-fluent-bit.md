<!--
title: Fluent Bit：Syslog 数据高效入驻 Elasticsearch
cover: https://cdn.thenewstack.io/media/2025/11/45038acc-birds.jpg
summary: 本指南展示如何使用Fluent Bit作为中央Syslog服务器，通过UDP收集来自Alpine容器的日志，并将其转发到Elasticsearch进行存储和分析。
-->

本指南展示如何使用Fluent Bit作为中央Syslog服务器，通过UDP收集来自Alpine容器的日志，并将其转发到Elasticsearch进行存储和分析。

> 译自：[Shipping Syslog Data to Elasticsearch With Fluent Bit](https://thenewstack.io/shipping-syslog-data-to-elasticsearch-with-fluent-bit/)
> 
> 作者：Sharad Regoti

[Fluent Bit](https://docs.fluentbit.io/manual) 是一个被广泛使用的开源数据收集代理、处理器和转发器，它使你能够从各种来源收集日志、指标和追踪，对其进行过滤和转换，然后将其转发到多个目的地。

在现代基础设施中，尽管结构化 JSON 日志记录兴起，但 [Syslog](https://en.wikipedia.org/wiki/Syslog) 仍然是网络设备、传统应用程序和 [Linux发行版](https://thenewstack.io/how-to-manage-linux-log-services/) 的标准。然而，在每台服务器上本地分析 Syslog 文件并不实际。

在本指南中，我们将把 Fluent Bit 设置为中央 Syslog 服务器，它通过 [UDP（用户数据报协议）](https://thenewstack.io/choosing-the-right-transport-protocol-tcp-vs-udp-vs-quic/) 接收日志，并将其直接传输到 Elasticsearch 进行分析。

[![](https://cdn.thenewstack.io/media/2025/11/c94f2c7e-image2.png)](https://cdn.thenewstack.io/media/2025/11/c94f2c7e-image2.png)

## **先决条件**

*   **Docker和Docker Compose：** 已安装在你的系统上。
*   **Elasticsearch**：我们将把日志发送到一个 Elasticsearch 实例。要跟着操作，你应该有一个正在运行的实例。你可以参考这个[指南](https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html)来在本地运行它。
*   **熟悉 Fluent Bit 概念：** 例如输入、输出和缓冲区。如果你不熟悉这些概念，请参考[官方文档](https://docs.fluentbit.io/manual/concepts/data-pipeline)。

## 什么是 Syslog？

Syslog 是一种消息日志记录标准。它允许生成消息的软件、存储消息的系统以及报告和分析消息的软件相互分离。

Syslog 消息通常通过 UDP 端口 514（在非 root 环境中为 5140）传输。由于它是一种“即发即弃”协议，因此速度快且轻量，使其成为从路由器、防火墙和轻量级 Linux 容器进行大容量日志记录的理想选择。然而，原始 Syslog 文本可能难以查询。通过使用 Fluent Bit，我们可以摄取这些消息，对其进行结构化，并将其存储在像 Elasticsearch 这样的搜索引擎中。

要了解更多关于 Syslog 的信息，你可以参考 [Syslog维基百科页面](https://en.wikipedia.org/wiki/Syslog)。

## 我们的用例

[![](https://cdn.thenewstack.io/media/2025/11/c96a49ed-image1.png)](https://cdn.thenewstack.io/media/2025/11/c96a49ed-image1.png)

在这个演示中，我们将使用 Docker Compose 创建一个模拟环境：

*   **Fluent Bit**：配置为监听 UDP 端口 5140 的 Syslog 流量。
*   **Alpine 日志记录器**：两个独立的 Alpine Linux 容器，将充当“网络设备”。它们将使用 `logger` 命令每 10 秒生成一次日志消息，并将其发送到我们的 Fluent Bit 容器。
*   **Elasticsearch**：日志将存储和索引的目标。

## 说明

**1. 创建项目目录**

首先，创建一个目录来存放你的配置和 Docker Compose 文件。

```
mkdir fluent-bit-syslog-demo
cd fluent-bit-syslog-demo
```

**2. 创建 Fluent Bit 配置**

创建一个名为 `fluent-bit/config` 的目录，并在其中创建一个名为 `fluent-bit.yaml` 的文件，内容如下：

```
service:
  flush: 1
  log_level: info
  parsers_file: parsers.conf

pipeline:

  inputs:
    - name: syslog
      mode: udp
      listen: 0.0.0.0
      port: 5140

  outputs:
    - name: es
      match: '*'
      # CHANGE THESE TO MATCH YOUR ELASTICSEARCH SETUP
      host: 192.168.1.5
      port: 9200
      index: syslog-data
      http_user: elastic
      http_passwd: rslglTS4
      suppress_type_name: 'On'
```

该文件告诉 Fluent Bit 监听 Syslog 消息并将它们转发到你的 Elasticsearch 实例。

**注意：** 更新输出部分中的 `host`、`http_user` 和 `http_passwd` 以匹配你实际的 Elasticsearch 凭据。

**3. 创建 Docker Compose 文件**

创建一个名为 `docker-compose.yaml` 的文件，内容如下：

```
services:
  fluent-bit:
    image: 'fluent/fluent-bit:latest'
    container_name: fluent-bit
    ports:
      - '6000:5140/udp'
      - '24224:24224'
    volumes:
      - './fluent-bit/config/fluent-bit.yaml:/fluent-bit/etc/fluent-bit.yaml'
    networks:
      - syslog-test
    restart: unless-stopped
    command: '-c /fluent-bit/etc/fluent-bit.yaml'
  alpine-logger-1:
    image: 'alpine:latest'
    container_name: alpine-logger-1
    depends_on:
      - fluent-bit
    networks:
      - syslog-test
    command: |
      /bin/sh -c " apk add --no-cache util-linux && while true; do
        logger -n fluent-bit -P 5140 -t alpine-test \"This is a test message from Alpine Logger 1 at \$(date)\"
        sleep 10
      done "
  alpine-logger-2:
    image: 'alpine:latest'
    container_name: alpine-logger-2
    depends_on:
      - fluent-bit
    networks:
      - syslog-test
    command: |
      /bin/sh -c " apk add --no-cache util-linux && while true; do
        logger -n fluent-bit -P 5140 -t alpine-test \"This is a test message from Alpine Logger 2 at \$(date)\"
        sleep 10
      done "
networks:
  syslog-test:
    driver: bridge
```

该文件定义了我们的 Fluent Bit 服务以及两个生成流量的 Alpine 容器。Alpine 容器使用 [logger](https://wiki.alpinelinux.org/wiki/Syslog) CLI 以 Syslog 格式创建日志。

**4. 运行容器**

使用 Docker Compose 启动环境：

```
docker compose up -d
```

一旦容器运行起来，Alpine 实例将立即开始向 Fluent Bit 发送日志，Fluent Bit 会将它们转发到 Elasticsearch。

**5. 在 Elasticsearch 中验证日志**

**注意：** 我们只在 Elasticsearch 中创建了模式为 `syslog-data*` 的索引。要在 Kibana 中查看这些日志，你需要创建一个[数据视图](https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views)。

[![](https://cdn.thenewstack.io/media/2025/11/998d67e9-image3.png)](https://cdn.thenewstack.io/media/2025/11/998d67e9-image3.png)

**6. 清理**

```
docker compose down -v
```

## 结论

在本指南中，我们成功地使用 Fluent Bit 设置了一个轻量级 Syslog 收集器。我们模拟了一个真实世界环境，其中多个服务器通过 UDP 将日志发送到中央点。Fluent Bit 收集了这些日志并将其传输到 Elasticsearch 进行存储和分析。