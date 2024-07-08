# How to Manage Linux Storage
![Featued image for: How to Manage Linux Storage](https://cdn.thenewstack.io/media/2024/07/138ac0f8-getty-images-acyelgjsmjs-unsplash-1024x675.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/)and
[permissions](https://thenewstack.io/linux-user-and-group-management/).
One of the most common [Linux sysadmin tasks](https://www.thenewstack.io/Linux) is managing storage space. Storage drives contain all kinds of information: user data, log files, temporary files, updates, and more. Many end-users don’t realize that storage space is still a finite resource on today’s computer systems, and they often fill the capacity with redundant, useless, and non-business files.

Administrators add solid-state or hard disk drives to Linux systems to increase capacity. However, the storage space must be organized into partitions and structured with a filesystem before use.

This article demonstrates how to add and identify storage space, including partitioning and installing a filesystem. It also shows the commands you need to investigate drive space utilization. You can work with these commands without any additional setup, but you may find it useful to review the [Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) article. You will need to add a storage disk to your lab computer or virtual machine to practice adding storage.

Be very careful when working with the commands below on systems containing actual data. Tools that manipulate partitions and filesystems can easily cause you to lose data, so always begin with a backup. Using a lab computer that does not contain any real user or business files is even better. Refer to this [tutorial](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) if you’d like to build a lab environment to practice these commands.

Note: It is a poor security practice to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the [sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You may be prompted for your password when using
sudo.

## Identify Storage Devices
Suppose a user has consumed all the space on their Linux system’s storage drive, or perhaps a server’s storage disk is full. While teaching users to manage space efficiently is helpful, it’s often true that the data consuming the drive is legitimate and necessary. That means you’ll need to add more storage space.

Assume you’ve physically installed an additional solid-state or hard disk drive in the computer. Your next task is to identify it so you can add one or more partitions.

### Drive Identification
Linux makes it easy to see the actual storage disks by representing them as files in the /dev directory. Each disk is identified by a series of letters.

- sd = storage disk
- a or b = first or second disk (it also counts c, d, etc.)
- 1 or 2 = partitions on the disk (it also counts higher)
The result is that /dev/sdb1 is storage device ( sd), second device ( b), first partition ( 1), or the first partition on the second storage device.

It is critical to understand that storage disks a, b, c, etc.in Linux have no relationship to C: or D: disks in Windows. The two operating systems do not represent their storage capacity in the same way.

Use the ls command to display the contents of the /dev/disk directory. In Ubuntu, you can view storage devices by-id, by-path, etc. You should see at least one entry that reads sda. That’s the first storage disk in the system. When you add a second disk, it will be labeled as sdb. Other identifiers include the disk’s Universally Unique ID (UUID).

![](https://cdn.thenewstack.io/media/2024/06/c72e4173-ls-dev-disks-by-uuid.png)
However, using the lsblkcommand to display the disks is easier. The tree-like output shows the storage devices, including sdaand sdb (assuming two physical disks are installed). It also shows any existing partitions.

![](https://cdn.thenewstack.io/media/2024/06/962afa3f-lsblk-dev-sda.png)
After you identify the new disk (probably sdb), the next step is creating one or more partitions on it to organize data. Administrators create partitions to store various types of data on different sections of the drive. Often, you’ll simply create a single partition that consumes the entire drive.

Another helpful command for showing partition information is cat /proc/partitions. This output displays all storage disks and partitions the system currently recognizes.

![](https://cdn.thenewstack.io/media/2024/06/765fc44e-cat-proc-parts.png)
## Manage Partitions
Linux uses two primary tools to manage partitions: fdisk and parted. They share many basic features (create, delete, and display partitions), but their advanced usage differs significantly.

### Manage Partitions with fdisk
The fdisk utility has been part of system setup for years. Its primary functions include creating and deleting partitions. It also displays partition information, helping administrators understand and plan storage capacity.

![](https://cdn.thenewstack.io/media/2024/06/ebc2e739-fdisk-l-dev-sda.png)
fdisk is an interactive program. Run it by typing
fdisk /dev/sda, then press the **m** key to display a menu. Here are the common menu items to be aware of:

Command: |
Description: |
n | Create a new partition |
d | Delete an existing partition |
p | Print the current partition table |
w | Write (save) changes to the partition table and exit fdisk |
q | Exit fdisk without saving changes to the partition table |
![](https://cdn.thenewstack.io/media/2024/06/c92c9036-fdisk-menu.png)
fdisk can handle more tasks, but these are the primary ones. Be aware that deleting or changing partitions makes existing data difficult or impossible to recover.

When you select the option to create a new partition (**n** in the menu),
fdisk prompts you through the rest of the partition configuration. You’ll set the partition size, which may be displayed and entered by identifying sectors or specifying capacity, such as mebibyte or gibibyte.

Note that gibibytes and gigabytes are slightly different measurements. Gibibytes are a precise measure of multiples of 1024, while gigabytes are based on powers of ten. The measures result in totals like 1024 (gibibytes) versus 1000 (gigabytes).

Here are the step-by-step instructions on creating a partition with fdisk :

- Open fdisk by specifying the drive you want to partition. For example, to work with drive /dev/sdb , type fdisk /dev/sdb .
- If necessary, set the partition table to GUID Partition Table (GPT) or Master Boot Record (MBR).
- Select
**n**to create a new partition. - Enter a partition number (1-4 for MBR tables and 1-128 for GPT tables). Note that if you choose to create an MBR table, you can define up to three primary partitions or one extended partition. This is only necessary with MBR tables.
- Set the size by defining the first available sector.
- Set the rest of the size. It’s easiest just to tell
fdisk to add a certain amount of space starting from the defined first sector. For example, to create a 50-gibibyte partition, set the ending size as
**+50G**. - Enter
**p**to print or display the partitions, including your new one. Note that fdisk has not yet made changes to the disk. - If you’re happy with the new partition’s settings, write (save) the changes using the
**w**This will also exit fdisk . If you don’t want to keep the changes, go back through and edit the settings or quit fdisk without saving by pressing**q**.
![](https://cdn.thenewstack.io/media/2024/06/3a10c7fc-fdisk-create-a.png)
![](https://cdn.thenewstack.io/media/2024/06/745e39fc-fdisk-create-print-b.png)
![](https://cdn.thenewstack.io/media/2024/06/34f0d351-fdisk-create-write-c.png)
Once you save the partition information and exit fdisk , use the lsblk command to display the new disk and partitions. On some systems, you may need to type the partprobe command to update the partition information.

![](https://cdn.thenewstack.io/media/2024/06/7a6b09ee-lsblk-dev-sdb.png)
### Manage Partitions with parted
The GNU parted (partition editor) utility serves a similar purpose as fdisk , though it is more robust because it allows administrators to extend or shrink partitions.

Like
fdisk,
parted is an interactive tool. Once you’re in the program, type **help** to see the various configuration options.

Common commands include:

Command: |
Description: |
mklabel | Define a partition table type, such as GPT or MBR |
mkpart | Create a new partition on the selected drive |
Display the current partition table | |
quit | Exit parted, saving any changes |
![](https://cdn.thenewstack.io/media/2024/06/3237b8ac-parted-help.png)
The general partition configuration steps are the same as those for fdisk . The steps are:

- Open parted to edit a drive, such as /dev/sdb , by typing parted /dev/sdb .
- If necessary, create a new partition table with the
**mklabel {type}**You can enter**msdos**for a Master Boot Record table or**gpt**for a GUID Partition Table. You’ll probably want to enter**msdos**. - Create a new partition using
**mkpart**and the desired type and size. Types include primary or logical if you plan to use the ext4 filesystem. - Parted prompts you for the first and last GiB, which is necessary to set the size you want. You can also set the size using percentages of the space.
- Use the
**print**command to display the modified (but unsaved) table. - Save your changes and exit parted using the
**quit**command.
![](https://cdn.thenewstack.io/media/2024/06/4fe2714b-parted-print-parts.png)
Remember to review the final configuration using the lsblk command. Try the partprobe command if the new partition isn’t displayed.

Parted is extremely flexible and powerful. The above steps are just the minimum commands to create a new partition.

Be careful if you use the resize command in parted to shrink a partition that contains data. You risk losing your data. I strongly recommend a backup before resizing partitions.

## Install a Filesystem
Now that you’ve divided the storage disk’s capacity into one or more partitions, you must add a filesystem to organize data. Windows typically relies on a single filesystem (NTFS), but Linux supports multiple filesystem options. The two most common are ext4 and XFS.

Use the
mkfs command to install a filesystem on a specified partition. For example, to add the XFS filesystem to
/dev/sdb1 , type:

1 |
$ sudo mkfs.xfs /dev/sdb1 |
A similar example using the ext4 filesystem looks like this:
1 |
$ sudo mkfs.ext4 /dev/sdb1 |
![](https://cdn.thenewstack.io/media/2024/06/618faeee-mkfs-sdb1.png)
The mkfs command has a few variations or options, but they are less commonly used.

The storage space is now ready for users. The only remaining step is making the capacity available by mounting it to a directory where they can save data.

## Create Mount Points
Linux does not label storage space with drive letters like Windows. Instead, administrators attach or “mount” the storage space to directories. Maybe the file server you’re working on is low on storage space, and a team is about to begin a major project. In the earlier steps, you added a disk, partitioned it, and installed a filesystem. Next, create a directory named projects and mount the new storage space there, making the capacity available.

First, create a directory at the root of the filesystem named
projects by using this command:

1 |
$ sudo mkdir /projects |
![](https://cdn.thenewstack.io/media/2024/06/fc5285b6-mkdir-projects.png)
Then, attach the storage space by using the
mount command:

1 |
$ sudo mount /dev/sdb1 /projects |
![](https://cdn.thenewstack.io/media/2024/06/1b351ca3-mount-projects-sdb.png)
The syntax for mountis to specify the physical device ( /dev/sdb1 in the above example) then the directory where it should be mounted ( /projectsin the above example).

Verify the existence of the storage space by using the
dfcommand.

1 |
$ df -h /projects |
![](https://cdn.thenewstack.io/media/2024/06/a9e87c27-df-h-projects.png)
There’s more information on the dfcommand below.

Don’t forget to use Linux permissions to control access to this storage space.

### A Note About umount
Removable media, such as DVDs and USB drives, must also be mounted using the
mountcommand. These temporary storage areas must also be detached using the
umountcommand. Notice the spelling of the command; to unmount, use the
umountcommand (without the **n** character).

## Check Storage Utilization
The above tools provide information on adding and configuring storage space, but two of the most useful investigative tools for managing drives are duand df. Their primary role is to show how storage space is currently being used.

### Use the du Command
The [du](https://linux.die.net/man/1/du) command displays disk usage. It shows the storage capacity specified directories consume, allowing you to identify which directories use the most space. For example, these directories might contain log files or user data.

Like other Linux commands, duincludes various flags or options to gather just the information you’re looking for.

Flag: |
Description: |
-h | Human-friendly format, such as G or M (rather than bytes) |
-s | Total sum for the specified location without per file/directory size |
-c | Total sum for the specified location and per file/directory size |
-a | Display all files and directories |
-t | Display the time of the last modification |
Of these, I suggest you pay the most attention to the -h option. This flag displays the consumed space in human-readable increments, such as megabytes or gigabytes.

![](https://cdn.thenewstack.io/media/2024/06/00b79038-du-withwithout-h.png)
Type this command to see how much space log files consume on your system:

1 |
$ du -hc /var/log |
![](https://cdn.thenewstack.io/media/2024/06/5d2a1fc8-du-c-total.png)
### Use the df Command
The [df](https://linux.die.net/man/1/df) command displays available storage space, which is the opposite information from
du (consumed space). It’s common to use the two tools together. For example, you might need to know how much storage capacity remains on a specific disk partition. The
df command and its related options show you this information.

Flag: |
Description: |
-h | Human-friendly format, such as G or M (rather than bytes) |
–total | Display a total for specified files |
-l | Limit to local file systems rather than remote |
Like
du ,
df also benefits from the
-h option to make the results more human-friendly and readable. The example below assumes your home directory.

1 |
$ df -h |
![](https://cdn.thenewstack.io/media/2024/06/6952afd3-df-h.png)
You’ll quickly discover that du and df are two essential commands for day-to-day Linux administration.

## Summarizing the Process
Rely on tools like du, df, and lsblkto investigate storage space utilization. Use the -h option to show the size in a human-friendly format. Don’t forget that adding the -l or -s flags to the lscommand will also provide file size information.

I’ll summarize the process of adding and managing storage space to a Linux system.

- Physically install the storage media (solid-state drive or hard disk drive).
- Identify it using commands like lsblk and cat /proc/partitions.
- Partition it using parted or fdisk. Parted is quite a bit more robust.
- Add a filesystem using the mkfs command.
- Create a directory to act as a mount point using the mkdir command.
- Mount the storage space to the directory using the mount command.
- Check the storage space using the dfand ducommands.
- Set standard Linux permissions (or access control lists) to control access to the storage space.
## Wrap Up
Storage capacity is not unlimited, and Linux users must be able to manage disk space on workstations and servers. This management begins with identifying newly installed storage drives, then creating partitions and adding filesystems to organize data. Administrators also mount the storage capacity to a directory to make it available to end-users. Standard Linux permissions control access to this storage space.

In addition to configuration, Linux users must analyze how storage space is used. The duand dfcommands are essential for this task. Both commands rely on powerful flags to show exactly the information you need to manage your systems.

Remember to be very careful when working with any partitions that contain data. It’s very easy to make a mistake with tools like fdisk and parted that cause you to lose data. It’s a best practice to begin the process with a backup.

Start today by using cat /proc/partitions, lsblk, du, and dfto examine your current storage use. Then use the other tools and commands to configure additional storage disks on your system if necessary.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)