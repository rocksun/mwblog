# Revolutionizing Application Security: The Plea for Unified Platforms
![Featued image for: Revolutionizing Application Security: The Plea for Unified Platforms](https://cdn.thenewstack.io/media/2025/04/5a7546e1-appsec-unified-platforms-1024x576.jpg)
A majority — 63% — of codebases in production have unpatched vulnerabilities rated high or critical according to [research from Palo Alto Networks](https://www.paloaltonetworks.com/prisma/unit42-cloud-threat-research). Coupled with the fact that 71% of organizations say that rushed cloud native application deployments have [introduced security vulnerabilities](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/state-of-cloud-native-security-2024), it comes as no surprise that 80% of security exposures nowadays occur in the cloud. These data points strongly suggest that the current approach to securing cloud native applications is inadequate, and that could affect your business.

To better understand the challenges of securing cloud applications, I spoke with [Sarit Tager](https://www.linkedin.com/in/sarit), vice president of product management, Cortex Cloud at Palo Alto Networks. We touched upon the four biggest inadequacies that are not being properly addressed, and discussed how you can adopt a more holistic approach to [cloud security](https://thenewstack.io/security/).

## 4 Biggest Challenges of Cloud Native Application Security
As organizations increasingly adopt cloud native applications, securing the entire application life cycle — from code development to runtime environments — grows more complex. The following are the four key challenges that arise in the process of securing cloud native applications.

### 1. Fragmentation
The complexity of cloud native environments, comprising multiple tools, third-party vendors and distributed systems, leads to fragmentation. Palo Alto Networks’ research has found that 54% of organizations say [complexity and fragmentation ](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/research/state-of-cloud-native-security-2024)of cloud environments present a major challenge to security. This, in turn, drastically expands an organization’s attack surface, making security management all the more challenging.

Organizations rely on a wide range of security solutions to protect cloud native applications. This includes static, dynamic and interactive application security testing (SAST, DAST, IAST), software composition analysis (SCA), and [software supply chain security](https://thenewstack.io/ebooks/security/a-blueprint-for-supply-chain-security/). These mechanisms are all effective in isolation, but the fragmentation can result in alert fatigue, siloed data and blind spots.

As Tager explained to me, current application security approaches are built in silos and can’t stop attacks as they happen.

### 2. The Shift Left
“Shift left” is a practice that focuses on addressing security risks earlier in the development cycle, before deployment. While effective in theory, this approach has proven problematic in practice as developers and security teams have conflicting priorities. For example, security is seen as a [gating factor](https://www.paloaltonetworks.com/resources/research/state-of-cloud-native-security-2024) hindering software releases for 86% of organizations. Meanwhile, 91% say that developers need to produce more secure code.

Developers are measured on the velocity and quality of code, often putting security on the back burner. The heavy workload developers face in organizations that have implemented shift-left policies can create bottlenecks, [runtime gaps](https://thenewstack.io/why-cloud-security-fails-the-posture-vs-runtime-gap/) and lead to developer burnout and reduced productivity. These factors combined can ultimately result in decreased security and efficiency.

### 3. The Need for Real-Time Threat Prevention
Cloud native applications are dynamic; constantly deployed, updated and scaled, so robust real-time protection measures are absolutely necessary. Every time an application is updated or deployed, new code, configurations or dependencies appear, all of which can introduce new vulnerabilities.

The problem is that it is difficult to implement real-time cloud security with a traditional, compartmentalized approach. Organizations need real-time security measures that provide continuous monitoring across the entire infrastructure, detect threats as they emerge and automatically respond to them. As Tager explained, implementing real-time prevention is necessary “to stay ahead of the pace of attackers.”

### 4. Supply Chain Risks
Software supply chain risks arise from vulnerabilities introduced through the myriad components and services used in the software development pipeline and applications deployment.

Cloud native applications tend to rely heavily on open source libraries and third-party components. In 2021, [Log4j’s Log4Shell vulnerability](https://thenewstack.io/log4j-why-organizations-are-failing-to-remediate-this-risk/) demonstrated how a single compromised component could affect millions of devices worldwide, exposing countless enterprises to risk.

Effective application security now extends far beyond the traditional scope of code scanning and must reflect the modern engineering environment. There are three critical supply chain disciplines organizations must now evaluate for proper protection: security in the pipeline (SIP), security of the pipeline (SOP) and security around the pipeline (SAP). Each supports the speed of engineering without compromising on risk and security management.

What is the solution to all of these challenges, then? The answer is unified security platforms.

## Why Unified Security Platforms Are the Way to Go
Given the four challenges outlined above, it is clear why organizations need to evolve beyond traditional point solutions. The old paradigm of isolated security tools is no longer viable in cloud native environments, where risks shift at a rapid pace.

A unified security platform is an integrated security solution that consolidates multiple security functions into a single system. Unlike traditional security models, unified platforms provide centralized visibility, automation and coordination across an enterprise’s entire security infrastructure. They offer a holistic, real-time security approach.

By integrating real-time monitoring, automated threat detection and proactive risk mitigation, these platforms eliminate the gaps attackers often exploit. With a unified security platform, organizations can transition from relying on isolated, disjointed processes, to embedding security into every stage of application development and cloud operations.

As Tager told me, “The usage of [cloud and AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) is only going to grow, and attackers will improve their tactics as they also begin to leverage AI for novel attacks. The only way to achieve real-time security is through a platform approach that centralizes the data across the entire cloud environment. One data lake that AI can run on to deliver timely insights and actions.”

To sum up, unified security platforms are the future because they:

- Eliminate fragmentation by reducing the complexity of managing multiple tools and vendors, consolidating disparate security functions into a single interface.
- Automate monitoring and security scanning of agents without slowing down development cycles (from code to cloud to security operations center), while offering runtime protection.
- Mitigate risks through automated compliance checks and policy enforcement over misconfigurations, exposed secrets and other vulnerabilities, leveraging tools such as AI.
- Provide real-time visibility and continuous monitoring across the entire cloud environment, thus enabling real-time threat prevention.
- Offer end-to-end visibility into the software supply chain, allowing organizations to assess and verify the security of open source libraries, third-party integrations and dependencies.
“This approach enables organizations to seamlessly build secure applications and prevent issues before they become threats. Instead of chasing threats after deployment, organizations achieve protection at the start, which is much faster,” according to Tager.

## A Unified AppSec, CloudSec, SecOps Approach
Organizations that adopt unified security platforms detect incidents 72 days faster and contain them 84 days sooner, according to a [2025 study](https://newsroom.ibm.com/2025-01-28-ibm-and-palo-alto-networks-find-platformization-is-key-to-reduce-cybersecurity-complexity) jointly conducted by [IBM](https://www.ibm.com?utm_content=inline+mention) and Palo Alto Networks. They also achieve an average return on investment (ROI) of 101%, compared to just 28% for those that have yet to embrace unified platforms.

Just as adversaries operate across the entire attack surface, defenders must take a similarly unified approach. Palo Alto Networks’ Cortex Cloud boosts application security and improves multicloud risk management while enabling real-time threat prevention and attack mitigation.

Cortex Cloud breaks down silos by bridging gaps between application security (AppSec), cloud security (CloudSec) and security operations center (SOC) teams. By unifying data, automating workflows and leveraging AI-driven insights, it enhances operational efficiency with the goal of reducing risk, preventing attacks and stopping threats in real time.

As Tager put it, “Cortex Cloud consolidates data from native scanners, third-party findings and runtime to enable AppSec teams to secure the entire engineering ecosystem — including code, software supply chain and tools. AppSec teams have all the necessary data and context to quickly take action and stop risks.”

Step into the future of real-time cloud security and [learn more about Cortex Cloud](https://www.paloaltonetworks.com/blog/2025/02/announcing-innovations-cortex-cloud/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)