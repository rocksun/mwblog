Tuxedo Computers is on a mission to make Linux accessible to the general public. Its primary means of pulling this off is by way of outstanding laptops and desktop computers. I’ve tested several from the company’s lineup and have always been impressed.

But did you know that Tuxedo Computers also has a Linux distribution?

That’s right. [Tuxedo OS](https://www.tuxedocomputers.com/en/TUXEDO-OS_1.tuxedo) is based on [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) and uses KDE Plasma for its desktop environment. Although Tuxedo OS is optimized for Tuxedo hardware, it will run on any off-the-shelf system. I will say this: Tuxedo OS is very impressive when running on the company’s own hardware. That being said, it still runs very well on other systems and virtual machines (VMs).

For my testing/review purposes, I installed Tuxedo OS as a [VirtualBox VM](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) with 3GB of RAM and 2 CPU cores. Let’s see how it fared.

## Easy Installation Process

The installation of Tuxedo OS is as easy as any [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/); in other words, it was a total point-and-click affair. After a few clicks (and typing my username information), I had the OS up and running in under five minutes (take that, Windows).

Upon first login, I found Tuxedo’s take on KDE Plasma to be without any significant changes to what you’d see out of the box on any distribution that uses the same desktop environment. It’s clean and easy to understand.

My only complaint is one I have with so many Linux distributions: the default dark theme. I cannot understand why so many development teams opt to ship Linux with a dark theme.

## KDE Plasma Desktop Experience and Customization

That’s fine, because KDE Plasma makes it very easy to switch from dark to light. Open System Settings, go to Colors & Themes > Global Theme, and select a light option (Figure 1).

![Screenshot](https://cdn.thenewstack.io/media/2025/11/1f25f356-tuxedoos1.jpg)

Figure 1: If you don’t like any of the default options, click Get New and download your theme of choice.

One of my favorite KDE Plasma Themes is called Se7en Aero; it’s glassy and beautiful. You could spend hours combing through and installing various KDE Plasma themes, so have at it.

Of course, KDE Plasma themes don’t really have anything to do with Tuxedo OS, but they are a nice way to customize your desktop.

Let’s take a look at a few features that are unique to Tuxedo OS.

## Tuxedo Control Center and Aquaris Tool

You’ll find an icon in the system tray that looks like a black square with a white X. Click on that, and the Tuxedo Control Center pop-up appears (Figure 2). From here, you can select a power profile, enable Power save blocker and open the Aquaris Control Center.

![Screenshot](https://cdn.thenewstack.io/media/2025/11/318df86c-tuxedocc.jpg)

Figure 2: The Control Center pop-up gives you access to several cool features.

The Aquaris Control Center gives you quick access to a dashboard (Figure 3), profiles, various tools, global profile settings and more.

![screenshot](https://cdn.thenewstack.io/media/2025/11/245293f8-tuxedoaq.jpg)

Figure 3: The Aquaris tool comes in handy, especially if you’re using a laptop.

I will say this: The Tuxedo Control Center is of much more use when running the OS on official Tuxedo hardware.

## Preinstalled Applications and Software Management

Tuxedo OS includes a bevy of preinstalled applications, such as Firefox, Kate (text editor), KDE Connect (sync phone and desktop), Thunderbird, Elisa (local music player and online radio), Kamoso (webcam software), VLC media player, LibreOffice (Calc, Draw, Impress, Math, and Writer), and much more.

Although [Samba](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/) isn’t preinstalled, if you open Dolphin (the default file manager), right-click a folder, click Properties, and then open the Share tab, you can install Samba with a single click (Figure 4).

![Screenshot](https://cdn.thenewstack.io/media/2025/11/230e1e66-tuxedosamba.jpg)

Figure 4: Installing Samba is simple on Tuxedo OS.

Once Samba is installed, walk through the rest of the prompts (including a system restart), and you’re ready to start sharing folders across your LAN. You won’t have to touch the command line to get Samba up and running, and folders in your Home directory shared.

You’ll also find [Flatpak support](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) rolled into KDE Discover, so you can easily install tons of apps (including proprietary software, such as Slack and Spotify).

## Exceptional Performance and AI Capabilities

Tuxedo OS performed like a champ. I assigned the VM just over 5GB of RAM and 3 CPU cores and had zero complaints. Granted, I didn’t push the OS terribly hard — at first. During my testing, I installed [Ollama](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/) to see how well it would perform.

After the installation was completed, I pulled the llama3.2 large language model (LLM). This is a 2 GB model that took roughly two minutes to pull. Once it was ready, I queried, “What is Linux?” I was really surprised at how fast it responded. Usually, when running Ollama in CPU-only mode, it can be slow, but on Tuxedo OS, Ollama screamed. I’ve seen instances on more powerful hardware that were slower than this. I’m not sure if that’s due to the custom Tuxedo kernel or what, but it’s impressive. So, if AI is your jam, you could do a whole lot worse than Tuxedo OS.

Regular apps ran smoothly and quickly. OS updates were fast, and animations were smooth.

In the end, I have zero complaints about the performance of Tuxedo OS.

Tuxedo OS is a wonderful Linux distribution that doesn’t require a Tuxedo computer to run well (although I would recommend you give their hardware a try). If you want a solid-performing, beautiful desktop OS, [download an ISO](https://os.tuxedocomputers.com/), grab a spare computer, or spin up a VM, install Tuxedo OS, and enjoy.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)