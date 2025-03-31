# Check Out Debian, the ‘Mother of All Linux Distributions’
![Featued image for: Check Out Debian, the ‘Mother of All Linux Distributions’](https://cdn.thenewstack.io/media/2024/05/199b905f-debian-1024x683.png)
How often have you heard or read about a distribution that was based on [Ubuntu](https://thenewstack.io/cubic-build-a-custom-linux-distribution-based-on-ubuntu/)? There’s [Kubuntu](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/), [elementaryOS](https://thenewstack.io/elementary-os-a-linux-distro-easy-to-use-and-easy-on-the-eyes/), [Zorin OS](https://thenewstack.io/zorin-os-the-perfect-linux-distro-for-migrating-from-windows/), [Deepin](https://www.deepin.org/index/en), [Ubuntu Budgie](https://ubuntubudgie.org/), [KDE neon](https://thenewstack.io/kde-neon-is-the-linux-distribution-with-the-dynamic-desktop/) … the list goes on and on and on.

There’s a reason so many operating system developers [base their distributions on Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/):

- It’s reliable.
- It’s user friendly.
- It offers one of the best installers on the market.
- It’s easy to customize.
- It has some of the best hardware detection available.
But what would you say if you knew that Ubuntu, in turn, was based on yet another distribution?

Most of you would probably say, “Duh.”

## Mother of All Linux Distributions
For those of you who did attempt to shame me with that single syllable, you should know that Ubuntu is based on [Debian](https://www.debian.org/).

The Debian project was founded in August 1993 as an effort to create a truly open Linux distribution, in the spirit of [Linux and GNU](https://thenewstack.io/learning-linux-start-here/). The name “Debian” was an amalgamation of the first names of its two co-creators: Debra Lynn and Ian Murdock.

Debian has become known as the “mother of all distributions” because of, well, Ubuntu. Because so many distributions are based on Ubuntu, and because Ubuntu is a “child” of Debian, it only makes sense to label it “mother.”

With all of those Ubuntu-based distributions, why would you bother with Debian? After all, isn’t it well known for shipping preinstalled software that could be considered out of date?

Well, yeah. But — and trust me when I tell you it’s a big, important *but* — Debian is all about one thing, and that is stability.

## Why Choose Debian?
There are plenty of reasons to adopt Debian as your go-to Linux distribution other than the rock-solid stability it offers, including:

**Security**: Debian isn’t only focused on stability. Debian is also very secure, thanks to its rigorous testing process. In fact, the Debian developers spend considerably more time testing than other distribution teams.**Free and open source**: Debian only includes software that is free and open source.**Large community**: Debian enjoys one of the largest and most active developer, maintainer and user communities, well beyond what is offered by any other distribution.**Customizability**: Debian allows for a high level of customization, thanks to a vast repository of software packages.**Low maintenance**: Because Debian is so stable, it requires almost no maintenance.**Documentation**: Debian is very well-documented.
For most average users, the primary reason to adopt Debian is a stability you won’t find in most other operating systems. In the years I’ve used Debian, I never experienced a single problem. Now, that could be said about a lot of Linux distributions, but Debian takes this to a much higher level.

## The Versions
There are three different “versions” of Debian:

**Stable**: The latest officially released distribution of Debian, which is recommended for daily use.**Testing**: The testing version contains packages that haven’t been accepted into a “stable” release yet, but are in the queue. The main advantage of using the testing release is that it includes more recent versions of software.**Unstable**: This is the version that has the most active development and is recommended to be used by developers and those who prefer to live “on the edge.” This version is not recommended for daily use.
Debian doesn’t release specific versions with specific desktops. Instead, you download a single ISO and, during the installation, you can select from GNOME, KDE Plasma, Xfce, MATE, Cinnamon, LXDE or LXQt. Of course, you could also install a different desktop environment after you’ve installed the OS, such as Budgie or COSMIC.

For the purpose of this review, I installed Debian with KDE Plasma.

![desktop screenshot.](https://cdn.thenewstack.io/media/2025/03/e998b570-debianhero.jpg)
The default Debian KDE Plasma desktop.

## Debian Is Debian
One of the things I truly respect about Debian is that, well, it’s always Debian. You know exactly what to expect when you first log in. It’s not that Debian is uneventful; it’s just so reliable that it feels kind of static. Even with KDE Plasma at version 5.27.5, it didn’t feel much fresher than the last time I used Debian. That’s probably due to the fact I usually install GNOME with Debian, so it’s still the same ol’ same ol’.

Debian also ships with the usual suspects of open source software:

- Firefox (ESR)
- LibreOffice
- Akregator (RSS feed reader)
- Dragon Player (video)
- GIMP (image editor)
- JuK (music player)
- KMail (email client)
- Konqueror (web browser)
- Sweeper (system cleaner)
There’s also Discover, which allows you to install all the software you may need. If you want to add either the [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) or [Snap](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/) backends, you can go to Discover > Settings and install the necessary packages (**Figure 1**).

![Screenshot](https://cdn.thenewstack.io/media/2025/03/f41f6609-debian1.jpg)
**Figure 1: **Adding Flatpak and/or Snap support in KDE Plasma’s Discover.
One of the nice things about adding either (or both) Flatpak or Snap is that Debian is then able to install newer versions of packages (so long as they are available within either the Flathub or Snapcraft repositories). Just make sure you restart Discover to allow the changes to take effect.

## Who Is Debian For?
Simply put, Debian is the Linux distribution you should use when stability is of the utmost importance. Debian is also great for legacy system support, which means it’ll run on your older hardware with ease.

But if you simply want an operating system that will rarely (if ever) fail you, Debian is one of the smartest choices you can make.

There is one thing, however, you should know about Debian: To deliver the highest possible security, the developers ship the OS such that standard users are not automatically given [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). Because of this, any changes you make that require admin rights have to be done after first changing to the root user with the command *su –*. You can add a user to the sudo group with this command:

1 |
usermod -aG sudo USER |
Replace “USER” in the statement above with the name of the user.
Once you’ve done that, the user needs to log out and log back in to allow the changes to take effect.

If security is the primary reason you’ve decided on Debian, I would not add users to the sudo group — that way, you control who has admin rights on the system.

If anyone asks me what I believe to be the most stable operating system, the answer is automatic: Debian. If anything, you can be certain that a machine running Debian will do so without failure (at least on a software level — because hardware always eventually fails) and will serve you a long, long time.

If I’ve piqued your interest in Debian, you can download the latest release from the [official Debian website](https://www.debian.org/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)