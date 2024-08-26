# 5 Hacks Learned by Writing Thousands of Lines of IaC
![Featued image for: 5 Hacks Learned by Writing Thousands of Lines of IaC](https://cdn.thenewstack.io/media/2024/08/41ad8116-iac-hacks-of-kindness-1024x576.jpg)
Over many decades of provisioning infrastructure and cloud resources, we’ve learned that doing so manually can be tedious and error-prone. This was the impetus for the evolution from automation tools like [Chef](https://www.chef.io?utm_content=inline+mention), [Puppet](https://puppet.com/?utm_content=inline+mention) and Ansible to [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/) frameworks like CloudFormation, [Terraform](https://roadmap.sh/terraform) and [Pulumi](https://www.pulumi.com?utm_content=inline+mention).

IaC has been the backbone to delivering best practices and guardrails that enable engineering teams to manage modern, complex infrastructure similar to how they manage software. This approach incorporates familiar practices like version control, peer review, [CI/CD](https://thenewstack.io/ci-cd/) tooling, security vulnerability scanning, immutability and cost projection into infrastructure management.

IaC introduced employing a single template with variables to deploy environments consistently, reducing errors and simplifying operations. This is particularly useful in [disaster recovery scenarios](https://thenewstack.io/disaster-recovery-is-different-for-the-cloud/), enabling quick redeployment and recovery from issues, with everything versioned and managed consistently.

Over nearly a decade of managing infrastructure, from writing scripts through the emergence of IaC, I’ve learned many lessons that changed how I think about and manage infrastructure at scale. These guiding practices support managing your IaC at modern cloud-fleet scale to provide engineering efficiency and security.

Here are five hacks I’ve picked up from writing thousands of lines of IaC code:

## 1. Use the DRY Pattern
The DRY (“don’t repeat yourself”) pattern has become very popular in software engineering for automating code quality through [integrated developer environments (IDEs)](https://thenewstack.io/are-cloud-based-ides-the-future-of-software-engineering/) and linters. These enforce code policies and formatting through boilerplates, templates and more. Adopting this pattern for IaC helps avoid repeating code by modularizing components, which significantly improves maintainability.

As infrastructure scales, managing a large codebase with repeating components becomes cumbersome and error-prone. By using modules, the infrastructure codebase remains clean, organized and efficient, much like application codebases. Changes to infrastructure configurations are more straightforward, as modifications to a module are automatically reflected wherever the module is used. This leads to more efficient development cycles, faster deployment times and a lower risk of introducing errors during updates.

For instance, a virtual private cloud (VPC) module can be reused across projects, preventing each team member from creating separate VPCs. Terraform modules facilitate this, streamlining the management of shared components like VPCs, AWS EC2 instances and their associated resources.

DRY also promotes better version control and peer review in IaC. Each module can be versioned independently, allowing precise tracking of changes and easier rollback if issues arise. Peer review processes are enhanced as team members can focus on specific modules, ensuring higher quality and adherence to best practices. This modular approach also facilitates collaboration, as developers can work on different modules simultaneously without interfering with each other’s work.

## 2. Use the Registry
A common feature across IaC tools is the registry that comes with them. These registries are central component repositories, where you can find, share and publish modules and packages the community can leverage.

These include everything from the most common modules for cloud providers like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud, to custom modules and tooling-specific components. Nearly all modern IaC platforms, including Terraform, Pulumi, CloudFormation and even [Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) in the [Kubernetes](https://thenewstack.io/kubernetes/) ecosystem, provide dedicated registries that work seamlessly with their platform.

For example, the Terraform Registry’s vast collection of prebuilt modules can accelerate the development process. These modules encapsulate reusable infrastructure components, from simple configurations like setting up a VPC to complex deployments involving multiple interconnected resources. These modules have been tested and validated by other users, providing a reliable foundation for building infrastructure without starting from scratch.

By using prebuilt modules, teams can quickly implement infrastructure components that adhere to best practices and are optimized for performance and security. This not only reduces the time and effort required to deploy infrastructure but also helps ensure consistency across different environments.

However, it is crucial to scan all public modules for vulnerabilities and misconfigurations before use to prevent introducing security issues if the modules contain malicious code or unintended misconfigurations. For instance, a module that creates i[dentity and access management (IAM)](https://thenewstack.io/getting-started-with-identity-and-access-management/) roles could inadvertently grant excessive permissions, leading to unauthorized access.

Therefore, it is essential to conduct thorough security reviews and vulnerability scans of any modules sourced from the IaC registry to mitigate these risks.

## 3. Maintain Consistency
Maintaining consistency is crucial for managing large-scale infrastructure effectively. Consistent naming conventions and practices not only make the codebase easier to understand and maintain but also facilitate collaboration among team members. This is because as infrastructure grows, maintaining clarity and organization in the codebase becomes increasingly important.

Standardizing naming conventions for resources, modules and variables helps team members understand the purpose and scope of each component, facilitating easier maintenance and collaboration. This consistency reduces confusion and errors, making it easier for new team members to get up to speed and for existing members to manage and update the infrastructure.

Using consistent naming conventions also enables defining better processes and practices to track changes and the IaC codebase’s evolution. Enforcing a naming convention makes it easier to, for example, document the system and its changes, automate linters and validators, conduct [effective code reviews](https://thenewstack.io/how-good-is-your-code-review-process/), modularize, and maintain consistent directory structures and resource tagging.

Implementing naming conventions and good practices helps teams maintain a clean, organized and understandable infrastructure codebase. This consistency enhances collaboration, reduces errors and makes the infrastructure more scalable and easier to manage as it grows.

## 4. Manage State Files Properly
When the open source [Terraform fork OpenTofu ](https://thenewstack.io/new-opentofu-release-challenges-terraforms-dominance/)decided to include [state file encryption,](https://opentofu.org/docs/language/state/encryption/) it drew attention to this longstanding feature request from the Terraform community (with code contributions as far back as 2016).

Managing Terraform state files properly is a critical aspect of IaC best practices. The state file represents the current state of the infrastructure and is essential for tracking and applying changes. Proper management ensures consistency, prevents data corruption and supports collaborative workflows.

The importance of managing state files cannot be overstated. Centralized state management allows multiple developers to work on the same infrastructure without conflicts, and proper state management supports collaboration by providing a shared, up-to-date view of the infrastructure.

Using methods that ensure the state file is consistent and not corrupted can prevent issues arising from concurrent modifications, manual edits and data corruption, thereby maintaining the infrastructure’s integrity. Proper state management includes regular backups and versioning, enabling quick recovery in case of accidental deletions, corruption or other disasters, and minimizing downtime and data loss.

**5 Good Practices for Managing IaC State**
While the specific implementation details and tools for state management vary across IaC platforms, the following underlying principles of maintaining a consistent, reliable and up-to-date Terraform or OpenTofu infrastructure state are universally important. This ensures the infrastructure remains robust, scalable and aligned with the defined configurations.

**Use remote state storage**: Instead of storing the state file locally, use remote storage solutions such as AWS S3, Google Cloud Storage or Azure Blob Storage. Remote storage centralizes the state file, making it accessible to all team members and CI/CD pipelines. This approach ensures everyone works with the same state, preventing conflicts and inconsistencies.**Implement locking mechanisms**: To prevent concurrent modifications, use a locking mechanism. For instance, AWS DynamoDB can lock the state file during updates. Locking ensures that only one process can modify the state at a time, preventing race conditions and data corruption.**Avoid manual edits**: Although the state file is human-readable, manual edits can lead to corruption. Always use Terraform commands to make any changes to the state file. This practice maintains the file’s integrity and ensures changes are applied correctly.**Regular backups and versioning**: Regularly back up the state file to prevent data loss. Enable versioning on the storage bucket to automatically keep previous versions of the state file. This allows easy recovery in case of accidental deletions or corruption.**Secure state files**: Ensure the state file is encrypted and access is restricted to authorized users and services. Encrypting the state file protects sensitive information, such as access keys and credentials, from unauthorized access. Implement strict access controls to limit who can read and modify the state file.
By following these high-level best practices, organizations can manage Terraform state files effectively, ensuring the consistency, security and availability of their infrastructure. Proper state management supports robust and scalable infrastructure deployments, facilitates collaboration and enhances overall infrastructure integrity.

## 5. Leverage Data Sources
Leveraging data sources is a powerful strategy in IaC management. Data sources allow IaC configurations to dynamically query and retrieve information from cloud providers and APIs, which enhances the infrastructure’s flexibility, adaptability and maintainability. This approach minimizes hardcoding values, such as Amazon Machine Image (AMI) IDs or network configurations; ensuring that the infrastructure always uses the most current and accurate data leads to fewer errors and simplifies updates — making the codebase more efficient to manage.

Whether you’re using Terraform, Pulumi, AWS CloudFormation or Azure Resource Manager, incorporating data sources helps create more dynamic and reusable configurations. You can adapt these configurations to various environments without modifications, maintaining consistency and promoting best practices. For example, querying for the latest virtual machine (VM) images or network IDs keeps configurations current with minimal manual intervention, supporting development and production environments seamlessly.

Additionally, using data sources helps mitigate [infrastructure drift](https://thenewstack.io/how-drift-detection-and-iac-help-maintain-a-secure-infrastructure/), a common challenge in IaC. Drift occurs when the actual state of the infrastructure diverges from the state defined in the IaC configuration, leading to inconsistencies and potential security risks.

Regular drift detection through tools and integrated checks in CI/CD pipelines helps promptly identify and rectify any changes to maintain the infrastructure’s integrity and reliability. This universal approach to IaC management through data sources helps ensure deployment consistency and security across platforms and tools.

## Don’t Reinvent the Wheel: A Decade of IaC Lessons
IaC management has transformed cloud operations at scale. The journey from manual provisioning to leveraging advanced IaC tools like Terraform, Pulumi and CloudFormation has shifted how modern infrastructure is managed. Experience in managing IaC at scale shows that adopting best practices such as following the DRY pattern, using registries, maintaining consistency, managing state files properly and leveraging data sources helps engineering teams achieve greater efficiency, security and scalability.

These practices enable engineering teams to effectively manage complex infrastructures, streamline operations and enhance the overall robustness of their deployments. These lessons learned from writing thousands of lines of IaC provide a foundation for building resilient, scalable and secure cloud environments. Ultimately they enable organizations to operate more efficiently, respond more swiftly to changes, incidents and downtime, and recover critical digital services more rapidly.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)