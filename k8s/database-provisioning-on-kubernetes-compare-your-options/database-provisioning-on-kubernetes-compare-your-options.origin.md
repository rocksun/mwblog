# Database Provisioning on Kubernetes: Compare Your Options
![Featued image for: Database Provisioning on Kubernetes: Compare Your Options](https://cdn.thenewstack.io/media/2024/10/1d0e2132-database-kubernetes-provisioning-options-1024x576.jpg)
The rise of Kubernetes as a standard for orchestrating containerized workloads has revolutionized how [databases](https://thenewstack.io/databases/) are managed. As businesses increasingly embrace cloud native architectures, [Kubernetes](https://thenewstack.io/kubernetes/) has become central to modernizing IT infrastructure.

This shift is not limited to stateless applications. The [Cloud Native Computing Foundation (CNCF) Annual Survey 2022](https://www.cncf.io/reports/cncf-annual-survey-2022/) found that 71% of all organizations ran databases and caches in Kubernetes, representing a 48% year-on-year increase. In fact, the adoption of [databases on Kubernetes](https://github.com/cncf/tag-storage/blob/master/data-on-kubernetes-whitepaper/data-on-kubernetes-whitepaper-databases.md) is growing at an unprecedented rate, driven by the desire for scalability and flexibility and the need to optimize resource usage across cloud and on-premises environments.

![Kubernetes growth areas: open source projects rank among the most frequently used solutions. Source: CNCF](https://cdn.thenewstack.io/media/2024/10/ae140d02-kubernetes-growth-areas-1024x480.png)
Kubernetes growth areas (Source: [CNCF)](https://www.cncf.io/reports/cncf-annual-survey-2022/#findings)

The motivation behind this shift is clear: Kubernetes offers a level of flexibility, scalability and resource efficiency that traditional database management methods simply can’t match. With its powerful orchestration capabilities, Kubernetes can automate tasks such as scaling, failover and recovery, making it an attractive platform for database management, especially in cloud native and hybrid environments.

However, as more organizations look to [adopt Kubernetes](https://roadmap.sh/kubernetes) for managing databases, they [face challenges](https://thenewstack.io/kubernetes-for-databases-weighing-the-pros-and-cons/) related to operational complexity, manual intervention and database-specific tuning. This is where database provisioning options on Kubernetes come into play, each with its own set of pros and cons. The [2022 Data on Kubernetes Report](https://dok.community/wp-content/uploads/2022/10/DoK_Report_2022.pdf) highlights that the biggest change for respondents is the difficulties in database provisioning.

![Automating app provisioning and config management is the largest challenge of managing data workloads on K8s](https://cdn.thenewstack.io/media/2024/10/ce86c5a8-challenges-managing-data-workloads-k8s.png)
(Source: [DoK report 2022)](https://dok.community/wp-content/uploads/2022/10/DoK_Report_2022.pdf)

## Kubernetes Database Provisioning Options
Several solutions exist for provisioning and managing cloud native databases on Kubernetes. From manual deployment methods to advanced automation tools, organizations have a variety of choices, each suited to different needs and technical requirements. Below are the most prominent options for provisioning database resources on Kubernetes:

- Manual deployment
- Helm charts
- Kubernetes Operators
- Cloud native database platforms
## Manual Deployment
Manual deployment involves directly provisioning a database on Kubernetes by configuring Kubernetes resources such as `PersistentVolumeClaims`
, `StatefulSets`
, `Services`
and `ConfigMaps`
. This method gives administrators full control over the database configuration, but it also comes with significant overhead.

**Benefits:**
**Full control over deployment**: Administrators can customize every aspect of the database setup, from storage provisioning to network configuration.**Flexibility**: This approach allows teams to build highly tailored database configurations that meet specific needs, particularly in complex environments.
**Considerations:**
**Complexity**: Manually managing databases on Kubernetes requires extensive knowledge of both the database system and Kubernetes. Routine tasks such as scaling, backups and failover must be configured and executed manually.**Operational overhead**: Manual intervention leads to high operations costs.**Error-prone**: Given the manual nature of this approach, there is a higher likelihood of human error, which can impact new database availability and performance.
## Helm Charts
[Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) is a package manager for Kubernetes that simplifies the deployment of applications by bundling Kubernetes resources into a reusable chart. Several Helm charts exist for popular databases such as [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/), [PostgreSQL](https://roadmap.sh/postgresql-dba) and [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), making it easier to deploy these on Kubernetes.
**Benefits:**
**Quick setup**: Helm charts simplify the deployment process by providing preconfigured templates for common databases, reducing the time needed to set up and configure a database.**Reusable**: Helm charts are reusable across environments, making them a popular choice for DevOps teams that want consistency across development, staging and production environments.**Community support**: Many open source Helm charts are maintained by the community, providing frequent updates and bug fixes.
**Considerations:**
**Limited customization**: Helm charts offer less flexibility compared to manual deployment. Customizing a Helm chart often requires modifying the underlying templates, which can be time-consuming.**No built-in automation**: Helm charts are a step above manual deployment, but they don’t include advanced automation features like scaling, failover or backup management. These tasks must be managed separately.
## Kubernetes Operators
[Kubernetes Operators](https://thenewstack.io/kubernetes-when-to-use-and-when-to-avoid-the-operator-pattern/), the most commonly used method for automating database provisioning, leverage Kubernetes’ native API to manage the life cycle of a specific database technology. An Operator encapsulates the operational knowledge required to manage databases, such as provisioning, scaling, failover, backups and upgrades, into a custom controller. Each Operator is database-specific, which means that an Operator designed for MySQL will only work with MySQL databases.
Operators from [Percona](https://www.percona.com/?utm_content=inline+mention), [Bitpoke](https://www.bitpoke.io/), [Oracle](https://developer.oracle.com/?utm_content=inline+mention) and other vendors are commonly used for automating the management of MySQL, PostgreSQL and MongoDB.

**Benefits:**
**Database-specific automation**: Operators automate database provisioning, scaling and failover processes based on the unique needs of each database.**Granular control**: Operators provide more control for fine-tuning and automating database operations.**Deep integration**: Operators integrate directly with Kubernetes, leveraging its native features like`StatefulSets`
,`PersistentVolumes`
and`ConfigMaps`
to ensure high availability and persistence.
**Considerations:**
**Database-specific**: Most Operators are tied to a specific database technology, meaning that organizations managing multiple database types need to deploy and manage multiple Operators, leading to increased complexity.**Manual effort for complex environments**: While operators automate many tasks, some actions, such as scaling and failover, often require manual intervention for multi-cluster, multi-region, and data center environments.**Command-line driven**: Most Operators are managed through the command line, which can be a steep learning curve for teams without deep Kubernetes expertise.
## Cloud Native Database Platform
As Kubernetes Operators gained traction for automating database provisioning, they introduced significant automation but also came with a steep learning curve and required considerable manual effort for scaling, failover and system integration. For organizations seeking an alternative, there is a new open source cloud native database platform designed to simplify database provisioning without the complexity.

This open source alternative to public database as a service (DBaaS), [Percona Everest](https://www.percona.com/software/percona-everest), aims to simplify database management for MySQL, PostgreSQL and MongoDB across both cloud and on-premises environments. By addressing the limitations of traditional Kubernetes Operators, it introduces a centralized management interface, enhanced automation and support for multiple databases under one solution.

**Benefits:**
**Unified platform:**Manage MySQL, PostgreSQL and MongoDB from one interface, drastically reducing the operational burden of handling multiple databases across various clusters.**Comprehensive automation:**Automate key functions like scaling, failover, backups and recovery, minimizing manual intervention and boosting efficiency when provisioning the database.**Multicloud and hybrid support:**Support hybrid and multicloud environments, enabling consistent database management across on-premises and cloud platforms.**Self-service capabilities:**Internal teams can use a web-based interface to self-provision and manage databases, speeding up deployments and reducing operational bottlenecks.
**Considerations:**
**Customization limitations:**The platform offers extensive automation and centralized control, but it may not have as much customization as individual Kubernetes Operators, especially when integrating with third-party monitoring or security tools.
## Comparing Database Provisioning Options on Kubernetes
This chart summarizes the pros and cons of the options described above.

Database Provisioning Feature |
Manual Deployment |
Helm Charts |
Kubernetes Operators |
Database Platform |
Ease of Use |
High complexity | Medium (template-based) | Medium (CLI-driven) | Low (UI-driven, minimal manual effort) |
Automation |
None | Limited (no scaling/failover/backups) | High (database-specific automation) | Extensive (multi-database automation) |
Customization |
Full control | Limited | High (customizable per database) | Moderate (simplified for ease of use) |
Multi-Database Support |
N/A | N/A | No | Yes |
Scaling & Failover |
Manual | Manual | Semi-automated | Fully automated |
Third-Party Integration |
Full control | Limited | High (for single database) | Moderate |
User Interface (UI) |
None | None | None (CLI-driven) | Web-based |
Learning Curve |
Steep | Moderate | High (requires database-specific knowledge) | Low (user-friendly UI/API) |
**Automate the Database Deployment Process**
For organizations focused on a single database technology or teams needing extensive customization, Kubernetes Operators still offer unmatched flexibility. However, if you’re managing multiple databases, need to reduce the operational burden, or want a UI-based, self-service approach, [Percona Everest](https://www.percona.com/software/percona-everest) represents a step forward in Kubernetes-based database automation.

Whether you’re managing a single or multiple databases across cloud and on-premises environments, you can automate and streamline database management on Kubernetes with open source solutions, avoiding vendor lock-in.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)