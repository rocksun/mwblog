# An Introduction To Developing From the Command Line in Linux
![Featued image for: An Introduction To Developing From the Command Line in Linux](https://cdn.thenewstack.io/media/2024/11/112ef20c-gabriel-heinzer-xbevm6oj1fs-unsplash-1024x768.jpg)
When you think of software development, you probably assume all types of applications and services must be used to get the job done. You’ll need a powerful [IDE](https://thenewstack.io/do-ides-make-you-stupid/), a [GUI](https://thenewstack.io/tauri-mixing-javascript-with-rust-for-gui-desktop-apps/) for version control, and a host of other tools.

What if I told you that wasn’t the case?

Back when I briefly studied [C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/), the professor informed us we’d have to purchase an IDE by [Microsoft](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/). Even though the student price for the software wasn’t terribly expensive, I didn’t have access to a Windows computer. Everything I did was within [Linux](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/), and I wasn’t about to change that.

What was I to do?

Like any good Linux user, I figured it out.

To my surprise, it wasn’t all that big of a challenge. I had to install a few pieces of software (such as the GNU C/C++ compiler), but once that was taken care of, I was set. I started working on my first assignment, and all went well.

In fact, in comparison to my fellow students, my process was considerably more efficient than theirs. Some complained that their computers weren’t powerful enough to run the IDE, while others had to overcome the learning curve involved with using such a powerful tool.

For me, I wrote my code using the nano text editor, compiled it with gcc, and ran the app. It was incredibly easy.

Here’s an example using [Hello, World](https://thenewstack.io/beyond-hello-world-startup-gamifies-development-skills/) in C.

The code is:

Save the file as *demo.c.*

Compile the application with the command:

1 |
cc demo.c -o demo |
Run the app with:
1 |
./demo |
The output will be:
1 |
Hello, New Stack! |
It really doesn’t get any easier than that.
But let’s take a step back and discuss what’s required.

## What You Need To Develop on Linux
Obviously, you need a running instance of Linux. This can be any distribution because the tools will be available, no matter what flavor of Linux you use, from standard repositories. There are, however, exceptions to this. For example, the version of Java found in most standard repositories will be out of date, which means you’ll need to add a repository that includes the latest releases.

What about other languages? Let’s take a look.

[Python](https://thenewstack.io/what-is-python/)– pre-installed on most Linux distributions.- C/C++ – can be installed from the standard repositories. On Fedora-based distributions, it can be added with the command
*sudo dnf groupinstall ‘Development Tools’*and on Ubuntu-based tools, that command is*sudo apt-get install build-essential -y.* - Go – The Go binary can be downloaded from
[https://go.dev](https://go.dev). Once downloaded, unpack the archive with a command like this: *sudo tar -C /usr/local/ -xzf goXXX.linux-amd64.tar.gz*(where XXX is the release number). You then must set the path for Go by adding the following line to the bottom of your ~/.profile file:*export PATH=$PATH:/usr/local/go/bin.*
- Java – How you install Java will depend on the version you need, but you can install the default package from the standard repositories with one of these commands: Ubuntu –
*sudo apt-get install default-jdk -y*or Fedora –*sudo dnf install <openjdk-package-name>*. You can locate the package you want to install with*dnf search openjdk*. - Node.js – On Ubuntu, install Node.js with
*sudo apt-get install nodejs -y*and on Fedora, the command is:*sudo :dnf install nodejs -y*
As you can see, installing the actual [programming languages](https://thenewstack.io/programming-languages/) is quite easy on Linux.

You might also want to install a debugger for your language of choice. For example, you can use the *gdb debugger* for C, C++, Ada, and Fortran. If you need a command line debugger, do a quick search, and you’ll quickly find out if your language of choice has a command line debugger and how to install it.

What’s next?

## Choose Your Editor
I’m just going to say this: Nano has been my editor of choice for a very long time. I know it’s not the popular choice, but I find it never gets in my way of doing what needs to be done.

That being said, most serious developers who use Linux tend to prefer the old-school (and supremely powerful) *vi* or *emacs*. The thing about both of those editors is they each have a learning curve. Let me explain the workflow for* vi*.

- Open a terminal window.
- Start
*vi*with the command*vi*. - Switch out of command mode into insert mode by pressing the i key on your keyboard.
- Type your code.
- Save and quit by first pressing the Escape key on your keyboard and then type
*:wq*(for write/quit).
That’s just the very basic usage, and you have to go through that process every time you use *vi.*

Here’s the same process with nano:

- Open a terminal window.
- Start nano with the command
*nano*. - Type your code.
- Save and quit with the Ctrl-X key combination.
With nano, there are few steps and fewer to remember. On the other hand, there are far fewer features. Because of this, I always recommend that new users start with nano, and once they feel as if they need more power and/or features, it’s time to migrate to *vi.*

## Git ‘Er Done
At some point, you’ll need a version control system, especially if you work with a team. Fortunately, you can interact with Git from the command line, so there’s no need for a GUI there either.

Git can be installed from the standard repositories, such as with the command:

1 |
sudo apt-get install git -y |
Once you have Git installed, the basic command line workflow goes something like this:
- Create a new repository – mkdir ~/new-project
- Initialize the repository –
*git init .* - Add files to the repository – you can either copy them or create them from scratch.
- Connect the local repository with the GitHub repository with the command:
*git remote add origin URL*(where URL is the address of the GitHub repository) - Pull the content of the remote repository with:
*git pull origin master* - Create a README file and then add it with
*git add README* - Make your first commit with
*git commit -m “Added new information to README file”* - Push to send the changes to the remote repository with
*git push*
Do note that you must create an access token from within your GitHub profile. You’ll also want to configure the global options with the commands:

Where NAME is your real name and EMAIL is the email address associated with your GitHub account.

Developing from the Linux command line isn’t nearly as challenging as you might think. Can you work this way at scale? Maybe.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)