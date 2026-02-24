随着[Kubernetes 1.35](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/)的发布，[Pod原地调整大小](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)功能已正式发布（GA），而[垂直Pod自动伸缩](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)的 *InPlaceOrRecreate* 更新模式已升级到测试版（beta）。这意味着VPA现在可以在不驱逐运行中的Pod的情况下调整其大小，这对于有状态和长时间运行的工作负载来说是一个重大改进。

在本教程中，我将引导您完成在Minikube上安装VPA、部署示例应用程序、观察资源推荐、启用原地调整大小以及生成流量以实时查看VPA调整Pod资源的动手步骤。

## 先决条件

在我们开始之前，请确保您的工作站上已安装以下工具。

*   [**Minikube**](https://minikube.sigs.k8s.io/docs/)用于配置本地单节点Kubernetes 1.35集群。
*   [**kubectl**](https://kubernetes.io/docs/reference/kubectl/)是Kubernetes命令行工具，配置用于与Minikube集群通信。
*   [**Git**](https://git-scm.com/)是克隆官方自动伸缩器存储库以安装VPA所必需的。

## 步骤1 – 启动和配置Minikube集群

如果您的Minikube集群尚未运行，请为其启动并分配足够的资源以支持VPA和演示工作负载。我建议至少分配4个CPU和4 GB内存。

`minikube start --cpus=4 --memory=4096`

验证集群正在运行且可访问。
`kubectl cluster-info`

输出应确认Kubernetes控制平面正在本地地址运行。

## 步骤2 – 启用Metrics Server

VPA依赖于[Kubernetes Metrics API](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)来观察Pod资源消耗。Minikube将Metrics Server作为内置插件捆绑。使用以下命令启用它。

`minikube addons enable metrics-server`

Metrics Server大约需要60秒才能开始收集数据。等待后，验证它是否正常运行。

`kubectl top nodes`

您应该看到Minikube节点的CPU和内存利用率。如果命令返回错误，指示指标尚未可用，请再等待30秒然后重试。

## 步骤3 – 安装VPA组件

虽然Kubernetes 1.35原生提供了原地调整大小机制，但VPA控制器本身仍需单独安装。克隆官方的自动伸缩器[存储库](https://github.com/kubernetes/autoscaler)并导航到VPA目录。

`git clone https://github.com/kubernetes/autoscaler.git  
cd autoscaler/vertical-pod-autoscaler`

运行安装脚本。

`./hack/vpa-up.sh`

这将创建VPA自定义资源定义，配置RBAC权限，部署Recommender、Updater和Admission Controller，并设置 mutating webhook。

确认所有三个VPA组件都在kube-system命名空间中运行。

`kubectl get pods -n kube-system | grep vpa`

您应该看到三个Pod（vpa-recommender、vpa-updater和vpa-admission-controller）都处于Running状态。

![](https://cdn.thenewstack.io/media/2026/02/ab2df57d-carbon-1024x202.png)

## 步骤4 – 部署示例NGINX应用程序

我们将部署一个带有两个副本的NGINX Web服务器，并故意降低资源请求。这为VPA观察使用情况并推荐调整留下了空间。

为演示创建一个专用命名空间。

创建部署，CPU请求仅为50毫核，内存请求为64 MiB。

应用这两个清单。

`kubectl apply -f vpa-demo-namespace.yaml  
kubectl apply -f vpa-demo-deployment.yaml`

验证两个NGINX Pod正在运行。

`kubectl get pods -n vpa-demo`

![](https://cdn.thenewstack.io/media/2026/02/b84f3804-carbon-1-1024x262.png)

## 步骤5 – 创建推荐模式下的VPA

首先将`updateMode`设置为`Off`，以便VPA计算推荐，而不修改任何正在运行的Pod。

`targetRef`将此VPA与我们的NGINX部署关联起来。`containerPolicies`部分通过`minAllowed`设置25毫核和32 MiB的下限，通过`maxAllowed`将推荐上限设置为1个CPU和512 MiB，并指示VPA通过`controlledResources`管理CPU和内存。

应用VPA资源。

`kubectl apply -f vpa-recommendation-only.yaml`

## 步骤6 – 检查VPA推荐

大约2到3分钟后，Recommender将收集到足够的指标来生成其初始推荐。检索VPA状态。

`kubectl get vpa nginx-vpa -n vpa-demo -o yaml`

查找`status.recommendation`部分。您将看到类似以下的输出。

`status:  
recommendation:  
containerRecommendations:  
- containerName: "nginx"  
target:  
cpu: "25m"  
memory: "262144k"  
lowerBound:  
cpu: "25m"  
memory: "262144k"  
upperBound:  
cpu: "1"  
memory: "262144k"  
uncappedTarget:  
cpu: "12m"  
memory: "262144k"`

如果启用了自动更新，`target`是VPA将设置的资源请求。`uncappedTarget`是应用`minAllowed`和`maxAllowed`约束之前的原始推荐。请注意，CPU的`uncappedTarget`是12毫核，但`target`显示25毫核，因为我们的`minAllowed`策略强制执行该下限。

## 步骤7 – 启用InPlaceOrRecreate更新模式

现在，让我们使用`InPlaceOrRecreate`模式启用自动资源调整。

在`InPlaceOrRecreate`模式下，Updater首先尝试通过`/resize`子资源修补Pod的资源规范来原地调整Pod大小。Pod的UID、容器ID和重启次数都保持不变。如果节点缺乏足够的资源，VPA会回退到传统的驱逐并重新创建的流程。`controlledValues`字段设置为`RequestsAndLimits`指示VPA在保持原始比例的同时调整请求和限制。

应用更新后的配置。

`kubectl apply -f vpa-inplace.yaml`

稍后，验证更新后的资源请求。

`kubectl describe pod -n vpa-demo -l app=nginx-vpa-demo | grep -A 3 "Requests:"`

Pod的age和restart count应该确认没有发生驱逐或重启。
对于运行Kubernetes 1.35之前版本的集群，您可以使用设置为`Auto`或`Recreate`的`updateMode`，通过Pod驱逐和重新创建实现相同的结果。

## 步骤8 – 生成负载并观察VPA的实际运行

要查看VPA动态调整资源，请将NGINX部署公开为Service，并生成持续的HTTP流量。

创建一个ClusterIP服务。

部署一个在紧密循环中发送请求的负载生成器Pod。

应用这两个清单。
`kubectl apply -f vpa-demo-service.yaml  
kubectl apply -f vpa-load-generator.yaml`

每30秒轮询VPA目标，观察推荐值的上升。

`kubectl get vpa nginx-vpa -n vpa-demo -o jsonpath='{.status.recommendation.containerRecommendations[0].target}' ; echo`

您应该看到CPU目标随着Recommender整合新的使用数据而增加。由于我们运行在`InPlaceOrRecreate`模式下，Updater将实时调整NGINX Pod的大小。通过检查Pod的age来确认Pod没有重启。

`kubectl get pods -n vpa-demo -l app=nginx-vpa-demo`

检查应用于运行中的Pod的实际资源请求。

`kubectl describe pod -n vpa-demo -l app=nginx-vpa-demo | grep -A 3 "Requests:"`

请求现在应该反映VPA提高的推荐值，而不是我们在部署清单中指定的原始50毫核。

观察完成后，停止负载生成器。

`kubectl delete pod load-generator -n vpa-demo`

## 清理

通过删除命名空间来移除所有演示资源。

`kubectl delete namespace vpa-demo`

要从集群中完全卸载VPA，请运行清理脚本。

`cd autoscaler/vertical-pod-autoscaler  
./hack/vpa-down.sh`

## 总结

在本教程中，我们在运行Kubernetes 1.35的Minikube集群上安装了VPA，部署了一个示例NGINX应用程序，在被动模式下观察了VPA推荐，启用了`InPlaceOrRecreate`更新策略，并验证了VPA可以在持续流量下不中断地调整运行中Pod的大小。此版本中正式发布的原地调整大小功能消除了Pod驱逐的需要，使得VPA成为有状态和对重启敏感的生产工作负载的实用选择。