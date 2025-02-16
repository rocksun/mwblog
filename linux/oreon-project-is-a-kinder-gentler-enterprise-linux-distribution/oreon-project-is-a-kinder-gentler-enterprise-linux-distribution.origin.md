# Oreon Project Is a Kinder, Gentler Enterprise Linux Distribution
![Featued image for: Oreon Project Is a Kinder, Gentler Enterprise Linux Distribution](https://cdn.thenewstack.io/media/2025/02/c3b1cdcb-oreonhero-1024x643.jpg)
Have you ever wondered why more people don’t use the likes of [AlmaLinux](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/), [CentOS Stream](https://thenewstack.io/back-to-the-future-a-look-at-centos-streams/) or [Rocky Linux](https://thenewstack.io/ciq-unveils-a-version-of-rocky-linux-for-the-enterprise/) as a desktop operating system? After all, those distributions are rock solid and very secure. Doesn’t that sound like the makings for an ideal desktop OS?

Nah.

Okay, yeah, it does … but that doesn’t mean people are going to use it as such. Why? Complication. I’m not saying that those enterprise-grade OSes are complicated, because they aren’t — at least not to experienced Linux users who need a reliable server OS.

But to desktop users, the likes of CentOS Stream is unthinkable. Yes, you can certainly use it as a desktop OS, but why would you when you might have to do extra work to get it to serve you well?

That’s where the [Oreon Project](https://oreonproject.org/oreon-10/) comes into play.

The primary goal of the Oreon Project is to make enterprise Linux more suitable as a desktop (or laptop) OS. To that end, the developers focus on providing the best user experience possible by default.

One of the biggest surprises with Oreon is that its lead developer, Brandon Lester, is a high-school student managing a small team to bring Oreon to life. He’s done a fantastic job.

## A New Kind of Enterprise Linux
I realized that Oreon was something altogether different when I started installing the OS. I know the Fedora-based installer well; it’s easy to use and is rock solid. However, those new to Linux could be intimidated by the steps used to install the OS.

Fortunately, Oreon takes a more Ubuntu-like install wizard approach (**Figure 1**), which lifts the user-friendliness of the installation to much higher grounds.

![Installation screenshot.](https://cdn.thenewstack.io/media/2025/02/af2d0230-oreoninstall.jpg)
Figure 1: The Oreon installation is a point-and-click affair that should be instantly familiar to anyone.

The Oreon installer only requires four clicks of the mouse, so you can be sure that anyone can install this OS.

## Preinstalled Applications and Flatpak Support
Oreon ships with the KDE Plasma desktop and a bare minimum of applications. Fortunately, you can install anything you need from the Discover app store, and with Flatpak added for good measure, there’s even more applications available for installation. The only caveat is that Discover doesn’t have Flatpak support rolled in. Fortunately, there’s a very simple fix for that. If you open Discover and click Settings, you’ll find an Add Flathub button near the top right (**Figure 2**).

![Screenshot of KDE Discover app.](https://cdn.thenewstack.io/media/2025/02/1afc55a4-oreondiscover.jpg)
Figure 2: KDE’s Discover app makes it easy to add Flatpak support.

Click Add Flathub and you’ll find the available software for installation has grown considerably.

What else has been done to Oreon to simplify its usage?

## SELinux
When I think of [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) (now maintained as open source by [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)), I see admins huddled over a desktop, attempting to figure out how to tell SELinux to allow something to work. I’ve used SELinux and understand how intimidating it can be.

Strike that — how *hard *it is to use.

Oreon ships with a handy little SELinux GUI called the SELinux Alert Browser. Should an event or process trigger SELinux, you can view what’s happening with the Alert Browser and then decide to troubleshoot, notify, ignore or delete (**Figure 3**).

![SELinux visual interface.](https://cdn.thenewstack.io/media/2025/02/34312d92-oreonselinux.jpg)
Figure 3: SELinux is easier to manage with the help of this GUI.

The troubleshooting feature of the app is quite impressive, and even gives you options to help solve issues (from within the Troubleshooting section).

But what really sets Oreon apart from the other enterprise-grade distributions, and why would you use it as a desktop OS?

Here are the main selling points that differentiate Oreon from the competition as a desktop operating system:

**User-Friendly**: Oreon is designed to be welcoming and accessible to Linux users of all skills. Whether you’re new to Linux or experienced, you shouldn’t have trouble making this OS work for you.**Long-Term Support (LTS)**: Oreon Lime R2 is on an eight-year life cycle, which means it’ll enjoy support until 2032.**Repositories**: Oreon includes essential repositories like Docker, EPEL, RPM Fusion and Flatpak preinstalled.**Lightweight Performance**: Oreon ensures you’ll get smooth performance, even when installed on older hardware, making it suitable for revitalizing aging machines.**Gaming Capabilities**: The Oreon team has ported a working version of WINE (that has support for WINE 32-bit and 64-bit applications), as well as implemented other fixes, so it can run Proton/WINE-based games smoothly. Oreon also supports game launchers such as Lutris, Steam and Bottles. Note that you do have to install these packages manually.
Of course, like so many Linux distributions these days, Oreon ships with a dark theme set by default. But since this is KDE Plasma, you can quickly configure it to exceed all of your light-themed desires (**Figure 4**).

![](https://cdn.thenewstack.io/media/2025/02/c3b1cdcb-oreonhero.jpg)
Figure 4: It took me all of two minutes to get KDE Plasma looking exactly how I wanted it.

## Who Is Oreon Best For?
I believe the goal of Oreon is to be the AlmaLinux/Rocky Linux/CentOS for the enterprise desktop, and the team has made a great start in that effort. That’s not to say Oreon isn’t viable for any desktop, but given the OS is based on AlmaLinux, it makes perfect sense that this would be a desktop operating system geared toward enterprise users.

From my testing, I would say that Oreon is best suited for those who want a rock-solid desktop operating system and either work within the company or from home. Or, if you like the idea of a Linux distribution that’s based on an enterprise-worthy OS that also adds gaming into the mix, Oreon makes a pretty strong case.

If you’re into what Oreon’s dishing out, head over to the official site, [download an ISO](https://oreonproject.org/download/), and either burn it to a USB drive or use it to start a virtual machine to see what this new Linux distribution is all about.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)