## Docker Testcontainers 现已在 Red Hat 的 OpenShift 上推出

![Docker Testcontainers 现已在 Red Hat 的 OpenShift 上推出](https://cdn.thenewstack.io/media/2024/04/485e2f45-87e0-4fc7-8817-0e3a58f97565-1-1024x768.jpg)

巴黎 —

[Docker](https://www.docker.com/?utm_content=inline+mention) 的 [Testcontainers](https://thenewstack.io/how-testcontainers-is-demonstrating-value-as-a-key-ci-tool/) Cloud 现已直接在 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 OpenShift 上推出。这意味着大量围绕使用这些容器进行测试、合规和其他 CD 方面的操作现已直接在 [OpenShift](https://www.redhat.com/fr/technologies/cloud-computing/openshift/red-hat-openshift-kubernetes) 集群中提供。这对于 [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) 社区来说也是一大福音，Testcontainers Cloud 在该社区中很受欢迎，同时它也支持 Java 以外的其他语言。

但首先，你为什么要关心使用 Testcontainers Cloud 进行 CI？这是因为 Testcontainers Cloud（Docker 在 12 月收购 [AtomicJar](https://www.atomicjar.com/) 时获得）为开发人员提供了一种方法，让他们可以超越其通常孤立的开发环境。如果没有某些 [CI 平台](https://thenewstack.io/ci-cd/) 和工具，开发人员可能无法直接访问应用程序开发流程之外的外壳或集群。因此，一旦它在 [Amazon AWS](https://aws.amazon.com/?utm_content=inline+mention) ECS 等集群上加载、利用或集成，它可能会被退回给开发人员进行更多工作。

而使用 [Docker Testcontainers Cloud](https://testcontainers.com/)，它可以在 CI 流程中直接重新配置或测试，从而节省大量麻烦。现在，它可用于测试和其他方面（无论是策略和合规性、治理等）这一事实意味着开发人员可以在本地进行迭代。他们可以受益于在 OpenShift 集群上安全运行的工作负载。

根据 Docker 容器文档，Testcontainers Cloud 被描述为一个开源框架，用于提供测试依赖项的“一次性”轻量级实例。通过直接在测试中将依赖项定义为代码，可以更轻松地进行可重复测试。除了 Java 之外，Testcontainers Cloud 库还适用于所有流行语言，包括 [Golang](https://go.dev/) .NET、[Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)、[Rust](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/) 和 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/)。单元测试使测试可以在本地和 CI 中运行。

同样，代码在开发过程中会针对 CI 进行检查和审查。在此开发过程中增加了透明度，以便他们不仅仅将代码通过围栏扔到集群上，然后可能被踢回来，这种情况经常发生，会浪费开发人员、[SRE](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/) 和其他利益相关者的时间。

现在，Testcontainers Cloud 直接集成在 Docker 保护伞下，可以在 Docker Hub 上访问，并直接与 OpenShift 集成。正如 Docker 首席技术官 [Justin Cormack](https://uk.linkedin.com/in/justincormack) 在巴黎举行的 KubeCon + CloudNativeCon Europe 期间告诉 The New Stack，“测试容器用户和 Red Hat 用户之间有很大的重叠。这是一个 Java 社区。”

此外，“Java 是 Testcontainers Cloud 的起点，尽管它现在也可用于其他语言。但 Java 仍然是最强大的核心社区，”Cormack 说。“Red Hat 也有强大的 Java 影响力。所以很多人都在做这件事。”

Cormack 指出，Docker Testcontainers Cloud 代表 Docker 提供了一个本地云产品，控制平面由 Docker 提供，数据平面保留在你的集群上，Cormack 说。“因此，这吸引了开发人员和不仅仅是开发人员的人员，吸引了 REHL 用户和 OpenShift 人员，他们也使用 Docker 容器，”Cormack 说。“以前，当你必须尝试自己构建这样的东西时，由于各种技术原因，这真的很难，而且非常混乱。当你已经在容器中时，你正在启动容器。”

## 减少认知负荷

作为 Red Hat 的
## Improving Developer Experience with Testcontainers and OpenShift

[Thomas Quast](https://twitter.com/t_millstream), product manager, and [Sergey Yegorov](https://github.com/bsideup), vice president of product and engineering for Docker, co-founded Testcontainers Cloud. In a [blog post](https://www.redhat.com/en/blog/improving-developer-experience-testcontainers-and-openshift?sc_cid=701f2000000tyN6AAI), they wrote that reducing developers' cognitive load is key to improving their productivity. They cited statistics from a Salesforce survey that showed [76% of organizations](https://www.salesforce.com/news/stories/new-research-shows-how-to-keep-developers-happy-amid-the-great-resignation/) reported that developers experience high cognitive load, which contributes to low productivity. Quast and Yegorov wrote that Testcontainers Cloud can reduce cognitive load and improve productivity by integrating CI support with platform engineering. According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-11-28-gartner-hype-cycle-shows-ai-practices-and-platform-engineering-will-reach-mainstream-adoption-in-software-engineering-in-two-to-five-years), 80% of software engineering organizations will establish platform teams as internal providers of reusable services, components, and application delivery tooling by 2026. "The Testcontainers Cloud team at Red Hat and Docker have collaborated to make the full power of Testcontainers Cloud available in OpenShift, while still leveraging the enterprise governance, security and compliance, and overall flexibility of the platform," Quast and Yegorov wrote.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

Technology moves fast. Don't miss a single episode. Subscribe to our YouTube channel to stream all of our podcasts, interviews, demos, and more.