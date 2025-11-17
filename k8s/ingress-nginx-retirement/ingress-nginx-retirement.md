
<!--
title: Ingress NGINX 退役：你需要知道的一切
cover: 
summary: Ingress NGINX因安全优先及维护挑战将于2026年3月退役。现有部署仍可用，但不再更新。建议迁移至Gateway API或其他Ingress控制器。
-->

Ingress NGINX因安全优先及维护挑战将于2026年3月退役。现有部署仍可用，但不再更新。建议迁移至Gateway API或其他Ingress控制器。

> 译自：[Ingress NGINX Retirement: What You Need to Know](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/)
> 
> 作者：Tabitha Sable (Kubernetes SRC)

为了优先保障生态系统的安全，Kubernetes SIG Network 和安全响应委员会宣布 [Ingress NGINX](https://github.com/kubernetes/ingress-nginx/) 即将退役。尽力维护将持续到 2026 年 3 月。此后，将不再发布新版本、修复错误，也不再更新以解决任何可能发现的安全漏洞。**现有的 Ingress NGINX 部署将继续运行，安装工件将保持可用。**

我们建议迁移到众多替代方案之一。请考虑[迁移到 Gateway API](https://gateway-api.sigs.k8s.io/guides/)，它是 Ingress 的现代替代方案。如果您必须继续使用 Ingress，Kubernetes 文档中[列出了许多替代的 Ingress 控制器](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)。请继续阅读，以获取关于 Ingress NGINX 的历史、现状以及后续步骤的更多信息。

## 关于 Ingress NGINX

[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) 是最初的、用户友好的方式，用于将网络流量导向在 Kubernetes 上运行的工作负载。（[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) 是一种实现许多相同目标的新方法。）为了使 Ingress 在您的集群中工作，必须运行一个 [Ingress 控制器](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)。有许多 Ingress 控制器可供选择，它们服务于不同用户和用例的需求。有些是云提供商特定，而另一些则更具通用适用性。

[Ingress NGINX](https://www.github.com/kubernetes/ingress-nginx) 曾是一个 Ingress 控制器，在 Kubernetes 项目早期作为 API 的一个示例实现而开发。其巨大的灵活性、广泛的功能以及不依赖于任何特定云或基础设施提供商的特性，使其变得非常受欢迎。自那时起，社区团体和云原生供应商在 Kubernetes 项目中创建了许多其他 Ingress 控制器。Ingress NGINX 继续是最受欢迎的控制器之一，被部署在许多托管 Kubernetes 平台中以及无数独立用户的集群内。

## 历史与挑战

Ingress NGINX 的广度和灵活性带来了维护挑战。对云原生软件不断变化的期望也增加了复杂性。曾经被认为是“有用”的选项有时却被视为严重的安全缺陷，例如通过“snippets”注解添加任意 NGINX 配置指令的能力。昨天的灵活性已成为今天无法克服的技术债务。

尽管该项目在用户中很受欢迎，但 Ingress NGINX 始终面临维护人员不足或勉强够用的困境。多年来，该项目只有一两个人利用自己的业余时间，在工作之余和周末进行开发工作。去年，Ingress NGINX 维护者[宣布](https://kccncna2024.sched.com/event/1hoxW/securing-the-future-of-ingress-nginx-james-strong-isovalent-marco-ebert-giant-swarm)了他们将逐步停止 Ingress NGINX 并与 Gateway API 社区共同开发一个替代控制器的计划。不幸的是，即使是那次宣布也未能引起更多人对维护 Ingress NGINX 或开发 InGate 来替代它的兴趣。(InGate 的开发从未达到足以创建成熟替代方案的程度；它也将被退役。)

## 现状与后续步骤

目前，Ingress NGINX 正在接受尽力维护。SIG Network 和安全响应委员会已经竭尽全力寻找更多支持以使 Ingress NGINX 可持续发展。为了优先考虑用户安全，我们必须让该项目退役。

Ingress NGINX 的维护将于 2026 年 3 月停止，该项目将被[退役](https://github.com/kubernetes-retired/)。此后，将不再发布新版本、修复错误，也不再更新以解决任何可能发现的安全漏洞。GitHub 仓库将变为只读并保留以供参考。

现有的 Ingress NGINX 部署不会受到影响。现有的项目工件，如 Helm Chart 和容器镜像，将保持可用。

在大多数情况下，您可以通过使用集群管理员权限运行 `kubectl get pods \--all-namespaces \--selector app.kubernetes.io/name=ingress-nginx` 来检查您是否正在使用 Ingress NGINX。

我们要感谢 Ingress NGINX 维护者在创建和维护该项目方面所做的工作——他们的奉献精神令人印象深刻。这个 Ingress 控制器在全球的数据中心和家庭实验室中处理了数十亿的请求。在许多方面，如果没有 Ingress NGINX，Kubernetes 就不会有今天的成就，我们感谢多年来付出的巨大努力。

**SIG Network 和安全响应委员会建议所有 Ingress NGINX 用户立即开始迁移到 Gateway API 或其他 Ingress 控制器。** Kubernetes 文档中列出了许多选项：[Gateway API](https://gateway-api.sigs.k8s.io/guides/)，[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)。您合作的供应商也可能提供其他选项。