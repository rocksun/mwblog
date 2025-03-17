# NVM: Manage Multiple Versions of Node.js on a Single System
![Featued image for: NVM: Manage Multiple Versions of Node.js on a Single System](https://cdn.thenewstack.io/media/2023/09/33e2dc43-umbrella-3380192_1280-1024x768.jpg)
## Overview
The article introduces NVM (Node Version Manager), a tool that enables developers to manage multiple versions of Node.js on a single system. This is particularly useful for projects that require different versions of Node.js, making it easy to switch between them as needed.

### Key Features and Benefits:
- Installable on various Linux distributions, macOS, and Windows (via Windows Subsystem for Linux)
- Can be installed on a per-user basis
- Invoked from the command line using a POSIX-compliant shell
- The article provides step-by-step instructions for installing NVM on Ubuntu Server 22.04.3 and Rocky Linux 9, as well as guides users through installing different versions of Node.js using NVM.
## Key Takeaways:
- Use NVM to manage multiple versions of Node.js on a single system
- Installable on various operating systems and architectures
- Can be used to install different versions of Node.js for individual projects or applications
Developers often have to depend on multiple versions of the same language, framework, or library. This can happen because one project might depend on the latest version of a language, whereas another project might require a previous release.

Some operating systems and/or languages don’t make the task of using multiple versions of the same language easy. If you happen to use Linux as your development platform and Node.js as one of the many languages you work with, you’re in luck, as there’s a handy tool to make this fairly simple.

The tool in question is called [NVM](https://github.com/nvm-sh/nvm), which stands for Node Version Manager. NVM can be installed on many different Linux distributions, such as Ubuntu, RHEL, CentOS Stream, [Rocky Linux,](https://thenewstack.io/post-centos-rocky-linux-fights-for-community-driven-enterprise-open-source/) [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/), and Debian, as well as MacOS and Windows (via Windows Subsystem for Linux).

Essentially, NVM is a version manager for Node.js that is installed on a per-user basis and is invoked from the command line on any POSIX-compliant shell (such as sh, dash, ksh, zsh, and bash).

I’m going to show you how to install and use NVM on Ubuntu Server 22.04.3 and Rocky Linux 9.

## What You’ll Need
To use NVM, you’ll need the following:

- Either an instance of Ubuntu or Rocky Linux (or another equivalent, such as AlmaLinux or CentOS Stream).
- Node.js installed.
- A user with sudo privileges.
- A network connection.
That’s it. Let’s get to work.

## Installing NVM on Ubuntu Server
Log into your Ubuntu Server instance. If your server includes a desktop environment, open a terminal window.

The next step is to install a few dependencies, which can be done with a single command:

1 |
sudo apt-get install build-essential libssl-dev -y |
Next, download and run the installation script with the command:
1 |
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash |
Once the command completes, log out and log back into your Ubuntu server instance.
## Installing NVM on Rocky Linux (or an Equivalent Distribution)
The installation of NVM on Rocky Linux is similar to that of Ubuntu, the only difference being the installation of the dependencies.

To install the dependencies, log into your Rocky Linux instance and, if necessary, open a terminal window. Then, issue the following command to install the dependencies:

1 |
sudo dnf group install "Development Tools" -y |
The installation of the dependencies will take considerably longer on Rocky Linux than it does on Ubuntu. When it completes, you can then issue the same install command on Rocky Linux as you did Ubuntu, which is:
1 |
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash |
When the command completes, log out of Rocky Linux and log back in. You can then verify the installation with the command:
1 |
nvm --version |
The output should be something like this:
1 |
0.39.5 |
NVM is now installed and ready to use.
If you find the prompt returns that NVM isn’t installed, you might have to reload your .bashrc script with the command:

1 |
source ~/.bashrc |
## Installing Node.js with NVM
Now that NVM is installed, you can use it to install different versions of Node.js. This process is the same, regardless of which distribution you are using. With NVM, you’ll find it possible to install Node.js versions from v0.1.14 all the way to v20.7.0. Of course, you probably won’t want to go all the way back to beta releases and as Node.js is upgraded, newer releases will be added.

To find the complete list of available Node.js releases for NVM, issue the command:

1 |
nvm list-remote |
The output will look something like this:
1234567891011121314151617181920212223 |
v19.0.1 v19.1.0 v19.2.0 v19.3.0 v19.4.0 v19.5.0 v19.6.0 v19.6.1 v19.7.0 v19.8.0 v19.8.1 v19.9.0 v20.0.0 v20.1.0 v20.2.0 v20.3.0 v20.3.1 v20.4.0 v20.5.0 v20.5.1 v20.6.0 v20.6.1 v20.7.0 |
Let’s say your current project requires Node.js version 19.0.1. To install this version, the command would be:
1 |
nvm install v19.0.1 |
When the command completes, you can verify the installation with the command:
1 |
nvm list |
You should see the following output:
-> v19.0.1
system
default -> v19.0.1

If you’ve installed Node.js from your default package manager (such as apt-get), you might see a system entry in the output. If you want to use the version of Node.js installed by the system, you could issue the command:

1 |
nvm use system |
If you have multiple versions of Node.js installed, you can choose which one to use with a command like:
1 |
nvm use v20.7.0 |
The output for the above command will look like this:
1 |
Now using node v20.7.0 (npm v10.1.0) |
With NVM, you can install as many versions of Node.js as needed and switch back and forth between versions with ease. Any time a project demands a different release, switch with the nvm use command and you’re good to go.
## Node.JS FAQ
### Q: What is Node.js?
A: Node.js is an open-source, cross-platform JavaScript runtime environment that allows developers to run JavaScript on the server-side. It provides an event-driven, non-blocking I/O model for building scalable and high-performance web applications.

### Q: What does “Node” stand for in Node.js?
A: The “node” part of Node.js is often misunderstood as standing for “neural network optimization,” but it comes from the name of a coffee shop called “Node Coffee Shop” where Jordan Walke, one of the creators of Node.js, worked at the time.

### Q: What versions of JavaScript can I use with Node.js?
A: You can use any version of JavaScript that is supported by your browser or other clients. However, for maximum compatibility and performance, it’s recommended to use a recent version like ECMAScript 2015 (ES6) or later.

### Q: Is Node.js only used for building web applications?
A: While Node.js is most commonly associated with building web applications, it can also be used for the following:

- Building desktop and mobile apps using frameworks like Electron
- Creating real-time data processing systems using WebSockets and server-sent events
- Integrating backend services with frontend applications
### Q: What are some common use cases for Node.js?
A: Some popular Node.js use cases include:

- Real-time web applications (e.g., chatbots, live updates)
- High-performance web servers (e.g., Express.js, Hapi)
- Microservices architecture
- IoT development
- Machine learning and AI
### Q: What is the difference between synchronous and asynchronous programming in Node.js?
A: Synchronous programming blocks the execution of code until a task is complete. Asynchronous programming allows your application to continue running while performing tasks that take longer, such as I/O operations.

### Q: Is Node.js secure?
A: Node.js isn’t immune to security concerns, but it does provide robust, built-in features such as:

- Buffers and streams for efficient data handling
- Built-in support for HTTPS and TLS encryption
- Sandbox-like environments (e.g., sandboxing in some browsers)
### Q: Can I use other programming languages with Node.js?
A: Although JavaScript is the primary language used with Node.js, you can also write code using:

- C++ via the V8 engine
- Rust via the v8-rs crate
- Python via third-party libraries like pyjs and node-python
### Q: What are some popular frameworks and tools for building web applications with Node.js?
A: Some popular choices for building web applications with Node.js include:

[Express.js](http://express.js)(web framework)[Hapi](https://hapi.dev/)(web framework)[Koa.js](http://koa.js)(web framework)[Socket.io](http://socket.io)(real-time communication library)[Redux](https://redux.js.org/)or[MobX](https://mobx.js.org/)(state management libraries)
### Q: Is Node.js still actively maintained and supported by the community?
A: The Node.js project is actively maintained and updated by a large team of developers, with regular releases and new features added regularly.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)