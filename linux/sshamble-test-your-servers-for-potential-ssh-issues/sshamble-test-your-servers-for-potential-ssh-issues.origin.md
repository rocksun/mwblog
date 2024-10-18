# SSHamble: Test Your Servers for Potential SSH Issues
![Featued image for: SSHamble: Test Your Servers for Potential SSH Issues](https://cdn.thenewstack.io/media/2024/08/26c52924-shamble-1024x683.png)
Using the [Secure Shell ](https://thenewstack.io/linux-ssh-and-key-based-authentication/)([SSH](https://thenewstack.io/dr-torq-go-remote-with-ssh/)) is a necessity for most [Linux admins](https://thenewstack.io/learning-linux-start-here/). This secure network protocol not only allows you to remote into the machines you need to administer but also copy files to and from your servers (with the [scp command](https://thenewstack.io/linux-lesson-copy-files-over-your-network-with-scp/)) and work with SSH key authentication (for even more security).

But just because SSH is far more secure than similar protocols doesn’t mean it’s not invulnerable. Over the years, several SSH flaws have been found (and patched), proving that nothing is 100% secure.

That’s why it’s crucial to keep SSH as secure as possible. This can be done by way of configuration files (such as */etc/ssh/sshd_config* and */etc/ssh/ssh_config*). But that’s not always enough because you may or may not know how vulnerable your SSH configuration is.

Fortunately, there are tools like [SSHamble](https://github.com/runZeroInc/sshamble) to help you out. An open source project managed by RunZero, SSHamble is defined as a research tool for SSH implementations. This tool checks for things like:

- Attacks against authentication
- Post-session authentication attacks
- Pre-authentication state transitions
- Authentication timing analysis
- Post-session enumeration
According to the [SSHamble](https://www.runzero.com/sshamble/) site, the app “simulates potential attack scenarios, including unauthorized remote access due to unexpected state transitions, remote command execution in post-session login implementations, and information leakage through unlimited high-speed authentication requests. The SSHamble interactive shell provides raw access to SSH requests in the post-session (but pre-execution) environment, allowing for simple testing of environment controls, signal processing, port forwarding, and more.”

Sounds important, yes?

Yes. Very much so.

But how do you use SSHamble?

Let me show you how.

## Installing SSHamble
The first thing you must do is install SSHamble. Because it’s not found in the standard repositories, you’ll need to go through a few steps to get it up and running. I’ll demonstrate two different methods of installation.

The first method requires the installation of Go. I’ll demonstrate this on an instance of Ubuntu Desktop 22.04. If you’re using a different Linux distribution, you’ll need to modify the Go installation steps. Unfortunately, SSHambe requires a minimum version of 1.23 for Go and the version installed from the standard repositories doesn’t meet that dependency. Instead, download the Go source with:

1 |
wget https://go.dev/dl/go1.23.0.linux-386.tar.gz |
Next, install Go with the command:
1 |
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.0.linux-386.tar.gz |
Add /usr/local/go/bin to your $PATH with:
1 |
export PATH=$PATH:/usr/local/go/bin |
You can also add the above line to the bottom of your ~/.bashrc file. Once you’ve done that, source the file with:
1 |
source ~/.bashrc |
Once Go is installed, clone the SSHamble Git repository with:
1 |
git clone https://github.com/runZeroInc/sshamble |
If the command complains that git isn’t installed,[ take care of that](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) with:
1 |
sudo apt-get install git -y |
Change into the newly created directory with:
1 |
cd sshamble |
Build SSHamble with the command:
1 |
go build -o sshamble |
If you receive an error mentioning “bits/libc-header-start.h: No such file or directory,” you can correct it by installing *gcc-multilib* with the command:
1 |
sudo apt-get install gcc-multilib -y |
When the installation completes, copy the SSHamble binary to */usr/local/bin* (so the command can be run from anywhere in the filesystem hierarchy) with the command:
1 |
sudo cp sshamble /usr/local/bin |
You can then verify the installation by issuing:
1 |
sshambe -h |
You should see the help file appear. If so, you’re good to go.
## Using SSHamble
First, issue the command:

1 |
sshamble scan -h |
This will list the full set of targets you can use for testing.
Let’s say you want to run a scan on every machine in your network. Let’s assume an IP address scheme of 192.168.1.0/24. To do that, issue the command:

1 |
sshamble scan -o results.json 192.168.1.0/24 |
Depending on how many machines you have on your network, the scan can take some time. When the scan completes, you’ll find the results.json file in the current working directory.
The next step is to analyze the results. You could go through the entire [JSON file](https://thenewstack.io/an-introduction-to-json/) to try and make sense, or you can use the analyze option like this:

1 |
sshamble analyze -o results-directory results.json |
The analysis takes considerably less time than the scan. If you then change into the results-directory folder, you’ll see several .csv files, such as *stats_auth_methods.csv*, *stats_hostkey_algos.csv*, *stats_kex_algos.csv*, and *stats_session_methods.csv* (in my results directory, there were 12 files after a full network scan).
For example, in the *stats_auth_methods.csv* file, I see the following results:

*publickey,6,192.168.1.11 192.168.1.142 192.168.1.166 192.168.1.176 192.168.1.253 192.168.1.30*
*password,6,192.168.1.11 192.168.1.142 192.168.1.166 192.168.1.176 192.168.1.253 192.168.1.30*
*keyboard-interactive,1,192.168.1.253*
The above indicates what machines include SSH key authentication, which use passwords, and which have keyboard-interactive (such as for 2FA).

Go through each one of those files to see what SSHamble has discovered. You might be surprised to find several issues you might need to shore up to keep SSH as secure as possible.

And that’s all there is to test your SSH implementations on your network with SSHamble. Although the documentation for SSHamble is a bit limited, the above commands should be enough to get you going with this handy tool.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)