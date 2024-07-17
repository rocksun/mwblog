# How to Migrate CentOS 7 to AlmaLinux
![Featued image for: How to Migrate CentOS 7 to AlmaLinux](https://cdn.thenewstack.io/media/2024/07/31ad3212-alma-linux-1024x683.jpg)
The former [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) CentOS 7 Linux distribution [is dead](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/). It was a [fun ride](https://thenewstack.io/centos-9-stream-is-now-available-but-should-you-use-it/) but it’s over. You could upgrade CentOS 7 to [CentOS Stream](https://thenewstack.io/wherefore-art-thou-centos-rocky-linux-cloudlinux-and-centos-stream/) but most are leery of doing so (because of the rolling release nature of Stream). The other option would be to migrate to one of the alternative distributions, such as [AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/).

Sounds complicated, right? You could have to deploy a new server with the latest version of [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/), copy all of the data from one machine to the next, rebuild your apps/services so they run, and hope for the best.

Fortunately, thanks to the developers of [AlmaLinux](https://thenewstack.io/linux-and-cloud-native-security-almalinux/), there’s a much easier way to do this.

I’m going to walk you through this process.

## What You’ll Need
To make this work, you’ll need a running instance of CentOS 7, a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/), and an external drive (just in case).

## Back Up Critical Data
Before you do anything, make sure to back up any critical data from the CentOS 7 server to an external drive. I would suggest you back up the following information:

- Configuration files (such as those found in /etc).
- User data.
- App data.
- Any customized scripts.
- Cron jobs.
- Service configurations (such as SSH, Apache, Samba).
- SSH keys.
- Mission-critical logs.
- Virtual hosts.
- Containers.
- Email configurations.
Make sure get everything.

## Update CentOS 7
Before you make the migration, you’ll want to make sure to upgrade CentOS 7. The EOL for CentOS 7 has already passed (June 30 2024), so there may not be any updates available.

To update, issue the command:

1 |
sudo dnf update -y |
After the update completes, reboot the server with:
1 |
sudo reboot |
## Install the Necessary Packages
Next, we need to install the elevate-release package, which is used for the migration. To install this package, issue the command:

1 |
sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm |
The elevate-release package does include support for third-party repositories, such as EPEL, Imunify, KernelCare, MariaDB, nginx, and PostgreSQL.
Once that completes, install the* leapp-upgrade* and data package with:

1 |
sudo yum install -y leapp-upgrade leapp-data-almalinux |
## Run the Pre-Upgrade Check
To continue, you must run a pre-upgrade check, which will let you know if it’s possible to continue with the migration. You might find the report contains errors that must be overcome before the migration can be run.

The pre-upgrade command is:

1 |
sudo leapp preupgrade |
This will generate an answer file that includes possible issues. To view that file, issue the command:
1 |
sudo cat /var/log/leapp/answerfile |
You might find that some packages are no longer available and have been replaced by alternatives. For example, the pam_pkcs11_module has been replaced with SSSD, so you have to confirm the resolution of that issue, which would be done with the command:
1 |
sudo leapp answer –section remove_pam_pkcs11_module_check.confirm=True |
You could also edit the file manually, going through each issue and doing as instructed. For example, the manual verification for the above module would require you to change the following line:
1 |
# Confirm = |
to
1 |
Confirm = True |
AlmaLinux has compiled a [list of frequent ELevate issues](https://wiki.almalinux.org/elevate/ELevate-frequent-issues.html). If you see errors in your report, make sure to check the issues page to see if yours is included (along with the fix for the issue).
The following fixes should resolve the most widely reported issues when migrating from CentOS 7:

123 |
sudo rmmod pata_acpiecho PermitRootLogin yes | sudo tee -a /etc/ssh/sshd_configsudo leapp answer --section remove_pam_pkcs11_module_check.confirm=True |
## Start the Upgrade
Once you’ve resolved the issues found in the pre-upgrade check, it’s time to launch the migration with the command:

1 |
sudo leapp upgrade |
When the upgrade completes, you’ll then need to reboot the machine. You should now find the machine is running AlmaLinux 8. It’s time to upgrade to the latest version.
## Upgrading AlmaLinux
Now that you’ve migrated from CentOS 7 to AlmaLinux 8, it’s time to upgrade from AlmaLinux 8 to AlmaLinux 9. To do that, you must open the **yum.conf** file for editing with:

1 |
sudo nano /etc/yum.conf |
In that file, make sure to delete anything from the exclude= line that relates to either elevate or leapp (such as leapp-upgrade-el7toel8). Once you’ve done that, save and close the file.
Next, open the** dnf.conf** file with:

1 |
sudo nano /etc/dnf/dnf.conf |
Do the same thing in this file as you did in **yum.conf**.
Run a check to see if there are any remaining packages from CentOS 7 with the command:

1 |
rpm -qa | grep el7 |
If you see anything in the output, consider removing those packages. Do the same by checking for elevate or leapp packages with:
12 |
rpm -qa | grep elevaterpm -qa | grep leapp |
If necessary, remove any packages from the output of the above two commands.
Finally, clean everything up with the command:

1 |
sudo dnf clean all |
To migrate AlmaLinux 8 to 9, install the elevate-release package with:
1 |
sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm |
Run the installation with:
1 |
sudo yum install -y leapp-upgrade leapp-data-almalinux |
Finally, run the elevation with:
1 |
sudo leapp upgrade |
When that completes, you can reboot with:
1 |
sudo reboot |
At this point, your release should be AlmaLinux 9 (check with the command cat /etc/os-release). If everything is running smoothly, you’re done.
I would suggest running this process on a non-production machine first. You might also make a clone of the CentOS 7 drive before starting the process. That way, should anything catastrophic happen, you can copy the cloned image back to the server.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)