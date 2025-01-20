# Open Source Drives the Twelve-Factor Modernization Project
![Featued image for: Open Source Drives the Twelve-Factor Modernization Project](https://cdn.thenewstack.io/media/2025/01/bb26f057-twelve-factor-open-source_modernization-1024x576.jpeg)
The Twelve-Factor methodology is a set of 12 principles that enable companies to create, run, and maintain enterprise-level software-as-a-service (SaaS) applications in a manner that is uniform and highly manageable. Twelve-Factor is not tied to any particular product, technology, or toolset. Rather, it’s a philosophy for software development that embraces portability, resiliency, stability and cost-efficiency as its driving forces.

The Twelve-Factor App was created by Heroku co-founder Adam Wiggins in 2011, so it’s been around for a while. Over the years, the [Twelve-Factor principles](https://thenewstack.io/learn-12-factor-apps-before-kubernetes/) have helped developers make applications that run in the cloud more resilient and easier to scale, manage and maintain.

When Twelve-Factor first appeared, web-based applications and [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) were still in their infancy. A lot has changed since then, but the Twelve-Factor methodology has largely remained the same. It’s well past time to modernize it and bring it up to date with how we use technology today, so [Twelve-Factor has gone open source](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/).

Before I get into the purpose and implications of making the Twelve-Factor methodology open source, I’ll start by describing the principles behind it.

## The Twelve Factors
The following is a brief review of the principles that drive Twelve-Factor, what each means and how to use them.

### Factor 1: Codebase
**What it means:** Use one codebase per app, tracked in version control, with multiple deploys. This ensures all assets related to the application are managed in a single repository.
**How to apply it:** Typically, supporting a single codebase means keeping all of a project’s source code and ancillary artifacts in a single source code repository, such as GitHub, BitBucket, AWS CodeCommit, or [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) Source Repositories. Codebases should not be scattered about among a variety of repositories.
### Factor 2: Dependencies
**What it means:** Explicitly declare and isolate all dependencies to avoid implicit reliance on system tools or libraries. This makes the application more predictable and easier to manage.
**How to apply it:** A key to supporting the dependencies principle is to use repositories that store independent libraries and packages in a controlled manner. Applications should separate custom code from independently developed libraries and list those libraries in a configuration file. Then, when it comes time to run an application, the independent libraries are added to the project at build and run time. Libraries are not stored with the source code but rather in a separate repository controlled by the library developer.
Examples of some of these repositories are [npm](https://www.npmjs.com/) for [Node.js](https://roadmap.sh/nodejs) projects, [PyPI](https://pypi.org/) for [Python](https://thenewstack.io/python/), [MVN Repository](https://mvnrepository.com/) for [Java](https://thenewstack.io/introduction-to-java-programming-language), [Chocolatey](https://chocolatey.org/) for .NET and [RubyGems](https://rubygems.org/) for the Ruby programming language.

### Factor 3: Configuration
**What it means:** Store any configuration that varies between deployments separately from the code. This allows you to make changes more easily without modifying the codebase.
**How to apply it:** Separating configuration from code has become a fundamental practice in enterprise system architecture. Sometimes, configuration information is stored in manifest files. Frameworks such as Kubernetes automatically inject the information declared in the manifest into the environment. Also, configuration updates are executed by changing the information in the manifest files. The framework notices the change and updates the environment automatically.
The Configuration factor has an open proposal for updates [(issue #4](https://github.com/twelve-factor/twelve-factor/issues/4)).

### Factor 4: Backing Services
**What it means:** Treat backing services (like databases, queues and memory caches) as attached resources that can be accessed via a URL or other locator stored in the configuration. This makes services easily interchangeable.
**How to apply it:** The principal requires resource access to be conducted over a standard protocol such as an HTTP/HTTPS connection.
The important thing to understand about using libraries and command-line interface (CLI) tools is that the technologies are abstractions of the actual resource. There is no tight binding to the resource. Rather, programmers declare access credentials for the resource and the action to perform on it. The tool takes care of the particulars of working with the resource.

Theoretically, programmers should be able to change from one resource provider to another with minimal impact. However, as with any technology, the devil is always in the details. Thus, programmers should use TCIP/IP-based resources. Then, the code will be structured to access the resources in a generic manner.

### Factor 5: Build, Release, Run
**What it means:** Strictly separate the build, release and run stages of the deployment process. The build stage compiles the code, the release stage adds environment-specific configurations and the run stage executes the application.
**How to apply it:** Comprehensive CI/CD applications such as Jenkins and TeamCity are useful for supporting the Build, Release, Run principle. These tools typically allow programmers to define an application’s configuration settings and source code repository. The tools have scripts that automatically get the source code from the designated repository. These scripts then build the application and apply the configuration settings to test the code. (These test scripts are stored in the repository along with the source code.) Once the built code passes testing, the script then deploys the built application to a designated runtime environment.
CI/CD tools work in conjunction with the Build, Release, Run principle, allowing for fast, accurate, and observable application deployment on an ongoing basis.

### Factor 6: Processes
**What it means:** Execute the app as one or more stateless processes. Persistent data should be stored in stateful backing services. This makes scaling easier and prevents unintended side effects.
**How to apply it:** Stateless code is the essential mantra of web-based applications. The only thing a process should do is execute processing logic. Side effects between processes are to be avoided; the process should not affect the overall state of the application or the state of another process within the application. To determine the state of a process, inspect an independent source of truth that coordinates activities among all processes.
### Factor 7: Port Binding
**What it means:** Use port binding to export services, making them self-contained and accessible via specified ports.
**How to apply it:** Certain port numbers have become emblematic of a particular service. For example, the default port for a non-secure web application is port 80. Secure websites are accessed via HTTPS on port 443. The Kafka messaging service listens to client traffic on port 9092. The default port for the MySQL database is 3306. Some companies will go to great lengths to keep their product’s brand identity associated with a port number.
[Docker](https://www.docker.com/?utm_content=inline+mention) and [Kubernetes](https://thenewstack.io/kubernetes/) use port declarations to define the access point of a service within a domain. At the development level, programmers typically work with a resource or service on their machines according to the localhost URL but then bind to the given resource or service via the associated port number.
### Factor 8: Concurrency
**What it means: **When scaling out an app, do so horizontally by adding more processes rather than scaling up individual processes vertically.
**How to apply it:** Support for on-demand horizontal scaling has become a critical feature in modern web-scale enterprise applications. Many technologies, including AWS Elastic Container Service (ECS), Docker Swarm, Google Cloud Run, Heroku, [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) Nomad and Kubernetes, support autoscaling.
The important thing to understand about the Concurrency principle is that applications must be composed of discrete, independent units of execution logic that can run redundantly and simultaneously. The number of units running can be scaled up or down to meet current traffic demands.

### Factor 9: Disposability
**What it means:** Ensure fast startup and shutdown times to maximize resiliency and make the system more robust.
**How to apply it:** The Disposability principle of Twelve-Factor speaks to the ephemeral nature of modern distributed applications. As the Concurrency principle indicates, applications will spin up resources in a redundant manner to meet the needs of the moment. As such, components are always “coming and going” to meet traffic demands.
When a resource is terminated, it must do so quickly and gracefully. This means making sure that no operations are terminated in an amorphous state. Operations must be completed, connections to external resources must be closed and the resource must be removed from memory safely. Once a component terminates, the overall state of the application should be consistent.

### Factor 10: Dev/Prod Parity
**What it means:** Keep development, staging and production environments as similar as possible to facilitate continuous deployment and reduce the gap between development and production.
**How to apply it:** The Dev/Prod Parity principle is similar to the Build, Release, Run principle in that it breaks up the application development process into discrete segments. However, while Build, Release, Run is concerned with getting code out the door, Dev/Prod Parity focuses on code consistency across escalating development environments.
Typically, different operations are performed at different phases of software development. In the development phase, code is committed by developers. That code is subjected to code analysis and unit (and maybe performance) testing. If all goes well, it’s moved to staging. In the staging phase, the code is subject to a broader testing regime that can include integration testing and penetration testing to find security risks. Staging is also where the code is subjected to usability testing to make sure that it satisfies human needs, if the application will be used by humans. Finally, upon success, the code is released in the production stage.

The important thing to understand about Dev/Prod Parity is that each environment — dev, staging and prod — must be identical, and the same tools must be used when executing automated work in each environment. Also, unless there is an emergency update, the escalation process must be one way: Code must move from dev to staging to prod. There can be no back and forth. And, in an emergency situation, such as a hotfix, when code bypasses the dev environment and is moved directly from a developer’s machine to staging, once the hotfix code is released to prod, the dev environment must be updated to accommodate the changes in staging.

In a well-run IT shop, a developer’s habit is to check for updates to the dev environment daily before starting a coding session on their local machines. This ensures that any emergency “backward” update (from staging to dev, in the case of a hotfix) will make its way back to the developer’s machine.

The critical factors in Dev/Prod Parity are the uniformity of infrastructure in each environment as well as the predictable control of the escalation process between environments.

### Factor 11: Logs
**What it means:** Treat logs as event streams and leave the execution environment to aggregate them. This simplifies log management and debugging.
**How to apply it:** Logging should be done by treating logging events as streams of data independent of any particular technology. The usual implementation is to treat a log event as a message that gets consumed by a data stream technology such as Kafka. Separating log emissions from log storage makes application portability easier.
Logging to a data stream puts the onus of storage and data management on the stream management technology. The tradeoff is that information about the machine and application emitting the log data becomes opaque. Thus, using a standardized message format becomes essential for efficiency. The message format should include information about the event, the machine, the application and any other environmental information relevant to the application’s operation.

There are many benefits to logging into an event stream, but you must do additional planning to ensure that the log presents information that is accurate, comprehensive and useful.

This Factor has an open proposal to expand it to reflect current observability practices, including telemetry ([issue #3](https://github.com/twelve-factor/twelve-factor/issues/3))

### Factor 12: Admin Process
**What it means:** Run admin tasks as one-off processes, managed in the same codebase and version control system as the application. This ensures consistency and ease of execution.
**How to apply it:** Applications must ship with their own admin capabilities, such as a dashboard. For example, Substack, an online publishing platform for writers, journalists and other content creators, ships with a dashboard feature that allows content creators to control publication operations and reader access. The platform also enables content creators to segment certain content for paid-only access and also to configure how funds are collected.
This administration feature is part of Substack. It is not a separate application, and its source code is not hosted in a separate repository. Both the general application and the admin processes are part of a unified codebase. Substack is one example of the principle of Admin Process. The important thing to understand is that administration features are managed as part of the application, not as something separate from the application.

## Going to the Next Level Via Open Source
One thing you may notice from the descriptions of each factor is that Twelve-Factor is agnostic about what technologies are used to support its principles.

When the Twelve-Factor App was introduced in 2011, the methodology was new thinking in the technology landscape. The principles’ agnostic nature made adoption easier, particularly for companies like Heroku, which provides [a platform](https://blog.heroku.com/next-generation-heroku-platform) that can support a wide variety of tools and technologies. However, over the intervening years, a wide variety of cloud providers adopted Twelve-Factor, and by making the methodology open source, Heroku is encouraging the community to help modernize it.

As [Betty Junod](https://www.linkedin.com/in/bettyjunod/), chief marketing officer at Heroku, explained in an interview:

*“When Adam Wiggins wrote it 14 years ago, the cloud was still new, and Docker and Kubernetes didn’t yet exist. He was charting the course for what great SaaS should look like. Since then, many things have changed, and revision is warranted. But, it shouldn’t be just Heroku’s point of view. Many cloud providers and end user organizations have embraced the Twelve-Factor principles. Each brings different experiences in running these kinds of apps and infrastructure in the cloud at a large scale. Their thinking and contributions need to be incorporated into taking Twelve-Factor to the next level.”*
As Junod indicates, the principles that drove Twelve-Factor made sense at the time, but the technical landscape has undergone dramatic changes. It must be modernized to address things like telemetry, authentication and service-to-service (S2S) communication, which modern developers and architects deal with daily but aren’t part of the original methodology.

To encourage broad participation in Twelve-Factor modernization, in November, [Heroku made the project open source](https://www.youtube.com/watch?v=JG1nGgirkB4) under a CC-BY-4.0 license. The company has migrated the source for Twelve-Factor from its [original website](https://github.com/heroku/12factor) to a new open-source[ repository](https://github.com/twelve-factor/twelve-factor).

The new repo provides a central point of activity for contributions to Twelve-Factor. It contains an updated version of the website code and documentation with more in-depth descriptions of the factors. The repository also contains links to new thinking and additional documentation from organizations, including [O’Reilly](https://www.oreilly.com/library/view/beyond-the-twelve-factor/9781492042631/), [Nginx](https://slidrio-decks.global.ssl.fastly.net/1020/original.pdf) and [IBM](https://www.ibm.com/blog/7-missing-factors-from-12-factor-applications/). These companies embrace the spirit of Twelve-Factor, and their perspectives are valuable for making it more practical today.

Two of the most significant benefits of open source are transparency and a mechanism for fostering community-based technical innovation. Along with broadening the scope of Twelve-Factor, that innovation is expected to inspire tools for creating applications based on the methodology, said [Vish Abrams](https://www.linkedin.com/in/vishvananda/), chief architect at Heroku and a maintainer of the Twelve-Factor repository, in a [recent discussion](https://discord.com/channels/@me/1315041275292155944/1315089927251300493) on the Twelve-Factor Discord server.

The trick is to make Twelve-Factor-based application development a comprehensive, unified experience. Open sourcing the project and thinking that drives Twelve-Factor is a major step forward toward building resilient, scalable and maintainable applications that operate at web scale.

## Get Involved
The Twelve-Factor approach to software development has inspired software development and architecture for more than a decade. Its principles define a unified, predictable way to make enterprise systems safer to deploy and easier to maintain.

But given the dramatic technological changes that have taken place over the last decade, Twelve-Factor needs to evolve to keep up with the times. The hope is that by making Twelve-Factor an open source project, a broader range of contributors with a variety of perspectives will help keep Twelve-Factor as useful today as it was when it was first released in 2011.

Learn how you can participate by reviewing the [Contributing page](https://github.com/twelve-factor/twelve-factor/blob/next/CONTRIBUTING.md) of the project’s repository.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)