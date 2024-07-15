# Linux: How File Permissions Work
![Featued image for: Linux: How File Permissions Work](https://cdn.thenewstack.io/media/2024/07/0984e8d2-getty-images-2wamii-zo8o-unsplash-1024x682.jpg)
[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)article. In this series, we also covered
[how to pick a distribution](https://thenewstack.io/choosing-a-linux-distribution/), how the Linux kernel
[interacts with hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)and how
[Linux manages system services](https://thenewstack.io/linux-skills-manage-system-services/),
[storage](https://thenewstack.io/how-to-manage-linux-storage/)and
[user and group permissions](https://thenewstack.io/linux-user-and-group-management/).
Permissions control user access to files and directories. For example, permissions determine whether a user can read the file sales.txt . They also determine whether a user can edit or change the contents of that file. Permissions also specify whether users can run a program or script.

If you’re already familiar with Windows permissions, you’ll find that [Linux](https://thenewstack.io/linux/) permissions are much simpler.

This article covers the identities and access levels available for standard Linux permissions, explains absolute versus symbolic modes and shows the syntax for the [chmod](https://linux.die.net/man/3/chmod) and [chown](https://linux.die.net/man/3/chown) commands.

I’ll begin with a quick command reference section demonstrating how to create a few users, groups, files and directories you can work with when setting permissions.

Review my previous post, “[Understand the Linux Command Line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/),” to work with these commands better.

## Set Up Users and Resources
Create a few user accounts so you can set different permissions for different people using the following example:

1 |
$ sudo useradd fsmith |
![](https://cdn.thenewstack.io/media/2024/03/632e2155-useradd-fsmith.png)
Use the same approach to create slee and mgarcia.

Note: It is a poor [security practice](https://thenewstack.io/lynis-run-a-security-audit-on-linux-for-free/) to log on to a Linux system as the root (administrator) user. Most systems force you to log on as a regular user and then use the [sudo](https://linux.die.net/man/8/sudo) (super user do) command to elevate your privileges. You may be prompted for your password when using
sudo.

Review the user management commands:

Command |
Description |
useradd username | Create a new user. |
usermod username | Modify an existing user. |
userdel username | Delete an existing user. |
Create a few groups, too. Here’s an example:

1 |
$ sudo groupadd IT |
Create
HR and
PR groups using the same syntax.
Review the group management commands:

Command |
Description |
groupadd groupname | Create a new group. |
groupmod groupname | Modify an existing group. |
groupdel groupname | Delete an existing group. |
You can find more details in my recent [Linux users and groups article](https://thenewstack.io/linux-user-and-group-management/).

Now that you have some users and groups, create some resources so you can control their access with permissions.

Change to the /home/fsmith home directory. Use the mkdir command to create the following directories:

- departments
- departments/it_dept
- departments/hr_dept
- departments/pr_dept
![](https://cdn.thenewstack.io/media/2024/03/c100e35a-ls-depts-dirs.png)
These represent three departments in a mock company for which you manage a Linux server.

Use the touch command to create these files in the specified directories:

- In the it_dept directory, create password-reset.txt
- In the hr_dept directory, create policies.txt
- In the pr_dept directory, create press-releases.txt
Find additional information on [managing Linux files and directories here](https://thenewstack.io/primer-get-to-know-linux-files-and-directories/).

Users, files, and permissions are all part of a single larger topic: [access control](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/). User accounts are an identity, and files are a resource. Permissions control access to resources based on identity. For example, permissions control whether
fsmith can read
fileA.txt and
slee can change the contents of
fileB.txt.

You might consider the content of the user and group management, file management, and file permissions tutorials to be one collection of related topics—controlling access to files.

## Understand Permissions and Identities
Setting permissions requires you to understand the available access levels and manage who those access levels apply to. This section covers the permissions and identities necessary to administer Linux permissions.

### Understand Access Levels
Linux permissions offer three levels of access: read, write and execute. They behave somewhat differently depending on whether they are applied to a file or directory.

The following table explains the read, write, and execute permissions as they apply to files.

Permission |
Character |
Description |
Read | r | View file contents |
Write | w | Modify file contents |
Execute | x | Run the file if it is a program or script |
This table shows how read, write and execute permissions apply to directories.

Permission |
Character |
Description |
Read | r | List and copy directory contents |
Write | w | Add or remove files in the directory (needs x, too) |
Execute | x | Change into the directory using cd |
One important distinction is that the execute permission is required on a directory for you to use the cd command to change into it. The execute permission is required on a file to run it as a program or script.

### Understand Identities
Linux recognizes three identities for access control:

- One user that owns the file or directory.
- One group that is associated with the file or directory.
- All others who aren’t that user or group member.
Identity |
Character |
Description |
User (owner) | u | The creator or identity associated with the file or directory. |
Group | g | The one group associated with the file or directory. |
Others | o | All other accounts that are not the User or Group. |
Three levels of access ( rwx) can be applied to three identities ( ugo).

## Display and Interpret Permissions
The command to display directory contents is ls (short for “list”). Add the -l option to display file and directory permissions. Use ls -l throughout these examples to display changes to permissions.

![](https://cdn.thenewstack.io/media/2024/03/c631867a-ls-l-depts.png)
![](https://cdn.thenewstack.io/media/2024/03/284ea07f-ls-l-depts-explain.png)
The above diagram is color-coded to explain which permissions apply to which identities. The permissions in the yellow box ( rwx) apply to the user, fsmith. The green box displays permissions for the IT group ( rw-). The others identity has only read ( r--), as shown in the red box. Dashes indicate a permission has not been granted.

## Understand Permissions Modes
Linux administrators have two different methods of setting permissions: Absolute mode and symbolic mode. Your system recognizes both, so use the one that is simplest for you. You’ll probably find yourself using both at various points.

### Understand Absolute Mode
Absolute mode uses numeric octal values to represent permissions levels.

Permission |
Octal value |
r (read) | 4 |
w (write) | 2 |
x (execute) | 1 |
Absolute mode adds the numeric permissions values to represent an overall level of access. The sum of the values goes in a specific order: user, then group, then others.

**Example 1**: Read, write, and execute access = r (4) + w (2) + x (1) = 7
- The absolute mode value for all access levels is 7 (4+2+1)
**Example 2**: Read and write (but not execute) = r (4) + w (2) = 6
- The absolute mode value for read and write but not execute access to a file is 6.
**Example 3**: Read only (no write and no execute) = r (4)
- The absolute mode value for read-only access is 4.
Absolute mode also uses the three identities in a specific order, which is always user, group, others ( ugo).

**Example 1**: The user has rwx, the group has r-x, and others has no access = 750
- The user has 7 (the value of read+write+execute), the group has 5 (read+execute), and others has 0 (no values).
**Example 2**: The user has rw-, the group has r–, and others has r– = 644
- The user has 6 (r+w), the group and others have 4 (read).
Absolute mode sounds very complex, but once you get used to the values, it is simpler and quicker than symbolic mode. I almost always use absolute when working with Linux.

### Understand Symbolic Mode
Symbolic mode combines the identity letters ( ugo), the permissions letters ( rwx), and math operators ( + , - , =) to configure permissions.

Here are a few examples:

- Granting a user the read permission to a file looks like this: u+r (add the read permission for the user).
- Giving the group read and write is g+rw (add the read and write permission for the group).
- Removing read and write from others is o-rw (subtract the read and write permission for others).
The advantage of symbolic mode is the ability to logic out what you want rather than simply applying a math result. You might say to yourself, “I want to add the read and write permission to the user and group.” That looks pretty logical: ug+rw.

## Use the `chmod`
Command
Now that you can interpret standard Linux permissions, it’s time to set permissions using the chmod (“change mode”) command. This is where you will use either absolute or symbolic mode.

Regardless of which mode you prefer, the chmod syntax looks like this:

$ chmod PERMISSION filename

The filename value is the command’s argument (what it acts on). In the following examples, I’ll apply various permissions to fileA.txt.

Absolute mode examples:

**Example 1**: Set the user permissions at u = rwx, group = r-x, and others = —.
$ chmod 760 fileA.txt

![](https://cdn.thenewstack.io/media/2024/03/29b81dcf-chmod760-filea.png)
**Example 2**: Set the user = rw-, group = r–, others = r–
$ chmod 644 fileA.txt

This method requires you to declare the actual permission levels you want using the sum for each of the three identities.

Note: There is a practice exercise for these concepts at the end of this tutorial.

### Symbolic Mode Examples
Symbolic mode differs because it adds or subtracts the desired permissions from the existing values. If a user already has read access to a file but you want to grant write access, too, then you are just adding write to the existing value:

1 |
$ chmod u+w fileA.txt |
![](https://cdn.thenewstack.io/media/2024/03/49be134a-chmoduplusw-filea.png)
This example leaves the existing read permission for the user and does not modify the group or others permissions at all.

Giving the group read and write looks like this:

1 |
$ chmod g+rw fileA.txt |
Again, this leaves existing user and others permissions alone.
There is a practice exercise for these concepts at the end of this tutorial.

Syntax review:

- Absolute mode uses a sum of values representing the rwx permissions. The values are listed in an order representing the user, group and others.
- Symbolic mode combines the initials for the three identities ( ugo) with the initials for the three access levels ( rwx) with + and - to add or remove permissions.
### Which Mode Should You Use?
So, which mode should you use in your day-to-day Linux tasks? You should know and recognize both for the following reasons:

- Certification exams will test you on both approaches.
- Documentation may be written using either method, so you must be able to understand each.
However, feel free to use the mode that makes the most sense to you. I prefer absolute mode because it requires less typing and is more straightforward. Others are happy using symbolic mode. Just be sure you understand both approaches.

## Manage File and Directory Ownership
The chmod command allows you to set permissions, but the chown command alters who the permissions apply to. You can change the user (owner) and group association to reassign various directories and files to anyone on the system.

### Use the `chown`
Command
There are three ownership changes you may wish to make: Change the owner (user), change the associated group or change both simultaneously.

To change the owner of the file or directory, type:

1 |
$ chown user FILE |
To change the group assigned to the file or directory, type:
1 |
$ chown :group FILE |
To change both values simultaneously, type:
1 |
$ chown user:group FILE |
Consider the following example, where you need to set the
fsmith account as the owner of the
password-reset.txt text file you created at the start of this tutorial:
1 |
$ chown fsmith password-reset.txt |
Next, associate the
HR group with the
hr_dept directory.
1 |
$ chown :HR hr_dept |
Maybe you need to set
mgarcia as the owner and associate the
PR group with the
pr_dept directory simultaneously:
1 |
$ chown mgarcia:PR pr_dept |
Use the
-R option to change ownership on a directory and everything in it. The
-R option stands for “recursive.” To associate the
IT group with any directories and files in the
it_dept directory, type:
1 |
$ chown -R :IT it_dept |
## Hands-On Opportunity
I’ve written a few basic exercises to help you practice using chmod and chown.

If you didn’t create the users, groups, directories and files mentioned at the start of the article, go back and do so now. Feel free to modify user names, groups, directories and files as needed. Practice using the commands in this tutorial by matching the requirements below.

### Practice Setting Ownership
Set ownership and group associations for the department directories using the chown command:

- Set fsmith as the owner of the it_dept directory (make this recursive).
- Set mgarcia as the owner of the pr_dept directory (make this recursive).
- Set slee as the owner of the hr_dept directory (make this recursive).
- Recursively associate the IT, HR, and PR groups with the matching department directory.
![](https://cdn.thenewstack.io/media/2024/03/48a4e10b-set-owner-grp.png)
### Practice Directory Permissions
Use absolute mode to set the following access levels:

- Set recursive permissions for mgarcia at rwx, the PR group at rwx, and others at r-x to the pr_dept directory.
- Set recursive permissions for slee at rwx, the HR group at rwx, and others at r-x to the hr_dept directory.
- Set recursive permissions for fsmith at rwx, the IT group at rwx, and others at rwx to the it_dept directory.
![](https://cdn.thenewstack.io/media/2024/03/27fc32a4-perms-results-abs.png)
### Practice File Permissions
Use the chown command to set ownership and the chmod command with symbolic mode to add and subtract permissions until they meet the following requirements:

- Grant fsmith at rw-, the current group at rw-, and others at rw- to the password-reset.txt file.
- Grant mgarcia at rwx, the current group at r--, and others at no access to the press-releases.txt file.
- Grant slee at rw-, the current group at rw-, and others at r-- to the policies.txt file.
![](https://cdn.thenewstack.io/media/2024/03/b002a44b-perms-results-sym.png)
Feel free to create other users, groups, directories, and files to practice permissions.

## Wrap Up
Controlling access to resources is a critical skill for administrators. It begins with creating the correct user and group accounts to represent users. Next, create and organize files and directories with security in mind. Finally, set appropriate permissions for the owner (u), group (g), and all others (o). This combination of identities, resources, and permissions are the fundamental components of controlling access to data.

This tutorial addresses standard Linux permissions, but there are additional special permissions that modify how they work. Additional Linux access control lists provide an even more robust way of controlling file security.

It’s well worth your time to practice managing access to files and directories by creating some sample resources and users and then setting various permissions and ownership.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)