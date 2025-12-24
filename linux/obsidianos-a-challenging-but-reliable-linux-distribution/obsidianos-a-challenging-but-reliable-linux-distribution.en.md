Before we get into the review of ObsidianOS, let’s talk about A/B partitioning. It is essential to everything about ObsidianOS.

## What Is A/B Partitioning?

A/B partitioning is a method to make seamless software updates a reality. Essentially, you are assured you will always have a working system, even though this distro isn’t immutable.

Here’s how A/B partitioning works:

You have a device with two “slots” — let’s call them A and B.

While you’re running Slot A, Slot B receives new updates in the background (so you are not interrupted).

When the update is complete, you reboot and select Slot B to be used. You log into Slot B, and then the entire process happens again, only with the background updates going to Slot A.

This update process always ensures that you won’t wind up with a brick on your desk or lap. You will always have a working partition to boot to, which means you can rest assured your PC will always work.

It’s kind of rare to use A/B partitioning on a standard [Linux file system](https://thenewstack.io/8-linux-desktop-distributions-to-try/). Most often, this kind of system uses [Btrfs](https://btrfs.readthedocs.io/en/latest/) copy-on-write file system because it allows for simple rollback. To have A/B partitioning on a system with a more reliable file system is a big win.

With that said, let’s learn more about ObsidianOS.

## What ObsidianOS Is Like

First off, you can download an ISO with a minimalist desktop, KDE Plasma, or COSMIC. I decided to go with the KDE Plasma variation to see what the developers did to it.

When testing, I typically use a [VirtualBox VM](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/) for the OS in question. In order for ObsidianOS to boot, I had to enable UEFI from within the Settings window. Once that was taken care of, I logged into the Live desktop (username user and an empty password) and began the installation process.

The installer was a bit flaky, with certain text unreadable (which caused me to have to guess a few times), and then it crashed on me. I ran the installer a second time. Again, the installation failed, so I rebooted the virtual machine to give it one more try.

Third time was not the charm, so I opted to go with the minimal option, which uses a text-based installer (Figure 1).

![](https://cdn.thenewstack.io/media/2025/12/5fc58e22-obsidian1.jpg)

Figure 1: Using the ObsidianOS text-based installer.

Turns out, there was a question I answered incorrectly using the GUI (because the pop-up window wasn’t legible). When prompted to Unmount slot “a” to slot “b” accept the default N and not Y. Do that, and the installation will work like a charm.

However, if you go this route, you’ll wind up with a text-based only system. On top of that, the installation didn’t give you the option to create a new user.

The installation of a [Linux distribution](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/) should not be this hard. Ever.

I then had to install both sudo and nano. First, I logged into the console-based system with user root and no password. Create a new user with:

```

useradd -m USERNAME
```

Where USERNAME is the user you want to add.

Set a password for that user with:

```

passwd USER
```

Then, I ran:

```

pacman -S sudo nano
```

Open the sudoers file with:

```

EDITOR=nano visudo
```

In that file, add the following:

```

USERNAME ALL=(ALL) ALL
```

Where USERNAME is the username you added earlier.

Save and close the file.

Update everything with:

```

pacman -Syu
```

Instead of installing KDE Plasma, I went with GNOME because it’s more straightforward to install. That can be accomplished with:

```

pacman -S xorg
```

Next, install GNOME with:

```

pacman -S gnome
```

When that completes, enable the login manager with:

```

sudo systemctl enable --now gdm.service
```

When the login window appears, type your username and password, and GNOME is ready to use (Figure 2).

![Screenshot.](https://cdn.thenewstack.io/media/2025/12/39825f1c-obsidian2.jpg)

Figure 2: Finally, I have a desktop.

Once on the desktop, you can install apps with pacman or [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/).

## ObsidianOS Control Center

Remember me mentioning A/B partitioning? Here’s where things get interesting. Open the ObsidianOS Control Center from the Application Overlay. In the Slots tab (Figure 3), you can switch the current active slot or switch once (during the next boot). Once you’ve switched slots, it’ll take effect on the next boot.

![screenshot](https://cdn.thenewstack.io/media/2025/12/4fc8fecf-obsidian3.jpg)

Figure 3: Managing A/B partition with a handy GUI.

Before you do that, however, you should download an update. For that, click the System Updates tab and click Download update (Figure 4).

![Ssccreenshot.](https://cdn.thenewstack.io/media/2025/12/f10da50c-obsidianupdates.jpg)

Figure 4: Make sure to select either slot a or b for the download. If you’re using slot a, download the update to target slot b.

With the update taken care of, go back to the Slots tab and make the switch.

## Who Is ObsidianOS For?

This is a tough question, but I believe the answer is that ObsidianOS is for users who want an operating system that will always work. But this means that ObsidianOS is best used by those with plenty of Linux experience.

If you’re new to Linux, and you choose ObsidianOS as your first distribution, you’ll find yourself in a world of confusion.

However, for those with plenty of Linux skills, ObsidianOS is a real treat.

If I’ve piqued your interest, [download an ISO of ObsidianOS](https://files.obsidianos.xyz/) and either try it out as a virtual machine or on a spare PC.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)