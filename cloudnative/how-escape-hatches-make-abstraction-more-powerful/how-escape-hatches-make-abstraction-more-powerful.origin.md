# How Escape Hatches Make Abstraction More Powerful
![Featued image for: How Escape Hatches Make Abstraction More Powerful](https://cdn.thenewstack.io/media/2024/03/f8c82ab7-escape123-1024x682.jpg)
The software community loves to debate on the topic of abstraction; somewhere, someone’s been burned by lock-in and can no longer fathom the possibility that there are actually well-crafted abstractions capable of catering to the unique nature of application development. At the same time, our entire industry is built on layers and layers of abstraction.
API gateways, for example, abstract away the details of routing, security and scalability of API endpoints, allowing developers to manage their APIs efficiently without delving into the underlying infrastructure. Similarly, Amazon S3 provides an abstracted, scalable storage solution, enabling users to store and retrieve any amount of data without managing the physical storage systems.
These abstractions are so seamlessly integrated into the fabric of cloud application development that they become almost invisible to the developers using them. Yet, they are foundational, enabling rapid development, deployment and scaling of applications by handling intricate details behind simple interfaces.
Escape hatches are a vital feature to ensure developers are not locked into specific technology, especially when abstraction is involved. They offer a path to directly access and use the underlying cloud services and work with existing resources or toolsets. In addition, they allow you to take advantage of the benefits of the framework while providing the flexibility, power and control necessary to build complex, high-performance and customized applications in a cloud native environment.
## Why Escape Hatches Are Crucial to Cloud Abstraction
While abstraction layers aim to cover common and foundational use cases, they are purposefully built to avoid exposing every single configuration or setting available. An escape hatch allows for more fine-grained control over the cloud services, enabling performance optimizations and customizations.
Abstraction layers that don’t purposefully introduce escape hatches are harder to trust and harder to work with. However, many abstraction frameworks readily acknowledge the need for escape hatches and anticipate that changes should be possible to any integration. Engineers who have been burnt once or twice may find these frameworks easier to trust.
## Examples of Good Escape Hatches
The best way to understand what makes a good escape hatch is to look at some examples. Previously, I noted that most software is built upon layers of abstraction, so I’ll start with one of the most common abstractions across projects: databases.
### Example 1: Prisma
[Prisma](https://www.prisma.io/) is an open source database toolkit that simplifies data access and management in Node.js and TypeScript applications. It provides an ORM (object-relational mapping) layer that enables developers to interact with their database through a high-level API.
Despite its abstraction, Prisma acknowledges the need for direct database access in certain scenarios, thus it provides escape hatches for when developers need more control or need to execute database operations not covered by Prisma’s API.
One of the most significant escape hatches Prisma offers is the ability to execute raw SQL queries directly against the database. This feature is crucial for scenarios where the Prisma Client API does not support a specific database operation or when an optimization requires direct SQL for efficiency.
Here’s a simple example of how you might use
$queryRaw to perform a complex
SELECT query that isn’t easily expressed through Prisma’s generated client API:
Note: Prisma mitigates with risks such as SQL injection by providing a tagged template literal syntax for
$queryRaw, which helps safeguard against SQL injection by allowing variable binding.
### Example 2: Pulumi
[Pulumi](https://www.pulumi.com/) is an Infrastructure as Code tool that allows developers to define, deploy and manage cloud services using programming languages such as TypeScript, Python, Go and C#. It supports multiple cloud providers, including [AWS](https://aws.amazon.com/?utm_content=inline-mention), [Microsoft](https://news.microsoft.com/?utm_content=inline-mention) Azure,
The Automation API encapsulates the APIs of various cloud providers, allowing developers to interact with cloud resources in a consistent and idiomatic way across different clouds. To access upcoming or experimental features not yet fully supported by Pulumi’s abstractions, escape hatches provide built-in flexibility and extensibility for developers.
Pulumi’s dynamic providers allow you to define custom resources when existing providers do not cover your needs. By implementing the four methods — create, read, update and delete — you can integrate any external service or API into a Pulumi application.
Here’s a snippet that you can expand on in the detailed
[Pulumi Dynamic Providers](https://www.pulumi.com/docs/concepts/resources/dynamic-providers/) guide:
This approach lets developers incorporate the latest cloud features into their Infrastructure as Code, even if those features aren’t yet encapsulated in Pulumi’s resource providers.
### Example 3: Nitric
[Nitric](https://nitric.io) is a framework built to leverage Pulumi, Terraform and the cloud SDKs, designed to simplify the development of cloud native applications by providing an abstracted set of APIs that can work across different cloud providers. The abstraction allows developers to write code that is less dependent on the specific services and APIs of any single cloud provider, making it easier to deploy applications across multiple clouds or switch providers if needed.
Nitric providers handle the provisioning and runtime operations of cloud applications. By extending a provider, developers get an escape hatch to override or extend the configuration of the abstracted resources. This includes tweaking performance settings, security rules or other provider-specific configurations that are not exposed through the framework’s standard API.
Here is an example of how a request for a bucket resource is deployed, which developers can easily modify or extend:
This approach means that when a developer needs to use a specific AWS service feature not currently abstracted by Nitric, they can drop down to the underlying abstracted technologies to accomplish their goals.
## Leverage Abstractions with Escape Hatches
Good escape hatches mean that the use of an abstraction framework doesn’t equate to being locked into its limitations. They provide a safe way for when you need to step outside the bounds of the abstraction to meet an application’s specific needs, whether for optimization, access to new features or integrating with legacy systems.
A balance between the convenience of abstraction and the flexibility provided by escape hatches ensures that developers can enjoy the best of both worlds. We’re thinking about and working on this problem at
[Nitric](https://nitric.io). Come chat with us! [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)