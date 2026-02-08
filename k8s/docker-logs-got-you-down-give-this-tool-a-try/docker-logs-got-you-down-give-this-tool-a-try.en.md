One of the more challenging aspects of using [Docker containers](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/) is troubleshooting. Unless you are a master of the art, just the mere act of finding out *where* to begin your troubleshooting journey can be a hair-pulling adventure.

Sure, you can troubleshoot from the command line, but when you’re dealing with a metric ton of containers, that’s just not practical. After all, you don’t want to wind up working 24/7, do you?

I didn’t think so.

With that in mind, what can you do to make troubleshooting your Docker a bit easier? The most important thing you can do is view logs. Unfortunately, that’s yet another [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) task that will challenge you.

Fortunately, there are tools like [Dozzle](https://dozzle.dev).

Dozzle is an open source project that is sponsored by Docker-OSS and serves as a web-based log viewer for Docker containers. Dozzle features real-time monitoring, stand-alone and multihost deployment, supports text/JSON/multiline logs with filtering and searching, an interactive terminal, and a user-friendly UI.

Dozzle is actually quite easy to deploy, making it an outstanding option for viewing Docker logs.

I’m going to show you how to deploy this easy-to-use Docker log viewing tool on a single host. All you’ll need is a machine that supports Docker. You’ll deploy Dozzle on the machine with the containers you want to monitor.

Let’s get to it.

## Installing Docker

In the name of not skipping steps, I want to first show you how to install Docker. If you already have Docker up and running, skip to the Deploying Dozzle section below. I’ll demonstrate this on [Ubuntu Server](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04. If you use a different [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) distribution, you’ll want to alter the installation process.

### 1. Add the necessary GPG key

The first thing you must do is add the official Docker GPG key, so you can actually install the software. The commands to do this are as follows:

### 2. Add the official Docker repository

Next, we need to add the official Docker repository, so our package manager knows where to find the software, which is done like so:

### 3. Install Docker and other bits

It’s now time to install Docker and a few other pieces of the puzzle. Do this with the following command:

### 4. Add your user to the Docker group

To be able to run Docker containers without requiring admin privileges, add your user to the Docker group with:  
  
Log out and log back in for the changes to take effect.

## Deploying Dozzle

It’s now time to deploy Dozzle. To do this, issue the following command:  
  
Note the port configuration. You can use both 8080:8080 if you’re certain port 8080 isn’t already in use. In my instance, 8080 was taken, so I had to deploy with 8082:8080.

If you’re unsure of what ports are in use, you can issue the following command:  
  
If you see 8080 listed, you’ll need to use a different port.

After a few seconds, open a web browser and point it to http://SERVER:PORT (where SERVER is the IP address of the hosting server and PORT is the port you used for Dozzle). You’ll be greeted by the Dozzle Dashboard (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/01/dab88f44-screenshot-2026-01-21-at-1.34.23-pm-scaled.png)

**Figure 1:** The Dozzle Dashboard is very easy to figure out.

On the left sidebar, you should see your host listed. Click on that, and every deployed container will be shown (**Figure 2**).

![](https://cdn.thenewstack.io/media/2026/01/2ac5a146-screenshot-2026-01-21-at-1.05.03-pm-scaled.png)

**Figure 2:** I have several containers running on my host.

## Viewing logs with Dozzle

Locate the container you’re having trouble with in the sidebar and click it; you will then see all of the collected logs for that container (**Figure 3**). 

![](https://cdn.thenewstack.io/media/2026/01/df06f4de-screenshot-2026-01-21-at-1.40.17-pm-scaled.png)

**Figure 3:** My Open Notebook container is running fine, but it’s still good to check the logs.

Comb through the log to see if you find anything amiss. If a container has exited or is having trouble, you should find some information here that could help you determine what the problem is.

One thing to keep in mind is that Dozzle is a one-trick pony — it’s used for viewing log files. You can’t manage containers here, so if a container is stopped or unhealthy, you’ll either have to drop to the command line to manage it or use a tool like [Docker Desktop](https://thenewstack.io/docker-desktop-the-easiest-way-to-debug-docker-containers/), [Rancher](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/), or [Portainer](https://thenewstack.io/catching-up-with-the-founder-and-ceo-of-portainer/).

Dozzle is such an easy system to deploy and use that it’s a no-brainer to add to your Docker toolkit. Give it a try and see if you don’t find it to be invaluable.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)