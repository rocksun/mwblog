# 使用 Rafay CLI 配置多集群服务网格

尽管 Istio 提供多集群连接功能，但配置它可能会复杂而繁琐。新工具可以提供帮助。

![](https://cdn.thenewstack.io/media/2023/08/ddc2c610-istio-1024x593.jpg)
*图片来自 Shutterstock 的 Laylistique*

这是两篇系列文章的第二部分。请阅读第一部分。

在过去的几个月里，我们的团队一直在扩展Rafay的SaaS控制器。作为这一过程的重要部分，我们着手设置了多集群Istio环境。在这个过程中，我们遇到并成功解决了之前提到的挑战。这些挑战包括管理配置的复杂性，确保跨集群的设置一致性，建立安全的网络连接以及处理服务发现、监视和故障排除的复杂性。

为了克服这些挑战，我们采用了基础设施即代码（IaC）方法来进行配置管理，并开发了一个命令行界面（CLI）自动化工具，以确保多集群Istio部署的一致性和流程化。CLI遵循Istio文档中描述的“不同网络上的多主节点”模型。我们在多集群Istio部署中使用的拓扑结构如下图所示。

CLI使用简单直接的配置。以下是配置格式的示例：

```
$ cat examples/mesh.yaml
apiVersion: ristioctl.k8smgmt.io/v3
kind: Certificate
metadata:
  name: ristioctl-certs	
spec:
  validityHours: 2190
  password: false
  sanSuffix: istio.io # Subject Alternative Name Suffix
  meshID: uswestmesh
---
apiVersion: ristioctl.k8smgmt.io/v3
kind: Cluster
metadata:
  name: cluster1
spec:
  kubeconfigFile: "kubeconfig-istio-demo.yaml"
  context: cluster1
  meshID: uswestmesh
  version: "1.18.0"
  installHelloWorld: true #deploy sample HelloWorld application
---
apiVersion: ristioctl.k8smgmt.io/v3
kind: Cluster
metadata:
  name: cluster2
spec:
  kubeconfigFile: "kubeconfig-istio-demo.yaml"
  context: cluster2
  meshID: uswestmesh
  version: "1.18.0"
  installHelloWorld: true   #deploy sample HelloWorld application
```

（注意：上面的示例是通用表示。）

在此配置中，CLI被设置为与两个Kubernetes集群一起工作：cluster1和cluster2。每个集群都定义了其各自的详细信息，包括Kubernetes kubeconfig文件、上下文和要安装的Istio版本。CLI使用此配置来在集群之间建立服务的连接，并创建多集群服务网格。
