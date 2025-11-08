An open source container platform, [Apptainer](https://apptainer.org/) (formerly Singularity) is designed for secure, [high-performance computing](https://thenewstack.io/hpc-kubernetes-ai-training-on-3500-gpus/) (HPC) environments. Unlike Docker, which [dominates desktops and cloud services](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/), Apptainer shines in multi-user Linux systems such as HPC clusters, where user-space containers without root privileges are required. It provides similar functionality to Docker, including compatibility with most Docker images, while addressing security and portability needs in HPC.

This guide will help Docker-savvy developers explore Apptainer on Linux, covering installation, basic usage, and use cases.

## Getting Started With Apptainer on Ubuntu

Installing Apptainer on Linux can be done via package managers or from source. Apptainer requires a modern Linux kernel (with user namespaces enabled for unprivileged use) and does not run on Windows/Mac without a Linux VM.

For many Debian/Ubuntu users, the easiest path is using the official Personal Package Archive (PPA):

```
sudo apt update &amp;&amp; sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update &amp;&amp; sudo apt install -y apptainer    # use apptainer-suid for SUID mode
```

These commands install Apptainer in unprivileged mode by default (no setuid binaries). If you need features requiring SUID (setuid root helpers for older kernels or certain mount functions), install the apptainer-suid package instead. In unprivileged mode, Apptainer leverages user namespaces so that you can run containers entirely as a regular user.

After installation, verify it works by executing a simple container, for example:

```
apptainer exec docker://alpine cat /etc/alpine-release
```

[![](https://cdn.thenewstack.io/media/2025/11/712f600a-apptainer-0-1024x409.png)](https://cdn.thenewstack.io/media/2025/11/712f600a-apptainer-0-1024x409.png)

This command pulls a tiny [Alpine Linux](https://thenewstack.io/alpine-linux-heart-docker/) image and prints its version file, confirming Apptainer is correctly set up.

You notice that Apptainer converts the Docker image to an SIF file in the current directory. The Singularity Image Format (SIF) is the standard container image format used by Apptainer and Singularity. SIF encapsulates the entire container environment — OS, software, metadata, and configuration — into a single, immutable file.

Like Docker images, this design ensures portability, reproducibility, and security for scientific, HPC, and enterprise workloads. SIF images are primarily read-only, allow signature verification and encryption, and integrate seamlessly with parallel filesystems. Since the entire image is stored in a single file, distributing and archiving containers is easy. Writable overlays and host-mount options provide flexibility where needed.

The .sif file is typically built from a definition (.def) file, which outlines the build steps, installed packages, and environment setup. Once created, a .sif image acts as a reliable, verifiable, and production-quality container image that is portable and ensures reproducible execution, as its contents never change after creation. Apptainer can use this file to instantiate the container, run specific commands, launch applications, or provide an interactive shell.

A basic Apptainer .def file is shown below. It builds an image definition from an existing Docker image.

```
Bootstrap: docker
From: ubuntu:22.04

%post
    apt-get update
    apt-get install -y python3

%runscript
    echo "Hello from Apptainer!"

%help
    This container installs Python 3 on Ubuntu 22.04 and prints a message when run.
```

You can build the image with the following command:

```
sudo apptainer build myimage.sif myfile.def
```

Apptainer internally maintains a cache for intermediate files and layers, typically at `~/.apptainer/cache` on your system.

## Running Basic Containers

Apptainer’s command-line interface is similar to Docker’s, but there is no daemon involved. You run containers directly via the apptainer command. Common subcommands include run, exec, and shell, which are analogous to Docker’s `docker run`, `docker exec`, and `docker run -it` for an interactive shell.

Use `apptainer run`  to execute the image’s default runscript. For example, after pulling an Apptainer image (.sif file), you can simply run it:

```
apptainer pull docker://alpine
apptainer run alpine_latest.sif
```

If the image has a defined runscript, apptainer run executes that. Otherwise, it falls back to an interactive shell. You can also run images directly via a URI without saving them.

```
apptainer run docker://ghcr.io/apptainer/lolcow
```

You can use `apptainer exec`  to run a specific command inside a container. For example:

```
apptainer exec alpine_latest.sif echo "Hello from inside container"
```

This is similar to `docker exec` but can be run even on an image file or a Docker Hub URI. If you don’t have the image yet, Apptainer will fetch it and run the command in a single step.

Use `apptainer shell`  to get a shell inside the container, useful for exploration or debugging. For instance:

```
apptainer shell alpine_latest.sif
<img class="aligncenter size-large wp-image-22805178" src="https://cdn.thenewstack.io/media/2025/11/487e0cc1-apptainer-1-1024x285.png" alt="" width="1024" height="285" />
```

## How Apptainer Executes Containers

Apptainer takes a fundamentally different approach to container runtime compared to Docker. There is no background daemon, and running a container is a direct invocation that creates the container environment in-process. When you run an apptainer container, it performs a series of steps: mounting the SIF image (which is a [SquashFS](https://docs.kernel.org/filesystems/squashfs.html) filesystem) in a minimal Linux user namespace, setting up necessary namespaces (mount, PID, etc., as needed), and then using an `exec()` system call to launch the specified process inside the container context. The result is that the containerized application runs as a child process of your Apptainer command, without any extra shims or wrappers left behind. Apptainer’s design results in minimal overhead: once the container process starts, there’s no ongoing manager process — it’s your app running directly on the host kernel with container isolation applied.

Importantly, Apptainer containers run with the same user identity as on the host by default. If you launch a container as an unprivileged user, you will be that user inside the container as well (UID/GID preserved). There is no docker0 network or default NAT: by default, Apptainer shares the host network stack (so networking is not isolated unless you use explicit options). The container process can see and use host resources like GPUs, network interfaces, and files (subject to what’s mounted) as permitted to the user. This model aligns with HPC use cases where you don’t want a container to have more privileges than the invoker and you want efficient access to hardware, such as high-speed interconnects.

To achieve container setup without root, Apptainer can be installed in setuid mode or fully unprivileged mode. In setuid mode, a small portion of Apptainer’s code (apptainer-suid) runs with root privileges to perform mount operations, then drops privileges. In unprivileged mode, it uses user namespace features (available on kernels ≥ 4.18) to mimic root inside a new namespace for setup. Either way, the result is that you don’t need a root-running daemon service. The container runs within the user’s session, making Apptainer inherently daemonless and kernel-integrated. From a developer’s perspective, this means you can invoke Apptainer commands like any other CLI tool, and containers exit when your command completes, leaving no lingering container processes.

## When To Use Apptainer Instead of Docker

Apptainer is preferred over Docker in several scenarios, especially in high-performance computing (HPC) and secure multi-tenant environments, for the following reasons:

### Rootless Execution and Security

Apptainer allows users to run containers without [requiring root](https://thenewstack.io/linux-cgroups-v2-brings-rootless-containers-superior-memory-management/) (administrator) privileges, making it inherently safer on multitenant systems and shared HPC clusters by avoiding the privilege escalation risks common to Docker’s daemon model.

### HPC and Scientific Computing Focus

Apptainer was explicitly designed for scientific computing and HPC, integrating with resource managers and job schedulers, whereas Docker was primarily developed for microservices and enterprise application deployment workflows.

### Single-File Container Images

Apptainer uses the Singularity Image Format (SIF), which packages the entire container as a single, immutable file. This makes distribution, sharing, and archiving easier than Docker, which structures containers as stacks of image layers in tar files.

### Native User Identity Preservation

The user’s identity (UID/GID) outside the container is preserved inside the container, ensuring transparent file system and permissions handling, which is crucial in university clusters or collaborative research environments.

### Compatibility With Existing HPC Infrastructure

Apptainer works seamlessly with existing HPC tools and storage, without needing changes to infrastructure. Its containers natively integrate with parallel filesystems and large-scale job schedulers and do not require a root-running background daemon, unlike Docker.

These advantages make Apptainer the preferred choice for secure, large-scale, and research-focused compute environments where rootless operation and seamless integration are priorities.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)