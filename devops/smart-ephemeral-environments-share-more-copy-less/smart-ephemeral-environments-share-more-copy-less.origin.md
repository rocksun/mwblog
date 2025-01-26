# Smart Ephemeral Environments: Share More, Copy Less
![Featued image for: Smart Ephemeral Environments: Share More, Copy Less](https://cdn.thenewstack.io/media/2025/01/f03d8ac1-testing12-1024x574.png)
Just last week, I was speaking with an engineering director at a fast-growing security company. Its team of 50 engineers had implemented something that made me pause: a sign-up system for developers to test on staging. Yes, you read that right: Engineers were having to wait in line for their turn to deploy and test their code changes. By Friday afternoons, the backlog would grow frustratingly long, with developers stuck waiting hours for their chance to verify their work. While creative, this was a clear sign of a deeper problem that I’ve seen repeatedly in growing engineering organizations.

This situation perfectly illustrates how [ traditional approaches to testing microservices](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/) don’t scale with team growth. When organizations break down their monoliths into microservices to enable independent development and deployment, they often overlook a critical aspect: Their testing strategy needs to evolve as well.

**The Traditional Testing Bottleneck**
The typical approach is to accumulate code changes and [test them in batches in a shared environment](https://thenewstack.io/why-environment-replication-doesnt-work-for-microservices-testing/). While this might work initially, it quickly becomes a bottleneck as teams grow. Let me paint a picture of what this looks like in practice:

A developer makes a change and waits hours to get it into the shared environment. When tests fail, they’re forced to context-switch back to code they wrote hours ago — or sometimes days ago. If multiple teams are pushing changes, debugging becomes a detective mission. Was it their change that broke things or someone else’s? In the worst cases, developers start finding workarounds, like testing directly in production, leading to even more problems down the line.

**The Infrastructure Cost Trap**
Many organizations try to solve this by creating multiple replicated environments. Teams start spinning up complete copies of their infrastructure, thinking it will solve the contention problem. Take [Brex’s experience](https://www.signadot.com/blog/how-brex-transformed-developer-experience-and-slashed-infrastructure-costs-with-signadot), for example. With a 1000+ microservices architecture, it found that preview environments were nearly as expensive as its production environment. The approach wasn’t just costly: Environments took an hour to spin up initially, and even after significant optimization, developers still faced 20- to 30-minute wait times.

**A New Paradigm: Shared Baseline Testing**
Leading technology companies like [Uber](https://www.uber.com/blog/simplifying-developer-testing-through-slate/), [Lyft](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f) and [DoorDash](https://careersatdoordash.com/blog/fast-feedback-loop-for-kubernetes-product-development-in-a-production-environment/) have pioneered a different approach. Instead of [duplicating entire environments](https://thenewstack.io/why-duplicating-environments-for-microservices-backfires/), they’ve moved to a model of isolating requests within a shared environment. This fundamental shift brings several key advantages:

First, it’s incredibly cost-efficient. You can support thousands of concurrent tests using a fraction of the infrastructure required by traditional approaches. Second, it’s fast. [Developers can begin testing](https://thenewstack.io/is-the-testing-pyramid-broken/) within seconds rather than waiting for environments to spin up. Most importantly, it scales naturally with team growth since you’re sharing infrastructure efficiently while maintaining perfect isolation for testing.

Let me dive into how this works in practice.

**How Shared Baseline Testing Works**
The key insight behind this approach is that, for most microservices testing, you don’t need to duplicate all your infrastructure. You just need to control the request path through your system. Think of it like having multiple parallel lanes of traffic flowing through the same highway infrastructure.

When a developer wants to test a change, they simply deploy their modified service alongside the existing production version. Special routing rules ensure that their test traffic flows through their version of the service while all other traffic continues through the production version. This [isolation extends through the entire request chain](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/), making it possible to test complex end-to-end scenarios safely.

This approach can be particularly powerful, allowing developers to collaborate naturally. Want to test how your frontend changes work with a colleague’s backend modifications? Simply combine your routing rules to create a unified test environment within seconds. This level of flexibility was simply impossible with traditional environment-based isolation.

**Real-World Impact**
The impact of this approach goes beyond just saving infrastructure costs. At Brex, moving to this model not only dramatically reduced its infrastructure spend but also led to measurable improvements in developer productivity and code quality. Engineers could iterate faster, leading to smaller, more focused changes and reduced change failure rates.

But changes in developer behavior are perhaps the most telling impact. When testing becomes fast and friction-free, teams naturally adopt better practices. Instead of batching changes to avoid environment setup time, they test more frequently. Instead of writing large, risky changes, they break them down into smaller, more manageable pieces. The result is a more sustainable and scalable development process.

**The Signadot Approach**
At Signadot, we’ve built a platform that brings the power of shared baseline testing to any team using Kubernetes, without requiring the massive engineering investment that companies like Uber and Lyft made internally. With just a pull request, developers get instant access to isolated test environments that perfectly mirror production, eliminating the wait times and debugging headaches that come with traditional approaches.

Would you like to get started? Check out our [quick start](https://www.signadot.com/docs/tutorials/quickstart/first-sandbox) guide or join our [Slack community](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email) to learn from others who have made this transition.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)