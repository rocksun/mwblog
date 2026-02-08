我们警告过你！

今天，[Ingress NGINX](https://github.com/kubernetes/ingress-nginx)仍被[50%的Kubernetes用户](https://isovalent.com/blog/post/state-of-kubernetes-networking-report-2025/)用于管理传入流量，但[它早已被计划退役](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)。我们警告过你，但你听了吗？没有。Reddit的一项调查显示，消息公布后，[仍有44%的用户在使用它](https://www.reddit.com/r/kubernetes/comments/1ox4doz/results_of_what_ingress_controller_are_you_using/)！

哇。说真的，你们是受虐狂吗？因为我不得不告诉你，Kubernetes指导和安全响应委员会于1月29日宣布：“到2026年3月，Kubernetes将退役Ingress NGINX。”

那么，你能在接下来的两个月内部署一个Ingress NGINX的替代品吗？或者，就像那些[仍在运行CentOS Linux](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/)的人一样，它已于2024年6月30日终止支持，你还会继续运行它，并抱有一线希望，认为没有人会利用它吗？

请注意，[Chainguard仍将通过其EmeritOSS计划支持Ingress NGINX](https://thenewstack.io/chainguard-emeritoss-backs-minio-other-orphaned-projects/)，所以这是一种选择。如果这是你的计划，你应该尽快与[Chainguard](https://www.chainguard.dev/)联系。

然而，请记住，正如Kubernetes指导委员会（KSC）所说，“项目退役后，将不再有任何版本错误修复、安全补丁或任何形式的更新。”

![](https://cdn.thenewstack.io/media/2026/02/d92f5a9c-kubernetes-ingress.png)

Kubernetes Ingress的工作原理（图片来源：CNCF）。

## 安全隐患

你还应该记住，首先，如果你正在使用Ingress NGINX，它是你Kubernetes部署的核心。其次，该程序一直容易出现安全漏洞，例如“IngressNightmare。”2025年3月发现的这组五个漏洞中，有一个安全漏洞，正如安全公司[Datadog](https://www.datadoghq.com/)所说，应“被视为五个漏洞中最严重的一个，并被分配了9.8的CVSS评分（危急）。当它与一个较低严重性的漏洞链式利用时，可以导致未经身份验证的远程代码执行。”

你希望独自面对这种问题吗？我想不是！

更糟糕的是，KSC警告说：“现有部署将继续运行，因此除非你主动检查，否则你可能不知道你受到了影响，直到你被入侵。”简而言之，你不知道的事情可能会伤害你。而且会严重伤害你！

## 为何退役Ingress NGINX？

那么，如果Ingress NGINX对如此多的Kubernetes部署至关重要，KSC为何要将其淘汰呢？好吧，没有人站出来支持这个项目。

开源项目最初是为了解决某个痛点而开始的，但那些最终被数万人使用的项目需要支持。它们需要资金、程序员和维护者。猜猜这个任务关键型项目临近结束时有多少维护者。尽管猜。

那是一个，偶尔两个。正如KSC所写：“它一直由一两个人利用业余时间独自维护。如果没有足够的人员来维护该工具达到我们和用户都认为安全的标准，那么负责任的选择就是逐步淘汰它，并将精力重新集中在像[Gateway API](https://gateway-api.sigs.k8s.io/guides/getting-started/)这样的现代替代方案上。”

KSC成员继续说道：“非常明确地说：在Ingress NGINX退役后选择继续使用它，会让你和你的用户面临攻击。”明白了吗？

如果你很快发现自己因试图独自维护该程序或切换到另一个程序而感到压力——顺便说一句，Ingress NGINX没有直接的替代品——你只能怪自己。

现在没有人能骑着白马来拯救吗？不。KSC已经忍无可忍。“我们做出这个决定并非轻率；尽管现在不便，但为了所有用户和整个生态系统的安全，这样做是必要的。不幸的是，Ingress NGINX最初设计的灵活性曾是一个福音，现在却变成了一个无法解决的负担。随着技术债务的堆积，以及加剧安全漏洞的基本设计决策，即使有资源，继续维护该工具也不再合理甚至不可能。”

祝你好运。你会需要的。