<!--

# Docker推出3个加速开发部署和调试的新工具
https://cdn.thenewstack.io/media/2023/10/8a66964e-dockercon23-1024x734.png
 -->


译自 [Docker Rolls out 3 Tools to Speed and Ease Development](https://thenewstack.io/docker-rolls-out-3-tools-to-speed-and-ease-development/) 。

在当地时间 6 月 12 日举行的 DockerCon 大会上，Docker 公司发布了 3 个新工具，这些工具可以利用混合云环境，来简化和加速开发者的部署和调试工作流程。

保持在本地开发有诸多好处，包括安全性、流畅的工作流程和丰富的工具。在云端开发也有不少优势，比如按需调配资源和简单易用。Docker 的新工具正是立足于这种理念——同时利用本地与云端的优势，实现本地与云端的混合开发。

“考虑到 Docker 桌面端部署在本地笔记本上，我们看到一个机会，将本地的长处与云端的长处结合起来，实现本地与云端的融合，而不是简单的本地或云端二选一。”Docker 首席执行官 [Scott Johnston](https://www.linkedin.com/in/scottcjohnston) 在本周洛杉矶 DockerCon 大会前对媒体表示。“概念上来说，这意味着你可以利用云端按需调配的资源，同时在本地保留习惯的工作流程和丰富的工具选择。”

为实现本地与云端的混合开发，[Docker](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 今天发布了 3 款新工具，所有工具均基于开源和开放标准。

## 1. Docker Scout GA - 提供应用洞察

Johnston 表示，开发者目前需要打开许多浏览器标签页来访问所需的各种工具，一项 GitHub 调查显示，开发团队平均 31% 的时间花费在发现和修复安全漏洞上。

Docker Scout GA 不是要取代所有这些工具,而是对它们进行补充和整合。它通过 [API](https://thenewstack.io/a-modern-approach-to-securing-apis/) 收集其他工具的数据和元信息，并根据这些信息对 Docker 应用提供安全洞察、策略评估、备选补救方案等。借助这种集成方式，Docker Scout 可以基于 Docker 现有内容，构建自动化和[软件清单](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)管理工具。

“它是一个本地和云端的服务，可以整合各种工具，收集它们的元数据和事件信息。”Johnston 介绍，“每次有镜像进入 CI 流程，或者提交到 Git 等，都会产生一个事件。我们收集这些事件，构建端到端的镜像视图。”

通过这种方式，Docker Scout 可以在镜像内容、操作历史和下游问题等方面提供精准的应用状态和上下文。它还可以根据分析提供各种应用问题的解决建议。

“例如，如果本地镜像使用某个存在 CVE([Common Vulnerabilities and Exposures](https://thenewstack.io/vulnerability-management-best-practices-for-patching-cves/)) 漏洞的库，而这个库实际已应用在生产环境，我们可以推荐升级到该库的安全版本，保证安全。”他说明，“这种主动防范安全问题的方式，比事后收到安全警报要好。”

Johnston 介绍，一位 DockerCon 的演讲客户使用 Scout 后，在一个小时内就能为 300 多个仓库提供覆盖保护和应用洞察。

Docker Scout 目前已集成诸如 Sysdig、JFrog Artifactory、[AWS ECR](https://thenewstack.io/managing-kubernetes-secrets-with-aws-secrets-manager/)、BastionZero、[GitHub](https://thenewstack.io/how-github-uses-github-to-be-productive-and-secure/)、GitLab、CircleCI 和 Jenkins 等多种工具。

## 2. 新一代 Docker 构建

Docker 构建会将源代码转换为容器镜像。这一环节通常在本地机器上完成，但明显占用开发者不少时间。

“开发者反映，每天耗费长达一个小时等待构建完成，这可能是一个大型构建，也可能是许多小构建的总和。但在工作日中的 8-10 个小时里，这仍然是相当可观的时间。”Johnston 表示，“因为受限于笔记本的计算资源，现有的 Docker 构建速度明显受到局限。”

下一代 Docker 构建利用云端资源进行构建，无需改变任何工具、流程或配置，他进一步解释说。测试显示，通过自动使用按需的云服务器和缓存，构建速度最高可提升 39 倍，大大节省时间。

“我们利用云端的计算资源进行大型构建，使用更强大的 CPU、内存和 IO，从而大幅压缩构建用时。”他举例，“一个原本需一个小时的构建，现在可能只要一两分钟。”

这相当于每天为开发者新增约一个小时的可用时间。他补充说。

## Docker 调试

开发者花费高达 60% 的时间用于应用调试。但大部分时间都花在配置工具和初始化上，而不是实际的问题定位。Johnston 表示这是一种短暂的调试过程，中间状态难以保留。

Docker Debug 提供语言无关、一体化的本地和远程容器应用调试工具箱，简化调试流程。

“它支持本地和远程容器的调试，集成各类工具，开发者可以把时间和精力放在问题解决上，无需浪费在配置和切换工具上。” Johnston 说。
