# Bluefin, a Next-Gen Linux Workstation for Containerized Apps
![Featued image for: Bluefin, a Next-Gen Linux Workstation for Containerized Apps](https://cdn.thenewstack.io/media/2025/01/e437f290-bluefinhero-1024x695.jpg)
Bluefin is a custom take on Fedora Silverblue.

If you’re not familiar with the [Silverblue project](https://fedoraproject.org/atomic-desktops/silverblue/), it’s a variant of [Fedora](https://thenewstack.io/fedora-41-offers-zippy-performance/) that uses an immutable file system to allow for atomic updates and easy rollbacks. Silverblue also makes use of rpm-ostree, which delivers consistent versioning updates for [Linux](https://thenewstack.io/learning-linux-start-here/).

One of the cool features of [rpm-ostree](https://coreos.github.io/rpm-ostree/) package system is that it makes it possible to rebase your installation, so you can easily switch between Silverblue (GNOME), Kinoite (KDE Plasma), Sericea (Sway), and Bluefin (a customized version of GNOME).

But we’re not here to talk about rebasing. Instead, let’s put [Bluefin](https://projectbluefin.io/) in the spotlight.

Bluefin uses applications from Flathub, requires near-zero maintenance, and includes GPU drivers, so you don’t have to install them manually.

Things to keep in mind before you dive into Bluefin:

- The Flatpak issue should certainly be taken seriously, as the application model for Bluefin centers around
[Flatpak apps](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)that are isolated and maintained in Flathub. If there’s an app you use that doesn’t work well with Wayland, Pipewire, Flapak, or Portals, chances are good it will not perform well on Bluefin. - Bluefin is not so much a distribution as it is a vehicle for
[containerized applications](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/). - Bluefin is optimized for the majority of users.
- Bluefin is focused on containers and “exposing new Linux users to the tools used in cloud native.”
What does that last bit even mean? Essentially, the developers have integrated Bluefin with a cloud native ecosystem. Most of this is under the hood, as you won’t find a collection of apps that are pre-installed and geared towards connecting with cloud-based services, such as Google. As far as the cloud native issue is concerned, know that it’s geared mostly toward developers.

But what about users? What does Bluefin offer that other distributions do not? The base goal for Bluefin is to create an open source operating system that is as maintenance-free as possible. For anyone who feels as though other Linux desktop distributions aren’t quite reliable enough, Bluefin gets the win thanks to its atomic layer, which is placed upon the default Fedora image. What this means is that you can also revert back to the default image should the need arise.

Enough with the under-the-hood discussion. Let’s talk about how Bluefin looks, works, and performs.

## The Look
Bluefin is beautiful. From the default wallpaper to the theme, the dock, and everything in between. I’d go so far as to say that this is one of the best-looking takes on the GNOME desktop I’ve used. While it’s still the same ol’ GNOME, it gets a bump from the following extensions:

- Blur My Shell
- Dash to Dock
- Apps Menu (installed by not enabled by default)
- Logo Menu
- Search Light (global search)
I’m one of those Linux users who demands both a high aesthetic and a highly functioning OS, and Bluefin checks both of those boxes with ease. Bluefin offers the ease of use found in typical GNOME desktops with the elegance of elementary OS.

It’s as easy to use as [any Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) but doesn’t “dumb” anything down. Someone who is new to Linux would feel right at home on Bluefin and experienced users won’t feel as if they’re working with a “toy” OS.

## Applications, Applications, Applications
Out of the box, you won’t find a ton of pre-installed applications on Bluefin. There’s the usual collection of GNOME apps (such as Calendar, Contacts, Weather, Maps, Calculator, Text Editor, Terminal), Firefox, Thunderbird, Clapper (media player), InputLeap (for sharing mouse and keyboard between desktops), Connections (for remote desktop connectivity), Mission Center (system resource monitor), and more.

That might seem a bit bare, but there’s always GNOME Software to use for installing other applications. Bluefin’s take on GNOME Software integrates Flapak, so the apps you install will all be from Flathub (Figure 1).

-
Figure 1: GNOME Software is a very user-friendly package manager GUI.

There’s also a small application called Warehouse, which allows you to control complicated Flatpak options. With Warehouse, you can easily roll back any unwanted updates, pin runtimes, mask Flatpaks, filter packages, sort date, view current app user date, cleanup any stray data, take snapshots of apps, install new packages, and more. Any Flatpak app you install will appear in Warehouse (Figure 2) and can be easily managed from within the GUI.

-
Figure 2: Warehouse is a boon to those who like using Flatpak apps.

With Warehouse, you can quickly delete user data from a specific app, open the user data folder for an app, open apps, uninstall apps, and more. On top of that, Bluefin ships with Flatseal, which simplifies the process of managing Flatpak permissions.

You’ll also find Brew, or [Homebrew](https://brew.sh/), installed by default. Brew is often thought of as the command-line package manager for macOS, but with a Linux version ready to do, there are so many applications you can install. For example, you can install the tree application with:

1 |
brew install tree |
Keep in mind that brew is used only for installing command-line tools.
## Who Is Bluefin for?
Some might be so inclined to say that Bluefin is a distribution that would best serve developers or experienced Linux users, but I would argue that it’s an equally strong contender for new users because of how reliable it is and how well-configured it comes out of the box. Bluefin is one of those distributions that is as close to set-it-and-forget-it as you’ll find.

For developers, you can rebase Bluefin for developer mode, which is a dedicated developer image with specific bundled tools, such as Visual Studio Code with Docker, DevPod, Podman, and Podman Desktop, performance tooling, and more.

To enable dev mode, you’ll need to run two commands. The first is:

1 |
ujust devmode |
After this command runs, reboot.
Next, you need to add your user account to the correct groups with the command:

1 |
ujust dx-group |
Log out and log back in. You should now be in the Bluefin devmode.
This take on Linux is every bit as solid as it is beautiful (and that’s saying something). After my testing period with Bluefin, I came away thinking, “I could see myself making this my default Linux distribution.

If I’ve piqued your interest in Bluefin, you can download the ISO by using the form under the TRY BLUEFIN section of the [website](https://projectbluefin.io). Burn the ISO to a bootable USB drive, insert it into your machine, boot, and install.

You won’t regret giving this distribution a chance.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)