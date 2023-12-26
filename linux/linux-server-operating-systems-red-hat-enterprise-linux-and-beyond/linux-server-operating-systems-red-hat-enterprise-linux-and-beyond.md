<!--
title: Linux服务器操作系统的选择
cover: https://cdn.thenewstack.io/media/2023/12/d89e743c-holiday_penguin-1024x683.png
-->

除了红帽企业版Linux，还有几个竞争对手克隆和分支，争夺您的 Linux 服务器和云计算开支。以下是它们的详细情况。

> 译自 [Linux Server Operating Systems: Red Hat Enterprise Linux and Beyond](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)，作者 Steven J. Vaughan-Nichols，又称 sjvn，自 CP/M-80 是尖端的个人电脑操作系统、300bps 是高速互联网连接、WordStar 是当时最先进的文字处理器的时候，就开始撰写关于技术和技术业务的文章，并且我们对此感到满意。

几年前，有关 [Red Hat Enterprise Linux（RHEL）](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)，情况相对简单。如果您需要支持，您可以与 [Red Hat ](https://www.openshift.com/try?utm_content=inline-mention)签订合同。如果没有，您可以使用社区版 RHEL，即 [Community Enterprise Operating System（CentOS）](https://linuxhint.com/everything-you-want-to-know-about-centos-as-linux-distribution/)。

事情发生了变化。

首先，Red Hat 早就知道大多数 RHEL 家族的客户都在使用[免费的 CentOS](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/) 而不是付费的 RHEL。因此，在2011年，Red Hat 将自己的补丁直接整合到其内核树中。所有的代码仍然存在，但正如一个人当时所说，“这有点像向某人要求家庭巧克力片饼干的食谱，却得到了饼干面糊。”

这并没有阻止一些团体和公司，比如[一直在模仿 RHEL](https://practical-tech.com/2006/10/25/oracles-red-hat-rip-off/) 的 [Oracle](https://developer.oracle.com/?utm_content=inline-mention)，他们会制作自己的 RHEL 克隆饼干。

在2014年，[Red Hat “收养”了 CentOS](https://www.zdnet.com/article/red-hat-incorporates-free-red-hat-clone-centos/)，希望将其用户转变为 RHEL 客户。但这并没有奏效。因此，在2020年，Red Hat [将 CentOS](https://thenewstack.io/red-hat-has-finally-given-centos-7-a-cloud-upgrade-plan/) 从一个稳定的 RHEL 克隆变成了一个滚动 Linux 发行版，CentOS Stream。这完全不同。正如一位用户所说，[“CentOS 的用例与 CentOS Stream 完全不同](https://www.reddit.com/r/linux/comments/k95dt7/centos_project_shifts_focus_to_centos_stream/)。许多人使用 CentOS 进行生产的企业工作负载，而不是进行开发。CentOS Stream 可能适用于开发/测试，但人们不太可能在生产环境中采用 CentOS Stream。”

事实上，公司并没有这么做。相反，两位领先的 Linux 开发者，[CloudLinux](https://www.cloudlinux.com/) 创始人兼首席执行官Igor Seletskiy 和 CentOS 创始人兼[CIQ](https://ciq.co/)首席执行官Gregory Kurtzer，分别创建了新的 RHEL 克隆，[AlmaLinux](https://almalinux.org/) 和 [Rocky Linux](https://rockylinux.org/)。

这两个新的 RHEL 克隆都提供商业支持。[CloudLinux](https://thenewstack.io/wherefore-art-thou-centos-rocky-linux-cloudlinux-and-centos-stream/) 是专为共享托管提供商设计的企业级 RHEL 克隆，为 AlmaLinux 提供技术支持，而 CIQ 则为 Rocky Linux 提供支持。第三方 Linux 咨询公司，如 [Perforce OpenLogic](https://www.openlogic.com/about-openlogic-perforce)，也提供支持。

但是，如果您拥有内部的 Linux 专业知识，您就不需要为此付费。AlmaLinux 和 Rocky Linux 都由非营利基金会管理。AlmaLinux 由 [AlmaLinux OS 基金会](https://wiki.almalinux.org/Transparency.html)运营，Rocky Linux 由 [Rocky Enterprise Software Foundation (RESF)](https://www.resf.org/) 管理。

事情一直保持这样，直到2023年夏天。Red Hat 限制了其 RHEL 代码的使用。这使得 RHEL 克隆者更难以创建自己的操作系统。

但是这并没有阻止它们。[AlmaLinux 决定不再基于 RHEL 的代码构建其发行版](https://www.zdnet.com/article/almalinux-is-dropping-out-of-the-rhel-clone-wars/)；相反，它将使用 CentOS Stream 的代码作为其基础。其他人采取了更积极的方式。[Oracle 抨击 Red Hat](https://www.zdnet.com/article/oracle-takes-on-red-hat-in-linux-code-fight/) 并发誓保持与 RHEL 的兼容性。[RESF 将使用其他方法获取 RHEL 代码](https://rockylinux.org/news/keeping-open-source-open/)。然后，在一次出人意料的举动中，欧洲 Linux 强国 [SUSE](https://www.suse.com/) 决定[将 RHEL 分叉](https://www.zdnet.com/article/suse-to-fork-red-hat-enterprise-linux/)为 [Liberty Linux](https://www.suse.com/c/suse-liberty-linux/)。

如果这对您来说听起来有很多重复努力，那对其中几个团体也是如此。因此，其中三个——CIQ、Oracle 和 SUSE——成立了[开放企业 Linux 协会（OpenELA）](https://openela.org/)。他们的联合目标是促进“通过提供开放和免费的企业级 Linux 源代码，开发与 Red Hat Enterprise Linux (RHEL) 兼容的发行版。”

这意味着将不会有 OpenELA 的二进制发行版。相反，它将发布一个可自由获取、可重新分发且维护的 [GitHub Enterprise Linux（EL）兼容源代码仓库](https://github.com/openela-main)。

今天，从 Red Hat，我们有 [RHEL 9.3](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/9.3_release_notes/index)，原版，以及 CentOS Stream，它是一个开发分发，位于 [Fedora Linux](https://fedoraproject.org/) 和 RHEL 之间的中间阶段。一般来说，CentOS 不适用于生产环境。

另一方面，我们有兼容 RHEL 但不直接基于 RHEL 代码的 [AlmaLinux 9.3](https://almalinux.org/blog/2023-11-13-announcing-93-stable/)。基于 RHEL 代码，我们还有 [Rocky Linux 9.3](https://rockylinux.org/ru/news/rocky-linux-9-3-ga-release/) 和 [Oracle Linux 9.3](https://blogs.oracle.com/linux/post/oracle-linux-9-update-3)。SUSE 现在通过其 Liberty Linux 计划提供支持，但尚未提供自己的 Linux 发行版。OpenELA 的代码库可供使用，据推测，Oracle、Rocky、SUSE 和任何其他希望使用它作为其发行版基础的人都将使用它。

明白了吗？

对用户来说，这意味着您在选择兼容 RHEL 的 Linux 时有很多选择。RHEL 9.3 及其变体是最新的，也是自 Red Hat 最近修改代码规则以来首次出现的版本。

我曾简要地使用过所有 9.3 变体的 RHEL 9.3，据我所知，它们之间都是兼容的。它们也都在主要的云服务提供商上可用。

那么，哪一个适合您呢？

如果您需要一流的企业支持，RHEL 就是适合您的 Linux。

此外，Red Hat 在其发行版中越来越多地整合了其他非 Linux 特性。例如，RHEL 订阅现在附带了 [Red Hat Insights](https://www.redhat.com/en/technologies/management/insights)，这是一套用于开发和管理大规模 Linux 平台的托管专家系统服务。它还集成了用于部署、运行、构建容器环境的 [Podman](https://thenewstack.io/red-hat-podman-container-engine-gets-a-desktop-interface/)，这是一个无守护进程的工具，并预先预配置了简化 Podman 系统操作的 [Ansible DevOps 角色和模块](https://thenewstack.io/red-hat-ansible-lightspeed-uses-ai-to-automate-infrastructure-management/)。

RHEL 还是基本上所有 Red Hat 其他程序的基础，例如 [Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline-mention)，其 Kubernetes 发行版，[Red Hat OpenStack Platform](https://www.redhat.com/en/technologies/linux-platforms/openstack-platform) 和 [Red Hat Ceph 存储](https://www.redhat.com/en/technologies/storage/ceph)。

如果贵公司对 Oracle 至关重要，继续使用 Oracle Linux 吧。这是没有错的选择。如果在服务器上使用 CloudLinux 并且效果很好，也没有理由更换。

您可以将 CentOS Stream 用于生产环境，但我不建议这样做。只有在您需要尖端 Linux 功能并且具备内部专业知识以充分利用它们时，才部署 CentOS Stream。否则，您只是在自找麻烦。

最后，如果您熟悉旧版 CentOS，AlmaLinux 或 Rocky Linux 都是优秀的选择。我在我的服务器和云实例上都使用了它们，并且一直很满意。
