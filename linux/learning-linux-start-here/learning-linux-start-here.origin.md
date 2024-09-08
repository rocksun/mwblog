# Learning Linux? Start Here
![Featued image for: Learning Linux? Start Here](https://cdn.thenewstack.io/media/2024/09/fa8b210b-zetong-li-my06s-wg_zc-unsplash-1024x682.jpg)
Learning Linux has never been easier. There are plenty of resources out there, lots of opportunities for hands-on experience, and more user-friendly distributions than ever. The biggest challenge you might face is how to approach your learning plan.

This article offers ideas about specific topic areas to cover and when to cover them. Use it as a learning plan to prepare for a job change, certification exam, or new development project. It maps to current (and future) articles that I and others have written on [The New Stack](https://www.thenewstack.io/Linux) that provide more depth and explanation.

## Hands-On Is Critical
Working at the [command line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) is intimidating to many newer IT people. It’s a necessary skill, however, and once you get comfortable, you’ll find it’s easier than expected. Command line administration offers capabilities graphical interfaces don’t have, including:

**Scripting**: Commands can be placed in text files that the system executes, enabling complex automation tasks that can be easily kicked off with a single command.**Speed**: Command-line interfaces are typically quicker than mouse-driven interactions for those familiar with Bash (which includes tricks like tab completion and history for greater efficiency).**Additional options**: Graphical interfaces often only include standard tasks in their menus, while commands typically have many additional features, options, and parameters that may be essential but less commonly used.**No graphical interface required**: Unlike most Windows and macOS installations, many Linux servers do not include a graphical interface due to its additional overhead. In these cases, command-line administration is the primary option.
[Building a lab environment](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) consisting of two or three Linux virtual machines will make learning the following skills easier. Nothing beats hands-on experience!
Don’t forget to use the man pages when you forget command options or subcommands.

Today, most Linux distributions require users to log on with a non-privileged (non-root) user account. Users can then elevate privileges for specific delegated tasks by using [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). Avoiding root logins is considered a Linux security best practice.

## Learn Access Control Methods
Managing access to files and folders is a critical Linux sysadmin skill. Access control begins with [user accounts](https://thenewstack.io/linux-user-and-group-management/), which establish a user’s identity. These accounts may be placed in groups for easier management.

Command: | Description: |
useradd | Create a user |
usermod | Modify a user |
userdel | Delete a user |
groupadd | Create a group |
groupmod | Modify a group |
groupdel | Delete a group |
The computer also maintains basic resources, such as [files and directories](https://thenewstack.io/linux-file-management/). Administrators and users create, modify, and delete these resources. Mastering the various commands for managing files and directories enables you to work with these resources efficiently.

Command: | Description: |
mkdir | Create a directory |
touch | Create a file or update its timestamp |
ls | List the contents of a directory |
cd | Change to a different directory |
Once the system understands who a user is and what file resources exist, it can enforce access controls. Permissions are associated with files to specify exactly what accounts have what privileges. This access list is checked whenever a user attempts to manage a file.

[Linux permissions](https://thenewstack.io/linux-how-file-permissions-work/) differ from Windows access controls. There are three levels of access (read, write, and execute), and they are applied to three identities (the user (owner), one group, and everyone else) using commands like
chmod and
chown. Linux permissions are simpler to manage than Windows permissions but somewhat less robust. Features like Access Control List (ACL) permissions do add significant functionality.
Learning to manage users and permissions is a cornerstone of Linux administration, so be sure to master these skills.

![](https://cdn.thenewstack.io/media/2024/07/dbe42982-ls-l.png)
## Manage Hardware, Services and Processes
The purpose of a Linux server is to provide services. These services could include file storage, printing, website access, database hosting, and more. Before deploying a service, determine whether the system has the [hardware capacity](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/) to support the role. Linux includes many built-in commands for reporting hardware, including top, lshw, and more.

Modern Linux distributions typically rely on systemd to [manage services](https://thenewstack.io/linux-skills-manage-system-services/). You interact with systemd using the
systemctl command and a series of standard subcommands. These allow you to start, stop, restart, enable, and disable services. The primary task is usually restarting a service, which is necessary for configuration changes or troubleshooting.

Command: | Description: |
systemctl status {service} | Display the current status of the service |
systemctl stop {service} | Temporarily stops the service |
systemctl start {service} | Temporarily start the service |
systemctl restart {service} | Restart a service after a configuration change |
systemctl enable {service} | Cause a service to start when the system boots |
systemctl disable {service} | Prevent a service from starting when the system boots |
![](https://cdn.thenewstack.io/media/2024/07/2f7ee41d-systemctl-status-sshd.png)
Processes are instances of running code. These may be parts of Linux itself or related to services and applications hosted on the system. Sysadmins [review these processes](https://thenewstack.io/linux-manage-system-processes/) during performance monitoring, security audits, troubleshooting, etc. Reviewing processes lets an admin know what’s happening on the Linux device.

Evaluating hardware and managing services is a vital skill for Linux users. If you’re using a learning plan to organize your Linux studies, work with these concepts and utilities as a single unit.

## Choose and Deploy a Linux Distribution
Microsoft and Apple only sell and maintain a small number of operating system versions. Due to its open source nature, Linux enables anyone to create [distributions](https://thenewstack.io/choosing-a-linux-distribution/), and it does not enforce OS versions with the same discipline as closed-source OSs. The result is that thousands of versions of Linux are available, and selecting one is often difficult.

The term *distribution* refers to a combination of a Linux kernel, various applications, and a purpose. Distributions are often specialized for a particular role, such as end-user workstation, web server, or IoT operating system. Choosing a distribution means finding (or creating) one that matches your purpose.

![](https://cdn.thenewstack.io/media/2024/07/8b9e7629-distrowatch.png)
You must also pay attention to [installation options](https://thenewstack.io/how-to-install-linux/). Will you install Linux on [bare metal hardware or a virtual machine](https://thenewstack.io/linux-choose-an-installation-platform/)? Will it be local or cloud-based? What processor will it rely on (Intel or ARM)? How much RAM, storage capacity, and network access will it require?

Finally, initiate the installation process. Most modern Linux distributions use an installation wizard to simplify the process.

Developing the knowledge to select and install a Linux distribution prepares you for deploying specialized Linux versions to users, servers, cloud environments, IoT ecosystems, and more.

## Maintain the System
Linux deployments may be around for years. It’s an extremely stable and long-lived operating system, making maintenance a key concern. In addition to the usual kernel and application updates, keep an eye on [storage capacity](https://thenewstack.io/how-to-manage-linux-storage/). This seems to be the one resource that always gets consumed. Files stored on a local Linux workstation or server may fill the storage space. High access times will annoy users, so keep storage capacity at reasonable levels and upgrade when necessary.

![](https://cdn.thenewstack.io/media/2024/07/e55d9ea0-df-h.png)
Log files maintain a record of system activity so you can evaluate performance, security, and general health. Make a habit of checking logs regularly. Centralizing log files for easier archiving and analysis across many systems is also a good idea. The Linux rsyslog service makes this process straightforward.

Package managers simplify application maintenance. One of the most confusing aspects of Linux for new users is that various distributions rely on different package managers. There really isn’t a universally agreed-upon tool for deploying, updating, and removing software. Plan to learn whichever package manager your chosen distribution uses.

Distribution: | Common package manager(s): |
Red Hat and related | dnf, yum, rpm |
Debian and related | apt |
SUSE and related | zypper |
Linux stores operating system, service, and application configurations in text files, so changing those settings means editing the files. Linux text editors were originally designed for command-line-only environments since graphical user interfaces are optional with most Linux distributions. It takes practice to gain proficiency with these text editors. At a minimum, learn to open, edit, save, and close text documents with [Vim](https://www.vim.org/) and [Nano](https://www.nano-editor.org/), the two most common editors found on most distributions.

## Configure Networking
Linux integrates into IP-based networks easily. Administrators may configure static or dynamic IP addressing and monitor networking with standard tools like [Nmap](https://nmap.org/) and [Wireshark](https://www.wireshark.org/). It’s also critical to allow and deny the correct traffic to and from the system using a firewall. Virtually all Linux distros include a firewall, though its interfaces vary. Most firewalls default to a “deny all” configuration, expecting administrators to manually specify exceptions for permitted traffic. Some firewalls assume a few basic protocols and leave ports open for those. The remote administration tool SSH is a great example.

![](https://cdn.thenewstack.io/media/2024/07/ff16665c-firewall-cmd-listall.png)
And speaking of SSH, implement key-based authentication for easier SSH connectivity. Key-based authentication also enables centralized configuration management, allowing automation tools to connect to remote systems without user intervention. This feature is critical for scaling resources, managing security, and deploying application versions.

Steps: | Description: |
ssh-keygen | Generate a unique public-private key pair |
ssh-copy-id remotehost | Copy the public key to the remote host |
ssh remoteuser@remotehost | Initiate a remote connection using SSH |
## Wrap Up
Be prepared for a significant effort if you plan to learn Linux. The payoff is big, however. You’ll be able to assemble a system that provides services to users, offers secure daily use, or [optimized for programming](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/). Mastering the command line gives you greater speed and automation opportunities, too.

Use the categories above as part of a learning plan, then develop the individual skills listed in each to maintain focus without being overwhelmed. When you’re comfortable with these topics, you can explore additional areas, such as web server configuration, automation, and more advanced storage options.

Remember that Linux is also the [primary cloud platform](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/). Many of the skills you’ll learn for physical Linux server management also apply to cloud VMs and [containers](https://thenewstack.io/alpine-linux-heart-docker/).

Start your journey toward Linux system administration today, and be ready to work with this powerful and versatile operating system.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)