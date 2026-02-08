For decades, I used VirtualBox for all my [virtual machine](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/) (VM) needs. I could use it as a graphical user interface (GUI), or I could run it from the command line. It was easy to work with, was cross-platform, and rarely caused me any problems.

Until it didn’t.

Over the past few years, I cannot tell you how many times I wound up with a broken VirtualBox installation that required me to completely remove the software and reinstall it. Generally speaking, it was a hassle, but the solution worked.

Until it didn’t.

A few weeks ago, VirtualBox broke again. I ran through the usual tricks, but was unable to get it working. I removed conflicting kernel modules (which were often the problem), did a purge uninstall, reboots, upgrades … you name it, I did it. This time, however, the fixes wouldn’t work.

The problem is, I depend on VMs every day. Without the ability to spin up VMs, I wouldn’t be able to review Linux distributions, test software, and perform several other tasks.

Thus, I permanently removed VirtualBox, vowing to never use it again.

The solution came by way of [KVM](https://thenewstack.io/amazon-web-services-open-sources-a-kvm-based-fuzzing-framework/), which is a [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) Kernel-based VM. KVM is an open source virtualization technology that allows the Linux kernel to function as a hypervisor to deliver near-native performance and reliability.

Since adopting KVM, I’ve not had a single issue with my VMs. However, I don’t use KVM alone. Instead, I pair it with [Virt-Manager](https://virt-manager.org/) to make working with VMs exponentially easier.

How do you install and use KVM/Virt-Manager?

Let me show you.

## What you’ll need

The only things you’ll need for this are a running instance of Linux, a user with sudo privileges, and an ISO of any Linux distribution.

Let’s get to work.

## Installing Virt-Manager

First off, you don’t have to install KVM, as it is built into the Linux kernel. With that said, you do need to install the GUI frontend, Virt-Manager, and here’s how:

* On Ubuntu/Debian-based machines: *sudo apt-get install virt-manager -y*
* On Fedora-based machines: *sudo dnf install virt-manager -y*
* On Arch-based machines: *sudo pacman -S virt-manager*
* On openSUSE-based machines: *sudo zypper install virt-manager*

With Virt-Manager installed, you’re ready to create your first VM.

## Creating a VM with KVM/Virt-Manager

You should find a new entry in your desktop menu named Virtual Machine Manager. Click on that to run the app. When it appears, you’ll see a single, small window (Figure 1).

![](https://cdn.thenewstack.io/media/2026/01/17838a53-virtman1.jpg)

Figure 1: The Virt-Manager main window in my default bubblegum pink theme.

Click the far left icon, which looks like a monitor, to create a new VM. In the resulting window (Figure 2), make sure Local install media is selected and click “Forward.”

![](https://cdn.thenewstack.io/media/2026/01/006d7fc3-virtman2.jpg)

Figure 2: Local install media should be selected by default.

In the next screen (Figure 3), click “Browse” and then, with your default file picker, locate and select the ISO you want to use.

![](https://cdn.thenewstack.io/media/2026/01/2d4b9868-virtman3.jpg)

Figure 3: If you’ve already created a VM, the ISO for your distribution will appear in the drop-down.

Chances are, Virt-Manager won’t auto-detect the OS, so type “gen” and then select “Generic Linux 2024.” Click “Forward” to continue.

You can now dedicate any amount of RAM and CPU cores you need for the OS (Figure 4).

![](https://cdn.thenewstack.io/media/2026/01/ce6fb997-virtman4.jpg)

Figure 4: I typically leave this as-is, unless the OS requires more RAM.

The next window (Figure 5) is where things start to get a bit more complicated. Don’t worry, once you understand what’s happening, you’ll be fine.

![](https://cdn.thenewstack.io/media/2026/01/c97bd37e-virtman5.jpg)

Figure 5: Make sure to use your storage wisely.

By default, Virt-Manager will store your VMs on the same drive as your OS. Because I create so many VMs, I prefer to store them on external drives to avoid running out of room. If you’re not worried about that, check “Create a disk image for the virtual machine” and allocate however much storage you want.

Choose “Select or create custom,” and then click “Manage.”

It’s now time to create a new storage pool and then a volume to house the VM. In the “Locate or create storage volume” window (Figure 6), click the + at the bottom left of the window. Give the new pool a name, change the Target Path to a directory on an external drive (if necessary), and click “Finish.”

![](https://cdn.thenewstack.io/media/2026/01/b0273c3d-virtman6.jpg)

Figure 6: You have to create a storage pool before you create a volume.

Once you’ve created the pool, click + to the right of Volumes. In the resulting window (Figure 7), give the new volume a name (probably the same name as the distro), allocate the space you want for the VM, and click “Finish.”

![](https://cdn.thenewstack.io/media/2026/01/bcb44692-virtman7.jpg)

Figure 7: You’re almost done.

Make sure your new volume is selected (it’ll end in qcow2) and click “Choose Volume.”

Back at the New VM window, click “Forward.” In the next window, give the VM a name and then check “Customize configuration before install.”

Click “Finish,” and the custom config window will open (Figure 8).

![](https://cdn.thenewstack.io/media/2026/01/fc28b8e2-virtman8.jpg)

Figure 8: There’s a lot to customize here.

For my KDE Neon installation, I have to select UEFI from the Firmware drop-down. Once I do that, I click “Apply” and then click “Begin Installation.”

At this point, a new window will open, where you can begin the OS installation process.

And that’s how you install Virt-Manager and use it, along with KVM, to create reliable, near-native-performing virtual machines.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)