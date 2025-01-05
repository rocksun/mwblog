# Bodhi Linux Offers Desktop Enlightenment
![Featued image for: Bodhi Linux Offers Desktop Enlightenment](https://cdn.thenewstack.io/media/2024/12/584b5cf1-bohdihero-1024x783.jpg)
Many moons ago, my favorite Linux desktop was[ Enlightenment](https://www.enlightenment.org/). Not only was it a unique-looking desktop, it was also highly configurable. I remember spending hours tweaking the desktop to look and feel exactly how I wanted it. And when my friends got a peek at Enlightenment, they all wanted a similar desktop.

Ya gotta run [Linux](https://thenewstack.io/learning-linux-start-here/) if you want one.

After moving away from the Enlightenment desktop, it still held a particular place in my heart, and every time I saw or used it, I was taken right back to that particular time in my life when I was wide-eyed and impressed with what I could do on a Linux desktop.

I’m used to the flexibility and reliability of Linux, but I still can’t help but smile when I see anything resembling the Enlightenment desktop.

Such is the case with [Bodhi Linux.](https://www.bodhilinux.com)

Bodhi doesn’t use the Enlightenment desktop but, rather, defaults to the Moksha desktop, which was based on Enlightenment. According to the official Bodhi website, Moksha “originates from Sanskrit, much like Bodhi, and translates to “emancipation, liberation or release.”

## Enlightenment
“It serves as a modern iteration of the Enlightenment 17 desktop environment. Moksha introduces several enhancements, such as many new features and two new modules, the integration of bug fixes and features from upcoming Enlightenment releases, and the elimination of incomplete or malfunctioning elements that were present in E17.”

Bodhi Linux has a [Ubuntu base](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/), so you get the usual tools, such as apt as a package manager.

I’ve installed Bodhi Linux several times over the years, and the process is as easy as any [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/). I did notice, this time around, that the downloading process (at the early stages of the installation) stalled a bit, but a bit of patience goes a long way. Once the downloads were taken care of, the installation zipped by, and I was ready to reboot and log in.

## First, Log In With Bodhi
Back in my earlier days of using Bodhi Linux, there was always a “first use” welcome wizard that asked a few questions regarding the Moksha desktop. That is no longer the case, which I believe was a smart choice. Now Bohdi simply dumps you onto the desktop, where you can start using the distribution.

As I was using Bodhi Linux as a [VirtualBox virtual machine](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/), the first thing I had to do was install the Guest Additions; otherwise, I couldn’t resize the screen. This didn’t come as a surprise, as Bodhi has always required this when run as a VirtualBox VM.

The default desktop has the usual green theme, and it’s beautiful. And, of course, there’s one of my favorite features found in both the Moksha and Enlightenment window managers — the desktop menu.

If you left-click on any blank space on the desktop, a menu will appear where you can access all installed applications and other entries. I’ve always found this menu to be very efficient because I don’t always have to move my cursor to the bottom-left corner of the display.

My next favorite feature in Moksha (which is also found in Enlightenment and a handful of other desktops) is window shading. Essentially, Window Shading rolls an app window into the title bar so you can better organize and access open apps (see Figure 1).

-
Figure 1: Window shading is a real highlight of the Moksha desktop.

It’s a multitasker’s dream come true. You can bet I will take any chance to use window shading on a desktop. The only hiccup with this is that the Chromium browser has to be configured to “use system title bars and borders;” otherwise, it’s borderless, and shading doesn’t work.

## Preinstalled Apps and the Appcenter
Out of the box, there’s not a lot to be found. There’s Leafpad (text editor), Chromium, Web Browser Manager (which allows you to easily install other browsers), PulseAudio Volume Control, the Synaptic package manager and a few utilities.

The Synaptic package manager allows you to easily install any applications from the standard repositories. It’s pretty old school, but it gets the job done with ease.

The Bodhi Appcenter (see Figure 2) uses Chromium to open a website that allows you to install applications, such as LibreOffice. Find the app you want to install on the site and click the associated Install button. That, however, is when the first issue appeared. When I attempted to install LibreOffice from the Appcenter, I received an error that it could not find the package “libreoffice.”

-
Figure 2: Unfortunately, Libre Office has to be installed via Synaptic.

Other applications were installed just fine in the Appcenter, but for whatever reason, Libre Office failed. That’s fine because you can open Synaptic, search for Libre Office and install away.

## Performance
Because Moksha is considered a fairly lightweight desktop, it performs exceptionally well. You’ll find Moskha to be faster than GNOME, KDE Plasma, and even rivals Cinnamon and Mate. Launch an application and it will open almost immediately. Animations are smooth, and windows move about gracefully and easily.

I ran the `sudo apt-get dist-upgrade`
command and was duly impressed with how quickly the distribution upgrade went off. Within five minutes, everything was upgraded and I could reboot into a newer iteration of Bodhi.

After the reboot, I was pleasantly surprised that the issue with the Libre Office installation in the Appcenter was resolved. Kudos to the devs on this. Even better, the already-outstanding performance was given a bit of a boost.

The one oddity I came across was the kernel that shipped with Bodhi Linux. Running the `uname -r command`
, I saw that kernel 5.15.0-130 was installed. That kernel has been around since 2021 but is supported through 2038, so it’ll be relevant for a long time. I would guess, however, that newer hardware would benefit from a new kernel. Unless you have newer hardware that isn’t recognized by the default Bodhi kernel, I would suggest sticking with the default because it works quite well.

Given that I have a soft spot in my heart for the Enlightenment window manager and I’ve used Bodhi as my default distribution before, I can highly recommend this Linux distribution to anyone looking for a desktop that is cooler than the competition, can be highly customized and performs brilliantly.

If I’ve piqued your interest, download an ISO for Bodhi Linux now and install it as a virtual machine or on a spare piece of hardware. You won’t regret it.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)