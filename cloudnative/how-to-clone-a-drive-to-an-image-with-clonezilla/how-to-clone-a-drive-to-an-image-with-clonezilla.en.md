There will come a time when you need to not only [back up your data](https://thenewstack.io/linux-create-system-backups-with-rsnapshot/), but also create an image of a machine so that you can recover, should disaster strike.

Think about it: Should a server (or desktop) go down due to hardware failure, you don’t want to have to take the time to rebuild it from scratch; that could take days or hours.

Instead, you should consider using image backups. This process is simple: you use a piece of software to create an image of a currently running machine. Should that machine go down, you could then use the image to rebuild a new machine as an exact clone of the original.

I know what you’re thinking. You’re probably wondering if you’d have to create a new image as often as you would create a standard backup.

Not necessarily. You could create a monthly image and then a daily data backup. That way, you could restore the most recent image as well as the most recent data.

Before we get into this: what is an image?

Simply put, an image is a complete, byte-for-byte snapshot of an entire hard drive, including the operating system, installed programs, settings, and files. When you have an image of a system, the hardware could fail, and all you would have to do is restore the image on a new piece of hardware (that has similar architecture and at least the same size internal drive). Once the image is restored, it will be as if nothing had ever happened.

Smooth.

That’s what you want, right?

But doesn’t this sound expensive? Not if you’re using open source software like [Clonezilla](https://clonezilla.org/).

Clonezilla is a free, open source disk imaging and cloning platform that is used for system deployment, backup, and bare-metal recovery. [Clonezilla is available as an ISO image](https://clonezilla.org/downloads.php), so you can download it, burn it to a USB  flash drive, and always have it with you, in case disaster strikes.

If you’re interested in finding out how this works, read on, my friend.

## What you’ll need

To work with Clonezilla, you’ll need the following:

* Clonezilla burned to a USB flash drive.
* A location to save the image (external drive or remote server, such as SSH, [Samba](https://thenewstack.io/samba-network-shares-for-rhel-based-linux-distributions/), or WebDAV).
* A bit of time.

Let me walk you through the steps of using Clonezilla to create an image of a currently running machine.

## Step 1: Burn the image

Obviously, the first step is to download the Clonezilla ISO image and create a bootable USB drive with it using a tool like UnetBootin. Once you’ve done that, insert the USB drive into the machine for which you want to create the image.

## Step 2: Get your image repository ready

If you’re going to use an external drive to house the image, plug it into the machine that will be cloned. If you’re going to use a server, make sure it’s accepting connections and that you have the necessary credentials.

## Step 3: Boot Clonezilla

Start (or restart) the machine to be cloned and boot into Clonezilla from the USB drive. You will notice that Clonezilla does not have a GUI; this is an ncurses interface, but it’s still easy to work with.

## Step 4: Select your image directory

You will eventually come to a window asking you to select an image directory (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/02/65b29421-cz1.jpg)

**Figure 1:** Don’t be put off by the ncurses UI, as Clonzilla is easier to use than you might think.

Using your keyboard arrow keys, make the selection you want, tab to OK, and hit Enter.

## Step 5: Select your mode

Next, you’ll be asked to select the mode you want to use. Because we’re focusing on creating an image of the server, make sure to select *savedisk* (**Figure 2)**, tab to OK, and hit Enter on your keyboard.

![](https://cdn.thenewstack.io/media/2026/02/7cddf605-cz2.jpg)

**Figure 2:** I always recommend using the savedisk mode in Clonezilla.

## Step 6: Name the image

Next, you need to name the image. By default, the image will be a date, but I would suggest you add something to the name to differentiate which server it is. For example, this might be a [MySQL](https://thenewstack.io/insert-data-into-a-mysql-database-via-a-python-script/) server, so you might want to use a name like mysql-feb-25-20206-img (**Figure 3**).

![](https://cdn.thenewstack.io/media/2026/02/9c822673-cz3_new.jpg)

**Figure 3:** Give your image a unique name.

## Step 7: Select the image save location

If you go the external drive route, make sure to select which drive you want to house the data (**Figure 4**).

![](https://cdn.thenewstack.io/media/2026/02/235ca27d-cz4.jpg)

**Figure 4:** Obviously, you wouldn’t want to save your image to the internal drive, but this is just for testing purposes, and I’m using Clonezilla as a virtual machine, so I could take screenshots.

## Step 8: Choose your compression

You have two options for compression: z1p and z9p (**Figure 5**). If you have a slower machine, select z9p, otherwise, choose z1p.

![](https://cdn.thenewstack.io/media/2026/02/078a5e6f-cz5.jpg)

**Figure 5:** Selecting the compression option you want to use.

## Step 9: Optional check/repair

At this point, you can also use Clonezilla to attempt a check and repair of the disk. If you don’t want to bother with that step, make sure to select sfsck (**Figure 6**) to skip the check/repair process.

![](https://cdn.thenewstack.io/media/2026/02/0770b53e-cz6.jpg)

**Figure 6:** Should you check and repair or not?

The cloning will begin. Depending on how large and how much data the drive holds, it can take some time. Let the process complete, and (before you reboot) verify that the image file has been saved to the destination.

And that is all there is to creating a backup image of a machine with Clonezilla. Once you have the image created, you can then use Clonezilla to restore the image to a new server, so your organization doesn’t miss a beat.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)