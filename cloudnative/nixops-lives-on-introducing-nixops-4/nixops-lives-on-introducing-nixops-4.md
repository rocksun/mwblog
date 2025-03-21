
<!--
title: NixOps依然存在：NixOps 4 介绍
cover: https://cdn.thenewstack.io/media/2025/03/2cd596d3-tim-hufner-fobq12oj6sy-unsplash-1.jpg
summary: NixOps 4 重生！新版吸取教训，借鉴 Terraform，专注 IaC 和 NixOS 部署。Flox 作为 Docker 替代方案，简化 Nix 使用，支持 Kubernetes。Cloud Native Nix 强调软件包安全性，利用 Nixpkgs 优势，减少虚拟机依赖，提升 FaaS 效率。
-->

NixOps 4 重生！新版吸取教训，借鉴 Terraform，专注 IaC 和 NixOS 部署。Flox 作为 Docker 替代方案，简化 Nix 使用，支持 Kubernetes。Cloud Native Nix 强调软件包安全性，利用 Nixpkgs 优势，减少虚拟机依赖，提升 FaaS 效率。

> 译自：[NixOps Lives On: Introducing NixOps 4](https://thenewstack.io/nixops-lives-on-introducing-nixops-4/)
> 
> 作者：B Cameron Gain

[Nix](https://nixos.org/) 已经开发了十多年。有人说它永远无法实现其完全可重现的环境和工作负载的承诺，以及与相关的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 发行版 [NixOS](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/) 相关的工作。

然而，已经取得了巨大的进展。该项目已经进行了这么长时间，这证明了社区的强烈兴趣及其普遍的确定性，即在理论上是可以做到的。虽然这非常难以实现，但已经取得了重大进展。例如，[Flox](https://thenewstack.io/docker-replacement-flox-has-libraries-for-kubernetes/) 就建立在 Nix 之上，这很明显。Flox 旨在提高可用性和部署，并且它已经证明了能够替代各种应用程序的 [Docker](https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers/) 功能，从而导致需求显着增加。

## NixOps 传奇

然后是 [NixOps](https://releases.nixos.org/nixops/nixops-1.5.1/manual/manual.html)，它是 NixOS 的部署和管理平台。它提供 [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) 功能，使用户能够以编程方式部署和管理 NixOS 系统和应用程序。然而，NixOps 的初始版本面临着重大挑战，并且有一段时间，它被认为基本上已经消亡。

现在，NixOps 已经复活。最新的迭代版本 [NixOps 4](https://github.com/nixops4/nixops4) 在今年早些时候在布鲁塞尔举行的 [FOSDEM](https://fosdem.org/2025/) 活动中进行了讨论。会议涵盖了过去失败的教训以及关于不该做什么的关键要点。以下是 NixOps 团队的说法。

由于 NixOps 曾经是唯一的 Nix 原生部署和配置工具，因此 NixOps4 代表了“该工具的完全重新设计”，吸取了 NixOps 的经验教训，并在其原始维护者 [Robert Hensing](https://www.linkedin.com/in/rhensing/?originalSubdomain=nl) 的帮助下，Hercules CI 的联合创始人兼 Nix 社区指导委员会成员说。NixOps4 也受到了 [Terraform](https://opentofu.org/) 的启发。

“在我们当前的项目中，我们使用 NixOps 的方式与我们迄今为止的方式大致相同，”Hensing 在 FOSDEM 的演讲中说。“还有一些资源限制和问题需要考虑，”Hensing 说。

Hensing 说，一个关键问题是 NixOps 状态生命周期是否会变得过于繁琐。“现在要充分评估其生态系统可能还为时过早，因为我花费了大量时间来确保资源状态得到正确管理，”Hensing 说。“我还没有完全决定。”

[无国界医生组织 (MSF)](https://www.msf.org/) 选择 NixOS 是因为其运营的复杂性。[Sohel Sarder](https://www.linkedin.com/in/sohel-sarder-84a5379a/) 是无国界医生的 DevOps 工程师，他在 FOSDEM 的演讲中说，“[NixOS @ Doctors Without Borders (MSF) — Why We Use It and How](https://fosdem.org/2025/schedule/event/fosdem-2025-5165-nixos-doctors-without-borders-msf-why-we-use-it-and-how/)“：“我们复杂的 IT 运营需要一个强大且具有弹性的系统，我们希望该系统能够自行快速发展，并且维护量最少。而且我们还希望同一个系统可以同时用于我们的现场运营管理和总部运营管理。因此，我们选择 NixOS，因为它支持声明式配置管理和基础设施即代码。”

## Flox 的灵活性

初创公司 Flox 已经证明了其对 Nix 的改编如何可以作为 Docker 的可行替代方案，因此值得仔细研究。虽然 Nix 已经存在多年，并且以其复杂性而闻名，但 Flox 简化了它的使用和采用。最近，Flox 已将其 Nix 版本定位为 Kubernetes 上 Docker 容器的潜在替代品。

Flox 被描述为开发人员和运营团队的环境和平台，以跨平台方式提供可重现性和应用程序部署。但是，它可以实现跨不同环境的一致性，并且可以利用 Flox，Flox 融合了 Nix 的最佳功能，使其更易于访问并简化了 Nix 环境的使用。

###
Nix 存储的运作方式与传统的 OCI 镜像仓库不同。虽然 OCI 镜像仓库运行良好，但它们的容器层依赖于分层文件系统。在这样的系统中，更改一个层会使所有后续层失效。

相比之下，Nix 存储在 Nix 存储中提供了许多派生，其中 Flox 称之为 Nixpkgs 软件包的数量超过 120,000 个。它们可能由单个文件或 shell 脚本组成，这有助于避免不必要的失效。

例如，在为 sh 设置依赖树时，只需要几个相关文件。然后，这些文件可以在各种项目中重复使用，与基于容器的系统相比，在依赖管理中提供更精细的分辨率。

## 云原生 Nix

正如 Flox 的高级 DevRel 工程师和 Kubernetes 贡献者 [Leigh Capili](https://www.linkedin.com/in/leighcs/) 在去年 11 月的 [Cloud Native Rejekts](https://www.linkedin.com/posts/the-new-stack_cloud-native-rejekts-na-2024-activity-7257357682527907840-bii5/) 大会上发表的题为“Cloud Native Nix!”的演讲中所解释的那样，一个云原生人员（已经从容器镜像和运行时中受益）会对以确保软件只访问它需要的内容的方式打包软件感兴趣。目标是将这种方法的重要性置于上下文中。

此环境可以轻松列出我正在使用的 Nix 软件包生态系统中的软件。Flox 是我们正在构建的一个开源项目，它可以让我轻松演示如何使用这些软件包。例如，我可以列出我的主目录中的软件，显示我想安装在系统上的软件包。您将看到诸如 zsh、我最喜欢的文本编辑器以及用于终端任务的实用程序之类的工具。

通常，软件的开发是为了运行、通过测试并打包到可以上传到镜像仓库的容器镜像中。使用这种方法，似乎没有理由重新考虑习惯。“现代工具，”Capili 说，“允许创建可以无限期存储并部署在诸如函数即服务 (FaaS)、Kubernetes 集群甚至 Docker Desktop 等平台上的工作产物。此工作流程似乎足以满足大多数需求。”

然而，当使用 MacBook 时，出现了一个重新考虑打包的令人信服的理由，Capili 说。MacBook 具有高级内核，例如 Darwin 内核，该内核也用于 iPhone。虽然 Darwin 内核提供了令人印象深刻的隔离功能，但它目前无法以所需的方式运行 OCI 容器。虽然有一个有趣的 Darwin Containers 项目将来可能会支持这一点，但 Capili 解释说，它尚未被广泛采用。

Capili 说，为了打包和使用所需的软件作为云原生专业人员，用户通常依赖于 Docker、Podman 或 nerdctl 等工具来访问在 Linux 环境上运行的守护程序。有趣的是，现代 Nixpigs 软件包中的绝大多数软件（大约 120,000 个软件包）都是在公共构建场上交叉构建的。然后将它们存储在一台 1.5 PB 实例上托管的二进制缓存中。Capili 说，这种设置使该软件可以本地用于 macOS，从而减少了频繁运行虚拟机，这是一个显着的优势。

在他的演讲中，Capili 解释了为什么一个已经从容器镜像和运行时中受益的云原生用户，会对以确保软件只访问它需要的内容的方式打包软件感兴趣。“目标是将这种方法的重要性置于上下文中，”Capili 说。

正如 Capili 解释的那样，通常，软件的开发是为了运行、通过测试并打包到可以上传到镜像仓库的容器镜像中。Capili 说，使用这种方法，似乎没有理由重新考虑习惯。现代工具允许创建可以无限期存储并部署在诸如 FaaS、Kubernetes 集群甚至 Docker Desktop 等平台上的工作产物。Capili 说，此工作流程似乎足以满足大多数需求。