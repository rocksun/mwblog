Slowly but surely, I’ve been migrating over to self-hosted services so I can finally cut the cord to third parties. By keeping things within [my LAN](https://thenewstack.io/build-your-own-private-cloud-at-home-with-docker/), I enjoy more security and privacy than I would if I continued using cloud hosts.

The problem is, I wind up with a lot of different services running that I have to then access via different IP addresses and ports. But what if I wanted to simply (and quickly) view the status of those services, take a gander at statistics, or even confirm that my [Docker containers](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/) are still running as expected? Do I open a browser tab for each of those to verify things are as expected?

I could.

Or, I could make use of a single dashboard that gives me all the information I need from a centralized location. [Homepage](https://gethomepage.dev/) is not designed to replace all of the apps and services you use, but rather makes it easy for you to check in on those services and even add links to third-party services that you might need/use.

Instead of having to use a web browser tab for each, you can simply open Homepage and get a glimpse of what’s going on within your LAN-based services/apps.

I want to show you how to deploy and configure Homepage, so you can simplify your monitoring workflow.

![](https://cdn.thenewstack.io/media/2026/02/7382dcff-homepage.jpg)

## Installation

Thanks to [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), installing Homepage is actually quite easy. Of course, you do need Docker installed, so I’ll walk you through that process first.

### Installing Docker

Here are the steps for installing Docker:

1. **Add the necessary GPG key**

Before you can install the necessary Docker repository, you must first add the official Docker GPG key. The commands to do this are:

```

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

2. **Add the official Docker repository**

Now, we can add the official Docker repository with the command:

```

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. **Install Docker**

Let’s now install the necessary software with the command:

```

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

4. **Add your user to the Docker group**

To run Docker containers without requiring admin privileges (which would cause security issues), add your user to the docker group with:

```

sudo usermod -aG docker $USER
```

Log out and log back in for the changes to take effect.

### Installing Homepage

With Docker installed, you can now install Homepage. There are two ways to install Homepage: using docker-compose or docker run. Let me show you both.

To install Homepage with docker-compose, you must create a docker-compose.yml file. Before you do that, let’s create a directory within your home using the command:

```

mkdir -p ~/docker/homepage
```

Change into the new directory with:

```

cd ~/docker/homepage
```

Create the yml file with:

```

nano docker-compose.yml
```

In that file, paste the following:

```

services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    ports:
      - 3000:3000
    volumes:
      - /path/to/config:/app/config # Make sure your local config directory exists
      - /var/run/docker.sock:/var/run/docker.sock:ro # (optional) For docker integrations
    environment:
      HOMEPAGE_ALLOWED_HOSTS: gethomepage.dev # required, may need port. See gethomepage.dev/installation/#homepage_allowed_hosts
```

Before you save this file, you need to make the following changes:

* ports – if you’re already using port 3000 on your hosting server, change that to something like 3001:3000
* volumes – change /path/to/config to /home/USER/docker/homepage (where USER is your username).
* HOMEPAGE\_ALLOWED\_HOSTS – change gethomepage.dev to the IP address and port of your hosting server (such as http://192.168.1.26:3001).

Save and close the file. You can then deploy the container with:

```

docker-compose up
```

Give it a minute or so, and you should then be able to access Homepage from your browser with the address http://SERVER:PORT (where SERVER is the IP address of your hosting server and PORT is the external port being used for the service).

If you don’t want to bother with Docker Compose, you can use the docker run command like this:

```

docker run -p 3000:3000 -e HOMEPAGE_ALLOWED_HOSTS=gethomepage.dev -v /path/to/config:/app/config -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/gethomepage/homepage:latest
```

Make the same changes to the above command that you did in your docker-compose.yml file.

## Customizing Homepage

I’m not going to go into great detail about customizing Homepage because you’ll have specific needs. I will, however, give you an example to get you started.

If you go to the ~/docker/homepage directory, you’ll find two particular files:

* services.yml – where you configure the services to be monitored.
* settings.yml – where you configure the basics for Homepage.

If you want to customize the look and feel of Homepage, open the settings.yml file and have at it. You can add a custom background image and even control blur for that image. For example, you could change the name of Homepage and add a background image with a configuration like this (in settings.yml):

```

title: My Homepage

background:
  image: /images/yourimagehere.jpg
  blur: sm # sm, "", md, xl... see https://tailwindcss.com/docs/backdrop-blur
  saturate: 50 # 0, 50, 100... see https://tailwindcss.com/docs/backdrop-satura>
  brightness: 50 # 0, 50, 75... see https://tailwindcss.com/docs/backdrop-brigh>
  opacity: 50 # 0-100
```

There’s a trick to this. Above, I’ve configured the image to be found in the images directory I added to docker/homepage. To use this, I have to declare it in either the docker-compose.yml file, like this:

```

- /home/USER/docker/homepage/config/images:/app/public/images
```

Where USER is your username.

Services are configured in the services.yml file. Let’s say you have UptimeKuma running on your network and you want to:

1. Add a link to it from within Homepage
2. Add a quick ping test to know that it’s running

To do this, you would add a section for UptimeKuma:

```

- Up or Down:
    - Example UptimeKuma:
        description: "UptimeKuma"
        icon: si-uptimekuma -#5CDD8B # icons found here https://simpleicons.org/
        href: http://192.168.1.27:3001/dashboard
        ping: https://192.168.1.27
```

You can add as many services as you like. To find out more about how to configure services, make sure to check out the official [Homepage documentation for service widgets](https://gethomepage.dev/widgets/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)