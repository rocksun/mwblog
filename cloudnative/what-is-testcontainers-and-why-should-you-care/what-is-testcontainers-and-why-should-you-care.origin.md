# What Is Testcontainers, and Why Should You Care?
![Featued image for: What Is Testcontainers, and Why Should You Care?](https://cdn.thenewstack.io/media/2024/09/d2ea2f8b-what-are-testcontainers-1024x576.jpg)
In modern software development, with its ongoing trend toward distributed system and
[microservice architectures](https://thenewstack.io/microservices/) with a big integration surface, writing software also means integrating with other systems. Integration tests are a great tool for ensuring the ongoing correctness of the system under test and for providing fast and constant feedback on the system’s behavior during the development cycle.
Integration tests, however, often require external dependencies, such as databases, message brokers or web servers, all with their own idiosyncrasies on how to be configured and run correctly. Traditionally, managing these dependencies has been cumbersome, prone to inconsistencies and difficult to replicate across different machines.
Historically this gave integration tests a bad reputation for being expensive to write and maintain. You either had to follow potentially outdated documentation to set up the environment in a laborious manual way (only to end up with a slightly broken environment) or use centrally maintained shared test environments that often resulted in test pollution.
This is where
[Testcontainers](https://testcontainers.com/) comes in. My colleague [Oleg Šelajev](https://2024.allthingsopen.org/speakers/oleg-selajev) will be presenting this at All Things Open 2024, in a talk titled “ [Making your own Testcontainers module for fun and profit!](https://2024.allthingsopen.org/sessions/making-your-own-testcontainers-module-for-fun-and-profit)”
## Meet Testcontainers
Testcontainers is an open source library for providing throwaway, lightweight instances of databases, message brokers, web browsers or just about anything that can run in a Docker container. By leveraging
[Docker](https://www.docker.com/?utm_content=inline+mention) to spin up lightweight, isolated instances of these services on demand and from within your codebase, Testcontainers solves the problem of environment management during testing and development.
Testcontainers allows developers to create reliable and repeatable test and development environments with minimal effort in an
[Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/) method. It uses familiar languages for writing the production and test code and helping ensure that the code is tested against real, consistent services. This approach reduces the friction in setting up and tearing down test environments and makes tests more reliable and easier to maintain. For developers, Testcontainers is a game-changer, streamlining the testing process and enabling more confident, robust development.
### Cleanup
Testcontainers also takes care of automatic cleanup of all
[Docker](https://roadmap.sh/docker) resources it creates, ensuring that your system remains free of clutter after tests are run. This cleanup process is seamlessly integrated with the test framework you are using, such as JUnit, where containers are automatically stopped and removed after the test execution.
Additionally, Testcontainers relies on a specialized sidecar container called
[Ryuk](https://hub.docker.com/r/testcontainers/ryuk), which monitors and ensures that all resources are properly cleaned up, even in cases where the test process might crash or terminate unexpectedly. By binding this cleanup process to the lifecycle of your test process and using Ryuk as a watchdog, Testcontainers guarantees that no stray containers, networks or volumes are left behind, keeping your environment clean and minimizing the risk of resource exhaustion or conflicts in subsequent test runs.
### Modules
Testcontainers offers a rich set of modules that encapsulate best practices for using containers in the context of testing, making it even easier to integrate various technologies into your test suites. These modules are preconfigured Docker containers tailored for specific technologies, such as databases (e.g.,
[PostgreSQL](https://roadmap.sh/postgresql-dba), MySQL), message brokers (e.g., [Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/), RabbitMQ) or even full-fledged application environments like Selenium for browser testing.
By using these modules, developers can leverage tried-and-tested configurations that have been optimized for reliability and efficiency in testing scenarios. The
[Testcontainers modules catalog](https://testcontainers.com/modules/) provides a comprehensive listing of available modules, allowing you to quickly find and implement the containerized services you need.
Here are two minimal examples showcasing the same action both in
[Java](https://thenewstack.io/java/) and [Go](https://thenewstack.io/go/): How to define a Docker container using a [Redis](https://redis.com/?utm_content=inline+mention) image, configuring its exposed port and starting the container in a way that will wait for the readiness of the Redis application within the container.
In Java:
|
1
2
3
|
GenericContainer redis = new GenericContainer("redis:5.0.3-alpine")
.withExposedPorts(379);
redis.start()
In Go:
|
1
2
3
4
5
6
7
8
|
container, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
ContainerRequest: testcontainers.ContainerRequest{
Image: "redis:5.0.3-alpine",
ExposedPorts: []string{"6379/tcp"},
WaitingFor: wait.ForLog("Ready to accept connections"),
},
Started: true,
})
### Testcontainers Cloud
Besides these widely established open source libraries, Testcontainers offers a product to offload those containers seamlessly into the cloud, without requiring any changes to your Testcontainers code whatsoever:
[Testcontainers Cloud](https://testcontainers.com/cloud/). By leveraging Testcontainers Cloud, you can significantly reduce the load on your local machine, freeing up resources for other tasks while still running complex, resource-intensive tests.
This approach speeds up your development workflow and gives your testing environment architectural parity with the desired Docker runtime (e.g., x86) as the containers are executed in a consistent and scalable cloud environment. Whether you’re dealing with heavy workloads or simply want to streamline your testing process, Testcontainers Cloud provides a seamless integration that enhances both performance and reliability, allowing you to focus more on coding and less on managing local resources.
## Wrapping Up
Testcontainers is a versatile and powerful tool that transforms how developers approach integration testing and local development. By providing an easy-to-use interface for spinning up Docker containers tailored to specific testing needs that is accessible straight from the familiarity of the utilized programming language, Testcontainers eliminates the common challenges associated with managing test environments.
With modules that encapsulate best practices, automatic cleanup to keep your system tidy, and the ability to offload container execution to Testcontainers Cloud, this approach offers a comprehensive solution for maintaining consistency, reliability and efficiency in your testing processes.
Whether you’re a developer looking to streamline your local workflow or a team aiming to scale your testing in the cloud, Testcontainers equips you with the tools necessary to ensure that your code works seamlessly across different environments. By adopting Testcontainers, you not only enhance the quality of your tests but also pave the way for a more robust and confident development cycle.
**Don’t miss our All Things Open 2024 session: Making your own Testcontainers module for fun and profit!**
## Learn More
- For the latest Testcontainers news, subscribe to the
[Docker Newsletter](https://www.docker.com/newsletter-subscription/).
- Get started with Testcontainers Cloud by
[creating a free account](https://testcontainers.com/cloud).
- Have questions on Testcontainers? Connect on the
[Testcontainers Slack](https://testcontainers.slack.com/).
- Learn about
[Testcontainers best practices](https://www.docker.com/blog/testcontainers-best-practices/).
- Get started with the
[Testcontainers guide](https://testcontainers.com/getting-started/).
- New to Docker?
[Get started](https://docs.docker.com/desktop/). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)