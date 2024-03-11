![](https://www.siderolabs.com/wp-content/uploads/2024/03/12-binaries-banner-1-1024x538.png)
Linux is a core component of your Kubernetes cluster. The distribution you choose will have a big impact on how quickly you can create a cluster, the stability of your workloads, and how much maintenance you’ll need to perform.
When creating a version of Linux for containers or Kubernetes, for many companies and distributions the common practice is to start with a general-purpose Linux and strip away things you don’t need. This results in a smaller footprint variation of the main distribution—e.g.
[Ubuntu minimal](https://wiki.ubuntu.com/Minimal)—but it always starts from a big, general purpose Linux and tries to make it smaller.
Talos Linux takes the opposite approach. What if the distribution only had to run Kubernetes? What is the minimal set of tooling and executables needed?
There are
**12 unique binaries** in /bin and /sbin in Talos 1.7.0. This greatly reduces the size of installation, the maintenance needed for the operating system, and the possible security vulnerabilities of the system.
For reference here are some other popular distributions and how many binaries they include by default. This also counts executables that are symlinked or hard linked to another file (e.g.
lvm is often symlinked multiple times for
lvs and
vgs).
|Talos Linux
|29
|Ubuntu Server 22.04
|2780
|Amazon Linux 2
|1382
|Flatcar Container Linux
|2391
All distros were set up with default installation options. No additional packages were installed and binaries were counted with:
ls -1 $(echo $PATH | tr ':' '\n') | wc -l
Talos doesn’t provide a shell,
ls,
tr, or
wc. Files were counted via the API and we didn’t count directories:
talosctl list -n $NODE_IP /sbin | wc -l
talosctl list -n $NODE_IP /bin | wc -l
With only 12 unique files on the system we can tell you what each one does.
## /sbin/init
The init binary is one of the biggest strengths of Talos Linux. Talos doesn’t ship with a general purpose init system like systemd. Talos’ init system is purpose built for running the Kubelet and a container runtime. The init system exposes a declarative API which is how the system is configured and maintained.
The init binary is
[called machined](https://github.com/siderolabs/talos/blob/main/internal/app/machined/main.go) and is written in go. It’s less than 400 lines of code and can be understood by a go developer in less than a day. As [opposed to systemd](https://github.com/systemd/systemd/blob/main/src/core/main.c) which is over 3000 lines of C code I’ll never comprehend.
The
/sbin/init binary is hard linked to
/sbin/dashboard,
/sbin/poweroff,
/sbin/shutdown, and
/sbin/wrapperd. While this technically is 5 files, it’s a single file hard linked 4 times to provide convenience commands.
The dashboard is used for providing local and remote information about the node. You can see an overview of how it works on YouTube.
The binaries
poweroff and
shutdown are commands to cleanly shut down the node. These are used by the kernel and external tools, but Talos uses the system API to shutdown.
The
[wrapperd](https://github.com/siderolabs/talos/blob/main/internal/app/wrapperd/main.go) binary is used during init to fork processes with reduced privledges. Because a child process will inherit a lot from the parent process wrapperd is used to remove kernel capabilities like CAP_SYSADMIN.
All of the other binaries on the system are included from other packages we build from source. You can see how they get built
[from GitHub](https://github.com/siderolabs/pkgs) and we will review each binary below.
## /bin/containerd*
This is the container runtime that ships with Talos. It is commonly used with Kubernetes clusters and is the default container runtime option for the majority of providers.
This also includes
/bin/containerd-shim-runc-v2 and
/bin/containerd-shim. Both of these shims provide the same function (executing a container under
runc) but
containerd-shim was originally used with docker and
containerd-shim-runc-v2 is used from containerd.
## /bin/runc
This is the true
[parent process of your containers](https://github.com/opencontainers/runc). It is daemonless so the containerd service can restart if needed without stopping all your containers.
## /sbin/modprobe
The command
[modprobe](https://linux.die.net/man/8/modprobe) is for managing kernel modules to add or remove functionality from your kernel. This is often for adding support for special hardware (e.g. GPUs) but is also used for additional kernel tooling.
Talos doesn’t use modprob directly but some modules require the binary to load other modules. You can add kernel modules to Talos via
[system extensions](https://www.talos.dev/latest/talos-guides/configuration/system-extensions/) and use pre-built extensions from the [Image Factory](https://www.talos.dev/latest/learn-more/image-factory/).
## /sbin/lvm
The
lvm binary is used for managing logical volumes in Linux. This is provided for services that run in Kubernetes that may need or expect a logical volume to be present on the host (e.g.
[rook](https://rook.io/docs/rook/latest-release/Getting-Started/Prerequisites/prerequisites/#lvm-package)).
## /sbin/dmsetup
This is used for managing logical volumes that use the device-mapper driver. It’s similar to
lvs commands but a separate binary for more complex disk configuration.
## /sbin/udevd
The udevd daemon takes kernel messages and passes the messages to other systems to read the messages. It can be configured as part of the
[Talos machine config](https://www.talos.dev/latest/reference/configuration/v1alpha1/config/#Config.machine.udev).
## /sbin/mkfs.xfs
This will create an
[XFS file system](https://en.wikipedia.org/wiki/XFS) on a disk or logical volume.
## /sbin/xfs_repair
This is used to repair an XFS file system if it becomes corrupted.
## /sbin/xtables-legacy-multi
This binary is symlinked by
iptables* and
ip6tables* to configure IP tables on the host. Container network interface (CNI) providers often mount directories from the host and expect these commands to exist because they cannot easily be run from within a container.
These symlinks account for 12 total files in the system but they all perform common iptables commands.
## Conclusion
It may seem impossible but that’s the entire system. Every binary is required to bootstrap a Kubernetes cluster or run a node as part of the cluster. This is why we call Talos Linux the
[Kubernetes Operating System](https://www.siderolabs.com/platform/talos-os-for-kubernetes/).
There are more executable files in /lib and /usr but those are Shared Object (.so) files and Kernel modules (.ko). These are necessary to run the system for drivers and various programs but are not called directly.
If you would like to download and install Talos on your system of choice you can get started at
[https://talos.dev](https://talos.dev).
To get an even easier interface to managing Kubernetes clusters on-prem or in a cloud provider check out Omni at
[https://www.siderolabs.com/platform/saas-for-kubernetes/](https://www.siderolabs.com/platform/saas-for-kubernetes/).
If you have questions or want to get started come join the
[Talos community Slack](https://slack.dev.talos-systems.io/).