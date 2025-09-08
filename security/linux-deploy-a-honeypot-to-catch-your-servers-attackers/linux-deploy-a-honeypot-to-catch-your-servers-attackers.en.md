Security is absolutely crucial at this point. No business (regardless of size) [can ignore security](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/) and assume [nothing will happen](https://thenewstack.io/xz-security-incident-the-importance-of-reputation-in-security/). It will, it’s only a matter of when.

And that’s if you’re constantly aware of what’s going on within your network. Imagine if you’re not paying attention.

The thing is, there are so many things to consider for security, and sometimes the obvious might go unchecked. For instance, telnet. Remember that? What was once a leader of remote connections became a back door for all sorts of nefarious goings on. Then came SSH, which is [exponentially more secure](https://thenewstack.io/linux-ssh-and-key-based-authentication/)… but not perfect.

You have to keep track of these things, always vigilant as to what is happening “under the hood” of your servers.

You can also lure would-be attackers to what’s called a honeypot.

Essentially, a honeypot is a decoy that lures attackers from your production servers, all the while saving the details on how those hackers attempted to gain entry. With the information saved by the honeypot, you can then take appropriate action to prevent attacks on your critical systems.

A honeypot is not a direct means of defense. Instead, a honeypot is a tool designed to help you detect and study unauthorized access attempts on your network.

Sounds hard, doesn’t it?

Thanks to [Linux](https://thenewstack.io/learning-linux-start-here/), it’s not nearly as challenging as you may think.

I’m going to walk you through the process of installing a honeypot on [Ubuntu Server](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/). The honeypot in question is [Cowrie](https://www.cowrie.org), which is an SSH/telnet-based honeypot that can help you see how attackers might be attempting to gain remote access to your systems.

Cowrie is open source and free to install/use. Cowrie is in active development and has been around for a while, so it’s a proven tool.

You can deploy Cowrie as a [Docker container](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), but I’m going to show you how to install it the old-fashioned way.

Exciting.

Are you ready?

## What You’ll Need

The only things you’ll need for this are a running instance of Ubuntu Server (preferably v 22.04 or newer) and a user with sudo privileges. Of course, you’ll also need a network connection, but that goes without saying.

Let’s make this happen.

## Install the Dependencies

The first step is to install the required dependencies. Log in to your Ubuntu Server instance and issue the following command:

```
sudo apt-get install git python3-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind virtualenv python3.12-venv -y
```

Once that’s installed, you’re ready to continue.

## Add the Cowrie User

We’re going to create a new user, named cowrie, without a password, which is done with the command:

```
sudo adduser --disabled-password cowrie
```

Answer the required questions (you can simply hit Enter to accept the default answers). With that taken care of, change to the cowrie user with the command:

```
sudo su - cowrie
```

## Clone the Cowrie Repository

We can now clone the Cowrie depository with the command:

```
git clone http://github.com/cowrie/cowrie
```

Once that’s taken care of, change to the new directory with:

```
cd cowrie
```

## Create a Virtual Environment

We now need to create a Python virtual environment with the command:

```
python3 -m venv cowrie-env
```

With that created, let’s run the installation steps, which can be accomplished with the following commands:

```
source cowrie-env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

## Create a Cowrie Configuration File

It’s time to create a Cowrie configuration file that will enable telnet. Create the file with the command (from within the cowrie directory):

```
nano etc/cowrie.conf
```

In that file, paste the following:

```
[telnet]
enabled = true
```

Save and close the file with Ctrl-x.

Start Cowrie with the command (run from within the Cowrie directory):

```
bin/cowrie start
```

## Redirect the Necessary Ports

We’ll now redirect both SSH and telnet ports so that SSH port 22 goes to 2222 and telnet port 23 goes to 2223. To do that, you’ll need to either exit from the Cowrie user and then make the changes with the following commands:

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223
```

## Verify It’s Working

On the honeypot, change back to the cowrie user (`sudo su - cowrie`) and let’s follow the Cowrie log, using the following command:

```
tail -f cowrie/var/log/cowrie/cowrie.log
```

Go to another machine on your network and attempt to either telnet or SSH into the honeypot server, and you’ll see entries appear in the log you’re following that indicate where the connection is coming from (and other bits of useful information). You can do the same thing by testing an SSH connection to the honeypot.

You’ll want to make sure to regularly check the Cowrie logs (as in regularly throughout the day) to see if anyone is attempting to access the server. If so, you’ll have an idea of where the connection is coming from and can mitigate it before anything disastrous happens.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)