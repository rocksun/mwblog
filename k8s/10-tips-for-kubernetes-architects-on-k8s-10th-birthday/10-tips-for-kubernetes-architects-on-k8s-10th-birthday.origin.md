# 10 Tips for Kubernetes Architects on K8s’ 10th Birthday
![Featued image for: 10 Tips for Kubernetes Architects on K8s’ 10th Birthday](https://cdn.thenewstack.io/media/2024/11/7098f5c6-kubecon-24-1024x683.png)
We caught up with [Taylor Dolezal](https://www.linkedin.com/in/onlydole/), head of ecosystem at the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), to discuss Kubernetes, as it is celebrating its [10th birthday this year](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/).

Dolezal has worked as a senior developer advocate for [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) and a site reliability engineer for Walt Disney Studios. He actually started his own IT career by founding his own software solutions company, called Pixelmachinist, that focused on businesses in the Cleveland area.

![Taylor Dolezal headshot.](https://cdn.thenewstack.io/media/2024/11/bff3b1cd-taylor-dolezal.jpg)
Taylor Dolezal (LinkedIn)

I caught up with Dolezal ahead of [KubeCon + CloudNativeCon North America 2024,](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america) which is taking place in Salt Lake City, Utah, Nov. 12-14. From its modest beginnings at the first Kubecon in San Francisco to a [sold-out event in 2018](https://thenewstack.io/digitalocean-opens-up-its-managed-kubernetes-service/) in Seattle, the event remains popular amongst platform maintainers, developers and architects.

From a monumental 1,937 submissions, attendees can choose from 218 sessions, keynotes, lightning talks, and breakout sessions, with 87 CNCF project maintainer-hosted sessions aimed at technologists across industries and skill sets. Attendees will also have access to over 40 CNCF Project Lightning Talks on Tuesday.

In this interview, Dolezal talks about Kubernetes and provides the top ten tips for architects to navigate the platform and the ecosystem. He talks about the success of the [Kubernetes community,](https://www.thenewstack.io/Kubernetes) which has managed to unify infrastructure, and how those “lessons learned” could be used to help developers and architects.

**Can you please introduce yourself and provide a brief background of your initial encounter with Kubernetes before we dive into the top 10?**
My journey with Kubernetes began in 2016 when I worked at The Walt Disney Studios. We were amid a significant cloud migration, and Kubernetes emerged as a promising solution for managing our growing containerized workloads.

At the time, Kubernetes was still in its early stages, and adopting it felt like stepping into uncharted territory. We faced numerous challenges, from understanding the core concepts to figuring out how to integrate cloud native principles into our existing systems. This hands-on experience of implementing Kubernetes in a large enterprise environment was invaluable. It deepened my technical understanding and gave me insights into the organizational and cultural shifts required for successful adoption.

As I became more involved in the Kubernetes community, contributing to various projects and participating in KubeCon events, I saw the immense potential of the broader cloud native ecosystem. My focus on community-led me to my current role at CNCF, where I work to foster collaboration between end users, vendors, and CNCF projects.

My background spans both the practical implementation side and the community-building aspect of Kubernetes. This dual perspective has been crucial in understanding the evolving needs of enterprises and how the ecosystem can adapt to meet those needs. It’s been fascinating to witness and contribute to the growth of Kubernetes from a promising technology to the standard for container orchestration.

**What key security considerations should Kubernetes architects focus on to ensure a secure and compliant cluster environment?**
Kubernetes security requires a comprehensive, proactive approach. Based on my experience with numerous organizations, several critical areas demand attention:

Identity and access management is fundamental. Organizations should implement fine-grained access controls beyond basic RBAC, potentially adopting a zero-trust model. The principle of least privilege should guide all access decisions.

Securing the application lifecycle is crucial. This security includes hardening CI/CD pipelines, implementing thorough image scanning and signing processes, and maintaining secure container registries. The goal is to ensure the integrity of every component in the environment, not just detect vulnerabilities.

Network security needs careful consideration. While Kubernetes network policies provide a foundation, many organizations adopt more advanced solutions for granular control over service-to-service communication and default encryption.

Data protection is essential for both at rest and in transit. This protection involves encryption and careful management of secrets and sensitive configuration data.

Continuous security monitoring and auditing are vital. Organizations should implement comprehensive logging and alerting systems, conduct regular security audits, and prepare for incident response.

Kubernetes security is an ongoing process, not a one-time setup. It requires treating infrastructure as code and incorporating security practices throughout the development lifecycle.

Community engagement plays a crucial role in Kubernetes security. [The Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)‘s research underscores how community-driven initiatives address security challenges. We collectively enhance the entire ecosystem’s security by contributing to projects, sharing experiences, and participating in community groups.

Successful organizations integrate security into their processes and focus on building resilient, self-healing environments that detect and respond to threats in real time rather than aiming for an ‘uncompromisable’ system.

**How can Kubernetes architects optimize resource utilization and reduce costs in large-scale deployments?**
Resource optimization in Kubernetes is an ongoing process that requires a strategic approach, especially in large-scale deployments. It’s about finding the right balance between performance, cost-efficiency, and scalability.

Leveraging Kubernetes native tools like the Horizontal Pod Autoscaler and Vertical Pod Autoscaler is a good starting point. These tools help dynamically adjust resources based on actual usage patterns. Implementing proper resource requests and limits for all containers is crucial to prevent contention and ensure fair allocation.

In cloud environments, utilizing node autoscaling can help match capacity with demand, optimizing costs. Consider using spot instances or preemptible VMs for noncritical workloads to reduce expenses further. Implementing pod disruption budgets ensures high availability during these scaling events.

Visibility is critical to optimization. Use tools like kube-state-metrics and [Prometheus](https://thenewstack.io/know-the-hidden-costs-of-diy-prometheus/) for detailed resource monitoring. Regular audits to clean up unused resources, such as orphaned volumes or unused load balancers, can lead to significant cost savings over time.

Adopting FinOps principles can help align financial and operational goals, providing a framework for ongoing optimization. Tools like [OpenCost](https://www.opencost.io/) offer valuable insights into Kubernetes spending, assisting teams to make informed decisions about resource allocation.

Remember, effective resource optimization is an iterative process. It requires ongoing monitoring, analysis, and adjustment to ensure your cloud native environment remains efficient and cost-effective as your applications and infrastructure evolve.

**What are the best practices for implementing and managing observability (logging, monitoring, and tracing) in a Kubernetes environment?**
Observability in Kubernetes environments is crucial for maintaining system health, performance, and security. Based on my experience working with various organizations, I recommend focusing on these key areas:

First, adopt a comprehensive approach that combines logging, monitoring, and tracing. Each of these components provides unique insights:

Logging captures detailed event data, which is crucial for debugging and audit trails. Implement a centralized logging strategy using a standard format across all applications and infrastructure components. This approach facilitates easier searching and analysis.

Monitoring tracks the health and performance of your systems. Focus on collecting infrastructure and application-specific metrics (like CPU and memory usage). Set up alerts based on these metrics to address issues proactively.

Distributed tracing helps understand the flow of requests across [microservices](https://www.thenewstack.io/microservices). This capability is instrumental in dealing with complex, distributed systems across large-scale environments.

Second, embrace the concept of “observability as code.” Define your observability configurations using declarative manifests and manage them alongside your application code. This practice ensures consistency and allows version control of your observability setup.

Third, consider the unique challenges of Kubernetes environments. The dynamic nature of container orchestration means traditional, static monitoring approaches often need to be revised. Implement solutions that automatically discover and monitor new services as they spin up.

Fourth, focus on meaningful, actionable metrics. It’s easy to get overwhelmed with data in complex systems. Work closely with development and operations teams to identify the most critical system health and performance indicators.

Lastly, cultivate an observability-minded culture. Encourage developers to instrument their code correctly and think about observability from the design phase. This proactive approach leads to more manageable and resilient systems in the long run.

Remember, effective observability is not collecting more data but gaining actionable insights. The goal is to quickly understand and resolve issues, predict potential problems, and continuously improve system performance and reliability.

**What tips can architects follow to ensure high availability (HA) and disaster recovery (DR) in Kubernetes clusters?**
Thinking beyond just your infrastructure is key regarding high availability and disaster recovery in Kubernetes. While robust cluster setup is important, true resilience comes from a holistic approach considering your applications, data, and team processes.

Failures often arise in unexpected ways. I’ve seen situations where a perfectly configured multicloud setup didn’t help because of an issue with a critical application component that wasn’t available. Looking at your entire stack is crucial, from the infrastructure to the application layer.

One often overlooked aspect is data. In a disaster scenario, having your applications up and running is only valid when your data is available or consistent, which can be challenging with stateful applications. Think about how your data moves and where it lives.

Another critical factor is your team’s readiness. I’ve found that regular disaster simulations are invaluable. They help you find gaps in your technical setup and your team’s response processes. It’s surprising how often these exercises reveal unforeseen issues your team can address in just a few sprints.

Automation is your friend in HA/DR scenarios, but it’s a double-edged sword. While it can speed up recovery, poorly implemented automation can also escalate problems. Balance is key.

Lastly, remember the human factor in your HA/DR strategy. Clear communication channels and well-defined roles can make a huge difference when responding to incidents. Confusion and a lack of clarity can cause enormous issues for your response teams as they try to get services or platforms back to a stable state.

**How can Kubernetes architects streamline continuous integration and continuous deployment (CI/CD) pipelines for better delivery efficiency?**
Streamlining CI/CD pipelines for Kubernetes deployments drives efficient, reliable software delivery. My experience with various organizations has revealed several highly effective strategies.

[GitOps principles](https://thenewstack.io/developers-want-pragmatic-gitops-and-better-cd-tools/) yield significant benefits in Kubernetes environments. Git repositories are the single source of truth for application code and infrastructure configurations, leading to consistent, auditable, and reproducible deployments. This approach aligns with Kubernetes’ declarative nature, simplifying rollbacks and environment parity.
Leveraging cloud native concepts enhances CI/CD efficiency. Namespaces for environment isolation, labels and annotations for resource management, and rolling update capabilities for zero-downtime deployments contribute to a streamlined Kubernetes-native workflow.

Infrastructure testing is often undervalued but critical. Validating Kubernetes manifests and policies pre-deployment catches potential issues early, saving significant time and resources. This practice complements traditional unit and integration tests, providing a more comprehensive quality assurance approach.

Progressive delivery techniques like canary deployments or feature flags enable controlled rollouts. These methods allow teams to closely monitor the impact of changes and quickly roll back if issues arise, reducing risk in production environments.

Automation extends beyond basic build and deploy processes. Integrating security scans, dependency updates, and compliance checks into the pipeline ensures consistency and frees teams to focus on higher-value activities.

Secrets management in Kubernetes requires careful consideration. Implementing secure, dynamic solutions for storing and rotating sensitive information like API keys and passwords is essential for maintaining a robust security posture.

Teams benefit when implementing observability for their CI/CD pipelines. Capturing comprehensive logs, monitoring, and tracing for pipelines helps provide crucial visibility, enabling quick identification and resolution of pipeline issues.

High-performing organizations treat their CI/CD pipeline as worthy of continuous refinement and investment. This mindset drives ongoing improvements in deployment speed, reliability, and security, keeping pace with evolving business needs and feature additions.

**What are some advanced networking considerations Kubernetes architects should keep in mind for scaling services across clusters?**
Networking in Kubernetes can get increasingly complex as organizations scale services across clusters. Multicluster service discovery presents significant challenges. A robust service mesh can provide a unified service discovery mechanism across clusters, enabling seamless communication and load balancing. This approach requires careful design to manage increased latency and potential points of failure.

Network policy enforcement across cluster boundaries demands sophisticated solutions. While Kubernetes network policies work well within a cluster, extending these policies across clusters often requires additional tooling or custom patterns. Addressing this challenge is crucial for maintaining consistent security postures across your entire infrastructure.

Edge routing and traffic management also grow in complexity with multicluster setups. Implementing intelligent edge routing to direct traffic to the most appropriate cluster based on factors like latency, load, or data residency requirements becomes essential, often involving integrating your Kubernetes networking with broader networking infrastructure and CDNs.

Performance optimization across geographically distributed clusters presents unique challenges. Techniques like topology-aware routing and smart client-side load balancing can significantly improve application performance by reducing intercluster traffic and latency.

DNS management across clusters requires careful consideration. Implementing a global DNS solution that is aware of your multicluster topology can significantly simplify service discovery and improve reliability. Implementing distributed tracing and centralized logging for network flows helps troubleshoot and optimize cross-cluster communication.

These considerations underscore the need for Kubernetes architects to think beyond single-cluster networking paradigms. Successful implementations often involve close collaboration with network engineering teams and a deep understanding of Kubernetes networking principles and broader enterprise networking concepts.

**How can Kubernetes architects effectively manage stateful applications and persistent storage in a Kubernetes ecosystem?**
One pattern I’ve seen emerge is the use of custom controllers for specific databases or stateful applications. These controllers can automate many of the complex operations that used to require manual intervention, like scaling, backups, and even some aspects of disaster recovery.

Persistent storage solutions have also come a long way. [The Container Storage Interface](https://thenewstack.io/how-the-container-storage-interface-csi-boosts-cloud-native-devops/) (CSI) has been a crucial development, allowing for a standardized way to integrate storage systems with Kubernetes. This has opened up a world of possibilities for organizations to use the storage solutions that best fit their needs, whether on-premises or in the cloud.

However, it’s important to note that managing stateful applications in Kubernetes is still a complex task. It requires careful planning and often specialized knowledge. I’ve seen teams succeed by treating their stateful services as first-class citizens in their Kubernetes strategy, investing time in understanding the specific requirements of each application, and designing their infrastructure accordingly.

The key lesson I’ve learned is that there’s no one-size-fits-all solution for stateful applications in Kubernetes. Success comes from a deep understanding of both your application’s needs and the capabilities of your chosen storage solutions. It’s about finding the right balance between leveraging Kubernetes’ orchestration power and respecting the unique characteristics of stateful workloads.

**What strategies should Kubernetes architects use for managing multiple clusters across different cloud providers or on-premise environments?**
Managing multiple Kubernetes clusters across diverse environments reminds me of my time at Disney Studios, where we faced the challenge of orchestrating workloads across over 350 applications. This experience taught me valuable lessons about the complexities of multicluster management.

The critical insight is that success lies not in treating each cluster as an isolated entity but in developing a unified strategy that acknowledges their unique characteristics. When managing clusters across different environments, standardization becomes crucial — not just in how you deploy workloads but in how you approach governance, security, and operations.

Through my work with CNCF’s end-user program, I’ve observed how organizations approach this challenge. The most successful ones start by establishing clear boundaries. They determine which workloads belong where based on factors like data sovereignty, latency requirements, and cost optimization.

One particularly effective pattern involves treating your multicluster strategy as a product. A clear roadmap, deep understanding of development and operations teams’ needs, and continuous iteration based on feedback create a platform that empowers teams to deploy and manage applications, regardless of their location.

Security and compliance in multicluster environments require special attention. Each cloud or on-premise environment has security considerations and compliance requirements. The challenge is maintaining consistent security policies while respecting these differences.

The most interesting developments I’ve seen come from organizations that embrace automation for deployment and their entire cluster lifecycle. They automate everything from initial cluster provisioning to ongoing maintenance and eventual decommissioning. This approach helps maintain consistency and reduces the operational burden of managing multiple clusters.

Multicluster management demands tight collaboration between platform, security, and application teams. Organizations excel when their technology choices align with operational capabilities and business objectives.

**How should Kubernetes architects address issues related to cluster lifecycle management and version upgrades?**
Cluster lifecycle management represents one of the more nuanced challenges in the Kubernetes ecosystem. Keeping current with Kubernetes releases and the complexity of enterprise environments demands thoughtful consideration of upgrade strategies.

Release cycles affect every layer of the stack — from core infrastructure to application workloads. Successful upgrade strategies account for this ripple effect. Development teams adapt their applications, operators learn new features and deprecations, and security teams evaluate changes to the security model.

[Kubernetes Enhancement Proposals](https://www.kubernetes.dev/resources/keps/) (KEPs) exemplify this structured approach to managing change. Each significant feature addition or modification in Kubernetes follows this process, providing architects with clear visibility into upcoming changes. KEPs detail the technical specifications, motivation, design constraints, and potential impacts across the ecosystem. This transparency allows architects to plan proactively for future upgrades and understand the reasoning behind specific changes.
Release planning requires balancing progress with stability. Skipping too many versions creates technical debt and security vulnerabilities while upgrading too frequently can overwhelm teams and introduce unnecessary risk. Understanding this dynamic helps architects design sustainable upgrade strategies.

Communication becomes a cornerstone of successful upgrades. Technical teams need migration paths, management needs risk assessments and timelines, and application teams need to understand potential impacts on their workloads. Clear communication channels and well-defined processes help orchestrate these complex changes.

Effective cluster lifecycle management transforms upgrades from dramatic events into routine operations. This transformation comes through testing environments, pragmatic automation, and a thorough understanding of environment-specific requirements and constraints.

**What are the top tips for maintaining a well-documented, consistent, and collaborative Kubernetes infrastructure?**
Documentation in Kubernetes demands more than just capturing technical specifications. Drawing from my experience working with SIG Docs, I’ve experienced successful documentation strategies evolving alongside the infrastructure they describe.

Working documentation lives close to the code. Architectural decisions, trade-offs, and future considerations provide teams with crucial context for maintaining and evolving their infrastructure. This practice helps teams understand both the current state and historical context.

Teams can underestimate the importance of standardization in documentation. A consistent structure for runbooks, architectural decision records, and operational procedures can speed up onboarding and reduce mental strain during incidents. This standardization is particularly beneficial when managing multiple clusters or working across cloud providers.

Infrastructure documentation should tell a story. Rather than isolated wiki pages or scattered READMEs, adequate documentation guides readers through the system’s evolution. When encountering an unfamiliar part of the infrastructure, teams should understand how it works, why it exists, and what problems it solves.

Cross-team collaboration thrives on shared understanding. Regular architecture reviews, incident retrospectives, and technical discussions generate valuable insights. Capturing these discussions and decisions helps teams build collective knowledge and avoid repeating past mistakes.

Feature flags, API versions, and deprecation policies need clear documentation trails. These elements directly impact application teams and require careful communication. By maintaining comprehensive records of these changes, architects help teams navigate transitions smoothly and plan effectively for future updates.

**Kubernetes roadmap. The CNCF landscape is extremely daunting. Cheat sheet for architects and developers for the next 1-2 years?**
The cloud native ecosystem’s strength lies in its organized approach to solving different technological needs. Rather than trying to understand every project, architects should focus on the categories that align with their specific challenges:

- App Definition and Development encompasses the tools and frameworks for building cloud native applications. This includes databases, streaming platforms, application definition, and continuous integration/delivery tools that form the backbone of modern application development.
- Observability and Analysis tools provide insights into system behavior, helping teams understand their applications in production. This category includes monitoring, logging, tracing, and chaos engineering tools that support reliable operations.
- Orchestration and Management focuses on scheduling, scaling, and maintaining containerized workloads. Beyond container orchestration, this includes service mesh, API gateways, and service discovery — critical components for managing distributed systems.
- Provisioning covers the tools needed to deploy and maintain cloud native infrastructure, including automation, security, key management, and image building. These tools help teams establish consistent, secure environments across different platforms.
- Runtime represents the foundation — container runtimes, storage, and networking components that make cloud native infrastructure possible. Understanding your runtime requirements helps inform decisions across all other categories.
The CNCF Technical Oversight Committee (TOC) and End User Technical Advisory Board (TAB) provide guidance through Technical Advisory Groups (TAGs) and User Groups, respectively. These communities offer direct access to expertise and real-world experience, helping teams navigate options within each category.

Each organization’s cloud native journey looks different. Understanding these landscape categories helps teams converse more about their needs and challenges. Engaging with relevant community groups can provide valuable insights and learning opportunities as you explore solutions that make sense for your context.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)