# Podman 5 Arrives with Multiplatform Images, VM Support
![Featued image for: Podman 5 Arrives with Multiplatform Images, VM Support](https://cdn.thenewstack.io/media/2024/04/38bf6368-podman-logo-1024x683.png)
If you’ve been using Podman for your container deployments or development, you’re in for a treat.
[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) recently launched version five of the [Podman container management system](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/), which has completely reworked the code for Podman’s virtual machine management tool ( *podman-machine*).
“Podman machine includes a set of subcommands that manage Podman’s virtual machine, which is necessary for users to be able to run Podman on MacOS or Windows,” the
[official release announcement](https://www.redhat.com/en/blog/podman-50-unveiled).
With
[Podman 5.0](https://github.com/containers/podman/releases/tag/v5.0.0), there are a number of new features and improvements, including the new *podman machine reset *option which simplifies the process of resetting Podman machines; a new subscription manager and *qemu-user-static* features for Podman machines; faster boot times for Podman machines; *podman farm build* for quickly building multiplatform images on remote machines; podman manifest, which adds support for [Open Container Initiative](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) artifacts; and a change to the rootless networking tool for a more performant network stack.
All of the changes made to Podman culminate in a much more flexible and responsive container runtime engine.
The thing is, the ability to use Podman 5 at the moment is fairly limited. As far as I can tell, the only way to get/test Podman 5 as of this week is via
[Fedora Linux](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/), as the only version available within other distributions’ repositories is 4.x. And with Fedora, the only way to install Podman 5 is via the development version.
## How to Install Podman 5 on Fedora
First off, I wouldn’t recommend installing the
[development version of Podman on a production](https://thenewstack.io/risk-aware-vs-risk-averse-product-development/) machine. Use this on a test environment only. I also wouldn’t recommend doing this on a virtual machine, as Podman will have trouble accessing the KVM system.
The other issue is that you can’t use any version of Fedora prior to Fedora 40 beta 1. If you’re using a release of Fedora that is 39 or earlier, this will not work. So, the first thing you’ll need to do is
[download an ISO of Fedora 40 beta](https://fedoraproject.org/workstation/download?beta). Once you’ve done that, create a bootable flash drive, boot into Fedora 40 beta 1, and install the OS.
After Fedora 40 beta 1 is installed, you can then install the development version of Podman 5.0 with the command:
|
1
|
sudo dnf update --refresh --enablerepo=updates-testing podman
Once that’s done, you can verify the installation with:
|
1
|
podman --version
You should see something like this in the output:
|
1
|
podman version 5.0.1
## Using Podman 5
One of the best features of Podman 5.0 is the ability to quickly reset machine environments. This command stops all running machines and removes them. As well,
[configuration data files](https://thenewstack.io/circleci-offers-a-private-option-for-orb-reusable-configuration-files/) (such as machine disk images and previously pulled cached images) are also removed. The command only has one option, which is –force (or just -f), which resets everything without confirmation.
Let’s say, for example, you’ve created a few machines like so:
- podman machine init dev1
- podman machine init dev2
- podman machine init web1
- podman machine init web2
You then started them with the commands:
|
1
|
podman machine start dev1
|
1
|
podman machine start dev2
|
1
|
podman machine start web1
|
1
|
podman machine start web2
Next, you accessed each machine with the command:
|
1
|
podman machine ssh NAME
Where NAME would be one of
*dev1*, *dev2*, *web1*, or *web2*.
Once you’ve accessed the machine, you
[worked your development](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) magic, ran some tests, or whatever it was you needed to do with the machines. After you’ve completed working with those machines, if you want to get rid of them with Podman 4.x, you would have had to individually stop them and then remove them with the commands:
|
1
|
podman machine stop NAME
|
1
|
podman machine rm NAME
Where NAME would be one of dev1, dev2, web1, or web2.
With Podman 5.0, that can all be done with the command:
|
1
|
podman machine reset
All of your machines will be stopped and deleted (along with associated files and data).
The new version also includes the podman farm build command, which builds images on farm nodes, then bundles them into a manifest list. I’ve not tested this feature yet, but according to the man page (read it with man podman-farm):
Podman manages the farms by writing and reading the
*podman-connections.json* file located under *$XDG_CONFIG_HOME/containers* or if the env is not set it defaults to *$HOME/.config/containers.* Or the *PODMAN_CONNECTIONS_CONF* environment variable can be set to a full file path which podman will use instead. This file is managed by the podman commands and should never be edited by users directly. To manually configure the farms use the [farm] section in containers.conf.
For those who don’t use Fedora 40, I have found no indication as to when it will be available for different distributions. If I had to guess, Podman 5.0 will hit Red Hat Enterprise Linux this year with the 9.4 release. Should that happen, it’ll most likely find its way to the likes of
[Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/), [AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/), and [Oracle Linux ](https://developer.oracle.com/?utm_content=inline+mention)soon after.
It’s also important that, before updating to Podman 5.0, users understand that Podman 4 machines will not be compatible with Podman 5.0. Because of that, you should remove all Podman 4 machines before upgrading to 5.0. After removing those machines and upgrading to Podman 5.0, it’s also recommended that you run the podman machine reset command before deploying any new machines.
To find out more about Podman 5.0, check out the
[new feature summary post on the Podman site](https://blog.podman.io/2024/03/podman-5-0-has-been-released/). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)