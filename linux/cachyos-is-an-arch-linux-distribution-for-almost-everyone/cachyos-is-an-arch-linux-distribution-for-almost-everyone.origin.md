# CachyOS Is an Arch Linux Distribution for (Almost) Everyone
![Featued image for: CachyOS Is an Arch Linux Distribution for (Almost) Everyone](https://cdn.thenewstack.io/media/2024/12/fc5cdb8e-cachyoshero-1024x628.jpg)
Arch Linux gets a bad rap for being far too challenging [a distribution](https://thenewstack.io/choosing-a-linux-distribution/) for the average user, which is a shame because it[’](https://www.docker.com/blog/ai-trends-report-2024/)s also a rock-solid distro from which anyone would benefit. One of the most challenging aspects of [Arch Linux](https://archlinux.org/) is the installation process, which requires a solid understanding of how Linux (and operating systems in general) work. For those without a grasp of [Linux fundamentals](https://thenewstack.io/learning-linux-start-here/), Arch is not a good option.

Fortunately, there are quite a few user-friendly takes on Arch Linux, all of which make the installation process a point-and-click affair. One such distribution is called [CachyOS](https://cachyos.org/). According to the official website, “Our distribution offers a seamless installation process and a range of customization options to personalize your computing experience. Whether you[’](https://www.docker.com/blog/ai-trends-report-2024/)re a beginner or an experienced user, CachyOS delivers optimized performance while maintaining its simplicity.”

Very early on in the installation process, you are presented with a choice of desktop environments (Figure 1).

- Figure 1: You can choose from several desktop environments for your CachyOS.
For new users, I would suggest selecting either Plasma Desktop, Budgie, Cinnamon or Mate.

Those with Linux experience would be happy with any of the options. If you want the most efficient desktop, maybe the i3 or [Hyprland tiling window managers](https://www.youtube.com/watch?v=wgajzUIZNh8) would be the best bet. I opted to go with Cosmic because I predict it will be my distribution in the future. If you[’](https://www.docker.com/blog/ai-trends-report-2024/)re unfamiliar with it, Cosmic is the desktop environment being developed by System76. At the moment, Cosmic is still in alpha, but I[’](https://www.docker.com/blog/ai-trends-report-2024/)ve found it to be surprisingly stable. Even so, I would not recommend Cosmic as your go-to — at least not until its official release.

I was actually (and pleasantly) surprised that CachyOS included Cosmic in its list of options and was happy to give it a go.

It did not disappoint.

## What Makes CachyOS Special?
The obvious answer to this is that it makes Arch Linux accessible to more users. CachyOS is as easy to use as those distributions considered to be the most user-friendly on the market (think [Linux Mint](https://thenewstack.io/tutorial-install-linux-mint-on-a-windows-laptop-using-a-usb-stick/) and [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)). Of course, that will depend on the desktop you go with but if you choose the right desktop, you’ll find CachyOS to be a treat to use.

The first thing to greet me upon login is the welcome tool, which includes quick access to a ReadMe, release notes, forums, software, apps/tweaks, install apps and more. Think of this as a “first steps” tool to help you know what[’](https://www.docker.com/blog/ai-trends-report-2024/)s what. From my perspective, every distribution should include a Welcome app.

For those [new to Linux](https://thenewstack.io/learning-linux-start-here/), the first two steps you’ll want to take would be the apps/tweaks and install apps options in the welcome app. The apps/tweak section offers tweaks such as *profile-sync-daemon enable*, *system-oomd enable*, *bpftune* enabled and Bluetooth enabled. The Fixes section includes options like system update, reinstalling all packages, refreshing keyrings, removing db lock, clearing package cache, removing orphans, installing gaming packages, installing Snapper support, ranking mirrors, change DNS server and installing SpoofDPI.

From **Welcome > Apps/Tweaks**, there’s also the CachyOS Kernel Manager, which allows you to select from several different kernels, such as a hardened kernel, a real-time kernel and more. The kernel installed by default is 6.11.7-1.

As far as pre-installed software, you’ll find the selection to be fairly limited. This, of course, also depends on the desktop you select. With the Cosmic option, there was Vim (a powerful text editor), Cosmic terminal (a terminal app), Catchy Browser (web browser), Meld (a diff tool), Btrfs Assistant (a tool to tweak the file Btrfs file system) and not much else.

It’s a good thing there’s Octopi, the front end for the Pacman package manager, which reminds me very much of Synaptic in that it’s not exactly the most modern-looking front end, but it’s very effective and easy to use. From within Octopi (Figure 2), you search for the app you want to install, right-click it, select “install” from the pop-up menu and then click the green check to proceed. You’ll be prompted to OK the installation and then required to type your user password. Once you’ve done that, the installation will start and complete.

-
Figure 2: The Octopi package manager should be familiar to anyone who’s used Synaptic.

Once installed, the software will be available from within the desktop menu.

Octopi isn’t the only installer application. There’s also the CachyOS Package Installer (Figure 3), which is actually easier to use than Octopi. With CachyOS Package Installer, you select the package you want to install, click Install and type your user password.

-
Figure 3: The CachyOS Package Installer.

If you’re new to the land of Linux, I would recommend going with the CachyOS Package Installer, as it’s simpler to use.

Just for fun, I used the CachyOS Kernel Manager and installed the *linux-cachyos-rt-bore*, which is based on different schedulers and some other performance improvements to see how it fared. Once the installation of the new kernel was completed, I rebooted and discovered a slight performance improvement, which is saying something, given how well the OS performed out of the box. It wasn’t perfect, as I did notice some “hiccups” as I moved the cursor about, almost as if the OS was briefly pausing.

To mitigate that issue, I upped the RAM allotted for the virtual machine to 6GB (from the usual 3GB I tend to give VMs). That change did not solve the problem, so I opted to install a different kernel, this time the 6.10 extra/linux-rt (real-time) kernel. Thankfully, the CachyOS Kernel Manager makes this very easy. That kernel solved the problem and CachyOS was back to running smooth as silk. Of course, your mileage may vary, depending on the hardware you use.

## Is CachyOS Right for You?
As a rule, I don’t generally recommend Arch-based Linux distributions for new users and CachyOS would fall under that same category. Does that mean every new user should avoid this distribution? No. If you’re feeling adventurous and want an operating system that will allow you to grow your skills, CachyOS is a great option. If you want something that’s best suited for those with very little Linux experience, I would recommend sticking with Ubuntu, Linux Mint or ZorinOS.

If, however, you want to experience an easy route to Arch Linux — and like the idea of being able to select from several different desktop environments during the OS installation — CachyOS is a great option. During my testing period, I thoroughly enjoyed working with COSMIC desktop (which will soon become my default on my System76 Thelio desktop machine) and believe it will be one of the hottest desktops available to the Linux market.

If you’re interested in testing the CachyOS waters, [download an ISO](https://cachyos.org), burn it to a bootable USB drive (with a tool like [uNetBootin](https://unetbootin.github.io/)) and kick the tires. I’m fairly confident you’ll like what you see.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)