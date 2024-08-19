# How to Manage a Linux Firewall
![Featued image for: How to Manage a Linux Firewall](https://cdn.thenewstack.io/media/2024/08/10729184-rowan-heuvel-yq0hnz6cqyo-unsplash-1024x683.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/)and
[installation platform](https://thenewstack.io/linux-choose-an-installation-platform/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/),
[file permissions](https://thenewstack.io/linux-how-file-permissions-work/),
[system processes](https://thenewstack.io/linux-manage-system-processes/), and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
Firewalls control access to networks and (potentially) network devices, including workstations and servers. Administrators rely on firewalls to permit or deny connections based on various criteria, including source, destination and protocol type.

Firewalls have the following three primary functions:

- Filter network traffic.
- Act as a gatekeeper between networks and network segments.
- Log and monitor network connection attempts.
Some firewalls offer additional functionality to allow more connection types. These features include:

- Network Address Translation (NAT) support to manage internal and external IP addresses.
- Virtual Private Network (VPN) endpoint support to allow secure connectivity.
These features help avoid malware by controlling connectivity. They also control access from internal and external clients to sensitive information. Finally, firewalls aid organizations in enforcing reliable, predictable and effective security policies to demonstrate compliance.

Some firewalls, including the Linux [firewalld](https://firewalld.org/) service, use predefined zones to set common rules. A firewall zone for a trusted network, such as the one at your home or business, will permit a different set of inbound connections than a zone for a public or untrusted network, which will probably not allow any inbound connections at all.

Firewall configurations almost always default to a “deny all” policy, meaning the firewall denies all inbound traffic, and the administrator configures exceptions for legitimate traffic. For example, if the firewall protects a network segment containing web servers, all traffic is blocked, and then the administrator opens ports 80 (HTTP) and 443 (HTTPS) explicitly.

Firewalls usually exist in two places: as a gatekeeper between networks or segments and as controllers of traffic in and out of individual devices.

- Network-based firewalls: Control access between networks or network segments to protect all data and devices in each segment.
- Host-based firewalls: Control connections to or from devices, helping to protect the data and services on each device.
Administrators may configure Linux systems as network routers and firewalls, though more efficient specialized hardware appliances exist for this function. However, basic Linux firewalls can be set to manage network control. You will usually configure a Linux firewall as a host-based solution to protect that specific device.

You can build a lab environment to practice with firewall settings by following the information found in the “[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)” piece. Refer to the “[Understand The Linux Command Line”](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) article if you need to review the syntax of Linux commands.

*Note: It is a poor security practice to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the sudo (super user do) command to elevate your privileges. You may be prompted for your password when using
sudo . Some commands in this tutorial may require the sudo command on your Linux distribution.*
## Understand How Firewalls Manage Network Traffic
Basic firewalls identify network traffic based on three criteria: source, destination and protocol. Firewalls accomplish this by examining addressing information found in TCP/IP communications. This data shows the sending device’s IP address, the destination system’s IP address and the communication protocol in use.

Suppose workstation3 with IP address 192.168.2.200 wants to establish an HTTP connection to webserver02 with IP address 192.168.2.10 . The firewall checks its rules to see whether the client device is allowed to send traffic to the destination server. It also checks the rules to see whether HTTP (port 80) traffic is allowed.

People tend to identify application layer services by protocol, such as the Hypertext Transfer Protocol (HTTP), Simple Mail Transfer Protocol (SMTP) or the Secure Shell (SSH). Network devices do not usually recognize these protocols by names but rather identify them by numeric values called port numbers. There are potentially over 65,000 possible port numbers, but only the first 1,023 are standardized. These are referred to as the “well-known” port numbers.

Here are a few common protocols and their well-known port numbers:

- Hypertext Transfer Protocol (HTTP): Port 80, web services
- Hypertext Transfer Protocol Secure (HTTPS): Port 443, encrypted web services
- Secure Shell (SSH): Port 22, secure remote administration
- File Transfer Protocol (FTP): Port 21, file transfers
- Simple Mail Transfer Protocol (SMTP): Port 25, email transfers
- Post Office Protocol v3 (POP3): Port 110, accessing email
- Internet Message Access Protocol (IMAP4): Port 143, accessing email
- Network Time Protocol (NTP): Port 123, time synchronization
- Remote Desktop Protocol (RDP): Port 3389, remote connectivity to graphical user interfaces
Some firewalls recognize these protocols by name, but you’ll often have to configure firewalls using port numbers, so it’s a good idea to memorize these.

## Common Linux Firewall Interfaces
The underlying firewall service for Linux is iptables or nftables. These are configurable parts of the Linux kernel capable of filtering network traffic. You’ll use a frontend application to manage these settings. There are several of these frontend programs, but two of the most common are listed below:

**Uncomplicated Firewall (UFW):**Straightforward if less advanced configuration.**firewalld**: More complex but with more configuration options.
The primary differences between them center on ease of use and advanced configurations. In addition, most Linux distributions that originate from Debian use UFW, while distributions derived from Red Hat usually rely on firewalld.

## Uncomplicated Firewall (UFW) Settings
The basic command syntax is the [ufw](https://manpages.org/ufw/8) command followed by one or more subcommands and configuration parameters. These tend to be pretty simple with UFW.

It may be a good idea to reset the UFW to its defaults if you’re on a Debian-based system where you’re unsure of the current configuration. I don’t recommend this on a production workstation or server, as it may disrupt communications.

Use the following commands to reset the inbound and outbound UFW settings:

123 |
$ sudo ufw default deny incoming$ sudo ufw default deny outgoing |
You should see a message indicating success for each command.
Network-based applications typically register themselves with UFW. Use the following command to display the registered applications:

1 |
$ sudo ufw app list |
The list will vary depending on the installed programs. Assume OpenSSH is installed for this tutorial.
Note that UFW allows specific sets of rules for specific interfaces. This is useful on servers with multiple network interface cards connected to different segments.

Enable the SSH service to pass traffic through the UFW firewall by using the following command:

1 |
$ sudo ufw allow OpenSSH |
This command works because OpenSSH is registered. UFW will allow SSH connections on port 22.
One possible security setting is changing the default port for various services. While port 22 is the well-known port for SSH, you can configure it to use a different port, such as 2222. In that case, you need to set UFW to recognize that port instead.

Define a specific port number as allowed in UFW with this command:

1 |
$ sudo ufw allow 2222 |
The final step is enabling UFW with the updated rules. Use these two commands to reset UFW:
123 |
$ sudo ufw disable$ sudo ufw enable |
Manage UFW log file settings with the
sudo ufw logging on command.
You can review your settings any time using the status subcommand:

1 |
$ sudo ufw status |
The above configurations permit inbound SSH connections from any workstation. However, SSH is mainly a sysadmin tool, so it’s likely only a limited number of workstations need to connect via SSH. Suppose you only want to permit SSH connections from the sysadmin workstation found at
192.168.2.42 . Use the following command:
1 |
$ sudo ufw allow from 192.168.2.42 to any port 22 |
The connection source is
192.168.2.42 (the admin computer), and the destination is
port 22 (SSH).
UFW allows many variations on this idea. For example, it recognizes subnets as a way of further focusing rules.

What about deny settings? UFW enables administrators to specify particular IP addresses (or subnets) from which to block communications. This might be useful when a given system needs to be explicitly blocked from access, or DDoS attacks originate from a particular host. An example of this kind of rule is:

1 |
$ sudo ufw deny from 192.168.2.200 |
To summarize, begin by checking the current UFW settings before adding or removing rules to control access. Enable the settings when you’re done. Here are the steps:
- List the current rules: sudo ufw status
- Add any necessary rules: sudo ufw allow OpenSSH
- Review the updated rules: sudo ufw status
- Reload the UFW configuration: sudo ufw disable followed by sudo ufw enable
![](https://cdn.thenewstack.io/media/2024/07/793f8336-openssh-status.png)
The primary configuration file for UFW is /etc/default/ufw , which allows you to define default policies, etc.

## Firewalld Settings
Linux distributions derived from [Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)tend to rely on the firewalld interface to manage connectivity. This utility uses the [firewall-cmd](https://manpages.org/firewall-cmd) command with a series of flags to define your settings. However, the overall functionality is the same as with UFW — define which connections are allowed and which are not. You can do this by service name, protocol or port number.

The
firewall-cmd command manages firewalld settings. This command contains many flags to display and configure rules. Notice that these flags use two dashes (
--option ), whereas many other Linux command options use only a single dash (
-option ). Use an
= character to define the parameter or setting.

1 |
$ sudo firewall-cmd --list-all |
![](https://cdn.thenewstack.io/media/2024/07/ed38734c-firewallcmd-list-all.png)
This example displays the current rules for the current zone. More examples follow below, including some with parameter settings.

Firewalld uses zones to define different roles or types of access. These zones have different default rules, and any custom rules you create are also zone-specific. Use the zones to make the firewall configuration easier, especially for devices that change location or purpose in the network.

Some of the common zones include:

- Home
- Work
- Internal
- DMZ
[Docker](https://www.docker.com/?utm_content=inline+mention)- Public
The Public zone is usually the default for most installations. If you don’t specify a zone, the system assumes the default zone. Set the default zone by using the --set-default-zone=internal setting.

Firewalld allows you to set zones on a per-interface basis, which is helpful for servers connected to multiple subnets. For example, you might have a department Linux webserver set to the Work or Internal zone and an Internet-facing Linux webserver configured for the Public zone.

Display the current zones on the system by using the
--get-active-zones subcommand:

1 |
$ sudo firewall-cmd --get-active-zones |
List all zones on the system with the
--get-zones option:
1 |
$ sudo firewall-cmd --get-zones |
![](https://cdn.thenewstack.io/media/2024/07/9641714d-firewallcmd-get-zones.png)
These are all the existing zones on your system.

Display a detailed list of zones and their rules with this command:

1 |
$ sudo firewall-cmd --list-all-zones |
You can assign a zone to each network interface card in the Linux system. Begin by using the
ip addr command to display the existing interfaces:
1 |
$ sudo ip addr |
Then run the command below to set an interface to the public zone:
1 |
$ sudo firewall-cmd --change-interface=enp0s5 --zone=public --permanent |
![](https://cdn.thenewstack.io/media/2024/07/91ecbee2-changezones.png)
Firewalld identifies potential connection types by associating them with specific services. Examples include ssh, http, https, etc. If these services do not match your needs —perhaps you have custom applications or services using non-standard port numbers — you can create whatever custom rules you need.

The following are some common configuration options:

- --permanent
- --zone=
- --add-service=
- --add-port=
- --remove-service=
- --remove-port=
- --reload
I cover the use of these options below.

Pay particular attention to the --permanent option. Using it makes the entries persist through reboots. If you don’t include that option, firewalld assumes you’re making a temporary rule change for the current runtime.

I used the SSH service above in the UFW example. I’ll do the same here with firewalld.

1 |
$ sudo firewall-cmd --zone=public --add-service=ssh --permanent |
You may use custom port numbers for in-house network applications. You could also try to hide network services by using a different network port from the default (for example, setting SSH to port 2222 instead of 22). If you need to define settings by port number, use the
--add-port= option. Here’s the same example for SSH’s port 22:
1 |
$ sudo firewall-cmd --zone=public --add-port=22/tcp --permanent |
Notice the port number value also shows the
tcp Transport layer protocol.
![](https://cdn.thenewstack.io/media/2024/07/654b1574-add-ssh-service.png)
![](https://cdn.thenewstack.io/media/2024/07/06780bc5-add-ssh-port.png)
View your settings by using this command:

1 |
$ sudo firewall-cmd --list-all |
Note that SSH is usually permitted by default anyway.
Use the same syntax with the
--remove-service=ssh or
--remove-port=22/tcp flags to delete an entry. For example, to block the SSH service, type this command:

1 |
$ sudo firewall-cmd --zone=public --remove-service=ssh --permanent |
Your specified firewalld settings do not go into effect immediately. Firewalld assumes you need time to create, edit or delete various entries in the rules. Once you’ve fine-tuned your configuration, use the
--reload option to implement the changes.
1 |
$ sudo firewall-cmd --reload |
![](https://cdn.thenewstack.io/media/2024/07/60c162f5-reload.png)
Remember, if you don’t include the --permanent flag with your rules, they will not persist after the next reboot.

Here is a summary of the basic configuration. Review the settings, add or remove rules and reload the configuration. Use the following steps as a guide:

- List the current rules: sudo firewall-cmd --zone=public --list-all
- Permanently add any necessary rules: sudo firewall-cmd --zone-public --add-service=ssh --permanent
- Remove any rules that no longer apply: sudo firewall-cmd --zone-public --remove-service=http --permanent
- Review the new settings: sudo firewall-cmd --zone=public --list all
- Reload the firewall to update the settings: sudo firewall-cmd --reload
## What About Graphical Firewall Interfaces?
It’s often easier to work with system configurations using a graphical interface. Command line tools are fast and scriptable, but only if you remember the specific commands. A graphical tool may be best if you’re sitting at a Linux workstation with a graphical user interface (GUI) and you just need to add a firewall rule quickly.

Both UFW and firewalld have GUI options available.

### The GUFW Interface
Use the following steps if GUFW is not already installed on your Debian-based distribution. You must add the universe repository, update the Apt configuration, and install the package. Here are the commands:

123 |
$ sudo apt add-apt-repository universe$ sudo apt update$ sudo apt install gufw -y |
After the installation, access the new GUI firewall interface by searching for GUFW.
![](https://cdn.thenewstack.io/media/2024/07/8156cb55-search-gufw.png)
You can enable and disable the firewall (think carefully before disabling it). You can also change profiles. Your choices are Home, Office, Public and Custom. These resemble firewalld zones. Finally, add or remove rules to permit or deny specified traffic.

![](https://cdn.thenewstack.io/media/2024/07/50dac73c-gufw-profiles.png)
![](https://cdn.thenewstack.io/media/2024/07/60b538fd-gufw-open22.png)
### The firewall-config Interface
Add the firewall-config utility to configure the firewall using a graphical interface if you’re on a Linux distribution related to Red Hat Linux.

Use this command to install
firewall-config :

1 |
$ sudo dnf install -y firewall-config |
Search for the term “firewall” to find the GUI firewall console.
![](https://cdn.thenewstack.io/media/2024/07/c811d840-firewall-gui.png)
The interface displays the available zones (the same as those found with the command-line firewall-cmd tool). Select a zone, then use the checkboxes for each listed service to permit or deny access.

![](https://cdn.thenewstack.io/media/2024/07/05442412-firewall-config-gui.png)
## Test Firewall Configurations
It’s a good idea to test your firewall settings, too. Obviously, you can read the rules and logic out what effect they should have on inbound connection attempts. This is certainly valid for basic auditing and confirmation. However, you should also test the allowed connections from remote systems to ensure the services that *should* have access actually *do* have access. Finally, consider using a network scanning application like [Nmap](https://nmap.org/) to validate the settings. This approach is more efficient than checking connectivity from lots of remote devices.

## Wrap Up
Firewalls are important components of a layered approach to security. Monitor and test firewall configurations regularly to ensure network services and systems are properly secured.

In most cases, Linux workstations and servers should use host-based firewall configurations to permit only necessary inbound connections. The connections will vary depending on the device’s role, such as webserver or database host. Firewalls typically default to a “deny all” configuration.

Some administrators use Linux systems as routers between network segments. The firewall mechanism supports this role too.

You must know which firewall interface is available on your selected distribution.

- UFW: Found on Debian-based systems, including Ubuntu, Linux Mint and Debian itself.
- firewalld: Found Red Hat-based systems, including Red Hat Enterprise Linux (RHEL), Fedora,
[AlmaLinux](https://thenewstack.io/almalinux-makes-in-place-upgradeseasier-for-centos-users/)and[Rocky Linux](https://thenewstack.io/post-centos-rocky-linux-fights-for-community-driven-enterprise-open-source/).
Evaluate what types of connections are necessary to the device, then review the existing firewall rules to ensure they match. If they do not, add or remove rules until only required connections are allowed. Don’t forget to enable the settings and make them persistent through reboots.

There’s certainly nothing wrong with managing firewall settings via a graphical interface, especially on end-user devices, such as laptops. The interface you use will vary by distribution.

- GUFW: For UFW-based systems, such as those derived from Debian.
- firewall-config: For firewalld-based systems, such as those derived from Red Hat Linux.
Begin today by reviewing and modifying your current firewall configurations to ensure secure, controlled connections to your Linux devices.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)