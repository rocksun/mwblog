Gentoo was that Linux distribution that every user strived to build, so they could wear it as a badge of honor.

Back in the day, [Gentoo Linux](https://www.gentoo.org/get-started/about/) was only meant for those with serious [Linux skills](https://thenewstack.io/introduction-to-linux-operating-system). The only distribution more challenging was [Linux From Scratch](https://www.linuxfromscratch.org/lfs/) (which was, essentially, building your own distribution).

Gentoo is a distribution that you have to compile everything (including the OS) from source. Installing this distribution was a big challenge and took a long time, not only to do but to do perfectly.

I’ve installed Gentoo a few times, and every time I do, I think, “This is the last time I attempt this.”

But, as with everything [Linux](https://thenewstack.io/learning-linux-start-here/), the evolution of Gentoo has brought about some changes and some offshoots that aspire to make installing the open source operating system considerably easier. One such distribution is MocaccinoOS. The tag line for this OS is, “MocaccinoOS is a minimal Linux meta-distribution for the 21st century!”

The main features of MocaccinoOS are:

* A focus on minimalism, a small footprint and ease of use.
* A native (vanilla) upstream kernel.
* Comes in two flavors: Mocaccino Micro, which uses the static, container-based package manager Luet, and Mocaccino Desktop, which was formerly the Sabyon branch of Gentoo.
* It’s a meta distribution, which means it can be used to bootstrap other operating systems.
* It’s cloud-first, which means it includes support for the most important cloud technology.
* Comes in GNOME, KDE Plasma, MATE and Xfce versions.

From my perspective, the single most important aspect of MocaccinoOS is that it uses the Calamares installer (Figure 1), which is a user-friendly graphical installer that is a total point-and-click affair. On top of that, you get a GUI package manager (depending on which version you use) for installing apps and updating software. MocaccinoOS also includes [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/), which means you can install proprietary apps like Slack and Spotify, with the help of Flathub support rolled into the GUI.

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/8d91420a-mocaccinoinstall.jpg)](https://cdn.thenewstack.io/media/2025/07/8d91420a-mocaccinoinstall.jpg) Figure 1: The installation of MocaccinoOS is as easy as any Linux distribution.

But if you’re thinking about using Gentoo, why would you go with a user-friendly version? Isn’t the whole point of Gentoo to show off your skills?

Because MocaccinoOS is innovative. Think about it this way: [MocaccinoOS](https://www.mocaccino.org/docs/) is all about container-based software, with an immutable design that uses atomic upgrades and offers user-friendly editions. For anyone who places reliability and stability at the top of their list of considerations for an operating system, that makes MocaccinnoOS hard to resist.

Sure, applications might take a bit longer to install, but the end result is well worth it.

One very important distinction found with MocaccinoOS is that it containerizes system components, which means faster, more reliable updates, cleaner rollbacks and better app isolation.

The end result is a lightning-fast, highly stable Linux operating system that will serve you well.

I did a quick install of MocaccinoOS (never thought I’d say that about a Gentoo-based OS). The version I chose included the [KDE Plasma](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/) desktop, and I love that the distribution actually defaulted to a light theme! I get so tired of every Linux distribution defaulting to a dark theme. The version of KDE Plasma even has the floating panel enabled by default and includes just the right amount of transparency to make the UI look modern and clean.

## The Luet Tools

Luet is a static Golang package manager that uses SAT and RL approaches for solving dependency issues. Luet actually makes it very easy to upgrade this Gentoo-based OS, with a single command:

```
sudo luet upgrade -y
```

Luet is fast and user-friendly (Figure 2).

[![Command line progress bars](https://cdn.thenewstack.io/media/2025/07/ecbdfe9e-mocaccinoluet.jpg)](https://cdn.thenewstack.io/media/2025/07/ecbdfe9e-mocaccinoluet.jpg)

Figure 2: Luet is as easy to use as apt or dnf.

When MocaccinoOS was known as Sabyon, the developers realized there were problems with the original package manager (Entropy), which were:

* No easy path for reproducible builds.
* Lack of divergent packages.
* Missing native distributed compilation.
* The build server was inflexible and not accommodating to more than one user at a time.
* Required specific knowledge and tools for the infrastructure.
* There was no way to track changes on the build server.

Those issues led to the creation of Luet, which abstracts the container layer to make everything much simpler and reliable.

MocaccinoOS has been around for a while now, so it’s had plenty of time to mature, and mature it has. I was seriously impressed with the stability of this distribution (as well as the ease of use).

## Included Software

Out of the box, you won’t find a ton of preinstalled software. On the KDE Plasma edition, you’ll get a set of Qt development tools, KolourPaint, Okular, Firefox, KDE Connect, VLC media player, Phonon Audio and Video player, and the usual collection of utilities. The good news is that all you have to do is fire up Discover to install whatever apps you need (Figure 3).

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/459c6785-mocaccinoldiscover.jpg)](https://cdn.thenewstack.io/media/2025/07/459c6785-mocaccinoldiscover.jpg)

Figure 3: Using Discover on MocaccinoOS is as easy to use as with any distribution.

Search for the software you want and click Install from Flathub to add the app.

## Who Is MocaccinoOS For?

If this were Gentoo, I’d say it’s only suited for those with tons of Linux experience. However, since the developers have gone out of their way to simplify Gentoo, I would say that this distribution is perfectly suited for Linux enthusiasts, developers, engineers, users who value security and anyone looking for a lightweight, reliable operating system. If, however, you’re brand new to Linux, I would say you should probably first have a fundamental understanding of how Linux works before you dive into MocaccinoOS.

If I’ve piqued your interest, head over to the official site, [download an ISO](https://github.com/mocaccinoOS/mocaccino/releases), burn it to a USB drive and install it on a spare machine (or as a virtual machine). I think you’ll be pleased with the experience.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)