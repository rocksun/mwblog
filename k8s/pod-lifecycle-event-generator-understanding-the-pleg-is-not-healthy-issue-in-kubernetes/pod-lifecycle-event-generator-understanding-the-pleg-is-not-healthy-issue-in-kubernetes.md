#  理解 Kubernetes 中的“PLEG is not healthy”问题

最近团队的 Kubernetes 频繁的遭遇 “PLEG is not healthy” 问题，虽然定位出一些原因，但是因为这个问题经常会引发 NodeNotReady 问题，所以还是需要深入理解一下原理。看到 RedHat 开发者网站的 [Pod Lifecycle Event Generator: Understanding the "PLEG is not healthy" issue in Kubernetes](https://developers.redhat.com/blog/2019/11/13/pod-lifecycle-event-generator-understanding-the-pleg-is-not-healthy-issue-in-kubernetes#)，感觉不错，翻译下分享给大家。

在本文中，我将探讨 Kubernetes 中的“PLEG is not healthy”问题，有时会导致“NodeNotReady”的状态。如果了解 Pod Lifecycle Event Generator (PLEG) 的工作方式，可以对解决此问题有所帮助。

## 什么是 PLEG？

kubelet（Kubernetes 中的组件）中的 PLEG 模块通过每个匹配的 Pod 级事件来调整容器运行时状态，并通过应用变更来保持 pod 缓存的状态同步。

让我们来看一下下面流程图中的虚红线部分。

![](https://developers.redhat.com/blog/wp-content/uploads/2019/10/orig-pleg-1.png)


## “PLEG is not healthy”是如何发生的？

Kubelet 通过在 SyncLoop() 中定期调用 Healthy() 来持续检查 PLEG 的健康状况，如下所示。

Healthy() 检查 relist 过程（ PLEG 的关键任务）是否在 3 分钟内完成。此函数被添加到 runtimeState 作为 “PLEG” ，并且从 “SyncLoop” 中定期调用（默认每 10 秒一次）。如果 “relist” 过程耗时超过 3 分钟，则会通过此堆栈过程报告“ PLEG 不健康”问题。

我将根据 Kubernetes 1.11（OpenShift 3.11） 中的相关源代码逐个部分为您解释。如果您对 Go 语法不太熟悉，也没关系，只需要阅读代码中的注释即可。为了便于阅读，我还将从源代码中截取不太重要的部分。

![](https://developers.redhat.com/blog/wp-content/uploads/2019/10/pleg-healthy-checks.png)

```go
//// pkg/kubelet/pleg/generic.go - Healthy()

// The threshold needs to be greater than the relisting period + the
// relisting time, which can vary significantly. Set a conservative
// threshold to avoid flipping between healthy and unhealthy.
relistThreshold = 3 * time.Minute
:
func (g *GenericPLEG) Healthy() (bool, error) {
  relistTime := g.getRelistTime()
  elapsed := g.clock.Since(relistTime)
  if elapsed > relistThreshold {
	return false, fmt.Errorf("pleg was last seen active %v ago; threshold is %v", elapsed, relistThreshold)
  }
  return true, nil
}

//// pkg/kubelet/kubelet.go - NewMainKubelet()
func NewMainKubelet(kubeCfg *kubeletconfiginternal.KubeletConfiguration, ...
:
  klet.runtimeState.addHealthCheck("PLEG", klet.pleg.Healthy)

//// pkg/kubelet/kubelet.go - syncLoop()
func (kl *Kubelet) syncLoop(updates <-chan kubetypes.PodUpdate, handler SyncHandler) {
:
// The resyncTicker wakes up kubelet to checks if there are any pod workers
// that need to be sync'd. A one-second period is sufficient because the
// sync interval is defaulted to 10s.
:
  const (
	base   = 100 * time.Millisecond
	max	= 5 * time.Second
	factor = 2
  )
  duration := base
  for {
      if rs := kl.runtimeState.runtimeErrors(); len(rs) != 0 {
   	   glog.Infof("skipping pod synchronization - %v", rs)
   	   // exponential backoff
   	   time.Sleep(duration)
   	   duration = time.Duration(math.Min(float64(max), factor*float64(duration)))
   	   continue
      }
	:
  }
:
}

//// pkg/kubelet/runtime.go - runtimeErrors()
func (s *runtimeState) runtimeErrors() []string {
:
    for _, hc := range s.healthChecks {
   	 if ok, err := hc.fn(); !ok {
   		 ret = append(ret, fmt.Sprintf("%s is not healthy: %v", hc.name, err))
   	 }
    }
:
}
```
