# Red Hat Enterprise Linux 10: An AI-Driven, Quantum-Ready Platform
![Featued image for: Red Hat Enterprise Linux 10: An AI-Driven, Quantum-Ready Platform](https://cdn.thenewstack.io/media/2025/05/7a5a6ecd-getty-images-el0zyfxt1gi-unsplash-redhat-1024x684.jpg)
BOSTON — At its annual [Red Hat Summit](https://www.redhat.com/en/summit), [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) launched [Red Hat Enterprise Linux 10 (RHEL 10)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), positioning the latest iteration of its flagship operating system as the foundation for its next generation of hybrid cloud and AI-powered enterprise IT.

Like almost every company today, Red Hat CEO [Matt Hicks](https://www.linkedin.com/in/mhicks-redhat) praised AI for what will bring to its programs. Unlike, say, AI-enabled pencil sharpeners, Red Hat is actually delivering useful functionality with its AI offerings.

As Hicks said, “AI will make Linux admin life better.” How? With the introduction of [Red Hat Enterprise Linux Lightspeed](https://www.redhat.com/en/about/press-releases/red-hat-infuses-generative-ai-across-hybrid-cloud-portfolio-red-hat-lightspeed). This new feature integrates generative AI (GenAI) directly into the platform, offering context-aware guidance and actionable recommendations through a natural language interface.

## Lightspeed, a New Shell
When Red Hat says “directly,” it means right into the [Linux shell](https://thenewstack.io/learning-linux-start-here/) itself. With Lightspeed, sysadmins can ask for help with shell commands and scripts. So, for example, if you want to finally perfect an age-old backup or restore script, Lightspeed can work alongside you to clean it up for once and for all. Or, say you’re a new sysadmin, you can also use the optional AI-powered command line assistant to find the specific command and its appropriate syntax for your particular problem.

Red Hat has done this because, according to a Red Hat-sponsored IDC study, [The business value of standardizing on Red Hat Enterprise Linux](https://www.redhat.com/en/resources/idc-business-value-of-standardizing-analyst-material), “organizations [are] struggling to hire the Linux skill sets they need to operate and support their expanding fleet of distributions, which opens them up to further risk around security, compliance, and application downtime.”

Beyond the marriage of AI and Linux administration, RHEL 10 also introduces [Federal Information Processing Standards (FIPS) compliance for post-quantum cryptography.](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) RHEL is the first Linux distro to incorporate quantum-resistant algorithms. The point is that Red Hat wants to enable you to protect organizations from emerging threats such as “[harvest now, decrypt later](https://www.keyfactor.com/blog/harvest-now-decrypt-later-a-new-form-of-attack/)” attacks and help customers meet evolving regulatory requirements. In short, RHEL is the first post-quantum cryptographic Linux.

## Immutable Linux
With RHEL 10, Red Hat introduces “image mode.” This is essentially an [immutable Linux](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/). Image model has been a long time coming. With this new model, Red Hat delivers RHEL as a bootable container image, which you work with using container-native tools and workflows. In it, the core programs and filesystems are read-only at runtime. Changes to the OS require building and deploying a new image, followed by a reboot.

While immutable Linux distros, such as [Fedora CoreOS](https://fedoraproject.org/coreos/), are common, RHEL is the first major server Linux operating system to move to the immutable model. Grey-haired Linux admins who cut their teeth on shell scripts and [Cockpit](https://cockpit-project.org/) may not be crazy about this move. Red Hat assures its users that this approach unifies the build, deployment and management of both operating systems and applications. This shift minimizes configuration drift and enables IT teams to manage their entire infrastructure with consistent tools and workflows, including containerized apps and their underlying platforms.

[Ashesh Badani](https://www.linkedin.com/in/asheshbadani/), Red Hat’s senior VP and chief product officer, explained in an interview that, “patching is something that every sysadmin does and issues always crop up, which lead to deviations from the desired system, and that’s when we end up with drift. Being able to manage that drift is a huge pain point for our customers. So being able to introduce image mode for RHEL is really being that concept of containers, and being able to manage an operating system as a container is a huge boost.”
Salesforce software architect [Anish Bhatt](https://www.linkedin.com/in/anishbhatt/) praised the new image mode: “It has brought stability to our environments, reducing configuration drift and enabling a more consistent deployment experience. Image mode is a meaningful step towards simplifying cloud-native application development and IT operations in a single pipeline.”

To help both old and new RHEL admins make the move, the latest version of [Red Hat Insights](https://www.redhat.com/en/technologies/management/insights), the platform’s analytics engine, now offers image builder package recommendations and enhanced planning tools. Insights helps you to make more informed decisions at build time.

Under the hood, RHEL uses the Linux kernel version 6.11.0 as its baseline. This is a big jump from RHEL 9’s 5.14 kernel. For those wanting a still newer kernel, CentOS Stream is now based on Linux 6.12.

## Red Hat Security
There are some other changes that admins must be aware of. The biggest to my mind is that [newly created users will have administrative privileges by default](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10-beta/html/10.0_beta_release_notes/overview#overview-major-changes). No! The very idea makes me twitch. Fortunately, you can turn this option off.

In a related change, with the new [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) RHEL system role, you can consistently manage sudo configuration at scale across your RHEL systems. That I’m fine with.

On the security front, RHEL 10 [OpenSSL TLS toolkit](https://github.com/openssl/openssl) introduces creation of FIPS-compliant [Public-Key Cryptography Standards (PKCS) #12 files](https://www.globalsign.com/en/blog/what-is-a-pkcs12-file), the pkcs11-provider for using hardware tokens, and many additional improvements. Red Hat has also updated the [OpenSSH](https://www.openssh.com/) suite in version 9.8, which provides many fixes and improvements over RHEL 9’s OpenSSH 8.7. Finally, the [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) userspace release 3.7 introduces a new option for audit2allow, providing CIL output mode, Wayland support for the SELinux sandbox and other improvements.

One security change I suspect many companies will find appealing is that Red Hat is offering its customers a new way to customize support for common vulnerabilities and exposure (CVE) fixes. With the Security Select Add-On, subscribers can purchase 10 CVE fixes of their choice. So if you think there’s a security hole you find to be seriously troubling, even if no one else does, you can have Red Hat fix it for you. Red Hat believes this will be particularly useful for those in highly regulated sectors like healthcare, finance, telecommunications and government.

The RHEL Security Select Add-on will be available to customers with subscriptions that include RHEL [Extended Life Cycle Support](https://www.redhat.com/en/resources/els-datasheet) or RHEL [Extended Update Support](https://www.redhat.com/en/resources/eus-datasheet) starting Q3 CY 2025. In other words, if there’s an old, annoying CVE in an otherwise out-of-date RHEL getting on your nerves, Red Hat will fix that bug for you, too.

[Ryan Caskey](https://www.linkedin.com/in/ryan-caskey-96307a17/), IDC research manager, noted the challenge of maintaining diverse Linux environments, stating that RHEL 10 “aims to establish a robust, foundational layer for both current and future IT strategic initiatives.”
Needless to say, RHEL 10 also includes updated languages and toolkits for your developers.

The new RHEL also comes with pre-tuned, fully supported RHEL images for AWS, Google Cloud, and Microsoft Azure. RHEL is also finally fully supported on Oracle Cloud Infrastructure (OCI).

Besides the usual x86, 64-bit ARM, IBM POWER and IBM Z architectures, RHEL 10 is also available as a developer preview for the RISC-V architecture, in collaboration with SiFive, targeting early adopters of the HiFive P550 platform.

As always, RHEL 10 is now available through the Red Hat Customer Portal. Developers can access RHEL 10 at no cost via [Red Hat’s Developer programs](https://developers.redhat.com/home). So, whether you’re already a RHEL customer or just want to kick its tires, RHEL 10 is ready for you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)