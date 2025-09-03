If you’ve used [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) as your [container](https://thenewstack.io/introduction-to-containers/) development environment, and your distribution of choice is based on [Fedora](https://thenewstack.io/ultramarine-linux-fedora-made-easy-and-beautiful-for-everyone/), then you’ve probably run into [Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/).

Podman is the replacement for Docker that has gained considerable popularity over the past few years. If you’ve used Podman, you might be wondering if there’s a user-friendly GUI available for the container service.

There is.

Actually, there are several, one of which is called Pods. Pods is a Linux GUI that can be installed and used for free, on any distribution that supports both Podman and [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/). This handy app includes features like:

* Local and remote Podman instances.
* View images, containers, and pods.
* View information about images, containers, and pods.
* Inspect images, containers, and pods.
* View/search container logs.
* Monitor container and pod processes.
* Download images and build them with [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles").
* Create pools and containers.
* Control container lifecycle (start, stop, pause, etc.)
* Delete images, containers, and pods.
* Prune images.
* Rename containers.

That’s a fairly complete list of features, which means Pods might be an outstanding option for those either just learning the ins and outs of Podman and containers, or even those who know their way around the technology and are looking for a simple GUI.

I want to show you how to install, configure, and use Pods to ease your Podman management.

## What You’ll Need

The only things you’ll need for this are a Linux distribution that supports both Podman and Flatpak. If you’re using Fedora Desktop, both of those apps should be preinstalled, so there’s no need to worry about dependencies.

Let’s get to the installation.

## Installing Pods

Thanks to the universal package manager, Flatpak, Pods is very easy to install. Open a terminal window on your desktop and issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | flatpak install flathub com.github.marhkb.Pods |

Once that command is completed, there are a few configurations to take care of.

## Configuring Podman

Next, we must configure Podman so that it will allow Pods to make the connection via the Podman socket. To do that, issue the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | systemctl --user enable --now podman.socket |

At this point, Podman is running on your system. Give it a moment, and Pods should be able to successfully connect.

## Connecting Pods to Your Local Podman Service

Locate Pods in your desktop menu and launch it. In the resulting window (**Figure 1**), give the connection a name and then click Connect.

**Figure 1**

[![](https://cdn.thenewstack.io/media/2025/09/9136740c-pods1.jpg)](https://cdn.thenewstack.io/media/2025/09/9136740c-pods1.jpg)

Creating the local connection shouldn’t take but a few seconds.

Once the connection is made, you should be delivered to the Pods main window (**Figure 2**), where you can create your first container.

**Figure 2**

[![](https://cdn.thenewstack.io/media/2025/09/f55c8423-pods2.jpg)](https://cdn.thenewstack.io/media/2025/09/f55c8423-pods2.jpg)

The Pods GUI is very user-friendly.

## Creating Your First Container With Pods

Select Containers in the left sidebar and then click Create Container. You can then either accept the randomly-generated name or manually type one (**Figure 3**).

**Figure 3**

[![](https://cdn.thenewstack.io/media/2025/09/01e18463-pods3.jpg)](https://cdn.thenewstack.io/media/2025/09/01e18463-pods3.jpg)

Creating your first container with Pods.

Let’s deploy Ubuntu as a container. Click the Remote Image button (next to Select Image). Type “ubuntu” in the search field and then locate the official images for Ubuntu (**Figure 4**).

**Figure 4**

[![](https://cdn.thenewstack.io/media/2025/09/711971d9-pods4.jpg)](https://cdn.thenewstack.io/media/2025/09/711971d9-pods4.jpg)

Make sure to use the official Ubuntu image.

Click Next to pull the latest version of the images.

Now that you have the image ready, you can then configure the container as needed. For example, you can click the Integrations tab (the puzzle piece icon) and then add port mapping, volumes (**Figure 5**), environment variables, and labels.

**Figure 5**

[![](https://cdn.thenewstack.io/media/2025/09/d0762d08-pods5.jpg)](https://cdn.thenewstack.io/media/2025/09/d0762d08-pods5.jpg)

Adding a volume for the container.

When you’re done configuring, click Run to deploy the container.  If the container doesn’t automatically run, you can then click on the Container link in the sidebar and view your new container. Click the run button to launch it.

Let’s say you’ve deployed your Ubuntu container and want to access it via shell. On the container page, locate Terminal under Utilities (**Figure 7**).

**Figure 6**

[![](https://cdn.thenewstack.io/media/2025/09/1704b7b6-pods7.jpg)](https://cdn.thenewstack.io/media/2025/09/1704b7b6-pods7.jpg)

All of the utilities that are available to your container.

Click Terminal and you will be given immediate access to your running container’s shell (**Figure 8**).

**Figure 8**

[![](https://cdn.thenewstack.io/media/2025/09/33e046a1-pods8.jpg)](https://cdn.thenewstack.io/media/2025/09/33e046a1-pods8.jpg)

Our Ubuntu container’s CLI is ready to use.

You can now do whatever you need to develop your new Ubuntu-based container. You might update all of the software with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | apt-get update && apt-get upgrade -y |

You could then install Node.js with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | apt-get install node.js -y |

You are ready to go.

Pods is a great way to start learning Podman. If you are new to this container technology, know that you will fail a few times before you get the hang of it. Make sure to always check the logs of your containers to see what errors were thrown, so you can troubleshoot and figure out what happened.

Once you’ve started to get the hang of things, you might then venture to the command line and attempt to deploy and manage your containers, pods, and volumes from the CLI.

Enjoy that fresh GUI taste of Pods.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)