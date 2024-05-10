# Red Hat Rethinks the Linux Distro for the Container Age
![Featued image for: Red Hat Rethinks the Linux Distro for the Container Age](https://cdn.thenewstack.io/media/2024/05/0a999618-denver-bear-1024x658.jpg)
DENVER — Just as you use containers to quickly launch applications,
[ Red Hat](https://www.openshift.com/try?utm_content=inline+mention) wants to make it just as easy to boot up entire Linux-based operating systems.
The company has made its flagship Linux distribution
[ Red Hat Enterprise Linux ](https://thenewstack.io/red-hat-enterprise-linux-8-1-released-with-live-kernel-patching/) (RHEL) bootable as a container image. In other words, all the operating code typically left out of a container, such as kernel-firmware, will be included in this image.
The company announced these initiatives during its annual user conference,
[Red Hat Summit](https://www.redhat.com/en/summit), being held this week in Denver.
“This is something the entire industry needs,” explained Colin Walters, a Red Hat senior principal software engineer, in a session at the summit. “The more you’re using cloud native tooling, instead of building a unique bin for infrastructure, the [more] you’re leveraging that open source maintainership and shared ownership.”
The approach is different from the company’s typical package mode, where the final copy of a new RHEL release is issued as a stand-alone package to be installed on a server or virtual machine, which then is modified by the admin through customization for specific workloads.
This package mode,
[ long a tradition in the Linux distribution community](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/), is increasingly different from how applications are managed these days, through containers.
The idea is that “lessons learned on the container side that we can bring over to the OS world so that these two worlds aren’t managed completely separately,” said
[Ben Breard](https://www.redhat.com/en/authors/ben-breard), a Red Hat senior principal marketing manager, in a Red Hat press conference ![](https://cdn.thenewstack.io/media/2024/05/983df5d9-red_hat-waters-02-1024x576.jpg)
Goals for a container-based Linux OS, from Colin Walters’ presentation.
## A Wider Workload
The move is one to make RHEL more flexible for a wider variety of workloads. The RHEL gold image is only applicable in some environments. Many environments, such as those at the edge or virtual desktop environments, end up needing to customize different bits.
Containerization would help streamline updates to these custom environments in a major way. And make testing and rollback far easier, the Red Hats claim.
Instead of making changes to the operating system after it has already been installed, the admin can configure the operating system at build time.
[GitOps](https://thenewstack.io/gitops-git-push-all-the-things/) or [continuous integration/continuous deployment](https://thenewstack.io/ci-cd/) workflows already familiar to developers can be standard procedures for maintaining a fleet of Linux servers running across different environments.
All the cloud native tools, in fact, are put into service for maintaining operating systems.
## Not Just for Ephemeral Workloads
This is not the first attempt at building an operating system in a container:
[RancherOS](https://thenewstack.io/rancher-labs-releases-rancheros-general-availability/), [Flatcar Linux](https://thenewstack.io/tutorial-install-flatcar-container-linux-on-remote-bare-metal-servers/), [Talos](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/), and [CoreOS](https://thenewstack.io/coreos-open-cloud-services/) ( [purchased by Red Hat in 2018](https://thenewstack.io/red-hat-will-acquire-coreos-greater-kubernetes-presence/)), among others, have all tackled this approach.
New to this release is a new bit of software called
[boot.c](https://github.com/containers/bootc), which layers components of a bootable host system using the same [Open Container Initiative](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) (OCI) standards that Docker builds an application container through multiple layers.
The release “includes a kernel-firmware and all the things that historically you’re supposed to leave out of containers,” Breard said. As a result, “we can now manage version and deploy the full operating system using the standard container tools that pretty much everybody has in-house.”
The work actually came out of the CoreOS features that were
[merged in OpenShift](https://thenewstack.io/coreos-says-red-hat-will-help-introduce-openshift-to-operators/). In 2020, Red Hat [renamed](https://www.redhat.com/en/technologies/cloud-computing/openshift/what-was-coreos) the CoreOS Container Linux OS as, somewhat confusingly, [Fedora CoreOS](https://fedoraproject.org/coreos/), “the container optimized OS.”
Unlike earlier container image-based systems, Red Hat’s will not be entirely ephemeral. Here the user data will be retained data in the
* /etc* directory while updating other components as needed.
This approach would be most valuable for systems where some system and application data must be retained, which Walters explained in most cases.
![](https://cdn.thenewstack.io/media/2024/05/983df5d9-red_hat-waters-02-1024x576.jpg)
Goals for a container-based Linux OS, from Colin Walters’ presentation.
*Disclosure: Red Hat paid for travel expenses for the reporter to attend this conference.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)