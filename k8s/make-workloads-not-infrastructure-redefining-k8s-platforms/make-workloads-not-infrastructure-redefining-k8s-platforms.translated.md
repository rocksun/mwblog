# 不用构建基础设施，构建工作负载：重新定义 K8s 平台

![Featued image for: Make Workloads, Not Infrastructure: Redefining K8s Platforms](https://cdn.thenewstack.io/media/2024/10/157865ae-redefiningkubernetesplatforms-1024x576.jpg)

正如 [Kelsey Hightower](https://www.linkedin.com/in/kelsey-hightower-849b342b1/) 在 2017 年所说，[Kubernetes 是一个用于构建平台的平台](https://opensource.com/article/18/1/kelsey-hightower-kubernetes-community)。Kubernetes 是为运维人员设计的，而不是为开发人员设计的。获取一个大型云托管的 Kubernetes 版本肯定会让你的运维团队感到高兴，但它也可能让你的开发团队感到不满。原因是 [Kubernetes](https://roadmap.sh/kubernetes) 不是开发人员需要的平台。它是一套复杂的原语，与他们的主要目标不一致：构建应用程序。

平台的定义在于你是否能够在其上构建。如果你是一名 [平台工程师](https://thenewstack.io/platform-engineering/)，Kubernetes 确实是一个平台。你可以在它之上构建你需要的任何东西。如果你是一名应用程序开发人员，Kubernetes 会让你感到不知所措。如果你是一名平台工程师，它也会让你感到不知所措！这可能是为什么许多基于 Kubernetes 构建的 [内部开发平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) (IDP) 项目会偏离轨道并被重新构建。尽管 Kubernetes 做了很多好事，但我们仍然缺乏一个开发人员喜欢的提交后平台。

让运维和开发都满意的目标是其他平台一直在努力解决的问题。随着我们进入 [KubeCon Salt Lake City 2024](https://thenewstack.io/event/kubecon-cloudnativecon-north-america/)，让我们重新审视它以及导致 Kubernetes 的其他一些平台。

## 寻找 Rails 时刻

在 2019 年，[Bryan Liles](https://www.linkedin.com/in/bryanliles/) 在 KubeCon 上发表了主题演讲“[寻找 Kubernetes 的‘Rails’ 时刻](https://www.youtube.com/watch?v=ZqQTEdHVaCw)”。他大胆地指出 [YAML 确实很糟糕](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/)。在 Kubernetes 世界中，YAML 清单意味着满屏的未定义字段和令人眼花缭乱的任务。这与 `rails new blog` 的体验相去甚远。换句话说，YAML 对应用程序开发人员来说是错误的抽象。

Ruby on Rails 是一个在 [LAMP](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/) (Linux、Apache、MySQL 和 PHP) 成为主导堆栈的时代构建的平台。与 Kubernetes 一样，LAMP 的问题在于如何让软件工程师能够使用它。

如今，Kubernetes 感觉就像 LAMP 中的 L。Linux 和 Kubernetes 都是其他组件构建其上的平台。Linux 绝对是一个操作系统 (OS)，而 Kubernetes 是云的操作系统。很难想象一个应用程序开发人员会处理内核级别的 Linux API。但在 Kubernetes 中，处理是现状。

平台工程师需要一个平台，它不仅可以抽象掉复杂性，还可以让开发人员专注于编写他们获得报酬的代码。

## Cloud Foundry 几乎成为了平台

Pivotal 的 [Cloud Foundry](https://www.cloudfoundry.org/?utm_content=inline+mention) (PCF) 是早期尝试提供一个复杂的平台即服务。他们准确地把握了简化应用程序部署和实现“你构建它，你运行它”理念的愿景。PCF 拥有像 Rails 一样的简单入门；不是 `rails blog new`，而是 `cf push`。体验感觉相似，但 Cloud Foundry 做出的重大飞跃是支持几乎所有语言和框架（不仅仅是 Ruby）。开发人员只需要提交他们的代码。PCF 是推动所有提交后操作的因素。

然而，该平台仍然需要大型团队来维护和运营，同时还需要大量的硬件投资，这些投资需要几个月才能完成。由于采用 PCF 所需的努力，它并没有完全发挥其潜力，也没有足够快地适应云原生时代。还记得 Kubernetes 缺少的部分是良好的开发人员体验吗？Cloud Foundry 缺少的部分是适应性和愉快的运维体验。

云原生生态系统更加健壮，问题规模也更大，考虑到与十年前相比，现在有更多软件工程师在交付工作负载——付出了相当大的努力，有时甚至不成功。

Cloud Foundry 在 2010 年代初崛起，与 Apache Mesos 处于同一时期。Mesos 与 PCF 处于光谱的另一端。它非常注重运维体验，但从未找到立足点。Heroku 来自同一时期，但专注于开发人员体验，同时隐藏了运维方面。

## Kubernetes 成为云的操作系统
当 Kubernetes 崛起时，其成功部分归功于其灵活性。Kubernetes 比其他平台更成功的原因有很多。K8s 为云提供了标准 API，它是声明式的，并且其对容器的关注很好地抽象了虚拟机 (VM)。Kubernetes 成功的另一个原因是其组件可以互换。例如，[K3s](https://k3s.io/) 发行版用更传统的关联数据库替换了 [etcd](https://thenewstack.io/about-etcd-the-distributed-key-value-store-used-for-kubernetes-googles-cluster-container-manager/)。

[Amazon](https://aws.amazon.com/?utm_content=inline+mention) Elastic Kubernetes Service (EKS)、[Google](https://cloud.google.com/?utm_content=inline+mention) Kubernetes Service (GKS) 和 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Kubernetes Service (AKS) 的出现巩固了 Kubernetes 作为云的最终操作系统的定位——每个都有自己的特点和挑战。

值得记住的是，应用程序抽象仍然是平台构建者留下的任务。原因显而易见。您希望如何将代码从开发环境迁移到生产环境？每个团队和组织都会以略微不同的方式进行操作。在回忆“Kubernetes 是一个用于构建平台的平台”这句话时，这是一个需要牢记的重要细节。找到合适的数字体验 (DX) 是一项非常具有挑战性的任务。

## 定义未来：开发人员和运维人员都喜欢的平台
那么，平台究竟应该是什么样子？大多数平台工程师都拥有一个共同的愿景：平台抽象了提交后的所有内容。这种抽象使开发人员能够以自助服务的方式交付工作负载。他们应该能够构建、部署和扩展工作负载，而无需成为基础设施专家。只要平台表面下方的 API 仍然可以进行调整，我们就拥有了一个成功的解决方案。

这一宏伟愿景转化为设计理念——最终转化为需求。以下是我在构建 [Northflank 平台](https://northflank.com/) 时所遵循的理念和需求：

**IaC 是起点：**基础设施即代码 (IaC) 至关重要，但它过于静态，并且发布过程本质上是动态的。它留下了诸如“如何将代码从开发环境迁移到预发布环境再到生产环境？”以及“如何在另一个区域或云中恢复生产环境？”等问题。平台应该提供一条解决这些问题的黄金路径。**自动化 CI/CD 管道：**CI/CD 是提交后旅程的起点。最大程度地减少人工干预，实现 GitOps 梦想。**您构建它，您运行它：**开发人员必须能够通过几次点击或命令来部署和扩展其应用程序。**多语言是标准：**大多数开发软件的企业规模太大，无法不使用[多种语言和框架](https://thenewstack.io/programming-languages/)。平台必须支持多语言——不仅支持短暂的，还支持有状态的和计划性的。**所有工作负载：**平台应该与工作负载的复杂性无关，并且能够支持所有容器化框架。**简化故障排除：**运行软件时最大的难题之一是故障排除。所有隐藏在应用程序开发人员面前的 API 仍然需要对站点可靠性工程师 (SRE) 可用。**双向实时接口：**如果我在 Git 中更新了工作负载，用户界面 (UI) 应该反映这些更改，反之亦然。不要让您的团队猜测其工作负载信息存储在何处。不要接受云 UI 中的陈旧信息。
从本质上讲，未来的平台应该使团队能够“构建工作负载，而不是基础设施”。

通过采用优先考虑开发人员体验而不影响操作灵活性的平台，组织可以加快交付周期、降低开销并保持竞争力。一个好的平台可以解放开发人员，让他们专注于自己的长处——编写代码——而运维人员则确保支持基础设施继续平稳运行。

## 结论
DevOps 是关于将开发人员和运维人员团结在一起的。如果平台只迎合其中一方，那么它们就不是真正的平台。在参加 KubeCon 2024 时，我会牢记这一点。在主活动中，有超过[十几个关于平台的演讲](https://kccncna2024.sched.com/overview/type/Platform+Engineering)，以及一个完整的[平台工程日联席活动](https://colocatedeventsna2024.sched.com/overview/type/Platform+Engineering+Day)。

我在这里分享的内容来自我在 [Northflank](https://northflank.com/) 上使用 Kubernetes 构建平台的经验。如果您在 KubeCon 上看到我，我很乐意听取您的想法。是否可以构建一个成功的平台，而该平台不优先考虑 DevOps 的任何一方？您在构建 IDP 时遵循哪些理念？您认为平台工程面临的主要挑战是什么？
*要详细了解 Kubernetes 和云原生生态系统，请加入我们参加 **KubeCon + CloudNativeCon 北美**，活动将于 2024 年 11 月 12 日至 15 日在犹他州盐湖城举行。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。