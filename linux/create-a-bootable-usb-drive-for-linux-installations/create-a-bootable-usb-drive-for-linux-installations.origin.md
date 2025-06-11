# Create a Bootable USB Drive for Linux Installations
![Featued image for: Create a Bootable USB Drive for Linux Installations](https://cdn.thenewstack.io/media/2025/06/40998da4-faruk-tokluoglu-fhiny0onkuu-unsplash-1024x683.jpg)
I talk about [Linux](https://thenewstack.io/learning-linux-start-here/) pretty much [every day](https://thenewstack.io/learn-linux-file-permissions-the-easy-way-and-the-hard-way-too/) and [have for decades](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/). But when you’re so immersed in something, it’s easy to forget that not everyone is riding the same train at the same speed.

For example, when I’m [writing a review](https://thenewstack.io/kde-neon-is-the-linux-distribution-with-the-dynamic-desktop/) of a [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/), I take for granted knowing what it means when I say, “Burn the ISO to a flash drive.”

Not everyone knows that that means.

Today, I’m going to rectify that. I’ll explain what it means and show you how it’s done.

First, what does it even mean?

## Burning an ISO
It’s easy to misunderstand the concept of burning an ISO to a flash drive. Back in the day, when you copied something to external media, it was usually involved burning music to a writable CD. An ISO image is a exact digital copy of an optical disc. (“ISO” refers to the [ISO 9660](https://www.lenovo.com/us/en/glossary/iso-image/) file format, and interestingly it is not an acronym, as it is derived from the Greek word “isos” (ίσος), meaning “equal.”)

Burning an ISO isn’t just copying a file to a flash drive. If you were to copy the image straight to a USB drive and try to boot from it, nothing would happen.

That’s the crux: You burn an ISO to a USB flash drive, such that it’s bootable. When you burn the ISO image, the process overwrites all data on the drive and creates a bootable structure that includes a structured file system and a bootloader. When you boot your machine with that USB drive, the bootloader takes over and lands you in a live instance of Linux. At that point, you can either try it out or install it.

So, yeah, burning an ISO is much more involved than copying a file. Fortunately, it’s not nearly as hard as you might think.

Let me show you. I’ll explain how you burn an ISO from within Linux, macOS and Windows.

## Linux
My favorite tool to burn ISO images is [Popsicle](https://github.com/pop-os/popsicle), which is included with [Pop!_OS](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/). There are plenty of GUI applications for burning ISOs, and they’re all very user-friendly. However, I’m going to show you how it’s done using the command line.

Gasp! Don’t worry, it’s not hard.

Let’s assume you’ve already downloaded an ISO image. For example, you could download the [Ubuntu Budgie ISO](https://ubuntubudgie.org/downloads/). Once you have that file on your internal storage (saved in *~/Downloads*), open a terminal window and navigate to the directory containing the file.

Next, insert a USB drive (make sure it’s at least 8GB, just to be safe) and make sure it’s not currently mounted. To do this, locate the name of the drive with the command:

1 |
lsblk |
Let’s say the name of your drive is */dev/sdb*. You can then burn the image with the command:
1 |
sudo dd if=/home/USER/Downloads/ubuntu-budgie-XXX.iso of=/dev/sdb bs=4M status=progress |
The “XXX” above should be replaced with the appropriate release number.
Hit Enter, and the process will begin. When it completes, you can remove the USB drive and use it to install Linux on any machine you need.

## macOS and Windows
With macOS and Windows, I would highly recommend using the [balenaEtcher](https://www.balena.io/etcher) tool for this process. This tool makes burning ISO images incredibly simple.

With balenaEtcher, you select the ISO to burn, select the target and then “flash” it (**Figure 1**).

![screenshot](https://cdn.thenewstack.io/media/2025/05/f88dbd84-etcher.jpg)
Figure 1: The balenaEtcher tool makes burning ISO images as easy as it gets.

When the burning is complete, you can close the app, safely remove the USB drive and use it to install Linux on whatever machine needs this open source OS.

## Other Options
Of course, there are plenty of other options that can be used to burn an ISO image to a flash drive. Here’s a list of possible options.

**Suitable for discs (CD, DVD, Blu-ray)** — note that some of these also support burning to USB flash drives:
[ImgBurn](https://www.imgburn.com/): With this app, you can burn ISO, BIN and NRG images. The app is suitable for all versions of Windows.[PowerISO](https://www.poweriso.com/): Another app that supports several disc formats and even allows editing ISO files. The free version of this app has a size limit for ISO files, so if you’re burning larger images, you might have to pony up for the paid version.[Active@ ISO Burner](https://www.lsoft.net/iso-burner/): This app also includes command-line automation and is only available for Windows.[Free ISO Burner](https://www.freeisoburner.com/): A simple UI that supports a wide range of discs, but this one should probably be avoided, as it is bundled with software you probably don’t want.[AnyBurn](https://www.anyburn.com/): A basic ISO burner that is available for all versions of Windows from 7 on.[WinISO](https://winiso.com/): This app allows burning, editing and converting ISO files. If you go this route, you’ll want to use the paid version, as the free version is limited.[InfraRecorder](http://infrarecorder.org/): This app is open source, portable and handles basic image burning.
**Suitable for USB flash drives**:
[Rufus](https://rufus.ie/): one of the more widely used tools for burning ISO images[AnyBurn](https://www.anyburn.com/): also works with USB drives[UNetbootin](https://unetbootin.github.io/): one of the oldest ISO burning apps, and it works on Linux, macOS and Windows
**Built-in tools**:
- Some Linux distributions include built-in ISO burning apps (such as Pop!_OS Popsicle).
- Burn an ISO in Windows 10/11: Right-click an ISO image, choose “Show more options” and select “Burn disc image.”
And there you have it. You now know what it means to burn an ISO image as well as the tools necessary to make it happen.

Enjoy!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)