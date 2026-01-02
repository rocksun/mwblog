If you run a collection of servers, be they a [home network](https://thenewstack.io/containerized-apps-for-your-home-network/) lab or those powering your business, you are going to want to know the status of each server or service.

That can be a real pain in the kiester if you have a lot of servers that you have to monitor regularly. Imagine if you had to log into each one of them individually to check on their status.

Or, maybe you have several [Docker containers](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/) that you need to keep tabs on to make sure they’re up and running. If they go down, you might even want to be alerted.

What do you do?

You could turn to an easy-to-use Docker container, [Uptime Kuma](https://uptime.kuma.pet/).

Uptime Kuma can monitor several services, from ping, HTTP(S), [MySQL](https://thenewstack.io/insert-data-into-a-mysql-database-via-a-python-script/), TCP port, SMTP, SNMP, gRPC(s), DNS, Docker containers and more. Most of the service setups are fairly straightforward, and the UI is incredibly well designed.

I’m going to show you how to install Uptime Kuma and add some hosts to keep an eye on.

## What You’ll Need

To use Uptime Kuma, you’ll need a host server (or desktop) that supports Docker and some hosts to monitor. If you’re using Uptime Kuma on [Linux](https://thenewstack.io/introduction-to-linux-operating-system/), you’ll need a user with sudo privileges so you can install Docker. As usual, I’ll demonstrate this on Linux (specifically, Ubuntu Server 24.04). If your hosting OS is different, make sure to alter the installation instructions accordingly. If you already have Docker installed, skip to the Uptime Kuma deployment section.

Ready? Let’s go.

## Installing Docker

### 1. Install the Dependencies

The first step is to install the necessary dependencies with the commands:

### 2. Add the Official Docker GPG Key

The next thing to do is add the official Docker GPG key. To do that, use the following commands:

### 3. Add the Correct Repository

You can now add the Docker repository, which is done with the following command:

Once that’s taken care of, update apt with:

### 4. Install Docker

It’s now time to finally install Docker, which is taken care of with the command:

### 5. Add Your User to the Correct Group

It’s required to add your user to the Docker group; otherwise, you’ll have to run Docker with admin privileges, which can lead to security issues. Add your user to the Docker group with:

Log out and log back in so the changes take effect.

## Deploying Uptime Kuma

Deploying Uptime Kuma can be done with a single command:

However, before you do that, consider whether you want to monitor Docker Containers on that server. If you do, you have to bind the /var/run/docker.sock to your Uptime Kuma container, which is done with the command:

Give Uptime Kuma a moment to start, and then point your browser to http://SERVER:3001 (where SERVER is the IP address of the hosting server).

The first thing to do is select your language and the database you want to use (Figure 1). I chose Embedded MariaDB because it’s the easiest route.

![](https://cdn.thenewstack.io/media/2025/12/e343f97e-screenshot-2025-12-24-at-10.54.46-am.png)

Figure 1: Choose your database wisely.

You’ll then be prompted to create a new admin account (Figure 2).

![](https://cdn.thenewstack.io/media/2025/12/2cd04eff-screenshot-2025-12-24-at-11.00.47-am-638x1024.png)

Figure 2: Make sure to use a strong/unique password for this account.

After setting up your admin user, you’ll find yourself on the Uptime Kuma dashboard (Figure 3), where you can start adding hosts/services to monitor.

![](https://cdn.thenewstack.io/media/2025/12/d9d2e3ab-screenshot-2025-12-24-at-1.27.39-pm-scaled.png)

Figure 3: I’ve already added a few hosts to monitor (one of which is down … gasp!).

## Adding a Host

I’ll now show you how to add a monitor for a Docker container. The Docker container I’ll add is hosted on the same server as Uptime Kuma (as I’ve yet to figure out how to get it to work with remote containers).

To monitor a container, you’ll first need to locate the container ID, which can be found using the command:

Copy the full ID of the container you want to monitor.

Next, go back to the Uptime Kuma dashboard and click Add New Monitor in the upper left corner. In the resulting pop-up (Figure 4), you’ll need to fill out the following information:

* Monitor Type: Docker container.
* Friendly Name: A human-readable name.
* Container Name / ID: The container ID to be monitored.
* Docker Host: You’ll have to click the + button, type localhost for the Friendly Name space, and click Save.

![](https://cdn.thenewstack.io/media/2025/12/a1c65782-screenshot-2025-12-24-at-1.36.40-pm.png)

Figure 4: Adding a Docker container for monitoring with Uptime Kuma.

Click Save, and the host is added. You should immediately see it listed on the dashboard.

And that’s the gist of getting Uptime Kuma up and running. With this easy-to-use tool, you can add as many servers and services as you need to monitor, so you don’t have to log into those machines individually or pay the high cost of a proprietary, complex monitoring system.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)