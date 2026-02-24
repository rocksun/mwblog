[Red Hat](https://www.redhat.com/en) is perhaps the biggest name in enterprise Linux, but it’s also a major cloud-native player thanks to its Kubernetes distribution, [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift). What it hasn’t had, though, is a supported, enterprise build of its own open source, container-oriented desktop app… until now. The recent release of the [Red Hat build of Podman Desktop](https://developers.redhat.com/products/red-hat-build-podman-desktop) is the company’s bet that a tight integration with OpenShift and Red Hat Enterprise Linux (RHEL) will make [Podman Desktop’](https://podman-desktop.io/)s container-native workflows attractive to corporate developers. 

Podman Desktop is a popular, open source Docker‑compatible container engine. It features a graphical front end that enables developers to manage containers, images, pods, and local Kubernetes from a single UI.

## Why?

Red Hat contributed it to the Cloud Native Computing Foundation in January 2025, where it is currently a sandbox project. So if Red Hat already supports Podman, why launch this new version? According to Red Hat, customers were asking for it.

“Until now, many teams have had to rely on unsupported open source tools or alternatives that lack the service-level agreements (SLAs) required for work,” the company writes in its [announcement](https://www.redhat.com/en/blog/introducing-red-hat-build-podman-desktop-enterprise-ready-local-container-development-environments). “The Red Hat build of Podman Desktop is a vendor-backed solution that comes with official Red Hat support, providing access to security fixes, product engineers and container experts. For IT decision-makers and platform engineers, this means more predictable lifecycle management, security patching, and the ability to manage container tools across thousands of workstations from Day 1.”

What the Red Hat build of Podman Desktop brings to the table is a vendor-backed desktop application for Linux, macOS, and Windows. It includes access to Red Hat support, security fixes, and product engineering.

VIDEO

## Enterprise-ready desktop container management

Positioned as “enterprise-ready local container development,” it is currently in technical preview and available through Red Hat’s developer channels for qualified customers. Red Hat pitches the offering as a way to lower the barrier to using containers by allowing developers to build, run, and debug containers and pods without deep command-line knowledge, while still aligning with corporate platforms and policies.

Technically, this new build comes with — Surprise! — tighter coupling with OpenShift and local Kubernetes environments. This move reflects Red Hat’s broader strategy to make the laptop a faithful stand‑in for production clusters. 

From the Podman Desktop GUI, developers can group containers into pods, generate Kubernetes YAML, and deploy to local clusters such as Kind or Minikube, as well as to remote OpenShift clusters and services like [Red Hat OpenShift Local](https://developers.redhat.com/products/openshift-local) and [Developer Sandbox](https://developers.redhat.com/developer-sandbox). The Red Hat build adds curated extensions for building and testing Open Container Initiative-compliant bootable container images tied to RHEL “image mode.” 

Red Hat is also using this desktop client as a policy enforcement point for organizations that struggle to reconcile developer agility with locked-down networks. With this corporate take on Podman, administrators can define and deploy a default configuration across fleets of machines, including registry mirrors, internal registries, HTTP proxies, and custom security certificates. Managers can also lock key settings so users cannot override corporate security rules. The application also validates managed configurations at startup. This helps ensure that new proxy endpoints, certificate updates, or registry policies are enforced the next time your developers open their local environment.

While Podman Desktop has existed as an upstream project for some time, Red Hat is explicitly targeting organizations that want [Docker](https://www.docker.com/)-style workflows without relying on the full Docker toolchain. The desktop tool supports [Dockerfiles](https://docs.docker.com/build/concepts/dockerfile/) and [Docker Compos](https://docs.docker.com/compose/)e via Podman’s Docker command aliasing. This will make migrating from existing Docker-based projects and scripts easier. 

On [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), Podman is already included with subscriptions. Podman Desktop can be installed directly from the RHEL extensions repository, where it is delivered as Red Hat-signed software alongside other curated developer tools. When installed this way, Podman Desktop automatically detects the underlying Podman engine on RHEL and binds to it, providing a graphical front end that mirrors the same container stack used in production.

The supported desktop build lands amid a broader Red Hat effort to promote Podman and its ecosystem as a first-class alternative to Docker in enterprise settings. This comes after Red Hat has already donated Podman and related tools, the [Podman Container Tools](https://www.cncf.io/projects/podman-container-tools/),  such as [Buildah](https://github.com/containers/buildah), [Skopeo](https://github.com/containers/skopeo), [bootc](https://bootc-dev.github.io/), and [Composefs](https://github.com/composefs/composefs), to the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/). This frames the Podman stack as a community-governed counterpart to proprietary container tooling while keeping a supported path for customers. 

That said, Red Hat is late to the commercially supported container developer environment market. [Docker Desktop](https://www.docker.com/products/docker-desktop/), [Rancher Desktop](https://rancherdesktop.io/), and [Portainer Business Edition](https://www.portainer.io/blog/portainer-community-edition-ce-vs-portainer-business-edition-be-whats-the-difference) have been available for years.  On the other hand, transforming Podman into a managed, policy-aware workstation environment that fits into OpenShift‑centric pipelines strikes me as a very attractive option for businesses built on the Red Hat software stack. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)