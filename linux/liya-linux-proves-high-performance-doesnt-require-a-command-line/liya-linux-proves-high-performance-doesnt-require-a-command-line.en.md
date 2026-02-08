Any [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) claiming that it wants to make [Linux easy](https://thenewstack.io/learning-linux-start-here/) and accessible to the general public, as well as to establish itself as a new industry standard for home computing, is bold.

But I like it. When a Linux distribution can make such a bold claim, it means they are trying to do something honorable and important: making Linux possible for everyone.

The problem is that a lot of distributions make that claim; while some of them succeed, some also fail.

The big question here is, does [Liya Linux](https://liyalinux.gitlab.io) make good on that claim? Knowing that this distribution is based on Arch Linux, that’s a fairly risky claim. And since Liya Linux is new to me (which is rare these days), I installed it as a virtual machine (VM) to see what it had to offer.

As soon as the installation started, I knew immediately that the developers took the claim seriously. Like many modern Linux distributions, Liya Linux offers a user-friendly, point-and-click installation.

It wasn’t until I logged in for the first time that I was able to see what the developers had done.

Before I get into that, it’s important to know that Liya uses the [Btrfs file system](https://itsfoss.com/btrfs/), complete with snapshots, as well as [Samba shares](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/) enabled by default, and a clean app selection that might not be as familiar as some distributions, but I found all of the preinstalled apps to be viable options for everyday users.

Even before I got to the app selection, the thing that immediately struck me was that Liya fooled me. Before I decided to give this distribution a try, I decided not to read up on it first because I wanted to be surprised. Right out of the gate, I was definitely taken by surprise.

When I first logged in, I assumed I was working with the [KDE Plasma desktop](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/). It was an easy assumption because it looked very much like KDE Plasma (with a few distribution-specific tweaks). The desktop was beautiful and carried the typical hallmarks of KDE Plasma.

Little did I know that the desktop was actually a customized [Cinnamon](https://thenewstack.io/what-makes-the-cinnamon-desktop-so-appealing/).

Wow. OK. I thought I knew my Linux desktops so well that I could pick them out from 100 yards. It looks like it was customized to resemble KDE Plasma, but when you start poking around, it becomes clear that you (I, actually) were wrong.

Fool me once …

That being said, this is the first time I’ve looked at the Cinnamon desktop and thought, “I really like that.” I often think Cinnamon is too boring, old school, and too Windows-y. This take on Cinnamon has just the right amount of modernity, while still clinging to the standard desktop metaphor, so it can appeal to all types of users.

It’s not until you take a gander at the Applications menu, however, that you realize Liya could well be an Arch-based distribution for the masses.

Look out, [Manjaro](https://thenewstack.io/manjaro-is-arch-linux-for-newbies/).

## Preinstalled apps

This is where things get really impressive. First off, Liya departs from the usually installed defaults and opts for the [Brave browser](https://brave.com/download/) and the [ONLYOFFICE office suite](https://www.onlyoffice.com/desktop). While this combo might not be that familiar to new users, both are very user-friendly. I actually prefer ONLYOFFICE to LibreOffice because it allows me to work both locally and via the cloud (even using LAN-based installations of the ONLYOFFICE server).

Along with those two defaults, you also get apps like Celluloid (video player), a few games, Deluges (Bittorent), Exaile (manage audio collection), Geary (email), Newelle (chat bot, Figure 1), Pika Backup, Pinta (image editor), Pix (photo organizer), Bleachbit (system cleaner), Firewall config gui, firmware installer, Gestures (gesture manager), and a lot more.

![Screenshot](https://cdn.thenewstack.io/media/2026/01/10690298-liya2.jpg)

Figure 1: Newelle is a new-ish app that makes using AI simple.

With Newelle, there’s no need to even install or connect to a large language model (LLM), as it’s all there, ready to go.

The thing that impresses me the most about Liya is that the developers have taken a nontraditional path with the default preinstalled apps, and yet they’ve created a collection that checks all the boxes. Given that so many distributions assume the best path forward is the traditional apps, it’s nice to see a distro take a different approach.

## How well does Liya perform?

The combination of Arch and Cinnamon makes for a speedy and stable desktop OS. Liya easily rivals [Linux Mint](https://thenewstack.io/reasons-to-love-linux-mint/) in both performance and usability.

Say what?

I must be crazy if I think an Arch-based distribution can live up to the ease of use found in Linux Mint. Arch is, after all, one of the most challenging Linux distros available. Although it’s easy to say that, when you’re presented with a take on Arch that is totally point-and-click, includes an outstanding collection of software, and adds a user-friendly app store on top of that, it can easily change one’s mind.

Some Arch-based distributions assume the user would rather work with the command line. There are some, however, that fully understand that the majority of people would rather avoid the command line, so they include a GUI for managing software. Manjaro was one of the first to do it, and Liya follows in those footsteps.

The graphical user interface (GUI) in question is Pamac, and although it might not be the most modern-looking app store available, it’s exponentially easier for new users than trying to understand pacman. All you have to do is open the app, search for what you want to install, and point-and-click your way to some new software. The one thing Liya doesn’t include is [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/), which means you do miss out on some important software, such as Spotify and Slack.

Fortunately, Flatpak is easily installed via [Pamac](https://itsfoss.com/install-pamac-arch-linux/). Just open the app store, search for Flatpak, and click the green install button (Figure 2).

![Screenshot](https://cdn.thenewstack.io/media/2026/01/980e5c88-liya1.jpg)

Figure 2: Installing Flatpak should be considered a necessity these days.

## Ranking of Arch-based distributions

If I had to rank Liya among the user-friendly Arch-based distributions, it might look like this:

Manjaro, Liya, EndeavourOS, Garuda Linux, Artix Linux, and CachyOS. Although I prefer the likes of EndeavorOS and Garuda to Liya, those two choices are mostly based on aesthetics. If I consider them only in terms of user-friendliness, Liya sits right behind Manjaro and could easily give it a run for its money someday.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)