If you’re looking for a new [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) to use for development purposes, you should consider [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/). Why? In a word, Toolbox.

Toolbox is a tool that ships with Fedora Silverblue that allows you to create [containerized environments](https://thenewstack.io/containers/) for everyday software development and debugging. Thanks to Fedora Silverblue’s immutable nature (where the core of the OS is mounted read-only), Toolbox provides a familiar package-based environment where tools and libraries can be installed and used.

## The Benefits of Toolbox

The benefits of using Toolbox include:

* Keeps the host operating system clean and stable.
* Avoids clutter that can occur after installing development tools and packages.
* Access to different distributions.
* Better isolation and organization for dependencies needed on different projects.
* Safe way to experiment because you can create a container and destroy it at will.

Even though toolbox containers are isolated, they still have access to the host system, so don’t assume it’s safe to develop or run software that you wouldn’t normally run on the host. You still have to use caution.

Keep in mind that Toolbox only creates command line environments, so if you’re developing GUI apps, this isn’t the tool you need. If you’re looking to build web apps, services or other command line-friendly tools, this app can be a real treat.

And because it’s preinstalled on Fedora Silverblue, once you have the operating system installed, you’re ready to go.

## A Containerized Environment

Keep in mind that Toolbox environments have seamless access to the user’s home directory, the Wayland and X11 sockets, networking, removable devices, [systemd journal](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/), [SSH agent](https://thenewstack.io/ssh-made-easy-with-ssh-agent-and-ssh-config/), D-Bus, ulimits, /dev, the udev database and more.

Because Fedora Silverblue (and other OStree-based distributions) discourage the installation of software on the host and, instead, install software as (or within) containers, it can be difficult to set up development environments or troubleshoot via the standard methods.

Hence, Toolbox.

But how do you use Toolbox?

I’m glad you asked.

Let’s dive in.

## Your First Steps With Toolbox

When you create a new Toolbox environment, each instance includes:

* Your username and permissions.
* Access to your home directory, system and session D-Bus, system journal, and Kerberos.
* Common command line tools, such as your package manager.

Toolbox (aka Toolbx) creates mutable containers where you can install all of your favorite development/troubleshooting tools, editors, SDKs and more.

Just remember, Toolbox does not make any promises of security, so use it carefully.

The first thing you must do is to download an OCI image and create a toolbx container, which is done with the command:

```
toolbox create
```

You’ll be asked to OK the process, so type Y to continue. This pulls from the Fedoraproject registry. Depending on your network connection, this could take a couple of minutes.

Once the registry has been pulled, you then enter the new Toolbox container with the command:

```
toolbox enter
```

You can leave the container with the command:

```
exit
```

By default, the create command pulls and creates a Fedora container. If you want to pull a different distribution (such as Ubuntu 24.04), you would pull it with:

```
toolbox create --distro utuntu --release 24.04
```

When pulling anything but the default, you have to tell Toolbox which release you want to use; otherwise, it’ll error out.

As well, if you create a different container (other than the default), you have to inform Toolbox which container you want to enter, like this:

```
toolbox enter ubuntu-toolbox-24.04
```

At this point, you have access to all of the necessary tools to install whatever you need to start developing. For example, if you need [Node.js](https://nodejs.org/) on a Ubuntu container, you would enter the commands:

```
sudo apt-get update
sudo apt-get install nodejs -y
```

You can install whatever tools you need within the container.

Again, leave the container with the exit command.

You can list all of your Toolbox containers with:

```
toolbox list
```

You should see that all of your containers are currently running.

## Installing Applications Into the Toolbox Container

You can also install applications into a Toolbox container without entering it. Let’s say you want to upgrade a current Fedora container without first entering it. To do that, you would run the command:

```
toolbox run sudo dnf update
```

Or you could install NGINX with:

```
toolbox run sudo dnf install nginx -y
```

If you want to do this on a different container (such as ubuntu-toolbox-24.04), the command would be:

```
toolbox run -c ubuntu-toolbox-24.04 sudo apt-get install nginx
```

If you want to remove a Toolbox container, the command is:

```
toolbox rm NAME
```

Where NAME is the name of the container. For example, you could remove the ubuntu-toolbox-24.04 container with:

```
toolbox rm ubuntu-toolbox-24.04
```

If you want to remove all of your containers, you have to first stop them. Oddly enough, Toolbox does not have a stop command, so you have to stop them using [Podman](https://thenewstack.io/pods-is-a-handy-linux-gui-for-managing-your-podman-containers/) like so:

```
podman stop fedora-toolbox-43
```

Once you’ve stopped a container, you can remove it with:

```
toolbox rm fedora-toolbox-43
```

And that, my friends, is how you can use Toolbox to create containerized environments for development purposes. This tool is quite handy to have around. Give it a try and see if it doesn’t become your go-to.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)