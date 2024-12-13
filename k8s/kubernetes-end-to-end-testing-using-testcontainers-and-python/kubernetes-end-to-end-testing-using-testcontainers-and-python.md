
<!--
title: 使用Testcontainers和Python进行Kubernetes端到端测试
cover: https://cdn.thenewstack.io/media/2024/12/bf92486b-kubernetes-testing-python-testcontainers.jpg
-->

学习如何结合 testcontainers-k3s 和 Python，创建隔离的、可复现的、类似生产环境的测试环境，以进行彻底的测试。

> 译自 [Kubernetes End-to-End Testing Using Testcontainers and Python](https://thenewstack.io/kubernetes-end-to-end-testing-using-testcontainers-and-python/)，作者 Manish Saini。

Kubernetes应用程序的测试通常涉及多个依赖项和复杂的环境。虽然端到端 (E2E) 测试提供了一种验证应用程序行为的现实方法，但复制生产环境可能具有挑战性。使用[Testcontainers](https://thenewstack.io/what-is-testcontainers-and-why-should-you-care/)，您可以通过使用轻量级、一次性容器来模拟Kubernetes集群及其依赖项来简化此过程。

您可以使用[testcontainers-python](https://testcontainers-python.readthedocs.io/en/latest/)库来执行[Kubernetes](https://thenewstack.io/kubernetes/)应用程序的端到端测试。

## 什么是Testcontainers？

[Testcontainers](https://testcontainers.com/)是一个开源库，支持运行轻量级、一次性容器进行测试。通过添加Kubernetes相关的模块，例如`testcontainers-k3s`，您可以将Kubernetes集群作为测试设置的一部分启动。

使用Testcontainers进行Kubernetes测试具有以下优势：

* **真实的测试环境**: 在隔离的容器中模拟Kubernetes集群和服务。
* **自动化**: 自动化数据库、消息代理或Kubernetes等依赖项的设置和拆卸。
* **效率**: 在干净、可重复的环境中运行测试，无需手动配置Kubernetes集群。
* **动态配置**: 为每个测试场景动态自定义依赖项。

## 为Python设置Testcontainers

### 先决条件

1. 安装最新版本[Python](https://thenewstack.io/what-is-python/) 3.8或更高版本
2. **Docker**: 确保已安装并运行Docker。
3. **安装Testcontainers**: 使用`pip`安装库。

## 运行Kubernetes应用程序的E2E测试

在此分步示例中，我将向您展示如何测试与PostgreSQL数据库交互的Kubernetes应用程序。测试将：

1. 使用`testcontainers-k3s`启动Kubernetes集群。
2. 部署应用程序和数据库。
3. 通过HTTP请求验证应用程序的行为。

### 1. 创建Python测试类

以下脚本使用Testcontainers中的`K3sContainer`设置Kubernetes集群：

### 2. 创建Kubernetes清单

为应用程序和[PostgreSQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-postgresql/)数据库创建Kubernetes清单。

#### app.yaml

#### postgres.yaml

### 3. 运行测试

使用您首选的Python测试运行器（例如[Pytest](https://pytest.org/)）执行测试：

```bash
pytest test_kubernetes_app.py
```

此测试将：

- 在Testcontainers实例中启动PostgreSQL。
- 启动轻量级Kubernetes集群。
- 部署应用程序和数据库。
- 验证应用程序是否可访问并按预期运行。

## Kubernetes E2E测试的最佳实践

* **资源管理**: 确保您的系统拥有足够的资源来运行容器和Kubernetes集群。
* **命名空间隔离**: 为每个测试使用单独的命名空间以避免冲突。
* **模拟外部API**: [模拟](https://thenewstack.io/the-tidal-wave-of-api-drift-use-mocking-to-stay-afloat/)不在测试范围内的依赖项以提高可靠性。
* **并行化**: 通过并行运行独立的测试用例来优化测试执行。

## 结论

由于其分布式特性，Kubernetes中的端到端测试可能令人生畏；但是，Testcontainers使该过程更容易。通过将`testcontainers-k3s`模块与Python结合使用，您可以为彻底测试创建隔离的、可重现的和类似生产的环境。这确保您的应用程序在投入生产之前按预期在Kubernetes中运行。

采用这种方法可以让您在管道早期发现关键问题并交付更强大的软件。为什么不尝试一下Testcontainers并增强您的Kubernetes测试策略呢？

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)