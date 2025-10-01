本周，Helm 及其他云原生开源项目的用户将不得不寻找其他免费来源，以获取其预编译的生产就绪应用程序镜像和 Helm Chart。截至周一，Broadcom 已对其镜像下载计划进行了调整，缩小了[免费下载](https://github.com/bitnami)的范围，转而提供数量较少、主要在商业许可下可用的资源。

许多开源应用程序的用户受到了这一变化的影响。

## 对开源应用程序用户的影响

然而，许多管理员已将 Bitnami 整合到他们自己的自动化部署策略中。对他们而言，未来的工作是寻找新的镜像和 Helm Chart，并制定新的迁移或镜像策略，以避免潜在的中断。

服务提供商 Prequel 在一篇[博客文章](https://www.prequel.dev/blog-post/bitnami-deprecation)中指出：“多年来，Bitnami 的镜像和 Helm Chart 是在 [Kubernetes](https://thenewstack.io/kubernetes/) 上运行流行应用程序的事实标准路径。这些镜像维护良好，默认设置合理，并且易于通过 Helm 安装。许多团队在部署、CI 管道和内部 Chart 中都使用了 Bitnami 镜像。”

## 对开源应用程序用户的影响

根据 Prequel 的文章，Bitnami 弃用带来的最大风险是：

*   *在重启或自动扩缩期间出现 Kubernetes ImagePullBackOff，*
*   *过时/未打补丁的镜像（CVE 漂移），*
*   *定时炸弹式重启：正在运行的 Pod 看起来正常，直到下一次拉取（然后失败）。*
*   *Chart 漂移和破坏升级的子 Chart 依赖项。*

尽管这对 [Helm 社区](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/)造成了干扰，但其他人也感受到了压力。一位 Reddit 用户[想知道](https://www.reddit.com/r/kubernetes/comments/1mjx86p/regarding_the_bitnami_situation/)他可以在哪里获取 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)、[Postgres](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) 和 [Redis](https://thenewstack.io/redis-is-open-source-again/) 的最新镜像。

## CNCF 澄清 Helm 项目状态

[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)甚至发布了一份[声明](https://www.cncf.io/blog/2025/09/24/cncfs-helm-project-remains-fully-open-source-and-unaffected-by-recent-vendor-deprecations/?ref=dailydev)，回应用户疑问，声称此举并未影响 Helm 本身。

CNCF 首席技术官 Chris Aniszczyk 和 Helm 联合创始人 Matt Butcher 在一份[声明](https://www.cncf.io/blog/2025/09/24/cncfs-helm-project-remains-fully-open-source-and-unaffected-by-recent-vendor-deprecations/?ref=dailydev)中写道：“Helm 是一个毕业项目，将继续由 CNCF 管理。它仍然是完全开源的，采用 Apache 2.0 许可，并由一个中立的社区治理。”“Bitnami 决定弃用其公共 Chart 和镜像仓库，这与 Helm 项目本身完全无关。”

## Broadcom 针对 Bitnami 的新商业模式

Broadcom 的 [Tanzu 部门](https://www.vmware.com/products/app-platform/tanzu)于[七月宣布了此举](https://news.broadcom.com/app-dev/broadcom-introduces-bitnami-secure-images-for-production-ready-containerized-applications)，当时[推出了一项新服务](https://github.com/bitnami/charts/issues/35164)，该服务基于 Bitnami 仓库，名为 [Bitnami Secure Images](https://www.arrow.com/globalecs/na/vendors/bitnami-secure-images/)，它将提供一套经过安全加固（支持 SBOM、CVE 补丁、企业支持）的 280 个镜像，并以商业形式提供（该仓库将由 [Arrow Electronics](https://www.arrow.com/company) 管理）。

作为此举的一部分，该公司逐步停用非最新版本的基于 [Debian](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/) 的镜像，将其转移到 [Bitnami Legacy](https://hub.docker.com/u/bitnamilegacy) 存档网站。

除少数例外，这些旧镜像将不再进行更新。该公司仍将提供有限的、免费的最新版本镜像子集供开发使用。

Helm Chart 仍将作为 [OCI 制品](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/)在 [Docker Hub](http://docker.io/bitnami) 上提供，但不会再更新。

[![Bitnami changes](https://cdn.thenewstack.io/media/2025/09/019753f6-broadcom-bitnami-changes.png)](https://cdn.thenewstack.io/media/2025/09/019753f6-broadcom-bitnami-changes.png)

Bitnami 变化

## 供应商如何填补空白

一些供应商迅速介入填补空缺：RapidFort [提供了其一套](https://www.rapidfort.com/blog/bitnami-goes-behind-paywall-rapidforts-curated-near-zero-cve-images-offer-superior-alternative)“近零 CVE”的精选镜像。Prequel 发布了一套 CRE（[通用可靠性枚举](https://docs.prequel.dev/cres/commercial)），作为一项付费服务的一部分，用于检测 Bitnami 镜像被拉取到生产环境的情况。

RapidFort 的文章总结道：“Bitnami 的中断既是挑战，也是机遇。虽然当务之急是替换 Bitnami 镜像以维持运营连续性，但更广阔的机遇在于通过 RapidFort 精选的近零 CVE 容器镜像，显著增强您组织的安全态势。”

[![screenshot](https://cdn.thenewstack.io/media/2025/09/c561d8bb-68bf3fc32c8101b9b93201e1_bdc994c4.png)](https://cdn.thenewstack.io/media/2025/09/c561d8bb-68bf3fc32c8101b9b93201e1_bdc994c4.png)

Prequel 规则目录

## Bitnami 简史

截至今年早些时候，Bitnami 每月提供多达 [5 亿个镜像](https://thenewstack.io/the-bitnami-open-source-application-catalog-turns-18/)，并且[甚至增加了对 Helm Chart 的支持](https://github.com/bitnami/charts)，扫描了 Helm Chart 中包含的所有镜像的漏洞。

Bitnami 本身是由 Daniel López 和 Erica Brescia 于 2007 年创立的，目标是让开发者更容易在不同平台上部署开源软件。