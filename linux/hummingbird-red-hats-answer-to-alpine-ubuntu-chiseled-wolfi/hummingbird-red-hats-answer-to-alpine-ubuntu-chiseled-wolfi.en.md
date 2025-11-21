Linux powerhouse [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) has unveiled [Project Hummingbird](https://gitlab.com/redhat/hummingbird/containers), a new initiative designed to accelerate cloud native development by delivering micro-sized container images for enterprise environments.

Wait, some of you are saying, didn’t [Red Hat acquire CoreOS](https://thenewstack.io/say-goodbye-to-coreos/) with its minimal Linux distribution, Container Linux, back in 2018? And, wasn’t Container Linux explicitly designed for containerized workloads and automated updates? Yes, it was.

## Flatcar Container Linux: Designed for Container Workloads

To continue, Container Linux morphed into [Flatcar Container Linux](https://thenewstack.io/flatcar-container-linux-moves-beyond-coreos-roots-with-commercial-editions/) and, in 2025, it’s now an active [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) [project](https://thenewstack.io/flatcar-container-linux-hitches-a-ride-with-the-cncf/). So, what’s new here?

Here’s where each one plays according to [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) and the [CNCF](https://cncf.io/?utm_content=inline+mention)‘s documentation.

[Flatcar Container Linux](https://flatcar-linux.org/) is a full, immutable Linux operating system designed to run container workloads directly on bare metal, virtual machines or cloud instances. It provides automatic OS updates, built-in container runtimes and emphasizes system immutability, making it ideal for clusters and edge deployments.

It’s designed to be the host OS for orchestrating and running containers at scale, especially in Kubernetes or managed [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) Cloud Infrastructure (OCI) environments, where administrators require robust, reproducible infrastructure.

## Introducing Project Hummingbird: Micro-Sized Container Images

Project Hummingbird delivers micro-sized, production-ready container images focused on minimalism, supply chain security and compliance for enterprise customers. Hummingbird’s images are not a full Linux distro but highly curated base images designed for containers, with a zero-common vulnerabilities and exposures (CVE) at release policy and comprehensive software bills of materials SBOMs) included by default.

It’s optimized for CI/CD pipelines, software supply chain requirements, and compliance-driven use cases where ultra-small image size and transparency are essential.

Got all that? Good.

Drawing inspiration from modern, lean Linux distributions such as [Alpine Linux](https://www.alpinelinux.org/), [Ubuntu Chiseled Images](https://ubuntu.com/containers/chiseled), and [Chainguard Wolfi](https://edu.chainguard.dev/open-source/wolfi/overview/), Project Hummingbird aims to help organizations speed up application delivery while maintaining robust supply chain security and compliance standards.

## Taking Inspiration from Alpine, Ubuntu Chiseled, Wolfi

Project Hummingbird’s approach mirrors Alpine Linux’s with its [musl-libc](https://musl.libc.org/) minimalism and small attack surface in container deployments. Like Alpine and security-focused alternatives such as Wolfi, an “undistro” emphasizing supply chain integrity and granular SBOMs, Hummingbird is built for rapid security patching and minimal risk.

Ubuntu Chiseled Images provide another strong parallel: using [Canonical’s “Chisel” tool](https://github.com/canonical/chisel), these Ubuntu spins let users tailor container bases precisely, resulting in images as small as 5MB that contain only the necessary runtime dependencies.

## Key Features of Project Hummingbird for Enterprise

Project Hummingbird is now available in early access for Red Hat subscription customers as a catalog of hardened, production-ready container images. These images, built from [Fedora Linux](https://www.fedoraproject.org/) components, are stripped of non-essential packages, reducing attack surfaces and minimizing potential vulnerabilities. Notable features include:

* **Zero-CVE status**: All images are shipped free of known vulnerabilities, with thorough production testing completed beforehand to ensure stability and utility.
* **Micro-sized images**: Core languages, runtimes (like .NET, Go, Java, Node), popular databases (MariaDB, PostgreSQL), and essential web servers are available in ultra-small images to reduce integration effort and resource usage.
* **Complete SBOMs**: Every image includes a comprehensive software bill of materials, supporting compliance needs and transparent auditing.

Enterprise support: Full support will be available with Red Hat subscriptions upon general availability, with freely available, redistributable images offered in a model similar to Red Hat UBI.

As [Gunnar Hellekson](https://www.linkedin.com/in/gunnarhellekson/), Red Hat’s general manager for Red Hat Enterprise Linux (RHEL), summed up in a statement,  “Project Hummingbird is designed to remove that trade-off [between moving fast and maintaining security] by providing a minimal, trusted and transparent zero-CVE foundation for building cloud native applications.

“This limits vulnerabilities so development and IT security teams have a clear, direct path to business value with speed, agility, security and peace of mind.”

## Red Hat’s Vision for Secure Cloud Native Enterprise Linux

Project Hummingbird attempts to position Red Hat as a major player in the next evolution of secure, cloud native enterprise Linux.

With its zero-CVE promise, production-ready minimal images, and deep integration with enterprise workflows, the initiative offers a compelling alternative for organizations adopting containerized workloads amid rising supply chain threats.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)