[Security](https://thenewstack.io/Security/) should never be taken for granted, no matter what operating system you use. You might have a [Linux desktop](https://thenewstack.io/8-linux-desktop-distributions-to-try/) and assume it to be invincible. In that assumption, you would be wrong.

If a computer is attached to a network, it is vulnerable.

Read that aloud, again and again.

Most operating systems have built-in firewalls and other systems for protection, and that’s great. However, it doesn’t mean the OS is bulletproof. There’s always some way that your security and/or privacy can be breached, and when it does, bad things can happen.

You don’t want that.

So, what do you do?

You can employ an application firewall to beef up the security of your desktop or laptop.

One such firewall is called [Portmaster](https://safing.io/).

Portmaster is a free application firewall (although there are paid versions with more features) that offers system-wide security to expose every connection every application makes to detect anything and everything that doesn’t have your best interests in mind.

With Portmaster, you can block ads and trackers, malware, content that’s NSFW, deceptive services, set global and per-app options, monitor all network activity, set secure DNS, allow/block specific websites, block specific countries, block p2p connections, and more. This application firewall is capable of automating protection, so it’s almost a set-it-and-forget-it tool.

Portmaster was created and is maintained by [Safing.io](http://safing.io) and can be installed on Linux and Windows (sorry, macOS).

Let’s install Portmaster and see how it works.

## What You’ll Need

I’m going to demonstrate the installation of Portmaster on Linux — specifically [Ubuntu 25.10](https://thenewstack.io/ubuntu-25-10-scraps-x11-for-wayland-a-solid-step-forward/). If you use either macOS or Windows, the installation is simply a matter of downloading the installer file, double-clicking it, and following the installation wizard.

For the Linux installation, you’ll need a user with sudo privileges. For all installations, you’ll need a working network connection.

That’s it. Let’s install.

## Installing Portmaster on Linux

Portmaster comes in installer packages for both Ubuntu- and Fedora-based distributions. To install the app on Ubuntu Linux, point your web browser to the [safing.io](http://safing.io) site, click the Download drop-down, and select the .deb option. After making your selection, click Free Download and save the file in your ~/Downloads directory.

After the file downloads, open a terminal window and change into the Downloads directory with the command:

```
cd ~/Downloads
```

Install the app with the command:

```
sudo dpkg -i Portmaster*.deb
```

If you’re using a Fedora-based distribution, the installation command would be:

```
sudo dnf install Portmaster*.deb
```

The installation should go off without a hitch. Once it’s installed, you’re ready to use the app.

## Using Portmaster

When you open Portmaster, you’ll be greeted by a setup wizard. The first step is to start the Portmaster service by clicking START NOW (Figure 1),

[![screenshot](https://cdn.thenewstack.io/media/2025/11/09558bba-portmaster1.jpg)](https://cdn.thenewstack.io/media/2025/11/09558bba-portmaster1.jpg)

Figure 1: You have to start the service before Portmaster will work.

The next steps in the wizard are customizing what it blocks (trackers, ads, etc.) and selecting a Secure DNS service by default. Portmaster uses Cloudflare, but you can choose Quad9, AdGuard, and Foundation For Applied Privacy (Figure 2).

[![screenshot](https://cdn.thenewstack.io/media/2025/11/8e7a12d5-portmaster4.jpg)](https://cdn.thenewstack.io/media/2025/11/8e7a12d5-portmaster4.jpg)

Figure 2: Selecting your secure DNS service.

The nice thing about the secure DNS feature is that it protects system-wide, so it’s not limited to just your web browser.

With the setup wizard complete, you’ll find yourself on the Portmaster dashboard, where you can get a real-time view of what’s happening.

At this point, open your web browser and attempt to go to any website. You should see on the Portmaster dashboard how many connections were blocked. For example, I visited just 3 different sites and found 177 connections had been blocked (Figure 3).

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/70846388-portmaster6.jpg)](https://cdn.thenewstack.io/media/2025/11/70846388-portmaster6.jpg)

Figure 3: Portmaster has been busy.

I intentionally mistyped a URL ([msnb.com](http://msnb.com) instead of [msnbc.com](http://msnbc.com)) and Portmaster automatically blocked it (most likely because the mistyped URL led to a malicious site (Figure 4). Should that happen, Portmaster does not offer you a way to subvert the block; it’s just blocked, and you’re done.

[![Screenshot](https://cdn.thenewstack.io/media/2025/11/5dc1b492-portmaster8.jpg)](https://cdn.thenewstack.io/media/2025/11/5dc1b492-portmaster8.jpg)

Figure 4: Too bad msnb.com, Portmaster found you out.

Click on the bell icon to view your notifications. In my notifications, I was informed that five apps were making connections: Speech Dispatcher, Network Manager, Firefox, and Chronyd.

You can click on one of those apps and then configure Portmaster to act on it in specific ways. For example, when I opened the Firefox entry (Figure 5), I found that Portmaster wasn’t blocking connections (which is necessary for it to function).

[![screenshot](https://cdn.thenewstack.io/media/2025/11/e8b8cdcd-portmaster9.jpg)](https://cdn.thenewstack.io/media/2025/11/e8b8cdcd-portmaster9.jpg)

Figure 5: Configuring Portmaster to handle Firefox.

I could also click the Settings tab and configure various aspects, such as network scope, connection types, rules, filter lists, and more (Figure 6).

[![screenshot](https://cdn.thenewstack.io/media/2025/11/3ae42f4d-portmaster10.jpg)](https://cdn.thenewstack.io/media/2025/11/3ae42f4d-portmaster10.jpg)

Figure 6: There are plenty of settings you can customize to get even better results.

There’s also the Global Settings feature, where you can reconfigure the settings you were offered during the setup wizard, as well as Networking Scope, Connection Types, Rules, subdomain blocking, and more.

What I found with Portmaster is that out of the box, it performed very well. I could have taken the time to further configure the app, but it offered plenty of security without having to monkey with the settings. Of course, you may find it needs tweaking. I you do find it doesn’t quite offer enough out-of-the-box security, dive into the settings and see if you can improve it for your needs.

You can use Portmaster for free, or you can purchase a Portmaster Plus account (4€ / month, or about $4.65 US)  to add privacy, investigative features, and Safing support, or a Portmaster Pro account (9.90€ / month, or about $11.52 US), which adds SPN (Safing Privacy Network, a privacy-focused network service that routes internet connections through multiple tunnels).

I would suggest giving the free version a try. If that isn’t enough, you can always upgrade.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)