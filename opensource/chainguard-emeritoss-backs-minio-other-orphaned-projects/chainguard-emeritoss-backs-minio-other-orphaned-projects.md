<!--
title: Chainguard EmeritOSS出手，支持MinIO及其他“孤儿”开源项目
cover: https://cdn.thenewstack.io/media/2026/01/aaa1f27d-jose-m-alarcon-ywz9m3mxeu0-unsplash.jpg
summary: Chainguard推出EmeritOSS项目，为MinIO等十余个被“遗弃”但广泛使用的开源项目提供持续维护和安全支持，解决开源软件无人管的困境。
-->

Chainguard推出EmeritOSS项目，为MinIO等十余个被“遗弃”但广泛使用的开源项目提供持续维护和安全支持，解决开源软件无人管的困境。

> 译自：[Chainguard EmeritOSS backs MinIO, other orphaned projects](https://thenewstack.io/chainguard-emeritoss-backs-minio-other-orphaned-projects/)
> 
> 作者：Steven J. Vaughan-Nichols

开源软件存在一个问题。许多被广泛使用但支持不足甚至被废弃的开源程序，如今却无人掌舵。

为解决这一问题，[Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 近期推出了 [Chainguard EmeritOSS](https://c67dcd9a.streak-link.com/Csf3OJpyshg0bW_ibgbecPa5/https%3A%2F%2Fgithub.com%2Fchainguard-forks%2F)，一个旨在支持这些至关重要却“无人爱护”的项目的计划。在支持了 [三个不同的程序](https://thenewstack.io/chainguard-takes-over-maintenance-of-aging-oss-projects/) 后，这家基础设施安全公司又将拯救另外10个项目。

其中最重要的可能就是 [MinIO](https://github.com/minio/minio)，一个轻量级、高性能的 [开源对象存储系统](https://thenewstack.io/add-object-storage-to-rocky-linux-with-minio/)，它完全兼容Amazon S3 API。

去年12月，维护者 [将该软件](https://medium.com/@heinancabouly/minios-maintenance-mode-a-wake-up-call-for-the-cncf-ecosystem-38add3bc6c4f) 置于 [仅维护模式](https://github.com/minio/minio)，这让仍在社区版的用户社区感到非常不满。该项目的同名公司此前负责维护，现在推荐其 [免费版本](https://www.min.io/download)（尽管并非开源）或其Alstor平台的商业版本作为替代。

Chainguard 加大了支持力度，甚至提供了 [安全的MinIO镜像](https://www.chainguard.dev/unchained/secure-and-free-minio-chainguard-containers)。

## 其他新支持的程序

其他 [新支持的“僵尸”程序](https://www.chainguard.dev/unchained/fork-yeah-were-adding-ten-new-open-source-projects-to-emeritoss) 包括：

[Prometheus PushProx](https://github.com/prometheus-community/PushProx)，一个代理和客户端解决方案，使 [Prometheus](https://prometheus.io/) 即使在NAT或防火墙后面也能抓取目标。虽然PushProx仍然在幕后“拉取”数据，但它运行一个隧道代理，将数据请求“推送”以检索数据。

[Cassandra Exporter](https://github.com/criteo/cassandra_exporter) 是一个独立的指标导出器，适用于 [Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/)。这个Java虚拟机 (JVM) 程序在不给Cassandra NoSQL DBMS造成过重负担的情况下，检索Cassandra的性能和使用指标。

[Prometheus exporter](https://github.com/prometheus-community/json_exporter) 抓取JavaScript Object Notation (JSON) API并使用 [JSONPath](https://jsonpath.com/) 配置将其转换为指标。有了这个有用的工具，你几乎可以从任何理解JSON的API中拉取数据。

[Prometheus RabbitMQ导出器](https://github.com/kbudde/rabbitmq_exporter) 通过Management API公开代理、队列、连接和交换状态。该导出器与传统 [RabbitMQ 3.x](https://www.rabbitmq.com/release-information) 版本兼容。它为监控RabbitMQ基础设施提供了广泛的过滤和配置功能。它常用于消息队列监控和警报。

[适用于Python RQ (Redis Queue) 的Prometheus导出器](https://github.com/mdawar/rq-exporter) 暴露作业队列指标，包括处理时间和计数。这使得管理人员可以通过HTTP端点（通常是“/metrics”）更有效地监控后台工作负载，然后Prometheus可以从该端点抓取数据。

当我还是一个年轻的 [Unix开发者](https://thenewstack.io/learning-linux-start-here/) 时，我只使用grep、awk和sed，但Logstash [过滤器范围插件](https://github.com/logstash-plugins/logstash-filter-range) 允许你定义数字或字符串范围，并检查给定字段的值是否落在这些范围内，而无需手动编写shell脚本。有了这些数据，你可以标记事件、删除不需要的数据、应用条件处理，你懂的。

[PgCat](https://github.com/postgresml/pgcat) 是一个PostgreSQL连接池和代理，支持分片、负载均衡、故障转移和镜像。它可以将客户端连接多路复用到PostgreSQL DBMSs，以减少连接开销和网络延迟。

[OpenStack](https://www.openstack.org/) [Velero插件](https://github.com/Lirt/velero-plugin-for-openstack) 为 [Velero](https://velero.io/) 添加了针对OpenStack Cinder卷、Swift容器和Manila共享的备份和恢复操作。它为OpenStack环境提供了卷快照和对象存储功能。没有它，Velero用于备份和恢复运行在OpenStack上的Kubernetes集群。

最后，[k8s-node-collector](https://github.com/aquasecurity/k8s-node-collector) 是一个小型实用工具，提供Kubernetes节点信息收集器，用于收集文件系统、进程和系统数据。它生成结构化的JSON输出，用于审计、合规性检查或自定义集成。

## 不再提供支持

当然，所有这些程序共同的特点是它们的创建者不再支持它们。正如Chainguard的CSO兼联合创始人 Kim Lewandowski 在宣布这一消息的博客文章中所写：“当一个项目不再需要持续维护或维护者需要退出时，Chainguard EmeritOSS就会介入。”

这是一项非常有用的服务。有太多任务关键型的 [开源程序](https://thenewstack.io/open-source/ "开源程序") 不再有归宿，而Chainguard正在为它们提供一个。正如 Lewandowski 所说：“EmeritOSS 为那些已经功成名就的项目而存在。它们已经发布、扩展并支持了实际系统，虽然它们的维护者可能准备退居二线，但软件本身仍然生命力十足。”

## 移交无人支持的项目

确实如此。正如Chainguard联合创始人兼CEO Dan Lorenc 在早期的一篇The New Stack专栏文章中解释道：“我们需要一种方式，让开源维护者能够优雅地 [移交‘已完成’项目](https://chainguard.dev/unchained/introducing-chainguard-emeritoss)，即使这些项目不再有重要的功能路线图。我们需要为他们提供一个地方：”

那个地方就是EmeritOSS。

你需要这些程序吗？ [Chainguard分叉的、专注于稳定性的EmeritOSS版本](https://github.com/chainguard-forks/) 将继续以源代码的形式在 [GitHub](https://github.com/chainguard-forks/) 上免费提供。不想费心处理代码？Chainguard还通过其商业发行版提供安全、持续维护的容器镜像和 [APK包](https://edu.chainguard.dev/open-source/wolfi/apk-package-manager/)。你是否依赖其他开源程序并需要帮助？你可以 [提交考虑](https://get.chainguard.dev/emeritoss-submission?__hstc=1638499.72def09cf1055c99e814f503d1822919.1768770970725.1768770970725.1768776191368.2&__hssc=1638499.1.1768776191368&__hsfp=4354069f6051f96c2c74e52210cf4c11&_gl=1*o0up4c*_gcl_au*OTQ2MzcwNDk5LjE3Njg3NzA5NzA.)，Chainguard可能会通过EmeritOSS支持它。