If you’re like me, you depend on a lot of systems and services, even within your home [LAN](https://thenewstack.io/git-set-up-a-local-repository-accessible-by-lan/). Because I work from home, that’s amplified to the point where I need certain applications available to me that aren’t hosted by a third party, for flexibility, ease of use, reliability and security.

Thankfully, [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) is there to make deploying those apps and services considerably easier; otherwise, I’d wind up having to first deploy a collection of [virtual machines (VMs)](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/), keep them running and worry about upgrading/managing them efficiently.

Yeah, Docker makes this entire process easier. Even better, I can spin up those apps and services in seconds, instead of having to go the traditional route, which can often take quite a bit longer to deploy.

But what are the apps and services that I depend on for my LAN to keep me productive? Surprise, surprise: I have a list, and here it is.

## Nextcloud

[Nextcloud](https://nextcloud.com/athome/) has essentially become my [Google](https://cloud.google.com/?utm_content=inline+mention) services for my home LAN. I began using Nextcloud in earnest on my LAN when I started fearing that Google would use my documents within Drive to train its AI. After that thought danced across the synapses of my mind, I pulled those documents and moved them to a Nextcloud deployment on my home network. Problem solved.

But Nextcloud isn’t just a document server; it’s much more. Nextcloud is an entire suite of applications that can be used for just about every need you have for a home office. There’s audio/video chat, calendars, email, whiteboard, AI assistant and agentic AI, file sharing, collaboration, file access control, versioning, machine learning (ML), tons of integrations, monitoring/auditing and so much more.

There’s even an app store, where you can extend the feature set to meet your exact needs.

Nextcloud is free to use and can be deployed with Docker from [Docker Hub](https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers/) as simply as:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d -p 8080:80 nextcloud |

## Grocy

If you need to manage things in your home, [Grocy](https://grocy.info/) is the way to go. As you might have suspected from the name, Grocy is all about groceries and meal planning. If you’re as busy as I am, planning meals isn’t always the easiest thing to do, but this handy Docker app makes it considerably easier. Not only can you keep track of the items you have in your kitchen or pantry, but you can also categorize them by location (e.g., fridge, freezer, pantry, garage, basement, etc.) and even keep track of recipes. On top of all this, Grocy even lets you keep track of chores you need to take care of around the house. You can even keep track of batteries, charging cycles and warranties so you can take the guesswork out of when you replaced those batteries in your smoke detectors.

Grocy can be deployed with a docker-compose and a Dockerfile that looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | --- |
|  |  |
|  | services: |
|  | grocy: |
|  | image: lscr.io/linuxserver/grocy:latest |
|  | container\_name: grocy |
|  | environment: |
|  | - PUID=1000 |
|  | - PGID=1000 |
|  | - TZ=Etc/UTC |
|  | volumes: |
|  | - /path/to/grocy/config:/config |
|  | ports: |
|  | - 9283:80 |
|  | restart: unless-stopped |

## Tududi

If you want a task manager that can be accessed from any machine on your network, consider [Tududi](https://tududi.com/). Tududi can help manage those tasks and even projects with a well-designed, user-friendly UI. The Tududi feature list includes comments, due dates, project names, status, priorities, hierarchical structure for tasks and projects, smart recurring tasks, areas, notes, tags and Telegram integration.

With the Telegram integration, you get the ability to create tasks directly through Telegram messages, receive daily digests of your tasks and quickly capture ideas and to-dos on the go. You also get smart parent-child relationships such that when a recurring task generates a new instance, each generated task maintains a link to the parent, those tasks are displayed as a Recurring Task Instance (with inherited settings), users can edit the parent recurrence pattern from the child task and changes to the parent settings affect all future instances within a series.

Tududi can be installed from Docker Hub with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker pull chrisvel/tududi:latest |

## Bitwarden

[Bitwarden](https://bitwarden.com/) is one of the finest password managers on the market. The app/service enjoys one of the best feature lists of all password managers and uses industry-standard encryption. Even so, there are certain highly sensitive bits of information that I would prefer to retain on my home LAN. For that, I make use of the Bitwarden server, which can be easily deployed via Docker. The Bitwarden server acts almost identically to the standard service, only it’s housed privately, so it doesn’t have to be available beyond your LAN. With that in mind, you could house highly sensitive information, and (as long as your network is secure), you shouldn’t have to worry about anyone stumbling upon your vault or the items contained within.

Bitwarden can be deployed with Docker with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker pull ghcr.io/bitwarden/self-host:sha256-6f575e9af6ba3c4632f32497b5c73696e92e8b077f3083e4d753c2c14c70bbe6.sig |

## Portainer

If you want to manage all of your containers with the help of a powerful, web-based GUI tool, [Portainer](https://www.portainer.io/) is hard to beat. Portainer allows you to see all running containers, view all container logs, get quick console access to containers, deploy code into containers using a simple form and turn your YAML into custom templates for easy reuse. Oh, and you can deploy, stop, run and remove containers. In fact, there’s very little you can’t do with Portainer.

Portainer is considered one of the most popular container management systems in the world and does require a bit of work to get up and running. You can check out the official [Portainer documentation](https://docs.portainer.io) and get up to speed on the process.

Although this is a short list of containers I regularly use on my LAN, there’s always room for more. Make sure to check out Docker Hub to see if there’s another app/service you could benefit from.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)