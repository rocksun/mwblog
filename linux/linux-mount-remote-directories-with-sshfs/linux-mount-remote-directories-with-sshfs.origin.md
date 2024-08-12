# Linux: Mount Remote Directories With SSHFS
![Featued image for: Linux: Mount Remote Directories With SSHFS](https://cdn.thenewstack.io/media/2024/07/62ac5402-island-2482200_1280-1024x718.jpg)
The Secure Shell ([SSH](https://thenewstack.io/linux-limit-concurrent-users-on-your-server-with-ssh/)) isn’t just about allowing you to remote into servers to tackle admin tasks. Thanks to this secure networking protocol, you can also mount remote directories with the help of the SSH File System (SSHF).

SSHFS uses SFTP (SSH File Transfer Protocol) to mount remote directories to a local machine using secure encryption, which means the connection is far more secure than your [standard FTP.](https://thenewstack.io/create-a-secure-ftp-server-with-linux-and-ssh/) As well, once a remote directory is mounted, it can be used as if it was on the local machine.

Consider SSHFS to be a more secure way of creating network shares, the only difference is you have to have SSHFS installed on any machine that needs to connect to the share (whereas with Samba, you only have to have it installed on the machine hosting the share).

Let’s walk through the process of getting SSHFS up and running, so you can securely mount remote directories to your local machine.

## What You’ll Need
To make this work, you’ll need at least two Linux machines. These machines can be [Ubuntu](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) or [Fedora-based](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/), because SSHFS is found in the standard repositories for most Linux distributions. You’ll also need a user with sudo privileges.

## Installing SSHFS
Since [SSHFS](https://man7.org/linux/man-pages/man1/sshfs.1.html) is found in the standard repositories, the installation is quite simple. Log into the server (which will house the directory to share) and install SSHFS with one of the following commands:

- Ubuntu-based distributions –
`sudo apt-get install sshfs -y`
- Fedora-based distributions –
`sudo dnf install fuse-sshfs -y`
- Arch-based distributions –
`sudo pacman -S sshfs`
- openSUSE-based distributions –
`sudo zypper -n in sshfs`
Next, log into your local machine and install the package as well.

Once installed, you’ll need to set** user_allow_other** in the SSHFS config file on the local machine. For that, open the file with:

1 |
sudo nano /etc/fuse.conf |
In that file, locate the line:
1 |
#user_allow_other |
Change that to:
1 |
user_allow_other |
Save and close the file.
## Creating a Directory for Mounting
Back on the server, we must create a directory that will be mounted on the client machines. We’ll place our new directory in /srv with the command:

1 |
sudo mkdir /srv/data |
With the new directory created, we need to give it ownership, such that either a user or group can access it. If you only have one user who needs to access it, you can change the ownership with the command:
1 |
sudo chown -R USERNAME:USERNAME /srv/data |
If you want to allow more than one user to access the directory, you’d need to first create a group with the command:
1 |
sudo groupadd GROUP |
Where** GROUP** is the name of the new group.
Next, add the necessary users to the group (one at a time) with the command:

1 |
sudo usermod -aG GROUP USERNAME |
Where GROUP is the name of the group and USERNAME is the name of the user to be added.
You would then need to change the ownership of the new directory to the new group with:

1 |
sudo chown -R USERNAME:GROUP /srv/data |
On the local machine, you’ll have to create a directory that will house the mounted remote directory. We’ll create this in a user’s home directory with:
1 |
mkdir ~/data_mount |
## Mount the Directory
It’s now time to mount our remote directory. Remember, we’re mounting the remote directory */srv/data* to the local directory *~/data_mount*. This is done with the command:

1 |
sshfs USER@SERVER:/srv/data ~/data_mount |
Where USER is the remote username and SERVER is the IP address of the remote server. You’ll be prompted for the remote user’s password. On successful authentication, the remote directory will be mounted to the local directory and you can access it as if it were native to the local machine. If you save or edit a file in *~/data_mount*, it will be reflected in */srv/data* on the remote machine.
This method of mounting is temporary. Let’s make it permanent.

## Permanently Mount the Remote Drive
To permanently mount the SSHFS drive, you have to jump through a few hoops before it’ll work. First, you must create an SSH key pair (on the local machine) with the command:

1 |
ssh-keygen -t rsa |
Make sure to give the key a strong/unique password.
Once the key is generated, copy it to the server with the command:

1 |
ssh-copy-id USER@SERVER |
Where USER is the remote user name and SERVER is the IP address of the remote server.
Let’s test the connection to ensure it’s working properly. From the local machine, SSH to the server with:

1 |
ssh USER@SERVER |
Where USER is the remote username and SERVER is the IP address of the remote server. You should be prompted for the SSH key password and not your user password. Once you’ve successfully authenticated, exit from the connection with the exit command.
To make this mount permanent, you need to modify the */etc/fstab* file on the local machine. Open that file for editing with:

1 |
sudo nano /etc/fstab |
At the bottom of the file, paste the following line:
1 |
USER1@SERVER:/srv/data /home/USER1/data_mount fuse.sshfs x-systemd.automount,_netdev,user,idmap=user,transform_symlinks,identityfile=/home/USER2/.ssh/id_rsa,allow_other,default_permissions,uid=USER_ID_N,gid=USER_GID_N 0 0 |
Where USER1 is the remote username, SERVER is the IP address of the server, USER2 is the username on the local machine, and USER_ID and GROUP_ID are unique to the local machine. You can locate the IDs with the command:
1 |
id |
You should see entries like this:
1 |
uid=1000(jack) gid=1000(jack) |
In the above example, the user ID is 1000 and the group ID is also 1000.
Save the file and test the mount with:

1 |
mount -a |
If you receive no errors, all is well.
There is one caveat to this. During the boot process, the mount will fail because it will be attempted before networking is brought up. Because of this, after a reboot on the local machine, you’ll have to open a terminal window and mount the SSHFS directory with the command:

1 |
mount -a |
Once you’ve done that, you’re ready to use the remote directory as if it were local.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)