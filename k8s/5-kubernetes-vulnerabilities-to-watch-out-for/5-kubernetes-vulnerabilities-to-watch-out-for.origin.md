# 5 Kubernetes Vulnerabilities To Watch Out For
![Featued image for: 5 Kubernetes Vulnerabilities To Watch Out For](https://cdn.thenewstack.io/media/2025/04/8f48446f-kubernetes-vulns-2025-1024x576.jpg)
Kubernetes just had a rough week for security, as [CVE-2025-1974](https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/) came to light on March 24. Since you’re probably already thinking heavily about [Kubernetes security](https://thenewstack.io/kubernetes-security-report-evolving-landscape-of-devsecops), we thought we’d do a quick tour of some other vulnerabilities you should watch out for and give you a brief idea of how to prevent them from ruining your week too.

Kubernetes security is its own thing — the Kubernetes platform involves numerous layers that all need to be secured. Container packaging enables hosting an almost infinite combination of languages, frameworks and commercial off-the-shelf software. That’s why security tools that are native to Kubernetes are key to a complete [Kubernetes security](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes) picture.

Here are five vulnerabilities to watch out for when running a Kubernetes cluster and some information about how to mitigate their impact.

## Struts
[CVE-2024-53677](https://nvd.nist.gov/vuln/detail/CVE-2024-53677)
These kids today with their React frameworks, their npm repos and their endless streams of event-driven websites. Back in the early 2000s, we didn’t have a [JavaScript](https://roadmap.sh/javascript) that was uniformly compatible enough to even call JavaScript! We had Java, and we liked it!

Of course, 20 years later, [Java](https://roadmap.sh/java) is still a mainstay of the enterprise workforce. There’s a library for everything, and instead of experiencing constant updates and framework refactorings, Java web assets tend to be relatively stable and unexciting. Unexciting is good, frankly.

Except when “unexciting” means that a nasty remote code execution attack makes it under the radar. This one’s been around the block before. In fact: The second of the big-time [Struts](https://struts.apache.org/) vulnerabilities was found in December 2024. This time, using a path traversal attack, it enabled malicious actors to upload or save a file in a restricted location, thereby allowing them to use remote code executions.

Something so stable, old and frankly boring is exactly where the nastiest vulnerabilities strike. Everyone expects a hot new web framework to have bugs, but the slowly baking projects that have been incrementing by 0.0.1 releases over the past 10 years can be the juiciest targets for reverse engineers, and Struts seems to be the gift that just kept on giving. Hopefully, it’s done giving its gifts.

## XZ Utils
[CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094)
Detecting supply chain attacks is incredibly difficult. And what if the social engineer is willing to spend years winning the trust of an entire open source community? That’s exactly what happened with XZ utils, and the attack was found through diligence and dedication to process and code review.

XZ utils is one of those dependencies that tends to get shoved into containers to support compression and decompression of xz files. Thus, if developers are trying to squeeze extra space out of every compressed file, they might choose xz over .zip.

And if they did, now they have to include XZ utils with their binary, which makes it a juicy target for someone trying to compromise a whole ecosystem of downstream projects and sites.

Once the vulnerability was detected in XZ utils versions 5.6 and 5.6.1, those versions were flagged in all containers scanned with tools like Red Hat Advanced Cluster Security for Kubernetes (RHACS). Users can use the RHACS policy to prevent admission of containers with this vulnerability and to identify already deployed containers at runtime.

## openSSH Server
[CVE-2024-6387](https://www.qualys.com/regresshion-cve-2024-6387/#:~:text=regreSSHion%2C%20CVE%2D2024%2D6387,poses%20a%20significant%20exploit%20risk.)
Whenever there is a vulnerability in any implementation of SSH, the sky is falling. No application provides greater access, nor more intimate a connection to the host computer than the Secure Shell.

Just think of all the amazing tools that literally just open an SSH connection and spew data into it: [rsync](https://en.wikipedia.org/wiki/Rsync), [Ansible](https://www.redhat.com/en/technologies/management/ansible), [sshuttle](https://github.com/sshuttle/sshuttle). SSH is the most fundamental way to get into a computer that’s not in front of you. Before we had SSH we had Telnet, and packet sniffing flourished.

Today, Telnet connections are encrypted and considered secure the world over. Until the sky begins falling again. Most recently, a machine-in-the-middle attack could allow someone to impersonate a server on the client thanks to a faulty DNS host key check on the OpenSSH client-side.

This was a very specific attack that worked only when the client set VerifyHostKeyDNS to either “yes” or “ask,” but the vulnerability seems to have been present since August 2023. Fortunately, it’s now known and can be flagged, in case any of your containers contain a vulnerable version of OpenSSH. Plus, since SSH really doesn’t belong in containers, you could block container images that included SSH from being deployed, removing the attack vector in the first place.

## /debug/pprof
[CVE-2019-11248](https://github.com/kubernetes/kubernetes/issues/81023)
Platform vulnerabilities are tricky due to service-level agreements (SLAs). Keeping open source packages up to date while delivering services according to promises can make security a difficult, never-ending race. And it’s even worse if the vulnerability is contained within support and troubleshooting tools. CVE-2019-11248 is essentially a dangling endpoint, open through an unauthenticated [Kubelet healthz port](https://kubernetes.io/docs/reference/using-api/health-checks/). Clever attackers could use this debugging endpoint to pull sensitive cluster information for illicit use. What kind of sensitive information? Oh, just memory addresses and configuration details.

The real danger here comes from forgetting to remove debugging tools from a cluster or container before deployment to production. That’s entirely understandable, considering how complex it can be to go digging through cluster logs to find the source of an error.

Tools that scan API access will warn of unusual or unauthorized activity. An attacker’s use of this particular vulnerability would trigger an alert, allowing an administrator to quickly respond and minimize damage that could result from the exploit. The overall goal is to remove these types of tools entirely and, barring that, to set up guardrails to prevent such tools from making it into production.

## Kubernetes Image Builder
[CVE-2024-9594](https://github.com/kubernetes/kubernetes/issues/128007)
Sometimes, just building a container image can cause problems. But maybe not the way you’d expect. In 2024, CVE-2024-9594 was found in the Kubernetes Image Builder, which is used to build virtual machine images. For versions of the Kubernetes Image Builder 0.1.37 and prior, default user credentials were enabled during the image build process when used on raw providers like QEMU, OVA or Nutanix. This meant that while a user was building an image with this tool, someone could then log in to the cluster using this information to gain root. Fortunately, this problem did not affect some Kubernetes distributions, including Red Hat OpenShift, which uses [Source-To-Image](https://github.com/openshift/source-to-image) instead, which was unaffected by this vulnerability.

This type of vulnerability is actually quite an old chestnut, though its appearance here is quite unique. An older example of this “if user is using X, system is vulnerable” comes from ancient UNIX systems: On a mid-’90s version of AIX (IBM’s UNIX), if root was reading mail in the Elm email client, any user could also access and read anything in root’s mail directory. Unfortunately, IBM learned that lesson in 1996.

## Old Vulns Never Die
It just goes to show that old vulnerability patterns never die, they just manifest in new implementations, languages and environments. This is why security tools need to be natively integrated with the platform, providing correlation between processes and Kubernetes objects so that Kubernetes administrators and application developers can make sense of the security findings. It’s not enough to simply collect the hordes of processes, software and container images below.

And yet, great security is tantamount to a great development environment for your teams. If your programmers don’t have to worry about major security concerns within the software they are using, because that software is monitored, measured and blessed; then those developers can focus on solving the problem in front of them instead of refactoring to remove a vulnerable bit of code every few weeks.

*Learn more about Red Hat Advanced Cluster Security for Kubernetes.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)