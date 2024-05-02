# Linux: How the Kernel Interacts with Hardware
![Featued image for: Linux: How the Kernel Interacts with Hardware](https://cdn.thenewstack.io/media/2024/04/3c893af6-ai-generated-8230770_1280-1024x574.png)
[Linux: Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).”
When understanding the structure of a computer system, it helps to think of it as containing four major subsystems. These subsystems are interrelated and impact each other, but begin by thinking of them as separate components.
The four subsystems are:
**Central Processing Unit (CPU)**: The processor is responsible for running code. **Random Access Memory (RAM)**: The memory temporarily stores data and allows for quick retrieval. It is closely associated with the CPU. **Storage**: Solid-state and hard disk drives store data even when the system is off. Storage capacity impacts system performance and capabilities. **Network**: Provides network connectivity, allowing the exchange of files or other communications. [Linux](https://thenewstack.io/Linux/) provides various tools for reporting and examining these components. This article demonstrates many of these utilities.
You will need a functional Linux distribution to follow along with the commands and examples below. You may use a physical or virtual computer, and any distribution should work. Note that some distributions include different tools from others. Most Linux distros include the tools described here.
This article is part of a larger series of Linux articles covering various sysadmin topics. You can build a lab environment by following the information found in the
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) piece.
## Display CPU and Memory Information
The CPU and memory are described above as separate subsystems, but they are closely related. This section covers displaying information about both.
Linux inventories the available hardware during the boot process. Some hardware information is stored in the
[/proc](https://linux.die.net/sag/proc-fs.html) directory, which is dynamically populated each time the system starts. This directory contains two files related to the processor and memory.
- /proc/cpuinfo : Provides information the system detected about the processor during the startup procedure.
- /proc/meminfo : Provides information the system detected about the memory during the startup procedure.
Use the
[cat](https://linux.die.net/man/1/cat) command to show this information. The
cat command displays the contents of files, making it a handy tool for reading files. The
/proc directory also contains PCI bus data, IO ports, and more.
|
1
|
$ cat /proc/cpuinfo
![](https://cdn.thenewstack.io/media/2024/04/4c390696-cat-proc-cpuinfo.png)
The output shows two CPU cores ( and 1 ), along with feature and architecture information. This screenshot is from a virtual machine and does not show the processor model or specifications.
The
meminfo file displays the total memory and how that memory is used.
|
1
|
$ cat /proc/meminfo
![](https://cdn.thenewstack.io/media/2024/04/7e6c776a-cat-meminfo.png)
Why does this information matter? Perhaps the system is new to you, and you don’t know what its current specifications are. Or maybe you’re considering an upgrade and want to see the existing hardware.
You can also use the
[lscpu](https://linux.die.net/man/1/lscpu) command to display information from
/proc/cpuinfo .
One common upgrade is memory. It’s relatively easy to improve the performance of some systems by adding RAM. The /proc/meminfo shows the quantity and type of installed memory.
### Memory Utilities
Two standard information-gathering tools for memory utilization are
[free](https://linux.die.net/man/1/free) and [vmstat](https://linux.die.net/man/8/vmstat). These tools provide basic information on how much system memory is recognized and how it is being used.
The free command displays how much RAM is currently unused on the system and therefore available for additional applications or services.
![](https://cdn.thenewstack.io/media/2024/04/6711ac89-free.png)
Use the -h option to display the results in a more user-friendly format.
The vmstat command indicates virtual memory utilization. Recall that both RAM and storage devices store information. If the system doesn’t have enough RAM to store the required data, it can borrow storage space from the disks. The disks provide additional “virtual memory.” However, this solution can drastically slow the system and should be avoided if possible. It’s better to add more memory or reduce the system’s workload. The use of virtual memory is also known as swapping.
![](https://cdn.thenewstack.io/media/2024/04/b5dc1bf3-vmstat-megs.png)
Use the -S M to display the results in megabytes.
### Use the uname Command
A quick command that displays basic CPU information is
[uname](https://linux.die.net/man/1/uname). It has several options that modify its output. Use the
-a option to show all processor and operating system details. ![](https://cdn.thenewstack.io/media/2024/04/5da22413-uname.png)
The uname command doesn’t provide much information but what it does show is helpful. The information includes Linux kernel version, hardware architecture, processor type, and operating system name.
## Display Storage Information
Hard disk drives (HDDs) or solid-state drives (SSDs) usually provide computer storage. These devices enable long-term file storage. Reviewing storage information on the system allows you to anticipate capacity problems and possibly increase performance.
Most people think of capacity as the primary storage attribute. Today’s storage disks tend to be very large, often larger than end-users need. Data should be stored on network servers in most business environments. However, it’s worthwhile to check storage capacity to ensure the system has plenty of space to work with, especially for servers.
Storage disks impact system performance. System, service, and user files are stored on the drives. The longer it takes to read and write these files, the slower the system becomes.
### Understand Partitions
Storage disks are divided into partitions. Partitions are logical storage units often assigned for specific types of data.
Display partition information by using the same cat command you used above for CPU and memory data. The argument is /proc/partitions .
$ cat /proc/partitions
![](https://cdn.thenewstack.io/media/2024/04/c47a04fb-cat-proc-partitions.png)
The first storage disk is typically named sda , the second sdb , and so on. Each partition on the disk is numbered, beginning with 1 . So, the third partition on the second storage disk is sdb3 .
The /proc directory also contains information about SCSI disks ( /proc/scsi/scsi ) and block devices ( /proc/diskstats ).
You can display similar information using the
[lsblk](https://linux.die.net/man/8/lsblk) command. You can point the command to a specific storage disk, such as
/dev/sda .
$ lsblk /dev/sda
![](https://cdn.thenewstack.io/media/2024/04/a8059866-lsblk-sda.png)
The lsblk command shows disks, partitions, and logical volumes using a hierarchical tree structure for easier interpretation.
### Display Capacity Information
The
/proc/partitions file and
lsblk output show the storage structure, but you typically use the
[df](https://linux.die.net/man/1/df) and [du](https://linux.die.net/man/1/du) commands to learn more about capacity and utilization.
The disk utilization ( du ) command is useful for understanding how much space specific directories or files consume. For example, if you have a folder full of pictures, you might use the du command to determine how much of your storage drive the folder uses. The du command estimates this consumption by adding the sizes of all selected directories and files.
You’ll almost always use the -h option to display sizes in human-readable formats, such as KB, MB, GB, etc.
Try using
du to check how much capacity log files consume on your Linux device. Linux stores log files in the
/var/log directory.
|
1
|
$ du -h /var/log
![](https://cdn.thenewstack.io/media/2024/04/eab18749-du-h-var-log.png)
The -s option provides a summary of the utilization without listing all files. This is helpful for directories with a lot of content.
![](https://cdn.thenewstack.io/media/2024/04/2d15283f-du-hs-var-log-summary.png)
The df utility shows overall drive capacity consumption by displaying the total available and used space. For example, if your system has a single hard disk drive with one partition, df would show how much of that drive is available for more files and programs and how much is already consumed.
The df command also benefits from the -h option to make its output more user-friendly.
$ df -h /dev/sda
![](https://cdn.thenewstack.io/media/2024/04/130149eb-df-h-sda.png)
## Display Network Information
Network connectivity is critical to most Linux devices. Wired and wireless network interface cards (NICs) attach the system to other network nodes, enabling email, web browsing, printing, file sharing, and more.
One of the most common network information-gathering and troubleshooting tools is the
[ip](https://linux.die.net/man/8/ip) command. This command includes numerous subcommands that modify its function. For example, use the
ip addr command to display basic network settings:
|
1
|
$ ip addr show enp0s5
![](https://cdn.thenewstack.io/media/2024/04/fca39281-ipaddr-show-eth.png)
The ip addr command shown above displays the interface name ( enp0s5 ), basic transfer information ( mtu 1500 ), and state ( UP ). It also shows the interface’s media access control (MAC) hardware address ( 00:1c:42:c2:62:1c ) and the IPv4 logical address ( 10.211.55.4/24 ). The status and IP address are particularly important for troubleshooting.
The older version of the
ip command is
[ifconfig](https://linux.die.net/man/8/ifconfig). Some Linux distributions may still recognize the command, but you should learn the
ip command instead.
### Use the ethtool Utility
The basic
[ethtool](https://linux.die.net/man/8/ethtool) command displays the current hardware settings for the specified network card (
enp0s5 ).
|
1
|
$ ethtool enp0s5
![](https://cdn.thenewstack.io/media/2024/04/894d8324-ethtool.png)
Add the
-i option to display device driver information.
|
1
|
$ ethtool -i enp0s5
![](https://cdn.thenewstack.io/media/2024/04/9473fab8-ethtool-i.png)
It’s generally a good idea to use the most current drivers.
One practical use of
ethtool is to cause the physical NIC’s light to blink for a period of time. This feature helps identify NICs on Linux devices with multiple interfaces.
|
1
|
$ ethtool --identify enp0s5 5
The above example blinks the light for five seconds.
## Use Monitoring Tools
The tools above display specific information about individual system components. However, tools like top, htop, and Glances provide a broader view of hardware. The utilities in this section show performance information in real-time and help you analyze how the hardware is used.
### Use the top Utility
The standard Linux hardware monitoring tool is
[top](https://linux.die.net/man/1/top). It displays basic hardware information in the upper frame, with a dynamic table of system processes and their CPU and memory consumption in the lower portion. ![](https://cdn.thenewstack.io/media/2024/04/08f4d1f8-top-hwinfo.png)
![](https://cdn.thenewstack.io/media/2024/04/853b3ac8-top-monitor.png)
Sort the main CPU and memory consumers by using the
**P** and **M** keys. When you’re done examining top’s results, press the **q** key to exit.
### Use the htop Utility
A more dynamic utilization tool is
[htop](https://linux.die.net/man/1/htop). Not all Linux distributions install it by default, so you may need to add it to your system. The htop tool is a real-time monitor with a more robust dashboard that includes color coding and dynamic elements. This is more of a monitoring tool than a way of gathering system hardware information, but it provides insights into how the hardware behaves and whether the system has sufficient resources for its workload.
### Use the Glances Utility
The
[Glances](https://nicolargo.github.io/glances/) hardware monitor is not installed on all Linux distributions by default, but it’s easy enough to add to the system. Glances offers real-time monitoring of system resources using an easy-to-read dashboard. Glances is great for Linux users with more than one system because it includes a web mode that allows remote connectivity to monitor multiple devices.
Glances is open source and written in Python so it can be run on Linux, macOS, and Windows systems, making it an even more compelling information-gathering tool.
## Wrap Up
Recall that a computer system consists of several subsystems. These include processing capabilities, storage, and networking. System administration includes displaying hardware information and using it to manage services, processes, applications, and more.
Linux users will want to see hardware information to help select system upgrades, monitor performance, and troubleshoot issues. Many resources, like /proc/cpuinfo and /proc/meminfo , provide static information. Others, such as top and Glances, offer a dynamic view of real-time processor, memory, storage, and network hardware resources. You’ll often find yourself using multiple tools to ensure you understand the system specifications.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)