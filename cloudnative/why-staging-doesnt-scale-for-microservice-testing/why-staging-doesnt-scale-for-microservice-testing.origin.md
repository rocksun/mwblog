# Why Staging Doesn’t Scale for Microservice Testing
![Featued image for: Why Staging Doesn’t Scale for Microservice Testing](https://cdn.thenewstack.io/media/2024/08/7348bf94-staging-doesnt-scale-microservice-testing-1024x576.jpg)
Picture this: You’re a developer in a midsized engineering team. You’ve just finished coding a brilliant new feature. You’re excited to deploy it to staging for testing. But wait… what’s this? Staging is broken. Again.

Sound familiar? If you’re nodding your head in frustration, you’re not alone. The eternal struggle with staging environments is a tale as old as software development itself.

## The High Stakes of Staging
Before we dive into the nitty-gritty, let’s address the elephant in the room: Why should you care about staging environments? The answer is simple: They’re the last line of defense between your code and production. In today’s world of [microservices architectures](https://thenewstack.io/microservices/) and continuous delivery, the importance of a stable staging environment cannot be overstated.

Consider this: According to the [2021 State of DevOps report](https://cloud.google.com/resources/state-of-devops), high-performing IT organizations deploy code 973 times more frequently than low-performing organizations. That’s a lot of code changes hitting staging environments every day. If these environments are unstable or unreliable, it’s like trying to build a house on quicksand — disaster is inevitable.

The impact of a broken staging environment is far-reaching:

**Release delays**: When staging is unstable, your carefully planned release schedule goes out the window. Suddenly, that feature you promised for next week is looking more like next month.**Developer productivity**: Nothing kills productivity faster than waiting for a staging environment to become available or stable. It’s like being stuck in traffic when you’re already late for an important meeting.**Quality assurance nightmares**: If staging is unreliable, how can you trust your testing is valid? It’s like trying to proofread a book while someone keeps changing the words.**Increased production risks**: When staging fails to catch bugs, they slip into production. And we all know that fixing a bug in production is like performing surgery on a patient who’s running a marathon.
## The Catch-22 of Staging Environments
Now, let’s address the core of the problem. Why are staging environments hard to keep stable? We’re dealing with a classic Catch-22 situation:

- Developers need a stable staging environment to test their code changes.
- The act of deploying code changes to test can render the environment unstable for others.
Welcome to the world of staging environments!

## Current Solutions (Or Should We Say Band-Aids?)
Over the years, engineering teams have come up with various workarounds to this problem. Let’s take a look at some of these “solutions” and their pros and cons.

### 1. The Slack Lock
Some teams use Slack to “lock” the staging environment for testing. It goes something like this:

Developer A: “Locking staging for the next hour. Don’t touch!”
Developer B: “But I need to test my critical bug fix!”
Developer A: “Too bad, I was here first!

While this might work for a team of three developers and a pet hamster, it doesn’t scale beyond that. It’s like having a single bathroom for an entire office building — chaos is inevitable.

### 2. Feature Flags Galore
Other teams turn to feature flags, thinking they’ve found the Holy Grail of staging management. The idea is to disable new code on staging until it’s ready for testing.

But here’s the catch: You still need to enable that flag eventually, and guess what? You’re right back where you started, fighting for a stable environment to test your now-enabled feature.

### 3. Environment Proliferation
Some organizations decide to spin up multiple “lower” environments. The theory is that developers can use these for initial testing before moving to the “official” staging environment. Sounds great, right?

Wrong. This approach is like solving a traffic jam by building more highways. Sure, it might help initially, but soon enough, you’re just dealing with the same problem on a larger scale.

The shortcomings of this approach are significant. Lower environments often lack full integration with third-party services, relying instead on mocks that don’t truly represent production behavior. Coordinating updates across multiple environments becomes a logistical nightmare, introducing inconsistencies and errors. The resource drain is substantial, both in terms of infrastructure costs and ongoing maintenance.

Perhaps most insidiously, these lower environments can create a false sense of security. They might not reveal issues that would occur in a full staging or production setup, leading to nasty surprises down the line. As your microservices architecture grows, so does the complexity of maintaining these multiple environments.

The irony is palpable — in trying to solve the staging environment problem, we’ve created a hydra of new issues. It’s a classic case of treating the symptom rather than the disease. What we need isn’t more environments but smarter ways to use the environments we have.

### 4. The Mock Madness
Another approach to tackle staging environment issues is using mocks for [integration testing](https://thenewstack.io/the-struggle-for-microservice-integration-testing/) before code is merged. This method has its merits but also comes with significant challenges.

On the positive side, mocks can provide a quick and lightweight way to simulate dependencies, allowing developers to test their code in isolation. This can speed up the development process and catch basic integration issues early. For simple systems or well-defined interfaces, mocks can be an effective tool in the testing arsenal.

However, as systems grow in complexity, the limitations of mocking become more apparent. Maintaining accurate mocks of service dependencies requires significant effort, especially in a rapidly evolving microservices environment. As services change, mocks need to be updated accordingly, which can become a time-consuming task.

Moreover, while mocks can catch certain types of issues, they may miss subtle interactions that only occur in a real integrated environment. This can lead to a false sense of security, where code passes all mock-based [tests but fails in actual integration](https://thenewstack.io/the-struggle-for-microservice-integration-testing/) scenarios.

The effort required to maintain comprehensive and up-to-date mocks often grows exponentially with the complexity of the system. At a certain point, the time invested in creating and updating mocks may outweigh the benefits they provide, especially when compared to testing in a more realistic environment.

## The Light at the End of the Tunnel
So are we doomed to live in a world where staging is eternally broken? As we’ve seen, traditional approaches to staging environments are fraught with challenges. To overcome these, we need to think differently.

This brings us to a promising new approach: canary-style testing in [shared environments](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/). This method allows developers to test their changes in isolation within a shared staging environment. It works by creating a “shadow” deployment of the services affected by a developer’s changes while leaving the rest of the environment untouched. This approach is similar to canary deployments in production but applied to the staging environment.

The key benefit is that developers can share an [environment without affecting each other’s work](https://thenewstack.io/environment-replication-doesnt-work-for-microservices/). When a developer wants to test a change, the system creates a unique path through the environment that includes their modified services, while using the existing versions of all other services.

Moreover, this approach enables testing at the granularity of every code change or [pull request](https://thenewstack.io/demo-testing-and-previewing-pull-requests-with-signadot/). This means developers can catch issues very early in the development process, often before the code is merged into the main branch. By identifying problems at this stage, teams can significantly reduce the likelihood of introducing bugs into the shared codebase.

This method provides the isolation needed for thorough testing without the overhead of managing multiple complete environments. It allows teams to test thoroughly in a production-like setting, catch issues early and maintain a stable shared environment all at the same time.

As [Kent C. Dodds](https://kentcdodds.com/), a renowned software engineer and educator, wrote:

The more your tests resemble the way your software is used, the more confidence they can give you.

— Kent C. Dodds 🌌 (@kentcdodds)

[March 23, 2018]
## Industry Leaders Paving the Way
This approach isn’t just a pipe dream; it’s being successfully implemented by some of the most innovative companies in the tech world:

**DoorDash’s fast feedback loop:**DoorDash implemented a system to enhance the feedback loop for[Kubernetes](https://roadmap.sh/kubernetes)product development within a production environment. This setup allows quick iterations and robust testing of new features directly in the production environment, thereby speeding up development without compromising on the quality or performance of the service.[Read more on DoorDash’s engineering blog](https://doordash.engineering/2022/06/23/fast-feedback-loop-for-kubernetes-product-development-in-a-production-environment/).**Uber’s SLATE:**Uber addresses staging environment challenges with SLATE (Short-Lived Application Testing Environment), allowing developers to create on-demand, ephemeral testing environments that integrate production instances of dependencies. This setup enhances isolation and increases development velocity, providing a robust solution for end-to-end testing needs while minimizing the impact on production systems.[Read more about SLATE on Uber’s blog](https://www.uber.com/blog/simplifying-developer-testing-through-slate/).**Lyft’s environment management:**Lyft developed a sophisticated control plane for managing its shared development environment, significantly simplifying the complexity associated with its microservices architecture. This system enhances developer productivity by improving the management and visibility of service dependencies within staging and development environments.[Learn about Lyft’s approach on its engineering blog](https://eng.lyft.com/building-a-control-plane-for-lyfts-shared-development-environment-6a40266fcf5e).
These industry leaders have recognized the power of safely sharing environments in solving the eternal staging dilemma. By adopting this approach, they’ve been able to increase developer productivity, improve code quality and accelerate release cycles.

## The Benefits of Safely Sharing Staging Environments
**Cost effectiveness**: Eliminate the need for multiple, resource-intensive environments.**Isolated testing**: Developers can test changes without affecting others’ work.**Early issue detection**: Catch problems at the individual code change level, before merging.**Realistic testing**: Use a shared environment that closely mirrors production.**Scalable**: Accommodate large teams and complex microservices architectures.
With cloud native infrastructure involving Kubernetes and service meshes like Istio and Linkerd, it’s easier than ever to implement sophisticated routing that enables safe sharing of staging environments. This approach allows teams to validate changes using a “canary on staging” strategy, providing a powerful way to catch issues early while maintaining a stable shared environment.

Moreover, this approach enables powerful capabilities like “feature previews.” These allow development teams to create temporary, isolated versions of their services that showcase specific features or changes. Product managers, QA teams and UX designers can then access these previews through mobile or web frontends, just as an end user would.

This capability allows comprehensive testing and early feedback on new features while they’re still being developed. Stakeholders can interact with the feature in a realistic environment, identifying potential issues or improvements before the code is finalized.

By facilitating this level of collaboration and early testing, feature previews significantly streamline the software delivery process. They reduce the likelihood of late-stage changes, improve the quality of features before they reach production and ultimately lead to faster, more confident releases.

## Conclusion: A New Era for Staging
The struggle with staging environments has been a persistent challenge for development teams. It’s time to break free from the cycle of broken staging environments, delayed releases and frustrated developers.

By adopting an approach that allows safe sharing of staging environments, teams can address the core issues that have plagued preproduction testing for years. This strategy turns the traditional Catch-22 on its head: Instead of deployments destabilizing the staging environment, this approach enhances stability with each test.

Perhaps most importantly, this approach moves teams closer to the ideal state where the main branch is always ready for production deployments. By enabling comprehensive testing before code is merged, the majority of issues are caught and resolved early, significantly reducing the risk of post-merge surprises.

Curious to learn more about how you can implement these strategies in your development process? Visit [Signadot’s](https://www.signadot.com/) website to discover how you can bring stability to your staging environment, efficiency to your development workflow and confidence to your releases. Your team’s productivity (and sanity) will thank you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)