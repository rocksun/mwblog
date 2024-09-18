# Build Kubernetes Security on Intents, Not Rules
![Featued image for: Build Kubernetes Security on Intents, Not Rules](https://cdn.thenewstack.io/media/2024/09/3217aca5-intent-driven-kubernetes-security-1024x576.jpg)
As Kubernetes evolves and adoption grows, ensuring its security remains a top priority for businesses. As organizations scale their
[use of Kubernetes](https://www.accuknox.com/blog/kubernetes-security-best-practices), they face increasing challenges in securing their environments. According to [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)’s 2024 State of Kubernetes security report, [67% of respondents have delayed or slowed](https://www.redhat.com/en/blog/state-kubernetes-security-2024#:~:text=Security%20issues%20continue%20to%20impact,which%20some%20organizations%20still%20struggle.) down application development due to Kubernetes security concerns.
This article will help chief security officers (CSOs) and
[DevOps engineers](https://roadmap.sh/devops) understand:
- The major challenges in managing
[Kubernetes](https://thenewstack.io/kubernetes/)security.
- The shortcomings of traditional security measures.
- Need for intent-driven Kubernetes security monitoring.
## Why Kubernetes Security Is So Complex
Since a Kubernetes cluster is made up of multiple microservices and components, each one of those can be a potential entry point for attackers. Essentially, the more moving parts you have, the larger your attack surface becomes.
That could be problematic for organizations that rely heavily on these systems. Just one misstep in Kubernetes configuration can lead to serious risks like data leakage or unauthorized access to workloads.
A security breach in such environments can be dangerous. Not only could it damage your company’s reputation, you will also lose your customers’ trust.
There are also financial repercussions to consider, like breach response costs, lost business and regulatory fines, as well as compliance with industry regulations, like
[PCI DSS](https://thenewstack.io/what-to-know-about-container-security-and-digital-payments/). These regulations are in place to protect data. Failing to comply can result in significant fines and penalties.
## 5 Major Challenges of Kubernetes Security
One thing is clear, Kubernetes’ potential is equal to its risk (if not riskier) unless it’s secured properly. Yet, companies find it extremely challenging to ensure every aspect of the Kubernetes cluster is secured.
Kubernetes’ multifaceted nature means organizations have to
[maintain security](https://roadmap.sh/cyber-security) at different layers, including infrastructure, network runtime, container runtime, control panel and so forth.
Here are the major challenges organizations face while establishing security across these layers:
### 1. Expanded Attack Surface
Each Kubernetes cluster has several microservices and components interacting within the environment that add potential entry points for attackers. The more containers and clusters you deploy, the larger the attack surface becomes, making it harder to pinpoint and mitigate vulnerabilities.
### 2. Configuration Management
Misconfiguration due to human error is one of the major challenges in Kubernetes.
On an episode of
[Cloud Security Podcast](https://www.cloudsecuritypodcast.tv/videos/kubernetes-goat-vulnerable-by-design), [Madhu Akula,](https://www.linkedin.com/in/madhuakula/) a prominent security leader and the creator of Kubernetes Goat, said: *“Kubernetes itself is not inherently vulnerable by design, but security issues often arise from misconfigurations. For instance, network security policies (NSPs) are crucial for controlling traffic between pods, yet many organizations neglect to implement them, inadvertently exposing applications to unauthorized access.”*
Since containers are dynamic, it’s difficult to identify what caused a misconfiguration and maintain a consistent security posture.
**3. Pod-to-Pod Networking**
Kubernetes provides extensive network configuration options, allowing all pods in a cluster to communicate with each other by default. If one pod is compromised, it can potentially attack other pods unless proper network policies are set up.
Say a financial services company deploys an application consisting of multiple microservices, such as a User Management Service, Transaction Processing Service, Customer Support Service and Analytics Service, each running in separate pods.
By default, Kubernetes allows all pods to communicate with each other, creating an open network. So if an attacker exploits a vulnerability in the User Management Service pod, which is responsible for user authentication and storing sensitive user data, they can use this initial foothold to scan and exploit vulnerabilities in other pods.
### 4. Software Supply-Chain Issues
Kubernetes environments are heavily reliant on a sprawling
[software supply chain](https://thenewstack.io/fortifying-the-software-supply-chain/), including application components and [CI/CD](https://thenewstack.io/ci-cd/) pipelines.
Vulnerabilities in any part of this chain — such as outdated libraries or weak access controls — can pose serious security risks.
On another
[Cloud Security Podcast](https://www.cloudsecuritypodcast.tv/videos/kubernetes-security-at-scale-in-a-ci-cd-pipeline), cybersecurity practitioner [Michael Fraser](https://www.linkedin.com/in/itascode/) said: *“Securing Kubernetes in a CI/CD pipeline is a multifaceted challenge that requires continuous vigilance — it’s not just about protecting the clusters but also ensuring that every deployment, configuration and interaction is resilient against evolving threats.”*
Managing these supply chain complexities requires robust controls from development through runtime.
### 5
**. **Infrastructure Security
Securing Kubernetes infrastructure involves protecting control plane components (like the API server) and worker nodes. Whether you manage Kubernetes on-premises or use a cloud service, securing these components can be complex.
The level of responsibility for this security varies based on whether you’re using a cloud provider or handling it yourself, adding an extra layer of complexity.
## Why Traditional Security Approaches Fall Short
While the following solutions may be effective in more static, monolithic architectures, they frequently fall short in the dynamic, distributed environments that characterize modern Kubernetes clusters.
Below are some key limitations of traditional Kubernetes security solutions:
### Reactive, Not Proactive
The traditional security approach focuses on runtime security scanning, which detects threats only when they are activated — in other words, after the damage has been done. This not only leaves a critical window of vulnerability, it also makes it challenging to mitigate issues before they escalate.
For example, in 2017, Equifax, one of the largest credit reporting agencies, suffered a massive data breach affecting
[147 million individuals.](https://www.hbs.edu/faculty/Pages/item.aspx?num=53509) The breach resulted from a vulnerability in Apache Struts, an open source web application framework, which Equifax had failed to patch promptly. Equifax’s security measures were primarily reactive. They discovered the breach only after it had already been exploited by attackers.
This approach led to severe financial and reputational damage, highlighting the need for proactive security solutions that address threats before they can be exploited.
### Performance Overhead
Traditional security protocols have computation processes piled up for different tasks including encrypting, decrypting, authenticating or signing data.
This not only results in performance issues but also increases latency, affecting service quality and user experience.
For example, encrypting a large file before it’s transmitted across a corporate network can introduce delays. This could slow down crucial business applications like financial transactions or real-time analytics.
### Outdated Information
Outdated security methods depend on established databases of known vulnerabilities to identify and mitigate risks. However, these approaches are ineffective against zero-day attacks, which exploit previously unknown flaws or newly discovered and uncatalogued threats.
As a result, systems remain vulnerable to emerging and undocumented security risks that traditional methods cannot detect or prevent.
These traditional security measures often need to catch up to the distributed and dynamic Kubernetes cluster. This gap points out the urgency of a solution that not only anticipates and neutralizes threats in real time but also maintains high performance.
## Intent-Based Security Management
[Nimbus](https://github.com/5GSEC/nimbus) is an open source tool maintained by AccuKnox that provides a new direction for Kubernetes security by simplifying and automating security management. The toolkit focuses on security intents rather than specific policies and tools. As the README explains: “Nimbus aims to decouple security intents from its actual implementation, i.e., use of policy engines and corresponding policies and rules.”
Key features include:
**Intent-based security management:**Users define security intents, such as “prevent privilege escalation,” and Nimbus handles the implementation through appropriate policies and tools. **Automated policy generation:**Nimbus uses Kubernetes’s active reconciliation logic to generate and enforce policies aligned with the defined security intents. **Flexibility and adaptability:**Nimbus can work with various policy engines and adapt to changes, such as switching from one container network interface (CNI) to another, without requiring manual reconfiguration.
By focusing on security intents, Nimbus reduces the complexity of managing multiple tools and policies, making it easier for organizations to maintain a robust security posture across their Kubernetes environments.
### How Nimbus Works
Nimbus operates by abstracting the complexity of security management into a more manageable framework. Here’s how it works:
#### 1. Defining Security Objectives
The first step is defining your organization’s high-level security requirements. That might be to “restrict access to sensitive data” or “prevent unauthorized changes to configurations.” These high-level security goals are also known as “intents.”
#### 2. Automating Policy Translation
Next, Nimbus takes these broad goals and breaks them down into specific, actionable policies and rules. It uses various policy engines to enforce specific measures.
For example, if your goal is to stop privilege escalation, Nimbus will create rules to enforce that, like controlling who gets admin rights and monitoring any unusual activity.
#### 3. Ongoing Reconciliation
Nimbus is always on the lookout, keeping an eye on your environment to make sure everything is working as intended. If something changes, Nimbus proactively adjusts the rules to keep up with the new situation.
#### 4. Using Kubernetes’s Built-In System
Nimbus uses Kubernetes’ built-in system for continuous Kubernetes security monitoring and adjustment. This means even if your environment evolves with new applications, updates or changes, Nimbus can seamlessly adapt to these modifications, aligning with your security goals to keep defenses proactive and adaptable. With automated policy generation and flexibility, Nimbus helps you stay ahead of threats in evolving environments.
## Wrapping Up
Traditional security measures no longer cut it for dynamic Kubernetes environments. If your organization is still relying on these methods, ask yourself:
- What will be the impact on your business if a vulnerability goes undetected for weeks?
- How much would a security breach cost in terms of reputation and revenue loss?
- Are your current measures enough to prevent delays in critical application development?
If your answer to the last question is no, it’s time to incorporate a better approach.
The
[AccuKnox Kubernetes security solution](https://www.accuknox.com/products/kubernetes-security) is designed for runtime protection, threat detection and regulatory compliance. Don’t wait for attackers to crawl in — secure your environment with AccuKnox today. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)