# Linux: Choose an Installation Platform
![Featued image for: Linux: Choose an Installation Platform](https://cdn.thenewstack.io/media/2024/07/afc234cd-martyn-de-jong-1bizoitnk-0-unsplash-1024x683.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/),
[file permissions](https://thenewstack.io/linux-how-file-permissions-work/), and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
You’ve chosen a Linux distribution and are ready to begin the installation process, but you need to figure out your hardware options. Do you have to go buy a new computer? Can you use an older system? What about this virtualization thing? Are containers a choice?

This article doesn’t provide technical configurations. Instead, it discusses installation options for experimenting with Linux as you pursue career development, programming, or technical certifications. It offers ideas about what hardware is necessary and how to use your existing resources. I also cover this information with an eye toward not spending too much money on the solution.

The related articles in the series discuss choosing one or more distributions and the actual installation process.

## Use a Hardware Platform
The term “bare metal” refers to a computer’s hardware without an operating system or applications (though firmware is usually in place). A computer typically has four major subsystems: processor, memory, storage, and networking. On bare metal hardware, these components are installed and ready, but no software exists to utilize them.

Installing Linux on a bare metal device means installing it on a computer with no other operating system or applications you intend to retain. This could be a new computer you’ve just assembled or an older device whose OS, applications, and data you intend to overwrite.

Linux is very flexible when it comes to hardware requirements. Most Linux distributions can get by on much smaller quantities of RAM and hard disk space than the Windows and macOS operating systems. Some distributions are even specialized to run well on much older hardware platforms. Because so many distributions exist and their functionality varies widely, it’s difficult to pin down a specific set of minimum and recommended hardware requirements. It’s best to check these recommendations on a per-distribution basis.

Here are a few sample recommendations:

[Ubuntu hardware specs](https://ubuntu.com/download/desktop#system-requirements): 2 GHz dual-core CPU, 4 GB of memory, 25 GB of drive space.[Fedora hardware specs](https://docs.fedoraproject.org/en-US/fedora/latest/release-notes/hardware_overview/): 2 GHz dual-core CPU, 2 GB of memory, 15 GB of drive space.
Those are pretty light requirements for today’s systems. You may find that an older computer gathering dust in your closet or basement will work very well for Linux, even if it no longer works effectively with other operating systems.

### Choose Linux-Specific Hardware
If you choose to buy hardware, be sure to look for Linux-compatible systems. For example, [Ubuntu certifies specific hardware](https://ubuntu.com/certified) for use with its distribution. Some major manufacturers, such as Dell, offer Linux as a preinstalled operating system choice on some systems.

Other vendors specialize in nothing but Linux. Consider [System76](https://system76.com/)‘s line of laptops, workstations, minis, and servers using their own Pop!_OS or Ubuntu 22.04 LTS. [Tuxedo Computers](https://www.tuxedocomputers.com/index.php) also offers Linux-specific computers with Tuxedo OS Linux and Ubuntu. Many additional choices exist.

However, Linux has a very robust set of drivers and is compatible with most of today’s standard and modern hardware. I wouldn’t hesitate to put the OS on nearly any computer I might come across.

## What Is Virtualization?
Virtualization software takes a very different approach from bare metal installations. This solution begins with a bare metal hardware device and an existing operating system, like Linux, Windows, or macOS. You’ll install virtualization software on the computer the same way you would a web browser or PDF reader. This software allows you to create virtual computers upon which you can install various operating systems, including Linux.

The virtualization software divides your computer’s process, memory, storage, and network capabilities into “virtual machines” and allows an operating system to be installed on them.

Virtualization is a weird concept. Let’s break it down by examining the two words “virtual machine.” The word “virtual” means pretend or simulated. In this case, the processor, memory, storage, and networking capabilities are being simulated. The word “machine” indicates they are simulated as if they were a real computer. In essence, you’re creating a pretend computer within the software of your regular computer and operating system.

![](https://cdn.thenewstack.io/media/2024/05/9ba0a520-ubuntu-vm.png)
Because this virtual machine looks and acts like a real computer, you can install an operating system on it so you can use it the same way you would any other computer.

### Virtualization Example
Consider the following example: Suppose I have an Apple MacBook Pro laptop. This physical device includes an installation of the Apple Sonoma macOS. I can use this laptop and the programs installed on it to write documents, explore the web, manage email, and edit images. In other words, this is a basic day-to-day use computer.

But what if I decide to learn some [Python programming](https://thenewstack.io/python/)? I could do that using macOS with no problem, but it might be useful to isolate my programming experiments so that if something goes wrong, I don’t blow up the computer I use for business. I could install virtualization software like Parallels on my Mac and then create a virtual machine that borrows processor, memory, storage, and networking from my physical computer. I’d then install the Fedora Linux distribution on that virtual machine. Fedora will treat this VM as if it were a real computer. I could then add any Python tools and resources to the Fedora VM and use it to work on my programming projects.

![](https://cdn.thenewstack.io/media/2024/05/4f39987e-vm-on-mac.png)
## Compare Bare Metal and Virtualization
The bare metal and virtualization approaches each have advantages, though I will say virtualization is really a very robust solution.

Advantages of bare metal:

- Hardware control
Disadvantages of bare metal:

- More expensive
- Space
- Power consumption
- Cooling
- Noise
Advantages of virtualization:

- Cost savings
- Space, cooling, and noise reduction
- Use one computer for many operating systems
Disadvantages of virtualization:

- Includes a learning curve, though basic deployments are straightforward
- Software may be expensive
- Can put a strain on the host computer’s resources
Most of today’s computers are plenty powerful to run the host operating system and at least a couple of VMs simultaneously. That’s enough to experiment with a few different Linux distributions to find the one you like. I regularly run Fedora and Ubuntu Linux VMs at the same time on my Mac laptop with no performance hit, and I wouldn’t hesitate to run two or three more VMs concurrently. Powerful servers may host many production VMs simultaneously.

### Virtualization Software Options
You have many options for virtualization software. The two main limitations are compatibility with your host OS (Windows, macOS, or Linux) and cost. The following list shows the most common choices.

[VMware Workstation Pro](https://www.vmware.com/products/workstation-pro.html): Runs Windows and Linux VMs on Windows and Linux host systems. VMware offers a few different purchase options, but Workstation Pro is $199.[Parallels](https://www.parallels.com/): Runs Windows and Linux VMs on Apple macOS host systems. Parallels offers a Standard or Pro subscription. The Pro subscription starts at $95.99/year.[Microsoft Hyper-V](https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-enabling-hyper-v-for-use-on-windows-11/ba-p/3745905): If you have Windows 11, you can add Microsoft’s Hyper-V virtualization software to run Windows and Linux VMs. Hyper-V itself does not have a cost, but you must have a licensed copy of Windows 11 Pro or Enterprise.[Oracle VirtualBox](https://www.virtualbox.org/): VirtualBox runs on Windows, Linux, and macOS hosts and supports Windows and Linux VMs. It’s free and open-source. VirtualBox is a robust option and a great choice for most users.[Gnome Boxes](https://apps.gnome.org/Boxes/): Boxes runs on Linux hosts and supports various Linux and Windows operating systems. It’s a free and open-source product for Linux systems.
Note that pricing and specification information is current at the time of writing.

![](https://cdn.thenewstack.io/media/2024/05/5fabc633-control-center.png)
## Consider a Raspberry Pi
Another interesting option is the [Raspberry Pi](https://www.raspberrypi.com/) platform. A Raspberry Pi is a small single-board computer with a remarkable amount of power in a very small package. You can install a [Raspberry Pi-specific Linux distribution](https://www.raspberrypi.com/software/) on it to run many applications, use Internet of Things utilities, or stream multimedia. These devices are small, flexible, and very affordable. They were originally designed to get kids interested in programming and computing. Ubuntu even has a [Pi version](https://ubuntu.com/download/raspberry-pi) of its distribution.

Raspberry Pi can be a great option for those looking to break into Linux.

![](https://cdn.thenewstack.io/media/2024/05/d1bb3a6b-rpi-rotated.jpg)
## What About Containers?
[Containers](https://www.docker.com/resources/what-container/) are a newer form of virtualization that receives a lot of attention today. You may wonder about using Linux in a container to learn the operating system. It’s certainly possible, but the process is more convoluted than a traditional virtual machine and not as easy to work with.
As with virtual machines, containers require host software (a container engine) running on your regular computer. However, containers are really meant to be computing environments for applications rather than for the OS layer.

While I strongly recommend [learning all you can about containers](https://thenewstack.io/containers/how-to-deploy-a-container-with-docker/), I think you’ll find there are more effective ways of working with the Linux OS than containerizing it.

## Wrap Up
The most essential part of learning a new operating system is hands-on experience. If you’re ready to work with Linux daily, you’ll need a way to practice commands, install software, configure security, etc. You can gain this experience by installing Linux on a physical computer system or creating virtual machines on your existing computer. Both options have advantages, but virtualization is usually cheaper and easier. Furthermore, you’ll need familiarity with virtualization anyway if you work in the IT industry. Finally, virtual machines make it much easier to experiment with the many available Linux distributions. I suggest starting with [Ubuntu](https://ubuntu.com/desktop), [Fedora](https://fedoraproject.org/workstation/), [Rocky](https://rockylinux.org/), or [Mint](https://www.linuxmint.com/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)