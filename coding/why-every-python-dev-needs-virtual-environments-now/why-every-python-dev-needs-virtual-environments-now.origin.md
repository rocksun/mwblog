# Why Every Python Dev Needs Virtual Environments Now
![Featued image for: Why Every Python Dev Needs Virtual Environments Now](https://cdn.thenewstack.io/media/2025/01/983492c7-unsplash-community-hdxlqjahsmu-unsplash-1024x693.jpg)
When developing with [Python](https://thenewstack.io/python/), chances are pretty good that you’ll need to install various libraries, dependencies and apps to get your project started. The good news is that (in most cases) those installations are pretty straightforward (thanks to [pip](https://thenewstack.io/how-to-use-python-pip-and-why-you-need-to/) and other tools).

Problems can arise, however, if you simply install all of those project requirements on your system. It’s like installing any given application, hoping it won’t cause problems with other applications, your OS or your data. In most cases, it’s safe, but there’s always that one instance where things can quickly go awry.

You do not want this. After all, your system is where you do your work, and your work is your livelihood. With that in mind, why would you want to risk even the slightest issue that could set you and your project back? This is especially so when you’re on a tight deadline and have to deliver on time or risk losing a client (or your job).

To that end, what do you do?

You use virtual environments.

## What Are Virtual Environments?
A virtual environment is an isolated sandbox that allows you to install everything you need for a project without affecting things globally. Within a virtual environment, you can install all of the libraries and dependencies you need without touching the global Python installation.

Think of Python Virtual Environments like a [virtual machine](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/). If you’ve ever used a tool like VirtualBox, you know that host and guest do not affect one another, and anything you do to a guest OS will have no bearing on the host OS. You could effectively install a Linux guest OS, log in, run the *sudo rm -rf /* command (don’t do that) and it would destroy the guest OS but not touch the host.

Python Virtual Environments work in a similar fashion and offer the following benefits:

- They allow you to work on multiple projects with different dependencies at the same time.
- They allow you to create portable projects.
- There’s no risk of version conflicts.
- They avoid the need for global package installation.
- They make it easier for testing.
- They make clean up easier.
- They simplify collaboration.
- They are more easily reproducible.
- They offer dependency isolation.
- They create a much cleaner and organized workspace.
Ask any seasoned [Python developer](https://thenewstack.io/why-should-python-developers-care-about-testing/) and they’ll tell you that every project you create should be done in a virtual environment.

The good news is that Python contains everything you need to create and use a virtual environment. Even better, creating a virtual environment is very easy.

Let me show you how to create, activate, deactivate and delete a Python virtual environment.

## What You’ll Need
The only thing you’ll need for this is to install Python on your OS of choice. I’ll demonstrate this on [Pop!_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) with Python version 3.10.12, but the process is the same, regardless of the operating system. Do note that as long as you’re using Python version 3.4 and up, it has everything you need to do this. If you’re using a version of Python older than 3.4, I suggest you upgrade; otherwise, you’ll need to install virtualenv using Pip (*pip install virtualenv*).

## Creating a Virtual Environment
The first thing you want to do is create a new virtual environment.

Log in to your OS and open a terminal window. Once you have access to the CLI, create a directory to house your Python projects like so:

1 |
mkdir PYTHON |
Change into that parent directory with the command:
1 |
cd PYTHON |
Let’s say you’re about to embark on developing a project named ProjectX. Create a new virtual environment for that project with the command:
1 |
python -m venv ProjectX |
If you receive an error, you might have to install the required venv command for your version of Python, like so:
1 |
sudo apt-get instll python3.10-venv |
If you’re using a version of Python older than 3.4, the command would be:
1 |
virtualenv ProjectX |
You should now find a new directory called ProjectX. Inside that directory, you’ll find the following sub-directories:
- bin
- include
- lib
- lib64
You should also find a file named pyvenv.cfg.

Change into the ProjectX directory with the command:

1 |
cd ProjectX |
Next, you need to activate the project with the command:
1 |
source bin/activate |
You should see your prompt change. It will now look something like this:
1 |
(ProjectX) hostname -> |
If you’re on a Windows environment, the activation will be one of the following:
- For cmd.exe – venv\Scripts\activate.bat
- For PowerShell – venv\Scripts\Activate.ps1
At this point, you can install all of the necessary libraries and dependencies required for the project without affecting your system. Once you have your dependencies installed, you can start working on your project.

## Deactivating a Project
When you’re finished working on a project, it’s good practice to deactivate it. This will leave the virtual environment intact but prevent anything from happening to it.

To deactivate a virtual environment, type the following command within the project directory:

1 |
deactivate |
Any time you need, you can change back into that directory and run the activate command as you did earlier.
## Deleting a Virtual Environment
If you need to delete that virtual environment, all you have to do is deactivate it and then delete the directory with the following commands:
If you’re working on a Windows environment, you’ll need to change the last two commands to use the Windows equivalent.

And that, my friends, is all there is to working with a Python virtual environment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)