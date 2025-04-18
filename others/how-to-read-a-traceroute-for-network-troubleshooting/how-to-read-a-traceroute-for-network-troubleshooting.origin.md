# How To Read a Traceroute for Network Troubleshooting
![Featued image for: How To Read a Traceroute for Network Troubleshooting](https://cdn.thenewstack.io/media/2025/04/861e0b4c-route-1024x552.png)
The traceroute tool is one of the most valuable yet straightforward diagnostic utilities available for [network](https://thenewstack.io/networking/) troubleshooting. Built into virtually every operating system, traceroute runs a connection test from one computer to another device, showing each “hop” the data takes between network devices.

This comprehensive guide will help you understand how traceroute works, interpret its results and recognize common network problems it can reveal.

**Traceroute: Understanding What It Does**
To see traceroute in action, we can begin with a simple example of running a traceroute from your computer to Catchpoint’s servers. The specific results will be different for each person. However, in most cases, the results will show you around four to 20 “hops” that packets take to get from your computer to Catchpoint’s servers and back. The first one would likely be your local router, and from there, the data will take multiple “hops” through your internal network and out through your internet service provider (ISP) and over the internet, before finally reaching Catchpoint’s servers.

Figure 1 shows an example of what you might see on the command prompt of a Windows computer.

![Figure 1: Image of a traceroute command and the results generated.](https://cdn.thenewstack.io/media/2025/04/e659ca9c-figure-1-1021x1024.png)
Figure 1: Image of a traceroute command and the results generated.

Understanding how to run this tool and what the different information displayed when you run a traceroute command means will help you [troubleshoot various types of problems](https://thenewstack.io/devops-as-a-graph-for-real-time-troubleshooting/).

**The Anatomy of Traceroute**
Traceroute is often associated with the closely related ping tool. As such, it is often thought that, like ping, it is standardized across all platforms. However, this is not the case.

**Windows traceroute**uses Internet Control Message Protocol (ICMP) exclusively (the same protocol as ping).**macOS and Linux**typically default to User Datagram Protocol (UDP) for traceroute, but can also be configured to use ICMP or Transmission Control Protocol (TCP).
Despite these differences, traceroute’s core function — showing you each hop between source and destination — remains the same.

**How To Run Traceroute and Interpret the Results**
Running a traceroute is straightforward. First, bring up a command prompt on your computer. For Windows 10, click on the Start button and type CMD to bring up the Command Prompt options, then click on the Command Prompt app to open it.

![Figure 2: Command Prompt options in Windows 10.](https://cdn.thenewstack.io/media/2025/04/45107265-image2.png)
Figure 2: Command Prompt options in Windows 10.

Once the Command Prompt has loaded, type the command `tracert`
followed by the destination you want to test. For example, to run a test on catchpoint.com, you would type `tracert catchpoint.com`
and hit Enter. (For [Linux ](https://www.linux.com/news/cli-magic-introduction-traceroute/)and [macOS](https://macreports.com/how-to-run-traceroute-on-macos/) devices, you would type `traceroute catchpoint.com`
instead.)

When you look at the traceroute results, you’ll see several key pieces of information organized in a table-like format:

Hop Number |
RTT Attempt 1 |
RTT Attempt 2 |
RTT Attempt 3 |
Hop Details |
1 | 2ms | 1ms | 1ms | 10.0.0.1 |
2 | 10ms | 10ms | 10ms | 96.120.40.245 |
3 | 10ms | 11ms | 12ms | 96.110.175.85 |
*Table 1: Representation of traceroute results.*
**Hop number:** Each device the data passes through is considered a hop. This could be a router, switch, server or computer.
**Round-trip time (RTT):** You’ll typically see three attempts (three RTT columns). Each entry shows how long it took for data to reach that hop and return to you. Significant discrepancies can indicate issues or intermittent latency.
**Hop details:** This is where you see either an IP address or, in some cases, a domain name. Some devices display extra info or may be configured to show nothing (indicated by an asterisk).
**Common Network Problems Discovered With Traceroute**
You can use this command to look for a variety of network issues to determine what types of problems may be present based on the results displayed.

**Asterisks (Timeouts) at Various Points**
The most common issue you will see with a traceroute is a timeout response, which is represented by an asterisk (*). These happen quite frequently and for a variety of different reasons. In the following example, you can see multiple hops have asterisks when attempting to run a traceroute to google.com.

![Figure 3: Example output of traceroute to Google.](https://cdn.thenewstack.io/media/2025/04/d1c21c02-figure-3-1024x678.png)
Figure 3: Example output of traceroute to Google.

When you see an asterisk, it will mean one of the following things:

**Single asterisk on a hop:**This means that the request timed out on just one of the three attempts. This can be a sign that there is an intermittent problem at that hop.**Three asterisks, then failure:**If you see that all three attempts at a hop have asterisks and then the traceroute errors out, it means that the hop is completely down.**Three asterisks, then success:**If you see three attempts at a hop failing, but then the rest of the traceroute continues without an issue, that is actually not a problem at all. This simply means that (as mentioned earlier) the device at that hop is configured not to respond to pings or traceroutes, so the attempt times out.
**Elevated Latency After One Hop**
If everything looks fine for several hops but then the response times jump up significantly at one point and each hop after that remains high, it likely means a problem either at that hop or on the connection between it and the previous one. Since the connection from you to each successive hop has to go through that one, they will all be affected by the latency it is causing.

If you can identify where that hop is located, you can work with the owner of that connection to troubleshoot the problem. The issue will most often be with their data circuit.

If you do not know the owner of that connection and this latency is causing significant problems, you may be able to work with your ISP to have your traffic routed around that point.

**One Hop of Elevated Latency**
If you see one hop that has an elevated response time, but then the rest of the hops return to normal, this is not anything to be concerned about. It simply means that the device at that hop is configured so that responding to traceroutes is a low priority, which causes this type of delay. While there may appear to be latency on the traceroute, that slowness will not affect normal internet traffic.

**Comparison of Traceroute on Windows, macOS and Linux**
All major [operating systems](https://thenewstack.io/choosing-an-operating-system-and-container-runtime-for-your-cloud-native-stack/) — Windows, macOS and Linux — have traceroute built in, but they differ in syntax, protocols and custom options.

The following table highlights some of the main differences between the implementation of traceroute on Windows, macOS and Linux operating systems:

Feature | Windows | macOS | Linux |
---|---|---|---|
Command Name | tracert | traceroute | traceroute |
Default Protocol | ICMP Echo Requests | UDP | UDP |
Change Protocol | Not applicable (ICMP only) | -I for ICMP, -T for TCP SYN | -I for ICMP, -T for TCP SYN |
Number of Probes per Hop | 3 (fixed) | 3 by default, can be changed with -q | 3 by default, can be changed with -q |
Default Number of Maximum Hops | 30 | 30 | 30 |
Options | Limited (-d, -h, -w) | Extensive (-m, -q, -p, etc.) | Extensive (-m, -q, -p, etc.) |
Continuous Tracing | No | No | No |
Output Format | Simplified, with basic information | Detailed with packet size, TTL, etc. | Detailed with packet size, TTL, etc. |
Installation | Built-in (Command Prompt/PowerShell) | Built-in (Terminal) | Typically built-in, installable if missing |
Customizable Timeout | Yes, with -w (in milliseconds) | Yes, with -W (in seconds) | Yes, with -w or -W (in seconds) |
Resolve Hostnames | By default | By default, can be disabled with -n | By default, can be disabled with -n |
IPv4/IPv6 Support | Supports both, uses -4 or -6 to force | Supports both, uses -4 or -6 to force | Supports both, uses -4 or -6 to force |
Packet Size | Fixed (cannot be changed) | Adjustable with -q | Adjustable with -q |
More information about traceroute in a macOS and Linux environment can be found at these links:

**Limitations of Traditional Traceroute Implementations**
There are many scenarios of network configurations and functionalities that can interfere with traditional traceroute implementations. For this reason, the results of a traceroute can be misleading.

**Firewalls and Security Appliances**
Modern firewalls often filter out or deprioritize ICMP and UDP probes, leading to incomplete paths and significant packet loss. This filtering misleads users into believing there is an issue with the network when, in reality, it might just be the security configurations causing the disruption.

**Load Balancing**
Load balancing is a network design technique that allows data to traverse a network over multiple paths, thus maximizing the use of the bandwidth of the available infrastructure. Load balancing can route packets along different paths, further distorting the results shown by traceroute.

**Network Address Translation (NAT)**
NAT modifies the IP address in the packet header as it passes through a router, making it difficult for traceroute to map the network path accurately. The change in IP addresses can result in misleading traceroute results, as the apparent source or destination IP address may not reflect the true network path.

**Additional Obstacles to Traceroute**
Although these are the most common network services and features that can interfere with traceroute, there are still others, including:

- Asymmetric routing, where packets take different paths to and from a destination.
- ICMP rate limiting or throttling can cause ICMP responses to be delayed or dropped, leading to false indications of high latency or packet loss.
- Quality of service (QoS) policies are used to prioritize or deprioritize certain types of traffic. The packets used by traceroute may be deprioritized in favor of other traffic types, leading to inaccurate measurements of latency and packet loss.
- In virtualized environments or cloud networks, the physical network path might not directly correspond to the virtualized network path that traceroute sees. Additionally, the internal routing within a cloud provider’s infrastructure might not be fully visible to the user, resulting in misrepresented traceroute results.
**Advanced Traceroute Solutions for Modern Networks**
Catchpoint offers traceroute tools with enhanced capabilities for diagnosing network paths and performance issues, including [Traceroute InSession](https://www.catchpoint.com/blog/traceroute-insession-a-traceroute-tool-for-modern-networks), which establishes a complete TCP session before tracerouting, helping it pass firewalls and security filters, and [Pietrasanta Traceroute](https://www.catchpoint.com/blog/install-pietrasanta-traceroute-on-windows-11), which supports multiple protocols (UDP, TCP, QUIC) and includes features like TCP InSession to simulate real application traffic.

Check out these resources to learn more about how these tools can help you diagnose network issues with precision and optimize performance.

- To try out the Pietrasanta Traceroute program, visit
[Catchpoint’s GitHub page.](https://github.com/catchpoint/Pietrasanta-traceroute) - To learn about Pietrasanta Traceroute from Catchpoint’s Luca Sani, staff engineer, watch his
[presentation at RIPE 87, Rome 2023](https://ripe87.ripe.net/archives/video/1171/). - To learn more about detecting Explicit Congestion Notification (ECN) bleaching with Pietrasanta Traceroute from Sani, watch his
[presentation at RIPE 88, Krakow 2024](https://ripe88.ripe.net/archives/video/1298/).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)