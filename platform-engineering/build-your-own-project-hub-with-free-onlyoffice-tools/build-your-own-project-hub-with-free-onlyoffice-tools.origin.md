# Build Your Own Project Hub With Free ONLYOFFICE Tools
![Featued image for: Build Your Own Project Hub With Free ONLYOFFICE Tools](https://cdn.thenewstack.io/media/2025/06/6cef833a-philip-oroni-bjat6xdzgqi-unsplash-1024x683.jpg)
[Project management tools](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) are an absolute must when working with teams. Without a project management solution, those projects are going to be a massive challenge to manage.
Of course, you could opt to go with a third-party solution, but there are two reasons why you might not want to do that:

- Cost
- Privacy
If you’re a small business or even a solo developer, you might still want a project management solution that’s not only cost-effective but also doesn’t store your project files on a third-party server. Both of those reasons should have you considering a solution like the [ONLYOFFICE Workspace](https://thenewstack.io/the-best-office-suites-for-linux/) tool.

There are two editions of this app: Enterprise and Community. Obviously, if you’re a bigger company, you’ll want to go with the Enterprise edition. If, however, you’re a smaller business (or small team), you should consider the Community edition. Or, if you just want to kick the tires of this tool (to see if the Enterprise version might be a better option), you can install the Community edition, test it out, and then (if it suits you) migrate to the bigger option.

I want to show you how to deploy the ONLYOFFICE Workspace community project management software.

## What You’ll Need
I’m going to demonstrate this process on Ubuntu Server 24.04, but you can deploy the software on any machine that supports [Docker](https://thenewstack.io/containers-in-the-age-of-ai-a-chat-with-new-docker-president-mark-cavage/). The only alterations you’ll need to make in the steps are how you install Docker on your machine. To that end, you’ll need a running instance of an OS that supports Docker and a user with admin privileges (for Ubuntu, that’ll require sudo access).

As far as system requirements, you’ll need a minimum of:

- CPU: At least 4-core (6-core recommended)
- RAM: At least 8GB (12GB recommended)
- HDD: At least 40GB of free space
- Additional requirements: At least 6GB of swap
- OS: amd64 Linux distribution with kernel version 3.10 or later
Let’s make this happen.

## Installing Docker
Log in to your instance of Ubuntu Server and first update/upgrade the system with the command:

`sudo apt-get update && sudo apt-get upgrade -y`
If the kernel is upgraded in the process, you’ll need to restart the server for the changes to take effect, which can be done with the command:

After the server reboots, install the necessary Docker components with:
After the installation completes, you need to add your user to the Docker group with the command:

Log out and log back in for the changes to take effect.

## Installing ONLYOFFICE Workspace
It’s now time to install the ONLYOFFICE Workspace. To do that, first download the installer script with the command:

Give the script executable permissions with the command:

Run the command with:

During the installation, you’ll first be asked if you want to run the installation for Docker. Accept the installation by hitting Enter. Next, you’ll be asked if you want to install the ONLYOFFICE mail server. I skipped this section because I’m installing it on my home LAN. If you have a domain associated with your server (and you know you’ll need the mail component, which you probably will), go ahead and proceed with the mail server installation. You’ll be required to enter your FQDN for the installation to continue.

At this point, the installation will begin pulling down the necessary Docker containers, and should take roughly 5-10 minutes (depending on the speed of your machine and network connection).

When the installation is complete, you can verify it by issuing the command:

You should see several containers running, such as communityserver, onlyoffice-control-panel, onlyoffice-document-server, onlyoffice-elasticsearch and onlyoffice-mysql-server. Those would all be listed as Up.

## Accessing the Service
Open a web browser on a machine that is connected to the same network as the ONLYOFFICE server and point it to [http://SERVER](http://server) (where SERVER is the IP address or domain of the hosting server).

You’ll be presented with a page where you must type/verify a password for the user, add an email address for the registration and select a language and a time zone (Figure 1).

![](https://cdn.thenewstack.io/media/2025/06/7932e6c5-ooportal1.jpg)
Figure 1. The first page of the final installation.

Once you’ve done that, click the check box for the terms of service and click Continue. This will land you on the ONLYOFFICE Workspace main page (Figure 2), where you’ll see icons for Projects, CRM, Mail, People and Control Panel.

![](https://cdn.thenewstack.io/media/2025/06/ebbd34f9-ooportal2.jpg)
Figure 2. The ONLYOFFICE Workspace main page.

Click Control Panel, and you can then configure several options for the service (Figure 3), such as backups, storage, updates, full-text search, branding, multitenancy, private rooms, LDAP, SSO, login history, audit trail and data import.

![](https://cdn.thenewstack.io/media/2025/06/18bc0ceb-ooportal3.jpg)
Figure 3. The ONLYOFFICE Workspace Control Panel.

Go back to the portal and click Projects, where you’ll be prompted to create your first project (Figure 4).

![](https://cdn.thenewstack.io/media/2025/06/b638bf39-ooportal4.jpg)
Figure 4. Creating your first project with ONLYOFFICE Workspace.

At this point, it’s just a matter of setting up your project to meet your needs, and that is all very straightforward.

Congratulations, you now have a running project management tool for your small business or dev team. If you find ONLYOFFICE Workspace to be sufficient for your needs, you’re good to go. If you long for a few more features and scalability, consider the Enterprise edition. You can read about the features and costs of the different Enterprise additions on this [pricing matrix](https://www.onlyoffice.com/workspace-prices.aspx).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)