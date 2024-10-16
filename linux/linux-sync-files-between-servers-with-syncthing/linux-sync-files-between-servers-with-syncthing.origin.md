# Linux: Sync Files Between Servers With Syncthing
![Featued image for: Linux: Sync Files Between Servers With Syncthing](https://cdn.thenewstack.io/media/2024/09/61d124c1-syncthing-1024x683.png)
Have you ever wanted to keep files and or folders in sync between Linux machines? You could use [Samba](https://thenewstack.io/samba-network-shares-for-rhel-based-linux-distributions/) or [NFS](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/) for that, but those solutions aren’t exactly geared toward synchronization. With Syncthing, you can not only set an encrypted sync option but also sync between computers, mobile devices and servers. On top of that, Syncthing is easier to set up and use than the other two options. And when you need to keep data between machines in a constant state of sync, this is the way to go.

I’m going to walk you through the process of installing [Syncthing](https://syncthing.net/) on [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/) and [Ubuntu Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) so you can see how easy it is to sync files between the two.

## What You’ll Need
The only things you’ll need for this are running instances of both AlmaLinux and Ubuntu Linux and a user with [sudo privileges.](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) Of course, you could follow along with two instances of AlmaLinux, two instances of Ubuntu, or two completely different distributions.

With those things at the ready, let’s get Syncthing installed.

## Installing Syncthing
The installation of Syncthing on AlmaLinux requires downloading a file, extracting it and then moving a file in the newly created directory. Here are the actual steps:

- Log in to your AlmaLinux machine.
- Download the latest version of Syncthing with the command:
`curl -s https://api.github.com/repos/syncthing/syncthing/releases/latest | grep browser_download_url | grep linux-amd64 | cut -d '"' -f 4 | wget -qi -`
. - Unpack the file with
`tar xvzf syncthing*tar.gz`
. - Move the required file with the command
`sudo mv syncthing-linux*/syncthing /usr/bin`
. - Verify the installation with
`syncthing --version`
.
The Ubuntu installation is even easier. Just follow these steps:

- Open a terminal window.
- Issue the command
`sudo apt-get install syncthing -y`
. - Allow the installation to complete.
## Creating a Systemd File
To make Syncthing run as a service on a [systemd-enabled distribution](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/), you have to create a systemd file with the command:

1 |
sudo nano /etc/systemd/system/syncthing@.service |
Notice the @ symbol? That’s there so you can start the Syncthing as a user.
In that file, paste the following:

123456789101112131415161718192021 |
[Unit]Description=Syncthing - Open Source Continuous File Synchronization for %IDocumentation=man:syncthing(1)After=network.target[Service]User=%iExecStart=/usr/bin/syncthing -no-browser -gui-address=0.0.0.0:8384 -no-restart -logflags=0Restart=on-failureSuccessExitStatus=3 4RestartForceExitStatus=3 4# HardeningProtectSystem=fullPrivateTmp=trueSystemCallArchitectures=nativeMemoryDenyWriteExecute=trueNoNewPrivileges=true[Install]WantedBy=multi-user.target |
Save and close the file.
Reload the systemd daemon with:

1 |
sudo systemctl daemon-reload |
Let’s say you want to run Syncthing as user “jack”. The command to start and enable the service would be:
1 |
sudo systemctl enable --now syncthing@jack |
Do the same thing on both AlmaLinux and Ubuntu.
## Allow Syncthing Through the firewall
Since we’re using two different distributions, you’ll need to use two different firewall tools. On AlmaLinux, we’ll open the firewall ports with the following:

123 |
sudo firewall-cmd --zone=public --add-service=syncthing --permanentsudo firewall-cmd --zone=public --add-service=syncthing-gui --permanentsudo firewall-cmd --reload |
For Ubuntu, the firewall can be opened with the following commands:
12 |
sudo ufw allow syncthingsudo ufw allow syncthing-gui |
## Configure Syncthing
Open the Syncthing configuration file with the command:

1 |
sudo nano ~/.local/state/syncthing/config.xml |
In that file, look for the following section:
Change `tls="false"`
to `tls="true"`
and make sure the address section is configured for the IP address of the hosting machine. Once you’ve done that, save and close the file.

Restart the Syncthing service with:

1 |
sudo systemctl restart syncthing@jack |
## Accessing the Syncthing Web UI
Open a web browser and point it to http://SERVER:8384 (where SERVER is the IP address of the hosting machine. On the main page, you’ll be warned that you need to set a remote access password. Do that by clicking Settings (Figure 1). In the Settings pop-up, click the GUI tab and then set a username and password.

-
Figure 1: The Syncthing Settings button (bottom right).

Click Save when you’re finished. This will send you to the login page, where you’ll need to type the username and password you just set.

## Connecting the Machines
Now that you have Syncthing up and running on both machines, it’s time to connect them. On one machine, go to the Syncthing Dashboard, click Action, and then click Show ID. You’ll be presented with a QR code and a long random string. Copy the string and then move to the other machine. On the second machine, in the Remote Devices section, click Add Device. In the Device ID section, paste the ID from the first machine, give the device a name and click Save.

Go to the Sharing tab and, in the Unshared Folders section, check the option Default Folder, then check the option for Auto Accept (Figure 2).

-
Figure 2: Adding a second node to Syncthing.

Click Save, then refresh the dashboard. The connected machine should now be listed as “Up to Date.”

Make sure you go through this process for both machines.

The default folder for Syncthing is *~/Sync*. Any files or folders you add to that folder on one machine will automatically be synced with the other. You can test that by issuing the following command on one machine:

1 |
touch ~/Sync/testing |
If you check on the second machine, you’ll find the testing file is in sync.
And that’s all there is to syncing machines with the help of Syncthing.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)