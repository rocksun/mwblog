# Platform Engineering: Overcoming Data Management Challenges
![Featued image for: Platform Engineering: Overcoming Data Management Challenges](https://cdn.thenewstack.io/media/2024/10/335c14c1-platform-engineering-data-management-1024x576.jpg)
Platform engineering is transforming how organizations develop and deploy applications, enabling developers to focus on solving business problems rather than managing complex cloud infrastructure.

By building [internal developer platforms (IDPs)](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/), businesses can accelerate innovation, increase revenue and improve customer retention, all while reducing cognitive load on developers.

[Gartner](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) predicts that 80% of large software engineering organizations will establish platform engineering teams by 2026. This is up from 45% in 2022.
## What Is Platform Engineering?
[Platform engineering](https://thenewstack.io/whats-platform-engineering-and-how-does-it-support-devops/) is the discipline of designing and building internal developer platforms, tool chains and workflows that enable self-service capabilities for software engineering organizations. The key goal of platform engineering is to move away from “ticket ops” — the practice where developers request infrastructure through tickets — and shift toward self-service platforms where developers can manage their infrastructure needs independently. This allows them to focus on creating value through application development.
Golden paths, or predefined templates for workflows, play a critical role in platform engineering. These pathways accelerate development by providing developers with preconfigured tools for tasks like CI/CD pipelines or new project setups. For example, [Bechtle](https://thenewstack.io/platform-engineering-reshapes-software-dev-at-bechtle/) implemented a standardized platform that dramatically reduced the time their developers spent managing infrastructure, allowing them to focus on software development and customer needs.

## Kubernetes and Platform Engineering
The rise of [Kubernetes](https://roadmap.sh/kubernetes) (K8s) has been instrumental in driving platform engineering adoption. Kubernetes and the broader cloud native landscape provide organizations with standardized tools to simplify the process of building IDPs.

Portworx’s most recent survey, “[The Voice of Kubernetes Experts Report](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand),” revealed that 80% of the organizations surveyed plan to build most of their new applications on cloud native platforms over the next five years, and 86% intend to build their cloud native platforms in hybrid cloud environments

With Kubernetes, platform engineers can automate many processes, providing self-service capabilities to development teams while maintaining consistency across environments.

The key benefits of using Kubernetes in platform engineering include:

**Consistency:**Kubernetes enables platform teams to adopt community-supported tools that provide consistent workflows across various infrastructure environments. Organizations can standardize the management of secrets, CI/CD pipelines and Day 2 operations such as[monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/).**Self-service access:**Tools like Backstage, Crossplane and Helm allow platform engineers to offer self-service capabilities, which empower developers to provision infrastructure resources without waiting for operations teams. This self-service model has been successfully implemented by companies like Bechtle, which used platform engineering to reduce developers’ dependency on operations teams for provisioning infrastructure.**Avoiding cloud lock-in:**By leveraging Kubernetes, platform engineers can create automation workflows that work across cloud providers, avoiding vendor lock-in. This helps ensure that applications are portable across any cloud or on-premises infrastructure stack.
## CSIs Create Platform Engineering Challenges
However, while Kubernetes addresses many challenges, it doesn’t completely solve the issue of consistency across cloud environments. For example, tools like Crossplane and Terraform help automate Kubernetes cluster provisioning, but cloud-specific [container storage interface (CSI)](https://github.com/container-storage-interface/spec/blob/master/spec.md) plugins often create storage and data management inconsistencies, such as:

**Lack of consistent storage features:**Different cloud providers offer varying storage services through their CSI plugins. For example,[AWS](https://aws.amazon.com/?utm_content=inline+mention)’s Elastic Block Storage CSI plugin requires extra steps to enable RWX (read-write-many) volumes, while[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)provides RWX volumes by default in Azure Kubernetes Service. These differences force platform engineers to develop custom scripts to ensure consistent storage features across cloud environments.**Replication and high availability:**Cloud providers implement replication and high availability in different ways, making it difficult to maintain consistency across development, testing and production environments. This can result in production issues that developers must address, often increasing complexity in the application code.**Day 2 operations:**Day 2 operations, such as data protection and disaster recovery, differ across cloud platforms, requiring platform teams to create additional customization. This contradicts the goal of platform engineering to reduce the cognitive load on developers and operations teams.
## Accelerate Developers With a Kubernetes Data Platform
Instead of individual CSI plugins for each storage array or cloud, a unified [Kubernetes data platform](https://thenewstack.io/managing-data-on-kubernetes-dok-solving-the-underlying-challenges/) can accelerate developers’ efforts to get features from development to production faster. It also provides application and data agility for your K8s workloads so you can migrate applications from on premises to the cloud, or vice-versa.

A Kubernetes data platform helps you address CSI-related challenges and simplify your environment by providing a consistent, cloud native storage layer across Kubernetes environments. It abstracts away discrepancies between cloud providers and CSI plugins, enabling developers and platform engineers to work with a unified platform without compromising on features.

**Consistent storage experience:**A K8s data platform allows platform teams to deliver a uniform storage experience across Kubernetes clusters, whether they are running on AWS, Azure or[Google](https://cloud.google.com/?utm_content=inline+mention)Cloud Platform (GCP). Developers can provision storage volumes (ReadWriteOnce [RWO] or RWX) without worrying about cloud-specific differences.**Resilience and reliability:**A K8s data platform provides in-cluster replication and disaster recovery across clusters and regions for high availability. This allows developers to focus on building applications rather than worrying about infrastructure failures.**New golden paths:**A K8s data platform enables platform engineers and DevOps teams to create new golden paths that simplify application testing and deployment. Developers can test applications in disaster recovery setups and validate that production environments will perform as expected. Also, integration with CI/CD tools like Flux and Argo CD enables full automation.**Database as a Service (DBaaS):**On a K8s data platform, platform engineers and DevOps teams can offer databases as a service across Kubernetes distributions. This can eliminate the need to manage multiple operators for different databases, enabling a unified[database management](https://thenewstack.io/databases-on-kubernetes-why-when-and-what-to-consider)experience.**Application migration:**When developers can migrate applications across regions and clouds seamlessly, platform teams can manage cross-region or cross-cloud migrations without introducing complexity for developers.
A Kubernetes data platform is a critical component of any [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/). This enables platform teams to package and automate [storage and database](https://thenewstack.io/bring-storage-and-databases-under-kubernetes-control) provisioning so that developers have self-service access to these capabilities.

**Case Study**
Ford Motor Company is a leader in the highly competitive auto manufacturing industry. With competition from all over the globe and the emergence of new startup electric vehicle (EV) manufacturers, Ford needed to accelerate its innovation cycles while maintaining strict quality standards.

Containers and Kubernetes were a key part of their digital transformation strategy. However, managing persistent storage became a burden on the developers, slowing their productivity and making it harder to meet the increasing demand for faster innovation. Additionally, Ford’s investment in Kubernetes made it essential to find a storage solution that could ensure business continuity and offer robust disaster recovery.

Ford was able to [overcome these challenges](https://portworx.com/customers/ford-motor-company/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) without increasing the operational complexity for its IT teams by implementing a Kubernetes data platform, gaining key benefits such as:

- High-performance persistent storage for Kubernetes applications.
- Seamless disaster recovery and business continuity for critical applications.
- A simplified self-service approach that freed developers from complex storage management.
- Faster service delivery and improved operational efficiency.
With Portworx as a key component of its application development stack, Ford saw transformative results in its IT infrastructure and developer productivity. Key improvements included:

- Modernized infrastructure with automated, self-service storage that empowered developers.
- Reduced complexity, enabling developers to focus on value creation and innovation.
- Increased developer productivity, accelerating time to market for new services and applications.
- Streamlined multicloud data mobility, ensuring seamless operations across different environments.
Satish Puranam, technical lead and manager of cloud at Ford, said, “At the end of the day, what we are talking about is enablement of developers and velocity of delivering services at a particular price point and at a particular quality… There’s hardly anything we can do in Kubernetes without having persistent storage.”

By addressing the storage management burden, Ford was able to maintain its high standards of quality while empowering its developers to innovate faster and with greater efficiency.

**Summary**
Platform engineering is transforming application development by enabling self-service capabilities and simplifying infrastructure management. However, persistent data management challenges continue to hinder the creation of fully consistent, scalable and secure platforms. Traditional storage vendor CSI plugins often face performance and scalability limitations, tying data and applications to specific storage infrastructures. Cloud providers further complicate this with data lock-in through proprietary CSIs and costly data egress fees.

Portworx overcomes these hurdles by offering consistent Kubernetes storage, high availability and seamless application migration across environments, empowering developers to focus on innovation and build secure, scalable applications in any cloud.

As organizations like Ford and Bechtle have shown, embracing platform engineering is essential for improving developer productivity and reducing the time spent managing infrastructure. This ensures that developers can “build once, port anywhere and run everywhere,” without compromising on performance or scalability across clouds.

Join our next [hands-on lab](https://portworx.com/hands-on-labs/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) to see how Portworx can enhance your internal development platform and accelerate your software development and generative AI projects.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)