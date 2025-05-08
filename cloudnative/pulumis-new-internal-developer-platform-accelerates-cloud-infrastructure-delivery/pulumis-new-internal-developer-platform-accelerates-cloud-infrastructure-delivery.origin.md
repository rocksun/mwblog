# Pulumi’s New Internal Developer Platform Accelerates Cloud Infrastructure Delivery
![Featued image for: Pulumi’s New Internal Developer Platform Accelerates Cloud Infrastructure Delivery](https://cdn.thenewstack.io/media/2024/11/75da641c-pulumi-1024x768.png)
At its [user conference](https://www.pulumi.com/pulumi-up/) today, Infrastructure as a Service (IaaS) provider [Pulumi](https://www.pulumi.com/) introduced Pulumi IDP, an internal developer platform (IDP) designed to speed up cloud software delivery while embedding security and governance from the get-go.

Built to run atop Pulumi’s popular open source[ infrastructure as code (IaC) platform](https://www.pulumi.com/product/infrastructure-as-code/), the company claims that Pulumi IDP enables engineering teams to go from “concept to cloud” in merely a few minutes — which can eliminate weeks or months of conventional overhead.

The platform addresses a rapidly expanding market segment — one which includes Qovery, Terraform, Humanitec, OpsLevel, and Coherence. According to [Gartner](https://gartner.com), [80% of large enterprises](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) are expected to deploy internal developer platforms within the next two years. Pulumi IDP addresses this trend by combining infrastructure-first principles with enterprise-grade controls, offering developers and platform engineers a flexible, extensible foundation for cloud innovation at scale.

Pulumi is launching its [IDP](https://thenewstack.io/platform-engineering-face-off-to-idp-or-not-to-idp/) to enable developers to spin up cloud environments easily while automatically maintaining best practices and security, thanks to a new agentic AI feature that can be accessed verbally if needed. This is designed to address the common problem of platform teams being bottlenecks.

The IDP aims to empower developers — in addition to line-of-business staff — without sacrificing time, security, or governance, CEO and co-founder[ Joe Duffy](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/) told *The New Stack.*

“Pulumi IDP is the cloud infrastructure platform modern teams have been asking for — multicloud, infrastructure-first, and deeply flexible,” Duffy said. “It enables organizations to move fast without breaking things or compromising on security or governance. This is about turning the cloud into a competitive advantage.”

Duffy said the eight-year-old, Seattle-based company reports over 1 million weekly [downloads](https://www.pulumi.com/docs/iac/get-started/) of its tools. It already is a prominent player in [infrastructure automation](https://thenewstack.io/introduction-to-infrastructure-as-code/) with more than 3,500 customers and 350,000 global users.

**A New Chapter in Developer Enablement**
Pulumi compiled insights into its [IDP](https://thenewstack.io/idp-vs-self-service-portal-a-platform-engineering-showdown/) gained from hundreds of customer implementations, transforming bespoke internal solutions into a ready-to-deploy platform that meets enterprise needs out of the box, Duffy said.

Rather than forcing platform teams to choose between building highly customized solutions or adopting inflexible commercial offerings, Pulumi IDP offers a third path — meeting teams at the infrastructure layer and extending upward to enable developer self-service.

“We’ve made it so that even line-of-business staff can use the IDP to save time on project deployments,” Duffy said. “Moderna, one of our customers, wanted to enable data scientists to actually spin up experimentation environments as they’re doing vaccine research and development. Obviously, data scientists typically aren’t cloud infrastructure experts. Now they can participate in the development of their tools. Moderna really needed to enable developers to spin up cloud environments as they’re developing their software without the data scientists having to file tickets and wait for months.”

Another early adopter, CLEAR, migrated from a lower-level HashiCorp Terraform-based stack to Pulumi, streamlining infrastructure deployment using a custom YAML schema that simplified cloud access for its development teams.

**Enabling Best Practices at Scale**
Pulumi IDP has an internal registry where platform teams can publish reusable infrastructure patterns such as components, templates, and policies. These building blocks — written in any supported language, such as Python, Go, Java, C#, TypeScript, or YAML — serve as standard blueprints for rapidly provisioning projects such as web apps, microservices, or data pipelines.

The registry supports built-in documentation, semantic versioning, usage tracking, and discoverability. Organizations can codify security, cost, compliance, and operational standards directly into these building blocks, ensuring new infrastructure adheres to internal requirements from the start.

In addition, this codification of organizational best practices brings rigor to infrastructure provisioning while giving developers the freedom to build faster without sacrificing oversight.

**Flexible Developer Interfaces With Built-In Guardrails**
Pulumi IDP provides developers and data scientists multiple entry points to create and manage infrastructure. Options in the package include a no-code user interface; low-code YAML-based CI/CD pipelines; direct IaC programming in preferred languages; and a REST API for full extensibility.

This flexibility enables teams with varied skill sets and workflows to adopt Pulumi IDP minus the friction of making a major tool change. Projects can be grouped into “services” — logical containers that include configurations, secrets, documentation, and observability tools. These services can represent anything from a microservice or Kubernetes cluster to a Jupyter notebook or serverless workflow, depending upon the use case.

**Advanced Operations and Security Controls**
Pulumi IDP isn’t limited to first-time provisioning—it also streamlines ongoing operations. Day-two capabilities include drift detection and remediation, policy auditing and enforcement, component lifecycle management, and change control with approval workflows. The latter has proven to be a huge time-saver, Duffy said.

Another feature is the new visual importer, which allows teams to bring previously unmanaged infrastructure under Pulumi’s governance with minimal effort. This functionality simplifies onboarding and accelerates cloud rationalization projects.

The platform also introduces an advanced identity and access management (IAM) system with fine-grained role-based access control (RBAC), custom permissions, and integration with enterprise identity systems via SAML/SSO. These security enhancements further extend Pulumi’s reputation for enterprise-ready infrastructure automation.

**SaaS and Self-Hosted Flexibility**
Pulumi IDP is available in two deployment models: a managed SaaS platform for most users and a self-hosted version for organizations with strict compliance or data residency requirements. The IDP integrates seamlessly with Pulumi’s existing enterprise ecosystem, including [Pulumi Copilot](https://www.pulumi.com/product/copilot), an AI-powered infrastructure management tool; [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments) for workflow automation; [Pulumi CrossGuard](https://www.pulumi.com/crossguard/), policy-as-code for compliance; and [Unified REST API](https://www.pulumi.com/docs/pulumi-cloud/reference/cloud-rest-api/) for standardized integration across the stack.

**Availability and Roadmap**
Pulumi IDP enters public preview today and is available at no cost for existing Pulumi customers and community users. General availability, along with enterprise licensing and support plans, is scheduled for later this year.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)