# Cloud Reliability Requires Runtime Security, Zero Trust
![Featued image for: Cloud Reliability Requires Runtime Security, Zero Trust](https://cdn.thenewstack.io/media/2024/06/ce8a1da2-cloud-reliability-requires-runtime-security-zero-trust1-1024x576.jpg)
In February 2024, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) issued a [security bulletin](https://access.redhat.com/errata/RHSA-2024:0717) alerting users about a vulnerability in runC. RunC is a core container infrastructure component used as the container runtime engine in [Docker](https://www.docker.com/?utm_content=inline+mention)‘s containerd and other runtimes.

Long story short, runC failed to properly isolate containers from the host operating system (OS) directory. The result? An attacker could leverage this vulnerability to infiltrate the host system via a container with a vulnerable version of runC.

**Securing Code Is Not Enough in Today’s Threat Landscape**
The vulnerability in runC establishes the [importance of runtime security](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/), specifically in cloud workloads. Before cloud, if your code was secure during build and deployment, you could sleep peacefully.

But with the rise of cloud computing and microservices, the number of moving parts across the entire IT workload has significantly increased. The container, the [Kubernetes](https://roadmap.sh/kubernetes) (K8s) cluster, the cloud platform — anything can contain a vulnerability. [Runtime security](https://www.accuknox.com/products/runtime-security) — continuous monitoring of your workload and platforms — is necessary.

Securing your codebase is just one part of the puzzle. Mitigating vulnerabilities or misconfigurations in the base layers should be viewed with a cloud native security approach. This helps you see security in terms of layers.

However, there are some challenges with runtime security:

- Cloud native environments evolve too fast.
- Microservices increase complexity.
- Ephemeral virtual infrastructure makes monitoring a nightmare.
- Vulnerabilities in older technologies used in conjunction with modern ones make matters more complex.
No matter how useful and relevant runtime security is, making it work is in itself an uphill task. This is where [Cloud Workload Protection Platform (CWPP)](https://www.accuknox.com/products/cwpp) tools take runtime security to the next level by:

- Automating.
- Continuous monitoring.
- Keeping an inventory of active assets.
- Standardizing security checks.
- Integrating security with operations (
[DevSecOps](https://thenewstack.io/what-is-devsecops/)). - Implementing strict
[zero trust](https://thenewstack.io/what-is-zero-trust-security/).
I will talk about these in detail. But let’s first understand why runtime security is so crucial in today’s threat landscape.

**Microservices Maximize the Attack Surface**
Most cloud workloads are in the form of microservices. We always urge people to move to the cloud and break monolithic apps into microservices. It’s good advice. However, microservices bring a unique set of complexities.

- When you break down your monolithic software into microservices, you’re basically increasing potential entry points for malicious actors. The attack surface expands. From APIs to database connections and third-party integrations, keeping tabs on entry points becomes a nightmare.
- These entry points are dynamic, meaning they are created and destroyed dynamically. There isn’t a fixed number of entry points in a group of microservices. Therefore, it’s not enough just to check for vulnerabilities during deployment.
**Cloud Elasticity: No Fixed Perimeter**
The allure of cloud computing lies in the ability to scale your infrastructure up and down at any time. This is an incredibly awesome option for companies that don’t want to buy on-premises hardware and spend a lot of money upfront, just to see those new shiny hardware pieces lying unused during off seasons.

But this elasticity brings a security problem: As instances pop up and vanish, it becomes difficult for the security team to set up a fixed perimeter to defend. It’s like constantly changing the position and number of entrances to your home.

Traditionally, you would apply network security policies to your fixed number of virtual machines (VMs) and host machines, and you’d be good to go. But when it comes to cloud security, you can’t manually apply security policies to instances whenever they pop up. You need to automate this with a configuration script. But, even a slight misconfiguration in this script will weaken the security of the instances.

**Cloud Infrastructure Parts Are Intrinsically Connected**
In 2019, Capital One suffered a massive data breach due to a misconfiguration in its [AWS](https://aws.amazon.com/?utm_content=inline+mention) web application firewall. Now, here’s the interesting thing: The attackers did not directly access the company’s S3 bucket. Rather, they employed a method known as lateral movement. A Redditor perfectly [summarized](https://www.reddit.com/r/aws/comments/cl4h6t/comment/evsu7cg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) the incident:

*“The attacker didn’t have direct access to the S3 buckets; rather, she had access to an EC2 server that had an AWS role allowing for access to the buckets. So although her account permissions were provisioned properly, she was able to tunnel through different resources to increase her permission level.”*
Without runtime security and active anomaly detection, this kind of lateral movement can’t be identified.

### A Case Study on the Equifax Data Breach
In 2017, Equifax suffered a massive data breach. The entry point? A client-facing Apache Struts server with a vulnerability. What’s more: The security certificate of the device responsible for monitoring network traffic associated with the server expired months before the attack happened.

The key concept here is “inventory of active assets.” Equifax didn’t have visibility into its inventory of active assets and the dependencies or tools used by these assets to work in a secure fashion.

Even the most tried and tested pieces of code can have vulnerabilities. Companies need to be vigilant about newly discovered vulnerabilities in old software and tools.

**Runtime Container and Application Security to the Rescue**
These cybersecurity threats can largely be mitigated with runtime security, which applies real-time checks instead of treating security as a one-off process.

Your applications are no longer monolithic. By seeing security in terms of layers, rather than as a monolith, everything falls into place. When you have real-time visibility into all the assets that are running in the container, the configuration of Kubernetes pods and the underlying OS, you have a clearer idea of which elements to protect — and what can go wrong — if these elements aren’t configured properly.

**CWPP Tools Automate Detection**
CWPPs gather and analyze all the active assets running on the cloud platform. And when we say “cloud workload,” we mean:

- The application code.
- The dependencies or libraries.
- The container image.
- Kubernetes and pods.
- Even the underlying OS.
Having visibility helps establish the relationships between your assets. How are they connected to each other? How do they “talk” to each other? The network graph answers these questions.

*The most important benefit of establishing the active asset inventory and identifying how they work and interact with each other is creating a baseline. This baseline forms the bedrock of real-time anomaly detection.*
For example, if Equifax had clear visibility into its active assets in 2017, it might not have suffered the data breach. The Apache team released the patched version in March 2017, well before [Equifax announced](https://investor.equifax.com/news-events/press-releases/detail/237/equifax-releases-details-on-cybersecurity-incident) it was breached in September. If the company had patched the Apache Struts vulnerability in time, the breach may not have happened.

When you proactively patch software when vulnerabilities are discovered, you reduce your attack surface. Because CWPP systems continually update their databases with known lists of vulnerabilities, these runtime application protection security systems can detect attempts to exploit these known vulnerabilities. For example, a CWPP system can actively detect a script trying to probe whether a website is using WordPress 6.5.0 (which has a severe vulnerability). Then the system can then take necessary actions, like blocking the offending IP address.

Another good way to mitigate attacks on a real-time basis is to explicitly define what containers can and cannot do. CWPP tools take it further by restricting what containers can and cannot do on the system level, not just a process level.

These tools can define which processes within a container can access a sensitive file, then codify and automatically enforce those rules to direct containers what and what not to access.

The same kind of runtime container security mechanism can be used for network microsegmentation. This allows stricter enforcement of rules in terms of which Kubernetes pods can communicate with each other or what ports should or should not be used.

**Runtime Security Limitations: How to Handle Them**
In 2023, Sophos released a security bulletin that explained how BlackCat ransomware infiltrated one of its customer’s Azure storage accounts. BlackCat is the same ransomware that [stole terabytes of data from Change Healthcare](https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html) and locked the company out of its systems in 2024.

The Sophos attackers first deactivated security policies enforced by the Sophos Central console. They accomplished this by infiltrating the LastPass Chrome extension and stealing a one-time password (OTP) that provided access to Sophos Central. Once they disabled the security policies, the attackers broke into the victim’s Azure Storage accounts.

This means the attacker hopped from the victim’s system to its Azure Storage account. The Scattered Spider ransomware also works similarly. Both ransomware groups employ social engineering tactics like phishing to gain an initial foothold.

Runtime security might not be efficient in this scenario. Instead, network segmentation could have limited the attacker’s access to sensitive Azure storage data. When you break your workloads into distinct network segments, you can define access policies for all the segments. Network segments isolate connected systems to prevent lateral movement by attackers.

Further, policies can be created that consider the workload’s sensitivity. In the Sophos case, the victim company could have enforced more strict firewall rules for the network segment associated with the Azure Storage account.

But let’s play the devil’s advocate here.

What if the attacker leverages [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)‘s Remote Desktop Protocol (RDP) and Remote Monitoring tools to infiltrate Azure Storage accounts? It would look like a valid entry into the Azure Storage accounts because it would use the victim’s IP. This is where zero trust comes in.

**Zero Trust and Least Privilege Remain the Key**
Let’s go back to the Capital One data breach. The attacker did not directly access the S3 bucket to steal data. Rather, she first intruded into an EC2 instance that had access to the S3 bucket.

If the organization had enforced a zero-trust policy, this incident likely would not have happened. Zero trust assumes your systems are already vulnerable and have been infiltrated by malicious actors.

If Capital One had this policy in place, it would have hardened the EC2 instance with multifactor [authentication](https://roadmap.sh/videos/basics-of-authentication). Even if the attacker had gained access to the instance, she could never have accessed the S3 bucket.

Runtime security tools constantly monitor cloud workloads, create baseline permission requirements for various workloads and continuously identify unnecessary permissions granted to containers, pods or cloud infrastructure like EC2.

Based on their findings, these tools recommend the least permissive policies that will let IT assets access only the locations or files they need to work properly; nothing else remains within their reach.

**The Bottom Line**
In 2022, 25,081 CVEs were published. By 2023, that figure grew to over 28,900. Your IT infrastructure — on- or off-premises — is a very alluring hunting ground for attackers.

Attacks have also become more sophisticated. Gone are the days of signature-based threat detection. You have to accept that the next cyberattack might be completely unique with no precedent whatsoever.

In this scenario, it’s imperative to take a proactive approach to security. Keep monitoring workloads and the cloud platform before, during and after deployment. It takes just one vulnerable entry point for attackers to ruin a business.

Runtime security tools like [AccuKnox CWPP](https://www.accuknox.com/ebooks/accuknox-cloud-workload-protection-platform-cwpp-an-inside-look) and a strict zero-trust policy will help keep your business safe for years to come — no matter how sophisticated attackers get.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)