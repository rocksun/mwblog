# How to Avoid Time Drifts on Your Linux Servers with Chrony
![Featued image for: How to Avoid Time Drifts on Your Linux Servers with Chrony](https://cdn.thenewstack.io/media/2024/08/7dc11acd-getty-images-f2pc4k6da84-unsplash-1024x682.jpg)
I cannot tell you how many times I’ve gone to [install a package on Linux](https://thenewstack.io/how-to-manage-linux-software/) or download a [Docker](https://www.docker.com/?utm_content=inline+mention) [image](https://thenewstack.io/the-case-for-environment-specific-docker-images/), only to get an error that it couldn’t be done. The very first time this happened was a hair-pulling experience because it took me far longer than it should to resolve the issue.

Turns out, it was all about time.

Either from an incorrectly configured locale or a simple drift in time, you could find yourself in a similar situation. Maybe you have a [Docker Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/) deployed and one of your nodes is no longer responding or connected. Or maybe you’re experiencing MariaDB database replication that’s started to fail. You’d be surprised at how much can go wrong because of incorrect time on a server.

So, how do you avoid this? There’s a simple tool you can install called [Chrony](https://chrony-project.org/) that keeps your server time in constant sync. Chrony can synchronize a system clock with NTP servers, reference clocks and manual input, as well as operate as an NTPv4 server and peer to keep the time on all of your Linux servers in sync.

Let me show you how to install and use Chrony on Linux.

## What You’ll Need
To work with Chrony, you’ll need one or more Linux servers and a user with sudo privileges.

Before we get to Chrony, there’s one task you must complete first.

## Setting Your Time Zone
To make sure your servers have the right time, Chrony requires that all of them must be configured for the right time zone. If your servers are all set to the same wrong time zone — or if they’re set to different time zones — Chrony will be of no use to you.

Ergo, let’s set the time zone on your servers.

This step is taken care of with the `timedatectl`
command, which is installed on most Linux servers by default. Before you do this, you’ll want to know which timezone you should set. To view a listing of all timezones, issue the command:

1 |
timedatectl list-timezones |
Scroll through that listing until you find the correct one for your area. For example, if you live in Louisville, Ky., the proper time zone is America/Kentucky/Louisville and is set like this:
1 |
sudo timedatectl set-timezone America/Kentucky/Louisville |
Once you’ve done that, you can verify the change with:
1 |
timedatectl |
Make sure you do the above on all of your servers (be they on bare metal, virtual machines or containers).
You’re now ready for Chrony.

## Installing Chrony
Chrony is found in the standard repositories for most distributions, which means the installation is very easy. For example, on a Ubuntu-based distribution, the installation command would be:

1 |
sudo apt-get install chrony -y |
If you’re on a Fedora-based distribution, the command is:
1 |
sudo dnf install chrony -y |
For Arch-based distributions:
1 |
sudo pacman -S chrony |
Once Chrony is installed, make sure to start and enable it with the command:
1 |
sudo systemctl enable --now chronyd |
## Enabling the Chrony NTP service
Next, you must enable the Chrony NTP service with the command:

1 |
sudo timedatectl set-ntp yes |
You’ll receive no output from the above command.
With that taken care of, check the time with:

1 |
timedatectl |
It should be spot on. Not only that, but you should also now see that the NTP service is listed as active, which means Chrony is keeping your time in check.
Do note that if you had to change the timezone of your machine, you should reboot so the changes take effect.

## Configuring Chrony
You shouldn’t have to do anything to Chrony to make it work correctly. Should you want to investigate the configuration, you can open the file for editing with:

1 |
sudo nano /etc/chrony.conf |
If you find the file isn’t there, try the command:
1 |
sudo nano /etc/chrony/chrony.conf |
At the top of the file, you’ll find a single public server listed that is used to keep time in sync. On my AlmaLinux test server, that line is:
1 |
pool 2.almalinux.pool.ntp.org iburst |
If you want, you can always change the default pool. For example, according to the NTP Pool Project, you could use the following pools for the United States:
server 0.us.pool.ntp.org
server 1.us.pool.ntp.org
server 2.us.pool.ntp.org
server 3.us.pool.ntp.org

There are several other options you can look through but you’ll most likely want to keep them as is.

You can also configure your Linux machine as a Chrony NTP server. For this, you must uncomment (remove the leading # character) the following lines in the Chrony configuration file:

12 |
allow 192.168.0.0/16local stratum 10 |
Make sure to also change the IP subnet to that of your LAN. Save and close the file. Next, restart Chrony with:
1 |
sudo systemctl restart chronyd |
Make sure to allow the NTP service through your firewall. For example, on AlmaLinux that would require the following two commands:
12 |
sudo firewall-cmd --add-service=ntp –permanentsudo firewall-cmd --reload |
You could then configure your NTP server within the chrony.conf files of the clients on your network. For example, if your NTP server is at 192.168.1.210, you could add the following in the Chrony config file:
1 |
pool 192.168.1.210 iburst maxsources 4 |
At this point, your client will remain in sync with your server. As long as your server is in sync with the NTP pool, any server (or desktop) that uses it as a time server will remain in sync.
Avoid time-related issues with this simple-to-use tool, and you’ll pull less hair and lose less sleep.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)