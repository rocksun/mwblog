# Linux: Zentyal Is the Small Business Server You May Need
![Featued image for: Linux: Zentyal Is the Small Business Server You May Need](https://cdn.thenewstack.io/media/2025/01/bae3809b-zentyal-1024x683.png)
Within the realm of [Linux](https://thenewstack.io/learning-linux-start-here/), there are certain distributions geared specifically for business server usage. The most popular options include [Red Hat Enterprise Linux](https://www.openshift.com/try?utm_content=inline+mention), [AlmaLinux](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/), [Rocky Linux](https://thenewstack.io/ciq-unveils-a-version-of-rocky-linux-for-the-enterprise/), [Oracle Linux](https://orca.security/?utm_content=inline+mention) and [CentOS Stream](https://thenewstack.io/back-to-the-future-a-look-at-centos-streams/).

But those aren’t the only options available. There are distributions that might not have the same name recognition, but that doesn’t make them any less viable.

One such distribution is [Zentyal](https://www.zentyal.com), which is a Linux alternative to Windows Server, and includes features like:

- Domain & Directory server
- Mail server
- Firewall
- IDS/IPS
- Iproute2, Netfilter, Squid, Suricata and FreeRADIUS
- Domain-based HTTPS webpage blocking
- NTP server
- Certification authority
- VPN
- Backup
- FTP
- IPSec/L2TP
- Antivirus
- Real-time alerts
- Daily reports
- Kernel management
- User authentication in HTTP proxy
- Docker containers
- Intrusion protection
- Jabber server
- Web server
- And much more
With Zentyal, you’ll find a free community edition and a paid version. The paid version can be had at various pricing tiers. (Check out the [Zentyal pricing matrix](https://www.zentyal.com/price-yearly-zentyal-server-subscription/) for more information.) I would suggest [downloading and installing the community edition](https://download02.public.zentyal.com/zentyal-8.0-development-amd64.iso?_gl=1*r7qpip*_gcl_au*MTkwNTI2MTQ3OS4xNzE1MTgxOTMw*_ga*MTg2OTA1MTc5Ny4xNzE1MTgxOTMw*_ga_N2CRZTM10X*MTcyMTE1NDU2NS40My4xLjE3MjExNTY2MzQuNTkuMC4w&_ga=2.204391384.972608446.1721055844-1869051797.1715181930) first. If you like what you see, consider purchasing a license for the full product.

It’s been a while since I’d tested Zentyal, so I downloaded the last version and gave it a spin as a virtual machine in VirtualBox on Pop!_OS Linux. Here are my impressions.

## Installation
Given that Zentyal is based on [Ubuntu 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/), it should come as no surprise that it’s very easy to install. In fact, it’s very much a point-and-click affair that can have you at the login prompt in less than five minutes. If you can install a piece of software, you can install Zentyal.

## Post-Installation
This is when I started to remember why Zentyal impresses me so much. Upon first login, the default browser will open. From the landing page, you are greeted with an onboarding wizard. From this wizard, you can select the software you want to install (Figure 1).

-
Figure 1: Selecting the packages to be installed on Zentyal server.

Select the packages you want, scroll down and click Install. You will then be prompted to confirm the installation of the selected packages by clicking Continue. A new page will appear (with an adorable panda), displaying the progress of the package installation. A few minutes after clicking Continue, all of the software I selected was installed and ready to go. Once the app installation is complete, you’ll then be prompted to configure the networking interfaces (Figure 2).

-
Figure 2: I only have a single network interface, so the setup is simple.

You will then be asked to select the type of server, which will be either a standalone server or an additional domain controller (Figure 3).

-
Figure 3: If your Zentyal server is part of a domain, make sure to select “Additional domain controller.”

Depending on the components you’ve added to the server, you may have a few more steps to configure, such as a virtual mail domain for the mail server. Once you’ve taken care of everything, click Finish and the configurations will be applied.

## Installing Zentyal on a Current Ubuntu Deployment
If you already have a Ubuntu server deployed, you can add Zentyal’s community edition on top of it. Here are the commands to do this:

First, download the installation script with this command:

1 |
wget https://raw.githubusercontent.com/zentyal/zentyal/master/extra/ubuntu_installers/zentyal_installer_8.0.sh |
Give the installer executable permissions with the following command:
1 |
sudo chmod u+x zentyal_installer_8.0.sh |
Finally, run the installer:
1 |
sudo ./zentyal_installer_8.0.sh |
Select whether you want to install Zentyal via console or GUI. (I suggest using the console option if you’re installing Zentyal as a virtual machine; otherwise, you might run into problems.)
Walk through the installation. When finished, you can then access the Zentyal web interface at https://SERVER:8443/ (where SERVER is the IP address of the hosting machine).

One thing to keep in mind is that, when installed this way, Zentyal allows any user that is part of the [sudo group](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) to access the web interface. Because of that, you might want to consider either removing some of those users from the group or configuring them within */etc/sudoers* to limit their reach.

Regardless of how you installed Zentyal, you can then access the Dashboard at the https://SERVER:8443/Dashboard/Index page (where SERVER is the IP address of the hosting machine). From the Dashboard you can manage all services. For example, if you plan on using Zentyal for Docker containers, click the Docker entry in the sidebar and then you’ll be prompted to enable Portainer (which is used as the container manager).

## In the End
I’m not going to tell you that Zentyal is a happy-go-lucky, point-and-click affair. Yes, it does have a well-designed web-based interface, but there’s still a bit of a learning curve involved. There are some components that have to be configured in a certain order — such as those that depend on SSL certificates and require you to issue a new certificate before they’ll work as expected. This will all depend on what modules you’ve installed and the dependencies they require.

As far as deploying a Linux server for your business, Zentyal is a fantastic option. It might not be quite as “plug-and-play” as some other server systems, but Zentyal is easy enough for any admin to deploy and make work for just about any business.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)