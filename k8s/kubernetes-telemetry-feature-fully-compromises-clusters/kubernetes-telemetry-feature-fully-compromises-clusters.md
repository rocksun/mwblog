<!--
title: Kubernetes致命“特性”曝光：只读权限即可完全攻陷集群
cover: https://cdn.thenewstack.io/media/2026/01/caa625c8-g_m1g4dwsaaqrq8.png
summary: 安全研究员发现Kubernetes `nodes/proxy GET` 特性存在漏洞，允许只读用户执行特权命令，甚至可摧毁集群。这是预期行为，而非bug。官方建议采用KEP-2862，同时建议用户立即审计RBAC策略并加强Kubelet访问控制。
-->

安全研究员发现Kubernetes `nodes/proxy GET` 特性存在漏洞，允许只读用户执行特权命令，甚至可摧毁集群。这是预期行为，而非bug。官方建议采用KEP-2862，同时建议用户立即审计RBAC策略并加强Kubelet访问控制。

> 译自：[Kubernetes telemetry feature fully compromises clusters](https://thenewstack.io/kubernetes-telemetry-feature-fully-compromises-clusters/)
> 
> 作者：Joab Jackson

如果Kubernetes管理员对即将到来的[Nginx网关截止](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)还没有足够担心的话，他们现在可能需要仔细检查他们的Helm chart，以潜在地阻止一个危险的设置。

安全研究员[Graham Helton](https://grahamhelton.com/)已经[分享了一个Kubernetes漏洞](https://grahamhelton.com/blog/nodes-proxy-rce)，他发现这个漏洞允许一些拥有只读权限的随机用户在集群中的任何pod上运行任意甚至特权命令。

他的诀窍是使用一个具有Kubernetes `nodes/proxy GET` 资源权限的服务账户，该资源被数十个监控工具使用，并提供了执行特权级别pod命令的权限。

换句话说，这是一个特性，而不是一个bug。

## 按预期工作

Helton最初在11月通过[Kubernetes bug赏金计划](https://x.com/GrahamHelton3/status/2015789987799667097)将这个奇怪的现象报告为一个bug。该问题很快被标记为已关闭，并被标记为“预期行为”。

`nodes/proxy GET` 调用旨在用于服务账户，并被许多监控工具使用。

一个GET请求如何转化为完全的远程代码执行，[是因为Websockets与Kublet的授权逻辑之间存在不匹配](https://x.com/GrahamHelton3/status/2015789990429487294)。

Helton发现了69个使用`nodes/proxy GET`的工具的Helm chart。对于它们来说，这提供了访问节点内部API以获取所需数据的权限。

Helton在[X上写道](https://x.com/GrahamHelton3/status/2015789990429487294)：“世界上一些最大的Kubernetes供应商都依赖它，因为没有普遍可用的替代方案。”

因此，`nodes/proxy Get`行为没有[CVE警报](https://thenewstack.io/why-the-value-of-cve-mitigation-outweighs-the-costs/)，因为它不是一个漏洞。

官方的解决方案是使用[KEP-2862](https://github.com/kubernetes/enhancements/issues/2862)（“细粒度Kubelet API授权”），这是一个预计在即将于四月发布的Kubernetes 1.36版本中提供的扩展。

## 如何摧毁一个Kubernetes集群

因此，如果你有一个订阅了`nodes/proxy GET`的服务账户，并且可以访问端口10250上的节点Kubelet，那么你就可以自由地向`/exec`端点发出任何命令，包括可能完全摧毁集群的特权系统pod命令。

[根据Helton的说法](https://x.com/GrahamHelton3/status/2015789990429487294)，你还可以做其他一些事情：窃取其他pod的服务账户令牌，或在控制平面pod中执行代码。

更糟糕的是，不会留下此类恶意行为的记录，因为Helton解释说：“Kubernetes AuditPolicy不会记录通过直接连接到Kubelet API执行的命令。”

以下是使这一切成为可能的集群权限设置：

```

 # Vulnerable ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
name: nodes-proxy-reader
rules:
- apiGroups: [""] \
resources: ["nodes/proxy"]
verbs: ["get"]
```

如果你想亲自尝试，Helton[发布了一个完整的实验](https://labs.iximiuz.com/tutorials/nodes-proxy-rce-c9e436a9)。

## 应该采取哪些预防措施？

对于拥有这些系统设置的人来说，可能需要提出一些尖锐的问题：你更看重你的可观测性还是你的安全性？

行业观察家Alex Ellis[称这次披露](https://x.com/alexellisuk/status/2016096083168915636)“令人担忧”。

云原生安全公司Edera的现场首席技术官Jed Salazar指出，这个漏洞指出了Kubernetes工作负载在2026年与2016年的不同之处。

它们不再仅仅是无状态应用程序。他写道，它们是“带有专有模型权重的人工智能训练管道、金融交易系统和包含患者数据的医疗保健应用程序”。“2026年监控堆栈受损的爆炸半径与2016年截然不同。”

Salazar写道，解决方案是架构隔离，这正是[Edera提供的](https://thenewstack.io/kubecon-eu-2025-edera-protect-offers-a-secure-container/)（Salazar指出，这种配置没有让Edera用户容易受到攻击）。

对于其他人，在KEP-2862完全投入生产之前，Salazar建议采取以下预防措施：

1. *立即审计你的RBAC策略中nodes/proxy权限,*
2. *考虑监控工具是否真正需要直接访问kubelet,*
3. *实施网络策略，限制对kubelet端口10250的访问,*
4. *计划在KEP-2862细粒度权限正式发布后迁移,*
5. *采用工作负载隔离技术，无论上游决策如何，都能限制爆炸半径。*