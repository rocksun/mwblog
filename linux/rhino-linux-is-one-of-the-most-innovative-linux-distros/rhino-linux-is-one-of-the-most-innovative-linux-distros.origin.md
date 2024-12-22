# Rhino Linux Is One of the Most Innovative Linux Distros
![Featued image for: Rhino Linux Is One of the Most Innovative Linux Distros](https://cdn.thenewstack.io/media/2024/12/3e57223b-rhinolinuxhero-1024x578.jpeg)
I’ve been reviewing and using [Linux distributions](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) for decades. I’ve [tried them all](https://thenewstack.io/syslinuxos-a-linux-distro-for-system-administrators/), from [the minimal](https://thenewstack.io/truenas-a-linux-distro-for-low-cost-network-attached-storage/) to those with [more features](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) than most users would ever need. I’ve reviewed desktop Linux distributions that were clearly more about efficiency than aesthetics, while I’ve also worked with distributions that cared more about the look than the functionality.

Then, there are distributions that are equal in usability and good looks. One such distribution is Rhino Linux.

[Rhino Linux](https://rhinolinux.org) is a reworking of Ubuntu, but it’s not just about re-inventing the Ubuntu desktop. Rhino Linux is a rolling release distribution, which means it’s always up to date, and you won’t have to worry about installing a new release once it’s available. Install Rhino Linux once, and as long as you keep on the update process, it will always include the newest software and security patches.
Rhino Linux also adds a few other tricks to make it a fascinating desktop distribution. For instance, you’ll find a handy search bar available from the desktop. Click the “U” on the vertical panel, and a search bar will appear. Ulauncher can be used as an application launcher, an online search tool and a directory browser.

Let me show you a few examples of how Ulauncher works.

- Open the search bar, type ~ and then you can navigate to a directory within your user’s home to view the files. Click on a file to open it.
- Type g followed by a space to run a Google search. Type so followed by a space to run a search on Stack Overflow. Type wiki followed by a space bar to search Wikipedia.
- Type the name of an application, and once the entry appears, click to launch it.
Ulauncher is a powerful search tool that makes finding what you need considerably easier. You can also add new search shortcuts. For example, say you want to add the DuckDuckGo search engine. Open Ulauncher preferences (Figure 1), go to Shortcuts, click Add Shortcut, and configure it like so:

- Name – DuckDuckGo
- Keyword – ddg
- Query or Script –
[https://duckduckgo.com/%s](https://duckduckgo.com/%s)

- Figure 1: You can add as many shortcuts as needed.
Click Save and then open Ulauncher with the keyboard combination Ctrl+Space. In the search bar, type ddg followed by a space and your search string. Hit Enter on your keyboard, and your default browser will open with the search results.

Speaking of quick access, if you look at the top of the Rhino Linux desktop, you’ll see a row of folder locations (Files, Documents, Music, Pictures, Video). If you click any of those entries, the files contained within that directory will appear. Click on an entry to open the file in question.

The Rhino Linux desktop is Xfce, but it’s configured with a unique (and beautiful) layout. Of course, since this is Xfce, there’s no end to the tweaking you can do. This customized desktop experience is called Unicorn, which is as fast as a traditional Xfce desktop but looks far more modern.

But Rhino Linux is much more than just a pretty face. This open source operating system also includes the AUR (Arch User Repositories) that work with Pacstall, which is a command line used on Ubuntu, so it can use those repositories that would otherwise not be available.

Pacstall works very similarly to the official Arch package manager, pacman. For example, if you want to install VS Codium (the open-source version of VS Code) from the AUR. This can be done with the command:

1 |
pacstall -I vscodium-deb |
You can check to see if an application is available from AUR with a command like:
1 |
pacstall -S vscodium |
The above command will list all available installation options.
One thing to keep in mind is that upon first login, you’ll be greeted by a setup wizard that allows you to add support for Flatpak, Nix, Snap and AppImage. I would suggest you enable at least one of these universal package managers by clicking the On/Off slider to the On position, then clicking Next (Figure 2).


- Figure 2: Enabling universal package managers in Rhino Linux.
When you enable Flatpak, you can also enable the Flatpak Beta Channel, as well as Flatseal (to manage Flatpak permissions).

After that, you can enable various container technologies (Figure 3), such as Docker, Podman, Distrobox, Apptainer, QEUM and VirtualBox.


- Figure 3: Adding container support to Rhino Linux.
The final screen allows you to enable Nala, GitHub CLI, Apport and Redshit. Once you’ve taken care of that, click Next, type your user password (when prompted), and everything will be taken care of.

I will say that I ran into an issue after an upgrade and ended up having to reinstall the OS. Even after running a few minutes of troubleshooting, I couldn’t figure out what happened. That’s fine because the Rhino Linux installation is incredibly simple. With a few quick clicks, the installation was off and running. When that was completed, I logged back in and started fresh. This is one of the beauties of testing via a virtual machine. I could have created a snapshot prior to the upgrade, but I’m not accustomed to Linux upgrades going sideways.

In spite of that one hiccup (that I did not experience in the second installation), I found Rhino Linux to be a fascinating and beautiful Linux distribution that would please just about any user.

If this Linux distribution sounds up your alley, I’d suggest downloading an ISO and installing it post haste. Trust me when I tell you that you won’t regret the decision. Rhino Linux is a gorgeous desktop that will appease both new users and those with plenty of Linux skills, as well as anyone looking to develop with the open source desktop.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)