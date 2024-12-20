# Why All the Major Cloud Platforms Are the Same
![Featued image for: Why All the Major Cloud Platforms Are the Same](https://cdn.thenewstack.io/media/2024/12/9d9c3947-cloud-1024x576.jpg)
Cloud platforms are far more similar than many realize. And they are also far more similar to nature’s evolutionary processes than most know.

In nature, convergent evolution describes how unrelated species independently develop similar traits to solve common problems. One of the most well-known examples is the evolution of wings in birds, bats and insects. Despite their vastly different origins (birds are avian, bats are mammals and insects are arthropods) they have all evolved wings to enable flight.

This phenomenon has been observed across an array of species and environments. Another intriguing example is the evolution of echolocation in bats and dolphins. Both mammals developed the ability to emit sound waves and interpret the returning echoes to navigate and hunt in low-light conditions.

OK, but how does it apply to cloud technology? The point here is that even wildly different entities can develop common traits when faced with the same challenges or advantages. Cloud platforms, such [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform (GCP), [Microsoft ](https://news.microsoft.com/?utm_content=inline+mention)Azure and [Oracle](https://developer.oracle.com/?utm_content=inline+mention), are very much like these species. While they all began with distinct origins and philosophies, they’re ultimately trying to solve similar problems and as such, they’ve independently developed common functionality that addresses those shared challenges.

While many similarities may stem from competition and direct inspiration, many others exist inadvertently as a result of convergence. Today this convergence and competition has existed long enough that all major cloud providers are more similar than they are different. Understanding this convergence allows us to make intelligent design decisions for the future of application development.

## The Evolution of Cloud-Managed Services
Let’s start with a short walk down memory lane, when AWS was trailblazing with its launch of Simple Storage Service (S3) in 2006. S3 addressed a critical challenge: providing scalable, secure and cost-effective storage for businesses without [requiring them to manage infrastructure](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/). Shortly after, Amazon Elastic Compute Cloud (EC2) revolutionized access to computing power, enabling organizations to deploy and scale applications on demand, without the capital investment in physical servers.

These innovations paved the way for AWS to position itself as a leader in cloud computing, effectively making enterprise-grade technology accessible to businesses of all sizes. This democratization of infrastructure allowed companies to focus on innovation rather than operational overhead, setting the tone for the cloud market’s rapid evolution.

A few years later, AWS addressed the need for databases with the launch of Amazon Relational Database Service (RDS) in 2009. RDS provided managed relational databases, simplifying the setup, operation and scaling of database systems like MySQL, PostgreSQL and SQL Server. This allowed developers to offload tedious tasks such as backups, patch management and scaling, while still maintaining control over their data structures and queries.

For non-relational workloads, AWS introduced Amazon DynamoDB in 2012, a fully managed NoSQL database designed for low-latency, high-scale applications. DynamoDB targeted use cases where traditional relational databases were less efficient, such as real-time analytics, gaming and IoT.

Together with S3 and EC2, these database services enabled AWS to offer a robust foundation for application development. S3 handled object storage, EC2 managed compute needs and RDS/DynamoDB covered data persistence. This comprehensive suite allowed businesses to build and run data-driven applications without the complexity of managing hardware or database infrastructure. It also laid the groundwork for more advanced services that further abstracted and automated database operations.

With the successes of AWS’s managed services, rivals like [Google and Azure](https://thenewstack.io/sustainability-how-did-amazon-azure-google-perform-in-2023/) recognized similar challenges in the market and developed their own solutions to address them:

**Google Cloud**
Google leveraged its expertise in search, data processing and distributed systems to launch innovative cloud offerings:

**Google App Engine**: As early as 2008, Google pioneered platform-as-a-service (PaaS) with App Engine, allowing developers to[deploy applications without worrying about the underlying infrastructure](https://thenewstack.io/beyond-iac-fixing-clouds-separation-of-concerns-problem/). This abstraction helped smaller teams focus on their code while Google handled scaling and operations.**Firebase**: Provided developers with real-time database solutions, serverless backends and integrated tools for mobile and web app development.
However, the common requirements of cloud applications and the established functionality of AWS meant other services, such as Google Cloud Storage (2010), were also needed to provide scalable, durable object storage akin to AWS S3.

**Microsoft Azure**
Azure capitalized on its established enterprise customer base and deep integration with existing Microsoft tools, but again common requirements lead to similar offerings:

**Azure Blob Storage**: Microsoft’s counterpart to S3, Blob Storage, launched in 2008, providing scalable object storage for unstructured data.**SQL Azure**: Recognizing the need for database solutions, Azure introduced SQL Azure (now Azure SQL Database) in 2010, a managed relational database service built on Microsoft’s SQL Server technology. It was targeted at businesses already familiar with SQL Server, reducing the barrier to cloud adoption.**Azure Cosmos DB**: Introduced in 2017, Cosmos DB addressed the growing demand for globally distributed, multimodel databases, similar to AWS DynamoDB but with support for a wider range of database paradigms.
## Market Demands That Drive Convergent Evolution
Cloud providers operate within a shared ecosystem of developer expectations and business requirements. At their early stages, cloud platforms had less in common, leading to perceptions of significant capability gaps. AWS’s early dominance in services like Lambda, DynamoDB, EC2 and S3 reinforced the idea that other providers were incomplete. However, as these technologies evolved, the differences between platforms shrank. Today, the managed services offered by AWS, GCP, Azure and Oracle are more alike than different.

Below, we examine how the following demands shaped serverless compute:

**Simplified infrastructure management**— Teams wanted to focus on building applications rather than provisioning, scaling and maintaining servers.**Event-driven architectures**— The rise of micro/macro services and event-driven workflows created a need for functions that could execute in response to specific triggers.**Cost efficiency**— Organizations sought to minimize costs by paying only for the resources consumed during use ( paying for the time a service spends processing a request).
The response:

**AWS Lambda**: The first well-known solution to meet this demand introduced ephemeral, event-driven code execution without the need for traditional servers. It focused on scalability and seamless integration with AWS’s growing ecosystem.**Azure Functions**: Evolved to prioritize deep integration with enterprise tools and workflows, responding to Microsoft customers’ demand for stateful workflows and enterprise-grade monitoring.**GCP Cloud Functions**: Tailored for organizations using Google’s data and AI services, addressing the need for functions that integrate easily with tools like BigQuery and Vertex AI.
## The Current State
Each provider brought unique strengths and strategic priorities to the table, creating differentiation initially, but eventually converging on a consistent baseline of functionality. We now have late joiners like Oracle emerging and despite its late entry and the added benefit of watching what worked for the other cloud providers, Oracle Cloud offers very similar capabilities.

This standardization reflects the shared expectations of developers and businesses worldwide and has resulted in a comprehensive suite of services that underpin cloud native applications.

Here’s how this standardization now offers key foundational functionality:

**Storage**: Every major cloud provider offers scalable, secure and highly available storage solutions, catering to use cases like object or block storage for high-performance needs.**Compute**: From virtual machines to serverless compute and container orchestration, compute services have evolved to meet diverse needs, including pay-per-use models (such as AWS Lambda and GCP Cloud Run) and robust VM instances for traditional workloads.**Databases**: Providers now offer managed relational databases, NoSQL solutions and distributed databases, eliminating the operational overhead for developers while ensuring scalability and high availability.**WebSockets**: Real-time communication has become a critical feature in modern applications. Providers now offer managed WebSocket solutions, enabling seamless bi-directional communication**High-performance compute (Batch)**: The demand for HPC workloads has driven the development of batch processing solutions tailored for AI, machine learning (ML) and scientific research.**Queues**: Managed message queues ensure reliable, decoupled communication between application components, reducing the complexity of distributed systems**Topic/Subscriptions**: Pub/sub-models have become indispensable for event-driven architectures, enabling scalable and efficient message broadcasting to multiple consumers.**Scheduled Tasks**: Providers have standardized task scheduling to trigger jobs at specified times or intervals, enabling automation of repetitive tasks.
## Beyond Convergent Evolution
[Cloud ecosystems have evolved to offer strikingly similar services](https://thenewstack.io/pros-and-cons-of-cloud-native-to-consider-before-adoption/) across providers, yet the journey through them remains complex and fragmented. Recognizing the convergent evolution of cloud services enables businesses to make decisions based on current realities, not historical impressions.
As cloud services align in capabilities and standards, organizations gain the ability to create portable solutions that can move seamlessly across platforms, reducing the risks and costs associated with vendor lock-in. This convergence also enables developers to leverage higher levels of abstraction, allowing them to focus more on delivering value through business logic rather than getting bogged down in the intricacies of the underlying infrastructure.

We originally built Nitric to build on the convergence, providing a [framework that developers could use to deploy truly portable cloud applications](https://thenewstack.io/nitric-a-cloud-portability-framework-for-code/). However, to date, most users have found that it brings value even when they are targeting a single cloud. By abstracting superficial differences, Nitric unlocks common functionality through intuitive, provider-agnostic APIs. This approach simplifies development and redefines how teams interact with cloud resources. For instance, let’s say we want to perform processes on a cadence (scheduled tasks).

**Runtime Setup Complexity**
For example, when working with scheduled tasks, developers must configure the application to handle the scheduled events appropriately. This involves:

**Integrating cloud-specific SDKs**:**AWS**: Using the AWS SDK to parse EventBridge payloads.**GCP**: Handling pub/sub messages triggered by Cloud Scheduler.**Azure**: Leveraging Dapr bindings for cron jobs.
**Dependency management**:- Ensuring the
[cloud SDKs](https://thenewstack.io/abstracting-cloud-sdks-starting-with-the-runtime/)are up to date and compatible with the runtime. - Adding additional libraries for JSON parsing, logging and monitoring of scheduled events.
- Ensuring the
**Code coupling**:- Application logic often becomes tightly coupled to the cloud provider’s APIs, limiting portability, even between different services from the same cloud provider.
- Code that handles scheduled events becomes harder to test without deploying to a live cloud environment.
**Error handling**:- Developing robust retry logic for when a scheduled task fails.
- Setting up appropriate logging and alerting to monitor runtime issues.
**Provisioning Setup Complexity**
Provisioning the infrastructure for scheduled tasks often requires dealing with multiple layers of cloud-specific configurations.

**Cloud-Specific Resources: **
**AWS EventBridge**:
- Creating a rule specifying the schedule (such as a, cron expression) and target (Lambda function, SQS queue).
- Configuring identity and access management (IAM) roles and policies to allow EventBridge to invoke the target resource.
**GCP Cloud Scheduler**:
- Defining the job with a schedule and target type (HTTP endpoint, Pub/Sub topic).
- Ensuring the target has the correct IAM permissions to accept scheduler invocations.
**Azure Logic Apps**:
- Building a Logic App workflow with timer triggers and configuring connectors to downstream services.
- Managing API connections, including authentication and permissions.
**Environment configuration**:
- Setting up environment variables or secrets for the scheduler to communicate with the application.
- Ensuring that infrastructure changes propagate seamlessly across staging, testing and production environments.
**Error visibility and recovery**
- Implementing manual checks or custom scripts to identify misconfigured schedules or permissions.
- Developing fallback mechanisms if the cloud provider’s native scheduling service experiences downtime.
**Simplifying the Complexity:**
Resource abstraction allows us to avoid direct interaction with cloud-specific APIs. Here is how you could do this in Nitric:

123456789101112131415 |
from nitric.resources import schedulefrom nitric.resources import Nitric# Run every 5 minutes@schedule("process-transactions").every("5 minutes")async def process_transactions(ctx): print("processing transaction")# Run at 22:00 Monday through Friday.@schedule("send-reminder").cron("0 22 * * 1-5")async def send_reminder(ctx): print("sending reminder")Nitric.run() |
Developers define schedules declaratively using Nitric’s high-level SDK:
**Automated mapping**: Nitric maps the schedule to the corresponding cloud service under the hood, managing differences like cron syntax or permissions automatically.**Seamless portability**: Since the schedule configuration is cloud-agnostic, switching between providers (AWS, GCP, Azure) requires no changes to the application code.**Consistency across projects:**All projects behave the same way, implementing scheduled tasks the same way, meaning less security holes to plug across varying implementations.
**Transforming Developer and Business Outcomes**
By focusing on portability, abstraction, and automation, [Nitric](https://nitric.io/docs) creates a development paradigm focused on what matters most, delivering impactful applications. The result is not just faster delivery cycles but also the confidence to innovate without being constrained by cosmetic platform differences or limitations.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)