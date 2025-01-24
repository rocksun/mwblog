# Return to PaaS: Building the Platform of Our Dreams
![Featued image for: Return to PaaS: Building the Platform of Our Dreams](https://cdn.thenewstack.io/media/2025/01/e7aaa7fe-return-to-paas-1024x576.jpg)
Think back to the beginning of the cloud era. The process of taking an application we had running on local host and deploying it to the cloud was a complex and arduous process. Developers would spend hours creating cloud environments, databases and servers. Building deployment pipelines to build and launch our products resulted in additional time to launch, slowing innovation and developers’ ability to ship finished products.

Along came products designed to ease the deployment of applications into the cloud, introducing Platform as a Service (PaaS) to the world of app development. No matter what language your application was written in, you could simply `git push`
your code and the platform would do the rest. Within minutes, your application would be deployed and live in the cloud.

For example, Heroku’s platform revolutionized cloud-first deployments, containerizing your apps in dynos with built-in database support. The complexity of deploying applications to the cloud was removed. Developer productivity increased — rather than worrying about tricky cloud infrastructure, they could go back to coding apps.

But now the growing complexity of cloud tooling is slowing down developer productivity and [overshadowing the original promise of DevOps](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/). As tech stacks expand and infrastructure demands increase, developers lose focus on delivering application value. To address this, we need solutions that simplify cloud deployments and allow teams to concentrate on building great apps.

**The Return of Complexity and Developer Pain**
Of course, the cloud has changed a lot since Heroku first launched. The success of PaaS and containerization has moved the entire industry to deploy to the cloud first. Apps now default to being cloud native, and as a result, entire ecosystems have been built to help developers launch cloud native apps. The promise of DevOps has led to developers not only owning the application code but also operating and maintaining the infrastructure that runs the applications.

This has led to even greater innovations in the cloud. [Kubernetes](https://thenewstack.io/kubernetes/) (K8s) has been referred to as the “operating system for the cloud.” K8s is built to help orchestrate the use of containers — deployment, scaling and management of code across our infrastructure. The power to control all our [DevOps](https://roadmap.sh/devops) needs in one ecosystem has led to massive adoption of K8s worldwide.

Innovation on the K8s platform has led to the creation of thousands of developer tools and products that build upon and improve building platforms on top of K8s. A robust ecosystem of open source cloud native tools are available to solve myriad problems.

However:

- The myriad tools and options come with a cost, slowing down development teams.
- Teams face challenges in determining the right tools, implementing them and maintaining platforms.
- Tech stacks are growing exponentially, adding complexity and cognitive load.
- The DevOps principle of “you build it, you own it” distracts developers from delivering application value.
- Teams are increasingly bogged down by maintaining complex solutions just to launch applications.
![Diagram of a complex Kubernetes architecture](https://cdn.thenewstack.io/media/2025/01/7aeca3d9-kubernetes-complexity-1024x672.jpeg)
Kubernetes complexity, based on a diagram from “[Navigating Kubernetes Complexity (Part I)](https://medium.com/pipedrive-engineering/navigating-kubernetes-complexity-part-i-37781d4b3ecf).”

Remember that it is not the cloud part we are building; we are building the **applications that run on that cloud.** Once again, we have teams bogged down to support and maintain complex solutions for launching applications.

**Platform Engineering: Reining In the Complexity**
Large organizations are more likely to have the budgets to support a team of platform engineers — a team with deep expertise in building and deploying cloud platforms. [Platform engineering teams](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/) provide standardization and automation for DevOps practices inside the organization. They create [internal developer platforms](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/), which allow internal developers to simply select what sort of infrastructure they need, and it will be created for them.

![Triangle with K8s infrastructure at the bottom, platform engineering in the center, and developer teams at the top](https://cdn.thenewstack.io/media/2025/01/3aeb90ca-platform-engineering-standardization-automation.jpeg)
Platform engineering teams are formed to provide standardization and automation for DevOps.

This provides a better developer experience by reducing the surface area of the DevOps landscape, lowering developer cognitive load and making cloud deployments easier.

Organizations can mitigate the challenges of sprawling tech stacks and streamline cloud operations by introducing dedicated platform engineering teams. However, not all organizations have the resources to implement these specialized teams. This exacerbates the need for more modern solutions.

**Introducing the Modern PaaS: Cloud First and K8s **
K8s has become the go-to platform for deploying containerized applications in the cloud. Smaller organizations may not have the time or expertise to create platform engineering teams or build bespoke cloud developer platforms. Larger organizations may wish to streamline certain applications without internal deployment discussions with their platform engineering teams. In many cases, we can leverage existing developer cloud platforms built on top of modern K8s cloud stacks. It is the return of the modern Platform as a Service.

The modern PaaS — like Heroku’s recently [launched next-generation PaaS](https://blog.heroku.com/next-generation-heroku-platform) — is built on the best practices of modern cloud deployment. You build your application, and Heroku creates containers (using Cloud Native Buildpacks). Heroku uses its [K8s expertise](https://blog.heroku.com/heroku-joins-cncf-platinum-member) to manage and orchestrate your application, and it abstracts away all of the complexity. For example, there is no need to become an expert in container observability, as OpenTelemetry is built in and connected to Heroku Metrics and available via the Heroku software development kit (SDK).

Developers (and even your platform engineering team) no longer need to roll out the same deployments over and over; the PaaS handles it for you, allowing engineers to focus on their core responsibilities.

**Summary**
At the dawn of the cloud, PaaS services helped developers bypass the complexity and frustration of cloud deployments so that they could [focus on their applications](https://thenewstack.io/open-source-drives-the-twelve-factor-modernization-project/). As the cloud has evolved and grown, the power and complexity of the cloud tooling ecosystem have grown exponentially. While these tools give development teams much more power and flexibility, the scale of implementing the required tooling is slowing developer productivity and operational complexity for delivery.

The return of cloud native Platform as a Service means that teams can lean on industry experts to build and abstract away the complexity from their cloud platforms. Developer productivity is increased, as they can focus on building and shipping apps — knowing that the deployment and management of their application is being safely managed by the PaaS.

*Visit Heroku to learn more about and try the next-generation PaaS.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)