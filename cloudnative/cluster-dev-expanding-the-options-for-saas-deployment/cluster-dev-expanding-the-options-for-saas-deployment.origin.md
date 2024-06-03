# Cluster.dev: Expanding the Options for SaaS Deployment
![Featued image for: Cluster.dev: Expanding the Options for SaaS Deployment](https://cdn.thenewstack.io/media/2024/05/a4836188-chincherinchee-seeds-7674154_1280-1024x708.jpg)
As the number of enterprise
[ Software-as-a-Service](https://thenewstack.io/how-saas-based-global-server-load-balancing-eases-it-burden/) ( [SaaS](https://thenewstack.io/private-saas-is-coming-are-you-ready/)) customers grows, B2B vendors face the challenge of aligning their software to high corporate standards. However, for certain industries, the multitenant nature of cloud-based SaaS makes it an unfeasible option due to security, compliance and performance reasons. In this article, we will explore various scenarios of implementing SaaS architecture, focusing on deploying to customer-managed environments as an alternative for enterprise-grade customers.
## Clarifying the Notion of SaaS Tenancy
Before we start, let’s briefly revise the meaning of the term SaaS, or Software as a Service: it is a software distribution model of granting
[users access to cloud-based products](https://thenewstack.io/adding-too-many-features-will-break-your-product-users-and-team/), tools, or services on a subscription basis.
Below, we will explore different scenarios of
[SaaS implementation in a cloud](https://thenewstack.io/3-key-factors-for-future-proofing-saas-cloud-platforms/) environment.
## Multitenant SaaS
Multitenancy is a concept often associated with SaaS, because a conventional SaaS model implies that multiple clients will utilize specific infrastructure resources. However, the extent of resource sharing can vary depending on the SaaS architecture: they may or may not be shared within a given implementation as shown in the examples below.
Scenario 1 illustrates a classical model of SaaS service consumption.
-
Scenario 1: SaaS architecture where all resources are shared
In this scenario, all clients are deployed in a provider’s cloud account where they share all the resources: the SaaS application, computing capacities, and a database.
Scenario two depicts an implementation model with partial resource sharing.
-
Scenario 2: SaaS architecture with partial resource sharing
As illustrated on the diagram, customers share a SaaS application/computing resource but have dedicated databases deployed for each user. Although this environment can be considered multitenant from the customer’s perspective, technically speaking, some parts of it are multitenant and some are not.
Both examples can be characterized as multi-tenant as they incorporate resource sharing, albeit with some variations.
### Pros of Multitenant SaaS
- Efficient resource usage and distribution. Using load balancers ensures that infrastructure available resources are allocated to handle heavier workloads.
- Faster scaling as clients use the same software and hardware.
- Affordable price as the cost of the environment is shared among multiple customers.
- Automated maintenance as part of SaaS subscription.
- Well-established process of onboarding guarantees an easy start for new customers.
### Cons of Multitenant SaaS
- Restricted customization options since all customers share the same operational conditions and common processes.
- Data security concerns as compromising one customer’s security can put others at risk.
- Possible performance issues as one customer’s downtime or peak load can affect the availability of neighbors’ services.
- Downtimes due to regular software upgrades and database maintenance.
## Single-Tenant SaaS
Single-tenant SaaS implies an architecture where the SaaS client is a tenant. In single-tenant environments clients are deployed with a dedicated set of resources that they have exclusive rights for. Since products within the single-tenant model cannot be shared, the tenants are free to customize the SaaS software according to their needs.
The diagram below delineates a single-tenant SaaS environment with a dedicated stack per tenant.
-
Scenario 3: Stack per tenant SaaS environment
### Pros of Single-Tenant SaaS
- Enhanced security as each customer’s data is isolated and stored on dedicated servers.
- Flexible customization options allow configuring
[infrastructure around concrete business needs](https://thenewstack.io/how-iac-meets-the-differing-infrastructure-needs-of-dev-and-ops/).
- Individual software upgrades in the time window convenient for a client.
- Reliable operations due to exclusive resource usage.
### Cons of Single-Tenant SaaS
- High-priced as each customer needs individual instances. Also, additional modifications require more time and resources which leads to higher costs.
- Limited scalability as expanding resources requires manual provisioning.
- Complex maintenance due to necessity to upkeep multiple instances with customized configuration.
- Slower onboarding as the SaaS provider needs time to configure infrastructure around each customer’s needs.
## Running SaaS on the Customer’s Side
In the previous examples, both multitenant and single-tenant
[infrastructures are deployed in a provider cloud](https://thenewstack.io/3-tips-to-secure-your-cloud-infrastructure-and-workloads/) account which makes certain processes common to all clients. The Scenario 3 diagram shows that despite being deployed in isolated infrastructures, tenants are still managed and operated collectively sharing the processes of deployment, monitoring, and onboarding. Furthermore, if a new SaaS software version is released, the provider upgrades it for all tenants simultaneously.
These examples suggest that all SaaS environments to some extent incorporate some form of multitenancy, regardless of their architecture. As such, it is not surprising that customers, driven by data security and privacy concerns, still prefer installing software in their own environments.
In this case, on-premise installation may seem like the optimal choice, granting a customer full control over resources, services, and data. However, certain challenges of in-site systems, such as the necessity to procure and maintain hardware and software, hiring staff with traditional IT skills for management, and limited scalability options, could render it highly inefficient for dynamic and fast-growing enterprises. Additionally, many
[security tools and architectures are tailored for cloud environments](https://thenewstack.io/the-role-of-context-in-securing-cloud-environments/), potentially impacting their performance on-site.
The solution is installing the software into customer-managed environments and running a replica instance of the SaaS within the company’s cloud account.
The
[research conducted by Replicated](https://www.replicated.com/state-of-the-industry-for-software-distribution-download-the-report) proves this option highly popular among customers: 79% of respondents increased their “customer-managed environments” software business due to a high demand, while 56% of respondents reported having more than 10 new customer installations each month.
One of the key advantages of this approach is the heightened security and control it affords.
Let’s take a closer look at this implementation model.
## Comprehensive Control
In a SaaS model with dedicated resources, customers pay for licenses but do not have access to the containers with code. In fact, customers have no control over the environment where the SaaS application runs.
On the contrary, deploying the SaaS replica to a
[cloud account empowers the client with complete control](https://thenewstack.io/cloud-control-planes-for-all-implement-internal-platforms-with-crossplane/) over the system. This grants access to the SaaS code and the underlying runtime environment. With full access to the server infrastructure, the customer can allocate resources, select instance types, customize scaling, and even migrate the SaaS application to another data center — options that are impossible with the traditional SaaS model.
## Security
Running
[SaaS in a dedicated infrastructure offers advanced security](https://thenewstack.io/top-6-saas-security-threats-for-2023/) features, such as dedicated servers and the freedom to implement proprietary security tools. But deploying SaaS into a [cloud account goes a step further by granting customers](https://thenewstack.io/what-tools-a-swedish-it-provider-relies-on-for-its-customers-cloud-native-journey/) access to the SaaS file system. This enables conducting vulnerability scanning across all layers of security posture, including container images, to ensure secure deployment without misconfigurations.
Additionally, as your IT staff has complete control over resources, services, and data, you decide who can access them and under what conditions.
## Installation to the Customer Cloud Account
One of the drawbacks of this scenario is the complicated installation process and the necessity to support customers through the initial steps and future upgrades. According to the Replicated survey, complex installation is among the main reasons why SaaS software setup and configuration in a customer’s environment could take up to 14 days. The commitment to simplify this process for their customers drives SaaS vendors to develop custom cloud installers for their software, and here is where
[Cluster.dev](https://docs.cluster.dev/) can help.
The Cluster.dev open source framework is aimed to address the challenges of SaaS companies building software for customer-managed environments. It enables bundling the software code with a preconfigured infrastructure into a single installation package, making it possible to create a one-click cloud installer for SaaS software. This kind of installation allows customers to launch the product seamlessly without specialized skills or knowledge. The script facilitates installation on any cloud platform or on-premises by employing templating and codifying best practices in deployment and Day 2 operations.
-
The Cluster.dev installer diagram
## Core Values for Vendors
- Enables customer self-service
- Decreases failures in delivering software to customers
- Simplifies user journey to adopt and operate your product
- Aligns with best practices established for cloud installations
- Makes distribution and version upgrade easy
- Can be integrated with cloud-managed services
## Conclusion
The concerns about data security and compliance compel certain customers to explore alternative ways of SaaS implementation. While the option of deploying SaaS directly to a cloud account looks attractive for enterprise customers from a standpoint of security and control, complicated installations and the necessity to support customers through upgrades could hinder this process for SaaS vendors.
[Cluster.dev](https://cluster.dev/) provides companies with better software deployment options by enabling a single command cloud installer for their SaaS, ensuring an easy start for new customers. *Anastasiya Kulyk, Technical Writer at SHALB, is a co-author of this article.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)