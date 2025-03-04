The complexity of cloud environments means that there is a virtually infinite list of potential security risks and vulnerabilities that could arise within cloud infrastructure or workloads. That said, some cloud security threats are more prevalent than others – and knowing which risks and vulnerabilities are trending is key to knowing what to prioritize when managing the attack surface for your organization. To that end, this article details seven of the most prominent cloud threats and vulnerabilities that emerged in 2024, including several discovered by Aqua researchers.

## What are Cloud Native Vulnerabilities?
A cloud native security vulnerability is any type of threat or risk that threat actors could exploit to breach cloud native services, such as containers. Examples of common types of cloud vulnerabilities include:

- Software vulnerabilities in the operating servers running on cloud servers.
[Insecure code inside container images](https://www.aquasec.com/cloud-native-academy/application-security/container-scanning/)that are used to deploy applications to the cloud.- Misconfigurations within containers, another risk that could lead to breaches of containerized applications.
- Misconfigured
[Identity and Access Management](https://www.aquasec.com/cloud-native-academy/application-security/identity-and-access-management/)(IAM) settings, which could lead to the exposure of sensitive information or provide attack vectors for taking control of applications. - Flaws in cloud APIs, which threat actors could abuse to gain unauthorized access or exfiltrate sensitive data.
Effective cloud security hinges on the ability to discover and remediate threats like these before attackers exploit them.

### The Top 7 Cloud Native Threats and Vulnerabilities of 2024
The goal of cloud security tools should be to discover security risks and vulnerabilities of all types. But again, focusing on the newest, most common, or most severe risks is one way to help decide which types of threats to prioritize.

The following container and cloud vulnerabilities fall into this category because most are relatively novel threats that, if left unmitigated, can pose significant harm to cloud environments and cloud-based workloads.

### #1 Perfctl
As Aqua [reported in October 2024](https://www.aquasec.com/blog/perfctl-a-stealthy-malware-targeting-millions-of-linux-servers/), perfctl is malware that targets Linux servers. The goal of the malware, which has been active for three or four years, is to run cryptomining software as part of a [cryptojacking attack](https://www.aquasec.com/cloud-native-academy/cloud-attacks/cryptojacking/) after it gains access to its victims’ servers. To do this, it exploits a Polkit vulnerability ([CVE-2021-4034](https://nvd.nist.gov/vuln/detail/cve-2021-4034)) to launch a privilege escalation attack.

What makes perfctl particularly notable – and especially risky – is the sophisticated techniques that it uses to evade detection. It relies on rootkits to hide its presence, ceases operations when users are active within a system (in order to avoid creating “noise” that could alert users to the breach) and deletes its binary and runs as a background service.

Practices like [network segmentation](https://www.aquasec.com/cloud-native-academy/container-security/network-segmentation/) and restrictions on file execution can harden servers against this and similar malware.

### #2 Bucket Monopoly
[Bucket Monopoly](https://www.aquasec.com/blog/bucket-monopoly-breaching-aws-accounts-through-shadow-resources/) is a vulnerability in six services running within the Amazon Web Services (AWS) cloud that allow attackers to carry out a wide variety of attacks, including remote code execution and account takeover in some cases.
The exploit relies on what’s known as the “Shadow Resource” attack vector, which abuses resources that AWS services generate automatically, often without the user’s knowledge.

After discovering these cloud security vulnerabilities, Aqua reported them to AWS, which remediated the issues before they were disclosed publicly. Still, this threat was a reminder of how even the best-managed public clouds can experience major security vulnerabilities within their core cloud services.

### #3 Snap Trap
In February of 2024, Aqua detailed a cloud security threat known as [Snap Trap](https://www.aquasec.com/blog/snap-trap-the-hidden-dangers-within-ubuntus-package-suggestion-system/), which allows threat actors to plant malicious software packages on systems running Ubuntu Linux. More specifically, it enables abuse of a feature in Ubuntu’s software package management system that auto-suggests the names of software packages. By manipulating how the feature works, threat actors can potentially trick users to install malicious packages instead of legitimate ones.

The exploit could also be used to plant malicious code inside containers, since containers based on Ubuntu commonly use Ubuntu’s package management tool to install software at runtime.

This flaw has been known since 2016 but never definitively mitigated. The best way to defend against it is to take advantage of capabilities – like those available through the Aqua platform – that block risky features such as the use of package managers to install software inside containers.

### #4 Hadooken
[Hadooken](https://www.aquasec.com/blog/hadooken-malware-targets-weblogic-applications/), which Aqua researchers discovered in late summer, is malware that targets Oracle WebLogic, a widely used Java EE application server. Exploitation of the vulnerability entails abusing weak credentials or vulnerable admin consoles to gain access to WebLogic systems. Once inside, attackers can escalate the breach by running arbitrary code or moving laterally to compromise other systems.
Hadooken is a prime example of why vulnerability scanning remains critical, even for organizations that rely on platforms from responsible vendors like Oracle.

### #5 GitHub Repo Secret Exposure
In an example of a cloud security threat that resulted from risky behavior on the part of humans rather than technical flaws, it came to light in May 2024 that access credentials for Azure and Red Hat platforms had been [exposed via GitHub repositories](https://www.aquasec.com/blog/github-repos-expose-azure-and-red-hat-secrets/). The exposures happened because employees of these tech companies created GitHub repos for personal projects where they accidentally stored access credentials.

This threat is a reminder of the importance of educating users about security best practices, as well as scanning resources like GitHub repos for [improperly managed secrets](https://www.aquasec.com/cloud-native-academy/supply-chain-security/secrets-management/).

### #6 CUPS Vulnerability
CUPS, an open source printing server, may seem innocuous enough. But as security researchers reported in September 2024, Linux systems that run CUPS are [vulnerable to an attack](https://www.aquasec.com/blog/cups-a-critical-9-9-linux-vulnerability-reviewed/) that allows remote threat actors to execute arbitrary code. Because the attack is relatively easy to carry out and affects a very popular software service, it’s considered a severe vulnerability.

To block the vulnerability, admins can remove CUPS software from affected systems or block access to CUPS from the network. To mitigate the threat at scale, consider using Aqua to enforce a runtime policy that prevents the CUPS service from running on all of your systems.

### #7 Lucifer
As we reported in February 2024, Lucifer is a malware campaign that targets Apache Hadoop and Apache Druid, which are popular open source “big data” software. Originally, the goals of the attackers appeared to be to experiment with [defense evasion](https://www.aquasec.com/cloud-native-academy/cloud-attacks/defense-evasion/) techniques, but Lucifer could lead to more serious threats, including remote code execution.

### Mitigating Cloud Security Threats and Vulnerabilities with Aqua
As a comprehensive cloud and container security platform, Aqua empowers organizations to detect and mitigate cloud security threats of all types – from operating system vulnerabilities like perfctl, to insecure cloud services like Bucket Monopoly, to insecure secrets management like the GitHub secrets exposure incident, and far beyond.