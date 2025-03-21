# Red Hat Enterprise Linux 9.5 发布，增强 AI 支持和自动化功能

![Red Hat Enterprise Linux 9.5 发布，增强 AI 支持和自动化功能](https://cdn.thenewstack.io/media/2024/11/c57d7e8e-redhat-1024x683.png)

曾经，新的企业级 Linux 版本发布都只关注 Linux 本身。但时代变了。最好的例子就是 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)。这个领先的 Linux 发行版，虽然仍然将 Linux 作为首要任务，但也[专注于云计算](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/)。现在，随着 [Red Hat Enterprise Linux (RHEL) 9.5](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/9.5_release_notes/index) 的发布，它正在将其产品组合扩展到 [人工智能](https://thenewstack.io/ai/) (AI) 领域。

为什么？根据 Red Hat 赞助的一份新的 IDC 报告 [《Red Hat Enterprise Linux 标准化的业务价值》](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fwww.redhat.com%2Fen%2Fresources%2Fidc-executive-summary-standardizing-analyst-material&esheet=54152568&newsitemid=20241113036427&lan=en-US&anchor=The+Business+Value+of+Standardizing+on+Red+Hat+Enterprise+Linux&index=1&md5=0bea3060b81f685e79f37d82d3edb93a&_gl=1*1xqv5kd*_gcl_au*MTkyMTc1NjE5MC4xNzMxNjA1MzMy*_ga*Mjk2NDc0MjU0LjE3MzE2MDUzMzI.*_ga_ZQWF70T3FK*MTczMjAzOTQ5Ny40LjAuMTczMjAzOTQ5Ny42MC4wLjA.)，“组织机构仍然难以在维护其 Linux 操作系统环境及其支持的工作负载之间取得平衡，同时还要面临时间和资源的限制。”

借助 RHEL 9.5，“RHEL 标准化通过整合操作系统、自动化诸如扩展和配置等高度手动化的任务以及降低部署的复杂性，提高了 IT 基础设施管理团队的敏捷性。因此，基础设施团队将 26% 的时间更多地用于业务和基础设施创新。”

Red Hat 并非只是说说而已。它正在付诸行动。[Red Hat 实际上正在使用 AI 来简化用户的工作](https://www.zdnet.com/article/how-red-hat-is-embracing-ai-to-make-sysadmin-lives-easier/)。例如，Red Hat 的 [Red Hat Lightspeed](https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed) 是一款生成式 AI 服务，旨在帮助自动化系统管理员的工作。Lightspeed 使用 [自然语言处理](https://www.ibm.com/topics/natural-language-processing) (NLP) 将提示转换为代码。它主要与 [Ansible](https://www.ansible.com/) DevOps 配合使用。这使得使用 Ansible Playbook 自动化系统管理工作比以往任何时候都更容易。

这些功能现在已被集成到 RHEL 9.5 中。新的 RHEL 系统角色是从 [Ansible 内容集合](https://www.redhat.com/en/technologies/management/ansible/content-collections) 中选择的。这些角色自动化日常管理任务，帮助您在规模上实现更一致的配置和工作流程。

## 企业 IT 的复杂性

RHEL 的总经理 Gunnar Hellekson 强调了企业 IT 日益增长的复杂性，尤其是在 AI 兴起的情况下。Hellekson 在一份声明中表示：“从我们构建的应用程序到它们运行的环境，企业 IT 的复杂性不会消失。相反，它正在呈指数级增长，尤其是在 AI 等新技术的推动下。”

例如，Red Hat 现在拥有一个专门的 AI 程序，[Red Hat Enterprise Linux AI 1.2](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai)。RHEL AI 1.2 旨在帮助公司构建自己的大型语言模型 (LLM) 的开发、测试和部署。

RHEL 9.5 还引入了增强的机密计算功能，以保护敏感的 AI 工作负载。此功能使组织能够在遵守数据合规性法规的同时处理大型数据集。随着法规围绕 AI 而制定，这一点变得越来越重要。

除了 AI 之外，安全性仍然是 Red Hat 最关注的问题。现在提供了预硬化镜像配置，以帮助公司尽早将安全性融入开发流程。

此外，OpenSSL TLS 工具包已升级到 3.2.2 版本。此版本支持证书压缩扩展 RFC 8879 和 Brainpool 曲线，这些已添加到 TLS 1.3 协议 RFC 8734 中。国家安全系统 (NSS) 加密工具包已重新调整到上游版本 3.101。这提供了许多错误修复和增强功能。

## 新的系统角色
RHEL 9.5 added several new system roles.  I believe the most significant—and I’m sure most sysadmins would agree—is the inclusion of a new [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) role, the primary command for Linux system administrators. This allows for the secure automation of large-scale sudo configuration and usage.  According to Red Hat’s press release, “This enables regular users to run commands typically reserved for administrators, with appropriate safeguards in place to manage rules.”

Under the hood, the latest RHEL runs on the Linux 5.14.0-503.11.1 kernel.  Of course, as always, RHEL 9.5 boasts the latest application development tools, languages, and databases to fuel innovative application development. This includes PostgreSQL’s PG Vector, new versions of node.js, the GCC toolset, the Rust toolset, and the LLVM toolset.

This release introduces new file management capabilities in the web console. This allows sysadmins to perform routine file management tasks without using the command line. This addition simplifies system administration and enables organizations to standardize deployments at scale.

Red Hat Enterprise Linux 9.5 is now generally available to existing customers with active RHEL subscriptions through the [Red Hat Customer Portal](https://access.redhat.com/). For those interested in trying out the latest release, a 60-day evaluation version is available for download. As always, there’s also a [free RHEL developer edition](https://developers.redhat.com/products/rhel/download#getredhatenterpriselinux7163).

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)  Technology moves fast. Don't miss an episode. Subscribe to our YouTube channel for all our podcasts, interviews, demos, and more.