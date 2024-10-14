# Linux: Create System Backups With rsnapshot
![Featued image for: Linux: Create System Backups With rsnapshot](https://cdn.thenewstack.io/media/2024/10/6e91333c-getty-images-bhjklypz8fy-unsplash-1024x683.jpg)
One step to data reliability is backing up your data on a regular basis. You never know when something could go wrong with a server or desktop, leading to a loss of critical files or configurations. To avoid such a nightmare, you might want to consider using a tool that handles incremental backups of local and remote file systems.

One such tool is rsnapshot, which benefits from using hard links, so disk space is used only when necessary. Rsnapshot works as a wrapper for the widely used [rsync tool](https://thenewstack.io/linux-synchronize-local-and-remote-directories-with-rsync/) and is fairly easy to install and configure.

I’m going to walk you through the process of installing and configuring rsnapshot on [Ubuntu Server 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/), but you can make use of this application on most Debian-based distributions as well as those based on Fedora.

## What You’ll Need
The only things you’ll need are a running instance of Ubuntu Server and a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). Because rsnapshot can also back up to an external drive, you might also consider connecting such a drive for even better backup reliability. After all, should your OS go down and render the machine unbootable, if your backups are stored on the drive housing the OS, you could lose those backups as well.

For example, you might connect and external drive and mount it to a new directory named */backup*, which is what I will demonstrate here. To make that happen, you might also want to configure that drive to automount at boot, which would require a line similar to this in the */etc/fstab* file:

1 |
/dev/disk/by-uuid/13557fad-d203-4448-991b-c8011907dc1d /backup auto rw,nosuid,nodev,nofail,x-gvfs-show 0 0 |
Make sure you use your particular drive UUID and any options you prefer for the automounting of drives.
With that said, let’s get to the installation.

## Installing rsnapshot
The rsnapshot package can be installed from the standard repositories with the command:

1 |
sudo apt-get install rsnapshot -y |
If you’re using a Fedora-based distribution, the installation command is:
1 |
sudo dnf install rsnapshot -y |
If your distribution of choice is Arch Linux, the command is:
1 |
sudo pacman -S rsnapshot |
This should install all dependencies. If you find rsync doesn’t install, do so with:
- Ubuntu:
`sudo apt-get install rsync -y`
- Fedora:
`sudo dnf install rsync -y`
- Arch:
`sudo pacman -S rsync`
## Configuring rsnapshot
Now that rsnapshot is installed, it’s time to configure it. One thing to keep in mind (and this is very important) is that you can’t use spaces in the configuration file; if you do, it will result in syntax errors. Instead, if necessary, [use tabs](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/).

Open the configuration file with the command:

1 |
sudo nano /etc/rsnapshot.conf |
The first line you want to look for is this one:
1 |
snapshot_root /var/cache/rsnapshot/ |
On a Fedora-based distribution, that line might read:
1 |
snapshot_root /snapshots/ |
The above line configures the directory that will house the backups. For example, if you’re going with my suggestion of an external drive mounted to */backup*, the line would be:
1 |
snapshot_root /backup |
You will also want to disable the creation of the root directory; otherwise, you’ll wind up with a child directory with */backup*. To disable this feature, look for the following line:
1 |
#no_create_root 1 |
Uncomment the line by removing the # character so the result looks like this:
1 |
no_create_root 1 |
You’ll need to know the path to the rsync executable, which can be found with the command:
1 |
which rsync |
The results should be */usr/bin/rsync*. If it’s anything else, take note, because you have to configure that path in the following line:
1 |
cmd_rsync /usr/bin/rsync |
Next, we need to set a retention policy. This is handed in the BACKUP LEVELS / INTERVALS section of the configuration file, where you’ll see the following default options:
123 |
retain alpha 6retain beta 7retain gamma 4 |
The names above are arbitrary and the number is how many backups of that type will be retained. You can change the names if you’d like to, but remember that they should be in ascending order, and that the names you choose will be used to run the specific backups. You could change those names from alpha, beta and gamma to daily, weekly and monthly, which would make a lot more sense.
The next section to configure is what you want to back up. This section is listed under #LOCALHOST (near the bottom of the configuration file), where you’ll find the following:

123 |
backup /home/ localhost/backup /etc/ localhost/backup /usr/local/ localhost/ |
You can change the directories to be backed up to whatever you need, but leave *localhost/* as is; that instructs rsnapshot that we’re backing up to the local machine.
It’s also possible to exclude and include files from the backups. This is handled above the LOCALHOST section, where you’ll see the following:

1234 |
#include ???#include ???#exclude ???#exclude ??? |
For example, you might have specific files you don’t want to include in the backup. For that, make sure to create an exclude line with the direct path to the file in question.
Once you’ve taken care of the above, save and close the file with the Ctrl+X keyboard shortcut.

## Testing the Configuration
Before you launch the backup, you should test the syntax of your configuration file with the command:

1 |
sudo rsnapshot configtest |
If the command returns `Syntax OK`
, you’re good to go.
Let’s run a test on the daily backup (which I used in place of alpha in the config file). To run the test, issue the command:

1 |
sudo rsnapshot -t daily |
You’ll see output that looks something like this:
1234567891011 |
echo 28061 > /var/run/rsnapshot.pidmkdir -m 0755 -p /backup/daily.0//usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \ /home/ /backup/daily.0/localhost/mkdir -m 0755 -p /backup/daily.0//usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded /etc/ \ /backup/daily.0/localhost/mkdir -m 0755 -p /backup/daily.0//usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \ /usr/local/ /backup/daily.0/localhost/touch /backup/daily.0/ |
To run the first backup, issue the command:
1 |
sudo rsnapshot daily |
When the backup completes, you’ll find a subdirectory named `daily.0`
in */backup* that houses the snapshot.
## Scheduling Backups
[Rsnapshot](https://rsnapshot.org/) doesn’t include a built-in scheduler, so you’ll have to make use of cron. What we’ll do is create three entries — one each for daily, weekly and monthly. Issue the command:
1 |
sudo crontab -e |
At the bottom of the file, add the following lines:
123 |
0 1 * * * root /usr/bin/rsnapshot daily0 5 * * 6 root /usr/bin/rsnapshot weekly0 2 1 * * root /usr/bin/rsnapshot monthly |
The above lines do the following:
- Takes a daily snapshot at 1 a.m.
- Takes a weekly snapshot every Saturday.
- Takes a monthly snapshot on the first of each month at 2 a.m.
And that’s it. You now have a backup system that will automatically take snapshots of the configured directories and save them to your chosen destination.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)