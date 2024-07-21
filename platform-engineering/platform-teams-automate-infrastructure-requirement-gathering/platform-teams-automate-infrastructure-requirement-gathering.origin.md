# Platform Teams: Automate Infrastructure Requirement Gathering
![Featued image for: Platform Teams: Automate Infrastructure Requirement Gathering](https://cdn.thenewstack.io/media/2024/07/53b35cfb-automate-1024x642.png)
One of the most challenging issues in application development is the disconnect between development and operations teams. Communication challenges quite easily lead to misaligned expectations and broken deployments. One of the most mission-critical and brittle areas of communication between these two teams is infrastructure requirements, and it has seemed impossible to solve over the years.

But there’s now finally a solution to this communication gap: automation to streamline infrastructure requirement gathering.

## Communication Challenges
Platform engineering teams frequently face the difficulty of gathering accurate requirements from development teams about their applications. Developers, often unaware of the specific [infrastructure information needed](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom/), might provide incomplete or incorrect data.

And, of course, there’s the more drastic “throw it over the fence” scenario. Once developers are finished building application logic, they hand it over to the [platform team to painstakingly figure out what infrastructure](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/), configurations and permissions are needed to run it reliably, securely and efficiently in the cloud.

Poor communication of infrastructure requirements can lead to infrastructure drift, where the deployed infrastructure no longer matches the actual needs of the application. This drift causes applications to fail, leading to stressful deployment days, late-night troubleshooting sessions and the dreaded war rooms.

## Infrastructure Drift and Its Consequences
Infrastructure drift occurs when the actual state of infrastructure deviates from the desired state defined in the [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/) scripts. Given the challenges with manual communication of infrastructure requirements, it’s no surprise that teams run into drift. Problems include:

**Manual changes:**Developers or operations teams might make manual changes to the infrastructure without updating the IaC scripts.**Inconsistent updates:**Updates to the application might not be reflected in the infrastructure configuration.**Lack of communication:**Developers might not communicate new requirements or changes effectively to the operations team.
The consequences of infrastructure drift are severe:

**Deployment failures:**Mismatched configurations can cause deployments to fail, leading to application downtime.**Increased stress:**Operations teams often have to deal with last-minute fixes, leading to long hours and high stress levels.**Reduced trust:**Frequent deployment issues erode trust between development and operations teams, making future deployments even more challenging.**Higher costs:**Infrastructure drift incurs costs due to lost revenue from downtime, unnecessary expenses from misconfigured resources, increased labor costs for fixing issues and security vulnerabilities requiring remediation.
The solution to these infrastructure drift issues, which stem from the challenges in communicating infrastructure requirements, lies in automation. Let me introduce the concept of a resource specification that can automatically communicate runtime application requirements to the operations team.

## The Solution: Automated Resource Specifications
Imagine a system where the required infrastructure resources are inferred directly from the application code. This system would generate a resource specification that acts as live documentation, detailing the runtime requirements of the application. This specification could then be used to automate the provisioning of infrastructure, ensuring that the deployed resources match the application’s needs precisely.

Imagine also that while infrastructure requirements are inferred from application code, operations teams still retain control over critical decisions. They select the cloud provider, services and security configurations for each resource, allowing them to apply their expertise and enforce best practices. This ensures that the infrastructure remains robust and compliant with organizational standards, combining automation with expert oversight.

This is the crux of the new concept of [Infrastructure from Code (IfC)](https://thenewstack.io/terraform-isnt-dead/), which builds upon Infrastructure as Code (IaC). What it means is that [IfC frameworks like Nitric](https://github.com/nitrictech/nitric) can provide the solution operations teams have been looking for: real-time, detailed specifications of the resources and permissions the application needs.

### An Example of Automated Resource Specification
Here’s an example of how resource specifications can be generated from application code. This application runs on a daily schedule and publishes an updated event which includes a URL.

From this code snippet, the Nitric framework gathers the following information:

- Bucket resource:
- ID: reports
- Config: Default setup.
- Topic resource:
- ID: updated
- Config: Default setup.
- Scheduled task resource:
- ID: process-reports
- Config: Target service
`hello-world_services-hello`
with a cadence of every five days.
- Policy resource:
- ID: eccfffd7a5e31407be6f7a5663665df4
- Config: Policy allowing read and write actions on the reports bucket for the
`hello-world_services-hello`
service.
- Policy resource:
- ID: 74e4fa18c1527363767c00582b792ed9
- Config: Policy allowing custom action 200 on the updated topic for the
`hello-world_services-hello`
service.
- Service resource:
- ID:
`hello-world_services-hello`
- Config: Service with an image
`hello-world_services-hello`
, one worker and an environment variable`NITRIC_BETA_PROVIDERS`
set to true.
- ID:
This information is compiled into a resource specification, ensuring that all necessary resources are provisioned accurately and consistently.

Note: The IDs are auto-generated to uniquely identify resources.

## Automatically Applying Resource Specifications
Generating the resource specification automatically solves a huge portion of the communication and drift issues I discussed above. But platform teams can further benefit from automatic application of those specifications to the IaC modules they’ve created. Frameworks like [Nitric](https://nitric.io), which I used for the example above, also automatically compose deployment scripts for the platform team.

Using the resource specification, each component is mapped to the corresponding IaC modules. For instance, if the application specifies a bucket resource and the target cloud provider is AWS, the system will use a Terraform module to provision a schedule handler:

This automated mapping ensures that the deployed infrastructure remains in sync with the application’s requirements, preventing drift and reducing the likelihood of deployment failures.

## No More ‘Throwing Over the Fence’
By bridging the gap between development and operations teams with automated resource specifications, it’s possible to create a more harmonious and efficient deployment process. This approach not only reduces the risk of infrastructure drift and deployment failures but also fosters better communication and trust between teams. Embracing this method can lead to more reliable, stress-free deployments and a more resilient infrastructure.

**Consistency:**Automated resource specifications ensure that the deployed infrastructure matches the application’s needs, reducing the risk of drift.**Efficiency:**By automating the generation and provisioning of resources, deployment times are shortened, and the need for manual intervention is minimized.**Reduced stress:**Operations teams can trust that the infrastructure will be provisioned correctly, leading to smoother deployments and fewer late-night troubleshooting sessions.**Improved communication:**Developers don’t need to worry about specifying infrastructure requirements manually; the system takes care of it, ensuring accurate communication of needs.
Learn more about this approach by checking out what we’re building with the [open source Nitric framework](https://github.com/nitrictech/nitric). We’d love your feedback, ideas and contributions to help automate the most tedious parts of platform engineering.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)