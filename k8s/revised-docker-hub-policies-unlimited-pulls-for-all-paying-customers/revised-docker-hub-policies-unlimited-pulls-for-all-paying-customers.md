
<!--
title: 修订后的Docker Hub政策：所有付费客户均可无限次拉取镜像
cover: https://cdn.thenewstack.io/media/2025/02/d92ef3a7-amie-johnson-vjxlzqi5tle-unsplash.jpg
-->

> 译自：[Revised Docker Hub Policies: Unlimited Pulls For All (Paying Customers)](https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers/)
> 
> 作者：Steven J Vaughan-Nichols

Docker 已修改之前宣布的拉取限制，并取消了基于消耗的镜像拉取收费。

流行的容器化平台 [Docker](https://www.docker.com/?utm_content=inline+mention) 宣布对其 [Docker Hub](https://hub.docker.com/) 政策进行重大更改，定于 2025 年 4 月 1 日生效。[Docker Hub 更改](https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/) 最初计划于 3 月 1 日进行，但已推迟一个月。

当它们出现时，我希望 Docker 的付费客户会很高兴。Docker 修改了之前宣布的拉取限制，并取消了基于消耗的镜像拉取费用。新政策包括：

- 所有 Docker 付费订阅者都可以无限制地拉取，但受合理使用限制。
- 未经验证的用户每 IP 地址每小时限制拉取 10 次。
- 免费的已验证用户现在每小时允许拉取 100 次，高于之前宣布的 40 次。
- 完全没有拉取次数限制或消耗费用。

此外，Docker 无限期推迟了基于存储的计费实施。该公司计划在考虑未来收费之前，专注于开发更好的存储管理工具。如果将来引入存储定价，将至少提前六个月通知客户。

这些变化是在 [Docker 提高了 Docker Pro 和 Docker Team 的订阅计划价格](https://thenewstack.io/docker-overhauls-simplifies-subscription-plans/) 之后发生的。这些政策变更旨在保持 Docker Hub 作为一个可靠且可扩展的平台，同时优先考虑开发人员体验。该公司估计，只有大约 7% 的 Docker 用户会受到未经身份验证的拉取的新限制的影响。

## 来自社区的反应

那些免费用户尤其直言不讳。在 [Ycombinator](https://www.ycombinator.com/) 上，免费服务的用户 [抱怨](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/) 这将如何损害他们的工作，以及 Docker 没有给他们足够的通知。然而，其他人指出，“[已经有 2-3 个月的沟通](https://news.ycombinator.com/item?id=43129450)，尽管它可能没有像某些人希望的那样细致或有针对性。”

尽管如此，其他反对这一变化的人咆哮道，“[这是诱饵和转换](https://news.ycombinator.com/item?id=43131967)，其风险在于“采用我们新的政策，这让我们赚钱，你从未注册过，否则你的业务就会失败。”然而，该帖子中最受欢迎的帖子观察到，“[不敢相信这个帖子中的权利感](https://news.ycombinator.com/item?id=43125967)。……你为什么期望一家商业公司免费为你提供容器？”

当然，如果你无法忍受这种 Docker Hub 政策的改变，没有人会用枪指着你的头坚持你使用这项服务。有些人已经 [转向 Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/)，还有一些新的服务，例如 [Spegel，一个用于在本地存储镜像工件的无状态缓存](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/)。此外，虽然 Docker Hub 仍然是最流行的容器存储服务，但还有许多其他服务，例如 GitLab Container Registry、GitHub Container Registry 和 JFrog Artifactory。

## 安全问题

这些政策变化是在最近发生的一起安全事件之后发生的，该事件涉及 [Docker Hub 上的恶意 Kong Ingress Controller 镜像](https://hackread.com/malicious-kong-ingress-controller-image-dockerhub/)，突显了容器注册表中强大的安全措施的重要性。安全不是免费的。

随着容器化格局的不断发展，Docker 的政策更新反映了该公司在平台可持续性、业务盈利能力和用户需求之间取得平衡的努力。随着实施日期的临近，这些变化的有效性以及对更广泛的容器生态系统的影响仍有待观察。我希望 Dockers 及其客户都能从中受益。
