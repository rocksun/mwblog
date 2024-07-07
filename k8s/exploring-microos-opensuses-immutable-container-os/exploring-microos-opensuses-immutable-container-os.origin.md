# Exploring MicroOS, OpenSUSE’s Immutable Container OS
![Featued image for: Exploring MicroOS, OpenSUSE’s Immutable Container OS](https://cdn.thenewstack.io/media/2024/07/a0489be3-opensuse-microos-1024x683.png)
The thing about [containerization](https://thenewstack.io/containers/) is that less is always more. When deploying containerized workloads, you need to think about your operating system a bit differently than you would with a traditional desktop or server. What you need is an operating system designed specifically for such workloads. You need atomic updates, rolling releases, and security geared specifically for containers.

That’s where [openSUSE MicroOS](https://microos.opensuse.org/) comes into play. This [container-centric](https://thenewstack.io/canonical-offers-lts-distroless-containerized-apps-for-k8s/) Linux distribution is predictable, immutable, scalable, uses transactional/secure updates, and all applications are installed in containers.

You might currently be using a standard distribution (such as[ Ubuntu Server](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/), [Debian](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/), [AlmaLinux](https://thenewstack.io/linux-and-cloud-native-security-almalinux/), or [Red Hat Enterprise Linux](https://www.openshift.com/try?utm_content=inline+mention)) for your container deployments. The problem with those operating systems is that things can be changed. Some unwanted ne’re do well could access a running container, hop onto the operating system, and inject malicious code.

With an immutable OS, that’s exponentially more challenging because no changes can be made on disk.

You probably want that and openSUSE MicroOS delivers.

I want to show you how easy openSUSE MicroOS is to install and even get [Cockpit](https://cockpit-project.org/) installed, so you have a web-based GUI to manage the platform (because it’s just easier for some than the CLI).

Are you ready for this?

Let’s do it.

## What You’ll Need
To make this work, you’ll need the ISO image of openSUSE MicroOS and a virtual machine platform. I’ll demonstrate the process using VirtualBox but you can use your VM technology of choice.

## Getting and Installing openSUSE MicroOS
The first thing to be done is to download the openSUSE MicroOS ISO image, which can be done from the [official site](https://get.opensuse.org/microos/). Make sure to download the file that’s correct for your architecture (it’s available for Intell/AMD, PowerPC, little endian, and aarch64).

Once you’ve saved the ISO image to your local drive, create a new virtual machine as you normally would in your VM platform of choice. In the first interactive screen (Figure 1), select Installation with your keyboard up/down keys and hit Enter.

-
Figure 1: This is the first screen in the MicroOS installation wizard.

You’ll then have to select your language and keyboard layout and accept the license agreement on the same page. By default, the language/keyboard is configured to English, so you can click Next to continue (Figure 2).

![License agreement](https://cdn.thenewstack.io/media/2024/07/65e54e4e-microos2.jpg)
Figure 2: License agreement

You’ll then be presented with a system role selection. For container deployments, select MicroOS Container Host and click Next (Figure 3). This installs MicroOS such that it’s optimized for containerized workloads which includes the [Podman runtime](https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/).

-
Figure 3: Selecting your system role during installation.

Make your selection and click Next.

In the NTP Servers window, keep the default and click Next.

You’ll then be asked to create a password for the root user. Type and confirm your password and click Next (Figure 4).

-
Figure 4: Creating a password for the root user.

You can also import a public SSH key but that key has to be copied from the MicroOS file system. To do that, you’d need to create a shared folder between your virtual machine and desktop. I’ll show you how to upload the SSH key later.

Finally, click Install to begin the process. When the installation completes, reboot and log in. This is a GUI-less OS, so you’ll find yourself at a terminal prompt.

## Installing Cockpit
For those who’d prefer to have a web-based GUI to manage MicroOS, here’s what you need to do. As the root user, issue the command:

1 |
transactional-update pkg install patterns-microos-cockpit cockpit-ws cockpit-tukit |
This will install Cockpit. Before you can use the app, you’ll need to reboot the machine with the command:
1 |
reboot |
You then must enable it with the command:
1 |
systemctl enable --now cockpit.socket |
Finally, allow Cockpit through the firewall with:
1 |
firewall-cmd --permanent --zone=public --add-service=cockpit |
Reload the firewall with:
1 |
firewall-cmd --reload |
Once you’ve taken care of that, locate the IP address of your MicroOS server with the command:
1 |
ip a |
You can then access Cockpit by pointing a browser to https://SERVER:9090 (where SERVER is the IP address of the MicroOS server). At the login screen, use root and the password you created during installation.
## Adding a New User
The first thing you’ll notice when you attempt to login to Cockpit is the root user isn’t allowed to do so. To get around this, you need to create a new user. Back at the command line, do this:

1 |
useradd -m USERNAME |
Where USERNAME is the user you want to add.
Next, give the user a strong/unique password with:

1 |
passwd USERNAME |
Where USERNAME is the new user you just added.
Once you’ve added the new user, you can then use those credentials to log into Cockpit. When you do, you’ll want to give that user administrative access by clicking Administrative Access near the top of the window.

Once you’ve taken care of that, you can go into Accounts (within Cockpit) and then add your SSH public key. Here’s how:

On your desktop (from where you’d SSH into MicroOS) issue the command (assuming you saved the key in the default location):

1 |
cat ~/.ssh/id_rsa.pub |
Copy the contents of that key and then go back to Cockpit > Accounts > Authorized public SSH keys and click Add Key. Paste the SSH key into the resulting window and click Add. Once you’ve done that, you should be able to SSH (with your SSH key) into MicroOS via that new user.
Now that you’ve taken care of this, you can either use Cockpit or the command line to work with your Podman containers.

And that is all there is to get openSUSE MicroOS up and running and ready for your first containerized deployment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)