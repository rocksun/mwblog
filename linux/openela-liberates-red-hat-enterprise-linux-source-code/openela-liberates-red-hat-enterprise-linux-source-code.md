
<!--
title: OpenELA公开发布Red Hat Enterprise Linux源代码
cover: https://cdn.thenewstack.io/media/2024/07/557b386a-milad-fakurian-rmklf_kkwio-unsplash.jpg
-->

OpenELA 已将其进程自动化，以便在 RHEL 新版本发布后几天内即可获得新的企业 Linux 源。

> 译自 [OpenELA Liberates Red Hat Enterprise Linux Source Code](https://thenewstack.io/openela-liberates-red-hat-enterprise-linux-source-code/)，作者 Steven J Vaughan-Nichols。

Open Enterprise Linux Association 宣布公开发布 RHEL 9.4 和 RHEL 8.10 的源代码，这标志着 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 与 Red Hat Enterprise Linux 克隆发行版分发商之间的斗争又迈出了新的一步。

我知道你在想什么。[Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) 的源代码不是已经公开了吗？我的意思是，Linux 是开源的典范。嗯，是也不是。2023 年 7 月，[Red Hat 宣布](https://www.redhat.com/en/blog/furthering-evolution-centos-stream)，“[CentOS Stream](https://www.centos.org/centos-stream/) 将成为公开发布 RHEL 相关源代码的唯一存储库。对于 Red Hat 客户和合作伙伴，源代码将继续通过 [Red Hat 客户门户](https://access.redhat.com/) 提供。”

CentOS Stream 是 RHEL 的持续交付开发发行版。它不是企业级的稳定版 Linux。RHEL 克隆发行版分发商，例如 [AlmaLinux OS](https://almalinux.org/)、[Oracle Linux](https://www.oracle.com/linux/)、[SUSE Liberty Linux](https://www.suse.com/shop/suse-liberty-linux/) 和 [Rocky Linux](https://rockylinux.org/)，对此感到不满。

[AlmaLinux 决定按照 Red Hat 的规则行事](https://www.zdnet.com/article/how-almalinux-stays-red-hat-enterprise-linux-compatible-without-red-hat-code/)。它使用了 CentOS Stream 的代码库。[CIQ](https://ciq.com/)，支持 Rocky Linux、Oracle 和 SUSE 的公司，选择成立 [Open Enterprise Linux Association (OpenELA)](https://openela.org/)。其目标是帮助创建“与 [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) 兼容的发行版，方法是提供开放和免费的企业级 Linux 源代码。”

正如 [Gregory Kurtzer](https://thenewstack.io/centos-creator-gregory-kurtzer-discusses-his-new-distro-rocky-linux/)，CIQ 的首席执行官和 [Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/) 的创始人当时解释的那样：“全球各地的组织都将 [CentOS](https://www.centos.org/) 作为标准，因为它免费提供，遵循企业级 Linux 标准，并且得到了良好的支持。在 [CentOS 被停用](https://www.zdnet.com/article/red-hat-resets-centos-linux-and-users-are-angry/) 之后，它不仅在生态系统中留下了巨大的空白，而且清楚地表明了社区需要团结起来，做得更好。OpenELA 正是如此——社区为确保所有专业 IT 部门和企业用例的协作和稳定未来而做出的回应。”

Red Hat 的 [Mike McGrath](https://www.redhat.com/en/authors/mike-mcgrath)，核心平台工程副总裁，坚持认为 [Red Hat 没有做错任何事](https://www.redhat.com/en/blog/red-hats-commitment-open-source-response-gitcentosorg-changes)。从 McGrath 的角度来看，Red Hat 仍然遵守所有 Linux 的 [开源许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)。问题在于分发商和用户“不想为投入 RHEL 的时间、精力和资源付费，或者那些想要重新打包以获取利润的人。”他继续说道，“我们不认为重新构建 RHEL 有价值，我们也没有义务让重新构建者更容易；这是我们自己的决定。”

OpenELA 的呼吁是获取代码并将其公开发布。问题是提取和公开发布代码并不容易。该组织的开发人员通过支付 [Red Hat Universal Base Image (UBI)](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image) 容器镜像和云实例，通过 Red Hat 客户门户合法地访问 RHEL 源代码。

现在，OpenELA 已将其流程自动化，因此新的企业级 Linux 源代码在每个新版本 RHEL 发布后几天内即可获得。[最新版本——RHEL 9.4 和 RHEL 8.10 的源代码包现已提供](https://github.com/orgs/openela-main/repositories)。

通过访问这些 [GitHub 存储库](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/)，任何人都可以构建自己的与 RHEL 兼容的二进制文件。Kurtzer 解释说：“任何有兴趣创建下游构建的人都可以访问 OpenELA 存储库以获取他们需要的源代码。由于我们不创建实际的构建，而只是提供对源代码的可靠访问，因此我们可以快速行动，并赋能整个开源生态系统，以加速其企业级 Linux 构建的开发和交付。”
如果您想自己构建，有几个工具可以简化操作。这些工具包括 [Rocky Peridot](https://github.com/rocky-linux/peridot)、[SUSE Open Build Service](https://build.opensuse.org/)、[Fedora Koji](https://koji.build/) 和 [AlmaLinux Build System](https://build.almalinux.org/)。

如果您构建了自己的企业 Linux 发行版，并且您愿意，欢迎加入 OpenELA。SUSE 首席技术官办公室成员，OpenELA 创始成员 [Alan Clark](https://www.linkedin.com/in/alanhclark/) 表示：“如果您创建了下游构建，我们欢迎您加入 OpenELA。OpenELA 在快速提供这些版本源代码方面的能力向开源社区表明，现在，有了 OpenELA，企业 Linux 源代码的访问权限可以可靠地获得。这是 OpenELA 任务的核心：与世界分享这些开源组件可以随意使用，正如它们应该的那样。”

甲骨文软件开发执行副总裁，OpenELA 创始成员 Wim Coekaerts 补充道：“OpenELA 自动化了下游发行版构建过程，以帮助用户尽可能高效地利用最新版本的企业 Linux 的优势。”

虽然代码相同，但 Coekaerts 还表示，甲骨文的目标是确保兼容的用户空间应用程序二进制接口 (ABI) 和 API。“对于应用程序来说，要保持兼容，不需要完全匹配源代码。”另一方面，[AlmaLinux](https://thenewstack.io/how-to-migrate-centos-7-to-almalinux/) 不是 OpenELA 成员，并且努力实现 ABI 兼容性。

OpenELA 不会发布自己的发行版。如果您想要一个基于 OpenELA 代码库的 Linux 发行版，请查看 [Rocky Linux 9.4](https://rockylinux.org/news/rocky-linux-9-4-ga-release)、[Rocky Linux 8.10](https://rockylinux.org/news/rocky-linux-8-10-ga-release)、[SUSE Liberty Linux](https://www.suse.com/c/suse-liberty-linux/)、[Oracle Linux 8.10](https://docs.oracle.com/en/operating-systems/oracle-linux/8/relnotes8.10/) 或 [Oracle Linux 9.4](https://blogs.oracle.com/linux/post/oracle-linux-9-update-4-is-generally-available)。

当然，正如 Red Hat 会很快告诉您的那样，如果您想要 Red Hat 级别的支持，您需要 RHEL 许可证，而不是 RHEL 克隆。
