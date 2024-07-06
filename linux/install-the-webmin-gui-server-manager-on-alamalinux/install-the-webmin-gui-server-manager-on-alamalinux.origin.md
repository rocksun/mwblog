# Install the Webmin GUI Server Manager on AlamaLinux
![Featued image for: Install the Webmin GUI Server Manager on AlamaLinux](https://cdn.thenewstack.io/media/2024/07/d7904a3a-webadmin-dashboard-1024x566.png)
When you’re new to [Linux](https://www.thenewstack.io/Linux), you might not want to have to do everything from [the command line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).

Although the CLI offers incredible power and flexibility, it can be a bit overwhelming to those who’ve not managed a server from within a terminal window. This is especially true for those migrating from Windows Server to Linux.

Fortunately, there are plenty of tools available for this purpose. Out of the box, you can always enable the [Cockpit GUI](https://cockpit-project.org/) for [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/), but that interface is a bit limited in the third-party modules that can be added.

There’s also [Webmin](https://webmin.com/), which has been around for a very long time. I remember, back when I first started working with Linux as a server OS, Webmin quickly became my best friend. With this powerful GUI app, I no longer felt as if my brain was about to implode with the sheer task of learning so many commands.

Webmin gave me all the power I needed so I could get the job done, while I learned the ins and outs of the command line tools necessary to manage a server.

But even though the CLI is second nature to me now, there are times when I prefer a GUI for the task. For instance, if I have numerous servers to manage or if I simply need to get a complicated job done quickly.

Out of the box, Webmin includes modules to help you manage:

- Bacula backups
- Bootup and shutdown
- Password management
- Disk and network file systems
- Disk quotas
- File system backups
- Log file rotation
- MIME-type programs
- PAM authentication
- Running processes
- Scheduled commands
- Scheduled cron jobs
- Software package updates
- Software packages
- System documentation
- System logs
- Users and groups
- Servers (such as SSH)
- HTTP tunnels
- Perl Modules
- Protected web directories
- Firewall
- Kerberos5
- NIS client and server
- TCP wrappers
- Linux RAID
- Partitions on local disks
- Cluster
If that’s not enough, there’s a site to search for [third-party modules](https://www.webmin.com/cgi-bin/search_third.cgi?modules=1) that can greatly expand the Webmin feature set.

I want to walk you through the steps for installing Webmin on AlmaLinux.

## What You’ll Need
To install Webmin, you’ll need a running instance of AlmaLinux and a user with sudo privileges. You’ll also need access to the root user for the initial Webmin login. That’s it. Let’s make some GUI magic.

## Update AlmaLinux
Before you start the installation, it’s best to go ahead and upgrade AlmaLinux. One thing to keep in mind is that, if the kernel is upgraded in the process, you’ll need to reboot the machine for the changes to take effect.

To upgrade AlmaLinux, log in to your server, open a terminal window and issue the command:

1 |
sudo dnf update -y |
When the upgrade finishes, reboot if necessary.
## Add the necessary repository
Because Webmin is not found in the standard repositories, you must create a new entry for dnf. Create the file with the command:

1 |
sudo nano /etc/yum.repos.d/webmin.repo |
In that file, paste the following:
12345 |
[Webmin]name=Webminmirrorlist=https://download.webmin.com/download/yum/mirrorlistenabled=1gpgkey=http://www.webmin.com/jcameron-key.asc |
Save and close the file with the keyboard combination Ctrl+x. Run another update command so dnf is aware of the new repository (*sudo dnf update*).
## Install Webmin
The next step is to install the Webmin manager, which can be accomplished with the command:

1 |
sudo dnf install webmin -y |
When this completes, the Webmin service is running and ready to accept connections. However, you still have to open the firewall, otherwise you won’t be able to access the GUI from a browser. To permanently open the required port, issue the command:
1 |
sudo firewall-cmd --add-port=10000/tcp --permanent |
You then must reload the firewall with the command:
###### sudo firewall-cmd –reload
## Log In to Webmin
With Webmin up and running, open a web browser that’s on the same network as the hosting server and point it to *http://SERVER:10000* (where SERVER is the IP address of the hosting server).

You’ll be greeted by a login window (Figure 1).

-
Figure 1: The Webmin login window

For your first login, you must use the *root* account, because you have to add any users who’ll need to access the GUI from within Webmin. Type *root* as the user and then type the root user password.

Once you’ve logged in, the first thing you should do is add any users to Webmin so the root user no longer has to be used. To do that, expand the Webmin entry in the sidebar and click Webmin users.

You don’t actually create new users but, instead, you convert existing users to Webmin users. To do that, click Create a New Webmin Group (Figure 2).

-
Figure 2: The Webmin users page is where you can convert existing users.

Next, give the new group a name (such as admin) and click Create. Back at the Webmin Users page, click Convert Unix to Webmin Users. On the resulting page (Figure 3), you can either select all users or type a list of users you want to convert.

-
Figure 3: Converting Unix users to Webmin users

Make sure to select the newly added group from the Webmin Group drop-down menu on the left pane, and then click Convert Now. After converting the users, you’ll want to go back to the new group and select which Webmin modules it can access. To do that, click Available Webmin Modules, and then go through the full list (Figure 4), checking any/all modules to which that group should have access.

-
Figure 4: Adding modules to a new Webmin group

Once you’ve taken care of that, click Save and the assigned modules are now accessible to the users within that group.

You can now log out of Webmin and log back in as a standard user.

Congratulations! You now have the power of the Webmin GUI to help you manage and configure your AlmaLinux server.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)