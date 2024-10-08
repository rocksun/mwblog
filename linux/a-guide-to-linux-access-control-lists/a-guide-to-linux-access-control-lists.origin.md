# A Guide to Linux Access Control Lists
![Featued image for: A Guide to Linux Access Control Lists](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
Those of us who shift rapidly between [Linux](https://thenewstack.io/learning-linux-start-here/) and [Microsoft Windows](https://news.microsoft.com/?utm_content=inline+mention) recognize some fundamental differences. One of these is permissions. Standard Linux permissions are pretty simple: Designate one user, one group, and then anyone else (known as “others”), and grant read, write, and execute permissions as necessary. Windows permissions are far more complex, with nesting, more access levels, and the mixing in of Share permissions. However, in many ways, Windows permissions are also more flexible and practical at scale.

This article covers Linux access control lists (ACLs), which provide significantly more flexibility than standard Linux permissions. I’ll discuss viewing and configuring ACLs for multiple individual users and multiple groups. Chances are, your [Linux distribution of choice](https://thenewstack.io/choosing-a-linux-distribution/) already enables ACLs (ACLs are actually a function of the filesystem).

## A Brief Review of Standard Linux Permissions
You can configure standard [Linux permissions](https://thenewstack.io/linux-how-file-permissions-work/) using the [
chmod](https://linux.die.net/man/1/chmod) command. The command sets any combination of three access levels: read, write, and execute. You can assign these levels of access to three identities:

- User (owner): One user account that owns the file (by default, this is the file creator).
- Group: One group of users as displayed in the /etc/group file.
- Others: Anyone who is not the user or a member of the assigned group.
![](https://cdn.thenewstack.io/media/2024/09/304daf50-basic-ls-l.png)
This approach is sufficient on a standalone system with few users and fewer groups. However, this method becomes far more cumbersome on shared systems, those with file-sharing features enabled, or devices with lots of SSH remote access.

That’s where the filesystem ACL feature comes in handy. It lets you configure several users and/or groups with various access levels.

## How Do ACLs Help?
ACLs allow you to specify multiple user accounts and provide them with different levels of access. It also means you don’t have to give one of those users ownership of the file. It offers the same flexibility with groups.

ACLs still recognize the three standard access levels of read, write, and execute, so you don’t have to relearn everything you already know about Linux permissions. In fact, ACLs work in tandem with standard permissions, so you’ll still use the basic user (u), group (g), and others (o) identities. You’re supplementing regular permissions, not replacing them.

### Verify Your Distribution Supports ACLs
Today’s modern Linux distributions typically support ACLs out of the box. Remember that ACLs are a function of the [filesystem](https://thenewstack.io/how-to-manage-linux-storage/), so begin there. The standard filesystems are ext4, XFS, and Btrfs. Each of these supports ACLs.

You probably don’t need to check for ACL support on your Linux distribution, but you can use the following command if you want to confirm it:

tune2fs -l /dev/sda1 | grep -i "Default mount options"

Expect to see acl listed in the output.

![](https://cdn.thenewstack.io/media/2024/09/2a9fd946-defaultmountoptions.png)
Note that the ls -l output displays a + character if ACLs are configured on the resource. In the following example, an ACL is applied to file1.txt.

![](https://cdn.thenewstack.io/media/2024/09/3e07f113-ls-l-withacl.png)
## Use the setfacl Command
The ACL configuration command is [
setfacl](https://linux.die.net/man/1/setfacl). It relies on the standard Linux command syntax:

command -options argument

The argument will be the file or directory to which you apply access controls.

The setfaclcommand has many options. The following list contains some of the most common:

-m : Modify the specified ACL.

-x : Remove entries from the ACL.

-b : Remove all entries from the ACL.

-d : Configure a default ACL for the given directory.

-R : Apply the ACL recursively to all directory contents.

However, setfacl also relies on additional parameters to define whether the new access controls apply to users or groups.

u:<username>

g:<groupname>

Combined, these settings allow administrators to implement far more robust and practical permissions configurations.

The following command example is a quick look at using setfacl. More specific examples follow in the next sections.

To configure an ACL for user django granting read ( r) permission to the sample.txt resource, type:

setfacl -m u:django:r sample.txt

A similar example for group engineering looks like this:

setfacl -m g:engineering:r sample.txt

Once you configure the ACL settings, you’ll want to review them to ensure they are correct. That’s where the getfacl command comes into play.

## Use the getfacl Command
The other relevant command for managing ACLs is [
getfacl](https://linux.die.net/man/1/getfacl), which displays the current ACL settings.

The basic syntax is the getfacl and the file or directory name you want to view:

getfacl /dev-projects

However, like most Linux commands, getfacl supports many useful options to modify its output. These include:

-c : Displays only ACL entries and discards the extra header information.

-R : Displays directory contents recursively.

-t : Displays the output in the more readable tabular format.

Use getfacl to review ACL settings when auditing or configuring access controls.

![](https://cdn.thenewstack.io/media/2024/09/b9016a72-basic-getfacl.png)
## ACL Use Cases
Below you’ll find two uses cases for ACLs, including a scenario and the relevant commands. Consider how similar situations may occur in your environment.

### Scenario 1
I’ll begin with a simple example: A sales group needing rwx to the /sales directory and a marketing group that should only have r-x privileges. No others need access. (Remember, these groups need the execute permission to cd into the directory.)

Start by granting the standard rwxpermissions to the sales group:

chown -R :sales /sales

chmod -R 770 /sales

Next, set an ACL for the marketing group:

setfacl -m g:marketing:r-x /sales

Confirm your settings with getfacl /sales.

Remember, ACLs work in conjunction with standard permissions, so don’t forget to use the ls -l command to account for both systems. However, the getfacl command does display the standard permissions in addition to the ACL entries.

### Scenario 2
Imagine another case where you need to grant different levels of access to various users and groups. Suppose you have a /dev-projects directory with the following requirements:

- Owner: root with full access ( rwx).
- Group: developers with full access ( rwx).
- Additional user: alex (code reviewer) with read-only access ( r-x).
- Additional user: silas (project manager) with read-only access ( r-x).
- Additional group: contract-dev-team with read-only access ( r-x).
Standard permissions won’t accommodate this sort of requirement, but ACLs handle it easily.

Begin by setting the standard permissions:

chown -R root:developers /dev-projects

chmod -R 770 /dev-projects

Next, configure ACL entries for the additional users and group:

setfacl -R u:alex:r-x /dev-projects

setfacl -R u:silas:r-x /dev/projects

setfacl -R g:contract-dev-team:r-x /dev/projects

Check the results by using getfacl and ls -l to display the settings.

## Wrap Up
Access Control Lists (ACLs) extend the functionality of Linux permissions to allow various access levels to different users and groups. While this does make troubleshooting more complex, the additional flexibility is well worth it.

ACL capabilities are a function of the filesystem. Today’s modern filesystems support ACLs and probably have it enabled already. Be sure to create a directory infrastructure that makes effective use of ACLs by organizing resources based on access requirements. In general, everything for the Sales team should exist in one parent directory, while everything needed by the Marketing group exists in another.

ACLs become particularly critical on larger deployments, such as major file servers supporting many users and resources with different access requirements. Examine your larger deployments today to see whether ACLs can help control resource access more effectively. And don’t forget to consider ACLs when troubleshooting seemingly mysterious access issues.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)