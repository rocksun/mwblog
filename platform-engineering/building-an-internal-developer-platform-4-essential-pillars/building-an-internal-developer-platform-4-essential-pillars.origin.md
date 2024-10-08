# Building an Internal Developer Platform: 4 Essential Pillars
![Featued image for: Building an Internal Developer Platform: 4 Essential Pillars](https://cdn.thenewstack.io/media/2024/10/887ec546-idp-4-pillars-1024x576.jpg)
As organizations increasingly adopt cloud native architectures, Kubernetes and modern DevOps practices, platform engineering teams are emerging as a critical function to empower developers. One of the primary responsibilities of these teams is to build [internal developer platforms (IDPs)](https://thenewstack.io/platform-engineering/) that streamline infrastructure management, governance and developer experience.

An IDP provides the abstraction and tooling needed to manage cloud infrastructure, application deployments and security requirements. It offers developers an efficient, self-service way to deliver their code to production.

Together, the four essential pillars for building a successful [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) — Infrastructure as Code, Policy as Code, GitOps and developer portals — simplify operations for platform teams and enable developers to move faster and more securely.

## 1. Infrastructure as Code
[Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) (IaC) is the backbone of any modern cloud native platform. It allows platform engineering teams to manage and provision infrastructure (such as compute, storage and networking resources) programmatically using code. IaC ensures that infrastructure definitions are version-controlled, reusable and consistent across different environments.
Some key benefits of IaC in an internal developer platform include:

**Automation and scalability:**Infrastructure can be automatically scaled or modified based on code changes. Tools like[Terraform](https://roadmap.sh/terraform),[AWS](https://aws.amazon.com/?utm_content=inline+mention)CloudFormation and[Pulumi](https://www.pulumi.com?utm_content=inline+mention)are popular for defining infrastructure as code.**Consistency:**By defining infrastructure declaratively, environments are consistently configured, preventing configuration drift and manual errors.**Version control:**Infrastructure changes can be tracked and audited, making rollback and disaster recovery straightforward in case of misconfigurations.
For example, using Terraform to define infrastructure templates for a multi-region Kubernetes deployment allows teams to create environments consistently across different cloud providers.

Without IaC, manual processes for infrastructure management can become error-prone, slow and difficult to scale as demand grows. IaC is the foundation for making the IDP reliable, predictable and scalable.

## 2. Policy as Code
Security, governance and compliance are integral to managing modern infrastructure, but manual policy enforcement doesn’t scale well and can create bottlenecks. [Policy as Code](https://nirmata.com/2024/06/24/top-10-reasons-why-policy-as-code/) (PaC) helps solve this challenge by programmatically defining governance, security and operational policies. These policies are automatically enforced across cloud environments, Kubernetes clusters and CI/CD pipelines. Essentially, they “shift down security” into the platform.

Critical advantages of PaC in an IDP include:

**Automated compliance:**Policies can be written to enforce security controls, such as preventing deployments with insecure configurations or blocking access to unapproved services. Tools like[Nirmata Kyverno](https://nirmata.com/kyverno-oss/),[Open Policy Agent](https://thenewstack.io/5-things-you-didnt-know-about-open-policy-agent/)(OPA) and[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention)Sentinel allow teams to define and enforce these policies.**Scalability:**By automating policy enforcement, you reduce the risk of misconfigurations, security breaches and noncompliance issues, even as your infrastructure scales.**Visibility and auditing:**PaC provides a clear, auditable record of policy decisions and changes, which is crucial for meeting regulatory requirements.
For example, teams can generate default network security policies, quotas and limits in Kubernetes using an admission controller like Kyverno whenever a new namespace is created.

Without PaC, enforcing security and compliance policies becomes a manual, error-prone process that slows development. PaC makes security and governance part of the automated workflow, enabling speed without sacrificing safety.

## 3. GitOps
[GitOps](https://thenewstack.io/4-core-principles-of-gitops/) is an operational model where all system configurations, including application deployments, infrastructure and policies, are managed through Git repositories. By adopting GitOps, platform teams can standardize how changes are made and ensure that the actual system state matches the desired state defined in Git.
GitOps has key advantages in an IDP, including:

**Version control for everything:**Git is the source of truth for infrastructure, applications and policies. Every change is accompanied by a pull request, providing traceability, transparency and collaboration.**Automated deployments:**Using tools like[Argo CD](https://thenewstack.io/how-far-can-you-go-with-argo/)or[Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/), GitOps automatically applies changes from Git to the target environment, ensuring that production environments are always in sync with the defined configurations.**Security and governance:**GitOps ensures that changes can be made only through approved processes (pull requests), which can include code reviews, automated tests and policy checks. This adds a layer of security and governance to the deployment process.
For example, if you use Argo CD to manage Kubernetes cluster configurations, when pull requests are merged in the Git repository, all changes are automatically deployed. Therefore, no manual intervention is needed to update infrastructure.

GitOps provides a predictable, reliable and secure deployment model. It standardizes operations across environments, minimizes human errors and creates a collaborative, auditable workflow for platform engineering and development teams.

## 4. Developer Portals
A [developer portal](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/) is a self-service interface that allows developers to interact with the platform without understanding the underlying infrastructure or operational complexities. It is a one-stop hub for accessing resources, managing deployments and finding documentation and tools.

Key features of a good developer portal include:

**Self-service capabilities:**Developers can provision environments, deploy applications or request services on demand without depending on the platform team. This reduces bottlenecks and speeds the development process.**Prebuilt templates and blueprints:**Providing standard configurations and deployment templates helps ensure that developers follow best practices and policies so they can focus on building their applications.**Collaboration and documentation:**A developer portal can include documentation, onboarding materials and FAQs to help new team members quickly get up to speed, making it easier to maintain platform consistency.
For example, implementing [Backstage](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/) as a developer portal enables developers to view and manage their application deployments, access documentation and leverage preconfigured Kubernetes templates for deployment.

A developer portal enhances the developer experience by making infrastructure and operational tasks readily accessible. It reduces the cognitive load on developers while ensuring that they adhere to platform governance and standards.

## Conclusion
Building an internal developer platform is not just about creating tools; it’s about delivering a seamless experience that empowers developers while maintaining operational efficiency, security and compliance. The four foundational components, Infrastructure as Code, Policy as Code, GitOps and developer portals, are the building blocks that make this possible.

When integrated effectively, these core pillars enable platform engineering teams to deliver a robust, scalable and secure internal developer platform that drives innovation and efficiency for development teams. Whether you’re a growing startup or a large enterprise, implementing these components will set up your IDP for long-term success. By adopting these principles and tools, your platform engineering team can create a powerful and developer-friendly IDP, accelerating software delivery while ensuring governance, security and scalability.

To learn more about how to get started with building a development platform, attend this session at [KubeCon North America 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/program/schedule/):

**Creating Paved Paths for Platform Engineers: **Ritesh Patel, Nirmata; Abby Bangser, Syntasso; Viktor Farcic, Upbound; Nicholas Morey, [Akuity](https://akuity.io/?utm_content=inline+mention); and Praseeda Sathaye, Amazon**
**Wednesday, November 13, 2024, 5:25 p.m. – 6:00 p.m. MST
Salt Palace | Level 1 | Grand Ballroom BDF

*To learn more about Kubernetes and the cloud native ecosystem, join us at **KubeCon + CloudNativeCon North America**, in Salt Lake City, Utah, on Nov. 12-15, 2024.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)