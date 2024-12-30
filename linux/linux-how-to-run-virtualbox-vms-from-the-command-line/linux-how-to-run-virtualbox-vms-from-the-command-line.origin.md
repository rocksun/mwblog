# Linux: How to Run VirtualBox VMs from the Command Line
![Featued image for: Linux: How to Run VirtualBox VMs from the Command Line](https://cdn.thenewstack.io/media/2024/11/74278f41-virtualbox-1024x683.png)
If you’ve finally started working with VirtualBox virtual machines, you’ve probably found the software [incredibly easy to use](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/). With [Oracle](https://developer.oracle.com/?utm_content=inline+mention)’s [VirtualBox](https://www.virtualbox.org/), you can create and deploy virtual machines of your favorite [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) for testing or daily usage, Windows and even macOS.

Here’s the thing: if you create a virtual machine instance of a server OS, you probably don’t want to keep the VirtualBox GUIs running so a headless server can be reached. GUIs not only take up system resources, but they could also make it easy for some unwitting person to step up to your desktop and stop a running server.

Should you run into such a case, you’ll want to know how to run those virtual machines from the [command line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).

Not only does this mean you’ll save precious CPU cycles and RAM, but you can also manage those VMs remotely. [SSH](https://thenewstack.io/linux-ssh-and-key-based-authentication/) into the host and start, pause, stop and even delete your virtual machines.

Let me show you how this is done.

## What You’ll Need
To make this work, you’ll need a running instance of VirtualBox installed on a Linux host. You’ll also need a user with sudo privileges. That’s it — let’s get to work.

## Installing the VirtualBox Extension Pack
The first thing you must do is install the VirtualBox Extension Pack. With the extension pack, any virtual machine that is started from the command line will not have access to the network. Without an available network, those virtual machines are pretty useless.

To install the VirtualBox extension pack, do the following:

- Download the
[latest version of the extension pack from the VirtualBox download site](https://www.virtualbox.org/wiki/Downloads). - Open VirtualBox.
- Click File > Tools > Extension Manager.
- Click Install (Figure 1).
- Navigate to where you saved the downloaded extension pack file, which will end in .vbox-extpack.
- Click Open.
- Type your
[sudo password](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). - Click OK.

-
Figure 1: If the extension pack has already been installed, it’ll be listed here.

Now that the extension pack is installed (it should be listed in the Manager), you’re ready to start working with your virtual machines from the command line.

## List Your Virtual Machines
To manage your virtual machines, you have to know their full names, which can be found with the command:

1 |
VBoxManage list vms |
The output should look something like this:
123456789101112131415161718 |
"KDE NEON" {02a76c48-cacf-4cfb-8ec2-97a84454d97f}"Ubuntu Golang" {3384369f-82a5-467a-aaf8-b1f5d806f404}"Ubuntu Server" {a647b5be-7736-453a-bae5-b30c40a15250}"Ubuntu 22.04" {bac0764b-ee2d-4476-b5f9-8f315e27f55c}"AlmaLinux 9.4 beta" {68294206-cdd5-4c2e-b807-f33c11f45751}"Debian Server" {a20b1fe6-1b9c-4788-b8c2-076662b0869d}"Ubuntu 24.04" {8e2b3b4d-8544-4c34-920a-4901d2b2362f}"COSMIC2" {a4e0c8e8-139f-4f73-b0e6-7d82a039083c}"Gentoo" {221e41f3-1923-4652-be7f-f939d757a54f}"AlmaLinux Home Auto" {443a6a7f-28ce-4ece-b80b-00140523492a}"Fedora 41" {90593cbc-58b5-460c-895b-b826bf705472}"Zorin 17.2" {bdf99643-807f-41e0-9470-1e2f681c758e}"Manjaro" {076bd311-9f69-4558-8834-38b7d80d7f75}"Debian" {2ffe5b00-31c3-42f6-8f5f-f4e069af6f67}"TrueNAS" {f7b591fa-3925-415a-94d1-859abd64e260}"Ubuntu Desktop" {5c7cf691-7436-400b-b76c-6787643be324}"Fedora KDE" {6978832e-d7c5-4a7f-8523-812f107a288c}"CachyOS" {413ede52-a002-48e3-b100-c10ac0c8f65e} |
Those are all the current virtual machines I have added to VirtualBox.
Say you want to start the virtual machine “Ubuntu Server.” For that, the command would be:

1 |
VBoxManage startvm "Ubuntu Server" --type headless |
The output should look like this:
12 |
Waiting for VM "Ubuntu Server" to power on...VM "Ubuntu Server" has been successfully started. |
You can verify that it’s running by issuing the following command:
1 |
VBoxManage list runningvms |
The output should look like this:
1 |
"Ubuntu Server" {a647b5be-7736-453a-bae5-b30c40a15250} |
You can then access the virtual machine as you normally would (as long as you remember the IP address of the server).
Here are some more commands you can use to manage those virtual machines (I’ll stick with the Ubuntu Server VM as an example):

- Pause a virtual machine:
`VBoxManage controlvm “Ubuntu Server” pause --type headless`
- Restart a paused virtual machine:
`VBoxManage controlvm “Ubuntu Server” resume --type headless`
- Shutdown a running virtual machine:
`VBoxManage controlvm “Ubuntu Server” poweroff --type headless`
- Delete a virtual machine:
`VBoxManage unregistervpm "Ubuntu Server" --delete-all`
## Creating a New Virtual Machine
You can also create virtual machines from the command line. The process is a bit more complicated than managing previously existing VMs, and you still have to use a GUI (such as an RDP client) to complete the OS installation. Make sure you’ve download the ISO for the OS you want to install before starting with this process. If you’re feeling brave, here are the steps (make sure to modify them as needed for your situation):

### Create the VM
First, create the virtual machine with the command:

1 |
VBoxManage createvm --name Ubuntu_Server --ostype --register --basefolder `pwd` Ubuntu24_LTS_64 |
### Configure the RAM and the Network Card
Next, you’ll need to configure the RAM and network card with the following three commands:

123 |
VBoxManage modifyvm Ubuntu_Server --ioapic onVBoxManage modifyvm Ubuntu_server --memory 1024 --vram 128VBoxManage modifyvm Ubuntu_Server --nic1 bridged |
### Create the Disk and Connect the ISO Image
We’ll now create an 80GB SATA HD and a CDROM with an attached Ubuntu ISO with the commands (modify as needed):

123456 |
VBoxManage createhd --filename `pwd`/Ubuntu_Server/Ubuntu_Server_DISK.vdi --size 80000 --format VDIVBoxManage storagectl Ubuntu_Server --name "SATA Controller" --add sata --controller IntelAhciVBoxManage storageattach Ubuntu_Server --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium `pwd`/Ubuntu_Server/Ubuntu_Server_DISK.vdi VBoxManage storagectl Ubuntu_Server --name "IDE Controller" --add ide --controller PIIX4 VBoxManage storageattach Ubuntu_Server --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium `pwd`/ISO VBoxManage modifyvm Ubuntu_Server --boot1 dvd --boot2 disk --boot3 none --boot4 none |
### Configure RDP Access
Next, configure RDP access so it can be accessed from the network with the commands:

123 |
VBoxManage modifyvm Ubuntu_Server --vrde on VBoxManage modifyvm Ubuntu_Server --vrdemulticon on --vrdeport 10001VBoxHeadless --startvm Ubuntu_Server |
You should then be able to start the new virtual machine with the command:
1 |
VBoxManage startvm Ubuntu_Server --type headless |
This will launch the VM and you can then access it via RDP on port 10001, where you can finish installing the guest OS.
And that’s all there is to managing your VirtualBox VMs from the command line. If I’m being 100% honest with you, I much prefer creating the virtual machines from the GUI and then managing them from the command line.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)