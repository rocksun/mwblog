The [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) run command is a great introduction to running [containers](https://thenewstack.io/introduction-to-containers/). It’s simple, it’s quick, and it’s fairly easy to learn.

It’s also a bit limiting. For one thing, those run commands can grow quite long, and just viewing them in your terminal window can be a real challenge. As well, it’s harder to edit those commands before running them. You might want to alter the port, which means you’ll need to use your keyboard arrow keys to navigate back, one character at a time, to the exact point where you can change the default port.

Although you might start out with *docker run*, you will inevitably migrate to *docker-compose*. With *docker-compose*, you build your container from within a file, so it’s easier to craft. Even better, you can build highly complex containers with a Docker Compose .yaml file.

But some aren’t exactly too fond of working with things via the terminal window. Unless you’re like me and have been using the [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) CLI (Command Line Interface) for decades, you might fall into that category.

What do you do?

Well, you could try a web-based tool for managing your *docker-compose* files. One such tool is [Dockge](https://github.com/louislam/dockge).

According to the project’s GitHub repository, Dockge is an “easy-to-use and reactive self-hosted Docker compose.yaml stack-oriented manager.”

Sounds interesting, right?

I gave it a try to see how easy it was to use and came away impressed.

Let’s install Dockge and see how it works.

## What you’ll need

For Dockge, you’ll need an OS that supports Docker and a user with admin privileges. I’m going to demonstrate with Ubuntu Server 24.04. If you’re using a different OS, you’ll only need to modify the Docker installation instructions. With Docker already installed, you can skip to the Deploying Dockge section.

## Installing Docker and Docker Compose

### Installing Docker

Here are the steps for installing Docker:

1. **Install the official Docker GPG key**

The first step is to add the official Docker GPG key, which can be done with the following commands:

sudo apt-get update  
sudo apt-get install ca-certificates curl  
sudo install -m 0755 -d /etc/apt/keyrings  
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc  
sudo chmod a+r /etc/apt/keyrings/docker.asc

2. **Add the official Docker repository**

Add the official Docker repository with the following command:

```

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc]
https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

3. **Install Docker**

Before you can install the software, update apt with:

```

sudo apt-get update
```

Now, you can install Docker and the other components with the command:

```

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

4. **Add your user to the Docker group**

You must now add your user to the docker group. If you don’t, you’ll have to run containers with admin privileges, which can cause serious security problems. To achieve this, add your user to the docker group with:

```

sudo usermod -aG docker $USER
```

Finally, log out and log back in for the changes to take effect.

## Deploying Dockge

Although we could deploy Dockge with a Docker run command, that would feel like a slap to the face; so, we’ll deploy Dockge using the docker-compose command. Before we do that, however, there are a few steps to take.

First, create the necessary directories that will store your Dockge’s stack information/files with the command:

```

mkdir -p /opt/stacks /opt/dockge
```

Change into the Dockge directory with:

```

cd /opt/dockge
```

The developer has made a pre-configured yaml file available for downloading, so you don’t have to create it yourself. Download that compose.yaml file with the command:

```

curl https://raw.githubusercontent.com/louislam/dockge/master/compose.yaml --output compose.yaml
```

You might want to open the file for editing, in case you want to change something (such as the default port – 5001).

With that yaml file exactly how you want it, bring up Dockge with the command:

```

docker compose up -d
```

NOTE: If you use V1 of docker-compose or Podman, the command will be:

```

docker-compose up -d
```

Give Dockge a minute to spin up.

## Accessing Dockge

Once Dockge is running, open a web browser and point it to http://SERVER:5001 (where SERVER is the IP address of the hosting server). If you’ve changed the default external port, make sure to change that in the URL as well.

You will be presented with the account setup page (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/02/1629e45c-screenshot-2026-02-16-at-7.21.09-am.png)

**Figure 1:** Don’t worry, your information is saved locally, so no telemetry is sent.

Fill out the necessary information and click Create.

You should now find yourself on the Dockge main page (**Figure 2**).

![](https://cdn.thenewstack.io/media/2026/02/2915f71f-screenshot-2026-02-16-at-7.39.07-am-scaled.png)

**Figure 2:** The Dockge main page is simple to view and understand.

If you already have a stack or two running, if you click on one Dockge will report that it’s not managed by Dockge, so you can’t really do anything with them.

To start building a new stack (get it?), click Compose and start filling out the fields. It’s very easy to get up to speed with this tool. You can even add variables to an .env file from within the build page.

You can add containers as well as networks. By default, you might notice that a volumes option isn’t available. It is, it’s just a bit hidden from sight. Click the Edit button next to Delete, and you’ll see the volumes option (**Figure 3**).

![](https://cdn.thenewstack.io/media/2026/02/48d8d9db-screenshot-2026-02-16-at-7.31.11-am.png)

**Figure 3:** You *can* add volumes with Dockge.

When complete, click save, and you’ll see the Docker Compose file in all its glory (**Figure 4**).

![](https://cdn.thenewstack.io/media/2026/02/beac18bb-screenshot-2026-02-16-at-7.32.34-am.png)

**Figure 4:** Our first Docker Compose file is ready to use.

You can now start, edit, or update the stack by clicking the associated button near the top.

As you can see, getting up to speed with Docker Compose files doesn’t have to be so challenging after all.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)