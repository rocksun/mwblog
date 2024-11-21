# Red Hat Enterprise Linux 9.5 Arrives With Enhanced AI Support and Automation
![Featued image for: Red Hat Enterprise Linux 9.5 Arrives With Enhanced AI Support and Automation](https://cdn.thenewstack.io/media/2024/11/c57d7e8e-redhat-1024x683.png)
Once upon a time, a new business Linux release was all about, well, Linux. The times have changed. There’s no better example than [Red Hat](https://www.openshift.com/try?utm_content=inline+mention). The leading Linux distribution, while still making Linux job one, has also [focused on cloud computing](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/). Now, with the release of [Red Hat Enterprise Linux (RHEL) 9.5](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/9.5_release_notes/index), it’s adding [artificial intelligence](https://thenewstack.io/ai/) (AI) to its portfolio.

Why? According to a new Red Hat-sponsored IDC report, [The Business Value of Standardizing on Red Hat Enterprise Linux](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fwww.redhat.com%2Fen%2Fresources%2Fidc-executive-summary-standardizing-analyst-material&esheet=54152568&newsitemid=20241113036427&lan=en-US&anchor=The+Business+Value+of+Standardizing+on+Red+Hat+Enterprise+Linux&index=1&md5=0bea3060b81f685e79f37d82d3edb93a&_gl=1*1xqv5kd*_gcl_au*MTkyMTc1NjE5MC4xNzMxNjA1MzMy*_ga*Mjk2NDc0MjU0LjE3MzE2MDUzMzI.*_ga_ZQWF70T3FK*MTczMjAzOTQ5Ny40LjAuMTczMjAzOTQ5Ny42MC4wLjA.), “Organizations continue to find themselves at odds with striking a balance between maintaining their Linux operating system environments and the workloads that they support, all while being stretched for time and resources.”

With RHEL 9.5, “RHEL standardization increased the agility of IT infrastructure administration management teams by consolidating OSs, automating highly manual tasks such as scaling and provisioning, and decreasing the complexity of deployments. As a result, infrastructure teams spent 26% more time on business and infrastructure innovation.”

Red Hat’s not just talking the talk. It’s walking the walk. [Red Hat actually uses AI to make work easier for users](https://www.zdnet.com/article/how-red-hat-is-embracing-ai-to-make-sysadmin-lives-easier/). For example, Red Hat’s [Red Hat Lightspeed](https://www.redhat.com/en/technologies/management/ansible/ansible-lightspeed) is a generative AI service designed to help automate sysadmin jobs. Lightspeed uses [natural language processing](https://www.ibm.com/topics/natural-language-processing) (NLP) to turn prompts into code. It’s been primarily used with the [Ansible](https://www.ansible.com/) DevOps. This makes automating system administration jobs using Ansible Playbooks easier than ever.

These features are now being baked into RHEL 9.5. The new RHEL system roles are a selection of [Ansible Content Collections](https://www.redhat.com/en/technologies/management/ansible/content-collections). These automate everyday administrative tasks to help you with more consistent configurations and workflows at scale.

## The Complexity of Enterprise IT
Gunnar Hellekson, RHEL’s general manager, emphasized the growing complexity in enterprise IT, especially with the rise of AI. In a statement, Hellekson said, “Complexity in enterprise IT, from the applications we build to the environments in which they run, isn’t going away. Rather, it’s growing exponentially, especially with the dynamics of new technologies like AI.”

For example, Red Hat now has a dedicated AI program, [Red Hat Enterprise Linux AI 1.2](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai). RHEL AI 1.2 is designed to help companies build their own development, testing, and deployment of large language models (LLMs).

RHEL 9.5 has also introduced enhanced confidential computing capabilities to protect sensitive AI workloads. This feature enables organizations to process large datasets while adhering to data compliance regulations. As regulations encircle AI, this is becoming ever more important.

Security continues to be top-of-mind for Red Hat outside of AI. Pre-hardened image configurations are now available to help companies build security into development processes earlier.

In addition, the OpenSSL TLS toolkit has been upgraded to version 3.2.2. This version supports certificate compression extension, RFC 8879, and Brainpool curves, which have been added to the TLS 1.3 protocol, RFC 8734. The National Security System (NSS) cryptographic toolkit packages have been rebased to upstream version 3.101. This provides many bug fixes and enhancements.

## New System Roles
RHEL 9.5 has added several new system roles. The one I think matters the most- and I’m sure most system administrators will agree with- is that it includes a new role for [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/), Linux’s master sysadmin command. This safely automates the configuration and use of sudo at scale. According to the Red Hat press release, “This enables everyday users to run commands typically reserved for admins, with the proper guardrails to manage rules accordingly.”

Under the hood, the latest RHEL is running the Linux 5.14.0-503.11.1 kernel. And, of course, as always, RHEL 9.5 has the latest application developer tools, languages, and databases to fuel innovative applications. This includes PG Vector for PostgreSQL, new versions of node.js, GCC toolset, Rust toolset, and LLVM toolset.

The release introduces new file management capabilities in the Web Console. This enables sysadmins to perform routine file management tasks without using the command line. This addition simplifies system administration and enables organizations to standardize scale deployment.

Red Hat Enterprise Linux 9.5 is now generally available to existing customers with an active RHEL subscription through the [Red Hat Customer Portal](https://access.redhat.com/). For those interested in trying the latest release, a 60-day evaluation edition is available for download. As always, there’s also a [free developer version of RHEL](https://developers.redhat.com/products/rhel/download#getredhatenterpriselinux7163).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)