# What Are Linux Namespaces and How Are They Used?
![Featued image for: What Are Linux Namespaces and How Are They Used?](https://cdn.thenewstack.io/media/2025/02/3d7503c1-getty-images-bdopvgvwcc0-unsplash-1024x683.jpg)
Would a rose by any other namespace still smell as sweet?

Shakespeare is now pounding on his casket, begging that I remove that twisted quote, but to the Bard, I say, “nay, nay.”

Namespaces have been a [Linux kernel](https://thenewstack.io/linux-kernel-6-13-stands-ready-with-security-performance-driver-updates/) feature since 2002. Since then, they’ve evolved into a very important aspect of Linux security. But it wasn’t until the advent of [containers](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/) that the importance of namespaces became obvious.

Essentially, [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) restrict resources that a containerized process can see so that one process can’t see the resources being used by another. This feature is crucial to the likes of containers and orchestration tools such as Kubernetes because, otherwise, one deployed container would be able to access or view resources used by another.

That, my friends, is a security issue. If one container was capable of [interacting with another](https://thenewstack.io/runc-related-leaky-vessels-threaten-container-security/) at the resource level, a malicious bit of code could wreak havoc on your system, network, and data.

The isolation of namespaces happens at the kernel level to isolate processes from one another.

There are different types of Linux namespaces, which are:

- User namespaces – adds unique user IDs and group IDs to be assigned to processes, which means it’s possible for certain processes to have admin privileges while others don’t.
- Process ID namespace – this assigns a set of PIDs to processes in one namespace while being able to assign different PIDs to the same processes in a different namespace.
- Network namespace – this is an independent network stack (routing table, IP addresses, socket listing, connection tracking table, firewall, etc) that can be assigned to specific namespaces.
- Mount namespace – an independent list of mount points that are visible to processes within a namespace.
- Interprocess communication (IPC) namespace – can be assigned it’s own IPC resources.
- UNIX Time-Sharing namespace – makes it possible to assign different hostname and domain names to different processes.
## How To Create a Namespace on Linux
Let’s say you want to create two network namespaces and then allow them to connect to one another.

The first step is to create the namespaces. We’ll call these namespaces net1 and net2 and create them with the following commands:

12 |
sudo ip netns add net1sudo ip netns add net2 |
We next have to create a pipe (a virtual ethernet pair) for the two interfaces, which is done with the following command:
1 |
sudo ip link add veth0 type veth peer name veth1 |
We now have to associate our namespaces with the pipe like so:
12 |
sudo ip link set veth0 netns net1sudo ip link set veth1 netns net2 |
The next step is to provide an IP address for each virtual interface. Make sure you do not set an IP address that is already in use on your network; otherwise, you’ll wind up with conflicts. We’ll assign 192.168.1.100 to veth0 and 192.168.1.101 to veth1 with the commands:
12 |
sudo ip -n s1 addr add 192.168.1.100/24 dev veth0sudo ip -n s1 addr add 192.168.1.101/24 dev veth1 |
Outstanding.
You can now verify that the IP addresses have been assigned and view the arp table. To view the IP address of net1, the command would be:

1 |
sudo ip netns exec net1 ip addr |
The output should look something like this:
As you can see, the correct IP address has been assigned to net1. The same thing can be done for net2 with the command:

1 |
sudo ip netns exec net2 ip addr |
We can now bring up those interfaces with the commands:
12 |
sudo ip -n net1 link set veth0 upsudo ip -n net2 link set veth1 up |
Let’s now test to see if they can ping one another. We’ll ping net2 from net1 with the command:
1 |
sudo ip netns exec net1 ping 192.168.1.101 |
Ping net1 from net2 with:
1 |
sudo ip netns exec net2 ping 192.168.1.100 |
In both instances, you should see successful ping results.
Now, let’s attempt to ping the 192.168.1.100 IP address from the host machine. So long as there is no device on your network with that address, it should be unreachable:

1 |
ping 192.168.1.100 |
You shouldn’t be able to reach that address.
What you’ve essentially done is create two network namespaces that can access one another but cannot be accessed by any other resources. That is what namespaces are all about.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)