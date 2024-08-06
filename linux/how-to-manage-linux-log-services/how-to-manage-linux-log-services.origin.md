# How To Manage Linux Log Services
![Featued image for: How To Manage Linux Log Services](https://cdn.thenewstack.io/media/2024/06/a8082e57-thomas-park-i_dqdjghckw-unsplash-1024x660.png)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/)and
[installation platform](https://thenewstack.io/linux-choose-an-installation-platform/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/),
[file permissions](https://thenewstack.io/linux-how-file-permissions-work/),
[system processes](https://thenewstack.io/linux-manage-system-processes/), and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
Log files are a critical tool for Linux users troubleshooting system issues, auditing uptime and managing security configurations. Like other operating systems, Linux includes robust logging features that track information like login attempts (successful and failed), software installation, application errors, system halts and more. Modern Linux systems rely on two logging services: syslog and journald. The common syslog implementation is [rsyslog](https://www.rsyslog.com/). Maintaining and reviewing system logs is a critical part of any Linux administrator’s job.

This article explains the rsyslog logging service and compares it with the newer journald system. It uses practical command examples to manage the services and update configuration files.

This discussion of log files fits into a broader series of Linux articles covering various sysadmin topics, including hardware identification and managing system processes. You can build a lab environment to try these commands yourself by following the information in the [Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) article. If you need to review Linux command syntax, read [Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).

This series also covered [how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/) and how the Linux kernel [interacts with hardware.](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)

Note: It is poor security practice to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the [sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You may be prompted for your password when using
sudo .

## Understand and Manage the rsyslog Service
Use the
systemctl command to manage the rsyslog service. You can start, stop and restart the service. These options are handy when making changes to the configuration file. The rsyslog service must be restarted to read the updated configuration file settings.

1 |
$ sudo systemctl restart rsyslogd |
You can cause the service to start or stop the service from starting when the system boots by using the
systemctl
enable and
disable commands. Here are examples of each:
1 |
$ sudo systemctl disable rsyslogd |
1 |
$ sudo systemctl enable rsyslogd |
These are the same commands and approaches you use to manage other services.
## Identify Specific Logs in /var/log
Linux distributions use a standard storage location for log files. The location is the /var/log directory. Additional logs and subdirectories exist in that directory. These vary by distribution and installed applications.

Use the
cd command to change to the
/var/log directory, and then [list the contents](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) using the
ls command.

Here are the common log files for Fedora and Ubuntu Linux. Notice that some of the logs vary between the two distributions. This is a common occurrence with Linux distributions.

Examples of log files found in Fedora Linux:

- /var/log/messages : System logs like kernel, authentication and services
- /var/log/secure or /var/log/auth.log : Authentication logs
- /var/log/boot.log : Boot log
- /var/log/kern.log : Linux kernel log entries
- /var/log/dnf.log : Installations and other package manager events
- /var/log/utmp : Current system logins and connections
- /var/log/btmp : Failed login information
- /var/log/wtmp : Historical record of utmp entries
Note that some logs referenced above are found in older Linux versions. Log entries for the kernel, services, authentication and other functions have been moved to the journald logs on many distributions.

![](https://cdn.thenewstack.io/media/2024/06/12360ac3-ls-var-log.png)
Examples of log files found in Ubuntu Linux:

- /var/log/syslog : System logs like kernel, authentication and services
- /var/log/kern.log : Linux kernel log entries
- /var/log/auth.log : User logins and sudo credential use
- /var/log/fail.log : Failed authentication attempts
- /var/log/lastlog : Most recent logins by users
- /var/log/apt : Installations and other package management events
Some distributions add or remove logs in the /var/log directory, so you may need to check the documentation for your specific Linux distro. Some logs above are now part of the journald logging mechanism and may no longer appear in the /var/log directory.

### Application Log Files
Many applications integrate with rsyslog to manage their logs. For example, rsyslog can manage and forward log files for the common Apache webserver program. Apache’s logs are usually at /var/log/httpd on Red Hat-based systems or /var/log/apache2 on Debian-based distros. Tools like the Nginx webserver and MySQL database use a similar logging scheme.

## Read and Search Log Files
Syslog log files are simple text documents, easy to open and read with applications like cat and less . Tools like grep and tail also enable robust filtering and search capabilities to help you find exactly what you’re looking for.

### Use grep to Search Logs
Most log files store their information in plain text, making them easy to read and search. For example, you may wish to check
/var/log/dnf.log to see whether the
vim software package is installed. Use the
grep pattern-matching utility to check for the application.

1 |
$ sudo cat /var/log/dnf.log | grep -i vim |
![](https://cdn.thenewstack.io/media/2024/06/58d86955-dnf-log-vim.png)
Any log file entries with the vim string should be displayed. The grep pattern matcher is helpful in these situations. The -i option used above causes it to ignore case.

### Use tail to Search Logs
Another helpful tool for checking log files is the
tail command. It displays the bottom of a file. Log files store the most recent entries at the bottom, so you can see the most current information by examining the end of the log file.

1 |
$ tail /var/log/dnf.log |
You can adjust how many lines
tail displays by using the
-n switch and the number of lines you want to see. The following example displays 20 lines instead of the default 10.
1 |
$ tail -n 20 /var/log/dnf.log |
However, the most useful flag for tail might be
-f . This option periodically refreshes the
tail output, allowing you to open a terminal window,
tail a log file and see the window update periodically with most recent log entries.
1 |
$ tail -f /var/log/dnf.log |
## What Is journald?
Today, most Linux distributions rely on systemd for system initialization and service management because it offers modern advantages over the older init system. You’ll use commands like
systemctl restart sshd to [manage services](https://thenewstack.io/linux-skills-manage-system-services/) with systemd.

Another aspect of systemd is log file management. systemd needed a different and more robust logging mechanism than rsyslog could offer. The result is journald, a new log file mechanism available on most current distributions. It collects information from the Linux kernel. It also logs information from services and applications that systemd manages.

However, many discussions of Linux logs make it sound as though you must pick one logging engine or the other. In reality, you’ll probably use both journald and rsyslog to keep an eye on what’s happening on your system.

### journald Advantages and Disadvantages
Like any other utility, journald has its advantages and disadvantages compared to similar services. The following are a few considerations.

Advantages:

- journald indexes entries, making lookups much faster.
- Easily filter and prioritize log file entries.
- Privileged access, where users can see logs pertaining to their jobs, and root can see all log entries.
- Flexible log rotation built in.
Disadvantages:

- It cannot natively forward logs to a central server for aggregation.
- It does not use standard text files to record information, making reading log entries with anything other than the journalctl command tougher.
## View Logs Using journalctl
The journalctl command allows administrators to configure journald settings and display log file entries. It offers extensive customization and flexibility.

There are two primary journald resources to be aware of:

- The default persistent storage location for journald logs is /var/log/journal .
- The primary configuration file is /etc/systemd/journald.conf .
Be sure to use the sudo command if the privilege is delegated to you. journald carefully filters what it displays depending on the user.

The journalctl command without arguments shows recent log entries in chronological order (oldest entries first). It automatically uses the less utility to break results into pages, so navigate the entries the same way you would with less .

Use the **q** key to exit the journal. Below is the partial output from the
journalctl command.

![](https://cdn.thenewstack.io/media/2024/06/55ed054a-journalctl.png)
To display logs in reverse order (most recent entries first), type:

1 |
journalctl -r |
Use the
-n flag with a specified number to display a limited number of entries. For example, to display five entries, type:
1 |
journalctl -n 5 |
![](https://cdn.thenewstack.io/media/2024/06/714cb3eb-journalctl-n5.png)
Some Linux users will be familiar with the trick of viewing log files in real time using the
tail -f command. The
-f option functions the same way with the
journalctl command, automatically refreshing the command output to show you the latest log entries in real time. Exit the output by using **Ctrl+C**.

1 |
journalctl -f |
The
-k option displays kernel messages. This flag is useful when troubleshooting problems at the kernel level without the clutter of service log entries.
![](https://cdn.thenewstack.io/media/2024/06/3d3994ec-journalctl-k-kernel.png)
Add the
| grep {string} command to filter your
journalctl output. For example, perhaps you’re looking for errors or misconfigurations in your system’s bootup sequence that might be slowing it down. One term to search for is “Unknown.” Use
grep and the
-k option to display kernel information.

1 |
$ sudo journalctl -k | grep -i unknown |
![](https://cdn.thenewstack.io/media/2024/06/0b3ceabc-journalctl-grep.png)
Some of the most important and interesting results will come from specific services. Specify the service name as the argument to the
journalctl command. For example, to display logs related to firewalld, type:

1 |
journalctl -u firewalld |
![](https://cdn.thenewstack.io/media/2024/06/60e7a8c8-journalctl-u-firewalld.png)
The -u flag stands for unit and offers administrators further control over the output displayed.

These are a handful of the journalctl options. It also offers filtering by time intervals and log entry severity. It’s easy to see why journalctl is popular with administrators who take the time to learn it — it offers great flexibility for filtering and managing log data.

## Integrating journald With rsyslog
A certain amount of integration is available between rsyslog and journald. While journald doesn’t forward log files to a remote central server for aggregation, it can forward log entries to rsyslog, which can then forward them to remote systems. This approach lets administrators continue to centralize logs for auditing and analysis while still benefiting from the additional information journald receives from the kernel and services managed by systemd.

You’ll likely use both mechanisms to monitor your Linux servers.

## Wrap Up
Administrators should regularly review log files for odd behavior, unexpected actions, suspicious login attempts, etc. Doing so helps you understand the system better and identify potential security or performance problems. You may also be required to demonstrate log file maintenance in compliance or security audits. Commands like grep , tail , and less help you view and manipulate rsyslog log file entries. You’ll use the journalctl command to view log entries managed by journald.

If you manage more than a few Linux systems, consider centralizing log files on a single server using rsyslog’s built-in forwarding mechanism. This is tougher to accomplish with journald logs, but it can be done.

One of the most confusing parts of managing Linux logs is the variations among distributions. Hopefully, your organization has standardized on just one or two specific distributions. If that’s the case, review the documentation or wiki for the distro and note the log files it uses. This process is tougher if your company uses many different distros.

Begin now to learn what logs exist, where they are found, and how to filter or search them to find what you need.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)