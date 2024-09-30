# Linux: Recover Files From a Machine That Won’t Boot
![Featued image for: Linux: Recover Files From a Machine That Won’t Boot](https://cdn.thenewstack.io/media/2024/09/ca82208c-anna-ogiienko-mqx2qynuhce-unsplash-1024x682.jpg)
Let me set the stage for you.

You have a server or desktop that’s been [working like a champ](https://thenewstack.io/learning-linux-start-here/) for years but all of a sudden it won’t boot.

Gasp.

To make matters worse, there are files on the internal drive that are of absolute importance. Without [those files](https://thenewstack.io/primer-get-to-know-linux-files-and-directories/), you could wind up in a real pickle.

No matter what you do, the machine won’t start up.

What do you do?

You turn to [Linux](https://thenewstack.io/Linux/).

Sure, there are tons of software out there that claim to be able to recover your data from a dying drive or machine that won’t boot but why take a chance on purchasing something unproven when you have free access to everything you need… and you know works.

Again, that something is [Linux](https://thenewstack.io/how-to-manage-linux-software/).

But how do you pull off such a feat?

It’s much easier than you think. There are, however, a few requirements.

## What You’ll Need
How this works depends on your situation. I’m going to assume the machine in question will not boot but you assume the drive is still functional. If the drive is no longer functioning, the process can get a bit trickier (and could require sending it off to a data recovery specialist).

To do this, you’ll need the means to connect the drive to another machine, a flash drive that can boot Linux, and either a second flash drive or another external drive to house the recovered files.

As far as the means to connect the drive, it can be either a full enclosure or just a cable. Either way, you need to be able to remove the drive from the dying machine and connect it to another machine. I will also show you a shortcut, in case the reason the machine will not boot is a broken OS.

Are you ready for this?

## Without Removing the Drive
Okay, let’s say you think the reason the machine won’t boot is because of a corrupted operating system. This can happen for several reasons, such as a failed Windows upgrade or (worse) a hacker.

Either way, let’s assume it’s all about the OS. That being the case, here’s what you need to do:

- Install
[Unetbootin](https://unetbootin.github.io)on another machine. - Open the application.
- Insert a flash drive.
- Select the distribution you want to download and install (I’d recommend Ubuntu).
- Select the flash drive to house the bootable Linux OS.
- Click OK (Figure 1).

-
Figure 1: The Unetbootin main window is very user-friendly.

Once the bootable drive has been created, remove it from the machine and plug it into the machine that won’t boot. Start the machine and make sure to select the USB drive as the primary boot device (how this is done will depend on your machine and BIOS).

If the machine still refuses to boot, you’ll need to skip to the next section. If the machine does boot to Linux, make sure to select “Try Linux” and not “Install.” You want to boot to the live version of the OS, as that will not make any changes to the drive housing the files you want to recover.

Once you’ve booted into the live Linux instance, plug in the second flash (or external) drive. From the desktop, open the file manager, where you should see all of the drives listed. Locate the one housing the files you need to recover and then navigate to the folder housing the files. Copy those files and then paste them into the other drive you’ve attached. Continue doing this until you’ve recovered all of the files from the original drive.

After doing this, you can shut down the machine and move the files to a machine that is currently running.

## With Removing the Drive
This process is very similar to that above, the difference being that you have to remove the drive from the machine that won’t boot and plug it into a machine that will. Once you’ve done that, if your OS detects and mounts the drive, you can simply copy the files from the connected drive to the internal drive and be done with it.

However, if the OS doesn’t detect the drive, your best bet is to create a bootable Linux flash drive, boot the system into a live instance, and go through the same process outlined above. The good news is that this will not alter the OS or any data on your internal drive. The good thing about this method is that you shouldn’t have to copy or move the files from the drive from the non-booting machine to an external drive.

Because Linux should recognize both the external and internal drives, you can simply boot into Linux, open the file manager, navigate to the files to be recovered, and move them to a folder located on the internal drive.

Once you’ve finished recovering the files, you can reboot the machine, remove the flash drive, and boot back into your OS, with the recovered files now accessible.

I’ve used both of the above methods to recover files from machines that won’t boot and have always had success. As I said, the only complication you could run into is if the source drive is dying and not even Linux can access it.

Good luck!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)