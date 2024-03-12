# Simplify Linux and Docker Command Lines with Bash Completion
![Featued image for: Simplify Linux and Docker Command Lines with Bash Completion](https://cdn.thenewstack.io/media/2024/03/e3ec3d33-wings-1024x643.png)
Do you have trouble remembering all of the
[Docker commands](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)? Or maybe you can’t remember all of the commands available to systemctl (of which there are a lot). If you’re [new to Linux](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/), the [vast array of commands](https://thenewstack.io/linux-pass-a-text-based-password-manager/) can be quite daunting.
I’ve been using Linux for nearly 30 years and I still have trouble remembering them all. When I first started down the open source path, remembering a single command was challenging. Now I use all sorts of commands, on both desktops and servers.
Then you add applications like Docker into the mix, which has a number of its own commands to remember, and the learning process becomes even more complex.
Remember the mention of systemctl above? The commands available include
*add-requires*, *is-enabled*, *reload*, *add-wants*, *is-failed*, *reload-or-restart*, *bind*, *isolate*, *rescue*, *cancel*, *is-system-running*, *reset-failed*, *cat*, *kexec*, *restart*, *condreload*, *kill*, *revert* … and that’s not even a quarter of the commands that systemctl has up its sleeve.
And then there’s Docker. On Linux, if I type “do” and use tab completion (by hitting the Tab button on my keyboard), I might see the following:
*do*, *dockerd-rootless-setuptool.sh*, *docker*, *dockerd-rootless.sh*, *docker-buildx*, *docker-init*, *docker-compose*, *docker-proxy*, *docker-credential-ecr-login*, *domainname*, *docker-credential-none*, *done*, *docker-credential-pass*, *do-release-upgrade*, *docker-credential-secretservice*, *dosfsck*, *dockerd* and *dosfslabel*.
That’s not much of a help, because although it might key us into the fact that there’s more than just one command with Docker, it not only includes all commands that start with do, it doesn’t help us to know that Docker includes commands like
*ps*, *images*, *import*, *info*, *inspect*, *pull*, *push*, *plugin*, * pause *… you get the idea.
Perhaps you know that the Docker subcommand you want to use starts with a “p” but that’s all you can remember. Of course, you could comb through the Docker manual page (with the command “man docker”). Not that there’s anything wrong with looking through man pages — in fact, I highly recommend it. You’re sure to learn something in the process.
But when you need to recall a subcommand fast, what do you do? Well, there’s a tiny application that can help you out with that. The app in question is called
[Bash Completion](https://github.com/scop/bash-completion) and it’s available from the standard repositories of [most Linux distributions](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/).
Now, the Bash Completion application works out of the box for
[Linux commands](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/), so all you have to do is install it and you’re good to go. However, for Docker, there’s an extra step you must take to make it work.
Before we get to that, let’s get this application installed.
## Installing Bash Completion
Some distributions have this application installed by default. If you aren’t certain, you can run the installation command and your package manager will let you know whether it’s already available.
For
[Debian/Ubuntu-based distributions](https://thenewstack.io/what-is-ubuntu-pro-and-how-can-you-use-it/), the command for installation is:
|
1
|
sudo apt-get install bash-completion -y
For Fedora/
[Red Hat](https://www.openshift.com/try?utm_content=inline-mention) Enterprise Linux-based distributions, the command is:
|
1
|
sudo dnf install bash-completion -y
Once you have the application installed, you can test it by typing the following:
|
1
|
systemctl s
Hit your keyboard Tab key twice and you’ll see all of the subcommands available to systemctl.
## Adding Docker Support
To add Docker support to bash-completion, you have to download what’s called the Docker complete file and copy it to the
*/etc/bash_completion* directory. You can take care of both of those actions with the command:
|
1
|
sudo curl https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/bash/docker -o /etc/bash_completion.d/docker.sh
On some distributions, you might be presented with a permissions error. If that’s the case you’ll need to first issue the command:
|
1
|
sudo -s
Once that’s taken care of, rerun the curl command. It should go off without a hitch.
With this done, you can then test bash-completion with Docker. For example, type:
|
1
|
docker i
Hit Tab twice and you’ll see output like this:
|
1
|
image images import info inspect
Type “docker p” and hit Tab twice to reveal output like the following:
|
1
|
pause plugin port ps pull push
The output should jog your memory so you can run the command you need.
## The Caveat
Bash Completion is a handy tool that will happily remind you of the subcommands available to the command you need to use. What it can’t do, however, is help you with the various options associated with the subcommands.
For instance, if you type “docker ps” and hit Tab twice, it’s not going to list out the options, which include
*-a* (or *–all*), *-f* (or *–filter*), *–format*, *-n* (or *–last*), *-l* (or *–latest*), *–no-trunc*, *-q* (or *–quiet*), *-s* (or *–size*). If you’re unsure of the available options, the tried-and-true man page is your friend.
For instance, you could type:
*man docker ps*
Hit Enter and you’ll see all of the options available to that command. The same holds true for most Docker subcommands. Type “man docker” followed by the subcommand you want to learn about, and then hit Enter. A world of knowledge will appear before your eyes.
That’s all there is to simplifying the Linux and the Docker command line. With the seemingly never-ending amount of commands available to Linux, any help you can get should be happily accepted.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)