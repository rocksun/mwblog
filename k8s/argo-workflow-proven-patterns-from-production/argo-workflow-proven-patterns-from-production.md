
# Argo Workflow-来自生产的成熟模式

TODO

译自 [Argo Workflows - Proven Patterns from Production](https://hodgkins.io/argo-workflow-proven-patterns-from-production) 。



[Argo Workflow](https://argoproj.github.io/argo-workflows/use-cases/infrastructure-automation/)为基础设施自动化提供了一个优秀的平台,已经取代 [Jenkins](https://hodgkins.io/automating-with-jenkins-and-powershell-on-windows-part-1) 成为我用于运行定时任务或事件驱动自动化任务的首选工具。

在使用 Argo 工作流的过程中,我也遇到过集群崩溃、工作流中断等问题,积累了许多需要重构以便维护的工作流经验。

本博客旨在分享我的一些学习经验和最佳实践,以帮助您避免我犯过的错误。

## 经验 - 配置工作流TTL和Pod垃圾回收

想避免压垮 Kubernetes 控制平面？那么将此事项排在待办列表的前面吧😜。

以下情况让我得到了这个教训。我在[遍历](https://github.com/argoproj/argo-workflows/blob/a45afc0c87b0ffa52a110c753b97d48f06cdf166/examples/loops-dag.yaml)一个列表项,为每个条目执行一个模板。该模板包含约 50 个步骤的有向无环图工作流。整个工作流总共运行了大约 1500 个 pod。

一开始没问题,直到我遍历的列表项变多,然后我开始注意到一些问题:

* 查看工作流时,Argo Workflows UI 非常缓慢无响应,使故障排除很困难。
* 一些失败步骤的工作流在重试时,最终超过了 etcd 中 1MB 的对象限制,导致“提交工作流失败:etcdserver:请求过大”等错误。
* 由于跟踪的 pod 数量,Kubernetes 几乎陷入瘫痪。这不仅仅是活动 pod,还包括 `completed` 状态的 pod。

Argo Workflows 文档优化部分中提到:

> Pod 垃圾回收 - 删除已完成 pod。默认情况下,pod 不会被删除。

我应该早点看到这个提示的😅。