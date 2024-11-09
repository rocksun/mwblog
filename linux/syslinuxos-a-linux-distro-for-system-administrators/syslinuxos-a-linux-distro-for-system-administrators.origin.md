# SysLinuxOS, A Linux Distro for System Administrators
![Featued image for: SysLinuxOS, A Linux Distro for System Administrators](https://cdn.thenewstack.io/media/2024/11/32a147b4-screenshot-from-syslinuxos-12-video-1024x587.jpg)
System integrators around the web are discovering
[SysLinuxOS](https://syslinuxos.com/), a Debian-based distro with a variety of networking and systems tools pre-installed.
It’s designed to meet the unique needs of system integrators, and it aims to be an international phenomenon. Its official blog offers readers a choice of nine languages — including Arabic, Chinese, French, German, Italian, Portuguese, Russian, and Spanish. It even ships with a choice of GNOME or MATE desktops.
But in the end, SysLinuxOs also serves as yet another demonstration of the
[ power of Linux](https://thenewstack.io/learning-linux-start-here/) and how open source operating systems have a superpower: How infinitely customizable they really are.
And how dedicated users are making that customization happen…
## The Creator Behind SysLinuxOS
“I felt the need to have a distro that included all the tools and that worked out of the box,” explained
[an early blog post](https://syslinuxos.com/perche-syslinuxos/) from the distro’s Milan-based creator, [Franco Conidi](https://www.linkedin.com/in/franco-conidi-edm/). An online biography identifies Conidi (aka “Edmond”) as a senior system integrator, sys-admin, and IT consultant.
“I’ll start by saying that I’m passionate about computers,” Conidi says in a short bio on his
[personal website](https://francoconidi.it/info/), “especially Gnu-Linux, and everything that concerns the world of open source… In general, everything that has to do with technology attracts me, and I’ve tried more or less all the most important distros…”
Conidi had been using
[Debian](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/) for years, and claimed to have such deep feelings for the OS that “I cuddle it, I look at it, I study it, continuously. I’m in love with it and with [this](https://www.debian.org/social_contract),” referring to Debian’s famous social contract promising their OS will always remain free and open.
With some added customizations, the SysLinuxOS
[home page](https://syslinuxos.com/) promises users “a robust and feature-rich operating system, designed specifically for professionals in system integration. With its enhanced desktop, improved security measures, advanced networking capabilities, and comprehensive monitoring tools.”
Its version numbers track those of Debian. In June of 2023,
[version 12 of SysLinuxOS](https://syslinuxos.com/syslinuxos-12-for-system-integrators/) coincided with the release of Debian 12 — but with the addition of features for sysadmins (including its two [ widgets monitoring running processes, network status, and PC performance). It also shipped with a dedicated menu for its network-analysis tools, along with several firewalls integrated by default (including Gufw, Firewalld, Opensnitch, and Shorewall), and security tools like Firejail, Firetools, Firewalk, and Suricata. conky](https://conky.sourceforge.net/documentation.html)
Its extensive list of monitoring tools included Cacti, Fail2ban, Icinga, Monit, Munin, Nagios4, Zabbix-Agent2, and Zabbix-Fronted, “among others, ensuring effective system monitoring and management.”
And since its launch, Conidi’s tried adding various tools, including
[two command line speed test tools](https://syslinuxos.com/fast-cli-speedtest-cli-su-syslinuxos/) — Fast-cli and Speedtest-cli — plus the whole [XAMPP web server stack](https://syslinuxos.com/xampp-php-8-syslinuxos-11/) of Apache HTTP Server, MySQL (or MariaDB), PHP and Perl, and the DHCP network server [installed](https://syslinuxos.com/server-dhcp-su-syslinuxos-11/). (Just add the name of your own network to */etc/default/isc-dhcp-server*…) ![Screenshot from the current SysLinuxOS home page](https://cdn.thenewstack.io/media/2024/11/a79cecd9-screenshot-from-syslinuxos-home-page-features.png)
Screenshot from the current SysLinuxOS home page
## Evolution of a Toolchest
It’s fascinating to see how SysLinuxOS has evolved. Earlier videos on its YouTube channel captured the sidebar of
*conky* applets showing CPU and RAM utilization, as well as network data transfers and a list of running processes.
While they’re still there in version 12, there are now also CPU, memory, and internet monitors displayed on the desktop, along with a clock. A
[review in Linux Magazine](https://www.linux-magazine.com/Issues/2024/287/SysLinuxOS) complains this “tends to make the desktop a little cluttered” though “the many, constantly changing status displays makes for a genuinely eye-catching user interface.”
But there are still plenty of tools — as evidenced by the running applications in a SysLinuxOS video. There’s TeamViewer, AnyDesk, GParted, Oracle VM VirtualBox, and Remmina (remote desktop client). And there’s also a “Networking” submenu with tools like Angry IP Scanner, CuteCom, EtherApe, Ettercap, GNS3, Gtkterm, LinSSID, Minicom, NpamSI4 (nmap interface), PackETH (ethernet packet generator), Packet Sender, Packet Tracer, Sparrow Wifi, Wifi QR, and
[ Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/). (And, of course, the PuTTY terminal emulator…)
Or, as its home page explains, SysLinuxOS “was built to work right out of the box, with all networking tools already installed by default.” It promises there’s “improved” hardware support by including “a good number of wifi/video/sound and Bluetooth drivers in addition to those contained in the kernel.” It brags that (along with the latest stable Linux kernel) SysLinuxOS includes all the major VPNs, tools for serial console, several remote control clients, and various browsers.
And there’s plenty of additional bells and whistles. Under Accessories, there’s even a
[Raspberry Pi](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) Imager and balenaEtcher for flashing images onto USB drives or SD cards. *Linux Magazine* notes that it also includes a fully configured version of the Windows runtime environment Wine, two different GUI frontends for firewall configurations, and “a very extensive selection” of software under its “Internet” menu, including Skype, Zoom, WhatsApp, and Telegram. (Plus Thunderbird for email and Cisco’s WebEx tool for collaboration.)
“SysLinuxOS puts an end to searching for the right tools for admin tasks,” they conclude, applauding the distro for providing “a very extensive selection of software, especially for using the internet” — including Firefox, Chrome, Edge, and Tor Browser. “Tor is actually downloaded from the Internet via a script and integrated into the system the first time you call it.”
“Instead of targeting a specific application scenario, SysLinuxOS’s developers bundle a wide variety of tools for virtually any admin task you can imagine…”
Of course you can install your own additional tools — but SysLinuxOS starts you off with a good selection that’s pre-installed.
*Linux Magazine* points out SysLinuxOS’s many package sources — which are enabled by default — include Skype, Google, Docker, and Microsoft. “This gives you access to more than 65,000 packages…” It even ships with both Docker and the Docker Compose tool, “which considerably simplifies the development, distribution, and management of applications in containers.”
## Passionate for Debian
A little more than a year ago, its creator shared some personal thoughts in
[a comment on their blog](https://syslinuxos.com/things-to-do-after-installing-syslinuxos-12/#comment-82). Not only did SysLinuxOS evolve directly from his passion for Debian — he’s been “dogfooding” his own OS ever since launching it. “I use SysLinuxOS as my daily desktop, and I’ve never had any issues.
“Certainly, there is room for improvement and there will be some bugs, but I will do my best to resolve them once I become aware of the problem… In this job, it’s just me, and behind me, it’s always just me.”
And there was a special promise to users with Version 12.3 —
[released in January](https://syslinuxos.com/syslinuxos-12-3-released/).
“I will do my best to make this distro useful and more complete for those who, like me, do the work of System Integrator or Network Administrator.”
# WebReduce
- Patches promised after testing five end-to-end encrypted cloud storage services discovered
[unauthorized server access also allowed bypassing of data encryption](https://brokencloudstorage.info/).
- Redmonk analyst thinks the term Open Source
[shouldn’t be extended into the AI world](https://redmonk.com/sogrady/2024/10/22/from-open-source-to-ai/).
- GitHub releases 2024 developer survey, “
[State of the Octoverse](https://github.blog/news-insights/octoverse/octoverse-2024/)“.
- Internet Archive releases
[.](https://blog.archive.org/2024/10/30/vanishing-culture-a-report-on-our-fragile-cultural-record/) *Vanishing Culture: A Report on Our Fragile Cultural Record*
- Cracking the
[30-year-old PKZIP file that helped end apartheid in South Africa](https://blog.jgc.org/2024/09/cracking-old-zip-file-to-help-open.html). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)