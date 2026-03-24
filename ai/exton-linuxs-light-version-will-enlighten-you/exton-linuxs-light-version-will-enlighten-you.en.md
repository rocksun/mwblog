I’ve been using [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) for a very, very long time. My Linux usage goes way back to the days of kernel version 2.0 and window managers like [AfterStep](http://www.afterstep.org/). In fact, AfterStep was the first window manager I used on Linux that opened my eyes to how flexible and amazing the open source OS is.

Soon after AfterStep, I discovered [Enlightenment](https://www.enlightenment.org/), which was equally as cool, but slightly easier to customize. Sure, Enlightenment (often referred to as simple “E”) didn’t have the fancy transparency customizations, but it had plenty of “fancy” in its own right.

Enlightenment was fast, stable, and fun.

After a few years of Enlightenment, I eventually migrated over to [Ubuntu](https://thenewstack.io/ubuntu-unity-25-04-brings-back-ubuntus-biggest-miss/) and its UI, but every so often, I would test the waters of Enlightenment, even if only to reminisce.

Thanks to those fond memories, every time I see a Linux distribution that offers the Enlightenment desktop, I can’t help but download an ISO, spin it up as a virtual machine, and see what’s what.

Such was the case with [Exton Linux’s ExLight](https://exlight.exton.net/) version, which includes the Enlightenment 0.27.1 Desktop environment, Refracta Snapshot (to create your own system based on Debian Trixie), and the Calamares 3.3.14-1 Installer Framework.

I was fairly certain what I’d find in this distribution, and I wasn’t wrong. ExLight impressed me in all the right ways.

But is it your next best path to Linux enlightenment? Let’s dive in and find out.

## What ExLight is

ExLight is a Linux distribution based on Debian 13 (aka “Trixie”), so it uses the APT package manager and has access to a vast repository of apps. ExLight performs incredibly well (even on older hardware) and is rock-solid enough for everyday usage.

The ExLight default desktop also includes just enough eye candy to give it a more modern look and feel, while also offering some of my favorite old-school features. It’s that mix of new and old that (in my mind) makes ExLight special.

## It’s all about efficiency

As I alluded to, Enlightenment is all about efficiency and simplicity.

For those who’ve never used Enlightenment, you might find the desktop looks somewhat familiar (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/03/48016ea6-exlight1-1024x634.jpg)

**Figure 1:** The default ExLight desktop makes me want to shout, “Eeeeagle!”

As you can see, you get a panel at the bottom of the display that includes the usual suspects: a “start” menu on the far left, a system tray on the far right, and app launchers in the middle.

You’ll also notice four icons that use the same image as on the desktop. Those icons are called the “Pager,” which allows you to switch between virtual desktops. You’ll see a green line under the currently active desktop.

There’s another Enlightenment feature, hidden in plain sight, that makes using this window manager (and, by design, ExLight) more efficient than many other desktops. If you left-click anywhere on the desktop, you’ll see the desktop menu, which is the same as the “Start” menu, only it’s accessible from any blank spot on the desktop (**Figure 2**).

![](https://cdn.thenewstack.io/media/2026/03/4558d1cb-exlight2-1024x630.jpg)

**Figure 2:** I remember first experiencing the desktop menu and realizing how much more efficient it was than the traditional menu.

Another hidden feature that makes the desktop so efficient is the ability to “shade” windows. What this means is that you can double-click a window titlebar and the window “rolls up,” so that all you see is the titlebar. You can have as many shaded windows on the desktop as you need and “unshade” them as necessary.

## Preinstalled apps

As far as preinstalled apps are concerned, you might find Exlight a bit “light” in that area. You’ll find Firefox, Leafpad (note pad), PCMan File Manager, Refracta Snapshot, GParted, Enlightenment File Manager, LXTerminal, XTerm, mpv (movie player), SMPlayer (media player), FileZilla (FTP client), GIMP, and a few utilities.

Although that is a lean app list, there’s also the Synaptic Package Manager (**Figure 3**), which is a GUI frontend for installing applications.

![](https://cdn.thenewstack.io/media/2026/03/2baa3bd0-exlight4-1024x676.jpg)

**Figure 3:** Synaptic might seem a bit old school, but it works like a charm.

One thing you’ll find missing from ExLight is one of the two main universal package managers, Flatpak and Snap. Of course, you can install either one with the commands:

* *sudo apt-get install snapd -y*
* *sudo apt-get install flatpak -y*

I would highly recommend installing one of those tools because they give you access to a lot of other apps (even proprietary options). With Flatpak or Snap, you’ll miss out on apps like Slack and Spotify.

If you use Flatpak, you’ll also need to set up Flathub as a repository, which can be done with the command:

*flatpak remote-add –if-not-exists flathub* [*https://flathub.org/repo/flathub.flatpakrepo*](https://flathub.org/repo/flathub.flatpakrepo)

## Performance

Remember, there’s a “light” in the name of this distribution, which indicates that it’s a lightweight take on Linux. It’s fast on older hardware and will blow you away on new machines. I did my usual testing with the Ollama AI app (install, pull llama3.2, and ask it two different questions).

The first question I always ask for this test is, “What is Linux?” It should come as no surprise that the answer came very fast. Sometimes, on less zippy distributions, there’s a lag before the response starts to appear; not so with ExLight.

The next query is more complicated:

“Write a Python GUI app that accepts user input for age, gender, email, phone, and favorite Linux distribution and append it to a file called input.txt.”

It came as no surprise that the response came as quickly as the first. In other words, ExLight passed my Ollama local AI test with flying colors.

## Is ExLight for you?

If you like the idea of an old-school Linux desktop on top of the latest iteration of Debian, then you cannot go wrong with Exlight. And although there aren’t a lot of developer tools preinstalled, you’ll find plenty in Syanptic, Flatpak, and Snap to meet or exceed your needs.

The time I spent with ExLight was a genuine pleasure, and I would highly recommend that you [download an ISO](https://sourceforge.net/projects/exlight/) and either spin it up as a virtual machine or install it on a spare machine.

You won’t regret giving this impressive distribution a try.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)