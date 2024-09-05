# Beyond IaC: Fixing Cloud’s Separation of Concerns Problem
![Featued image for: Beyond IaC: Fixing Cloud’s Separation of Concerns Problem](https://cdn.thenewstack.io/media/2024/09/0eb06b5c-lanes-1024x576.jpg)
[Juice Dash](https://www.shutterstock.com/g/Juice+Dash)on Shutterstock
Managed services and Infrastructure as Code (IaC) have become indispensable for modern apps. They simplify the deployment and management of cloud resources, offering a streamlined path to building scalable, reliable systems. However, there’s a hidden cost to this convenience: a growing brittleness in our applications and a severe lack of true separation of concerns. Let’s explore these issues, using a practical example to highlight the challenges of working with managed services and IaC.

## The Questions To Ask
Here are some questions to ask to determine if your environment suffers from the lack of separation:

- If you no longer need a resource, like an S3 bucket, could a mistake mean it continues existing in the project’s IaC (such as a Terraform project), while no longer being referenced in the application code? (Do the code and the IaC need to be kept in sync manually?)
- If your application needs a new resource, do application developers need to talk to automation engineers to have it added to the IaC code (a Terraform project) or platform? (Is an application change also an automation change?)
- Does changing the services deployed in your IaC code (such as changing
[AWS](https://aws.amazon.com/?utm_content=inline+mention)SNS to EventBridge) cause simultaneous changes in your application code (swapping from the SNS client library to the EventBridge library)? - When you build a new app or use new resources, are local tests insufficient? Do you need to test your app in the cloud to be sure it works?
- Could a typo in a value, such as an environment variable name, cause your application to break?
- Do you limit projects to restricted scaffolds or templates (such as through a developer portal) to ensure teams use infrastructure that meets your organization’s policies?
- If a cloud provider released a faster, cheaper or better alternative to an existing managed service, would it take considerable time or effort to migrate to that service? Have you avoided or postponed these sorts of changes previously?
If the answer is yes to any of the above, you have the problem we’re discussing. If you answered no to everything, either you’re avoiding managed services, you already use Infrastructure from Code (IfC) or you’ve found another solution — one that I’d love to learn about.

## The Illusion of Separation: A Practical Example
Consider a common scenario: You’ve built an application that relies on SNS for asynchronous messaging. After some time, you decide to switch from SNS to EventBridge — perhaps due to cost, performance, standardization with other apps, or because you need to consume other event sources. This same sort of change could occur with any other managed service, such as file storage, queues, HTTP gateways, etc.

On the surface, these seem like easy changes: The two services have similar interfaces and provide similar functionality for your needs. Let’s break down what really happens:

### 1. Code Changes
Your application code is tightly coupled to the SNS service. You use the SNS libraries directly in your code, you handle SNS-specific errors, and rely on features the way SNS implements them. Swapping out SNS for another service means rewriting significant portions of your code. You’ll need to replace the libraries, modify API calls and perhaps rethink your error handling and retry logic.

### 2. IaC Changes
Your Infrastructure as Code (IaC) scripts are equally tied to SNS. Terraform, CloudFormation or any other IaC tool you’ve used will have scripts explicitly defining the SNS topic, policies/roles, and environment variables for services that send messages to the topic and any subscribers that respond to events sent to the topic. Replacing SNS with another service means diving into these scripts, modifying resources, updating permissions and ensuring the new service is correctly configured.

### 3. Test Changes
Your tests also need to be updated. Unit tests and integration tests must be rewritten to accommodate the new service. Mocking SNS in your tests? Those mocks need to be replaced with ones for the new service. Mocking SNS events in your subscriber tests? Those need to change too.

### 4. Deployment Risks
There’s no way to know if your changes are correct until you deploy them. Even with comprehensive local testing, there’s always a risk that something will break once deployed. It might be a typo in your environment variables or an incorrect IAM policy that fails to allow subscriptions to trigger subscribers. These issues are extremely common and particularly frustrating. If they’re deep enough in your application, they may only become apparent when your users start experiencing problems.

### 5. Configuration Pitfalls
Even if you get the code and IaC changes right, configuration issues can still arise. Managed services often rely on specific configuration values, such as resource IDs or endpoint URLs. A simple typo in these configurations can lead to hours of debugging. Unlike traditional code, these errors won’t be caught at compile time — you’re left to discover them during runtime.

## The Illusion of Separation
Many believe that separating code with different responsibilities into different files or modules means they’ve achieved separation of concerns (for instance, IaC code like Terraform being separate from app code). Separation of concerns isn’t just about proximity: It also means changes in one module don’t force changes in unrelated areas. In our example, a simple switch from one managed service to another equivalent service requires changes across the entire stack — code, IaC, tests and configurations. They all look separate on the surface, but the coupling is so significant that the system ends up brittle, and changes ripple throughout the project.

### What Separation Is Really About
One description of separation of concern is:

“Modularity, and hence separation of concerns, is achieved by encapsulating information inside a section of code that has a well-defined interface.”
— [Wikipedia](https://en.wikipedia.org/wiki/Separation_of_concerns)

Where is this well-defined interface for infrastructure code in typical cloud development? The traditional model fails to provide it, leaving developers and infrastructure teams to constantly coordinate, reconfigure and retest every time a change is made.

## A Better Approach: Infrastructure From Code
This is where Infrastructure from Code (IfC) comes in. The style of IfC provided by Nitric solves the problem by providing a well-defined interface for infrastructure requirements and usage. It separates the concerns of application architecture from deployment architecture by abstracting the underlying infrastructure details away from the application layer. Unlike traditional IaC, it doesn’t just separate the deployment scripts into other files — it completely decouples the application, separating client SDKs, tests, resources identifiers and other components that cause a brittle relationship between the deployment automation and the application code.

With IfC, when you change providers or individual cloud services, the changes are isolated to a new infrastructure layer. Application developers aren’t forced to know the details. They can build and test their applications, confident that the infrastructure will work seamlessly regardless of the underlying provider because it will conform to a strict interface. Similarly, deployment automation engineers can focus on ensuring the infrastructure is robust, knowing that their changes won’t inadvertently break the application.

## A Real-World Example
Let’s walk through a concrete example. We’ll start with a project using Terraform for Infrastructure as Code. (We use Terraform here due to its familiarity. The example would be equally valid with Pulumi, AWS Cloud Development Kit or another IaC tool.) The project deploys a basic Go application that interacts with an SNS topic. We’ll then swap the SNS topic for an EventBridge event bus, showing the necessary application code, deployment code and test changes. We’ll also demonstrate how the same project could be implemented using Nitric and Infrastructure from Code, highlighting the reduction in complexity and the improved separation of concerns without limiting configurability or access to the underlying services.

You can see the full [project on GitHub](https://github.com/jyecusch/iac-ifc-comparison), where each step is represented by a commit, illustrating the breadth of changes needed for what should be a simple swap.

## Steps To Change the IaC Example
For brevity we only include examples of the changes. The full diff is significant, and can be viewed on the latest commit [on GitHub](https://github.com/jyecusch/iac-ifc-comparison/commits/main/).

### 1. Update the application code
Since the code uses the AWS SNS and Lambda libraries, we need to update references and implementations to use EventBridge instead for sending and receiving messages.

For example, this code to publish messages to SNS…

… would change to code that sends the messages to EventBridge instead:

### 2. Next, update the tests
Since the code relied on the SNS and Lambda libraries, those services were mocked for unit testing. With the change, our tests need to be updated to mock the new services and event types.

For example, instead of creating a mock SNS client…

… we’ll create a mock EventBridge client instead:

You might generate the mock clients automatically, but the tests using those mocks need to change regardless.

### 3. Lastly, update the deployment automation
In our example we’ve included a Terraform module for EventBridge from the outset to better simulate an established environment. This makes the Terraform changes minimal — as they should be.

We start with an SNS module and variables passed to the publisher:

We change that to an EventBridge module and the new variables needed by the publish:

Unfortunately, one problem that remains is that we need to be sure the environment variables in the Terraform HCL (HashiCorp Configuration Language), such as `SNS_TOPIC_ARN`
or `EVENT_BUS_NAME`
, exactly match the names used in the application code. Typos or other mistakes here can be tricky to find without deploying the application and testing it.

## Steps To Change the IfC
Unlike the IaC, the IfC changes are so minimal that we can show the entire change needed here instead of just an example.

We start with a `nitric.aws.yaml`
stack file configured to use the default Nitric AWS provider, which uses SNS for topics:

Then, we swap for any other provider we want. In this case, it’s an extended provider that uses EventBridge instead of SNS:

All of the other code and tests remain unchanged because they were consuming the [Nitric Topics API](https://nitric.io/docs/messaging), which decoupled the code from direct integration with SNS or EventBridge.

Much like building Terraform modules, the EventBridge change in the Nitric provider is isolated. However, unlike using Terraform alone, Nitric can also encapsulate the runtime code for the new service, making it possible to build and test independently.

Since a Nitric provider can be built or customized using any IaC tool, such as Terraform, Pulumi or AWS CDK, granular control can still be maintained and nothing will be lost by adding IfC.

## Next Steps
The promise of managed services and IaC is undeniable, but without proper separation of concerns, you’re left with a brittle, tightly coupled system. Infrastructure from Code solutions can introduce a new layer of separation, providing a clean separation between application development and deployment.

We’d love for you to try it yourself by following a guide in the [Nitric Docs](https://nitric.io/docs) or reviewing the project on [GitHub](https://github.com/nitrictech/nitric).

If you have feedback on this article, Nitric or the example project, we’d be grateful to hear it. [Chat with us on Discord](https://nitric.io/chat).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)