# EndeavourOS Neo Provides a Stylish Route to Arch Linux
![Featued image for: EndeavourOS Neo Provides a Stylish Route to Arch Linux](https://cdn.thenewstack.io/media/2024/12/6c89a5c1-endeavorhero-1024x645.jpg)
Arch Linux has a reputation for being a real pain to install. If you want the OG [Arch Linux](https://archlinux.org/) — self-described as “a simple lightweight distribution” — you’ll need to either configure a text file or use a script, as there is no traditional installer on most modern [Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/).

Because of that, Arch Linux is rarely considered an option for users with little to no experience with the [open source operating system](https://thenewstack.io/choosing-a-linux-distribution/).

That’s okay because there are plenty of variations on the Arch theme that make it considerably easier to install the OS while remaining very much Arch at heart.

One such distribution is called [EndeavourOS](https://endeavouros.com). Although this take on Arch isn’t the oldest around (first released in May 2019), it’s one of my favorite options for getting an incredibly stable desktop operating system.

The highlight of EndeavourOS is the addition to the Calamares Installer, so you don’t have to walk through the overly complicated text-based installer. Calamares is a point-and-click affair that is simple enough for anyone to install this operating system.

The EndeavourOS team has taken Calamares one step further by customizing the installer to include support for both online and offline installation. With an offline installation, you do not have to have a working network connection during the process. For this installation, the Xfce desktop (complete with EndeavourOS theming) will be installed.

As for the online installer, you get a choice from 9 different desktop environments, such as GNOME, Plasma Desktop, Xfce, LXQt, i3 and more. Instead of going the normal route with either GNOME or Plasma Desktop, I initially decided to go with the i3 tiling window manager because it’s something to be experienced.

However, after the installation and remembering how complicated i3 can be, I decided to instead review the Plasma version of EndeavourOS, as part of its latest release EndeavourOS Neo. After all, the idea behind this distribution is to make Arch Linux easy enough for the average user, and i3 does not fit that bill. Ergo — Plasma Desktop.

Before I get into the desktop UI, let’s talk about what EndeavourOS ships with. The default list of applications isn’t exactly extensive, but there’s always the app installer (easily accessed from within the Welcome tool), which allows you to add all sorts of apps.

For example, if you want to install the [LibreOffice office suite](https://thenewstack.io/designing-libreoffice-preparing-images-graphics-editors/), go to the Welcome app and click the Add More Apps tab. From there, click “Choose popular apps to install,” expand the Office entry, select LibreOffice fresh (latest, greatest version) or still (stable version), and click Install Now (Figure 1).

-
Figure 1: Installing the fresh version of LibreOffice.

When prompted, type your user password and OK the installation. When the installation is finished, hit Enter on your keyboard to dismiss the window. You can then either install more applications or open LibreOffice from your desktop menu.

Or, you can always go the command route. To install LibreOffice Fresh, the command would be:

1 |
sudo pacman -S libreoffice-fresh |
I might also suggest installing the Pamac GUI for the pacman package manager. To do that, open the terminal window and issue the command:
1 |
yay -S pamac-aur |
The reason why you use yay instead of pacman is that pacman doesn’t support the AUR repository, which is where Pamac is located. Once you’ve installed Pamac, you’ll find it in your desktop menu, where you can open it and install applications to your heart’s content (Figure 2). After installation, you’ll find Pamac in the desktop menu located at *System > Add/Remove Software*.
-
Figure 2: The Pamac GUI is so much easier than the included installer.

I realize using Pamac goes against the ethos of EndeavourOS (which would have you default to the command line) but a distribution intent on making Arch Linux easier should make everything easier for the end user, and Pacmac does just that.

Of course, you also get Python3 installed, Firefox, the Kate text editor, Meld (for “diff’in” files), KDE Connect (for connecting other devices) and VLC media player, as well as the Haruna media player.

I would also suggest you install Flatpak so you can gain access to even more applications. To do that, issue the command:

1 |
sudo pacman -S flatpak |
With Flatpak installed, you can add third-party apps, such as Spotify, Slack and others.
## Those Pesky Dark Themes
Out of the box, EndeavourOS is very much a dark-themed distribution. I’m not a big fan of dark themes, so I set about switching to a lighter theme, which is done in System Settings > Colors & Themes, and choose a light theme.

The only caveat to this is that only the Breeze Dark EndeavourOS theme includes all the customizations done by the development team. Even so, this is Plasma Desktop, so it’s still beautiful.

You can also click the Get New Themes in the top right corner of the Global Theme window, which will open a new window containing tons of themes to choose from. Some of these themes are fairly basic, while others actually configure your desktop with various effects.

One of my favorite themes is the Apple MacOS Theme [White Sur] by Vince. With this theme, you could also add a top bar and configure the panel to look more like a dock. Viola, you have a very Apple-like desktop (Figure 3).

-
Figure 3: I’ve Mac-ified my desktop!

If you’re unsure of which version you should use, the combination of KDE’s Plasma Desktop and the Arch underpinnings make for a very performant system. With all of the configuration options found in Plasma Desktop, you can be sure you’ll be able to configure the desktop exactly how you want it.

## In the End…
Who is EndeavourOS for? Well, if you read too much into the forums, you might be so inclined to think that it’s all about the experienced user or those who might not have much experience with Linux but want to hit the ground running. However, with just a little work, you can have a version of EndeavourOS that is perfectly capable of serving anyone, regardless of their experience level.

Even better, EndeavourOS is a beautiful desktop operating system, and for anyone who wants to get a taste of Arch Linux, this is a great option. And even though the definition used on the default desktop wallpaper might make you think the developers expect you to put in the effort to get this up and running, from my experience, that’s not exactly necessary. Install Pamac and Flatpak and then use those tools to install the software you require.

EndeavourOS gives you Arch Linux without all the Arch-ness.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)