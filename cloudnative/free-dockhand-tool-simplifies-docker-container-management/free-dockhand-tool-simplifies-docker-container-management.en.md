Do you have too many [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) [containers](https://thenewstack.io/introduction-to-containers/) running? A quick check of my home lab and on just a single server, I have 10 running [Docker containers](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/). How do I manage them, let alone just keep track of what’s what?

I could deploy [Portainer](https://thenewstack.io/build-and-use-a-custom-image-with-portainer/), but that’s overkill at this point. Besides, Portainer is more an enterprise app now, so using it on a home lab, a development environment, or a small business just isn’t really all that practical.

That’s where an app like [Dockhand](https://dockhand.pro/) comes into play.

Dockhand is a powerful and easy-to-use container manager/monitor that is free to use for home labs, and I have found it indispensable for keeping tabs on my containers. With Dockhand, I can view logs, access the shell, view stacks, images, volumes, networks, registries, activities, and schedules. I can stop, pause, restart, edit, and delete containers, create health checks, check for and apply updates and so much more.

You can even create and deploy containers!

Once you start using Dockhand, you’ll wonder how you got along without it. In fact, I find I can actually do more with my Docker containers when using Dockhand than without. This app just simplifies everything.

But how do you deploy and use Dockhand?

Easily, that’s how.

Let me show you.

## Deploying Dockhand

It should go without saying that you need a platform that supports Docker. You’ll also need some running containers, which I assume you already have; otherwise, why would you need a platform for which to monitor them?

Deploying Dockhand is as simple as running this single command on your hosting platform:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d \ |
|  | --name dockhand \ |
|  | --restart unless-stopped \ |
|  | -p 3000:3000 \ |
|  | -v /var/run/docker.sock:/var/run/docker.sock \ |
|  | -v dockhand\_data:/app/data \ |
|  | fnsys/dockhand:latest |

Give the container a moment to spin up. After a couple of minutes have passed, open a web browser and point it to

[http://SERVER:3000](http://server:3000)

(where SERVER is the IP address of your hosting server). You should be presented with an empty dashboard. What we need to do next is configure your first environment.

## Adding an Environment

We’ll first add our local environment. To do this, “Add environment” from the Dashboard (**Figure 1**).

[![](https://cdn.thenewstack.io/media/2026/01/395dfa37-dockhand1.jpg)](https://cdn.thenewstack.io/media/2026/01/395dfa37-dockhand1.jpg)

**Figure 1:** Your Dockhand dashboard gives you quick access to your environments and other features.

In the resulting pop-up (**Figure 2**), all you have to do is give the environment a name and click Add.

[![](https://cdn.thenewstack.io/media/2026/01/19f5b155-dockhand2.jpg)](https://cdn.thenewstack.io/media/2026/01/19f5b155-dockhand2.jpg)

**Figure 2:** We’re adding a local environment here.

Once you’ve added the environment, you should see it appear in the Dashboard.

## Using the Dashboard

Click on the Dashboard icon in the side panel and then click on the environment you just created. What you should see now is a listing of every Docker service running (**Figure 3**).

[![](https://cdn.thenewstack.io/media/2026/01/4ee592be-dockhand3.jpg)](https://cdn.thenewstack.io/media/2026/01/4ee592be-dockhand3.jpg)

**Figure 3:** I have several containers running.

Let’s say you want to create a new container in this local environment. For that, click Create at the top. In the resulting pop-up (**Figure 4**), type the name of the image you want to pull and click Pull.

[![](https://cdn.thenewstack.io/media/2026/01/84785b7f-dockhand4.jpg)](https://cdn.thenewstack.io/media/2026/01/84785b7f-dockhand4.jpg)

**Figure 4:** If you haven’t already pulled an image, you’ll need to do so here.

I’m going to pull the latest Vaultwarden image (vaultwarden/server:latest). Once that’s taken care of, Dockhand will automatically switch you to the Container tab, where you can start building your new container (**Figure 5**).

[![](https://cdn.thenewstack.io/media/2026/01/f018396f-dockhand5.jpg)](https://cdn.thenewstack.io/media/2026/01/f018396f-dockhand5.jpg)

**Figure 5:** We’re going to deploy a Vaultwarden container.

The information you’ll need is as follows:

* Name: vaultwarden
* Volume mapings: hostpath – /vw-data/ and container path – :/data/
* Ports: Host – 443 Container – 443 (you have to use SSL for Vaultwarden)

Of course, you’ll need to fill that out according to your needs. Also, keep in

When you’ve finished filling out the necessary information for your container and click “Create container.” Your container should be listed as running.

It really is that simple.

## Troubleshooting a Container

Let’s say you have a container that’s giving you fits. What can you do? With the help of Dockhand, you can troubleshoot.

For example, I have a [GitLab](https://about.gitlab.com/?utm_content=inline+mention) container that has failed. To find out what’s going on, click the offending container from within the list of Containers, and you’ll see a Logs tab. Click that tab to reveal any information that’s been logged (**Figure 6**).

[![](https://cdn.thenewstack.io/media/2026/01/fec164ad-dockhand6.jpg)](https://cdn.thenewstack.io/media/2026/01/fec164ad-dockhand6.jpg)

**Figure 6:** My Gitlab container isn’t behaving.

The log will be set to autoscroll. I find downloading the log file makes it much easier to comb through. To do that, click the downward-pointing arrow near the upper-right corner (**Figure 7**).

[![](https://cdn.thenewstack.io/media/2026/01/cb19ec90-dockhand7.jpg)](https://cdn.thenewstack.io/media/2026/01/cb19ec90-dockhand7.jpg)

**Figure 7:** The running log of my failing Gitlab container.

The log will be a .txt file, which you can open on your machine and look through it to troubleshoot the container. Of course, you’ll need to know how to read a Docker log file to get the most out of this feature.

You can also look at the overview tab, which will give you any error codes. In my case, I see exit code 137, which indicates that a container was terminated due to an out-of-memory (OOM) condition or received a kill signal

Getting closer.

As you can see, Dockhand is incredibly handy to have around. If you’re looking for an easy way to manage your containers, I highly recommend give this system a try and see if it doesn’t simplify managing the running containers on your home lab or small business.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)