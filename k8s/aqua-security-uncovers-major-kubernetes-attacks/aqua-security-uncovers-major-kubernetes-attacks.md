# Aqua Security 揭示了重大的 Kubernetes 攻击事件

愚蠢的 Kubernetes 错误配置继续导致重大的安全问题。

翻译自 [Aqua Security Uncovers Major Kubernetes Attacks](https://thenewstack.io/aqua-security-uncovers-major-kubernetes-attacks/) 。

![](https://cdn.thenewstack.io/media/2023/08/d95fd20c-pawel-czerwinski-og-fruqoi3g-unsplash-e1691530187422-1024x683.jpg)

[Aqua Security](https://www.aquasec.com/)，一家领先的云原生安全机构，经过其研究团队 Aqua Nautilus 三个月的调查，揭示了令人震惊的发现。该研究显示，包括财富 500 强公司、开源项目和个人在内的 350 多个实体的 Kubernetes 集群暴露且容易受攻击。

令人难以置信的是，经过检查的集群中有高达 60% 已被入侵，恶意软件和后门已被积极部署。这些漏洞源于两个主要的配置错误，凸显了已知和被忽视的配置错误的危险性。

## 错误的手

Aqua Nautilus 的首席威胁情报分析师 [Assaf Morag](https://blog.aquasec.com/author/assaf-morag) 强调了情况的严重性，他说：“公司 Kubernetes 集群落入错误的人手中可能意味着灭亡。从专有代码、客户数据、财务记录到加密密钥，一切都面临风险。”

例如，Aqua 发现 Kubernetes 集群通常是组织的软件开发生命周期（SDLC）的一部分。因此，Kubernetes 集群还可以访问源代码管理（SCM）、持续集成/持续部署（CI/CD）、registry 和云服务提供商。简而言之，应有尽有。

由于 Kubernetes 已成为管理容器的默认平台，许多企业使用它来高效地管理容器化的应用程序。现在，只要他们知道如何保护它就好了！Morag 补充说：“尽管有诸如 [Aqua 的软件供应链安全套件](https://www.aquasec.com/products/software-supply-chain-security/)等 Kubernetes 安全工具，但在所有组织规模中，配置错误仍然猖獗。这些漏洞可能造成的损害是巨大的。”

你认为呢？

## 漠不关心？

那么，受到侵害的团体对所有这些问题有何反应？受影响的集群所有者最初的回应是漠不关心。许多人将被入侵的集群视为简单的“测试环境”。Denial 不仅仅是埃及的一条河。

他们应该关心。三个不同的加密货币挖掘运营商主要是使用被入侵的 Kubernetes 集群。它们分别是 TeamTNT 的 Silentbob 攻击、基于角色的访问控制 [（RBAC）Buster 攻击](https://blog.aquasec.com/leveraging-kubernetes-rbac-to-backdoor-clusters)，以及另一个 [Dero 攻击](https://www.crowdstrike.com/blog/crowdstrike-discovers-first-ever-dero-cryptojacking-campaign-targeting-kubernetes/)。也许你的企业可以承担挥霍计算资源来挖掘加密货币。我的不能。

那么，[这些加密货币挖掘者是如何闯入的呢？](https://blog.aquasec.com/kubernetes-exposed-one-yaml-away-from-disaster)

首当其冲的是，集群对未经身份验证的请求通常是默认启用的。这意味着任何人都可以发送请求并从 Kubernetes 集群获得响应。大多数云提供商的 API 服务器的默认配置是可以被任何人通过互联网访问。

好吧，这很糟糕，但并不是无法解决的问题。然而，由于任何人都可以从 API 服务器获得答案，这意味着他们可以列出存储在分布式密钥存储 etcd 中的所有 secrets 。如果将 secrets 包含在环境变量中，例如链接到其他环境和 secrets ，或者包括 Docker Hub、云服务提供商、GitHub、GitLab、Bitbucket 等等的凭据。如果以这种方式存储秘密，应该阻止匿名用户访问您的集群。

一般来说，匿名用户没有其他权限。但是太多的管理员给了匿名用户权限。不要问我为什么。这只会带来麻烦。

Aqua 报告中提到了“在某些情况下，从业人员将匿名用户角色与其他角色绑定在一起，通常是管理员角色。从那时起，攻击者非法访问 Kubernetes 集群只有一个很短的步骤。因此，这“离灾难只有一个 YAML 文件之遥。”

另一个常见的配置错误是如何设置 “kubectl proxy” 命令。当你运行 “kubectl proxy” 时，你正在将经过授权和身份验证的请求转发给 API 服务器。

因此，例如，当您使用以下标志运行相同的命令“--address=`0.0.0.0` --accept-hosts `.*`” 时，您的工作站代理将现在侦听并将经过授权和身份验证的请求从任何具有对工作站的 HTTP 访问权限的主机转发给 API 服务器。请注意，特权与运行 “kubectl proxy” 命令的用户的特权相同。糟糕。

那么你能做什么呢？加固您的系统。具体来说，Aqua Nautilus 建议使用本地的 Kubernetes 功能，如 RBAC 和准入控制策略，以增强安全性。定期审计以及像 Aqua Trivy、Aqua Tracee 和 Kube-Hunter 这样的开源工具可以帮助实时检测和预防威胁。

实际上，这都是相当简单、直接的安全措施。不幸的是，我们中有太多人仍然忽视基本的安全常识。Aqua 提醒我们，我们不能忽视它。

