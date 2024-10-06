# Why Staging Is a Bottleneck for Microservice Testing
![Featued image for: Why Staging Is a Bottleneck for Microservice Testing](https://cdn.thenewstack.io/media/2024/10/314e8cee-bottleneck-1024x576.jpg)
A typical CI/CD workflow for engineering teams adopting [microservices architecture](https://thenewstack.io/microservices/) looks something like this:

- Build and run basic unit tests before merging the pull request (PR).
- After merging the PR, a CI/CD pipeline deploys the build to a shared staging environment.
- Integration and end-to-end (E2E) tests are run on this environment, often scheduled in batches.
For every microservice, there could be multiple deployments to the staging environment each day. While this setup has become the norm, shared staging environments often create bottlenecks that slow down teams and undermine the advantages of microservices. Let’s dive into why this happens and how leading engineering teams are moving beyond staging to [scale testing effectively](https://thenewstack.io/why-staging-doesnt-scale-for-microservice-testing/).

## The Fragility of Shared Staging Environments
**One PR, many problems**: When one team deploys a PR with bugs to staging, it can disrupt the entire engineering team. This problem is exacerbated in shared staging environments, where a bug from one team can block multiple others.**Finding the offending PR is a needle in a haystack**: With hundreds of PRs being merged daily, finding the one that broke the environment is time-consuming.**Test failures are ambiguous**: Dependencies between microservices make it challenging to isolate why a test fails. For example, consider the following e-commerce microservices architecture:
Source:

[DeathStarBench](https://github.com/delimitrou/DeathStarBench), an open source benchmark suite for cloud microservicesIn this architecture, multiple services such as payment, orders, shipping and media interact with each other. A failure in one service, such as the payment service, might not be immediately obvious and could manifest as a problem in the orders service. These interdependencies make it difficult to pinpoint the root cause of test failures, especially when many services are involved. Debugging failures in such a complex web of microservices is time-consuming, as each service may have different teams responsible for maintaining it.

**Feature testing becomes a waiting game**: Multiple teams often wait for their turn to test features in staging. This creates bottlenecks. The pressure on teams to share resources can severely delay releases, as they fight for access to the staging environment. Developers who attempt to spin up the entire stack on their local machines for testing run into similar issues. As[distributed systems engineer Cindy Sridharan notes](https://copyconstruct.medium.com/testing-microservices-the-sane-way-9bb31d158c16), “I now believe trying to spin up the full stack on developer laptops is fundamentally the wrong mindset to begin with, be it at startups or at bigger companies.” The complexities of microservices make it impractical to replicate entire environments locally, just as it’s difficult to maintain shared staging environments at scale.**Delayed feedback from scheduled tests**: Automated tests are often scheduled for off-peak hours, like nightly runs. By the time a failure is detected, several PRs may have been deployed, making it even harder to track down the offending code. This delays the feedback loop and introduces a “time tax” on productivity.
## Ripple Effect: Slowing Down Engineering and Lowering Quality
These issues lead to a substantial drain on developer productivity. Bottlenecks in CI/CD pipelines cause them to spend more time debugging than coding. If your engineering team is losing several days a month to staging-related issues, that’s a serious hit to both your velocity and morale.

From a release process perspective, the delays caused by a fragile staging environment lead to slower shipping of features and patches. When teams spend more time fixing staging issues than building new features, product development slows down. In fast-moving industries, this can be a major competitive disadvantage.

If your release process is painful, you ship less often, and the cost of mistakes in production is higher. This slowdown can also compromise product quality, as engineers, under pressure to meet deadlines, may skip adding new test cases. The result? Bugs find their way into production. For e-commerce companies, for example, even a minor bug can disrupt the checkout process, leading to loss of revenue and damage to the brand.

Finally, there’s the impact on developer experience. Developers thrive in environments where they can ship code quickly and efficiently. Friction in the release process frustrates developers, increasing burnout and turnover. Happy developers write better code, and frictionless release processes are key to that.

## Why Staging Breaks Down: The Contention Problem
At its core, the issue with shared staging environments is contention. Teams cannot safely test their changes in isolation. This lack of isolation leads to bottlenecks, blocking teams from efficiently validating their work.

As Sridharan aptly puts it:

![As an industry, we're beholden to test methodologies invented in an era vastly different to the current one we're in.](https://cdn.thenewstack.io/media/2024/10/da8b83f4-image2-300x165.jpg)
Quote by Sridharan

Staging environments were designed with monolithic applications in mind, not for the dynamic, decentralized nature of microservices.

A naive approach might be to create more staging environments, but this doesn’t scale well either. Managing multiple environments introduces more complexity, and as noted in “[Environment Replication Doesn’t Work for Microservices](https://thenewstack.io/environment-replication-doesnt-work-for-microservices/),” replicating environments accurately across microservices is extremely difficult and costly.

## A Better Approach: Isolated Testing
So what’s the solution? Some of the most innovative companies in tech — like Uber, Lyft and DoorDash — have moved away from shared staging environments. They’ve developed methods to test in isolation by sandboxing services and using dynamic traffic routing.

As the [Lyft blog post](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f) on staging overrides notes:

“We fundamentally shifted our approach for the isolation model: instead of providing fully isolated environments, we isolated requests within a shared environment.”

By isolating microservice changes, teams avoid contention and can test code independently. This model of isolated testing eliminates the problems caused by shared environments and enables true continuous delivery. Isolated [testing allows teams to catch issues early in the development cycle](https://thenewstack.io/is-the-testing-pyramid-broken/), reducing the complexity and cost of fixing bugs later on.

## Isolated Testing in Action
Building in-house systems to achieve this level of isolation can be technically complex and costly. However, platforms like [Signadot](https://www.signadot.com?utm_content=inline+mention) offer solutions to provide isolated testing environments at scale. Thanks to sandboxing and traffic routing, teams can [test microservices safely and efficiently](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/) without the need for traditional staging environments.

## Conclusion: The Future of Testing Microservices
Staging environments worked well for monolithic applications but have outlived their usefulness for today’s microservice architectures. As engineering teams scale, shared environments introduce costly delays, reduce quality and frustrate developers.

The future of [testing microservices lies in isolated testing](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/). By moving away from shared environments, teams can test in parallel, enabling faster, higher-quality releases. In a world where speed, quality and developer happiness are paramount, isolated testing is not just a nice-to-have — it’s essential.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)