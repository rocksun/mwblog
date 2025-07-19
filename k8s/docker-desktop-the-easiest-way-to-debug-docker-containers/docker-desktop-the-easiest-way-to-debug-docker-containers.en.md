If you’re a [container developer](https://thenewstack.io/containers/) and you use [Docker](https://www.docker.com/?utm_content=inline+mention), you might have experienced that when you have problems, finding answers to those problems can be a bit tricky. Sure, Docker has some command-line tools for this purpose, but they aren’t always the easiest to use. I’ve done a bit of debugging from the command line and never failed to find it more cumbersome than I prefer.

Consider this command:

```
docker container ls --all --format ‘{{ json . }}’ | python3 -m json.tool --json-lines
```

Do you really want to depend on such a complex command that you have to not only understand but memorize? Even worse, the output isn’t always exactly telling (unless you know exactly what you’re looking for).

What if I told you there was an easier way?

There is, and it comes by way of the [Docker Desktop app.](https://thenewstack.io/create-a-development-environment-in-docker-desktop/)

That’s right, to gain access to the most efficient and simple method of viewing Docker logs, you’ll want the [Docker Desktop application](https://docs.docker.com/desktop/). But the new log viewing feature isn’t built into the app by default, so there’s an extra step you have to take to get it working.

With the Logs Explorer extension, you can browse through Docker logs, filter the results, use advanced search capabilities, and even view new logs in real time.

It’s pretty nifty.

Imagine launching a container and being able to debug it as it’s launching. No more guesswork and running `docker ps -a` command over and over to see if your container is in a running state.

Fortunately, the Logs Explorer extension is available for Docker Desktop, so you don’t have to deal with confusing, complicated commands.

I know what you’re saying… If you’re going to learn the ins and outs of Docker, you need to know the commands. There is a lot of truth to that, and those who’ve been using Docker for a long time should know those commands. But what about those who are only just now starting their container journey?

Imagine how much easier it would be for a junior container developer to learn the basics of debugging and troubleshooting a container from within Docker Desktop. That, my friends, is worth the price of entry (the extension is free).

With all of that said, let’s see what there is to see.

## First, Install Docker Desktop

I’m going to demonstrate this on [macOS](https://thenewstack.io/how-to-set-up-macos-as-a-development-machine/) because installing Docker Desktop on Linux is currently in a laughably bad state.

To install Docker Desktop (which also installs the required Docker runtime engine), download the binary installer for either Apple Silicon or Intel-based systems from the official [Docker Desktop download page](https://docs.docker.com/desktop/setup/install/mac-install/). Once the file has downloaded, double-click on it, and then drag the Docker Desktop icon to the folder icon. This should only take seconds to complete.

After the installation, you can eject the installer, and you’re good to go.

When you open Docker Desktop for the first time, you can either log in, create an account, or skip it. If you’re just getting involved with this, go ahead and skip that part because you can always go back and create an account later.

## Installing the Extension

The Logs Explorer extension is very easy to install. All you have to do is expand the Extensions menu entry in the sidebar and then click Manage. In the Manage section, click the Browse tab and then type logs explorer in the search field.

Once the official Logs Explorer extension appears, click the associated Install button (Figure 1). You will be prompted for your macOS user password before the extension installation can complete.

[![screenshot](https://cdn.thenewstack.io/media/2025/07/1344d1e4-le1.jpg)](https://cdn.thenewstack.io/media/2025/07/1344d1e4-le1.jpg) Figure 1: Installing the Logs Explorer extension is much easier than you think.

With the extension installed, you’ll notice the new Logs Explorer entry in the sidebar.

Let’s see how it works.

## Hello, World!

Yup, we’re going to use the tried and true Hello, World! app to demonstrate the newly installed extension.

Click the Docker Hub entry in the sidebar and type hello world in the search field. Hit Enter on your keyboard, locate the Hello World entry, and click the associated downward-pointing arrow to pull the image.

After the image is pulled, click on Images in the sidebar, select Hello World, and then click Run (Figure 2).

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/ce728a99-le2.jpg)](https://cdn.thenewstack.io/media/2025/07/ce728a99-le2.jpg) Figure 2: You’re about to run your first container with Docker Desktop.

As soon as you hit Run, click the Logs Explorer link in the sidebar, and you’ll see the log output in real time (Figure 3).

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/59d29da3-le3.jpg)](https://cdn.thenewstack.io/media/2025/07/59d29da3-le3.jpg) Figure 3: Now, this is helpful.

Obviously, the Hello World app isn’t going to produce a lot of usable output, because it’s such a small container. Even so, you get an idea of what the Logs Explorer extension has to offer. If this were a more complicated container, you would see considerably more output (as well as more useful output).

You can also filter the output. Say you’re debugging a massive container deployment that includes [NGINX,](https://thenewstack.io/nginx-one-console-not-for-experts-only/) and you want to view only the output that pertains to NGINX. Type nginx in the search field and you’ll only see those entries that include NGINX.

This extension should be considered a must for those who are new to developing containers with Docker. Once you get the hang of interpreting the logs with the Logs Explorer extension, you can then migrate to the command line with enough confidence to get you through.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)