# Canonical Offers LTS ‘Distroless’ Containerized Apps for K8s
![Featued image for: Canonical Offers LTS ‘Distroless’ Containerized Apps for K8s](https://cdn.thenewstack.io/media/2024/06/6123a22b-clay-banks-pho_ila8dgg-unsplash-1024x784.jpg)
Canonical is expanding Long Term Support (LTS) beyond its flagship [Ubuntu Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) distribution, promising [to provide](https://canonical.com/blog/canonical-offers-12-year-lts-for-any-open-source-docker-image) 12-year security support for any [Docker](https://www.docker.com/?utm_content=inline+mention)-packaged open source software.

These “distroless” containers would be ideal for Kubernetes environments, where they can be packed together in a pod for maximum computational efficiency.

Canonical will certify the LTS containers to run on its own [MicroK8s](https://thenewstack.io/microk8s-and-portainer-is-the-easiest-way-to-deploy-an-application-on-kubernetes/) and [Charmed Kubernetes](https://ubuntu.com/kubernetes/charmed-k8s) platforms, naturally.

But the LTS packages will also be certified by Canonical to run on other major production-grade Kubernetes environments, such as [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) OpenShift (by way of [Red Hat Enterprise Linux](https://thenewstack.io/red-hats-new-linux-distro-brings-centos-closer-to-rhel/)), and [VMware](https://tanzu.vmware.com?utm_content=inline+mention)‘s K8s platforms: [Tanzu Kubernetes Grid](https://tanzu.vmware.com/kubernetes-grid) and [vSphere with Kubernetes](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/vsphere/vmw-vsphere7-solution-brochure.pdf).

On public clouds, Canonical will officially certify containers to run on [Azure](https://news.microsoft.com/?utm_content=inline+mention), [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), [IBM](https://www.ibm.com?utm_content=inline+mention) and [Oracle ](https://developer.oracle.com/?utm_content=inline+mention).

The images will be built on the standardized[ Open Container Initiative](https://thenewstack.io/open-container-initiative-creates-a-distribution-specification-for-registries/) (OCI) format, so the LTS containers should run in any OCI-compliant runtime environment.

## Canonical Containerizes Deb Packages
To date, Canonical uses [deb packaging format](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html) to put apps on its own Linux distribution, [Ubuntu](https://thenewstack.io/enable-automatic-updates-for-ubuntu-server/). Thus far, Ubuntu and the community have produced over 36,700 deb packages. ‘Deb’ comes from [Debian](https://thenewstack.io/build-a-debian-deb-file-from-your-projects-source/), which is the stock distribution Canonical uses to build its own Ubuntu distribution.

Many of these applications packaged in deb also have been containerized, using [Docker and similar tools](https://thenewstack.io/docker-rolls-out-3-tools-to-speed-and-ease-development/).

In this new program, Canonical will maintain 12 years of security maintenance for any open source application that has been containerized in the OCI format (such as Docker).

Many open source applications are already available, on sites such as [Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/). For the service, Canonical will even take requests to “LTS” your favorite open source application. It will analyze your app dependency tree and bring those packages under LTS maintenance that aren’t already covered by Ubuntu Pro.

To support a proprietary application, customers can request an LTS base image with all the needed [open source dependencies](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/).

Those with Ubuntu Pro subscriptions, which are [free for the first five instances](https://ubuntu.com/pricing/pro), can use the supported images, which will be updated with security fixes when needed. The same pricing structure will also be used for running “Everything LTS” containers on other certified platforms — VMware, RHEL and the public cloud hosts.

The move will also provide the company’s own Ubuntu Pro distribution with thousands of new open source upstream components, including the many new applications springing up for running generative AI applications, many of which have not yet been packaged in deb.

## ‘Distroless’ Containers
Regular containers, such as those packaged in Docker, can usually run across any Linux distribution that supports Docker. These traditional containers still include some operating system (OS) utilities for support, such as the [Secure Shell](https://thenewstack.io/port-knocking-ubuntu-servers-or-containers-for-more-secure-ssh/) (SSH), which allows users to log in to the container.

The distroless containers, however, include only the files, or binaries, specifically needed to run an application, reducing the size of the container and the surface area an attacker can use to exploit the software. Unnecessary packages and metadata are removed.

With distroless, containers don’t have SSH. No one can log in with “root” access. The containerized apps don’t have package managers; they can’t be updated. They are, in industry parlance, truly “immutable.” When they need to be updated, they are replaced by a new copy.

Also gone: install scripts, documentation, header files, info about other dependencies. Instead, such external information is kept in YAML files, called slices, alongside the containers. themselves.

Building a container by scratch can be tricky. Canonical uses the [Debian Chisel](https://github.com/canonical/chisel) tool for building distroless containers for the various platforms.


## Benefits of Going ‘Distroless’
A major advantage of LTS is that the user does not have to worry about keeping their apps updated with the latest security fixes.

The company will patch any applications where a [CVE-registered vulnerability](https://thenewstack.io/five-myths-about-cves/) is found. CVE patching is required for many government and industry security mandates, including FIPS, FedRAMP, EU Cyber Resilience Act (CRA), FCC U.S. Cyber Trust Mark and DISA-STIG.

In addition to security, there are a number of secondary benefits to distroless containers. They can be downloaded more quickly, and they spin up more quickly. You can pack more of them into a single server.

Overall Canonical has estimated that distroless containers can offer a general overall performance boost of 20% to 25%. And you can still use existing container build systems to update your applications as well.

Along with Microsoft, Canonical has already created a set of [distroless containers for .NET users](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/).

With this method, .Net containers were trimmed by about 100MB, for a size of 6MB, compressed, the companies have estimated.

## Bootable Containers from Red Hat
Canonical is not the only company rethinking how to do Linux distributions for [cloud native computing](https://thenewstack.io/cloud-native/). Earlier this year, Red Hat made its flagship Linux distribution RHEL bootable as a container image. All the operating code typically left out of a container, such as kernel-firmware, will be included in this image.

At the Red Hat Summit in May, Red Hat technicians demonstrated how to boot RHEL from the [Podman container management console](https://thenewstack.io/deploy-a-pod-on-centos-with-podman/) or be spun up under OpenShift, and even how to burn ISOs from the images, so they can be spun up on any machine.

Though Red Hat’s approach differs from Canonical’s, both are hammering away at the same idea: How to clear away the legacy operating system clutter for better performance in cloud environs.

Red Hat wanted to use the best technologies on “on the container side that we can bring over to the OS world so that these two worlds aren’t managed completely separately,” said [Ben Breard](https://www.redhat.com/en/authors/ben-breard), a Red Hat senior principal marketing manager, in a [Red Hat press conference at the Summit](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)