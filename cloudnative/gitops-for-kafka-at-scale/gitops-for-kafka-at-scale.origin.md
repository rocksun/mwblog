# GitOps for Kafka at Scale
![Featued image for: GitOps for Kafka at Scale](https://cdn.thenewstack.io/media/2024/05/bf7c9f79-01.-cover@2x-1024x576.png)
Managing complex infrastructures in distributed systems like
[Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/) requires more than manual intervention; it requires a scalable and automated approach.
According to Confluent’s
[2023 Data Streaming Report](https://assets.confluent.io/m/52436fc9cd4844f4/original/20230510-RPT-Data_Streaming_Report.pdf?utm_medium=report&utm_campaign=tm.campaigns_cd.brand-2023q2-brandhub&session_ref=https://www.google.com/), 74% of IT leaders cite inconsistent use of integration methods and standards as hurdles and challenges to advancing data streaming.
As deployments grow in size and complexity, keeping track of configurations, updates and dependencies becomes a daunting task for platform teams. At the same time, identifying ownership, discovering existing resources and cross-team
[data](https://thenewstack.io/data/) sharing become challenges for development teams.
GitOps and Infrastructure as Code (IaC) are foundational practices in the
[DevOps](https://roadmap.sh/devops) and cloud native spaces. These [practices can be leveraged on Kafka](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/) to bring consistency, standardization and business agility.
In the context of Kafka, GitOps relates to:
- Deployment automation
- Kafka resource configuration
- Access provisioning
- Kafka client configurations
Automating these processes empowers developers to implement rapid changes, introduces governance best practices and alleviates the burden on platform teams responsible for Kafka operations.
## Manual Configuration Management Doesn’t Scale
Initially, having a limited number of Kafka projects with focused scopes keeps requests manageable for ops and platform teams. These teams typically handle Kafka resource requests (e.g., topic creation, configuration, partition modification, schema registration) and access requests through Jira tickets and manual resource provisioning.
However, as adoption increases, the influx of requests surges, Kafka’s infrastructure complexity widens and the team generally has to grow to support it. The method swiftly becomes cumbersome and inefficient. Ad hoc changes also increase the risk of human error, inconsistencies and misconfigurations. For example, a simple typo in an access-control list (ACL) entry can easily lead to failure or unauthorized consumers.
The manual process lacks version control, traceability and transparency.
## IaC Is Foundational for Apache Kafka
Without GitOps, you risk a sprawling mess of topic names, insane numbers of partitions, and no uniform strategy for managing broker, producer/consumer and security configurations.
To scale adoption beyond a critical mass of teams, resources and projects, automation is essential. Otherwise, how do you expect to manage over 100 Transport Layer Security (TLS) certificates, 3,500 Avro schemas, 1,000 topics and 5,000 ACLs? The list goes on!
## GitOps for Configuration Management
Topics, subjects, connect configurations and security configurations can be numerous and varied. If not properly managed, the multitude of configurations can lead to performance degradation and reliability issues.
GitOps allows Kafka configurations to be stored in repositories as YAML or JSON files. The example below demonstrates how to do GitOps using
[Conduktor](https://conduktor.io/) resources.
Storing resource configurations as code allows changes to the desired state of your Kafka infrastructure to be managed through pull requests. This practice relies on three fundamental principles: review, approval and audit trails.
It results in a more globally transparent approach with self-documenting artifacts and a collective understanding of the Kafka infrastructure setup. This encourages communication and knowledge sharing between teams.
## GitOps Provides Control Over Expensive Configurations
But what good is an IaC approach without control over the configurations? You’ll want to avoid a Wild West scenario, and that’s where automated policy enforcement in your CI/CD pipeline comes into play.
As a platform administrator, you’ll want to restrict expensive Kafka configurations globally. For example:
**Replication factor**of **3**to ensure high availability and fault tolerance. **Max partitions**of **10**to prevent excessive resource consumption. **Max retention**of **1 day**to limit storage costs. **Topic naming**that follows internal standards for semantic clarity. *Example code representation of Kafka topic policies in * [: Conduktor](https://docs.conduktor.io/platform/guides/self-service/)
Any variation of a resource configuration policy can be stored as IaC, allowing it to be orchestrated as checks within CI/CD workflows. This enables automated provisioning of Kafka resources without compromising on the risks associated with Kafka’s many configurations.
By design, it introduces an overarching governance layer. The process minimizes deployment errors, reduces manual intervention and introduces a safe framework for using Kafka at scale.
## To Centralize or Decentralize? That Is the Question
Utilizing IaC enables platform teams to push responsibility out to domain owners for managing their Kafka configurations. This helps remove some dependencies on platform teams, who rarely have the relevant business context behind specific Kafka configurations.
Does “Do you really need THAT many
[partitions](https://www.conduktor.io/kafka/kafka-topics-choosing-the-replication-factor-and-partitions-count/)?” sound familiar? By empowering domain owners, platform teams can focus on providing the tools, frameworks and workflows to support IaC implementation.
This shift in responsibilities fosters a culture of accountability and ownership, which is fundamental for scaling. Ask yourself: How long did you wait for your last topic to be created? If the answer is more than a few hours, you’re likely experiencing a bottleneck.
Utilizing an IaC approach does raise questions about how a company should operate. Which should you implement?
**Centralized approach**: One repository to store Kafka configurations for the whole company. **Decentralized approach**: Multiple repositories for each team or domain.
The right choice depends on how the company is structured and the desired trade-off between agility and governance requirements.
|
Centralized |
Decentralized
|
Pros |
|
|
Cons |
|
Perhaps the best solution is to consider a hybrid approach, whereby less critical configurations are managed by teams, and the most critical ones are managed centrally for consistency and compliance.
## Combining Resource Policies and CI/CD Solves Everything, Right? Wrong!
In the Kafka ecosystem, you have to look beyond resource configurations to understand where additional challenges and complexities exist. Streaming applications are directly connected to Kafka, and their behavior and configuration are typically not governed by GitOps principles.
Did you know there are
[over 100 client configuration settings](https://www.conduktor.io/kafka/kafka-options-explorer/) in Kafka? Without Kafka expertise, many are inclined to use the default settings of their Kafka client. That shouldn’t be a problem, right? Maybe not at first, but as you scale, you need to factor in the impact those defaults will have on your network, disk, quality of service and costs.
If you’re not familiar with Kafka client configurations like the following, consult the
[Kafka Options Explorer](https://www.conduktor.io/kafka/kafka-options-explorer/) for a complete list.
|
1
2
3
4
5
|
acks=all
batch.size=16384
linger.ms=0
fetch.min.bytes=1024
compression.type=lz4
While some of the above show default settings (e.g.,
batch.size and
linger.ms), using a compression type is not a default Kafka client setting. It can, however, be used to enhance performance, reduce network load and save on storage costs. Equally, using an
acks value of
all is not the default, but it is recommended in cases where maximum reliability and durability are required.
## Kafka Client Configurations Are a Minefield
Ultimately, Kafka client configurations are a minefield, and it’s a big ask for developers to be tuned into the intricacies and consequences of each setting. However, the impact of one poorly informed configuration can have a severe impact on your entire Kafka platform and the underlying applications.
With a sprinkling of automation, it’s possible to avoid mistakes with client configurations.
This is a policy on client configurations to enforce using:
- A
compressionformat to conserve storage and reduce network bandwidth.
acks(acknowledgements) equals
-1for the highest level of durability and reliability.
- A record header for message routing and filtering.
Such policies enable teams to operate autonomously but maintain overarching control on Kafka producer/consumer settings at a global level.
## Use a Proxy To Enforce Best Practices on Client Configurations
As previously highlighted, applications are directly connected to Kafka, and their configurations are not typically governed by GitOps. One way to solve this problem architecturally is through a Kafka
[proxy](https://docs.conduktor.io/gateway/).
The proxy acts as an intermediary for handling Kafka requests before forwarding them onto the Kafka broker. This could include evaluating the request against client configuration policies, and even manipulating the request (e.g., field-level encryption) before sending it on to the broker.
The proxy approach centralizes configuration validation, which brings consistency and compliance across clients without the need to change each client application. This reduces the risk of one misinformed client causing problems for others and the maintenance overhead of keeping client libraries up to date.
## GitOps Brings Consistency and Business Agility to Managing Kafka
As Kafka adoption scales, new applications will bring new requirements, teams and complexities. Utilizing a GitOps approach to managing Kafka resources, client configurations and rules puts emphasis on automation, traceability and collaboration in your Kafka development.
If you’re scaling Kafka adoption and need a framework that brings consistency, standardization and business agility, reach out and book a
[Conduktor demo](https://www.conduktor.io/contact/demo/). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)