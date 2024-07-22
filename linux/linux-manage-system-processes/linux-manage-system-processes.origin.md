# Linux: Manage System Processes
![Featued image for: Linux: Manage System Processes](https://cdn.thenewstack.io/media/2024/06/d4c22c47-penguin-6905568_1280-1024x577.jpg)
A process is an instance of running code. It’s an executing program, such as a web browser or text editor. The Linux operating system itself also consists of processes. These running services, applications and OS components consume resources on the computer and may access data. Understanding processes is crucial as it enables efficient resource management and troubleshooting, tasks that often fall under the purview of a Linux administrator.

This tutorial dives into the practical aspects of managing processes in Linux. It equips you with the knowledge to identify and display processes, a skill that comes in handy during troubleshooting and resource management. You’ll also explore various Linux utilities that provide insights into process behavior, a valuable toolset for any Linux user or administrator.

To follow along with this tutorial’s commands and examples, you will need a[ functional Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/). Whether you’re using a physical or virtual computer, any Linux distribution should suffice. Keep in mind that while some distributions may include different tools, the ones I’ll be discussing here are found on most Linux distros. This tutorial is part of a comprehensive series on Linux system administrator that’s designed to equip you with the skills and knowledge needed to effectively manage your Linux environment.

You can build a lab environment by following the information found in the [Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) article.

In this series, we also covered how the Linux kernel [interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/), how [Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/) and how [Linux manages users](https://thenewstack.io/linux-user-and-group-management/).

## Understand Processes
Processes are programs in execution on the system. They consist of several components, including:

- Program instructions: Machine code instructions processed by the CPU.
- Data: Information manipulated by the process.
- Resources: Processor time, memory space, storage space and network connectivity consumed by the process.
- Process ID (PID): A unique identity for the process. The PID allows administrators to reference the process to manage it.
- Parent Process ID (PPID): A process that spawned the process you’re working with.
Linux processes have several characteristics, including:

- Hierarchy of parent and child processes.
- Scheduling for access to system resources (mainly the CPU).
- Isolation of process address spaces for stability and security.
Processes may exist in several states, namely running, sleeping or stopped. Linux distributions include various tools to view and manage processes on the system. These tools include ps , pidof , kill and others. This tutorial examines multiple utilities.

Refer to the [Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) article if you need to review the syntax of Linux commands.

## What Administration Do Processes Need?
Most of the time, Linux users and administrators manage applications by starting and stopping them with commands or graphical icons. Launching these applications initiates one or more processes. Exiting the program ends those processes.

Here are the typical ways of starting and stopping the man page application to show the help file for the [ls](https://linux.die.net/man/1/ls) command.

1 |
$ man ls |
This command launches any necessary processes to run the machine code, making up the man page-viewer application.
Exit the man page program gracefully by selecting the **q** key. This should close the program, ending any related processes.

Note: The man page system contains Linux documentation. It is useful for displaying a help file showing a command’s syntax and various options (modifiers). The syntax is man program-name, such as the man ls example above.

So what administration is there to do? If the application starts and stops cleanly, there’s little for the administrator to worry about. However, if the program does not function correctly, the administrator may need to manually close the application or check to see what resources it is consuming.

Linux users refer to programs by name, such as the Vim text editor. However, the computer references these processes by an ID number.

## What Are Process IDs?
Process IDs (PIDs) are unique numbers assigned to processes by the Linux kernel when the process spawns (starts). PIDs are important because they are a way to reference the process for attention by the administrator. The administrator may need to know how much memory or processor time the process consumes. The administrator may also need to end the process manually if it does not quit correctly.

![](https://cdn.thenewstack.io/media/2024/04/4bd43786-ps-man-pid.png)
Note: It is poor security practice to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the [sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You may be prompted for your password when using sudo. Some commands in this tutorial may require the sudo command on your Linux distribution.

## Display and Manage Processes
The primary process management command is ps . This flexible and powerful command displays processes and offers many options.

List all processes along with supplementary information:

1 |
$ ps -ef |
![](https://cdn.thenewstack.io/media/2024/04/cd01b0ed-ps-ef.png)
This is probably the most common use of the [ps](https://linux.die.net/man/1/ps) command for most administrative tasks.

The ps -ef command displays all running processes, meaning you’re likely to get an immense number of results. Later in the tutorial, I’ll show you how to filter or search for these results using the grep utility.

List all processes by a given user by using the
-u option:

1 |
$ ps -u username |
Reference the [man page for ps](https://linux.die.net/man/1/ps) to learn about additional options.
### Managing Jobs
Programs typically run in the foreground, meaning they consume the interface and both you and the system focus on them. However, it is possible to execute processes in the background. This causes them to run but permits you to continue using the command-line interface (CLI) to accomplish other tasks.

To foreground and background processes, you must work with a different set of identifiers. Specifically, these are job IDs. Job IDs are slightly different from process IDs. Process IDs are labeled systemwide, while job IDs are identified on a per-user basis. All jobs are processes, but not all processes are jobs (since some processes are not assigned to specific users).

When you first run a job, it executes in the foreground, consuming the shell and preventing you from running other commands. This could be an issue if you’re launching a long backup job or another task that takes a while to run.

You can interrupt a running process using **Ctrl-Z** and then type
bg to background it. You can launch a program directly into the background by typing the program name and adding the
& character.

1 |
$ man ls & |
This command example runs the
man ls command in the background.
Display running jobs using the jobs command.

![](https://cdn.thenewstack.io/media/2024/04/3a92ab9e-jobs.png)
Bring a job to the foreground (maybe to check its progress or status) by using the
fg command and the job ID number.

1 |
$ fg %1 |
![](https://cdn.thenewstack.io/media/2024/04/de93f9ae-fg-man.png)
### Use grep to Filter ps Results
Production Linux systems may have thousands of processes running simultaneously, making browsing or searching the
ps command output difficult. You can combine
ps with a filtering or pattern-matching utility named [grep](https://linux.die.net/man/1/grep) to find exactly what you’re looking for.

The syntax for using
ps and
grep together looks like this:

1 |
$ ps -ef | grep process_name |
I’ll break down each part.
- ps -ef : The ps command with the options you want.
- | : The “pipe” character takes the output of the first command and uses it as the input of the second command. In this case, it takes the results of the ps command (a list of all processes) and makes it the input of the grep command (a search tool).
- grep process_name : The grep command searches the ps results for the process_name you specified, filtering or narrowing the output to something more manageable.
![](https://cdn.thenewstack.io/media/2024/04/d8033290-grep-ssh.png)
Note: You can use
| grep pattern with many other commands. Use the
-i option with grep to ignore upper- and lowercase differences. For example, try it with the
ls command to search the
/etc directory (configuration files) for any network files and directories:

1 |
$ ls /etc | grep -i net |
![](https://cdn.thenewstack.io/media/2024/04/879cc438-grep-net.png)
## Kill Processes
Most applications will exit gracefully, meaning they return their CPU time and memory address to the operating system and end their own process. Sometimes, an application does not exit gracefully, and the administrator must end the process using the [kill](https://linux.die.net/man/1/kill) command.

The kill command can send various signals to the application, but the most important is the -9 or SIGKILL . This signal unequivocally ends the process, forcing it to close and return its resources to the system.

Be aware that you will lose any unsaved data if you end a program this way. Killing a process is usually a last resort.

The command looks like this (assuming PID 9876):

1 |
$ kill -9 9876 |
Other signals include:
-
SIGINT (
2 ): Interrupts or ends the process (
**Ctrl+C**). - SIGTERM ( 15 ): Ends the process gracefully.
Killing a process is a severe action. Attempt to end the process gracefully when possible.

### Understand Zombie Processes
One administrative task you may encounter is eliminating zombie processes. Zombie processes are leftover remaining components from programs that are no longer running but did not properly end all processes. These zombie processes continue to consume process IDs when they no longer support an application. This isn’t normally a problem, but you should be aware of them. You’ll need to clean up zombie processes by ending the parent processes.

Again, zombie processes don’t consume many CPU or memory resources, so don’t be too concerned.

## Other Commands
The main process management tool is ps , but several other useful tools exist for manipulating processes. These tools include pgrep , pidof and pstree .

### The pgrep Command
The [pgrep](https://linux.die.net/man/1/pgrep) command combines the
ps and
grep utilities to simplify searching for specific processes. Add the
-l option to display the actual process name with the PID. For example, to search for processes related to the SSH utility, type:

1 |
$ pgrep -l ssh |
![](https://cdn.thenewstack.io/media/2024/04/72822cd7-pgrep-l-ssh.png)
### The pidof Command
The [pidof](https://linux.die.net/man/8/pidof) command shows PID information for running applications. The syntax is the
pidof command plus the program name.

1 |
$ pidof program_name |
![](https://cdn.thenewstack.io/media/2024/04/9db1a183-pidof-sshd.png)
Note that the program name might be different from the application title.

The command is useful for discovering a process ID so you can view its resources or kill it (if necessary).

### The pstree Command
Some applications are complex enough to require more than one process. Others dedicate new processes to each new network connection or service request. These processes are called parent processes, and the subprocesses they start are called child processes.

When examining system performance, displaying a parent process and its related child processes in a visual format may be helpful. The [pstree](https://linux.die.net/man/1/pstree) command provides that capability.

With no argument or options specified,
pstree displays all processes on the system.

1 |
$ pstree |
![](https://cdn.thenewstack.io/media/2024/04/1e20bfd0-pstree.png)
It may be more useful to display the
pstree beginning with the parent process you’re interested in. For example, to see the process tree for the parent process 9876, type the following command:

1 |
$ pstree 9876 |
If a user started the program, you could display the processes (parent and child) for any applications run under that user’s authority. Use this command:
1 |
$ pstree username |
Add the
-p option to display the PID of displayed processes:
1 |
$ pstree -p username |
![](https://cdn.thenewstack.io/media/2024/04/70c5ff6b-pstree-damon-gui.png)
## Other Process Commands
The [top](https://linux.die.net/man/1/top) utility also displays process information. While
top is usually considered a performance monitoring utility, processes consume resources, impacting the system’s performance. You might use
top with the
ps command to determine which processes are causing issues.

![](https://cdn.thenewstack.io/media/2024/04/5d3943bf-top.png)
Some Linux distributions use the [htop](https://linux.die.net/man/1/htop) command as a more robust alternative to
top .

## Wrap Up
Linux users and administrators will periodically need to manage the code running on their systems. Code being executed by the CPU is called a process, and you can display processes and related information using the ps command. One critical component of process management is the process ID — the label by which the system identifies the process. You’ll use this PID to investigate or kill the process if necessary.

Other Linux tools also work with processes, including pgrep , pidof , pstree and top . Use these tools to learn more about what’s running on your system and troubleshoot issues.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)