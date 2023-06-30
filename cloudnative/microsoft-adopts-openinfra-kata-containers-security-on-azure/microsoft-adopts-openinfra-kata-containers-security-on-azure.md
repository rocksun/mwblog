# 微软在 Azure 上采用 OpenInfra Kata 容器安全技术

微软的客户希望在 Azure 上获得更多安全性，因此微软选择了 Kata 容器来提供给他们。

翻译自 [Microsoft Adopts OpenInfra Kata Containers Security on Azure](https://thenewstack.io/microsoft-adopts-openinfra-kata-containers-security-on-azure/) 。

![](https://cdn.thenewstack.io/media/2023/06/1f8454d9-colors-1838392_1280-e1687989078427-1024x683.jpg)

每个人都希望在其云处理和数据上获得更多安全性。为了实现这一目标，微软在最近的 [OpenInfra 峰会](https://openinfra.dev/summit/vancouver-2023/)上宣布，它即将向 [Azure](https://azure.microsoft.com/en-ca) 的客户提供更多安全性。实现这一目标的方式是在开源 [Kata 容器](https://katacontainers.io/)内提供 [Azure Kubernetes Service（AKS）](https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes) 上的机密容器。此举旨在加强云安全性，为敏感数据和应用程序提供增强的保护。

Kata 容器提供了带有轻量级虚拟机的安全容器运行时。这些容器与普通容器相似，但具有虚拟机更强的工作负载隔离能力。它依赖于 AMD SVM 和 Intel VT-x CPU 虚拟化技术，提供了额外的保护层次。

## Azure 的实现

在 Azure 的实现中，Azure 利用 AMD 的 SEV-SNP 硬件支持的可信执行环境（TEEs）来提供机密的 Kara 容器。这些容器为正在使用的代码和数据提供完整性，保护内存中的数据免受 Azure 操作员的访问，并通过[验明身份](https://csrc.nist.gov/glossary/term/attestation)来进行远程[加密验证](https://thenewstack.io/cryptographic-keys-in-a-cloud-native-environment/)。在这一方案中，现有的未经修改的应用程序可以继续在这些容器上无缝运行。

为了实现这种与应用程序飞地类似的隔离级别，并加强对虚拟机管理员的保护，这些容器在每个 Pod 上运行专用的"子虚拟机（VM）"中。每个容器拥有自己的内存加密密钥，并配备 AMD SEV-SNP 保护，其生命周期与机密 Kubernetes Pod 的生命周期相关联。

通过以这种隔离级别运行 [Kubernetes Pod](https://thenewstack.io/kubernetes-way-part-one/) ，利用嵌套虚拟化，客户可以在与父 VM 和租户操作系统管理员隔离的环境中运行任何 Linux [Open Container Initiative (OCI)](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) 兼容的容器。

## Kata和AKS

微软的 AKS 产品经理 [Michael Withrow](https://www.linkedin.com/in/mwithrow/) 解释说，客户不仅要求更多安全性（这在今天是不言而喻的），他们特别要求了 Kata 。这项 [OpenInfra 基金会](https://openinfra.dev/)的技术因易于使用、易于实施和极高的安全性而声名鹊起。

在实际应用中，Kata 和 AKS 的结合可用于从共享主机中进行工作负载隔离、不受信任容器的隔离（也称为沙箱化）以及共享集群的多租户。从实际情况来看，微软认为在消费者市场（银行、医疗、公共部门和国防市场）中存在这一结合的巨大市场潜力。

尽管目前尚未完全准备好投入生产使用，但已经进入了公开预览阶段。微软希望在接下来的几个月内将其提供给商业客户使用。一旦正式推出，我预计会有很多用户涌向使用它。