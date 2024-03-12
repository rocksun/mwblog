# How to Scaffold a New Application with a Developer Portal
![Featued image for: How to Scaffold a New Application with a Developer Portal](https://cdn.thenewstack.io/media/2024/03/16d01e0a-scaffold-new-application-portal-1024x576.jpg)
When platform teams start creating a new application, they often get bogged down during the scaffolding process — putting the structure, file system and other pieces in place to start writing code. This bottleneck often stems from issues that developers and R&D managers want to solve.
Developers want:
- To move away from creating each new microservice or application from scratch and to start using standardized automation.
- A self-service process to create the initial application skeleton rather than opening a ticket to the platform team to help configure CI/CD or create cloud resources.
R&D managers want:
- To align their microservices and set their
[organizational standards](https://thenewstack.io/setting-kubernetes-standards-with-platform-engineering/)for CI/CD, security and documentation with ease.
- To provide golden paths for developers to manage their own microservice development cycle without assistance.
Often, the go-to approach for scaffolding a new application is to create a new repository from a template. However, a single templated repository may not meet all of a developer’s needs. They might require multiple git repositories, more logic with external tools and platforms, more work to set up automation and other complexities.
## The Alternative: A Big Mess for Development Teams
Manually building microservices creates a real mess for development teams. Let’s look at two perspectives.
### The Developer’s Perspective
When developers don’t have a template, they have to cobble together microservices piece by piece, manually configuring and setting up the infrastructure. This creates chaos, with inconsistent coding practices and difficulty meeting organizational standards.
Having to rely on traditional ticketing systems to create infrastructure compounds the issues, adding frustration, causing delays and slowing down the development process.
Imagine a developer from a large organization who needs to develop a new microservice as part of a ticket created by the product manager. Just because they’ve considered all of the implementation steps — such as which language they’ll use, how they will make it generic to support different webhooks and how they’ll write awesome code — doesn’t mean they’re ready to go.
Ideally, they can check if someone has already written code that they can reuse. Then they’ll need to:
- Create a new repository with a README file and a folder hierarchy aligned with the organization’s standards.
- Create a Kafka topic by writing an Infrastructure as Code (IaC) code section to spin up a Kafka topic alongside their service. Alternately, in a larger corporate organization, they’ll have to open a ticket to the
[platform engineering team](https://thenewstack.io/how-team-topologies-supports-platform-engineering/), which means waiting one to three days.
- Create a boilerplate for tests and configure the CI process.
- Configure
[SonarCloud](https://www.sonarsource.com/ ?utm_content=inline-mention)scans on every merge to the main branch.
- Create a new Argo CD app and connect it to their new service by opening a pull request to the Argo management repository.
- Deploy the initial application to a test environment.
This adds up to a great deal of work before the developers can even start coding. Developers must have significant knowledge of the engineering organization’s standards to comply with them. Being responsible for so many tasks outside their comfort zone (coding) increases cognitive load and makes it more challenging for those developers to get through their to-do lists.
It’s also difficult for R&D managers to guide developers through these issues. This impacts productivity, innovation and efficiency of the entire development workflow, and ultimately affects the overall business.
### The Platform Engineer’s Perspective
For platform engineers, engineering standards are key to keeping microservices organized and consistent. They manage hundreds of microservices and see the same problems again and again: different repository structures that make it difficult to search for information, lack of essential documentation, unprotected repository branches, deployment setup issues and outdated versions.
The reality is that it’s impossible to expect so many different teams to comply with their company standards without having guidance or automation.
## How to Give Developers a Golden Path
Giving developers a ready-to-use setup for new applications helps solve these problems. Using an internal developer portal for the setup goes beyond a basic repository, and provides essential automated resources, such as:
- A ready-to-use repository
- An easy-to-follow pipeline
- A Terraform request for a new database
- An Argo CD app
- A simple Kubernetes deployment
- A new lambda function linked to the repository
- Preconfigured
[AWS](https://aws.amazon.com/?utm_content=inline-mention)S3 buckets
Developers can use these ready-made paths to adhere to standards with ease and maintain consistency without complications.
## Three Steps to Create a Self-Service Scaffold
To get started quickly, follow these steps:
### Step 1: Define the Application Suite
No two platform teams have the same standards and scaffolding processes. Platform engineers need to ask what developers need when packaging a new application to help them focus on the thing they do best: writing code.
While the answers to these questions may vary across teams, they likely involve elements that engineers can automate or templatize to give developers a head start and independence.
Gaining continuous feedback from developers on their pain points and what they’d like to see — through surveys, informal conversations and qualitative interviews — enables engineers to embrace a
[product mindset](https://www.getport.io/blog/platform-as-a-product-portal-as-a-product-why-you-should-use-both). This ensures that platform engineers [focus on what developers actually need](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) to scaffold an application, not what they think should be included.
For this example, imagine that scaffolding a new application includes creating a repository, configuring CI/CD and creating cloud resources with Terraform.
### Step 2: Determine the Developers’ Inputs
Identifying which parameters should be defined by developers is key. You want to focus on
[abstracting away complexity](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/), so ask only for inputs that genuinely matter for customizing the scaffolding process. In other words, focus on the “what” rather than the “how” to enable developers to pinpoint specific aspects of their projects without having to think about implementation details.
Here is an example list of basic common inputs:
- Application name
- Description
- Programming language
- Number of Kubernetes replicas
- Kafka topic name
- Database
### Step 3: Create the Scaffolding Automation
Using the developers’ inputs, the scaffolding logic can automate the setup of the new project, eliminating manual steps for creating the repository, setting up the infrastructure and configuring the tools and environments.
The example in the following diagram achieves automation using a GitHub Action.
The diagram shows how the automation interacts with the different platforms based on the developer’s inputs, while adhering to the specific permissions that have been chosen and managing resources using the company’s best practices.
## Enabling Self-Service with a Portal
The previous steps enabled automation for creating a new application. But that’s not always enough.
Managing application creation with GitHub Actions can be challenging for developers, highlighting the need for a centralized solution. A self-service portal with an intuitive user interface, detailed role-based access control (RBAC), robust input validation and a customized approval process can significantly simplify the application setup process without additional development effort.
I will demonstrate how this works with Port, a no-code platform for
[creating internal developer portals](https://thenewstack.io/how-to-create-an-internal-developer-portal-mvp/). Port can integrate with your existing automation, wrap it with an intuitive user interface and create an easy, abstracted experience for developers. Port also supports managing and triggering long-running and asynchronous actions, and shows developers the run logs they need.
The process begins when a user triggers a self-service action in the developer portal UI.
A payload that includes the user inputs and relevant action metadata is sent to the desired GitHub workflow.
A job is triggered and the user receives continuous indication about its progress.
### Visualize Application Creation
Once you’ve built a customized self-service experience that matches the scaffolding logic and have used it to create an application, you can visualize all of the created resources (e.g., Argo application, cloud resources, Sonar scans) in one place in the context of the related application. This way, the whole process and its outputs are reflected in every step for your developers.
Once everything is set up, the routine to create a new application using Port will be as follows:
1. A developer signs in to Port and clicks on the “Scaffold new Service” action in the Self-Service Hub.
2. The developer provides the relevant inputs for the scaffolding process in a customized form.
3. The action initiates and the scaffolding process is reflected in Port, including the process status and logs.
4. Once the application is scaffolded, the developer can see it in the service catalog, connected to the relevant related resources, such as SonarQube issues, Argo applications, Amazon RDS instances, AWS S3 buckets and Kafka topics.
5. The application and its related entities can also be visualized in a bird’s-eye graph view.
## What’s Next?
You’ve created your application, but you’re not exactly done. The process above is the first step in ensuring an application meets standards. From then on, you have to ensure the standards are maintained. To do this, you can use the portal’s
[Scorecards](https://www.getport.io/product/scorecards-and-initiatives) to evaluate the maturity, production readiness and engineering quality of your applications.
To streamline the process of scaffolding a new application, you need to think with a product cap on: The scaffolding has to meet the goals of the developers, while ensuring the process incorporates your organization’s DNA. Port enables you to customize the process to fit your culture and standards. By doing so, you give developers the best possible experience while keeping your guardrails in place.
For more insights on scaffolding a new application, check out our
[step-by-step guide](https://docs.getport.io/guides-and-tutorials/scaffold-a-new-service). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)