How do you block ads? Most people install various and sundry ad-blocking software on their computers or add browser extensions to handle the task.

Either way you go, blocking ads can help prevent your web browser from loading ads that could consume too many system resources or even inject malicious code into your system. I’ve had instances where a single ad bogged down my CPU so much that the computer came to a screeching halt. The only solution was a hard reboot.

After that, I was on a quest to do whatever it took to avoid another such instance. At first, I thought about going the browser extension route, but I realized I’d have to install extensions on every browser I used on every desktop and laptop on my home network. That’s all fine and good if you only have a few machines connected to your LAN. But what if you have considerably more?

You might want to consider an app like Pi-Hole.

[Pi-Hole](https://pi-hole.net/) is a popular open source project that provides a simple, easy-to-use solution for blocking advertisements and trackers on the internet. Instead of working on a computer-by-computer basis, Pi-Hole functions network-wide. It’s named after the mathematical constant pi (π), which represents the ratio of a circle’s circumference to its diameter.

How it works is simple: first, you deploy/install Pi-Hole, and then you configure each computer to use Pi-Hole as its DNS server. That’s it.

Pi-Hole offers network-wide protection, the ability to block in-app advertisements, improves network performance (because ads can typically slow down), and a web-based interface for statistical monitoring. Pi-Hole also includes a built-in DHCP server for even more control over your network.

Now, I want to mention something before we continue. The best way to get Pi-Hole working on your network is to point your modem/router’s DNS settings to the Pi-Hole server. The reason I mention this is that if you use AT&T Fiber, you cannot change the DNS settings on the router.

I’ve deployed and used Pi-Hole on several occasions, and every time AT&T Fiber is involved, things get tricky. However, if you’re using an ISP that allows you to change the DNS addresses on your modem/router, you should be good to go.

Let’s deploy Pi-Hole.

## Installing Docker

Since we’re deploying Pi-Hole as a [Docker container](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/), you might need to install [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) first. If you’re using macOS or Windows, you can simply install [Docker Desktop](https://www.docker.com/products/docker-desktop/), which installs the necessary Docker tools along with it. If you’re using Linux, the process is a bit more complicated. Here are the steps on Ubuntu Server 24.04.

The first step is to add the required Docker GPG key with the following commands:

1. *sudo apt-get update*
2. *sudo apt-get install ca-certificates curl*
3. *sudo install -m 0755 -d /etc/apt/keyrings*
4. *sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc*
5. *sudo chmod a+r /etc/apt/keyrings/docker.asc*

Next, add the official Docker repository with the following command:

*echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo “${UBUNTU\_CODENAME:-$VERSION\_CODENAME}”) stable” | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null*

Update and install Docker using the commands:

```

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

You then need to add your user to the Docker group (so you can manage your containers without using sudo, which can lead to security issues) with the following command:

```

sudo usermod -aG docker $USER
```

Log out and log back in so your changes take effect.

Verify that you can use Docker with:

```

docker ps -a
```

You should see an empty list without any errors presented.

## Deploy Pi-Hole

With Docker installed, we can finally deploy Pi-Hole. A few things to note:

You’ll need to make sure to change any external ports (those on the left side of the : character) to those that are available. You’ll also want to change the webserver\_api\_password (PASSWORD) to something strong and unique.

With that in mind, the docker run command for this is:

```

docker run --name pihole -p 54:53/tcp -p 54:53/udp -p 8081:80/tcp -p 443:443/tcp -e TZ=America/Kentucky/Louisville -e FTLCONF_webserver_api_password="PASSWORD" -e FTLCONF_dns_listeningMode=all -v ./etc-pihole:/etc/pihole -v ./etc-dnsmasq.d:/etc/dnsmasq.d --cap-add NET_ADMIN -d --restart unless-stopped pihole/pihole:latest
```

You’ll need to give the container a minute or two to deploy. Once the container is listed as “healthy” (using the command *docker ps -a*), you should be good to go.

## Accessing Pi-Hole

You’ll want to be able to access your Pi-Hole dashboard, which can be done by pointing a browser that is connected to your LAN to http://SERVER:PORT/admin/ (where SERVER is the IP address of the hosting server and PORT is the external port you configured in the docker run command).

You’ll be greeted by a login page, where you’ll need to type the password you configured for *webserver\_api\_password* in the docker run command.

Once you’ve logged in, you’ll see the Pi-Hole dashboard (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/03/73ca6ce1-screenshot-2026-03-16-at-12.13.48-pm.png)

**Figure 1:** A newly-deployed Pi-Hole instance is ready to be used.

## Configuring your machines to use Pi-Hole

There are two ways you can configure the computers on your network to use Pi-Hole. The more involved method is to configure each machine to use the Pi-Hole server address as its DNS address.

The next method allows you to configure DNS once and be done with it. For this, you have to have access to your ISP’s modem/router and then configure the router’s DNS to use the Pi-Hole IP address. Once you’ve done that, you’ll need to disable DHCP on your ISP’s modem/router and enable it on the Pi-Hole server.

To enable DHCP on your Pi-Hole server, go to Settings > DHCP (in the Pi-Hole web-based GUI), enable the DHCP server, configure the range of IP addresses to hand out, and then configure the router/gateway address that is associated with your modem/router **(Figure****2**).

![](https://cdn.thenewstack.io/media/2026/03/ed63edb2-screenshot-2026-03-16-at-12.17.49-pm.png)

**Figure 2:**Using Pi-Hole to serve up DHCP addresses is the more convenient route.

You can then either restart your machines or have them renew their IP address DHCP address leases, and those machines will begin using Pi-Hole’s DNS addresses, which also means they are being protected from ads.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)