# AlmaLinux: Deploy a DHCP Server for Your Internal Network
![Featued image for: AlmaLinux: Deploy a DHCP Server for Your Internal Network](https://cdn.thenewstack.io/media/2024/07/31ad3212-alma-linux-1024x683.jpg)
Chances are pretty good you already have a DHCP server on your network. DHCP stands for [Dynamic Host Configuration Protocol](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top), and it is the network protocol that bridges your internal servers with the Internet.

But if that DHCP server happens to also serve as your router or modem, you may be missing out on the flexibility and power that comes with deploying one on a dedicated server.

There’s also the security issue.

Consider this: When using a router or modem as a DHCP server, you’re locked into that device and whenever the manufacturer of that device releases security updates. That may or may not be fast enough for today’s landscape, where new [vulnerabilities are found](https://thenewstack.io/kubernetes-access-vulnerability-found-in-windows-nodes/) daily.

If you’re serious about your security, you might prefer the idea of having more control over such a thing.

That’s where Linux comes into play. By deploying a DHCP server via a traditional Linux server, you are in control of the updates and even the device’s security. And when you adopt [AlmaLinux](https://thenewstack.io/almalinux-makes-in-place-upgradeseasier-for-centos-users/) as your DHCP server, you also gain the benefits of SELinux and other security mechanisms that help lock down the operating system.

I want to show you how easy it is to deploy a DHCP server with [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/).

![DHCP diagram](https://cdn.thenewstack.io/media/2024/09/f102cf55-roadmapsh-dhcp-813x1024.png)
Source: [Roamap.sh](https://roadmap.sh/guides/dhcp-in-one-picture)

## What You’ll Need
The only things you’ll need for this are a running instance of AlmaLinux and a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). One thing to keep in mind is that you want to ensure that you don’t wind up with multiple DHCP servers on your network. With multiple DHCP servers at work, you could wind up with address collision, which could cause more trouble than you want to deal with. I

f you already have a DHCP server with your router or modem, make sure to turn off that feature when you deploy the new machine.

## Update AlmaLinux
Before we dive into this, make sure your instance of AlmaLinux is up to date. To do that, log into the server and issue the command:

1 |
sudo dnf update |
Once that is completed, you’re ready to continue. Do note, however, that if the kernel is upgraded, you’ll need to reboot the machine for the changes to take effect.
## Install the DHCP Server Software
To install the DHCP server software, issue the command:

1 |
sudo dnf install dhcp-server -y |
The DHCP service is not running at the moment and we’ll leave it as such until we take care of a few configurations (otherwise, there could be problems).
## Configure your new DHCP server
The first thing you need to do is find the name of the network interface that will be used. To do that, issue the command:

1 |
ip a |
You should see something like this in the output:
`enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:b6:98:a3 brd ff:ff:ff:ff:ff:ff`
The name of the network interface above is enp0s3. That’s the information you’ll need.

Open the necessary configuration file with the command:

1 |
sudo nano /etc/dhcp/dhcpd.conf |
In that file, you’ll find nothing but a few lines that are commented out. Fortunately, the DHCP server software ships with an example config file, which can be viewed with the command:
1 |
less /usr/share/doc/dhcp-server/dhcpd.conf.example |
You could either view that file side-by-side with the actual config file, or make a copy of it in place of the empty file with the command:
1 |
sudo cp /usr/share/doc/dhcp-server/dhcpd.conf.example /etc/dhcp/dhcpd.conf |
There are a few lines/sections you’ll need to customize. The first to look for is this two-line block:
*default-lease-time 900;*
*max-lease-time 10800;*
You’ll want to make sure to customize both the default and max lease times for the DHCP addresses the server will hand out.

Next, make sure to uncomment (remove the leading # character) the line:

1 |
#authoritative; |
So that line looks like:
1 |
authoritative; |
Finally, look for the following section:
123456 |
subnet 192.168.1.0 netmask 255.255.255.0 {range 192.168.1.51 192.168.200.99;option routers 192.168.1.1;option subnet-mask 255.255.255.0;option domain-name-servers 192.168.1.1;} |
- The option routers line specifies a list of IP addresses for routers on the client’s subnet.
- The option subnet-mask defines the subnet for the network
- The option domain-name-servers is a list of DNS servers you want to use.
You’ll need to adjust the addresses in the above section to match your network as well as the range of addresses you want the server to hand out.

For example, you might have 192.168.1.10 up to 192.168.1.50 reserved for static IPs (such as for other servers) on your network. Because of that, you won’t want the DHCP server to assign addresses in that range, otherwise conflicts will occur.

Save and close the file.

## Open the Firewall
Next, you’ll need to open the firewall so the server can accept DHCP requests from machines on your network. The DHCP server uses port 67, so open it with:

1 |
sudo firewall-cmd --add-port=67/udp --permanent |
Reload the firewall with the command:
1 |
sudo firewall-cmd --reload |
## Start and Enable the Service
Once everything is taken care of, you need to start and enable the service. Do that with the command:

1 |
sudo systemctl enable --now dhcpd |
Your AlmaLinux server is now accepting DHCP requests and will hand out addresses as needed. This serer should work tirelessly for you but make sure to regularly check in and apply any upgrades that are available.
And there you have it, your own DHCP server that should be more powerful and flexible than what you were using. Enjoy!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)