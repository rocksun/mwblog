Imagine having an OS that won’t track you, push ads on you, and not force “free” trials on you.

Sounds like [Linux](https://thenewstack.io/introduction-to-linux-operating-system/), doesn’t it?

It should, because that’s what most Linux distributions strive for (and achieve).

But some distributions take this idea a bit further by being “free-trade.” What does free-trade mean? Well, for one, it means the developer wants nothing from you, so zero data is collected, and doesn’t charge a fee.

Essentially, it’s [FOSS](https://thenewstack.io/what-can-enterprise-open-source-really-do-for-you/) (Free Open Source Software) at its core, so you can trust the developer when they say they want nothing from you.

[Tromjaro](https://www.tromjaro.com/) is based on [Manjaro](https://manjaro.org/), but it adds quite a bit into the mix that the OG does not.

For example, Tromjaro uses a customized version of [Firefox](https://thenewstack.io/how-mozillas-ai-strategy-disconnects-from-its-browser-heritage/) (making it trade-free) so it cannot collect data, use tracking, or geo-block, and even added tools so that you can download videos, audio files, and photos from any website.

Along with those additions, the Tromjaro take on Firefox adds:

* Privacy Badger – learns to block trackers.
* uBlock Origin – content blocker.
* SponsorBlock – allows you to skip YouTube video sponsors.
* LibRedirect – redirects websites to privacy-friendly frontends.
* Sci-Hub X Now – unlocks scientific papers.
* Wayback Machine – gives you fast access to the Wayback Machine.
* KeePassXC – plugin for the password manager.
* Enable Right Click & Copy – forces right click & copy.

Manjaro also makes it easy to record your screen, send files, communicate, control remote machines, follow RSS feeds, block web content, add web apps, and use the free-trade [RiseupVPN](https://riseup.net/en/vpn).

And then there are other features, one of which I was very excited to see. That feature is called the HUD. This outstanding addition was first offered in [Ubuntu](https://thenewstack.io/ubuntu-unity-25-04-brings-back-ubuntus-biggest-miss/), back when Unity was its default desktop. The idea behind HUD is that you place the focus on a specific application (by clicking on it), press a hotkey, and it brings up a menu search tool for that app. Search for the menu item you want and press Enter.

For example, you might want to center text in LibreOffice. You could open the HUD, search for Center, and select the correct option. This prevents you from having to search through extensive menus to find what you’re looking for.

Now, before you get too excited about this feature, understand two things: Not all applications support the HUD, and I was unable to get it to work. Sadly, I tried everything (even various applications), but to no avail.

## What’s special about Tromjaro?

One of the questions I always ask myself is what a particular [Linux distribution](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/) has to offer that’s different than the competition?

Tromjaro wants to be the distribution for you that guarantees that no information will be collected. That’s important, but a lot of distributions can make that same claim.

Well, one thing that stands out with Tromjaro is that it includes a desktop layout switcher (**Figure 1**). The default desktop with Tromjaro is Xfce, and it offers six different layouts: Windows-like, MX-like, Unity-like, macOS-like, GNOME-like, and TOPX-like.

![](https://cdn.thenewstack.io/media/2026/03/dee5e54d-tromjarolayout.jpg)

**Figure 1:** The Tromjaro Xfce layout switcher.

This is very similar to what you’ll find in Zorin OS, only with Zorin OS, you can pay to activate four more layouts. Tromjaro doesn’t offer that option. Of course, it’s Xfce, so you can customize it to your heart’s content.

One aspect of Tromjaro that makes it stand out is the sheer amount of preinstalled software that it includes. This should have been obvious, given that the ISO image is nearly 6 GB in size. Open the Xfce desktop menu (**Figure 2**), and you’ll see that the developer is serious about including everything but the kitchen sink.

![](https://cdn.thenewstack.io/media/2026/03/2b5c5f5a-tromjaromenu.jpg)

**Figure 2:** The Tromjaro Xfce desktop menu reveals tons of preinstalled applications.

As well, if you open the Settings app, you’ll be greeted by more options than you’ll ever need.

Tucked within the Settings app, you’ll find an option labeled as Drivers, Kernels, Language, Time, Date, User, Accounts, Keyboard Layouts. This is the Manjaro Settings Manager, and one of the most important tools you’ll find in it is the Kernel Manager (**Figure 3**), where you can switch from the current kernel to any from a list that includes Linux 6.19.2-1, all the way down to 5.10.250-1.

![](https://cdn.thenewstack.io/media/2026/03/b1158ab9-tromjarokernel.jpg)

**Figure 3:** The Linux Kernel Manager is an important tool for those who like to ensure they have the latest kernel.

Out of the box, Tromjaro shipped with the 6.12.73-1 kernel. I decided to test the Kernel Manager and install 6.19.2-1 to see how it would fare.

After the installation of the new kernel, I rebooted and, lo and behold, the 6.19 kernel was active.

Speaking of installing software, Tromjaro includes the pacman GUI frontend, Pamac (**Figure 4**). This is an important addition because you don’t want to have to dive into the terminal to install apps if you’re new to Linux.

![](https://cdn.thenewstack.io/media/2026/03/32d1a1ed-tromjaropamac.jpg)

**Figure 4:** This GUI makes installing software much easier.

## Who is Tromjaro for?

Even with the Pamac GUI, would I be willing to recommend Tromjaro to just any user? No. Remember, Tromjaro is based on Manjaro, which is based on Arch, and Arch isn’t exactly the most user-friendly distribution available.

The reason most people agree with that sentiment is two-fold. First, it’s the rolling release nature of Arch Linux, and many believe that rolling release distributions aren’t as stable as standard releases. In all of my years of dealing with Linux, I’ve never found a rolling release distro to be unstable. The second reason is the *pacman* package manager. Although I don’t find *pacman* to be any more challenging than apt or dnf, new users should never be sent to a Linux distribution that requires use of the command line.

Well, Tromjaro avoids that by including Pamac.

Even with the Pamac GUI, I’m not going to recommend this distribution for anyone who is new to Linux. A big part of the reason for that is the use of the Xfce desktop. Although Xfce desktop isn’t at all hard to interact with, it offers far too many customizations for a new user. If you’ve never worked with Linux, and you dive into the Xfce Settings manager (**Figure 5**), you’ll find a vast array of options to configure.

![](https://cdn.thenewstack.io/media/2026/03/34bccf43-tromjaroxfcesettings.jpg)

**Figure 5:** The Xfce Settings app can be a bit overwhelming to new users.

I’m not at all averse to Xfce, but given the massive amount of customizations you can do, it wouldn’t be all that hard for someone who doesn’t know what they are doing to “break” the desktop. Because of that alone, I don’t typically recommend Xfce to those who are new to Linux.

If you do have at least an average level of Linux skills, Tromjaro is an awesome Linux distribution that could serve you well. Regardless if you’re just a web surfer, a content creator, or a developer, Tromjaro would be a swell option for your next desktop distribution.

[Grab an ISO of Tromjaro](https://www.tromjaro.com/download/) from the official site and install it to see how this take on Linux fares.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)