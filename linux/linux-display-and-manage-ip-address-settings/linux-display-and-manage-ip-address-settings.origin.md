# Linux: Display and Manage IP Address Settings
![Featued image for: Linux: Display and Manage IP Address Settings](https://cdn.thenewstack.io/media/2024/08/5b178800-humboldt-penguin-7283765_1280-1024x682.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/)and
[installation platform](https://thenewstack.io/linux-choose-an-installation-platform/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/),
[file permissions](https://thenewstack.io/linux-how-file-permissions-work/),
[system processes](https://thenewstack.io/linux-manage-system-processes/), and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
Modern computers and their users rely on network connectivity for nearly everything, including cloud-based applications, software access, data access and communication. It seems that every aspect of computing relies on networking. Linux workstations and servers are no different in this necessity than Windows or macOS systems.

One of a Linux sysadmin’s primary responsibilities is ensuring network connectivity. This requires understanding the system’s identity on the network and configuring it to participate in network data exchanges.

Linux systems have three identities on a network. Various network devices use each identity differently.

Here are the three identities with a summary of their use:

**Hostname**: A human-friendly name providing users and administrators with an easy way to identify a node.**IP address**: A logical address routers and network configuration tools use to identify the system.**MAC address**: A physical address on the network interface card (NIC) that uniquely identifies it to switches and other Layer 2 devices.
For example, a computer’s three identities might look like this:

- Hostname: computer27
- IP address: 192.168.2.200
- MAC address: 00:1c:42:73:8d:f2
The use and function of these three network identities are assumed knowledge for this article. Be sure to review basic network information if you need a refresher. You may want to [construct a lab environment](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) to practice the commands covered in this article. Refer to [this article](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) if you need to review basic Linux command syntax.

Avoid logging on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the sudo (super user do) command and your password to elevate your privileges. Some commands in this tutorial may require the sudo command on your Linux distribution. You must also use sudo to open text editors with elevated privileges to manage the network configuration files.

$ sudo vim /etc/resolv.conf

This article examines the use and configuration of the three network identities by giving command examples and offering ways to maintain network settings easily.

## Display System Identities
Use the hostname command to display the system’s human-friendly name. This is almost certainly the only way end users will recognize their computer. The hostname may be part of a larger naming structure called a fully qualified domain name (FQDN), indicating the system’s position in a hierarchical naming structure.

1 |
$ hostname |
![](https://cdn.thenewstack.io/media/2024/07/ed3aba05-hostname.png)
A single command also displays IP and MAC addresses, though the output is much less straightforward. Use the
ip addr command to display information about each network interface in the system. Remember that each will have its own unique IP and MAC address. Servers often contain two or more NICs for redundancy or connectivity to multiple segments.

1 |
$ sudo ip addr |
![](https://cdn.thenewstack.io/media/2024/07/1674b903-ipaddr.png)
Older Linux systems used the ifconfig command for this purpose.

How were these values selected and assigned? Administrators configure hostnames when installing the operating system. IP addresses may be manually configured by administrators or dynamically assigned by Dynamic Host Configuration Protocol (DHCP) servers. MAC addresses are hard-coded by their manufacturer. Of these, you’re only likely to change a system’s hostname and IP address, which will probably happen rarely.

Even simple networks get unwieldy quickly, so many IT departments document these configurations for easy reference during troubleshooting.

## Manage the System Hostname
The system hostname is typically set when installing Linux. Larger organizations often use a specific naming convention that indicates the system’s role or use in the network. Smaller companies may use simple names. Regardless, the system name must be unique in the environment.

Display the current hostname by typing the hostname command.

Temporarily change the system’s hostname to
comp99 by typing this command:

1 |
$ sudo hostname comp99.mycompany |
However, this name assignment will be lost when the system reboots next.
If you need to permanently change the hostname after installing the OS, use the
hostnamectl command. Suppose you need to set the new hostname as
comp42 in the
mycompany domain. Use the following command:

1 |
$ sudo hostnamectl set-hostname comp42.mycompany |
![](https://cdn.thenewstack.io/media/2024/07/b41b173d-set-hostnamectl.png)
This method makes the change persist through reboots. The hostnamectl command modifies the /etc/hostname file, so you don’t need to find and edit it directly.

Changing a system’s hostname means that any script, network mapping, or user that references by name will no longer be able to do so. Because of this, it’s generally not recommended to reference systems by their hostnames. IP addresses are often a better way to refer to network servers, printers and other devices.

## Manage the System IP Address
Administrators are responsible for assigning IP addresses. They may accomplish this by manually entering a unique IP address on each system in the network (very tedious) or by configuring a server with a pool of addresses from which workstations can lease an IP configuration. Most administrators use a combination of these two approaches by assigning servers and other essential network devices static IP addresses and having workstations and end-user devices lease configurations from a server.

### Static IP Address Configuration
Static IP addresses are useful for network nodes that require a consistent and unchanging IP address identifier. Linux servers are a great example of this, as are printers, routers and other infrastructure devices. Manually typing an IP address configuration is time-consuming, and the configuration cannot tolerate typographical errors or duplicate IP address assignments, making this approach very inefficient on a large scale for workstations and client devices.

Since there tend to be fewer servers and similar devices, static assignments work well for these. You can set a temporary IP address that disappears after a reboot or a persistent setting the system retains unless you change it.

Assign a temporary IP address to the eth0 network interface by using the following command:

1 |
$ sudo ip addr add 192.168.2.200/24 dev eth0 |
![](https://cdn.thenewstack.io/media/2024/07/1ed4ea65-tempip.png)
Remove the static IP address by using the
del subcommand, as seen below:

1 |
$ sudo ip addr del 192.168.2.200/24 dev eth0 |
Note that the commands above do not permanently set the IP address. They only apply to the current runtime and do not persist across reboots.
You’ll probably find that the [NetworkManager](https://www.networkmanager.dev/) component of Linux networking is easier for handling network configuration. The tool uses the
nmcli command to manage network settings rather than directly editing network configuration files and restarting network services.

Type the
nmcli command with no flags to see whether NetworkManager is installed:

1 |
$ sudo nmcli |
![](https://cdn.thenewstack.io/media/2024/07/2b0f735c-nmcli.png)
Not all distributions use nmcli, but most distros related to Red Hat do. If necessary, use the distribution’s package manager (probably APT or DNF) to install NetworkManager. For Debian-type systems, enter sudo apt install network-manager . On Red Hat-related systems, enter sudo dnf install NetworkManager .

View the network devices to identify the device name you want to work with:

1 |
$ sudo nmcli device status |
![](https://cdn.thenewstack.io/media/2024/07/13c6a553-nmcli-dev-status.png)
Suppose the output shows a network interface device named
enp0s5 . Use the following
nmcli command to configure the
eth0 interface with a static IP address of 192.168.2.200, a subnet mask of /24, and a default gateway of 192.168.2.1:

1 |
$ sudo nmcli con add con-name "static-connection" ifname eth0 type ethernet ip4 192.168.2.200/24 gw4 192.168.2.1 |
![](https://cdn.thenewstack.io/media/2024/07/b0ae2e99-staticip.png)
Reload the interface using these
nmcli commands:

123 |
$ sudo nmcli con down eth0$ sudo nmcli con up eth0 |
Modifying the network configuration files is another way to make the IP address persistent. These files vary by distribution, but here are two common examples.
On Red Hat and similar distributions, use a text editor to edit the following files:

123 |
/etc/sysconfig/network/etc/sysconfig/network-scripts/ifcfg-eth0 |
Edit the
/etc/sysconfig/network file with the settings for the hostname, default gateway and IPv6 configurations.
Modify the /etc/sysconfig/network-scripts/ifcfg-eth0 file with the appropriate IP address, subnet mask, gateway (default gateway) and at least one DNS server address.

You should restart the networking service using the sudo systemctl restart network command. Like other commands, this one may vary on different distributions.

Debian and its related distributions (Ubuntu, Mint, etc.) use the [Netplan](https://ubuntu.com/server/docs/about-netplan) configuration to manage networking. You specify the same kind of information as you do with Red Hat-derived distros. Netplan is an interface to NetworkManager that configures network settings using YAML files.

Edit the default file in the /etc/netplan directory to add settings for your network interface. Note that this file is in YAML, which is very picky about syntax (especially spaces). Remember to run the text editor using sudo to elevate your privileges.

Here’s a sample of the entry for the
enp0s5 interface. Just replace the IP settings with the appropriate values for your network. The
dhcp4: no parameter sets this as a static IP address. This line will read dhcp4: true if the system is currently a DHCP client.

12345678910111213 |
ethernets: enp0s5: dhcp4: no Addresses: [192.168.2.200/24] Gateway: 192.168.2.1 Nameservers: Addresses: [192.168.2.10, 192.168.2.11] |
Save and close the file, then run this command to update the settings:
1 |
$ sudo netplan apply |
Confirm the IP address is correct with the
ip addr command (or try the
hostname -I command).
Be careful editing the [YAML document](https://yaml.org/spec/1.2.2/#chapter-1-introduction-to-yaml). YAML is very particular about spacing, so be sure to match the template.

If you want to make the system a DHCP client rather than maintain a static IP address configuration, edit the file by removing the addresses and nameservers lines, then set the DHCP line to dhcp4: true . The system will then be a DHCP client.

### Use the Graphical Interface for Static IP Configuration
The network settings graphical user interface includes a Manual option that allows administrators to configure IP address, subnet mask, gateway and DNS server entries. Be very careful to avoid typographical errors here. You must also remember that no systems on your network can have the same IP address, so careful documentation of statically assigned IP addresses is required. This configuration tool is similar among various distributions because the same network settings are always needed.

![](https://cdn.thenewstack.io/media/2024/07/468baae5-gui-static-ip.png)
### Dynamic IP address Configuration
End-user workstations rarely have to be discovered by other systems on the network. Since business data is typically stored and shared from Linux file servers, there should be little content on user systems that other systems must reference. Therefore, it’s not necessary to have permanent static IP addresses. Having these devices acquire IP addresses from a central server is far more efficient.

The Dynamic Host Configuration Protocol (DHCP) service enables administrators to define a server with a pool of available IP addresses and all their related settings (subnet mask, default gateway/router, etc.). During the boot process, DHCP client devices send a network broadcast requesting the use of an IP address. The DHCP leases an IP configuration to the client. This process is less difficult, more flexible and quicker than static configurations by administrators. It is also less error-prone.

The DHCP lease generation process consists of four steps initiated by the client system. These steps allow the client to request IP settings and let the DHCP server respond.

Here are the steps:

- DHCPDiscover: A broadcast by the client device asking for a DHCP server.
- DHCPOffer: A response by the DHCP server offering an IP address configuration.
- DHCPRequest: A formal request by the DHCP client to use the offered IP address configuration.
- DHCPAck: An acknowledgment of the assigned configuration by the DHCP server.
The client device periodically checks in with the DHCP server to renew the IP address lease.

Most client devices assume they will be DHCP clients, so that’s usually the default setting. From an end-user’s perspective, this means their computer is self-configuring for network connectivity. You’ll probably leave your Linux system as a DHCP client, whether in a home environment or business network. For example, a Linux laptop will be a DHCP client when connecting to the wireless network at a coffee shop and your home. You want your laptop to configure itself for whatever environment it’s in.

To configure a host as a DHCP client using NetworkManager, type the following command:

1 |
$ sudo nmcli con modify eth0 ipv4.method auto |
Reload the interface with the following
nmcli commands:
123 |
$ sudo nmcli con down eth0$ sudo nmcli con up eth0 |
As mentioned above, to set a Debian-based distribution as a DHCP client, edit the interface file in the
/etc/netplan directory with the following entry:
1 |
dhcp4: true |
### Use the Graphical Interface for DHCP
The graphical network configuration tool offers various options, including an Automatic (DHCP) or Manual (static) setting. The Automatic setting configures the system as a DHCP client, enabling it to go through the lease generation process described above.

![](https://cdn.thenewstack.io/media/2024/07/bcdb4c2f-rh-gui-dhcpclient.png)
Most distributions have a very similar GUI network configuration tool. These settings are always required, so any graphical tool should be easy to interpret.

## Default Gateway Configuration
The primary settings provided by a DHCP server are the client’s IP address and subnet mask. However, the DHCP server will probably also include a default gateway value. This value is the IP address of the router on the subnet. Client computers don’t require a router to communicate with other nodes on the same subnet, but they do need a router for connectivity with machines on other subnets. If a system needs to send information to a node with a different network ID than its own, it forwards the message to the router. The default gateway value lets the computer know where the router is in this process.

The gateway IP address is part of the IP address setting provided by the DHCP server. If an administrator configures IP addressing manually, they must set the gateway value as part of that configuration.

## Configure Name Resolution
The relationship between hostnames and IP addresses is critical. Most people refer to systems by their hostnames, but most network devices recognize the IP address to manage communication. It would be very difficult for end users to remember that 172.16.33.58 is the “color-sales-printer” or 192.168.2.10 is the “dev-dept-fileserver.” Imagine if you had to keep track of all your favorite Internet sites by their specific IP addresses!

Name resolution refers to storing and using information about which hostnames are related to which IP addresses.

The Domain Naming System (DNS) provides name resolution. This service maintains a database of hostnames and IP addresses. If a user types in a command containing a hostname, such as ping server07 , their workstation queries DNS, asking for the IP address for server07 . The computers cannot communicate based on hostnames; TCP/IP communications require IP addresses. However, since IP addresses are challenging for people to remember, they need to be able to refer to systems by name. DNS relates these two values so that the network node and the user can work with the correct data.

Suppose you tell your computer to ping server07 . Since it doesn’t know what to do with this name, it asks the DNS server, which responds with the appropriate IP address.

The process basically looks like this:

- User types ping server07
- Their workstation doesn’t know what server07 is, and it needs an IP address
- The workstation sends a query to the DNS server, asking, “What is the IP address for server07?”
- The DNS server checks its resource records until it finds a record showing “server07 = 192.168.2.22”
- The server responds to the workstation, stating, “The IP address for server07 is 192.168.2.22”
- The workstation runs ping 192.168.2.22
The workstation must know the DNS server’s IP address so it can send the query. This setting is critical for computers. The DHCP server usually provides it, along with the computer’s IP address, subnet mask, and default gateway.

The above example assumes name resolution on an internal business network. Accessing websites on the internet uses a more complicated variation of the process. The concepts are similar, but more DNS servers are involved.

DHCP servers typically provide DNS server IP addresses as part of the standard IP address settings leased to the client device.

If you’re managing a static IP address configuration on your server, you should set the DNS server IP addresses. You can statically configure DNS servers for the client to query using the
nmcli command. Here’s an example:

1 |
$ sudo nmcli con mod "static-connection" ipv4.dns "192.168.2.10,192.168.2.11" |
To configure the client device manually to query a DNS server, edit the
/etc/resolv.conf file. You’ll typically specify two DNS servers (name resolution is important enough to justify multiple servers).
Edit the two nameserver lines with the IP addresses of your DNS servers.

![](https://cdn.thenewstack.io/media/2024/07/6d81ad6b-nameservers.png)
Be sure to use
sudo to elevate your privileges when editing this file. For example, to use Vim to edit the name resolution file, type:

1 |
$ sudo vim /etc/resolv.conf |
## Display the System’s MAC Address
You can use the ip command to display the NIC’s MAC address. Doing so may be useful during troubleshooting or when documenting a system’s configuration, but it’s not a setting you’ll often change or use yourself.

Various commands exist to show the MAC address for each network interface card installed on the system. Here are a few examples:

- ip addr : Displays lots of NIC information, including IP address and MAC address.
- ip link show : Displays the MAC address, MTU size and the status of each NIC.
- ip link show eth0 : Displays the MAC address, MTU size and status of the specified NIC (eth0 in this example).
![screenshot of the IP link command.](https://cdn.thenewstack.io/media/2024/08/33675a7c-ip-link-show.png)
Figure 11: The IP link command is one of several that displays the MAC address.

Discovering your system’s MAC address can be helpful when working with tools like [Nmap](https://nmap.org/), [tcpdump](https://www.tcpdump.org/) and [Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/). These troubleshooting utilities display detailed network information, including MAC addresses. You might need to determine where packets originate or what NIC is sending error packets on the network.

When sending information, computers add their own MAC address to data frames. They also add the destination computer’s MAC address. The source computer must discover the MAC address of any destination systems on the same network segment. They find this information using the Address Resolution Protocol (ARP). Each computer also caches (temporarily saves) MAC addresses it discovers for efficiency. You can view and clear this cache.

View the MAC address cache on your Linux computer by using this
ip command:

1 |
$ sudo ip neigh show |
Viewing the MAC address cache is a good way to learn about your segment’s network devices and troubleshoot failed connections.
Clear the ARP cache with the following command:

1 |
$ sudo ip neigh flush all |
Clearing the cache forces the computer to rediscover local MAC addresses, helping ensure the information in the cache is current and accurate.
## Wrap Up
Recognizing the three identities networked computers use is helpful for security auditing, troubleshooting, system configuration, and more. Each identity is used by a different aspect of the network infrastructure.

- Hostnames: Typically used by people.
- IP addresses: Typically used by computers and routers.
- MAC addresses: Typically used by computers and switches.
Little configuration is available for MAC addresses, and hostnames are usually set during the operating system installation. IP address settings are where most configuration and troubleshooting will occur.

Administrators may configure IP settings manually (called a “static IP address”) or allow systems to lease IP settings from a DHCP server (called “dynamic IP addressing”). Regardless, the common settings are shown below:

- IP address: Logical address that shows what network segment the computer resides on.
- Subnet mask: Indicates which part of the IP address is the network ID and which part is the host ID.
- Default gateway: The IP address of the router.
- Name servers: The IP address of one or more DNS name servers.
Managing and troubleshooting IP addressing is a standard skill for Linux administrators. Expect to work at the command line and graphical interface when managing Linux network nodes. Begin exploring the network settings on your Linux lab computer today.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)