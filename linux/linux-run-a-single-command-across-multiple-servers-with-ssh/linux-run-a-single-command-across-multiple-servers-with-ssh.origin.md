# Linux: Run a Single Command across Multiple Servers with SSH
![Featued image for: Linux: Run a Single Command across Multiple Servers with SSH](https://cdn.thenewstack.io/media/2024/03/46226c01-marathon-2366475_1280-1024x682.jpg)
With
[Linux](https://thenewstack.io/Linux/), there are always numerous routes to wind up at the same location. That’s actually part of the strength of this operating system: It’s up to you how to get from point A to point B. Think of it as the “Mad Libs” of operating systems.
Take, for instance, the ability to run commands on remote machines. There are plenty of options, such as
[Red Hat](https://www.openshift.com/try?utm_content=inline-mention) Ansible, Puppet and Chef, which are all amazing platforms but [may be a bit overkill for what you need](https://thenewstack.io/in-space-you-might-still-need-two-factor-authentication/).
Consider this: You have a workstation and 5 or 10 servers you need to manage. You can use that workstation and Secure Shell into each server, run the command necessary, exit from the server, and rinse, wash, and repeat until you’ve taken care of everything.
That’s time-consuming and can lead to problems. Imagine if you ran the wrong command on the wrong machine. You don’t want that.
You also want to simplify as much as possible, which is why this handy SSH tip can make your life a bit easier.
Let’s say you have a number of
[Ubuntu Servers and Rocky Linux](https://thenewstack.io/install-ansible-on-ubuntu-server-to-automate-linux-server-deployments/) servers, each of which you want to ensure are always up to date. As I mentioned earlier, you can log into each Ubuntu server and issue the command:
|
1
|
sudo apt-get update && sudo apt-get upgrade -y
Then, you can log into each Rocky
[Linux server and issue the command](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/):
|
1
|
sudo dnf update -y
That may take a bit more time than you probably have to spare. So, how do we make
[Secure Shell](https://thenewstack.io/ssh-made-easy-with-ssh-agent-and-ssh-config/) ( [SSH](https://thenewstack.io/dr-torq-go-remote-with-ssh/)) do the heavy lifting for us? Thanks to [SSH](https://thenewstack.io/create-a-local-git-repository-on-linux-with-the-help-of-ssh/) config files, it’s actually fairly easy.
Let me show you how.
## Creating Your SSH Config File
The first thing we’ll do is create an SSH config file. We’ll stick with our example of
[Ubuntu and Rocky Linux servers](https://thenewstack.io/ubuntu-server-struggles-with-post-docker-kubernetes-installs/). Create the config file with the command:
|
1
|
nano ~/.ssh/config
Remember, you’ll want to create the file as the user who will run the command. We’re going to create four entries in this file (you can create as many as needed) — two for Ubuntu Servers and two for Rocky Linux servers — with the following information:
- ubuntu-web at 192.168.1.100
- ubuntu-db at 192.168.1.101
- rocky-web at 192.168.1.102
- rocky-db at 192.168.1.103
Those can be named anything you like, but it’s important that the names start with either Ubuntu or Rocky. The config entries will look like this:
|
1
2
3
4
5
6
7
8
9
10
11
|
Host ubuntu-web
Hostname 192.168.1.100
Host ubuntu-db
Hostname 192.168.1.101
Host rocky-web
Hostname 192.168.1.102
Host rocky-db
Hostname 192.168.1.103
Save and close the file.
Next, we have to create two scripts that will accept user input for the command to be run, get the hosts from the config file, test to see if the command run requires sudo permission, and then loop over the hosts to execute the commands. Create the first script with the command:
|
1
|
nano ~/ubuntu-cmd
You can name that file anything you’d like. In the file, paste the following content:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
|
#!/bin/bash
# Get the user's input for the command
[[ -z ${@} ]] && exit || CMD_EXEC="${@}"
# Locate the hosts from ~/.ssh/config with Host entries that are prefixed by `ubuntu-`
HOSTS=$(grep -Po 'Host\s\Kubuntu-.*' "$HOME/.ssh/config")
# Test for a sudo requirement
if [[ $CMD_EXEC =~ ^sudo ]]
then
# Ask for the sudo password
read -sp '[sudo] password for remote_admin: ' password; echo
# Rewrite the command as needed
CMD_EXEC=$(sed "s/^sudo/echo '$password' | sudo -S/" <<< "$CMD_EXEC")
fi
# Iterate through the hosts and execute the SSH command, remove `-a` to override ">"
while IFS= read -r host
do
echo -e '\n\033[1;33m'"HOST: ${host}"'\033[0m'
ssh -n "$host" "$CMD_EXEC 2>&1" | tee -a "/tmp/$(basename "${0}").${host}."
done <<< "$HOSTS"
Save and close the file.
Next, create the script for the Rocky Linux hosts with the command:
|
1
|
nano ~/rocky-cmd
In that file, paste the following:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
|
#!/bin/bash
# Get the user's input for the command
[[ -z ${@} ]] && exit || CMD_EXEC="${@}"
# Get the hosts from ~/.ssh/config whose names are prefixed by `rocky-`
HOSTS=$(grep -Po 'Host\s\Krocky-.*' "$HOME/.ssh/config")
# Test for a sudo requirement
if [[ $CMD_EXEC =~ ^sudo ]]
then
# Ask for the sudo password
read -sp '[sudo] password for remote_admin: ' password; echo
# Rewrite the command as needed
CMD_EXEC=$(sed "s/^sudo/echo '$password' | sudo -S/" <<< "$CMD_EXEC")
fi
# iterate through the hosts and execute the SSH command, remove `-a` to override ">"
while IFS= read -r host
do
echo -e '\n\033[1;33m'"HOST: ${host}"'\033[0m'
ssh -n "$host" "$CMD_EXEC 2>&1" | tee -a "/tmp/$(basename "${0}").${host}."
done <<< "$HOSTS"
Save and close the file.
Next, we’re going to move the scripts to
*/usr/local/bin*:
|
1
2
3
|
sudo mv ubuntu-cmd /usr/local/bin
sudo mv rocky-cmd /usr/local/bin
Next, change the ownership of the scripts:
|
1
2
|
sudo chown $USER /usr/local/bin/ubuntu-cmd
sudo chown $USER /usr/local/bin/rocky-cmd
Finally, give the files executable permissions:
|
1
2
|
sudo chmod u+x /usr/local/bin/ubuntu-cmd
sudo chmod u+x /usr/local/bin/rocky-cmd
## How to Use the Scripts
Let’s say you want to send the
*sudo apt-get update && sudo apt-get upgrade -y* command to your Ubuntu servers. For that, you would issue the following command:
|
1
|
ubuntu-cmd sudo apt-get update && sudo apt-get upgrade -y
You would be prompted for your sudo password on the remote machine, and, once you’ve successfully authenticated, it would run the commands and then iterate to the next host.
You’d then do the same thing with the Rocky hosts, like so:
|
1
|
rocky-cmd sudo dnf update -y
Again, it would iterate through all of your configured hosts and run the command on each.
Congratulations! You’ve just made your Linux server management life a bit easier … without having to rely on more complicated, third-party platforms to do the heavy lifting.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)