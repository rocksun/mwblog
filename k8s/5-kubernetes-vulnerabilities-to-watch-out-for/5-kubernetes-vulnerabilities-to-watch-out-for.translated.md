# 需要注意的 5 个 Kubernetes 漏洞

![Featued image for: 5 Kubernetes Vulnerabilities To Watch Out For](https://cdn.thenewstack.io/media/2025/04/8f48446f-kubernetes-vulns-2025-1024x576.jpg)

Kubernetes 最近在安全性方面度过了艰难的一周，因为 [CVE-2025-1974](https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/) 于 3 月 24 日曝光。 鉴于您可能已经在认真考虑 [Kubernetes 安全性](https://thenewstack.io/kubernetes-security-report-evolving-landscape-of-devsecops)，我们认为应该快速浏览一下您应该注意的其他一些漏洞，并简要介绍如何防止它们破坏您的一周。

Kubernetes 安全性是独立存在的——Kubernetes 平台涉及许多需要保护的层。 容器打包能够托管几乎无限的语言、框架和商用现成软件的组合。 这就是为什么 Kubernetes 原生的安全工具是完整 [Kubernetes 安全性](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes) 图景的关键。

以下是在运行 Kubernetes 集群时需要注意的五个漏洞，以及有关如何减轻其影响的一些信息。

## Struts

[CVE-2024-53677](https://nvd.nist.gov/vuln/detail/CVE-2024-53677)

现在的孩子们使用 React 框架、npm 仓库和无休止的事件驱动网站。 早在 2000 年代初，我们甚至没有一个统一兼容的 [JavaScript](https://roadmap.sh/javascript) 来称之为 JavaScript！ 我们有 Java，而且我们喜欢它！

当然，20 年后，[Java](https://roadmap.sh/java) 仍然是企业员工的主力军。 有一个适用于所有内容的库，而且 Java Web 资产往往相对稳定且不令人兴奋，而不是经历持续的更新和框架重构。 坦率地说，不令人兴奋是件好事。

除非“不令人兴奋”意味着一个恶意的远程代码执行攻击在雷达下进行。 这一次以前也出现过。 事实上：2024 年 12 月发现了大型 [Struts](https://struts.apache.org/) 漏洞中的第二个。 这次，通过使用路径遍历攻击，它使恶意行为者能够在受限位置上传或保存文件，从而允许他们使用远程代码执行。

如此稳定、古老且坦率地说很无聊的东西正是最恶劣的漏洞发生的地方。 每个人都期望一个热门的新 Web 框架存在错误，但是过去 10 年中以 0.0.1 版本缓慢增长的项目可能是逆向工程师最感兴趣的目标，而 Struts 似乎是不断给予的礼物。 希望它已经完成了赠送礼物。

## XZ Utils

[CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094)

检测供应链攻击非常困难。 如果社会工程师愿意花费数年时间赢得整个开源社区的信任呢？ 这正是 XZ utils 发生的事情，并且该攻击是通过对流程和代码审查的勤奋和奉献精神发现的。

XZ utils 是那些倾向于被塞进容器中以支持 xz 文件压缩和解压缩的依赖项之一。 因此，如果开发人员试图从每个压缩文件中挤出额外的空间，他们可能会选择 xz 而不是 .zip。

如果他们这样做了，现在他们必须将 XZ utils 包含在其二进制文件中，这使其成为试图破坏下游项目和站点整个生态系统的人的诱人目标。

一旦在 XZ utils 5.6 和 5.6.1 版本中检测到该漏洞，这些版本将在使用 Red Hat Advanced Cluster Security for Kubernetes (RHACS) 等工具扫描的所有容器中标记。 用户可以使用 RHACS 策略来防止具有此漏洞的容器的准入，并识别运行时已部署的容器。

## openSSH Server

[CVE-2024-6387](https://www.qualys.com/regresshion-cve-2024-6387/#:~:text=regreSSHion%2C%20CVE%2D2024%2D6387,poses%20a%20significant%20exploit%20risk.)

每当 SSH 的任何实现中存在漏洞时，天都要塌下来了。 没有哪个应用程序提供比安全外壳更大的访问权限，也没有哪个应用程序提供比安全外壳更密切的与主机的连接。

只需考虑所有令人惊叹的工具，它们实际上只是打开一个 SSH 连接并将数据喷射到其中：[rsync](https://en.wikipedia.org/wiki/Rsync)、[Ansible](https://www.redhat.com/en/technologies/management/ansible)、[sshuttle](https://github.com/sshuttle/sshuttle)。 SSH 是进入不在您面前的计算机的最基本方式。 在我们拥有 SSH 之前，我们有 Telnet，并且数据包嗅探蓬勃发展。
如今，Telnet连接已加密，并在全球范围内被认为是安全的。直到天塌下来。最近，由于OpenSSH客户端上存在缺陷的DNS主机密钥检查，中间人攻击可能允许某人在客户端上模拟服务器。

这是一个非常具体的攻击，仅当客户端将VerifyHostKeyDNS设置为“yes”或“ask”时才有效，但该漏洞似乎自2023年8月以来就已存在。幸运的是，现在已经知道了，并且可以标记，以防您的任何容器包含易受攻击的OpenSSH版本。此外，由于SSH实际上不属于容器，因此您可以阻止包含SSH的容器镜像被部署，从而从一开始就消除了攻击媒介。

## /debug/pprof

[CVE-2019-11248](https://github.com/kubernetes/kubernetes/issues/81023)

由于服务级别协议（SLA），平台漏洞非常棘手。在按照承诺交付服务的同时，保持开源软件包的更新可能会使安全性成为一场艰巨的、永无止境的竞赛。如果漏洞包含在支持和故障排除工具中，情况会更糟。CVE-2019-11248本质上是一个悬空的端点，通过未经身份验证的[Kubelet healthz端口](https://kubernetes.io/docs/reference/using-api/health-checks/)打开。聪明的攻击者可以使用此调试端点来提取敏感的集群信息以供非法使用。什么样的敏感信息？哦，只是内存地址和配置详细信息。

这里真正的危险在于忘记在部署到生产环境之前从集群或容器中删除调试工具。考虑到挖掘集群日志以查找错误源是多么复杂，这完全可以理解。

扫描API访问的工具会警告异常或未经授权的活动。攻击者对此特定漏洞的使用将触发警报，使管理员能够快速响应并最大程度地减少利用可能造成的损害。总体目标是完全删除这些类型的工具，如果不能完全删除，则设置防护栏以防止此类工具进入生产环境。

## Kubernetes Image Builder

[CVE-2024-9594](https://github.com/kubernetes/kubernetes/issues/128007)

有时，仅仅构建容器镜像就会导致问题。但也许不是你期望的方式。2024年，在Kubernetes Image Builder中发现了CVE-2024-9594，它用于构建虚拟机镜像。对于Kubernetes Image Builder 0.1.37及更早版本，在使用QEMU、OVA或Nutanix等原始提供程序时，在镜像构建过程中启用了默认用户凭据。这意味着当用户使用此工具构建镜像时，有人可以使用此信息登录到集群以获得root权限。幸运的是，此问题并未影响某些Kubernetes发行版，包括Red Hat OpenShift，它使用[Source-To-Image](https://github.com/openshift/source-to-image)代替，该漏洞不受影响。

这种类型的漏洞实际上是一个非常古老的难题，尽管它在这里的出现非常独特。这个“如果用户正在使用X，系统易受攻击”的较早示例来自古老的UNIX系统：在90年代中期的AIX（IBM的UNIX）版本中，如果root用户正在Elm电子邮件客户端中阅读邮件，则任何用户也可以访问和阅读root用户邮件目录中的任何内容。不幸的是，IBM在1996年吸取了教训。

## 旧漏洞永不消亡

这表明旧的漏洞模式永远不会消亡，它们只是在新实现、语言和环境中表现出来。这就是为什么安全工具需要与平台原生集成，在进程和Kubernetes对象之间提供关联，以便Kubernetes管理员和应用程序开发人员可以理解安全发现。仅仅收集下面的大量进程、软件和容器镜像是不够的。

然而，强大的安全性对于团队来说等同于出色的开发环境。如果您的程序员不必担心他们正在使用的软件中的主要安全问题，因为该软件受到监控、测量和祝福；那么这些开发人员可以专注于解决他们面前的问题，而不是每隔几周重构以删除易受攻击的代码。

*了解更多关于用于Kubernetes的Red Hat Advanced Cluster Security的信息。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的YouTube
频道以流式传输我们所有的播客、访谈、演示等。