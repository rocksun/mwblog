# Linux: SSH and Key-Based Authentication
![Featued image for: Linux: SSH and Key-Based Authentication](https://cdn.thenewstack.io/media/2024/07/8631cdfe-sea-snail-345678_1280-1024x682.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/)and
[installation platform](https://thenewstack.io/linux-choose-an-installation-platform/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/),
[file permissions](https://thenewstack.io/linux-how-file-permissions-work/),
[system processes](https://thenewstack.io/linux-manage-system-processes/), and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
The Secure Shell (SSH) is a critical remote administration tool for Linux systems and network devices. It’s also essential for macOS access and is often added to Windows computers (or used in conjunction with PowerShell). I’ll demonstrate concepts and configurations using [OpenSSH](https://www.openssh.com/).

SSH’s primary benefits include the following:

- Remote access to a wide variety of platforms.
- Remote command execution.
- Default installation on most Linux distributions.
- Strong authentication mechanisms.
- Support for secure file transfers, such as SCP and SFTP.
- Provides tunneling for other non-secure applications.
- Enhances automation and scripting.
Learning to leverage SSH is an essential Linux sysadmin skill. This article covers basic SSH configurations, password-based authentication and general security settings. It also shows how to improve SSH functionality with key-based authentication for better remote administration and integration with automation tools.

SSH helps mitigate eavesdropping attacks by encrypting authentication and network traffic. It’s a critical means of protecting administrative connections to servers, routers, switches, IoT devices and even cloud connections.

This article provides commands for managing remote Linux systems. I suggest using a [Linux lab environment](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) when completing these exercises. Review [Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) to work with these commands better.

## Establish an SSH Connection Using a Password
You might already know the basic SSH syntax for connecting to remote machines. Use the
ssh command and target a particular hostname or IP address:

1 |
$ ssh server07 |
Enhance the command by including the username for the remote user account you want to authenticate. For example, to connect using remote user **admin03**, type:
1 |
$ ssh admin03@server07 |
SSH prompts you to enter the password of the user account hosted on the remote system. On most systems, the command prompt will change to show the hostname of the remote computer.
At this point, you can begin executing Linux commands and run any programs installed on the remote device, such as [Vim](https://www.vim.org/), [Apache](https://apache.org/), or [MariaDB](https://mariadb.org/). Remember that you may need to use
sudo to elevate your privileges on the remote system.

Once you complete your remote administration tasks, type exit or logout to disconnect the SSH session.

### Common SSH Use Cases
There are plenty of examples for using remote SSH connections, including:

- Run remote backups with Duplicity, Kopia, tar or other tools.
- Compile or install applications using compilers or package managers.
- Modify system and application configuration files for web and database services.
- Restart services. (Remember, you’ll be disconnected if you restart network or firewall services.)
However, the above use cases only allow for manual remote administration, where the administrator connects to one system at a time and runs commands (or scripts). It also means passwords must be tracked and maintained, which could be challenging when dealing with multiple remote devices.

Modern SSH implementations offer a far more robust way of proving your identity called key-based authentication. Implementing key-based authentication initially simplifies authentication for remote administration, but it is especially critical for automation functions.

Key-based authentication allows automation tools to authenticate to remote systems without requiring an administrator to type a password (or store a password in a configuration file). I examine this idea in more detail below.

## What Is Key-Based Authentication?
Key-based authentication is a major improvement in SSH authentication, and it replaces password authentication. It relies on asymmetric key cryptography. This method relies on two mathematically related keys. Each key plays a specific role. The keys are:

- Public key: This key can be transferred to remote systems across the network. Any data encrypted with the public key can only be decrypted with the related private key.
- Private key: This key remains securely stored on the local device and never traverses the network. Any data encrypted with the private key can only be decrypted with the public key.
You’ll generate a public-private key pair on the administration workstation (the administrator’s local computer), then copy the public key to one or more remote servers.

During the connection attempt, the remote server encrypts a message challenge using the admin workstation’s public key. This message can only be decrypted with the admin workstation’s private key. If the workstation decrypts the challenge and replies with the correct information, the remote server knows its identity is confirmed.

The asymmetric keys are much harder to guess or brute-force than standard passwords, making this approach far more secure and reliable than passwords that may be based on predictable words or phrases.

## Configure Key-Based Authentication for SSH
Implementing key-based SSH authentication is straightforward. The general steps are generating a key pair, copying the public key to the remote device and testing the connection.

Here is an explanation of the steps:

- Generate the key pair using the
ssh-keygen command. It creates two hidden files in the current user’s home directory. The files are
~/.ssh/id_rsa (private key) and
~/.ssh/id_rsa.pub (public key). You’ll typically press
**Enter**through the interactive prompts. - Copy the public key to the remote SSH device using the
ssh-copy-id command with the specified user. You must enter your password during this step, but this is the last time you’ll do so. The utility also prompts you for a
**yes**or**no**confirmation. The public key file will reside in the ~/.ssh/authorized_users file on the remote host. - Test the connection by typing ssh admin03@server07 (substitute your own credentials and hostname). The remote system should not challenge you for a password. The authentication is silent.
You’ll establish authenticated remote connections using the key pair from this point forward.

The following list summarizes the commands:

123 |
$ sudo ssh-keygen$ sudo ssh-copy-id admin03@server07$ sudo ssh admin03@server07 |
![](https://cdn.thenewstack.io/media/2024/07/94942803-ssh-keygen.png)
When you generate the key pair, you’ll be offered the chance to add a passphrase. You can also specify encryption algorithms and key sizes at this time. Most administrators will press **Enter** through these prompts, bypassing additional passphrase access.

After you copy the client’s public key to the remote server, you’ll no longer be challenged for a password during the connection attempt. Type the regular SSH connection command and the authentication process silently succeeds.

### Use Key-Based Authentication for General Administration
The initial benefit of key-based authentication is simplicity. You’ll no longer be challenged for difficult-to-remember passwords. Authentication happens silently. The process is quicker, and you can begin your admin tasks immediately.

This is especially handy when you use SSH to quickly run a single remote command without manual intervention, such as:

1 |
# ssh admin03@server07 'run-backup.sh' |
There’s no question this quicker authentication is helpful, but the real benefit of key-based SSH authentication occurs when automation gets involved.
### Use Key-Based Authentication with Automation
SSH connectivity continues to be relevant in modern DevOps and Infrastructure as Code (IaC) environments. Many configuration management utilities must connect to remote systems to inventory software, manage settings, or initiate software testing. These tools must still authenticate to the remote systems if they use SSH.

Early approaches paused the configuration management tasks until administrators manually entered passwords. Clearly, that method does not enhance automation. Other designs embedded passwords or other authentication information directly in management files, risking accidental exposure to anyone who could access the files (or instances of the files, such as those found in backups).

Modern configuration management tools that use SSH can take advantage of key-based authentication to establish remote connections for a completely zero-touch solution.

Here are just a few automated configuration management tools that can use SSH connectivity:

[Ansible](https://thenewstack.io/install-ansible-on-ubuntu-server-to-automate-linux-server-deployments/)- Chef
- Puppet
Implementing key-based authentication means remote connections can be defined within these configuration management tools, and they’ll run without pausing for a manually entered password. There is no need for user intervention, which is essential when configuration management tasks run in the middle of the night or during scale-up incidents.

Another benefit of using keys for authentication is avoiding the need to embed passwords in deployment and configuration files. This risky practice can easily expose passwords for admin accounts.

### Use Key-Based Authentication with Multiple Remote Servers
What if the admin workstation actually needs to connect to multiple remote SSH servers. You could maintain separate key pairs for each, but this would be very tedious. With a few quick configuration file edits, you can use the same key pair to authenticate to multiple remote devices. This approach even supports different connection options for each target system.

The steps to configure the local system for key-based authentication to multiple target servers begin in the same way as above. However, do not generate new key pairs for each connection. Each time you run the ssh-keygen command it overwrites the existing key pair. You’ll use the same public and private keys for all connections.

The first two steps in the process are:

- Generate a key pair on the local system using the ssh-keygen command.
- Copy the new public key to each remote server using the ssh-copy-id command.
The most significant configuration change when dealing with multi-server connections is editing the client’s user-specific local SSH configuration file. Create (or edit) the ~/.ssh/config file. You have several choices, including:

- Hostnames.
- Client identity files for various private keys.
- Alternate port numbers.
For example, you might set up the following configuration to connect to various remote systems using a single private key named
id_rsa:

123456789 |
Host server07 Hostname server07 User admin03 IdentityFile ~/.ssh/id_rsaHost server09 Hostname server09 User admin03 IdentityFile ~/.ssh/id_rsa |
Finally, test the key-based authentication connection to ensure it can reach the remote device and to ensure the correct settings.
## Configure Additional SSH Security Settings
SSH includes various other options to enhance security and customize its use in your environment. The primary SSH server configuration file is usually stored at /etc/ssh/sshd_config. It contains many entries. Review the comments and best practices carefully.

Here are some standard security configurations you may consider implementing.

- Set SSH to refuse password-based authentication:
**PasswordAuthentication no.** - Set SSH to refuse direct root logins across the network:
**PermitRootLogin no.** - Change the default SSH port from 22 to a non-standard port to control connectivity.
- Set a banner warning message.
- Configure idle times to reduce hung connections. (Be careful of this setting with configuration managers, as it may be difficult to anticipate how long they will need to be connected.)
It’s poor security practice to log on to a local or remote Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the [sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You might be prompted for your password when using
sudo.

The **PermitRootLogin no** configuration mentioned above is a great way of enforcing this. You’ll establish the connection by authenticating with a non-privileged user on the remote SSH target, then elevate your privileges using
sudo on that box. Combine this method with key-based authentication to manage SSH security better.

![](https://cdn.thenewstack.io/media/2024/07/9cf38e87-norootlogin.png)
### Configure the Firewall for SSH
Remember to update your firewall settings. If SSH was preinstalled and running with your Linux distribution, the firewall is probably already open for port 22. If you have to add it, don’t forget to update the firewall rules to permit remote connections.

If you will only manage the server from a single admin workstation or jump box, restrict inbound SSH connections to that device’s identity only. That prevents SSH connections from any other network node.

![](https://cdn.thenewstack.io/media/2024/07/3ffb19e9-firewall.png)
### Audit Log Files for SSH Connections
Audit log files regularly for remote SSH connections to identify any unauthorized connections or repeated failed connection attempts. These may indicate users or malicious actors attempting to access the remote server.

If you manage several remote Linux servers using SSH, consider centralizing your log files using rsyslog. Doing so makes reviewing SSH connections easier, helping you verify that only authorized connections occur.

## Wrap Up
Linux and network administrators rely on SSH for secure, convenient access to remote systems. It’s an essential part of their toolboxes. Password-based authentication to a few remote devices is viable, but it’s not convenient when implementing automation with lots of target servers.

Integrating SSH into your larger CI/CD and orchestration pipelines provides a simple, secure solution for remote connectivity. SSH functions with Linux, macOS, Windows and many network devices (routers, switches, etc.), making it a standard administration utility.

Start today by auditing your current SSH communications, then implement key-based authentication and automate as many configurations as possible. You might just find your environment is more secure and easier to work with.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)