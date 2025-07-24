Are you a digital nomad who is always on the go but still needs to get things done? And by “things,” I mean develop. If that sounds like you, chances are pretty good you carry a laptop around with you. And why not? Laptops have full-blown [operating systems](https://thenewstack.io/introduction-to-linux-operating-system/) that make it possible to install and use your favorite [IDEs](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) and all the tools necessary to work on whatever projects you have to juggle.

But what if you could lighten the load a bit and use an [Android](https://thenewstack.io/how-we-engineered-capturing-android-anrs-in-otel/) tablet for some of those projects? After all, a tablet is considerably easier to carry around than a laptop (even with a keyboard case involved).

Before I get into this, know that you’re not going to be able to recreate the same type of development environment that you have on your laptop or desktop. Even so, you can still get by with a tablet and do so fairly well.

With that said, how do you get started developing on an [Android tablet](https://thenewstack.io/generative-ai-thread-runs-through-googles-new-products/)? Let me see if I can help you.

## First Things First

I don’t care how fast you can type on your phone or tablet’s virtual keyboard; you’re going to want to get a physical keyboard, otherwise, whatever you’re working on will take considerable time.

There are tons of available Bluetooth keyboards available for Android, such as [this $15 option on Amazon](https://www.amazon.com/Bluetooth-Keyboard-Protable-Rechargeable-Illuminated/dp/B098QJT63W). You don’t need anything fancy, just a keyboard, so you’re not poking at your tablet with your index fingers and thumbs.

## Linux Support

On some Android tablets (running Android 15 or newer), you can enable a Linux development environment. What this does is give you a full-blown terminal running in a sandboxed [Linux](https://thenewstack.io/choosing-a-linux-distribution/) environment. With this enabled, you have access to all the command-line tools you need, and can even install more with the *apt* package manager.

To enable the Linux development environment, you must first enable the developer tools, which is done by going to Settings > About tablet and tapping the build number 7 times. Once you’ve done that, you’ll find a Linux terminal app in your App Drawer. Make sure to run the *apt-get update* command before attempting to install any command-line tools (otherwise, it will fail).

If your tablet doesn’t include the Linux environment support, you can always install [Termux](https://play.google.com/store/apps/details?id=com.termux), which is a terminal emulator and Linux environment.

## Install a Database

If you need a database for development, you should be able to do so from within the Linux environment (either native or via Termux) with the following command (I’ll demonstrate with MongoDB and Termux):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | pkg update |
|  | pkg upgrade |
|  | pkg i tur-repo -y |
|  | pkg i mongod -y |

Once installed, you can access the MongoDB console with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

You can add the Apache web server and PHP with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Install a Code Editor/IDE

The truth is that there aren’t very many good IDEs available for Android. That doesn’t mean there are none available. You can try out the following to see if one of them suits your needs:

* [Code Studio](https://play.google.com/store/apps/details?id=com.alif.ide) – for developing Android apps, Java console programs, and websites.
* [PyCoder](https://play.google.com/store/apps/details?id=com.ikou.pycoding) – Python3 IDE with built-in AI.
* [CodeSnack IDE](https://play.google.com/store/apps/details?id=com.cloudcompilerapp) – allows you to develop with several different languages and provides easy-to-use tools such as code by samples.
* [Code Editor](https://play.google.com/store/apps/details?id=com.rhmsoft.code) – supports languages like C, C++, [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/), [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/), [JavaScript](https://thenewstack.io/introduction-to-javascript/), HTML, CSS, and more.

## Access Remote Machines and GitHub

Most of what I do is via Linux machines. On those machines, I keep an SSH server running, so I can log into them at any time. You can install an SSH client on your Android tablet, SSH into your Linux machine, and use all of the tools you have available. One of my favorite SSH clients for Android is [Termius](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client), which makes it easy to save hosts and includes all of the features you’ll need to simplify accessing your remote machines.

You can also install the [GitHub](https://play.google.com/store/apps/details?id=com.github.android) app on your tablet, so you can triage notifications, review, comment, and merge. Keep in mind that you can’t push and pull with this app. You can, however, install [Git](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/) (the command-line tool) with either Termux or via the built-in Linux environment. The commands for that would be:

* Linux environment – *apt install git -y*
* Termux – *pkg i git -y*

## Add a Project Management App

You can also add a project management app. I prefer Kanban but there are plenty of good management apps on Android, such as:

## Get the Right Tablet

The final consideration is the right tablet. You don’t want to use an underpowered device with a poor display. If you want to purchase a tablet that will give you plenty of power, a solid display, and plenty of storage, consider one of the following:

It’s not impossible to develop with your Android tablet. With just a bit of creativity, you can have a lightweight tool to carry with you that is capable of keeping you on track for your projects, no matter where the road takes you.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)