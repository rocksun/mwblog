# Use Podman to Create and Work with Virtual Machines
![Featued image for: Use Podman to Create and Work with Virtual Machines](https://cdn.thenewstack.io/media/2024/04/38bf6368-podman-logo-1024x683.png)
When you think of
[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)’s Podman, one thing comes to mind: [containers](https://thenewstack.io/containers/). That’s because [Podman was created](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/) as a tool for [creating and managing containerized applications](https://thenewstack.io/install-and-use-podman-desktop-gui-to-manage-containers/) and services. ![](https://cdn.thenewstack.io/media/2024/03/bd92cdb3-podman-3-logo-95w-90h.webp)
Podman
But Podman has another trick up its sleeve. With the help of the
[QEMU emulator](https://www.qemu.org/), Podman is capable of creating a basic Fedora CoreOS virtual machine that can be used for containers, containerized workloads or for the development of such containerized applications (so long as they work within the realm of [Fedora CoreOS)](https://fedoraproject.org/coreos/download?stream=stable).
For those who aren’t familiar with Fedora CoreOS, it was created specifically to be optimized to run containerized applications. Fedora CoreOS was initially released on Nov. 6, 2003, and has been steadily growing since. As the name implies, Fedora CoreOS is kept to a bare minimum by design, so it only has what you need.
Podman makes deploying Fedora CoreOS virtual machines a breeze. By doing this, you don’t have to worry about pulling down the latest version of Fedora CoreOS from Docker Hub or any other third-party repository. That means the
[virtual machines are clean](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/).
But how do you start working with these virtual machines? Let me show you how.
## What You’ll Need
To work with Podman Machines, you’ll want to have a Ubuntu-based Linux distribution. Although the version of Podman on RHEL-based distributions supports the Machines command, it’s not currently possible to install the necessary QEMU software to make it work. That’s why I’m going to focus my demonstration on Ubuntu. You’ll also need a user with
[sudo privileges](https://thenewstack.io/sudo-update-offers-python-plug-ins-extended-logging-auditing/) for the installation.
That’s it. Let’s make some VM magic.
## Installing Podman and the Requirements
Ubuntu doesn’t ship with Podman installed. The good news is that it can be installed from the standard repositories. So log into your Ubuntu system, open a terminal window, and install Podman with the command:
|
1
|
sudo apt-get install podman -y
You’ll be prompted for your user password in order to gain admin privileges. Once that installation is complete, you’ll then need to install the required QEMU software, which is accomplished with the command:
|
1
|
sudo apt-get install qemu-system -y
When that completes, there’s one (or two) more step(s) you must take. First, download the gvproxy file and save it to the proper location with the command:
Finally, you need to make sure the KVM kernel module is loaded, which means the machine you’re running on must support KVM. This can be done with one of the following:
|
1
2
|
sudo modprobe kvm-intel
sudo modprobe kvm-amd
You’re now ready to move on to creating your first Fedora CoreOS virtual machine.
## Deploying a Virtual Machine
Podman virtual machines are managed with the
*podman* machine command (along with various options). First, view the current machines with the command:
|
1
|
podman machine list
You shouldn’t see any virtual machines listed because we haven’t created any. To create your first VM, you initialize it with the command:
|
1
|
podman machine init
The above command will create a new VM with a randomly generated name. You can also generate one with a user-specified name like this:
|
1
|
podman machine init NAME
Where NAME is the name of the machine you want to deploy.
Now, if you view the available VMs (with the command podman machine list), you should see one listed, either with a randomly generated or user-created name.
Let’s say you created a new VM called vm1. To start that machine, issue the command:
|
1
|
podman machine start vm1
The virtual machine will start, and when you receive your prompt back, you’re ready to go.
## SSH into Your Virtual Machine
With the virtual machine running, it’s now time to access it, which is done via SSH. Before you try to run the standard ssh command, that’s not how it works in this case. To SSH into your virtual machine, you run the command:
|
1
|
podman machine ssh NAME
Where NAME is the name of the virtual machine. If you didn’t supply a name when you created the VM, you could simply issue the command:
|
1
|
podman machine ssh
At this point, you’ll find yourself inside the running virtual machine, where you can start developing your containerized application. When you’re finished, you can exit from the machine with the command:
|
1
|
exit
Finally, you can stop the virtual machine with the command:
|
1
|
podman machine stop
Of course, if you gave the VM a custom name, that command would be:
|
1
|
podman machine stop NAME
Where NAME is the name of the machine you wish to stop.
You can deploy as many virtual machines as you like. I would recommend, however, that you always give your VM a unique identifying name to indicate the containerized app or service you’re building.
You can also delete a VM with the command:
|
1
|
podman machine rm NAME
Where NAME is the name of the VM you wish to delete.
And that, my friends, is all there is to deploying virtual machines with the Podman application.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)