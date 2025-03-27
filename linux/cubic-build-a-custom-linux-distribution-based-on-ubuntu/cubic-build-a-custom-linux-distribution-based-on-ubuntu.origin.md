# Cubic: Build a Custom Linux Distribution Based on Ubuntu
![Featued image for: Cubic: Build a Custom Linux Distribution Based on Ubuntu](https://cdn.thenewstack.io/media/2025/03/b72ba278-karographix-photography-f7rp5ed74be-unsplash-cubic-1024x668.jpg)
Have you ever wanted to build your own custom [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/)? You might have a specific need for a distribution that includes specific apps, files, and customizations so you can then turn around and install it on any number of machines on your business or home network.

It might sound like a challenging task, but there’s a GUI tool for Ubuntu (and [Ubuntu-based distributions](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)) that makes it much easier.

That app is called [Cubic](https://github.com/PJ-Singh-001/Cubic).

Cubic makes it easy to navigate the ISO customization steps (with the help of a GUI and an integrated virtual command line environment) to customize the Linux filesystem. With Cubic you can create new distributions or customize existing ones.

Cubic can be used on Ubuntu 18.04.5 and newer or Debian 11 Bullseye and newer. With Cubic, you can customize the following live ISO images:

- All versions of Ubuntu from 14.04 and newer.
- Most distributions based on Ubuntu.
- Many versions of Debian (tested on Debian 11 Bullseye and above).
- Many distributions based on Debian.
How do you use Cubic? Let me show you.

## What You’ll Need
To make this work, you’ll need a running instance of a Ubuntu-based distribution, plenty of local storage (or an attached USB drive), and a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). You’ll also need to download the ISO image for the distribution you want to customize. Do note that some distributions do not work well with Cubic. During my testing, I created ISOs from an [elementaryOS image](https://thenewstack.io/elementary-os-a-linux-distro-easy-to-use-and-easy-on-the-eyes/) and one for Debian. The end result was an ISO image from elementaryOS that wouldn’t boot but one based on Debian that worked fine, so your mileage may vary.

That’s it. Let’s get to work.

## Installing Cubic
The first thing you have to do is install Cubic. To do that, log into your Ubuntu-based distribution, open a terminal app, and first add the necessary repository with the command:

1 |
sudo apt-add-repository ppa:cubic-wizard/release |
Update apt with the command:
1 |
sudo apt-get update |
Finally, install Cubic with:
1 |
sudo apt-get install --no-install-recommends cubic -y |
Once the app is installed, you can open it from your desktop menu.
## Using Cubic
When you first open Cubic, you’ll need to select a project directory by clicking the small folder icon to the right of the drop-down (**Figure 1**).

![Cubic start page.](https://cdn.thenewstack.io/media/2025/03/826d7394-cubic1.jpg)
Figure 1: The main Cubic window is very well-designed and simple to use.

Once you’ve selected a project directory, click Next.

In the resulting window (**Figure 2**), you must first select the original ISO image to be used. Click the folder icon associated with Filename and then locate the ISO you downloaded. This will automatically fill in most of the other bits of information. If something fails to autofill, you can’t fill it in manually, so it’ll remain blank.

![Cubic screenshot.](https://cdn.thenewstack.io/media/2025/03/38377506-cubic2.jpg)
Figure 2: After you select your ISO, everything should auto-populate.

Click Next.

Cubic will then analyze the disk image, copy files from the original image to the project folder, and extract the uncompressed Linux file system. When that completes, click Customize, which will land you in the terminal-based virtual environment (**Figure 3**).

![Cubic screenshot.](https://cdn.thenewstack.io/media/2025/03/51e1bde3-cubic3.jpg)
Figure 3: The Cubic virtual environment is where you customize the distribution.

You can now use the command line you’ll use for customization. Yes, that means you’ll need to use the command line. You can use the apt or flatpak package managers to install (or remove) anything you need for the distribution. For example, you might want to install LibreOffice, GIMP, Slack, Snapd, and whatever apps you need like so:

1 |
apt-get install libreoffice gimp snapd |
One thing you cannot do is use [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) or [Snap](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/) to install apps because they cannot connect to the system bus.
You could even replace the kernel for, say, a real-time or HWE kernel for better hardware recognition and less latency, or enable zRAM for better performance.

Maybe you want to create specific users for the ISO with the command:

1 |
adduser USERNAME |
Where USERNAME is the name of the user to be added.
The tasks you can undertake from the virtual terminal is impressive. You can read more about this on the [official Cubic Terminal Page Wiki](https://github.com/PJ-Singh-001/Cubic/wiki/Terminal-Page).

Once you’ve finished with the customizations, click Next. The virtual environment will close and Cubic will then land on a page where you can remove any applications to shrink the size of the ISO it creates. You can go through the list (**Figure 4**) and select whatever apps you don’t need.

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/59b5c7d7-cubic4.jpg)
Figure 4: The Cubic app removal page.

Make sure to not select anything the system relies on to run. For this, you only want to remove user-facing applications.

When you complete that, click Next. In the resulting window (**Figure 5**), you can select the kernel you want to use.

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/9bcbd50f-cubic5.jpg)
Figure 5: I would suggest sticking with the default here.

Click Next and then, in the resulting window (**Figure 6**), select your compression level and then click Generate.

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/17f5136f-cubic6.jpg)
Figure 6: If you want smaller ISO images, use zstd or xz compression.

And now… we wait. This process can take some time (depending on the original ISO and the customizations you’ve made). When the generation completes, click Finish.

Once the generation completes, you receive a summary and can click Close. Your new custom ISO image will be found in the project directory you selected at the beginning of the process. You can burn that image to a USB drive or share it with other people, who can then install the distribution at will.

And that, my friends, is you how can create a custom Linux distribution based on Ubuntu or Debian. Enjoy this awesome tool.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)