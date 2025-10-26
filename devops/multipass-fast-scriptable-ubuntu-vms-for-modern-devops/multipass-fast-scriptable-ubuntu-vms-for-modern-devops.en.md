Canonical’s Multipass is a versatile tool for launching and managing lightweight Ubuntu virtual machines (VMs) across platforms, including macOS, Windows and Linux.

Designed for developers and operations teams, [Multipass](https://canonical.com/multipass) streamlines local VM provisioning, offering near-instant Ubuntu instances from the command line or via scripts. Its focus on ease of use, automation and minimal friction makes it a solid candidate for rapid development, cloud native testing and [continuous integration](https://thenewstack.io/ci-cd/) (CI) workflows.

## Architectural Overview of Multipass

Multipass is built on a client-server architecture. This design separates the user-facing command line interface (CLI) from the system services that handle the life cycle of VM instances. The Multipass client interacts with the Multipass daemon, a privileged background service responsible for VM orchestration and resource management. This separation not only enhances security but also allows for scripting and integration into automation workflows without direct system intervention.

[![](https://cdn.thenewstack.io/media/2025/10/6e984517-screenshot-2025-10-17-at-10.44.08%E2%80%AFam-1024x717.png)](https://cdn.thenewstack.io/media/2025/10/6e984517-screenshot-2025-10-17-at-10.44.08%E2%80%AFam-1024x717.png)

The daemon leverages the underlying hypervisor provided by the host operating system. On macOS, Multipass uses Apple’s [Hypervisor Framework](https://developer.apple.com/documentation/hypervisor), which ensures native performance and security isolation. On Windows, it utilizes [Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v) if available, or falls back to [VirtualBox](https://www.virtualbox.org/) if required. Linux hosts commonly rely on [KVM](https://www.redhat.com/en/topics/virtualization/what-is-KVM) for hardware-accelerated virtualization. Multipass automatically detects available backends and selects the most optimal one, but users can also override the default choice using configuration options.

Storage management in Multipass employs images that are thin-provisioned and optimized for minimal on-disk footprint. Each instance gets a default home and ephemeral root file system, with the option to mount arbitrary host directories inside the VM. Networking is abstracted to present instances with connectivity that mirrors cloud environments, supporting DNS resolution and outbound traffic by default. Advanced users can configure custom bridges or additional NICs for more complex scenarios.

Multipass handles images by default via Canonical’s official streamlined [Ubuntu releases](https://releases.ubuntu.com/). These minimal images are [frequently updated](https://thenewstack.io/ubuntu-25-10-replaces-sudo-with-a-rust-based-equivalent/) and optimized for size and security. Multipass maintains a local cache of images to reduce download times for subsequent launches. Users can also launch custom images or [Snap packages](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/), extending the architecture for specialized use cases, including cross-distro development or lightweight, container-like VM deployments.

## Getting Started With Multipass

Installing Multipass is straightforward on all major operating systems. Downloads and instructions are available from the project’s website and documentation. On macOS, Multipass can be installed using Homebrew or by downloading a signed DMG package. For Windows, MSI installers support seamless setup. On Linux, Multipass is distributed as a Snap package, ensuring automatic updates and sandboxed execution.

[![](https://cdn.thenewstack.io/media/2025/10/8b72d936-carbon-1024x806.png)](https://cdn.thenewstack.io/media/2025/10/8b72d936-carbon-1024x806.png)

Once installed, starting an Ubuntu VM takes a single terminal command. Running `multipass launch` downloads the latest Ubuntu image if needed and provisions a new instance. By default, the instance has 1GB of RAM, a single CPU core and 5GB of disk space, but these resources can be easily customized at launch. For example, specifying `multipass launch --name dev --cpus 2 --memory 4G --disk 20G` sets up a development VM with increased resources.

[![](https://cdn.thenewstack.io/media/2025/10/a843dff4-carbon-1-1024x223.png)](https://cdn.thenewstack.io/media/2025/10/a843dff4-carbon-1-1024x223.png)

Accessing the shell of an instance is done using `multipass shell`, which drops the user into a fully functional Ubuntu environment. The CLI makes it simple to manage life cycle actions, such as starting, stopping, suspending or deleting instances. Users can list all running and stopped instances with `multipass list`, inspect detailed configuration using `multipass info` and transfer files with `multipass transfer`.

Multipass supports mounting host directories into instances via the `multipass mount` command, simplifying workflows that need to share source code, or build artifacts or data files across host and guest. File changes are instantly available without network overhead, making it ideal for local development where live synchronization is needed. Networking is transparent, allowing SSH, HTTP servers and other networked services to work as if running natively.

Scripting Multipass is another advantage. It integrates into CI pipelines, custom development toolchains or system automation scripts. YAML-based cloud-init can be supplied at launch for hands-off provisioning, package installation and configuration. Multipass instances are ephemeral by design, allowing them to be spun up, used and destroyed in seconds.

Updating Multipass itself or the Ubuntu images it uses is handled automatically on Snap-enabled Linux setups; macOS and Windows users receive update notifications. Instance images are updated on request or upon first launch.

Multipass also interoperates with public clouds thanks to its similar instance management semantics. Development and test workloads constructed using Multipass locally can be readily migrated or adapted to run on cloud-based Ubuntu servers without significant changes, supporting hybrid and multicloud workflows.

## Comparison of Multipass With VirtualBox

A key decision for users wanting local VM management is whether to choose Multipass or VirtualBox. Both provide VM capabilities but differ in philosophy, feature set and use case optimization.

Multipass is primarily optimized for streamlined Ubuntu VM provisioning and ephemeral environments. It is engineered for minimal friction, rapid instance startup and a cloud-like workflow. Automation and scripting are first-class, thanks to its modern CLI and support for native OS integration. Multipass does not provide extensive graphical interfaces or support for running arbitrary guest operating systems outside its Ubuntu base images, although some customization is possible.

VirtualBox offers a more traditional virtualization approach. It supports hosting a wide variety of operating systems, including Windows, Linux variants, BSD, macOS and others. VirtualBox provides robust graphical controls, including a GUI for managing VM settings, snapshots, network devices and storage. It excels in scenarios where fine-grained configuration and cross-OS testing are necessary.

The architecture of [VirtualBox](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/) is monolithic, integrating the entire stack within its own service and application layers. VM performance with VirtualBox is generally excellent, though sometimes slightly lower than native hypervisor integrations like Hyper-V or macOS Hypervisor Framework used by Multipass. Advanced VirtualBox features include bridged or host-only networking, USB hardware pass-through and detailed VM device emulation.

Multipass stands out for developer productivity and automation. Its lightweight images, fast provisioning and cloud-init compatibility make it ideal for CI/CD systems, ephemeral test beds, microservices prototyping and cloud native workflows. The streamlined approach comes at the cost of flexibility: Multipass is not a general-purpose VM hypervisor, but a specialized tool with its sights set on Ubuntu-first development experiences.

In contrast, VirtualBox is better suited for scenarios demanding graphical VM interaction, non-Ubuntu guest OSes, persistent environments or legacy network and hardware integration. It is also a natural choice for end users who need to manually manage and interact with desktops inside VMs, such as for legacy application compatibility, OS evaluation or classroom instruction.

## Conclusion

Multipass offers a developer-first approach to VM orchestration, optimized for Ubuntu and cloud native scenarios on modern desktops. Its architecture leverages OS-native hypervisors to deliver high performance, security and low overhead, while exposing a powerful yet simple CLI for instant VM management, scripting and automation. Although Multipass does not replace full-featured general VM solutions like VirtualBox, it outshines them for scenarios focused on Ubuntu development, automation and ephemeral workloads. The choice between Multipass and VirtualBox depends on whether streamlined, code-driven Ubuntu VM management or graphical, multi-OS versatility is the priority for your workflow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)