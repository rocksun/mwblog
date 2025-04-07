# ReactOS, an Open Source Take on Windows
![Featued image for: ReactOS, an Open Source Take on Windows](https://cdn.thenewstack.io/media/2025/03/ece24b22-reactoshero-1-1024x652.jpg)
Did you know that there’s an open source operating system that was designed to be compatible with Windows?

This isn’t a [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) created to look and feel like Microsoft Windows. In reality, the visual similarities end at the Windows aesthetics. Sure, [any Linux distribution](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/) could ship with Wine pre-installed, which allows the user to install Windows applications, but such OSes are still Linux.

Before I continue, I think it’s well-known where I fall into the grand scheme of operating system things. I’m a Linux user [to the core](https://thenewstack.io/author/jack-wallen/) and have been for decades.

That being said, there are plenty of people out there who’d like to remain with Windows but don’t want to have to purchase a new PC when Windows 10 support goes away. And although I’d much rather recommend a Linux distribution (because it’s more secure, reliable, and runs on all types of hardware), I know there are those who refuse to even consider using Linux.

That’s where [ReactOS](https://reactos.org/) comes in. This open source take on Windows aims to:

- Create a free alternative to Microsoft Windows.
- Ensure compatibility with existing software (games, productivity apps, and other programs that rely on Windows APIs).
- Provide security improvements.
The first stable release of ReactOS was made available in 2011. In 2013, a beta release was made available that included improved support for 64-bit systems and hardware acceleration. Finally, in 2020, the project reached the Technical Alpha milestone, which meant the team had made significant progress with regards to stability and performance.

I remember the first time I tested ReactOS (which was back when it was first released). Although I could see what the OS was trying to do, it was barely usable. Now? Well, let’s just say the latest release really took me by surprise.

One thing to keep in mind with ReactOS: Do not expect anything even remotely modern look. The latest release looks very much like the old Windows XP UI.

It’s ugly.

Another thing to consider is that ReactOS approaches software management in a similar fashion to Linux. There’s the ReactOS Application Manager, which is an app store where you can install the applications you need. I even attempted to download an installer for the Opera browser, and the default web browser (which is called, are you ready for this, Internet Explorer) wouldn’t comply. I then opened the Application Manager, found Opera, installed it, and was ready to go.

Or was I?

Even with the latest available version of Opera installed, there were issues. I then went to install Firefox, only to find the versions available were way out of date. I then downloaded the latest Firefox installer (from mozilla.org) and set about to install it via the .exe.

After double-clicking the downloaded .exe file and walking through the installation wizard, I had the latest version of Firefox installed, and everything worked as expected.

Next, I downloaded the installer for the latest version of LibreOffice. During the download, I was warned that my version of Firefox was out of date, which was odd, but then it also mentioned installing on a supported platform.

Odd.

The browser still ran as it downloaded the [LibreOffice file](https://thenewstack.io/designing-libreoffice-preparing-images-graphics-editors/), so I let it continue.

Double-clicking the LibreOffice installer, nothing happened.

Frak.

Back at the Applications Manager, I found a version of LibreOffice (Figure 1), but it was way out of date (version 5.4.7.2). I will not go back to such an outdated version. Another attempted download of the latest version of LibreOffice to see if I could get the installer to run.

-
Figure 1: LibreOffice has been installed on ReactOS.

This was also when things really started to fall apart. I attempted to move the installer file from Downloads to My Documents (because that’s where I was able to get the Firefox installer to run), but that caused the file manager to crash. So, I rebooted because (ya know) Windows often needs a reboot to solve mysterious problems.

After the reboot, I attempted the install again with the same results.

The lesson here is that if you want to use ReactOS, your best bet is installing applications only from the Application Manager, as anything outside of that may or may not install or run.

## Why Bother With ReactOS?
At this point, you’re probably already tossing your hands up in the air to say, “Why bother?” That’s a valid question, and I found it difficult to come up with an answer other than you are a die-hard Windows user and you can’t afford a new machine to replace Windows 10, and Linux isn’t your cup o’ tea. ReactOS might be nearly 15 years old, but it still feels like a work in progress; it’s buggy, slow, and doesn’t support a large number of applications.

In the end, the only reason I can imagine someone would want to take up ReactOS would be to [join the developer team](https://reactos.org/contributing/#paid-jobs) to help carry the OS forward. I would imagine if the team was able to smooth out the bugs, make it possible to install more (and newer) applications, and update the UI, they’d have a game-changer on their hands.

If they were to ask me, I’d suggest upgrading the UI to look and feel more like the latest iteration of KDE Plasma. I don’t know how they are developing the OS (or if it’s even possible), but porting KDE Plasma to ReacOS would make a huge difference because they could create a desktop layout that was more like a modern take on Windows.

As it stands, it feels like you’re using an entire operating system that runs on top of Wine.

Even so, I think ReactOS is an important project because it shows what need can inspire. There is a need for an open-source operating system that is 1:1 compatible with Windows, and if that ever comes to fruition, it will do so by way of ReactOS.

I wouldn’t suggest anyone use ReactOS as a daily operating system. But if you want to see what can be done, it’s a great project to pick up. And if the team could find some new developers to pick up the cause, it might make waves and now is the ideal time for that to happen.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)