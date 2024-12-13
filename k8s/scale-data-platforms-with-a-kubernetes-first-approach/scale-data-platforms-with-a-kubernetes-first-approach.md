
<!--
title: 基于 Kubernetes 的首要方法扩展数据平台
cover: https://cdn.thenewstack.io/media/2024/12/a169aad9-kubernetes.png
-->

Kubernetes 运算符——管理有状态应用程序的特定于应用程序的控制器——可以使数据库管理成为一种可行甚至更优的选择。

> 译自 [Scale Data Platforms With a Kubernetes-First Approach](https://thenewstack.io/scale-data-platforms-with-a-kubernetes-first-approach/)，作者 Matt Sarrel。

数据平台是现代数据驱动型组织的核心，它能够大规模地集成、管理和分析数据。无论是基于云的、本地部署的还是混合的，它都将来自各种来源（交易和运营、内部和外部）的数据集中存储，并供应用程序（主要用于机器学习、分析和报告）进行处理和访问。[数据平台](https://thenewstack.io/data/)为从金融交易到社交媒体信息流的一切提供动力。

随着应用程序和数据需求的发展，它们需要低延迟、可扩展的性能，并且不能停机。[Kubernetes](https://thenewstack.io/kubernetes/)已成为这些架构的关键推动者，它通过有效编排容器（包含运行应用程序所需的一切的轻量级、可移植软件包，从代码和运行时到依赖项）来实现。这种方法允许实时运营、交易和分析工作负载在不同的环境中无缝部署和扩展。

在本文中，我将比较在 Kubernetes 内部运行数据库与在传统基础设施（裸机或虚拟机）上运行数据库。我还将重点介绍 Kubernetes 运算符（用于管理和自动化有状态应用程序的特定于应用程序的控制器）如何使该系统上的数据库管理成为许多组织中可行甚至更优的选择。

## 传统数据平台管理

部署和管理数据库传统上涉及一个手动且容易出错的过程，尤其是在从本地硬件或原始云实例开始时。数据库是复杂的系统，通常需要复杂的配置和持续维护（所谓的“第二天运营”）。这些任务包括扩展、修补、性能优化、备份和恢复——所有这些都需要仔细注意。

在这些传统设置中，数据库管理通常意味着手动配置服务器、配置数据库、管理存储以及手动处理扩展和容错。这种传统方法不仅浪费时间且容易出现人为错误，还会导致运营开销和停机时间方面的巨大成本。当运行分布式数据库（多个节点）时，这些挑战会成倍增加，尤其是在为[高可用性](https://aerospike.com/glossary/high-availability-database/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack) (HA)运行多个集群时。

然而，随着[云原生技术](https://thenewstack.io/cloud-native/)（如 Kubernetes）的兴起，组织现在可以通过自动化和编排来管理许多这些问题。可以使用数据平台的 Kubernetes 运算符通过 Kubernetes 自动化手动流程。

## Kubernetes 内部数据平台的新时代

在您自己的 Kubernetes 部署中运行数据平台提供了几个引人注目的优势，特别是对于已经标准化该系统的组织。

### 简化的部署和统一管理

Kubernetes 为管理应用程序代码和基础设施提供了一个统一的平台。在 Kubernetes 上部署数据库使您可以集中管理整个堆栈，从应用程序层到数据库层。这允许更容易地协调资源、更好的可观察性和自动化的配置和扩展。

Kubernetes 通过抽象基础设施来帮助降低管理数据库的运营复杂性。使用 Kubernetes 时，部署数据库涉及定义一些高级 YAML 文件，这些文件可以进行版本控制、审查和共享。这种声明式方法使 Kubernetes 中的数据库管理成为一个 GitOps 友好的过程，非常适合现代 CI/CD 工作流程。

### 高可用性和自我修复

Kubernetes 的自我修复功能确保如果节点发生故障，工作负载可以重新调度到正常的节点。当与某些数据库架构（复制、集群）的固有容错能力相结合时，Kubernetes 可以通过选举新的主节点或重新同步副本来自动从故障中恢复，而不会停机。

例如，在 Kubernetes 中运行的[Aerospike](https://aerospike.com/products/database/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack) 或 MySQL 等数据平台依赖于运算符来监控 pod 和节点的运行状况，以便在出现问题时触发自动修复。如果节点发生故障，运算符将与 Kubernetes 协同工作，重新调度和重新分配工作负载，以确保数据库继续运行而无需人工干预，从而提高可用性并减少停机时间。
Kubernetes Operators实现自动化自我管理

寻求更多控制权的组织可以选择在Kubernetes上运行自管理数据库，无论是在本地还是在云中。Kubernetes Operators在此方法中扮演着关键角色。Operator通过自定义资源定义（CRD）扩展Kubernetes，以自动化部署和Day 2操作，例如扩展、备份和升级。[Aerospike的Kubernetes Operator (AKO)](https://aerospike.com/products/kubernetes-operator/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack)以规模化的方式体现了这种能力，为电商市场[Flipkart](https://aerospike.com/press-release/aerospike-database-on-kubernetes-enabled-95-million-transactions-per-second/?utm_source=byline&utm_medium=pr&utm_campaign=The%20New%20Stack)管理着超过170个集群，并在“十亿日”活动期间使其能够处理每秒9500万笔交易。

Operators使组织能够构建自己的自愈型自动化数据平台，提供更大的灵活性和[成本节约以及对数据基础设施的控制](https://thenewstack.io/improving-price-performance-lowers-infrastructure-costs/)。关键功能包括：

- **自动化部署**: Operators部署和扩展数据库，维护正确的配置，包括安全配置（这是人为错误的常见来源）。
- **多云和混合云支持**: Operators在混合和多云环境中部署和管理数据库集群，从而实现灾难恢复和高可用性。
- **管理备份和恢复**: Operators集成备份解决方案，安排备份并处理恢复。
- **修补和滚动升级**: Operators更新和修补数据库，无需停机。
- **监控和可观察性**: 与[工具](https://aerospike.com/products/observability-management/)（如Prometheus和Grafana）集成，可以对数据库的健康状况和性能进行详细的监控、警报和仪表板显示。

这种方法允许开发团队专注于构建应用程序，而Kubernetes和Operators则自动化和管理底层数据库基础设施。

### 云可移植性至关重要

Kubernetes提供了一个传统部署通常缺乏的关键优势：云可移植性。在Kubernetes中运行数据库允许您轻松地在云提供商之间迁移或运行多云环境。

使用Kubernetes，您可以声明性地定义您的基础设施，从而可以跨不同环境移动或复制相同的数据库设置。对于那些希望避免供应商锁定或出于成本、冗余或性能原因而在多个云中优化其工作负载的组织来说，这尤其有利。

### 控制和灵活性

在Kubernetes内部运行数据库的另一个关键优势是它提供的无与伦比的灵活性。通过在Kubernetes上的内部或您自己的云中管理数据库，您可以控制诸如自动扩展、备份和监控等重要功能——而无需绑定到数据库即服务 (DBaaS) 产品的预定义配置。Kubernetes支持对资源分配进行细粒度控制，允许您根据特定的性能和操作要求定制数据库部署。

此外，Kubernetes促进了无缝的工作负载整合，最大限度地利用现有云基础设施。通过在同一组节点上编排多个工作负载，与静态裸机或独立管理的虚拟实例相比，Kubernetes提供了一种更动态、更高效的资源管理方式。这种灵活性使组织能够根据需求变化调整其数据库基础设施，从而优化当前需求和未来的可扩展性。

## 现实检验——您的数据平台是否需要Kubernetes？

虽然在Kubernetes中运行数据库有很多优点，但它并非适用于所有情况。当然，如果您的组织缺乏Kubernetes专业知识，那么额外的开销可能会超过其好处。如果您完全依赖于传统或利基数据平台，那么您可能必须等待供应商开发一个Operator，然后可能还要等待一段时间才能将其用作自动化工具。虽然Kubernetes提供自愈功能，但某些数据库系统通常需要更高级的配置和微调才能确保最大的可靠性和性能，这在Kubernetes中可能难以实现。

如果您的组织符合上述任何一种情况，则必须在将Kubernetes用于数据平台之前解决这些问题。

## 数据平台的未来就在今天

越来越多的组织选择在 Kubernetes 中运行数据库，因为它在数据库管理方面具有灵活性和可扩展性以及自动化优势。Kubernetes 运算符自动化关键的第二阶段操作——例如备份、监控和自我修复——而 Kubernetes 提供了易于部署、扩展和容错的基础架构。对于已经使用 Kubernetes 作为其容器编排平台的团队来说，在其中运行数据库可以提供一个统一的堆栈，从而获得更大的控制力和灵活性。但是，团队必须仔细权衡利弊，以确保这种方法符合其运营需求。有一点很明确：在裸机或虚拟机上手动管理数据库的日子即将结束，因为 Kubernetes 提供了一种更自动化、更经济高效且更面向未来的解决方案。
