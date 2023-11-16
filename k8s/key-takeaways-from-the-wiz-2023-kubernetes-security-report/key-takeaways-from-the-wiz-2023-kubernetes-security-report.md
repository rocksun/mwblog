<!-- 
# Wiz 2023年Kubernetes安全报告的关键要点
https://www.datocms-assets.com/75231/1699451961-k8s-report-blog-cover.png?dpr=0.5&fm=webp
 -->

Wiz最近发布了其2023年Kubernetes安全报告，重点介绍几个关键要点。

译自 [Key takeaways from the Wiz 2023 Kubernetes Security Report](https://www.wiz.io/blog/key-takeaways-from-the-wiz-2023-kubernetes-security-report) 。

Kubernetes(K8s)改变了云原生应用部署和管理方式，但管理相关环境(特别是安全方面)的信息仍不足。

Wiz对**超过20万云账户的扫描基础上**发布的2023年Kubernetes安全报告，揭示了Kubernetes集群的安全现状，将安全风险与集群攻击链的不同阶段(从初始访问到影响)关联。研究发现，尽管Kubernetes环境对攻击者十分诱人(入侵尝试也在增多)，但总体容器安全成熟度仍较低。下文将讨论原因及改进建议。

报告还确定了云环境中最薄弱环节，提出“区域防守”策略进行有效缓解。

## Kubernetes环境成为主要攻击目标

**Wiz实验显示，新创建的Kubernetes集群仅22分钟就开始受到恶意扫描。**

[Shodan](https://trends.shodan.io/)数据显示K8s日益流行，公共K8s API服务器数量上升:

![Public Kubernetes API server endpoints](https://www.datocms-assets.com/75231/1699470355-kubernetes-adoption-continues-to-soar.png?fm=webp)

*Public Kubernetes API server endpoints*

但随Kubernetes采用增加，安全风险也在增长。下图显示本不该外部可访问的开放kubelet端点:

![](https://www.datocms-assets.com/75231/1699470300-public-kubelet-endpoints-are-also-on-the-rise.png?fm=webp)

*Public Kubelet endpoints*

不仅Kubernetes安全风险增加，攻击也在增多。K8s集群高效，适合运行加密挖矿工作负载，[PyLoose](https://www.wiz.io/blog/pyloose-first-python-based-fileless-attack-on-cloud-workloads)、[newhello](https://www.wiz.io/blog/cryptojacking-attacks-summer-2023)等攻击案例即为证明。成熟挖矿软件如XMRig、CCMiner、XMR-Stak-RX也日益转至Kubernetes基础设施。攻击者也变得更擅长从K8s集群横向移动至云环境。例如，[RBAC Buster](https://blog.aquasec.com/leveraging-kubernetes-rbac-to-backdoor-clusters)最初通过匿名访问方式接触K8s API服务器，之后尝试窃取AWS凭据进一步渗透云基础设施。部分攻击不仅停留在加密挖矿，还窃取知识产权。

Kubernetes基础设施受到更多恶意关注的进一步证据是，新创建集群很快成为攻击目标。Wiz威胁研究实验显示，新创建的GKE集群3小时内开始受到互联网恶意扫描。AKS集群约2小时13分钟，EKS集群仅22分钟。数据明确显示Kubernetes正在成为核心攻击目标。

![](https://www.datocms-assets.com/75231/1699470366-from-exposure-to-discovery-how-long-does-it-take-for-a-newly-created-cluster-to-get-malicious-scans.png?fm=webp)

*从暴露到发现: 新创建的集群需要多长时间才会受到恶意扫描?*

## 容器安全成熟度较低

**仅9%的集群使用网络策略进行内部流量隔离。**

面对Kubernetes安全风险，安全社区提出各种控制、功能和设计决策以提高托管及本地集群的安全性。但我们发现，尽管有各种安全选项，普遍的安全控制采用仍在落后。下表显示主要安全功能的使用和采用情况:

![](https://www.datocms-assets.com/75231/1699470374-despite-rise-in-attacks-k8-native-security-controls-usage-remains-low.png?fm=webp)

*K8 native security controls usage*

## 问题不在于安全选项缺乏，而在于采用不足。

多层防御是挫败潜在攻击的最佳方式。

如果将观察结果映射到典型Kubernetes攻击链，可以找出生态系统最薄弱环节。结论是，攻击者一旦进入环境，就没有太多阻碍。从风险角度，我们观察到以下趋势:

- 攻击者最不可能通过控制平面获得初始访问，相关配置错误或漏洞较少。数据平面漏洞提供更多初始访问机会。
- 一旦获得初始访问，集群内横向移动和提权机会充裕。
- 防御最后一道关口 - 影响的安全实践不足，特别是云环境，有太多途径可横向移动至云。随Kubernetes与云环境融合加深，这些途径还会增加。
- 最糟糕的是，现有跨阶段安全控制使用不足。这表明安全社区需要优先推广控制采用，而不是推出新的控制。

## 关键要点——区域防守策略

作为K8s集群运维，我们无法控制攻击增加，但可以做好准备。这是报告的出发点。参考篮球比喻，我们提出区域防守策略。每个防守球员守住给定区域，而不是人盯人。我们建议:

- 持续扫描外部暴露和面向外部的安全态势 - 保护初始访问。
- 检测和修复关键漏洞:公开暴露的pod和服务 - 保护初始访问，减小数据平面攻击面; 集群频繁更新 - 减小控制平面攻击面。
- 运行时保护 - 检测恶意执行以防突破初始防线。
- 积极采用集群内部隔离控制，首要是Pod安全标准，以及合理的基于命名空间的隔离、RBAC、网络策略和用户命名空间 - 防止横向移动。
- 持续检查K8s工作负载的IAM和RBAC卫生状况 - 限制命名空间/集群级别潜在影响，防止扩散至更广云环境。

[这里](https://www.wiz.io/lp/the-2023-kubernetes-security-report)下载完整报告。