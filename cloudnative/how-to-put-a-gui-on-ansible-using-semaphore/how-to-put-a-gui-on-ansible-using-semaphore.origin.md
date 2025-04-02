# How to Put a GUI on Ansible, Using Semaphore
![Featued image for: How to Put a GUI on Ansible, Using Semaphore](https://cdn.thenewstack.io/media/2023/04/f647832c-semaphore-1024x528.jpg)
Ansible can be great for automating routine IT tasks, but some may feel stymied by the command line. Here’s how to install the Semaphore graphical user interface.

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s open source Ansible is an open source IT automation platform, [written in Python](https://thenewstack.io/what-is-python/), that can configure systems, deploy software, and orchestrate advanced workflows. By default, Ansible is a command-line tool but isn’t terribly complicated to work with.
However, there are some who’d much prefer having a graphical user interface (GUI) to make the platform more efficient to use. Thankfully, there’s one particular GUI, called Semaphore, that can help make using Ansible easier for larger environments and organizations.

I want to walk you through the process of installing Semaphore. I’m going to demonstrate on Ubuntu Linux (version 22.04), so you’ll want to make sure to have Ansible installed and working. To do that, make sure to first follow [this tutorial](https://thenewstack.io/install-ansible-on-ubuntu-server-to-automate-linux-server-deployments/). Once you’ve taken care of that, you are ready to install Semaphore.

## What You’ll Need
Obviously, you’ll need Ansible up and running on Ubuntu. You’ll also need a user with `sudo`
privileges. That’s it. Let’s get to the installation.

## Installing Semaphore
Although you can easily install Semaphore with Snap, we’re going to go a different route, so we can ensure the platform is available from anywhere on your LAN.

The first thing to do is install a database server. We’re going to go with MariaDB. To install MariaDB on Ubuntu, you must add the repository with the command:

1 |
curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash -s — |
After that command finishes, install both the server and client with:
1 |
sudo apt install mariadb-server mariadb-client |
With MariaDB installed, secure it with the command:
1 |
sudo mariadb-secure-installation |
Answer n to the first question and y to the remaining. You’ll also be prompted to create and verify a root user password.
With the database installed, it’s time to add Semaphore. We’ll first set a variable for the version with the command:

1 |
VER=$(curl -s https://api.github.com/repos/ansible-semaphore/semaphore/releases/latest|grep tag_name | cut -d '"' -f 4|sed 's/v//g') |
We can now use that variable to download the correct version with the command:
1 |
wget https://github.com/ansible-semaphore/semaphore/releases/download/v${VER}/semaphore_${VER}_linux_amd64.deb |
Install Semaphore with:
1 |
sudo apt install ./semaphore_${VER}_linux_amd64.deb |
Boom! Semaphore is installed and ready to be configured.
## Configure Semaphore
You don’t just edit a configuration file because none exists yet. To generate the configure file, run semaphore such that it will prompt you to configure everything. The command for this is:

1 |
sudo semaphore setup |
The first section of the configuration looks like this:
12345678910111213 |
Hello! You will now be guided through a setup to:1. Set up configuration for a MySQL/MariaDB database2. Set up a path for your playbooks (auto-created)3. Run database Migrations4. Set up initial semaphore user & passwordWhat database to use:1 - MySQL2 - BoltDB3 - PostgreSQL(default 1): |
Make sure to select MySQL for your database and then configure it accordingly. You can accept the default for everything, but you will have to type the MariaDB root user password you created earlier.
When you get to the Hostname section (which looks like db Hostname (default 127.0.0.1:3306):), make sure to type it in the form:

1 |
http://SERVER:3000 |
Where SERVER is the IP address of your hosting server.
Near the end of the prompt, you’ll also be asked to create a new admin user for the web UI.

## Create a Systemd File
Next, we need to create a systemd file so the Semaphore service can be controlled. Create the file with the command:

1 |
sudo nano /etc/systemd/system/semaphore.service |
In that file, paste the following:
123456789101112131415 |
[Unit]Description=Semaphore Ansible UIDocumentation=https://github.com/ansible-semaphore/semaphoreWants=network-online.targetAfter=network-online.target[Service]Type=simpleExecReload=/bin/kill -HUP $MAINPIDExecStart=/usr/bin/semaphore server --config /etc/semaphore/config.jsonSyslogIdentifier=semaphoreRestart=always[Install]WantedBy=multi-user.target |
Save and close the file.
Reload the systemd daemon with:

1 |
sudo systemctl daemon-reload |
Start and enable the Semaphore service with:
1 |
sudo systemctl enable --now semaphore |
## Accessing the Semaphore Web UI
With the service running and accepting connections, open a web browser that’s on a machine connected to the same LAN and point it to http://SERVER:3000 (Where SERVER is the IP address of the hosting server). You will be greeted by the Semaphore login prompt (Figure 1).


-
Figure 1: The Semaphore login screen.

## Creation of projects
You will then be prompted to create your first project (Figure 2), so give it a name and configure the optional Telegram Chat ID and Max Number of Parallel Tasks. Once you’ve taken care of that, click CREATE.

-
Figure 2: Creating a new project in Semaphore.

From the project page (Figure 3), you can start by adding inventory (which are machines Ansible will manage), as well as environment variables, key stores, repositories, task templates, and team members. Make sure to create your first key store, inventory, and playbook repositories (you do still have to manually create playbooks at this point — a process that I describe in the article linked at the top of this article).

-
Figure 3: Your first Semaphore project is ready to go.

Congratulations, at this point, Ansible should be considerably easier to manage.

## Ansible Automation Platform FAQ

### Q: What is Ansible?
A: Ansible is an open-source IT automation platform that can configure systems, deploy software, and orchestrate advanced workflows.


### Q: How do I get started with Ansible?
A: To start using Ansible, you’ll need to install it on a server within your LAN. You can download the latest version from the official Ansible website or use a package manager like pip for Python.


### Q: What is an inventory file in Ansible?
A: An inventory file lists all the hosts that are managed by Ansible. It’s used to specify which machines should be included in a playbook or a collection of playbooks.


### Q: How do I create a new playbook in Ansible?
A: To create a new playbook, you’ll need to write a YAML file with the necessary configurations. The file will include tasks, hosts, and other settings that define the automation process.


### Q: What is the difference between run once and infinite repeat in an Ansible playbook?
A: In an Ansible playbook, “run once” means that the playbook will execute only once on each host, whereas “infinite repeat” allows you to set a task as repeating indefinitely until it fails or succeeds.


### Q: Can I use Ansible with multiple operating systems?
A: Yes! Ansible supports many different operating systems, including Linux, macOS, and Windows. You can also use Ansible on both local and remote hosts.


### Q: How do I manage user permissions in an Ansible environment?
A: In a secure Ansible environment, you should ensure that users have the minimum necessary permissions to run playbooks or access inventory files. This helps prevent unauthorized access to your infrastructure.


### Q: What is bolt in Ansible?
A: Bolt is the command-line interface for running plays without writing a playbook file. It allows you to execute specific tasks using a simple syntax, which makes it easy to automate repetitive tasks.


### Q: Can I integrate Ansible with other tools and services?
A: Yes! Ansible integrates well with many third-party tools and services, such as AWS EC2, Docker, Kubernetes, and Jenkins. You can also use custom plugins to extend its capabilities.


### Q: How do I troubleshoot issues in an Ansible playbook?
A: To troubleshoot issues with your Ansible playbook, you’ll want to check the logs (usually stored in a logs directory) for any error messages or warnings.


[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)