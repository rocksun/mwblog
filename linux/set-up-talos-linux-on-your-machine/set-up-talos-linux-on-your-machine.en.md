Sidero Labs’ [Talos Linux](https://thenewstack.io/open-source-talos-linux-bringing-simplicity-to-kubernetes/) is [not an orthodox Linux distro](https://thenewstack.io/no-ssh-what-is-talos-this-linux-distro-for-kubernetes/). It’s designed to offer a refreshing alternative to the high cost and complexity of managing disparate Kubernetes and other deployments.

It can be argued that it does the opposite of [Red Hat’s](https://www.openshift.com/try?utm_content=inline+mention)  Linux OpenShift, SUSE Rancher, and other Kubernetes distributions. In all of these, Kubernetes is installed and runs on top of a general-purpose operating system.

[Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention), with its open source Talos Linux, argues that this entire foundation is not only unnecessary but a liability, especially for private cloud and edge use cases.

In this tutorial, we show how to install Talos Linux locally on your Mac. It can be assumed most of these commands are applicable when using a Linux OS.

## Getting Started

First, from the command line, install Homebrew in order to install Talos Linux and other dependencies when they are required. If you have Homebrew already installed, updates will be installed automatically as Talos Linux is installed, as  you’ll see in the screenshot below during Talos Linux’s  installation process. This command is used to download and install Homebrew in case it is not installed on your Mac:

[![](https://cdn.thenewstack.io/media/2025/11/044ebf72-screenshot-2025-11-05-at-9.13.18%E2%80%AFpm-1024x22.png)](https://cdn.thenewstack.io/media/2025/11/044ebf72-screenshot-2025-11-05-at-9.13.18%E2%80%AFpm-1024x22.png)

Once Homebrew is installed, use it to install Talos Linux:

[![](https://cdn.thenewstack.io/media/2025/11/258bb7d0-screenshot-2025-11-04-at-12.44.46%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/258bb7d0-screenshot-2025-11-04-at-12.44.46%E2%80%AFpm.png)

Start the socket\_vmnet service, in order to connect the VMs:

[![](https://cdn.thenewstack.io/media/2025/11/3e9ace3e-screenshot-2025-11-05-at-9.19.02%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/3e9ace3e-screenshot-2025-11-05-at-9.19.02%E2%80%AFpm.png)

You can now initialize the bootstrap Kubernetes control plane for your Talos cluster:

[![](https://cdn.thenewstack.io/media/2025/11/a587c75f-screenshot-2025-11-05-at-9.49.18%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/a587c75f-screenshot-2025-11-05-at-9.49.18%E2%80%AFpm.png)

Homebrew will begin installing everything for you. A good time to make some real coffee with H2O and all that good stuff, but the process should not take but a few minutes:

[![](https://cdn.thenewstack.io/media/2025/11/8c2c2531-screenshot-2025-11-04-at-12.46.52%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/8c2c2531-screenshot-2025-11-04-at-12.46.52%E2%80%AFpm.png)

## Install Talos Cluster

Now you are ready to install your Talos cluster:

[![](https://cdn.thenewstack.io/media/2025/11/4f12fa79-screenshot-2025-11-04-at-12.49.32%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/4f12fa79-screenshot-2025-11-04-at-12.49.32%E2%80%AFpm.png)

Configure kubeconfig so that  talosctl merge the new cluster’s configuration into the default kubeconfig file):

[![](https://cdn.thenewstack.io/media/2025/11/6778e4d9-screenshot-2025-11-05-at-9.42.00%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/6778e4d9-screenshot-2025-11-05-at-9.42.00%E2%80%AFpm.png)

Now make sure your cluster is running:

[![](https://cdn.thenewstack.io/media/2025/11/d9f01f9f-screenshot-2025-11-05-at-9.47.34%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/d9f01f9f-screenshot-2025-11-05-at-9.47.34%E2%80%AFpm.png)

Open [Docker](https://www.docker.com/?utm_content=inline+mention) and check that it’s running:

[![](https://cdn.thenewstack.io/media/2025/11/0b0ac949-screenshot-2025-11-04-at-12.53.24%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/0b0ac949-screenshot-2025-11-04-at-12.53.24%E2%80%AFpm.png)

This is what you should see:

[![](https://cdn.thenewstack.io/media/2025/11/c2a681c0-screenshot-2025-11-04-at-1.03.51%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/c2a681c0-screenshot-2025-11-04-at-1.03.51%E2%80%AFpm.png)

You run these commands, and Talos Linux manages your cluster. After running the commands above, Talos Linux should be ready to use to manage your Kubernetes cluster or clusters.

The installation is vastly simpler compared to many other Kubernetes management platforms. It is not unfun to set up and play around with, either.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)