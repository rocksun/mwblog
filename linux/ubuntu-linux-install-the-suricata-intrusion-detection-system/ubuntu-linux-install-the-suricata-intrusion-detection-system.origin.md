# Ubuntu Linux: Install the Suricata Intrusion Detection System
![Featued image for: Ubuntu Linux: Install the Suricata Intrusion Detection System](https://cdn.thenewstack.io/media/2024/09/ffe09c33-suricata-1024x746.jpg)
An Intrusion Detection System (IDS) is essential for monitoring network traffic and checking for malicious activity. If your servers are of the [Linux type](https://thenewstack.io/linux-choose-an-installation-platform/), you have plenty of options, one of which is Suricata.

Suricata is a high-performance, open source network analysis and threat detection software that is used by numerous private and public organizations and includes features like alerts, automated protocol detention, Lua scripting, and industry-standard outputs. It offers six modes of operation:

- Intrusion Detection System (the default)
- Intrusion Prevention System
- Network Security Monitoring System
- Full Packet Capture
- Condition PCAP capture
- Firewall
Most users will go with the default mode, which is a combination of IDS and network security monitoring, which ensures alerts include information about protocol, flow, file transaction/extraction, anomaly, and flow logs. You can read more about Suricata from the [official site](https://suricata.io).

Suricata is free to install and use.

What I want to do is walk you through the process of installing this IDS on [Ubuntu Server 22.04](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/).

## What You’ll Need
To get Suricata up and running, you’ll need a running instance of Ubuntu Server 22.04 and a user with[ sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). That’s it… let’s get to work.

## Install the Necessary Requirements
The first thing to be done is the installation of the necessary requirements. Log into your Ubuntu server and install those packages with the command:

1 |
sudo apt install autoconf automake build-essential cargo cbindgen libjansson-dev libpcap-dev libcap-ng-dev libmagic-dev liblz4-dev libpcre2-dev libtool libyaml-dev make pkg-config rustc zlib1g-dev -y |
When the above command completes, you’re ready to move on.
## Download and Unpack the Source
Next, we can download the Suricata source and unpack it. Download the compressed archive file with the command:

1 |
wget https://www.openinfosecfoundation.org/download/suricata-7.0.6.tar.gz |
You might want to visit the [Suricata download page](https://www.openinfosecfoundation.org/download/) to ensure you’re grabbing the most current version.
Unpack the file with the command:

1 |
tar xvzf suricata-7.0.6.tar.gz |
The above command will create a new folder, called suricata-7.0.6.
## Build and Install the Package
We can now build the package. Change into the newly-created directory with:

1 |
cd suricata-7.0.6 |
In that directory, run the configure script with:
1 |
./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var |
The above command will take a minute or so to complete.
Finally, install the package with the command:

1 |
sudo make && sudo make install-full |
The installation will take between 5-10 minutes, depending on the speed of your hardware.
Another method of installing Surcicata is via a PPA repository. Add the repository with the command:

1 |
sudo add-apt-repository ppa:oisf/suricata-stable |
Update apt with:
1 |
sudo apt-get update |
Install Suricata with:
1 |
sudo apt-get install suricata -y |
Do note: I prefer installing with the PPA method because it adds a [systemd startup](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/) file for easy service control.
## Start the Service
With the installation complete, it’s time to start the service with the command:

1 |
sudo systemctl enable --now suricata |
## Configure Suricata
It’s time to configure Suricata. Open the configuration file with:

1 |
sudo nano /etc/suricata/suricata.yaml |
I’m going to assume you’ll be using Suricata on a LAN. For that, look for the line that starts with HOME_NET. In that line, you’ll need to configure your subnet (such as 192.168.1.0/16).
Next, look for the af-packet line. Below that you’ll see -interface: eth0. You need to change eth0 to the name of your networking interface (which can be found with the ip a command).

Once that’s taken care of, you’ll need to add the following to enable live rule reloading. The following can be added to the bottom of the configuration file:

*detect-engine:*
*– rule-reload: true*
Save and close the file.

## Update the Suricata Rules
With the configuration taken care of, you’ll then want to update the Suricata rule sets with the command:

1 |
sudo suricata-update |
## Running Suricata
It’s time to take Suricata for a test run. After the rules have updated, we’re going to test the rules with the following command:

1 |
sudo suricata -T -c /etc/suricata/suricata.yaml -v |
You shouldn’t receive any error message, and the test will end with the following:
*Notice: suricata: Configuration provided was successfully loaded. Exiting.*
Restart the service with:

1 |
sudo systemctl restart suricata |
## Test Suricata
Let’s run a quick test. Below is a command used to trigger a false alert. Do this:

Log into the server from a second terminal (or tab). From the first window, issue the command:

1 |
tail -f /var/log/suricata/fast.log |
From the second terminal, issue the command:
1 |
curl http://testmynids.org/uid/index.html |
In the first window, you should see output like this:
*09/04/2024-17:44:43.767928 [**] [1:2100498:7] GPL ATTACK_RESPONSE id check returned root [**] [Classification: Potentially Bad Traffic] [Priority: 2] {TCP} 2600:9000:24d7:6c00:0018:30b3:e400:93a1:80 -> 2600:1700:6d90:f6b0:0000:0000:0000:001c:35524*
Suricata caught the false alert.

Now that you have Suricata up and running (and successfully tested) check out the official documentation for Suricata rules that can help you get the most out of this free, open-source intrusion detection system. Suricata is a fairly complex system to use, so I would recommend you go through the official documentation to better understand how it works.

If you’d prefer to manage Suricata with a GUI, I’d recommend checking out [IDS Tower](https://idstower.com).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)