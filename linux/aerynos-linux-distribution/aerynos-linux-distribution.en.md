There are thousands upon thousands of [Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/), so when a new flavor comes into being, the first thing I check is to see what sets it apart from others.

With each passing day, that’s becoming harder and harder to do.

Nevertheless, developers never cease to amaze me with their ideas, abilities, and promises.

Such is the case with [AerynOS](https://aerynos.com/). This independent [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) distribution (meaning that it’s not based on another distro) aims to be blazing fast, effortlessly powerful, and offer updates that never fail.

That’s a tall order for nearly any Linux distribution.

Does AerynOS deliver?

Let’s find out.

## What is AerynOS?

Let’s first discuss what AerynOS is.

AerynOS is not based on any other distribution. Because of that, AerynOS is free to create and release whatever the developers want. To that end, the team has opted to use a next-generation package manager, Moss (more on that in a bit).

This distribution also features a rapid build system, called Boulder, which allows developers to create simple [YAML](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) recipes so there’s less time packaging applications and more time creating them.

The AerynOS distribution also does a great job of handling complex EFI configurations automatically to alleviate possible boot issues.

AerynOS is a new distribution, so it’s still in early development. It’s not recommended to be used as a daily OS. Instead, this is a good time to check out the distribution, test it, and report any possible bugs you’ve found. If bug hunting isn’t your bag, you can simply see what AearynOS is all about.

AerynOS defaults to the [GNOME desktop](https://thenewstack.io/what-makes-gnome-so-appealing/), but allows you to select from a number of options during the installation, such as KDE Plasma and COSMIC. For my testing, I went with COSMIC because it’s one of my favorite Linux DEs.

I did go into this knowing that AerynOS isn’t exactly ready for prime time, so I knew not to knock it down for instability issues. I can’t tell you how many times I’ve tested early iterations of Linux distributions and found them to be rock solid.

Let’s see how AerynOS fared.

## Installation

Unlike most modern Linux distributions, AerynOS doesn’t have a pretty GUI installer. Instead, you have a text-based installer that’s actually really easy to use. However, before you even launch the installer, the first thing you have to do is format your drive.

The formatting of the drive is handled via GParted, which is a GUI partition manager for Linux (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/03/fbea04f9-aerynospartition.jpg)

**Figure 1:** GParted makes partitioning drives incredibly easy.

You can’t just create a single partition, mounted at /, and call it a day. Instead, you have to do the following:

1. Create a new GPT partition table.
2. Create a boot partition of at least 2GB with the ESP flag enabled (right-click the partition and click the check box associated with GPT).
3. Apply the changes.
4. Close GParted.

At this point, you’re ready to install. Click the overview button at the top left corner of the display and then click the square of dots at the right edge of the favorites bar. In the Application Overview, click Install AerynOS, and a terminal window will open.

All you have to do here is answer the straightforward questions (select the drive for installation, create a user, add a password, and select the desktop environment you want). The installation should take about 2 minutes. When the installation is complete, reboot and log in to your new AerynOS desktop.

## First impressions

The default COSMIC layout for AerynOS (after I switched from dark to light mode) is simple: you have a dock at the bottom with quick launchers (**Figure 2**), where you can open various applications.

![](https://cdn.thenewstack.io/media/2026/03/3da798c8-aerynosdesktop.jpg)

**Figure 2:** The default COSMIC desktop is sleek and elegant.

I like how the AerynOS developers laid out COSMIC. If you don’t like the Dock mode, you can always select a Panel mode when you first log in.

If you click the square of dots on the dock (or hit your keyboard’s Super button), you open the COSMIC search tool, where you can search for files, applications, and more.

Outside of the classy COSMIC layout, there’s not much to see here. When you open the search tool, you’ll find the barest minimum of applications. Fortunately, there’s the COSMIC Store, where you can install apps to your heart’s content (**Figure 3**).

![](https://cdn.thenewstack.io/media/2026/03/b11d4808-aerynsospopshop.jpg)

**Figure 3:** The COSMIC Store is as easy to use as any app store.

The apps you install via the COSMIC Store are all Flatpak, which means you’ll get a mix of open-source and proprietary software. You can easily install Spotify and Slack from here as well.

## Performance

The developers have set out to create a Linux distribution that is blazingly fast. I will say that running AerynOS as a virtual machine puts it at a slight disadvantage (mostly due to graphics). Even so, AerynOS performed very well. Apps installed and opened quickly, the OS booted fast, and nothing seemed to slow it down.

That’s pretty impressive for such a new distribution running as a VM.

## Who is AerynOS for?

This is a bit challenging to answer, because what mostly sets AerynOS apart is under the hood. That being said, AerynOS also happens to be an atomic distribution, which means upgrades are guaranteed to work.

Atomic upgrades essentially function like this:

* When an upgrade is available, it’s applied as a separate image from the one that is currently running.
* If the upgrade succeeds, it will be applied at the next boot.
* If the upgrade fails, it’s abandoned and will be attempted later.

If you put this together with the goals of the developers, when AerynOS is available for general release, it’ll be a distribution for anyone looking to use a very fast distribution, with guaranteed boots and upgrades. Those guarantees will go a long way to ensuring users do not end up dealing with the frustrations they’ve had to endure with other operating systems (hint, hint… Windows). And with the choice of three brilliant desktops, how can you go wrong?

Give AerynOS some time to reach v1.0 and bet that you’ll find this Linux distribution will quickly climb to the top (or near the top) of the Distrowatch Page Hit Ranking tracker.

If you’re interested, [download an ISO of AerynOS now](https://aerynos.com/download/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)