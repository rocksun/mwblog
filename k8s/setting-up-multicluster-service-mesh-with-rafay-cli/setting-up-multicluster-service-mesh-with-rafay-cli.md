# 使用 Rafay CLI 配置多集群服务网格

尽管 Istio 提供多集群连接功能，但配置它可能会复杂而繁琐。新工具可以提供帮助。

![](https://cdn.thenewstack.io/media/2023/08/ddc2c610-istio-1024x593.jpg)
*图片来自 Shutterstock 的 Laylistique*

这是两篇系列文章的第二部分。请阅读[第一部分](http://yylives.cc/2023/09/02/simplifying-cluster-connectivity-with-istio-service-mesh/)。

在过去的几个月里，我们的团队一直在扩展 Rafay 的 SaaS 控制器。作为这一过程的重要部分，我们着手设置了多集群 Istio 环境。在这个过程中，我们遇到并成功解决了之前提到的挑战。这些挑战包括管理配置的复杂性，确保跨集群的设置一致性，建立安全的网络连接以及处理服务发现、监视和故障排除的复杂性。

为了克服这些挑战，我们采用了基础设施即代码（IaC）方法来进行配置管理，并开发了一个命令行界面（CLI）自动化工具，以确保多集群 Istio 部署的一致性和流程化。CLI 遵循 Istio 文档中描述的“不同网络上的多主节点”模型。我们在多集群 Istio 部署中使用的拓扑结构如下图所示。

![](https://cdn.thenewstack.io/media/2023/08/3fde089e-image1.png)

CLI 使用简单直接的配置。以下是配置格式的示例：

```yaml
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

（注意：上面的示例是通用展示。）

在此配置中，CLI 被设置为与两个 Kubernetes 集群一起工作：cluster1 和 cluster2。每个集群都定义了其各自的详细信息，包括 Kubernetes kubeconfig 文件、上下文和要安装的 Istio 版本。CLI 使用此配置来在集群之间建立服务的连接，并创建多集群服务网格。

配置说明：

**Certificate**：此配置使用 CLI 在网格中建立所有集群之间的信任。它将为每个集群生成并部署不同的证书。所有集群证书都由相同的根证书颁发机构（CA）颁发。在内部，CLI 使用 [step-ca](https://github.com/smallstep/cli) 工具。

![](https://cdn.thenewstack.io/media/2023/08/9eb112d5-image3.png)

说明：

- apiVersion：正在使用的 API 版本，本例中是 ristioctl.k8smgmt.io/v3 。
- kind：资源类型，在本例中为 Certificate（证书）。
- metadata：与资源关联的元数据，如资源名称。
- spec：此部分包含资源的规范或设置。
  - validityHours：指定证书的有效期（以小时为单位）。
  - password：指示是否需要密码。
  - sanSuffix：证书的主体备用名称（SAN）后缀。
  - meshID：多集群服务网格的标识符。

**Cluster**：这些是用于定义将成为多集群服务网格一部分的各个 Kubernetes 集群的集群资源。每个集群资源代表一个不同的 Kubernetes 集群。

![](https://cdn.thenewstack.io/media/2023/08/e053c056-image2.png)

说明：

- kubeconfigFile：指定相应集群的 kubeconfig 文件路径，其中包含身份验证详细信息和集群信息。
- context：与集群关联的 Kubernetes 上下文，定义了一组命名的访问参数。
- meshID：标识这些集群将连接到的多集群服务网格。
- version：指定要在这些集群中部署的 Istio 版本。
- installHelloWorld：指示是否在每个集群中部署一个示例 HelloWorld 应用程序。

总的来说，此配置描述了使用 ristioctl CLI 工具设置多集群服务网格所需的设置。它包括证书和将成为服务网格一部分的 Kubernetes 集群的规范。ristioctl CLI 工具将使用此配置部署 Istio 和其他必需的配置，以在这些集群之间创建一个统一且可扩展的网格。下面的步骤概述了 CLI 工具在内部处理的任务，以设置多集群服务网格。让我们进一步解释每个步骤：

- **配置跨所有集群的信任关系**：CLI 工具在参与多集群服务网格的 Kubernetes 集群之间建立信任关系。这种信任允许不同集群中的服务进行安全通信和身份验证。这涉及生成和分发用于相互 TLS（传输层安全）身份验证的证书和密钥。
- **将 Istio 部署到集群中**：CLI 将 Istio 部署到网格中的每个 Kubernetes 集群中。
- **将东西向网关部署到集群中**：东西向网关是一个负责处理服务网格内部流量的 Istio 组件，特别是不同集群中服务之间的流量（东西向流量）。CLI 将东西向网关部署到每个集群中，以实现跨集群通信。
- **暴露集群中的服务**：CLI 确保在每个集群中运行的服务被适当地暴露并可访问其他多集群服务网格中的集群。
- **使用 Rafay ZTKA-based 安全通道提供跨集群服务发现**：Rafay ZTKA（Zero Trust Kubectl Access）是一种安全通道技术，可实现跨集群 Kube API 服务器通信。

通过自动化这些步骤，CLI 简化了设置多集群服务网格的过程，减少了用户的操作复杂性，并确保在不同环境中的集群之间创建了一个统一且可扩展的网格。这种方法增强了连接性、安全性和可观察性，使组织能够轻松采用多云或混合云策略。

要使用它：

```bash
ristioctl apply -f examples/mesh.yaml
```

CLI 是开源的。您可以在 [https://github.com/RafaySystems/rafay-istio-multicluster/blob/main/README.md](https://github.com/RafaySystems/rafay-istio-multicluster/blob/main/README.md) 上找到更多详细信息。

我们使用 Rafay Zero Trust Kubectl Access（ZTKA） 来防止将 Kubernetes 集群 Kube API 服务器暴露给不同的网络，以提高安全性。要实现这一点，您需要在配置中包含 Rafay 的 ZTKA kubeconfig 。结果的拓扑将类似于以下内容：

## 结论

多集群服务连接对于各种组织需求至关重要。虽然 Istio 提供了多集群连接，但配置可能复杂和繁琐。因此，我们开发了一个工具来简化配置过程。确保在集群之间建立安全的网络连接是保护多集群环境中的数据的重要手段。通过我们的工具，组织可以简化多集群服务网格的设置，并建立一个安全且可扩展的基础设施，以有效支持其分布式应用程序。
