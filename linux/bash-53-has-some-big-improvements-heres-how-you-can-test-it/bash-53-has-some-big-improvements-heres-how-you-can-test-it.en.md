The GNU Foundation has announced that the latest public release of the Bash (version 5.3) command line interpreter is now available, after three long years since the previous stable release.

The new version of Bash includes some interesting new features that will appeal to all types of users. First, let’s talk about what’s new in Bash, and then I’ll show you how you can install the latest release (from source) on your Linux distribution of choice.

## What Is Bash?

First, let’s talk about Bash. What exactly is this piece o’ software?

Bash is the most commonly used shell for [Linux](https://thenewstack.io/learning-linux-start-here/).

But what is a shell?

In Linux, a shell serves as a command interpreter. [Without a shell](https://thenewstack.io/jeffrey-snover-remembers-the-fight-to-launch-powershell/), you wouldn’t be able to run commands in Linux. When you run a command in Linux, Bash understands those commands and then executes them successfully. Of course, in typical Linux fashion, there are several shells available to choose from. There’s bash, csh, Bourne, KornShell (ksh), T Shell (tcsh), Z Shell, Debian Almquist Shell (dash) and more.

Bash is the default on most [Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/) because it’s one of the easiest to use, is highly configurable, and includes all the features you would need in a shell. It should be noted that installing new shells for your distribution of choice isn’t always a straightforward experience, but it is very possible.

For example, if you wanted to install the fish shell on Ubuntu, you would first [run the command](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/):

```
sudo apt-get update &amp;&amp; sudo apt-get install fish -y
```

You would then start the fish shell with the command:

```
fish
```

You could also make fish the default shell with the Change Shell command:

```
sudo chsh -s /usr/bin/fish
```

Your default shell is now fish.

But we’re talking about Bash, so let’s get back to it.

## What’s New in Bash?

Version 5.3 adds some significant new features, the most important of which is a new form of command substitution that executes a command in the current shell context. According to the official changelog, “Two forms are implemented: one that reads the command substitution’s output and another that expects to find the result in the REPLY shell variable when the command substitution completes.”

The difference between the two is the addition of the pipe character, like so:

```
${ command; }
${ | command; }
```

The first captures the output of the command without forking it, and the second runs the command in the current shell and leaves the results in REPLY.

For those who are unfamiliar with REPLY, it is a default variable that stores the response from the read command when no variable is specified. It allows you to access the input provided by the user without needing to define a separate variable for it.

Then there’s the new GLOBSORT shell variable, which determines how the shell sorts the results of pathname completion.

Other additions include:

* The compgen builtin now has an option to place generated completions into a designated shell variable (vs. standard output).
* A new -E option for the read builtin that uses readline with the default bash completion (including programmable completion).
* A new `-p PATH’ option for the source builtin which forces the user of the PATH argument, as opposed to using $PATH to search for a file.

## How To Install Bash 5.3

As of this writing, Bash 5.3 is still in release candidate status, so it’ll be some time before it reaches the standard repositories. If, however, you’re anxious to test out the new features, you can install it from source. Here’s how.

The first step is to download the source. You can either download it using wget with:

```
wget http://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz
```

Unpack the file with:

```
tar -xvzf bash-5.3.tar.gz
```

Install the necessary dependencies (so you can install from source) with the command:

```
sudo apt-get install build-essential -y
```

Change into the bash folder with:

```
cd bash-5.3
```

Configure the build with the command:

```
./configure
```

Next, you have to compile the code with the command:

```
make
```

The above command can take some time to run, so allow it to complete.

Run the install with:

```
sudo make install
```

Make sure bash is your default shell with:

```
sudo chsh -s /usr/local/bin/bash
```

At this point, you should have Bash 5.3 installed. You can verify the installation with the command:

```
bash --version
```

You should see version 5.3.0 listed near the top.

In my opinion, I wouldn’t install 5.3 on a production machine yet because, well, you never know what could happen. If you’re really curious (or want to get up to speed with the new release), I would suggest either installing the latest public release on a spare (nonproduction) machine or in a virtual machine (VM). You certainly don’t want to break your shell on a production machine, as the consequences of that could be devastating (as in, you can no longer run commands … yikes!).

Enjoy that new Bash smell.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)