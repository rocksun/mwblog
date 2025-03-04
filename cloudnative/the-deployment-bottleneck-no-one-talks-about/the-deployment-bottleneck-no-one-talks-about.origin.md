# The Deployment Bottleneck No One Talks About
![Featued image for: The Deployment Bottleneck No One Talks About](https://cdn.thenewstack.io/media/2025/03/a800b619-bottleneck-1024x577.png)
Most applications rely on cloud SDKs to connect to services like message brokers, queues, databases, APIs and more. This introduces deployment friction in three key ways:

**Infrastructure management**– Developers must provision services separately, often leading to misalignment between application code and infrastructure.**Cloud-specific dependencies**– SDKs tightly couple code to a single provider, complicating many tasks, like migrations, local development, testing and multicloud strategies.**Long debugging and recovery times**– Infrastructure mismatches result in failed deployments that are difficult to troubleshoot and roll back.
Rather than working directly with cloud SDKs, a better approach is to introduce a standardized layer between applications and cloud services. This allows developers to interact with essential resources without being tightly coupled to a specific provider’s SDKs. A framework like Dapr helps achieve this by providing a uniform API for interacting with cloud resources.

## Dapr: A Sidecar That Standardizes Cloud APIs
Dapr (Distributed Application Runtime) is a runtime abstraction framework that provides a consistent API for cloud native applications to interact with services like message queues, storage and pub/sub. By acting as a sidecar process, Dapr enables applications to remain cloud-agnostic while simplifying distributed system development.

#### Example: Sending messages with a direct SDK call to AWS
123456789101112 |
import boto3 # AWS-specific SQS setup sqs = boto3.client('sqs') queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/my-queue' def send_message(message): response = sqs.send_message( QueueUrl=queue_url, MessageBody=message ) return response |
This approach has several drawbacks:
- Code is tightly coupled to AWS, which means that switching providers or message brokers/queues requires rewriting the SDK integration.
- Infrastructure must be provisioned in a separate project containing the Infrastructure as Code (IaC) deployment scripts.
- If the queue setup changes, application logic must be updated to match, otherwise there is the risk of infrastructure risk.
#### Example: Sending messages with Dapr
Instead of interacting with a specific cloud service, applications send messages to Dapr’s publish API, which routes them to the appropriate backend.

123456789101112 |
import requestsDAPR_PORT = 3500QUEUE_NAME = "azure-servicebus"def send_message(message): url = f"http://localhost:{DAPR_PORT}/v1.0/bindings/{QUEUE_NAME}" payload = {"data": message, "operation": "create"} response = requests.post(url, json=payload) return response.status_codesend_message({"orderId": "12345"}) |
**Benefits of Using Dapr**
**Faster development and reduced complexity**– Eliminates the need to integrate multiple cloud SDKs or write custom service discovery logic. Dapr provides a simple, consistent API that speeds up development.**Seamless multicloud and hybrid deployment**– Applications remain cloud-agnostic, making it easier to run workloads across AWS, Azure, Google Cloud Platform (GCP), or on-premises without major code changes.**Built-in resilience and observability**– Supports automatic retries, circuit breakers and distributed tracing, improving system reliability and making debugging easier.**Event-driven and scalable by design**– Native support for pub/sub messaging enables developers to build reactive, event-driven architectures that scale efficiently.**Less operational overhead**– Handles service communication patterns automatically, reducing the burden of writing and maintaining glue code for service interactions.
From this, it is clear that Dapr [simplifies the way applications interact with cloud services](https://thenewstack.io/how-simplifying-our-architecture-saved-us-thousands-monthly/), but, before Dapr can interact with the queue, we’ll need to provision it using Terraform or another IaC tool:

1234567891011 |
resource "azurerm_servicebus_namespace" "example" { name = "example-namespace" location = "East US" resource_group_name = azurerm_resource_group.example.name sku = "Standard"}resource "azurerm_servicebus_queue" "example" { name = "example-queue" namespace_id = azurerm_servicebus_namespace.example.id} |
Once created, we’ll also need to configure Dapr to use the correct plugin by defining a component file:
12345678910111213 |
apiVersion: dapr.io/v1alpha1kind: Componentmetadata: name: azure-servicebus namespace: defaultspec: type: bindings.azure.servicebusqueues version: v1 metadata: - name: connectionString value: "Endpoint=sb://example-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your-key" - name: queueName value: "example-queue" |
Even with the runtime abstraction, there is still a fair amount of work that developers have to do to get a basic application running, so this leads us to our next question. What if we didn’t need to create a Terraform project and a configuration file every time?
## Automating Infrastructure Based on Application Behavior
Dapr simplifies interactions with cloud services, but developers must still define and provision infrastructure separately. The next logical step is automating infrastructure provisioning based on the application’s resource usage.

**How this could work:**
**Application-defined infrastructure**– Infrastructure is inferred from the way the application interacts with cloud services.**Least privilege access**– Permissions adapt dynamically each time the application is redeployed, ensuring that the principles of least privilege permissions are always applied.
Infrastructure integrations now serve two purposes as they now also identify the application’s infrastructure requirements.

**Example: Fully Automated Infrastructure Provisioning**
A runtime-aware system can automatically provision the necessary resources based on application usage.

In this example:

- An API is exposed for creating user profiles.
- A key-value store is used to store user details.
- A storage bucket is used for profile picture uploads.
12345678910111213141516171819202122232425262728 |
import jsonfrom uuid import uuid4from nitric.resources import api, kv, bucketfrom nitric.application import Nitricfrom nitric.context import HttpContext# Create an API named publicprofile_api = api("public")# Access profile key-value store with permissionsprofiles = kv("profiles").allow("get", "set", "delete")# Define a storage bucket for profile picturesprofile_pics = bucket("profile-pics").allow("write", "read", "delete")@profile_api.post("/profiles")async def create_profile(ctx: HttpContext) -> None: pid = str(uuid4()) name = ctx.req.json["name"] age = ctx.req.json["age"] hometown = ctx.req.json["homeTown"] await profiles.set(pid, {"name": name, "age": age, "hometown": hometown}) ctx.res.body = {"msg": f"Profile with id {pid} created."}Nitric.run() |
The key here is that the application is able to automatically communicate its required resources and permissions to generate a specification that can be mapped to pre-built IaC modules that fulfill the requirements.
You might also notice that at no point have we specified which cloud the IaC will be generated for. This means that [IaC can be automated](https://thenewstack.io/achieve-gitops-on-day-one-with-iac-automation/) for any cloud, so long as we have Terraform or Pulumi modules that can provision into that cloud. You can learn more about how this works in practice [here](https://nitric.io/blog/cloud-sdks).

## Addressing Concerns With Automation
When introducing automation into enterprise workflows, it’s natural to have concerns about security, compliance and governance. Let’s break down these challenges and how they can be effectively managed.

**Separation of Concerns in Infrastructure Definition**
One of the biggest concerns with frameworks that [generate infrastructure from application code](https://thenewstack.io/can-ai-generate-functional-terraform/) is the fear that developers will end up defining infrastructure directly. Does this blur the line between application and operations responsibilities?

This approach actually strengthens separation of concerns when done right. Instead of manually provisioning resources, developers describe their application’s runtime needs without specifying how they’re deployed. Operations teams retain control over enforcement, security and cost management while reducing friction in translating application requirements into infrastructure. In fact, this [reduces misconfigurations and speeds up delivery](https://nitric.io/blog/dropbio) by ensuring infrastructure always aligns with what the application actually needs.

**Security Risks in IAM Policies and Provisioning**
Could automation inadvertently grant excessive permissions or provision unauthorized resources? The good news is that automation doesn’t mean losing control; it actually strengthens security when done right. By enforcing policies through code, using tools like Open Policy Agent (OPA), AWS SCPs (service control policies) or predefined identity and access management (IAM) templates, organizations can ensure that permissions are consistently applied and reviewed before deployment. In fact, automation reduces human error, which is a common [cause of security gaps](https://thenewstack.io/how-iam-missteps-cause-data-breaches/).

**Compliance with SOC 2, HIPAA and PCI DSS**
Many organizations worry that automation might conflict with strict regulatory frameworks like SOC 2, HIPAA or PCI DSS. In reality, automation is a powerful tool for maintaining compliance rather than undermining it.

Regulations emphasize traceability, repeatability and control, all of which automation enhances. Instead of relying on manual processes, which can be inconsistent and error-prone, automated workflows ensure every deployment aligns with compliance requirements. Pre-approved infrastructure configurations can help as well. By defining approved patterns and enforcing them through automation, organizations can ensure that only compliant setups are deployed.

**Enterprise Workflows and Pre-Approved Configurations**
For enterprises, automation must align with structured workflows. It’s understandable to worry that fully abstracting infrastructure provisioning could remove necessary guardrails. Instead of allowing unrestricted provisioning, automation can enforce enterprise-approved configurations. Platform teams still set the rules, defining approved configurations and ensuring consistency across environments.

## Final Thoughts
Rather than replacing governance and compliance processes, automation can reinforce them by making security and compliance part of the development workflow. With predefined policies, continuous monitoring and standardized configurations, organizations can improve both security and efficiency while maintaining the necessary controls.

You can try out this automation approach using Nitric. [Here are some tutorials](https://nitric.io/docs/guides) to get you started.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)