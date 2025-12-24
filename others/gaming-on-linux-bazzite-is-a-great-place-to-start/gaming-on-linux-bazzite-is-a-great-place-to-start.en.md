Gaming on [Linux](https://thenewstack.io/learning-linux-start-here/) got a huge boost recently, thanks to the pending release of the upcoming Steam Machine, a [compact gaming machine](https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-specs-availability/) powered by Arch Linux.

That doesn’t mean, however, you’ll have to wait for that new device to be released. Why? There are several Linux distributions that have been created with gaming in mind. One such distribution is called [Bazzite](https://bazzite.gg/).

According to the official PR material, “Bazzite makes gaming and everyday use smoother and simpler across desktop PCs, handhelds, tablets, and home theater PCs.”

Your first question might be, “What does Bazzite do differently?” The list might be short in size, but it’s huge in results. Bazzite includes the following additions to the standard Linux distribution:

* Steam, Proton, Proton+, Lutris, and Protontricks are pre-installed.
* HDR & VRR support
* Improved CPU schedulers
* Several community-developed tools and customizations to streamlining the gaming experience
* Support for several gaming controllers (Xbox, Wii, Switch, PS3/4/5, and others).
* Latest NVIDIA and Mesa drivers for AMD and Intel.
* Support for additional Wi-Fi and display hardware
* Waydroid for Android app support
* Homebrew included

You can check the entire gaming hardware compatibility listing [here](https://docs.bazzite.gg/Gaming/Hardware_compatibility_for_gaming/).

Bazzite not only works on desktops and laptops, but also on handhelds and tablets. And because you’ll be using Steam, you’ll have access to your entire Steam library.

Bazzite is also an image-based OS, which means if an update were to cause problems, you can easily roll back to a previous working image. And because Bazzite is an immutable distribution, it’s also highly secure. The entire core system is mounted in read-only mode, so those files cannot be altered.

Bazzite was built from Fedora Kinoite and uses either the KDE Plasma or GNOME desktop.

All of this comes together to create a Linux distribution that can run just about anything.

I installed the [GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/) version of Bazzite to see what was what.

## Gaming on Linux

Since Bazzite is promoted as a gaming distribution, I thought the first thing I should do is see how well it performs with Steam Games. I opened the app (there’s no installation of anything needed), logged into my account, and fired up a game in my library.

I’ve gone through these motions before and have found mixed results with some Linux distributions. I wasn’t surprised, however, at how seamlessly Steam worked with Bazzite. In minutes, I had Albion Online up and running. It’s not the most popular game on the planet, but it’s one I tend to use to test Steam on Linux.

As usual, it did take some time to download the game and start playing. All-in-all, it was about five minutes before I was testing the game (Figure 1).

[![Games screenshot.](https://cdn.thenewstack.io/media/2025/11/e1a86c37-albion.jpg)](https://cdn.thenewstack.io/media/2025/11/e1a86c37-albion.jpg)

Figure 1: Playing games on Bazzite is vastly simplified with Steam.

One thing that I’ve always understood is that using Steam on a PC isn’t quite as easy as using a dedicated console. Games have to be downloaded, space has to be reserved, etc. But once you start playing on Bazzite, it runs as well as it would on a console. In fact, I don’t think I’ve ever experienced such seamless gaming on Linux. It runs so well.

Graphics are outstanding, sound is great, and play is smooth. Of course, how well a game runs will depend on the game and the hardware. Sure, load times might be slow, but playing is solid.

You can also use Lutris as an even easier path to gaming with Bazzite. The one caveat to Lutris is that you have to download GOG files for installation of those games, and many GOG files have an associated price. But, hey, pay to play is the name of the game in this world.

## Beyond Gaming

Yes, Bazzite might be geared towards gaming, but that doesn’t mean it can’t be used for other purposes. Although the distribution doesn’t ship with much in the way of productivity, it does use [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) and the Bazaar app store, which means you can install tons of applications. With a couple of clicks, you can install anything you need (such as office suites, IDEs, browsers, and all points in between – Figure 2).

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/c1068130-bazzitebazaar.jpg)](https://cdn.thenewstack.io/media/2025/11/c1068130-bazzitebazaar.jpg)

Figure 2: The Bazaar app store is very easy to use.

I found Bazzite to be a rock-solid distribution for both productivity and creativity.

And then there’s the Btrfs Assistant (Figure 3), where you can manage Btrfs snapshots, which are used for rolling back, should a problem occur.

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/cac56082-bazzitebtrfs.jpg)](https://cdn.thenewstack.io/media/2025/11/cac56082-bazzitebtrfs.jpg)

Figure 3: This tool should be considered a must-use.

The Btrfs Assistant does have a slight learning curve, but once you get up to speed, you’ll be zipping your way through creating and managing snapshots like a pro.

## Distroshelf for Containerized Distributions

Another outstanding application included with Bazzite is Distroshelf, which allows you to quickly spin up [containerized](https://thenewstack.io/containers/) versions of Linux distributions in the same way you would with GNOME Boxes. All you have to do is download a base image and allow Distroshelf to install it (Figure 4). It does take a bit of time to get a VM up and running, but only because of the large download sizes of the required files. Other than that, it’s as easy to use as it gets.

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/e2e79e23-distroshelf.jpg)](https://cdn.thenewstack.io/media/2025/11/e2e79e23-distroshelf.jpg)

Figure 4: Distroshelf is a great way to run virtual machines in Bazzite.

All in all, I found Bazzite to be a remarkably solid and fun distribution to use. I would suggest you [download an ISO](https://bazzite.gg/#) and spin it up as either a virtual machine or on a spare system. I have the utmost confidence that you’ll enjoy the experiences as much as I did.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)