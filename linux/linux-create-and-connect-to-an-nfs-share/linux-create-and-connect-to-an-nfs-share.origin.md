# Linux: Create and Connect to an NFS Share
![Featued image for: Linux: Create and Connect to an NFS Share](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
NFS stands for [Network File System](https://www.techtarget.com/searchenterprisedesktop/definition/Network-File-System) and is yet another way to share directories over a network. NFS has been around since the mid-80s and although it’s not quite as [easy to use as Samba](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/), it’s still a valid protocol for sharing files and folders.

But why would you choose NFS instead of Samba? One of the biggest reasons is that NFS is considerably faster than Samba. This is especially true when sharing larger files. I’ve witnessed Samba shares drag to a painfully slow crawl for no apparent reason. With NFS, that’s far less likely to happen.

The two main downfalls of NFS is that it’s not quite as easy to use as Samba (which is why a lot of people opt to go the SMB route) and that it doesn’t include any means of access control. Because of that, only use NFS on machines and networks that you trust are secure. And if you need better performance for LAN-based sharing, NFS is a great option.

Let me show you how it’s done.

## What You’ll Need
For this demonstration, you’ll need two [Linux machines](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/) on the same LAN. It doesn’t matter what distribution you’re using (because the necessary NFS software is available from most standard repositories). You’ll also need a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). I’ll demonstrate this on [Pop!_OS ](https://pop.system76.com/)and [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/) server.

Time to dig in.

## Installing the Necessary Packages
The first thing we’ll do is log into the machine that will be our server and install the required software with the command:

1 |
sudo dnf install nfs-utils -y |
Next, head over to the client, and install the same package with:
1 |
sudo apt-get install nfs-common -y |
Notice the different names of packages from the server to the client. Make sure to install the right software on the right OS.
## Create an NFS Share
Next, we’re clear to create the NFS share. Back at the server, we’re going to create a directory in the root, called nfs-share with the command:

1 |
sudo mkdir nfs-share |
Change the permissions of the directory with:
1 |
sudo chmod -R 777 /nfs-share |
## Define the New Share
We now have to define the new share in the* /etc/*exports file. On the server, open that file for editing with the command:

1 |
sudo nano /etc/exports |
The format of each entry is:
*directory client_IP (permissions)*
Let’s say you have the following details:

- directory – /nfs-share
- client_IP – 192.168.1.79
- permissions – read/write
The entry for the above information would be:

*/nfs_share 192.168.1.79(rw)*
Save and close the file.

## Start the NFS Server and Open the Firewall
On the server, let’s open the firewall so our clients have access to the share. This is accomplished with the following two commands:

1 |
sudo firewall-cmd --permanent --zone=public --add-service=nfs |
1 |
sudo firewall-cmd --reload |
It’s now time to start and enable the NFS service, which can be done with a single command:
1 |
sudo systemctl enable --now nfs-server |
You can verify the server is running with:
1 |
systemctl status nfs-server |
## Add Some Test Files and Create a Client Directory
Back on the server, let’s add some test files with the command:

1 |
touch /nfs-share/{test1,test2,test3} |
On the client machine, create a directory that will serve as the mount point for the share with the command:
1 |
mkdir ~/nfs_mount |
You can place that directory anywhere you like (so long as your user has permission to access it).
## Mount the Share
Let’s say our NFS server is at IP address 192.168.1.210. On the client machine, the share is mounted with the command:

1 |
sudo mount 192.168.1.210:/nfs-share ~/nfs_mount |
The NFS share directory on the server should now be mounted to the NFS mount directory on the client. If you view the contents of the *nfs_mount* folder on your client, you should see that it contains the files test1, test2, and test3 (which you created on the server).
If you want to make the mounting of the NFS share easier, we can add an entry to [fstab](https://wiki.archlinux.org/title/Fstab). Open the file on the client machine for editing with the command:

sudo nano /etc/fstab

At the bottom of the file, add the following (modifying it to match your configurations):

*192.168.1.210:/nfs-share /home/USER/nfs-mount nfs rw 0 0*
Notice that you cannot use ~/ to indicate your home directory in fstab. Instead, use the full path to the mount directory.

Test the configuration with:

1 |
mount -a |
If you receive no errors, you’re good to go. You can verify it works by restarting your client machine. The NFS share should automatically mount.
And that’s all there is to setting up a basic NFS share on Linux. If you need faster copy and write speeds than you’re finding with Samba, NFS is a great option. Just remember that NFS isn’t quite as flexible as Samba, so you won’t be integrating with Active Directory or sharing printers. As well, there are no file manager integrations for NFS, so any time you want to configure a new share or connect to an existing one, it’s all about the command line.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)