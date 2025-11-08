How many machines do you have on your network that run [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) [containers](https://thenewstack.io/introduction-to-containers/)? One? Two? 20?

Now, how are those machines and containers performing? How quickly can you log into those machines and run the necessary commands to suss out that information? Even better, do you know the commands required to do this?

What if I told you you could deploy a container on one machine and then deploy agents on every server you need to monitor? And what if I told you this could all be done via Docker, and it’s really easy? The end result is a single dashboard that gives you quick access to resource usage for those machines used for your container deployments.

That container is called [Beszel](https://beszel.dev/), and it’s capable of displaying Docker statistics, historical data and alert functions.

The feature set of Beszel includes:

* A user-friendly web interface
* Simple configuration
* Automatic backup support
* Multiuser
* OAuth authentication
* API access

It’s easy enough to deploy and use that you’ll consider it a no-brainer.

Let me show you how to deploy Beszel and connect an agent so you can keep track of your Docker server’s system resources.

## What You’ll Need

The only things you’ll need are more than one machine that supports Docker. I’m going to demonstrate this on [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04, so if you’re using a different OS, you’ll need to alter the Docker installation process.

## Installing Docker

If you’re looking into monitoring the resources of your servers that run Docker containers, you probably already have Docker installed. On the off chance you don’t, here’s how (otherwise, skip to the next section).

**1. Add the official Docker GPG key with the commands:**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get update |
|  | sudo apt-get install ca-certificates curl |
|  | sudo install -m 0755 -d /etc/apt/keyrings |
|  | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc |
|  | sudo chmod a+r /etc/apt/keyrings/docker.asc |

**2. Add the required Docker repository with the commands:**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | echo \ |
|  | "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \ |
|  | $(. /etc/os-release && echo "${UBUNTU\_CODENAME:-$VERSION\_CODENAME}") stable" | \ |
|  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null |
|  | sudo apt-get update |

**3. Install the required software with the following command:**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y |

**4. Add your user to the Docker group:**

To run the Docker command as a standard user, you’ll need to add that user to the Docker group. This is done so you can run the Docker command without sudo privileges. Add your user to the Docker group with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo usermod -aG docker $USER |

Log out and log back in so the changes take effect.

## Deploying Beszel

We can now deploy the Beszel hub. To that, we’ll use the *docker run* command like so:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker volume create beszel\_data && \ |
|  | docker run -d \ |
|  | --name beszel \ |
|  | --restart=unless-stopped \ |
|  | --volume beszel\_data:/beszel\_data \ |
|  | -p 8090:8090 \ |
|  | henrygd/beszel |

Give this a minute or two to spin up. After that time has passed, open a web browser and point it to:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Where SERVER is the IP address of the hosting server.

You should be presented with an account creation page. Once you’ve done that, log in and you’ll see the Beszel main window (Figure 1).

[![](https://cdn.thenewstack.io/media/2025/11/da830332-beszel1.jpg)](https://cdn.thenewstack.io/media/2025/11/da830332-beszel1.jpg)

Figure 1. The Beszel hub is now ready to accept connections from agents.

## Deploying the Agents

In the upper right-hand corner, click Add System. A pop-up will appear (Figure 2), asking you to fill out the information for the server you want to monitor. Add a name and the host IP address.

[![](https://cdn.thenewstack.io/media/2025/11/d245d003-screenshot-2025-11-07-at-4.14.50%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/d245d003-screenshot-2025-11-07-at-4.14.50%E2%80%AFpm.png)

Figure 2. Fill out the information to add a new system.

Next, click “Copy Docker compose,” which will copy the necessary contents for agent deployments.

Log into the first machine you want to monitor and create a new docker-compose.yaml file with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Paste the copied content into the new file. That content should look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | services: |
|  | beszel-agent: |
|  | image: henrygd/beszel-agent |
|  | container\_name: beszel-agent |
|  | restart: unless-stopped |
|  | network\_mode: host |
|  | volumes: |
|  | - /var/run/docker.sock:/var/run/docker.sock:ro |
|  | - ./beszel\_agent\_data:/var/lib/beszel-agent |
|  | # monitor other disks / partitions by mounting a folder in /extra-filesystems |
|  | # - /mnt/disk/.beszel:/extra-filesystems/sda1:ro |
|  | environment: |
|  | LISTEN: 45876 |
|  | KEY: 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDkDP8dJ2QSK3Z9jSm3P5X1NhOlgXZI83uMq74npgk4j' |
|  | TOKEN: 7dd3-6d258uY0fn-8a19-1f66bba3c |
|  | HUB\_URL: http://192.168.1.26:8090 |

Save and close the file.

Deploy the agent with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

The agent will deploy, and within minutes, you can refresh the web page for the hub, and the new server will be listed.

You can then deploy the agent on every machine you need to monitor.

Once the agents appear, you can view their resource usage and also click the container button at the top (looks like a small 3D rectangle) to view the resource usage of every container deployed on that machine (Figure 3). The listing will also show the health status of each container.

[![](https://cdn.thenewstack.io/media/2025/11/75e50884-beszel2.jpg)](https://cdn.thenewstack.io/media/2025/11/75e50884-beszel2.jpg)

Figure 3. All your containers are belong to us!

Now that is handy.

If you need to keep tabs on the resource usage of your containers, as well as the health status, Beszel is one of the best options I’ve found that is free and easy to use. Give Beszel a try and see if it doesn’t make monitoring those containers considerably easier.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)