# Linux Skills: Manage System Services
![Featued image for: Linux Skills: Manage System Services](https://cdn.thenewstack.io/media/2024/06/304436eb-derek-oyen-3xd5j9-drda-unsplash-1024x576.jpg)
Services are long-running applications that provide functionality to users, the local system or remote systems. Services enable most of the network capabilities we take for granted today. Examples of services include the transfer of email, web pages, print jobs, file sharing and more.
System administrators are responsible for service management on Linux devices. These tasks include configuration, startup options, security, etc.
You will need a functional Linux distribution to work with the service management examples below. You may use a physical or virtual computer, and any distribution should work. Note that some distributions include different tools from others. The tools described here are found on most Linux distros.
This article on services fits into a larger series of Linux articles covering various sysadmin topics, including hardware identification and managing system processes. You can build a lab environment by following the information in the
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) article. If you need to review Linux command syntax, read [Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).
In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/) and how the Linux kernel [interacts with hardware.](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)
## What Are Some Common Services?
There are several services you will probably encounter regularly on most Linux systems. You’ll likely manipulate or check their status as part of configuration and troubleshooting tasks.
The following list offers some sample services to be familiar with and a summary of their function.
- sshd : The Secure Shell (ssh) is an essential Linux remote administration tool.
- httpd : The Apache web server is a standard web server service on Linux systems.
- firewalld : The firewall filters network traffic in and out of the system using rules to determine what to allow or block.
- cupsd : The Common Unix Printing System (CUPS) offers excellent management of print servers.
- rsyslogd : The rsyslog service manages system and application log files.
I’ll clear up a confusing point here: the difference between daemons, services and processes.
A Linux daemon runs in the background and does not have a control terminal interface. It responds to events or times to perform a task. It is a type of service.
A Linux service responds to requests from other programs. Not all services are daemons.
Linux processes are instances of running code. Daemons and services may have processes, but so might other software, such as end-user applications like the Chrome web browser or the Vim text editor.
## Check Service Status
The service management command on modern Linux devices is
[
systemctl](https://www.man7.org/linux/man-pages/man1/systemctl.1.html) . The syntax is command, subcommand, service name. It looks like this:
|
1
|
systemctl <subcommand> <servicename>
This example demonstrates the syntax by showing the status subcommand and the sshd service:
|
1
|
$ systemctl status sshd
You will probably need to use the sudo command to elevate your privileges when working with systemctl .
Note: It is a poor security practice to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the
[sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You may be prompted for your password when using
sudo .
The status information allows you to see whether the service is up and running. If it is not running, you will need to start it to use its functionality.
![](https://cdn.thenewstack.io/media/2024/04/fa868594-systemctl-status-sshd.png)
Status results are divided into three categories, with several possible states per category. The following list displays some of the possible states for each category.
- Unit Status
- active (running) – Service is running (this is usually the desired result).
- inactive – Service is not running (you may have stopped it).
- failed – Service failed and is not running.
- Loaded Status
- loaded – Unit configuration file has loaded.
- error – Unit configuration file failed to load.
- Enabled Status
- enabled – Service starts automatically with the system.
- disabled – Service does not start automatically with the system.
### Display Subcommands With the Tab Key
Commands like
systemctl or
ip have many subcommands, and it may be challenging to remember them all. One trick for displaying the available subcommands is to use the Linux tab-completion feature. Type the command, enter a space, and then press the Tab key twice. The available subcommands appear.
|
1
|
$ systemctl <tab><tab>
Be sure to put a space after systemctl .
## What Management Do Services Need?
What kinds of management do services need? Services require security settings, configuration options, resource access, network access, etc. Linux stores these configurations in text files. Each service has one or more text files. When the service starts up (usually when the computer boots), it reads the text file and applies the settings.
That’s an important detail. Services use the settings they find in the text file when they start. If an administrator changes these settings, the service must be restarted to cause it to reread the configuration file and apply the new settings.
Therefore, one of the first sysadmin tasks for managing services is restarting them.
## Start, Stop or Restart Services
Use the systemctl command to manage services. The command recognizes many subcommands, including a restart option.
The syntax is:
|
1
|
systemctl restart <servicename>
For example, to restart the sshd service on the system, type:
|
1
|
$ sudo systemctl restart sshd
![](https://cdn.thenewstack.io/media/2024/04/0f0cf374-sudo-systemctl-restart-sshd.png)
The SSH service shuts down and then starts again. When it does, it applies whatever settings it finds in the SSH configuration file (usually found at /etc/ssh/sshd_config ).
One consideration with restarting a network service like
sshd or
httpd is that it drops existing connections, potentially interrupting user activity. Instead of restarting, you might choose to
reload the configuration, which maintains existing connections.
|
1
|
$ systemctl reload sshd
For both restart and reload use cases, you probably made changes to the configuration file, and the service needs to implement the new settings.
You can also manually manage services by using the
stop and
start subcommands:
|
1
|
$ sudo systemctl stop sshd
|
1
|
$ sudo systemctl start sshd
![](https://cdn.thenewstack.io/media/2024/04/5b7c318c-systemctl-stop-start-sshd.png)
You might want to temporarily stop a service during troubleshooting, security audits or other events when you’re trying to measure the effect of a specific service on the system. Once done, you can manually start the service again.
Note that there is often no feedback from the system with some of these commands. It just manages the service.
## Configure Services to Start Automatically
Starting and stopping services only manages their status during the current system runtime (the current instance of the system). Administrators typically need to instruct services to start automatically when the system boots or not to start when the system boots. The applicable subcommands for these settings are enable and disable .
To cause the SSH service to start automatically when the system boots, type:
|
1
|
$ sudo systemctl enable sshd
To prevent SSH from starting when the system boots, type:
|
1
|
$ sudo systemctl disable sshd
You would probably enable a service after its initial installation.
### Service Management Example
Suppose you’ve just installed the Apache web service on your Linux system and want to manage it. After editing the configuration file, your next step is the start the service so you can test whether it works as expected. Once satisfied, enable it so it launches when the system starts. Finally, confirm the service is running by using the status subcommand.
Here’s an example of the commands:
|
1
|
$ sudo systemctl start httpd
|
1
|
$ sudo systemctl enable httpd
|
1
|
$ systemctl status httpd
You can start and enable a service in one shot using the --now option:
|
1
|
$ sudo systemctl enable --now sshd
### Check the Startup Configuration of Services
The
is-enabled subcommand is useful for checking the startup status of a service without making any changes.
|
1
|
$ systemctl is-enabled ssh
The command returns one of three responses:
- enabled – Service runs automatically.
- disabled – Service does not run automatically.
- static – Service runs when called by another service.
You can also see the service’s current state by using the
is-active subcommand:
|
1
|
$ systemctl is-active ssh
![](https://cdn.thenewstack.io/media/2024/04/e9d09505-systemctl-is-enabled-active-ssh.png)
Note that the service name is aliased to ssh on this distro.
### Prevent Services From Starting
Use the mask and unmask subcommands to prevent or allow services to start. The mask subcommand stops the service from being manually started with the systemctl start command or by being called by another service. The unmask subcommand reverses the setting, allowing the service to run if started. Use the same systemctl syntax you learned above with these two subcommands.
## Wrap Up
Service management is a daily function for Linux sysadmins. Luckily, the systemctl syntax is fairly straightforward. You’ll mainly use the status and restart subcommands. Don’t forget how services discover their configuration settings: They read a configuration file when they start, and they only read it again (to find your changes) if you restart them. That means restarting services is an essential step in system and service configuration.
While this article does not focus directly on security, it’s worth noting that service management is a critical part of hardening. Hardening a system includes removing everything it does not need for its specified role. That means using systemctl to disable any unnecessary or unused services.
Use your lab computer to practice the systemctl command and explore the various subcommands. Be sure to practice the tab-completion trick to display available subcommands I introduced at the start of the article. Learning this tool today will make your Linux administration journey much easier.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)