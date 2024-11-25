# 10 Reasons To Choose Ubuntu Server Over the Competition
![Featued image for: 10 Reasons To Choose Ubuntu Server Over the Competition](https://cdn.thenewstack.io/media/2023/12/b0026b48-ubuntu-1024x683.png)
When you think of a server’s operating system (OS), what comes to mind? If you’ve been living under a [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)-ian rock for the past decade, Windows Server is probably your first thought.

What if I told you there was a better option?

Actually, there are several alternatives Microsoft Server, all of which fall under the auspices of open source. There’s [Red Hat Enterprise Linux](https://thenewstack.io/red-hat-enterprise-linux-9-5-arrives-with-enhanced-ai-support-and-automation/), [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/), [Oracle Linux](https://developer.oracle.com/?utm_content=inline+mention), [Fedora Server](https://thenewstack.io/fedora-41-offers-zippy-performance/), [Debian Server](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/), and others.

For me, however, the go-to choice is [Ubuntu Server](https://thenewstack.io/ubuntu-24-10-refreshes-gnome-permission-prompts/), from Canonical. I switched to Ubuntu Server over a decade ago and haven’t looked back. That’s not to say I don’t work with other server OSes. In the past couple of years, I’ve had plenty of deployments based on [AlmaLinux,](https://thenewstack.io/almalinux-kitten-offers-preview-of-distros-next-release/) which has been an outstanding choice.

But any time the decision is mine, Ubuntu Server is the way to go. Why, you ask? Let me offer 10 reasons why I’ve been defaulting to Ubuntu Server for over a decade.

## 1. apt
Of all the package managers I’ve used, I find the Advanced Package Tool ([apt](https://ubuntu.com/server/docs/package-management)) to be not only the easiest to work with but also the most capable of resolving issues… even with broken packages. For example, if I install something with apt and the installation fails, most often, I can fix the problem with the [sudo command](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/): `sudo apt-get install -f`
. The -f is short for –fix-broken, which attempts to correct a system with broken dependencies. That command has helped to get me out of so many jams over the years that it’s become an invaluable option. Few package managers are as easy to use and reliable as apt.

## 2. No SELinux
[SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) is a very powerful security control framework that is found on most Fedora-based Linux operating systems. I have nothing against SELinux, but it can cause problems in such a way as rendering a newly installed app useless. I’ve seen it happen so many times. The issue is so prevalent that a lot of admins mistakenly disable SELinux to avoid the problems. Unfortunately, that removes one of the more important security tools, leaving the OS vulnerable. Instead of disabling SELinux, it is critical to learn its ins and outs so you can avoid disabling it. Ubuntu Server opts for[ AppArmor](https://thenewstack.io/4-ways-to-use-kernel-security-features-for-process-monitoring/), which offers strong security without preventing apps from functioning as expected.
## 3. Vast Selection of Apps and Tools
Thanks to the combination of apt and Snap (more on this in a bit), you’ll find a vast number of applications and tools available for installation on Ubuntu Server. Ubuntu Server enjoys one of the largest selections of apps available for any Linux distribution. And if you can’t find an app in the default repositories, chances are pretty good there’s a third-party repository you can add to install the app in question.

## 4. Outstanding Support
As of this moment, Ubuntu Server 24.04 (which is a Long Term Suppor release) is supported until 2029. If you add LTS Expanded Seuciryt Maintenance, that support window is stretched out to 2035, with legacy support adding an extra year. Imagine deploying a server operating system, knowing it will enjoy support for 12 years. That’s a long time. Before the security window has expired, you will have most likely upgraded to a new release and will enjoy even more support.

## 5. Predictable Releases
Ubuntu releases fall into two categories: long-term releases and short-term releases. Long-term releases are .04 and short-term releases are .10. The LTS releases are always made available during the fourth month of the year and short-term releases are available on the 10th month of the year. The Ubuntu release cycle happens like clockwork and is as dependable and predictable as any software release on the planet.

## 6. Efficient Use of Resources
I’ve worked with many different server operating systems over the years and I’ve never experienced one that makes more efficient use of resources than Ubuntu Server. The operating system alone performs almost like a lightweight Linux distribution, which means the apps and services you add will all perform very well. I can always count on Ubuntu Server to perform like a champ, even on a server with low resources. If you’re deploying Ubuntu Server on a cloud-based host (such as AWS), you can rest assured you won’t have to worry about the OS consuming too much compute or networking resources by itself.

## 7. User Friendless (Especially for those new to Linux)
If you’ve never worked with [Linux before](https://thenewstack.io/learning-linux-start-here/), Ubuntu Server is the obvious choice. Ubuntu has been well-regarded as one of the most user-friendly distributions on the market and that goes for the server as well. One of the reasons I feel so strongly about this is because Ubuntu doesn’t put too much in the way to block you from success. It’s very straightforward and offers one of the more shallow learning curves of all the server-specific OSes on the market.

## 8. Solid Hardware Support
It’s a very rare occasion where I install Ubuntu and my hardware isn’t recognized. This is especially true for a server where you’re not going to be adding scanners, using wireless network connections, or niche peripherals. When deploying Ubuntu Server, I’ve not once had to search for drivers to get anything running as it all “just works.”

## 9. Snap Packages
I know Snap gets a lot of guff from those who aren’t fans of Canonical, but [Snap packages](https://snapcraft.io/) make deploying certain apps and services so easy that anyone could do it. For example, if you want to run the Nextcloud cloud server, you can install it with Snap using the command sudo snap install nextcloud. When the installation command completes, open your browser, point it to the IP address of the hosting server, create an admin account, and you’re ready to go. It doesn’t get any easier than that.

## 10. Availability of Online Help
When you run into an issue with Ubuntu Server, Google (or DuckDuckGo — which is my go-to search engine) is your friend. You’ll find so many places to find help, such as the [Ubuntu Forums](https://ubuntuforums.org), where you’ll find a large community of users who are capable of answering your questions. You’ll also find plenty of communities on Mastodon (such as the official [Ubuntu community](https://mastodon.social/@ubuntu@ubuntu.social)) and the [official Ubuntu Discourse channel](https://discourse.ubuntu.com).

If you’ve not tried Ubuntu Server, I would highly recommend you [download an ISO](https://ubuntu.com/download/server) and spin up a virtual machine to see just how easy and reliable this open source, server-centric operating system is.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)