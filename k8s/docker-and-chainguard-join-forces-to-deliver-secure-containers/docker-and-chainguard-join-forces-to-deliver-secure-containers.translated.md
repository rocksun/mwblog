## Docker 和 Chainguard 携手提供安全容器

![Docker 和 Chainguard 携手提供安全容器的特色图片](https://cdn.thenewstack.io/media/2024/03/86c760d9-desk-593327_1280-2-1024x682.jpg)

Chainguard 的安全开发者镜像现在将通过 Docker Verified Publisher 计划在 Docker Hub 上提供。

我喜欢 [Docker](https://www.docker.com/?utm_content=inline-mention) 用于管理容器，我喜欢 [Chainguard](https://www.chainguard.dev/?utm_content=inline-mention) 用于其安全容器镜像，因此我非常高兴这两家公司携手将 [Chainguard 开发者镜像](https://www.chainguard.dev/chainguard-images) 通过 [Docker Verified Publisher (DVP)](https://docs.docker.com/trusted-content/dvp-program/) 计划提供给 [Docker Hub](https://hub.docker.com/)。

对于那些不知道的人来说，Chainguard 开发者镜像在设计上是强化的。每个容器镜像都包含最少的软件包数量，因此它们具有尽可能小的攻击面。此外，Chainguard 镜像每天都会打补丁，而无需等待上游发行版。结果如何？据该公司称，Chainguard 镜像比其竞争对手少了 80% 的 [常见漏洞和披露 (CVE)](https://cve.mitre.org/)。

Chainguard 生产镜像还满足了对修补服务级别协议 (SLA)、FedRAMP 的 FIPS 验证镜像和安全 AI 镜像的最苛刻要求。换句话说，它们非常好。

[Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) 当然是一个备受推崇的容器注册表，拥有超过 1000 万个帐户，其庞大社区的拉取量接近 5000 亿次。我敢肯定，一定有人从未使用过 Docker Hub。我只是从未见过他们。

特别是，DVP 计划为 Docker 客户和用户提供受信任的内容。这 [使开发团队能够安全地构建](https://thenewstack.io/how-to-enable-developer-teams-to-improve-container-security/) 并最大程度地减少对恶意软件的访问。

Chainguard 开发者镜像共同为 Docker Hub 的用户提供了安全、最小的容器镜像，用于不断扩大的云原生和开源项目，包括 Python、Node.JS 和 Java 等重量级项目。

Docker 的首席技术官 Justin Cormack 赞扬了此次集成，强调了 [Docker Verified Publisher 计划在 Docker 提供](https://thenewstack.io/docker-delivers-docker-extensions-docker-desktop-for-linux/) 各种受信任的顶级内容的使命中的核心作用。“通过将 Chainguard 开发者镜像集成到 Docker Hub 中，我们为 Docker 用户提供了安全、最小且高性能的镜像。”

Chainguard 的首席执行官兼联合创始人 Dan Lorenc 呼应了 Cormack 的热情，他强调，这种合作关系使 Docker 用户能够利用可靠的来源来获取安全、强化、高质量的镜像，从而使他们能够自信地满足严格的安全标准。“Chainguard 镜像经过专门设计，旨在满足 Docker Business 和 Trusted Content 用户的需求，他们完全依赖 Docker 来提供他们可以信赖的优质、安全和强化的镜像。”

不仅仅是 Docker 和 Chainguard 赞扬这种配对。人工智能开发公司 [Acorn Lab](https://www.acorn.io/) 的联合创始人兼首席架构师 Darren Shepherd 非常高兴看到这种组合。“最终，Chainguard 强化的容器镜像可以在 Docker Hub 上访问。从今天开始，我估计我的 Docker 运行效率现在提高了 70%，“说真的，这是我一段时间以来一直在询问 Chainguard 的事情，我很高兴看到这一天到来。我只希望发生的下一个关键创新是将 [Wolfi](https://github.com/wolfi-dev) [Chainguard 的安全优先、特定于容器的 Linux 发行版] 添加到库命名空间中。”

这种联盟标志着他们在 [保护全球软件供应链](https://thenewstack.io/linux-foundations-sigstore-aims-to-more-easily-secure-software-supply-chains/) 的共同目标中取得了一项重大进展。它确保了开发人员拥有最安全的资源和技术，这是当今快速发展的数字领域中必不可少的。

对于渴望探索 Chainguard 开发者镜像的开发人员，目前可用的 384 个镜像可在 [通过 Chainguard 的 DVP 页面在 Docker Hub 上](https://hub.docker.com/u/chainguard) 轻松获得。

与往常一样，经过身份验证的 Docker Pro、Teams 和 Business 用户的速率限制每天最多为 5,000 次拉取。个人或免费层 Docker Hub 用户每六小时可以访问 200 次拉取，未经身份验证的 Docker Hub 用户每六小时可以进行 100 次镜像拉取。如果您遇到速率限制问题，您始终可以从 [Chainguard 的目录](https://images.chainguard.dev/?category=featured?utm_source=blog&utm_medium=website&utm_campaign=FY25-EC-Blog_sourced) 直接拉取镜像。

[YOUTUBE.COM/THENEWSTACK](https://www.youtube.com/channel/UC06vC74r3p4VG6s3FuzR1Sw)
**[科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)**