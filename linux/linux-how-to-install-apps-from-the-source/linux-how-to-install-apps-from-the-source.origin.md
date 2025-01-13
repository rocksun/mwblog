# Linux: How To Install Apps From the Source
![Featued image for: Linux: How To Install Apps From the Source](https://cdn.thenewstack.io/media/2025/01/49ac0687-olivie-strauss-49fb-ltae40-unsplash-1024x683.jpg)
When I first started using [Linux](https://thenewstack.io/learning-linux-start-here/), there was one way to install applications… from the original source code. Those days have long since passed, and now, there are several ways to install software:

- Source
- Default package manager
- Universal package manager
- AppImages
The most reliable and easiest methods for installing applications are the default package managers — such as APT for Debian — and universal package managers, such as FlatPak. Following that would be [AppImage](https://appimage.org/), which allows you to install Linux apps on any platform.

That leaves installing from the source.

Why is the oldest method of installing Linux applications at the bottom of the list? It’s not just the simplicity offered by package managers. In fact, there’s a very good reason why you should go with a package manager installation over source. When you install via a package manager, your system is aware of that application.

What does that even mean?

Let me give you a simple explanation.

Let’s say you install AppX using your default package manager. When you do this, the system is aware of the application, such that any time an upgrade is available for that app, it’ll be applied the next time you run an upgrade with the package manager.

Now, let’s say you install AppX via source. The next time you run an update with your package manager, AppX will not be updated. Why? Because the package manager isn’t aware of it, nor does it have the capability of upgrading an app installed via source.

What does this mean? Well, let’s stick with our example. You installed AppX via source in January, and you’ve regularly updated your system with the default package manager. In December, you check on AppX, only to discover that it is way out of date. Between January and December, the AppX developers have released several updates that included security patches.

Guess what? AppX on your system is now vulnerable. Had you installed AppX via the package manager, you wouldn’t have that problem.

Another issue (one that could be considered far more important) is that applications installed via package managers and housed in the standard repositories of your distribution have been vetted and should be devoid of malicious code (in theory — as nothing is ever guaranteed).

Finally, installing from a distribution’s package manager helps to resolve all dependency issues, so you don’t wind up getting caught in what is often referred to as “dependency hell,” where you have to install one dependency to solve another dependency, which resolves another dependency, which… you get the idea. I remember, back in the day, spending hours trying to resolve dependencies for source-based installations, and it’s [no laughing matter](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/).

That’s not to say that installing from a source should be avoided at all costs. There may be instances where you run across an application that is only installable via source. When that happens, you may not have any other choice. Should that arise, it’s crucial that you vet the software on your own to ensure there’s no malicious code contained within the source.

Okay, so you’ve decided to install an app via source and you’ve made sure the app is safe. How do you install it?

Let me serve as your guide on this journey.

## It Starts With Dependencies
Remember me mentioning dependency hell? This is probably the part of installing from a source that prevents most people from moving forward. The thing about installing from source is that you first have to meet all dependencies before you attempt to compile and install that app.

Often, within the source folder for an app, there’ll be a README file that should contain all the information about dependencies. Read that file and then start the process of locating, downloading, and installing the dependencies. Sometimes, those dependencies can be installed via your package manager. Other times, AppX might require a specific version of a dependency, which means you might have to install that from the source. If that dependency has its own dependencies, you’ll want to first try to install those with the default package manager before you dive deeper down the source-install rabbit hole.

But how do you actually do the installation?

Patience, we’re getting there.

## How Does This Work?
Okay, so you’ve downloaded the source for AppX (or you’ve cloned it from a [Git repository](https://thenewstack.io/development-git-clone-a-project/)). You know the app is safe and you’re ready to give this a go.

Here’s how it works. I’m going to stick with our fictional AppX app example.

Before you move forward, you’ll probably need to install a few pieces o’ the puzzle, otherwise, you won’t have the required software to build the app. If your distribution of choice is based on [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/), that can usually be done with the command:

1 |
sudo apt-get install build-essential -y |
The build-essential package installs things like libc, gcc, g++, make, dpkg-dev, etc.
On a Fedora-based distribution, that command would be:

1 |
sudo dnf install dh-autoreconf curl-devel expat-devel gettext-devel openssl-devel perl-devel zlib-devel gcc curl cmake -y |
With that out of the way, you’re ready to continue.
When you download the package, the first thing you’ll have to do is unpack the file. Most often, those files will be compressed and archived with a tool like tar. The easiest way to take care of this is to open your file manager, navigate to the file, right-click the file, and select Extract Here. This will create a new directory, which is usually named after the app.

At this point, you have a directory named AppX. Change into that directory with:

1 |
cd AppX |
Generally speaking, the process looks like this:
123 |
./compilemakesudo make install |
Before you run the *./compile* command, you might want to scan through the configure file found within the source directory, which might contain options you can configure before running the configure command. Also, in the README, there might be details of flags you can use for the configuration, which you should definitely know about.
Only upon a successful *./configure* run can you then move to the make command, which compiles the application. If the* ./configure* command fails, you can look through the output to find out why (most often, it’s a missing dependency). If make is successful, you can then run the make install command, which installs the executable binary to a directory in your $PATH, so the app can be run as expected.

Now that you have the app installed from the source, you’ll want to remember to regularly check to see if there’s a new update available. If so, you’ll have to go through the same process again, which is one reason why you should stick to installing apps from the default package managers.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)