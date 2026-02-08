Recently, I procured a [Zettlab AI NAS](https://www.kickstarter.com/projects/zettlab/zettlab-ai-nas-personal-cloud-for-smart-data-management?ref=6fpvej&gad_source=1&gad_campaignid=23334065990&gclid=CjwKCAiAmp3LBhAkEiwAJM2JUOP6EzOeloI--9WDIXsPXMpY9EQLbsyNU9UQJiO48lLcMgLXL_VBgxoC5uUQAvD_BwE). This was mostly to be used to house a metric ton of video files that I work with, as my external drives were constantly getting full of clips that I no longer needed to work on, but didn’t want to get rid of (you know… just in case).

After deploying the [NAS](https://thenewstack.io/openmediavault-a-linux-based-solution-for-building-a-nas/), I started poking around and noticed it had an app store. Curiosity got the best of me, so I decided to give the app store a look. As I expected, the usual trove of apps was to be found. However, one app caught my attention.

[Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/).

Yup. My NAS included Docker as an app. Even better, it wasn’t the command line Docker; it was a full-blown graphical user interface (GUI).

Interesting.

Obviously, I installed the Docker app, totally uncertain as to what it was. When the installation was completed, I opened the app and found it to be a well-designed GUI that allows me to create Docker projects, manage images and containers, and create and manage containers and networks. When creating containers, you have access to all of the features you’ll need (Figure 1), such as environment variables, limits, restart configuration, storage paths, network settings, port settings and commands.

[![](https://cdn.thenewstack.io/media/2026/01/6e89e49f-screenshot-2026-01-14-at-1.57.19-pm-scaled.png)](https://cdn.thenewstack.io/media/2026/01/6e89e49f-screenshot-2026-01-14-at-1.57.19-pm-scaled.png)

Figure 1: Creating a container from a pulled image is simple.

In fewer than two minutes, I was able to deploy an instance of Node-Red from within my NAS.

Yeah, it’s that simple.

Essentially, what this does is allow you to expand the feature set of your NAS well beyond what it might include by default.

The only downfall of this setup is that I don’t have SSH access to the NAS. This, of course, may not apply to your NAS. In fact, your NAS may not have an app store with Docker available. Because of that, you might consider purchasing a NAS that includes Docker support.

## But Why Would You Want To Do This?

Here’s why I even went down the Docker rabbit hole with my NAS. As I was looking through the app store, I noticed [Nextcloud](https://thenewstack.io/how-to-deploy-the-nextcloud-cloud-server-on-almalinux/). Being a fan of the platform, I quickly installed it, only to realize that I was limited to the [SQLite database](https://thenewstack.io/the-origin-story-of-sqlite-the-worlds-most-widely-used-database-software/), which is much slower than either MySQL/MariaDB or [PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/).

After removing the Nextcloud app, I continued searching to see if there was something I could install to serve as a CMS tool (to help me migrate from [Google](https://cloud.google.com/?utm_content=inline+mention) Drive/Docs). That’s when I saw the Docker listing. Naturally, I thought, “I can install Docker and then deploy Nextcloud with a MariaDB database.”

This, of course, brought up the next issue I faced. I attempted to set up a MariaDB container and then connect Nextcloud to that, but I was unsuccessful. I knew there had to be a way to do this, so I continued digging.

That’s when I came across the ability to create a Docker Compose file from within the Project page. All I had to do was configure the compose file correctly, deploy it and wait for everything to spin up.

Boom. Nextcloud in a box.

After I deployed Nextcloud via the Project page (and my Docker Compose file), everything was working exactly as expected. Yes, I could have simply installed the Nextcloud app from within the Zettlab App Store, but running Nextcloud with SQLite is not something I want to have to ever deal with again.

Okay, but does that answer the question as to why you would even bother using Docker through your NAS? After all, your NAS is all about storage, right? Well, imagine, if you will, you could (with the help of Docker) create your own, in-house replacement for Google Workspace. That’s been a goal of mine for some time. Of course, I could simply spin up some virtual machines (VMs) for this, but when I have a powerful enough system with puhlenty of storage space, why not make use of what I already have?

Thanks to Docker, that is not only possible but easy.

I realize that not all NAS devices are created equal. Yours might not include Docker support. I do know that major NAS devices — such as Synology, QNAP and ASUSTOR — feature Docker, so if you own one of those, make sure to enable Docker support so you can expand the features and work with your own home lab, via containers.

One of the things I appreciate about this setup is that I don’t have to remember IP addresses of the various VMs for which I’ve deployed different containers. All I have to remember is the ports assigned to each container.

Would this work in a business production environment? Probably not. Although you could possibly use it for a small department, most businesses are better off taking a more traditional path.

But if you need to quickly spin up a Docker container for your home lab (or small business), this might be the best way to go. On top of all that, you have plenty of storage to use as well (for containers and non-containers).

That’s a win-win for me.

If you have a NAS device, check to see if it supports Docker out of the box, or if you can add Docker by way of an app. If so, have at those containers!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)