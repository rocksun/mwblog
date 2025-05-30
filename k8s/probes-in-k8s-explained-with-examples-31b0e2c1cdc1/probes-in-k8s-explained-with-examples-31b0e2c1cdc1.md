
<!--
title: 使用探针在Kubernetes中构建自愈应用程序
cover: https://miro.medium.com/v2/resize:fit:909/1*6773n1kDv-5hs5Q9dVOFXA.png
summary: 容器宕机？Kubernetes探针来救场！🔥Liveness Probe、Readiness Probe、Startup Probe三大探针，YAML实战+图表详解，教你精准重启、流量控制、延迟检查，Exec、HTTP探针机制全掌握，让你的云原生应用永不失联！🚀
-->

容器宕机？Kubernetes探针来救场！🔥Liveness Probe、Readiness Probe、Startup Probe三大探针，YAML实战+图表详解，教你精准重启、流量控制、延迟检查，Exec、HTTP探针机制全掌握，让你的云原生应用永不失联！🚀

> 译自：[Build Self-Healing Apps in Kubernetes Using Probes](https://medium.com/@Vishwa22/probes-in-k8s-explained-with-examples-31b0e2c1cdc1)
> 
> 作者：VISHWA S

你的容器可能正在运行……但完全没有响应。
Kubernetes 探针可以帮助你检测到这一点并采取措施。
在这篇文章中，我将向你展示**如何正确使用存活探针、就绪探针和启动探针**，并提供**真实的 YAML、图表和用例**。

## Kubernetes 中的探针是什么？

探针是 Kubernetes 检查你的容器是否**存活**并**准备好**服务流量的方式。

它们帮助 Kubernetes：

- 知道容器是否需要**重启**（如果它不健康）。
- 知道容器是否**准备好接收流量**。

## 三种类型的探针

**1. 存活探针 (Liveness Probe)**

检查容器是否**存活**（即，没有卡住，没有响应）。

- 如果探针失败，Kubernetes **重启容器**。
- 适用于可能进入**死锁**或卡住状态的应用程序。

**2. 就绪探针 (Readiness Probe)**

检查容器是否**准备好接受流量**。

- 如果它失败，**流量不会发送**到容器。
- 当你的应用程序需要时间初始化或依赖于外部事物时非常有用。

**3. 启动探针 (Startup Probe)**

用于延迟**存活 + 就绪**检查，直到应用程序**完全启动**。

- 防止应用程序启动时间过长时出现误报。
- 一旦成功，其他探针就会启动。

## 探针机制（它们如何工作）

**a. Exec 探针**

- 在**容器内运行命令**。
- 如果退出代码 = `0`，则成功；否则失败。

**例子**：

`livenessProbe:`
```yaml
exec:
  command:
  - cat
  - /tmp/healthy
initialDelaySeconds: 5
periodSeconds: 5
```

**b. HTTP 探针**

- 向特定路径/端口发出 **HTTP GET** 请求。
- 如果它返回 `2xx` 或 `3xx` 状态代码 → 成功。