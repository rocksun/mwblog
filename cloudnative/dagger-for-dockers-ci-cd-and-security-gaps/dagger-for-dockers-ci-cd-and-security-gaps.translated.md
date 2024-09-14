# Dagger 用于 Docker 的 CI/CD 和安全漏洞

![用于 Docker 的 CI/CD 和安全漏洞的特色图片](https://cdn.thenewstack.io/media/2024/09/b31bafd4-olivie-strauss-fsdvg0_9haa-unsplash-1-1024x683.jpg)

我的想法是将我的 [Neo4j 知识图谱](https://thenewstack.io/build-a-movie-database-with-neo4js-knowledge-graph-sandbox/) 项目分享到 [Docker](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) [容器](https://thenewstack.io/containers/) 上，以便可能与可以帮助该项目的人员进行工作和修改。再次强调，这不是一个商业项目，而是一个涉及海洋数据分析的沙盒项目。

然而，我与至少两位开发人员交谈过，他们坚决反对这样做，他们说我需要 [GitHub](https://thenewstack.io/this-year-in-programming-go-rust-github-lead-2021-stories/) 或 [git](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) 来进行任何工作，原因有很多——我所知道的，也是众所周知的——例如它的系统化方法、它对拉取请求的有效性以及它跟踪和审计过去更改的能力等等。

但再次强调，我想要一些简单的东西，我认为只需要最多两三个人来审查应用程序中的代码，仅此而已，因为其他所有事情都将由我来做。当在我的项目中使用来自其他运行时的代码时，我也可以使用来自 [DockerHub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/) 的经过硬化的 [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) 容器来确保安全性，而不是必须费心处理签名和 [SBOM](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) 等等。由于 Chainguard 持续更新其容器镜像，因此您可以将安全更新交给它来管理。

在寻找分享我的知识图谱应用程序的正确选项时，我想起了 Chainguard 开发者关系倡导者 [Adrian Mouat](https://www.linkedin.com/in/adrianmouat/) 在今年早些时候在巴黎举行的 KubeCon + CloudNativeCon EU 上发表的演讲。该演讲名为“以现代方式构建容器镜像”（我当时就在那里听演讲，而且座无虚席）。

使用

[@dagger_io] 来构建管道输入：[Chainguard] 的“以现代方式构建容器镜像”——[Chainguard] 的 Adrian Mouat 演示。他说，它的“真正优势”在于它的模块。[@KubeCon_][@linuxfoundation][@thenewstack][pic.twitter.com/bTCpBcuV1C]— BC Gain (@bcamerongain)

[2024 年 3 月 22 日]

我从中学到的关键要素，不一定是针对我的项目，而是总体而言，是 GitHub 确实一直是部署和其他许多方面的首选方式。但是，它可以通过改进得到补充，尤其是在管道 CI/CD 组织方面。

Docker 专门针对 CI/CD 而言，存在不足。虽然回到我的原始项目，是的，我认为 Docker 非常适合我想要做的事情。但事实证明，再次强调，对于 CI/CD 而言，Docker 确实存在缺点，在某些安全方面也是如此。

Mouat 演讲中提出的一个关键点是，[Dagger](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/) 似乎非常适合 CI/CD，此外，它还可以与 GitHub 集成以用于 CI/CD 项目，正如 Mouat 所解释的那样。

## 我想要我的 CI/CD

Dagger 通过容器化提供可编程的 CI/CD。但如上所述，这不是非此即彼的情况，就像我的项目一样。再次强调，我的项目只是关于将一个简单的应用程序打包到容器中，然后发送给几个人。它绝对不是一个完整的 CI/CD 类型的协作。

正如 Mouat 在他的演讲中所定义的那样，Dagger 是一种利用 [BuildKit](https://docs.docker.com/build/buildkit/) 的强大功能来定义代码中的 CI/CD 管道的工具。他说，它擅长创建可以在项目之间重复使用的复杂构建管道，并提供强大的缓存和并行功能。

这些可重复使用的容器中的构建管道是关键。

“将可重复使用的构建管道定义为代码是减少 [DevOps](https://thenewstack.io/devops/) 复杂性和增强安全性和合规性的关键先决条件。允许开发人员使用他们熟悉的 Docker BuildKit 工具在本地运行这些管道，可以自动确保开发和生产环境之间的一致性，”TechTarget 的企业战略集团分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 说。“这对实施策略驱动的安全至关重要，可以提高开发人员的生产力，同时确保安全性。”

再次强调，Dagger 可以与 GitHub、[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 或纯 git 集成，或者可以集成。因此，在许多方面，您都获得了两全其美，兼具安全性方面和简化性。
CI/CD pipelines' programmability and the different options Dagger provides make it particularly well-suited for CI/CD. This is where a simple Docker container, while great for my project, might fall short—at least according to [Sam Alba](https://www.linkedin.com/in/samalba/), co-founder and VP of Engineering at Dagger and former VP of Engineering at Docker.

Before the Dagger project was created in 2018, [Alba wrote in a blog post on The New Stack](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/): "While we've made great progress, there's still a lot of work to be done, especially beyond containers as the only unit and orchestrating pipelines of containers."

During his time at Docker, "the overall automation of the software supply chain" wasn't addressed, Alba wrote: "We unlocked so much value at the end of the supply chain, but didn't adequately address the needs of developers when they're coding and collaborating, and CI/CD is still a mess today."

For local image sharing, Docker can be great. In his presentation, Mouat demonstrated the feasibility of using an upstream [Golang](https://thenewstack.io/golang-what-are-constants-in-go-and-how-do-you-use-them/) image, compiling it in a [Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/) application, and setting up the entry point.

"As you might know, this does work. The problem is, we still have our build tools in that image," Mouat said. "So, our final image doesn't just contain our application. It contains all the build tools, and all the stuff in the underlying Debian operating system that we don't actually need to run the application. Ideally, I want to get rid of it because it's just a source of potential CVEs [Common Vulnerabilities and Exposures] and problems."

As Mouat said in his presentation, Dagger isn't just designed to build container images. It's actually designed to solve the entire CI/CD problem, "you're trying to debug CI/CD, but it works differently," Mouat said. "You can't run it locally, or at least the way it runs locally is different from the way it runs remotely, and you end up with 20 commits that are all like, 'This works, kind of,'" Mouat said. "It keeps failing, and you're going crazy. That's what Dagger is aiming to solve."

## The Right Container
Docker is still king in many ways, including its lightweight nature and repeatability. While it may be limited in some ways, it's perfectly sufficient for other use cases. This is evident in my project, where I just want to share my Neo4j knowledge graph with a few people.

However, for full CI/CD, especially the security challenges associated with it, Dagger is worth serious consideration. This also aligns with the established need for [shifting left](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), which remains a challenge.

"Shifting left software supply chain security and compliance is the only way to limit operational risk for organizations, and it has even become a prerequisite for working with most governments. Building policy-based security management into the software supply chain lays the foundation for a stronger security posture," Volk said. "This protects the entire software supply chain in a proactive, automated way, without ultimately becoming seaweed on the anchor of application developers. This makes CIOs very happy."

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)