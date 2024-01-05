<!--
title: Kubernetes的Top 4攻击链及其破解方法
cover: ./cover.jpg
-->

尽管Kubernetes的采用率持续飙升，但它已成为网络攻击的主要目标。不幸的是，Kubernetes集群很复杂，[难以保护](https://www.armosec.io/blog/kubernetes-cluster-security/)。确保您的Kubernetes环境安全需要对威胁基础设施的常见[攻击链](https://www.armosec.io/glossary/attack-chain-in-kubernetes/)有深入的理解。

> 译自 [Top four Kubernetes Attack Chains and how to break them ](https://www.armosec.io/blog/kubernetes-attack-chains-and-how-to-break-them/)。作者 Oshrat Nir 。

在本博客文章中，我们深入研究了针对Kubernetes的顶级攻击链，揭示了风险并提供宝贵的见解以增强您的防御能力。

## 攻击路径A：暴露的端点攻击

在这种类型的网络攻击中，恶意行为者瞄准一个将其一个或多个端点暴露给公共互联网的Kubernetes集群。这些端点可以包括Kubernetes API服务器、kubelet或其他未正确保护的服务。

一旦攻击者访问了暴露的端点，他们可以利用它进一步访问集群，包括其敏感数据和资源。

### 攻击链

![](https://www.armosec.io/wp-content/uploads/2023/10/Exposed-endpoint-attack-on-an-ingress-controller-in-a-Kubernetes-cluster-1024x494.png.webp)

*图1：对Kubernetes集群中的入口控制器进行的暴露的端点攻击*

这个攻击链场景涉及一个面向公共的容器化工作负载，具有远程代码执行漏洞。这个漏洞可以类比为后门，允许攻击者渗透并接管容器化进程。

此场景涉及的步骤如下。

### 步骤1：侦察

黑客在集群网络中探测公共漏洞，并发现一个具有[远程代码执行漏洞](https://www.armosec.io/blog/remote-code-execution-rce/)的暴露工作负载。这个工作负载可以是由pod使用的服务，也可能是一个未经安全配置的Kubernetes API服务器或kubelet，默认启用匿名访问。

当集群中的工作负载被公开暴露时，攻击者可以从受损的工作负载发送API请求，以探测集群并窃取有关其他集群资源的敏感信息。

### 步骤2：利用

如果集群使用默认设置，其中服务帐户令牌被挂载到集群中的每个创建的pod中，攻击者可以访问令牌并使用它来进行身份验证，从而访问Kubernetes API服务器。这使他们能够获得该服务帐户的资源和特权。

### 步骤3：横向 & 纵向移动

如果工作负载挂载了[Kubernetes secrets](https://www.armosec.io/blog/revealing-the-secrets-of-kubernetes-secrets/)，威胁就会加深，因为攻击者将能够从Kubernetes API服务器检索这些secrets，并有可能访问高价值的系统信息，如凭证。

### 步骤4：数据外泄

如果工作负载在具有特权的容器上运行，攻击者将获得对主机资源的访问权，然后可以执行操作以访问敏感数据并干扰服务。

如果工作负载具有对系统数据库的网络访问权限，攻击者还可以利用这个优势来操纵或外泄有价值的数据。

### 对策

减轻暴露的端点攻击风险的最佳方式是使用漏洞管理工具和流程来识别和修补代码漏洞和[集群配置错误](https://www.armosec.io/blog/kubernetes-misconfigurations/)。

为了在这种情况下减少攻击面，禁用pod配置中的服务帐户自动挂载设置是一种方法。这将阻止服务帐户令牌被挂载到集群中的每个pod，使黑客更难以探测集群并访问其他集群资源。

另一种减轻攻击链的对策是利用防火墙设置[网络策略](https://www.armosec.io/blog/kubernetes-network-policies-best-practices/)，限制主机之间的网络流量。这将防止攻击者探测网络并在集群内进行横向移动。

最后，通过使用 `-anonymous-auth=false` 标志来禁用匿名访问，来确保Kubernetes API服务器和kubelet的安全性。

对API服务器的用户访问应通过外部身份验证方法进行认证，例如内置于托管Kubernetes服务（如AWS EKS或Azure AKS）中的OpenID Connect（OIDC）。

## 攻击路径B：特权升级攻击

特权升级攻击是指攻击者未经授权地访问Kubernetes集群中的特权角色和资源。这可以通过利用集群环境中的安全漏洞实现，包括过于宽松的基于角色的访问控制（RBAC）策略或暴露的pod。

### 攻击链

![](https://www.armosec.io/wp-content/uploads/2023/10/Privilege-escalation-attack-on-an-exposed-pod-with-default-settings-in-a-Kubernetes-cluster-1024x635.png.webp)

*图2： Kubernetes集群中一个带有默认设置的暴露的pod的特权升级攻击*

这个攻击链涉及利用暴露的pod的凭据以在Kubernetes环境中获取更高特权。此场景中的步骤如下。

### 步骤1：侦察

攻击者使用端口扫描器扫描集群网络，查找暴露的pod，并找到一个使用默认服务帐户令牌挂载的暴露的pod。

Kubernetes默认为每个命名空间自动创建一个服务帐户令牌。如果在将pod部署到命名空间时未手动分配服务帐户，则Kubernetes将该命名空间的默认服务帐户令牌分配给该pod。

### 步骤2：利用

黑客渗透了一个使用默认设置的带有服务帐户令牌挂载的暴露的pod。服务帐户令牌为他们提供了通过与令牌相关联的服务帐户访问Kubernetes API服务器的入口。

### 步骤3：横向 & 纵向移动

如果未启用RBAC或与pod相关的RBAC策略过于宽松，攻击者可以使用受损pod的服务帐户创建一个具有管理员权限的新特权容器。

### 步骤4：数据外泄

具有管理员权限的黑客可以创建绑定和群集绑定到cluster-admin ClusterRole或其他特权角色，从而获得对集群中所有资源的访问权。

### 对策

减少攻击面的一个关键方法是使用准入控制器限制集群中过于宽松容器的部署，包括具有特权的容器和挂载包含敏感数据的卷的容器（如Kubernetes secrets和云凭据）。这可以防止特权容器被部署到集群中，使攻击者更难以在集群中保持持久性。

由于在特权升级攻击中通常通过API调用从Kubernetes API服务器检索或生成Kubernetes凭据，因此在配置Kubernetes RBAC策略时应用“最小权限原则”是减轻此风险的关键方法。确保每个用户或服务帐户配置有访问网络资源所需的最小权限，并限制未经授权的用户创建特权角色绑定。

除了实施这些对策之外，定期审查RBAC策略和角色也是很重要的，以确保权限不会漂移。

## 攻击路径C：供应链攻击

针对软件供应链的恶意行为可能涉及利用[容器镜像](https://www.armosec.io/glossary/container-image/)、应用程序依赖关系或在构建和[部署Kubernetes应用程序](https://www.armosec.io/blog/kubernetes-deployment-and-service/)中使用的持续集成和持续交付（[CI/CD](https://www.armosec.io/glossary/ci-cd/)）流水线中的其他组件的漏洞。

### 攻击链

![](https://www.armosec.io/wp-content/uploads/2023/10/Threats-to-the-CICD-pipeline-1024x590.png.webp)

*图3：CI/CD流水线的威胁（来源：美国国防部）*

供应链攻击通常遵循以下步骤。

### 步骤1：侦察

攻击者通过扫描YAML配置文件和转储包含访问Git仓库的密钥的环境变量，获取凭据。

### 步骤2：利用

黑客将恶意镜像放置在公共容器注册表中，或者在良性镜像和基础设施即代码（IaC）配置文件中注入恶意代码；这样一来，他们实际上是在软件供应链中植入了数字木马。

### 步骤3：横向 & 纵向移动

当集群中的应用程序使用受损的镜像时，攻击者可以执行恶意代码执行，访问工作负载可以访问的所有集群资源，如密钥、ConfigMaps、持久卷和网络。

### 步骤4：数据外泄

恶意行为者还可以将计算资源转向非法活动，如加密货币挖矿。

这种类型的攻击非常阴险，因为它利用开发人员对公共库的固有信任，将其变成了入侵的工具。

### 对策

在Kubernetes中减轻供应链攻击的风险涉及在CI/CD流水线的每个阶段保护组件。您可以在Git仓库和容器镜像中使用自动化漏洞扫描，以在部署之前发现和修复漏洞。为了确保镜像的来源并防止在应用程序中意外使用受损镜像，请确保验证镜像签名，以确保使用的是预期的镜像。

在持续部署阶段，使用[Pod安全标准](https://www.armosec.io/glossary/pod-security-standards/)和Pod安全准入，或者使用Open Policy Agent（OPA）和Kyverno等策略引擎，防止部署不符合规范的镜像。这有助于防止在集群中部署恶意应用程序。

## 攻击路径D：开发者凭证盗窃

开发者凭证盗窃是一种网络攻击，黑客窃取开发人员或具有对Kubernetes集群访问权限的DevOps工程师的凭证。这可能使他们能够访问集群及其资源，包括敏感数据和应用程序。

### 攻击链

在这第四种攻击链类型中，黑客通过以下步骤冒充开发人员身份以获取对Kubernetes环境的访问。

### 步骤 1：侦察

在扫描集群网络以寻找暴露的Pod后，恶意行为者发现了一个暴露的Pod。然后，他们利用被入侵的Pod通过kubectl命令探测集群环境中的访问令牌，这些令牌位于Kubernetes配置文件中。如果Kubernetes集群托管在云服务提供商上，攻击者将查询云元数据API以获取云凭据，并访问存储IaC状态文件的S3存储桶，其中可能以明文形式包含敏感信息。

### 步骤 2：利用

他们窃取来自开发人员或DevOps工程师的版本控制系统（例如Git）的访问令牌。

### 步骤 3：横向 & 纵向移动

携带这些凭据，黑客可以冒充开发人员以更改代码并从Git仓库中窃取机密信息，特别是如果使用IaC来管理集群。

### 步骤 4：数据外泄

如果集群使用GitOps，自动从Git中拉取更改，攻击者可以通过Git将恶意工作负载引入集群，导致机密信息和数据的全面泄露。

### 对策

为了降低开发者凭证盗窃的风险，请避免在配置文件中使用明文凭证。此外，使用托管的秘密存储，例如Hashicorp Vault或AWS Secrets Manager，以确保您的机密和凭据得到安全存储。

## 结论

了解针对Kubernetes的常见攻击链对于保护您的环境免受恶意行为者的侵害至关重要。通过保持警惕，实施安全最佳实践，并利用适当的对策，您可以增强防御，确保您的Kubernetes部署的完整性。

保持信息更新，定期更新基础设施，并采用主动的安全立场，以减轻风险并保护您宝贵的工作负载。ARMO平台的[攻击路径功能](https://www.armosec.io/blog/blocking-kubernetes-attack-paths/)使用户能够可视化恶意行为者可利用的弱点。一旦可视化，它突显了攻击路径中的步骤，在这些步骤中可以阻止攻击，并指导工程师进行补救步骤。了解有关[ARMO平台](https://www.armosec.io/platform/)以及它如何在攻击发生之前帮助您阻止攻击的更多信息。

