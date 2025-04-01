# Leaner Development: How To Account for the Container Tax
![Featued image for: Leaner Development: How To Account for the Container Tax](https://cdn.thenewstack.io/media/2025/04/906009dd-containers-1024x576.jpg)
[Prostock-studio](https://www.shutterstock.com/g/prostock_studio)on Shutterstock
In 2010, a ubiquitous Microsoft ad featured aesthetically blessed office workers having a collective realization that would solve all their problems:

It was time to go “[to the cloud!](https://blogs.windows.com/windowsexperience/2010/12/07/to-the-cloud-an-in-depth-look-at-the-pcs-scenarios-from-our-new-tv-ad-campaign/)”

Cue the record scratch effect. Many tech-driven companies have gone to the cloud, but they’re not particularly ecstatic about it. As with most things, going “to the cloud” isn’t as simple as advertisers would have you believe.

Cloud architecture is a broad umbrella. It includes virtual machines (VMs), [containerized applications](https://www.paloaltonetworks.com/cyberpedia/containerization#:~:text=In%20recent%20years%2C%20an%20average,%2C%20test%2C%20and%20development%20environments.) and serverless functions. Of these, [containers](https://www.datadoghq.com/container-report/) are the dominant model. As a sign of just how fast [containerization](https://thenewstack.io/containers/) has grown, 80% of respondents to a [CNCF survey](https://www.cncf.io/reports/cncf-annual-survey-2023/) reported using [Kubernetes](https://thenewstack.io/kubernetes/) for container orchestration, a system that’s only now celebrating its 10th anniversary.

Given how much business is now taking place there, it’s time we put aside our rose-colored glasses and look squarely at the practicalities of containerized development. With a more realistic understanding of the benefits and challenges, we may find solutions to recapture the excitement of when “the cloud” was still shiny and new.

## Containers 101: The What and The Why
Containerization is a significant departure from client-server architecture in two important ways.

**Containers make application code fully independent of the server and operating system (OS)**. In theory, developers can create production cloud applications focusing only on application code. All other services are cloud-based, often determined by the cloud provider. This makes cloud computing accessible to smaller, less specialized teams and lets companies turn their attention to their core business.**Containers are immutable, ephemeral and declarative**, making them highly scalable and stable. Containers get spun up as necessary from a container image — a declarative script for a container engine that builds a single instance of the application isolated from other code**.**A container orchestrator helps distribute traffic to keep containers healthy and disposes of containers when appropriate. Any configuration or code changes you make in the container image carry over to new containers, but once you build a container, you can’t change it.
### Containers Deliver Big Benefits
Due in large part to their immutability, containers offer significant advantages:

**Platform-neutral:**As they’re not OS-specific, you can build them from any computer and have them run on any server, so long as you install a compatible container engine.**Fast deployment:**Most cloud hosts offer broad container support so developers can provision and deploy a new app within hours. This process is much less time-consuming and knowledge-intensive, making cloud computing accessible to more players.**Scalable and stable:**The container engine provides compute resources to a container as needed, adapting automatically to app complexity or traffic changes.**Robust security:**Immutability and disposability mean fewer opportunities for users to penetrate sensitive resources. The attack surface is smaller, and enforcing the principle of least privilege is easier because dependencies, functionality, and data remain isolated.
With all these advantages, it’s no surprise container adoption is accelerating — more than [30% annual growth](https://www.grandviewresearch.com/industry-analysis/application-container-market) projected in the next five years. But if you’ve ever worked with containers, you know the experience is far from perfect.

## Containers Can Be a Pandora’s Box
The nature of containers — immutable, ephemeral and declarative — also creates some fairly predictable challenges. Developers often call containers a “black box,” which is an apt metaphor.

It’s hard to know exactly what’s going on inside containers. They’re inherently hands-off, which makes them easy to deploy, but this also facilitates unseen errors that are hard to troubleshoot.

### Wasn’t Containerization Supposed to Fix Development?
One of the most commonly praised benefits of containerization is that it makes the problem of [“It works on my machine”](https://medium.com/@sulthanftr/stopping-it-works-on-my-machine-once-and-for-all-containerization-and-orchestration-ac07d2ae8a22) much less common. But that’s only one of many [issues affecting developer productivity](https://survey.stackoverflow.co/2024/professional-developers/#1-frequency-of-productivity-frictions), highlighting that containerization isn’t a cure-all.

It’s also true that containers create problems of their own. Several issues tend to interfere with developers’ daily workflows:

**It’s hard to debug what you can’t see:**Most standard troubleshooting tools and debugging practices don’t work once you containerize the code. And if the code doesn’t work as expected, it’s hard to know where in the container to look.**Container build times can be slow and unpredictable:**Debugging often works better when devs can make a small change and immediately see the effect. That’s impossible with[standard container practices](https://www.getambassador.io/docs/telepresence/latest/concepts/devloop), which significantly slow down the[inner dev loop](https://www.getambassador.io/docs/telepresence/latest/concepts/devloop). The inner dev loop is a single developer workflow, meaning one single developer should be able to set up and use an inner dev loop to code and test changes quickly.**Conflicting configurations can be hard to untangle:**It’s sometimes difficult to predict how security settings, permissions and other configurations will interact between a local environment, a container and a host environment. Changing the wrong settings can propagate problems in unexpected ways.**Collaboration can be challenging:**The immutable, ephemeral nature of containers makes creating shared containers during the development phase difficult. Two developers working on the same project may not be able to readily work on the same code as they could in a server-based environment.**Dependencies and integrations can be tough to test:**The container build process can obscure dependencies and make their uses difficult to understand. Many developers turn to in-memory or mock dependencies instead of using live API integrations, hiding many potential problems.
Each of these challenges has workarounds, but implementing them all is a lot of work and expense and creates more layers of tooling and processes that slow developers down.

Containers have created new challenges for DevOps teams, as well:

**Managing containers across multiple hosts is complicated:**In an ideal world, you’d have all your containers on a single host with the same container engine, so your DevOps teams could be experts in a single thing. The reality is that most companies have multiple applications split among various container types at several different hosts.**Provisioning servers and data resources for microservices can be challenging:**Overall, containerization isan excellent fit for microservices, but building a sustainable architecture takes careful planning.**Containers have unique security risks:**This goes back to their “black box” nature, which makes it harder to detect[risks](https://www.logicmonitor.com/blog/benefits-and-challenges-of-containerization-for-it-operations). Logging and monitoring are especially important as countermeasures.
These drawbacks don’t outweigh the benefits of containers. Overall, containerization has been a net positive, but as with any tech, it’s trickier in practice. Keeping a close eye on the downsides is essential to managing them effectively.

## The ‘Container Tax’ – What Does It Cost Us?
Most of the benefits of containers accrue to operational teams, who are rid of worrying about physical infrastructure and basic maintenance tasks. Containerization makes applications more stable, cost-effective and scalable, meaning operations teams are more specialized and proactive.

A containerized environment also allows DevOps and site reliability engineers (SREs) to focus on service architecture, performance optimization, security improvements and other projects that can contribute meaningfully to a company’s bottom line.

The costs, meanwhile, accrue mostly to [developers](https://thenewstack.io/optimize-your-inner-dev-loop-to-increase-developer-velocity/), who are bogged down by a multitude of small productivity drains. You might consider this an acceptable trade-off, but slower devs are [a problem for the whole organization.](https://thenewstack.io/hello-world-what-happened-to-the-inner-dev-loop/)

Developers are the people actually building your products and running crucial services. If they’re chronically frustrated, the basic functions of your business will lag behind your goals. The “container tax” — the accrual of those consistent, little productivity drains — is a price most companies can’t really afford to pay.

The good news is that there are things that can help developers work faster, with less redundancy and fewer obstacles. Productivity improvements can be tough to achieve, but improving the way your developers work day-to-day is an obvious target.

## Next-Level Container Management
Improving container management has mostly focused on container orchestration. As mentioned, uptake on Kubernetes has been huge. Industry standards, particularly the work of the [Open Container Initiative](https://opencontainers.org/) (OCI), are making DevOps easier.

Containerization is maturing, and following [best practices for container engines](https://docs.docker.com/build/building/best-practices) and [orchestration](https://www.getambassador.io/blog/kubernetes-best-practices) can go a long way to make your implementation more successful.

As useful as all this is, little of it helps improve developers’ daily workflow. We must find a way to give developers a break on the container tax so they can focus on creating better applications — and we must do it in a way that preserves operational benefits.

## The Best of Both Worlds – Containers Go Local
The next generation of developer tools will build on Kubernetes and container management expertise to deliver a more streamlined developer experience. Developers must be able to work independently in a familiar local development environment while focusing on building high-quality applications.

Equally, they must have access to data and services that accurately reflect the deployment environment and cluster architecture so that they can write code that works in practice.

Building on industry standards like OCI and OpenAPI, tools like [Blackbird](https://www.getambassador.io/products/blackbird/api-development), which aim to make API development more efficient, are expanding to include container-specific features like [Telepresence](https://www.getambassador.io/products/telepresence) (now Cluster Commands in Blackbird).

This new generation of tools delivers some long-awaited possibilities for developers:

**Create parallel**without relying on DevOps teams or missing key configuration details.[production-like environments](https://www.getambassador.io/blog/prod-like-development-environments-improve-api-efficiency)**Connect local development to a live,**so you can test and iterate code with real data and service integrations.[remote Kubernetes cluster](https://www.getambassador.io/blog/boost-developer-velocity-optimizing-feedback-loops)s**Run personal**so developers can collaborate and test using real cluster traffic without disrupting service delivery.[traffic intercepts](https://www.getambassador.io/blog/unlocking-power-telepresence-intercept-specification)**Use familiar, developer-friendly**to troubleshoot containers.**debugging tools****Test****integrations****and****mock APIs****under production-like conditions**to understand how code will perform in deployment.
The solution to the container “tax” isn’t to abandon containers. It’s to look for practical innovations that bridge the gap between local development environments and remote container clusters. These tools need to reflect best practices in DevOps and developer experience (DevEx) so developers can create container applications that work as designed.

## Multicloud Environments: Deliverables and Efficiency
The reality of cloud computing isn’t what that ad campaign promised 15 years ago. For one, fewer of us are working in corporate conference rooms these days, opting instead for the kitchen table or a coffee shop — one of many realities made feasible by cloud computing.

Other realities are a little less liberating. Most companies have [multicloud deployments](https://www.newhorizons.com/resources/blog/multi-cloud-challenges) that give rise to management challenges. Adding [serverless functions](https://spectralops.io/blog/7-smart-steps-to-run-serverless-containers-on-kubernetes/) to the picture creates more complexity. [Cloud security](https://cloudsecurityalliance.org/research/guidance) is a moving target. [Cost management](https://www.getambassador.io/blog/kubernetes-cost-optimization-strategies) is a constant battle.

Developers are also facing ever more pressure for efficiency. The tech industry is still adjusting to the [2024 contraction](https://www.forbes.com/sites/emilsayegh/2024/08/19/the-great-tech-reset-unpacking-the-layoff-surge-of-2024/), and the impact of AI is shifting [hiring plans](https://fortune.com/2025/03/13/ai-transforming-software-development-jobs-meta-ibm-anthropic/) across the sector. With [economic headwinds](https://www.schwab.com/learn/story/future-uncertain-recession-coming) growing, technical leaders must think carefully about delivering more with less.

Containerization is undoubtedly a huge boon for innovation in the development process, but it’s far from a perfect solution. Going “to the cloud,” whether it’s with VMs, containers or serverless functions, isn’t an end in itself. The goal should be a sustainable, maintainable path forward for your developers, DevOps and product teams.

Look for pragmatic solutions that help you realize the value of containers without becoming a minefield of their own.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)