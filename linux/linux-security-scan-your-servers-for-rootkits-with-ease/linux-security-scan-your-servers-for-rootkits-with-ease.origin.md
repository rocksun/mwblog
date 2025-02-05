# Linux Security: Scan Your Servers for Rootkits With Ease
![Featued image for: Linux Security: Scan Your Servers for Rootkits With Ease](https://cdn.thenewstack.io/media/2025/01/121fc7d0-getty-images-fayapriipvq-unsplash-1024x683.jpg)
Linux is one of the most secure operating systems on the planet. However, nothing is guaranteed, and if a server is connected to a network, it’s vulnerable… even if that server is powered by [Linux](https://thenewstack.io/learning-linux-start-here/). There’s always someone [lurking in the shadows](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/), hoping to gain access to those servers and exploit them as a means to a profitable end.

There’s malware, ransomware, and, perhaps worst of all, [rootkits](https://thenewstack.io/rootkits-come-to-containers-and-bring-trouble-with-them/), which are surreptitiously installed software that attackers can use to take over your computer. They all seem to always be ready to take your company down.

Fortunately, with Linux, there are tools you can use to scan those servers for rootkits.

## What Is a Rootkit?
For those who aren’t familiar, a rootkit is a category of malicious software that gains control over an operating system or device and manipulates its behavior, all the while concealing its existence.

The primary goal of a rootkit is to prevent detection by security software, antivirus programs, and other monitoring tools so that it can continue doing what it does (which is always malicious).

Rootkits often work at multiple levels:

**Low-level system manipulation**: Rootkits can alter the underlying system files, registry entries, or kernel modules to evade detection.**Kernel mode operations**: Some rootkits operate in what is called kernel mode to give them low-level access to system resources and make it harder for other software to detect their presence.**File and process hiding**: Rootkits almost always hide themselves by modifying file names, icons, processes, network connections, and other crucial services.
There are two different types of rootkits:

**Bootkit**: Bootkits infect the master boot record (MBR) on a hard drive at startup time to prevent system boots from legitimate operating systems.**Kernel-mode rootkit**: These rootkits run in kernel mode and can intercept system calls, manipulate memory, or create fake network traffic.
Rootkits typically include additional features such as network activity monitoring, process control, and data encryption.

Now that you have a basic understanding of what a rootkit is, let’s find out how you can scan for them on Linux.

## Chkrootkit
Chkrootkit is a simple rootkit detector that checks for various signs of infections on Unix-like filesystems. [Chkrootkit](https://www.chkrootkit.org/) can be installed on [Ubuntu-based systems](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) from the standard repositories with the command:

1 |
sudo apt-get install chkrootkit -y |
During the installation, you’ll be asked if you want to configure chkrootkit for email alerts. If you decide you want to do this, make sure you have the necessary information for an SMTP server to us. If not, select local only.
If you’re using a Fedora-based distribution, the command for installation is:

1 |
sudo dnf install chkrootkit -y |
Once the software is installed, you can run a scan with the command:
1 |
sudo chkrootkit |
The app will immediately launch and start checking for known rootkits. When it finishes, you’ll see a report for everything it’s found (or, hopefully, not found).
You can set up a cron job for chkrootkit to run nightly (at midnight) with a command. To do that, open the crontab editor with:

1 |
sudo crontab -e |
At the bottom of the file, add the following:
Where EMAIL is your email address.
Save and close the file. Your system will now be automatically scanned for rootkits at midnight, and the report will be sent to the email you configured.

## LMD
LMD stands for Linux Malware Detect and is a full-featured open-source malware scanner. LMD features a full reporting system, email alerts, and uses threat data from network intrusion detection systems to create signatures of malware that is in active use.

The best part about LMD is that it’s regularly updated to keep up with the constantly changing landscape of malware in the wild.

Here are the steps for installing LMD on Linux.

- Open a terminal window.
- Download the source with the command wget http://www.rfxn.com/downloads/maldetect-current.tar.gz
- Extract the archive with tar xvzf maldetect-current.tar.gz
- Change into the maldetect directory with cd maldetect
- Run the installation with the command sudo ./install.sh
The installation happens fairly quickly, so blink, and it’s all over.

Next, you need to configure LDM. Open the configuration file with:

1 |
sudo nano /usr/local/maldetect/conf.maldet |
Within this file, you’ll find plenty of customization options. For example, you’ll find the quarantine_clean option, which is used to tell LMD to automatically clean any detected malware. Set that option to 1 to enable it. Go through that entire file and configure everything you need for your situation. Save the file when finished.
With LMD configured and ready, you can launch a manual scan with the command:

1 |
sudo maldet -a / |
You can also specify specific directories to scan. If you do opt to scan everything under the root directory (/), know that it’s going to take some time to complete. For instance, on my Ubuntu Server 24.04 instance, there are over 62 thousand files to scan.
Another nice feature is the ability to monitor directory changes. For example, you could monitor the */etc* directory like this:

1 |
sudo maldet --monitor /etc |
One thing to keep in mind is that if you do go with the monitor option, you’ll need to alsy install inotify-tools with the command:
1 |
sudo apt-get install inotify-tools -y |
With the monitor option running, you’ll find the log at */usr/local/maldetect/logs/inotify_log*. Make sure to regularly read that file to see if anything in* /etc/* has changed. That log file is updated in real-time, so as soon as something changes, it’ll be written to the file.
You can also list quarantined files with the following:

1 |
sudo maldet -l |
To schedule a daily scan with LMD, you’ll use a cronjob. If you want that scan to run at midnight every day, you can add the necessary line to corn. Using [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/), open[ crontab](https://thenewstack.io/linux-how-to-use-cron-to-schedule-jobs/) for editing with:
1 |
sudo crontab -e |
At the bottom of that file, add the following:
And there you have it: your Linux servers are now being monitored for rootkits. Never assume, just because it’s Linux, that those servers are guaranteed to be hack-proof.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)